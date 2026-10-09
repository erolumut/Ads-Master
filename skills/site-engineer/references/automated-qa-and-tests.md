# Automated QA and Tests

> The automated checks behind release QA and launch QA, with copy paste Playwright templates for ecommerce and lead gen. Tool versions as of 2026-10: Playwright 1.64 (2026-10-07), Lighthouse 13 (since 2025-10-10; PageSpeed Insights since 2025-10-20), Shopify CLI 4.9. Pin versions in `package.json` and update deliberately.

## 1. The check stack (cheapest first)

| Layer | Tool | Runs | Blocks release when |
|-------|------|------|---------------------|
| Static | `shopify theme check --fail-level error`, ESLint, Stylelint, `tsc --noEmit`, PHP lint (`php -l`), PHPCS for WordPress | Every commit | Any error |
| Build | `next build`, theme push with `--strict`, `npm ci --ignore-scripts` then build | Every PR | Build fails |
| Smoke e2e | Playwright: home, collection, PDP, add to cart, cart, checkout handoff, lead form; account flows (signup, login, logout, password reset, test mode payment) on staging or preview with a mail catcher | Every preview, before every publish, after publish (read only); account flows before the first paid launch and on every auth, email or payment change | Any failure on desktop or mobile project |
| Tracking | Playwright network assertions for pixel and analytics events, consent states | Every L2 and L3 release | Missing, duplicated or wrong value events |
| Visual | Playwright `toHaveScreenshot` or a visual service (Percy, Chromatic, Argos, Applitools) | Every L1 to L4 release | Unexplained diff |
| Accessibility | `@axe-core/playwright` on changed templates | Every L1 to L4 release | New serious or critical violations |
| Performance | Lighthouse CI with assertions; PSI and CrUX API for field data | Every L1 to L4 release; weekly on live | Budget breach without approved exception |
| Links and redirects | Link checker (lychee, linkinator, or the Playwright crawler below) | Every release touching navigation or URLs; weekly on live | New 4xx, 5xx or chains over 1 hop |
| Structured data | JSON-LD extraction test; Rich Results Test for samples | Every PDP or template release | Parse errors, missing Product fields, price mismatch |
| Security | Secret scan (gitleaks or trufflehog), dependency audit (`npm audit`, `osv-scanner`), headers check | Every PR | Secrets, critical vulnerabilities with a fix available |

## 2. Project setup

```bash
npm i -D @playwright/test@1.64 @axe-core/playwright
npx playwright install --with-deps chromium webkit
```

Folder layout (inside the client repo, proposed as a diff):

```
qa/
  playwright.config.ts
  fixtures.ts
  helpers/price.ts
  tests/smoke.ecommerce.spec.ts
  tests/smoke.leadgen.spec.ts
  tests/smoke.account.spec.ts
  tests/tracking.spec.ts
  tests/utm-redirects.spec.ts
  tests/visual.spec.ts
  tests/a11y.spec.ts
  tests/structured-data.spec.ts
  tests/links.spec.ts
lighthouserc.json
```

## 3. `qa/playwright.config.ts`

```ts
import { defineConfig, devices } from '@playwright/test';

const BASE_URL = process.env.BASE_URL ?? 'http://127.0.0.1:9292'; // shopify theme dev default port

export default defineConfig({
  testDir: './tests',
  timeout: 60_000,
  expect: { timeout: 10_000 },
  fullyParallel: true,
  retries: process.env.CI ? 1 : 0,
  reporter: [['html', { open: 'never' }], ['json', { outputFile: 'qa-results.json' }]],
  use: {
    baseURL: BASE_URL,
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
    locale: process.env.QA_LOCALE ?? 'en-US',
  },
  projects: [
    { name: 'desktop-chrome', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile-safari', use: { ...devices['iPhone 13'] } },
    { name: 'mobile-android', use: { ...devices['Pixel 7'] } },
  ],
});
```

Notes:
- Emulation is not a phone. It catches layout and flow regressions, not iOS keyboard, toolbar, safe area or in-app browser behavior ([Mobile web polish](mobile-web-polish.md)).
- Do not put secrets in `use.extraHTTPHeaders`: those headers go to every host the page calls, including third party tags. Add protection bypass headers only for the preview origin (fixture below).

## 4. `qa/fixtures.ts` (preview access, consent, console errors)

