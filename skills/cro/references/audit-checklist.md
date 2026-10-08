# CRO Audit Checklist (scored)

> Run per funnel (for example: paid social to PDP to checkout; search to lead form). Score each item Pass (full points), Partial (half), Fail (0) or N/A (excluded). Record evidence for every score: screenshot, data range, recording link or test result. Never score from memory.

Severity points: Critical = 5, High = 3, Medium = 2, Low = 1.

## A. Measurement readiness (gate: if A1 to A3 fail, stop and hand to `measurement`)

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| A1 | Primary conversion tracked once per conversion, matches backend within 10% | All CRO decisions depend on it | Compare GA4 or platform conversions vs orders or CRM leads for the same 30 days | Critical | Hand to `measurement` |
| A2 | Funnel step events exist (view_item, add_to_cart, begin_checkout, purchase, or LP view, form_start, generate_lead) | Locates leaks | GA4 DebugView, funnel exploration returns data at each step | Critical | Implement events |
| A3 | Purchase and pixel events survived the Shopify Thank you and Order status upgrade (Shopify only) | Auto-upgrade removed legacy scripts after 26 Aug 2026 for non-Plus | Test order; check GA4, Meta, Google Ads, TikTok events | Critical | App pixels or custom pixels |
| A4 | UTMs consistent on all paid links | Message match and channel analysis | Landing page report: share of paid sessions with utm_source and utm_campaign | High | UTM template with channel agents |
| A5 | Behavior analytics installed with masking and consent | Research input | Clarity or Contentsquare live, masking settings checked | Medium | Install, configure |
| A6 | Lead quality or order value flows back from CRM or backend | Optimize for value, not volume | CRM stage by source report exists | High | Offline conversions via `measurement` |
| A7 | AI referral traffic separated in reporting | New segment, different behavior | Custom channel group or segment present | Low | Add channel group |

## B. Traffic fit and message match

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| B1 | Top 20 ads by spend score 7+ of 8 on message match | Broken scent wastes paid clicks | Score ad and LP pairs ([Message match](message-match-by-channel.md)) | Critical | Dynamic hero or one page per angle |
| B2 | Non-brand traffic does not land on the homepage by default | Homepage serves many intents | Landing page report by campaign | High | Dedicated LP or category page |
| B3 | Page type matches awareness level | Wrong depth loses cold or hot traffic | Map campaigns to awareness ([Landing page anatomy](landing-page-anatomy.md)) | High | Pre-sell, LP or PDP as appropriate |
| B4 | Final URL expansion pages (PMax, AI Max) are conversion-ready or excluded | Paid traffic reaches weak pages | Google Ads landing pages and URL report | Medium | Fix pages or exclude via `google-ads` |
| B5 | PDP price, availability and variant match the feed | Disapprovals and distrust | Spot check 20 SKUs vs Merchant Center | High | Hand to `commerce-feeds` |
| B6 | Landing pages accessible to ad review crawlers (Google, Meta, OpenAI OAI-AdsBot) | Disapprovals, stalled delivery | robots.txt and WAF rules | Medium | Allow crawlers on LPs |

## C. Value proposition and first screen

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| C1 | Five-second test: 4 of 5 people state what it is and who it is for | Clarity drives everything | Lyssna or quick hallway test with target users | Critical | Rewrite hero ([Offer and copy](offer-and-copy.md)) |
| C2 | H1 states a specific outcome or offer (no slogans) | Specific beats clever | Read the H1 | High | Use headline formulas |
| C3 | Primary CTA visible on first screen at 390 x 844 | Mobile majority | Screenshot at 390 x 844 | High | Reorder, shorten hero |
| C4 | Proof strip in first screen (rating with count, logos, customer count) | Trust before the ask | Screenshot | Medium | Add real proof |
| C5 | Hero visual shows product in use or result (not stock or abstract) | Comprehension | Visual check | Medium | Replace image |
| C6 | No auto-rotating carousel or popup in the first 10 seconds | Dilution and annoyance | Load page fresh on mobile | Medium | Remove |

## D. Offer, pricing and risk reversal

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| D1 | Price (or price range) visible before the ask | Uncertainty kills action | Check page | High | Show price or "from" price |
| D2 | Total cost including shipping and fees knowable before checkout | Top abandonment cause (Baymard) | Cart and PDP shipping info | Critical | Shipping estimator, threshold message |
| D3 | Risk reversal stated near CTA (guarantee, returns, trial, cancel) | Reduces anxiety | Check near CTA and in cart | High | Add guarantee line |
| D4 | Urgency and scarcity are real and verifiable | Legal risk, trust | Inspect timers, stock counters | Critical | Remove fake elements |
| D5 | Discount claims follow local law (EU 30-day prior price rule) | Legal risk | Check reference prices | High | Fix reference price display |
| D6 | Offer is competitive vs top 3 competitors | Offer beats layout | `market-intel` comparison | Medium | Propose offer tests |

