# Cohort and LTV Analysis

Definitions, queries and a script for repeat rate at 30, 45, 60 and 90 days, time to second order, LTV curves, LTV by acquisition source and first product, predicted LTV and the reporting format. Backend orders are the source of truth (`MEASUREMENT.md`); ESP revenue is not.

## 1. Data requirements

| Field | Notes |
|-------|------|
| customer_id | Stable ID; merge guest checkouts by normalized email or phone (hash in analysis tables) |
| order_id, order_date (store time zone) | |
| net_revenue | After discounts and refunds, excluding tax and shipping charged (decide and record in METRICS.md) |
| contribution | Net revenue minus COGS, fulfillment, payment fees, shipping subsidy, returns cost; if unavailable use a margin % from PROJECT_BRIEF.md and label it |
| discount_code, discount_amount | For discount dependency cuts |
| first_product or first category | From order lines of the first order |
| acquisition source | First touch or platform attribution plus post purchase survey (from measurement) |
| channel of order | Site, marketplace, retail (exclude or separate) |
| is_subscription_order | |

Exclude test orders, fully refunded orders, B2B wholesale (unless analyzing it), employee orders. Use only aggregated outputs in deliverables; never write customer level rows with identifiers into `ads-master/`.

## 2. Repeat rate by cohort (30, 45, 60, 90 days)

```sql
-- BigQuery. orders: customer_id, order_id, order_date, net_revenue (clean, see section 1)
WITH firsts AS (
  SELECT customer_id, MIN(DATE(order_date)) AS first_date
  FROM orders GROUP BY customer_id
),
seconds AS (
  SELECT o.customer_id, MIN(DATE(o.order_date)) AS second_date
  FROM orders o JOIN firsts f USING (customer_id)
  WHERE DATE(o.order_date) > f.first_date
  GROUP BY o.customer_id
)
SELECT
  DATE_TRUNC(f.first_date, MONTH) AS cohort_month,
  COUNT(*) AS new_customers,
  -- only count a window when the whole cohort is mature for it
  IF(DATE_ADD(LAST_DAY(f.first_date), INTERVAL 30 DAY) <= CURRENT_DATE(),
     COUNTIF(DATE_DIFF(s.second_date, f.first_date, DAY) <= 30) / COUNT(*), NULL) AS repeat_30,
  IF(DATE_ADD(LAST_DAY(f.first_date), INTERVAL 45 DAY) <= CURRENT_DATE(),
     COUNTIF(DATE_DIFF(s.second_date, f.first_date, DAY) <= 45) / COUNT(*), NULL) AS repeat_45,
  IF(DATE_ADD(LAST_DAY(f.first_date), INTERVAL 60 DAY) <= CURRENT_DATE(),
     COUNTIF(DATE_DIFF(s.second_date, f.first_date, DAY) <= 60) / COUNT(*), NULL) AS repeat_60,
  IF(DATE_ADD(LAST_DAY(f.first_date), INTERVAL 90 DAY) <= CURRENT_DATE(),
     COUNTIF(DATE_DIFF(s.second_date, f.first_date, DAY) <= 90) / COUNT(*), NULL) AS repeat_90
FROM firsts f LEFT JOIN seconds s USING (customer_id)
WHERE f.first_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 24 MONTH)
GROUP BY cohort_month
ORDER BY cohort_month;
```

Note: the second order must fall on a later date than the first, so same day reorders (often split shipments or a forgotten item) are ignored. If the business has many legitimate same day repeat orders, change `>` to `>=` and deduplicate by order_id.

## 3. Python script (orders CSV to cohort table)

Run locally on an export in `ads-master/data/imports/` (for example `2026-10-01_shopify_orders.csv` with columns customer_id, order_id, order_date, net_revenue). Writes only aggregates.