```ts
import { test as base, expect } from '@playwright/test';

const ORIGIN = new URL(process.env.BASE_URL ?? 'http://127.0.0.1:9292').origin;
const FIRST_PARTY = [new URL(ORIGIN).hostname, ...(process.env.QA_FIRST_PARTY_HOSTS ?? '').split(',').filter(Boolean)];

export const test = base.extend<{ errors: string[] }>({
  context: async ({ context }, use) => {
    // Headers only for our origin: QA marker (form handlers route QA submissions to a test inbox)
    // and the Vercel preview protection bypass secret from CI env. Never sent to third parties.
    const bypass = process.env.VERCEL_AUTOMATION_BYPASS_SECRET;
    await context.route((url) => url.origin === ORIGIN, (route) => {
      const headers = { ...route.request().headers(), 'x-qa-test': '1' };
      if (bypass) headers['x-vercel-protection-bypass'] = bypass;
      return route.continue({ headers });
    });
    await use(context);
  },
  page: async ({ page }, use) => {
    // Shopify unpublished theme: open the preview URL once to set the preview cookie; pb=0 hides the preview bar
    if (process.env.SHOPIFY_PREVIEW_URL) {
      const u = new URL(process.env.SHOPIFY_PREVIEW_URL);
      u.searchParams.set('pb', '0');
      await page.goto(u.toString());
    }
    // Password protected dev stores
    if (process.env.STORE_PASSWORD && (await page.locator('form[action*="/password"]').count())) {
      await page.locator('input[type="password"]').fill(process.env.STORE_PASSWORD);
      await page.locator('form[action*="/password"] button, form[action*="/password"] [type="submit"]').first().click();
    }
    await use(page);
  },
  errors: [async ({ page }, use) => {
    const errors: string[] = [];
    page.on('pageerror', (e) => errors.push(`pageerror: ${e.message}`));
    page.on('console', (m) => {
      if (m.type() !== 'error') return;
      const src = m.location().url;
      if (!src || FIRST_PARTY.some((h) => src.includes(h))) errors.push(`console: ${m.text()}`);
    });
    await use(errors);
    expect(errors, 'first party JS errors').toEqual([]);
  }, { auto: true }],
});

export { expect };

// Accept or reject consent through the CMP. Set selectors per project.
export async function setConsent(page, choice: 'accept' | 'reject') {
  const sel = choice === 'accept' ? process.env.QA_CONSENT_ACCEPT : process.env.QA_CONSENT_REJECT;
  if (!sel) return;
  const btn = page.locator(sel).first();
  if (await btn.isVisible().catch(() => false)) await btn.click();
}
```

## 5. `qa/helpers/price.ts`

```ts
// Parses "€1.234,56", "1,234.56 USD", "₺1.234,56", "1 234,56 €" to 1234.56
export function parsePrice(text: string): number {
  const cleaned = text.replace(/[^\d.,]/g, '');
  const lastComma = cleaned.lastIndexOf(',');
  const lastDot = cleaned.lastIndexOf('.');
  const decimalSep = lastComma > lastDot ? ',' : '.';
  const [intPart, decPart = ''] = decimalSep === ','
    ? [cleaned.slice(0, lastComma), cleaned.slice(lastComma + 1)]
    : [cleaned.slice(0, lastDot === -1 ? cleaned.length : lastDot), lastDot === -1 ? '' : cleaned.slice(lastDot + 1)];
  // "1.234" or "1.234.567": 3 digits after the last separator and no different separator before it = thousands
  const otherSep = decimalSep === ',' ? '.' : ',';
  if (decPart.length === 3 && !intPart.includes(otherSep)) return Number(cleaned.replace(/[.,]/g, ''));
  return Number(intPart.replace(/[.,]/g, '') + (decPart ? '.' + decPart : ''));
}
```

## 6. Template: ecommerce smoke test (`smoke.ecommerce.spec.ts`)

Works on Shopify themes out of the box (uses `/cart.js`); adapt the cart check for WooCommerce (Store API `/wp-json/wc/store/v1/cart`) or headless carts.

```ts
import { test, expect, setConsent } from '../fixtures';
import { parsePrice } from '../helpers/price';

const PDP = process.env.QA_PDP_PATH ?? '/products/qa-test-product';
const ADD = /add to cart|add to bag|in den warenkorb|sepete ekle|in winkelwagen|ajouter au panier/i;
const CHECKOUT = /check ?out|zur kasse|ödeme|afrekenen|paiement|commander/i;

test.describe('ecommerce smoke', () => {
  test('home, collection and PDP render', async ({ page }) => {
    for (const path of ['/', process.env.QA_COLLECTION_PATH ?? '/collections/all', PDP]) {
      const res = await page.goto(path);
      expect(res?.status(), path).toBeLessThan(400);
      await expect(page.locator('h1').first()).toBeVisible();
    }
  });

  test('add to cart, cart total, checkout handoff (stops before payment)', async ({ page }) => {
    await page.goto(PDP);
    await setConsent(page, 'accept');
    const priceText = await page.locator(process.env.QA_PRICE_SELECTOR ?? '[data-qa="price"], .price').first().innerText();
    const shownPrice = parsePrice(priceText);

    const add = page.getByRole('button', { name: ADD }).first();
    await expect(add).toBeEnabled();
    const addResponse = page.waitForResponse((r) => /\/cart\/add/.test(r.url()) && r.request().method() === 'POST');
    await add.click();
    expect((await addResponse).ok()).toBeTruthy();

    const cart = await (await page.request.get('/cart.js')).json(); // Shopify; shares cookies with the page
    expect(cart.item_count).toBeGreaterThan(0);
    expect(cart.items[0].final_line_price / 100).toBeCloseTo(shownPrice * cart.items[0].quantity, 2);

    await page.goto('/cart');
    await page.getByRole('button', { name: CHECKOUT }).or(page.getByRole('link', { name: CHECKOUT })).first().click();
    await page.waitForURL(/\/checkouts?\//, { timeout: 30_000 });
    // Never fill contact or payment fields in automated tests on a live store.
  });

  test('sold out product cannot be added', async ({ page }) => {
    test.skip(!process.env.QA_SOLD_OUT_PATH, 'set QA_SOLD_OUT_PATH to a hidden sold out QA product');
    await page.goto(process.env.QA_SOLD_OUT_PATH!);
    const add = page.getByRole('button', { name: ADD }).first();
    await expect(add).toBeDisabled();
  });
});
```

