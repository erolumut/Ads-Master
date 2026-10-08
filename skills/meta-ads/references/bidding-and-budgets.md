# Bidding and Budgets

> Knowledge as of 2026-10. Bid strategy labels in Ads Manager: Highest volume, Highest value, Cost per result goal, ROAS goal, Bid cap. API names: LOWEST_COST_WITHOUT_CAP, COST_CAP, LOWEST_COST_WITH_MIN_ROAS, LOWEST_COST_WITH_BID_CAP (value optimization uses optimization_goal VALUE).

## 1. Unit economics first (compute before choosing a bid strategy)

Pull these from ads-master/PROJECT_BRIEF.md section 3. If missing, ask once, then mark assumptions.

| Metric | Formula | Example |
|--------|---------|---------|
| Contribution margin % (CM) | (Revenue minus COGS, shipping, payment fees, returns, variable costs) / Revenue | 45% |
| Breakeven ROAS | 1 / CM | 1 / 0.45 = 2.22 |
| Breakeven CPA (first order) | AOV x CM | 80 x 0.45 = 36 |
| LTV-based allowable CPA | 12-month LTV gross profit x payback share | 150 x 0.6 = 90 |
| Target platform ROAS | Breakeven ROAS x (1 + profit buffer) / incrementality factor | 2.22 x 1.2 / 0.8 = 3.33 |
| Lead gen allowable CPL | Allowable CAC x lead to customer rate | 900 x 0.08 = 72 |
| Cost per qualified lead target | Allowable CAC x SQL to customer rate | 900 x 0.25 = 225 |

Incrementality factor: ratio of incremental conversions (from a lift or geo test) to platform-reported conversions for the same period. Without a test, do not assume a number; use 1.0 for planning and flag the gap to `measurement`.

## 2. Bid strategy selection

| Strategy | UI label | How it behaves | Use when | Avoid when |
|----------|----------|---------------|----------|-----------|
| Lowest cost | Highest volume | Spends the full budget, gets the most results at the lowest average cost available | New campaigns, tests, Starter tier, when budget is the control | Hard CPA ceiling with large budgets in volatile auctions |
| Value optimization | Highest value | Spends budget to maximize total purchase value | Purchase values vary (AOV spread 2x or more), value is passed correctly | Values missing or constant, under about 30 purchases per week |
| Cost cap | Cost per result goal | Aims to keep average cost per result at or below goal; may underspend | Scale tier with a known target CPA; using budget as a ceiling and goal as the control | Thin data (learning never completes), goal set below what auctions allow |
| Minimum ROAS | ROAS goal | Aims to keep ROAS at or above goal; may underspend | Value-optimized ecommerce with stable values and a hard ROAS floor | Long consideration cycles where 7-day values are not representative |
| Bid cap | Bid cap | Hard ceiling on bid per auction | Experienced operators, flash sales, auctions with large CPM swings, controlling marginal cost | Most accounts; easy to choke delivery |

Setting values:
- Cost per result goal: start at target CPA, or at the trailing 14-day CPA if that is lower than target and volume matters. Give 3 to 7 days before changing. Change in steps of 10 to 20%.
- ROAS goal: start at about 80 to 90% of the trailing 14-day platform ROAS of the same campaign, never above the target from section 1 at launch. Raise in 5 to 10% steps after a stable week.
- Bid cap: start at 1.5 to 2 x target CPA (because bids are per auction and conversion rates vary), then tighten. Use lifetime budgets or large daily budgets because spend only happens when bids win.
[Practitioner consensus] on the starting points; Meta documents the behaviors but not the starting values.

Cost-controlled scaling pattern: set the cost per result goal or ROAS goal at target and set the budget at 2 to 5 x what you expect to spend. Spend then follows efficiency. Watch for days when it overspends at goal (good) versus spends nothing (goal too tight or creative fatigue).

## 3. Value optimization and value rules

Value optimization prerequisites:
- Purchase events carry `value` and `currency` on both Pixel and Conversions API, deduplicated.
- Values reflect revenue (or better, gross profit when sent as a custom value strategy approved by measurement).
- Enough purchase volume; Meta shows eligibility in the UI. Treat about 30 purchases per week at the ad set as the practical floor [Practitioner consensus].

