# Offer Playbooks and Output Templates

> Step by step plays for the situations that come up most. Each play ends in a deliverable saved to `ads-master/outputs/offer-strategy/` and, where something would change prices, discounts or shipping, a change request for human approval (G3).

## Play 1: Offer audit (new project or quarterly)
1. Load PROJECT_BRIEF.md (offer, channels, unit economics), METRICS.md, STRATEGY.md, memory, last 10 journal entries.
2. Pull data (state source and date range): 12 months of orders with discount codes, discount amounts, shipping charged, returns; product costs; carrier invoices; payment fees by method; marketplace prices for hero SKUs (from `market-intel`).
3. Compute: discount rate by month, promo dependency, AOV distribution, free shipping threshold hit rate, CM2 by offer type, cohort 90 day repeat by acquisition offer.
4. Score with the [Audit checklist](audit-checklist.md).
5. Output: audit with top 5 opportunities ranked by expected contribution, risks (legal, channel), test backlog, handoffs.

## Play 2: First order offer redesign
1. Measure the current first order offer: share of new customers using it, acquisition investment per new customer, 90 day contribution of offer cohorts vs non-offer cohorts.
2. Generate at least 3 alternatives (lower discount, gift, free shipping, amount off with minimum spend, bundle starter kit).
3. Model each in [Offer economics](offer-economics.md) section 4 and 5; compute breakeven lift.
4. Check channel conflict for each alternative.
5. Design the test (visitor A/B or code split; primary metric 90 day contribution per new customer if time allows, else first order contribution after acquisition with a 90 day follow-up).
6. Draft the change request; hand display to `storefront-ux`, popup and welcome flow changes to `lifecycle-crm`, compliance review to `compliance`.

## Play 3: Black Friday and Cyber Week plan
1. Week minus 12: pull last year's post-mortem, inventory plan, margin by category.
2. Decide per category: participate with price, participate with value-add, or hold full price.
3. Set depth by category from economics and competitor expectations (Adobe 2026 forecast: discounts up to 30% in Cyber Week, category peaks electronics about 30%, toys 29%, TVs, computers and apparel about 23% [Study, 2026-09]); never deeper than the contribution floor allows without an explicit acquisition investment budget.
4. Verify reference prices (30 days EU and UK; 10 days for Turkish discount ads) and freeze pre-event prices.
5. Plan the sequence: VIP early access (no deeper discount, earlier access), main event, Cyber Monday twist (bundle or gift), post-event full price return.
6. Run the backward timeline in [Promo calendar](promo-calendar-and-events.md) section 6.
7. Define stop rules and the incident path (wrong price live, stock below threshold).
8. Post-mortem within 14 days with pull-forward analysis.

## Play 4: Free shipping threshold change
1. AOV histogram, shipping cost by order size and zone, return rate by order size.
2. Candidate thresholds at 15% to 30% above the median order, each with gap filler products.
3. Economics per candidate ([Offer economics](offer-economics.md) section 7).
4. Test by geo or switchback if visitor level is not possible; primary metric contribution per visitor; guardrails return rate and small basket conversion.
5. Roll out the winner; recheck after 90 days and after carrier rate changes.

## Play 5: Bundle and multipack ladder launch
1. Pick products with repeat use or natural pairing; check stock depth.
2. Build the ladder table ([Bundles](bundles-and-price-ladders.md) section 2); every rung beats the previous on CM2 per order.
3. Choose the default rung to test; free shipping crossing on the target rung.
4. Write bundle specs; hand to `site-engineer` (app or Cart Transform), `storefront-ux` (selector), `commerce-feeds` (bundle attributes).
5. Test default rung; read units per customer at 90 days before declaring success.

## Play 6: Weaning a brand off constant discounting
Symptoms: discount rate above 20% of gross sales, more than 40% of revenue on promotion, full price conversion collapsing, customers waiting for codes [Practitioner consensus thresholds; set your own].
1. Quantify: contribution lost to discounts on orders that would have happened anyway (holdouts on past promo emails if available; otherwise pre and post).
2. Replace sitewide percent off with value-adds and bundles for 1 to 2 cycles; keep one or two tent-pole events.
3. Remove always-on codes from public view; keep a welcome offer with a cap.
4. Move loyal customers to early access and perks instead of deeper discounts (`lifecycle-crm`).
5. Expect a revenue dip of some weeks; track contribution after marketing weekly, not revenue.
6. Reset reference prices: hold full price for 30 days (EU and UK) before the next reduction claim.
7. Log the decision in DECISIONS.md via `growth-orchestrator`.

## Play 7: Price increase
1. Compute allowable volume loss: `i / (m + i)`; for m = 53.5% and a 10% increase, about 15.7% of volume can be lost before contribution falls.
2. Check competitor prices (`market-intel`), cost drivers (tariffs, carrier increases, duties such as the EU EUR 3 low value parcel duty from 2026-07-01 for non-EU shippers), elasticity from past changes.
3. Choose method: across the board, by SKU (heroes held, long tail up), pack size change (with clear unit pricing; shrinking packs silently is a trust and legal risk), or new tier.
4. Subscription and SaaS customers: notice period, grandfathering window, communication plan (`lifecycle-crm`).
5. Retail partners and marketplaces: update recommended prices and wholesale prices; never dictate resale prices.
6. Monitor weekly: conversion, units, CM2, complaints, competitor reaction; rollback criteria agreed in advance.

