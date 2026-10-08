# Implementation Recipes

Code level recipes for the stacks this agent meets most: plain HTML with GTM, Shopify (Customer events and webhooks), WooCommerce, Next.js and other SPAs, and a server-side event sender with hashing and deduplication. Every recipe is a starting point: adapt names, IDs and consent logic to the project, propose it as a diff, and test before release. Never commit secrets; read tokens from environment variables or a secret manager.

## Recipe 0: data layer contract

Agree this contract with developers before writing tags. One event per business action, pushed after the action succeeds.

| Event | When | Required keys |
|-------|------|---------------|
| page_view (SPA only, virtual) | Route change completed | page_location, page_title, page_type |
| view_item | Product page render | ecommerce.items[], ecommerce.value, ecommerce.currency |
| add_to_cart | Cart API returned success | ecommerce.items[], value, currency, event_id |
| begin_checkout | Checkout started | items[], value, currency, event_id |
| purchase | Order confirmed (once) | event_id, ecommerce.transaction_id, value, tax, shipping, currency, items[], user_data (hashed or raw for enhanced conversions, never in URLs), customer_type |
| generate_lead | Form accepted by server | event_id, lead_type, form_id, value, currency, user_data |
| sign_up | Account created | event_id, method |

Rules: `event_id` is generated once per action (order ID for purchases, UUID for others) and reused by every pixel and the server copy. Clear `ecommerce` before each ecommerce push. Values in currency units with decimals.

## Recipe 1: head order (consent, CMP, GTM)

```html
<head>
  <!-- 1. Consent defaults (see consent-and-privacy.md for region list) -->
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('consent', 'default', {
      ad_storage: 'denied', analytics_storage: 'denied',
      ad_user_data: 'denied', ad_personalization: 'denied',
      wait_for_update: 500
      // add region: [...] for region-specific defaults
    });
  </script>
  <!-- 2. CMP script (must call gtag('consent','update',...) on load and on choice) -->
  <script src="https://cmp.example/loader.js" async></script>
  <!-- 3. GTM (or Google tag via your Google tag gateway path) -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
</head>
```

If the CMP is loaded through a GTM template instead, keep step 1 out of the page and use the template on the Consent Initialization trigger. Never both.

## Recipe 2: ecommerce pushes with event_id

```js
// Utility: stable event IDs
function newEventId(prefix) {
  return prefix + '_' + (crypto.randomUUID ? crypto.randomUUID() : Date.now() + '_' + Math.random().toString(36).slice(2));
}

// add_to_cart after the cart API succeeds
async function onAddToCart(product, qty) {
  const res = await fetch('/cart/add', { method: 'POST', body: JSON.stringify({ id: product.id, qty }) });
  if (!res.ok) return;
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({ ecommerce: null });
  dataLayer.push({
    event: 'add_to_cart',
    event_id: newEventId('atc'),
    ecommerce: {
      currency: 'USD',
      value: product.price * qty,
      items: [{ item_id: product.sku, item_name: product.name, price: product.price, quantity: qty }]
    }
  });
}
```

In GTM: GA4 event tag `add_to_cart` with "Send ecommerce data" from data layer; Meta pixel tag with `eventID: {{DLV event_id}}`; TikTok tag with `event_id`.

## Recipe 3: purchase on the confirmation page, fired once

Server-render the purchase payload only the first time the confirmation page is viewed for that order (flag in the database), and guard in the browser too.

```html
<script>
(function () {
  var order = window.__ORDER__; // rendered by server: {id, value, tax, shipping, currency, items, email, phone, isNew}
  if (!order) return;
  var key = 'am_tracked_' + order.id;
  try { if (localStorage.getItem(key)) return; } catch (e) {}
  window.dataLayer = window.dataLayer || [];
  dataLayer.push({ ecommerce: null });
  dataLayer.push({
    event: 'purchase',
    event_id: 'order_' + order.id,
    customer_type: order.isNew ? 'new' : 'returning',
    user_data: { email: order.email, phone_number: order.phone }, // read by tags for enhanced conversions; never put in URLs
    ecommerce: {
      transaction_id: String(order.id),
      value: order.value, tax: order.tax, shipping: order.shipping,
      currency: order.currency, items: order.items
    }
  });
  try { localStorage.setItem(key, '1'); } catch (e) {}
})();
</script>
```

## Recipe 4: click ID and UTM capture (all sites)

