# Bidding, Budgets and Frequency

> Scope: bidding strategies, choosing and moving cost caps, manual bidding for small audiences, charge types, budget minimums and pacing, Dynamic Group Budget, frequency caps and budget sizing for learning. Verified 2026-10-08 where labeled; minimums and pacing behaviors change, so confirm in Campaign Manager. UI names since 2025-10: Campaign (old campaign group), Ad set (old campaign).

## 1. Bidding strategies

| Strategy | How it works | Use when | Risk |
|----------|-------------|----------|------|
| Maximum delivery (automated) | LinkedIn bids to spend the budget for the most results | New campaigns, learning the market price, broad audiences | Can overpay in small audiences; volatile CPMs |
| Cost cap | Automated bidding that tries to keep average cost per result at or below your cap | Known acceptable cost per result; scaling | Under delivery if the cap is below market |
| Manual bidding | You set the max bid per click or per thousand impressions | Small ABM audiences, retargeting, strict cost control | Under delivery or overpay if set poorly |
[Official, 2026-10] for the three strategies (Help Center: options depend on objective and format); "Target cost" was replaced by Cost cap [Unverified] for the date. No new bid strategy (value based or otherwise) was found for 2025 to 2026. New optimization goal: Qualified leads for Lead generation (2025-04; API MAX_QUALIFIED_LEAD in 202602) [Official, 2026-02]. Ad selection weighs the bid with predicted engagement, so relevance lowers effective cost [Official].

Charge types by format: CPM or CPC for Sponsored Content, CPV for video, cost per send for Sponsored Messaging, CPC or CPM for text ads [Official, 2026-10]. Benchmark for sends: $0.36 per send for content offers and $0.49 for demo offers (Kiin panel, 2026) [Study, 2026]. Sponsored Messaging lead gen ad sets default to OPTIMIZED creative selection since 2026-07; set ROUND_ROBIN (even rotation) to keep tests fair [Official, 2026-07].

## 2. Strategy selection tree
```
Is the audience under about 20,000 members (ABM, retargeting)?
  yes -> Manual bidding (CPM for awareness, CPC for clicks) starting near the low end of the suggested range
  no  -> continue
Do you know the acceptable cost per result from history?
  no  -> Maximum delivery for 2 to 3 weeks with a daily budget you can afford to learn with
  yes -> Cost cap at your acceptable cost per result (from CRM economics), then adjust
Is volume stalling under a cost cap?
  yes -> raise cap 10% to 15% or broaden audience; check creative CTR first
```

## 3. Setting a cost cap from economics
```
max cost per SQL     = first year gross profit x SQL to won rate x payback share
max cost per lead    = max cost per SQL x lead to SQL rate
initial cost cap     = min(max cost per lead, observed cost per lead under Maximum delivery x 0.9)
```
Example: first year gross profit $20,000, SQL to won 25%, payback share 40% gives max cost per SQL $2,000. Lead to SQL 12% gives max CPL $240. Observed CPL under Maximum delivery $210 gives initial cap $189. If volume collapses, step up toward $240 in 10% increments. Illustrative numbers.

## 4. Manual bidding for small audiences
- Start at or slightly below the bottom of the suggested range shown in Campaign Manager for CPM or CPC.
- If daily spend reaches under 50% of budget for 3 days, raise the bid 10% to 15%.
- If CTR is healthy and cost per result exceeds target, lower the bid 10% and broaden roles.
- For ABM awareness, prefer CPM: you are paying for reach into named accounts, and CPC bidding in tiny audiences can price you out of delivery.

## 5. Budgets and minimums
| Item | Rule | Label | Practice |
|------|------|-------|----------|
| Daily budget minimum | $10 per day (USD accounts), any format | [Official, 2026-10] | Small budgets learn slowly; consolidate |
| Lifetime budget minimum | $100 for new, inactive ad sets; after launch the minimum becomes $10 x total scheduled days; the screen shows the floor if the budget is too low | [Official, 2026-10] | Use lifetime budgets for fixed flights (events) |
| Daily overspend | Daily spend can reach up to 50% above the daily budget on a given day (Help Center example: $100 daily budget, up to $150 in a day, January total capped at $3,100) | [Official, 2026-10] | Pace on weekly or monthly totals, never on one day |
| Daily reset | Once the daily budget is reached the ad set leaves the auction until the next day, reported as midnight UTC | [Practitioner consensus, 2025-08] (B2Linked) | US West Coast budgets reset late afternoon local time |
| Pacing | LinkedIn recommends lifetime budgets with lifetime pacing, which predicts a week of platform activity to spread spend | [Official, 2026-10] | Use for flights with fixed totals |
| Dynamic Group Budget (campaign level budget) | One budget across 1 to 50 ad sets in a campaign; Sponsored Content only; all ad sets share objective, bid strategy and budget type; daily or lifetime, not both; Maximum delivery recommended; no forecasting; cannot be turned off or the objective changed after launch; suggested start $100 daily or $1,000 lifetime | [Official, 2026-10] | Judge on total results and average cost per result at campaign level, not per ad set; large audiences pull more budget |
| Accelerate floors | Getting started guide lists lifetime floors of $700 (Website visits) and $3,000 (Lead generation) with a 14 day minimum | [Contested] (undated PDF) | Check the setup screen |
| Minimum bids | Floors exist by format and audience; Campaign Manager shows suggested ranges based on what competing advertisers likely pay | [Official, 2026-10] for suggested ranges; floors [Unverified] | Check suggested ranges |

Budget sizing for learning:
```
monthly budget per campaign = target cost per result x 30 to 50 results
```
Example: target cost per lead $200 means $6,000 to $10,000 per month per lead gen campaign to learn properly [Practitioner consensus]. At Starter tier, run fewer campaigns rather than starving many.

