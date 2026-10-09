# Price Changes, Increases and Inflation Pricing

> Owns: whether, when and how much to change list prices; inflation and currency pricing (Turkey and other high inflation markets); communication and grandfathering plans; post-change monitoring. Hands to `offer-strategy`: promotions used to soften an increase, and price increase offers for subscribers. Hands to `lifecycle-crm`: customer notices. Hands to `compliance`: reference price, notice period and subscription law. Hands to `commerce-feeds` and `site-engineer`: implementation.

## 1. The price lever

A 1% price increase with stable volume raised operating profit by about 11% on average in the classic McKinsey analysis of large companies (Marn and Rosiello 1992) [Study, prior knowledge]. The lever is still large but realization is hard: Simon-Kucher's Global Pricing Study 2025 (over 2,200 respondents, 28 countries) reported average price realization dropping to 43% of targeted increases; 53% use contract indexation but only about half enforce it consistently [Study, 2025-06, figures from brochure via search]. Bain's 2025 commercial and revenue growth agenda found list price increases matched or exceeded input cost increases in 55% of surveyed companies [Study, 2025].

## 2. Allowable volume loss

```
Allowable volume loss for increase i at contribution margin m (both as shares of price):  L = i / (m + i)
Required volume gain for decrease d:                                                         G = d / (m - d)
```

| CM2 margin_on_price | +5% | +10% | -5% | -10% |
|---------------------|-----|------|-----|------|
| 30% | 14.3% loss allowed | 25.0% | 20.0% gain needed | 50.0% |
| 45% | 10.0% | 18.2% | 12.5% | 28.6% |
| 60% | 7.7% | 14.3% | 9.1% | 20.0% |

High margin businesses tolerate less volume loss from increases and need less gain from decreases. Compare L with the elasticity estimate ([Elasticity and tests](elasticity-and-price-tests.md)): if expected loss is below L, the increase adds contribution.

## 3. When to change price

| Trigger | Response |
|---------|----------|
| Landed cost up more than 5% (or carrier, packaging, fees) | Recompute CM2; if below floor, increase or re-pack |
| Benchmark shows index under 90 with superior value | Increase toward the position |
| Competitor increases across the category | Follow within 1 to 2 months if position allows |
| FX moves (imported goods, Turkey) | Indexed repricing rule (section 6) |
| New pack or architecture | Reset prices at launch of the new structure |
| Persistent stockouts at current price | Signal of underpricing |

## 4. Change design

1. Decide scope: which SKUs and channels, size of change, rounding to price points (avoid crossing left digits by small amounts; see [Architecture](price-architecture-and-pack-sizes.md)).
2. Prefer architecture moves when increases are sensitive: new pack sizes, new tiers, removing the cheapest rung, changing what is included. Do not use hidden shrinkflation ([Architecture](price-architecture-and-pack-sizes.md) section 7).
3. Sequence: hero last if it is the most visible; or all at once to avoid repeated news. Avoid changes right before reference price windows of planned promotions (EU 30 day prior price rule; Turkey 10 day rule for price tags since 2025-10-11 and for discount ads since 2026-08-01) [Official, via offer-strategy research].
4. Retail partners: the brand changes its sell-in price list with the notice period in the contract; the retailer decides shelf prices. Never discuss the retailer's shelf price as an expectation.
5. Grandfathering: existing subscribers or contracts keep the old price for a defined period (1 to 3 cycles in consumer subscriptions, contract term in B2B) [Practitioner consensus]. Check subscription law: price changes for subscriptions require clear notice and often consent or a cancellation right (EU unfair terms rules; UK and US state auto-renewal laws) [route to compliance].
6. Communication: lead with the reason (cost, quality investment), state the new price and date, offer the grandfathering or stock-up window, and keep it short. Customer messages go through `compliance` and `lifecycle-crm`.

Communication template (draft for compliance):

```
Subject: Price update from <date>
From <date>, <product> will cost <new price> (was <old price>). <One sentence reason: ingredient and delivery costs rose by X since Y, if true and sourced>.
Subscribers: your price stays <old price> until <date>. You can change or cancel anytime at <link>.
```

## 5. Post-change monitoring

| Metric | Window | Alert |
|--------|--------|-------|
| Conversion rate by SKU and channel | 4 weeks vs pre-period and vs control market if any | Drop larger than L implies |
| Units and CM2 per visitor | 4 to 8 weeks | Below pre-period |
| Subscription churn and pause rate | 2 cycles | Above baseline + 2 points |
| Retail sell-out (if panel data) | 8 weeks | Retail drop |
| Competitor reaction | Weekly benchmark | Competitor promo spike |
| Customer service contacts on price | 4 weeks | Spike |

Record the change in DECISIONS.md (via orchestrator) and a journal entry; update price history evidence.

## 6. Inflation and currency pricing (Turkey and similar)

Context (verify monthly): Turkey CPI 29.73% year on year in September 2026, monthly 1.84%, food 27.62% year on year, core 29% (TÜİK, released 2026-10-05); producer prices 27.38% [Official, via press]. USD/TRY about 49.17 on 2026-10-06 (free market quotes) [Press]. Ministry of Trade unfair price enforcement: TRY 399.5M fahiş fiyat fines in the first nine months of 2026 within about TRY 2.6B total administrative fines [Press, 2026-10].

