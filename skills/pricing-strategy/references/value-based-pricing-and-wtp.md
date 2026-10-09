# Value Based Pricing and Willingness to Pay

> Owns: estimating economic value to the customer and willingness to pay (WTP), choosing a research method, and turning results into a price level. Hands to `offer-strategy`: price research for offer design is shared; detailed survey mechanics are in [Pricing research and tests](../../offer-strategy/references/pricing-research-and-tests.md). Hands to `cro` and `market-intel`: running surveys, interviews and voice of customer collection.

Three ways to set a price: cost plus (what it costs us), competition based (what others charge), value based (what it is worth to the customer). Cost sets the floor, value sets the ceiling, competition shows where customers will compare. The recommendation lives between floor and ceiling at a position you can defend.

## 1. Economic value estimation (EVE)

```
Economic value = reference value (price of the next best alternative, per unit of value)
               + positive differentiation value (what our advantages are worth to this customer)
               - negative differentiation value (what our weaknesses cost them)
Price ceiling for a rational buyer = economic value
Recommended price = between floor (cost + required CM2) and ceiling, at a share of the differentiation value
```

Procedure:
1. Define the next best alternative per segment (the bar they would buy instead, the agency they would hire, the spreadsheet they use now).
2. Normalize its price per unit of value (per bar, per gram of protein, per hour, per seat).
3. List differentiators with proof (organic certification, taste test results, shelf life, speed, service level). For each, estimate value to the customer in money (time saved x hourly value; cost avoided; premium paid elsewhere for the same attribute).
4. Subtract negatives (lower protein, higher delivery cost, unknown brand risk).
5. Decide the share of differentiation value to keep (often 30 to 60% in B2B; in consumer goods use WTP research instead because value is perceived, not calculated) [Practitioner consensus].

Example (illustrative consumer case): next best alternative for an organic vegan bar buyer is a natural snack bar at EUR [R] per bar on shelf. Differentiation: certified organic (customers pay a premium for organic in the category: measure from shelf, organic vs conventional variants of comparable products), vegan with complete ingredient transparency (evidence from VOC). Negative: less protein than performance bars. The EVE frames the ceiling; WTP research tests it.

## 2. WTP methods

| Method | Use when | Sample | Strength | Weakness |
|--------|----------|--------|----------|----------|
| Customer interviews (value conversations) | Early stage, B2B, services | 10 to 20 interviews | Finds value drivers and reference points | Not a price number |
| Van Westendorp Price Sensitivity Meter | Range finding for a new product | 150 to 300 per segment | Cheap, fast range | Stated, no purchase context; no demand curve |
| Newton Miller Smith extension | Van Westendorp plus purchase likelihood | Same | Adds a revenue optimal point | Still stated |
| Gabor Granger | Demand curve for a known product at set prices | 200 to 400 | Direct demand curve | Anchoring on first price; stated |
| Choice based conjoint (CBC) | Trade-offs between attributes and price, competitor context | 300 to 1,000 | Closest survey method to real choice; tests packs and tiers | Cost, design skill |
| Incentive compatible (BDM, real purchase) | When accuracy matters, pilot markets | 100 to 300 | Revealed WTP | Operational effort |
| Live price tests | Product live with traffic | See [Elasticity and tests](elasticity-and-price-tests.md) | Revealed behavior | Legal and trust limits |
| Synthetic respondents (LLM panels) | Questionnaire drafting only | n/a | Speed | 2026 benchmark found systematic WTP errors (too high for hedonic products, inconsistent for utilitarian) [Study, 2026, via offer-strategy dossier]. Never a pricing decision input |

Stated WTP overstates real WTP in most studies (hypothetical bias) [Study, prior knowledge]. Calibrate stated results downward or validate with a live test before committing.

## 3. Van Westendorp setup (quick)

Four questions per respondent, about a concrete product with picture, pack size and per unit price context:
1. At what price would this be so expensive that you would not consider buying it? (too expensive)
2. At what price would you consider it expensive, but still consider buying it? (expensive)
3. At what price would you consider it a bargain? (cheap)
4. At what price would it be so cheap that you would doubt its quality? (too cheap)

Read: plot cumulative curves; the range between the point of marginal cheapness (too cheap x expensive) and point of marginal expensiveness (too expensive x cheap) is the acceptable range. Add purchase likelihood (NMS) at the "cheap" and "expensive" points to find a revenue optimal price. Ask in per unit terms and pack terms if packs differ.

## 4. Conjoint for pack and tier decisions

Attributes for a bar brand (example): brand (us, A, B, private label), protein per bar (10 g, 15 g, 20 g), certification (organic, none), pack (single, 12, 24), price per bar (4 to 5 levels around the market range), delivery (free, EUR 3.95). Output: part-worths, WTP for organic, price sensitivity per segment, share simulations for proposed ladders vs competitors. Tools: Sawtooth, Conjointly, Qualtrics conjoint, Displayr (see [Tools](tools-api-mcp.md)).

## 5. Segmenting WTP

WTP differs by segment more than by product. Typical splits: heavy vs light users (stock up rung for heavy users), occasion (gym vs office snack), channel (retail impulse vs planned DTC), country (Netherlands vs Turkey purchasing power), B2B company size. Fences let different segments pay different prices legitimately: pack size, channel, subscription commitment, timing, version (good better best). Fences based on personal data are a legal risk ([Elasticity and tests](elasticity-and-price-tests.md) section on personalized pricing).

## 6. From WTP to price

1. Take the acceptable range (Van Westendorp) or demand curve (Gabor Granger, conjoint).
2. Overlay CM2 per unit at each price (cost basis) and compute contribution x expected volume.
3. Overlay the benchmark: index vs reference set; check the positioning hypothesis.
4. Choose the price that maximizes contribution within the positioning range, then round to the price point rule.
5. Label confidence: survey only (low to medium), survey plus live test (high).

## 7. Value communication links

A price is only defensible if the value is communicated: unit price comparisons in the right unit (per gram of protein if that is our strength, per bar if not), certification proof, taste or usage proof. Every claim goes through `compliance` and `brand/CLAIMS.md`. Positioning messages are briefed to `creative-strategy`.

## 8. Value metric (SaaS and services)

Choose the unit the customer pays by so that price grows with value received: seats, contacts, events, transactions, outcomes (resolutions), credits. See [SaaS and B2B pricing](saas-and-b2b-pricing.md).

## 9. Common mistakes

1. Asking "what would you pay" directly with no context.
2. Running Van Westendorp and treating the optimal point as the price.
3. Using LLM synthetic panels as evidence.
4. Ignoring the reference price customers already have (retail shelf price, competitor pack).
5. Surveying current customers only (they already accepted your price).
6. Mixing segments with different alternatives in one curve.
