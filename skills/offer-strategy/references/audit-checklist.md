# Offer Strategy Audit Checklist (scored)

> Score each item Pass (2), Partial (1), Fail (0) or N/A. Severity weights: Critical x3, High x2, Medium x1. Record evidence (file, export, screenshot, date) for every score. Never score from memory or assumption.

## A. Economics foundation

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | CM2 per order known for core products, with every variable cost line | Offers are judged on contribution | Cost stack in [Offer economics](offer-economics.md) section 1 filled with sources | Critical | Build the cost stack from invoices and exports |
| A2 | Acquisition investment (media plus shipping subsidy plus bonus product cost plus incremental discount cost) reported next to media CPA | Hidden offer costs inflate apparent efficiency | Monthly report or METRICS.md definition in use | Critical | Add to weekly reporting |
| A3 | Offer costs counted once (inside CM2 or inside acquisition investment) | Double counting misleads decisions | Review the formulas in use | High | Standardize per offer-economics.md rule 1 |
| A4 | Contribution floor per order and per bundle defined in STRATEGY.md | Prevents margin negative offers | STRATEGY.md | High | Propose floor via growth-orchestrator |
| A5 | Breakeven lift computed before any offer goes live | Sets the bar the test must clear | Offer briefs | High | Use the calculator |
| A6 | Costs refreshed after tariff, duty, carrier or fee changes in the last 6 months | Margin shocks make old offers unprofitable | Date of last cost update | High | Play 12 |

## B. Offer architecture

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Each core product has a clear primary offer (price, terms, guarantee, incentive) written down | Ambiguity leads to random promos | PROJECT_BRIEF.md section 2, offer briefs | High | Write the offer table |
| B2 | First order offer cost within the economics (payback horizon from STRATEGY.md) | Largest recurring offer cost | Cohort analysis by acquisition offer | Critical | Play 2 |
| B3 | Barrier other than price addressed (shipping, risk, effort, payment) before discounting | Cheaper levers exist | VOC, abandonment reasons, offer brief | Medium | Incentive decision tree |
| B4 | Offers differ by segment where economics differ (new vs returning, markets, channels) | One size offers waste subsidy | Discount configuration | Medium | Segment rules |

## C. Price ladder and bundles

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Ladder rungs increase CM2 per order | Prevents upsells that lose money | Ladder table | High | Reprice rungs |
| C2 | Per unit price shown on every rung, and legal unit price where required | Customer clarity and EU and UK unit pricing rules | PDP screenshots per market | High | Handoff to storefront-ux |
| C3 | Bundle CM2 % meets the floor | Margin protection | Bundle specs | High | Reprice or retire |
| C4 | Bundles auto hide or block when a component is out of stock | Overselling, cancellations | Test with a stocked out component | High | App or Function config via site-engineer |
| C5 | Units per customer at 90 days measured for multipack buyers vs single buyers | Detects cannibalization | Cohort query | Medium | Add to monthly report |
| C6 | No fake decoy options | Wasted space, legal risk | Pricing and PDP review | Medium | Remove or make genuine |

## D. Incentives and discounts

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Discount rate tracked monthly with a target | Discount creep is silent | Report | High | Add metric and target |
| D2 | Promo dependency (share of revenue on promotion) tracked | Measures training to wait | Report | High | Add metric |
| D3 | Stacking rules configured and tested | Unintended stacking is a common loss and incident | Test carts; discount combination settings | Critical | Fix combinations; QA checklist |
| D4 | Codes have usage limits; partner codes unique | Leakage to coupon sites | Discount settings | Medium | Limits and unique codes |
| D5 | Excluded SKUs defined (gift cards, new launches, low margin) | Protects margin | Discount scopes | Medium | Add exclusions |
| D6 | Gift with purchase uses landed cost and has reserved stock | Cost accuracy, fulfillment | Gift SKU stock, offer brief | Medium | Reserve stock |

## E. Shipping

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Free shipping threshold set from the AOV distribution and tested | The threshold drives AOV and margin | Histogram, test record | High | Play 4 |
| E2 | Gap filler products exist near the threshold gap | Thresholds without fillers only tax small orders | Product list | Medium | Add fillers; handoff storefront-ux |
| E3 | Shipping cost shown early (PDP or cart) | Extra costs are the top abandonment reason (39% in recent Baymard data) | Storefront check | High | Handoff storefront-ux and cro |
| E4 | Return rate of threshold-crossing orders monitored | Padding and returns | Order level report | Medium | Add guardrail |
| E5 | Cross-border shipping and duty costs current (US de minimis end, EU EUR 3 parcel duty) | Landed cost accuracy | Cost stack date | High | Update costs |

## F. Guarantees and risk reversal

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Guarantee targets the top purchase risk from VOC | Relevance drives lift | VOC summary vs guarantee | Medium | Redesign |
| F2 | Statutory rights not advertised as a special benefit (EU, UK) | Blacklisted practice | Site and ad copy | Critical | Rewrite with compliance |
| F3 | Guarantee cost modeled and claim rate tracked | Prevents silent cost growth | Claims report | Medium | Add tracking |
| F4 | Terms page matches all claims | Consistency, legal | Compare copy | High | Align |