Test data rules: keep hidden QA products (not in sales channels feeds, `noindex`, excluded from search) for sold out, many variants, long names and sale states. Never run checkout submission on a live store in automation. A real test order on production is G3 and needs approval.

## 7. Template: lead gen form in test mode (`smoke.leadgen.spec.ts`)

Prerequisite (propose as a code diff, G1): the form handler recognizes QA submissions (header `x-qa-test: 1`, which the fixture sends only to your origin, or an `@example.com` address) and routes them to a test inbox, skipping CRM writes and conversion uploads. Without that, run this test against staging only.

```ts
import { test, expect, setConsent } from '../fixtures';

const FORM = process.env.QA_FORM_PATH ?? '/contact';
const ORIGIN = new URL(process.env.BASE_URL ?? 'http://127.0.0.1:3000').origin;

test('lead form submits, confirms, and leaks no PII', async ({ page }) => {
  // the fixture adds x-qa-test: 1 to every request to ORIGIN
  const outbound: string[] = [];
  page.on('request', (r) => { if (!r.url().startsWith(ORIGIN)) outbound.push(r.url() + ' ' + (r.postData() ?? '')); });

  await page.goto(FORM + '?utm_source=qa&utm_medium=test&utm_campaign=release-qa');
  await setConsent(page, 'accept');
  const email = `qa.release+${Date.now()}@example.com`;
  await page.getByLabel(/name|ad soyad|naam/i).first().fill('Aleksandra Wiśniewska-Kowalczyk');
  await page.getByLabel(/e-?mail|e-?posta/i).first().fill(email);
  const phone = page.getByLabel(/phone|telefon|telefoon/i).first();
  if (await phone.count()) await phone.fill('+90 555 000 00 00');
  const msg = page.getByLabel(/message|mesaj|bericht/i).first();
  if (await msg.count()) await msg.fill('Release QA test. Please ignore.');

  await page.getByRole('button', { name: /submit|send|get (a )?quote|request|gönder|verstuur/i }).first().click();
  await expect(page.getByText(/thank you|thanks|received|teşekkür|bedankt/i).first()).toBeVisible({ timeout: 20_000 });

  expect(page.url(), 'no email in URL').not.toMatch(/%40|@/);
  for (const req of outbound) {
    expect(decodeURIComponent(req), 'no raw email sent to third parties').not.toContain(email);
  }
});

test('validation errors are inline and announced', async ({ page }) => {
  await page.goto(FORM);
  await page.getByRole('button', { name: /submit|send|get (a )?quote|request/i }).first().click();
  const invalid = page.locator('[aria-invalid="true"]');
  await expect(invalid.first()).toBeVisible();
  // errors must be inline messages linked to fields, not toasts
  const describedBy = await invalid.first().getAttribute('aria-describedby');
  expect(describedBy, 'error message linked with aria-describedby').toBeTruthy();
});
```

Hashed identifiers for enhanced conversions or CAPI are allowed in outbound requests by design; this test only flags raw addresses. Coordinate the rule set with `measurement`.

## 7b. Account flow smoke tests (`smoke.account.spec.ts`)

A paid click that cannot sign up, log in, pay or reset a password is spend with no way back. Run these flows on staging or on a preview whose email goes to a mail catcher and whose payments run in test mode. On production run only read only checks (pages render, forms load) unless the human approves a test account: creating accounts and sending emails on production are writes. These tests are the proof for the pre-spend gate in [Launch QA for ads](launch-qa-for-ads.md) section 11.

