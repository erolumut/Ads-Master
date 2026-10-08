# Unified Metrics and the Daily Report

> Knowledge as of 2026-10. Scope: one daily fact table that every agent reads, the formulas for every calculated metric, how to show platform reported and backend observed numbers side by side, decision windows, status logic derived from the project's target CPA, a copy-paste daily report template, data sources per stack, and `scripts/daily_report.py`. The project's `ads-master/METRICS.md` is the source of truth for definitions; this module is the default it starts from. Warehouse SQL and dashboards live in [Dashboards and reporting](dashboards-and-reporting.md); value design in [Value and profit optimization](value-and-profit-optimization.md); why numbers disagree in [Attribution](attribution.md).

## 1. Rules

1. Two columns, never merged: platform reported (what each ad platform claims) and backend observed (orders, revenue and customers in the store, CRM or ERP). Sum of platform conversions is never truth.
2. Report daily, decide on 3 and 7 day windows. Act on a single day only for incidents (tracking break, delivery stop, overspend, disapproval, stockout).
3. Every report separates FACTS (numbers with sources), INTERPRETATION (what they likely mean) and RECOMMENDATION (what to do, with the approval it needs), and states a confidence level.
4. Status colors derive from the project's target CPA (and the implied targets it produces), never from industry benchmarks or fixed numbers.
5. One currency, one time zone, one definition set. Convert currency with dated FX rates; align platform account time zones with the backend.
6. PII rule: aggregates only. Order IDs are hashed (salted SHA-256) wherever they must appear; no names, emails, phones or addresses in any report, journal, memory or CSV the agents write.
7. State the data used: files or connectors, date range, time zone, export time. A number without a source does not go in the report.

## 2. The standard daily fact table

Grain: one row per date (report time zone). Platform fields can also be kept at date x channel grain; the daily report needs both.

| Column | Type | Source | Definition |
|--------|------|--------|-----------|
| date | date | all | Calendar day in the report time zone |
| spend_<channel> | money | platform export or API | Media spend per channel (Meta, Google, Microsoft, TikTok, LinkedIn, ChatGPT ads, other) |
| spend_total | money | sum | All media spend; agency and tool fees are a separate line if METRICS.md includes them |
| impressions, clicks | count | platform | Use link clicks (Meta) or clicks to the site, not all clicks; name the column choice in METRICS.md |
| platform_conversions_<channel> | count | platform | Primary conversion with the attribution setting written in METRICS.md |
| platform_conversion_value_<channel> | money | platform | Value of the same conversions |
| orders | count | backend | Paid, non test, non cancelled orders created that day |
| revenue | money | backend | Product revenue after discounts, ex tax, ex shipping |
| new_customer_orders, new_customer_revenue | count, money | backend | First ever order of the customer (or no order in 365 days if METRICS.md says so) |
| repeat_orders | count | derived | orders minus new_customer_orders |
| bundle_mix | counts | backend | Orders and revenue per bundle or SKU group |
| discounts | money | backend | Discount amount granted (codes, automatic, bundle discounts) |
| shipping_charged | money | backend | Shipping paid by the customer |
| shipping_cost | money | 3PL invoice, carrier API or per order estimate | Real or estimated cost of shipping the order |
| product_cost | money | ERP, cost per item field, finance sheet | Landed COGS of items sold |
| bonus_product_cost | money | backend plus COGS | Cost of free gifts or bonus items in the order |
| refunds | money | backend | Refunded amount; record by order date for cohort views or by refund date for cash views, and say which |
| payment_fees | money | PSP report or rate | Optional; rate x (revenue + shipping) plus fixed fee |
| orders_without_utm | count | backend | Orders with no utm_source (or landing click ID) |

Store it as `ads-master/data/imports/fact_daily.csv` (written by `daily_report.py --fact-table`) or as `fct_marketing_daily` in the warehouse.

## 3. Calculated metrics

