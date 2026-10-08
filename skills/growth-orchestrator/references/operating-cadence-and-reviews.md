# Operating Cadence and Reviews

The rhythm that turns agents into a team: what happens daily, weekly, monthly, quarterly and annually, who does it, and what the orchestrator writes. The `ads-review` skill runs the cycle; this module defines the orchestrator's part and the standards.

## 1. Rhythm overview
| Cadence | Trigger | Conductor action | Orchestrator deliverable | Time box |
|---------|---------|------------------|--------------------------|----------|
| Daily | `/ads-review daily` or schedule | Fan out exception checks to active paid agents | None unless exceptions; then a journal alert | 5 to 10 min |
| Weekly | `/ads-review weekly` | Fan out weekly reviews, run blocking handoffs | `_weekly-review.md`, PRIORITIES.md | 30 to 60 min |
| Monthly | `/ads-review monthly` | Weekly flow + freshness checks + market-intel + measurement reconciliation | `_monthly-review.md`, budget plan, forecast | 1 to 2 h |
| Quarterly | `/ads-review quarterly` | Full audits, landscape refresh, test plan | `_strategy-draft-<YYYY-QN>.md`, HEARTBEAT.md update | half day |
| Annual | Human request | Budget envelope, brand split, geo plan | `_annual-plan-<YYYY>.md` | 1 day |

## 2. Daily (exceptions only)
Thresholds (defaults; tune per project in memory once confirmed):
| Check | Amber | Red |
|-------|-------|-----|
| Pacing vs plan (month to date) | outside 90 to 110% | outside 80 to 120% |
| Conversions vs 7 day average | minus 30% | minus 50% or zero |
| CPA or ROAS vs 7 day average (meaningful volume) | 20% worse | 30% worse |
| Disapprovals or policy flags | any on non core ads | any on core campaigns or account level |
| Budget limited campaigns at or better than target | present | present for 3+ days |
| Platform vs backend gap (yesterday) | over 25% | over 50% |
Rule: a red tracking item routes to measurement immediately (Tracking break workflow).

## 3. Weekly (the learning loop)
### 3.1 Sequence
1. Specialists deliver weekly reviews (ads-review brief) in parallel.
2. Conductor runs blocking handoffs (usually measurement).
3. Orchestrator synthesis using `ads-master/templates/WEEKLY_REVIEW.md`:
   - Headline: how the business did and why (2 sentences).
   - Business KPIs from backend: revenue or pipeline, MER, nCAC, new customers or SQLs, CM3 if available.
   - Channel scorecard from each agent with green, amber, red.
   - Organic and AI visibility lines.
   - Experiments closed, launched, decisions.
   - Learnings worth keeping (candidates for memory).
   - Decisions for the human with a recommendation each.
   - Priorities for next week (max 5).
4. Update PRIORITIES.md. Write the journal entry.

### 3.2 Status rules for the scorecard
| Status | Rule |
|--------|------|
| Green | Primary KPI at or better than target and trend stable or improving |
| Amber | Within 15% of target, or at target with a deteriorating 4 week trend |
| Red | More than 15% worse than target, or a guardrail broken (tracking, policy, pacing) |

### 3.3 PRIORITIES.md rules
- Max 5 rows. Each row: priority, owner agent, expected impact (metric and size), status.
- Score candidates with ICE (experiment-program.md). Ties go to the item that unblocks others (measurement, feed, site).
- Each priority traces to the quarterly goal in STRATEGY.md. If it does not, park it.
- "Parked" lists items with the reason. "Decisions waiting on the human" lists each decision with a deadline.
- A priority that stays "in progress" for 3 weeks gets split or escalated.

Template (fills the existing file):
```
## Week of YYYY-MM-DD
| # | Priority | Agent | Expected impact | Status |
|---|----------|-------|-----------------|--------|
| 1 | Fix purchase event dedup (CAPI + pixel) | measurement | Restores Meta optimization signal; CPA minus 10 to 20% expected | in progress |
| 2 | Launch 6 new concepts from VoC angles | creative-strategy, meta-ads | Lower fatigue; CPA minus 10% | waiting approval |
| 3 | Move $3k from retargeting to TikTok test | growth-orchestrator, tiktok-ads | nCAC flat, +60 new customers | waiting approval |
## Parked
- Pinterest test (reason: creative capacity; revisit 2026-12)
## Decisions waiting on the human
- Approve Q4 budget plan (deadline 2026-10-15)
```