```python
#!/usr/bin/env python3
"""cohort_repeat.py: repeat rate at 30/45/60/90 days and 12 month revenue per customer by first order month."""
import csv, sys, statistics
from collections import defaultdict
from datetime import date, datetime, timedelta

path = sys.argv[1]
today = date.fromisoformat(sys.argv[2]) if len(sys.argv) > 2 else date.today()
orders = defaultdict(list)
with open(path, newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        d = datetime.fromisoformat(row["order_date"][:10]).date()
        orders[row["customer_id"]].append((d, float(row["net_revenue"] or 0)))

windows = [30, 45, 60, 90]
cohorts = defaultdict(lambda: {"n": 0, "rep": defaultdict(int), "rev365": 0.0, "gaps": []})
for cid, rows in orders.items():
    rows.sort()
    first = rows[0][0]
    later = [r for r in rows[1:] if (r[0] - first).days >= 1]   # ignore same day split orders
    c = cohorts[first.strftime("%Y-%m")]
    c["n"] += 1
    if later:
        gap = (later[0][0] - first).days
        c["gaps"].append(gap)
        for w in windows:
            if gap <= w:
                c["rep"][w] += 1
    c["rev365"] += sum(v for d, v in rows if (d - first).days < 365)

print("cohort,new_customers," + ",".join(f"repeat_{w}" for w in windows) + ",median_days_to_2nd,rev_365_per_customer")
for key in sorted(cohorts):
    c = cohorts[key]
    y, m = map(int, key.split("-"))
    cohort_end = (date(y + (m == 12), m % 12 + 1, 1) - timedelta(days=1))
    cells = []
    for w in windows:
        cells.append(f"{c['rep'][w] / c['n']:.3f}" if cohort_end + timedelta(days=w) <= today else "")
    med = statistics.median(c["gaps"]) if c["gaps"] else ""
    rev = f"{c['rev365'] / c['n']:.2f}" if cohort_end + timedelta(days=365) <= today else ""
    print(f"{key},{c['n']}," + ",".join(cells) + f",{med},{rev}")
```

Usage: `python3 cohort_repeat.py ads-master/data/imports/2026-10-01_shopify_orders.csv 2026-10-08 > cohort.csv`. Blank cells mean the cohort is not mature for that window.

## 4. Median days to second order and the reorder interval

- Compute the median (not mean) days from first to second order among repeaters, overall and by first product category.
- Distribution matters: in one vendor analysis of 156K DTC customers, 50.3% of second orders came within 30 days and 76.4% within 90 days of the first, and only 3.7% after a year [Unverified, vendor dataset 2026]. Vendor ranges for median time to second purchase: apparel 15 to 27 days, supplements 27 to 68 days, durables 30+ days [Unverified, vendor 2026]. Your data decides.
- Use the median days to second order to time post purchase cross sell (50% to 70% of it) and to define At risk (1.5x) and Lapsed (3x) stages.

## 5. LTV curves

```sql
-- Cumulative net revenue (or contribution) per customer by months since first order
WITH firsts AS (
  SELECT customer_id, MIN(DATE(order_date)) AS first_date FROM orders GROUP BY customer_id
)
SELECT
  DATE_TRUNC(f.first_date, QUARTER) AS cohort_q,
  DATE_DIFF(DATE(o.order_date), f.first_date, MONTH) AS month_n,
  SUM(o.net_revenue) / COUNT(DISTINCT f.customer_id) AS revenue_per_customer_in_month
FROM orders o JOIN firsts f USING (customer_id)
WHERE f.first_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 MONTH)
GROUP BY 1, 2
ORDER BY 1, 2;
```

Note: the denominator above counts only customers with an order in that month; for a correct per cohort average, divide by the cohort size from `firsts` (join a cohort size table). Plot cumulative values per cohort; compare curve shape after program changes.

Definitions:
```
12 month contribution LTV = cumulative contribution per customer at month 12 (mature cohorts only)
LTV to CAC = 12 month contribution LTV / acquisition investment per new customer (METRICS.md)
Payback month = first month where cumulative contribution per customer >= acquisition investment per new customer
```

