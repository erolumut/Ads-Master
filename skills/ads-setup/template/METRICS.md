# Metric Dictionary

> One definition per metric for this project. Every agent uses these definitions. Change them only with a `DECISIONS.md` entry.

| Metric | Definition for this project | Source of truth | Grain | Additivity | Notes |
|--------|------------------------------|-----------------|-------|------------|-------|
| Revenue | Net of VAT, discounts and refunds? (decide) |  | order | additive |  |
| Order (counted) | Paid, not test, not fully refunded? (decide) |  | order | additive |  |
| New customer | First paid order ever for this email or customer ID |  | customer | additive |  |
| AOV | Revenue / orders |  | order | ratio |  |
| Platform CPA | Platform spend / platform reported conversions (state the attribution setting) | Ad platform | campaign day | ratio | Directional |
| Blended CAC | Total paid media / new customers | Backend + platforms | day | ratio |  |
| nCAC | Paid media / new customers (new customer revenue only) |  | day | ratio |  |
| Acquisition investment | Media spend + shipping subsidy + bonus product cost + incremental discount cost | Backend + platforms | day | additive | Use it, not media CPA alone, when offers subsidize the first order |
| Blended first order acquisition cost | Acquisition investment / new customers |  | day | ratio |  |
| MER | Total revenue / total paid media |  | day | ratio |  |
| aMER | New customer revenue / total paid media |  | day | ratio |  |
| Contribution before marketing | Revenue - product cost - fulfillment - payment fees - shipping subsidy - discounts |  | order | additive |  |
| Contribution after marketing | Contribution before marketing - media spend |  | day | additive |  |
| POAS | Gross profit / ad spend |  | campaign day | ratio |  |
| Repeat rate | Share of acquired customers ordering again within 30, 45, 60, 90 days | Backend | first order cohort | ratio | Cohort by first order date |
| Lead to customer rate | Customers / qualified leads (lead gen) | CRM | lead cohort | ratio |  |

## Game metrics (game projects only; exact formulas and traps in the measurement skill, references/game-kpis.md)

| Metric | Definition for this project | Source of truth | Grain | Additivity | Notes |
|--------|------------------------------|-----------------|-------|------------|-------|
| DAU | Distinct users with a qualifying event in the day (state the event and the timezone) |  | day | count, not additive across days |  |
| D1, D7, D30 retention | Classic: active exactly on day N / install cohort (state timezone and install definition) |  | install cohort | ratio | Never mix classic and rolling |
| ARPDAU | (IAP net revenue + ad revenue) / DAU, shown split |  | day | ratio |  |
| Payer conversion | Payers / users in the stated window (cohort or daily, say which) |  | cohort or day | ratio |  |
| Impressions per DAU | Ad impressions / DAU, per placement |  | day | ratio |  |
| Event participation | Event participants / DAU in the event window |  | event | ratio |  |
| Counted attempts per day | Constant per ranked board, from data/monetization-policy.json |  | board | constant | Never changed by purchases or rewards |

## Soft launch gates (game projects; derived from this game's own curve, not copied)

| Gate | Threshold | Minimum cohort | Window | Decision |
|------|-----------|----------------|--------|----------|
| D1 |  |  |  |  |
| D7 |  |  |  |  |
| ARPDAU or D7 ROAS |  |  |  |  |

## Reporting rules
- Additivity decides how a metric rolls up. Additive metrics (spend, revenue, orders) are summed. Ratio metrics (ROAS, CPA, CAC, MER, POAS, AOV, CVR, repeat rate) are never averaged across campaigns, days or markets: sum the numerator and the denominator, then divide. A report that averages ratios is wrong.
- Every figure in an outbound report is re-derived from the source file or connector for that report (measure before quote). Never copy a number from notes, memory or an earlier report.
- Always show platform reported and backend observed side by side. Never hide the gap; explain it.
- Report daily, decide on 3 and 7 day windows (except incidents).
- Every number carries its source and date range.
- Separate FACTS, INTERPRETATION and RECOMMENDATION in every report.
