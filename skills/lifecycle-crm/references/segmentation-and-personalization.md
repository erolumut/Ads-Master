# Segmentation and Personalization

Engagement tiers that survive Apple Mail Privacy Protection, RFM, predicted LTV, consumption based and affinity segments, zero party data, the personalization ladder and the AI decisioning tools of 2026. Every segment definition here is a starting point; validate with the project's own data.

## 1. Engagement tiers (email)

Opens are unreliable: Apple Mail (including MPP prefetch) accounted for roughly 62% of tracked opens in Litmus's July 2026 sample [Study, Litmus via secondary, 2026-07], AI assistants and security scanners also trigger opens, and France's CNIL requires consent for individual open tracking used for campaign optimization (since 2026-07-14 for existing contacts) [Official, CNIL 2026-04]. Build tiers on clicks, orders and site activity; use opens only with Apple Privacy opens excluded and never for French recipients without consent.

| Tier | Definition (default) | Campaign frequency (default) |
|------|---------------------|-----------------------------|
| E0 New | Subscribed in last 30 days | Welcome series plus 1 to 2 campaigns per week |
| E1 Hot | Clicked email OR ordered OR Active on Site in last 30 days | 2 to 5 per week |
| E2 Warm | Same signals in 31 to 90 days | 1 to 2 per week |
| E3 Cool | Same signals in 91 to 180 days | 2 to 4 per month, best content only |
| E4 Cold | No signal in 180+ days, subscribed 60+ days | Sunset flow only, then suppress |

Klaviyo segment example (E1 Hot):
```
Can receive email marketing
AND (Clicked Email at least once in the last 30 days
     OR Placed Order at least once in the last 30 days
     OR Active on Site at least once in the last 30 days)
AND NOT in segment "Global control group"
```
Klaviyo exposes an Apple Privacy open flag on Opened Email events that can be filtered in segments [Official, Klaviyo; verify the exact property name in the account]. Equivalents: Braze (engagement filters, "Last engaged with message"), Iterable (user criteria on email click events), Customer.io (segment on email clicked events).

Frequency rule: raise frequency only where incremental revenue per send stays positive and unsubscribe plus spam rates stay within limits. Gmail's Manage subscriptions view (July 2025) lists senders by volume, so high frequency senders are the most exposed to one tap unsubscribes [Official, Google 2025-07].

## 2. RFM

Recency (days since last order), Frequency (orders in window), Monetary (net revenue or, better, contribution in window). Score 1 to 5 per dimension with quintiles.

```sql
-- BigQuery; orders table: customer_id, order_id, order_date, net_revenue (refunds removed)
WITH base AS (
  SELECT customer_id,
         DATE_DIFF(CURRENT_DATE(), MAX(DATE(order_date)), DAY) AS recency_days,
         COUNT(DISTINCT order_id) AS frequency,
         SUM(net_revenue) AS monetary
  FROM orders
  WHERE order_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 24 MONTH)
  GROUP BY customer_id
)
SELECT customer_id, recency_days, frequency, monetary,
       6 - NTILE(5) OVER (ORDER BY recency_days) AS r,
       NTILE(5) OVER (ORDER BY frequency) AS f,
       NTILE(5) OVER (ORDER BY monetary) AS m
FROM base;
```

Frequency is lumpy (most customers have 1 order), so quintiles on frequency collapse; use fixed bands instead (1, 2, 3, 4 to 5, 6+).

| RFM group | Rule (example) | Treatment |
|-----------|---------------|-----------|
| Champions | R 5, F 4 to 5 | Early access, referral ask, loyalty perks, no discounts |
| Loyal | R 3 to 5, F 3 to 5 | Cross sell, VIP, reviews and UGC |
| Promising new | R 5, F 1 | Second order engine (post purchase) |
| Need attention | R 3, F 2 to 3 | Personalized picks, replenishment |
| At risk high value | R 1 to 2, M 4 to 5 | Personal winback, service outreach, best offer tested |
| Hibernating | R 1 to 2, F 1 to 2, M 1 to 2 | Low cost winback then sunset |

