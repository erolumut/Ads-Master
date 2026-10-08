# Landing Page Build Recipes (code level)

> The agent works inside real codebases. It proposes landing pages and test variants as code diffs that a human reviews and deploys. It never pushes, merges, publishes themes or deploys. Every recipe below is server rendered, fast, accessible and tracked.

## 1. Detect the stack first

| Signal in repo | Stack | Where landing pages live |
|----------------|-------|--------------------------|
| `package.json` with `next` | Next.js | `app/` (App Router) or `pages/` (Pages Router) |
| `layout/theme.liquid`, `sections/`, `templates/*.json` | Shopify Online Store 2.0 theme | `templates/page.<name>.json` + `sections/*.liquid` |
| `wp-content/`, `theme.json`, `functions.php` | WordPress | Block theme `templates/`, `patterns/`, or page builder data in the database |
| Webflow export or no code in repo | Webflow | Designer and CMS (agent writes specs and custom code embeds) |
| `astro.config.*`, `nuxt.config.*`, `svelte.config.*`, `gatsby-config.*` | Other SSR or SSG | Framework pages directory |
| Hydrogen (`@shopify/hydrogen`) | Shopify headless | `app/routes/` |

Procedure:
1. Read `package.json` or theme files; note framework version (APIs differ by major version).
2. Find existing LP templates, design tokens and components; reuse them.
3. Find tracking: GTM container snippet, `dataLayer` usage, analytics SDKs, consent manager.
4. Find the testing setup: feature flag SDK (GrowthBook, PostHog, LaunchDarkly, Optimizely, Statsig), client-side snippet (VWO, AB Tasty, Convert, Kameleoon), Shopify Rollouts, or none.
5. Run the dev server or build locally if allowed, to verify changes.

## 2. Component checklist (every LP)

| Component | Must have |
|-----------|-----------|
| Hero | `<h1>` with matched headline, subhead, hero `<img>` with width, height, `fetchpriority="high"`, no lazy; primary CTA as `<a>` or `<button>`; proof strip |
| Proof strip | Rating with count (from real data source), logos as `<img>` with alt |
| Benefits | 3 to 6 items, semantic list |
| How it works | Ordered list, 3 steps |
| Testimonials | Real quotes with attribution; source of each quote recorded in the copy deck |
| Offer box | Price, inclusions, guarantee, CTA |
| FAQ | `<details><summary>` (no JS needed), FAQ content also visible to crawlers |
| Form | Labels, autocomplete, inputmode, server validation, honeypot, accessible errors, success state |
| Sticky mobile CTA | Appears after hero scrolls out; does not cover content or cookie banner; respects safe-area insets |
| Footer | Contact, policies, legal, no full nav on paid LPs |
| Tracking | `cta_click`, `form_start_custom`, `generate_lead` or ecommerce events, `experiment_viewed` with IDs |
| SEO controls | `noindex` on paid-only duplicates; canonical where needed |

## 3. Next.js (App Router) recipes

### 3.1 Server-rendered LP with allowlisted message match
```tsx
// app/lp/running/page.tsx  (Next.js 15+: searchParams is a Promise; in 14, it is a plain object)
import Image from 'next/image';
import type { Metadata } from 'next';
import copy from './copy.json'; // { "default": {...}, "flat-feet": {...} }
import { LeadOrShopCta } from './cta';

export const metadata: Metadata = {
  title: 'Running shoes for your stride | Brand',
  robots: { index: false, follow: true }, // paid-only page
};

type Variant = keyof typeof copy;

export default async function Page({ searchParams }: { searchParams: Promise<Record<string, string | undefined>> }) {
  const sp = await searchParams;
  const key = (sp.angle && sp.angle in copy ? sp.angle : 'default') as Variant;
  const c = copy[key];
  return (
    <main>
      <section className="hero">
        <h1>{c.h1}</h1>
        <p className="sub">{c.sub}</p>
        <Image src="/img/hero-runner.avif" alt={c.heroAlt} width={1200} height={1500}
               sizes="(max-width: 768px) 100vw, 50vw" priority />
        <LeadOrShopCta label={c.cta} href="/products/stride-1" variantKey={key} />
        <p className="proof">Rated 4.8 from 2,314 reviews</p>{/* replace with real data source */}
      </section>
      {/* benefits, how it works, reviews, offer, FAQ, final CTA */}
    </main>
  );
}
```
Notes:
- Using `searchParams` makes the route dynamic. For heavy traffic, prefer one static route per angle (`/lp/running/[angle]` with `generateStaticParams`) and point ads at those URLs.
- `priority` marks the hero image for preload; check the installed Next.js version's docs for the current prop name [Unverified for newest majors].

