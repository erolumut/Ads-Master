# Ecommerce: Collection, PDP, Cart and Checkout

> Most ecommerce conversion is lost between the product page and the payment step. Baymard's research is the strongest public evidence base for this funnel. Use it for heuristics, then confirm with the store's own data.

## 1. Evidence base (dated)

| Finding | Source and date | Caveat |
|---------|-----------------|--------|
| Average documented cart abandonment rate 70.22%, from 50 studies | Baymard, list updated 2025-09 [Study, 2025-09] | Mix of methods and years; compare against your own rate, not this |
| Checkout design fixes could lift conversion 35.26% for an average large ecommerce site | Baymard [Study, 2025] | Modeled estimate from usability testing, not a controlled test |
| Average checkout has 11.3 form fields (2024), down from 11.8 (2021) and 12.7 (2019); 8 fields are enough for most | Baymard [Study, 2024] | Counting rules matter (fields vs elements) |
| 64% of desktop sites, 63% of mobile sites and 46% of apps rate "mediocre" or worse on checkout UX | Baymard benchmark update 2025-11 [Study, 2025-11] | Large US and EU retailers |
| Research base: 272 think-aloud sessions, eye tracking, 850+ checkout steps benchmarked, 9 quantitative studies with 11,777 participants | Baymard [Study, 2025] | |

### Reasons for abandonment during checkout (Baymard, US adults)
Two denominators circulate. Quote the one you use.

| Reason | Share of US online shoppers who abandoned in last 3 months (approx.) | Share excluding "just browsing" (commonly cited) |
|--------|-----------------------|----------------------------|
| Just browsing or not ready to buy | about 42% to 43% | excluded |
| Extra costs too high (shipping, tax, fees) | about 39% to 40% | 48% |
| Site wanted me to create an account | | 26% |
| Did not trust the site with my card details | about 19% | 25% |
| Delivery too slow | about 20% | 23% |
| Checkout too long or complicated | | 22% |
| Could not see or calculate total cost upfront | | 21% |
| Website had errors or crashed | | 17% |
| Returns policy not satisfactory | | 15% |
| Not enough payment methods | | 13% |
| Card declined | | 9% |

[Study, Baymard 2024 to 2025; secondary sources disagree on exact values, verify on baymard.com/lists/cart-abandonment-rate before quoting externally]. The pattern is stable: surprise costs, forced accounts, trust, delivery speed and checkout length dominate.

## 2. Funnel metrics to track

| Metric | Formula | Notes |
|--------|---------|-------|
| Session CVR | orders / sessions | Headline; mix-sensitive |
| Revenue per visitor (RPV) | revenue / sessions (or users) | Primary metric for most ecommerce tests |
| Add to cart rate | sessions with add_to_cart / sessions | PDP effectiveness |
| Cart to checkout rate | sessions with begin_checkout / sessions with add_to_cart | Cart effectiveness and cost transparency |
| Checkout completion | purchases / sessions with begin_checkout | Checkout UX, payment, costs |
| Payment failure rate | failed payment attempts / attempts | Gateway, 3DS, fraud rules |
| AOV | revenue / orders | Guardrail on discount and bundle tests |
| Return rate | returned orders / orders | Guardrail on PDP claims and fit tools |

## 3. Collection and category pages
- Product cards show: image (second image on hover desktop), name, price and savings, rating with count, key variant swatches, badges (only meaningful ones: "Best seller", "New").
- Filters relevant to the category (size, fit, material, price, use case); show applied filters as removable chips; on mobile, filter button sticky; show result counts.
- Sort default "Best selling" or "Recommended", not "Newest" unless fashion drops.
- Load more or pagination: either works; keep scroll position on back navigation (bfcache helps; see [Speed](speed-and-core-web-vitals.md)).
- Paid traffic to collections (PMax, AI Max, Meta catalog) needs a short intro and the products the ad promised first.
- Site search: autocomplete with product thumbnails, synonyms and misspellings handled, no dead "0 results" page (show best sellers and contact).

## 4. Product detail page (PDP) checklist

### Above the fold (mobile)
- [ ] Product title clear; matches ad or feed.
- [ ] Primary image shows the product clearly; gallery swipeable; 6 or more images including in-scale and in-use photos; video where demonstration helps.
- [ ] Price, savings, unit price where required by law (EU), stock status.
- [ ] Rating stars with review count, tap scrolls to reviews.
- [ ] Variant selectors as buttons or swatches, not dropdowns, for 2 to 10 options; unavailable variants visible but marked.
- [ ] Add to cart button full width; sticky on mobile after scroll.
- [ ] Delivery estimate ("Get it by Thu 16 Oct") and shipping cost or free shipping threshold.
- [ ] Returns line and guarantee near the button.
- [ ] Express payment buttons (Shop Pay, Apple Pay, Google Pay, PayPal) where they do not distract from add to cart; test.
- [ ] Installment messaging if offered.

