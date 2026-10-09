# Commercial Pricing Method (end to end)

> Owns: the consulting process from intake to the Commercial Pricing Report. Every pricing engagement follows these phases in order. Skipping a phase is allowed only when its output already exists in `ads-master/` and is less than 90 days old (30 days in Turkey or any market with inflation above 10%).

The output style is a senior commercial consultant's recommendation: "You sell at X today. Competitors and retailers sell at Y. Your strengths and weaknesses are these. Your costs are these. So set the minimum basket at N, offer free delivery above Z, sell at this price ladder, and here are the margin and the risks." Every sentence of that statement must trace back to a phase below.

## Phase map

| Phase | Question | Output | Reference |
|-------|----------|--------|-----------|
| 0. Frame | What decision is being made, by when, for which channels and markets? | Decision statement, scope, constraints | This file, section 1 |
| 1. Intake | What do we sell, at what prices, through which channels, at what cost? | Intake sheet with sources | Section 2 |
| 2. Current state | What does the customer pay today, per unit, by channel, and what do we earn? | Current price map, current CM2 by basket | [Cost to serve](cost-to-serve-and-margin-waterfall.md) |
| 3. Market | What do competitors and retailers charge per unit, how often on promotion, with which delivery terms? | Normalized benchmark table, price index | [Competitive benchmarking](competitive-price-benchmarking.md) |
| 4. Positioning | Where do we stand on value, and what price position can we defend? | Positioning map, strengths and weaknesses with proof, positioning hypothesis | [Positioning maps](positioning-maps-and-strengths.md), [Value based pricing](value-based-pricing-and-wtp.md) |
| 5. Cost basis | What does each basket cost to serve, what is the minimum viable basket? | Margin waterfall, script output | [Cost to serve](cost-to-serve-and-margin-waterfall.md) |
| 6. Architecture | Which packs, tiers and price points, and what per unit curve? | Price ladder with CM2 per rung | [Architecture](price-architecture-and-pack-sizes.md) |
| 7. Delivery policy | Minimum order, delivery fee, free delivery threshold, letterbox formats | Policy with economics | [Minimum basket](minimum-basket-and-delivery-policy.md) |
| 8. Channels | How do DTC, retail and marketplace prices relate? | Channel corridor, conflict check | [Channel corridors](channel-price-corridors.md) |
| 9. Launch and change economics | What does the launch or change cost, what volume is needed? | Launch economics, breakeven volume, change plan | [Price changes](price-changes-and-inflation.md), handoff to `offer-strategy` for incentives |
| 10. Validation | How do we know the price is right after launch? | Test plan, KPIs, review dates | [Elasticity and tests](elasticity-and-price-tests.md) |
| 11. Report | One document the human can decide from | Commercial Pricing Report | [Report template](commercial-pricing-report-template.md) |

## 1. Frame the decision (phase 0)

Write one sentence before any analysis: "Decide [price level / ladder / minimum order / threshold / channel corridor / increase] for [SKUs] in [markets and channels] by [date], within [constraints]."

Typical decisions:
- New DTC launch next to an existing retail listing (the Amara pattern).
- New market entry (price localization, VAT, carrier, competitors).
- Cost shock (COGS, carrier, FX) requiring a price increase or a pack change.
- Marketplace entry (price parity, fees, featured offer).
- SaaS packaging or tier change; B2B price list renewal.
- Margin rescue: contribution below floor.

Constraints to capture: contracts with retailers (listing terms, promo commitments), existing reference prices (prior price rules), committed customer prices (subscriptions, B2B contracts), stock and MOQs, legal markets, the human's risk appetite.

## 2. Intake (phase 1)

Ask only what is not in `ads-master/`. Minimum facts, in order of importance:

| # | Fact | Where to look first | Why it matters |
|---|------|---------------------|----------------|
| 1 | Products, pack sizes, current prices incl VAT by channel | PROJECT_BRIEF.md sections 1 and 2, site, backend | Current state |
| 2 | Full cost per unit (landed COGS) from the internal cost sheet | PROJECT_BRIEF.md section 3, data/imports/ | Margin floor |
| 3 | Fulfillment and carrier contract (bands, surcharges), packaging | 3PL and carrier invoices | Cost to serve |
| 4 | Payment method mix and PSP | PSP payout report | Fixed vs percent fees |
| 5 | Retail partners: shelf price observed, sell-in price, retailer margin, trade terms | Retail contract, field checks | Channel corridor |
| 6 | Marketplaces and fees | Seller center | Channel corridor |
| 7 | 12 month order export with basket size, shipping charged, discounts | data/imports/ (HOW_TO_EXPORT.md) | Basket distribution, AOV |
| 8 | Competitor set (3 to 8 named) and where they sell | COMPETITORS.md, `market-intel` outputs | Benchmark |
| 9 | Positioning claims with proof | BRAND.md, brand/PRODUCT_FACTS.md, CLAIMS.md | Value story |
| 10 | Targets: CM2 floor, payback horizon, volume ambitions | STRATEGY.md | Floor and trade-offs |
| 11 | Markets, currencies, VAT classes | PROJECT_BRIEF.md | Normalization |
| 12 | Price history (last 90 days per SKU and channel) | Backend, feed history | Legal reference prices |

