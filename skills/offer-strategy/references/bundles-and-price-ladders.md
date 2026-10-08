# Bundles, Multipacks and Price Ladders

> A good ladder lets each customer pick the amount they want to buy while every rung earns at least as much per order as the rung below. Build the ladder from unit economics, then test which rung becomes the default.

## 1. Bundle types

| Type | Definition | Use when | Watch |
|------|-----------|----------|-------|
| Multipack (same SKU x N) | 2, 3, 6 units of one product | Consumables, replenishment, gifting | Stockpiling lowers frequency; compare 90 day units per customer |
| Fixed bundle (curated set) | Defined set of different products | Routines (cleanse, tone, moisturize), starter kits, gift sets | Dead weight items lower perceived value |
| Mix and match | Customer picks N items from a set at a set price | Flavors, colors, scents | Inventory planning, app support |
| Starter kit | Hardware plus consumables, or core product plus accessories | Products with a refill or accessory business | Kit price anchors the refill price |
| Volume tiers | Unit price drops with quantity (1, 3, 5+) | B2B, wholesale-like DTC, supplements | Clear per unit display (EU and UK unit pricing rules) |
| Good, better, best tiers | Three versions with rising features | Products with natural feature tiers; SaaS plans | Middle tier must be the intended default |
| Product plus service | Item plus installation, setup, extended guarantee | High consideration, effort barriers | Service capacity and cost |
| Cross-category bundle | Pairs a hero with a slower seller | Introduce a second line | Slow seller must still add perceived value |
| DTC exclusive bundle | Configuration not sold by retail partners | Avoid direct price comparison with retail and marketplaces | Must be genuinely different (see [Channel conflict](channel-conflict-and-price-parity.md)) |

## 2. Unit economics of a ladder (worked example)

Inputs (illustrative, net of VAT, EUR): unit price 30, landed cost 8 per unit, pick and pack 3 per order plus 0.50 per extra unit, shipping 5 per order plus 0.80 per extra unit, payment 2% plus 0.25. Returns ignored for clarity.

| Rung | Price | Price per unit | Discount vs single | CM2 per order | CM2 per unit | CM2 % |
|------|-------|----------------|--------------------|---------------|--------------|-------|
| 1 unit | 30.00 | 30.00 | 0% | 13.15 | 13.15 | 43.8% |
| 2 pack | 54.00 | 27.00 | 10% | 27.37 | 13.68 | 50.7% |
| 3 pack at 24 per unit | 72.00 | 24.00 | 20% | 35.71 | 11.90 | 49.6% |
| 3 pack at 28 per unit | 84.00 | 28.00 | 6.7% | 47.47 | 15.82 | 56.5% |
| 5 pack at 21 per unit | 105.00 | 21.00 | 30% | 49.45 | 9.89 | 47.1% |
| 5 pack at 25 per unit | 125.00 | 25.00 | 16.7% | 69.05 | 13.81 | 55.2% |

What the table shows:
- Because pick, pack and shipping are mostly per order, a 2 pack at 10% off earns more per unit than a single. Moderate multipack discounts are often margin positive.
- Deep per unit discounts (3 pack at 20% off, 5 pack at 30% off) earn less per unit than the single. They only pay if they raise total units per customer over time, or if they win customers who would not buy otherwise.
- The question is never "is the 3 pack profitable", it is "what would this customer have bought instead". If most 3 pack buyers would have bought 2 single units over the next 90 days, the 3 pack at 20% off loses money.

Ladder rules:
1. Every rung earns CM2 per order above the rung below.
2. Per unit discount steps grow with diminishing increments (for example 0%, 10%, 15%, 20%), never jumps that make the middle rung look bad unless that is the intent.
3. Show price per unit on every rung (and the legally required unit price per kg, litre or item where it applies; see [Price display law handoff](price-display-law-handoff.md)).
4. The default selected rung (preselected option on PDP) is a business decision: test it. The display itself is owned by `storefront-ux`.
5. Free shipping should fall naturally on the target rung (for example the 2 pack crosses the threshold, the single does not).
6. Check stock depth for multipacks: a 5 pack promotion can drain inventory five times faster.

## 3. Bundle pricing methods

| Method | How | When |
|--------|-----|------|
| Sum minus discount | Bundle = sum of components x (1 minus d) | Simple, transparent; d usually 10% to 25% [Practitioner consensus] |
| Value based | Price at what the solved problem is worth; components hidden | Kits that solve a job, gift sets, routines |
| Anchor plus bonus | Price at the hero item's price, include a low cost extra | Protects reference price of the hero |
| Margin target | Bundle price = total landed cost / (1 minus target CM2 % minus variable cost %) | Ensures each bundle meets the contribution floor |
| Competitive | Set against a competitor's comparable bundle | Only with `market-intel` data, never as the only method |

Margin floor check for any bundle: `Bundle CM2 % >= max(core range CM2 % minus 5 points, the floor in STRATEGY.md)` unless the bundle is a deliberate acquisition offer with an acquisition investment budget.

## 4. Good, better, best design