| Flow | Assert | Common breakage |
|------|--------|-----------------|
| Signup with email verification | Verification email arrives within 60 s; its link points at this environment and works once; the unverified state behaves as designed; resend works and is rate limited; signing up again with the same address shows a neutral message | Email never sent or sent from an unauthenticated domain; link points at localhost or a preview host; signup started in an in-app browser but the link opens the default browser, so the session lands elsewhere |
| Login | Right password logs in; a wrong password shows one generic message (never "no account with this email"); repeated failures hit the rate limit or a challenge | Account enumeration; no rate limit on login |
| Logout | Session cookie cleared and the server session revoked; back button and reload do not show account pages; the old session token is rejected by the API | Client only logout that leaves the server session valid |
| Password reset | Request shows the same neutral message for known and unknown addresses; the email arrives; the link works once and expires; the old password is rejected and the new one works; other sessions are signed out where the product promises it | Token consumed when the link is opened, so mail scanners burn it (rules below); link never expires; old password still accepted |
| Magic link (if used) | Works once, expires, signs in the device that asked for it; a typed code fallback exists | Opens in the default browser instead of the in-app browser where the user started, so the visitor never gets signed in where they were [Practitioner consensus] |
| Account deletion (if offered) | Confirmation step; login fails afterwards; personal data removed or anonymized as the privacy policy says; confirmation email sent; active subscriptions cancelled | Deleted user still gets marketing email; subscription keeps billing |
| Payment in test mode | Success; a declined card shows a clear inline error and keeps the cart; a 3DS challenge completes, and a failed challenge returns to checkout with a message; the order or subscription record and the purchase event exist exactly once | Decline clears the form; the 3DS frame is blocked by CSP or breaks inside in-app browsers; purchase event fires on a decline |

Test data and safety rules:
- Mail goes to a catcher, never to a real inbox: Mailpit (SMTP on port 1025, web UI and API on 8025 by default) when the app sends over SMTP, or the email provider's sandbox or test inbox, read through its API, when the app sends through an API. Use reserved domains (`example.com`, `.test`) and never a real customer address.
- Payments use the provider's test mode and test cards, on staging or a development store. Stripe, for example, documents `4242 4242 4242 4242` (succeeds), `4000 0000 0000 0002` (generic decline) and `4000 0027 6000 3184` (requires 3DS authentication on every payment) [Official, verify on the provider's testing page]; Adyen, Mollie, iyzico and PayTR publish their own. Never switch a live store's payments to test mode while it takes traffic: real customers' orders fail.
- One time tokens (verification, reset, magic link) are consumed by a POST after a user action, never by the GET or HEAD that opens the link. Corporate mail scanners such as Microsoft Defender Safe Links open links before the user does, and products that consume tokens on open report "invalid or expired link" for those users [Practitioner consensus, multiple vendor reports].
- Prove expiry where time is cheap: a server unit test on the token lifetime, or staging with a short lifetime and the expiry test below. Never wait out a production lifetime in e2e.

Minimal outline for password reset (it signs up a fresh account first, so the old password is known on every run):

