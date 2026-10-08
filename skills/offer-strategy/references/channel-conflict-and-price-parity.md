# Channel Conflict, Price Parity and MAP

> A DTC discount is visible to every retail buyer, marketplace algorithm and price comparison engine within hours. Design offers so the channels you depend on are not damaged, and never use pricing controls that competition law forbids. Competition law questions go to `compliance` and counsel; this module tells you when to ask.

## 1. Map the channels first

Fill this before any offer that changes a visible price:

| Channel | Who sets the consumer price | Current price for hero SKUs | Contract terms on promotions | Algorithm sensitivity |
|---------|-----------------------------|-----------------------------|------------------------------|-----------------------|
| DTC site | You | | n/a | Google Shopping price competitiveness |
| Amazon (1P vendor) | Amazon | | Vendor agreements, funding | Amazon matches external prices |
| Amazon (3P seller) | You | | n/a | Featured offer eligibility vs external prices |
| Other marketplaces (bol, Trendyol, Hepsiburada, Zalando, eBay) | You or the platform (platform funded campaigns) | | Campaign participation terms | Ranking and buy box rules |
| Retail partners (brick and mortar, online retailers) | The retailer (independent) | | Promo calendars, co-op funds, recommended prices | Retail buyer relationships |
| Distributors and resellers | The reseller | | Distribution agreements | Price monitoring tools |
| Wholesale and B2B | Negotiated | | Price lists | n/a |

Sources: `PROJECT_BRIEF.md` section 1 (sales channels and their price points), contracts (human), `market-intel` price monitoring.

## 2. What can go wrong

| Conflict | Mechanism | Symptom |
|----------|-----------|---------|
| Marketplace featured offer loss | Amazon makes offers ineligible for the Featured Offer when they are not priced competitively against retailers outside Amazon or are much higher than recent prices (Seller Central staff description; Amazon publishes no numeric tolerance) [Official forum, secondary] | Buy box suppressed on your ASINs after a DTC sale |
| Amazon 1P price matching | Amazon lowers its retail price to match your DTC discount, then pushes margin recovery to the vendor | Vendor margin claims, chargebacks |
| Retail buyer backlash | Retailer sees a deeper DTC price than its own | Delisting threats, lost shelf space, co-op cuts |
| Price comparison spirals | Resellers follow your promo price down and stay there | Permanent price erosion |
| Reference price destruction | Frequent promos lower the "real" price in shoppers' minds and legally reset the prior price baseline | Full price sales collapse |
| Feed price disparity | Google Shopping price competitiveness reports show you above benchmark on some channels and below on others | Mixed ad performance (`commerce-feeds` owns the reports) |

## 3. What the law allows (summary, verify with counsel)

| Jurisdiction | Allowed | Not allowed | Recent enforcement |
|--------------|---------|-------------|--------------------|
| EU (Vertical Block Exemption Regulation 2022/720 and Vertical Guidelines, valid to 2034-05-31) | Recommended retail prices and maximum resale prices (if not turned into fixed or minimum prices by pressure or incentives); dual pricing for online and offline wholesale under conditions; DTC exclusive products | Resale price maintenance (fixed or minimum resale prices) is a hardcore restriction; minimum advertised price policies that restrict the online advertised price are treated as RPM; restricting online sales in effect | European Commission fined Gucci, Chloé and Loewe about EUR 157.4M on 2025-10-14 for RPM including maximum discount limits and set promotion windows [Official, 2025-10]; Italy's AGCM fined Morellato over EUR 25M on 2026-03-17 for capping online discounts with monitoring software [Official, 2026-03] |
| UK (Competition Act 1998, VABEO 2022) | Recommended prices; maximum prices | RPM; online MAP policies are generally unlawful per the CMA open letter | Past fines include Dar Lighting GBP 1.5M (2022) and the GAK retailer settlement (2020) [Official] |
| US federal | Unilateral MAP policies (supplier announces a policy and stops supplying violators, without agreement: Colgate doctrine); RPM assessed under the rule of reason since Leegin (2007) | Agreements that fix prices horizontally; coercive enforcement that becomes an agreement | FTC v Amazon monopolization trial on pricing policies set for 2027-03-29 (Amazon moved in October 2026 to continue it); De Coster consumer class action on Amazon anti-discounting certified 2025-08-06, jury trial set for 2027-06-14 [Official and press, 2025 to 2026] |
| US states | Varies | Some states treat minimum RPM more strictly than federal law (for example Maryland since 2009) [Practitioner consensus, verify] | State AG actions (District of Columbia v Amazon on fair pricing policy) |
| Turkey (Law No. 4054, vertical agreements communiqué) | Maximum or recommended prices clearly labeled as such | Fixed or minimum resale prices, including indirect pressure (threats to delay or stop supply) | Rekabet Kurulu fined Arçelik Pazarlama about TRY 365M, plus settlements with İntema (TRY 64.8M) and Seher Gıda (TRY 173.8M), among others [Official, dates vary, verify] |