### Below the fold
- [ ] Benefits in scannable bullets, then details.
- [ ] Specs table (dimensions, materials, compatibility). AI assistants and comparison shoppers need this.
- [ ] Size guide with fit advice and model measurements; fit predictor for apparel if returns are high.
- [ ] Reviews: filter by rating, sort by most helpful, show photos, show negative reviews (hiding them is illegal under the FTC reviews rule and reduces trust).
- [ ] Q&A or FAQ from support tickets.
- [ ] UGC photos or short videos.
- [ ] Cross-sell (complete the look, frequently bought together) below the main purchase area.
- [ ] Shipping, returns, warranty details in expandable sections.
- [ ] Structured data (Product, Offer, AggregateRating) correct; hand to `seo` for validation.

## 5. Cart

| Rule | Why |
|------|-----|
| Show estimated total including shipping and taxes as early as possible | Surprise costs are the top abandonment reason |
| Free shipping progress bar ("$12 away from free shipping") | Raises AOV when the threshold is reachable; test the threshold |
| Express checkout buttons in cart | Skips forms for wallet users |
| Easy quantity edit and remove; save for later | Reduces frustration |
| Product thumbnails and variant details | Confirms the right item |
| Promo code field collapsed as a link ("Have a code?") | An open field sends visitors to search for coupons [Practitioner consensus, Baymard] |
| Trust and returns line near checkout button | Reduces anxiety |
| Cart drawer vs cart page | Drawer keeps shopping momentum; page gives space for reassurance. Test; keep a full cart page reachable |
| Upsells limited to 1 to 3 relevant items | Too many distract from checkout |

## 6. Checkout

### 6.1 Rules
1. Guest checkout is the default, visible option. Offer account creation after purchase (one click, password only).
2. Minimum fields: email, shipping address (with autocomplete), shipping method, payment. Single name field or two; address line 2 collapsed; company field collapsed.
3. Address autocomplete and postal code lookup where available.
4. Shipping options show cost and delivery date, not just "Standard".
5. Payment methods match the market (table below). Wallets first on mobile.
6. Order summary always visible (collapsed on mobile with total).
7. Inline errors that preserve entered data; card errors explained in plain language.
8. No exits: minimal header, no navigation, no popups.
9. Trust: security note near card fields, recognizable payment logos, contact option.
10. Total price including all mandatory fees shown before the final step; no new fees at the last step.

### 6.2 Payment methods by market (verify with the payment provider before changing)
| Market | Methods to offer beyond cards |
|--------|-------------------------------|
| US | Apple Pay, Google Pay, PayPal and Venmo, Shop Pay (Shopify), BNPL (Klarna, Afterpay, Affirm) |
| UK | Apple Pay, Google Pay, PayPal, Klarna, Clearpay |
| Netherlands | iDEAL (dominant), cards, PayPal |
| Belgium | Bancontact |
| Germany | PayPal, Klarna (invoice), SEPA, cards |
| Poland | BLIK, Przelewy24 |
| Nordics | Klarna, Vipps or MobilePay, Swish (Sweden) |
| Brazil | Pix, boleto, installments on cards |
| India | UPI, cards, wallets |
| Turkey | Installments on cards (taksit), local cards |

Shopify states Shop Pay can lift checkout conversion substantially versus guest checkout (vendor claim, figures vary by publication) [Official vendor claim, unverified magnitude]. Test wallet ordering and visibility rather than assuming.

### 6.3 Mobile checkout
- Large inputs, correct keyboards (`autocomplete` values: `email`, `shipping street-address`, `postal-code`, `cc-number`, `cc-exp`, `cc-csc`).
- Wallet buttons at the top of checkout.
- Avoid dropdowns for country or state when autocomplete can fill them.
- Test in Meta, Instagram and TikTok in-app browsers; wallet availability differs.

## 7. Shopify specifics (constraints as of 2026-10)