```ts
import { randomUUID } from 'node:crypto';
import type { APIRequestContext, Page } from '@playwright/test';
import { test, expect } from '../fixtures';

// Staging or preview only, with the app's SMTP pointed at Mailpit. API schema of your version: <MAILPIT_URL>/api/v1/
const MAILPIT = process.env.MAILPIT_URL ?? 'http://127.0.0.1:8025';
const ORIGIN = new URL(process.env.BASE_URL ?? 'http://127.0.0.1:3000').origin;
const PATH = {
  signup: process.env.QA_SIGNUP_PATH ?? '/signup',
  login: process.env.QA_LOGIN_PATH ?? '/login',
  forgot: process.env.QA_FORGOT_PATH ?? '/forgot-password',
};
const VERIFY_LINK = /https?:\/\/[^\s"'<>]*verif[^\s"'<>]*/i;
const RESET_LINK = /https?:\/\/[^\s"'<>]*reset[^\s"'<>]*/i;

// One fresh account per worker: reserved domain, caught by Mailpit, never a real customer
const email = `qa.account+${Date.now()}-${process.pid}@example.test`;
const oldPassword = `Qa-old-${randomUUID()}`;
const newPassword = `Qa-new-${randomUUID()}`;

test.describe.configure({ mode: 'serial' });

// First link matching `pattern` in an email to `to` received after `since` (runner and Mailpit share a clock)
async function mailLink(request: APIRequestContext, to: string, since: number, pattern: RegExp): Promise<string> {
  let link = '';
  await expect.poll(async () => {
    const res = await request.get(`${MAILPIT}/api/v1/search`, { params: { query: `to:"${to}"` } });
    const { messages = [] } = (await res.json()) as { messages?: Array<{ ID: string; Created: string }> };
    for (const m of messages.filter((x) => Date.parse(x.Created) >= since)) {
      const msg = await (await request.get(`${MAILPIT}/api/v1/message/${m.ID}`)).json();
      link = `${msg.HTML ?? ''} ${msg.Text ?? ''}`.replace(/&amp;/g, '&').match(pattern)?.[0] ?? '';
      if (link) break;
    }
    return link;
  }, { message: `email to ${to} with a link matching ${pattern}`, timeout: 60_000 }).not.toBe('');
  expect(new URL(link).origin, 'link points at this environment, not localhost or another host').toBe(ORIGIN);
  return link;
}

async function requestReset(page: Page, address = email): Promise<void> {
  await page.goto(PATH.forgot);
  await page.getByLabel(/e-?mail/i).first().fill(address);
  await page.getByRole('button', { name: /reset|send/i }).click();
}

async function logIn(page: Page, password: string): Promise<void> {
  await page.goto(PATH.login);
  await page.getByLabel(/e-?mail/i).first().fill(email);
  await page.locator('input[type="password"]').first().fill(password);
  await page.getByRole('button', { name: /log ?in|sign ?in/i }).click();
}

test('signup: verification email arrives and its link works', async ({ page, request }) => {
  const since = Date.now();
  await page.goto(PATH.signup);
  await page.getByLabel(/e-?mail/i).first().fill(email);
  for (const field of await page.locator('input[type="password"]').all()) await field.fill(oldPassword);
  await page.getByRole('button', { name: /sign ?up|create account|register/i }).click();
  await page.goto(await mailLink(request, email, since, VERIFY_LINK));
  await expect(page.getByText(/verified|confirmed/i).first()).toBeVisible();
});

test('password reset: neutral message, link works once, old password rejected', async ({ page, request }) => {
  // Same message for an unknown and a known address (typed address masked): no account enumeration
  const neutral = page.getByText(/if an account exists|check your (e-?mail|inbox)/i).first();
  const masked = async (): Promise<string> => (await neutral.innerText()).replace(/\S+@\S+/g, '<email>');
  await requestReset(page, `qa.nobody+${Date.now()}@example.test`);
  await expect(neutral).toBeVisible();
  const unknownText = await masked();
  const since = Date.now();
  await requestReset(page);
  await expect.poll(masked).toBe(unknownText);
  const link = await mailLink(request, email, since, RESET_LINK);
  expect(link, 'no email address in the reset URL').not.toMatch(/%40|@/);

  // Opening the link must not burn the token: mail scanners send HEAD and GET before the user clicks
  await request.fetch(link, { method: 'HEAD' });
  await page.goto(link);
  await page.goto(link);
  const fields = page.locator('input[type="password"]'); // new password and its confirmation; a "Show password" button can match getByLabel
  await expect(fields.first()).toBeVisible();
  for (const field of await fields.all()) await field.fill(newPassword);
  await page.getByRole('button', { name: /reset|save|update|change/i }).click();
  await expect(page.getByText(/password (has been )?(reset|updated|changed)/i).first()).toBeVisible();

  // Single use: the same link must not open a working form again
  await page.goto(link);
  await expect(page.getByText(/expired|invalid|already used/i).first()).toBeVisible();
  await expect(page.locator('input[type="password"]')).toHaveCount(0);

  await logIn(page, oldPassword);
  await expect(page.getByText(/incorrect|invalid|wrong/i).first()).toBeVisible();
  await logIn(page, newPassword);
  await expect(page).not.toHaveURL(new RegExp(PATH.login));
});

test('password reset link expires', async ({ page, request }) => {
  const ttl = Number(process.env.QA_RESET_TTL_SECONDS ?? 0); // staging only, a short lifetime such as 60
  test.skip(!ttl, 'set a short reset token lifetime on staging and QA_RESET_TTL_SECONDS');
  test.setTimeout((ttl + 120) * 1_000);
  const since = Date.now();
  await requestReset(page);
  const link = await mailLink(request, email, since, RESET_LINK);
  await page.waitForTimeout((ttl + 5) * 1_000); // allowed exception (section 17): server time cannot be faked from the browser
  await page.goto(link);
  await expect(page.getByText(/expired|invalid/i).first()).toBeVisible();
  await expect(page.locator('input[type="password"]')).toHaveCount(0);
});
```

Notes:
- If a rejected login answers with HTTP 401, Chromium logs "Failed to load resource" as a console error and the auto `errors` fixture (section 4) fails the test. Allow that one message in the fixture for this spec instead of switching the fixture off.
- Run the file on one desktop and one mobile project, not all three: each worker creates an account. Replace the copy regexes with `data-qa` attributes as soon as the product has them (section 17).
- Logout, magic link, deletion and payment follow the same pattern: act in the page, read the mail catcher or the payment provider's test dashboard, assert the record and the event exist exactly once.

## 8. Template: tracking assertions (`tracking.spec.ts`)