### 3.2 Edge assignment for an A/B test without flicker
```ts
// middleware.ts (renamed proxy.ts in newer Next.js majors; check the version) [Unverified naming]
import { NextResponse, type NextRequest } from 'next/server';

const EXP = { id: 'lp-running-hero-2026-10', variants: ['control', 'b'] as const, splitB: 50 };
const BOT = /bot|crawler|spider|crawling|preview|headless|lighthouse/i;

export function middleware(req: NextRequest) {
  const cookie = `exp_${EXP.id}`;
  const ua = req.headers.get('user-agent') || '';
  let v = req.cookies.get(cookie)?.value as (typeof EXP.variants)[number] | undefined;
  const isBot = BOT.test(ua);
  if (!v || !EXP.variants.includes(v)) {
    v = isBot ? 'control' : (crypto.getRandomValues(new Uint32Array(1))[0] % 100 < EXP.splitB ? 'b' : 'control');
  }
  const url = req.nextUrl.clone();
  url.pathname = `/lp/running/${v}`;           // static variant routes, cacheable
  const res = NextResponse.rewrite(url);       // visitor keeps the original URL
  if (!isBot) res.cookies.set(cookie, v, { path: '/', maxAge: 60 * 60 * 24 * 30, sameSite: 'lax' });
  return res;
}
export const config = { matcher: ['/lp/running'] };
```
```tsx
// app/lp/running/[variant]/exposure.tsx
'use client';
import { useEffect } from 'react';
export function Exposure({ experimentId, variantId }: { experimentId: string; variantId: string }) {
  useEffect(() => {
    const w = window as any;
    w.dataLayer = w.dataLayer || [];
    w.dataLayer.push({ event: 'experiment_viewed', experiment_id: experimentId, variant_id: variantId });
  }, [experimentId, variantId]);
  return null;
}
```
Rules: bots get control and no cookie (excluded from analysis by not firing exposure in headless contexts where possible); exposure fires once per page view, dedupe per user in analysis; the variant routes must be `noindex`. With a flag SDK (GrowthBook, PostHog, LaunchDarkly, Optimizely, Statsig), replace the random assignment with the SDK's server-side evaluation using a stable visitor ID cookie so analysis happens in that platform.

### 3.3 Lead form with a server action
```tsx
// app/lp/running/actions.ts
'use server';
export type State = { ok: boolean; error?: string };
export async function submitLead(_: State, fd: FormData): Promise<State> {
  if (fd.get('company_website')) return { ok: true };            // honeypot: pretend success
  const started = Number(fd.get('t0') || 0);
  if (Date.now() - started < 3000) return { ok: true };         // too fast, likely bot
  const email = String(fd.get('email') || '').trim();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return { ok: false, error: 'Enter a valid email, like name@company.com' };
  const res = await fetch(process.env.CRM_WEBHOOK_URL!, {
    method: 'POST', headers: { 'content-type': 'application/json' },
    body: JSON.stringify({ email, name: fd.get('name'), utm: fd.get('utm'), variant: fd.get('variant') }),
  });
  return res.ok ? { ok: true } : { ok: false, error: 'Something went wrong. Please try again or call us.' };
}
```
```tsx
// app/lp/running/lead-form.tsx
'use client';
import { useActionState, useEffect } from 'react';
import { submitLead, type State } from './actions';
export function LeadForm({ variant, utm }: { variant: string; utm: string }) {
  const [state, action, pending] = useActionState<State, FormData>(submitLead, { ok: false });
  useEffect(() => { if (state.ok) (window as any).dataLayer?.push({ event: 'generate_lead', form_id: 'lp-running', variant_id: variant }); }, [state.ok, variant]);
  if (state.ok) return <p role="status">Thanks. We will email your fitting guide within 5 minutes.</p>;
  return (
    <form action={action} noValidate data-track-form="lp-running">
      <label htmlFor="name">First name</label>
      <input id="name" name="name" autoComplete="given-name" required />
      <label htmlFor="email">Email</label>
      <input id="email" name="email" type="email" autoComplete="email" required aria-describedby={state.error ? 'err' : undefined} />
      <input type="text" name="company_website" tabIndex={-1} autoComplete="off" className="hp" aria-hidden="true" />
      <input type="hidden" name="t0" value={Date.now()} />
      <input type="hidden" name="utm" value={utm} /><input type="hidden" name="variant" value={variant} />
      {state.error && <p id="err" role="alert">{state.error}</p>}
      <button type="submit" disabled={pending}>{pending ? 'Sending...' : 'Get my fitting guide'}</button>
      <p className="micro">No spam. Unsubscribe anytime.</p>
    </form>
  );
}
```
`.hp { position:absolute; left:-9999px; }` hides the honeypot from people but not from bots. `useActionState` requires React 19 (Next.js 15+). The `t0` value renders on the server; that is acceptable for a time check. Coordinate the `generate_lead` event and CRM mapping with `measurement`.

