# Unit Economics and Forecasting

Every target in Ads Master derives from these formulas. Show the math in every deliverable, with the source of each input.

## 1. Definitions and formulas
| Metric | Formula | Use | Watch out |
|--------|---------|-----|-----------|
| Net revenue | Gross sales minus discounts, returns, VAT or sales tax | Base for everything | Platform "revenue" often includes tax and shipping; normalize |
| CM1 (gross margin) | Net revenue minus COGS | Product profitability | |
| CM2 (contribution before marketing) | CM1 minus shipping, payment fees, pick and pack, returns cost, marketplace fees | Breakeven ROAS input | Include every variable cost per order |
| CM3 (contribution after marketing) | CM2 minus marketing spend | The scoreboard | Use all marketing spend, not only paid media |
| Contribution margin % | CM2 / net revenue | Targets | |
| Breakeven ROAS | 1 / contribution margin % | Minimum acceptable revenue ROAS on first order | Revenue ROAS uses platform attributed revenue; reconcile |
| Breakeven CPA | AOV x contribution margin % | First order CPA ceiling | |
| Target ROAS | 1 / (contribution margin % minus target profit % of revenue) | Bidding target | Target profit % must be below CM % |
| POAS | Contribution (or gross profit) attributed / ad spend | Profit based bidding (needs margin in conversion value) | Breakeven POAS = 1.0 when contribution is used |
| MER | Total net revenue / total marketing spend | Blended efficiency | Includes returning customers and organic |
| Target MER | 1 / (contribution margin % minus target CM3 % of revenue) | Blended guardrail | |
| aMER | New customer net revenue / total marketing spend | Acquisition efficiency | Needs new vs returning split in backend |
| CAC (blended) | Marketing spend / all customers acquired in period | Rough view | Inflated by returning buyers counted as customers |
| nCAC | Acquisition marketing spend / new customers | Growth efficiency | Define whether retention spend is excluded |
| LTV (gross margin) | Sum over horizon of (orders x AOV x contribution margin %) per customer | Allowable CAC | State horizon: 6, 12 or 24 months |
| LTV (subscription) | ARPA x gross margin % / monthly churn rate | SaaS and subscriptions | Use cohort data when churn changes over tenure |
| LTV to CAC | LTV / nCAC | Health check | 3 is a common target; under 1.5 is a red flag [Practitioner consensus] |
| CAC payback (months) | nCAC / monthly contribution per customer | Cash planning | Use contribution, not revenue |
| Incremental CPA | Platform CPA / incrementality factor | Allocation | Factor from lift tests (budget-allocation.md) |

## 2. Ecommerce worked example
Inputs (from PROJECT_BRIEF.md; example values):
| Item | Per order |
|------|-----------|
| AOV (net of VAT and discounts) | $100.00 |
| COGS | $35.00 |
| Shipping cost | $8.00 |
| Payment fees (3%) | $3.00 |
| Pick and pack | $3.00 |
| Returns allowance (net cost) | $4.00 |
| **CM2** | **$47.00** |

- Contribution margin % = 47 / 100 = 47%.
- Breakeven ROAS = 1 / 0.47 = 2.13. Breakeven CPA = $47.
- Target ROAS for 10% profit on revenue after ads = 1 / (0.47 minus 0.10) = 2.70. Target CPA = 100 x 0.37 = $37.
- POAS view: at ROAS 2.70, contribution per $1 of ad spend = 2.70 x 0.47 = 1.27, so POAS 1.27 (profit of $0.27 per $1 after ad cost).

### 2.1 With LTV
Assume 12 month orders per new customer = 1.8 (first order plus 0.8 repeats), repeat AOV $90.
- 12 month contribution LTV = (100 + 0.8 x 90) x 0.47 = (100 + 72) x 0.47 = $80.84.
- Max nCAC at LTV to CAC 3 = 80.84 / 3 = $26.95 (conservative, profit focused).
- Max nCAC for 12 month payback with zero profit = $80.84 (aggressive, growth focused).
- Pick a point between based on cash and goal. Write it in STRATEGY.md with the reasoning.

