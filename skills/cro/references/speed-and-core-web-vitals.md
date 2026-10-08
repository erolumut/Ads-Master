# Speed and Core Web Vitals for Conversion

> Speed is a conversion lever and a cost lever: paid clicks that leave before the page renders are pure waste. Optimize for field data on real mobile devices, starting with landing pages that receive the most paid traffic.

## 1. Thresholds (75th percentile of field page loads)

| Metric | Good | Needs improvement | Poor | Measures |
|--------|------|-------------------|------|----------|
| LCP (Largest Contentful Paint) | 2.5 s or less | 2.5 to 4.0 s | over 4.0 s | Loading of the main content |
| INP (Interaction to Next Paint) | 200 ms or less | 200 to 500 ms | over 500 ms | Responsiveness to taps, clicks, keys |
| CLS (Cumulative Layout Shift) | 0.1 or less | 0.1 to 0.25 | over 0.25 | Visual stability |

INP replaced FID as a Core Web Vital on 12 March 2024 [Official, web.dev 2024-03]. Thresholds apply at p75 per device type [Official].

State of the web: July 2025 CrUX mobile data shows about 62% of pages with good LCP, 77% good INP and 81% good CLS [Study, 2025-07, secondary summary]. The 2025 Web Almanac reports the FID to INP switch cut mobile pass rates by about 5 points [Study, 2025]. LCP is the metric most sites fail.

## 2. Evidence that speed moves conversion

| Case | Change | Business result | Design | Source and date |
|------|--------|-----------------|--------|-----------------|
| Rakuten 24 | Optimized CWV on a landing page | RPV +53.37%, CVR +33.13% | A/B test, 50/50, one month | web.dev case study [Study, 2022] |
| Vodafone Italy | LCP improved 31% | 8% more sales | A/B test | web.dev [Study, 2021] |
| redBus | INP improved 72% | 7% more sales | Before/after | web.dev [Study, 2023] |
| QuintoAndar | INP reduced 80% | Conversions +36% | Before/after | web.dev [Study, 2023] |
| Economic Times | INP from over 1,000 ms to 257 ms | Bounce rate -50%, pageviews +43% on topic pages | Before/after | web.dev [Study, 2023] |
| Renault | LCP 1 s faster | Conversions +13%, bounce -14 points | Correlational, 10M+ visits, 33 countries, Dec 2020 to Mar 2021 | web.dev via secondary [Study, 2021] |
| Deloitte and Google "Milliseconds Make Millions" | 0.1 s faster mobile speed | Retail conversions +8.4%, travel +10.1% | Observational across 37 brands | [Study, 2020] |
| Contentsquare, 997 sites | Good vs poor INP | Retail CVR 2.5% vs 2.0% | Correlational, vendor data from May 2023 | [Study, 2024] |

Caveats: most evidence is before/after or correlational, published by vendors or Google. The A/B tests (Rakuten, Vodafone) are the strongest. Recent roundups repeat older numbers; no major new 2025 to 2026 controlled study was found during research [Unverified absence]. Treat speed as a strong prior, then measure on your own site (section 9).

## 3. Measure: field first, lab second

| Source | Type | Use |
|--------|------|-----|
| Chrome UX Report (CrUX) via PageSpeed Insights or CrUX API | Field, 28-day rolling, Chrome users | Pass or fail per URL and origin |
| CrUX History API | Field, weekly history | Trend after a release |
| Search Console Core Web Vitals report | Field, grouped URLs | Template-level issues |
| RUM (web-vitals JS library, or RUM tools such as DebugBear, SpeedCurve, RUMvision) | Field, your users, all browsers you instrument | Attribution to elements, segments by source and device |
| Lighthouse, PageSpeed lab, WebPageTest | Lab, simulated | Debugging, regressions in CI |
| Clarity, Contentsquare | Behavior plus some performance | Rage clicks linked to slow interactions |

Paid landing pages with query parameters may not have URL-level CrUX data. Use origin data, RUM, or lab tests on a mid-range Android profile (Moto G Power class, 4G throttling).

### 3.1 RUM snippet (web-vitals library with attribution)
```html
<script type="module">
  import {onLCP, onINP, onCLS} from 'https://unpkg.com/web-vitals@4/dist/web-vitals.attribution.js?module';
  function send(m) {
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
      event: 'web_vitals', metric_name: m.name, metric_value: Math.round(m.name === 'CLS' ? m.value * 1000 : m.value),
      metric_rating: m.rating, metric_id: m.id,
      debug_target: (m.attribution && (m.attribution.element || m.attribution.interactionTarget || m.attribution.largestShiftTarget)) || ''
    });
  }
  onLCP(send); onINP(send); onCLS(send);
</script>
```
Pin an exact version in production and self-host if the CSP blocks third-party scripts. Send to GA4 via GTM as an event with parameters registered as custom dimensions (coordinate with `measurement`).

