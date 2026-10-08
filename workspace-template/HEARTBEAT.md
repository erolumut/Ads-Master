# Heartbeat

> The operating rhythm for this project. The growth-orchestrator keeps it current. Run a cycle by asking Claude: "run the daily cycle" or "run the weekly review" (the `ads-review` skill), or schedule it with `/loop`, a Routine or a CI job.

## Active agents
| Agent | Active | Cadence | Notes |
|-------|--------|---------|-------|
| growth-orchestrator | yes | weekly + monthly | |
| measurement | yes | weekly health check | Always on. Bad data breaks every other agent. |
| meta-ads | | | |
| google-ads | | | |
| microsoft-ads | | | |
| chatgpt-ads | | | |
| tiktok-ads | | | |
| linkedin-ads | | | |
| seo | | | |
| ai-search-optimization | | | |
| commerce-feeds | | | |
| cro | | | |
| creative-strategy | | | |
| market-intel | | | |

## Daily (5 minutes, paid channels only)
- Spend pacing vs plan, tracking sanity (conversions not zero, no spikes), disapprovals, budget caps hit.

## Weekly (the learning loop)
1. Each active agent scores its KPIs vs targets and writes a journal entry.
2. Experiments: close finished tests, log learnings, launch next from backlog.
3. growth-orchestrator writes the weekly review and updates PRIORITIES.md.

## Monthly
- Budget reallocation proposal, creative refresh plan, SEO and AI visibility report, measurement audit, freshness check of platform changes.

## Quarterly
- Strategy reset, incrementality test plan, full audits per channel.
