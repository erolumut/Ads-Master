# Optimization Loop and Diagnostics

> Knowledge as of 2026-10. The loop: observe with the right windows, decompose before acting, change one lever at a time, respect learning, log everything.

## 1. Cadence

| Cadence | Time | Checks | Allowed actions (after human approval) |
|---------|------|--------|-----------------------------------------|
| Daily | 5 to 10 min | Spend pacing vs plan, conversions not zero, CPA or ROAS outside guardrails by more than 50%, disapprovals, account alerts, Meta status page incidents | Pause broken ads, fix disapprovals, emergency budget cuts |
| Every 3 days | 15 min | New ads spend share, early kill candidates, frequency on top ads | Turn off clear losers, small budget moves |
| Weekly | 45 to 90 min | KPI vs target, creative performance by concept, fatigue, audience segment mix, learning status, Opportunity Score recommendations, experiment reads | Budget shifts, new concepts launch, bid goal steps, value rule changes |
| Monthly | 2 to 3 hours | Structure review, creative coverage grid, attribution and backend reconciliation, MER and new customer CAC, policy and account health, freshness check | Structure changes, test roadmap, budget plan |
| Quarterly | half day | Full audit (audit-checklist), incrementality test, strategy reset with `growth-orchestrator` | Major changes |

Data windows: judge CPA and ROAS on 7-day rolling at minimum; 14 to 28 days for low-volume accounts. Never judge on today's numbers (attribution still filling in, especially view and 7-day click windows).

## 2. Learning phase rules

- Learning: the ad set is exploring; performance is less stable. Exits after about 50 optimization events within 7 days of the last significant edit [Official].
- Learning limited: Meta predicts the ad set will not reach the threshold. Fixes in order: consolidate ad sets, raise budget toward 7 x CPA per day, move optimization one funnel step up, widen audience or placements, reduce bid constraints.
- Significant edits [Official]: targeting change, creative change (including adding a new ad), optimization event change, pausing 7+ days, bid strategy change, large budget or bid changes.
- Batch edits: make all planned changes in one session, once per week per ad set, rather than daily tweaks.
- Do not judge performance during learning unless spend exceeds 3 x target CPA with no conversions.

## 3. The breakdown effect (must understand before acting on breakdowns)

[Official, long-standing] Meta's system allocates spend to get the most results at the lowest marginal cost across the whole ad set. A segment (placement, age, gender, region) with a higher average CPA in a breakdown may still be where the cheapest next results come from, and a segment with low average CPA may be saturated. Cutting the "expensive" segment often raises total CPA.

Rules:
1. Do not exclude placements, ages or regions based on Ads Manager breakdown CPA alone.
2. Only act on segment differences when backed by downstream value data (CRM close rate, LTV, return rate) that Meta cannot see. Then use value rules (price), not exclusions (block).
3. If you must test an exclusion, run an A/B test (with vs without) and judge on total CPA.

## 4. Auction overlap

[Official] When ad sets from the same account are eligible for the same auction, Meta enters only the one with the highest total value, and the others lose delivery. Check: Delivery Insights or the "Auction overlap" signal in Ads Manager (labels vary). Fixes: consolidate overlapping ad sets, move concepts into one ad set, or separate by hard controls (geo).

## 5. Frequency and fatigue

| Campaign type | Warning zone (7-day frequency) | Note |
|---------------|-------------------------------|------|
| Cold acquisition, broad | above 2.5 to 3.5 | Check CTR and CPA trend before acting |
| Retargeting | above 6 to 10 | Small audiences saturate quickly |
| Awareness / reach | per plan, use frequency caps in Reach and frequency | |
[Practitioner consensus]. Frequency alone is not a problem; frequency plus declining CTR and rising CPA is fatigue. Response: add new concepts, broaden reach (geo, placements), or reduce budget. See creative module section 9.

## 6. Performance decomposition (do this before any diagnosis)

```
CPA  = CPM / (1000 x CTR_link x CVR)
ROAS = (CTR_link x CVR x AOV x 1000) / CPM
```
Compare last 7 days vs prior 7 (and vs same period last year for seasonality). Identify which term moved:

| Term moved | Look at | Typical causes |
|-----------|---------|----------------|
| CPM up | Auction seasonality, audience size, placement mix, ad quality ranking, new competitors | Q4 and BFCM, narrow audiences, low quality creative, policy limited delivery |
| CTR down | Creative fatigue, frequency, hook rate, placement mix shift | Same concepts too long, new placements (Audience Network, Threads) |
| CVR down | Landing page, price, stock, checkout, offer end, site speed, tracking | Site changes, OOS products, payment issues, attribution change |
| AOV down | Product mix, discounting | Promo, catalog shifts |

