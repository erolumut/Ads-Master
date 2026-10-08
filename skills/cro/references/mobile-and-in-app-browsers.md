# Mobile and In-App Browsers

> Knowledge as of 2026-10. Scope: the phone and in-app browser (IAB) layer of paid social conversion: how the Instagram, Facebook, TikTok, LinkedIn and Snapchat in-app browsers change login, cookies, wallets, autofill, payment redirects, downloads and tracking; how to test inside each app; mobile checkout and form details with code; worst case content checks for commerce pages; and real device testing. Speed is in [Speed and Core Web Vitals](speed-and-core-web-vitals.md); checkout UX evidence in [Ecommerce PDP, cart and checkout](ecommerce-pdp-cart-checkout.md); forms in [Forms and lead capture](forms-and-lead-capture.md). The platform-layer fixes and the worst case data method here were inspired by ideas in Emil Kowalski's skills repository (mobile-native and break-ui); the text is original. See section 9 for sources.

## 1. Why it matters

Most paid social clicks come from phones and open inside the app that showed the ad, not in Safari or Chrome [Practitioner consensus]. The visitor is in an embedded browser with its own cookie jar, no saved logins, often no Apple Pay, a toolbar eating screen height and a close button one tap away from the feed. A page that converts in desktop QA can fail here.

| App | iOS | Android | Notes |
|-----|-----|---------|-------|
| Instagram, Facebook | WKWebView; Meta's apps inject JavaScript into pages opened in the IAB (Meta said: to aggregate pixel conversion events) [Study, 2022-08, Krause] | Meta ships its own Chromium based WebView for the Facebook IAB, updated with the app [Official, Meta Engineering 2022-09] | Meta offers its own autofill of contact and payment details inside the IAB when the user saved them [Official, Meta Help] |
| TikTok | WKWebView with injected JavaScript reported [Study, 2022-08, Krause] | Android WebView | User agent contains `BytedanceWebview` or `musical_ly` [Practitioner] |
| LinkedIn | In-app browser | In-app browser; an "Open web links in app" setting reportedly lets users switch it off [Unverified] | B2B lead forms and demo pages land here |
| Snapchat | In-app browser | In-app browser | Short sessions; fast first screen matters most |

Every iOS browser and IAB uses WebKit, so Safari rules apply everywhere on iPhone. No official 2026 change to how Meta's apps open outbound links was found in the 2026-10 check; settings to open links externally come and go by app version (Facebook Android has had a "Links open externally" toggle; Instagram has no global setting as of 2026 per third-party guides) [Unverified]. Meta moved iOS Facebook Login from an in-app browser flow to a fast app switch into the Facebook app [Official via trade press; date unverified].

## 2. Quirks and their impact

