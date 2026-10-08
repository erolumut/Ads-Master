# Output Templates

Copy paste templates for every orchestrator deliverable. Reviews use the workspace templates in `ads-master/templates/` (WEEKLY_REVIEW.md, MONTHLY_REVIEW.md, CHANGE_REQUEST.md, EXPERIMENT_BRIEF.md, AUDIT_REPORT.md, JOURNAL_ENTRY.md); the templates below add orchestrator specific sections. Save every file as `ads-master/outputs/growth-orchestrator/YYYY-MM-DD_growth-orchestrator_<description>.md`.

Every deliverable opens with the same header:
```
# <Title>
Date: YYYY-MM-DD | Agent: growth-orchestrator | Data: <sources and date ranges> | Currency: <code>
## Summary (5 lines max)
## Data used and gaps
## Decisions and recommendations (numbered; impact, confidence)
```
And closes with:
```
## Change list for approval (see ads-master/templates/CHANGE_REQUEST.md)
## Delegation plan or Handoffs requested
```

---

## 1. Growth diagnosis (`_diagnosis.md`)
```
# Growth Diagnosis: <Project>
## Summary
Binding constraint: <measurement | economics | conversion | creative and offer | demand and reach | capacity>
Evidence: <2 to 3 facts with sources>
Next 30 days: <focus>
## Data used and gaps
| Data | Source | Range | Status |
## Unit economics snapshot
| Metric | Value | Formula or source |
| Contribution margin % | | |
| Breakeven ROAS / CPA | | 1 / CM% ; AOV x CM% |
| nCAC (reconciled) | | |
| LTV (12 months, contribution) | | |
| LTV to CAC | | |
| Payback (months) | | |
## Health score (0 to 5)
| Area | Score | Why |
## Stage and model diagnostics (red flags)
## Agents to activate (HEARTBEAT.md proposal)
| Agent | Active | Cadence | Reason |
## First 5 priorities
## Delegation plan (wave 1)
## Questions for the human (only those that change the plan)
```

## 2. Delegation plan (`_delegation-plan-<workflow>.md`)
```
# Delegation Plan: <workflow> for <project>
Goal: <one sentence> | Gate: <condition before wave 2> | Time box: <sessions or days>
| Step | Wave | Agent (slug) | Parallel or sequential | Inputs | Brief | Output path | Passes to |
|------|------|--------------|------------------------|--------|-------|-------------|-----------|
Synthesis: <who and output path>
Approval gates: <what the human approves and when>
Status log:
| Step | Status (pending, sent, delivered, missing) | Notes |
```

## 3. Channel mix plan (`_channel-mix.md`)
```
# Channel Mix Plan: <Project>, <period>
## Channel roles
| Channel | Role | Status (keep, scale, test, cut) | Budget share | Primary KPI | Guardrail | Evidence |
## Channels to add (tests)
| Channel | Why now | MVB and duration | Success criterion | Measurement design |
## Channels to cut or shrink
| Channel | Evidence | Plan (steps) | What we watch |
## Brand vs performance split
| Bucket | Current | Proposed | Reason |
```

## 4. Budget allocation plan (`_budget-plan-<YYYY-MM>.md`)
```
# Budget Plan: <YYYY-MM>
Total: <amount> (<change vs last month>) | Bucket split: core <x>%, adjacent <y>%, new <z>%
## Allocation
| Channel | Last month | Proposed | Change % | Bucket | Marginal evidence (type, date) | Expected conversions (range) | Risk | Rollback trigger |
## Expected impact
| Metric | Last month actual | Forecast base | Range |
| Spend | | | |
| New customers or SQLs | | | |
| Revenue | | | |
| MER / aMER | | | |
| CM3 | | | |
## Pacing plan
| Week | Planned spend | Seasonality weight | Notes |
## Guardrails
- Brand search floor, retargeting cap, concentration cap, MER floor
```

## 5. Unit economics sheet (`_unit-economics.md`)
```
# Unit Economics: <Project>, as of <date>
## Inputs (with sources)
| Input | Value | Source | Date |
## Derived
| Metric | Value | Formula |
| CM2 per order | | AOV - COGS - shipping - fees - pick and pack - returns |
| Contribution margin % | | CM2 / AOV |
| Breakeven ROAS | | 1 / CM% |
| Target ROAS (profit p) | | 1 / (CM% - p) |
| Breakeven and target CPA | | AOV x CM% ; AOV x (CM% - p) |
| LTV contribution (6, 12 months) | | cohort orders x AOV x CM% |
| Max nCAC (LTV to CAC 3) | | LTV / 3 |
| Max nCAC (payback n months) | | contribution in n months |
| Lead gen: max CPL, max cost per SQL | | see funnel math |
## Channel targets
| Channel | KPI | Target | Derivation | Incrementality factor |
## Sensitivity (CM3 change for +10% in each driver)
```