## 7. Diagnostic trees

### 7.1 CPA up or ROAS down (7 days)
1. Tracking: are backend orders also down? If backend is stable and only Meta dropped, check Events Manager, dedup, attribution date changes. Hand off to `measurement` if broken.
2. External: Meta status page incident, holiday, competitor sale, news event, seasonality (Q4 CPM rise), site outage.
3. Changes: anything edited in the last 14 days (journal and Ads Manager activity history). Learning resets?
4. Decompose (section 6). Fix the moving term:
   - CPM: broaden, refresh creative, check ad relevance diagnostics, check placement shifts.
   - CTR: new concepts, new hooks, format change.
   - CVR: hand off to `cro` with landing page evidence; check offer and stock.
5. If nothing found and the drop is within normal variance (compare 8-week standard deviation), wait 3 to 7 days.

### 7.2 Spend not delivering (underspend)
| Cause | Check | Fix |
|------|-------|-----|
| Cost per result goal or ROAS goal too tight | Spend vs budget, goal vs trailing CPA | Loosen goal 10 to 20% |
| Bid cap too low | Auction win rate | Raise cap |
| Audience too narrow | Audience definition, controls | Broaden, Advantage+ audience |
| Ads rejected or limited | Ad status, Account Quality | Fix policy issues |
| Learning limited | Learning status | Consolidate |
| Payment issue or spending limit | Billing | Fix payment |
| Low quality ranking | Ad relevance diagnostics | New creative |

### 7.3 New ads get no spend
- Meta favors incumbents with history. Options: use the creative testing tool, put new concepts in a new ad set with its own budget for a test window, or pause the weakest incumbents to make room. Do not duplicate the incumbent ad set.

### 7.4 Lead volume fine, quality poor
See [lead-gen-and-messaging](lead-gen-and-messaging.md): switch form to higher intent, add qualifying questions, optimize to conversion leads, add placement value rules on low quality placements, review creative promise.

### 7.5 Sudden account-wide collapse
1. Account Quality (Business Support Home) for restrictions.
2. Payment method failed.
3. Dataset or domain issue.
4. Meta delivery incident (metastatus.com).
5. Policy sweep (many ads disapproved).
Go to the recovery play in [playbooks](playbooks.md).

## 8. Ad relevance diagnostics

Quality ranking, engagement rate ranking and conversion rate ranking compare the ad to ads competing for the same audience [Official]. Read only for ads with 500+ impressions. Below average in quality ranking points to creative or perceived low quality (clickbait, engagement bait, withheld information). Below average conversion rate ranking with good engagement points to landing page or offer.

## 9. Opportunity Score and recommendations

Opportunity Score (0 to 100) reflects how many Ads Manager recommendations you applied, weighted by Meta's estimate of impact; dismissing recommendations lowers it; Meta reported a median 12% lower cost per result for advertisers adopting recommendations [Official, 2024 to 2025]. It measures alignment with Meta best practices, not performance.

| Recommendation type | Default response |
|--------------------|------------------|
| Consolidate fragmented ad sets, fix learning limited | Usually accept |
| Turn on Advantage+ audience or placements | Accept unless legal or brand reason |
| Add Conversions API, improve EMQ | Accept |
| Raise budget | Evaluate marginal CPA first |
| Loosen cost per result goal or ROAS goal | Evaluate against unit economics |
| Turn on creative enhancements | Review brand risk |
| Duplicate or "add more creative" | Accept only with distinct concepts |
Record dismissals with reasons in the weekly report so reviewers know the score is not a KPI.

## 10. Weekly optimization report (template)

```
# Meta weekly review, week of YYYY-MM-DD
Data: Ads Manager export / API, date range, attribution setting. Backend source and range.
## Scorecard
| KPI | This week | Last week | 4-week avg | Target | Status |
(Spend, Results, CPA, ROAS, MER contribution, New customer %, CPM, CTR link, CVR, Frequency)
## What changed and why (decomposition)
## Creative: top 5 concepts, fatigue list, new concepts launched, kills
## Tests: running, finished (result, learning), next
## Recommendations (change list for approval)
| # | Change | Level | Reason | Expected impact | Risk | Reversible? |
## Risks and alerts
## Handoffs requested
```
Save to ads-master/outputs/meta-ads/YYYY-MM-DD_meta-ads_weekly-review.md.
