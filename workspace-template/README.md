# ads-master workspace

This folder is the project brain for the Ads Master agents. It holds facts about this business, earned learnings, the shared journal and every deliverable. The agents themselves (the global playbooks) live in the Ads Master plugin or in `.claude/`.

## Fill these first (15 minutes, highest leverage)

1. `PROJECT_BRIEF.md` business model, offer, unit economics, goals, budgets, markets.
2. `MEASUREMENT.md` what counts as a conversion, its value, and where the truth lives.
3. `AUDIENCE.md` and `BRAND.md` who you sell to and how you sound.

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

## Golden rules

- Agents never spend money, publish ads or change live settings without your approval.
- Memory is earned from real data, never assumed.
- Knowledge files change only with your approval. Agents propose changes through the journal.
