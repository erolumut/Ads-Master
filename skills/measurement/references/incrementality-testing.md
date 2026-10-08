# Incrementality Testing

Incrementality answers "what would have happened without this spend?" It is the verdict that calibrates attribution and MMM. This module covers designs, platform lift tools, geo experiments, small budget options, power analysis, reading results, vendors and pitfalls.

## 1. When to test (prioritization)

Score candidate tests by: spend at stake x uncertainty x decision value. Test first:
1. The largest channel by spend (most money at risk).
2. Channels most likely to be over credited: brand search, retargeting, view-through heavy video, Advantage+ or PMax with high existing customer share.
3. Channels the platforms under credit but you believe matter (upper funnel video, creators, podcasts, CTV).
4. Any channel before a budget change larger than 20%.

## 2. Design hierarchy

| Design | Randomization unit | Strength | Weakness | Typical use |
|--------|--------------------|----------|----------|-------------|
| Platform conversion lift (user level holdout) | Users, by the platform | Randomized, easy, measures platform outcomes incl. logged-in views | Platform runs it and defines conversions; only that platform | Meta, Google, TikTok channel value |
| Geo experiment (randomized or matched markets) | Regions (DMA, state, province, city) | Platform independent, uses backend outcomes | Needs enough geos and volume; spillover | Channel and cross-channel value, MMM calibration |
| Synthetic control geo test | Test regions vs weighted combination of control regions | Works with few test regions | Model assumptions | Small budgets, national brands |
| Time-based switchback (on and off) | Time blocks, sometimes by geo | Cheap | Seasonality, carryover | Small channels, brand search |
| Holdout audience (always on) | A fixed share of users or geos never served | Continuous read | Opportunity cost | Retargeting, email, CRM audiences |
| Pre and post | None | Cheapest | Confounded by everything else | Last resort, with synthetic control at minimum |

## 3. Platform lift tools (status October 2026)

| Platform | Tool | Requirements and notes | Label |
|----------|------|------------------------|-------|
| Google Ads | Conversion Lift (user based) | Minimum campaign budget $5,000 USD and at least 1,000 observed conversions (conversions with supplementary data do not count); feasibility rating High (60% to 90% chance of conclusive result), Medium, Low (0% to 30%); directional results below 90% confidence available; Search and Performance Max joined Display, Video, Demand Gen and App as self-serve | [Official help page; threshold cut reported 2025-05 (GML) or 2025-11, sources differ] |
| Google Ads | Conversion Lift (geography based) | Beta, limited access, needs a Google representative, single-country campaigns; Search, Shopping and PMax | [Official] |
| Google Ads | Search Lift, Brand Lift | Search interest and brand metrics | [Official] |
| Meta | Conversion Lift (Experiments in Ads Manager) | Randomized test and control at user level; eligibility and minimum sizes shown in the tool; works with pixel, CAPI and offline events | [Official; verify current thresholds] |
| Meta | GeoLift (open-source R package) | Geo experiments with synthetic control, market selection and power analysis | [Official open source] |
| TikTok | Conversion Lift Study | Usually via TikTok representative; spend and duration minimums apply | [verify] |
| Microsoft Ads | PMax uplift experiments | Reported generally available by 2026-09-08 | [Official per microsoft-ads research, 2026] |

Platform lift caveat: the platform defines the conversion (its pixel or CAPI events) and runs the analysis. Use backend data where the tool supports offline outcomes.

## 4. Geo experiment procedure