| Metric | Formula | Use | Watch out |
|--------|---------|-----|-----------|
| CTR | clicks / impressions | Creative and audience fit | Define the click type |
| CPC | spend / clicks | Auction cost | Rises with better placements; not a goal |
| CPM | spend / impressions x 1000 | Reach cost, seasonality | Q4 inflation; compare same weeks last year |
| Platform CPA | platform spend / platform conversions | In-platform optimization | Attribution setting dependent; overlapping credit |
| Platform ROAS | platform conversion value / spend | In-platform optimization | Same as above |
| Blended CAC (cost per order) | media spend / all orders | Total efficiency | Repeat customers lower it; not an acquisition metric |
| nCAC | media spend / new customer orders | Acquisition efficiency, compared with target CPA | Backend new customer flag must be reliable |
| AOV | revenue / orders | Basket health | Bundles and gifts move it |
| New customer AOV | new customer revenue / new customer orders | Input to implied aMER target | Usually below repeat AOV |
| MER | net revenue / media spend | Blended efficiency, cannot be gamed by attribution | Includes organic and repeat demand |
| aMER | new customer net revenue / media spend | Acquisition efficiency | Define once if spend is total or acquisition only |
| Net revenue | revenue minus refunds | Base for MER | Pick order date or refund date for refunds |
| Contribution before marketing (CM2) | net revenue + shipping charged minus product cost minus bonus product cost minus shipping cost minus payment fees | Money the order leaves before ads | Add packaging and pick and pack if material |
| Contribution after marketing (CM3) | CM2 minus media spend | Profit-led north star | Negative is acceptable only if STRATEGY.md funds LTV-backed acquisition |
| POAS (blended) | CM2 / media spend | Profit return per unit of spend; 1.00x is first order breakeven | Platform POAS needs margin values sent server side |
| Shipping subsidy | max(0, shipping cost minus shipping charged), per order | Hidden acquisition cost of free shipping | Estimate cost per zone if invoices lag |
| Incremental discount cost | discount above the baseline discount a customer would get anyway, per order | Hidden acquisition cost of welcome codes | Baseline per METRICS.md (default 0 for first order codes) |
| Acquisition investment | media spend + shipping subsidy + bonus product cost + incremental discount cost (on new customer orders, unless METRICS.md says all orders) | The full cost of buying a new customer | Same scope every day |
| Blended first order acquisition cost | acquisition investment / new customers | Compare with target CPA and first order contribution | Always above nCAC when offers subsidize acquisition |
| First order contribution per new customer | CM2 of new customer orders / new customers | Payback on the first order | If below acquisition cost, payback depends on repeat purchases |
| Discount rate | discounts / (revenue + discounts) | Promo depth | Rising rate with flat AOV erodes margin |
| Refund rate | refunds / revenue | Quality, fraud, offer fit | Lags by days to weeks |
| Platform ratio | sum of platform conversions / backend orders (also value / net revenue) | Attribution inflation tracker | Track its trend, not its level |
| Deflated CPA | channel spend / backend orders with that channel's UTM | Last click backend view per channel | Undercounts view-through and cross device effects |
| Implied aMER target | new customer AOV / target CPA | Green line for aMER | Recompute when AOV moves |
| Translated platform CPA target | target CPA / platform ratio | Target to enter in a platform bid strategy | Use the 28 day ratio; tell the channel agent |

Worked example (sample data, last 7 days to 2026-10-07, fictional brand): spend EUR 7,087.50; 245 orders, 147 new; net revenue EUR 8,830.25. nCAC = 7,087.50 / 147 = EUR 48.21. Acquisition investment = 7,087.50 + 338.40 shipping subsidy + 77.70 bonus cost + 390.75 incremental discount = EUR 7,894.35, so first order acquisition cost = EUR 53.70. First order contribution = EUR 19.98, so the brand loses about EUR 33.72 per new customer on the first order and needs repeat purchases to pay back. With a target CPA of EUR 45 and new customer AOV EUR 35.68, the implied aMER target is 0.79x; actual 0.73x is AMBER.

## 4. Platform reported vs backend observed

Always show both, per window, with the ratio and the share of orders without UTMs. Explain gaps with these causes before anyone calls a channel good or bad.

