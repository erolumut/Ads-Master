# Cost to Serve and Margin Waterfall

> Owns: the cost basis behind every price recommendation (landed cost, packaging, fulfillment, carrier by zone and weight, payment fees, returns, marketplace and retail fees, VAT), contribution per order by basket size and the minimum viable basket. Hands to `offer-strategy`: the cost of incentives (discount, gift, free shipping promotions) built on top of this basis, see [Offer economics](../../offer-strategy/references/offer-economics.md). Hands to `growth-orchestrator`: acquisition cost, payback and budget.

No price, ladder, minimum basket or delivery threshold is recommended until this waterfall exists for the hero SKU and the three most common basket sizes, with every input sourced and dated.

## 1. The waterfall (per order)

```
Gross price paid by customer (incl VAT)                     P_gross
- VAT on goods                                              P_gross - P_gross / (1 + vat)
= Net product revenue                                       R = P_gross / (1 + vat)
- Landed COGS (unit cost + inbound freight + duties) x units
= CM1 (gross margin)
+ Net shipping revenue (shipping charged / (1 + vat_ship))
- Packaging (box, filler, tape, insert) per order and per unit
- Pick and pack (per order + per unit; 3PL invoice lines)
- Carrier (base rate by band + fuel or energy surcharge + zone surcharge)
- Payment fees (% of gross paid + fixed per transaction; by method mix)
- Channel fees (marketplace referral %, fixed fee per item, fulfillment fee; retail: see section 6)
- Returns allowance (refund value not resold + return label + handling) as % of R
= CM2 (contribution after cost to serve)
- Variable marketing per order (media + acquisition investment / orders)   -> owned by growth-orchestrator
= CM3 (contribution after marketing)
```

Rules:
- Revenue is always ex VAT. A EUR 2.79 bar at 9% VAT is EUR 2.56 of revenue. At 21% VAT it is EUR 2.31. Comparing gross prices across countries or VAT classes without this step is the most common error in DIY pricing sheets.
- Payment fees are charged on what the customer pays (incl VAT and shipping). Calculate them on the gross amount.
- Carrier cost is a step function of size and weight. A letterbox parcel and a box parcel can differ by 50% or more. Model bands, not an average.
- Returns allowance is category specific: under 1% for food and consumables, 5 to 15% for beauty and home, 20 to 50% for fashion [Practitioner consensus; use own data].
- Marketing is NOT inside CM2. Price level decisions are made on CM2; the growth plan is made on CM3. State both when the recommendation changes acquisition economics.

## 1b. Costing conventions (follow these in every sheet and report)

These conventions match the owner's costing tool, so numbers move between that tool and the pricing reports without translation.

| Convention | Rule | Why |
|-----------|------|-----|
| Three margin layers | (1) Variable unit cost: landed COGS plus per unit variable costs. (2) Contribution margin: price ex VAT minus all variable costs to serve the order (CM2 above). (3) Fully loaded margin: contribution minus allocated fixed costs (rent, staff, software, overhead); computed only at month close, from actuals | Price level and basket decisions run on contribution; fully loaded margin is a month close control, never an input for a single price point |
| Margin vs markup | `margin_on_price = (price ex VAT - cost) / price ex VAT`; `markup_on_cost = (price ex VAT - cost) / cost`. Two named formulas. Never mix them; label every percentage with which one it is | 35% margin_on_price equals 53.8% markup_on_cost; confusing them misprices by a third |
| Effective dated costs | Every cost carries an "as of" date ("COGS EUR 0.85 as of 2026-09-01"). The report states the cost date used. When a cost changes, add a new dated value; never overwrite history | Prices are reviewed against the cost that was true when they were set; reconstructing why a price was chosen needs the dated cost |
| Inheritance of overrides | Values inherit product -> brand -> company. A product level value overrides the brand, the brand overrides the company default. An empty value means inherit, not zero | A blank packaging cost on one SKU must take the brand default, not EUR 0 |
| Incomplete, not zero | When a required input is missing after inheritance, the result status is INCOMPLETE and the report lists the missing inputs. Never compute with zero in place of a missing cost | A margin computed with a missing carrier cost looks healthy and is wrong |
| Recommend, never publish | The agent recommends prices. Publishing a price, threshold or price list anywhere (store, marketplace, feed, retailer price file, billing system) is G3 and needs explicit human approval | Fence from GUARDRAILS.md |

