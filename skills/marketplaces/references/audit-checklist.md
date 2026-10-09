# Marketplace Audit Checklist (scored)

> Score each item Pass (2), Partial (1), Fail (0) or N/A. Severity weights: Critical x3, High x2, Medium x1. Record evidence (report name, export file, screenshot, date range) for every score. Never score from memory or assumption. Run per marketplace and country; summarize across marketplaces at the end.

## A. Economics

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | CM2 per unit (before ads) known for every active SKU with fees read from the account this quarter | Ads targets and prices depend on it | Unit economics output with sources and dates | Critical | Build with [Unit economics](marketplace-unit-economics.md) |
| A2 | Breakeven ACoS per product group documented and used for targets | Prevents loss making ads | Ads targets vs breakeven table | Critical | Recompute; reset targets |
| A3 | Marketplace CM3 (after ads) positive for at least 80% of revenue | Profitability | Monthly P and L by SKU | High | Price, fee, ad or assortment fixes |
| A4 | VAT basis consistent (gross vs net) in ACoS targets | Common error inflates allowed ACoS | Target sheet notes | High | Align basis |
| A5 | Fee changes of the last 12 months applied (Amazon US 2026-01-15, Amazon EU 2026-01-05, bol LVB 2026-09-09, noon 2026-10-01, Turkish cargo updates) | Margin shocks | Date of last fee refresh | High | Fee change protocol |
| A6 | Turkish lira inputs refreshed monthly and compared in real terms | Inflation distorts trends | Report notes | Medium | Monthly refresh |

## B. Account health and compliance

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | No open account health warnings or policy violations | Suspension risk | Account Health dashboard, partner panels | Critical | POA or document submission (human approved) |
| B2 | ODR under 1%, late shipment under 4%, cancellations under 2.5%, valid tracking over 95% (Amazon FBM) | Account health | Account Health | Critical | Operations fixes |
| B3 | Seller scores at target (bol partner rating, Trendyol seller score 9.0 or higher, Hepsiburada store score stable) | Buybox and visibility | Panels | High | Service and delivery fixes |
| B4 | Compliance documents on file per SKU (GPSR, CE, CPSC, SASO as relevant; invoices from authorized sources) | Authenticity and safety complaints | Compliance folder | High | Collect before next audit |
| B5 | Customer questions answered within 24 hours | Scores and conversion | Panels | Medium | Rota and templates |
| B6 | Turkish 2027 marketplace liability preparation (defect process, documentation) | Constitutional Court decision effective 2027-03-02 | Process doc | Medium | Prepare with compliance |

## C. Inventory and fulfillment

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | In-stock rate above 98% on top 20% SKUs (last 90 days) | Rank and ads continuity | Inventory history | Critical | Reorder points |
| C2 | Days of cover 4 to 8 weeks in marketplace warehouses; under 90 days of cover to avoid aged fees | Fees and stockouts | Restock and inventory reports | High | Rebalance, AWD or 3PL buffer |
| C3 | Event stock planned 8 to 12 weeks ahead | Capacity limits | Event plan | High | Plan |
| C4 | Stranded, suppressed and unfulfillable inventory near zero | Wasted storage | Reports | Medium | Fix listings, removal orders (approved) |
| C5 | Fulfillment model chosen per SKU with economics (FBA vs FBM, LVB vs own, TEX desi) | Cost and buybox | Fulfillment matrix | Medium | Decide per SKU |
| C6 | US FBA inbound units arrive prepped and labeled (since 2026-01-01) | Inbound defect fees | Inbound defect report | Medium | Supplier prep spec |

## D. Featured offer and pricing

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Featured offer or buybox above 95% on own brand products | Sales and ads eligibility | Business Reports, panels | Critical | Price, stock, delivery, seller checks |
| D2 | No suppressed featured offers from pricing | Ads stop, sales drop | Pricing Health | High | Price review |
| D3 | Repricers have floor prices from the contribution model | Price wars | Repricer settings | High | Set floors |
| D4 | Channel price map current (within 30 days) | Conflict control | Map file | High | Refresh |
| D5 | Reference price evidence stored (EU 30 days, TR 10 days) for every discount | Legal | Price history | High | Store evidence |

## E. Listings

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Titles follow marketplace rules (Amazon 200 char limit, no banned characters, no word more than twice) | Suppression risk, CTR | Listing export | High | Rewrite |
| E2 | Hero listings answer top 10 shopper questions in bullets or A+ | Conversion and AI assistant answers | Manual review | High | Listing pack |
| E3 | 7 or more images incl. infographics and size; video on hero SKUs | Conversion | Detail pages | High | Image brief |
| E4 | A+ and Brand Story live on hero SKUs (Brand Registry) | Conversion | Detail pages | Medium | Build A+ |
| E5 | Backend search terms under byte limit, no brands or ASINs | Indexing | Listing export | Medium | Clean |
| E6 | Attributes complete (filters) on all marketplaces | Discovery | Catalog quality reports | Medium | Fill attributes |
| E7 | Every fact traceable to PRODUCT_FACTS.md, claims in CLAIMS.md | Compliance | Spot check 10 listings | Critical | Fix and route to compliance |
| E8 | Detail page change monitoring active | Hijacked content | Tool or weekly check | Medium | Set up |
| E9 | Localized by native speakers per market | Conversion and accuracy | Spot check | Medium | Translation review |

