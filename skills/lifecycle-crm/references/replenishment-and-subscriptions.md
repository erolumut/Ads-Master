# Replenishment and Subscriptions

Consumption timed reminders, subscribe and save economics, subscription lifecycle flows, tools and the legal rules for auto renewal. Consumables (supplements, beauty, pet, coffee, cleaning, contact lenses, baby, food) live or die on the second and third order; this module is the engine for them.

## 1. Consumption based timing

Three ways to set the reminder date, in order of preference:

| Method | When to use | How |
|--------|-------------|-----|
| Empirical reorder interval per SKU | At least about 100 customers who bought the same SKU twice | Median days between consecutive orders of the SKU (query below), optionally by pack size |
| Days of supply | New SKU or thin data | Days of supply per unit x units bought (for example 60 capsules at 2 per day = 30 days; 2 bottles = 60 days) |
| Category default | No product data at all | Start at the category's typical interval from the brand team, then replace with data within 90 days |

Send rules [Practitioner consensus]:
- Reminder 1 at about 80% to 90% of the expected depletion date (before they run out).
- Reminder 2 at about 100% to 110% (if no order).
- Reminder 3 at about 130% with an alternative (subscription offer, bundle, larger pack).
- Adjust for shipping time: subtract typical delivery days from the reminder date.
- Recompute per customer: if a customer reorders consistently early or late, use their personal interval after 2 or more reorders.

### 1.1 SQL: median reorder interval by SKU

Assumes an `order_lines` table (customer_id, order_id, order_date, sku, quantity) and excludes cancelled and fully refunded orders upstream. BigQuery syntax; adapt for Postgres (use `percentile_cont(0.5) within group (order by gap_days)`).

```sql
WITH sku_orders AS (
  SELECT customer_id, sku, DATE(order_date) AS d, SUM(quantity) AS qty
  FROM order_lines
  WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 24 MONTH)
  GROUP BY 1, 2, 3
),
gaps AS (
  SELECT
    sku,
    customer_id,
    qty AS prev_qty,
    DATE_DIFF(LEAD(d) OVER (PARTITION BY customer_id, sku ORDER BY d), d, DAY) AS gap_days
  FROM sku_orders
)
SELECT
  sku,
  COUNT(*) AS reorder_pairs,
  APPROX_QUANTILES(gap_days, 100)[OFFSET(50)] AS median_gap_days,
  APPROX_QUANTILES(gap_days, 100)[OFFSET(25)] AS p25_gap_days,
  APPROX_QUANTILES(gap_days, 100)[OFFSET(75)] AS p75_gap_days,
  APPROX_QUANTILES(SAFE_DIVIDE(gap_days, prev_qty), 100)[OFFSET(50)] AS median_days_per_unit
FROM gaps
WHERE gap_days IS NOT NULL AND gap_days BETWEEN 3 AND 365
GROUP BY sku
HAVING reorder_pairs >= 50
ORDER BY reorder_pairs DESC;
```

Use `median_days_per_unit x quantity bought` for the reminder when customers buy multiples.

### 1.2 Implementing in the ESP

| ESP | Pattern |
|-----|---------|
| Klaviyo | Flow triggered by Placed Order (or Ordered Product per line item) with a trigger split per SKU or category; time delay set per branch; or write an "expected_next_order_date" profile property from the warehouse and trigger a date based flow. Klaviyo predictive analytics also exposes an expected date of next order when its data thresholds are met [Official, Klaviyo help] |
| Braze, Iterable, Customer.io | Event triggered journey with per product delay attributes from the catalog, or a computed attribute synced from the warehouse (reverse ETL) |
| Omnisend, Mailchimp | Product based automation with fixed delay per product group |
| Shopify Flow plus ESP | Tag orders by SKU group and pass the tag as a property |

### 1.3 Replenishment flow spec

| Step | Timing | Channel | Content | Offer |
|------|--------|---------|---------|-------|
| R1 | 85% of expected depletion minus delivery days | Email | "Running low?" with exact product, size, one click reorder link (cart permalink) | None |
| R2 | 105% | SMS (if consented) or email | Short reminder with reorder link | None |
| R3 | 130% | Email | Subscribe and save offer or bundle; alternatives if they switched | Subscription discount (offer-strategy sets the level) |
| Exit | Any Placed Order containing the SKU or its substitutes; active subscription to the SKU | | | |

Measure: reorder rate of the SKU within 1.5x interval, holdout vs treatment.

## 2. Subscribe and save economics

```
One time buyer 12 month contribution  = orders_12m x AOV x contribution margin
Subscriber 12 month contribution      = sum over months of (survival_m x price x (1 - sub discount) x contribution margin)
Simple steady state subscriber LTV    = monthly contribution per active subscriber / monthly churn
Break even subscription discount: the discount d where subscriber contribution with d equals one time contribution
```

Worked example (illustrative): product 30 EUR, contribution margin 55%, one time buyers average 2.1 orders per 12 months (contribution 34.65 EUR). Subscription at 15% off: monthly contribution 30 x 0.85 x 0.55 = 14.03 EUR. With monthly churn 12%, survival over 12 months sums to about 7.4 shipments, contribution about 103.8 EUR. Even at 20% monthly churn (about 4.7 shipments, 66 EUR) the subscription wins. The decision depends on churn, which you measure; involuntary churn (failed payments) is often a large share and is fixable.

Rules:
- Offer subscription after the first order experience is proven (post delivery), not only on the PDP.
- Prefer flexible subscriptions (skip, swap, delay, change frequency) to reduce cancellations; flexibility is a retention feature.
- Track discount cost as part of acquisition investment when the subscription discount is the first order offer (METRICS.md).
- offer-strategy owns the discount level; you own timing and messaging.

