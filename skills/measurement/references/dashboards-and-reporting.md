# Dashboards and Reporting

Reporting exists to drive decisions. This module defines the metric dictionary, the reporting layers, a BigQuery model that joins spend, backend and GA4 data, dashboard specs (Looker Studio or any BI tool), and automated data quality monitoring.

## 1. Metric dictionary

Write these definitions into MEASUREMENT.md so every agent uses the same math.

| Metric | Formula | Notes |
|--------|---------|-------|
| Spend | Sum of media spend (platform reported, in reporting currency) | Add agency and tool fees separately as "total marketing cost" if used in MER |
| Revenue (net) | Backend revenue minus refunds and cancellations, ex tax, ex shipping | Pick gross or net once |
| MER (marketing efficiency ratio) | Revenue / total marketing spend | Blended, cannot be gamed by attribution |
| aMER (acquisition MER) | New customer revenue / total marketing spend | Shows acquisition efficiency; some teams divide by acquisition spend only, define once |
| nCAC | Acquisition spend (or total spend) / new customers | Backend new customer definition (first order ever, or no order in 365 days) |
| Blended CAC | Total marketing spend / all customers acquired | |
| ROAS (platform) | Platform attributed value / platform spend | Optimization metric only |
| Calibrated ROAS | Platform ROAS x incrementality factor | See [Strategy](measurement-strategy-and-kpi-tree.md) |
| POAS | Gross profit (or contribution) attributed / spend | Profit based platform metric |
| CM1 | Revenue minus COGS | Gross profit |
| CM2 | CM1 minus fulfillment, shipping, payment fees, returns | Contribution before marketing |
| CM3 | CM2 minus marketing spend | Contribution after marketing; profit-led North Star |
| First order contribution per new customer | CM2 of first orders / new customers | Compare to nCAC |
| Payback (months) | nCAC / monthly CM2 per customer | From cohort data |
| LTV (12 month, contribution) | Cohort CM2 per customer over 12 months | Cohort tables |
| Cost per qualified lead | Spend / qualified leads (CRM) | Lead gen |
| Pipeline ROAS | Pipeline value created / spend | B2B |
| Closed won ROAS | Closed won revenue (or gross profit) / spend | B2B, lagging |
| Capture rate | GA4 conversions / backend conversions | Data quality |
| Platform ratio | Platform conversions / backend conversions | Attribution inflation tracker |

## 2. Reporting layers

| Layer | Audience | Cadence | Content |
|-------|----------|---------|---------|
| Daily pulse | Operators, agents | Daily | Spend pacing, backend orders or leads vs forecast, MER, data quality status (green, amber, red) |
| Weekly performance | Team, growth-orchestrator | Weekly | Channel table (spend, platform conversions, calibrated CPA or ROAS), MER, aMER, nCAC, new customer share, tests running, incidents |
| Monthly business review | Founders, finance | Monthly | CM3 trend, cohort LTV and payback, reconciliation table, incrementality evidence, budget proposal |
| Quarterly measurement review | Leadership | Quarterly | Audit score, MMM results, test calendar, roadmap |

## 3. BigQuery model

### Sources

| Source | Load method |
|--------|-------------|
| GA4 | Native BigQuery export (daily, optionally streaming) |
| Google Ads | BigQuery Data Transfer Service for Google Ads (native) |
| Meta, TikTok, LinkedIn, Microsoft, Pinterest, Snap, Reddit, ChatGPT Ads | Connector tools (several commercial ETL vendors) or custom API jobs; store daily campaign and ad level spend, impressions, clicks, platform conversions and value with the attribution setting used |
| Backend orders | Shopify, WooCommerce, Stripe, ERP via connector or nightly export; include order_id, customer_id, created_at with timezone, revenue fields, discounts, refunds, new customer flag, payment method, country, landing click IDs |
| CRM | HubSpot, Salesforce, Pipedrive via connector; leads, stages, timestamps, amounts, click IDs |
| COGS and margins | Finance sheet or ERP table by SKU and date |
| Survey | Post-purchase survey app export |