## Play 8: Subscription offer launch
1. Confirm consumption cycle and repeat rate of one-time buyers.
2. Model retention breakeven ([Subscriptions](subscriptions-and-repeat-offers.md) section 2).
3. Set discount, first order incentive (if any), cadence options, skip and swap, cancel flow (one save offer).
4. Legal terms and disclosures through `compliance`; flows through `lifecycle-crm`; PDP selector through `storefront-ux`; app setup and QA through `site-engineer`.
5. Track first order churn, survival curve by offer, subscriber CM2 per order.

## Play 9: Lead gen offer upgrade
1. Pull lead to SQL and SQL to customer rates by offer and source from the CRM.
2. Identify the rung (see [Lead gen and SaaS](lead-gen-and-saas-offers.md) section 1) and whether quality or volume is the constraint.
3. Design a better rung or a qualifying version (paid diagnostic credited to the job, calculator with qualifying inputs).
4. Model CPQL and value per lead; set max CPQL.
5. Test with qualified pipeline per euro as primary metric; involve sales for lead quality review.

## Play 10: SaaS packaging and annual plan change
1. Map the value metric and current plan usage distribution.
2. Model annual discount with churn math ([Lead gen and SaaS](lead-gen-and-saas-offers.md) section 7).
3. Draft the 3 tier plus enterprise structure; AI features on credits with included allowance.
4. Price change policy for existing customers.
5. Test on the pricing page with year 1 revenue per signup as primary metric; hand page to `cro`.

## Play 11: Marketplace or retail conflict incident
Trigger: featured offer lost on top ASINs, retailer complaint, reseller price war.
1. Confirm the cause (which price, which channel, when).
2. If a DTC promo is the cause: decide with the human whether to end, exclude SKUs, or accept the cost for the promo window.
3. Never respond by asking resellers to raise prices (EU, UK, Turkey competition law).
4. Plan future promos with exclusive bundles or value-adds for affected SKUs.
5. Journal entry for `market-intel` and channel agents.

## Play 12: Margin shock recovery (cost or shipping increase)
Trigger: landed cost, duties, carrier rates or payment fees rise and CM2 falls below the floor.
1. Recompute CM2 per SKU and per offer with the new costs (tariffs, US de minimis end for imports since 2025-08-29, EU parcel duty for non-EU senders from 2026-07-01).
2. Rank fixes: free shipping threshold up, discount depth down, bundle mix, price increase (Play 7), fulfillment changes.
3. Pause or reprice offers that now lose money; update the breakeven ROAS and CPA for channel agents via `growth-orchestrator`.

## Play 13: Clearance and stock rescue
1. Identify aged or excess stock with days of cover above plan.
2. Prefer bundles with best sellers and outlet sections over sitewide discounts.
3. Time box markdowns; keep reference price rules; separate clearance from the core range.
4. Check marketplace channels for liquidation without hurting the main brand price.

## Output templates

### Offer brief

```
# Offer brief: <name> | Offer ID | Date | Author: offer-strategy
## Purpose and goal (one metric)
## Data used (sources and date ranges)
## Offer mechanics (what the customer gets, pays, when, conditions)
## Who it is for (segments, markets, channels) and who is excluded
## Economics (CM2 control vs offer, offer cost per order, acquisition investment, breakeven lift, payback)
## Channel conflict check (section 9 of channel-conflict-and-price-parity.md)
## Legal handoff package (section 4 of price-display-law-handoff.md)
## Implementation spec (platform, discount spec, bundle spec)
## Test plan (design, primary metric, guardrails, sample, duration, stop rules)
## Display and messaging handoffs (storefront-ux, cro, creative-strategy, lifecycle-crm, channel agents)
## Approvals needed (G3 lines)
## Handoffs requested
```

### Offer economics sheet (summary table)

```
| Variant | Price | Discount | Gift cost | Shipping charged | CM2 | CM2 % | Offer cost per order | Breakeven lift | Expected lift (source) |
```

### Change request lines (use ads-master/templates/CHANGE_REQUEST.md)

```
| # | Object (discount ID, price list, shipping rate) | Current (snapshot) | Proposed | Start and end (time zone) | Rollback | Evidence (offer brief link) | Approver |
```

### Monthly offer report

```
# Monthly offer report: <month> | Data sources and date ranges
## KPIs vs last month and last year (discount rate, promo dependency, AOV, CM2 per order, acquisition investment per new customer, 90 day repeat by acquisition offer, return rate on offer orders)
## Offers live and their results
## Tests (status, readouts)
## Channel conflict signals
## Legal and compliance items
## Next month calendar and decisions needed
## Handoffs requested
```