| Topic | Current state | Source |
|-------|--------------|--------|
| checkout.liquid | Deprecated for the information, shipping and payment pages (Plus) since August 2024; replaced by checkout extensibility | [Official, Shopify 2024] |
| Thank you and Order status pages | Plus deadline 28 August 2025; non-Plus deadline 26 August 2026. Unupgraded stores were auto-upgraded and lost Additional Scripts, script tags and checkout.liquid customizations on those pages | [Unverified post-deadline behavior; pre-deadline secondary sources 2026] |
| Customization on core checkout steps | Checkout UI extensions on information, shipping and payment steps are Shopify Plus only | [Secondary sources 2026; verify on shopify.dev] |
| Customization for all plans | Checkout and accounts editor branding (colors, fonts, logo), app blocks on Thank you and Order status pages | [Secondary sources 2026] |
| Tracking | Web Pixels: app pixels preferred, custom pixels (sandboxed) as fallback; legacy Additional Scripts gone. Verify purchase events after the August 2026 deadline | [Secondary sources 2026] |
| Logic | Shopify Functions for discounts, delivery and payment customization (hide, reorder, rename methods) | [Official, shopify.dev] |
| Native A/B testing | Rollouts: server-side split of theme variants; first in Winter '26 Edition, expanded in June 2026 to whole themes plus checkout and customer account configurations; revenue per visitor as primary metric; no audience targeting; no confidence intervals; cannot test pricing or discount logic; plan availability reported inconsistently | [Unverified, secondary sources 2026] |
| Price and shipping tests | Third-party apps (for example Intelligems) | [Unverified capabilities, check app listing] |
| Theme tests with targeting and stats | Third-party apps (for example Shoplift) or full platforms (Optimizely, Wingify VWO, Convert) | [Unverified, check app listing] |

Post-August 2026 audit for every Shopify store (high priority):
1. Settings > Checkout: confirm Thank you and Order status pages are on the new version and note what was removed.
2. Place a test order; verify GA4 `purchase`, Meta Purchase, Google Ads conversion, TikTok and other pixels fire once with correct value and currency (with `measurement`).
3. Rebuild post-purchase surveys, upsells and tracking as app blocks or pixels.

Shopify CRO quick wins (theme level): reduce apps that inject scripts on every page; preload the hero or main product image; use `image_url` with widths and `image_tag` with `sizes`; avoid heavy review widgets above the fold (render stars server side); sticky add to cart; delivery date estimate app or metafield.

## 8. Other platforms
- WooCommerce: Cart and Checkout blocks are the default for new stores since WooCommerce 8.3 (Nov 2023) [Official, 2023-11]; classic shortcode checkouts still exist on older stores. Plugin bloat and uncached cart fragments hurt speed.
- BigCommerce, Adobe Commerce (Magento), Salesforce Commerce Cloud: checkout customization is more open; test with server-side or platform-native tools.
- Headless (Next.js storefronts, Hydrogen): full control of PDP and cart; checkout often remains platform hosted (Shopify checkout for Hydrogen).

## 9. Post-purchase
- Thank you page: order summary, delivery date, account creation with one click, post-purchase survey ("What almost stopped you?"), referral offer, post-purchase upsell only if relevant and one-click.
- Order confirmation email within one minute; tracking link.
- Measure repeat purchase rate per acquisition source; hand to `growth-orchestrator`.

## 10. Agentic commerce (watch)
AI agents now browse and buy for users (for example ChatGPT Instant Checkout via the Agentic Commerce Protocol announced September 2025) [Unverified, verify current scope]. Implications for CRO: product data, prices, availability, shipping and return policies must be machine-readable and consistent across feed, page and structured data; checkout must not depend on visual-only cues. Coordinate with `commerce-feeds` and `ai-search-optimization`.

## 11. Ecommerce test backlog starters (rank with [Prioritization](prioritization-and-playbooks.md))
| Area | Test idea | Primary metric | Guardrail |
|------|-----------|----------------|-----------|
| PDP | Delivery date estimate near add to cart | Add to cart rate, RPV | Returns |
| PDP | Reviews summary and photo reviews above the fold | RPV | Page speed |
| PDP | Bundle selector (1, 2, 3 packs with savings) | RPV, AOV | Margin per visitor |
| Collection | Product cards with rating and key benefit | Click to PDP, RPV | |
| Cart | Free shipping progress bar with threshold test | RPV, AOV | Margin |
| Cart | Express checkout buttons in cart drawer | Checkout completion | |
| Checkout | Shipping cost shown on PDP and cart (no surprise) | Checkout completion | |
| Checkout | Payment method order by market | Checkout completion | Payment failure rate |
| Sitewide | Remove or delay non-critical apps and tags | RPV, LCP, INP | Tracking completeness |
| Offer | Guarantee length (30 vs 60 vs 100 days) | RPV | Return rate |