```ts
import { test, expect, setConsent } from '../fixtures';

type Hit = { vendor: string; event: string; url: string; body: string };
const matchers: Array<[string, RegExp, (url: URL, body: string) => string | null]> = [
  ['meta', /facebook\.com\/tr/, (u) => u.searchParams.get('ev')],
  ['ga4', /\/g\/collect/, (u, b) => u.searchParams.get('en') ?? (b.match(/en=([^&\s]+)/)?.[1] ?? null)],
  ['tiktok', /analytics\.tiktok\.com\/api\/v2\/pixel/, (_u, b) => b.match(/"event":"([^"]+)"/)?.[1] ?? null],
];

function collect(page): Hit[] {
  const hits: Hit[] = [];
  page.on('request', (r) => {
    for (const [vendor, re, ev] of matchers) {
      if (!re.test(r.url())) continue;
      const body = r.postData() ?? '';
      const event = ev(new URL(r.url()), body);
      if (event) hits.push({ vendor, event, url: r.url(), body });
    }
  });
  return hits;
}

test('add to cart fires once per vendor, with dedup id for Meta', async ({ page }) => {
  const hits = collect(page);
  await page.goto(process.env.QA_PDP_PATH ?? '/products/qa-test-product');
  await setConsent(page, 'accept');
  await page.getByRole('button', { name: /add to cart|add to bag/i }).first().click();
  await page.waitForTimeout(3_000); // allow batched beacons to flush
  const atc = (v: string, names: string[]) => hits.filter((h) => h.vendor === v && names.includes(h.event));
  expect(atc('meta', ['AddToCart'])).toHaveLength(1);
  expect(new URL(atc('meta', ['AddToCart'])[0].url).searchParams.get('eid'), 'Meta event_id for CAPI dedup').toBeTruthy();
  expect(atc('ga4', ['add_to_cart']).length).toBeLessThanOrEqual(1);
});

test('reject consent: no marketing pixels fire', async ({ page }) => {
  const hits = collect(page);
  await page.goto('/');
  await setConsent(page, 'reject');
  await page.reload();
  await page.waitForTimeout(3_000);
  expect(hits.filter((h) => h.vendor !== 'ga4'), 'marketing pixels after reject').toEqual([]);
  // GA4 cookieless pings under consent mode may be expected; confirm the rule with measurement
});
```

Endpoints change; when a vendor moves to first party or server side collection (Google tag gateway, server side GTM), point the matcher at the first party path. Agree event names, values and dedup keys with `measurement` (MEASUREMENT.md is the source of truth).

## 9. Template: UTMs and click IDs survive redirects (`utm-redirects.spec.ts`)

```ts
import { test, expect } from '../fixtures';

const PARAMS = 'utm_source=qa&utm_medium=cpc&utm_campaign=launch_q4&gclid=QA_GCLID&fbclid=QA_FBCLID&ttclid=QA_TTCLID&msclkid=QA_MSCLKID';
const URLS = (process.env.QA_LANDING_PATHS ?? '/').split(',');

for (const path of URLS) {
  test(`params preserved: ${path}`, async ({ page, request }) => {
    // 1. Redirect chain without following
    let url = new URL(path + (path.includes('?') ? '&' : '?') + PARAMS, process.env.BASE_URL).toString();
    const hops: string[] = [];
    for (let i = 0; i < 5; i++) {
      const res = await request.get(url, { maxRedirects: 0 });
      if (![301, 302, 303, 307, 308].includes(res.status())) break;
      url = new URL(res.headers()['location'], url).toString();
      hops.push(`${res.status()} -> ${url}`);
    }
    expect(hops.length, `redirect hops: ${hops.join(' | ')}`).toBeLessThanOrEqual(1);
    // 2. Final browser URL still carries every parameter
    await page.goto(path + (path.includes('?') ? '&' : '?') + PARAMS);
    const final = new URL(page.url());
    for (const key of ['utm_source', 'utm_medium', 'utm_campaign', 'gclid', 'fbclid', 'ttclid', 'msclkid']) {
      expect(final.searchParams.get(key), `${key} lost on ${final.pathname}`).not.toBeNull();
    }
  });
}
```

## 10. Template: visual regression (`visual.spec.ts`)

```ts
import { test, expect } from '../fixtures';

const PAGES = ['/', process.env.QA_COLLECTION_PATH ?? '/collections/all', process.env.QA_PDP_PATH ?? '/products/qa-test-product', '/cart'];

for (const path of PAGES) {
  test(`visual ${path}`, async ({ page }) => {
    await page.goto(path);
    await page.waitForLoadState('networkidle');
    await page.addStyleTag({ content: '*{caret-color:transparent!important} [data-qa-dynamic]{visibility:hidden!important}' });
    await expect(page).toHaveScreenshot(`${path.replace(/\W+/g, '_') || 'home'}.png`, {
      fullPage: true,
      animations: 'disabled',
      maxDiffPixelRatio: 0.01,
      mask: [page.locator('iframe'), page.locator('[data-qa-dynamic]'), page.locator('.reviews, [class*="review"]')],
    });
  });
}
```