## E. Social proof and trust

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| E1 | Reviews are real, unfiltered and include negatives | FTC rule (Oct 2024), EU Omnibus | Review app settings, moderation policy | Critical | Show all, disclose verification |
| E2 | Testimonials attributed (name, role or location) and matched to segment | Believability | Check | Medium | Collect and attribute |
| E3 | Contact info, address and policies easy to find | Legitimacy | Footer and checkout | Medium | Add |
| E4 | Security and payment trust near payment fields | Card trust abandonment | Checkout view | Medium | Add notes and logos |
| E5 | Proof placed next to the claim it supports | Proof needs context | Page review | Low | Move blocks |

## F. Friction: forms and flows

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| F1 | Every form field justified (route, qualify, legal) | Fields cost completions | Field audit table ([Forms](forms-and-lead-capture.md)) | High | Remove or defer fields |
| F2 | Labels visible, correct input types and autocomplete | Mobile completion | Inspect HTML | High | Fix attributes |
| F3 | Inline errors explain the fix and keep entered data | Error recovery | Submit invalid data | High | Fix validation |
| F4 | No CAPTCHA puzzles | Friction | Check | Medium | Honeypot plus invisible challenge |
| F5 | Success state states next step and timing; booking offered instantly for qualified leads | Speed to lead | Submit a test lead | High | Instant scheduling |
| F6 | Form field-level analytics in place | Find killer fields | Events in GA4 or form tool | Medium | Implement tracking |
| F7 | Native lead forms judged on SQL cost, not CPL | Quality | CRM report | High | Change KPI with channel agents |

## G. Ecommerce: collection, PDP, cart, checkout (N/A if not ecommerce)

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| G1 | Guest checkout default and visible | Forced accounts drive abandonment | Checkout | Critical | Enable guest checkout |
| G2 | Express wallets available (Apple Pay, Google Pay, PayPal, Shop Pay as relevant) | Mobile speed | Checkout on iOS and Android | High | Enable |
| G3 | Local payment methods for each major market | Payment coverage | Market table ([Ecommerce](ecommerce-pdp-cart-checkout.md)) | High | Add methods |
| G4 | Checkout has about 8 fields with address autocomplete | Baymard benchmark | Count fields | Medium | Remove fields, add autocomplete |
| G5 | PDP shows delivery date estimate and returns near add to cart | Delivery speed and returns concerns | PDP view | High | Add |
| G6 | PDP has 6+ images incl. in-use and scale, plus specs table | Comprehension, AI agents | PDP view | Medium | Add assets |
| G7 | Sticky add to cart on mobile PDP | Reach CTA | Scroll test | Medium | Implement |
| G8 | Variant selection cannot fail silently | Errors | Add to cart without choosing size | High | Clear error state |
| G9 | Promo code field collapsed | Coupon hunting | Cart view | Low | Collapse |
| G10 | Collection pages have relevant filters, ratings and prices on cards | Findability | Collection view | Medium | Improve cards and filters |
| G11 | Site search handles typos and synonyms, no dead ends | Search users convert higher | Test 10 queries | Medium | Configure search |

## H. SaaS and pricing (N/A if not SaaS)

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| H1 | Activation event defined and tracked | Signups are not the goal | MEASUREMENT.md, analytics | Critical | Define with product and `measurement` |
| H2 | Pricing page: 3 to 4 tiers, "best for" lines, highlighted tier, clear units | Decision ease | Page review | High | Restructure |
| H3 | SSO signup and minimal fields | Signup friction | Signup test | High | Add SSO, defer fields |
| H4 | Billing FAQ (refunds, upgrades, cancel, overages) | Anxiety | Page review | Medium | Add FAQ |
| H5 | Demo flow offers instant scheduling and a self-serve alternative | Speed and fit | Submit test | High | Router and product tour |
| H6 | Tests report activation or paid per visitor, not signups only | Avoid false wins | Test readouts | High | Change primary metric |

## I. Mobile UX

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| I1 | Mobile CVR at least one third of desktop on the same source | Large gap means mobile problems | GA4 by device and source | High | Mobile research sprint |
| I2 | Tap targets at least 44 x 44 px, no overlapping sticky elements | Mis-taps | Device test | Medium | Adjust CSS |
| I3 | Works in Meta, Instagram, TikTok, LinkedIn in-app browsers | Most social clicks open there | Open ad preview links on phones | High | Fix flows, test wallets |
| I4 | No horizontal scroll, readable 16px base text | Usability | Device test | Medium | Fix CSS |

