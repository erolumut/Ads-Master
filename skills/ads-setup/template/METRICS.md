# Metric Dictionary

> One definition per metric for this project. Every agent uses these definitions. Change them only with a `DECISIONS.md` entry.

| Metric | Definition for this project | Source of truth | Notes |
|--------|------------------------------|-----------------|-------|
| Revenue | Net of VAT, discounts and refunds? (decide) | | |
| Order (counted) | Paid, not test, not fully refunded? (decide) | | |
| New customer | First paid order ever for this email or customer ID | | |
| AOV | Revenue / orders | | |
| Platform CPA | Platform spend / platform reported conversions (state the attribution setting) | Ad platform | Directional |
| Blended CAC | Total paid media / new customers | Backend + platforms | |
| nCAC | Paid media / new customers (new customer revenue only) | | |
| Acquisition investment | Media spend + shipping subsidy + bonus product cost + incremental discount cost | Backend + platforms | Use it, not media CPA alone, when offers subsidize the first order |
| Blended first order acquisition cost | Acquisition investment / new customers | | |
| MER | Total revenue / total paid media | | |
| aMER | New customer revenue / total paid media | | |
| Contribution before marketing | Revenue - product cost - fulfillment - payment fees - shipping subsidy - discounts | | |
| Contribution after marketing | Contribution before marketing - media spend | | |
| POAS | Gross profit / ad spend | | |
| Repeat rate | Share of acquired customers ordering again within 30, 45, 60, 90 days | Backend | Cohort by first order date |
| Lead to customer rate | Customers / qualified leads (lead gen) | CRM | |

## Reporting rules
- Always show platform reported and backend observed side by side. Never hide the gap; explain it.
- Report daily, decide on 3 and 7 day windows (except incidents).
- Every number carries its source and date range.
- Separate FACTS, INTERPRETATION and RECOMMENDATION in every report.