Runs on every page as early as possible (before SPA routers rewrite the URL). Stores the latest value per platform for 90 days and UTMs as first and last touch. Fills hidden form fields.

```js
(function () {
  var PARAMS = ['gclid','gbraid','wbraid','fbclid','ttclid','msclkid','li_fat_id','epik','ScCid','rdt_cid','oppref',
                'utm_source','utm_medium','utm_campaign','utm_content','utm_term','utm_id'];
  var DAYS = 90;
  function setCookie(n, v) {
    var exp = new Date(Date.now() + DAYS * 864e5).toUTCString();
    document.cookie = 'am_' + n + '=' + encodeURIComponent(v) + '; expires=' + exp + '; path=/; SameSite=Lax; Secure';
  }
  function getCookie(n) {
    var m = document.cookie.match('(?:^|; )am_' + n + '=([^;]*)');
    return m ? decodeURIComponent(m[1]) : '';
  }
  var qs = new URLSearchParams(window.location.search);
  var hasUtm = false;
  PARAMS.forEach(function (p) {
    var v = qs.get(p);
    if (!v) return;
    setCookie(p, v);
    try { localStorage.setItem('am_' + p, v); } catch (e) {}
    if (p.indexOf('utm_') === 0) hasUtm = true;
  });
  if (hasUtm && !getCookie('ft_utm_source')) {
    ['utm_source','utm_medium','utm_campaign'].forEach(function (p) { if (qs.get(p)) setCookie('ft_' + p, qs.get(p)); });
  }
  // Build Meta fbc if fbclid present and _fbc missing
  var fbclid = qs.get('fbclid');
  if (fbclid && document.cookie.indexOf('_fbc=') === -1) setCookie('fbc', 'fb.1.' + Date.now() + '.' + fbclid);
  if (!getCookie('landing_page')) setCookie('landing_page', location.pathname);

  function fill() {
    PARAMS.concat(['fbc','landing_page','ft_utm_source','ft_utm_medium','ft_utm_campaign']).forEach(function (p) {
      var v = getCookie(p) || (function(){ try { return localStorage.getItem('am_' + p) || ''; } catch (e) { return ''; } })();
      document.querySelectorAll('input[name="' + p + '"]').forEach(function (el) { if (!el.value) el.value = v; });
    });
  }
  document.addEventListener('DOMContentLoaded', fill);
  window.amFillTracking = fill; // call after dynamic forms render
})();
```

Consent note: click ID storage for measurement may require consent in opt-in regions. Gate the script on the CMP's ad or analytics category where counsel requires it, and record consent with the lead.

## Recipe 5: Shopify (Customer events custom pixel plus webhook)

Context: Shopify checkout extensibility replaced checkout.liquid and Additional scripts. The Thank you and Order status page upgrade deadlines were 2025-08-28 for Plus (remaining Plus stores auto-upgraded from January 2026) and 2026-08-26 for non-Plus stores, when script tags and Additional scripts stopped running on those pages [Official, shopify.dev 2026; whether every unupgraded store was auto-upgraded on the day is reported inconsistently]. After the deadline, place a test order and confirm GA4, Google Ads and Meta purchases fire. Tracking now runs through app pixels (Google and YouTube app, Facebook and Instagram app, TikTok app) and custom pixels in Settings > Customer events, which run in a sandbox without access to the storefront DOM.

Prefer native app pixels for GA4, Google Ads (with enhanced conversions) and Meta (Facebook and Instagram app, data sharing "Maximum" for CAPI). Use a custom pixel for platforms without a good app or when you need control.

### 5a. Custom pixel (Settings > Customer events > Add custom pixel)

Set the pixel's Customer privacy permission to "Required" for the right category (marketing for ad pixels) so it only runs with consent.