### Layers

1. raw: untouched loads.
2. staging: typed, renamed, deduplicated, currency converted with dated FX, timezone aligned.
3. marts: `fct_marketing_daily` (date x channel x campaign), `fct_orders`, `dim_customers`, `fct_cohorts`, `fct_leads_pipeline`.

### fct_marketing_daily (example)

```sql
-- Daily blended view: spend by channel plus backend outcomes
WITH spend AS (
  SELECT date, channel, SUM(spend) AS spend,
         SUM(platform_conversions) AS platform_conv,
         SUM(platform_value) AS platform_value
  FROM `project.staging.ad_spend_daily`      -- unioned platforms, reporting currency
  GROUP BY 1, 2
),
orders AS (
  SELECT DATE(created_at, 'Europe/Istanbul') AS date,
         COUNT(*) AS orders,
         COUNTIF(is_new_customer) AS new_customers,
         SUM(net_revenue) AS revenue,
         SUM(IF(is_new_customer, net_revenue, 0)) AS new_customer_revenue,
         SUM(cm2) AS cm2
  FROM `project.staging.orders`
  WHERE is_test = FALSE
  GROUP BY 1
),
total_spend AS (
  SELECT date, SUM(spend) AS total_spend FROM spend GROUP BY 1
)
SELECT
  o.date,
  t.total_spend,
  o.orders, o.new_customers, o.revenue, o.new_customer_revenue, o.cm2,
  SAFE_DIVIDE(o.revenue, t.total_spend) AS mer,
  SAFE_DIVIDE(o.new_customer_revenue, t.total_spend) AS amer,
  SAFE_DIVIDE(t.total_spend, o.new_customers) AS ncac,
  o.cm2-t.total_spend AS cm3
FROM orders o
LEFT JOIN total_spend t USING (date)
ORDER BY o.date;
```

Use 7-day and 28-day rolling sums for decisions; daily ratios are noisy.

### Cohort LTV (example)

```sql
WITH first_orders AS (
  SELECT customer_id, MIN(DATE(created_at)) AS first_date
  FROM `project.staging.orders` WHERE is_test = FALSE GROUP BY 1
)
SELECT
  DATE_TRUNC(f.first_date, MONTH) AS cohort_month,
  DATE_DIFF(DATE(o.created_at), f.first_date, MONTH) AS months_since_first,
  COUNT(DISTINCT f.customer_id) AS customers_active,
  SUM(o.cm2) AS cm2
FROM first_orders f
JOIN `project.staging.orders` o USING (customer_id)
GROUP BY 1, 2
ORDER BY 1, 2;
```

## 4. Dashboard spec

Build in Looker Studio (free, native Google connectors) or the team's BI tool. For anything beyond small GA4 views, connect to BigQuery marts, not directly to the GA4 connector, because GA4 API quotas and sampling or thresholding make large Looker Studio GA4 reports slow or incomplete [Practitioner consensus].

Page 1, Executive:
- Scorecards: revenue, CM3, MER, aMER, nCAC, new customers (28-day rolling vs previous period and vs target).
- Line: MER and aMER (28-day rolling) with annotations (tracking changes, attribution changes, promotions).
- Bar: spend by channel (stacked) vs new customers.

Page 2, Channels:
- Table: channel, spend, platform conversions, platform CPA or ROAS, incrementality factor, calibrated CPA or ROAS, survey share, target, status.
- Note row: attribution setting per platform.

Page 3, Funnel and site:
- GA4 sessions by channel group (including AI Assistants), conversion rate, landing page table.

Page 4, Data quality:
- Capture rate (GA4 vs backend) by day and region, duplicate rate, Unassigned share, consent granted share, EMQ (manual input or API), upload success and latency, last successful load per source.