Practical consequence: in the EU, UK and Turkey you can recommend prices but cannot make retailers or resellers follow them, cannot cap their discounts, and cannot police online advertised prices. In the US a carefully run unilateral MAP policy is common, but its design is a legal job.

## 4. Offer designs that avoid conflict

| Design | How | Why it works |
|--------|-----|--------------|
| DTC exclusive bundles and kits | Configurations not sold elsewhere (kit with accessory, multipack size, exclusive colorway) | No like-for-like price comparison; must be genuinely different, not a relabel |
| Value-add instead of price cut | Gift, extended guarantee, free engraving, faster shipping | Visible price unchanged on all channels |
| Member prices and loyalty perks | Prices for logged in members | Lower public price visibility; in the UK show the ordinary price next to the loyalty price since 2026-04-06 [Official, 2026-04] |
| Coordinated promo windows | Share the promo calendar with retail partners; they choose independently whether to join | Reduces surprise; do not dictate their prices |
| Different assortment depth | DTC holds full range and new launches; marketplaces hold core SKUs | Each channel has a role |
| Codes for closed audiences | Email or SMS subscriber codes, unique single use | Lower leakage to coupon sites; still visible to aggregators sometimes |
| Shipping and service differentiation | Free returns, subscriptions, personalization on DTC | Competes on service, not price |
| Separate brand or line for marketplaces | Different product line or pack size for value channels | Clear separation; costly |

## 5. Marketplace specifics

| Marketplace | Offer mechanics to know | Conflict watch |
|-------------|-------------------------|----------------|
| Amazon (3P) | Deals, coupons, Prime exclusive discounts, Subscribe and Save; Pricing Health dashboard flags offers; featured offer eligibility compares external prices | DTC promos can suppress the featured offer for everyone selling the ASIN [secondary] |
| Amazon (1P) | Amazon sets retail price; vendor funded promotions | Price matching to your DTC price |
| Trendyol, Hepsiburada (Turkey) | Platform campaigns (seller funded or platform funded), coupons, "Efsane" events | Turkish 10 day reference price is per channel; the marketplace price history is its own baseline |
| bol (Netherlands, Belgium) | Platform campaigns and deals | ACM rules apply to sellers' price claims |
| Zalando, eBay, others | Campaign participation programs | Check terms on price parity clauses |

Price parity clauses imposed by a marketplace on sellers (wide parity) face competition law scrutiny in the EU and UK; check current terms with counsel rather than assuming.

## 6. Procedure: offer conflict check (run before any visible price change)
1. List all channels selling the SKUs in the offer and their current consumer prices (from `market-intel` monitoring or a manual check, dated).
2. Compute the offer's visible price on DTC. If it is below any channel's current price by more than the tolerance you have observed (start with 0%), flag it.
3. For Amazon 3P SKUs: estimate featured offer risk; consider excluding those SKUs, or using a value-add.
4. For retail partners: check contracts for promotion notice periods and funding; inform them of the DTC calendar without asking them to follow any price (legal phrasing reviewed by counsel).
5. For marketplaces with their own events: decide which events you join and fund.
6. Write the decision and the residual risk in the offer brief; the human approves.
7. Monitor during the offer: featured offer status, marketplace sales, retailer price changes, support tickets about price differences.

