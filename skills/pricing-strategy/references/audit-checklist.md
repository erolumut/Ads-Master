# Pricing Audit Checklist (scored)

Run quarterly, at every new market or channel entry, after any cost shock above 5%, and before a Commercial Pricing Report when no audit exists from the last 90 days. Score each item: Pass (2), Partial (1), Fail (0), N/A (excluded). Severity: Critical (C), High (H), Medium (M), Low (L). Any Critical fail goes to the top of the output.

Output file: `ads-master/outputs/pricing-strategy/YYYY-MM-DD_pricing-strategy_audit.md`.

## A. Cost basis and data quality

| # | Check | Why | How to verify | Sev | Fix |
|---|-------|-----|---------------|-----|-----|
| A1 | Landed COGS per SKU exists with an "as of" date under 6 months (3 in Turkey) | All prices rest on it | Cost sheet, costing tool | C | Build or refresh cost sheet |
| A2 | Cost to serve per order modeled by basket size (packaging, pick, carrier band, payment, returns) | Minimum basket and threshold depend on it | Script run in outputs | C | Run [Cost to serve](cost-to-serve-and-margin-waterfall.md) |
| A3 | Missing inputs flagged INCOMPLETE, not computed as zero | Zero costs inflate margins | Inspect sheets and script status line | H | Fill inputs or mark incomplete |
| A4 | Overrides inherit product to brand to company; blanks are inherit, not zero | Silent zero costs | Inspect costing tool settings | H | Fix inheritance |
| A5 | Every percentage labeled margin_on_price or markup_on_cost | Mixing misprices by a third | Read reports and sheets | H | Relabel |
| A6 | Carrier surcharges (fuel, energy, zone) included | Surcharges near 25% on some carriers | Carrier invoices vs model | H | Add surcharge |
| A7 | Payment fee model reflects method mix (fixed vs percent) | Small baskets dominated by fixed fees | PSP report | M | Update mix |
| A8 | VAT rate per product class confirmed | Revenue errors of 10%+ | Tax adviser or official list | H | Confirm |
| A9 | Fully loaded margin computed at month close from actuals, not used for single price decisions | Wrong decision layer | Finance pack | M | Separate layers |

## B. Price level and positioning

| # | Check | Why | How to verify | Sev | Fix |
|---|-------|-----|---------------|-----|-----|
| B1 | Benchmark of 3 to 8 competitors normalized per unit and value unit, dated within 30 days (7 in Turkey) | Price level evidence | Benchmark table | H | Request `market-intel` data; normalize |
| B2 | Regular and effective (promo weighted) price index computed | Promo heavy competitors mislead | Benchmark | M | Add promo frequency and depth |
| B3 | Written positioning hypothesis with proof based strengths and weaknesses | Defensible price | Report section | M | Write it |
| B4 | Price index consistent with the chosen position | Under or overpricing | Index vs position band | H | Plan change |
| B5 | WTP evidence exists for the hero price (survey or test) | Confidence | Research files | M | Plan research |

## C. Architecture

| # | Check | Why | How to verify | Sev | Fix |
|---|-------|-----|---------------|-----|-----|
| C1 | 2 to 4 rungs per line with named roles | Clarity | Assortment | M | Simplify |
| C2 | CM2 per order rises with every rung | Ladder economics | Script ladder check | H | Reprice rungs |
| C3 | Per unit price falls up the ladder in regular and promo states (no quantity surcharge) | Trust and unit price display | Price table incl promos | H | Fix prices |
| C4 | Entry rung clears the minimum viable basket | Avoid loss making orders | Script | C | Re-pack or minimum |
| C5 | Price endings follow one rule; no small left digit crossings | Left digit bias | Price list | L | Re-round |
| C6 | No hidden shrinkflation; pack changes communicated | Law in FR and AT; reputation | Change log | H | Communicate, compliance |

## D. Minimum basket and delivery

| # | Check | Why | How to verify | Sev | Fix |
|---|-------|-----|---------------|-----|-----|
| D1 | Share of orders below minimum viable basket known | Size of the loss | Order export | H | Compute |
| D2 | Free delivery threshold at or above the economic floor | Each order near threshold must clear floor | Script section 3 | C | Raise threshold or change fee |
| D3 | Hero rung qualifies for free delivery | Mix toward hero | Prices vs threshold | M | Align |
| D4 | Dead zone analyzed | Hidden contribution loss | Script scan | M | Adjust threshold |
| D5 | Delivery fees and minimums shown clearly before checkout (C-62/25) | Legal | Site check | H | `compliance`, `storefront-ux` |
| D6 | Thresholds per zone for cross-border | Cost differs by zone | Settings | M | Zone thresholds |

