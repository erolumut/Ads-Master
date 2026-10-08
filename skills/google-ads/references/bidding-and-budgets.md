# Bidding and Budgets

> Knowledge as of 2026-10. Two 2026 changes alter how targets behave: the target-based bidding update rolled out 2026-08-17 to 2026-08-27, and campaign total budgets entered open beta 2026-01-15. Verify both in Google Ads Help.

## 1. The strategy menu

| Strategy | Optimizes | Use when | Avoid when |
|---|---|---|---|
| Maximize conversions | Most conversions for the budget | Launch, budget is the constraint, lead gen with uniform lead value | Values differ a lot between conversions |
| Maximize conversions + target CPA | Conversions at an average CPA | Lead gen, uniform value, 30+ conversions in 30 days | Values vary; very low data |
| Maximize conversion value | Most value for the budget | Ecommerce launch, value-based lead gen | No real values |
| Maximize conversion value + target ROAS | Value at an average ROAS | Ecommerce, value-based lead gen, 50+ conversions in 30 days with varied values | Fixed values only |
| Target impression share | Visibility | Brand terms only | Non-brand (buys expensive irrelevant clicks) |
| Maximize clicks | Clicks | No tracking, brand with cap, traffic tests | Conversion goals |
| Manual CPC | Your bids | Very low data, strict brand control, testing | Accounts with enough data (you lose auction-time signals) |
| Target CPM, CPV | Reach, views | Video reach and views | Conversion goals |
| tCPI, tCPA, tROAS in App campaigns | Installs, in-app actions, value | App | |

Enhanced CPC was retired for Search and Display; affected campaigns run as Manual CPC [Official, announced 2024-10, effective 2025-03].

## 2. Choosing a strategy (decision tree)

1. Is conversion tracking verified with the business outcome as primary? No: Maximize clicks with a max CPC cap, or Manual CPC, while tracking is fixed.
2. Brand campaign? Yes: target impression share (top or absolute top, 85% to 95%) with a max CPC limit, or Maximize clicks with cap. Switch to tCPA if brand CPC rises because competitors bid.
3. Do conversion values vary by more than about 30% between conversions? Yes: value-based (Maximize conversion value, then tROAS). No: Maximize conversions, then tCPA.
4. Fewer than 15 conversions in 30 days for this strategy? Pool campaigns in a portfolio strategy, or use Maximize conversions without a target.
5. 30+ (tCPA) or 50+ (tROAS) conversions in 30 days? Add a target set at the last 30-day actual, then tighten gradually.

## 3. Setting targets: formulas

```
Breakeven CPA          = average gross profit per conversion (after COGS, shipping, fees, returns)
Target CPA             = breakeven CPA x (1 - required margin of safety), or LTV-based CPA (below)
LTV-based CPA          = (12-month contribution per customer) x (share of LTV you will pay to acquire), e.g. 40%
Lead gen target CPA    = target cost per sale x lead-to-sale rate
                         e.g. 900 per sale x 12% lead-to-sale = 108 per lead
Breakeven ROAS         = 1 / contribution margin           (40% margin -> 2.5 = 250%)
Target ROAS            = breakeven ROAS x (1 + profit buffer)  (250% x 1.2 = 300%)
POAS                   = gross profit attributed / ad cost (target above 1.0 to be profitable on first order)
Marginal ROAS          = change in value / change in cost when budget or target moves
```

Google ROAS targets are entered as percentages (300% = 3.0). Check whether the account's conversion values include tax and shipping; inconsistent value definitions break tROAS.

Target change rules [Practitioner consensus]:
- Start the target at the last 30-day actual, not at the goal.
- Change targets by 10% to 15% at a time, at most every 1 to 2 weeks (2 to 3 conversion cycles for long lags).
- Never change target and budget on the same day in the same direction of risk.
- After a target change, judge on at least 2 weeks or 30 conversions.

## 4. Target-based bidding update (August 2026)

Google updated its bidding systems so that campaigns perform more consistently toward the targets you set. Rollout ran from 2026-08-17 and completed 2026-08-27. [Official, 2026-07 help articles "Changes to target based bid strategies" and FAQ]