Value rules let you tell Meta that some segments are worth more or less. Reported mechanics: bid adjustments from minus 90% to plus 1,000% (a placement can be made expensive to win, never impossible), up to 10 rules per rule set, criteria include age, gender, location, operating system, placement and audience segments where available [Official, 2025; ranges per secondary 2026 reports]. Rule set and criteria counts differ across 2026 guides (one rule set per ad set vs six per account; two vs four criteria per rule), so check the account. Reported eligibility: highest volume and cost per result goal ad sets, not bid cap or ROAS goal; not Sales campaigns mixing web and in-store conversions or Leads campaigns mixing web and calls [Practitioner reports, 2026-09]. Since the 2026-08 placement changes, placement value rules are the way to down-weight a placement without blocking it [Practitioner consensus, 2026-08].

| Use case | Rule | Evidence required |
|----------|------|-------------------|
| Women 35 to 54 have 1.6x LTV (CRM) | +60% for that segment | CRM LTV by segment, at least 6 months of data |
| Audience Network leads close at one third of the rate | Minus 60% on Audience Network | CRM close rate by placement |
| One region has 2x shipping cost | Minus 30% on that region | Margin by region |
| iOS users have higher AOV | +20% on iOS | Backend AOV by OS |

Rules for value rules: base every rule on backend or CRM data, never on Ads Manager CPA by segment alone (breakdown effect). Re-validate quarterly. Log each rule in ads-master/EXPERIMENTS.md with a holdout or pre/post read.

## 4. New customer and existing customer settings

Meta tracks audience segments (new audience, engaged audience, existing customers) defined in ad account settings. These power:
- Reporting breakdowns by audience segment (spend and results on new versus existing customers).
- Customer acquisition controls in Sales campaigns. Current state:
  - The legacy "existing customer budget cap" in Advantage+ shopping is no longer available; Meta's Help Center note (quoted by Jon Loomer, 2025) says to achieve the same result manually by excluding existing customer custom audiences [Official, 2025]. A few 2026 guides claim a reintroduced percentage cap; this could not be confirmed [Unverified].
  - Customer Lifecycle Strategy: an ad set setting in Sales campaigns with two options, reach new and existing customers (default) or acquire new customers only. It reads the Existing customers audience segment from Advertising settings and applies the exclusion automatically; Meta warns cost per result may rise. Closed beta from about April 2026, opened to all advertisers at Advertising Week on 2026-10-06 [Official, 2026-10] via Relevant Audience and Foxwell Digital. Early testers describe it as cleaner exclusions, not a new acquisition model [Practitioner reports, 2026-06].

Procedure:
1. Define existing customers with a CRM customer list (refreshed weekly via API or integration) plus purchase events (180 days). Define engaged audience with site visitors and social engagers.
2. Check the audience segment breakdown for the last 30 days. If existing customers receive more than 20 to 30% of acquisition spend and the business goal is growth, apply the new customer control available in the account: Customer Lifecycle Strategy set to acquire new customers only, or an excluded existing customer custom audience, or a two ad set split (existing customers only vs broad excluding them) with an ad set spend limit on the existing customer ad set.
3. Validate with backend new customer counts and new customer CAC, not platform numbers alone.

## 5. Incremental attribution optimization

What it is: an attribution model option (Standard or Incremental) where Meta optimizes delivery toward conversions predicted to be caused by the ad rather than conversions that would have happened anyway. Launched to Ads Manager in 2025 (incremental conversions can be viewed retroactively from 2025-04-01 via reporting columns); Meta reported a 46% lift in incremental conversions in its tests and earlier tests averaging more than 20% [Official, 2025]. An updated model in April 2026 with a 25% average increase appears in one agency blog only; no Meta announcement was found [Unverified, 2026-04]. Independent reads are mixed and improving: Haus reported a 43% win rate against standard settings in early tests [Study, 2025], then a pooled incremental return of 1.26x for incremental vs standard attribution across tests from July 2025 to June 2026 (DTC-only 1.38x, omnichannel 1.02x) [Study, 2026, vendor]; Cassandra reported incremental ROAS of 1.90x for cold acquisition and 3.64x for retargeting against platform-reported 8x [Study, 2025 to 2026, vendor].

Eligibility and constraints (verify in UI): Sales or Leads (some accounts also Engagement and App), website conversion location, maximize conversions or value goals; cost caps reported unsupported; only applies to new ad sets; replaces the standard attribution setting for that ad set.