| Step | Rule |
|------|------|
| 1. Define the value metric | What grows from tier to tier (quantity, features, service level, usage) |
| 2. Build the middle first | The tier most customers should pick; price it on value and margin |
| 3. Build the low tier as an entry, not a trap | It must be useful; a useless low tier creates complaints and refunds |
| 4. Build the high tier as an anchor and a real option | Some customers want the most; the high tier also makes the middle look reasonable (anchoring) |
| 5. Price gaps | Middle to high gap smaller in percent than the value gap; common practice: high tier 1.5x to 2.5x the middle [Practitioner consensus] |
| 6. Name tiers by who they are for | "Starter", "Family", "Pro" beat "Basic", "Premium" when the buyer identifies with the use case |
| 7. Track | Tier mix, CM2 by tier, refund rate by tier, upgrade rate |

Evidence: the compromise effect (preference for the middle option when it sits between two extremes) appears in many lab studies since Simonson 1989 [Study, 1989]; anchoring on a first number replicated well in Many Labs 1 (Klein et al. 2014) [Study, 2014]. Both effects are real in labs; their size in live pricing pages varies, so treat tier structure as a test.

## 5. Decoys: evidence quality and when to use them

| Claim | Evidence | Label |
|-------|----------|-------|
| Adding an asymmetrically dominated option raises share of the target option | Huber, Payne and Puto 1982; many lab replications with numeric attributes | [Study, 1982] |
| The effect is weak or absent with realistic, perceptual or qualitative stimuli | Frederick, Lee and Baskin 2014 and Yang and Lynn 2014 (11 reliable effects in 91 attempts) | [Study, 2014] |
| Meta-analysis still finds a significant average effect, with strong moderators | Milberg et al. 2014; Heath and Chatterjee 1995 (decoys help higher quality brands more) | [Study] |
| Field test on a flight aggregator (over 140,000 sessions) found no general attraction effect | 2021 field experiment | [Study, 2021] |
| Pricing page "decoy" tactics produce reliable lifts | Widely repeated, based on the Economist subscription anecdote | [Contested] |

Rule: do not add a fake option whose only job is to look bad. It wastes page space, can confuse, and if it misleads it is a legal risk. Add a third option only if some customers genuinely want it; then the anchoring effect is a bonus, not the reason.

## 6. Choice set size

Choice overload (the jam study, Iyengar and Lepper 2000) did not hold up as a general law: a meta-analysis found a mean effect near zero (Scheibehenne, Greifeneder and Todd 2010), and a later meta-analysis identified when it appears: complex choice sets, difficult decisions, unclear preferences, and a goal of minimizing effort (Chernev, Böckenholt and Goodman 2015) [Contested]. Practical rule: 2 to 4 rungs per ladder, one preselected default, and a clear recommendation for first time buyers.

## 7. Bundle portfolio review (quarterly)

| Metric | Formula | Action threshold |
|--------|---------|------------------|
| Bundle attach rate | Orders with a bundle / all orders | Falling 3 quarters in a row: refresh bundles |
| Bundle CM2 % vs single CM2 % | Per bundle | Below the floor: reprice or retire |
| Units per customer 90 days (bundle buyers vs single buyers, same acquisition month) | Cohort query | Bundle buyers no higher: discount is subsidy |
| Repeat rate of bundle first-order customers | 60 and 90 days | Lower than singles: bundle may overstock customers |
| Component stockouts | Days any component was out of stock | Bundles must auto hide when a component is out |
| Return rate by bundle | Returns / orders | Above core range by 3 points: check fit or expectations |

## 8. Bundle specification template

```
Bundle ID:            (matches SKU and EXPERIMENTS.md)
Type:                 multipack | fixed | mix and match | starter kit | tier | product plus service | DTC exclusive
Components and qty:
Price (net, gross):   Price per unit:   Unit price per legal measure:
Sum of components at list:   Implied saving (amount and %):   Reference price basis (compliance check):
CM2 per order:        CM2 %:          Floor in STRATEGY.md:
Target rung / default: Free shipping crossing: yes | no
Channels:             DTC only | all | excluded from marketplaces | retail exclusive
Inventory:            component stock cover in days at forecast velocity
Implementation:       Shopify Bundles app | Cart Transform app | WooCommerce Product Bundles | other (see implementation-on-platforms.md)
Feed handling:        handoff to commerce-feeds (bundle flag, GTIN rules, multipack attribute)
Test plan:            link to test plan
Approvals:            prices are G3
```

## 9. Common bundle mistakes
- Bundling a hero with dead stock and calling it value: customers see through it, return rates rise.
- A ladder where the per unit price is not shown, so customers cannot see the saving (and EU or UK unit pricing rules may be breached).
- Deep multipack discounts that cannibalize future single purchases; measure units per customer, not order size.
- Bundles live while a component is sold out (oversell, cancellations, ad spend to a dead offer).
- Marketplace listings of the same bundle at a different price, which breaks parity and can suppress the featured offer on Amazon.
- Feeds that submit a bundle as the single product (GTIN and price mismatch). Hand feed handling to `commerce-feeds`.
