# Workflow Patterns Ledger

What we learned from a survey of twelve working repositories (product apps, data pipelines, a costing tool, a local travel site, games, PWAs) and where each pattern now lives. The survey read every file type: git hooks, CI workflows, scripts, lint configs, `.claude/` agents, commands, hooks and rules, test harnesses and docs. Source repos are referenced by name only; nothing was copied verbatim.

Status: **Adopted** (shipped in this repo), **Kit** (shipped in `kits/workflow-kit`), **Planned** (agreed, not built), **Noted** (useful, no owner yet).

## 1. Gates and hooks (deterministic)

| Pattern | What it does | Seen in | Status | Where |
|---------|--------------|---------|--------|-------|
| PreToolUse policy hook | Parses each tool call and blocks or asks on risky commands | costing tool, housing tracker | Adopted | `scripts/guard.py` (gates G0 to G4) |
| Commit time invariants hook | Wakes only on `git commit`; trigger globs map to must contain or must not contain rules; blocks with the rule id | housing tracker | Kit | `invariants_check.py`, `templates/invariants.json` |
| Validate only pre-commit dispatcher | Maps staged paths to checks, never auto-fixes, refuses staged `.env` files, agents never use `--no-verify` | Avlu, holiday park pricing tool | Kit | `precommit_dispatch.sh`, `templates/githooks/` |
| Pre-push sync guard | Fetches and blocks a push when the branch is behind; no force push | Avlu, holiday park pricing tool | Kit | `templates/githooks/pre-push` |
| Workflow YAML lint | Duplicate keys, missing `on` or `jobs`, missing `permissions`, untrusted input inside `run:`, unpinned actions, status functions outside `if:` | Avlu, holiday park pricing tool | Kit | `check_workflows.py` |
| Exit code convention | 0 pass, 1 fail, 2 could not run. A skipped check is never reported as ok. Every summary ends with what the gate cannot cover | Avlu, holiday park pricing tool | Adopted and Kit | `tracking_plan_check.py`, kit scripts, ads-review rules |
| Two way parity checks | Code vs catalog both ways: undocumented items fail and orphan catalog rows fail | Avlu, macro creator | Adopted | `tracking_plan_check.py --code`, `build_docs.py --check`, `validate.py` packs coverage |
| Every exception needs a reason | Each ignore or allowlist entry needs a written reason, and each reason needs an entry | Avlu | Planned | validate.py for `[Unverified]` labels without a VERIFIED.md row |
| Dry run by default | Destructive scripts need `--apply --yes` | Avlu | Kit | kit script convention |
| Local gate in a clean clone, cleared commits ledger, CI parity test | The local gate is the authority, CI cannot have a step the gate lacks, deploys ship only cleared SHAs | holiday park pricing tool | Noted | candidate for kit v2 |
| Budget gates with warn soak | JSON thresholds, baseline seeded on first run, warn for two weeks then fail | Avlu, macro creator | Adopted (rule) | tracking plan rollout step 5 |
| Self-hosted runner fallback, off the hour cron, SHA pinned actions | Keeps CI alive when hosted minutes run out | Avlu, holiday park pricing tool | Noted | CI starter pack candidate |

## 2. Reviewers and agents (prose, applied as gates)

| Pattern | What it does | Seen in | Status | Where |
|---------|--------------|---------|--------|-------|
| Single veto guardians | Read only reviewer, numbered PASS or FAIL with file:line evidence, ambiguous counts as FAIL, never softens a FAIL | costing tool, holiday park pricing tool, Avlu | Kit | `templates/GUARDIAN-TEMPLATE.md`, review-gates skill |
| Guardian fan-out command | Run mechanical gates once, dispatch guardians in parallel, merge to one verdict | holiday park pricing tool, Avlu | Kit | review-gates skill |
| Mission fence | "The model proposes, a human decides": no automated path may approve, pay, publish prices or spend | costing tool, holiday park pricing tool | Adopted | G3 gate, pricing-strategy hard rules |
| Log triage agent | Cheap model turns long CI or test output into exact facts, no diagnosis | Avlu | Kit | `agents/log-triage.md` |
| Routing audit | Compares the model each subagent was asked for with the model that actually ran | Avlu | Kit | `agent_models.py` |
| Hook nudges a guardian | Changed paths suggest which reviewer to run | macro creator | Planned | Stop hook hint in guard.py |
| Path scoped rules with hidden provenance | `paths:` frontmatter, source kept in HTML comments | Avlu | Kit | rules template |