## 4. Diagnose LCP
LCP has four subparts [Official, web.dev]:
1. Time to First Byte (server, CDN, redirects).
2. Resource load delay (time before the browser starts fetching the LCP image).
3. Resource load duration (image size, format, bandwidth).
4. Element render delay (render-blocking CSS and JS, client-side rendering, hidden-until-JS heroes).

| Symptom | Fix |
|---------|-----|
| TTFB over 800 ms | CDN with HTML caching or edge rendering; remove redirect chains (ad click > tracking redirect > http > https > www); cache pages server side |
| LCP image discovered late (CSS background, JS carousel, lazy-loaded) | Use a real `<img>` in HTML; never `loading="lazy"` on the LCP image; add `fetchpriority="high"`; preload if it is a CSS background |
| Large image | Serve AVIF or WebP with `srcset` and `sizes`; target under about 100 to 200 KB for a mobile hero [Practitioner consensus] |
| Render-blocking CSS and fonts | Inline critical CSS, defer the rest; `font-display: swap` or `optional`; preload the one font used above the fold; subset fonts |
| Client-side A/B test hides the page (anti-flicker snippet) | Move tests server side or edge; cap anti-flicker timeout; see section 7 |
| Hero rendered by JavaScript after hydration | Server render the hero HTML |

## 5. Diagnose INP
INP phases: input delay (main thread busy), processing time (event handlers), presentation delay (rendering).

| Symptom | Fix |
|---------|-----|
| Long tasks from third-party scripts (chat, reviews, tag managers, heatmaps, A/B tools) | Delay non-critical third parties until interaction or idle; load chat on click via a facade |
| Heavy event handlers (add to cart, variant select, filter) | Do the visible update first, defer the rest with `requestAnimationFrame` plus `setTimeout`, or `scheduler.yield()` where supported |
| Large DOM (mega menus, huge collection pages) | Paginate, virtualize long lists, simplify menus |
| Hydration of large React trees | Server components, partial hydration, smaller client bundles |
| Layout thrashing | Batch reads and writes, avoid forced synchronous layout |

## 6. Diagnose CLS
| Cause | Fix |
|-------|-----|
| Images without dimensions | `width` and `height` attributes or `aspect-ratio` |
| Late banners (cookie consent, promo bars, app install banners) | Reserve space, or overlay without pushing content |
| Web fonts swapping metrics | `size-adjust` and fallback font metric overrides; `font-display: optional` |
| Injected content above existing content (reviews widget, recommendations) | Reserve min-height for widgets |
| Client-side A/B test changes after paint | Server side variants |

## 7. Third-party tags and testing tools

Third parties are the most common cause of slow landing pages on marketing sites [Practitioner consensus].

### 7.1 Tag audit procedure
1. List every third-party domain on the top 5 landing pages (DevTools > Network, group by domain, or WebPageTest "domains" view).
2. For each: owner, purpose, still used?, loads on which pages, consent category, main thread time (Performance panel or Lighthouse "Reduce the impact of third-party code").
3. Measure impact by blocking: DevTools > Network request blocking, or WebPageTest block domain; compare LCP and Total Blocking Time.
4. Decide: remove, load on interaction (facade), load after consent and idle, move server side (with `measurement`), or keep.
5. Set a budget (section 8) and a rule: new tags need an owner and an expiry date.

### 7.2 Client-side A/B testing tools and flicker
- Client-side tools change the page after it starts rendering. To avoid flicker they hide the page with an anti-flicker snippet until variants apply, which delays LCP for every visitor, including control.
- Mitigations: load the testing script synchronously from a fast CDN only on pages under test; keep the timeout short (for example 1 to 2 s max, tool dependent); use server-side or edge testing for hero and above the fold tests; Shopify Rollouts splits server side.
- Always compare LCP between control and variant as a guardrail. A variant that wins only because control is slowed by the tool is not a win.

### 7.3 Consent banners
- Consent banners are often the LCP element on mobile (a large text block). Keep banner text short so the hero stays the LCP element, or accept it and make the banner render fast (inline CSS, no heavy framework).
- Banners that push content cause CLS; overlay instead.
- Consent rate and design rules belong to `measurement`; CRO checks the banner's effect on first screen visibility, speed and bounce. Never design a banner that tricks consent (EU regulators treat that as invalid consent).

## 8. Performance budgets for landing pages [Practitioner consensus starting points]

