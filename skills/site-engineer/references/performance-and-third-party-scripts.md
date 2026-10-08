# Performance Budgets and Third Party Script Governance

> Engineering governance for speed: budgets enforced in CI, a tag register that controls marketing pixels and apps, image and font rules, and field Core Web Vitals monitoring. Diagnosis of individual LCP, INP and CLS problems and the conversion evidence live in the `cro` skill (speed and Core Web Vitals reference); tracking design lives with `measurement`. Knowledge as of 2026-10.

## 1. Facts that shape the policy

| Fact | Source | Label |
|------|--------|-------|
| Core Web Vitals thresholds unchanged: LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less, at the 75th percentile of page loads | web.dev thresholds article, checked 2026-10 | [Official] |
| Lighthouse 13 (2025-10-10; PSI since 2025-10-20) replaced legacy audits with insight audits; performance scoring unchanged | Chrome for Developers blog, PSI release notes | [Official, 2025-10] |
| Final Soft Navigations origin trial in Chrome 147 to 149, shipping planned later in 2026; aims to measure Core Web Vitals for single page app route changes | Chrome for Developers blog, 2026-04-20 | [Official, 2026-04] |
| Top 1,000 sites: median 129 third party requests on desktop and 106 on mobile (all sites 83 and 79); top 1,000 grew by 15 requests year over year while distinct third party domains fell | HTTP Archive Web Almanac 2025, Third Parties chapter | [Study, 2025] |
| Server side tagging makes some vendor traffic invisible to client side measurement, so third party prevalence figures are lower bounds | Web Almanac 2025 | [Study, 2025] |
| Median mobile Total Blocking Time 1,916 ms in 2025, up 58% vs 2024, largely attributed to third party JavaScript | Secondary article citing the 2025 Web Almanac; not confirmed in the chapter | [Unverified] |
| Shopify documents a procedure to audit and remove third party scripts from themes | shopify.dev performance best practices | [Official] |

## 2. Budgets (starting points; replace with the project's own baseline after 4 weeks of data)

| Page type | Field LCP p75 | Field INP p75 | CLS p75 | Lab TBT (mobile) | JS transferred | Third party requests | Fonts |
|-----------|---------------|---------------|---------|------------------|----------------|----------------------|-------|
| Paid landing page | 2.0 s target, 2.5 s max | 150 ms target, 200 ms max | 0.05 target, 0.1 max | 200 ms | 250 KB compressed | 15 | 2 files |
| Home | 2.5 s | 200 ms | 0.1 | 300 ms | 350 KB | 25 | 3 files |
| Collection or search | 2.5 s | 200 ms | 0.1 | 300 ms | 350 KB | 25 | 3 files |
| PDP | 2.5 s | 200 ms | 0.1 | 300 ms | 400 KB | 30 | 3 files |
| Cart and checkout handoff | 2.0 s | 150 ms | 0.05 | 200 ms | 300 KB | 15 | 2 files |

These are practitioner starting points [Practitioner consensus], not platform rules. Enforce lab budgets in Lighthouse CI ([Automated QA](automated-qa-and-tests.md) section 14) and watch field budgets monthly. A release that breaks a budget needs an approved exception recorded in `DECISIONS.md` with an expiry date.

## 3. The tag register (one row per script, kept in `ads-master/outputs/site-engineer/` and refreshed monthly)

| Column | Example |
|--------|---------|
| Script or app | Reviews app embed |
| Vendor and domain(s) | `cdn.reviews-vendor.example`, `api.reviews-vendor.example` |
| Owner (person or slug) | cro, human: Ayse |
| Purpose and business value | Star ratings on PDP and collection; review collection emails |
| Loaded by | Shopify app embed / GTM tag / theme code / hardcoded in layout |
| Pages | PDP, collection |
| Trigger and timing | After consent (marketing) / immediately / on interaction |
| Consent category | Necessary, analytics, marketing, functional |
| Cost | Requests, KB, main thread ms (method below), LCP or INP impact |
| Data sent | Page URL, product ID; never PII in URLs |
| Last reviewed | YYYY-MM-DD |
| Decision | Keep, defer, load on interaction, move server side (`measurement`), remove |

Governance rules:
1. No new script without a register row, an owner and a consent category. App installs on Shopify and plugin installs on WordPress count as new scripts.
2. Duplicates are removed: two analytics libraries, two Meta Pixel installs (theme plus app plus GTM), old A/B testing snippets, uninstalled app leftovers.
3. Marketing tags load after consent where the law requires it (with `measurement` and `compliance`), and never block rendering.
4. Each quarter, every script must justify itself with its owner. No owner means removal proposal.
5. Pixels are owned by `measurement`. Site-engineer proposes load changes; `measurement` confirms event integrity after any change.

## 4. Measuring a script's cost

