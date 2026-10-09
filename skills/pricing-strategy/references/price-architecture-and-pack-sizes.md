# Price Architecture and Pack Sizes

> Owns: the structure of prices: pack sizes, good better best tiers, the price per unit curve, price points and endings, the role of each rung, assortment rules per channel. Hands to `offer-strategy`: bundle mechanics as incentives (mix and match promos, gift with purchase, promo bundles), see [Bundles and price ladders](../../offer-strategy/references/bundles-and-price-ladders.md). Hands to `storefront-ux`: how the ladder is displayed (selectors, per unit display, default selection).

## 1. Architecture principles

1. Every rung has one job: entry (trial, low commitment), hero (default, best value story), stock up (loyalty, lowest per unit). Optional: premium or gift rung, subscription rung.
2. CM2 per order rises with every rung. CM2 per unit may fall, but not below the floor per unit you need to fund acquisition.
3. Per unit price falls with every rung. A quantity surcharge (larger pack more expensive per unit) destroys trust once noticed.
4. Steps between rungs are big enough to matter and small enough not to collapse margin: per unit steps of about 5 to 12% between adjacent rungs are a working range [Practitioner consensus].
5. The hero rung is the one you want most customers to choose; design the others around it.
6. Two to four rungs per product line. More choices rarely help: the choice overload meta-analysis mean effect is near zero (Scheibehenne et al. 2010) and the effect appears only under specific moderators (Chernev et al. 2015) [Study], so the reason to stay small is clarity and operations, not psychology.
7. Assortment differs by channel on purpose (see [Channel corridors](channel-price-corridors.md)).

## 2. Designing pack sizes

Inputs: consumption rate (units per week per household), shelf life, carrier formats (letterbox vs box), production and packaging minimums, retail pack sizes, competitor pack sizes.

| Rung | Sizing rule | Example (bars, illustrative) |
|------|-------------|------------------------------|
| Entry | Covers 1 to 2 weeks of consumption; at or just above the minimum viable basket; fits the cheapest carrier format if possible | 12 bars |
| Hero | Covers about one month; qualifies for free delivery; aligns with replenishment and subscription cadence | 24 bars |
| Stock up | 2 to 3 months; shelf life must exceed consumption time by a safe margin; check storage and cash | 48 bars |
| Bulk or subscriber only | Only for heavy users or subscription | 96 bars |

Carrier formats are design constraints. In the Netherlands a letterbox parcel was EUR 4.40 to 4.55 (PostNL, 2026) vs about EUR 7.00 for a box parcel at low volumes [Official, 2026]. A pack that fits the letterbox format saves about EUR 2.50 per order. Design an entry pack to fit it when the product allows.

## 3. Pricing the ladder

Method A: per unit curve from the hero.
1. Set the hero per unit price from positioning and the benchmark (price index target).
2. Entry per unit = hero per unit x (1 + 8 to 15%).
3. Stock up per unit = hero per unit x (1 - 6 to 10%).
4. Round to price points (section 5), recompute CM2 with the script, check monotonic CM2 per order.

Method B: cost plus floor per rung.
1. Minimum price per rung = (CM2 floor + cost to serve + units x landed COGS) grossed up for fees and VAT.
2. Place market based prices above the minimum.
Use B as a check on A, never as the main method (cost plus ignores value).

Method C: value based (see [Value based pricing](value-based-pricing-and-wtp.md)): set hero from willingness to pay data, then A.

Ladder check table (the script prints it):

| Rung | Units | Price incl VAT | Per unit | Step vs lower | CM2 per order | CM2 per unit | OK? |
|------|-------|----------------|----------|---------------|---------------|--------------|-----|

## 4. Good better best (tiers of quality or features)

| Tier | Contents | Price logic | Purpose |
|------|----------|-------------|---------|
| Good | Core product, standard service | Entry price, competitive with value players | Capture price sensitive segment, defend share |
| Better | Core plus the most valued upgrade | Most sales here; price set at value of the upgrade | Hero |
| Best | Everything, premium service | Anchor; priced for the low price sensitivity segment | Raise perceived value of Better, capture top segment |

Decoys: the classic attraction effect (Huber, Payne and Puto 1982) is widely used on tier pages, but replications with realistic stimuli often fail (Frederick, Lee and Baskin 2014; Yang and Lynn 2014) and a field test with over 140,000 sessions found no general effect [Study, via offer-strategy dossier]. Add a tier only when a real segment wants it, then test.

## 5. Price points and endings

Evidence:
- Left digit bias is real at scale. Strulov-Shlain (Review of Economic Studies) used scanner data on about 3,500 products in 25 US chains: consumers react to a 1 cent increase from a 99 ending as if it were a 15 to 25 cent increase, and retailers price as if the bias were smaller, forgoing 1 to 4% of potential gross profit [Study, 2019 working paper, published later].
- Classic field experiment: Anderson and Simester (2003) found 9 ending prices increased demand in mail order catalog tests, with stronger effects on new items [Study, prior knowledge].
- 99 endings signal "deal" and lower quality to some buyers; round prices fit premium and gift positioning and feel easier for hedonic purchases (Wadhwa and Zhang 2015) [Study, prior knowledge].
- 99 ending prices are stickier: a 2024 University of Chicago thesis on Dominick's data found greater rigidity for 99 endings [Study, unreviewed thesis]. Practical consequence: once you sit at 2.99, the next step is 3.49 or 3.99, not 3.09.