```js
// Shopify custom pixel. Runs in a sandbox: use analytics.subscribe, not DOM listeners.
// Loads GTM inside the sandbox and forwards Shopify standard events to the data layer.
window.dataLayer = window.dataLayer || [];
function gtag(){ dataLayer.push(arguments); }
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-XXXXXXX');

function toItems(lineItems) {
  return (lineItems || []).map(function (li) {
    return {
      item_id: (li.variant && (li.variant.sku || li.variant.id)) || '',
      item_name: li.title,
      price: li.variant && li.variant.price ? Number(li.variant.price.amount) : undefined,
      quantity: li.quantity
    };
  });
}
function numericId(gid) { return String(gid || '').split('/').pop(); }

analytics.subscribe('product_added_to_cart', function (event) {
  var line = event.data.cartLine;
  dataLayer.push({ ecommerce: null });
  dataLayer.push({
    event: 'add_to_cart', event_id: event.id,
    ecommerce: {
      currency: line.cost.totalAmount.currencyCode,
      value: Number(line.cost.totalAmount.amount),
      items: [{ item_id: line.merchandise.sku || line.merchandise.id, item_name: line.merchandise.product.title,
                price: Number(line.merchandise.price.amount), quantity: line.quantity }]
    }
  });
});

analytics.subscribe('checkout_started', function (event) {
  var c = event.data.checkout;
  dataLayer.push({ ecommerce: null });
  dataLayer.push({ event: 'begin_checkout', event_id: event.id,
    ecommerce: { currency: c.currencyCode, value: Number(c.totalPrice.amount), items: toItems(c.lineItems) } });
});

analytics.subscribe('checkout_completed', function (event) {
  var c = event.data.checkout;
  var orderId = numericId(c.order && c.order.id);
  var tax = c.totalTax ? Number(c.totalTax.amount) : 0;
  var ship = c.shippingLine && c.shippingLine.price ? Number(c.shippingLine.price.amount) : 0;
  dataLayer.push({ ecommerce: null });
  dataLayer.push({
    event: 'purchase',
    event_id: 'order_' + orderId,            // the webhook sender uses the same ID
    user_data: { email: c.email, phone_number: c.phone },
    ecommerce: {
      transaction_id: orderId,
      value: Number(c.totalPrice.amount)-tax-ship,
      tax: tax, shipping: ship, currency: c.currencyCode,
      items: toItems(c.lineItems)
    }
  });
});
```

Field names follow the Web Pixels API standard events (page_viewed, product_viewed, collection_viewed, search_submitted, product_added_to_cart, cart_viewed, checkout_started, checkout_contact_info_submitted, checkout_address_info_submitted, checkout_shipping_info_submitted, payment_info_submitted, checkout_completed). Check the current schema at shopify.dev before shipping; property paths change between API versions.

Limitations: the sandbox has its own document, so GTM preview and some tag templates behave differently; Tag Assistant may not attach. Test with real test orders and platform test tools.

### 5b. Server: order webhook to CAPIs

Subscribe to `orders/paid` (or `orders/create` if payment is captured later and you accept unpaid orders) via an app or Shopify Flow plus a webhook. Verify the HMAC, then send with the shared sender (Recipe 8). Store fbp, fbc, client_id and click IDs on the order via cart attributes or note attributes at checkout if you need them server-side (the custom pixel can read cookies like `_fbp` with `browser.cookie.get` and send them to your endpoint).

```ts
// app/api/shopify/orders-paid/route.ts (Next.js route handler as an example host)
import crypto from 'node:crypto';
import { sendPurchase } from '@/lib/server-events';

export async function POST(req: Request) {
  const raw = await req.text();
  const hmac = req.headers.get('x-shopify-hmac-sha256') || '';
  const digest = crypto.createHmac('sha256', process.env.SHOPIFY_WEBHOOK_SECRET!).update(raw, 'utf8').digest('base64');
  if (!crypto.timingSafeEqual(Buffer.from(digest), Buffer.from(hmac))) return new Response('bad hmac', { status: 401 });
  const o = JSON.parse(raw);
  const attrs = Object.fromEntries((o.note_attributes || []).map((a: any) => [a.name, a.value]));
  if (attrs.consent_ads !== 'true') return new Response('no ad consent', { status: 200 });
  await sendPurchase({
    eventId: 'order_' + o.id,
    orderId: String(o.id),
    eventTime: Math.floor(new Date(o.processed_at || o.created_at).getTime() / 1000),
    value: Number(o.current_subtotal_price),
    currency: o.currency,
    email: o.email, phone: o.phone || o.billing_address?.phone,
    firstName: o.customer?.first_name, lastName: o.customer?.last_name,
    city: o.billing_address?.city, zip: o.billing_address?.zip, country: o.billing_address?.country_code,
    externalId: o.customer?.id ? String(o.customer.id) : undefined,
    ip: o.browser_ip, userAgent: o.client_details?.user_agent,
    fbp: attrs._fbp, fbc: attrs.fbc, ttclid: attrs.ttclid, ttp: attrs._ttp,
    gaClientId: attrs.ga_client_id, gaSessionId: attrs.ga_session_id,
    sourceUrl: 'https://' + process.env.SHOP_DOMAIN + '/checkouts/thank-you',
    items: (o.line_items || []).map((li: any) => ({ id: li.sku || String(li.variant_id), quantity: li.quantity, price: Number(li.price) }))
  });
  return new Response('ok');
}
```