When to test it:
- Account has stable tracking (EMQ for Purchase 7+ and deduplication working).
- At least 50 conversions per week in the ad set.
- High existing customer share or high organic baseline (brands with strong demand where standard attribution over-credits).
Design: run as an Experiments A/B test (standard vs incremental ad sets) for at least 2 to 4 weeks, judged on backend new customers and MER, not on platform ROAS (incremental reporting will show fewer conversions by design).

## 6. Budgets and the learning phase

Learning threshold: about 50 optimization events per ad set within 7 days after the last significant edit [Official, long-standing]. "Learning limited" appears when the ad set is not expected to reach it.

Budget needed per ad set:
```
Daily budget needed = (50 x target CPA) / 7  ~= 7.1 x target CPA
Example: target CPA 40 -> about 285 per day per ad set
If budget is lower: consolidate ad sets, optimize to a higher funnel event, or accept learning limited with highest volume.
```

Significant edits that restart learning [Official]: any targeting change, any creative change, optimization event change, adding a new ad to the ad set, pausing 7 days or more, bid strategy change, and significant changes to budget or bid amount.

Budget change rules [Practitioner consensus]:
| Situation | Change size | Frequency |
|-----------|------------|-----------|
| Stable ad set, scaling up | +15 to 30% | Every 48 to 72 hours |
| Under campaign budget (Advantage campaign budget) | +20 to 50% | Every 48 to 72 hours, campaign budget smooths shocks |
| Cost-controlled campaigns | Budget changes are low risk; the goal is the control | Any time; change the goal in 10% steps |
| Cutting spend | Up to 50% in one step | As needed; cuts rarely harm efficiency |
| Sale event | Use budget scheduling instead of manual edits | Planned in advance |

Daily versus lifetime budgets:
- Daily budgets can overspend on high-opportunity days by up to 75% (raised from 25% in early 2025), with weekly spend (Sunday to Saturday) capped at 7 x daily budget [Official in-account notice and support text, 2025-03, via Jon Loomer].
- Lifetime budgets are required for ad scheduling (dayparting). Dayparting is rarely worth it except for call centers and businesses with staffed hours (messaging, calls).

Campaign budget versus ad set budgets:
| Use campaign budget (Advantage campaign budget) | Use ad set budgets |
|---|---|
| Scaling campaigns with similar ad sets | Tests that need equal spend |
| Advantage+ status required | Strict allocation by geo or product line |
| You want Meta to move spend to the best marginal results | New ad set would get starved by a strong incumbent |

## 7. Budget allocation formulas

Spend split by maturity (starting point, then follow marginal returns):
| Maturity | Scaling | Testing | Catalog / retention | Experiments |
|----------|---------|---------|---------------------|-------------|
| New account | 70% | 30% | 0% | 0% |
| Running | 75% | 15% | 10% | 0 to 5% |
| Plateau | 60% | 25% | 10% | 5% |
| Scaling | 75% | 10% | 10% | 5% |

Marginal CPA check (use daily data, 14 to 28 days):
```
Marginal CPA between two spend levels = (Spend_2 minus Spend_1) / (Conversions_2 minus Conversions_1)
If marginal CPA > allowable CPA, the last increment lost money even if average CPA looks fine.
```
Use backend conversions where possible.

## 8. Worked examples

Example A (ecommerce, Growth tier): AOV 70, CM 40%, breakeven ROAS 2.5, 120 purchases per month, Meta spend 9k.
1. One Advantage+ sales campaign, highest volume, purchase optimization, 300 per day (about 7 x CPA of 42 would be 294).
2. After 4 stable weeks with values varying 2.5x, switch a duplicate test to highest value via an A/B test.
3. Do not set a ROAS goal until weekly purchases exceed about 50 per ad set.

Example B (lead gen, Scale tier): allowable CAC 1,200, lead to SQL 30%, SQL to close 25%, allowable cost per lead = 1,200 x 0.3 x 0.25 = 90.
1. Leads campaign optimized for conversion leads once the CRM sends lead stage events.
2. Cost per result goal at 90 on the lead, budget 3 x expected spend.
3. Weekly check: cost per SQL from CRM. If cost per SQL exceeds 300 (1,200 x 0.25), tighten the form (higher intent) before lowering the cost goal.

Example C (app): install CPA 4, D7 payer rate 2.5%, allowable cost per payer 160. Optimize to install while app event volume is under 50 per week, then to the purchase app event with value once volume allows, with SKAdNetwork and MMP reconciliation handled by `measurement`.
