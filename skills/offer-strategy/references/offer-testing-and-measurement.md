# Offer Testing and Measurement

> An offer test answers one question: did this offer create more contribution than it cost, and did it attract customers worth having? Conversion rate alone answers neither. Statistics depth for page tests lives in the `cro` skill; this module covers what is specific to offers.

## 1. Metrics

Primary (pick one per test):

| Metric | Formula | Use for |
|--------|---------|---------|
| Contribution per visitor (CM2 per session) | Sum of CM2 of orders / sessions in the arm | Most ecommerce offer tests |
| Contribution after acquisition per new customer | (CM2 of first orders minus acquisition investment) / new customers | First order offers with paid traffic |
| 90 day contribution per new customer | First order plus repeat CM2 within 90 days, minus offer costs | Acquisition offers where repeat matters |
| Qualified pipeline per visitor or per euro | Qualified leads or pipeline value / sessions or spend | Lead gen offers |
| Year 1 revenue or contribution per signup | Expected from trial to paid, plan mix and churn | SaaS entry offers and annual discounts |

Guardrails (always report):

| Guardrail | Why |
|-----------|-----|
| Refund and return rate by arm | Free shipping and deep discounts raise returns (Shehu et al. 2020) |
| New customer share | Offer may only subsidize existing customers |
| Discount rate | Discounts / gross sales at list |
| 30, 60, 90 day repeat rate by acquisition offer | Deep acquisition discounts can attract lower value customers (Lewis 2006) |
| Full price share of revenue | Promo dependency |
| Support contacts and complaints about price | Trust damage, price test exposure |
| Chargebacks and fraud | Code abuse, BNPL disputes |
| Stock cover of promoted SKUs | Stockouts end tests early and waste spend |
| Contribution after marketing (CM3), whole business | The scoreboard |

## 2. Designs

| Design | When | How | Main threats |
|--------|------|-----|--------------|
| Visitor level A/B (app or flag) | Enough traffic, offer shown on site | Random split by visitor; arms differ only by offer | Cross-device contamination, code leakage, legal limits on list price tests ([Pricing research](pricing-research-and-tests.md) section 7) |
| Audience holdout (email, SMS, push) | Promos sent to a list | Randomly hold out 10% to 20% of the audience; they get no promo message | Holdout too small; holdout sees the promo elsewhere (site banner) |
| Code split | Partner, influencer or paid traffic | Different codes per arm with random assignment of audiences or ad sets | Codes leak to coupon sites |
| Geo split (matched markets) | Offers that cannot be randomized by visitor (shipping thresholds, sitewide promos), or channel level offers | Match regions on pre-period sales; treat half; compare with synthetic control or difference in differences | Few units, spillover, regional events; requires `measurement` support |
| Switchback (time split) | Low traffic, site wide offers | Alternate control and offer by week (or by day for high traffic), randomize order, at least 4 cycles each | Seasonality, carryover, returning customers seeing both |
| Pre and post with forecast baseline | Last resort, or when the change must ship for all | Forecast from at least 8 weeks of history and same period last year; compare actual vs forecast with an interval | Everything else that changed |
| Staggered rollout by market | Multi market brands | Launch in one market, use others as control, then roll | Market differences |

Rule of thumb for which design: randomize by visitor if you can and the law allows; otherwise geo; otherwise switchback; pre and post only for low risk changes, labeled as weak evidence.

## 3. Sample size for contribution per visitor

Contribution per visitor has a high variance (most visitors buy nothing), so offer tests need more traffic than conversion rate tests on the same lift.

```
n per arm = 2 x (z_alpha/2 + z_beta)^2 x variance / delta^2
variance per visitor = p x (sd_order^2 + mean_order^2) - (p x mean_order)^2
p = conversion rate, mean_order and sd_order = CM2 per order mean and standard deviation
```

Worked example: conversion 2.5%, CM2 per order mean EUR 30, sd EUR 20, so contribution per visitor EUR 0.75 with sd EUR 5.65. At 95% confidence and 80% power:

| Relative lift to detect | Visitors per arm |
|-------------------------|------------------|
| 5% | about 356,500 |
| 10% | about 89,100 |
| 15% | about 39,600 |
| 20% | about 22,300 |

For comparison, detecting a 10% conversion rate lift at 2.5% baseline needs about 64,200 visitors per arm. If traffic cannot reach the sample in about 6 weeks: test bolder offers (bigger expected effect), use switchbacks with many cycles, use CUPED with pre-period spend per customer for known customers (see the `cro` experimentation module), or accept a decision rule based on a Bayesian probability of beating control with a pre-agreed loss threshold.

```python
import math
def n_per_arm(p, mean_order, sd_order, rel_lift, z_a=1.959964, z_b=0.841621):
    mean = p * mean_order
    var = p * (sd_order**2 + mean_order**2) - mean**2
    return math.ceil(2 * (z_a + z_b)**2 * var / (mean * rel_lift)**2)
print(n_per_arm(0.025, 30, 20, 0.10))   # about 89,128
```

## 4. Incrementality of a promotion (no randomized control available)

