# Authoring Spec

The contract every agent package in Ads Master follows. Read this before adding or editing an agent. Consistency is what makes the system plug and play: every agent boots the same way, reads the same project files, writes to the same places and hands off with the same slugs.

## 1. Mental model

```
Global brain (this repo, reusable)          Project state (per project, in the client repo)
---------------------------------          ------------------------------------------------
agents/<slug>.md      persona + loop        ads-master/PROJECT_BRIEF.md   business facts
skills/<slug>/SKILL.md   playbook entry     ads-master/MEASUREMENT.md     tracking truth
skills/<slug>/references/*.md  deep modules ads-master/memory/<slug>.md   earned learnings
research/<slug>.md    market research       ads-master/journal/           shared event log
                                            ads-master/outputs/<slug>/    deliverables
```

Knowledge is global and versioned in this repo. State is local to each project. Agents never store project facts inside the global brain, and never store generic best practice inside a project.

### How delegation works in Claude Code

A subagent cannot spawn another subagent. So:

- The **main session** is the conductor. For multi agent work it loads the `growth-orchestrator` skill, then delegates to specialist subagents (in parallel when the work is independent) and synthesizes their outputs.
- A **specialist subagent** that needs another specialist performs a handoff: it writes a journal entry with the request and ends its final response with a `Handoffs requested` section (target slug plus a 2 to 4 line brief). The main session executes those delegations.
- The `growth-orchestrator` subagent does single threaded strategy work (diagnosis, budget, forecasting, synthesis) and returns a delegation plan when fan-out is needed.

## 2. Package layout per domain

```
agents/<slug>.md                      Claude Code subagent definition
skills/<slug>/SKILL.md                Skill entry point (max ~450 lines)
skills/<slug>/references/*.md         6 to 14 deep modules (each 120 to 600 lines)
research/<slug>.md                    Market research dossier with dated sources
```

Slugs are lowercase and hyphenated. The agent file, skill folder and research file share the same slug.

## 3. `agents/<slug>.md` format

```markdown
---
name: <slug>
description: <When the main session should delegate to this agent. Lead with the domain, list concrete trigger tasks, say "Use proactively when ..." for obvious triggers. Max ~600 characters.>
model: inherit
skills:
  - <slug>
---

# <Agent Title>

You are ... (one paragraph identity: senior operator, what you optimize, how you think)

## Mission
One sentence.

## KPIs you own
Table: KPI | Definition | Healthy range or target logic | Source of truth

## Startup sequence (every task)
1. Load your skill playbook (`<slug>` skill). Use its Task Router to pick the reference modules for the task.
2. Read project state if present (see section 6 of the spec). If `ads-master/` is missing, run in "cold start" mode: ask only for the minimum facts listed in the skill's Intake, or suggest running the `ads-setup` skill.
3. Read `ads-master/memory/<slug>.md` and the latest 10 journal entries.
4. Run the Freshness Check when the task depends on platform features, policies or settings.

## Operating loop
Diagnose -> Prioritize (impact x confidence x ease) -> Act (produce the deliverable) -> QA against the Quality Bar -> Log.

## Decision rules
The 8 to 15 rules that most often decide outcomes in this domain.

## Handoffs
Table: Situation | Hand off to (slug) | What to pass

## Hard rules
Never spend, publish, change bids or budgets, or edit live accounts without explicit human approval. Never invent data. Label every number with its source. Follow the skill guardrails.

## Output format
How deliverables are structured and where they are saved.

## Memory and journal protocol
What qualifies as a memory entry, what goes to the journal, file names.
```

Notes on the frontmatter:
- Omit `tools` so the agent inherits every tool, including web search and any ad platform MCP connectors the user has installed.
- `skills` is a YAML list. It preloads the playbook into the subagent. The body still tells the agent to invoke the skill if it is not in context (covers runtimes that ignore the field).
- Do not use the `memory` field. Project memory lives in `ads-master/memory/<slug>.md` so it stays visible, versioned and tool agnostic.
- Do not reference `${CLAUDE_PLUGIN_ROOT}` in agent bodies. It only expands in plugin installs and breaks project installs.

## 4. `skills/<slug>/SKILL.md` format