If the Meta Facebook and Instagram app already sends CAPI purchases, do not add a second Meta server sender (double counting risk); use the custom sender only for platforms the apps do not cover.

## Recipe 6: WooCommerce

Use a maintained plugin for the data layer where possible (for example GTM4WP for WooCommerce data layer events, or the official Google for WooCommerce and Meta plugins). When custom code is needed:

```php
<?php
// Purchase data layer on the thank you page, fired once per order (HPOS compatible meta API)
add_action( 'woocommerce_thankyou', function ( $order_id ) {
    if ( ! $order_id ) { return; }
    $order = wc_get_order( $order_id );
    if ( ! $order || $order->get_meta( '_am_dl_tracked' ) ) { return; }
    $items = array();
    foreach ( $order->get_items() as $item ) {
        $product = $item->get_product();
        $items[] = array(
            'item_id'   => $product ? ( $product->get_sku() ? $product->get_sku() : (string) $product->get_id() ) : (string) $item->get_product_id(),
            'item_name' => $item->get_name(),
            'price'     => (float) $order->get_item_total( $item, false ),
            'quantity'  => (int) $item->get_quantity(),
        );
    }
    $tax      = (float) $order->get_total_tax();
    $shipping = (float) $order->get_shipping_total();
    $payload  = array(
        'event'     => 'purchase',
        'event_id'  => 'order_' . $order->get_id(),
        'user_data' => array( 'email' => $order->get_billing_email(), 'phone_number' => $order->get_billing_phone() ),
        'ecommerce' => array(
            'transaction_id' => (string) $order->get_order_number(),
            'value'          => round( (float) $order->get_total()-$tax-$shipping, 2 ),
            'tax'            => $tax,
            'shipping'       => $shipping,
            'currency'       => $order->get_currency(),
            'items'          => $items,
        ),
    );
    echo '<script>window.dataLayer=window.dataLayer||[];dataLayer.push({ecommerce:null});dataLayer.push(' . wp_json_encode( $payload ) . ');</script>';
    $order->update_meta_data( '_am_dl_tracked', 1 );
    $order->save();
}, 20 );

// Capture browser identifiers at checkout for server events
add_action( 'woocommerce_checkout_create_order', function ( $order ) {
    foreach ( array( '_fbp', '_fbc', 'am_fbc', '_ttp', 'am_ttclid', 'am_gclid', 'am_msclkid', '_ga' ) as $c ) {
        if ( isset( $_COOKIE[ $c ] ) ) { $order->update_meta_data( '_am_' . $c, sanitize_text_field( wp_unslash( $_COOKIE[ $c ] ) ) ); }
    }
    $order->update_meta_data( '_am_ip', WC_Geolocation::get_ip_address() );
    $order->update_meta_data( '_am_ua', isset( $_SERVER['HTTP_USER_AGENT'] ) ? sanitize_text_field( wp_unslash( $_SERVER['HTTP_USER_AGENT'] ) ) : '' );
} );

// Server-side purchase, async via Action Scheduler (bundled with WooCommerce)
add_action( 'woocommerce_order_status_processing', function ( $order_id ) {
    as_enqueue_async_action( 'am_send_capi_purchase', array( 'order_id' => $order_id ), 'ads-master' );
} );
add_action( 'am_send_capi_purchase', function ( $order_id ) {
    $order = wc_get_order( $order_id );
    if ( ! $order || $order->get_meta( '_am_capi_sent' ) ) { return; }
    $norm  = function ( $s ) { return strtolower( trim( (string) $s ) ); };
    $phone = preg_replace( '/\D+/', '', (string) $order->get_billing_phone() ); // add country code logic for local numbers
    $body  = array( 'data' => array( array(
        'event_name'       => 'Purchase',
        'event_time'       => $order->get_date_created()->getTimestamp(),
        'event_id'         => 'order_' . $order->get_id(),
        'action_source'    => 'website',
        'event_source_url' => $order->get_checkout_order_received_url(),
        'user_data'        => array_filter( array(
            'em'                => array( hash( 'sha256', $norm( $order->get_billing_email() ) ) ),
            'ph'                => $phone ? array( hash( 'sha256', $phone ) ) : null,
            'client_ip_address' => $order->get_meta( '_am_ip' ),
            'client_user_agent' => $order->get_meta( '_am_ua' ),
            'fbp'               => $order->get_meta( '_am__fbp' ),
            'fbc'               => $order->get_meta( '_am__fbc' ) ? $order->get_meta( '_am__fbc' ) : $order->get_meta( '_am_am_fbc' ),
        ) ),
        'custom_data'      => array( 'currency' => $order->get_currency(), 'value' => (float) $order->get_subtotal(), 'order_id' => (string) $order->get_id() ),
    ) ) );
    $url  = 'https://graph.facebook.com/' . META_API_VERSION . '/' . META_PIXEL_ID . '/events?access_token=' . META_CAPI_TOKEN;
    $resp = wp_remote_post( $url, array( 'timeout' => 10, 'headers' => array( 'Content-Type' => 'application/json' ), 'body' => wp_json_encode( $body ) ) );
    if ( ! is_wp_error( $resp ) && 200 === wp_remote_retrieve_response_code( $resp ) ) {
        $order->update_meta_data( '_am_capi_sent', 1 );
        $order->save();
    } else {
        throw new Exception( 'CAPI send failed' ); // Action Scheduler logs and you can retry
    }
} );
```