## 4. Shopify (Online Store 2.0) recipes

### 4.1 Dedicated landing page template
```json
// templates/page.lp-running.json
{
  "layout": "theme",
  "sections": {
    "hero": {
      "type": "lp-hero",
      "settings": {
        "heading": "Running shoes for flat feet",
        "subheading": "Stability without the stiff feel. Free 60-day trial runs.",
        "cta_label": "Shop the Stride 1",
        "cta_link": "shopify://products/stride-1",
        "proof": "4.8 stars from 2,314 reviews"
      }
    },
    "main": { "type": "main-page", "settings": {} }
  },
  "order": ["hero", "main"]
}
```
Create one page per angle in Online Store > Pages, assign the template. Use an alternate layout without the main menu for dedicated paid LPs if the theme supports it (`"layout": "landing"` with `layout/landing.liquid`).

### 4.2 Hero section
```liquid
{% comment %} sections/lp-hero.liquid {% endcomment %}
<section class="lp-hero" aria-labelledby="lp-hero-{{ section.id }}">
  <div class="lp-hero__copy">
    <h1 id="lp-hero-{{ section.id }}">{{ section.settings.heading | escape }}</h1>
    {%- if section.settings.subheading != blank -%}<p class="lp-hero__sub">{{ section.settings.subheading | escape }}</p>{%- endif -%}
    <a class="button button--primary lp-hero__cta" href="{{ section.settings.cta_link }}"
       data-event="cta_click" data-cta="hero">{{ section.settings.cta_label | escape }}</a>
    {%- if section.settings.proof != blank -%}<p class="lp-hero__proof">{{ section.settings.proof | escape }}</p>{%- endif -%}
  </div>
  {%- if section.settings.image != blank -%}
    {{ section.settings.image | image_url: width: 1500
       | image_tag: loading: 'eager', fetchpriority: 'high', preload: true,
         sizes: '(min-width: 990px) 50vw, 100vw', widths: '375, 550, 750, 1100, 1500',
         alt: section.settings.image.alt | default: section.settings.heading }}
  {%- endif -%}
</section>
{% schema %}
{
  "name": "LP hero",
  "settings": [
    { "type": "text", "id": "heading", "label": "Heading" },
    { "type": "textarea", "id": "subheading", "label": "Subheading" },
    { "type": "image_picker", "id": "image", "label": "Hero image" },
    { "type": "text", "id": "cta_label", "label": "Button label", "default": "Shop now" },
    { "type": "url", "id": "cta_link", "label": "Button link" },
    { "type": "text", "id": "proof", "label": "Proof line (must be true and current)" }
  ],
  "presets": [{ "name": "LP hero" }]
}
{% endschema %}
```
Notes:
- Liquid does not reliably read arbitrary query parameters, and full-page caching serves the same HTML to everyone. Use one page per angle rather than parameter-driven copy.
- Review stars: render from product metafields server side instead of a blocking widget above the fold.
- Theme A/B test: duplicate the theme, apply the change, and run it in Shopify Rollouts (server-side split, RPV primary metric, no confidence intervals: compute significance yourself with [Experimentation statistics](experimentation-statistics.md)). Or use a theme testing app or platform with targeting and stats.
- Never publish a theme or change the live theme without human approval. Provide the diff and a preview link from the theme editor or CLI (`shopify theme dev` locally, or `shopify theme push --unpublished` only with approval).

### 4.3 Sticky add to cart (PDP) snippet logic
- Observe the main add to cart button with `IntersectionObserver`; show the sticky bar when it leaves the viewport.
- The sticky button submits the same product form (`form="product-form-{{ section.id }}"`), so variant selection stays consistent.
- Reserve space at the bottom of the page when the bar is visible to avoid covering content; include `padding-bottom: env(safe-area-inset-bottom)`.

