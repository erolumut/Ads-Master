# Pricing Research and Live Price Tests

> Stated willingness to pay is a hypothesis; revealed behavior is evidence. Use surveys to find the range, then confirm with a test that respects law, platform rules and customer trust.

## 1. Method selection

| Method | Answers | Sample | Cost and time | Weakness |
|--------|---------|--------|---------------|----------|
| Customer interviews (10 to 20) | Value drivers, alternatives, how they judge price | 10 to 20 | Low, 1 to 2 weeks | Not quantitative |
| Van Westendorp Price Sensitivity Meter | Acceptable price range | 150 to 400 per segment | Low, 1 to 2 weeks | No purchase intent, no competitive context |
| Van Westendorp with Newton, Miller and Smith extension | Range plus rough demand and revenue curve | 200 to 400 | Low | Stated intent overstates purchase |
| Gabor Granger | Purchase likelihood at set prices, revenue maximizing price | 200 to 500 | Low | Single product, no context, hypothetical bias |
| Conjoint (choice based, CBC) | Trade-offs between price and features, WTP per feature, simulated share | Rule of thumb n >= 500 x c / (t x a) (Sawtooth: c = largest number of levels of any attribute, t = tasks, a = alternatives per task) | Medium to high | Design skill needed, still stated preference |
| MaxDiff | Ranking of features or benefits | 200 to 500 | Low to medium | No price on its own |
| BDM (Becker, DeGroot, Marschak) incentive compatible elicitation | Real WTP (respondent may actually buy) | 100 to 300 | Medium | Logistics; product must be deliverable |
| Live A/B price test | Revealed demand at price points | Traffic driven (see section 6) | Medium | Legal and platform constraints, trust |
| Geo or time based price test | Revealed demand by market or period | Markets or weeks | Medium | Confounding by market and season |
| Synthetic respondents (LLM panels) | Early exploration only | n/a | Very low | Systematic WTP errors (see section 4) |

## 2. Van Westendorp procedure

Questions (show the product description and a realistic image first; keep currency and tax basis explicit):
1. At what price would you consider the product so expensive that you would not consider buying it? (too expensive)
2. At what price would you consider the product to be priced so low that you would feel the quality could not be very good? (too cheap)
3. At what price would you consider the product starting to get expensive, so that it is not out of the question, but you would have to give some thought to buying it? (expensive)
4. At what price would you consider the product to be a bargain, a great buy for the money? (cheap)
Extension: 5. At the price you called a bargain, how likely are you to buy (5 point scale)? 6. Same at the price you called expensive.

Analysis:
- Plot cumulative distributions: "too cheap" and "cheap" descending, "expensive" and "too expensive" ascending.
- Point of marginal cheapness (PMC): "too cheap" crosses "not cheap" (1 minus cheap).
- Point of marginal expensiveness (PME): "too expensive" crosses "not expensive" (1 minus expensive).
- Optimal price point (OPP): "too cheap" crosses "too expensive".
- Indifference price point (IPP): "cheap" crosses "expensive".
- Acceptable range: PMC to PME. Recommend testing 2 to 3 live prices inside the range, not choosing a single survey number.
- Clean data: drop respondents whose answers are not ordered (too cheap below cheap below expensive below too expensive).

## 3. Gabor Granger procedure
1. Pick 5 to 7 price points spanning the plausible range.
2. Ask purchase likelihood at a random starting price; move up after "yes", down after "no" (or show all prices in random order to separate groups to avoid order bias).
3. Demand curve: share "definitely or probably would buy" at each price. Revenue index = price x share; contribution index = (price minus variable cost) x share.
4. Calibrate: stated intent overstates actual purchase. Common practice discounts top box answers and heavily discounts second box answers; calibrate against your own launch data when you have it [Practitioner consensus]. Use the curve shape, not its level.
5. Choose the contribution maximizing price (not the revenue maximizing price), then test live.

## 4. Synthetic respondents: current evidence (2026)

| Evidence | Finding | Label |
|----------|---------|-------|
| Oetzel and Maiberger, Journal of Marketing Analytics 2026, benchmark vs BDM real WTP across four products | For hedonic products synthetic WTP was too high and implied over-optimistic demand and profit; for utilitarian products results ranged from close to substantially too low | [Study, 2026] |
| Diagnostics paper on LLM consumer panels (arXiv, 2026) | Aggregate metrics hide variance compression, coefficient sign flips and 10 to 30 point subgroup errors; a small human calibration sample (n = 50 to 300) reduced bias substantially | [Study, 2026], preprint |
| Earlier conjoint WTP work | Off-the-shelf LLM WTP often wrong in sign or size; fine tuning on category conjoint data helps | [Study], preprints |
| Vendor claims of up to 90% alignment | No public method | [Unverified] |

Rule: synthetic panels may generate hypotheses and questionnaire drafts. Never set or change a price from synthetic data alone; validate with a human sample and then a live test.

## 5. Price elasticity from your own data
- Use past price changes, promotions and markdowns as natural experiments. Estimate arc elasticity: `E = (%change in units) / (%change in price)`, using a comparison period that controls for season (same weeks last year, or a control SKU or market).
- Exclude periods with stockouts, ad budget changes above 20%, or site incidents.
- Elasticity from promotions overstates elasticity of list price changes (promotions add urgency and visibility). Label it.
- Contribution maximizing price for constant elasticity: `P* = MC x E / (E + 1)` for E below minus 1 (MC = marginal variable cost per unit). Use only as a sanity check.

