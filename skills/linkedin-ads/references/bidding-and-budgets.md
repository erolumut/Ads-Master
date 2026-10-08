# Bidding, Budgets and Frequency

> Scope: bidding strategies, choosing and moving cost caps, manual bidding for small audiences, charge types, budget minimums and pacing, frequency management and budget sizing for learning. Minimums and pacing behaviors change; verify in Campaign Manager.

## 1. Bidding strategies

| Strategy | How it works | Use when | Risk |
|----------|-------------|----------|------|
| Maximum delivery (automated) | LinkedIn bids to spend the budget for the most results | New campaigns, learning the market price, broad audiences | Can overpay in small audiences; volatile CPMs |
| Cost cap | Automated bidding that tries to keep average cost per result at or below your cap | Known acceptable cost per result; scaling | Under delivery if the cap is below market |
| Manual bidding | You set the max bid per click or per thousand impressions | Small ABM audiences, retargeting, strict cost control | Under delivery or overpay if set poorly |
[Official, 2024] for the three strategies; "Target cost" was retired in favor of cost cap [Unverified] for the date.

Charge types by format (as known): CPM or CPC for Sponsored Content, CPV for video, cost per send for Sponsored Messaging, CPC or CPM for text ads [Official, 2024] [Unverified] for 2026 changes.

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
| Item | As known | Label | Practice |
|------|----------|-------|----------|
| Campaign daily budget minimum | $10 (USD accounts) | [Unverified] for 2026 | Small budgets learn slowly; consolidate |
| Lifetime budget minimum | $100 | [Unverified] | Use lifetime budgets for fixed flights (events) |
| Campaign group budget | Optional group level budget and schedule | [Unverified] for current behavior | Use to cap programs |
| Daily overspend | LinkedIn can exceed the daily budget on some days while managing to the overall budget | [Unverified] for the exact rule | Pace on weekly or monthly totals |
| Minimum bids | Floors exist by format and audience | [Unverified] | Check suggested ranges |

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
- Track 30 day frequency by campaign (impressions / unique members reached) and CTR by week.
- ABM and retargeting audiences saturate quickly; plan more creative variants and rotate offers rather than raising budget.
- Frequency caps exist for some awareness or reach optimized campaigns [Unverified] for 2026 availability; otherwise control frequency through budget, audience size and creative count.
- Signals of over frequency: CTR falls 30%+ from launch while frequency rises; negative social signals; rising CPC with stable CPM.

Frequency planning rule of thumb [Practitioner consensus]:
| Program | Target 30 day frequency per member |
|---------|-----------------------------------|
| Cold ICP awareness | 2 to 6 |
| ABM tier 1 | 6 to 15 with 4+ creatives rotating |
| Retargeting | 4 to 10 with offer rotation |

## 8. When to raise or cut budget
| Situation | Move |
|-----------|------|
| Cost per qualified lead under target, delivery capped by budget | Raise 15% to 20% per week |
| Cost per qualified lead under target, delivery not capped | Broaden audience or add creative; budget increase will not deliver |
| Cost per qualified lead over target for 30 days with healthy CTR | Lower cap or bid; tighten audience; check form friction and follow up |
| CTR below own baseline by 30% | Creative refresh before budget changes |
| Demand creation campaign with rising engager pools and pipeline influence | Hold budget through at least one sales cycle before judging |

## 9. Common bidding and budget mistakes
| Mistake | Effect | Fix |
|---------|--------|-----|
| Maximum delivery on a 2,000 member ABM list | Very high CPMs | Manual CPM |
| Cost cap set from wishful CPL | No delivery | Cap from observed cost and economics |
| Ten campaigns at $10 per day | No learning | Consolidate |
| Judging awareness spend on leads | Cutting what builds future pipeline | Judge on reach, engagement and later pipeline |
| Changing bids, budget and creative at once | Unreadable results | One change per cycle |