## J. Speed and Core Web Vitals

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| J1 | Field LCP p75 at or under 2.5 s on mobile for top LPs | Conversion and paid waste | CrUX API or PSI, RUM | High | [Speed](speed-and-core-web-vitals.md) LCP fixes |
| J2 | Field INP p75 at or under 200 ms | Responsiveness on PDP and forms | CrUX or RUM | High | Third-party and handler fixes |
| J3 | CLS at or under 0.1 | Mis-taps, trust | CrUX or RUM | Medium | Reserve space |
| J4 | Hero image is not lazy, has fetchpriority high, modern format | LCP | Inspect HTML | Medium | Fix markup |
| J5 | Third-party scripts inventoried with owners; non-critical deferred | Bloat | Network panel by domain | Medium | Tag governance |
| J6 | Testing tool does not hide the page for more than about 1 to 2 s (anti-flicker) | Slows control too | Script config, LCP comparison | Medium | Server-side tests, shorter timeout |
| J7 | Ad click to LP has 0 or 1 redirects | TTFB | Follow ad URL with curl -IL | Medium | Remove redirects |

## K. Accessibility and compliance

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| K1 | Checkout or lead form completable by keyboard and screen reader | EAA (in force 28 June 2025) for EU consumer ecommerce; ADA risk in US; lost customers | Keyboard run, VoiceOver or NVDA | Critical | Fix labels, focus, errors |
| K2 | Text contrast 4.5:1, focus visible | WCAG 2.1 and 2.2 AA (EN 301 549 basis) | axe, manual | High | Fix tokens |
| K3 | No accessibility overlay used as the compliance claim | Regulators and courts reject overlays | Check scripts | Medium | Remove claim, fix source |
| K4 | Accessibility statement published for EU consumer services | EAA requirement | Footer | Medium | Publish statement |
| K5 | Consent banner does not block the CTA, does not shift layout, offers reject as easily as accept | Conversion, CLS, valid consent | Mobile test | Medium | Redesign with `measurement` |
| K6 | No dark patterns (pre-ticked add-ons, confirmshaming, hidden fees, hard cancel) | Legal and trust | Walk the flow | Critical | Remove |
| K7 | Claims substantiated and approved (BRAND.md) | Legal, ad review | Claims list | High | Remove or substantiate |

## L. Experimentation program health (N/A if no testing program)

| ID | Check | Why | How to verify | Sev | Fix |
|----|-------|-----|---------------|-----|-----|
| L1 | Every test has hypothesis, primary metric, sample size and stop rule before launch | Valid decisions | EXPERIMENTS.md and plans | High | Use test plan template |
| L2 | SRM checked on every readout | Broken tests | Readouts | High | Add SRM check |
| L3 | Win rate between about 10% and 30% | Very high suggests false positives | Program metrics | Medium | Tighten stats |
| L4 | Guardrails defined (AOV, quality, speed) | Avoid hidden losses | Plans | Medium | Add guardrails |
| L5 | Learning repository exists and is used for new hypotheses | Compounding | Repository check | Low | Create |
| L6 | Tests sized for feasible MDE and duration under 6 weeks | Avoid inconclusive tests | Plans | Medium | Bolder tests, better pages |

## Scoring rubric

1. Section score = points earned / points possible (excluding N/A) x 100.
2. Overall score = weighted average of section scores with these weights (renormalize when a section is N/A):

| Section | Weight |
|---------|--------|
| A Measurement | 15 |
| B Message match | 12 |
| C Value proposition | 12 |
| D Offer | 10 |
| E Trust | 7 |
| F Friction | 10 |
| G Ecommerce or H SaaS (whichever applies) | 12 |
| I Mobile | 6 |
| J Speed | 8 |
| K Accessibility and compliance | 5 |
| L Program | 3 |

3. Caps: any failed Critical item in A caps the overall score at 49. Any failed Critical in D4, E1, K1 or K6 caps the overall score at 59 and triggers a "fix now" recommendation to the human.

| Overall | Grade | Meaning |
|---------|-------|---------|
| 85 to 100 | A | Optimized; focus on bold tests and personalization |
| 70 to 84 | B | Solid; run the test backlog |
| 55 to 69 | C | Clear leaks; fix lane first, then tests |
| 40 to 54 | D | Major issues; pause scaling paid spend on affected pages until fixed |
| under 40 | F | Broken funnel or measurement; fix before any optimization |

## Audit output template
Save as `ads-master/outputs/cro/YYYY-MM-DD_cro_audit-<funnel>.md`.
```
# CRO audit: <funnel> | Date | Data sources and ranges | Devices tested
## Score summary (section scores, overall, grade, caps applied)
## Critical and high failures (ID, evidence, fix, owner, estimated value)
## Full checklist results (tables with Pass/Partial/Fail/N/A and evidence)
## Fix lane (approval list)
## Test backlog (scored)
## Research gaps
## Handoffs requested
```