| Quirk | What happens | Conversion impact | Tracking impact | Mitigation |
|-------|-------------|-------------------|-----------------|-----------|
| Separate cookie jar | IAB does not share cookies with Safari or Chrome | Returning customers look logged out; saved carts and discount codes vanish | Click in IAB, purchase later in Safari: click ID cookie is gone | Guest checkout first; magic link or one-time code login; persist cart server side by email capture; send conversions server side with hashed email or phone (measurement) |
| Third-party cookies blocked | WKWebView apps get full third-party cookie blocking and ITP style protections by default on modern iOS [Official, WebKit 2020; verify current iOS] | Embedded third-party login, payment or review iframes that rely on cookies fail | Third-party pixels lose state | First-party endpoints, server-side tagging, avoid cookie dependent iframes in checkout |
| Apple Pay missing | WebKit disables Apple Pay in web views where the host app injected scripts [Official, WebKit changeset 2019]; Meta and TikTok inject scripts, and merchants report Apple Pay missing in those IABs [Practitioner, inference] | The fastest mobile payment disappears for iPhone buyers from social | None directly | Feature detect (`window.ApplePaySession && ApplePaySession.canMakePayments()`), show the next best express option (Shop Pay, PayPal, card with autofill); never leave an empty button slot |
| Google Pay in Android WebView | Supported from WebView 137 with Play services 25.18.30, but only when the host app enables Payment Request in its WebView settings [Official, Google, 2025-05] | Depends on each app's integration; test, do not assume | None | Feature detect with the Google Pay `isReadyToPay` call; fallback buttons |
| Sign in with Google | Google blocks OAuth in embedded web views (`disallowed_useragent`) [Official, Google, 2021-06] | Social login buttons dead end | Login funnel drops | Email or passkey based login; hide Google sign-in when an IAB is detected, or explain "open in browser" |
| Autofill | Safari contact and card autofill and iCloud Keychain passwords are often unavailable; Meta's own autofill fills fields it recognizes [Official, Meta Help; Practitioner] | Typing on a phone keyboard kills conversion | None | Standard `autocomplete` tokens (section 4) so every autofill engine recognizes fields; fewer fields |
| Payment redirects and popups | 3-D Secure, PayPal, BNPL, iDEAL and bank redirects may open popups or new windows that IABs handle badly; Stripe warns popup based methods may not work in in-app webviews [Official, Stripe docs] | Payment fails or the return URL lands in another browser | Purchase recorded in a different browser session | Use redirect (not popup) flows, test return URLs inside each app, keep order state server side so the thank you page works anywhere |
| File downloads | PDFs, calendar files and vCards may not download or open | Lead magnets and booking confirmations fail | Missing download events | Show the content as a page; email the file; add to calendar via links that also work in browser |
| New tabs and `window.open` | `target="_blank"` and scripted windows behave inconsistently, sometimes leaving the IAB | Users lose their place | Session split | Keep the funnel in one tab; no forced new windows |
| App links and deep links | Meta's iOS web view reportedly blocks automatic app launches from the page [Practitioner, 2025 to 2026] | "Open in app" flows stall | Attribution to app installs breaks | Offer a visible button; use deferred deep linking through the app's attribution provider (mobile-app-growth) |
| Short sessions and close button | One tap returns to the feed; no history to come back to | Abandonment without a return path | Fewer multi-page sessions | Value and CTA in the first screen; capture email early with a clear reason; retargeting |
| Toolbars and viewport | IAB chrome at top and bottom takes height; `100vh` overflows | Sticky CTAs hidden under bars | None | `svh` and `dvh` units and safe area insets (section 4) |
| Consent | CMP state is per browser; consent given in Safari does not carry over | Banner covers the first screen on every IAB visit | Consent rate in IAB differs | Compact mobile banner that does not cover the CTA; measure consent rate by user agent (measurement) |

Detect an IAB only to adapt (hide a button that cannot work, show a hint), never to change content or prices. User agent markers [Practitioner, verify on current versions]: `FBAN` or `FBAV` (Facebook), `Instagram`, `BytedanceWebview` or `musical_ly` (TikTok), `LinkedInApp`, `Snapchat`. Prefer feature detection for wallets.

```js
// Adapt, do not cloak: hide unavailable options and offer a fallback
const ua = navigator.userAgent || "";
const inApp = /FBAN|FBAV|Instagram|BytedanceWebview|musical_ly|LinkedInApp|Snapchat/i.test(ua);
const applePay = !!(window.ApplePaySession && ApplePaySession.canMakePayments && ApplePaySession.canMakePayments());
document.documentElement.dataset.inApp = inApp ? "1" : "0";
if (!applePay) document.querySelectorAll("[data-wallet=apple-pay]").forEach((el) => el.hidden = true);
// Report the context for analysis (no personal data)
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({ event: "browser_context", in_app: inApp, apple_pay: applePay });
```

## 3. How to test inside each app

1. Get the real path: send ad previews to a phone (Meta Ads Manager preview share, TikTok Ads Manager preview QR code, LinkedIn and Snapchat preview links), or paste the landing URL with its UTMs into a private DM to your own test account and tap it.
2. Confirm you are in the IAB: open a staging page that prints `navigator.userAgent`, `ApplePaySession` availability, cookie support and viewport sizes.
3. Debugging: Safari Web Inspector only attaches to app web views that the app marks inspectable (iOS 16.4 and later require `isInspectable`) [Official, WebKit 2023-03]; Android `chrome://inspect` only sees web views with debugging enabled. Third-party release apps usually allow neither, so use an on-page debug console on staging only (for example Eruda), server logs, and session recordings with consent (Clarity).
4. Run the matrix below on at least one iPhone and one mid-range Android. Record pass or fail, screenshots and notes in `ads-master/outputs/cro/YYYY-MM-DD_cro_in-app-browser-qa.md`.
5. Retest after every theme, checkout, payment, consent or tag release, and when an app shows a major version update.

