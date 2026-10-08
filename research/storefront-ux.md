# Storefront UX: Market Research Dossier (October 2026)

Research behind the `storefront-ux` agent and skill. Method: research bodies (Baymard Institute, Nielsen Norman Group, web.dev, WebAIM), official platform sources (Shopify changelogs, Editions, Help Center, developer docs; EUR-Lex and regulators), and read-only study of open source storefronts and UI primitives cloned on 2026-10-08 (Shopify Horizon, Dawn, Hydrogen, theme-liquid-docs, ui-extensions; Vercel Next.js Commerce; Medusa starter; Saleor Paper; WooCommerce blocks; Base UI; Radix; React Aria; shadcn/ui; Embla; cmdk; sonner; vaul; Emil Kowalski's skills). Baymard and Shopify sites could not be fetched directly from this environment; their figures come from search-indexed article text and are labeled. Evidence labels follow `docs/AUTHORING_SPEC.md`.

## 1. Executive summary

1. Most leading stores are still mediocre at the basics: up to 62% of leading sites are mediocre or worse on product pages (2026), 58% of desktop and 78% of mobile sites on product lists and filtering (2025-09), 58% desktop and 67% mobile on homepage and navigation (2025), and 46% desktop, 58% mobile, 64% apps on search (2026) [Study, Baymard]. The biggest wins are table stakes, not clever tests.
2. The cheapest PDP fixes are still undone: 57% of sites lack button-style size selectors, 81% do not show unit prices, 67% do not estimate total cost near the buy button (2026), 91% lack in-scale images (2025) [Study, Baymard].
3. Shopify reset its storefront foundation: Horizon (launched 2025-05-21, v4.2.0 on 2026-09-18) with nested theme blocks, then Spring '26 (2026-06-17) added standard storefront events and actions (`shopify:cart:lines-update`, `Shopify.actions.openCart`) that apps and AI agents can rely on [Official]. Dawn is maintained (v16.0.0, 2026-08-10) but no longer the flagship.
4. Shopify closed several legacy doors in 2026: Scripts stopped on 2026-06-30, non-Plus Thank you and Order status pages auto-upgraded on 2026-08-26 (additional scripts removed), legacy customer accounts deprecated on 2026-02-26 with no sunset date yet, and script tags are reported to stop running on 2027-03-01 [Official, secondary for script tags].
5. Accessibility moved from risk to enforcement: the EAA applies since 2025-06-28; the Netherlands ACM found about 61% of ~100 large webshops inaccessible with ordering blocked by inaccessible buttons and CAPTCHA (2026-03); a French court ordered Carrefour to fix its site and app within 6 months with EUR 500 per day penalties (2026-06-04) [Official, court reports].
6. Standards are shifting to WCAG 2.2: ETSI published EN 301 549 v4.1.1 on 2026-09-02 (WCAG 2.2 AA plus EAA mapping), with Official Journal citation expected late November to December 2026 [Official]. Build to WCAG 2.2 AA now; the WebAIM Million 2026 still finds detectable failures on 95.9% of home pages [Study].
7. EU consumer law now reaches storefront UI directly: the withdrawal function (two-step "withdraw from contract here" flow) applies since 2026-06-19; CCD2 brings BNPL into scope from 2026-11-20 (no preselection, credit warnings); EmpCo bans uncertified sustainability labels from 2026-09-27; the Digital Fairness Act proposal (dark patterns, timers) is expected in Q4 2026 [Official].
8. Payment visibility is market-specific and changing: iDEAL became iDEAL | Wero (co-branding by 2026-03-31, Wero rollout from Q4 2026, iDEAL end planned 2027-12-31); in Germany PayPal (28.5%) and invoice (25.8%) lead; in Turkey installments and the TROY scheme (25.3% of card value in 2025) need domestic acquiring; in the Gulf, mada, Apple Pay, Tabby, Tamara and COD matter and Shopify Payments is unavailable [Official, Study, vendor].
9. Speed still pays: Rakuten 24 (+53.37% RPV), Vodafone (LCP 31% better, +8% sales), Ray-Ban (conversion doubled with prerendering) [Study, web.dev]; Shopify runs platform-wide prefetch rules since 2025-06 (up to 180 ms faster) and its origins pass mobile CWV far more often than Adobe Commerce (76.5% vs 44.3%, June 2026, secondary) [Official, Unverified].
10. The open source UI stack matured and churned: Base UI reached 1.0 (2025-12-11) and added a Drawer (1.2.0, 2026-02-12) while vaul went unmaintained (2025-10-03) yet still powers shadcn/ui's Drawer; sonner (2.0.8) remains the default toast library but ships a 4-second default that is short for storefront text [Official repos].

## 2. State of storefront UX in 2026 (with numbers)

| Area | Number | Source, date | Label |
|------|--------|--------------|-------|
| Product page | Up to 62% mediocre or worse; 48% desktop and 38% mobile decent or good | Baymard 2026 | [Study, 2026] |
| Product page details | 57% no button size selectors, 81% no unit price, 67% no total cost estimate near buy section | Baymard 2026 | [Study, 2026] |
| Product page layout and images | 28% horizontal tabs; 55% decent images; 91% no in-scale images | Baymard 2025 | [Study, 2025] |
| Product lists | 58% desktop, 78% mobile mediocre or worse; 28% no applied filter overview | Baymard 2025-09 (21,000+ parameters, 170+ sites) | [Study, 2025-09] |
| Homepage and navigation | 58% desktop, 67% mobile mediocre or worse; 59% of mobile homepages lack full scope links | Baymard 2025 (180+ sites) | [Study, 2025] |
| Search | 46% desktop, 58% mobile, 64% app mediocre or worse; autocomplete on 80% of sites, done right on 19% | Baymard 2026 and autocomplete research | [Study, 2026] |
| Mobile overall | 75% mediocre; 42% do not combine variations; 54% no address validation | Baymard 2026 (150+ sites, 71,000+ elements) | [Study, 2026] |
| Checkout | 64% of 180+ sites mediocre or worse; 62% guest checkout not most prominent; 72% no card type detection; 11.3 fields average | Baymard | [Study, 2025] |
| Cart abandonment | 70.22% documented average | Baymard, updated 2025-09 | [Study, 2025-09] |
| Shoppers | 1,083 US shoppers: returns frequency declining over 3 years; loyalty is 4th account expectation; email frequency top unsubscribe driver | Baymard quantitative 2026-08-04 | [Study, 2026-08] |
| Accessibility | 95.9% of home pages with detectable WCAG failures; 56.1 errors per page; low contrast 83.9% | WebAIM Million 2026 (via coverage) | [Study, 2026-02] |
| Accessibility enforcement | About 61% of ~100 large Dutch webshops not accessible | ACM 2026-03 | [Official, 2026-03] |
| Performance | Shopify 76.5% of mobile origins pass CWV vs Adobe Commerce 44.3% and BigCommerce 64.3% | CrUX June 2026 via Webtonic | [Unverified, 2026-06] |
| Payments Germany | PayPal 28.5%, invoice 25.8%, direct debit 17.3%, cards 12.3% (2024 data) | EHI Online-Payment 2025 | [Study, 2025] |
| Payments Turkey | TROY 25.3% of card transaction value, 90 million cards (2025); installments about 55% of online transactions (2024) | BKM 2026-01; Worldline 2024 | [Official] [Study] |

Platform reality: Shopify is the reference platform for most DTC builds (Horizon, theme blocks, Functions, Markets, Rollouts); WooCommerce ships Product Filters, Mini-Cart and Add to Cart with Options blocks on the Interactivity API; Shopware and Adobe Commerce keep full checkout control at higher cost; headless stacks (Hydrogen on React Router 7, Next.js Commerce on Next 15, Medusa, Saleor Paper) trade speed of change for ownership of search, SEO, accessibility and performance.

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Impact on storefronts | Label |
|------|--------|-----------------------|-------|
| 2025-01 | Searchspring, Klevu and Intelligent Reach merge as Athos Commerce | Search vendor roadmaps and pricing in flux | [Official vendor] |
| 2025-01 | FTC order: accessiBe to pay USD 1 million over misleading overlay claims | Overlays are not a compliance route | [Official, 2025-01] |
| 2025-05-21 | Shopify Summer '25: Horizon theme family (10 presets), theme blocks showcase, AI block generation | New default architecture for Liquid stores | [Official, 2025-05] |
| 2025-06 | Shopify enables platform-wide speculation rules (prefetch) on Liquid storefronts | Up to 180 ms faster navigations | [Official, 2025-06] |
| 2025-06-28 | European Accessibility Act applies | Accessibility becomes enforceable for EU ecommerce | [Official] |
| 2025-08-28 | Shopify Plus deadline for Thank you and Order status upgrade | Additional scripts end on Plus | [Official] |
| 2025-09-09 | Baymard Product List UX 2025 update | Current PLP benchmark | [Study, 2025-09] |
| 2025-09 | Baymard cart abandonment average updated (70.22%) | Benchmark | [Study, 2025-09] |
| 2025-10 | Shopify API 2025-10: nested cart lines in Storefront API and checkout UI extensions; UI extensions use Polaris web components | Add-ons and warranties tied to parent lines | [Official, 2025-10] |
| 2025-10-03 | vaul marked unmaintained | Drawer library replacement needed | [Official repo] |
| 2025-10 | Sweden's PTS starts ecommerce accessibility supervision (28 cases) | Regulator activity | [Official] |
| 2025-11 | French disability groups sue Auchan, Carrefour, E.Leclerc, Picard | First EAA court actions | [Practitioner reports] |
| 2025-11-20 | CCD2 transposition deadline (many states late) | National BNPL rules being finalized | [Official] |
| 2025-12-11 | Base UI 1.0.0 | Stable unstyled primitives | [Official repo] |
| 2025-12 | Shopify Winter '26 Edition: Functions generally available, nested cart lines across surfaces, checkout updates | Bundles and add-ons in themes | [Official, 2025-12] |
| 2025-12-19 | Withdrawal function transposition deadline | National laws (Germany § 356a BGB published 2026-02-05) | [Official] |
| 2026-01 | Shopify starts auto-upgrading remaining Plus Thank you and Order status pages | Tracking migrations | [Official] |
| 2026-01-22 to 2026-03-31 | iDEAL to iDEAL \| Wero co-branding window | Logo and name updates in checkout and storefront | [Official, 2026] |
| 2026-01-23 | BKM publishes TROY 2025 data (90 million cards, 25.3% value share) | Turkish payment mix | [Official] |
| 2026-02-12 | Base UI 1.2.0 adds Drawer | vaul replacement | [Official repo] |
| 2026-02 | WebAIM Million 2026: 95.9% of home pages failing | Accessibility baseline | [Study, 2026-02] |
| 2026-02-26 | Shopify deprecates legacy customer accounts | Account pages move to UI extensions | [Official, 2026-02] |
| 2026-03 | ACM publishes webshop accessibility test results | Dutch enforcement pressure | [Official, 2026-03] |
| 2026-03-26 | Managed Markets adaptive pricing reaches earlier merchants | International price display | [Official, 2026-03] |
| 2026 (H1) | Baymard Product Page 2026, Search 2026, Mobile 2026 benchmarks | Current PDP, search, mobile figures | [Study, 2026] |
| 2026-05 | Lille court dismisses EAA claim against Auchan's ecommerce arm (appeal in Douai) | Threshold debate | [Practitioner reports] |
| 2026-06-04 | Caen court orders Carrefour to make site and app accessible within 6 months, EUR 500 per day | First EAA ruling against a retailer | [Practitioner reports] |
| 2026-06-17 | Shopify Spring '26 Edition: standard storefront events and actions, checkout redesign, `color_palette` setting, accelerated checkout with nested lines | Theme JS contracts for apps and agents | [Official, 2026-06] |
| 2026-06-19 | EU withdrawal function applies | Order status and account flows | [Official] |
| 2026-06-24 | Horizon 4.1.1 | Fixes | [Official] |
| 2026-06-30 | Shopify Scripts stop executing | Functions only | [Official] |
| 2026-06 | Reports of a new Shopify storefront search engine, SKU and synonym regressions | Re-test search configuration | [Unverified] |
| 2026-07 | Baymard cross-sell guideline 578 updated; Shopify hreflang toggle reported | Cart cross-sells; international SEO | [Study] [Unverified] |
| 2026-07-10 | Managed Markets duties-inclusive pricing | Price display across borders | [Official, 2026-07] |
| 2026-07-16 | EPI and Dutch banks confirm Wero roadmap | NL checkout planning | [Official, via CM.com] |
| 2026-08-04 | Baymard quantitative insights 2026 | Account and loyalty expectations | [Study, 2026-08] |
| 2026-08-10 | Dawn 16.0.0 commit; sonner 2.0.8 | Maintenance signals | [Official repos] |
| 2026-08-24 | EN 301 549 v4.1.1 adopted; Shopify DDU support ends | Standards; duties display | [Official] |
| 2026-08-26 | Non-Plus Shopify Thank you and Order status auto-upgrade | Tracking and post-purchase blocks rebuilt | [Official, 2026-08] |
| 2026-09-02 | ETSI publishes EN 301 549 v4.1.1 (WCAG 2.2) | New build target | [Official, 2026-09] |
| 2026-09-04 | Base UI 1.8.0 | Primitive maturity | [Official repo] |
| 2026-09-18 | Horizon 4.2.0: RTL direction via `request.locale.direction`, logical CSS, stale cart after Back fixed, Quick Add JS loaded only when enabled | Arabic and Hebrew storefronts; cart integrity | [Official, 2026-09] |
| 2026-09-21 to 23 | Shopify session counting change reported | Before/after readouts spanning those dates need care | [Unverified] |
| 2026-09-27 | EmpCo (Directive 2024/825) applies | Sustainability labels on cards and PDPs | [Official] |
| 2026-10-01 | Reported: apps can no longer create script tags; market-driven shipping model for new stores | App delivery via theme app extensions | [Unverified] |
| 2026-10-06 | Algolia acquires Velou (catalog enrichment) | Search vendor landscape | [Official vendor] |
| Upcoming 2026-11-11 | Digital Fairness Act indicative College date | Dark pattern rules | [Unverified] |
| Upcoming 2026-11-20 | CCD2 applies | BNPL UI rules | [Official] |
| Upcoming late 2026-11 to 2026-12 | EN 301 549 v4.1.1 Official Journal citation expected | Presumption of conformity | [Official, expected] |
| Upcoming Q4 2026 | Wero merchant rollout in NL | Payment method switch | [Official] |
| Upcoming 2027-03-01 | Script tags reported to stop running on storefronts | Legacy app scripts break | [Unverified] |
| Upcoming 2027-12-31 | iDEAL decommission planned | Complete Wero migration | [Official, vendor reports] |

## 4. Best practice consensus

| Topic | Consensus | Evidence |
|-------|-----------|----------|
| Navigation | Category-first top level, full scope on mobile, mega menus as disclosure for deep catalogs, visible or combination navigation on mobile | Baymard 2025, NN/g |
| Search | Visible field, autocomplete with query and scope suggestions, typo tolerance, synonyms from zero result logs, no dead ends, query persisted | Baymard 2026 |
| Filters | Category-specific facets, applied filter overview, counts, URL state, accessible fieldsets, mobile drawer with result count | Baymard 2025-09, Horizon, WooCommerce |
| Cards | Price, unit price, rating with count, swatches, one badge, variant grouping | Baymard 2026, EU price law |
| PDP | Button and swatch options, sold-out visible, delivery date, total cost hint, in-scale images, vertical sections, reviews with distribution and photos, size guide in context | Baymard 2025 and 2026 |
| Cart | Clear totals, editing with undo, relevant non-blocking cross-sells, express checkout below primary | Baymard |
| Checkout | Guest first, total cost early, local payment methods first, minimal fields with autocomplete, accessible errors, no CAPTCHA walls | Baymard, ACM, WCAG 2.2 |
| Feedback | Inline for errors and results in view; status live regions; toasts only for non-critical out-of-view events | NN/g, Primer, Spectrum |
| Motion | Transform and opacity, under about 300 ms, ease-out entries, reduced motion honored | Practitioner consensus (Emil Kowalski), WCAG |
| Accessibility | WCAG 2.2 AA as the target; native elements and maintained primitives; manual testing beyond automated tools | W3C, EN 301 549 v4.1.1, regulators |
| International | Country decides currency, taxes, payments; suggest not force; logical CSS for RTL | Shopify Markets, Horizon 4.2.0 |
| Performance | LCP image prioritized, JS budgets per template, prefetch or prerender high-intent navigations | web.dev, Shopify |

## 5. Contested topics

| Topic | Side A | Side B | Our position |
|-------|--------|--------|--------------|
| Infinite scroll vs load more vs pagination | Baymard (2016 testing): load more best, infinite scroll harmful on search and mobile | Horizon defaults to auto-loading with URL updates; many stores report more products viewed | Load more on search; infinite auto-load acceptable on category PLPs only with URL state, Back restore and reachable footer; test on high-traffic stores |
| Sticky add to cart on mobile | Common lift reports from practitioners | Can obscure content, chat and focus (WCAG 2.4.11), adds noise | TF; implement only with the Horizon-style observer rules and focus padding |
| Cart drawer vs cart page vs direct checkout | Drawers keep context and show cross-sells | Pages handle large carts; direct checkout cuts steps for single-item stores | Choose by catalog and cart size; test direct checkout for 1 to 10 SKU stores |
| Toasts for add to cart | Libraries like sonner make toasts easy and polished | Primer and accessibility practitioners warn toasts are missed and fail some users; WCAG 2.2.1 debate | Never toast-only; button state plus drawer plus status region |
| Free shipping progress bars | Raise AOV by making the threshold concrete | Can lower CVR and margin; often wrong in multi-currency setups | TF with RPV and margin as judges; must be per-market correct |
| Quick add on PLP | Faster repeat buying | Wrong-size orders and returns in apparel | Use for consumables and single-variant items; test for apparel |
| Hover vs click mega menus | Hover is fast for mouse users | Accidental opens, touch and keyboard issues | Click plus hover with intent delay, disclosure semantics |
| Headless vs Liquid in 2026 | Headless gives full control and modern React | Horizon closes many gaps; headless means rebuilding search, SEO, accessibility and analytics | Headless only with a measured need and the team to own it |
| Native Shopify search vs third-party | Native is free, fast, integrated with filters | 2026 reports of SKU and synonym regressions; limited merchandising | Run the 12 relevance checks; switch only when checks fail or the catalog demands it |
| EN 301 549 status under the EAA | v3.2.1 is the cited reference today (Level Access) | No standard is cited under the EAA itself, so no presumption (Legalithm) | Build to WCAG 2.2 AA; name the tested version in statements |
| Auto-playing product video | Motion shows product in use | Distracting, costs LCP, accessibility issues | Poster plus user start or muted short loop with pause and reduced motion stop |

## 6. What top operators do differently

- Treat the storefront as a product: a component inventory with owners, a design system on maintained primitives, per-template JS and CWV budgets enforced in CI.
- Fix data before UI: normalized attributes and metafields make filters, search, swatches, cards and feeds work at once.
- Run search operations weekly: zero results, synonyms, redirects and pins, with the 12 relevance checks as a regression suite.
- Split lanes: ship table stakes fixes every sprint with before/after readouts; reserve A/B tests for bold, uncertain ideas.
- Test on real devices and in the social in-app browsers that send paid traffic.
- Keep an app diet: every app has an owner, a KPI and a JS cost; remove the rest.
- Build market modules (payments, legal flows, formats, RTL) as checklists, not one-off fixes.
- Put accessibility in the definition of done: keyboard and screen reader purchase path on every release.
- Mine support tickets, return reasons and reviews into PDP content every month.
- Watch the platform changelog and act before deadlines (Scripts, Thank you pages, customer accounts, script tags, iDEAL branding).

## 7. Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|-----------|
| Theme migration without parity (filters, redirects, account templates, tracking) | Traffic and conversion drop; unplanned customer accounts upgrade | Parity checklist with `site-engineer` and `seo`; check legacy account templates |
| App and script sprawl | INP failures, CLS, slower mobile conversion | App inventory, JS budget, theme app extensions only |
| Fake urgency and scarcity apps | Legal exposure (UCPD, FTC, DFA to come), trust loss | Ban by rule; compliance review |
| Disabling sold-out variants | Lost back-in-stock demand, confused users, accessibility issue | Label and keep selectable |
| Toast-only add to cart and error feedback | Missed confirmations, screen reader silence | Inline plus live region plus drawer |
| Forced IP redirects and currency without country | Wrong taxes, shipping and SEO problems | Suggest banner, country selector |
| Payment logos for unavailable methods; stale iDEAL branding | Abandonment at payment; risk of iDEAL deactivation | Per-market icons; co-branding check |
| Thank you page tracking not migrated after 2026-08-26 | Ad platforms lose purchases, bidding degrades | Test orders with `measurement` |
| Accessibility overlays as the plan | Remaining violations, legal risk, FTC action precedent | Fix code; test manually |
| Building drawers on unmaintained libraries | Security and compatibility debt | Base UI Drawer, native dialog |
| Free shipping bar in the wrong currency or ignoring discounts | False promises, support tickets | Per-market threshold source, post-discount math |
| Long SEO text above the grid | Products pushed below the fold | Move below grid with `seo` |

## 8. Benchmarks (use with caution; compare to own history first)

| Metric | Value | Source, date | Sample | Caveat |
|--------|-------|--------------|--------|--------|
| PDP mediocre or worse | Up to 62% | Baymard 2026 | Leading US and EU sites | Paywalled detail; benchmark sites, not SMBs |
| PLP mediocre or worse | 58% desktop, 78% mobile | Baymard 2025-09 | 170+ sites, 21,000+ parameters | Large retailers |
| Search mediocre or worse | 46% desktop, 58% mobile, 64% apps | Baymard 2026 | Benchmark sites | Third-party summaries cite 56% overall |
| Homepage and nav mediocre or worse | 58% desktop, 67% mobile | Baymard 2025 | 180+ sites | |
| Checkout mediocre or worse | 64% | Baymard 2025 | 180+ sites | |
| Cart abandonment | 70.22% | Baymard 2025-09 | 50 studies | Mixed methods and years |
| Checkout UX potential | 35.26% CVR lift | Baymard | Modeled for large sites | Not a forecast |
| Home pages with WCAG failures | 95.9% | WebAIM Million 2026 | 1,000,000 home pages | Automated detection only |
| Large Dutch webshops not accessible | About 61% | ACM 2026-03 | About 100 large webshops and providers | Regulator test set |
| Mobile CWV pass, Shopify origins | 76.5% (Adobe Commerce 44.3%) | CrUX June 2026 via secondary | 424,052 and 33,388 origins | Not verified against raw CrUX |
| Rakuten 24 after CWV work | RPV +53.37%, CVR +33.13% | web.dev | One retailer | Case study |
| Vodafone Italy | LCP 31% better, 8% more sales | web.dev | One test | Case study |
| Ray-Ban prerendering | Conversion about doubled, exit rate 13% lower | web.dev | One retailer | Case study |
| Shopify speculation rules | Up to 180 ms faster loads | Shopify performance blog 2025 | Platform | Supported scenarios only |
| German payment shares | PayPal 28.5%, invoice 25.8% | EHI 2025 (2024 data) | German online retail | Sources differ by survey |
| Turkish card scheme | TROY 25.3% of card value | BKM 2026-01 | National | Card payments only |
| Review reliance | 95% of test participants | Baymard | Usability testing | Qualitative sessions |

## 9. Tools, APIs and MCP servers

| Tool | What it lets the agent do | Gate | Label |
|------|---------------------------|------|-------|
| Shopify CLI (`theme dev`, `theme check`, `theme pull`, `theme push --unpublished`, `theme publish`) | Read, lint, preview and (with approval) publish themes | G0 to G3 | [Official] |
| Shopify Dev MCP server and Shopify AI Toolkit | Docs and API schema lookups for Liquid, Storefront API, Functions; the Hydrogen skeleton now recommends the AI Toolkit (2026.4.6) | G0 | [Official] [Unverified on feature set] |
| Shopify Storefront API, Ajax Cart API, Section Rendering API, Predictive Search API | Cart, search and partial rendering in themes and headless | G0 to G2 in dev stores | [Official] |
| Standard storefront events and actions | Listen to cart and product events; call `Shopify.actions.*` | G1 code | [Official, 2026-06] |
| Search & Discovery app and Shopify Analytics search reports | Filters, synonyms, boosts; top and zero result queries | G0 read, G3 change | [Official] |
| Shopify Rollouts | Theme and checkout experiments (with `cro`) | G3 | [Official] |
| WooCommerce Store API, Shopware Store API, Adobe Commerce GraphQL | Cart and catalog in other platforms | G0 to G2 | [Official] |
| PageSpeed Insights API and CrUX API | Field CWV per URL and origin | G0 | [Official] |
| Lighthouse and Lighthouse CI | Lab checks and budgets in CI (with `site-engineer`) | G1 | [Official] |
| axe-core and axe DevTools, Pa11y, WAVE, Accessibility Insights | Automated accessibility checks | G0 | [Official vendor] |
| Chrome DevTools MCP (Google) and Playwright MCP (Microsoft) | Drive a browser for task scripts, traces, screenshots, accessibility tree | G0 on live, G1 on previews | [Official, 2025] |
| Microsoft Clarity, Hotjar, Contentsquare | Recordings, heatmaps, rage and dead clicks | G0 | [Official vendor] |
| Algolia, Athos Commerce, Searchanise, Doofinder, Constructor, Meilisearch, Typesense APIs | Search relevance analytics and configuration | G0 read, G3 change | [Official vendor] |
| `scripts/storefront_lint.py` (this package) | Static HTML checks on saved pages: lang, zoom, alt, names, labels, menus, live regions, scripts | G0 | This repo |

## 10. Official sources to monitor

| Source | Cadence |
|--------|---------|
| Shopify Changelog and developer changelog; Shopify Editions | Weekly; each Edition |
| `Shopify/horizon` release notes, `Shopify/dawn` commits, `Shopify/theme-liquid-docs`, `Shopify/ui-extensions` CHANGELOG, Hydrogen CHANGELOG | Monthly |
| Base UI, Radix, React Aria, sonner, Embla, cmdk changelogs; vaul README | Quarterly |
| Baymard current-state articles; NN/g; web.dev case studies; WebAIM Million (February) | Quarterly |
| EUR-Lex and Official Journal (EAA standards, CCD2, withdrawal function, DFA, EmpCo), AccessibleEU | Monthly until year end 2026 |
| ACM (NL), PTS (SE), French court reports, German BFSG market surveillance | Monthly |
| iDEAL and EPI (Wero), BKM (TROY), EHI (Germany payments) | Quarterly |
| WooCommerce developer blog, Shopware release notes, Adobe Commerce release notes | Quarterly |

## 11. Open questions and watch list

- Final sunset date for Shopify legacy customer accounts (announced "later in 2026", not published as of 2026-10-08).
- Script tag timeline (creation blocked 2026-10-01, stop 2027-03-01) needs confirmation in Shopify's own changelog.
- Whether Shopify's 2026 search engine change (reported June 2026) is complete and how SKU search and synonyms behave now.
- Rollouts statistics: whether confidence intervals or significance are shown for all metrics; sources disagree.
- EN 301 549 v4.1.1 Official Journal citation date and whether national regulators adopt WCAG 2.2 immediately.
- Carrefour compliance deadline (about early December 2026) and the Douai appeal in the Auchan case: scope thresholds for large retailers.
- Digital Fairness Act text: specific bans on countdown timers, drip pricing, personalized pricing, subscription traps.
- CCD2 national texts for BNPL widgets on PDPs (warning wording per country).
- Wero merchant features and pricing at rollout; consumer adoption speed in NL and Germany.
- Embla v9 stable release; Base UI API stability for Drawer; shadcn/ui moving its Drawer off vaul.
- Agentic shopping: how much traffic arrives through AI agents using standard storefront actions and catalogs, and what storefront UX means for them (with `ai-search-optimization` and `commerce-feeds`).

## 12. Sources

1. Product List UX Best Practices 2025. Baymard Institute. https://baymard.com/blog/current-state-product-list-and-filtering. 2025-09-09.
2. Product Page UX Best Practices 2026. Baymard Institute. https://baymard.com/blog/current-state-ecommerce-product-page-ux. 2026.
3. Homepage and Navigation UX Best Practices 2025. Baymard Institute. https://baymard.com/blog/ecommerce-navigation-best-practice. 2025.
4. Make Product Categories the Top-Level Navigation Items on Mobile Sites. Baymard Institute. https://baymard.com/blog/main-navigation-product-categories. Pre-2025.
5. Mobile UX Trends 2026: 10 Best Practices. Baymard Institute. https://baymard.com/blog/mobile-ux-ecommerce. 2026.
6. Mobile App UX Benchmark 2026. Baymard Institute. https://baymard.com/research-articles/mobile-app-ux-benchmark-2026. 2026.
7. Ecommerce UX Trends 2026: Stats and Insights. Baymard Institute. https://baymard.com/blog/ecommerce-quantitative-ux-insights-2026. 2026-08-04.
8. Ecommerce Search UX Best Practices 2026. Baymard Institute. https://baymard.com/research-articles/ecommerce-search-query-types. 2026.
9. Autocomplete design patterns (only 19% get everything right). Baymard Institute. https://baymard.com/blog/autocomplete-design. Undated.
10. Always copy the active autocomplete suggestion to the search field. Baymard Institute. https://baymard.com/blog/copy-search-suggestion-to-search-field. Undated.
11. Cart abandonment rate statistics. Baymard Institute. https://baymard.com/lists/cart-abandonment-rate. Updated 2025-09.
12. Reasons for abandonments during checkout, US 2025. Statista. https://statista.com/statistics/1228452/reasons-for-abandonments-during-checkout-united-states. 2025-05.
13. Ecommerce Checkout UX Guide. Baymard Institute. https://baymard.com/blog/checkout-flow-ux-optimization. 2025.
14. Payment UX standards. Baymard Institute. https://baymard.com/blog/payment-ux. 2025 to 2026.
15. Electronics and Office UX Benchmark 2026. Baymard Institute. https://baymard.com/research-articles/electronics-and-office-ux-benchmark-2026. 2026.
16. Product recommendations in the cart. Baymard Institute. https://baymard.com/blog/product-recommendations-cart. Pre-2025.
17. Guideline 578: Adapting cross-sells to the user's context. Baymard Institute. https://baymard.com/guidelines/578-adapting-cross-sells-to-the-user-s-context. Updated 2026-07.
18. User reviews section design examples. Baymard Institute. https://baymard.com/ecommerce-design-examples/44-user-reviews-section. Undated.
19. Infinite Scrolling, Pagination or Load More Buttons? Smashing Magazine. https://smashingmagazine.com/2016/03/pagination-infinite-scrolling-load-more-buttons. 2016-03.
20. Baymard checkout benchmark summary. Archetype Themes on X. https://x.com/ArchetypeThemes/status/1999479602910232729. 2025-12.
21. Hamburger Menus and Hidden Navigation Hurt UX Metrics. Nielsen Norman Group. https://www.nngroup.com/articles/hamburger-menus/. Undated in summary.
22. The Hamburger-Menu Icon Today: Is it Recognizable? Nielsen Norman Group. https://www.nngroup.com/articles/hamburger-menu-icon-recognizability/. 2025.
23. Mega Menus Gone Wrong. Nielsen Norman Group. https://www.nngroup.com/articles/mega-menus-gone-wrong/. Undated in summary.
24. Menu-Design Checklist: 17 UX Guidelines. Nielsen Norman Group. https://www.nngroup.com/articles/menu-design/. Undated in summary.
25. Basic Patterns for Mobile Navigation. Nielsen Norman Group. https://www.nngroup.com/articles/mobile-navigation-patterns/. Undated in summary.
26. Indicators, Validations, and Notifications. Nielsen Norman Group. https://nngroup.com/articles/indicators-validations-notifications. Undated in summary.
27. The business impact of Core Web Vitals. web.dev. https://web.dev/case-studies/vitals-business-impact. Ongoing.
28. Rakuten 24 Core Web Vitals case study. web.dev. https://web.dev/case-studies/rakuten. About 2022.
29. Farfetch Core Web Vitals case study. web.dev. https://web.dev/case-studies/farfetch. About 2022.
30. Ray-Ban Speculation Rules case study. web.dev. https://web.dev/case-studies/rayban-speculation-rules. About 2025.
31. Fotocasa INP case study. web.dev. https://web.dev/case-studies/fotocasa-cwv. About 2025-10.
32. Speculation Rules at Shopify. Shopify Performance blog. https://performance.shopify.com/blogs/blog/speculation-rules-at-shopify. 2025.
33. Speed up navigations with the Speculation Rules API. Shopify.dev. https://shopify.dev/docs/storefronts/themes/best-practices/performance/use-speculation-rules. 2025 to 2026.
34. E-Commerce Technical SEO Statistics 2026. Webtonic. https://www.webtonic.io/blog/e-commerce-technical-seo-statistics. 2026.
35. Shopify Editions Summer '25. Shopify. https://www.shopify.com/editions/summer2025. 2025-05.
36. Shopify's design vision brings Horizon into view. Shopify News. https://www.shopify.com/news/summer-25-edition-design. 2025-05.
37. Shopify Editions Winter '26. Shopify. https://www.shopify.com/editions/winter2026. 2025-12.
38. The Spring '26 Edition is live. Shopify Changelog. https://changelog.shopify.com/posts/the-spring-26-edition-is-live. 2026-06-17.
39. Standard storefront events and actions. Shopify developer changelog. https://shopify.dev/changelog/posts/standard-storefront-events-and-actions. 2026-06.
40. Standard storefront events and actions (docs). Shopify.dev. https://shopify.dev/docs/storefronts/themes/best-practices/standard-events-and-actions. 2026.
41. Standard storefront events and actions now support cart attributes. Shopify developer changelog. https://shopify.dev/changelog/events-and-actions-cart-attributes-support. 2026.
42. Horizon themes collection. Shopify Theme Store. https://themes.shopify.com/collections/horizon-themes. 2025 to 2026.
43. Legacy customer accounts are now deprecated. Shopify developer changelog. https://shopify.dev/changelog/legacy-customer-accounts-are-deprecated. 2026-02-26.
44. Thank you and Order status upgrade customization options. Shopify Help Center. https://help.shopify.com/en/manual/checkout-settings/customize-checkout-configurations/upgrade-thank-you-order-status/customization-options. 2026.
45. Shopify Thank You Page Tracking: The August 26, 2026 Deadline. WeltPixel. https://weltpixel.com/blogs/news/shopify-thank-you-page-tracking-the-august-26-2026-deadline. 2026.
46. Shopify Updates June 2026. Fudge. https://www.fudge.ai/blog/shopify-updates-june-2026/. 2026-06.
47. Shopify Updates August 2026. Fudge. https://www.fudge.ai/blog/shopify-updates-august-2026/. 2026-08.
48. Rollouts analytics. Shopify Help Center. https://help.shopify.com/en/manual/markets-new/rollouts/analytics. 2026.
49. Rollout types. Shopify Help Center. https://help.shopify.com/en/manual/markets/rollouts/rollout-types. 2026.
50. Shopify Rollouts Is Useful. It's Not A/B Testing. Shoplift. https://www.shoplift.ai/post/shopify-rollouts-is-useful-for-deployment-management-not-experimentation. 2026.
51. Smarter international pricing with Managed Markets. Shopify Changelog. https://changelog.shopify.com/posts/smarter-international-pricing-with-managed-markets. 2026-03.
52. Duties-inclusive pricing from Managed Markets. Shopify Changelog. https://changelog.shopify.com/posts/drive-international-conversion-with-automated-duties-inclusive-pricing-from-shopify-managed-markets. 2026-07-10.
53. Catalogs. Shopify Help Center. https://help.shopify.com/en/manual/markets/customizations/catalogs. 2026.
54. Nested cart lines. Shopify.dev. https://shopify.dev/docs/apps/build/product-merchandising/nested-cart-lines. 2025-10.
55. Cart Transform Function API. Shopify.dev. https://shopify.dev/docs/api/functions/reference/cart-transform/graphql. 2026.
56. EU right of withdrawal. Shopify Help Center. https://help.shopify.com/en/manual/compliance/legal/eu-right-of-withdrawal. 2026.
57. Shopify Spring '26 Edition for developers. learnshopify.dev. https://learnshopify.dev/blog/shopify-spring-2026-edition-developers. 2026-06.
58. Shopify Horizon vs Dawn 2026. Craftshift. https://craftshift.com/shopify-horizon-vs-dawn-2026/. 2026.
59. Goodbye Dawn! Shopify Launches Horizon. Ed Codes. https://ed.codes/blog/shopify-horizon-theme-and-blocks. 2025.
60. Rapid Search vs Shopify Search and Discovery. Rapid Search. https://www.rapidsearch.app/blog/rapid-search-vs-shopify-search-and-discovery. 2026.
61. Shopify/horizon. GitHub. https://github.com/Shopify/horizon. v4.2.0, 2026-09-21.
62. Shopify/dawn. GitHub. https://github.com/Shopify/dawn. v16.0.0, 2026-08-10.
63. Shopify/hydrogen. GitHub. https://github.com/Shopify/hydrogen. 2026-10-06.
64. Shopify/theme-liquid-docs. GitHub. https://github.com/Shopify/theme-liquid-docs. 2026-10.
65. Shopify/ui-extensions. GitHub. https://github.com/Shopify/ui-extensions. 2026.10.0-rc.13.
66. vercel/commerce. GitHub. https://github.com/vercel/commerce. 2026-06-10.
67. medusajs/nextjs-starter-medusa. GitHub. https://github.com/medusajs/nextjs-starter-medusa. 2026-04-23.
68. saleor/storefront. GitHub. https://github.com/saleor/storefront. 2026-10-01.
69. woocommerce/woocommerce. GitHub. https://github.com/woocommerce/woocommerce. 2026-10-08.
70. mui/base-ui. GitHub. https://github.com/mui/base-ui. 1.8.0, 2026-09-04.
71. radix-ui/primitives. GitHub. https://github.com/radix-ui/primitives. 2026-10-08.
72. adobe/react-spectrum. GitHub. https://github.com/adobe/react-spectrum. 2026-10-08.
73. shadcn-ui/ui. GitHub. https://github.com/shadcn-ui/ui. 2026-10-08.
74. davidjerleke/embla-carousel. GitHub. https://github.com/davidjerleke/embla-carousel. 9.0.0-rc04.
75. pacocoursey/cmdk. GitHub. https://github.com/pacocoursey/cmdk. 2025-10-28.
76. emilkowalski/sonner. GitHub. https://github.com/emilkowalski/sonner. 2.0.8, 2026-08-10.
77. emilkowalski/vaul. GitHub. https://github.com/emilkowalski/vaul. 2025-10-03.
78. emilkowalski/skills. GitHub. https://github.com/emilkowalski/skills. 2026-10-02.
79. WCAG 2.2. W3C. https://www.w3.org/TR/WCAG22/. 2023-10-05.
80. ARIA Authoring Practices Guide patterns. W3C WAI. https://www.w3.org/WAI/ARIA/apg/patterns/. Ongoing.
81. EN 301 549 has been updated. AccessibleEU. https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en. 2026-09-07.
82. EN 301 549 v4.1.1 is final. Deque. https://www.deque.com/blog/en-301-549-v4-1-1-is-final-what-changed-what-it-means-and-what-you-should-do/. 2026-09.
83. EN 301 549 v4.1.1: What Changed and When It Applies. Level Access. https://www.levelaccess.com/compliance-overview/en-301-549-compliance/. 2026.
84. No presumption of conformity under the EAA. Legalithm. https://www.legalithm.com/en/blog/en-301-549-no-presumption-of-conformity-eaa. 2026-08.
85. ACM: klant met beperking kan bij merendeel grote webwinkels niet terecht. ACM. https://www.acm.nl/nl/publicaties/acm-klant-met-beperking-kan-bij-merendeel-grote-webwinkels-niet-terecht. 2026-03.
86. PTS inleder en tillsyn av e-handelstjänster. PTS. https://pts.se/nyheter-och-pressmeddelanden/pts-inleder-en-tillsyn-av-e-handelstjanster/. 2025-10.
87. European Accessibility Act: first court ruling. LI Solutions. https://li.solutions/blog/eaa-enforcement-2026/. 2026.
88. The critical European Accessibility Act just turned 1. The Washington Times. https://www.washingtontimes.com/news/2026/jul/8/critical-european-accessibility-act-turned-1/. 2026-07-08.
89. WebAIM Million 2026 coverage. Priority Pixels. https://prioritypixels.co.uk/insights/web-accessibility-is-getting-worse-according-to-the-2026-webaim-million-report/. 2026.
90. Accessible notifications and messages. GitHub Primer. https://primer.style/accessibility/toasts/. Ongoing.
91. Toast. Adobe Spectrum Web Components. https://opensource.adobe.com/spectrum-web-components/components/toast/. Ongoing.
92. WAI interest group thread on toasts. W3C. https://lists.w3.org/Archives/Public/w3c-wai-ig/2025AprJun/0066.html. 2025.
93. Directive (EU) 2019/882 (European Accessibility Act). EUR-Lex. https://eur-lex.europa.eu/eli/dir/2019/882/oj. 2019.
94. Directive (EU) 2023/2673 (withdrawal function). EUR-Lex. https://eur-lex.europa.eu/eli/dir/2023/2673/oj. 2023.
95. EU Withdrawal Button advisory. Arnold and Porter. https://www.arnoldporter.com/en/perspectives/advisories/2026/05/eu-withdrawal-button-uk-subscription-rules-and-data-protection-risks-for-us-online-sellers. 2026-05.
96. Pitfalls for e-commerce: the EU withdrawal button. Freshfields. https://www.freshfields.com/en/our-thinking/blogs/risk-and-compliance/pitfalls-for-e-commerce-how-the-new-eu-withdrawal-button-widerrufsbutton-wi-102ms91. 2026.
97. Directive (EU) 2023/2225 (CCD2). EUR-Lex. https://eur-lex.europa.eu/eli/dir/2023/2225/oj. 2023.
98. New Consumer Credit Directive. Taylor Wessing. https://www.taylorwessing.com/en/insights-and-events/insights/2025/06/new-consumer-credit-directive. 2025-06.
99. CCD2 explained by country. Briqpay. https://briqpay.com/blog/ccd2-explained-eu-consumer-credit-directive-bnpl-country-by-country. 2026.
100. Digital Fairness Act legislative train. European Parliament. https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act. 2026.
101. Digital Fairness Act targeted for 11 November 2026. Digital Fairness Act newsletter. https://newsletter.digitalfairnessact.com/p/digital-fairness-act-targeted-for. 2026.
102. Regulation (EU) 2023/988 (GPSR). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2023/988/oj. 2023.
103. Directive (EU) 2019/2161 (Omnibus). EUR-Lex. https://eur-lex.europa.eu/eli/dir/2019/2161/oj. 2019.
104. Directive 98/6/EC (unit prices). EUR-Lex. https://eur-lex.europa.eu/eli/dir/1998/6/oj. 1998.
105. Directive (EU) 2024/825 (Empowering consumers for the green transition). EUR-Lex. https://eur-lex.europa.eu/eli/dir/2024/825/oj. 2024.
106. § 312j BGB. Gesetze im Internet. https://www.gesetze-im-internet.de/bgb/__312j.html. Current.
107. Preisangabenverordnung (PAngV 2022). Gesetze im Internet. https://www.gesetze-im-internet.de/pangv_2022/. 2022.
108. From iDEAL to Wero. ING. https://www.ingwb.com/en/service/payments-and-collections/from-ideal-to-wero. 2026.
109. iDEAL to Wero migration. Stripe. https://support.stripe.com/questions/ideal-to-wero-migration. 2026.
110. iDEAL vs Wero guide. MultiSafepay. https://www.multisafepay.com/blog/from-ideal-to-wero-what-dutch-merchants-need-to-know. 2026.
111. iDEAL to Wero guide 2026 to 2027. CM.com. https://www.cm.com/blog/ideal-to-wero-what-merchants-need-to-know-about-the-transition/. 2026.
112. TROY 2025 Verileri Basın Bülteni. BKM. https://bkm.com.tr/wp-content/uploads/2026/03/TROY-2025-Verileri-Basin-Bulteni.pdf. 2026-01-23.
113. A bridge to growth: Türkiye. Worldline. https://financial-institutions.worldline.com/content/dam/worldline/global/documents/brochures/brochure-a-bridge-to-growth-turkiye.pdf. 2024.
114. EHI-Studie Online-Payment 2025. retail-news.de. https://retail-news.de/ehi-studie-paypal-dominanz-online-zahlung/. 2025.
115. UAE payments and COD guide. Salla. https://salla.com/en/?p=41588. 2026.
116. UAE Ecommerce on Shopify: Market Entry Guide 2026. EasySell. https://easysellapp.com/blogs/wiki/uae-ecommerce-shopify-market-entry-guide-2026. 2026.
117. Klevu is now Athos Commerce. Klevu. https://www.klevu.com/. 2025.
118. Algolia Acquires Velou. Algolia. https://www.algolia.com/about/news/algolia-acquires-velou. 2026-10-06.
119. Ecommerce Search and Product Discovery Solutions 2026. Constructor. https://constructor.com/blog/ecommerce-search-product-discovery-solutions. 2026.
