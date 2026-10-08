---
name: ads-review
description: Run the Ads Master operating rhythm (the heartbeat) for the current project. Modes are daily (pacing, tracking and disapproval alerts), weekly (every active agent scores KPIs, closes experiments and proposes changes, then a cross channel review and priorities), monthly (budget reallocation, platform change check, SEO and AI visibility report) and quarterly (strategy reset and test plan). Use when the user asks to run the daily check, weekly review, monthly report, heartbeat, status update or "how are we doing" across marketing channels.
---

# Ads Review (the heartbeat)

The main session runs this skill as the conductor. It fans out to the active specialist agents, then synthesizes. Default mode is `weekly` when no argument is given.

## Preconditions
- `ads-master/` exists. If not, run the `ads-setup` skill first.
- Read `ads-master/HEARTBEAT.md` (active agents), `STRATEGY.md`, `PRIORITIES.md`, `EXPERIMENTS.md`, `MEASUREMENT.md` and journal entries since the last review.
- Check data freshness: list files in `ads-master/data/imports/` newer than the last review, and which connectors are available. If a channel has no data for the period, say so and do not guess.

## Mode: daily (5 minutes, alerts only)
Delegate in parallel to the active paid channel agents with this brief:
> Daily check for <project>. Using the latest data, report only exceptions: spend pacing more than 20 percent off plan, conversions at zero or more than 50 percent below the 7 day average, CPA or ROAS more than 30 percent worse than the 7 day average on meaningful volume, disapprovals or policy issues, budget limited campaigns that are profitable, tracking anomalies. No changes. If nothing is wrong, reply "No exceptions".

Then: if any agent flags a tracking anomaly, delegate to `measurement` immediately. Write one journal entry only if there are exceptions. Present exceptions with a recommended action each.

## Mode: weekly (the learning loop)
1. **Fan out.** Delegate to every active specialist in parallel (paid channels, seo, ai-search-optimization, cro, commerce-feeds, creative-strategy, measurement). Brief for each:
   > Weekly review for <project>, week of <date>. Follow the weekly Cadence section of your skill. Use data from <sources and date range>. Deliver: (1) KPI scorecard vs targets in STRATEGY.md and your memory baselines, (2) wins and misses with the evidence, (3) experiments to close or launch (update EXPERIMENTS.md rows you own), (4) a change list for approval using ads-master/templates/CHANGE_REQUEST.md, (5) memory updates only for confirmed patterns, (6) a journal entry. Save to ads-master/outputs/<slug>/<date>_<slug>_weekly-review.md. End with "Handoffs requested" if you need another agent.
2. **Execute handoffs.** Collect each response. Run any requested handoffs that are needed before the synthesis (for example a tracking fix).
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
- Reviews never change live accounts. They produce change lists for approval.
- Missing data is reported as missing. No estimates presented as facts.
- One review document per period. Never overwrite a previous review.
