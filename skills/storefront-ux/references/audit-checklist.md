# Audit Checklist (Scored Conformance Checklist)

The scored best practice conformance checklist by page type. Use it with the [Audit method](storefront-audit-method.md). Each item: ID, check, why, how to verify, severity, lane. Pattern IDs (P01 to P62) point to the [Pattern library](ux-pattern-library.md).

Lane: **TS** = table stakes, ship without a test (fix as a diff after approval, measure before/after). **TF** = test first, hand to `cro`. **TS/TF** = fixing the defect is TS, the new design is TF.

Severity weights: Critical 5, High 3, Medium 2, Low 1. Mark each item Pass, Partial, Fail or N/A.

## G. Global (every template)

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| G01 | p75 mobile field LCP 2.5 s or less, INP 200 ms or less, CLS 0.1 or less on home, PLP, PDP, cart | Speed is conversion (P62) | CrUX API or PageSpeed Insights per template | High | TS |
| G02 | LCP image eager with `fetchpriority="high"`; other images lazy with dimensions | LCP and CLS | Page source, DevTools | High | TS |
| G03 | App and third-party JS inventory within the template budget; no leftover app code | INP, stability | Network panel, theme app embeds | High | TS |
| G04 | Zoom not disabled in the viewport meta | WCAG 1.4.4 | Page source | Critical | TS |
| G05 | Form inputs at least 16 px on mobile | iOS input zoom | Computed styles on a phone | Medium | TS |
| G06 | Hover effects gated by `(hover: hover) and (pointer: fine)` | Stuck hover on touch | CSS review, real device | Low | TS |
| G07 | `<html lang>` per locale and `dir` for RTL locales | WCAG 3.1.1, RTL | Page source per locale | High | TS |
| G08 | Skip link and visible focus indicator everywhere | WCAG 2.4.1, 2.4.7 | Keyboard walk | High | TS |
| G09 | Sticky header, sticky add to cart and banners never obscure focused elements | WCAG 2.4.11 | Keyboard walk with sticky UI active | Medium | TS |
| G10 | Cookie banner keyboard and screen reader accessible, does not block ordering | Legal and WCAG | Keyboard and VoiceOver | High | TS |
| G11 | Help or contact entry in a consistent place on every template | WCAG 3.2.6 | Compare templates | Medium | TS |
| G12 | Real device pass on iPhone Safari, mid-tier Android, Instagram and TikTok in-app browsers | Emulation misses bugs | Device test log | High | TS |
| G13 | No fake urgency or scarcity (timers that reset, invented stock or viewer counts) | UCPD, FTC, trust | Reload tests, inventory comparison | Critical | TS |
| G14 | Accessibility statement and feedback route (EU) | EAA service information | Footer links | High | TS |
| G15 | Cart state correct after browser Back (bfcache) | Stale cart confusion | Add item, navigate, Back | Medium | TS |

## N. Navigation and homepage

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| N01 | Top level nav items are product categories in customer words (P01) | Findability | Compare with search log terms | High | TS |
| N02 | Every category reachable within 3 steps, each node has "Shop all" | Full scope | Walk the tree | Medium | TS |
| N03 | Mega menu uses disclosure buttons; keyboard and Escape work; no ARIA menu roles (P02) | WCAG 2.1.1, 4.1.2 | Keyboard and screen reader | High | TS |
| N04 | Mega menu has hover intent delay and click support | Accidental opens | Pointer test | Medium | TS |
| N05 | Mobile menu is modal, focus managed, drill-down with Back and level titles (P03) | Usability and a11y | VoiceOver, keyboard | High | TS |
| N06 | Mobile homepage gives the full category scope (P04) | 59% fail (Baymard 2025) | Mobile view | High | TS |
| N07 | Hero has one message and one primary CTA; no auto-rotation, or a pause control (P05) | WCAG 2.2.2, clarity | View, wait 10 s | Medium | TS/TF |
| N08 | Each homepage section has a job, owner and KPI; no orphan app sections (P06) | Bloat, focus | Section inventory | Medium | TS |
| N09 | Announcement bar shows true, current information (P07) | Trust, legal | Compare with policies | High | TS |
| N10 | Breadcrumbs reflect hierarchy on deep catalogs (P08) | Orientation | View PLP and PDP | Low | TS |
| N11 | Footer has service links, policies, locale selector, accurate payment icons per market (P09) | Trust | View per market | Medium | TS |
| N12 | 404 page offers search, categories and bestsellers | Dead ends | Visit a bad URL | Low | TS |

