# ads-master workspace

This folder is the project brain for the Ads Master agents. It holds facts about this business, earned learnings, the shared journal and every deliverable. The agents themselves (the global playbooks) live in the Ads Master plugin or in `.claude/`.

## Fill these first (15 minutes, highest leverage)

1. `PROJECT_BRIEF.md` business model, offer, unit economics, goals, budgets, markets.
2. `MEASUREMENT.md` and `METRICS.md` what counts as a conversion, its value, and where the truth lives.
3. `GUARDRAILS.md` and `guardrails.json` automation stage and money caps.
4. `AUDIENCE.md`, `BRAND.md` and `brand/PRODUCT_FACTS.md` who you sell to, how you sound, what is provably true.

Or run the `ads-setup` skill and let Claude interview you and scan the codebase.

## How the folder works

| Path | What it is | Who writes |
|------|-----------|-----------|
| `PROJECT_BRIEF.md` | Business facts and constraints | You |
| `BRAND.md` `AUDIENCE.md` `COMPETITORS.md` | Static reference | You (agents propose) |
| `STRATEGY.md` | Quarter goals, channel roles, budget split | You with growth-orchestrator |
| `MEASUREMENT.md` | Tracking stack and sources of truth | You with measurement agent |
| `PRIORITIES.md` | This week's ranked work | growth-orchestrator |
| `HEARTBEAT.md` | Which agent runs what, and when | growth-orchestrator |
| `EXPERIMENTS.md` | Experiment backlog and results | All agents |
| `memory/<agent>.md` | Learnings confirmed by data | Each agent, own file only |
| `journal/` | Shared event log between agents | All agents, new files only |
| `data/imports/` | CSV exports and screenshots you drop in | You or connectors |
| `outputs/<agent>/` | Audits, plans, briefs, reports | Each agent |
| `templates/` | Journal, change request, audit, experiment and review formats | Shared |
| `GUARDRAILS.md` + `guardrails.json` | Automation stage, money caps, gates, approvers (the hooks enforce the JSON) | You |
| `DECISIONS.md` | Decision log: what was decided, why, when to revisit | You and growth-orchestrator |
| `INCIDENTS.md` | Stop conditions, runbook, incident log | All agents |
| `METRICS.md` | One definition per metric (including acquisition investment) | You with measurement |
| `brand/PRODUCT_FACTS.md`, `brand/CLAIMS.md` | Verified facts and the claims registry | You with compliance |
| `brand/VIDEO_RULES.md` | The video brand system per video type: colours, type, backgrounds, music, sound, banned effects | creative-strategy and video-studio, you approve |
| `GAME_ECONOMY.md`, `data/monetization-policy.example.json` | Game projects only: currencies, catalog, offers, ad placements and fairness rules; copy the example to `data/monetization-policy.json` | You with game-monetization |
| `LIVEOPS_CALENDAR.md` | Game projects only: events, seasons and store event submissions | You with game-liveops |
| `SUBMISSION.md` | Apps and games: the store submission dossier (checklist, review notes, demo account location, SDK data map) | You with store-submission |
| `creative-library/registry.csv` | Creative IDs, metadata and learnings | creative-strategy, video-studio, channel agents |
| `logs/` | Audit log of write attempts and session reports | Hooks and agents |

## Golden rules

- Agents never spend money, publish ads, message customers or change live settings without your approval. Hooks enforce `guardrails.json` on every tool call.
- Memory is earned from real data, never assumed.
- Knowledge files change only with your approval. Agents propose changes through the journal.