Baselines: create them from the live site before the release (`npx playwright test visual --update-snapshots` against production, read only), then compare the preview. Run baselines and comparisons in the same environment (the official Playwright Docker image for the pinned version) because fonts and rendering differ across machines. Mask carousels, timers, reviews and personalization.

## 11. Template: accessibility (`a11y.spec.ts`)

```ts
import { test, expect } from '../fixtures';
import AxeBuilder from '@axe-core/playwright';
import fs from 'node:fs';

const BASELINE = 'qa/a11y-baseline.json'; // known violations accepted with a ticket
const known: Record<string, string[]> = fs.existsSync(BASELINE) ? JSON.parse(fs.readFileSync(BASELINE, 'utf8')) : {};

for (const path of ['/', process.env.QA_PDP_PATH ?? '/products/qa-test-product', '/cart', process.env.QA_FORM_PATH ?? '/contact']) {
  test(`axe ${path}`, async ({ page }) => {
    await page.goto(path);
    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa', 'wcag22aa'])
      .exclude('iframe')
      .analyze();
    const blocking = results.violations
      .filter((v) => v.impact === 'serious' || v.impact === 'critical')
      .filter((v) => !(known[path] ?? []).includes(v.id))
      .map((v) => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, help: v.helpUrl }));
    expect(blocking, JSON.stringify(blocking, null, 2)).toEqual([]);
  });
}
```

Automated checks find a minority of accessibility issues. Add keyboard checks for cart drawers, variant pickers, filters and forms (Tab order, Escape closes, focus returns) and hand pattern level fixes to `storefront-ux`.

## 12. Template: structured data and price parity (`structured-data.spec.ts`)

```ts
import { test, expect } from '../fixtures';
import { parsePrice } from '../helpers/price';

test('PDP Product JSON-LD parses and matches the visible price', async ({ page }) => {
  await page.goto(process.env.QA_PDP_PATH ?? '/products/qa-test-product');
  const blocks = await page.locator('script[type="application/ld+json"]').allTextContents();
  const nodes = blocks.flatMap((t) => { const j = JSON.parse(t); return Array.isArray(j) ? j : j['@graph'] ?? [j]; });
  const products = nodes.filter((n) => [].concat(n['@type']).includes('Product') || [].concat(n['@type']).includes('ProductGroup'));
  expect(products.length, 'exactly one Product or ProductGroup entity').toBe(1);
  const p = products[0];
  expect(p.name).toBeTruthy();
  expect(p.image).toBeTruthy();
  const offers = [].concat(p.offers ?? p.hasVariant?.flatMap((v) => v.offers) ?? []);
  expect(offers.length).toBeGreaterThan(0);
  const visible = parsePrice(await page.locator(process.env.QA_PRICE_SELECTOR ?? '[data-qa="price"], .price').first().innerText());
  const ldPrices = offers.map((o) => Number(o.price ?? o.lowPrice));
  expect(ldPrices, `visible ${visible} vs JSON-LD ${ldPrices}`).toContain(visible);
  expect(offers.every((o) => o.priceCurrency && o.availability)).toBeTruthy();
});
```

Structured data strategy and rich result eligibility belong to `seo`; this test only guards against regressions and price drift (the misrepresentation risk shared with `commerce-feeds`).

## 13. Template: changed page link check (`links.spec.ts`)

```ts
import { test, expect } from '../fixtures';

test('no broken internal links or chains on key pages', async ({ page, request }) => {
  const start = (process.env.QA_LINK_PAGES ?? '/').split(',');
  const origin = new URL(process.env.BASE_URL!).origin;
  const seen = new Set<string>(); const problems: string[] = [];
  for (const path of start) {
    await page.goto(path);
    const hrefs = await page.locator('a[href]').evaluateAll((as) => as.map((a) => (a as HTMLAnchorElement).href));
    for (const href of hrefs) {
      const u = new URL(href);
      if (u.origin !== origin || seen.has(u.pathname)) continue;
      seen.add(u.pathname);
      const res = await request.get(u.pathname, { maxRedirects: 0 });
      if (res.status() >= 400) problems.push(`${res.status()} ${u.pathname} (from ${path})`);
      if ([301, 302, 307, 308].includes(res.status())) problems.push(`redirect ${u.pathname} -> ${res.headers()['location']} (update the link)`);
    }
  }
  expect(problems, problems.join('\n')).toEqual([]);
});
```

For full site crawls use lychee or linkinator in CI, or hand to `seo` for crawler tools.

## 14. Lighthouse CI (`lighthouserc.json`)

```json
{
  "ci": {
    "collect": {
      "url": ["${BASE_URL}/", "${BASE_URL}/collections/all", "${BASE_URL}/products/qa-test-product"],
      "numberOfRuns": 3,
      "settings": { "preset": "desktop" }
    },
    "assert": {
      "assertions": {
        "categories:performance": ["warn", { "minScore": 0.6 }],
        "categories:accessibility": ["error", { "minScore": 0.9 }],
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["warn", { "maxNumericValue": 300 }],
        "resource-summary:script:size": ["warn", { "maxNumericValue": 450000 }],
        "resource-summary:third-party:count": ["warn", { "maxNumericValue": 30 }]
      }
    },
    "upload": { "target": "filesystem", "outputDir": "qa/lhci" }
  }
}
```