Report header line (required): `Cost basis: <cost sheet name or tool>, costs as of YYYY-MM-DD; status COMPLETE | INCOMPLETE (missing: ...)`.

## 2. Input sheet (copy into the output)

| Input | Value | Unit | Source | Date range | Confidence |
|-------|-------|------|--------|-----------|------------|
| Current price per SKU and pack (incl VAT) | | currency | Site, backend export | | |
| VAT rate per product class and market | | % | Tax adviser, official list | | |
| Unit cost (production) | | per unit | Cost sheet, supplier invoice | | |
| Inbound freight and duties per unit | | per unit | Freight invoices | | |
| Packaging per order and per unit | | | Packaging supplier, 3PL | | |
| Pick and pack per order and per unit | | | 3PL contract | | |
| Storage per unit per month | | | 3PL contract | | |
| Carrier rate by band and zone | | per parcel | Carrier contract or rate card | | |
| Fuel or energy surcharge | | % | Carrier monthly index | | |
| Payment method mix and fee per method | | % and fixed | PSP invoice, payout report | | |
| Return rate and cost per return | | % and per return | Backend, 3PL | | |
| Marketplace fees (referral, fixed, fulfillment) | | | Seller center fee page | | |
| Retail sell-in price, retailer margin, trade spend | | | Retail contract, invoices | | |
| Shipping charged to customer and current threshold | | | Store settings | | |

Confidence: A (contract or invoice), B (published rate card), C (third party estimate), D (assumption). Every C or D input gets a sensitivity line in the report.

## 3. Formulas

```
R            = P_gross / (1 + vat)
CM1          = R - units x landed_cogs
ship_net     = ship_charged_gross / (1 + vat_ship)
carrier      = band_cost(units, kg, zone) x (1 + fuel_pct)
payment      = (P_gross + ship_charged_gross) x pay_pct + pay_fixed
channel      = R x channel_pct + channel_fixed
returns      = R x return_allowance_pct
CM2          = CM1 + ship_net - packaging - pick_pack - carrier - payment - channel - returns
CM2 %        = CM2 / (R + ship_net)
CM2 per unit = CM2 / units
Floor        = max(floor_amount, floor_pct x (R + ship_net))
Minimum viable basket = min units such that CM2(units) >= Floor
Fixed cost per order (F) = packaging_order + pick_order + carrier + pay_fixed (+ channel_fixed)
Unit margin (u)          = price_net_per_unit x (1 - pay_pct' - channel_pct - return_pct) - landed_cogs - pick_unit
Breakeven units (no shipping charged) = ceil((F + Floor) / u)
```

Interpretation: the minimum viable basket is the order size at which the fixed cost per order (packaging, pick, carrier, fixed payment fee) is covered with the required contribution left over. It is the economic foundation for both the minimum order value and the free delivery threshold ([Minimum basket and delivery policy](minimum-basket-and-delivery-policy.md)).

Setting the floor:
- Floor amount: the contribution an order must leave to justify handling it at all. Start with the fully loaded cost of customer service per order plus a share of overhead per order, or use the value in STRATEGY.md.
- Floor percent: the CM2 % below which the business cannot fund acquisition. A practical start is the CM2 % that gives a breakeven ROAS (1 / CM2 %) the paid channels can reach; confirm with `growth-orchestrator`.

## 4. Cost references by market (planning only, verify per project)

These are indicative public figures for planning when the project has no contract yet. Contracted rates replace them as soon as available. Run the Freshness Protocol and label them in outputs.

### Netherlands parcel (domestic)

| Item | Figure | Source and label |
|------|--------|------------------|
| PostNL business parcel, domestic, by annual volume band (ex VAT) | EUR 7.40 (100 to 250 per year), 7.35 (250 to 500), 7.30 (500 to 1,000), 7.00 (1,000 to 2,500), 6.85 (2,500 to 5,000), 6.65 (5,000 to 10,000); custom above 10,000 | PostNL Zakelijke Pakkettarieven 2026 PDF [Official, 2026-01, seen via search snippet] |
| PostNL brievenbuspakje+ (letterbox parcel up to 2 kg), online franking | EUR 4.40 (January 2026 folder); EUR 4.55 in the 12 July 2026 tariff book | PostNL tariff folder 2026 and Tarieven en diensten 12 juli 2026 [Official, 2026-01 and 2026-07, seen via search snippet] |
| Platform rates via Sendcloud (with negotiated discount) | From EUR 2.99 PostNL, EUR 3.67 DHL, EUR 3.38 DPD (start prices, smallest format) | Sendcloud NL campaign page [Vendor, 2025 to 2026] |
| DHL eCommerce NL fuel surcharge | 22.75% (July 2026), 23.50% (August 2026), 28.00% (September 2026); applied on transport rate, lagged one month, linked to CBS diesel price | dhlecommerce.nl fuel surcharge index [Official, 2026-09] |
| DHL eCommerce NL other domestic surcharges | Wadden Islands EUR 6.00; manual handling EUR 3.95; energy surcharge exists (amount not confirmed) | QLS knowledge base [Third party, 2026] [Unverified] |