Budget split by funnel (starting point, adjust with data):
| Program | Starter | Growth | Scale |
|---------|---------|--------|-------|
| Demand creation (awareness, engagement, video, Thought Leader) | 20% to 30% | 30% to 50% | 40% to 60% |
| Retargeting and nurture | 30% to 40% | 20% to 30% | 15% to 25% |
| Lead capture and ABM conversion | 30% to 50% | 20% to 40% | 20% to 35% |
Rationale: the 95 to 5 principle and long B2B cycles favor protected demand creation spend [Study, 2021]; Binet and Field's B2B work also argues for substantial brand investment [Study, 2019]. Treat splits as hypotheses to test with holdouts.

## 6. Pacing
```
expected spend to date = monthly budget x (days elapsed / days in month)
pacing ratio = actual spend to date / expected spend to date   (0.9 to 1.1 fine)
```
Under delivery causes: audience too small, cap or manual bid too low, creative with low CTR (relevance), rejected ads, payment issue. Over delivery causes: budget edits, campaign group budgets missing, duplicate campaigns.

## 7. Frequency management
- Track 30 day frequency by ad set (impressions / unique members reached) and CTR by week. Reach is estimated, and Average frequency is impressions per member account that saw at least one impression [Official, 2026-10].
- Frequency cap setting [Official, 2025-07]:
  - Where: Budget and schedule section of Classic ad sets with the Brand awareness objective; applies across the LinkedIn feed, Audience Network and CTV Ads; editable while running; rollout was gradual, so some accounts may not show it.
  - Options: Default (LinkedIn sets a dynamic cap for the optimization goal) or Customize (3 to 30 impressions per member account per 7 days).
  - Behavior: with the Impressions goal the custom cap overrides the default; with the Reach goal the cap is an input and LinkedIn may favor the setting that maximizes reach.
  - API: MAX_FREQUENCY with a 7 day span, BRAND_AWARENESS only.
- Other objectives have no manual cap; control frequency through budget, audience size and creative count. ABM and retargeting audiences saturate quickly; plan more creative variants and rotate offers rather than raising budget.
- Signals of over frequency: CTR falls 30%+ from launch while frequency rises; negative social signals; rising CPC with stable CPM.

Frequency planning rule of thumb [Practitioner consensus]:
| Program | Target 30 day frequency per member | Brand awareness cap setting (per 7 days) |
|---------|-----------------------------------|------------------------------------------|
| Cold ICP awareness | 2 to 6 | Customize 3 |
| ABM tier 1 | 6 to 15 with 4+ creatives rotating | Customize 4 to 6 |
| Retargeting | 4 to 10 with offer rotation | Not available outside Brand awareness |

## 8. When to raise or cut budget
| Situation | Move |
|-----------|------|
| Cost per qualified lead under target, delivery capped by budget | Raise 15% to 20% per week |
| Cost per qualified lead under target, delivery not capped | Broaden audience or add creative; budget increase will not deliver |
| Cost per qualified lead over target for 30 days with healthy CTR | Lower cap or bid; tighten audience; check form friction and follow up |
| CTR below own baseline by 30% | Creative refresh before budget changes |
| Demand creation campaign with rising engager pools and pipeline influence | Hold budget through at least one sales cycle before judging |

## 9. Worked budget plan (Growth tier, illustrative)

Monthly LinkedIn budget $20,000; target cost per SQL $1,500; observed CPL $180 under Maximum delivery; lead to SQL 12%.

| Program | Campaigns | Budget | Bidding | KPI and ceiling |
|---------|-----------|--------|---------|-----------------|
| Demand creation | 2 (Thought Leader to ICP, document ungated to ICP) | $7,000 | Maximum delivery, then Cost cap per engagement | ICP reach, engager pool, pipeline influence |
| ABM tier 1 | 1 (company list x buying committee) | $4,000 | Manual CPM | Account reach 80%+, engaged accounts |
| Retargeting | 1 (engagers and visitors to demo offer) | $4,000 | Cost cap at $160 per lead | Cost per SQL under $1,500 |
| Lead capture | 1 (ICP to assessment offer with qualifying question) | $5,000 | Cost cap at $180 per lead | Cost per SQL under $1,500 |
Check: lead capture plus retargeting $9,000 at about $170 per lead gives about 53 leads and about 6 SQLs at a 12% rate, roughly $1,500 per SQL. If the SQL rate drops below 10%, cost per SQL breaks the ceiling; fix quality before adding budget.

## 10. Flights, campaign groups and schedules
- Use lifetime budgets with start and end dates for events, launches and tests so spend cannot run past the window.
- Use campaign level (old campaign group) budgets or schedules to cap a program when several ad sets share an allocation; Dynamic Group Budget goes further and reallocates between ad sets automatically [Official, 2026-10].
- For always on programs, use daily budgets and review pacing weekly.
- Before holidays, decide per program: hold, reduce or pause; record in the journal.
- After any pause longer than 2 weeks, expect a short relearning period; avoid judging the first week.

## 11. Common bidding and budget mistakes
| Mistake | Effect | Fix |
|---------|--------|-----|
| Maximum delivery on a 2,000 member ABM list | Very high CPMs | Manual CPM |
| Cost cap set from wishful CPL | No delivery | Cap from observed cost and economics |
| Ten campaigns at $10 per day | No learning | Consolidate |
| Judging awareness spend on leads | Cutting what builds future pipeline | Judge on reach, engagement and later pipeline |
| Changing bids, budget and creative at once | Unreadable results | One change per cycle |
