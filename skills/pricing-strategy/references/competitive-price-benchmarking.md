# Competitive Price Benchmarking

> Owns: normalization of competitor and retail prices to comparable per unit figures, the price index, promo depth and frequency analysis, and the interpretation for price level decisions. Hands to `market-intel`: collecting raw competitor data, ad library and offer monitoring, monitoring cadence and tools setup. Hands to `marketplaces`: buy box and marketplace price monitoring operations.

A raw list of competitor prices is not a benchmark. A benchmark compares like with like: same unit of value, same VAT basis, same delivery terms, regular vs promo separated, all dated.

## 1. Define the comparison set

| Set | Who | Why |
|-----|-----|-----|
| Direct substitutes | Same job, same format (another organic bar) | Sets the parity zone |
| Adjacent category leaders | Same occasion, different promise (performance protein bars, natural snack bars) | Sets the ceiling and floor of the category |
| Retail shelf of our own product | Our SKU at each retailer | Channel corridor input |
| Private label | Retailer own brand in the category | Price floor customers see on shelf |
| Marketplace sellers of our product | Resellers on bol.com, Amazon, Trendyol | Corridor and parity risk |

Pick 3 to 8 competitors. More dilutes attention. Each one gets a reason to be in the set.

## 2. Unit of comparison

| Category | Primary unit | Secondary unit |
|----------|-------------|----------------|
| Snacks, bars, beverages | Per unit (bar, can) | Per 100 g or 100 ml (legal unit price basis), per serving |
| Protein and supplements | Per serving | Per gram of protein or active ingredient (value per functional unit) |
| Cosmetics | Per 100 ml | Per application or per month of use |
| Pet food | Per kg | Per day of feeding for a reference animal |
| Apparel | Per item | Per wear (only for positioning arguments) |
| Services | Per hour or per job | Per outcome (per room cleaned, per lead) |
| SaaS | Per seat per month at annual billing | Per unit of the value metric (per contact, per 1,000 events) |

The legal unit price (per kg, per liter, per 100 g or 100 ml under EU Directive 98/6/EC and national rules, UK Price Marking Order from 2026-04-06 with a wider scope) is the comparison customers see on shelf and increasingly online. Always compute it, even if positioning uses another unit.

## 3. Normalization procedure

1. Record raw: product name, pack size (units, weight), price shown, currency, channel (shelf, retailer online, DTC site, marketplace), seller (brand or reseller), date and time, regular or promo, promo mechanic (x% off, 2 for 1, second at half price, bonus pack), delivery fee and threshold, subscription price if any.
2. Effective pack price: apply the promo mechanic to the price a single customer pays for the basket that triggers it (2 for 1 on a 12 pack: price of two 12 packs divided by 24 units).
3. Per unit incl VAT: effective pack price / units.
4. Per unit ex VAT: divide by (1 + VAT rate of that market and class). Required when comparing across countries or against cost.
5. Delivered per unit for online: (pack price + delivery fee for the reference basket) / units. Use the reference basket the customer most likely buys (one pack, or the threshold basket).
6. Value unit: per 100 g, per serving, per gram of protein, etc.
7. Flag outliers: clearance, short dated, multipack only sold at one retailer, bundle with other products.

Spreadsheet columns: competitor | product | pack units | pack weight | channel | seller | date | regular price | promo price | mechanic | effective pack price | per unit incl VAT | per unit ex VAT | delivery fee | threshold | delivered per unit | per 100 g | per value unit | source URL or photo ref | collector.

## 4. Shelf vs online

| Aspect | Shelf (physical retail) | Online (retailer site, DTC, marketplace) |
|--------|------------------------|------------------------------------------|
| How to capture | Store check with photo (date, store, shelf tag and promo tag), retailer app | Site capture, price monitoring tool, retailer online store |
| Promo pattern | Weekly folder cycles (Dutch supermarkets run weekly offers), multi-buy mechanics | Codes, sitewide events, subscription prices, threshold incentives |
| Unit price | Shown on shelf tag | Often shown; check |
| Delivery cost | None | Must be added for the reference basket |
| Volatility | Weekly | Daily or intraday for marketplaces |

For a brand with retail partners: the shelf price is the anchor customers compare the DTC offer with. Capture it at least monthly in 3 stores per main retailer, and weekly during launch.

## 5. Promo depth and frequency

Regular price alone misleads when a competitor is on promotion 40% of weeks.

```
Promo frequency      = weeks with any promo on the SKU / weeks observed
Average promo depth  = mean(1 - promo effective price / regular price) over promo weeks
Effective price      = regular x (1 - frequency x depth)          (simple time-weighted approximation)
Volume-weighted effective price needs sell-out data (retail panel) and is better when available.
```

Collect at least 8 weeks (12 for seasonal categories). Retailer folder archives and price monitoring histories help. Record mechanics separately: "1+1 gratis" is 50% depth on two units, "2e halve prijs" is 25% on two units, "3 for 2" is 33.3%.