Rules:
| Situation | Ending |
|-----------|--------|
| Price sensitive mass category, value positioning | .99 or .95, avoid crossing a left digit (2.99 not 3.05) |
| Premium, gift, natural or craft positioning | Round (30.00) or .00/.50; consistency across the ladder matters more |
| Bundles where per unit price is the message | Choose the pack price so the per unit price lands on a clean figure (24 bars at 59.95 = 2.50 per bar after rounding: show 2.50) |
| Turkey | Round to 9 or 0 endings in TRY (for example 249.90, 250); frequent repricing makes rounding rules important; use a rounding rule, not ad hoc |
| B2B and SaaS | Round numbers; per seat prices often end in 0 or 5 |
| Multi-currency storefronts | Use platform rounding rules per market (Shopify Markets rounding rounds converted prices to the common denominator of each currency; fixed prices per market override) [Official, Shopify Help Center] |

Do not cross a left digit threshold for small gains: moving 2.99 to 3.09 (+3.3%) may cost more volume than moving to 3.29 (+10%) returns, because both cross the same left digit. If you must cross, cross with a meaningful step.

## 6. Unit price perception and quantity surcharges

- Quantity surcharges (larger pack costs more per unit) occur in roughly 10 to 34% of products sold in several sizes across store surveys; in one US survey 76.6% of 400 households believed larger sizes are always cheaper per unit [Study, multiple, older; NZ 2026 coverage]. Shoppers are inattentive: during surcharges large pack sales fell only about 14% in the median case [Study].
- Regulators and media now highlight surcharges (New Zealand 2026 coverage; UK Price Marking Order reforms 2026-04-06 widen unit pricing). A surcharge in your ladder is a reputational and legal display risk, not a margin trick.
- Unit price display is mandatory for many consumer goods (EU Directive 98/6/EC per kg or liter; national rules; Turkish price tag regulation requires unit prices). Ask `compliance` for the exact rule; ask `storefront-ux` to show it beside every ladder price.

Rule: per unit prices must fall up the ladder in every channel and in every promo state. Check that a promo on a small pack does not make it cheaper per unit than the large pack (a common source of accidental surcharges).

## 7. Shrinkflation and pack changes

Reducing pack size at the same price is a price increase and is now regulated in several markets:
- France: in force since 2024-07-01 for large retailers (400 m2 and above): shelf notice for two months when quantity falls and unit price rises [Official, via law firm summaries].
- Austria: Anti-Deceptive Packaging Act in force 2026-04-01 to 2030-06-30: notice for 60 days when a quantity reduction raises the unit price by more than 3%; fines up to EUR 2,500 per product [Official, via Library of Congress and law firms, 2026].
- Germany: no statute; courts found misleading packaging (Hamburg 2024; Mondelez Milka 100 g to 90 g ruling reported 2026) [Press, 2026].
- Turkey: no dedicated rule found; Ministry of Trade inspections sanction weight reductions with unchanged packaging under consumer law [Press, 2026] [Unverified].
- EU level: no harmonized rule; the Commission pushed back on Italy's national labeling rule [Press, 2026].

Prefer an open price increase or a genuinely new pack (different count, visibly different design) with clear communication. Hand the display question to `compliance`.

## 8. Assortment by channel (summary)

| Channel | Packs | Why |
|---------|-------|-----|
| Retail | Single units, small multipacks the retailer chooses | Retailer controls shelf price |
| DTC | Multi-packs, mixed boxes, subscriptions, exclusive flavors | Avoid like-for-like comparison with retail; basket economics |
| Marketplace | Packs that clear marketplace fees and carrier cost; often a distinct pack count | Fee structure and price parity |
| B2B or wholesale | Case quantities, pallet tiers | Volume price list |

## 9. Architecture audit (quick)

- [ ] 2 to 4 rungs per line, each with a named role.
- [ ] Per unit price falls up the ladder in all states (regular and promo).
- [ ] CM2 per order rises up the ladder (script check).
- [ ] Entry rung clears the minimum viable basket.
- [ ] Hero rung qualifies for free delivery.
- [ ] Stock up rung has shelf life and stock coverage checked.
- [ ] Price endings follow one rule per brand and channel.
- [ ] No left digit crossed without a meaningful step.
- [ ] Unit prices displayed (compliance checked).
- [ ] Channel specific packs defined to reduce like-for-like comparisons.

## 10. Common mistakes

1. Too many sizes, each with thin volume and confusing per unit steps.
2. Stock up rung so cheap per unit that it cannibalizes the hero and drops blended CM2 per unit below the acquisition floor.
3. Same pack sold on DTC below the retail shelf price.
4. Single unit DTC orders that lose money on carrier cost.
5. Hidden surcharges created by promotions on small packs.
6. Changing endings randomly across SKUs, which makes the ladder look unprincipled.
