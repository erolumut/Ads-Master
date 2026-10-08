# Budget Allocation

Allocate the next dollar to its highest marginal contribution, keep a protected test budget, and pace spend so the month lands on plan.

## 1. Average vs marginal returns
- **Average CPA** = total spend / total conversions. Tells you if a channel was worth it in aggregate.
- **Marginal CPA** = extra spend / extra conversions from that extra spend. Tells you what the next dollar buys.
- Channels saturate: as spend rises, each extra dollar reaches less responsive people at higher prices. Average CPA lags marginal CPA, so a channel can look fine on average while the last $10k was unprofitable.

Worked example:
| Month | Meta spend | Conversions | Average CPA | Marginal CPA vs previous month |
|-------|-----------|-------------|-------------|--------------------------------|
| Jan | $20,000 | 500 | $40.00 | n/a |
| Feb | $30,000 | 650 | $46.15 | $10,000 / 150 = $66.67 |
| Mar | $40,000 | 740 | $54.05 | $10,000 / 90 = $111.11 |
With a target CPA of $60, the average in March ($54) looks acceptable, but the last $10k bought conversions at $111. The right move is to hold Meta near $30k and test the extra $10k elsewhere.

Caveat: month over month marginal estimates mix seasonality and creative changes. Prefer response curves over several weeks, budget step tests, or MMM.

## 2. Response curves
### 2.1 Shape
Use a concave curve. Two practical forms:
- Log: `conversions = a * ln(spend) + b`, marginal conversions per $ = `a / spend`.
- Hill (used in MMM tools such as Google Meridian and Meta Robyn): `response = max_response * spend^s / (spend^s + half_sat^s)`.

### 2.2 Fit a log curve from weekly data (simple, good enough for monthly planning)
Requirements: 12+ weeks of spend and conversions for the channel, spend varied by at least 30% between low and high weeks, no tracking breaks, seasonality adjusted if strong.

```python
# python3 fit_curve.py weekly.csv  (columns: week,spend,conversions)
import csv, math, sys
rows = [r for r in csv.DictReader(open(sys.argv[1]))]
x = [math.log(float(r["spend"])) for r in rows]
y = [float(r["conversions"]) for r in rows]
n = len(x); mx = sum(x)/n; my = sum(y)/n
a = sum((xi-mx)*(yi-my) for xi, yi in zip(x, y)) / sum((xi-mx)**2 for xi in x)
b = my - a*mx
ss_res = sum((yi-(a*xi+b))**2 for xi, yi in zip(x, y)); ss_tot = sum((yi-my)**2 for yi in y)
print(f"a={a:.2f} b={b:.2f} R2={1-ss_res/ss_tot:.2f}")
for s in [5000, 7500, 10000, 12500, 15000]:
    conv = a*math.log(s)+b; marg_cpa = s/a  # marginal CPA = 1 / (a/s)
    print(f"weekly spend {s}: conv {conv:.0f}, avg CPA {s/conv:.2f}, marginal CPA {marg_cpa:.2f}")
```
Read: marginal CPA = spend / a. Example: a = 120, weekly spend $10,000, marginal CPA = $83. If max acceptable marginal CPA is $70, the channel's efficient weekly spend is about 70 x 120 = $8,400.

If R2 is under about 0.3, the curve is not informative: run a budget step test (section 5) instead.

### 2.3 Equalize marginal returns
At the optimum, every channel's marginal CPA (or marginal ROAS) is equal and at or better than the maximum acceptable marginal value. Procedure:
1. For each channel compute marginal CPA at current spend.
2. Move budget from the channel with the worst marginal CPA to the one with the best, in steps of 10 to 20%.
3. Recompute. Stop when marginal CPAs are within about 15% of each other or a channel hits its constraint (minimum viable budget, maximum audience, brand floor).

### 2.4 Max acceptable marginal CPA
```
Max marginal CPA (first order economics) = AOV x contribution margin %
Max marginal CPA (LTV economics) = LTV gross margin in payback window - required profit
```
Example: AOV $80, contribution margin 45%, max first order marginal CPA = $36. If 6 month gross margin LTV is $70 and the business accepts 6 month payback with no profit target, max marginal CPA = $70.

## 3. The 70/20/10 budget
| Bucket | Share | What goes in | Rules |
|--------|-------|--------------|-------|
| Core (70%) | Proven campaigns at or better than target | Scale within marginal limits | Weekly optimization, step changes up to 20% |
| Adjacent (20%) | Extensions of what works: new audiences, formats, markets, product lines on proven channels | Expected to reach target within 4 to 8 weeks | Graduates to core when it hits target 4 weeks in a row |
| New (10%) | New channels, new offers, unproven formats | Learning, not ROAS | Pre-registered success criteria and stop rules in EXPERIMENTS.md |
Starter tier: 85 to 100% core; focus beats exploration. Enterprise: test share can rise to 20% with MMM and lift tests reading it.

## 4. Reallocation cadence
| Cadence | Scope | Limits | Inputs |
|---------|-------|--------|--------|
| Daily | Pacing only | No strategic moves | Spend vs plan |
| Weekly | Within channel (campaigns, ad sets) | Max 20% change per line item per week to avoid resetting learning (Meta and TikTok learning phases, Google Smart Bidding recalibration) [Practitioner consensus] | Channel agent weekly reviews |
| Monthly | Across channels | Max 20 to 30% shift of a channel's budget per month unless a test result justifies more | Marginal CPA estimates, curves, MER trend |
| Quarterly | Strategic mix, new channels, brand share | Based on lift tests, MMM, strategy | Quarterly reset |