Takeaways: a Dutch DTC brand under 2,500 parcels per year pays roughly EUR 7 per box parcel before platform discounts, and a letterbox format saves about EUR 2.50 per order. Fuel surcharges near 25% on some carriers make "base rate" quotes misleading. Always add the surcharge.

### Turkey parcel (domestic)

| Item | Figure | Source and label |
|------|--------|------------------|
| Yurtiçi Kargo list price, 0 to 1 desi, same city | About TRY 154 to 209 (Sentos list); TRY 167 (0 desi) to 226.50 (1 desi) (Kargonomi) | Third party lists, 2026 [Unverified]; VAT inclusion differs by source |
| Aras Kargo list price, 1 desi | TRY 163.26 (Sentos, updated 2026-07-17); TRY 149.54 ex KDV in city (Kargonomi, from 2026-01-01) | Third party lists [Unverified] |
| Marketplace contracted rates (Trendyol agreement) | Yurtiçi 1 to 5 desi about TRY 112.77 to 142.91; Aras 1 to 5 desi about TRY 83.93 to 111.70 | Dopigo, Kargo Entegratör, 2026 [Unverified] |

Takeaways: in Turkey, contracted e-commerce and marketplace rates sit 30 to 50% below list prices, list prices move several times per year with inflation (CPI 29.73% year on year in September 2026, TÜİK), and desi (volumetric weight) drives cost. Recompute monthly. Check whether a quote includes KDV.

### Payment fees

| Provider and method | Figure | Label |
|---------------------|--------|-------|
| Stripe NL, standard EEA cards | 1.5% + EUR 0.25 | [Official, stripe.com/en-nl/pricing, 2026] |
| Stripe NL, premium EEA cards | 2.8% + EUR 0.25 | [Official, 2026] |
| Stripe NL, iDEAL (iDEAL Wero) | EUR 0.29 per payment (+2% if currency conversion) | [Official, 2026]; Wero rollout to Dutch shoppers late 2026, full transition by 2028 per Stripe guide |
| Mollie, iDEAL | EUR 0.29 in most sources, EUR 0.32 in a June 2026 verified listing | [Contested]; confirm on mollie.com |
| Mollie, EU consumer cards | 1.8% + EUR 0.25 | [Unverified, third party] |
| Adyen | Interchange++ with about 0.60% markup plus about EUR 0.11 per transaction; iDEAL about EUR 0.22; minimum invoice reported EUR 100 to 1,000 per month | [Unverified, third party, 2026] |
| iyzico, single payment (tek çekim) | About 1.95% most cited (range 1.19% to 2.99% + TRY 0.25) | [Unverified, comparison sites, 2026] |
| PayTR, single payment | Ranges 1.49% to 2.89% most cited; settlement terms (bloke, vade) change effective cost | [Unverified, comparison sites, 2026] |

Takeaways: for a Dutch basket where iDEAL dominates, blended payment cost is mostly a fixed EUR 0.22 to 0.32 per order, which penalizes small baskets. In Turkey, installments (taksit) carry much higher rates (12 installments about 3.45% at iyzico per one comparison site [Unverified]); model the installment mix explicitly.

### Marketplace fees (summary; detail belongs to `marketplaces`)