## F. Reviews

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | No review incentives, gating or manipulation anywhere | Suspension and fines | Inserts, emails, social, packaging | Critical | Remove immediately |
| F2 | Hero SKUs at 4.3 stars or higher, or a fix plan | Conversion and ads | Product pages | High | Root cause loop |
| F3 | Request a Review automated (approved) | Velocity | Settings | Medium | Enable after approval |
| F4 | Vine used only on eligible, confident new ASINs | Cost and risk | Vine dashboard | Medium | Rules |
| F5 | Monthly review theme report to product team | Product improvement | Output files | Medium | Start loop |

## G. Ads structure

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Campaigns split by intent (brand, category, competitor, discovery, launch) and product group | Control | Campaign names | High | Restructure |
| G2 | Naming convention consistent across marketplaces | Reporting | Campaign list | Medium | Rename (G3) |
| G3 | Harvest and negatives done in the last 30 days | Waste | Search term reports | High | Harvest routine |
| G4 | Bid strategies chosen deliberately (no blanket Dynamic up and down) | Overbidding | Settings | Medium | Change |
| G5 | Ads paused on out of stock, no featured offer or low rating ASINs | Waste | Ads vs inventory | High | Pause rules |
| G6 | Budget caps at portfolio or campaign level match the plan | Spend control | Settings vs STRATEGY.md | Critical | Set caps |
| G7 | Automation (rules, Ads Agent, third-party bidders) has caps and approval logged | Runaway changes | Rules list, logs | High | Add caps |

## H. Ads performance and measurement

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | TACoS tracked weekly with total sales | Real efficiency | Report | Critical | Build report |
| H2 | ACoS by intent at or below targets | Profit | Report | High | Bid changes |
| H3 | Brand defense validated by a holdout in the last 12 months | Waste or protection | EXPERIMENTS.md | Medium | Run test |
| H4 | Search Query Performance reviewed monthly for top queries | Funnel diagnosis | Output | Medium | SQP workflow |
| H5 | Amazon Attribution tags on all external links; Brand Referral Bonus credits tracked | Bonus and halo | Attribution console | High | Tag links |
| H6 | 2026 view attribution change noted in year over year comparisons | Misreads | Reports | Medium | Use all views metrics |
| H7 | AMC 1P paid features opt-out decision before 2026-12-31 | Unplanned fees | AMC settings | Medium | Decide |

## I. Channel conflict

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Assortment split documented (exclusive SKUs, packs) | Conflict prevention | STRATEGY.md | Medium | Design |
| I2 | Calendar coordinated with DTC and retail events | Featured offer loss | Calendar | High | Align |
| I3 | No reseller price instructions or discount caps anywhere | Competition law | Contracts, emails | Critical | Stop and route to compliance |
| I4 | Cannibalization and halo reviewed at least yearly | Channel decisions | Test or analysis | Medium | Test plan |

## J. Data, tools and security

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| J1 | No credentials in files, outputs or memory | Security | Grep workspace | Critical | Remove and rotate (human) |
| J2 | Connectors use least privilege; no buyer PII stored | Privacy | Roles and scopes | Critical | Reduce scopes |
| J3 | Third-party MCP servers reviewed before use | Supply chain | Review notes | High | Review |
| J4 | API versions current (bol v10 non-deprecated endpoints, SP-API inbound v2024-03-20) | Breakage | Integration notes | Medium | Migrate |

## Scoring rubric

```
Item score = status points (2, 1, 0) x severity weight (3, 2, 1)
Section score % = sum of item scores / sum of maximum item scores (N/A excluded)
Total score % = sum over all sections / maximum
```

| Total score | Rating | Meaning |
|-------------|--------|---------|
| 85% to 100% | Strong | Focus on growth tests: new keywords, DSP, new marketplaces |
| 70% to 84% | Sound with gaps | Fix High items within 30 days |
| 50% to 69% | Leaking | Fix Critical items now; freeze ad scaling until A, B, C1, D1 and G6 pass |
| Below 50% | At risk | Stop scaling; account health, stock and economics first |

Any Critical item at Fail is reported at the top regardless of total. Legal items (E7, F1, I3) go to `compliance` the same day; security items (J1, J2) to the human immediately.

## Audit output template

```
# Marketplace audit: <brand> | <marketplaces and countries> | Date | Data sources and date ranges
## Score summary (total %, section %, rating, per marketplace)
## Critical failures (item, evidence, fix, owner)
## Top 5 opportunities ranked by expected monthly contribution (assumptions labeled)
## Full results table
## 30, 60, 90 day plan
## Test backlog (EXPERIMENTS.md rows drafted)
## Change requests needed (G3)
## Handoffs requested
```