| Cause | Direction | How to check | What to do |
|-------|-----------|-------------|------------|
| Attribution windows (7-day click, 1-day view, 30-day click) | Platform higher | Attribution setting per platform in METRICS.md | Compare like for like; never change windows to make numbers look better |
| View-through and engaged-view credit | Platform higher | Click only columns vs default columns | Report click-through separately; test incrementality |
| Several platforms claiming one order | Sum of platforms above backend | Platform ratio above 1 and rising with more channels | Use backend for allocation; incrementality tests decide credit |
| Cross device and modeled conversions | Platform higher than UTM view | Platform notes on modeled data | Accept; calibrate with lift tests |
| Consent denied, ad blockers, ITP | Platform and GA4 lower | Capture rate by region and browser | Server-side events, conversion APIs, consent mode |
| Missing or stripped UTMs, in-app browsers | Backend channel view lower | orders_without_utm share | Fix UTM templates; capture click IDs server side |
| Returning customers re-converting via ads | Platform higher; nCAC unaffected | New customer share per platform | Exclude purchasers where the platform allows; bid on new customer value |
| Time zone or date of conversion vs click date | Day level mismatch | Account time zones; conversion date setting | Compare 3 and 7 day windows |
| Refunds and cancellations | Platform higher on value | Backend refunds | Send adjustments or retractions where supported |

Interpretation rule: a platform ratio far below 1 suggests tracking loss (hand to measurement); far above 1 suggests overlapping credit. Judge both against the project's own 28 day history, not a fixed band.

## 5. Decision windows

| Window | Use | Allowed decisions |
|--------|-----|------------------|
| Yesterday (1 day) | Incident detection, pacing | Pause for incidents only (broken checkout, tracking at zero, runaway spend, policy issues, stockouts); everything else waits |
| Last 3 days | Early signal | Prepare a hypothesis, check creative fatigue and offers, brief channel agents |
| Last 7 days | Primary decision window | Budget and bid proposals (with approval), creative rotation, scaling candidates |
| 14 to 28 days | Structural | Channel mix, target changes, translated platform targets, incrementality readouts |
| Cohort (30, 60, 90 days) | Payback | Allowable CAC and target CPA updates |

Channel agents apply their own learning phase rules on top (for example, how often a bid strategy can change). The daily report never authorizes changes by itself.

## 6. Status logic from the target CPA

Target CPA = the allowable cost per new customer in METRICS.md or STRATEGY.md (set from first order contribution plus the payback the business accepts, for example contribution from the first order plus repeat contribution expected within the payback window). The script and the template derive every color from it:

| Metric | GREEN | AMBER | RED |
|--------|-------|-------|-----|
| nCAC, blended first order acquisition cost | at or below target CPA | up to target x (1 + band) | above that |
| aMER | at or above implied target (new customer AOV / target CPA) | down to implied target / (1 + band) | below that |
| POAS | at or above 1.00x (first order breakeven) | down to 1 / (1 + band) | below that |
| Platform CPA per channel | at or below translated target (target / platform ratio) | up to translated target x (1 + band) | above that; label "platform reported" |

Band: default 0.2. Derive it from noise when possible: the relative noise of a count of n new customers is about 1 / sqrt(n), so a two standard deviation band is about 2 / sqrt(n). With 147 new customers in 7 days that is about 0.16; with 25 it is 0.4 (Starter tier noise). Use `--amber-band` to set it and record the choice in METRICS.md. Status changes need both the 3 and 7 day windows to agree before a recommendation moves money.

## 7. Daily report template

Save as `ads-master/outputs/measurement/YYYY-MM-DD_measurement_daily-report.md` (or the path the `ads-review` daily mode uses). Never overwrite.

```markdown
# Daily report: <brand>, <YYYY-MM-DD (yesterday)>
Data used: <platform exports or connectors with date range>; <backend source> to <date>; time zone <tz>; currency <cur>; exported <time>.
Target CPA: <value> (METRICS.md). Band: <x>%. Confidence: <High | Medium | Low> (<reasons>).

## 1. Status
| Metric | 1d | 3d | 7d | Target logic | Status 3d | Status 7d |
nCAC, first order acquisition cost, aMER, MER, POAS, contribution after marketing

## 2. FACTS
### 2.1 Platform reported by channel (spend, CTR, CPC, CPM, conversions, CPA, ROAS)
### 2.2 Backend observed (orders, new, repeat, revenue, refunds, net revenue, AOV, new AOV, discounts, shipping charged and cost, product and bonus cost, CM2)
### 2.3 Unit economics (acquisition investment and its parts, blended CAC, nCAC, first order acquisition cost, first order contribution, MER, aMER, POAS, CM3)
### 2.4 Platform reported vs backend observed (ratios per window, per channel UTM view, orders without UTM, gap explanation)
### 2.5 Product and bundle mix
### 2.6 Incident checks (yesterday)

## 3. INTERPRETATION
- <one line per signal, each pointing at a fact above; say "likely" when it is inference>

## 4. RECOMMENDATION
- <action, owner slug, approval needed (yes), window it is based on, what would change the call>

## 5. Open questions and data gaps
```