## S. Search

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| S01 | Visible search field on desktop (30+ SKUs); reachable on mobile home and PLP (P10) | High-intent path | View | High | TS |
| S02 | Autocomplete shows query suggestions, category scopes and products, 10 items or fewer (P11) | 19% get it right | Type 3 queries | High | TS |
| S03 | Combobox semantics; arrow keys copy suggestion into field; Escape closes | WCAG, Baymard | Keyboard and screen reader | High | TS |
| S04 | Debounced requests, stale responses ignored (no flicker) | Stability | Fast typing on mobile | Medium | TS |
| S05 | At least 10 of the 12 relevance checks pass (typos, synonyms, units, SKU, casing) (P12) | 69% misspelling risk | Run the checks | High | TS |
| S06 | Synonyms reviewed from the zero result report at least monthly | Vocabulary gaps | Change log | Medium | TS |
| S07 | Zero result page with suggestions, categories, bestsellers, contact (P13) | Dead end | Search nonsense | High | TS |
| S08 | Query persists in the field on results page | Refinement | View | Medium | TS |
| S09 | Results page has PLP filters and sort; relevance default (P14) | Narrowing | View | Medium | TS |
| S10 | SKU and barcode searchable where customers use codes (P16) | Repeat and B2B | Test codes | Medium | TS |
| S11 | Non-product queries (returns, shipping, size guide) reach help pages | Service | Test queries | Low | TS |
| S12 | Search, zero result and result click events tracked | Measurement | GA4 debug view | Medium | TS |

## L. Collection and category pages (PLP)

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| L01 | Category-specific filters on categories with 20+ products (P17) | 58% desktop, 78% mobile mediocre | Review 3 PLPs | High | TS |
| L02 | Desktop filters visible without opening a drawer | Discoverability | View at 1280 px | Medium | TS |
| L03 | Mobile filter drawer with live result count and "See N items" | Mobile filtering | Phone test | High | TS |
| L04 | Applied filters overview with remove and "Clear all" (P18) | 28% lack it | Apply 3 filters | High | TS |
| L05 | Filter values show counts; zero-result values hidden or disabled | Dead ends | Apply filters | Medium | TS |
| L06 | Filter groups are fieldsets with checkboxes; result counts announced | WCAG 1.3.1, 4.1.3 | Screen reader | High | TS |
| L07 | Price filter has typed inputs, not only a slider | WCAG 2.5.7 | View | Medium | TS |
| L08 | Sort includes price, newest, rating (count-weighted); search defaults to relevance (P19) | Intent | View | Medium | TS |
| L09 | Cards show price, genuine compare-at, unit price where required, rating with count, swatches (P20) | Decision info, legal | View 10 cards | High | TS |
| L10 | Color variants grouped with swatches where users shop by style (P21) | 42% do not | View | Medium | TF |
| L11 | Load more or pagination keeps URL state; Back restores position (P23) | Lost place | Click into PDP and Back | High | TS |
| L12 | Sold-out items last and labeled; "In stock" filter (P25) | Dead ends | View | Medium | TS |
| L13 | Fixed aspect ratio images in the grid; no layout shift | CLS | DevTools | Medium | TS |
| L14 | Quick add only for variant-light products, with drawer feedback (P22) | Wrong orders | Test | Low | TF |