## E. Channels

| # | Check | Why | How to verify | Sev | Fix |
|---|-------|-----|---------------|-----|-----|
| E1 | Channel price map per pack and unit (DTC, retail shelf, marketplace) dated | Conflict visibility | Corridor table | H | Build |
| E2 | No like-for-like pack sold on DTC below observed shelf per unit without a decision | Retail conflict | Corridor table | H | Differentiate or reprice own channel |
| E3 | No reseller price instructions, minimums, discount caps or MAP pressure anywhere (emails, contracts, portals) | Hardcore competition law | Review communications with `compliance` | C | Stop, legal review |
| E4 | Marketplace pack prices clear fees and CM targets | Fee drag | Fee model | M | Reprice or re-pack |
| E5 | Brand CM per unit compared across channels | Channel strategy | Report | M | Compute |

## F. Price claim parity and display

| # | Check | Why | How to verify | Sev | Fix |
|---|-------|-----|---------------|-----|-----|
| F1 | Price claim parity: advertised price (ads, emails) = sum of shown line items = JSON-LD Offer price = feed price = checkout price, per SKU and market | Mismatches cause Merchant Center disapprovals, misleading pricing and wrong price incidents | Sample 10 SKUs: ad, PDP visible price, PDP structured data, feed (Merchant Center diagnostics), checkout total with delivery | C | Hand mismatches to `commerce-feeds` (feed, structured data) and `site-engineer` (site, checkout); log as incident if a wrong price is live |
| F2 | Unit prices displayed where required (per kg, l, 100 g; UK PMO 2026 scope) | Legal | PDP and shelf | H | `compliance`, `storefront-ux` |
| F3 | Prior price evidence kept 30 days (EU) and 10 days (Turkey) for any discount display | Legal | Price history | H | Price history store |
| F4 | Prices incl VAT for consumers; ex VAT labeling for B2B clear | Legal | Site | H | Fix display |
| F5 | No personalized prices based on personal data without disclosure and compliance sign off | Law (EU disclosure, US states) | Tool settings, tests | C | Stop, review |

## G. Change management and tests

| # | Check | Why | How to verify | Sev | Fix |
|---|-------|-----|---------------|-----|-----|
| G1 | Price change log with dates, reasons, cost index | Evidence (Turkey unfair price rules), learning | DECISIONS.md, journal | M | Start log |
| G2 | Price changes go through change requests with snapshot and rollback (G3) | Guardrails | Change requests | C | Enforce |
| G3 | Subscribers and contracts grandfathered per policy | Churn and law | Policy | M | Define policy |
| G4 | Price tests use lawful designs and contribution metrics | Trust and validity | EXPERIMENTS.md | H | Redesign |
| G5 | Inflation repricing rule defined for high inflation markets | Margin erosion | Policy | H | Define band rule |

## H. B2B and SaaS (if applicable)

| # | Check | Why | How to verify | Sev | Fix |
|---|-------|-----|---------------|-----|-----|
| H1 | Value metric documented and scored | Revenue scales with value | Pricing doc | M | Workshop |
| H2 | Price waterfall per account; pocket price dispersion known | Leakage | CRM and invoices | H | Build waterfall |
| H3 | Discount approval matrix enforced | Leakage | CRM | M | Enforce |
| H4 | Indexation clauses applied at renewal | Realization | Contracts | H | Apply |
| H5 | AI credit pricing above inference cost at target margin | Margin | Cost data | H | Reprice |

## Scoring rubric

```
Score % = sum(points) / (2 x applicable items) x 100
```

| Score | Rating | Meaning |
|-------|--------|---------|
| 85 to 100 | Strong | Pricing system is evidence based; focus on tests and fine tuning |
| 70 to 84 | Adequate | Gaps in one or two sections; fix High items this quarter |
| 50 to 69 | Weak | Prices rest on partial evidence; full Commercial Pricing Report recommended |
| under 50 | Critical | Cost basis or legal exposure unclear; fix Critical items before any pricing change |

Any Critical fail caps the rating at Weak regardless of score.

## Audit output template

```markdown
# Pricing audit: <brand> <date>
Data used: <files, date ranges, connectors>; cost basis as of <date>; status COMPLETE | INCOMPLETE (missing: ...)
Score: <x%> (<rating>); Critical fails: <list>
## Critical fails (fix first)
## Top 5 opportunities with estimated contribution impact (labeled estimate)
## Section results (A to H tables with scores)
## Parity sample (F1): SKU | ad price | PDP price | JSON-LD | feed | checkout | match?
## Recommended next steps and owners
## Handoffs requested
```
