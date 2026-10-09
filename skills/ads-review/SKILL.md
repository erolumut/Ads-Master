---
name: ads-review
description: Run the Ads Master operating rhythm (the heartbeat) for the current project. Modes are daily (the daily report with spend vs plan, platform reported vs backend observed, acquisition investment, stock, tracking and policy alerts), weekly (every active agent scores KPIs, closes experiments and proposes changes, then a cross channel review and priorities), monthly (budget reallocation, platform change check, SEO and AI visibility report) and quarterly (strategy reset and test plan). Use when the user asks to run the daily check, weekly review, monthly report, heartbeat, status update or "how are we doing" across marketing channels.
---

# Ads Review (the heartbeat)

The main session runs this skill as the conductor. It fans out to the active specialist agents, then synthesizes. Default mode is `weekly` when no argument is given.

## Preconditions
- `ads-master/` exists. If not, run the `ads-setup` skill first.
- Read `ads-master/HEARTBEAT.md` (active agents), `STRATEGY.md`, `PRIORITIES.md`, `EXPERIMENTS.md`, `MEASUREMENT.md` and journal entries since the last review.
- Check data freshness: list files in `ads-master/data/imports/` newer than the last review, and which connectors are available. If a channel has no data for the period, say so and do not guess.

## Mode: daily (the daily report, 5 to 10 minutes)
Goal: numbers every day, decisions on 3 and 7 day windows. One bad day is not a trend; incidents are the exception.

1. **Data.** Pull yesterday, last 3 days and last 7 days from connectors or the newest exports in `ads-master/data/imports/`. If the measurement package's `scripts/daily_report.py` is available, run it on the platform spend CSV and the backend orders CSV; otherwise compute the same metrics by hand. Definitions come from `ads-master/METRICS.md`.
2. **Fan out (parallel, only active paid channel agents plus measurement):**
   > Daily check for <project>. Report only exceptions on 3 and 7 day windows: spend pacing more than 20 percent off plan or above the caps in GUARDRAILS.md, conversions at zero or more than 50 percent below the 7 day average, CPA or ROAS more than 30 percent worse than the 7 day average on meaningful volume, disapprovals or policy issues, budget limited profitable campaigns, tracking anomalies, advertised items sold out or below stock cover. No changes. If nothing is wrong, reply "No exceptions".
3. **Write the report** to `ads-master/outputs/growth-orchestrator/<date>_growth-orchestrator_daily-report.md`:
   - **FACTS:** spend yesterday and month to date vs ceiling; orders or leads (backend observed); revenue; new customers; AOV; platform reported conversions and value next to backend observed (never hide the gap); blended CAC and nCAC; acquisition investment and blended first order acquisition cost when offers subsidize; product or bundle mix; best and worst creative by ID; stock cover of advertised items.
   - **INTERPRETATION:** what changed and the most likely reason, with a confidence level (low, medium, high).
   - **RECOMMENDATION:** one action or "no change", with the decision window it is based on. Status green, amber or red against the target logic in STRATEGY.md.
4. **Alert queue.** Keep open exceptions in `ads-master/logs/alerts.csv` with one row per rule and entity: `rule,entity,alert_from,last_seen,status,ack_by,note`. `alert_from` is the date the condition started. A condition that is still true updates `last_seen` instead of adding a row, so an acknowledged alert stays acknowledged and the queue can reach zero. Close a row when the condition clears. The report lists new rows first, then open unacknowledged rows.
5. **Incidents:** if a stop condition from `ads-master/INCIDENTS.md` appears, put it at the top, delegate to `measurement` (tracking), `site-engineer` (site), `commerce-feeds` or `offer-strategy` (stock, price), `compliance` (claims) immediately, and log it.
6. Write a journal entry only when there are exceptions or a decision.