## D. Product detail page (PDP)

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| D01 | 5+ images incl. in-scale and detail; zoom; video where it explains (P26) | 91% lack in-scale | View | High | TS |
| D02 | Gallery accessible: alt text per view, named controls, swipe plus buttons | WCAG 1.1.1, 2.5.7 | Screen reader | High | TS |
| D03 | Buttons or swatches for options with up to about 12 values (P27) | 57% do not | View | High | TS |
| D04 | Sold-out values visible, labeled, focusable, with notify option (P27, P38) | Demand capture, a11y | Select a sold-out value | High | TS |
| D05 | Variant change updates price, image, stock, URL and is announced | Clarity | Test with screen reader | Medium | TS |
| D06 | Compare-at prices genuine; EU prior-lowest-price rule applied where reductions are announced (P28) | Omnibus, trust | `compliance` review | Critical | TS |
| D07 | Unit price shown where required (EU goods sold by quantity) | Directive 98/6/EC, 81% miss | View | High | TS |
| D08 | Tax and shipping note per market (DE "inkl. MwSt., zzgl. Versand") | Legal | View per market | High | TS |
| D09 | Delivery date or range per market near the buy button (P29) | Baymard 2026 | View per market | High | TS |
| D10 | Shipping cost or threshold shown near the buy section | 67% miss total cost | View | High | TS |
| D11 | Stock signals match inventory | UCPD, trust | Compare with admin | Critical | TS |
| D12 | Size guide in context for sized products, cm and inches (P30) | Returns | Open it | High | TS |
| D13 | Description in vertical collapsible sections; no horizontal tabs (P31) | 28% tabs | View | Medium | TS |
| D14 | Specs in a scannable table or definition list | Comparison | View | Medium | TS |
| D15 | EU listings show GPSR info: manufacturer, contact, warnings (P39) | Regulation (EU) 2023/988 | View | Critical | TS |
| D16 | Review summary near title (average and count); distribution, filters, photos, responses (P32) | 95% rely on reviews | View | High | TS/TF |
| D17 | Reviews genuine; collection and verification method disclosed (EU) | Omnibus, FTC | `compliance` review | Critical | TS |
| D18 | Add to cart feedback: button state, drawer or inline panel, status region (P35) | Missed confirmations | Test | High | TS |
| D19 | Trust lines (returns, shipping, payment) near the button and accurate (P37) | Last-mile doubt | Compare with policies | Medium | TS |
| D20 | Paid add-ons unchecked by default; bundle contents clear (P36) | CRD Art. 22 | View | High | TS |
| D21 | Sticky add to cart (if present) appears only after the main button leaves view and never obscures content (P34) | WCAG 2.4.11 | Scroll test | Medium | TF |
| D22 | BNPL and installment messaging compliant: no preselection, CCD2 warning where required (P48) | Law from 2026-11-20 | `compliance` review | High | TS |
| D23 | Subscription option shows price per delivery and terms | Clarity, legal | View | Medium | TS |

## C. Cart and cart drawer

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| C01 | Drawer or cart dialog semantics: labeled, focus moves in, Escape, focus returns (P40, P59) | Keyboard traps block orders | Keyboard and screen reader | Critical | TS |
| C02 | Quantity steppers labeled with product; max from inventory; inline errors (P43) | Errors at checkout | Test | High | TS |
| C03 | Remove offers inline undo | Fear of mistakes | Test | Medium | TS |
| C04 | Subtotal with shipping and tax note; totals match checkout per market | Trust | Compare cart vs checkout | Critical | TS |
| C05 | Free shipping progress correct in market currency after discounts (P41) | Wrong promises | Test 2 markets | High | TS/TF |
| C06 | Cross-sells 3 or fewer, relevant, labeled, non-blocking (P42) | 52% irrelevant | View | Medium | TF |
| C07 | Discount code collapsed with inline feedback (P45) | Code hunting | Apply valid and invalid codes | Low | TS |
| C08 | Express checkout below the primary checkout button; only wallets available in the market (P44) | Focus | View per market | Medium | TS |
| C09 | Nested add-ons shown under and removed with their parent | Integrity | Remove parent | Medium | TS |
| C10 | Cart correct after Back and reload | Stale state | Back test | High | TS |
| C11 | Cart events fire once (add, remove, view cart, begin checkout) | Measurement | Debug view with `measurement` | High | TS |
| C12 | Primary checkout button visible in the drawer on mobile without scrolling | Path to buy | Phone test | High | TS |