| Marketplace | Structure | Figure | Label |
|-------------|-----------|--------|-------|
| Amazon EU | Referral % by category plus FBA fulfilment fee | From 2026-01-05: grocery and gourmet, and vitamins and supplements, 8% to 5% for items up to EUR 10; Low-Price FBA extended to most categories up to EUR 20; average fee cut about EUR 0.17 per unit across EU stores | aboutamazon.eu [Official, 2025-12] |
| Amazon EU | FBA fuel and logistics surcharge | Reported 1.5% surcharge on FBA fulfilment fees from 2026-04-17 | [Unverified, third party] |
| bol.com | Fixed fee per item plus % commission by category (commission ex VAT, 21% VAT on top) | Fixed fee reported EUR 0.20 (under EUR 10), 0.40 (EUR 10 to 20), 0.85 (over EUR 20); category % about 4% to 21%, 12.4% cited as common | Boloo, Zoloo, Winkelfactuur 2026 [Unverified, conflicting]; confirm in Verkoopaccount under Tarieven |
| Trendyol | Category commission (KDV dahil) plus service fee (hizmet bedeli) | Supermarket and food 10% to 15.25% reported; service fee described either as a percentage or as TRY 6.99 to 10.99 per shipment | Paraşüt (2026-01-14 rates), Sentos, Stokoloji [Unverified, conflicting] |

### VAT

| Market | Rates (verify product classification) |
|--------|----------------------------------------|
| Netherlands | 21% standard; 9% reduced (most food) [Official, Belastingdienst, prior knowledge] |
| Turkey | 20% standard, 10% and 1% reduced; basic foods at 1% since 2022; some food groups at higher rates. Classification of snacks and protein bars not confirmed [Unverified]; check the GİB rate lists by product and GTİP code |
| Other EU | Look up the national rate per product class; never assume the domestic rate applies |

## 5. Worked example (illustrative, generated by the script)

Inputs are ILLUSTRATIVE and labeled as such inside the script: a Dutch DTC bar at EUR 2.79 single price incl 9% VAT, landed COGS EUR 0.85, packaging EUR 0.60 per order, pick and pack EUR 1.50 per order + EUR 0.02 per bar, letterbox parcel EUR 4.55 up to 6 bars and box parcel EUR 7.00 up to 96 bars, blended payment 0.6% + EUR 0.27, returns 1%, shipping charged EUR 4.95 below a EUR 50 free delivery threshold, floor max(EUR 8.00, 20% of net revenue). Output of `python3 scripts/basket_economics.py --demo`:

Ladder under the current policy:

| basket | units | price incl VAT | per bar | shipping charged | net revenue | carrier | CM2 | CM2 % | CM2 per bar |
|---|---|---|---|---|---|---|---|---|---|
| Trial 12 | 12 | 32.95 | 2.75 | 4.95 | 34.77 | 7.00 | 14.43 | 41.5% | 1.20 |
| Entry 24 | 24 | 59.95 | 2.50 | 0.00 | 55.00 | 7.00 | 23.84 | 43.3% | 0.99 |
| Hero 48 | 48 | 109.95 | 2.29 | 0.00 | 100.87 | 7.00 | 48.07 | 47.7% | 1.00 |
| Stock up 96 | 96 | 199.95 | 2.08 | 0.00 | 183.44 | 7.00 | 87.52 | 47.7% | 0.91 |

Single bar price x basket size:

| bars | basket incl VAT | shipping charged | carrier | CM2 | CM2 % | floor | clears |
|---|---|---|---|---|---|---|---|
| 1 | 2.79 | 4.95 | 4.55 | -0.76 | -10.7% | 8.00 | no |
| 4 | 11.16 | 4.95 | 4.55 | 4.18 | 28.3% | 8.00 | no |
| 6 | 16.74 | 4.95 | 4.55 | 7.48 | 37.6% | 8.00 | no |
| 8 | 22.32 | 4.95 | 7.00 | 8.32 | 33.3% | 8.00 | yes |
| 12 | 33.48 | 4.95 | 7.00 | 14.91 | 42.3% | 8.00 | yes |
| 16 | 44.64 | 4.95 | 7.00 | 21.50 | 47.3% | 9.10 | yes |
| 18 | 50.22 | 0.00 | 7.00 | 20.28 | 44.0% | 9.21 | yes |

Minimum viable basket: 8 bars (EUR 22.32) when shipping is charged; 12 bars (EUR 33.48) when delivery is free.

Retail comparison (illustrative shelf EUR 2.99, retailer margin 30% of shelf ex VAT, trade spend 10% of sell-in, logistics EUR 0.08 per bar): implied sell-in EUR 1.92, brand CM per bar in retail EUR 0.80. DTC CM2 per bar is EUR 0.91 to 1.20 before marketing, so DTC is only better than retail per bar if acquisition cost per bar stays under about EUR 0.11 to 0.40. That is the real question for a brand with a retail partner.