## 7. Monitoring signals (handoff to `market-intel` for collection)

| Signal | Source | Threshold |
|--------|--------|-----------|
| Featured offer percentage on top ASINs | Seller Central business reports | Drop of 10 points or more after a DTC promo |
| Lowest public price per hero SKU across channels | Price monitoring tools, Google Shopping price competitiveness | Any channel below DTC by more than 5% for 7 days |
| Retailer promo prices | Retailer sites, flyers | New lows triggered by your promo |
| Coupon site leakage | Coupon aggregators | Private codes appearing publicly |
| Customer complaints about price differences | Support tickets | More than 1% of tickets |

## 8. What not to do
- Do not tell retailers or resellers the price they must charge, and do not cap their discounts (EU, UK, Turkey).
- Do not threaten to cut supply because of a reseller's price (indirect RPM in the EU, UK, Turkey; risky in the US).
- Do not use price monitoring software to police resellers' discounts; the Morellato and 2018 consumer electronics cases show regulators treat this as RPM enforcement.
- Do not raise list prices before a promotion to manufacture a discount (consumer law, all markets).
- Do not run a DTC sitewide sale deeper than retail without a plan for Amazon featured offers and retailer relations.

## 9. Channel conflict section for the offer brief

```
Channels selling these SKUs: 
Lowest current price by channel (date, source):
Visible DTC offer price:
Conflict flags: featured offer | retailer | reseller | marketplace event | feed parity
Mitigation chosen: exclusive bundle | value-add | member price | SKU exclusion | none
Counsel or compliance review needed: yes | no (reason)
Monitoring during offer: signals and owner
```

## 10. Price architecture across channels (corridor)

Set a corridor per hero SKU and review it quarterly. These are your own planning numbers; retailers and resellers remain free to set their prices.

| Element | Example | Purpose |
|---------|---------|---------|
| DTC list price | EUR 60 | Reference for brand pricing |
| Recommended retail price communicated to partners | EUR 60 (clearly labeled as recommended) | Allowed in EU, UK, Turkey when not enforced |
| Wholesale price | EUR 30 | Partner margin |
| DTC promo floor (self imposed) | EUR 48 (20% off) | Stops DTC from undercutting partners more than planned |
| Marketplace target (3P) | EUR 60 plus or minus marketplace fees | Featured offer stability |
| DTC exclusive bundle price | EUR 75 for the kit | Value without like-for-like comparison |

## 11. Worked example: DTC promo vs Amazon featured offer

Situation (illustrative): hero SKU sells EUR 40,000 per month on Amazon (3P) at EUR 60 and EUR 25,000 per month on DTC. A planned DTC sitewide 25% off would show EUR 45 publicly for 5 days.
- If the Amazon offer loses featured offer status for the 5 days plus a 3 day recovery and Amazon sales drop 60% in that period, the loss is about 40,000 x (8 / 30) x 0.6 = EUR 6,400 of revenue, roughly EUR 1,900 of contribution at a 30% marketplace contribution margin (illustrative inputs).
- Options: exclude the hero SKU from the promo, run a DTC exclusive kit at the same visible saving, or also discount on Amazon if the economics hold.
- Decision recorded in the offer brief with the residual risk; monitor featured offer percentage daily during the promo.

## 12. Partner communication template (have counsel review before use)

```
Subject: <Brand> DTC promotion calendar <period>
We are sharing our direct-to-consumer promotion dates for planning purposes:
<dates, offer type, categories>
Our recommended retail prices are unchanged: <list>.
Your pricing remains entirely your decision. This note does not ask you to change your prices or to participate.
Questions about co-marketing or promotional funding: <contact>.
```