## X. Checkout and payments

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| X01 | Guest checkout is the default; account offered after purchase (P46) | 62% fail | Walk checkout | Critical | TS |
| X02 | Market's top payment method first; icons equal availability (P47) | Payment drop-off | Walk per market | High | TS |
| X03 | NL shows iDEAL \| Wero branding; Wero switch planned before 2027-12-31 | Scheme rules | View | High | TS |
| X04 | BNPL not preselected; CCD2 information flows readable on mobile (P48) | Law from 2026-11-20 | Walk | Critical | TS |
| X05 | Delivery options show carrier, date and cost; pickup points where expected (P51) | Clarity | Walk | High | TS |
| X06 | Total cost visible at every step; no fees added late | Drip pricing, abandonment | Walk | Critical | TS |
| X07 | Address autocomplete or validation; correct `autocomplete` tokens; minimal fields (P49) | 54% lack validation | Walk | Medium | TS |
| X08 | Inline errors plus summary; data preserved after errors (P50) | WCAG 3.3.1, 3.3.7 | Submit with errors | High | TS |
| X09 | No inaccessible CAPTCHA; keyboard and screen reader users can place an order | ACM 2026 findings, WCAG 3.3.8 | Keyboard and screen reader order | Critical | TS |
| X10 | DE: final button states the payment obligation | § 312j BGB | View German checkout | Critical | TS |
| X11 | TR: pre-information form and distance sales contract acknowledged; installment table shown | Turkish regulation | Walk Turkish checkout | Critical | TS |
| X12 | Test order per market verifies purchase tracking after any checkout or app change | Lost conversions | Test order with `measurement` | Critical | TS |

## A. Post-purchase and accounts

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| A01 | Thank you page confirms, sets delivery expectations, offers account and one next action (P52) | Anxiety, retention | Test order | Medium | TS |
| A02 | Thank you page tracking via web or app pixels (additional scripts gone since 2026-08-26 on non-Plus) | Conversions to ad platforms | Test order with `measurement` | Critical | TS |
| A03 | Order status shows tracking, timeline and returns entry (P53) | Support load | View | High | TS |
| A04 | EU withdrawal function: labeled entry, two steps, partial items, acknowledgment, guest route (P53) | Law from 2026-06-19 | Walk as guest and logged in | Critical | TS |
| A05 | Account dashboard: buy again, addresses, loyalty balance (P54) | Baymard 2026 | View | Medium | TS |
| A06 | Shopify: new customer accounts in use or a migration plan; no unplanned upgrade from theme changes | Deprecated legacy accounts | Admin settings, theme files | High | TS |
| A07 | Self-serve returns with reason codes | Insights, support | Walk | Medium | TS |
| A08 | Wishlist works for guests and merges on login (if offered) (P55) | Login walls | Test | Low | TF |
| A09 | Back-in-stock and wishlist alerts have consent text | GDPR, KVKK | View | High | TS |
| A10 | Communication preferences offer frequency options (link to `lifecycle-crm` center) | Baymard 2026 unsubscribe driver | View | Low | TS |

## I. International

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| I01 | Market suggestion banner, no forced redirect, choice remembered (P61) | Trust, SEO | VPN test | High | TS |
| I02 | Prices in market currency consistent from PLP to checkout | Wrong charges | Compare per market | Critical | TS |
| I03 | Local payment icons, delivery estimates and legal pages per market | Expectations | View per market | High | TS |
| I04 | Translations complete on templates, cart, notifications, checkout-adjacent text | Trust | Review per language | High | TS |
| I05 | RTL: `dir`, logical CSS, mirrored directional icons, `<bdi>` for numbers and codes | Broken layouts | Arabic locale walk | High | TS |
| I06 | Search handles local language: Turkish casing, local synonyms, stemming | Findability | Run checks | Medium | TS |
| I07 | Dates, numbers, plurals via locale APIs | Correctness | Review | Medium | TS |
| I08 | Text expansion (German, Finnish) does not break buttons, chips, nav | Layout | Review in German | Medium | TS |