## 3. Numbers you can trust (the answer to "how do we make uncertain certain")

| Pattern | What it does | Seen in | Status | Where |
|---------|--------------|---------|--------|-------|
| Metrics as code with additivity | Every metric has a grain and an additivity class; ratios are never averaged | holiday park pricing tool | Adopted | `template/METRICS.md` Grain and Additivity columns, reporting rules |
| Measure before quote | Every number in an outbound message is re-derived from the source, never copied from notes | holiday park pricing tool | Adopted | ads-review rules, METRICS reporting rules |
| Incomplete, not zero | Missing inputs produce status "incomplete" with the list, never a zero | costing tool | Adopted | pricing-strategy cost model |
| Margin on price vs markup on cost | Two named formulas, never mixed | costing tool | Adopted | pricing-strategy |
| Effective dated costs | "Cost as of a date"; every report states the cost date | costing tool | Adopted | pricing-strategy |
| Price claim parity | Advertised price = shown line items = JSON-LD Offer = feed = checkout | local travel site | Adopted | pricing-strategy audit, commerce-feeds and site-engineer handoffs |
| Transition based alerts | One alert row per rule and entity with a start date, so acknowledgements stick | holiday park pricing tool | Adopted | ads-review daily step 4, `template/logs/alerts.csv` |
| Evidence ladder | Live account, official source, two dated sources, controlled test | this repo | Adopted | `ads-verify`, `VERIFIED.md` |

## 4. Measurement and growth logic

| Pattern | What it does | Seen in | Status | Where |
|---------|--------------|---------|--------|-------|
| Allowlisted event catalog | Undeclared events and props dropped, hashed ids, route folding, bot and internal flags, server clock | therapist portal, medicine cabinet app | Adopted | measurement `tracking-plan-as-code.md`, `tracking_plan_check.py` |
| Engaged time, rage and dead taps | Active time definition and frustration signals from first-party taps | therapist portal | Noted | cro research inputs |
| Lifecycle states | new, active, returning, at risk, dormant, churned from events | medicine cabinet app | Noted | lifecycle-crm segment source |
| Virality metrics | Invites per user, invite to join rate, k-factor, share channels | daily games app | Noted | mobile-app-growth and lifecycle-crm referral |
| Cross platform price divergence | Price gap of the same item between two platforms | housing tracker | Noted | pricing-strategy and marketplaces monitoring |
| Drift sentinel | Alerts only when several inputs drift at once (PSI or KS) | housing tracker | Noted | measurement anomaly design |
| Scraper resilience | Detects anti-bot pages, scores profile health, budgeted requests | housing tracker | Noted | market-intel collection base |
| Post-deploy smoke scripts | Dependency free checks that run locally and against production via `BASE_URL`; health route returns the commit SHA | social game PWA, Avlu | Planned | site-engineer launch QA |
| Approved copy snapshot tests | Sensitive copy must stay byte identical to the approved version | social game PWA | Planned | compliance, approved claims |
| Risk register | Risk, early warning, ready solution; reviewed each sprint | social game PWA | Planned | growth risk rows in `INCIDENTS.md` |
| Snapshot before change | Export settings before any bulk edit; kept out of automation | costing tool | Adopted | gate model: snapshot, change, read back, log |

## 5. Findings about specific projects (for their own sessions)

- Local travel site: no analytics or conversion tracking on the WhatsApp and enquiry paths, placeholder contact numbers in site data, no AI crawler rules in robots. Fix all three before any paid traffic. The all inclusive price with a per airport breakdown is a strong offer angle.
- Costing tool: its costing spec maps directly onto breakeven ROAS and POAS inputs for the brand it serves.

## Maintenance

Add a row when a pattern is adopted or rejected. Move Noted rows to Planned only with an owner. Review this file in the quarterly reset.