Run a mobile config too (default Lighthouse settings are mobile emulation). Lighthouse 13 removed many legacy audit IDs from reports and JSON (for example `render-blocking-resources`, `uses-optimized-images`, `third-party-summary`, `layout-shifts`, `server-response-time`) and replaced them with insight audits (`render-blocking-insight`, `image-delivery-insight`, `third-parties-insight`, `cls-culprits-insight`, `document-latency-insight`, `lcp-discovery-insight` and others). Scripts and assertions that read old IDs break silently or fail; assert on metrics and resource summaries, and update any parser [Official, 2025-10-10]. Scoring did not change.

Field data (what Google and users see): CrUX API or PageSpeed Insights API.

```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=$URL&strategy=mobile&category=performance&key=$PSI_API_KEY" \
  | jq '{lcp: .loadingExperience.metrics.LARGEST_CONTENTFUL_PAINT_MS.percentile, inp: .loadingExperience.metrics.INTERACTION_TO_NEXT_PAINT.percentile, cls: .loadingExperience.metrics.CUMULATIVE_LAYOUT_SHIFT_SCORE.percentile, lighthouse: .lighthouseResult.lighthouseVersion}'
```

The API key lives in the environment; never paste it into outputs.

## 15. CI workflow (GitHub Actions, propose as a diff; the human enables it)

```yaml
name: preview-qa
on:
  deployment_status:      # Vercel and Netlify post deployment statuses to GitHub
jobs:
  qa:
    if: github.event.deployment_status.state == 'success'
    runs-on: ubuntu-latest
    timeout-minutes: 30
    env:
      BASE_URL: ${{ github.event.deployment_status.environment_url }}
      VERCEL_AUTOMATION_BYPASS_SECRET: ${{ secrets.VERCEL_AUTOMATION_BYPASS_SECRET }}
      QA_PDP_PATH: /products/qa-test-product
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: 22 }
      - run: npm ci --ignore-scripts
      - run: npx playwright install --with-deps chromium webkit
      - run: npx playwright test -c qa/playwright.config.ts
      - run: npx @lhci/cli autorun
      - uses: actions/upload-artifact@v4
        if: always()
        with: { name: qa-report, path: playwright-report }
```

Shopify variant: a job that runs `shopify theme push --development --development-context "pr-${{ github.event.number }}" --json` with a Theme Access password from secrets, reads `preview_url`, then runs the suite with `SHOPIFY_PREVIEW_URL`. A CI job that pushes themes is a G2 automation the human must approve; it must never use `--live`, `--allow-live` or `--publish`.

Pin action versions to commit SHAs in high security repos, and keep `--ignore-scripts` on installs (supply chain worms in 2025 and 2026 ran in install hooks; see [Security review](security-review.md)).

## 16. AI assisted test authoring

- Playwright Test Agents (since 1.56, 2025-10): `npx playwright init-agents --loop=claude` generates planner, generator and healer agent definitions. Planner explores and writes a Markdown plan, generator writes tests, healer reruns and repairs failing tests. Regenerate definitions after each Playwright upgrade [Official].
- Healer risk: a healer can make a failing test pass by weakening the assertion or skipping the test when the product is actually broken. Review every healed diff; a test changed from failing to skipped is a release blocker until explained.
- Playwright MCP and Chrome DevTools MCP let an agent drive a browser for exploratory QA ([Tools](tools-api-mcp.md)). Use them to explore, then commit deterministic tests; do not treat an agent's exploratory pass as the release gate.
- Useful recent APIs: `page.consoleMessages()`, `page.pageErrors()`, `page.requests()` (1.56) for quick diagnostics; `locator.visible()` (1.63) instead of `:visible`; test `lock` (1.63) for tests sharing one external resource such as a test inbox; `page.webmcp` (1.64, experimental) to test WebMCP tools a page registers for AI agents.

## 17. Flake policy

| Rule | Why |
|------|-----|
| A flaky smoke test is a failing smoke test until fixed or quarantined with an owner and date | Ignored flakes hide real breakage |
| Prefer role and label locators (`getByRole`, `getByLabel`) and `data-qa` attributes over CSS classes | Theme updates rename classes |
| Wait for responses or states, not timeouts; the only `waitForTimeout` calls allowed are the beacon flush in tracking tests and the token lifetime wait in the reset expiry test (section 7b) | Timing based tests flake |
| Third party widgets (reviews, chat, upsell apps) are masked or excluded from assertions | Vendors change without notice |
| Run against preview and live separately; live runs are read only | Avoid side effects on production |