Confidence rubric:

| Level | Criteria (all must hold) |
|-------|--------------------------|
| High | At least 30 new customers in the 7 day window, every channel has spend rows for all 7 days, orders for all 7 days, at least 80% of orders carry a UTM or click ID, no open tracking incident |
| Medium | At least 10 new customers, or one minor gap (one missing day for one channel, UTM coverage 60% to 80%) |
| Low | Fewer than 10 new customers, several missing days, an open tracking incident or a known definition change in the window |

Incident checks (run on yesterday): spend with zero backend orders; backend orders with zero platform conversions while spending (tracking break); spend above 1.5x or below 0.5x the 7 day daily average; platform ratio moved more than 50% vs 7 days; a channel with no spend row. Any hit opens an entry in `ads-master/INCIDENTS.md` and goes to the top of the report.

## 8. Data sources per stack

| Stack | Orders and revenue | New customer flag | Costs | Refunds | Access |
|-------|-------------------|-------------------|-------|---------|--------|
| Shopify | Admin GraphQL API orders (or Analytics reports, or the orders CSV export with personal columns removed) | Compute from first order per hashed customer ID; Shopify analytics also offers a new vs returning customer split [verify report names in the store] | Variant cost per item (inventory item unit cost) for COGS; shipping label or 3PL invoices for shipping cost | Order refunds in the API; refund date differs from order date | Custom app token with read_orders, read_products; never store the token in files |
| WooCommerce | REST API `wc/v3/orders` or Analytics > Orders export | Compute from customer history (guest orders by hashed email inside the export job, then drop the email) | Cost of goods plugin or core COGS field where available [verify version] | Refunds endpoint | Read only API keys |
| CRM (HubSpot, Salesforce, Pipedrive) | Closed won deals as orders, amount as revenue (B2B and lead gen) | First closed won deal per company | Gross margin per product line from finance | Credit notes | Read scopes; see [Offline and CRM](offline-and-crm-conversions.md) |
| GA4 | Not the order truth; use for sessions, landing pages, AI assistant channel, capture rate | n/a | n/a | n/a | GA4 MCP server or Data API; BigQuery export |
| BigQuery or warehouse | `fct_orders`, `fct_marketing_daily` | `dim_customers` first order date | COGS table by SKU and date | Refund table | MCP Toolbox for Databases or BigQuery API; SQL in [Dashboards](dashboards-and-reporting.md) |
| Platform CSV exports | Meta Ads Manager (Amount spent, Impressions, Link clicks, Purchases, Purchases conversion value), Google Ads (Cost, Impr., Clicks, Conversions, Conv. value), Microsoft Ads (Spend, Impr., Clicks, Conv., Revenue), TikTok (Cost, Impressions, Clicks, Purchases or Complete payment, value) | n/a | n/a | n/a | Column names vary by locale and version; map them to the standard columns in `ads-master/data/imports/HOW_TO_EXPORT.md` |
| MCP connectors | Google Ads MCP (read GAQL), Google Analytics MCP, community Meta, TikTok and LinkedIn servers, Shopify Dev MCP for API schemas | | | | Read only scopes; see [Tools, APIs and MCP](tools-api-mcp.md) |

Export rule: one file per platform per day range, daily grain, account time zone noted in the file name or HOW_TO_EXPORT.md, currency stated.

## 9. Running daily_report.py

Location: `skills/measurement/scripts/daily_report.py`. Python 3 standard library only. Sample inputs (fictional brand "Example Socks Co.", 14 days, 489 orders) are in `skills/measurement/scripts/samples/`.

```bash
python3 daily_report.py \
  --spend ads-master/data/imports/meta_ads.csv ads-master/data/imports/google_ads.csv \
  --orders ads-master/data/imports/orders.csv \
  --target-cpa 45 --currency EUR --brand "Example Socks Co." \
  --payment-fee-rate 0.029 --channel-map "newsletter=email" \
  --fact-table ads-master/data/imports/fact_daily.csv \
  --out ads-master/outputs/measurement/2026-10-08_measurement_daily-report.md
```