## 5. WordPress recipes
- Build LPs with the block editor and a theme template without navigation: `templates/page-landing.html` in a block theme containing only a minimal header part, `core/post-content` and a minimal footer part.
- Register reusable sections as block patterns (`patterns/lp-hero.php`) so marketers edit text without breaking layout.
- Avoid heavy page builders on paid LPs; if the site uses one, audit its asset output with the speed checklist.
- Caching: A/B tests that vary HTML need cache variation (by cookie) or client-side swaps limited to below the fold. Server-side testing plugins exist for WordPress (for example Nelio A/B Testing) [Unverified current features].
- Forms: Gravity Forms, WPForms or similar; enable honeypot and server-side validation; send leads to CRM via native add-ons or webhooks.

## 6. Webflow recipes
- CMS collection "Landing pages" with fields: slug, H1, subhead, hero image, CTA label, CTA link, proof line, FAQ items (reference collection), noindex toggle. One item per angle gives message match at scale.
- Template page binds fields; set `noindex` via custom code in page settings when the toggle is on.
- Custom code embeds load in the order placed; put tracking in the site-wide head via GTM, defer everything else.
- Testing: Webflow's native optimization product or third-party tools [Unverified current features]; otherwise client-side tools with the flicker caveats in [Speed](speed-and-core-web-vitals.md).

## 7. Plain HTML skeleton (static hosting, any CMS custom template)
```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Running shoes for flat feet | Brand</title>
  <meta name="robots" content="noindex, follow">
  <link rel="preload" as="image" href="/img/hero-750.avif" imagesrcset="/img/hero-375.avif 375w, /img/hero-750.avif 750w, /img/hero-1200.avif 1200w" imagesizes="100vw" fetchpriority="high">
  <style>/* critical CSS only: layout, hero, button. Keep under about 14 KB */
    body{margin:0;font:16px/1.5 system-ui,sans-serif;color:#111}
    .hero{display:grid;gap:12px;padding:16px;max-width:1100px;margin:auto}
    .hero img{width:100%;height:auto;aspect-ratio:4/5;object-fit:cover}
    .cta{display:block;text-align:center;padding:14px 20px;min-height:48px;background:#0a5;color:#fff;font-weight:700;border-radius:8px;text-decoration:none}
    .cta:focus-visible{outline:3px solid #000;outline-offset:2px}
    .sticky{position:fixed;left:0;right:0;bottom:0;padding:8px 16px calc(8px + env(safe-area-inset-bottom));background:#fff;box-shadow:0 -2px 8px rgba(0,0,0,.1);transform:translateY(110%);transition:transform .2s}
    .sticky.show{transform:none}
  </style>
  <link rel="stylesheet" href="/css/lp.css" media="print" onload="this.media='all'">
</head>
<body>
  <main>
    <section class="hero">
      <h1>Running shoes for flat feet</h1>
      <p>Stability without the stiff feel. Free 60-day trial runs.</p>
      <img src="/img/hero-750.avif" srcset="/img/hero-375.avif 375w, /img/hero-750.avif 750w, /img/hero-1200.avif 1200w"
           sizes="100vw" width="750" height="938" alt="Runner on a trail wearing Stride 1 shoes" fetchpriority="high">
      <a class="cta" id="hero-cta" href="/products/stride-1" data-event="cta_click" data-cta="hero">Shop the Stride 1, $129</a>
      <p>4.8 stars from 2,314 reviews. Free returns.</p>
    </section>
    <!-- sections -->
    <section aria-labelledby="faq"><h2 id="faq">Questions</h2>
      <details><summary>What if they do not fit?</summary><p>Return or exchange free within 60 days, even if worn outside.</p></details>
    </section>
  </main>
  <div class="sticky" id="sticky" aria-hidden="true"><a class="cta" href="/products/stride-1" tabindex="-1" data-event="cta_click" data-cta="sticky">Shop the Stride 1</a></div>
  <script>
    window.dataLayer = window.dataLayer || [];
    document.addEventListener('click', function (e) {
      var el = e.target.closest('[data-event="cta_click"]');
      if (el) dataLayer.push({event: 'cta_click', cta_position: el.getAttribute('data-cta'), page_path: location.pathname});
    });
    var s = document.getElementById('sticky');
    new IntersectionObserver(function (en) {
      var hidden = !en[0].isIntersecting;
      s.classList.toggle('show', hidden); s.setAttribute('aria-hidden', String(!hidden));
      s.querySelector('a').tabIndex = hidden ? 0 : -1;
    }).observe(document.getElementById('hero-cta'));
  </script>
</body>
</html>
```
Replace the proof line and price with values from real data. Load GTM or analytics through the site's standard consent-aware snippet.

## 8. Tracking spec for LPs and variants (agree with `measurement`)