### 2.2 Translate to channel targets
| Channel KPI | Formula | Value |
|-------------|---------|-------|
| First order tCPA ceiling | Breakeven CPA | $47 |
| Growth tCPA (6 month payback) | 6 month contribution LTV | Compute with 6 month repeat rate |
| tROAS (Google, revenue values) | Target ROAS from section 1, adjusted by incrementality factor | 2.70 / factor |
| POAS bidding (value = margin) | Target POAS 1.0 to 1.3 | Needs margin in conversion values (commerce-feeds custom labels or server-side value rules) |

## 3. Lead gen and B2B funnel math
### 3.1 Funnel
```
Spend -> Leads (CPL) -> MQL (lead to MQL %) -> SQL (MQL to SQL %) -> Opportunity -> Closed won (win rate) -> Revenue (ACV or deal value)
Cost per SQL = CPL / (lead to SQL rate)
Cost per customer (media CAC) = CPL / (lead to customer rate)
```

### 3.2 Worked example (B2B SaaS)
| Input | Value | Source |
|-------|-------|--------|
| ACV | $12,000 | CRM |
| Gross margin | 80% | Finance |
| Target CAC payback | 12 months | STRATEGY.md |
| Media share of fully loaded CAC | 50% (rest is sales cost) | Finance estimate |
| Lead to SQL | 25% | CRM, last 2 quarters |
| SQL to closed won | 20% | CRM |

- Max fully loaded CAC (12 month payback) = 12,000 x 0.80 = $9,600.
- Max media CAC = 9,600 x 0.5 = $4,800.
- Leads per customer = 1 / (0.25 x 0.20) = 20.
- Max CPL = 4,800 / 20 = $240. Max cost per SQL = 4,800 x 0.20 = $960.
- Channel check: LinkedIn CPL $180 with lead to SQL 15% gives cost per SQL $1,200 (above $960, fail despite lower CPL). Search CPL $260 with lead to SQL 35% gives cost per SQL $743 (pass). Judge on cost per SQL and closed won, never CPL alone.

### 3.3 Local services example
Average job value $450, gross margin 55%, booking rate from qualified calls 40%, qualified share of calls 70%.
- Contribution per job = $247.50. If break even on first job: max cost per job = $247.50.
- Calls per job = 1 / (0.7 x 0.4) = 3.57. Max cost per call = 247.50 / 3.57 = $69.30.
- With repeat or referral value (for example 1.5 jobs per customer over 12 months), max cost per job rises to $371.25.

### 3.4 Lead value for value based bidding
Value per lead stage = probability to close from that stage x deal value x gross margin. Example: SQL value = 0.20 x 12,000 x 0.8 = $1,920. Send stage values through offline conversion imports (measurement agent) so platforms bid on value, not lead count.

## 4. App economics
- Cost per install (CPI), install to paying %, ARPPU, retention curve.
- Max CPI = (D90 or D180 revenue per install x gross margin after store fees) / required payback multiple.
- Example: D180 revenue per install $3.20, store fee 15% to 30% (verify program eligibility), gross margin after fees 75% gives contribution $2.40. For payback at D180, max CPI $2.40.

## 5. Inflation and currency adjustments (high inflation markets such as Turkey)
- Re-base targets monthly: CPA and AOV in local currency both inflate. Compare in real terms: real value = nominal value / CPI index (base month = 100).
- Example: CPC TRY 8.00 in October 2025 and TRY 10.40 in October 2026 (+30%). If CPI rose 30% in the same period, real CPC is flat. A 30% "CPC increase" is then not an auction problem.
- Use contribution margin %, ROAS and POAS for cross period comparison (ratios are less inflation sensitive than absolute CPA).
- If costs are in USD or EUR (imported goods) and revenue in local currency, margin moves with FX: refresh CM % monthly.
- Ad invoices from foreign entities may carry withholding and reverse charge VAT that raise the true cost of media (geo-market-modules.md). Use the true cost in CAC.

## 6. Forecasting model
### 6.1 Driver tree
```
Revenue = New customer revenue + Returning customer revenue
New customer revenue = sum over channels (conversions(spend_c) x new customer share_c x AOV_new) + organic new
conversions(spend_c) = response curve of channel c (budget-allocation.md), seasonality adjusted
Returning revenue = active customer base x repeat rate x AOV_repeat (from cohorts)
Organic = trend x seasonality (seo and ai-search-optimization inputs)
```