Define META_API_VERSION, META_PIXEL_ID and META_CAPI_TOKEN in wp-config.php from environment variables. Gate on stored consent before sending.

## Recipe 7: Next.js (App Router) and SPAs

### 7a. Layout with consent default and GTM

```tsx
// app/layout.tsx
import Script from 'next/script';
import { GoogleTagManager } from '@next/third-parties/google';
import { Suspense } from 'react';
import RouteTracker from './route-tracker';

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <Script id="consent-default" strategy="beforeInteractive">{`
          window.dataLayer = window.dataLayer || [];
          function gtag(){dataLayer.push(arguments);}
          gtag('consent','default',{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500});
        `}</Script>
      </head>
      <GoogleTagManager gtmId={process.env.NEXT_PUBLIC_GTM_ID!} />
      <body>
        {children}
        <Suspense fallback={null}><RouteTracker /></Suspense>
      </body>
    </html>
  );
}
```

### 7b. Route change page views

Choose one method. Either GA4 enhanced measurement "Page changes based on browser history events" (no code; GA4 sends page_view on pushState), or manual virtual page views (below) with that enhanced measurement option off. Never both.

```tsx
// app/route-tracker.tsx
'use client';
import { usePathname, useSearchParams } from 'next/navigation';
import { useEffect, useRef } from 'react';

export default function RouteTracker() {
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const first = useRef(true);
  useEffect(() => {
    if (first.current) { first.current = false; return; } // initial page_view sent by the Google tag
    const url = pathname + (searchParams?.toString() ? '?' + searchParams.toString() : '');
    (window as any).dataLayer = (window as any).dataLayer || [];
    (window as any).dataLayer.push({
      event: 'page_view',
      page_location: window.location.origin + url,
      page_title: document.title
    });
  }, [pathname, searchParams]);
  return null;
}
```

In GTM: GA4 event tag "page_view" on Custom Event `page_view`, with the Google tag set to not send the automatic page view on history changes. Title may lag one render in some apps; set `page_title` from route metadata if needed.

Pages Router: subscribe to `router.events.on('routeChangeComplete', handler)` in `_app.tsx`. React Router, Vue Router, SvelteKit: same pattern in the router's after-navigation hook.

### 7c. Server action or route handler for conversions

Send lead and purchase server events from the place where the business action is confirmed (server action, API route, webhook), not from the client. Pass event_id from the client (generated before submit) so the browser pixel and the server event match.

```ts
// app/actions/submit-lead.ts
'use server';
import { cookies, headers } from 'next/headers';
import { sendLead } from '@/lib/server-events';

export async function submitLead(form: FormData) {
  const eventId = String(form.get('event_id'));
  // ...validate, save to CRM with click IDs from hidden fields...
  const c = await cookies(); const h = await headers();
  if (c.get('am_consent_ads')?.value === 'true') {
    await sendLead({
      eventId, email: String(form.get('email')), phone: String(form.get('phone') || ''),
      ip: h.get('x-forwarded-for')?.split(',')[0]?.trim(), userAgent: h.get('user-agent') || undefined,
      fbp: c.get('_fbp')?.value, fbc: c.get('_fbc')?.value || c.get('am_fbc')?.value,
      ttclid: c.get('am_ttclid')?.value, ttp: c.get('_ttp')?.value,
      sourceUrl: h.get('referer') || undefined, value: 300, currency: 'USD'
    });
  }
}
```