Interpretation:
- High frequency, deep promos (over 30% of weeks, over 25% depth): the regular price is a reference price only; customers anchor on the promo price. Compete on effective price or avoid the comparison with differentiated packs.
- Low frequency: regular price is the real price. Parity decisions use it.

## 6. Price index and benchmark table (deliverable)

```
Price index (regular)   = our regular per unit / median competitor regular per unit x 100
Price index (effective) = our effective per unit / median competitor effective per unit x 100
Value index             = our per value unit / median competitor per value unit x 100
```

Benchmark table layout for the report:

| Competitor | Product and pack | Channel | Price incl VAT | Units | Per unit | Per 100 g | Value unit | Regular or promo | Promo freq (8 wk) | Delivery terms | Source, date |
|-----------|------------------|---------|----------------|-------|----------|-----------|------------|------------------|-------------------|----------------|--------------|

Then three lines of interpretation: where the market clusters (median and interquartile range), where our product sits, where there is white space.

## 7. Data sources

| Source | What it gives | Cost and access | Notes |
|--------|---------------|-----------------|-------|
| Manual shelf checks | Shelf price, promo tags, unit price | Time | Most reliable for retail; photo every tag |
| Retailer websites and apps | Online shelf price, folder promos | Free | Albert Heijn, Jumbo, Picnic and others publish online prices; check store vs online differences |
| Competitor DTC sites | Bundle prices, thresholds, subscriptions | Free | Record delivery terms at checkout |
| Marketplaces | Seller prices, buy box price | Free; Keepa for Amazon history | Keepa API is token based; community MCP servers exist |
| Price monitoring SaaS | Scheduled scraping, history, alerts | See [Tools](tools-api-mcp.md) | Prisync, Price2Spy, Omnia, Minderest, Competera, DataWeave |
| Retail panels | Sell-out volume and price | Paid (Circana, NielsenIQ) | Needed for volume-weighted effective price |
| Google Shopping and Merchant Center price competitiveness | Benchmark price vs your price per product | Free in Merchant Center | Via `commerce-feeds` |
| Ad libraries | Offer messaging and promo timing | Free | Via `market-intel` |

Legal and ethical limits: collect public prices only; respect site terms and robots rules; do not log in to competitor accounts or use fake identities; never share price intentions with competitors (information exchange is a competition law risk). Monitoring your resellers' prices is lawful as information, but using it to pressure them is resale price maintenance (EU fines on Gucci, Chloé and Loewe for RPM, 2025-10-14; Italy AGCM on Morellato, 2026-03-17, involved online price monitoring used to police discounts) [Official].

## 8. Freshness of benchmark data

| Market condition | Maximum age before refresh |
|------------------|----------------------------|
| Stable EU market, no events | 30 days |
| Before and during BFCM, Sinterklaas, Ramadan, 11.11 | 7 days |
| Turkey (CPI 29.73% year on year in September 2026, TÜİK) | 7 to 14 days; record the date of every price |
| Marketplace buy box | Daily |
| Launch period | Weekly |

## 9. Reading the benchmark: decision table

| Finding | Meaning | Pricing response |
|---------|---------|------------------|
| Our regular index 115+, value index under 100 | We are more expensive per unit but cheaper per value unit | Lead with the value unit in communication (with `compliance`), keep price |
| Our index 115+, value index 115+ | Premium without a value unit advantage | Need non-price proof (organic, taste, brand); else lower or re-pack |
| Index under 90 with superior value | Underpriced | Price increase candidate ([Price changes](price-changes-and-inflation.md)) |
| Competitors promo heavy, we are not | Effective gap larger than regular gap | Compare effective prices; consider differentiated packs rather than matching promos |
| Retail shelf per unit below our DTC per unit at the hero rung | DTC looks expensive vs retail | DTC must win on convenience, assortment or bundle value, or the DTC rung price must move |
| Retail shelf per unit far above our DTC per unit | Retailer conflict | See [Channel corridors](channel-price-corridors.md) |
| Competitor free delivery threshold far below ours | Our delivery terms are the weak point | See [Minimum basket](minimum-basket-and-delivery-policy.md) |

## 10. Worked normalization (illustrative)

| Competitor | Pack | Price incl VAT | Mechanic | Effective pack | Per bar incl VAT | Per bar ex 9% VAT | Grams per bar | Per 100 g |
|-----------|------|----------------|----------|----------------|------------------|-------------------|---------------|-----------|
| Competitor A (performance protein) | 12 x 55 g | [P_A] | none | [P_A] | P_A / 12 | (P_A / 12) / 1.09 | 55 | (P_A / 12) / 0.55 |
| Competitor B (protein, value) | 12 x 45 g | [P_B] | 2e halve prijs | 0.75 x 2 x P_B for 24 bars | 0.75 x P_B / 12 | | 45 | |
| Our bar (retail shelf) | 1 x 40 g | 2.99 (illustrative) | none | 2.99 | 2.99 | 2.74 | 40 | 7.48 |
| Our bar (DTC hero 24) | 24 x 40 g | 59.95 (illustrative) | none | 59.95 | 2.50 | 2.29 | 40 | 6.24 |