What changes:
- Budget-limited campaigns using tCPA or tROAS that were beating their targets may now move closer to the target. Example reported from Google's help content: a 10 tCPA campaign delivering 5 conversions may drift toward 10. [Official example via trade press, 2026]
- Google does not change your budgets or targets automatically.

What to do:
1. List campaigns that are budget-limited and beating target by 20% or more (GAQL budget query plus CPA vs target).
2. Either lower the target to the level you actually want (tighter tCPA, higher tROAS), or raise the budget if the marginal results are profitable.
3. Compare performance 4 weeks before 2026-08-17 vs 4 weeks after 2026-08-27 for these campaigns; annotate the journal so other agents do not misread the shift.

## 5. Learning periods

- A learning period follows: new strategy, target change, conversion goal change, large budget change, major structure change.
- Typical length: about 1 to 2 weeks or a few conversion cycles; one Google help variant mentions up to about 50 conversion events or 3 conversion cycles [Contested, 2026-09].
- During learning, do not judge CPA or ROAS daily. Use 7-day rolling numbers and check for tracking breaks first.

## 6. Portfolio strategies and bid limits

- A portfolio bid strategy shares one target across campaigns and pools learning. Use it for campaigns split for budget or reporting reasons that share a target.
- Portfolio tCPA and tROAS support max and min CPC bid limits (standard campaign-level targets do not). Use max CPC limits to avoid runaway CPCs in brand or highly competitive auctions; caps reduce volume.
- Do not combine campaigns with very different conversion lags or values in one portfolio.

## 7. Seasonality adjustments and data exclusions

| Tool | Use | Do not use |
|---|---|---|
| Seasonality adjustment | Short events (1 to 7 days best, up to 14) where conversion rate is expected to change sharply: flash sale, Black Friday, a promo launch. Enter the expected conversion rate change | Long seasons (Smart Bidding already adapts), normal weekly cycles |
| Data exclusion | Tracking outages, double counting, site downtime: exclude the affected dates so Smart Bidding ignores them | Normal performance dips |

Both are set in Tools, Shared library, Bid strategies, Advanced controls. Scope by campaign type or specific campaigns, and by date and time.

## 8. Smart Bidding Exploration

- Lets tROAS flex down (10% to 30%, your choice) to explore new query categories. Generally available for Search tROAS from 2025-07 [Official]. Google reported an 18% average increase in unique converting query categories and 19% more conversions (internal data, 2025-03-11 to 2025-04-11) [Official claim, not independently verified].
- Expanded to Shopping and PMax (PMax without product feeds globally available from 2026-06) [Practitioner report, 2026-06, verify].
- Use when: tROAS campaign with broad match or AI Max, not budget-limited (Search lost IS budget near 0%), stable tracking, 30 to 50+ conversions a month.
- Expect: lower average ROAS on explored traffic, more total conversion value. Judge on total profit, over 6 weeks.

## 9. Journey aware bidding (lead gen, beta)

- Uses later funnel stages (MQL, SQL, proposal, won) that you import as signals to improve bidding toward the primary biddable conversion. The later stages inform the model without counting as conversions. [Practitioner reports, 2026]
- Status: discussed in 2025, beta for Search tCPA in 2026 (reports say from 2026-05), no GA date confirmed [Contested timing, Unverified eligibility]. Reports say it is gated to lead gen accounts that already import offline conversions.
- Preparation: import every CRM stage with GCLID or enhanced conversions for leads, consistently, within 24 to 48 hours of the stage change.

## 10. New customer acquisition and retention goals

| Mode | Behavior | Use |
|---|---|---|
| Bid equally for new and existing customers | Default | Retention is not a goal |
| Bid higher for new customers than existing customers | Adds a new customer value to conversions from new customers | Growth with existing customer remarketing elsewhere |
| Only bid for new customers | Restricts bidding to new customers (Search, PMax) | Pure acquisition budgets |
| High value new customer (option) | Adds extra value for predicted high value new customers | When you can define high value customers via lists |
| Retention goals (PMax) | Re-engage lapsed customers | Lifecycle programs |