`cookies()` and `headers()` are async in recent Next.js versions; adjust for the project's version.

## Recipe 8: server-side event sender (TypeScript, Node 18+)

```ts
// lib/server-events.ts
import crypto from 'node:crypto';

const sha = (v?: string) => (v ? crypto.createHash('sha256').update(v, 'utf8').digest('hex') : undefined);
const normEmail = (e?: string) => (e ? e.trim().toLowerCase() : undefined);
// Digits only, with country code. Configure the default country code for local numbers.
const normPhoneDigits = (p?: string, defaultCc = process.env.DEFAULT_CC || '') => {
  if (!p) return undefined;
  let d = p.replace(/\D+/g, '');
  if (d.startsWith('00')) d = d.slice(2);
  else if (d.startsWith('0') && defaultCc) d = defaultCc + d.slice(1);
  return d || undefined;
};
const e164 = (p?: string) => { const d = normPhoneDigits(p); return d ? '+' + d : undefined; };
const normName = (s?: string) => (s ? s.trim().toLowerCase().replace(/[^\p{L}\p{N}]/gu, '') : undefined);

type Item = { id: string; quantity: number; price: number };
export type ConvEvent = {
  eventId: string; orderId?: string; eventTime?: number; value?: number; currency?: string;
  email?: string; phone?: string; firstName?: string; lastName?: string; city?: string; zip?: string; country?: string;
  externalId?: string; ip?: string; userAgent?: string; fbp?: string; fbc?: string; ttclid?: string; ttp?: string;
  gaClientId?: string; gaSessionId?: string; sourceUrl?: string; items?: Item[];
};

async function post(url: string, body: unknown, headers: Record<string, string> = {}, tries = 4) {
  for (let i = 0; i < tries; i++) {
    const res = await fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json', ...headers }, body: JSON.stringify(body) });
    if (res.ok) return res;
    if (res.status < 500 && res.status !== 429) throw new Error(url + ' ' + res.status + ' ' + (await res.text()));
    await new Promise(r => setTimeout(r, 500 * 2 ** i));
  }
  throw new Error('retries exhausted: ' + url);
}

function metaUserData(e: ConvEvent) {
  const ud: Record<string, unknown> = {
    em: e.email ? [sha(normEmail(e.email))] : undefined,
    ph: e.phone ? [sha(normPhoneDigits(e.phone))] : undefined,
    fn: e.firstName ? [sha(normName(e.firstName))] : undefined,
    ln: e.lastName ? [sha(normName(e.lastName))] : undefined,
    ct: e.city ? [sha(normName(e.city))] : undefined,
    zp: e.zip ? [sha(e.zip.trim().toLowerCase().replace(/\s+/g, ''))] : undefined,
    country: e.country ? [sha(e.country.trim().toLowerCase())] : undefined,
    external_id: e.externalId ? [sha(e.externalId)] : undefined,
    client_ip_address: e.ip, client_user_agent: e.userAgent, fbp: e.fbp, fbc: e.fbc
  };
  return Object.fromEntries(Object.entries(ud).filter(([, v]) => v !== undefined));
}

export async function sendMeta(eventName: string, e: ConvEvent) {
  if (!process.env.META_PIXEL_ID) return;
  const url = `https://graph.facebook.com/${process.env.META_API_VERSION}/${process.env.META_PIXEL_ID}/events?access_token=${process.env.META_CAPI_TOKEN}`;
  return post(url, {
    data: [{
      event_name: eventName, event_time: e.eventTime ?? Math.floor(Date.now() / 1000), event_id: e.eventId,
      action_source: 'website', event_source_url: e.sourceUrl, user_data: metaUserData(e),
      custom_data: { currency: e.currency, value: e.value, order_id: e.orderId,
        contents: e.items?.map(i => ({ id: i.id, quantity: i.quantity, item_price: i.price })), content_type: e.items ? 'product' : undefined }
    }],
    ...(process.env.META_TEST_EVENT_CODE ? { test_event_code: process.env.META_TEST_EVENT_CODE } : {})
  });
}