## 3. Subscription KPIs

| KPI | Definition | Watch |
|-----|-----------|-------|
| Active subscribers | Subscriptions with a future charge scheduled | Net change monthly |
| Monthly churn | Cancelled in month / active at start | Split voluntary vs involuntary |
| Involuntary churn | Cancelled or expired due to payment failure | Dunning recovery rate |
| Dunning recovery rate | Recovered failed charges / failed charges | Card updater, retries, SMS reminders |
| Save rate | Cancellation attempts that ended in skip, swap, pause or offer accepted / attempts | Must still allow cancellation (law) |
| Average subscription age | Months since start among active | Cohort curves |
| Shipments per subscriber (12 month) | | LTV driver |
| Subscription share of revenue | | Concentration risk |

## 4. Tools (October 2026)

| Tool | Position | 2025 to 2026 notes |
|------|----------|-------------------|
| Recharge | Largest Shopify subscription platform; self-reports handling 71% of subscriptions sold on Shopify stores | Acquired Skio on 2026-04-30 for a reported $105 million; both products operate separately with a combined roadmap promised over about 12 months [Official, Recharge and Skio blogs, 2026-04; price per press reports] |
| Skio | Shopify subscriptions with passwordless login and SMS based management | Now part of Recharge; confirm roadmap and migration terms before signing multi year contracts [Unverified long term plans] |
| Loop Subscriptions | Independent Shopify subscription app | Claims of brand counts conflict (2,400+ vs 6,000+) [Unverified]; marketed on lower fees |
| Stay AI | Independent, retention and AI features | Positioned as independent alternative after the Recharge and Skio deal [Practitioner commentary, 2026] |
| Appstle, Seal, Bold and others | Lower cost Shopify options | Check checkout extensibility compatibility |
| Shopify Subscriptions (native app) | Basic subscriptions | Limited flexibility; fine for Starter tier |
| Chargebee, Recurly, Stripe Billing | SaaS and non Shopify recurring billing | Dunning and revenue recovery built in |

Integration checklist with the ESP: subscription created, charge upcoming, charge succeeded, charge failed, subscription skipped, swapped, paused, cancelled (with reason), reactivated. Verify these events reach the ESP before building flows.

## 5. Subscription lifecycle flows

| Flow | Trigger | Timing | Content | Notes |
|------|---------|--------|---------|------|
| Subscription welcome | Subscription created | Immediately, then at first delivery | How to manage (skip, swap, change date), what to expect, support | Reduces early cancellations |
| Upcoming charge reminder | Charge upcoming | 3 to 7 days before charge | Date, amount, items, one tap skip, swap or add on | Required by some laws for certain renewals (section 6); also reduces chargebacks |
| Add on and cross sell | Charge upcoming | With reminder | One relevant add on | Measure attach rate |
| Dunning | Charge failed | Immediately, +2, +5, +8 days (align with retry schedule) | Update payment link; SMS if consented | Biggest quick win in many programs |
| Cancellation flow (in portal) | Cancel clicked | In session | Reason survey, then a relevant alternative (skip, frequency change, swap, pause, discount) AND a clear cancel button | The save offer can never be the only exit (California ARL) |
| Cancelled winback | Subscription cancelled | +30, +60, +90 days, by reason | Address reason (new flavor, frequency, price) | Exclude cancellations for fraud or chargeback |
| Paused reminder | Pause ending | 7 days before resume | Confirm or adjust | |
| Anniversary | Subscription age milestone | At 6 and 12 months | Recognition, loyalty perk | |

## 6. Auto renewal and subscription law (summary; full detail in [Consent and law](consent-and-law.md))

| Jurisdiction | Rule (October 2026) | Implication |
|--------------|---------------------|-------------|
| US federal | FTC "click to cancel" amendments to the Negative Option Rule were vacated by the Eighth Circuit on 2025-07-08 before taking effect; the FTC published an ANPRM to restart rulemaking on 2026-03-13 (comments closed 2026-04-13) [Official, FTC 2026-03; court ruling 2025-07] | No new federal rule yet; ROSCA and Section 5 enforcement continue (clear disclosure, express informed consent, simple cancellation) |
| California | Amended Automatic Renewal Law (AB 2863) applies to contracts entered, amended or extended on or after 2025-07-01: express affirmative consent with records kept 3 years or 1 year after termination (whichever is longer), cancellation as easy as sign up without forced live contact, save offers allowed only if cancel remains available, annual reminders, price change notice 7 to 30 days before, renewal notice 15 to 45 days before for terms of 1 year or more [Official summaries, law firm alerts 2025-06] | Build to California standard for all US customers unless counsel says otherwise |
| Other US states | About 25 states have auto renewal laws with varying notice rules [Unverified count, 2026 guide] | compliance agent maps per state |
| EU | Consumer Rights Directive withdrawal rules; several member states require easy online termination (for example Germany's termination button for online contracts since 2022) [Official, national law] | Cancel path online, confirmation on durable medium |
| UK | DMCC Act subscription contract rules are due to commence later than the April 2025 consumer enforcement start [Unverified commencement date] | Check before building UK renewal reminders |

Never draft a cancellation flow that hides the cancel option, requires a phone call, or loops the user through offers. Send every subscription flow spec to `compliance`.

## 7. Replenishment and subscription audit questions

- Is the reminder date derived from data per SKU, and does it account for quantity and delivery time?
- Do reminders exit when the customer reorders through any channel (including marketplaces if data is available)?
- Are subscription events in the ESP and are flows live for upcoming charge, dunning and cancellation?
- Is involuntary churn measured separately and is dunning recovering at least a meaningful share of failures?
- Can a customer cancel online in the same number of steps as sign up?
- Are subscription discounts and first order offers counted in acquisition investment?