Requirements: Customer Match lists of existing customers (refresh at least monthly) and/or conversion-based detection. Set the new customer value from data (incremental 12-month contribution of a new customer), not a guess. API v25 moved lifecycle goal configuration into the unified Goal and CampaignGoalConfig resources (breaking change for automations) [Official via trade press, 2026-07].

## 11. Budgets: mechanics

| Rule | Detail |
|---|---|
| Daily overdelivery | A campaign can spend up to 2x its average daily budget on a given day [Official] |
| Monthly charging limit | You are not charged more than the average daily budget x 30.4 in a month [Official] |
| Budget changes mid-month | The monthly limit recalculates; large mid-day changes can create uneven spend |
| Shared budgets | One budget across campaigns. Use for small accounts or brand clusters; avoid mixing campaigns with different targets because the budget flows to the easiest spender |
| Campaign total budgets | Set one budget for a date range: 3 to 90 days for Search, Shopping and PMax; up to 1 year for Demand Gen and YouTube. No daily cap, never charged more than the total, pacing recalculates from remaining budget [Official, 2026-01 open beta] |
| Demand-led pacing | Reported upgrade to budget pacing for Search and Shopping in 2026 [Unverified] |
| Missed Opportunities | Report (beta) moved into Recommendations in 2026-07: missed clicks, conversions and value split by budget or bid limits [Practitioner report, 2026-07] |
| Budget simulators and bid simulators | Estimate marginal results of budget and target changes. Use as directional only |

## 12. Budget allocation logic

1. Fund brand first (cheap, protects demand), sized to 90% to 95% impression share unless tests prove brand is not incremental.
2. Fund non-brand campaigns where marginal CPA or ROAS meets target, starting with the best marginal return.
3. Identify the binding constraint for each campaign:
| Signal | Constraint | Action |
|---|---|---|
| Search lost IS (budget) above 10% and CPA at or below target | Budget | Raise budget 15% to 20% per step, or loosen nothing |
| Search lost IS (rank) above 40%, spend under budget | Target or Ad Rank | Loosen target 10%, improve ads and landing pages |
| Spend under 80% of budget with target met | Target too strict or limited demand | Loosen target, broaden match or AI Max test |
| Spend at budget, CPA above target | Inefficient | Tighten target, cut waste, fix tracking or landing pages |
4. Move money between campaigns based on marginal returns from simulators and Missed Opportunities, then confirm with real results after 2 weeks.
5. Big reallocations (over 20% of channel budget) need an incrementality read; hand off to growth-orchestrator and measurement.

## 13. Pacing procedure (daily, 2 minutes)

```
Days elapsed                  = d, days in month = D
Month-to-date spend           = S
Projected month spend         = S / d x D
Pacing ratio                  = projected / planned monthly budget
Healthy                       = 0.95 to 1.05
Action if above 1.10          = propose budget cut on lowest marginal return campaigns
Action if below 0.90          = check limited by target, disapprovals, tracking, then propose loosening
```

The budget pacing script in [GAQL and scripts](gaql-and-scripts.md) automates this.

## 14. Bidding diagnostics

| Symptom | Causes | Fix |
|---|---|---|
| Spend collapsed after setting a target | Target too aggressive vs history | Reset target to 30-day actual, step down 10% every 2 weeks |
| CPA jumped after a budget increase | Moving into less efficient auctions; learning | Wait 2 weeks; if marginal CPA is above target, revert half |
| ROAS drifted toward target after 2026-08 | Target-based bidding update on budget-limited campaigns | Tighten target or raise budget deliberately |
| Smart Bidding chasing micro conversions | Wrong primary conversion actions | Fix goals (conversion module) |
| Erratic results after promotions | Seasonality adjustment missing or left on too long | Add for short events only, remove after |
| Learning after every small change | Too many edits | Batch changes weekly |
| Bidding learned from a tracking outage | Data not excluded | Add data exclusion for the outage dates |
