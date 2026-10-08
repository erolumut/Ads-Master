# Value and Profit Optimization

Bidding systems maximize whatever value you send them. Send revenue and they chase revenue, including low margin and one-time buyers. This module covers profit values (POAS), new versus returning customer values, predicted LTV, lead values and the safe rollout of value changes.

## 1. Value hierarchy

| Level | Value sent | When to use | Data needed |
|-------|-----------|-------------|-------------|
| 1 | Revenue (excluding tax and shipping) | Uniform margins, Starter tier | Order value |
| 2 | Revenue with a new customer premium | Acquisition goal, repeat business | New customer flag at order time |
| 3 | Gross profit | Margins vary by more than about 15 points across products | COGS by SKU |
| 4 | Contribution margin | Shipping, payment fees, returns vary by product or region | COGS, shipping cost, fees, return rates |
| 5 | Predicted LTV (pLTV) | Subscriptions, consumables, high repeat rate | Cohort history or a model |

Move up one level at a time, and only when the data feeding the value is reliable and refreshed.

## 2. Core formulas

```
Gross profit (order)          = revenue (ex tax, ex shipping) minus COGS
Contribution margin (order)   = gross profit minus shipping cost minus payment fees minus expected returns cost minus pick and pack
POAS                          = gross profit (or contribution) attributed / ad spend
Breakeven POAS                = 1.0 when the value is contribution margin before marketing
Breakeven ROAS                = 1 / contribution margin %   (example: 38% margin -> 2.63)
Target ROAS from target POAS  = target POAS / contribution margin %
MER                           = total revenue / total marketing spend
aMER (acquisition MER)        = new customer revenue / total marketing spend (or / acquisition spend; define once)
nCAC                          = acquisition spend / new customers
LTV:CAC                       = contribution margin LTV over a fixed horizon / nCAC
Payback months                = nCAC / monthly contribution margin per customer
```

Worked example: AOV $85, COGS $34, shipping $7, fees $3, returns allowance $4. Gross profit $51; contribution $37 (43.5%). Breakeven ROAS on revenue = 1 / 0.435 = 2.30. A campaign at ROAS 2.5 is profitable on first order; a campaign at 2.0 is not, unless new customer LTV covers it.

## 3. Sending profit as the conversion value

Never put COGS or margin in the browser data layer. Competitors and scrapers can read it.

| Method | How | Pros | Cons |
|--------|-----|------|------|
| A. sGTM lookup | Browser sends revenue and item IDs; server container looks up margin by SKU (Firestore, Google Sheets, BigQuery via API) and rewrites value before sending to Google Ads and Meta | Real time, margin hidden | Needs sGTM, margin table upkeep |
| B. Backend sender | Order webhook computes profit from ERP data and sends server events with profit value | Most accurate | Browser event values differ; set browser event value to the same profit or send purchase only server-side for that platform |
| C. Google conversions with cart data plus COGS | Send items (id, price, quantity) with the Google Ads purchase tag, add cost_of_goods_sold in Merchant Center; Google reports gross profit metrics | No margin exposure in tags, profit reporting in Google Ads | Reporting; bidding still on the value you send unless you also change it |
| D. Offline value adjustment | Upload restatements with profit value after the order | Works without sGTM | Delayed; Google only |
| E. Profit tools | Third-party profit tracking apps that send profit to Google Ads (several exist for Shopify and WooCommerce) | Fast setup | Vendor dependency; check how they treat consent |

Rule for dual values: keep GA4 purchase value as revenue (finance comparability) and send profit to ad platforms as their conversion value. Document both in MEASUREMENT.md.

## 4. Margin feeds and segmentation

- Add margin bands as custom labels in the product feed (for example custom_label_0 = margin_high, margin_mid, margin_low) so channel agents can split Shopping and PMax campaigns or asset groups by margin. Hand off to commerce-feeds.
- Refresh labels at least monthly and after price or cost changes.
- Exclude or cap products with negative contribution after shipping (often low price, heavy items).

## 5. New versus returning customers

| Platform | Mechanism | Measurement requirement |
|----------|-----------|-------------------------|
| Google Ads | Customer acquisition goal: "Bid higher for new customers than for existing customers" (adds a value per new customer) or "Only bid for new customers"; new customers identified by Customer Match lists, conversion tag new_customer parameter, or Google's detection | Send `new_customer: true or false` on the purchase conversion; keep customer lists fresh (upload with consent) |
| Meta | Advantage+ sales campaigns: define existing customers via customer lists and pixel or app events, use budget caps for existing customers, report new versus existing | Customer list refresh, purchase events with external_id |
| Microsoft | PMax new customer acquisition goal (GA in 2026 per Microsoft Ads releases) | Customer lists, conversion goals |
| TikTok and others | Mostly via audience exclusions and reporting | Customer lists |
| GA4 and backend | Flag first order per customer (email or customer ID) in backend; send as purchase parameter (for example customer_type new or returning) | Backend logic, consistent definition (lookback, for example no order in 365 days counts as new) |