Platform notes for budget changes:
- Meta: large budget edits can re-enter learning; increases of about 20% or less every few days are the common practice [Practitioner consensus]. Campaign budget (Advantage+ campaign budget) lets Meta shift between ad sets.
- Google: Smart Bidding adapts to budget changes; target changes (tCPA, tROAS) have more effect than budget. Avoid changing both at once. Use seasonality adjustments only for short, predictable conversion rate shifts [Official, Google Ads Help].
- TikTok: Smart+ and ad group budgets behave like Meta; avoid daily big swings.
- LinkedIn and Microsoft: smaller auctions; changes show quickly; watch frequency on LinkedIn.

## 5. Budget step tests (when curves are weak)
1. Pick one channel. Hold creative and targets stable.
2. Raise budget 20 to 30% for 14 days (or until about 100 conversions at the new level).
3. Compute marginal CPA = (spend new - spend old) / (conversions new - conversions old), on backend or deduplicated numbers.
4. If marginal CPA is under max acceptable, step again. If over, step back and log the ceiling in memory once confirmed twice.
For a cleaner read, run the step as a geo test: raise budget in a random half of regions, compare to the other half (measurement agent designs it).

## 6. Using incrementality and MMM results
| Evidence | How to use it in allocation |
|----------|------------------------------|
| Conversion lift or holdout test (Meta, Google, TikTok lift studies) | Incrementality factor = incremental conversions / platform attributed conversions. Multiply platform CPA by 1/factor to get incremental CPA. Example: platform CPA $40, factor 0.6, incremental CPA $66.67 |
| Geo lift (GeoLift, Meridian geo models, matched markets) | iROAS per channel; use as the allocation number for that channel until retested |
| MMM (Meridian, Robyn, vendor) | Response curves and marginal ROI per channel; use the optimizer output as a starting allocation, constrained by MVB, brand floors and practical step limits |
| No test yet | Use reconciled platform numbers with a conservative discount for retargeting heavy channels; schedule a test for the largest line item |

Rules:
- Calibrate the MMM with lift tests where possible; an MMM that contradicts two lift tests is wrong until proven otherwise [Practitioner consensus].
- Re-test the biggest channel at least twice a year and after major structural changes.
- Never move more than about 30% of total budget on a single MMM run; step it and watch MER.

## 7. Budget pacing
### 7.1 Monthly pacing
```
Expected spend to date = monthly budget x (sum of seasonality weights for days elapsed / sum for the month)
Pacing % = actual spend to date / expected spend to date
Daily budget for remaining days = (monthly budget - spend to date) / remaining weighted days x weight of each day
```
Without a weighting, use days elapsed / days in month. Flag pacing outside 90 to 110% in the daily check; outside 80 to 120% is an alert.

Google note: campaign daily budgets can spend up to 2 times the daily budget on a given day, while monthly charges are capped at about 30.4 times the average daily budget [Official, Google Ads Help]. Plan with the monthly cap, not the daily number.

### 7.2 Seasonality index
Build from the last 2 years of daily revenue: index for a day or week = its revenue share divided by the average share. Apply to budget weights and to forecasts. For new businesses use Google Trends for the category in the target geo as a proxy (market-intel).

### 7.3 Peak periods
- Raise budgets before peak days (1 to 3 days early) so automated bidding can adjust; set Google seasonality adjustments for promotions of 1 to 7 days where conversion rate is expected to jump [Official, Google Ads Help].
- Hold the MER floor: daily check that blended MER stays above target MER; pull back on channels whose marginal CPA spikes.
- Post peak: reduce budgets gradually and revert seasonality settings.

## 8. Allocation worked example (Growth tier ecommerce)
Inputs: monthly budget $40,000. Contribution margin 50%, AOV $90, breakeven ROAS 2.0, max first order marginal CPA $45 (no LTV support assumed).
| Channel | Current | Avg CPA (reconciled) | Marginal CPA at current (curve) | Incrementality factor | Incremental marginal CPA |
|---------|---------|----------------------|----------------------------------|-----------------------|--------------------------|
| Google PMax + Search | $18,000 | $30 | $38 | 0.8 (lift test, 2026-Q2) | $47.50 |
| Meta | $16,000 | $35 | $42 | 0.9 (lift test, 2026-Q1) | $46.67 |
| TikTok | $4,000 | $45 | $40 | no test (assume 0.85) | $47.06 |
| Retargeting (all) | $2,000 | $15 | $60 | 0.4 (holdout) | $150 |
Decision: cut retargeting to $1,000 (incremental marginal CPA far above max), move $1,000 to TikTok (lowest incremental marginal CPA with room to learn), hold Google and Meta. All three main channels sit near the $45 ceiling, so additional growth needs better creative or offer (lowering CPA), not more budget. Log as hypothesis; recheck in 4 weeks.

## 9. Guardrails and floors
| Floor or cap | Default | Why |
|--------------|---------|-----|
| Brand search | Fund enough for 90%+ impression share on brand terms if competitors bid on them | Cheap protection; test incrementality in a brand holdout when competitors are absent |
| Retargeting | Under 10 to 20% of paid media | Low incrementality |
| Single channel concentration | Under 60% at Scale tier unless proven incremental | Platform risk (policy, outages, auction shocks) |
| Test budget | 10% at Growth and above | Future winners |
| Brand or demand creation | Set in brand-vs-performance.md | Long term demand |
| Cash | Spend limited by payback and cash runway | Growth that runs out of cash is not growth |

## 10. Allocation output (what to deliver)
1. Current vs proposed budget per channel and bucket (core, adjacent, new).
2. Marginal evidence per line (curve, step test, lift, MMM) with dates.
3. Expected impact on conversions, revenue, MER and contribution margin, with ranges.
4. Risks and rollback triggers.
5. Pacing plan for the month (weekly targets).
6. Change list (CHANGE_REQUEST.md) for the human.