```
Baseline = forecast of sales without the promo (same weeks last year adjusted for trend, or 8 week run rate adjusted for season)
Promo lift = actual during promo minus baseline during promo
Pull-forward = actual minus baseline in the 2 to 4 weeks after (usually negative)
Incremental units = promo lift + pull-forward (+ pre-promo dip if customers waited, usually negative)
Incremental contribution = incremental units x CM2 per unit at promo price
                         minus discount given to baseline buyers (baseline units x discount per unit)
                         minus fixed promo costs (creative, fees, extra media)
```

Worked example (illustrative): baseline 1,000 units per week, CM2 per unit at full price EUR 13; a one-week 20% off promo sells 1,800 units at CM2 EUR 7 per unit (after the EUR 6 discount); the following two weeks sell 850 units per week (pull-forward of 300 units).
- Incremental units = 800 minus 300 = 500.
- Contribution with promo over 3 weeks = 1,800 x 7 + 1,700 x 13 = 12,600 + 22,100 = EUR 34,700.
- Contribution without promo = 3,000 x 13 = EUR 39,000.
- Result: the promo lost EUR 4,300 of contribution despite 80% more units in promo week. Report it that way.

## 5. Cohort quality by acquisition offer

Tag every first order with the offer that acquired it (discount code, automatic discount ID, gift SKU, landing page offer parameter). `measurement` makes sure the tag reaches the warehouse or export.

Example SQL (BigQuery style; adapt table names to the project's export, aggregated output only):

```sql
WITH first_orders AS (
  SELECT customer_id,
         MIN(created_at) AS first_at,
         ARRAY_AGG(offer_id ORDER BY created_at LIMIT 1)[OFFSET(0)] AS acq_offer
  FROM orders
  WHERE financial_status IN ('paid', 'partially_refunded')
  GROUP BY customer_id
),
cohort AS (
  SELECT f.acq_offer,
         f.customer_id,
         SUM(IF(o.created_at <= TIMESTAMP_ADD(f.first_at, INTERVAL 90 DAY), o.cm2, 0)) AS cm2_90d,
         COUNTIF(o.created_at > f.first_at
                 AND o.created_at <= TIMESTAMP_ADD(f.first_at, INTERVAL 90 DAY)) AS repeat_orders_90d
  FROM first_orders f
  JOIN orders o USING (customer_id)
  WHERE f.first_at < TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 90 DAY)
  GROUP BY f.acq_offer, f.customer_id
)
SELECT acq_offer,
       COUNT(*) AS customers,
       ROUND(AVG(cm2_90d), 2) AS avg_cm2_90d,
       ROUND(COUNTIF(repeat_orders_90d > 0) / COUNT(*), 3) AS repeat_rate_90d
FROM cohort
GROUP BY acq_offer
HAVING customers >= 100
ORDER BY avg_cm2_90d DESC;
```

Read it with the acquisition investment per offer: the best offer maximizes `avg_cm2_90d minus acquisition investment per customer`, not first order conversion.

## 6. Promo post-mortem template

```
# Promo post-mortem: <event> | <dates> | Data sources and date ranges
## Summary (3 to 5 bullets: incremental contribution, new customers, verdict)
## Offer as run (mechanics, depth, channels, SKUs, codes)
## Results vs baseline
| Metric | Baseline | Actual | Delta | Source |
| Units, orders, revenue, CM2, CM3 (whole business) |
| New customers, new customer share |
| Discount rate, full price share |
| Return and refund rate |
## Pull-forward and post-promo dip (2 to 4 weeks after)
## Channel effects (marketplace featured offer, retail partner reactions)
## Cohort quality (first 30 days now, update at 90 days)
## Incidents (stockouts, stacking errors, wrong prices, site issues)
## Learnings (confirmed vs hypotheses) and next time
## Memory candidates (only if confirmed by data)
```

## 7. Stop rules for live offers
- Stop and alert immediately: wrong price or discount live, unintended stacking, offer applied to excluded SKUs, promoted item sold out, legal complaint (this is an `ads-master/INCIDENTS.md` stop condition).
- Stop the test arm: guardrail harm beyond the pre-agreed threshold (for example return rate up 3 points, support contacts doubled), sample ratio mismatch, code leakage contaminating control.
- Do not stop early for a good-looking primary metric on a fixed horizon test.

## 8. EXPERIMENTS.md row format

```
| E### | YYYY-MM-DD | offer-strategy | If we offer <X> to <segment> instead of <control>, then <primary metric> rises by <n>%, because <evidence> | Contribution per visitor | I/C/E | A/B or geo or switchback or holdout | Stop rule | backlog | | |
```

## 9. Common measurement mistakes
- Judging an offer on conversion rate or platform ROAS when the discount itself lowered contribution.
- Counting all orders that used a code as incremental (most code use on sitewide promos is subsidy).
- Ignoring the 2 to 4 weeks after a promo.
- Comparing acquisition offers on first order only, when the cohort's repeat behavior differs.
- Running an offer test where the control also sees the offer (site banner, email, influencer code).
- Letting the ad platform optimize toward the arm with more conversions: hold budgets fixed by arm or use separate campaigns with equal budgets.