Sync RFM scores to the ESP as profile properties (reverse ETL, ESP API, or CSV import approved as G3 when it changes consent or list membership; property only updates are G2).

## 3. Predicted LTV and churn risk

| Source | What it gives | Requirements and caveats |
|--------|---------------|-------------------------|
| Klaviyo predictive analytics | Predicted CLV (next 12 months), historic CLV, total CLV, churn risk, expected date of next order, predicted gender | At least 500 customers who placed orders, an ecommerce integration or API order feed, at least 180 days of order history with orders in the last 30 days, some customers with 3 or more orders [Official, Klaviyo help center; English page confirms 500, other locale pages list the rest] |
| Braze | Predictive Churn, Predictive Purchases (likelihood scores); Decisioning Studio for next best action | Plan dependent; Decisioning Studio Go GA scheduled 2026-10-14 [Official, Braze 2026-09] |
| Iterable | Predictive goals, Nova agents | Plan dependent [Official, 2026] |
| Warehouse model | BG/NBD plus Gamma-Gamma (PyMC-Marketing CLV module), or gradient boosted model on features | Needs analyst; best for paid media value signals ([Cohort and LTV analysis](cohort-and-ltv-analysis.md) section 7) |

Uses: VIP early identification (top predicted CLV decile of first time buyers), churn risk winback timing, value based audiences for paid media, suppression of low value discount seekers from deep offers. Always validate predictions against realized outcomes for a past cohort before acting on them.

## 4. Consumption and lifecycle segments

- Due for replenishment: expected depletion date within next 7 days ([Replenishment](replenishment-and-subscriptions.md)).
- Overdue: past 1.3x expected depletion with no order.
- First time buyers by first product (the first product predicts the second; cross sell table).
- Subscribers vs non subscribers (never send subscribe and save offers to active subscribers of the same SKU).
- Discount dependency: share of orders with a code; customers with 100% discounted orders get value messaging and fewer codes.
- Return heavy customers: high return rate excluded from aggressive campaigns (offer-strategy and finance view).
- Channel preference: SMS clickers vs email clickers.

## 5. Product and category affinity

- Category browse and purchase counts as profile properties (last 90 days).
- Price band affinity (median item price bought).
- Size, color, skin type, pet type and other attributes via zero party data and order lines.
- Use affinity for campaign versions (3 to 5 versions per send by top categories) rather than one generic blast.

## 6. Zero party data

Data a customer intentionally shares: preferences, goals, sizes, routines, birthdays, intent timing.

| Collection point | Question examples | Storage |
|------------------|------------------|---------|
| Signup form step 2 | "What are you shopping for?", "Skin type?", "Dog or cat?" | Profile property with timestamp and source |
| Quiz | Routine finder, size finder | Properties plus recommended product |
| Post purchase survey | "Where did you hear about us?" (attribution input for `measurement`), "Who is it for?" | Properties; aggregate to measurement |
| Preference center | Topics, frequency, channels | Subscription preferences |
| Winback survey | "Why did you stop?" | Properties; feeds product and offer-strategy |

Rules: ask only what you will use within 30 days; show the value exchange; do not ask for special category data (health conditions, religion, sexual orientation) without a lawful basis reviewed by `compliance`. Meta's customer list terms (updated December 2025) restrict building ad audiences from health or financial information [Unverified exact wording via secondary, 2025-12], so never export health related zero party data to ad platforms.

## 7. The personalization ladder

| Level | What | Evidence needed | Effort |
|-------|------|----------------|--------|
| 1 | Name, last viewed item, dynamic cart | None (hygiene) | Low |
| 2 | Lifecycle stage and engagement tier content | Holdout optional | Low |
| 3 | Category affinity versions of campaigns | A/B vs generic | Medium |
| 4 | Product recommendations (catalog based, "bought together") | A/B vs bestsellers block | Medium |
| 5 | Predictive timing and channel (send time optimization, channel selection) | A/B or vendor control group | Medium |
| 6 | AI decisioning of offer, content, time, frequency per person (Braze Decisioning Studio, Klaviyo Composer and personalization models, Iterable Nova) | Holdout at program level; guardrails on offers and claims | High |