## G. Subscriptions and repeat offers

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Subscription discount set from retention breakeven | Avoids subsidy without frequency gain | Model | High | Recompute |
| G2 | Cancellation as easy as sign-up; one save step maximum | ROSCA, state laws, Amazon order precedent | Walk through the cancel flow | Critical | Fix flow (lifecycle-crm, site-engineer) |
| G3 | Discount duration and renewal price disclosed at sign-up | Material terms | PDP and checkout | Critical | Rewrite with compliance |
| G4 | First order churn and survival curve tracked by offer | Detects discount seekers | Subscription app reports | Medium | Add report |
| G5 | Maximum discount per segment defined for lifecycle flows | Flows must not invent discounts | Offer brief passed to lifecycle-crm | Medium | Define caps |

## H. Promo calendar

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | 12 month promo calendar exists per market with a promo days budget | Prevents reactive discounting | Calendar file | High | Build calendar |
| H2 | Pre-event prices stable for the lookback window (30 days EU and UK; 10 days Turkey ads) | Legal reference price | Price history | Critical | Freeze prices; compliance |
| H3 | Post-mortems done for the last 2 tent-pole events with pull-forward analysis | Learning loop | Outputs folder | Medium | Run post-mortem |
| H4 | Value-add events mixed with price events | Reduces discount training | Calendar | Medium | Rebalance |

## I. Channel conflict

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Channel price map for hero SKUs maintained (dated) | Visibility of conflicts | Price map | High | Request market-intel monitoring |
| I2 | DTC promos checked for Amazon featured offer and retailer impact before launch | Avoids channel damage | Offer briefs | High | Conflict procedure |
| I3 | No resale price maintenance, discount caps or online MAP enforcement in EU, UK, Turkey | Fines up to 10% of turnover | Contracts and communications review by counsel | Critical | Legal review |
| I4 | DTC exclusive assortment or value-add strategy for conflict-prone SKUs | Protects channels | Assortment list | Medium | Design exclusives |

## J. Price display and legal handoff

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| J1 | Daily price history stored per SKU and channel | Evidence for reference prices | Data source | Critical | Set up export or app |
| J2 | Reference prices and percentages computed from the lowest prior price | Omnibus, CJEU Aldi Süd, ACM, Turkey rules | Sample 10 promoted SKUs | Critical | Fix and document |
| J3 | Headline prices include mandatory fees (drip pricing rules) | UK blacklist, US state laws | Checkout walk-through | Critical | Fix with compliance |
| J4 | "Free" claims truly free; urgency and stock claims true | Blacklisted practices | Copy and timer review | High | Remove or fix |
| J5 | Price tests reviewed for personalization disclosure and feed parity | Legal and Merchant Center risk | Test plans | High | Redesign tests |

## K. Measurement and implementation

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| K1 | Every order carries its offer ID (code, automatic discount, gift SKU, tag) in the backend export | Cohort and incrementality analysis | Sample export | Critical | Handoff measurement |
| K2 | Offer tests use contribution per visitor or cohort contribution as primary metric | Conversion alone misleads | EXPERIMENTS.md rows | High | Rewrite test plans |
| K3 | Promo email and SMS sends use holdouts at least quarterly | Measures true incrementality | Lifecycle reports | Medium | Ask lifecycle-crm |
| K4 | Launch QA checklist used for every offer | Prevents incidents | Change requests | High | Adopt checklist |
| K5 | Shopify Scripts fully replaced by Functions or native settings and checked for double discounts (Plus stores) | Scripts sunset 2026-06-30 | Discount list, test carts | Critical (Plus) | site-engineer audit |
| K6 | Feed sale prices and promotions match site offers | Disapprovals, misleading ads | Merchant Center diagnostics | High | Handoff commerce-feeds |

## Scoring rubric

```
Item score = status points (2, 1, 0) x severity weight (3, 2, 1)
Section score % = sum of item scores / sum of maximum item scores (N/A excluded)
Total score % = sum over all sections / maximum
```

| Total score | Rating | Meaning |
|-------------|--------|---------|
| 85% to 100% | Strong | Offers are designed and measured on contribution; focus on testing bolder offers |
| 70% to 84% | Sound with gaps | Fix High items within 30 days |
| 50% to 69% | Leaking margin | Fix Critical items now; pause new offers until A, D3, J1 to J3 and K1 pass |
| Below 50% | Unmanaged | Stop new promotions; rebuild economics and legal basics first |

Any Critical item at Fail (0) is reported at the top of the audit regardless of the total score. Critical legal items (F2, G2, G3, H2, I3, J2, J3) also go to `compliance` the same day.

## Audit output template

```
# Offer audit: <brand> | Date | Data sources and date ranges
## Score summary (total %, section %, rating)
## Critical failures (item, evidence, fix, owner)
## Top 5 opportunities ranked by expected monthly contribution (with assumptions labeled)
## Full results table
## Test backlog (EXPERIMENTS.md rows drafted)
## Legal and channel risks
## Handoffs requested
```