| Flow | Instagram iOS | Instagram Android | Facebook iOS | Facebook Android | TikTok iOS | TikTok Android | LinkedIn | Snapchat |
|------|---------------|-------------------|--------------|------------------|-----------|----------------|----------|----------|
| First screen renders under 2.5 s on 4G, CTA visible above toolbars | | | | | | | | |
| Add to cart, cart persists after reload | | | | | | | | |
| Express wallets shown only when available; fallback visible | | | | | | | | |
| Card payment with 3-D Secure completes and returns | | | | | | | | |
| Redirect payment method (PayPal, iDEAL, BNPL) completes and returns | | | | | | | | |
| Login or account creation (no Google OAuth dead end) | | | | | | | | |
| Lead form submits; error states readable; keyboard does not hide the button | | | | | | | | |
| Download or calendar file works or has an alternative | | | | | | | | |
| Consent banner does not cover CTA; choice saved | | | | | | | | |
| Purchase or lead event fires once (pixel plus server event deduplicated) | | | | | | | | |

## 4. Mobile checkout and form details

| Detail | Rule | Why |
|--------|------|-----|
| Input font size | 16px minimum on inputs, selects and textareas | iOS Safari zooms into smaller inputs and does not zoom back [Practitioner consensus] |
| Zoom | Never `user-scalable=no` or `maximum-scale=1` | Accessibility failure (WCAG 1.4.4); fix the font size instead |
| Keyboard type | `type="email"`, `type="tel"`, `inputmode="numeric"` for codes and postal codes without letters, `inputmode="decimal"` for amounts | Right keyboard on first tap |
| Autocomplete tokens | `name`, `given-name`, `family-name`, `email`, `tel`, `street-address` or `address-line1` and `address-line2`, `address-level2` (city), `address-level1` (region), `postal-code`, `country`, `cc-name`, `cc-number`, `cc-exp`, `cc-csc`, `one-time-code`; prefix `shipping` or `billing` | Every autofill engine (browser, password manager, Meta autofill) maps fields |
| Return key | `enterkeyhint="next"` between fields, `"done"` or `"send"` on the last | Users know what the key does |
| Text helpers | `autocapitalize="none"` and `autocorrect="off"` on emails and codes, `spellcheck="false"` | Prevents "Name@Example.com" errors |
| Express checkout | Wallet buttons above the fold on cart and checkout, with a visible fallback | Fastest path on mobile; IABs drop some wallets |
| Sticky add to cart | Fixed bar with price and button, padded by `env(safe-area-inset-bottom)` | Stays tappable above the home indicator |
| Viewport units | `min-height: 100svh` for heroes (stable, never cut off); `height: 100dvh` for app shells, drawers and full screen checkout steps | `100vh` equals the largest viewport and overflows under toolbars |
| Notch and edges | `viewport-fit=cover` plus `env(safe-area-inset-*)` padding on fixed bars | Without the meta tag the insets are 0 |
| Tap response | `touch-action: manipulation` on buttons and links; `:active` styles | Removes double-tap zoom delay; instant feedback |
| Hover | Wrap `:hover` rules in `@media (hover: hover) and (pointer: fine)` | Stops stuck hover states after a tap |
| Tap highlight | `-webkit-tap-highlight-color: transparent` once, with your own `:active` states | Removes the gray flash |
| Overscroll | `overscroll-behavior: contain` on drawers, sheets and cart panels | Scrolling a drawer does not scroll the page behind |
| Target size | At least 24 by 24 CSS px (WCAG 2.2 SC 2.5.8 AA); aim for 44 to 48 px on primary actions | Fewer mis-taps |
| Keyboard overlap | `interactive-widget=resizes-content` in the viewport meta on Android Chrome; scroll the focused field and the submit button into view | Button stays visible above the keyboard |
| Errors | Inline, next to the field, keep entered values, plain language | Phone retyping is expensive |

