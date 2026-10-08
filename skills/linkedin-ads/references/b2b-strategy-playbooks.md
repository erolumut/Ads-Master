# B2B Strategy and Playbooks

> Scope: the strategic frame for LinkedIn in B2B (95 to 5 rule, buying committees, demand creation vs demand capture, lead quality vs volume, sales and marketing alignment) and step by step plays for launch, ABM, demand creation, lead quality recovery, scaling, recovery and events.

## 1. The 95 to 5 rule
- Source: John Dawes (Ehrenberg-Bass Institute) for the LinkedIn B2B Institute, "Advertising effectiveness and the 95-5 rule" [Study, 2021].
- Logic: if a business buys a solution about every 5 years, roughly 20% of buyers are in market in a year and about 5% in a quarter; about 95% are out of market at any time.
- Implication: ads that only harvest in market buyers address a small pool; advertising also has to build memory among the 95% so the brand is considered when they enter the market.
- Practical use in budgets: protect a demand creation share (see [Bidding](bidding-and-budgets.md) section 5), measured on reach in the ICP, engagement, branded search and later pipeline, not same week leads.

Estimate your in market share:
```
in market share per quarter ≈ 1 / (average years between purchases x 4)
example: 4 year replacement cycle -> 1 / 16 ≈ 6% of ICP accounts in market per quarter
```
Use the number to set expectations: a lead capture campaign to the full ICP can only harvest that share.

## 2. Brand and activation balance
Les Binet and Peter Field's B2B analysis for the LinkedIn B2B Institute ("The 5 Principles of Growth in B2B Marketing") argued that B2B brands need substantial brand building alongside activation, with an indicative split near half brand [Study, 2019]. Treat as a starting hypothesis for mature categories; early stage companies with tiny ICPs often run more activation and ABM.

## 3. Buying committee
- B2B purchases involve several stakeholders; widely cited research puts buying groups at 6 to 10 people [Study, Gartner, as widely cited].
- Implication: reaching one contact per account is not enough. Map roles (economic buyer, champion, users, technical evaluator, procurement) and plan coverage (see [Targeting and ABM](targeting-and-abm.md) section 3).
- KPI: roles reached per priority account; contacts engaged per opportunity in the CRM.

## 4. Demand creation vs demand capture
| Dimension | Demand creation | Demand capture |
|-----------|----------------|----------------|
| Audience | Whole ICP, mostly out of market | In market signals (retargeting, engaged accounts, intent) |
| Offer | Insight, perspective, education (ungated) | Demo, trial, assessment, pricing |
| Formats | Thought Leader Ads, video, documents, events | Lead gen forms, conversation ads, single image retargeting |
| KPIs | ICP reach, engagement, engager pool growth, branded search, pipeline influence over 60 to 180 days | Cost per qualified lead, pipeline per dollar |
| Time horizon | Quarters | Weeks |
LinkedIn is unusually strong at creation because of professional targeting; search (google-ads, microsoft-ads) is usually stronger at capture. Coordinate through growth-orchestrator.

## 5. Lead quality vs volume
- Gated content at low CPL often yields low SQL rates. Volume without quality wastes sales time.
- Decide with sales which outcome matters this quarter. If sales capacity is the constraint, choose quality levers (qualifying questions, higher intent forms, stricter audiences).
- Report both: leads and cost per qualified lead; never celebrate CPL alone.

## 6. Sales and marketing alignment (operating agreement)
| Item | Agreement |
|------|-----------|
| Definitions | MQL, SQL, opportunity criteria written and shared |
| Routing | Which leads go to SDRs vs nurture, by form answer and score |
| SLA | Follow up time by lead type (for example 1 business hour for demo requests) |
| Feedback | Disqualification reasons logged in CRM with a picklist |
| Meeting | Monthly lead quality review with sales leader |
| ABM | Shared account list, tiers, weekly engaged account report |
Store the agreement in MEASUREMENT.md (via measurement agent) and reference it in deliverables.

## 7. Plays