Page 5, Leads (lead gen and B2B):
- Leads to qualified to opportunity to closed won by source and campaign, cost per stage, pipeline ROAS, speed to lead.

Design rules: one currency, one timezone, definitions in a footer, every chart titled with the question it answers, platform metrics visually separated from backend metrics, no pie charts for more than 4 categories. Load the `dataviz` guidance if building charts in code.

## 5. Data quality monitoring

### Daily checks (automate at Growth tier and above)

| Check | Rule | Severity |
|-------|------|----------|
| Zero primary conversions | Backend has orders or leads but GA4 or a platform shows zero for the day | Critical |
| Spike | Conversions over 2x the trailing 7-day median with no promotion flagged | High |
| Capture rate drift | GA4 to backend capture rate moves more than 10 points vs 14-day average | High |
| Duplicate transaction IDs | Over 1% of purchase events | High |
| Missing loads | Any source not loaded by 09:00 local | High |
| Upload failures | Offline upload or CAPI error rate over 2% | High |
| Unassigned share | Over 5% of sessions or doubled week over week | Medium |
| Consent granted share | Drops more than 15 points in a region | Medium |
| Revenue mismatch | GA4 revenue per order deviates more than 10% from backend AOV | Medium |
| sGTM health | 5xx rate over 1% or request volume down more than 30% day over day | High |

### Anomaly query (example)

```sql
-- Flag days where GA4 purchases deviate strongly from backend orders
WITH ga AS (
  SELECT PARSE_DATE('%Y%m%d', event_date) AS d, COUNT(DISTINCT ecommerce.transaction_id) AS ga_tx
  FROM `project.analytics_123456.events_*`
  WHERE event_name = 'purchase'
    AND _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 35 DAY))
  GROUP BY 1
),
be AS (
  SELECT DATE(created_at, 'Europe/Istanbul') AS d, COUNT(*) AS orders
  FROM `project.staging.orders`
  WHERE is_test = FALSE AND DATE(created_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 35 DAY)
  GROUP BY 1
),
j AS (
  SELECT be.d, be.orders, IFNULL(ga.ga_tx, 0) AS ga_tx,
         SAFE_DIVIDE(IFNULL(ga.ga_tx, 0), be.orders) AS capture
  FROM be LEFT JOIN ga USING (d)
)
SELECT d, orders, ga_tx, capture,
  AVG(capture) OVER (ORDER BY d ROWS BETWEEN 14 PRECEDING AND 1 PRECEDING) AS capture_14d,
  ABS(capture-AVG(capture) OVER (ORDER BY d ROWS BETWEEN 14 PRECEDING AND 1 PRECEDING)) > 0.10 AS alert
FROM j
ORDER BY d DESC;
```

### Alert routing

- Schedule queries (BigQuery scheduled queries or a cron job) and send results to email, Slack or the project's alert channel.
- Every alert writes a journal entry `YYYY-MM-DD_HHMM_measurement_alert-<topic>.md` with tag alert, the data, and the owner.
- Runbook per alert: first three checks and the rollback path (see [Playbooks](playbooks.md) recovery play).
- GA4 custom insights (anomaly alerts on key metrics) are a free backup at Starter tier.

## 6. Weekly report template

```
# Weekly measurement and performance note: week of YYYY-MM-DD
Data used: backend (Shopify) to YYYY-MM-DD, GA4 export, platform APIs (list), timezone
1. Health: data quality status (green, amber, red) and incidents
2. Blended: revenue, CM3, MER, aMER, nCAC vs target and last 4 weeks
3. Channels: table with platform and calibrated metrics
4. Tests: running, finished (results), next
5. Changes and annotations this week (tracking, attribution, promos)
6. Recommendations and Handoffs requested
```

## 7. Monthly report additions

- Reconciliation table (see [Attribution](attribution.md) section 5).
- Cohort LTV and payback update.
- Survey mix vs platform mix.
- Incrementality evidence table and factors in use.
- MEASUREMENT.md proposed updates.
- Freshness Protocol findings.