Baseline code:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
<form autocomplete="on">
  <input name="email" type="email" autocomplete="email" autocapitalize="none" autocorrect="off" spellcheck="false" enterkeyhint="next" required>
  <input name="tel" type="tel" autocomplete="shipping tel" enterkeyhint="next">
  <input name="address1" autocomplete="shipping address-line1" enterkeyhint="next">
  <input name="postal" autocomplete="shipping postal-code" inputmode="text" enterkeyhint="next">
  <input name="cc" autocomplete="cc-number" inputmode="numeric" enterkeyhint="next">
  <input name="otp" autocomplete="one-time-code" inputmode="numeric" enterkeyhint="done">
  <button type="submit">Pay securely</button>
</form>
```

```css
html { -webkit-tap-highlight-color: transparent; -webkit-text-size-adjust: 100%; }
input, select, textarea { font-size: 16px; }
button, a, [role="button"] { touch-action: manipulation; }
.hero { min-height: 100svh; }
.checkout-shell { height: 100dvh; }
.sticky-atc {
  position: fixed; inset-inline: 0; bottom: 0;
  padding: 12px 16px calc(12px + env(safe-area-inset-bottom, 0px));
  background: var(--surface);
}
.cart-drawer { overflow-y: auto; overscroll-behavior: contain; }
.btn:active { transform: scale(0.98); }
@media (hover: hover) and (pointer: fine) {
  .btn:hover { filter: brightness(1.05); }
}
```

Use `inputmode="text"` for postal codes in markets with letters (UK `SW1A 1AA`, Netherlands `1234 AB`) and `numeric` only where codes are digits (Turkey, Germany, US).

## 5. Worst case content checks for commerce pages

Demo data makes pages look good. Before launch, render each template with the worst realistic values from the catalog and look at 320 px width, 200% text zoom, dark mode and, for Arabic markets, right to left. Change the data, not the CSS, to produce the case.

| Case | Realistic worst value | What breaks | Fix |
|------|----------------------|-------------|-----|
| Long product name | "Merino Everyday Crew Socks, Extra Cushioned Heel and Toe, Unisex, Pack of 6" | Title wraps to 4 lines, pushes price and button below the fold | Clamp on cards (2 lines) with full name on PDP; never truncate price |
| Long variant name | "Heather Charcoal Melange / EU 43 to 46 / Extra Long Leg" | Swatch labels overflow, select box clips | Wrap labels; show selected variant in full under the selector |
| Turkish, German, Dutch copy | Translations run about 30% longer than English, short labels can double: "In den Warenkorb legen", "Sepete ekle", "In winkelwagen" | Fixed width buttons and badges overflow | Width from content with `min-width`; test every language |
| Turkish casing | "İndirim", "ışık"; `text-transform: uppercase` without `lang="tr"` turns "indirim" into "INDIRIM" | Wrong letters in headlines and buttons | Set `lang` per page; avoid forced uppercase; see creative-strategy localization module |
| German compounds | "Versandkostenfreigrenze" | Unbreakable words overflow | `hyphens: auto` with `lang="de"`, `overflow-wrap: anywhere` as last resort |
| Price formats | "1.234,56 TL", "₺1.234,56", "EUR 1.234,56", "€ 1.234,56" (nl), "1.234,56 €" (de) | Hard coded separators, currency on the wrong side, columns misaligned | `Intl.NumberFormat(locale, { style: "currency", currency })`; `font-variant-numeric: tabular-nums` |
| Installments | "3 taksit x 412,50 TL" or "6 Raten à 21,50 €" | Long price lines wrap under the button | Separate line under the price |
| Zero reviews | No rating yet | Empty stars look like 0 out of 5 | Hide the rating block or say "No reviews yet" |
| One review | "1 reviews", 5.0 from 1 review | Plural bug; inflated trust | `Intl.PluralRules`; show the count next to the score |
| Sold out | Whole product, one variant, all sizes in one color | Disabled button with no explanation; dead end from ads | "Notify me" capture, show alternatives, pause ads on sold out products (commerce-feeds, channel agents) |
| Back in stock and low stock | "Back in stock", "Only 2 left" | Claims that are not true are a dark pattern | Show only real inventory states |
| Many variants | 12 colors x 9 sizes | Swatch grid pushes CTA far down | Size select plus color swatches with overflow "+5" |
| Long discount or bundle text | "Buy 2 get the third pair free, applies to merino range only" | Promo badge covers image or wraps | Badge max 2 lines; terms link |
| Shipping threshold | "Add TL 87,50 for free shipping" in several languages | Progress bars overflow | Test longest language |
| Long addresses | Turkish addresses with mahalle, sokak, numara and daire; Dutch postcode plus house number additions | Fields too short, validation rejects valid input | Long fields, permissive validation, address lookup |
| Right to left (Arabic) | Arabic product name with a Latin brand name and a price | Icons and chevrons point the wrong way, mixed text reorders | `dir="rtl"`, CSS logical properties, `<bdi>` around Latin and numbers, mirror only directional icons |
| Missing or odd images | 404 image, 4000 x 600 banner as product image | Broken icon, layout jump | Fixed `aspect-ratio`, `object-fit`, fallback image |
| Huge cart | 20 line items, long names | Totals pushed off screen | Collapsible line items; sticky total |

## 6. Real device testing

| Need | How |
|------|-----|
| iPhone debugging | iPhone: Settings > Apps > Safari > Advanced > Web Inspector on. Mac: Safari > Develop > device name. Works for Safari and inspectable web views |
| Android debugging | Developer options and USB debugging on; desktop Chrome `chrome://inspect#devices`; port forwarding for a local dev server |
| Local build on a phone | Serve on `0.0.0.0` and open the LAN IP, or use an HTTPS tunnel (wallets and many APIs require HTTPS) |
| Device set | One current iPhone, one iPhone several generations old, one mid-range Android (performance), plus tablets if traffic warrants; cloud device labs for coverage, not for IAB behavior |
| Conditions | Keyboard open, landscape once, slow network throttling, low power mode, large text setting |

