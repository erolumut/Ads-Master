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
| video-studio | | | |
| compliance | yes | on every publish | Pre-publish gate for ads, pages, emails, feeds, videos |
| storefront-ux | | | Storefront conformance audit and component builds |
| site-engineer | | | Release QA before any site change goes live |
| lifecycle-crm | | | |
| offer-strategy | | | |
| mobile-app-growth | | | |

## Daily (5 minutes)
- Daily report (`/ads-review daily`): spend vs plan, platform reported vs backend observed, acquisition investment, tracking sanity, disapprovals, stock cover of advertised items, incidents. FACTS, INTERPRETATION, RECOMMENDATION. Decide on 3 and 7 day windows, not on one day.

## Weekly (the learning loop)
1. Each active agent scores its KPIs vs targets and writes a journal entry.
2. Experiments: close finished tests, log learnings, launch next from backlog.
3. growth-orchestrator writes the weekly review and updates PRIORITIES.md.

## Monthly
- Budget reallocation proposal, creative refresh plan, SEO and AI visibility report, measurement audit, freshness check of platform changes.

## Quarterly
- Strategy reset, incrementality test plan, full audits per channel.