## 6. Live price tests: designs and limits

| Design | How | Pros | Cons and risks |
|--------|-----|------|----------------|
| Visitor level A/B on list price | Random visitors see price A or B (app such as Intelligems, ABConvert or Elevate on Shopify; feature flags on custom stacks) | Fast causal read | Different customers see different prices at the same time: trust risk, social sharing, legal review needed; feed price mismatch for Shopping traffic |
| A/B via discount instead of list price | Same list price; variant gets an automatic discount | No list price mismatch; easy rollback | Tests a discount, not a list price; reference price rules for the discount claim |
| New SKU or bundle price test | Launch a new bundle or size at test prices | Low risk to existing reference prices | Less general |
| Geo split | Different prices by market or region (separate currencies or storefronts) | Clean separation | Markets differ; EU Geo-blocking Regulation forbids discriminating by nationality or residence for the same offer, so only separate offers per storefront and market with clear disclosure |
| Time split (switchback) | Alternate price by week | Works on low traffic | Seasonality, carryover, returning visitor confusion |
| Sequential rollout (pre and post) | Change price, compare to forecast or synthetic control | Simple | Weakest causal design |

Platform constraint: Google Merchant Center requires the price in the feed to match the landing page price the user sees; visitor level price tests can trigger price mismatch disapprovals. Mitigate by excluding Shopping and PMax traffic from the test, by testing through discounts at checkout instead of list price, or by testing on SKUs not in the feed. Coordinate with `commerce-feeds` before any list price test [Practitioner consensus]. Shopify's native Rollouts tests themes and checkout configurations but not prices or discount logic, according to 2026 secondary reviews [Unverified, 2026].

## 7. Legal limits on price tests and personalized prices (hand to `compliance`)

| Jurisdiction | Rule that touches price tests | Status Oct 2026 |
|--------------|-------------------------------|-----------------|
| EU | Consumer Rights Directive as amended by the Omnibus Directive: inform consumers when a price was personalized on the basis of automated decision-making | In force since 2022-05-28 [Official, 2019] |
| EU | Geo-blocking Regulation 2018/302: no different general conditions, including prices, based on nationality or place of residence for the same offer | In force [Official, 2018] |
| EU | Digital Fairness Act: expected to address unfair personalization and dark patterns | Proposal expected Q4 2026, not yet tabled as of mid-September 2026 [Official plan, 2026] |
| New York | Algorithmic Pricing Disclosure Act: prices set by an algorithm using personal data must show "THIS PRICE WAS SET BY AN ALGORITHM USING YOUR PERSONAL DATA." | In effect since 2025-11-10; survived a First Amendment challenge, appeal pending [Official, 2025] |
| New York | One Fair Price Act (ban on surveillance pricing, carve-outs for bona fide discounts, loyalty, coupons, subscribe and save) | Passed legislature June 2026; awaiting signature as of August reporting [Unverified status] |
| Maryland, Connecticut, New Jersey | Surveillance pricing restrictions (food retail focus in Maryland and Connecticut; New Jersey broader with private right of action from 2027-08-01) | Enacted 2026, various dates [Official, 2026] |
| US federal | FTC surveillance pricing study (2025) and a reported April 2026 ANPRM on personalized pricing disclosure | Monitor [Unverified] |
| UK | DMCC Act unfair practices regime; misleading pricing enforcement by the CMA | In force since 2025-04-06 [Official, 2025] |

Practical rules:
1. Random A/B assignment is not the same as personalization from personal data, but regulators and journalists may not see the difference. Instacart stopped item price testing in December 2025 after a Consumer Reports and Groundwork study found price differences of up to 23% for identical items, and the New York AG questioned its disclosures in January 2026 [Official, 2026-01].
2. Prefer tests that do not show two different list prices for the same item at the same time: discount tests, new SKU tests, geo or time splits.
3. If a visitor level list price test is approved, keep it short, cap the price gap, honor the lower price for anyone who complains, and exclude logged in repeat customers.
4. Never use protected attributes, health or financial vulnerability, or device type as a price input.

## 8. Price test plan template

```
Test ID (EXPERIMENTS.md):
Question: what price (or offer) maximizes contribution per visitor for <product or range>?
Prices or offers tested:            Control:
Design: visitor A/B | discount A/B | new SKU | geo | switchback | pre/post
Traffic included / excluded (Shopping, PMax, logged in customers, B2B):
Primary metric: contribution per visitor (CM2 per session) over the test window
Secondary: conversion rate, AOV, units per order, new customer share
Guardrails: refund and return rate, support contacts about price, feed disapprovals, chargebacks
Sample size and duration (see offer-testing-and-measurement.md):
Legal review: compliance sign off ID, disclosure text if any
Feed coordination: commerce-feeds sign off
Rollback: how to revert in under 15 minutes
Stop rule: harm on guardrails, disapprovals, or complaints above <n>
Approvals: price changes are G3 (human approves each line)
```

## 9. Research report template (pricing)

```
# Pricing research: <product> | Date | Data sources and dates
## Summary (3 to 5 bullets, with recommended test prices)
## Method and sample (who, how recruited, incentive, exclusions)
## Value drivers and alternatives (from interviews)
## Price range (Van Westendorp chart and points)
## Demand curve (Gabor Granger or conjoint simulator) with contribution index
## Competitive context (from market-intel, dated)
## Recommendation: prices to test, design, expected effect with uncertainty
## Risks: channel conflict, legal, brand
```