## 8. Drift sentinel for ad data

Section 5 catches a break in one metric. The drift sentinel watches the distribution of the inputs that budgets, bids and models rely on, and alerts only when the picture shifts as a whole or one critical input breaks, which keeps alert fatigue down. Pattern proven in production data pipelines, generalized here [Practitioner consensus].

### 8.1 Inputs, windows and tests

| Input | Values compared | Test |
|-------|-----------------|------|
| Spend share by channel | Spend per channel, summed per window | PSI over channels |
| CPC | CPC per campaign and day | KS (PSI on 10 baseline decile bins only with 100 or more rows in the current window) |
| AOV | Order values | KS |
| Conversion rate | Daily value per channel (backend conversions / clicks or sessions) | KS on daily values |
| New customer share | Daily value (new customer orders / orders) | KS on daily values |

Baseline = the 28 days ending 7 days ago (the gap keeps a slow drift out of its own baseline); current = the last 7 days. Days marked in the promo calendar are excluded or compared with the same event last year, and the row's `note` says so.

```
PSI = sum over bins of (cur_i minus base_i) x ln(cur_i / base_i)        (shares per bin, floored at 0.0001)
KS  = max over x of |F_base(x) minus F_cur(x)|                            (two sample)
drifted(input) = PSI over 0.25, or KS with p under 0.01 and statistic over 0.1
```

PSI under 0.1 reads as stable, 0.1 to 0.25 as moderate, over 0.25 as a major shift [Practitioner consensus, credit risk convention]. PSI needs volume: about 10 or more observations per bin in the current window [Practitioner consensus]. On a handful of values (7 daily values, or 21 campaign days on 10 bins) empty bins dominate and a no change simulation flags most weeks. On a binary rate it fails the other way: a CVR drop from 3% to 2% scores about 0.004. Large samples make tiny KS gaps significant, so the rule needs the statistic and the p value.

### 8.2 When to alert

| Rule | Fires when |
|------|-----------|
| `drift_multi` | 3 or more inputs drifted on the same run for the same entity (account, channel or market) |
| `drift_hard_<input>` | One critical input crosses its hard threshold on its own. Defaults [Practitioner consensus], kept in MEASUREMENT.md: conversion rate more than 50% below the baseline median (the ads-review daily rule), one channel's spend share up 20 points or more, AOV moved 30% or more, new customer share down 15 points or more |

Alerts are transitions, not states: one row per rule and entity in `ads-master/logs/alerts.csv` (`rule,entity,alert_from,last_seen,status,ack_by,note`), the queue the `ads-review` daily report reads.

```
for each (rule, entity) evaluated on this run:
  row = the open row for (rule, entity)                       # status is not closed
  condition true,  row exists -> set last_seen = today        # status and ack_by stay as they are
  condition true,  no row     -> append rule, entity, alert_from = today, last_seen = today, status = open
  condition false, row exists -> set status = closed          # a recurrence later opens a new row
```

### 8.3 Sync health check (run first)

Per source, the job counts rows per day at the source (platform report rows, backend orders) and in the warehouse, and reads the latest timestamp on both sides. `sync_rows` fires when any of the last 7 days differs by more than 1% or a day is missing in the warehouse while the source has rows; `sync_stale` fires when the warehouse is more than 26 hours behind the source for a daily load (2x the interval otherwise) [Practitioner consensus]. Both write to the same queue. While a source is unhealthy, the drift rules that read it stay silent and the `note` says why: drift on a half loaded table is noise.

Handoffs: `growth-orchestrator` when `drift_multi` is open (response curves, targets and MMM priors fitted on the baseline may no longer hold, so model driven budget shifts wait for review), the channel agent whose channel drifted, `offer-strategy` for AOV drift tied to promotions, `site-engineer` for a conversion rate drop with healthy sync and a stable traffic mix.