Rule: personalization ships only after it beats a holdout or a generic version. AI generated copy uses only PRODUCT_FACTS.md and CLAIMS.md; AI offer selection operates only inside the offer bounds approved by offer-strategy and the human.

## 8. AI segmentation and agents (2026 state)

| Tool | Capability (as announced) | Status |
|------|---------------------------|--------|
| Klaviyo Composer | Generates campaigns, flows, segments and push campaigns from a prompt; human approves before anything goes live | Debuted 2026-03-24; public beta from 2026-06-30 [Official, Klaviyo newsroom 2026] |
| Klaviyo data platform SQL via Composer and MCP | Natural language question to SQL over account data, returns answer and query | Preview announced at K:BOS 2026-09 [Secondary, 2026-09; Unverified availability] |
| Braze Decisioning Studio Go | Self-serve agents test variant, time, day and frequency per recipient within marketer guardrails; first agents optimize email clicks | Beta, GA 2026-10-14 [Official, Braze 2026-09-29] |
| Braze Agentic Standards | Checks campaigns and Canvases against marketer rules, logs fixes | GA expected 2026-10 [Official, 2026-09] |
| Iterable Nova Agent, Monitoring and Analytics Agents | Build, audit, personalize; anomaly detection; natural language analytics | Nova 2026-04-22; Fall release 2026-09-24 phased rollout [Official, Iterable 2026] |
| Customer.io agent | Builds campaigns, reviews underperformers, behavioral analysis | Beta features 2026 [Official, Customer.io 2026] |
| Mailchimp Analytics AI, AI Segment Builder (beta) | Conversational analytics, AI built segments | 2026-05-28 [Official, Intuit] |
| Omnisend Reports AI | Natural language reporting | All paid users from 2026-08 [Official, Omnisend changelog] |

Guardrails for every AI feature: keep it in draft or suggestion mode at automation stages 1 to 3; require a human to approve any send, offer, segment that changes consent scope, or flow activation (G3); log AI generated content IDs in the change request; check facts and claims; keep a holdout so AI "lift" is measured, not assumed.

## 9. Data hygiene for segmentation

- One person, one profile: merge by email and phone; guest checkouts create duplicates (Klaviyo profile merge API exists [Official, Klaviyo API 2026-07-15]).
- Consistent event names after platform migrations (old and new "Placed Order" metrics both mapped).
- Revenue net of refunds for monetary scores.
- Time zones stored for SMS quiet hours (from phone country and area code, or shipping address).
- Test and employee profiles excluded by a property, not by memory.
- Suppressed profiles retained (to keep suppression), never re-imported as subscribed.

## 10. Lifecycle states from events

Every customer holds exactly one state per weekly snapshot, derived from purchase or usage events and measured against the customer's own rhythm. A weekly buyer who goes quiet turns At risk long before a twice a year buyer with the same silence. Pattern proven in production apps, generalized here [Practitioner consensus]. It refines the stage model in [Strategy and metrics](lifecycle-strategy-and-metrics.md) section 1: At risk keeps its 1.5x to 3x band, and Lapsed splits into Dormant and Churned.

### 10.1 Cadence and states

Event = a paid order net of full refunds (ecommerce), or the core usage event for apps and SaaS (never a bare app open). Cadence blends the customer's own median gap with the store median reorder interval ([Cohort and LTV analysis](cohort-and-ltv-analysis.md) section 4), so a customer with few events leans on the store figure:

```
cadence = (n_gaps x own_median_gap + 2 x store_median) / (n_gaps + 2)     -- n_gaps = events minus 1
r       = days since last event / cadence
```