| Method | How | Notes |
|--------|-----|-------|
| Lighthouse with blocked URLs | `npx lighthouse <url> --blocked-url-patterns="*reviews-vendor.example*" --output=json` vs a normal run (3 runs each, median) | Lab only; consistent environment |
| Playwright A/B in lab | `context.route(/reviews-vendor\.example/, r => r.abort())`, then collect `PerformanceObserver` long tasks and LCP entries in both modes | Good for CI tracking |
| DevTools Performance panel or Chrome DevTools MCP performance trace | Trace with CPU 4x and network throttling, look at third party attribution and long tasks | The MCP server returns named insights (LCP breakdown, render blocking requests, third parties) |
| Lighthouse 13 `third-parties-insight` | Transfer size and main thread time by entity | Uses the third-party-web entity list |
| RUM | `web-vitals` with attribution build, segment INP by interaction target and long animation frame scripts | Field truth; needs consent compliant collection |

Report each script as: requests, transferred KB, main thread ms (median of 3), effect on lab LCP and TBT, and the business value from the owner. Removing a 300 ms main thread script from a PDP is usually worth more than micro optimizing first party code.

## 5. Loading patterns for third parties

| Pattern | When | Risk |
|---------|------|------|
| `defer` or `async` script | Default for any non critical script | `async` order is not guaranteed |
| Load on interaction (chat widget on first scroll or click on the chat button, video embed facade) | Chat, video embeds, maps, review widgets below the fold | Event tracking must still work on interaction |
| Load after consent | Marketing pixels, session replay | Implement with the CMP and consent mode (`measurement`) |
| Server side tagging (server GTM, Google tag gateway, CAPI) | Reduce client pixels | Owned by `measurement`; data and consent obligations still apply |
| Web worker offload (Partytown and similar) | Experimental for some tags | Breaks tags that need synchronous DOM access; test event integrity; many vendors unsupported [Practitioner consensus] |
| Facades (static image plus play button for YouTube, static map) | Heavy embeds | Accessibility of the facade button |
| Remove | No owner, duplicate, no measurable value | None; keep the register history |

Shopify specifics: apps should inject through app embeds and app blocks; disable embeds per theme in the theme editor; leftover snippets from uninstalled apps often remain in `theme.liquid` or snippets (search for vendor domains); Shopify web pixels run in a sandbox with limited page access, which protects the main thread and limits what they can read.

## 6. Images

| Rule | Implementation |
|------|----------------|
| Modern formats | AVIF or WebP through the platform CDN (Shopify `image_url` serves optimized formats; Next.js `next/image`; Cloudflare or imgix for custom) |
| Responsive sizes | `srcset` and `sizes` matching the layout; never ship a 2,000 px image to a 390 px slot |
| LCP image | Not lazy loaded; `fetchpriority="high"`; discoverable in the initial HTML (not injected by JS or CSS background); preloaded only if it is not in the HTML |
| Below the fold | `loading="lazy"` and `decoding="async"` |
| Dimensions | `width` and `height` or `aspect-ratio` on every image and video to prevent CLS |
| Carousels | Only the first slide eager; others lazy |
| Product zoom images | Load on interaction |

## 7. Fonts

| Rule | Implementation |
|------|----------------|
| Few files | 2 to 3 font files on landing pages (regular, bold, maybe one display) |
| Self host or platform host | Avoid third party font CSS on the critical path; Shopify font picker fonts are served from Shopify's CDN |
| `font-display` | `swap` for body text; `optional` for decorative fonts if layout shifts are a problem |
| Subsetting | Subset to the scripts the markets need (Latin Extended for Turkish, German and Dutch characters: ı, İ, ş, ğ, ç, ö, ü, ß, ĳ); check the Lira sign ₺ and Euro sign € exist in the font |
| Metric overrides | `size-adjust`, `ascent-override` on fallback fonts to reduce shift on swap |
| Preload | Only the one or two fonts used above the fold, with `crossorigin` |

## 8. Field monitoring

CrUX API for an origin or URL (needs an API key in the environment):

```bash
curl -s -X POST "https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=$CRUX_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{"url": "https://www.example.com/products/top-product", "formFactor": "PHONE", "metrics": ["largest_contentful_paint", "interaction_to_next_paint", "cumulative_layout_shift"]}' \
  | jq '.record.metrics | map_values(.percentiles.p75)'
```

- Low traffic URLs have no URL level data; fall back to the origin record or RUM.
- CrUX reports a trailing 28 day window. A fix shows fully in field data about four weeks after release; read RUM for faster feedback.
- Single page apps: until Soft Navigations ship broadly, CrUX and most RUM attribute route changes to the first page load; measure route change performance with your own RUM marks.
- Segment by device and, for paid traffic, by landing page and source (in-app browsers report as mobile Chrome or Safari variants).

## 9. Performance review checklist for a release

| # | Check | Fail action |
|---|-------|-------------|
| 1 | Lab budgets pass on mobile and desktop for changed templates | Fix or approved exception |
| 2 | No new render blocking CSS or JS in the head | Defer, inline critical CSS only when needed |
| 3 | No new third party domain without a register row | Block release until added and approved |
| 4 | LCP element is the intended element and loads early (Lighthouse `lcp-discovery-insight`, `lcp-phases-insight`) | Fix discovery or priority |
| 5 | No layout shifts from new components (`cls-culprits-insight`) | Reserve space |
| 6 | Interactions on changed components under 200 ms on a mid tier Android or 4x CPU throttling | Break up long tasks, reduce re-renders |
| 7 | Image and font rules in sections 6 and 7 followed | Fix |
| 8 | Page weight change explained in the release notes | Document |