export async function sendTikTok(eventName: string, e: ConvEvent) {
  if (!process.env.TIKTOK_PIXEL_CODE) return;
  return post('https://business-api.tiktok.com/open_api/v1.3/event/track/', {
    event_source: 'web', event_source_id: process.env.TIKTOK_PIXEL_CODE,
    data: [{
      event: eventName, event_time: e.eventTime ?? Math.floor(Date.now() / 1000), event_id: e.eventId,
      user: { email: sha(normEmail(e.email)), phone: sha(e164(e.phone)), external_id: sha(e.externalId),
              ttclid: e.ttclid, ttp: e.ttp, ip: e.ip, user_agent: e.userAgent },
      page: { url: e.sourceUrl },
      properties: { currency: e.currency, value: e.value, order_id: e.orderId, content_type: 'product',
        contents: e.items?.map(i => ({ content_id: i.id, quantity: i.quantity, price: i.price })) }
    }]
  }, { 'Access-Token': process.env.TIKTOK_ACCESS_TOKEN! });
}

export async function sendGa4(eventName: string, e: ConvEvent, params: Record<string, unknown> = {}) {
  if (!process.env.GA4_MEASUREMENT_ID || !e.gaClientId) return; // no client_id: skip rather than create Unassigned noise
  const url = `https://www.google-analytics.com/mp/collect?measurement_id=${process.env.GA4_MEASUREMENT_ID}&api_secret=${process.env.GA4_API_SECRET}`;
  return post(url, {
    client_id: e.gaClientId,
    events: [{ name: eventName, params: { session_id: e.gaSessionId, engagement_time_msec: 1, ...params } }]
  });
}

export async function sendPurchase(e: ConvEvent) {
  const results = await Promise.allSettled([
    sendMeta('Purchase', e),
    sendTikTok('CompletePayment', e)
    // GA4 purchase from server only if the browser purchase is missing for this order (avoid duplicates)
  ]);
  results.forEach((r, i) => { if (r.status === 'rejected') console.error('server event failed', i, r.reason); });
  return results;
}

export async function sendLead(e: ConvEvent) {
  return Promise.allSettled([sendMeta('Lead', e), sendTikTok('SubmitForm', e)]);
}
```

Parsing GA cookies for client_id and session_id: `_ga` looks like `GA1.1.1234567890.1759990000` (client_id is the last two parts joined by a dot). The `_ga_<ID>` session cookie changed format in 2025 from `GS1.1.<session_id>.<n>...` to a `GS2.1.s<session_id>$o<n>$g...` style [Practitioner reports, 2025]; parse both, or read the IDs in GTM with the built-in Client ID and Session ID variables (added December 2025) and push them into the order.

Python equivalent for hashing:

```python
import hashlib, re
def sha256(v: str) -> str: return hashlib.sha256(v.encode("utf-8")).hexdigest()
def norm_email(e: str) -> str: return e.strip().lower()
def norm_phone_digits(p: str, default_cc: str = "") -> str:
    d = re.sub(r"\D+", "", p or "")
    if d.startswith("00"): d = d[2:]
    elif d.startswith("0") and default_cc: d = default_cc + d[1:]
    return d
```

## Recipe 9: proposing changes (diff format and checklist)

Deliver code as a unified diff in the deliverable, plus:
1. What changes and why (link to finding ID).
2. Files touched; environment variables needed (names only, no values).
3. Consent behavior of the change.
4. Test steps: local or staging URL, actions, expected data layer output, expected network requests (endpoints below), platform test tool screenshots.
5. Rollback: revert commit or GTM version number.
6. Monitoring for 7 days: which reconciliation numbers should move and by how much.

Network endpoints to look for in DevTools:

| Platform | Request pattern |
|----------|-----------------|
| GA4 | `/g/collect?v=2` (google-analytics.com, region1, or your gateway path) |
| Google Ads | `googleadservices.com/pagead/conversion`, `/ccm/collect` |
| Meta | `facebook.com/tr` |
| TikTok | `analytics.tiktok.com/api/v2/pixel` |
| Microsoft UET | `bat.bing.com/action` |
| LinkedIn | `px.ads.linkedin.com` |
| Pinterest | `ct.pinterest.com` |
| Snap | `tr.snapchat.com` |
| Reddit | `alb.reddit.com` |
| sGTM | Your tagging server domain or path |
