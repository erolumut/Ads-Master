# Ads Master

Research backed growth agents for Claude Code: paid media (Meta, Google, Microsoft, ChatGPT, TikTok, LinkedIn), marketplaces, app growth, SEO, AI search optimization, storefront UX, CRO, site engineering, pricing, offers, product feeds, creative strategy, video production, lifecycle CRM, measurement, compliance and market intelligence, coordinated by a growth orchestrator and protected by deterministic guardrail hooks.

## Two ways this repo is used

1. **As the source of the agents** (developing or improving them). Follow `docs/AUTHORING_SPEC.md` and `docs/GUARDRAILS_MODEL.md`. Run `python3 scripts/validate.py` and `python3 scripts/test_guard.py` before committing.
2. **As a workspace for one business.** The agents load from `.claude/agents` and `.claude/skills` (symlinks to `agents/` and `skills/`). Run `/ads-setup` to create `ads-master/` here, then work as you would in any installed project.

## Map

| Path | What |
|------|------|
| `agents/<slug>.md` | Subagent definitions (persona, KPIs, loop, handoffs, hard rules) |
| `skills/<slug>/SKILL.md` | Playbook entry point with adaptation matrix and task router |
| `skills/<slug>/references/` | Deep modules: audits, playbooks, settings, benchmarks, sources |
| `skills/ads-setup/` | Creates the per project workspace from `skills/ads-setup/template/` |
| `skills/ads-review/` | The heartbeat: daily, weekly, monthly, quarterly cycles |
| `research/` | Market research dossiers (October 2026) behind every playbook |
| `AGENT_REGISTRY.md` | Roster, KPIs, cadences, handoffs |
| `scripts/install.sh` | Copy agents, skills and the guard hook into another project |
| `scripts/guard.py`, `hooks/hooks.json` | Deterministic guardrails (gates G0 to G4, automation stages) |
| `scripts/validate.py` | Structure, YAML and style checks |

## How work flows

- The main session is the conductor. For multi channel work, load the `growth-orchestrator` skill and delegate to specialist agents, in parallel when independent.
- Specialists do not call each other (nested subagents are disabled with `disallowedTools: Agent`). They write to `ads-master/journal/` and end with "Handoffs requested". The main session executes those.
- Project facts live in `ads-master/` (per project). Generic knowledge lives in `skills/` (global). Never mix them.

## Non-negotiables

- No spend, launch, bid, budget, publishing, customer messaging or live account change without explicit human approval. Agents draft change requests; the guard hook enforces `ads-master/guardrails.json`.
- Customer facing copy passes the compliance agent; site changes pass site-engineer release QA.
- No invented numbers. Every figure names its source and date range.
- Platform features change monthly. Run the skill's Freshness Protocol before acting on settings, policies or benchmarks.

## Writing style for this repo

English, direct, practitioner grade. No em dashes or en dashes. Banned words and other rules: `docs/AUTHORING_SPEC.md` section 8.

## How we work on this repo (Workflow Kit, loaded via `scripts/link_dev.py`)

- Plan first for anything beyond a small fix (`planner-session`). Route work with `model-routing`: `scout`, `data-extractor`, `log-triage` on haiku; `researcher`, `mechanic` on sonnet; `verifier` before a claim counts; `fable-advisor` only at critical points.
- Several sessions on this repo: `parallel-sessions` and its ledger. Stage paths explicitly.
- Done means reviewed (`review-gates`): evidence for every PASS, and a check that could not run is never a pass.
- Before committing: `python3 scripts/validate.py`, `python3 scripts/test_guard.py`, and `python3 scripts/build_docs.py` if agents, skills, packs or kits changed.