| Budget | Target for a paid LP (mobile) |
|--------|-------------------------------|
| LCP (field p75) | under 2.0 s (headroom under the 2.5 s threshold) |
| INP (field p75) | under 150 ms |
| CLS | under 0.05 |
| HTML document | under 100 KB compressed |
| Hero image | under 150 KB (AVIF or WebP) |
| Total JavaScript | under 200 KB compressed on dedicated LPs; under 350 KB on PDPs |
| Third-party domains | 10 or fewer on dedicated LPs |
| Fonts | 2 families max, 4 files max, preload only above-the-fold font |
| Redirects from ad click | 0 or 1 |

Lighthouse CI budget file example (`budget.json`):
```json
[{
  "path": "/lp/*",
  "timings": [{"metric": "largest-contentful-paint", "budget": 2500}, {"metric": "cumulative-layout-shift", "budget": 0.1}],
  "resourceSizes": [{"resourceType": "script", "budget": 200}, {"resourceType": "image", "budget": 400}, {"resourceType": "total", "budget": 900}],
  "resourceCounts": [{"resourceType": "third-party", "budget": 10}]
}]
```

## 9. Platform specifics

### Shopify
- Remove uninstalled apps' leftover snippets (search theme code for app names); many apps inject scripts on every page.
- Hero and main product image: `{{ image | image_url: width: 1200 | image_tag: loading: 'eager', fetchpriority: 'high', sizes: '100vw', widths: '400, 600, 800, 1000, 1200' }}`. Lazy load everything below the fold.
- Prefer theme app extensions and app blocks over script tags.
- Avoid render-blocking review and upsell widgets above the fold; render star ratings from metafields server side.
- Online Store 2.0 themes (Dawn and successors) are a fast base; heavy page builder apps often add weight [Practitioner consensus].

### WordPress
- Page caching plus a CDN; object caching for WooCommerce.
- Remove page builder bloat on LPs (build LPs with blocks); dequeue plugin assets on pages that do not need them.
- WooCommerce cart fragments: disable on non-cart pages where safe.

### Webflow
- Compress and size images in the asset manager; avoid heavy interactions and Lottie above the fold; custom code embeds load synchronously by default, so move them to the end of body or load deferred.

### Next.js
- `next/image` with explicit `sizes`; mark the hero as high priority (the `priority` prop; newer major versions may rename it, check the installed version's docs) [Unverified naming in latest versions].
- `next/font` to self-host fonts with metric overrides.
- Server components by default; mark only interactive islands with `'use client'`.
- Static generation or ISR for LPs; edge or middleware for variant assignment without client flicker.

## 10. Navigation speed upgrades
- Speculation Rules API: prerender or prefetch likely next pages (PDP from collection, checkout from cart) in Chromium browsers. Example:
```html
<script type="speculationrules">
{"prerender": [{"where": {"href_matches": "/products/*"}, "eagerness": "moderate"}]}
</script>
```
  Exclude cart actions, logout and any URL with side effects. Analytics must handle prerendered pageviews (most modern tags do; verify).
- Back/forward cache (bfcache): avoid `unload` handlers and `Cache-Control: no-store` on browse pages so back navigation is instant (collection to PDP and back). Test in DevTools > Application > Back/forward cache.
- 103 Early Hints and `preconnect` to critical third-party origins (image CDN, payment).

## 11. Put a dollar value on speed (for prioritization)
Option A (preferred): A/B test a faster version (Rakuten style), or a slowdown test where a variant adds a delay (for example +500 ms) to measure sensitivity, then extrapolate the value of speed-ups. Slowdown tests cost real revenue during the test; get human approval and keep them short [Practitioner consensus, used at large companies].
Option B: segment existing data: CVR by LCP bucket from RUM (correlational, confounded by device and network; use only to size, not to prove).

Estimate:
```
Monthly value = monthly sessions on affected pages x baseline CVR x expected relative lift x AOV (or lead value)
Expected relative lift: use 2% to 5% for moving from "needs improvement" to "good" LCP as a conservative planning prior, then replace with your own test result. [Practitioner consensus; not a benchmark]
```

## 12. Speed QA checklist before launching any LP or variant
- [ ] Field or lab LCP under 2.5 s on mid-range mobile, CLS under 0.1, no long tasks over 200 ms on load.
- [ ] Hero image is an `<img>` with `fetchpriority="high"`, sized, modern format, not lazy.
- [ ] No more than 1 redirect from the ad click.
- [ ] Third-party scripts listed with owner; non-critical ones deferred.
- [ ] Variant does not add flicker or layout shift compared with control.
- [ ] Tested in in-app browsers of the paid social channels used.