Intake conventions (from the owner's costing tool, see [Cost to serve](cost-to-serve-and-margin-waterfall.md) section 1b): record every cost with its "as of" date; resolve blanks by inheritance (product, then brand, then company default), never as zero; if a required cost is still missing, mark the analysis INCOMPLETE and list the missing inputs instead of estimating silently; label every percentage as margin_on_price or markup_on_cost.

Cold start: when `ads-master/` is missing, ask for items 1, 2, 3, 5 (if retail exists), 8 and 10 only, then proceed with labeled assumptions for the rest.

## 3. Current state (phase 2)

Build the current price map:

| SKU or pack | Channel | Price incl VAT | Units | Price per unit incl VAT | Price per 100 g or per serving | Delivery fee | Free delivery threshold | Promo in last 90 days |
|-------------|---------|----------------|-------|-------------------------|-------------------------------|--------------|-------------------------|-----------------------|

Then current CM2 by the three most common basket sizes (from the order export) using the script. State the share of orders below the minimum viable basket. That share is the size of the minimum order problem.

## 4. Market (phase 3)

Request a `market-intel` handoff for raw competitor data when it does not exist or is older than 30 days. Normalize it yourself ([Competitive benchmarking](competitive-price-benchmarking.md)): per unit, per 100 g or serving, per active ingredient where relevant, ex VAT for cross-border, shelf vs online, regular vs promo, delivery-inclusive price for the typical basket.

Deliver a price index: our price per unit / median competitor price per unit x 100, for regular and effective (promo-weighted) prices.

## 5. Positioning (phase 4)

1. List strengths and weaknesses with proof (fact, source). Adjectives without proof are not strengths.
2. Place the brand and competitors on two maps: price per unit vs perceived value or quality signal, and price per unit vs a differentiating attribute (protein per bar, natural ingredients, organic certification, speed, service level).
3. Write a positioning hypothesis: "We are [segment] for [customer] who value [attribute]. Our defensible price position is [premium, parity, value] at index [range] vs [reference set]."
4. Test the hypothesis against willingness to pay evidence where available ([Value based pricing](value-based-pricing-and-wtp.md)).

## 6. Cost basis (phase 5)

Run [Cost to serve](cost-to-serve-and-margin-waterfall.md). Required outputs: CM2 per basket, minimum viable basket under charged and free delivery, sensitivity table.

## 7. Architecture (phase 6)

Design the ladder ([Architecture](price-architecture-and-pack-sizes.md)):
- Entry rung: low commitment, high per unit price, clears the floor.
- Hero rung: the default most customers should choose; the best value story.
- Stock up rung: lowest per unit price, highest CM2 per order, stock and cash checked.
Each rung earns more CM2 per order than the one below; per unit price steps of about 5 to 12% between rungs are a working range [Practitioner consensus]. Check price endings ([charm and round pricing evidence](price-architecture-and-pack-sizes.md)).

## 8. Delivery policy (phase 7)

Set: minimum order value (or bundle-only assortment), delivery fee below the threshold, free delivery threshold, express options. The threshold must be at or above the economic minimum (script section 3) and sit sensibly against competitor thresholds and current AOV ([Minimum basket](minimum-basket-and-delivery-policy.md)).

## 9. Channels (phase 8)

Build the corridor: DTC per unit price at each rung vs retail shelf per unit vs marketplace price. Decide the gap the brand will tolerate and how the DTC offer is differentiated (pack sizes not sold in retail, bundles, subscriptions, exclusive flavors) instead of undercutting ([Channel corridors](channel-price-corridors.md)). Never recommend controlling a reseller's price.

## 10. Launch and change economics (phase 9)

- Launch: model the intro period. Pricing-strategy sets the list price; `offer-strategy` designs the incentive (bonus product vs discount vs free delivery) and returns its cost. Pricing-strategy then checks the incentive does not break the corridor or reference price rules, and includes the combined economics in the report.
- Change: for an increase, compute allowable volume loss: i / (m + i) where m is the CM2 margin rate per unit and i the increase as a share of price. For a decrease, required volume gain: d / (m - d). Plan communication and grandfathering ([Price changes](price-changes-and-inflation.md)).

## 11. Validation (phase 10)

Pick the test design the traffic and legal situation allow ([Elasticity and tests](elasticity-and-price-tests.md)). Define the primary metric (contribution per visitor or per customer over 90 days), guardrails (conversion, return rate, retail sell-out), the review date and the kill criteria.

## 12. Report (phase 11)

Write the Commercial Pricing Report ([template](commercial-pricing-report-template.md)). End with decisions the human must make, each with options, the recommendation and what happens if they choose otherwise.

## Quality bar (every engagement)

- [ ] Every price is shown incl VAT (what the customer sees) and every margin ex VAT.
- [ ] Every competitor price is normalized per unit and dated, with the source (shelf check, site, marketplace) and whether it was a promo price.
- [ ] Cost inputs carry confidence grades A to D; C and D inputs have a sensitivity line.
- [ ] The minimum viable basket and threshold come from the script, not from intuition.
- [ ] Each ladder rung earns more CM2 per order than the rung below.
- [ ] The channel corridor is explicit and contains no instruction to resellers.
- [ ] Price display items (unit price, prior price, delivery cost display) are listed as a `compliance` handoff.
- [ ] Facts, interpretation and recommendation are separated.
- [ ] Decisions for the human are numbered with options and consequences.
- [ ] No live price, threshold or listing changed; G3 lines are in a change request.

## Timing guide

| Engagement | Effort | Notes |
|-----------|--------|-------|
| Quick price check (one SKU, one market) | 1 session | Phases 2, 3, 5, short report |
| DTC launch next to retail (Amara pattern) | 2 to 4 sessions | All phases; waits on `market-intel` data and cost sheet |
| New market entry | 2 to 3 sessions | Phases 1 to 8 for the new market; VAT, carrier, competitors are new |
| Price increase program | 1 to 2 sessions plus monitoring | Phases 2, 5, 9, 10 |
| SaaS packaging review | 2 to 4 sessions | [SaaS and B2B](saas-and-b2b-pricing.md) replaces phases 6 and 7 |

## Plays (launch, optimize, scale, recover)

### Play 1. DTC launch next to an existing retail listing (the Amara pattern)
1. Intake items 1, 2, 3, 5, 8, 10; shelf checks in 3 stores per retailer (photo, date).
2. Benchmark 3 to 8 competitors per unit and per 100 g; split performance, natural and own cluster.
3. Script: MVB charged and free; retail block with sell-in and trade spend.
4. Ladder: entry, hero, stock up; no single units if MVB says so; exclusive mixed boxes.
5. Delivery: fee below threshold, threshold aligned under the hero price.
6. Corridor: three options with per bar gaps and CM per bar by channel.
7. Launch incentive economics from `offer-strategy` (bonus bars vs discount vs free delivery).
8. Report with 5 decisions; change request after approval; journal entry for `storefront-ux`, `commerce-feeds`, `compliance`.

### Play 2. Margin rescue (CM2 below floor)
1. Rerun the waterfall with current dated costs; find the driver (COGS, carrier, payment mix, returns, fees).
2. Fix cost to serve first (carrier format, packaging, payment method default, minimum order).
3. Then architecture (remove loss making rungs, re-pack).
4. Then price (increase with allowable loss check and communication plan).
5. Track CM2 per order weekly for 8 weeks.

### Play 3. New market entry
1. VAT, carrier zones, payment methods and marketplaces for the market.
2. Local benchmark (never convert home prices by FX alone).
3. Local price points and endings; Shopify Markets rounding or fixed prices.
4. Zone specific threshold; legal display handoff for the market.

### Play 4. Marketplace entry
1. Fee model per marketplace (via `marketplaces` for current fees).
2. Marketplace pack that clears fees and does not undercut DTC or retail per unit.
3. Corridor rule for the brand's own store price.

### Play 5. Price increase program
See [Price changes](price-changes-and-inflation.md) sections 2 to 5 and worked examples.

### Play 6. Price level validation after launch
Monthly benchmark refresh, conversion and CM2 per visitor by rung, retail sell-out where available; pack or switchback tests per [Elasticity and tests](elasticity-and-price-tests.md).

### Play 7. Inflation market operating rhythm (Turkey)
Monthly cost index, repricing when the band is exceeded, weekly competitor captures, 10 day rule check before any discount communication, evidence file for every change.