### 6.2 Bottom up vs top down
- Bottom up: given a budget, sum channel curves to forecast conversions and revenue.
- Top down: given a revenue target, solve for required spend by inverting curves (raise spend in the channel with the best marginal return until the target is met or marginal CPA hits the ceiling). If the ceiling is hit first, the target needs non media levers (CVR, AOV, new channel, brand) and the forecast must say so.

### 6.3 Scenarios
| Driver | Conservative | Base | Aggressive |
|--------|--------------|------|------------|
| CPA vs last 90 days (seasonality adjusted) | +15% | 0% | minus 10% |
| Site conversion rate | minus 10% | 0% | +10% (only if cro tests are scheduled) |
| AOV | minus 5% | 0% | +5% (only if AOV tests are scheduled) |
| Organic and AI traffic | trend minus 10% | trend | trend +5% |
| New channel contribution | 0 | 50% of test target | 100% of test target |
Every aggressive assumption must point to a scheduled action. Every conservative one to a known risk.

### 6.4 Scenario forecast script
```python
# python3 forecast.py  (edit the inputs dict; prints a monthly table per scenario)
inputs = {
  "months": ["2026-11", "2026-12", "2027-01"],
  "season": [1.25, 1.40, 0.85],              # seasonality index from last 2 years
  "spend": [40000, 48000, 32000],            # planned paid media
  "base_cpa": 38.0,                          # reconciled, last 90 days, seasonality adjusted
  "aov": 92.0, "cm_pct": 0.47,
  "returning_rev": [60000, 75000, 45000],    # from cohort model
  "organic_new_rev": [20000, 26000, 16000],
}
scen = {"conservative": (1.15, 0.95), "base": (1.0, 1.0), "aggressive": (0.90, 1.05)}
for name, (cpa_mult, aov_mult) in scen.items():
    print(f"\n{name}")
    for i, m in enumerate(inputs["months"]):
        cpa = inputs["base_cpa"] * cpa_mult / inputs["season"][i] ** 0.5  # peak months convert better, dampened
        conv = inputs["spend"][i] / cpa
        rev = conv * inputs["aov"] * aov_mult + inputs["returning_rev"][i] + inputs["organic_new_rev"][i]
        cm3 = rev * inputs["cm_pct"]-inputs["spend"][i]
        print(f"{m}: conv {conv:.0f}, revenue {rev:,.0f}, MER {rev/inputs['spend'][i]:.2f}, CM3 {cm3:,.0f}")
```
The square root dampening of seasonality on CPA is a planning heuristic, not a law. Replace it with the project's own seasonal CPA pattern once two seasons of data exist.

### 6.5 Forecast output table
| Month | Scenario | Spend | Conversions | New customers | Revenue | MER | aMER | CM3 | Key assumptions |
|-------|----------|-------|-------------|---------------|---------|-----|------|-----|-----------------|

### 6.6 Forecast accuracy loop
- Log each month's base forecast and actuals in the monthly review.
- MAPE = average of |actual minus forecast| / actual. Target under 15% after 3 months of data.
- When a miss exceeds 20%, decompose: spend vs plan, CPA vs assumption, CVR, AOV, organic, returning. Fix the driver that missed and record it in memory if it repeats.

## 7. Sensitivity table (what moves contribution most)
Compute CM3 change for a 10% improvement in each driver, holding others fixed. Typical ordering for paid heavy ecommerce: conversion rate and AOV changes often move CM3 more than a 10% CPC change because they also lift organic and returning revenue [Practitioner consensus]. Use the table to argue for cro and offer work when media is near its marginal ceiling.

| Driver +10% | Delta CM3 | Owner |
|-------------|-----------|-------|
| Site CVR | | cro |
| AOV | | cro, market-intel (bundles, pricing) |
| CPA minus 10% | | channel agents, creative-strategy |
| Repeat rate | | email and SMS (other-channels-quick-guides.md) |
| Gross margin | | human (pricing, suppliers) |

## 8. Checklist before publishing targets
- [ ] Contribution margin includes every variable cost; source named.
- [ ] Revenue normalized (net of VAT, discounts, returns).
- [ ] New vs returning split available, or the gap noted.
- [ ] LTV horizon stated; cohort source stated.
- [ ] Incrementality factors applied where tests exist.
- [ ] Taxes on ad spend and FX included for the geo.
- [ ] Targets written into STRATEGY.md draft and shared with each channel agent.