1. Question and KPI: one channel or campaign set, one KPI from backend data by geo (orders, new customers, revenue, qualified leads). Never use platform-reported conversions as the KPI.
2. Geo unit: smallest unit you can both target in the platform and measure in the backend (US DMA or state, Turkey province, EU NUTS regions or cities). Need at least about 20 units; more is better.
3. Data: at least 2x the test length of daily or weekly pre-period data per geo (ideally 6 to 12 months) to choose markets and fit the model.
4. Market selection: GeoLift market selection or matched markets by correlation of pre-period KPI; exclude outlier geos (very large metros can be held out or forced into control).
5. Power analysis: estimate the minimum detectable effect (MDE) for candidate test sizes, durations and budgets. Proceed only if the MDE is below the effect you expect and below the effect that would change the decision.
6. Treatment: for a "go dark" test, turn spend off in test geos (measures current spend value). For a "scale" test, increase spend in test geos by a defined multiple (measures marginal return). Keep everything else equal.
7. Duration: 2 to 6 weeks of treatment, plus a cooldown of 1 to 2 weeks (or the typical purchase lag) for carryover, measured in the analysis.
8. Guard against contamination: exclude test geos in every campaign of the tested channel; keep national campaigns (TV, other channels) constant or present in both arms; watch for algorithms shifting budget.
9. Freeze: no other major changes in test or control (prices, promotions by region, site changes).
10. Readout: lift, incremental conversions, iROAS or incremental CPA with confidence or credible intervals; compare to platform-attributed conversions in test geos to compute the incrementality factor.
11. Decide and log: EXPERIMENTS.md row, MEASUREMENT.md incrementality evidence, journal entry, handoff to growth-orchestrator and the channel agent.

### GeoLift (R) skeleton

```r
# Illustrative; check GeoLift documentation for current function arguments
library(GeoLift)
geo <- GeoDataRead(data = df, date_id = "date", location_id = "region",
                   Y_id = "orders", format = "yyyy-mm-dd", summary = TRUE)
sel <- GeoLiftMarketSelection(data = geo, treatment_periods = c(21, 28),
                              N = c(3, 4, 5), Y_id = "Y", location_id = "location",
                              time_id = "time", effect_size = seq(0, 0.3, 0.05),
                              cpic = 42, budget = 40000, alpha = 0.1,
                              side_of_test = "one_sided", fixed_effects = TRUE)
# After the test period:
fit <- GeoLift(Y_id = "Y", data = geo, locations = c("izmir", "bursa", "antalya"),
               treatment_start_time = 181, treatment_end_time = 208)
summary(fit)
```

cpic is the cost per incremental conversion assumption used to size the budget. Use your current calibrated CPA, not platform CPA.

Alternatives: Google's CausalImpact (R) or tfcausalimpact (Python) for synthetic control on a single treated series; Google's Trimmed Match for paired geo designs; PyMC or custom Bayesian structural time series; vendor platforms.

## 5. Sizing and power

Quick MDE intuition for geo and user tests:
- Noise matters more than volume: a KPI with stable day to day patterns across geos supports smaller MDEs.
- Longer tests reduce MDE roughly with the square root of duration until seasonality and carryover dominate.
- A 50/50 split minimizes MDE for a fixed total; spend constraints often push to smaller test cells.

User-level two-proportion approximation (per arm sample size):

```
n per arm = (z_alpha/2 + z_beta)^2 x [p1 x (1 minus p1) + p2 x (1 minus p2)] / (p1 minus p2)^2
alpha 0.10 two-sided -> z = 1.645; power 0.80 -> z = 0.842
Example: control conversion rate 2.0%, expected treatment 2.3% (15% lift)
n = (1.645 + 0.842)^2 x (0.0196 + 0.02247) / 0.003^2 = 6.185 x 0.04207 / 0.000009 = about 28,900 users per arm
(a 5% lift, 2.0% to 2.1%, needs about 9 times as many users: halving the effect roughly quadruples the sample)
```

If the test cannot reach the needed size, change the design: higher volume KPI, bigger test share, longer duration, or test a bigger change (go dark rather than a 20% cut).

Budget for a go dark test equals the spend you withhold (opportunity cost), not new money. For a scale test, budget = extra spend in test geos.

## 6. Small budget designs (Starter and Growth)

| Situation | Design | Notes |
|-----------|--------|-------|
| One main channel, national, under $10k per month | Geo holdout of 20% to 30% of regions for 4 weeks with synthetic control readout | Accept wide intervals; repeat to accumulate evidence |
| Brand search | Pause brand ads in half of regions (or alternate weeks) where competitors do not bid on your brand; measure total brand clicks (paid plus organic) and backend orders | Often shows brand ads capture demand that organic would get; competitor bidding changes the answer |
| Retargeting | Exclude a random 20% of the audience (customer list or pixel audience split by hashed ID) | Many platforms support audience splits or A/B in Experiments |
| Google with 1,000+ conversions and $5k budget | User-based Conversion Lift | Use feasibility rating; prefer High |
| Meta with enough volume | Conversion Lift in Experiments | Read the tool's power estimate before launch |
| Very small accounts | Switchback (on and off by week) across 6 to 8 weeks, reading backend orders | Weakest; treat as directional |