Emulation in desktop DevTools does not reproduce IAB cookies, wallets, sticky hover, tap delay, safe areas or the software keyboard. Real devices are the release bar.

## 7. Scored checklist

| ID | Check | Severity |
|----|-------|----------|
| M1 | Landing and checkout flows pass the IAB matrix for every app that sends paid traffic | Critical |
| M2 | Purchase or lead event fires once in IAB sessions (pixel and server event deduplicated) | Critical |
| M3 | Wallet buttons feature detected with visible fallback | High |
| M4 | No Google OAuth dead end in IABs | High |
| M5 | Payment redirects return correctly inside each app | High |
| M6 | Guest checkout available; cart persists server side | High |
| M7 | 16px inputs; zoom not disabled | High |
| M8 | Correct `type`, `inputmode`, `autocomplete` and `enterkeyhint` on every checkout and lead field | High |
| M9 | First screen shows value and CTA above IAB toolbars on a 360 x 640 viewport | High |
| M10 | Sticky CTA respects safe area insets; no `100vh` on bottom pinned UI | Medium |
| M11 | Hover styles gated by `(hover: hover) and (pointer: fine)` | Medium |
| M12 | Tap targets at least 24 px, primary actions 44 px or more | Medium |
| M13 | Downloads have an in-page or email alternative | Medium |
| M14 | Worst case content checks passed for every target language | Medium |
| M15 | Locale price, date and plural formatting via Intl APIs | Medium |
| M16 | RTL layout verified for Arabic markets | Medium (High if Arabic market is active) |
| M17 | Consent banner does not cover the CTA on mobile | Medium |
| M18 | Real device test log updated within the last release | Low |

Score: Critical 10 points, High 5, Medium 2, Low 1 per passed item; report the percentage of available points and every failed Critical and High item.