## K. Accessibility (cross-cutting)

| ID | Check | Why | How to verify | Sev | Lane |
|----|-------|-----|---------------|-----|------|
| K01 | Zero critical and serious automated findings on key templates | Baseline | axe DevTools, Lighthouse | Critical | TS |
| K02 | Keyboard-only purchase path complete (home to order) | WCAG 2.1.1 | Keyboard test | Critical | TS |
| K03 | Screen reader purchase path complete (VoiceOver iOS, NVDA) | EAA, ACM findings | Screen reader test | Critical | TS |
| K04 | Contrast passes: text 4.5:1, large text and UI parts 3:1 | 83.9% of home pages fail (WebAIM 2026) | Token check | High | TS |
| K05 | Targets at least 24 by 24 CSS px (44 px recommended on mobile) | WCAG 2.5.8 | Measure swatches, steppers, close icons | High | TS |
| K06 | Status messages through live regions (cart, filters, add to cart) | WCAG 4.1.3 | Screen reader | High | TS |
| K07 | Reflow at 320 px and 400% zoom without horizontal scroll | WCAG 1.4.10 | Zoom test | High | TS |
| K08 | Reduced motion respected; no auto-motion over 5 s without pause | WCAG 2.2.2, 2.3.3 | OS setting | Medium | TS |
| K09 | Meaningful alt text; no text baked into images | WCAG 1.1.1 | Review | High | TS |
| K10 | No overlay widget relied on for conformance | Overlays do not fix code | Page source | Medium | TS |

## Scoring rubric

```
Item points:     Pass = weight, Partial = weight / 2, Fail = 0, N/A = excluded
Weights:         Critical 5, High 3, Medium 2, Low 1
Section score:   earned points / possible points x 100        (G, N, S, L, D, C, X, A, I, K)
Page-type score: traffic-weighted average of N, S, L, D, C, X, A (weights = session share of each template;
                 X and A use checkout and order share)
Overall score:   0.15 x G + 0.15 x K + 0.10 x I (or redistribute if single market) + 0.60 x page-type score
```

| Overall score | Grade | Meaning |
|---------------|-------|---------|
| 90 to 100 | Strong | Few gaps; move to testing bigger ideas with `cro` |
| 75 to 89 | Decent | Ship the TS backlog in 1 to 2 release cycles |
| 60 to 74 | Mediocre | Most leaks are table stakes; fix before any A/B testing |
| Under 60 | Poor | Structural rebuild candidates (theme, search engine, IA) |

Blocker rule: any Critical item marked Fail is a blocker regardless of the score. Blockers go first in the change list, marked as incidents when they stop purchases (see `ads-master/INCIDENTS.md`: checkout or destination broken, wrong price live, unverified claim live).

Re-score the same templates after each release cycle and log the trend in the monthly report.

## Output template

```markdown
# Conformance scores: <store> (<date>)
Data used: <analytics, recordings, CrUX dates> | Devices: <list> | Markets: <list>

| Section | Score | Pass | Partial | Fail | N/A | Blockers |
|---------|-------|------|---------|------|-----|----------|
| G Global | | | | | | |
| N Navigation and home | | | | | | |
| S Search | | | | | | |
| L PLP | | | | | | |
| D PDP | | | | | | |
| C Cart | | | | | | |
| X Checkout | | | | | | |
| A Post-purchase | | | | | | |
| I International | | | | | | |
| K Accessibility | | | | | | |
| Overall | | | | | | |

## Blockers
## Failed and partial items (ID, finding, evidence, pattern, lane, I x C x E)
```