What the example teaches:
1. Single unit orders lose money (CM2 negative at 1 bar even with EUR 4.95 shipping charged). A minimum order or a bundle-only assortment is not a choice, it is arithmetic.
2. The letterbox format boundary (6 bars) creates a step: 6 bars clears more CM2 % than 8 bars. Pack sizes that fit the cheaper carrier format are worth designing for.
3. The threshold dead zone: 16 bars with shipping charged earns EUR 21.50, 18 bars with free delivery earns EUR 20.28. Customers who top up just over the threshold are worth less than those just below it. The threshold only pays if it moves enough orders from below the minimum viable basket upward or lifts conversion.
4. Ladder rungs each earn more CM2 per order than the rung below, and the per bar price steps are 8 to 9%: within the range customers notice without collapsing CM2 per unit.

## 6. Retail and wholesale waterfall (brand view)

```
Shelf price incl VAT                                 S_gross
Shelf price ex VAT                                   S = S_gross / (1 + vat)
Retailer margin (front margin, % of S)               m_r      -> sell-in price W = S x (1 - m_r)
Trade spend (promo funding, listing fees, back margin, payment discounts) as % of W   t
Net net sell-in                                      W_nn = W x (1 - t)
- Landed COGS, outbound logistics to DC, pallet and case costs
= Brand contribution per unit in retail
```

Notes:
- Retailer margin is quoted on the shelf price ex VAT, markup on the sell-in price. 35% margin equals about 54% markup. Always say which one.
- Conventional grocery retailer margins are often cited at 25 to 35% of shelf price, convenience 35 to 45% [Unverified, agency source attnagency.com]; New Zealand dry grocery suppliers claimed 35 to 41% [Unverified, Newshub 2023]. Use the project's actual sell-in price; ask for it at intake.
- Dutch supermarkets push back on supplier prices hard (delistings during negotiations, buying alliances such as Jumbo's membership in international buying groups) [Press, multiple years]. A DTC price that undercuts shelf price becomes a negotiation weapon for the retailer.
- Brands cannot set the retailer's shelf price. Recommended retail prices are allowed only as genuine recommendations (see [Channel price corridors](channel-price-corridors.md)).

## 7. Running the script

```
python3 skills/pricing-strategy/scripts/basket_economics.py --print-template > ads-master/data/imports/basket_inputs.json
# fill values with sourced inputs, then:
python3 skills/pricing-strategy/scripts/basket_economics.py --config ads-master/data/imports/basket_inputs.json --csv ads-master/outputs/pricing-strategy/basket_scan.csv
```

Inputs: prices incl VAT; costs ex VAT; `cost_as_of` date; null for any unknown cost (the run then stops with status INCOMPLETE and lists the missing inputs instead of computing with zero); carrier bands by `max_units` (size limited formats such as letterbox) or `max_kg`; floor as amount and percent; optional `retail` block. Output: ladder table with a monotonic check, single unit scan with minimum viable basket (charged and free delivery), free delivery threshold candidates, retail vs DTC per unit comparison. Paste the tables into the report with the input sheet beside them.

## 8. Sensitivity (always include)

| Driver | Test range | Why |
|--------|-----------|-----|
| Carrier rate | -15% to +25% | Surcharges, contract renewal, volume band change |
| Landed COGS | -10% to +20% | Raw materials, FX (Turkey), MOQ changes |
| Payment mix | iDEAL share -20 points; card share +20 | Fixed vs percentage fee mix |
| Return rate | x2 | New channels and new customers return more |
| VAT rate | Reclassification | Food classification disputes |
| Basket mix | Shift 10 points of orders one rung down | Ladder dependency |

Report the minimum viable basket and the threshold verdict under the worst plausible combination. If the recommendation flips, say so in the risks section.

## 9. Common errors

1. Computing margin on gross (VAT included) prices.
2. Using an average shipping cost instead of the band step.
3. Ignoring fuel or energy surcharges (DHL eCommerce NL at 28% in September 2026).
4. Treating payment fees as a percentage when the order mix is mostly fixed fee methods (iDEAL, Wero, bank transfer).
5. Putting media cost into CM2 and then counting it again in CAC.
6. Comparing DTC per unit prices with retail shelf prices without the retailer margin and trade spend view.
7. Using last year's Turkish costs: at 25 to 30% annual inflation a 6 month old cost base is wrong by 12% or more.
8. Forgetting storage and slow moving stock for large packs (the 96 pack ties up stock and cash).