## 6. Cuts that drive decisions

| Cut | Decision it informs |
|-----|---------------------|
| By acquisition source | Budget allocation (growth-orchestrator), value based bidding (measurement) |
| By first product or category | Hero products for acquisition (products that create repeaters), cross sell table |
| By first order discount (none, small, deep) | Offer strategy (offer-strategy), welcome incentive |
| By subscription vs one time | Subscription offer strategy |
| By market or country | Market expansion |
| By month of acquisition (peak vs non peak) | Peak cohort expectations |
| By capture source (pop up offer, quiz, checkout) | List growth strategy |

Next product affinity (for cross sell):
```sql
WITH firsts AS (
  SELECT customer_id, MIN(DATE(order_date)) AS first_date FROM order_lines GROUP BY customer_id
),
first_items AS (
  SELECT DISTINCT l.customer_id, l.category AS first_cat
  FROM order_lines l JOIN firsts f ON l.customer_id = f.customer_id AND DATE(l.order_date) = f.first_date
),
next_items AS (
  SELECT DISTINCT l.customer_id, l.category AS next_cat
  FROM order_lines l JOIN firsts f USING (customer_id)
  WHERE DATE(l.order_date) > f.first_date AND DATE(l.order_date) <= DATE_ADD(f.first_date, INTERVAL 120 DAY)
)
SELECT first_cat, next_cat, COUNT(*) AS customers
FROM first_items JOIN next_items USING (customer_id)
GROUP BY 1, 2
ORDER BY first_cat, customers DESC;
```

## 7. Predicted LTV

| Method | Pros | Cons |
|--------|------|------|
| ESP built in (Klaviyo predicted CLV; thresholds in [Segmentation](segmentation-and-personalization.md) section 3) | No build | Black box; revenue based, not contribution |
| BG/NBD plus Gamma-Gamma (PyMC-Marketing CLV module; the older `lifetimes` package is no longer maintained) | Interpretable, works on transaction history only | Assumes non contractual purchasing; weak for very new customers |
| Supervised model on first order features (product, AOV, discount, source, device, region, time to first order) predicting 12 month value | Works at first purchase (good for bidding) | Needs 12+ months of labeled cohorts and validation |
| Survival or churn models for subscriptions | Fits contractual businesses | Needs subscription event history |

Validation table (required before use): for a past cohort, group customers into deciles of predicted value and compare mean predicted vs realized 12 month value; report rank correlation and calibration error.

## 8. Benchmarks (compare to own history first)

| Metric | Value | Source, date | Caveat |
|--------|-------|--------------|--------|
| 12 month repeat purchase rate, DTC | 18.8% across 156K customers | Vendor dataset (bsandco) [Unverified, 2026] | Same dataset reused by several vendors |
| 12 month repeat rate by vertical (vendor ranges) | Consumables 30% to 45%, beauty 25% to 40%, apparel about 20% to 32%, home 18% to 25%, electronics 12% to 18% | Vendor blogs [Unverified, 2025 to 2026] | Definitions differ (2+ orders vs repeat order share) |
| Median repeat rate (benchmark site) | 24% median, 38% top quartile | Benchmark aggregator [Unverified, 2026] | Method unknown |

These are weak benchmarks. Weight the project's own cohort trend far above any of them.

## 9. Cohort report template

```
# Cohort report: <brand> <YYYY-MM>
Data: <orders source>, first orders <range>, as of <date>; exclusions <list>; revenue definition <METRICS.md>
FACTS
- Repeat rate at 30/45/60/90 days, last 6 mature cohorts vs prior 6 and same months LY
- Median days to second order (overall and by top 5 first categories)
- 12 month contribution LTV by acquisition source (mature cohorts); payback months
- Discount cut: repeat and LTV by first order discount band
INTERPRETATION
RECOMMENDATION (lifecycle actions, offer changes via offer-strategy, budget implications via growth-orchestrator, value signals via measurement)
Handoffs requested
```