```markdown
---
name: <slug>
description: <What the skill covers and when to use it, written so Claude triggers it on the right requests. Include platform names, key feature names and task verbs (audit, launch, scale, troubleshoot, forecast). Max 1024 characters.>
---

# <Skill Title>

> Knowledge as of <YYYY-MM>. Platforms change monthly. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark.

## Mission and scope
## Intake (minimum facts needed; where to find them in ads-master/)
## Operating protocol (numbered, the full loop)
## Adaptation matrix
   Rows: business model (ecommerce, lead gen, B2B SaaS, local services, app, marketplace or content publisher)
   Columns or sub-rows: budget and signal tier (Starter, Growth, Scale, Enterprise), maturity (new account, running, plateau, scaling)
   Cells: what changes (structure, bidding, KPI, cadence, creative volume, tests)
## Task router
   Table: Task | Read these references | Output template
## The laws (non-negotiable best practices, 15 to 25, each one line with the why)
## Diagnostics (symptom -> likely causes -> checks -> fixes)
## Cadence (daily, weekly, monthly, quarterly checks: the heartbeat)
## Guardrails and approvals
## Outputs (file naming and required sections)
## Freshness protocol (official sources and changelogs to check, what to verify, how to log changes)
## Reference index (one line per reference file, as relative links: [Account structure](references/account-structure.md))
```

Keep SKILL.md under 500 lines. Link every reference file with a relative markdown link so Claude can open it on demand. Only `name` and `description` go in the frontmatter (keeps the skill portable to claude.ai and the Skills API).

Budget and signal tiers used across all agents:

| Tier | Monthly paid media | Typical signal |
|------|--------------------|----------------|
| Starter | under $3k | under 30 conversions per month per channel |
| Growth | $3k to $30k | 30 to 300 conversions per month |
| Scale | $30k to $300k | 300 to 3,000 conversions per month |
| Enterprise | over $300k | multi market, multi brand, MMM ready |

## 5. Reference modules

Each reference file is a self-contained deep module: procedures, checklists, settings tables, formulas, worked examples, queries or scripts, and benchmarks. Every package must include:

- `audit-checklist.md`: a scored audit (each item: check, why, how to verify, severity, fix). Ends with a scoring rubric.
- `playbooks.md` or several playbook files: step by step plays for launch, optimize, scale, recover.
- `sources.md`: annotated source list (title, publisher, URL, date, what it supports).

Other modules are domain specific (account structure, bidding, creative, measurement, policies, tools and APIs, benchmarks, etc.).

## 6. Project state contract (what agents read and write)

Agents look for an `ads-master/` folder at the project root. Created by the `ads-setup` skill from `workspace-template/`.

| File | Owner | Agents may |
|------|-------|-----------|
| `PROJECT_BRIEF.md` | Human | Read. Propose edits via journal. |
| `BRAND.md`, `AUDIENCE.md`, `COMPETITORS.md` | Human | Read. Propose edits via journal. |
| `STRATEGY.md` | Human with growth-orchestrator | Read. Orchestrator drafts updates for approval. |
| `MEASUREMENT.md` | Human with measurement agent | Read. Measurement agent drafts updates for approval. |
| `PRIORITIES.md` | growth-orchestrator | Read. Only orchestrator edits. |
| `EXPERIMENTS.md` | All agents | Append new rows. Update status of own rows. |
| `HEARTBEAT.md` | growth-orchestrator | Read. Only orchestrator edits. |
| `memory/<slug>.md` | That agent | Only that agent edits its own file. |
| `journal/YYYY-MM-DD_HHMM_<slug>_<topic>.md` | Any agent | Create new entries. Never edit others. |
| `data/imports/` | Human or connectors | Read. |
| `outputs/<slug>/YYYY-MM-DD_<slug>_<description>.md` | That agent | Create. Never overwrite; create a new dated file. |

## 7. Evidence labels

Use these inline labels for claims in references and research:

- `[Official, YYYY-MM]` platform documentation or announcement
- `[Study, YYYY-MM]` published data study with a method
- `[Practitioner consensus]` widely repeated by credible operators, no hard data
- `[Contested]` credible people disagree; present both sides
- `[Unverified]` single source or could not confirm; treat as hypothesis

Benchmarks always carry source, date, sample and the caveat that they vary by vertical, geo and season. Agents compare a project against its own history first and benchmarks second.

## 8. Writing style

- English. Direct, specific, imperative. Practitioner grade. No filler, no hype.
- Prefer tables, checklists and numbered procedures over prose.
- Ranges use "to" (3 to 5), not dashes.
- Do not use em dashes or en dashes anywhere. Do not use a spaced hyphen to join sentences. Use periods, commas, colons or parentheses instead. Hyphens inside compound words (first-party, 7-day click) are fine.
- Banned words: excel, excellent, robust, honed, spearheaded, prospect, prospecting, resonate, thrive. Say "cold audience acquisition" or "new customer acquisition" instead of prospecting.
- Never invent statistics, quotes or features. If something could not be verified, label it `[Unverified]`.

## 9. Adding a new agent

1. Copy an existing package of the closest domain.
2. Rename the slug in all four places (agent, skill folder, skill `name`, research file).
3. Rewrite the mission, KPIs, intake, adaptation matrix and task router first. Then the references.
4. Add it to `AGENT_REGISTRY.md` and to the routing table in `skills/growth-orchestrator/SKILL.md`.
5. Run `scripts/validate.sh`.