## 8. Handoffs

| Situation | Hand off to | Pass |
|-----------|-------------|------|
| Code changes to theme, checkout or forms | site-engineer | Failed matrix cells, code snippets above, acceptance tests |
| Events missing or duplicated in IAB sessions | measurement | User agent split of capture rate, event IDs, consent rate |
| Destination settings, ad previews, browser add-ons | meta-ads, tiktok-ads, linkedin-ads | Which placements send traffic, test results |
| Language, casing, RTL and local formats | creative-strategy (localization module) | Strings that broke, locale list |
| Payment method mix per market | offer-strategy, compliance | Wallet availability by app, failure rates |

## 9. Sources

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | iOS Privacy: Instagram and Facebook can track anything you do on any website in their in-app browser | Felix Krause | https://krausefx.com/blog/ios-privacy-instagram-and-facebook-can-track-anything-you-do-on-any-website-in-their-in-app-browser | 2022-08 | Script injection in Meta and TikTok IABs |
| 2 | Launching a new Chromium-based WebView for Android | Meta Engineering | https://engineering.fb.com/2022/09/30/android/launching-a-new-chromium-based-webview-for-android/ | 2022-09-30 | Facebook Android IAB engine |
| 3 | How we use autofill | Meta Help Center | https://www.meta.com/help/meta-pay/1896636927418202/ | n.d. | Meta autofill of contact and payment details in the IAB |
| 4 | Meta updates login with Facebook | Social Media Today | https://www.socialmediatoday.com/news/meta-updates-login-with-facebook/829135/ | n.d. | iOS login fast app switch |
| 5 | Changeset 246056: Apple Pay payment APIs disabled in web views with injected user scripts | WebKit | https://trac.webkit.org/r246056 | 2019 | Apple Pay unavailable in script injected web views |
| 6 | Mobile app integration (Apple Pay in WKWebView) | Ezypay developer docs | https://developer.ezypay.com/docs/mobile-app-integration | n.d. | Practical effect of user scripts on ApplePaySession |
| 7 | Adding support for Google Pay within Android WebView | Google Developers Blog | https://developers.googleblog.com/en/adding-support-for-google-pay-within-android-webview/ | 2025-05-28 | WebView 137, Play services 25.18.30, host app opt in |
| 8 | Using Android WebView (Google Pay API) | Google Pay docs | https://developers.google.com/pay/api/android/guides/recipes/using-android-webview | n.d. | Payment Request disabled by default in WebView |
| 9 | OAuth 2.0 policies (embedded web views) | Google Identity | https://developers.google.com/identity/protocols/oauth2/policies | n.d. | Google sign-in blocked in embedded web views (enforced since 2021) |
| 10 | Donation options for in-app browsers | Fundraise Up | https://fundraiseup.com/support/app-browsers | n.d. | Popup based payment methods fail in IABs |
| 11 | The pitfalls of in-app browsers | Frontend Masters | https://frontendmasters.com/blog/the-pitfalls-of-in-app-browsers/ | 2024-07 | Retest of Instagram IAB behavior |
| 12 | Deep links in Instagram and Facebook in-app browsers | WarpLink | https://warplink.app/blog/deep-linking-in-app-browsers | 2025 to 2026 | Blocked automatic app launches (vendor blog) |
| 13 | How to disable the in-app browser (iPhone and Android, 2026) | u2l.ai | https://u2l.ai/blog/how-to-disable-in-app-browser | 2026 | Per app settings (vendor blog, unverified) |
| 14 | WebKit blog posts on full third-party cookie blocking (2020) and inspecting web content in apps (2023) | WebKit | https://webkit.org/blog/ | 2020-03, 2023-03 | WKWebView cookie rules; isInspectable |
| 15 | Understanding SC 2.5.8 Target Size (Minimum) | W3C WAI | https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html | 2023-10 | 24 by 24 px minimum |
| 16 | Skills repository (mobile-native and break-ui skills) | Emil Kowalski | Shared by the human; local copy reviewed 2026-10-08 | 2026 | Idea source for platform-layer fixes and worst case data testing |
