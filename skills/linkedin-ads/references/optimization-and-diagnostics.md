# Optimization and Diagnostics

> Scope: the weekly optimization routine, reports to pull, diagnostic trees for common LinkedIn failures, creative and audience optimization, testing rules and change discipline.

## 1. Weekly routine (60 to 90 minutes at Growth tier)

| Step | Where | Check | Action |
|------|-------|-------|--------|
| 1 | Campaign performance, last 7 and 28 days | Spend, results, cost per result vs target, pacing | Flag campaigns 20%+ off target |
| 2 | Ad level performance | CTR, engagement rate, cost per result, impressions share per ad | Pause clear losers after enough impressions; queue refresh |
| 3 | Frequency and reach | 30 day frequency and reach by campaign | Refresh or widen when CTR decays |
| 4 | Lead gen forms | Opens, submissions, completion rate | Investigate drops (form length, mobile) |
| 5 | CRM (weekly snapshot) | New leads by campaign, early qualification notes | Share with sales; note quality signals |
| 6 | Demographics report (every 2 weeks) | ICP match by seniority, function, company size | Exclusions or audience edits |
| 7 | Company engagement (ABM, weekly) | Engaged accounts, changes | Send list to sales |
| 8 | Tests | Status of A/B tests | Read or extend |
| 9 | Change log | What changed last week | Avoid stacking changes |

## 2. Reports to export (save to `ads-master/data/imports/`)
| Report | Breakdown | Range | Use |
|--------|-----------|-------|-----|
| Campaign performance | Campaign, day | 90 days | Trends, pacing |
| Ad performance | Ad, week | 90 days | Creative decisions |
| Demographics | Job title, function, seniority, company size, industry, company | 30 and 90 days | ICP match |
| Lead gen form report | Form, campaign | 90 days | Completion rates |
| Conversions | Conversion rule, campaign, click vs view | 90 days | Attribution reading |
| Company engagement | Company, list | 30 and 90 days | ABM |
| CRM export | Lead, source fields, stage, reason, opportunity value | 180 days | Quality and pipeline |
Name files `YYYY-MM-DD_linkedin_<report>.csv` and state the range in deliverables.

## 3. Diagnostic trees

### 3.1 Campaign not delivering
```
Ad status approved?            no  -> fix rejection reason, resubmit
Payment method valid?          no  -> billing
Audience size above 300 and realistic for the format?  no -> widen attributes or merge audiences
Bidding: Manual or Cost cap below suggested range?     yes -> raise 10% to 15%, or switch to Maximum delivery to learn
Budget too low for the bid (daily budget under a few clicks)? yes -> consolidate budgets
Start and end dates, campaign group status active?     no -> fix schedule
Creative CTR far below baseline (relevance)?           yes -> new creative
```

### 3.2 Cost per lead rising 30%+ for 2 weeks
```
CPM up?   yes -> competition or audience saturation; check frequency, widen audience, lower cap only if delivery holds
CTR down? yes -> fatigue; refresh creative and angle
Form open rate stable but completion down? yes -> form friction, mobile issue, new question added
Changes in last 14 days? yes -> revert or wait out learning
Seasonality (holidays, quarter end)? yes -> compare same period last year; adjust expectations
```

### 3.3 Leads fine, SQL rate falling
```
Audience expansion or Audience Network turned on? yes -> turn off, compare
Demographics report shows off ICP seniority or company size? yes -> exclusions, tighten
Offer shifted to lower intent content? yes -> move gated content to retargeting, add qualifying question
Sales follow up slower than SLA? yes -> fix routing before ad changes
Specific ad or audience code dominates disqualified leads? yes -> pause or rework that segment
```

### 3.4 Conversions dropped to zero
```
Insight Tag active? no -> site change removed it: hand off to measurement (P1)
Conversion rule status active and attached to campaigns? no -> fix
Consent banner change reducing tag firing? check consent rate
CAPI pipeline errors? check integration logs, token expiry
Lead gen form leads still arriving? if yes, problem is website conversions only
```

### 3.5 ABM accounts not engaging
```
Company list match rate under 60%? yes -> add domains and LinkedIn URLs, clean names
Tier 1 accounts with zero impressions? yes -> Manual CPM bid up, check role layer is not too narrow
Creative generic? yes -> industry or account specific versions
Budget per account too thin? compute spend / accounts; concentrate on fewer accounts
```

### 3.6 Spend concentrated on one ad
- LinkedIn delivery favors early leaders. If the test needs equal exposure, use A/B testing or separate campaigns; otherwise accept and refresh losers.

## 4. Audience optimization rules
- Review Demographics every 2 weeks. If any seniority or function outside the ICP takes over 15% of impressions, exclude it or tighten.
- Do not narrow below the size needed for delivery; prefer exclusions of clear non buyers over adding more AND layers.
- When an audience saturates (frequency rising, CTR falling, reach flat), add adjacent roles, regions or company sizes as a new campaign rather than inflating budget.
- Refresh matched audiences monthly (company and contact lists) and keep customer exclusions current.

## 5. Creative optimization rules
- Screen creative on CTR and engagement after about 1,000 to 2,000 impressions per ad [Practitioner consensus]; decide on cost per qualified result once volume allows.
- Keep 2 to 4 active ads per campaign; replace the weakest every 2 to 4 weeks in small audiences.
- Reuse winning angles across formats (document, video, Thought Leader post) rather than tweaking colors.
- Log winning angles in memory only after they win in two audiences or two periods.

## 6. Testing rules
| Rule | Standard |
|------|----------|
| One variable | Creative angle, format, offer, audience, or bidding, never several |
| Duration | At least 2 weeks for creative screens; 4+ weeks for lead quality tests |
| Size | 30+ results per arm for conversion metrics; otherwise treat as directional |
| Decision metric | Cost per qualified lead or pipeline when available |
| Logging | Row in `ads-master/EXPERIMENTS.md` before launch |

High value test backlog:
1. Thought Leader Ads vs company page ads with the same message.
2. Gated document (lead form) vs ungated document plus retargeting to a lead form.
3. Lead gen form with qualifying question vs without.
4. Higher intent form option vs standard.
5. Job titles vs function plus seniority audience.
6. Maximum delivery vs Cost cap at the same budget.
7. Accelerate campaign vs best classic campaign.
8. Conversation ad vs single image ad for demo requests to retargeting audiences.
9. Audience expansion on vs off (expect cheaper leads, check SQL rate).
10. Account holdout test for ABM influence.

## 7. Change discipline
- One meaningful change per campaign per 7 to 14 days.
- Every change goes into the weekly deliverable change list with approval status.
- Keep a simple change log in the journal for audits and diagnosis.