### Play 1. Launch (days 0 to 90)
| Phase | Steps |
|-------|-------|
| Days 0 to 7 | Intake; Business Manager and ad account ownership; Insight Tag and conversion rules; CRM sync test; qualified lead definition; exclusion lists; audience plan with sizes |
| Days 7 to 14 | Launch Starter or Growth structure (see [Account structure](account-structure-and-objectives.md)); Audience expansion and Network off; 2 to 4 ads per campaign |
| Days 14 to 21 | Demographics report check; exclusions; first creative read (CTR, engagement) |
| Days 21 to 45 | Lead quality review with sales; form tweaks; retargeting ladder live |
| Days 45 to 90 | Move to Cost cap where cost is known; first A/B test; monthly pipeline report; decide scale or fix |
Exit: 90 day report with cost per SQL, pipeline per dollar, ICP match and next quarter plan.

### Play 2. ABM program
1. Account tiers with sales; upload company lists per tier.
2. Role layers per tier; Manual CPM bidding for tier 1.
3. Air cover: Thought Leader Ads and video to tiers 1 to 3.
4. Engaged account retargeting with case studies and events.
5. Conversion offers to engaged accounts; conversation ads from a named sender.
6. Weekly engaged account list to sales; sales plays logged.
7. Quarterly: account holdout analysis and pipeline from target accounts.

### Play 3. Demand creation engine
1. Pick 2 to 5 voices for Thought Leader Ads and 1 flagship content asset per quarter (benchmark report, framework).
2. Cut the asset into document ads, short videos and posts.
3. Run Engagement or Brand awareness to the ICP; build engager audiences (video 50%+, document readers, post engagers).
4. Retarget engagers with deeper content, then with conversion offers.
5. Track monthly: ICP reach, engager pool size, branded search trend (from google-ads and microsoft-ads), pipeline from engagers.

### Play 4. Lead quality recovery
Entry: sales reports poor leads or SQL rate fell 30%+.
1. Pull CRM stages and disqualification reasons by campaign, audience and offer (see [Lead gen forms](lead-gen-forms-and-crm.md) section 6).
2. Turn off Audience expansion and Audience Network if on.
3. Check Demographics report for off ICP impressions; add exclusions.
4. Add a qualifying question or switch to the higher intent form option.
5. Replace low intent offers to cold audiences with ungated content; keep gated offers for retargeting.
6. Fix follow up speed and routing with sales.
7. Re-measure after 30 days.

### Play 5. Scale
Entry: cost per SQL at or below target for 6+ weeks.
1. Raise budget 15% to 20% per week on capped campaigns.
2. Add adjacent roles and regions as separate campaigns.
3. Test predictive audiences seeded from SQLs or closed won contacts [Unverified] for seed rules.
4. Test Accelerate campaigns against the best classic campaign.
5. Expand demand creation (video, BrandLink or CTV where available) with a lift test.
Stop rule: if cost per SQL rises 20% above target for 2 weeks after a step, revert the step.

### Play 6. Recover (performance collapse)
1. Freeze changes; check spend pacing, rejected ads, tag and sync status.
2. Check change history: audience edits, bid changes, budget edits, new campaigns overlapping audiences.
3. Check creative fatigue (CTR trend, frequency).
4. Check seasonality (holidays, fiscal year ends) and competitor activity in the LinkedIn Ad Library.
5. Fix the root cause; journal it; memory entry if repeated.

### Play 7. Webinar or event promotion
| When | Action |
|------|--------|
| 4 to 6 weeks before | LinkedIn Event page; event ads to ICP; Thought Leader posts from speakers |
| 2 to 4 weeks before | Retarget engagers; conversation ads to tier 1 accounts |
| Final week | Reminder ads to registrants' companies; message ads to warm lists where allowed |
| After | Retarget attendees and registrants with replay and next step offer; sync attendance to CRM |
KPI: cost per attendee from ICP, pipeline from attendees within 90 days.

## 8. Monthly pipeline report template
```
# LinkedIn Ads monthly report: <month>
Data: Campaign Manager export <range>, CRM report <range>
| Program | Spend | Leads | SQLs | Cost per SQL | Opps | Pipeline | Pipeline per $ | ICP match |
## Demand creation: reach in ICP, engager pool, branded search trend
## ABM: accounts reached %, engaged accounts, opportunities in target accounts
## Lead quality: SQL rate by campaign, top disqualification reasons
## Tests: status and results (EXPERIMENTS.md IDs)
## Next month: changes for approval
## Handoffs requested
```