| State | Rule at each weekly snapshot (first match wins) |
|-------|--------------------------------------------------|
| Churned | Explicit end (subscription cancelled with no one time order since, or account deleted) OR r over 6 OR 730 days without an event |
| Dormant | r over 3, up to 6 |
| At risk | r over 1.5, up to 3 |
| New | Exactly 1 event, r up to 1.5 |
| Returning | Last event ended a gap over 1.5 x cadence (the customer had been At risk or worse), r up to 1.5 |
| Active | 2 or more events, last gap within 1.5 x cadence, r up to 1.5 |

The multipliers 1.5, 3 and 6, the shrink weight 2 and the 730 day cap are starting points [Practitioner consensus]; check them against the project's repeat curve before use. With 1 or 2 gaps the blend leans on the store median, so a slow but steady buyer can read as At risk or Returning until a few more gaps exist; that is intended, since 1 or 2 gaps are weak evidence. In SQL: join events to `GENERATE_DATE_ARRAY(start, CURRENT_DATE(), INTERVAL 1 WEEK)` keeping events before each snapshot, take `APPROX_QUANTILES(gap, 2)[SAFE_OFFSET(1)]` as the own median (`IFNULL` to 0 when n_gaps is 0) and `ARRAY_AGG(gap IGNORE NULLS ORDER BY event_date DESC LIMIT 1)[SAFE_OFFSET(0)]` as the last gap, then apply the table as a `CASE`.

### 10.2 Weekly cohort table

| First event week | Customers | Active or Returning at W4 | W8 | W12 | W26 | Churned at W26 |
|------------------|-----------|---------------------------|----|-----|-----|----------------|

Under it, one flow line per week: counts per state, save rate (At risk last week that are Returning this week / At risk last week), revival rate (the same from Dormant) and slip rate (Active or Returning last week that are At risk this week / Active or Returning last week). A rising slip rate is the earliest retention warning; compare it with its own 8 week median.

### 10.3 State to flow, suppression and paid media

| State | Flow ([Core flows](core-flows.md)) | Suppression rule | Paid media use (through `measurement`) |
|-------|------------------------------------|------------------|----------------------------------------|
| New | Post purchase, first time buyer branch (section 6) | Out of welcome discounts, first order offers and winback | Excluded from acquisition; existing customer list |
| Active | Replenishment ([Replenishment and subscriptions](replenishment-and-subscriptions.md)), cross sell and VIP (sections 7 and 11) | Out of winback and discount led campaigns | Excluded from acquisition; cross sell audiences for high value only |
| Returning | Repeat buyer branch with a welcome back note, no new incentive | Out of winback for one cadence | Existing customer list; out of reactivation ads |
| At risk | Winback W1 to W2 (section 8) and the "why did you stop?" survey | Out of generic campaigns while in winback (one stream at a time) | Paid winback only after 21 days of email and SMS non response |
| Dormant | Winback W3 to W4 with a tested incentive inside offer-strategy bounds | Campaign frequency cut to the E3 cadence (engagement tiers, section 1 of this file) | Reactivation audience with a spend cap |
| Churned | Sunset (section 9) for email non engagers; one churn survey | Out of all promotional sends after sunset; never re-subscribed by import | Existing customer list only if METRICS.md defines new customers as first order ever (under a 365 day rule they count as new again); reactivation spend only as a test |

Write the state to the profile as a property (G2) daily or weekly; the ESP's native ad syncs or the `measurement` pipeline build one audience per state. Every upload is G3 with the lawful basis check and an audience register row ([Lifecycle and paid media](lifecycle-and-paid-media.md) sections 1 and 3).

Handoffs: `measurement` (state pipeline, audience syncs, the existing customer list behind new customer goals), channel agents through the main session (exclusions and reactivation audiences), `offer-strategy` (incentive bounds for Dormant), `compliance` (consent for advertising use), `growth-orchestrator` (weekly state counts and slip rate).
