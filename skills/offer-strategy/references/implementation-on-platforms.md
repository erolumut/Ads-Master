# Implementing Offers on Commerce and Billing Platforms

> Offer-strategy writes the offer specification and picks the mechanism. `site-engineer` builds, previews, QAs and releases it; `storefront-ux` builds the display; `commerce-feeds` handles feed promotions and sale prices. Creating or editing live discounts, prices and shipping rates is G3; drafting a discount that is inactive or scheduled is G2 (see `ads-master/GUARDRAILS.md`).

## 1. Shopify (state as of 2026-10)

| Need | Mechanism | Notes |
|------|-----------|-------|
| Percent or amount off products or collections | Native discount: Amount off products (code or automatic) | Product discount class |
| Order level discount, tiered spend | Native Amount off order; tiers usually need an app or a Discount Function | Order discount class |
| Buy X get Y, gift with purchase | Native Buy X get Y (gift at 100% off); automatic adds may need an app or Cart Transform | Gift must be a stocked SKU |
| Free shipping | Native Free shipping discount or shipping profile rates with order price conditions | Shipping discount class; shipping rate conditions are the cleaner always-on threshold |
| Combining discounts | Each discount declares which classes it combines with (product, order, shipping) | Shoppers can use up to 5 product or order codes plus 1 shipping code per order; stacking works on Online Store, Storefront API and POS [Official, help center] |
| Limits | Up to 25 active automatic discounts including app-created ones; a store can activate at most 25 discount functions [Official, 2024 to 2025] | Plan the promo stack; retire old automatic discounts |
| Custom logic (tiers by segment, complex BOGO, bundles pricing) | Discount Function API (unified product, order and shipping logic in one function since API version 2025-04) [Official, 2025-05] | Built by `site-engineer` or an app; standalone shipping discount function API is deprecated |
| Former Shopify Scripts | Scripts sunset 2026-06-30; published Scripts were deactivated; Script Editor access ended 2026-07-30 [Official, 2026] | Audit Plus stores for silent discount failures and double discounting after migration |
| Fixed bundles and multipacks | Shopify Bundles app (free, fixed bundles and multipacks); limits reported at about 30 components and 100 variants per bundle [secondary, verify] | Mix and match needs a Cart Transform based app |
| Mix and match bundles | Apps built on the Cart Transform Function API; set requiresComponents on parent variants that cannot sell alone [Official] | Feed handling via `commerce-feeds` |
| Market specific prices | Shopify Markets price lists, rounding rules, market specific discounts | Check prior price rules per market |
| B2B prices | B2B catalogs and price lists (Plus) | Keep B2B prices out of consumer feeds |
| Subscriptions | Shopify Subscriptions app, Recharge (reported to be acquiring Skio, May 2026 [Unverified]), Loop, others | Selling plans; check portal features (skip, swap) |
| Post-purchase upsell | Post-purchase extensions; Summer '26 Edition reportedly extended post-purchase upsells beyond Plus to Advanced and Shopify plans [Unverified, 2026] | Offer economics as in [Bundles](bundles-and-price-ladders.md) |
| Compare-at price | Product compare-at price field | Does not prove the 30 day low; keep a price history (see [Price display law](price-display-law-handoff.md)) |
| Price and offer tests | Third party apps (Intelligems, ABConvert, Elevate); native Rollouts tests themes and checkout configurations, not prices or discount logic, per 2026 reviews [Unverified] | Coordinate feed parity with `commerce-feeds` |
| AI channels | Shopify reports products syndicating to ChatGPT, Copilot, AI Mode and Gemini (Summer '26, secondary) | Offers and prices must be consistent everywhere the catalog appears |

Shopify discount spec (hand to `site-engineer`):

```
Discount ID / title (internal):         Customer facing title:
Type: amount off products | amount off order | buy X get Y | free shipping | function based
Method: code (code string) | automatic
Value: % or amount, per item or once per order
Applies to: collections / products / variants / exclusions
Minimum requirements: subtotal | quantity
Customer eligibility: all | segments | specific customers
Combinations: product yes/no, order yes/no, shipping yes/no
Usage limits: total uses, one per customer
Markets: which markets; currency rounding
Active dates: start and end with time zone
Sales channels: online store, POS, Shop app, others
Test cases: list of carts with expected totals (include stacking with welcome code, excluded SKUs, gift cards)
Rollback: deactivate discount ID; restore previous automatic discount if replaced
Approval: G3 for activation
```

## 2. WooCommerce

| Need | Mechanism | Notes |
|------|-----------|-------|
| Coupons | Core coupons: percentage, fixed cart, fixed product; usage limits, min and max spend, product and category rules, email restrictions | Coupons do not auto-apply without an extension or code |
| Sale prices | Product sale price with schedule dates | Keep price history for prior price claims |
| Free shipping threshold | Free shipping method with minimum order amount in a shipping zone | Per zone |
| Tiered and dynamic pricing | Extensions (for example WooCommerce Dynamic Pricing or similar) | Test stacking with coupons |
| Bundles | Official Product Bundles extension (simple, variable and subscription items; bulk discounts) or third party | Inventory sync per component |
| Subscriptions | WooCommerce Subscriptions extension | Renewal and cancellation flows must meet subscription law |
| Gifts | Extensions or a 100% coupon on a gift product with conditions | Stock control |
| Prior price compliance | Plugins that store lowest price history | Verify plugin accuracy against an export |

Every WooCommerce change goes through staging first (`site-engineer`), because plugin conflicts often break cart totals.

## 3. Other commerce platforms (quick map)

| Platform | Promotions | Bundles | Notes |
|----------|-----------|---------|-------|
| BigCommerce | Promotions engine (automatic and coupon), tiered pricing via price lists | Apps | Check promotion stacking rules |
| Adobe Commerce (Magento) | Catalog price rules and cart price rules, coupon generation | Bundle product type native | Rule priority and "discard subsequent rules" settings decide stacking |
| Salesforce Commerce Cloud | Promotions and campaigns with qualifiers | Product sets and bundles | Enterprise; changes via release process |
| Custom or headless | Promotion service or commerce engine rules | Depends | Cache and ISR can show stale prices (see `site-engineer`) |

## 4. SaaS billing

| Need | Stripe Billing | Chargebee or Paddle | Notes |
|------|----------------|---------------------|-------|
| Free trial with or without card | Subscription trial settings; checkout can collect a payment method only when needed | Trial configurations per plan | Card required trials need consent and reminders (subscription law) |
| Coupons and promotion codes | Coupons (percent or amount, duration once, repeating or forever) and customer-facing promotion codes | Coupons and promo codes | Duration matters: "50% off for 3 months" must say so |
| Annual vs monthly | Separate prices on the same product | Plan variants | Show effective monthly price and the annual total |
| Usage and credits | Metered prices and credit grants; Stripe completed its Metronome acquisition in January 2026 [Unverified] | Usage based billing | Show usage in product |
| Price changes for existing customers | Migrate subscriptions at renewal or schedule updates | Same | Notice periods by contract and law |

## 5. Marketplaces and feeds (handoff)

| Item | Owner | Offer-strategy provides |
|------|-------|-------------------------|
| Google Merchant Center promotions, sale price and sale price effective dates | `commerce-feeds` | Offer dates, eligible SKUs, promo text, codes |
| Price parity between feed, landing page and checkout | `commerce-feeds`, `site-engineer` | List of price changes with timestamps |
| Amazon deals, coupons, Subscribe and Save | Human or marketplace manager | Economics and channel conflict check |
| Trendyol, Hepsiburada, bol campaigns | Human | Which events to join, max funded discount |
| Ad promotion assets (Google promotion assets, Meta offers) | Channel agents | Exact offer wording approved by `compliance` |

## 6. Launch QA checklist for an offer (with `site-engineer`)
- [ ] Every test cart in the spec returns the expected total, including tax and shipping.
- [ ] Stacking: welcome code plus sitewide promo plus loyalty behaves as specified.
- [ ] Excluded SKUs (gift cards, new launches, low margin) do not discount.
- [ ] Gift SKU adds, has stock, ships with the order, and is handled on returns as the terms say.
- [ ] Prices and offer text match across ad, landing page, PDP, cart, checkout, feed and email.
- [ ] Reference prices match the prior price evidence file.
- [ ] Unit prices show on multipacks where required.
- [ ] Offer starts and ends at the stated time in each market's time zone.
- [ ] Discount usage, offer tags and order notes reach the backend export (`measurement`).
- [ ] Rollback tested: deactivating the discount restores normal prices without cache delays.
- [ ] Change request approved line by line; actions logged in `ads-master/logs/actions.jsonl` by the hook.

## 7. Implementation mistakes that cost money
- Leaving an old automatic discount active that stacks with the new promo.
- Migrating a Shopify Script to a Function and leaving both active for a window (double discounts).
- Gift with purchase without stock reservation: orders ship without the gift, complaints follow.
- Free shipping discount that applies to heavy or international zones by accident.
- Codes without usage limits shared on coupon sites.
- Price changes on the site without a matching feed update, causing Merchant Center disapprovals.
- Ending a promo by editing the discount value instead of deactivating it, which breaks reporting history.

## 8. Offer ID and naming convention

Use one ID across the brief, EXPERIMENTS.md, discount titles, codes, order tags and reports so analysis never depends on guesswork.

```
Format: OF-<YYYYMM>-<market>-<type>-<short name>
Types:  FO (first order), SW (sitewide), BN (bundle), GW (gift), FS (free shipping), SB (subscription), LO (loyalty), CL (clearance), PT (price test)
Example: OF-202611-NL-SW-blackfriday25
Code example: BF25NL (public) or unique codes generated per partner with the prefix OF-202611-NL-PA
Order tag: offer:OF-202611-NL-SW-blackfriday25
```

## 9. Rollback runbook for a live offer incident
1. Deactivate the discount or revert the price list (keep the object; do not delete it, deletion is G4 and loses history).
2. Purge caches or force a rebuild where the storefront caches prices (`site-engineer`).
3. Pause ads that promote the offer (channel agents, with human approval).
4. Update feeds and remove feed promotions (`commerce-feeds`).
5. Record the affected order range; decide with the human whether to honor mispriced orders (often required or wise).
6. Write an incident row in `ads-master/INCIDENTS.md` and a journal entry.