Rules:
1. Separate cost drivers by currency: imported inputs (USD or EUR linked), local inputs (TRY, CPI linked), logistics (TRY, revised several times a year).
2. Build a cost index: weighted change of drivers since the last price set. Reprice when the index moves more than a set band (for example 5 to 8%), not on a fixed calendar alone.
3. Reprice in fewer, larger steps with rounded price points rather than weekly small changes (menu costs, customer trust, marketplace algorithms).
4. Mind unfair pricing rules: increases must be justified by costs; keep the cost evidence file (the Ministry's Haksız Fiyat Değerlendirme Kurulu fines excessive increases) [Official, press reports]. Document every change with the cost index.
5. Discount advertising uses the lowest price of the prior 10 days in the same channel (from 2026-08-01); frequent increases followed by promotions are risky [Official, via secondary].
6. Installments (taksit) cost more; price installment plans with the PSP rate per term.
7. For EUR or USD pricing in B2B contracts, use indexation clauses (CPI, PPI or FX with a band) and enforce them.
8. Marketplace contracted logistics rates and commissions change; refresh the fee table monthly.

Indexation formula (B2B or internal rule):

```
New price = old price x (1 + w_fx x FX change + w_cpi x CPI change + w_log x logistics change), applied when |index change| > band
Round to price point rule. Log the computation.
```

## 7. Price decreases

Decrease only with a clear goal (volume needed for scale economics, repositioning, competitive threat) and the required gain G computed. A decrease resets reference prices downward and is hard to reverse. Prefer architecture (bigger pack at lower per unit) or offers (temporary, designed by `offer-strategy`) when the goal is temporary.

## 8. Change request lines

Every price change is G3: snapshot of current price per SKU, channel and market; proposed price; start date and time with time zone; rollback; evidence (cost index, benchmark); approver. Feed and site changes go together to avoid feed price mismatch disapprovals (`commerce-feeds`).

## 9. Common mistakes

1. Many small increases that each make news.
2. Raising prices shortly before a promotion (reference price rules).
3. Not grandfathering subscribers and triggering churn plus complaints.
4. Increases without updated feeds and structured data (price mismatch).
5. In Turkey, pricing in TRY from an old cost base after a currency move.
6. Communicating a cost reason that is not documented.

## 10. Worked example: cost shock in the Netherlands (illustrative)

Inputs (illustrative): hero 24 pack at EUR 59.95; landed COGS rises from EUR 0.85 to EUR 0.95 per bar (+11.8%, as of 2026-11-01); carrier unchanged.

1. Script rerun: hero CM2 falls from EUR 23.84 to EUR 21.44 (24 x EUR 0.10 = EUR 2.40 less).
2. To restore CM2 per order: add EUR 2.40 ex VAT = EUR 2.62 incl 9% VAT. Candidate prices: EUR 62.49 (+4.2%) or EUR 64.95 (+8.3%).
3. Allowable volume loss at CM2 margin_on_price of about 39% (EUR 21.44 / EUR 55.00) for +4.2%: 0.042 / (0.39 + 0.042) = 9.7%. For +8.3%: 17.5%.
4. Benchmark: if the hero per bar (EUR 2.60 or 2.71) stays under the observed shelf per bar, conflict risk stays low; check.
5. Choose: EUR 62.49 nearly restores contribution with low risk; EUR 64.95 crosses no new left digit vs 62.49 but approaches the shelf price per bar. EUR 62.49 recovers EUR 2.33 ex VAT of the EUR 2.40 lost (97%); recommend it unless the benchmark shows room.
6. Plan: subscribers keep EUR 59.95 for two cycles; announce 30 days ahead; feeds and site updated together; monitor 4 weeks.

## 11. Worked example: Turkish repricing rule (illustrative)

Cost mix of a TRY priced product: 40% imported inputs (USD linked), 35% local inputs (CPI linked), 25% logistics and marketplace fees.
Since the last price set: USD/TRY +6%, CPI +7.5%, logistics +10%.
Cost index change = 0.40 x 6% + 0.35 x 7.5% + 0.25 x 10% = 2.4 + 2.6 + 2.5 = 7.5%.
Rule: reprice when the index exceeds a 6% band. Action: raise by 7.5% on cost share. If cost is 55% of price, the price increase needed to keep contribution in TRY is 7.5% x 0.55 = 4.1%; to keep contribution in real terms, add the CPI change on the contribution share (7.5% x 0.45 = 3.4%) for a total of about 7.5%. Round to the price point rule, document the index computation as evidence, and avoid any discount advertising in the 10 days after the change unless the discount is calculated from the lowest price of the prior 10 days.

Cost basis line for every change plan: `Cost basis: <sheet or tool>, costs as of YYYY-MM-DD; status COMPLETE | INCOMPLETE (missing: ...)`. Label CM2 percentages as margin_on_price.