## 7. Reading results

| Metric | Formula |
|--------|---------|
| Lift % | (test outcome minus counterfactual) / counterfactual |
| Incremental conversions | test outcome minus counterfactual over the test period plus cooldown |
| iROAS | incremental revenue (or gross profit) / spend in test cells |
| Incremental CPA | spend in test cells / incremental conversions |
| Incrementality factor | incremental conversions / platform-attributed conversions in the same cells and period |

Decision rules:
1. Interval entirely above breakeven (iROAS or incremental CPA vs target): keep or scale, then test the next budget level.
2. Interval straddles breakeven: do not make big moves; extend, repeat or redesign with more power.
3. Interval entirely below breakeven: reduce spend or restructure (creative, audience, objective), then retest.
4. A null result from an underpowered test is not evidence of zero effect. Report the MDE with every null.
5. Apply the incrementality factor only to the scope tested; refresh every 6 to 12 months.

Report template:

```
Test: <ID> <channel> <design> <dates incl cooldown>
KPI and source: backend <KPI> by <geo unit>
Cells: test geos (n), control geos (n), spend in test cells
Result: lift X% (90% interval a% to b%), incremental conversions N (interval), iROAS R (interval)
Platform-attributed conversions in test cells: P -> incrementality factor N / P
Power: planned MDE m%, achieved
Decision: <keep, scale, cut, retest> and why
Caveats: contamination, seasonality, external events
```

## 8. Vendors and tools

| Option | Type | Notes |
|--------|------|-------|
| GeoLift (Meta, open source) | R package | Free; needs analyst skill |
| CausalImpact, tfcausalimpact, Trimmed Match (Google open source) | R and Python | Free |
| PyMC-Marketing | Python | Bayesian MMM with lift test calibration |
| Haus | Managed geo experiment platform (synthetic control), plus causal MMM | Commercial; pricing not public [Unverified] |
| Measured | Incrementality testing and media planning platform | Commercial |
| Recast | Bayesian MMM with geo test tooling | Commercial |
| Lifesight | Unified measurement (MMM, experiments, attribution) | Commercial |
| Other self-serve geo test tools | Several newer vendors offer lower cost self-serve geo tests | Evaluate design transparency |

Vendor evaluation questions: method (synthetic control, randomization, Bayesian or frequentist), power analysis before launch, use of backend data, handling of carryover and spillover, transparency of code or method notes, cost per test, ability to export results, how results feed MMM.

## 9. Pitfalls

| Pitfall | Effect | Prevention |
|---------|--------|-----------|
| Peeking and stopping early | False positives | Fix duration in advance; use sequential methods if you must monitor |
| Using platform conversions as the KPI | Circular evidence | Backend outcomes by geo |
| Spillover (people cross geo borders, national campaigns) | Diluted lift | Larger geo units, buffers, keep other channels constant |
| Algorithm reallocation | Spend leaks into control or shifts within test | Exclude geos at campaign level in every campaign; monitor spend by geo daily |
| Simultaneous promotions by region | Confounded result | Freeze regional promos |
| Ignoring carryover | Underestimated lift | Cooldown period in readout |
| One test treated as permanent truth | Stale decisions | Retest every 6 to 12 months or after big changes |
| Testing too small a change | Unreadable | Go dark or 2x scale |

## 10. EXPERIMENTS.md row example

| ID | Date | Agent | Hypothesis | Primary metric | ICE | Design | Stop rule | Status | Result | Learning |
|----|------|-------|-----------|----------------|-----|--------|-----------|--------|--------|----------|
| E014 | 2026-10-12 | measurement | If we pause Meta in 6 matched provinces for 4 weeks, backend new customer orders there drop by at least 12%, because Meta drives incremental acquisition | Backend new customer orders by province | 8/6/6 | Geo go dark, synthetic control (GeoLift), 2-week cooldown | Fixed 6 weeks; no early stop | backlog | | |