Value of a new customer premium:

```
New customer premium = (12-month contribution LTV of a new customer) minus (first order contribution)
Example: first order contribution $37, 12-month contribution LTV $78 -> premium about $41 per new customer
Discount it for uncertainty (use 50% to 80% of the premium) until a cohort confirms it
```

## 6. Predicted LTV values

| Approach | Data | Tooling | Fit |
|----------|------|---------|-----|
| Cohort multiplier | 12 to 24 months of order history | SQL in BigQuery | Growth tier, simple |
| Segment multipliers | Cohort multipliers by first product, channel, discount use, region | SQL | Growth to Scale |
| Probabilistic CLV (BG/NBD plus Gamma-Gamma) | Transaction history per customer | PyMC-Marketing CLV module, lifetimes library | Scale |
| ML pLTV at first order | First order features, browsing, demographics | BigQuery ML, Vertex AI, vendor tools | Scale, Enterprise |
| GA4 predictive metrics | Purchase probability, churn probability, predicted revenue (eligibility: at least 1,000 returning purchasers and 1,000 non-purchasers in a 7-day window within the last 28 days) [Official, verify] | GA4 audiences | Audiences, not values |

Rules for pLTV values:
1. Fixed horizon (90 or 180 days) and contribution basis, not revenue.
2. Cap outliers (for example at the 99th percentile) so one wholesale buyer does not teach the algorithm a false pattern.
3. Send at conversion time (pLTV at first order) or via adjustment within the platform's allowed window.
4. Back-test: compare predicted vs actual for cohorts at least monthly; recalibrate if error over 20%.
5. Keep revenue in GA4 and finance reports; pLTV only in bidding values.

## 7. Lead gen and SaaS values

Use stage values from [Offline and CRM conversions](offline-and-crm-conversions.md) section 4. Additional rules:
- Score leads at submission with known predictors (company size, role, service type, budget field, geography) and send a predicted value with the lead event; correct later with offline stages.
- For SaaS, value trials by predicted conversion to paid times first-year gross profit; value activation events (PQL) higher than raw signups.
- Disqualified leads: send a low or zero value, or do not send; never let spam leads carry the same value as real ones.

## 8. Google Ads value tools

| Tool | Use | Caveat |
|------|-----|--------|
| Conversion value rules (location, device, audience, new customer) | Adjust value by segment when you know segments differ in true value | Adds complexity; validate with backend profit by segment |
| Conversion adjustments | Retract or restate values after refunds or deal changes | Needs order_id |
| Conversions with cart data | Item-level reporting, gross profit with COGS | Merchant Center feed must have matching IDs |
| Portfolio and seasonality adjustments | Temporary conversion rate shifts (sales events) | Channel agent owns bidding; measurement provides the data |
| Data exclusions | Exclude periods with broken tracking from bidding | Use after outages; hand off to google-ads |

## 9. Safe rollout of a value change

1. Simulate: recompute last 90 days of orders with the new value logic; compare value totals and distribution by campaign. Expect campaign ROAS targets to shift.
2. Translate targets: if values fall from revenue to profit (for example 45% of revenue), target ROAS must fall to about 45% of the old target to keep the same aggressiveness. Hand off to channel agents with the exact factor.
3. Start with secondary: create the new value conversion as secondary for 2 to 4 weeks to compare.
4. Switch on a low traffic day, one platform at a time, with the target translated at the same moment.
5. Annotate and monitor 14 days: spend pacing, conversion volume, value per conversion, backend profit.
6. Roll back if backend contribution margin after marketing drops more than an agreed threshold (for example 10%) after the learning period.

## 10. Common mistakes

| Mistake | Effect | Fix |
|---------|--------|-----|
| Revenue includes tax and shipping in one platform and not another | ROAS comparisons meaningless | One convention |
| Margin in the data layer | Competitive leak | Server-side lookup |
| Switching to profit values without lowering tROAS | Spend collapses | Translate targets |
| Values in cents | 100x inflated values | Units |
| Different currencies across platforms | Wrong totals | Report in one currency with dated FX rates |
| New customer flag based on browser cookie | Returning customers counted as new | Backend customer ID or email |
| pLTV with no back-test | Systematic overbidding | Monthly predicted vs actual |