## 4. Monthly
Adds to weekly:
| Item | Owner | Output |
|------|-------|--------|
| Budget reallocation on marginal returns | growth-orchestrator | Proposal table in MONTHLY_REVIEW.md + CHANGE_REQUEST.md |
| Unit economics update (CM, nCAC, LTV to CAC, payback) | growth-orchestrator | MONTHLY_REVIEW.md table |
| Forecast next month (3 scenarios) and accuracy of last month | growth-orchestrator | Forecast table, MAPE |
| Platform changes in the last 30 days | every agent (Freshness Protocol) | "Platform changes this month" table |
| Creative refresh plan | creative-strategy | Concept slate |
| SEO and AI visibility report | seo, ai-search-optimization | Monthly reports |
| Measurement reconciliation | measurement | Platform vs backend by channel |
| Competitor movement | market-intel | Monthly movement summary |
| HEARTBEAT.md review | growth-orchestrator | Activate or deactivate agents |

## 5. Quarterly strategy reset
1. Full audits from every active agent (their audit-checklist.md) and the growth system audit (audit-checklist.md here).
2. market-intel landscape refresh; measurement incrementality and MMM plan.
3. Orchestrator drafts STRATEGY.md for approval:
   - One primary objective and its metric.
   - Targets table with owner agent.
   - Channel roles with budget share, primary KPI and guardrail KPI.
   - 3 bets for the quarter with success criteria.
   - Not doing (deliberately), with reasons.
4. HEARTBEAT.md: active agents and cadences for the quarter.
5. Test calendar: at least one incrementality test on the largest line item per half year.

STRATEGY.md drafting rules: write it as a draft file in outputs first; the human approves; only then does the main session copy it into `ads-master/STRATEGY.md`.

## 6. HEARTBEAT.md maintenance
- Active column: yes or no per agent, from activation rules in SKILL.md and the diagnosis.
- Cadence column: daily alerts only for paid agents with spend over about $100 per day; weekly for all active; monthly for market-intel and ai-search-optimization at minimum.
- Notes: the reason for activation or deactivation and the date.
- Scheduling options to suggest (the human chooses): `/loop` in a session, a Claude Code Routine or scheduled trigger, a CI job running Claude Code headless that commits outputs to a branch, or a cron on a workstation.

## 7. Decision log
Every approved or rejected recommendation gets a journal entry tagged `decision`: what was decided, by whom, the evidence, the expected impact and the review date. At the review date, the orchestrator checks the outcome and writes a `learning` entry. Repeated confirmed outcomes go to memory.

## 8. Stakeholder reporting
| Audience | What they need | Format | Frequency |
|----------|----------------|--------|-----------|
| Founder or CEO | Revenue, profit after marketing, growth vs plan, the 3 decisions needed | Executive one pager (output-templates.md) | Weekly or monthly |
| CFO or finance | Spend vs budget, CM3, nCAC, payback, forecast with scenarios, cash needs | Monthly review finance section | Monthly |
| Board | Quarter results vs plan, unit economics trend, strategy changes, risks | Quarterly summary | Quarterly |
| Channel owners or agencies | Channel scorecard, targets, change approvals | Agent outputs + change lists | Weekly |
| Sales (lead gen, B2B) | Lead volume and quality by source, SQL rates, feedback loop | Pipeline section | Weekly |

Reporting rules:
- Lead with business outcomes (revenue, profit, customers), then channels.
- Show platform and backend numbers side by side when they differ, labeled.
- Always include the comparison base (target, last period, same period last year).
- One page first; appendices for detail.
- In high inflation markets, add real (CPI adjusted) or hard currency views next to nominal local currency numbers.

## 9. KPI tree (use to structure reviews)
```
Contribution after marketing (CM3)
  = Net revenue x CM% - marketing spend
Net revenue
  = New customer revenue + Returning revenue
New customer revenue
  = New customers x first order AOV
New customers
  = Paid new customers (spend / nCAC) + Organic and AI new customers + Referral
Returning revenue
  = Active customers x repeat rate x repeat AOV
```
Each node has an owner agent. Reviews walk the tree top down and stop at the first node that explains most of the variance.

## 10. Anti patterns
- Reviews that list metrics without decisions.
- More than 5 priorities, or priorities without owners.
- Changing targets every week (targets change quarterly unless economics change).
- Reporting platform ROAS to the CEO without backend reconciliation.
- Skipping the monthly freshness check: platform changes (for example a default setting switching to automated) silently move results.