P_A and P_B are placeholders. Replace them with dated captures from `market-intel`. Note how per 100 g changes the story for a lighter bar: a 40 g bar at EUR 2.50 is EUR 6.25 per 100 g (6.24 from the unrounded EUR 59.95 / 24), more than a 55 g bar at EUR 2.75 (EUR 5.00 per 100 g). If the shelf shows unit prices per 100 g, the lighter product looks expensive even when the per bar price is lower. Positioning must address that.

## 11. Common mistakes

1. Comparing a promo price of a competitor with our regular price (or the reverse).
2. Mixing incl VAT and ex VAT figures.
3. Ignoring delivery cost in online comparisons.
4. Benchmarking against one competitor that happens to be cheapest.
5. Using undated screenshots; prices in Turkey move monthly.
6. Comparing per unit when the shelf shows per 100 g.
7. Treating marketplace reseller prices as the brand's price.

## 12. Cross channel price divergence monitor

Watches the same SKU across DTC, marketplaces and retailers so the brand sees corridor breaks, promo collisions and market tension early. It informs the brand's own prices, packs, promotions and listings only; it is never used to pressure a reseller or retailer (section 7, [Channel price corridors](channel-price-corridors.md) section 3). Pattern proven in production monitors, generalized here [Practitioner consensus].

### 12.1 Data and formulas

One row per SKU, channel, seller and capture date, normalized per unit with section 3 (same VAT basis, delivery stated, regular and promo flagged), with lineage from `market-intel` ([Tools, APIs and MCP](../../market-intel/references/tools-api-mcp.md) section 11). Compare the same pack, or per unit with the pack difference flagged.

```
reference price  = the brand's own regular DTC price per unit for the same pack
                   (no DTC: median retail shelf price per unit; the report states which)
divergence %     = (channel price per unit minus reference price per unit) / reference price per unit x 100
move label       = down, up or flat vs the same SKU and seller at the previous capture (flat within 1%)
down share       = downs / (downs + ups), per market and week, across sellers and channels
withdrawal rate  = listings live last week that are delisted or out of stock this week / listings live last week
```

| Signal | Reading |
|--------|---------|
| Down share over 0.6 for 2 weeks | Price pressure: sellers chase volume or clear stock, or demand is softening |
| Down share under 0.4 for 2 weeks | Firming market: cost pass through or strong demand; read it before any own increase ([Price changes](price-changes-and-inflation.md)) |
| Withdrawal rate at 2x its 8 week median | Market tension: shortage, sellers leaving on thin margins, or platform delisting |
| One seller far below the reference | Clearance, short dated stock, grey import or a promo; read the mechanic before reacting |

### 12.2 Alert thresholds [Practitioner consensus]

| Alert | Starting threshold | Goes to |
|-------|--------------------|---------|
| Featured Offer risk | Our own marketplace listing per unit more than 5% above the lowest public price per unit for the same item elsewhere, or above it by any amount during our own DTC promo (Amazon publishes the policy but no threshold, so 5% is a starting point [Unverified]) | `marketplaces` ([Channel conflict with DTC](../../marketplaces/references/channel-conflict-with-dtc.md) section 5) |
| Promo conflict | A planned or live own promo takes a channel below its corridor floor, or overlaps a partner channel's event on the same pack | `offer-strategy` ([Channel conflict and price parity](../../offer-strategy/references/channel-conflict-and-price-parity.md)) |
| Reference undercut | Any channel below minus 10% for 3 or more days on a hero SKU (same 10% as the market-intel price undercut alert) | Own corridor and pack review (this skill); `marketplaces` if a listing looks counterfeit or unauthorized |
| Shelf above DTC | Retail shelf per unit more than 15% above our DTC hero per unit | Corridor review (section 9, retailer conflict) |
| Market tension | Down share over 0.6 for 2 weeks, or withdrawal rate at 2x its baseline | Price level review (this skill); `market-intel` to explain the cause |

Alerts follow the transition rule of the alert queue: one row per rule and entity (a SKU, or a SKU and channel) with an `alert_from` date, so an acknowledged alert stays acknowledged ([Dashboards and reporting](../../measurement/references/dashboards-and-reporting.md) section 8). Every response is a decision about the brand's own channels (price, pack, promo timing, listing), never a message to a reseller about their price; anything near that line goes to `compliance` first.

Handoffs: `marketplaces` (Featured Offer risk, unauthorized sellers), `offer-strategy` (promo conflict, promo calendar), `market-intel` (collection, lineage, cadence), `compliance` (MAP, RPM and any partner communication), `growth-orchestrator` (market tension that changes the plan).