## 6. Forecast (`_forecast-<period>.md`)
```
# Forecast: <period>
## Assumptions by scenario
| Driver | Conservative | Base | Aggressive | Linked action or risk |
## Forecast
| Month | Scenario | Spend | Conversions | New customers | Revenue | MER | aMER | CM3 |
## Last period accuracy
| Month | Forecast (base) | Actual | Error % | Driver that missed |
MAPE (last 3 months): <x>%
```

## 7. Weekly review additions (on top of WEEKLY_REVIEW.md)
```
## Data used
| Source | Range | Notes (missing, delayed) |
## Cross channel insights
- <pattern seen across agents, with evidence>
## Budget shifts within guardrails (for approval)
| Channel | From | To | Why |
## Conflicts between agents and resolution
| Topic | Agent A says | Agent B says | Decision | Rule applied |
## PRIORITIES.md diff
| Change | Item | Reason |
```

## 8. Monthly review additions (on top of MONTHLY_REVIEW.md)
```
## Marginal returns by channel
| Channel | Spend | Avg CPA | Marginal CPA (method) | Incrementality factor | Incremental marginal CPA | Verdict |
## Geo and macro adjustments
| Market | Inflation or FX change | Target re-base | Tax or fee change |
## Experiment portfolio
| Launched | Concluded | Win rate | Learnings added to memory |
## HEARTBEAT.md changes
```

## 9. Quarterly strategy draft (`_strategy-draft-<YYYY-QN>.md`)
Follows the STRATEGY.md structure so the human can copy it in after approval.
```
# Strategy (DRAFT for approval): <YYYY-QN>
## Quarter
## Primary objective
## Targets
| Goal | Metric | Current | Target | Owner agent |
## Channel roles
| Channel | Role | Budget share | Primary KPI | Guardrail KPI |
## Bets this quarter
1. <bet>: success criterion, read date, owner
## Not doing (deliberately)
## Changes vs last quarter and why
## Test calendar (incrementality, channel tests, big swings)
| Test | Design | Start | Read date | Owner |
```

## 10. Executive one pager (`_exec-summary-<period>.md`)
```
# <Project>: <period> in one page
## Headline
<Revenue / pipeline vs plan, profit after marketing vs plan, one reason>
## Scoreboard
| Metric | Plan | Actual | vs plan | vs last period |
| Revenue or pipeline | | | | |
| Marketing spend | | | | |
| CM3 (profit after marketing) | | | | |
| New customers / SQLs | | | | |
| nCAC | | | | |
| MER | | | | |
## What worked
## What did not
## Decisions needed (max 3, each with recommendation and deadline)
## Next period focus (max 3)
```

## 11. CFO and board section
```
## Finance view
| Item | Budget | Actual | Variance | Note |
| Paid media (platform spend) | | | | |
| Taxes and fees on media (withholding, regulatory fees) | | | | |
| Agency and tools | | | | |
| Total marketing | | | | |
| Contribution after marketing (CM3) | | | | |
| CAC payback (months) | | | | |
| Cash needs next quarter (scenario range) | | | | |
## Risks
| Risk | Probability | Impact | Mitigation |
```

## 12. Growth audit synthesis (`_growth-audit.md`)
```
# Growth Audit: <Project>
## Verdict (three sentences)
## System score (audit-checklist.md)
| Section | Score | Weight | Weighted |
## Binding constraint and evidence
## Channel scorecard (from agent audits)
| Agent | Audit score | Top issue | Marginal CPA at +20% | Headroom |
## Top 10 issues by contribution margin impact
| # | Issue | Evidence (agent output) | Impact estimate | Fix | Effort | Owner |
## Budget reallocation proposal
## 90 day roadmap
| Days 1 to 30 | Days 31 to 60 | Days 61 to 90 |
## Experiments to add (EXPERIMENTS.md rows)
## Conflicts and how they were resolved
## Consolidated change list for approval
```

## 13. Journal entry (decision)
```
# Approved: <decision in five to eight words>
Date: YYYY-MM-DD HH:MM | Agent: growth-orchestrator | Tags: decision
## What happened
## Why it matters
## Data (source and date range)
## Action items
- [ ] <action> (owner: <slug or human>)
## Review date and how we will judge it
## Related files
```

## 14. Writing rules for every deliverable
- Numbers: source and date range on first use; platform vs backend labeled; currency stated; ranges for forecasts.
- Lead with business outcomes, then channels, then tactics.
- One decision per line in decision tables; each with a recommendation.
- No jargon without the formula next to it the first time (MER, aMER, nCAC, POAS).
- In high inflation markets, show real or hard currency columns next to nominal.