## Mode: weekly (the learning loop)
1. **Fan out.** Delegate to every active specialist in parallel (paid channels, mobile-app-growth, seo, ai-search-optimization, cro, storefront-ux, site-engineer, commerce-feeds, creative-strategy, video-studio, offer-strategy, lifecycle-crm, measurement; compliance reviews anything due to publish). Brief for each:
   > Weekly review for <project>, week of <date>. Follow the weekly Cadence section of your skill. Use data from <sources and date range>. Deliver: (1) KPI scorecard vs targets in STRATEGY.md and your memory baselines, (2) wins and misses with the evidence, (3) experiments to close or launch (update EXPERIMENTS.md rows you own), (4) a change list for approval using ads-master/templates/CHANGE_REQUEST.md, (5) memory updates only for confirmed patterns, (6) a journal entry. Save to ads-master/outputs/<slug>/<date>_<slug>_weekly-review.md. End with "Handoffs requested" if you need another agent.
2. **Execute handoffs.** Collect each response. Review the risk register in `ads-master/INCIDENTS.md`: check each early warning against this week's data, update Last reviewed, and turn any fired risk into an incident row. Run any requested handoffs that are needed before the synthesis (for example a tracking fix).
3. **Synthesize.** Delegate to the `growth-orchestrator` agent (or follow the growth-orchestrator skill in this session) to write `ads-master/outputs/growth-orchestrator/<date>_growth-orchestrator_weekly-review.md` using `ads-master/templates/WEEKLY_REVIEW.md`: business KPIs, channel scorecard, cross channel insights, budget shifts within guardrails, experiment decisions, and an updated `PRIORITIES.md` (max 5 items).
4. **Present to the human.** A short summary: the headline, red items, decisions needed (with a recommendation each), and the consolidated change list. Nothing is executed until approved.

## Mode: monthly
Everything in weekly, plus:
- `growth-orchestrator`: budget reallocation proposal based on marginal returns, unit economics update, forecast for next month, `MONTHLY_REVIEW.md` template.
- Every agent: run its Freshness Protocol and report platform changes from the last 30 days that affect this project.
- `seo` and `ai-search-optimization`: monthly visibility reports.
- `creative-strategy`: creative refresh plan based on fatigue and concept performance.
- `measurement`: tracking health audit and reconciliation of platform conversions vs source of truth.
- `market-intel`: competitor movement summary (new offers, ads, rankings, AI recommendations).
- `lifecycle-crm`: cohort repeat rates (30, 45, 60, 90 days), flow revenue and list health.
- `offer-strategy`: offer and bundle performance, promo calendar for next month, price consistency across channels and retail.
- `compliance`: claims registry review (expired evidence, new claims found in live copy).
- `storefront-ux`: conformance audit delta on the top templates (homepage, collection, PDP, cart).
- `site-engineer`: release log review and a worst case data pass on the top landing pages.
- Verification pass (`ads-verify` skill, starting with `verified_check.py`): expire old rows in `ads-master/VERIFIED.md`, re-verify those still used, and clear the 10 open claims that block decisions this month.

## Mode: quarterly
- `growth-orchestrator`: strategy reset (draft STRATEGY.md for approval), channel mix review, incrementality and MMM plan with `measurement`.
- Every active agent: full audit using its `audit-checklist.md`.
- `market-intel`: full competitive landscape refresh.

## Scheduling the heartbeat
Pick what fits the team:
- In a session: `/loop 1d /ads-review daily` or ask for a self paced loop.
- Claude Code cloud Routines or scheduled triggers: weekly prompt "Run /ads-review weekly for this repo and open a PR with the outputs".
- CI: a scheduled GitHub Action running Claude Code headless (`claude -p "/ads-review weekly"`) that commits `ads-master/outputs/` to a branch for review.
- Cron on a workstation: `claude -p "/ads-review daily" --output-format text >> ads-master/journal/daily.log`.

## Rules
- Reviews never change live accounts. They produce change lists for approval, within the gates and automation stage in `ads-master/GUARDRAILS.md`.
- Every report separates FACTS, INTERPRETATION and RECOMMENDATION and shows platform reported next to backend observed.
- Missing data is reported as missing. No estimates presented as facts.
- Measure before quote: every number in a report is computed from the named source for that report's date range, never copied from notes, memory or an earlier report. Ratios are recomputed from summed numerators and denominators, never averaged (see `METRICS.md`).
- A check that could not run (no export, connector down, script missing) is reported as "could not run" with the reason, never as green.
- One review document per period. Never overwrite a previous review.