| Input | Columns |
|-------|---------|
| `--spend` (one or more) | date, channel, spend, impressions, clicks, conversions, conversion_value |
| `--orders` | date, order_id, revenue, is_new_customer, discount, shipping_charged, shipping_cost, product_cost, bonus_product_cost, refund, utm_source, bundle (or sku_group) |

| Option | Default | Meaning |
|--------|---------|---------|
| `--target-cpa` | none | Enables status colors; without it the report says "no status" |
| `--amber-band` | 0.2 | Share above target that is still AMBER (section 6) |
| `--date` | latest date in data | The "yesterday" of the report |
| `--acq-scope` | new | Count shipping subsidy, bonus cost and discount on new customer orders only, or `all` |
| `--baseline-discount` | 0 | Per order discount that is not acquisition cost |
| `--payment-fee-rate`, `--payment-fee-fixed` | 0 | Payment fee estimate for contribution |
| `--channel-map` | built in | Extra utm_source to channel pairs; defaults map facebook, ig, instagram to meta, google and youtube to google, bing to microsoft, and others |
| `--salt` or env `DAILY_REPORT_SALT` | empty | Salt for hashing order IDs in warnings |
| `--fact-table` | none | Writes the daily fact table CSV |

Behavior: rows with bad numbers are skipped with a warning; duplicate order IDs are counted once and reported as hashed IDs; columns that look like personal data (email, phone, name, address, IP) are ignored and flagged; the report lists warnings at the end. Numbers accept `1234.5` and `1234,5`.

Tested 2026-10-08 on the samples: 14 day fact table written; report produced nCAC 7 days EUR 48.21 vs target EUR 45 (AMBER), first order acquisition cost EUR 53.70, platform to backend order ratio 0.95x, Meta platform conversions 1.54x its UTM orders, confidence High. Edge tests: a missing Google day dropped confidence to Medium and raised the "no spend recorded" incident; an extra email column was ignored with a PII warning; a duplicated order row was counted once; without `--target-cpa` the report showed no status.

Wire it into the `ads-review` daily mode: export or pull data, run the script, read the FACTS, write INTERPRETATION and RECOMMENDATION with judgement (the script's rule based lines are a draft), and journal anything other agents must know.

## 10. Common mistakes

| Mistake | Fix |
|---------|-----|
| Summing platform ROAS into a "total ROAS" | Use MER and aMER from the backend |
| Judging a channel on yesterday | 3 and 7 day windows; single days only for incidents |
| Ignoring free shipping and gifts in CAC | Acquisition investment and first order acquisition cost |
| Fixed color thresholds copied from another brand | Derive from target CPA, implied aMER and POAS breakeven |
| Mixing order date refunds and refund date refunds | Choose one in METRICS.md |
| New customer flag from the platform | Backend first order per hashed customer ID |
| Pasting order exports with names and emails into the workspace | Strip personal columns at export; hash IDs |
| Changing attribution settings without annotation | Journal entry and a note in the report, rebaseline targets |

## 11. Sources

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | Shopify Admin GraphQL API | Shopify | https://shopify.dev/docs/api/admin-graphql | versioned | Orders, refunds, inventory item unit cost |
| 2 | WooCommerce REST API documentation | WooCommerce | https://woocommerce.github.io/woocommerce-rest-api-docs/ | n.d. | Orders and refunds endpoints |
| 3 | Google Analytics MCP server | Google | https://github.com/googleanalytics/google-analytics-mcp | 2025 | Read only GA4 reports |
| 4 | Google Ads MCP server | Google | https://github.com/googleads/google-ads-mcp | 2025 | Read only GAQL |
| 5 | Dashboards and reporting, Value and profit optimization, Attribution | Ads Master measurement package | [Dashboards](dashboards-and-reporting.md), [Value and profit](value-and-profit-optimization.md), [Attribution](attribution.md) | 2026-10 | Metric dictionary, POAS, platform gaps |
| 6 | daily_report.py sample run | This repository | skills/measurement/scripts/samples/ | 2026-10-08 | Worked example numbers (fictional data) |