| Event | When | Parameters |
|-------|------|------------|
| `experiment_viewed` | Variant rendered to a user | `experiment_id`, `variant_id` |
| `cta_click` | Any primary CTA click | `cta_position` (hero, sticky, final), `page_path`, `variant_id` |
| `form_start_custom` | First field focus | `form_id` |
| `form_field_error` | Validation error | `form_id`, `field_name` |
| `generate_lead` | Server-confirmed lead | `form_id`, `variant_id`, `value` (if lead value agreed) |
| `view_item`, `add_to_cart`, `begin_checkout`, `purchase` | Ecommerce standard | GA4 ecommerce schema |
| `web_vitals` | LCP, INP, CLS measured | `metric_name`, `metric_value`, `metric_rating` |

Register `experiment_id`, `variant_id`, `cta_position` as GA4 custom dimensions (event scope). Never send personal data in event parameters.

## 9. Proposing a variant as a diff

Deliver variants as a patch the human can review:
```
ads-master/outputs/cro/YYYY-MM-DD_cro_variant-<test-id>.md
  - Hypothesis and test ID (EXPERIMENTS.md row)
  - Files changed (paths) and the unified diff, or the branch name if the human asked for a branch
  - Screenshots: control and variant at 390 x 844 and 1440 x 900
  - QA results (checklist below)
  - Rollout plan: tool, allocation, start date, stop rule
```
Do not commit, push, merge, deploy, publish themes or start tests in a live tool. If the human asks you to apply the diff locally, do so on the working tree only and say exactly what changed.

### Variant QA checklist
- [ ] Builds and type checks pass; no console errors.
- [ ] Control unchanged (diff touches only the variant path or flag branch).
- [ ] Assignment sticky; exposure event fires once; IDs match EXPERIMENTS.md.
- [ ] Mobile and desktop screenshots reviewed; in-app browser check for social traffic.
- [ ] LCP and CLS of variant not worse than control in lab test (same conditions).
- [ ] Accessibility checks (section 10) pass.
- [ ] Copy uses only approved claims; proof numbers sourced.
- [ ] Variant URLs `noindex` if separate.

## 10. Accessibility checklist for components (WCAG 2.2 AA essentials)
- Text contrast 4.5:1 (3:1 for large text); UI component and focus indicator contrast 3:1.
- Every input has a programmatic label; errors identified in text and linked with `aria-describedby`; `role="alert"` for submit errors.
- Keyboard: all CTAs and form controls reachable and operable; visible focus; no keyboard traps in modals; Escape closes dialogs.
- Target size at least 24 x 24 CSS px (WCAG 2.2 SC 2.5.8); aim for 44 x 44.
- Images have meaningful `alt`; decorative images `alt=""`.
- Headings in order (one `h1`); landmarks (`main`, `nav`, `footer`).
- Motion: respect `prefers-reduced-motion`; no auto-playing video with sound; carousels have pause.
- Do not rely on overlays or widgets to claim compliance; fix the source.

Automated checks catch only part of the issues; test keyboard flow and a screen reader (VoiceOver or NVDA) on the form and checkout path.

## 11. Performance guard in CI (optional, propose to the human)
```json
// lighthouserc.json
{
  "ci": {
    "collect": { "url": ["http://localhost:3000/lp/running"], "numberOfRuns": 3, "settings": { "preset": "mobile" } },
    "assert": {
      "assertions": {
        "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
        "cumulative-layout-shift": ["error", { "maxNumericValue": 0.1 }],
        "total-blocking-time": ["warn", { "maxNumericValue": 200 }],
        "categories:accessibility": ["error", { "minScore": 0.9 }]
      }
    }
  }
}
```

## 12. Playwright QA for variants (optional)
```js
// qa/variants.spec.js  run: BASE_URL=http://localhost:3000 npx playwright test qa/variants.spec.js
const { test, expect } = require('@playwright/test');
for (const v of ['control', 'b']) {
  test(`lp running ${v}`, async ({ browser }) => {
    const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true });
    await ctx.addCookies([{ name: 'exp_lp-running-hero-2026-10', value: v, url: process.env.BASE_URL }]);
    const page = await ctx.newPage();
    const errors = [];
    page.on('pageerror', (e) => errors.push(e.message));
    await page.goto(`${process.env.BASE_URL}/lp/running`);
    await expect(page.getByRole('heading', { level: 1 })).toBeVisible();
    await expect(page.locator('#hero-cta, [data-cta="hero"]').first()).toBeInViewport();
    await page.screenshot({ path: `qa-${v}-mobile.png`, fullPage: false });
    expect(errors).toEqual([]);
  });
}
```
