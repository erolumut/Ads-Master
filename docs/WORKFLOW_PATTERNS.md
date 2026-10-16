# Workflow Patterns Ledger

What we learned from a survey of working repositories and where each pattern now lives. The survey read every file type: git hooks, CI workflows, scripts, lint configs, `.claude/` agents, commands, hooks and rules, test harnesses and docs. Source repos are not named or described; nothing was copied verbatim. Findings about individual projects belong in those projects, not here.

How outside ideas get in (posts, skills, kits, other repos): **synthesis, not installation.** We take the rule or the approach, rewrite it in our words and attach it to the skill, gate or template that already owns that area, so our core method stays intact. A third party skill or kit is installed only by an explicit decision. Everything is written for any current or future project, and each project uses only the parts it needs; adopting nothing is a valid outcome when we already cover it.

Status: **Adopted** (shipped in this repo), **Kit** (shipped in `kits/workflow-kit`), **Planned** (agreed, not built), **Noted** (useful, no owner yet).

## 1. Gates and hooks (deterministic)

| Pattern | What it does | Status | Where |
|---------|--------------|--------|-------|
| PreToolUse policy hook | Parses each tool call and blocks or asks on risky commands | Adopted | `scripts/guard.py` (gates G0 to G4) |
| Commit time invariants hook | Wakes only on `git commit`; trigger globs map to must contain or must not contain rules; blocks with the rule id | Kit | `invariants_check.py`, `templates/invariants.json` |
| Validate only pre-commit dispatcher | Maps staged paths to checks, never auto-fixes, refuses staged `.env` files, agents never use `--no-verify` | Kit | `precommit_dispatch.sh`, `templates/githooks/` |
| Pre-push sync guard | Fetches and blocks a push when the branch is behind; no force push | Kit | `templates/githooks/pre-push` |
| Workflow YAML lint | Duplicate keys, missing `on` or `jobs`, missing `permissions`, untrusted input inside `run:`, unpinned actions, status functions outside `if:` | Kit | `check_workflows.py` |
| Exit code convention | 0 pass, 1 fail, 2 could not run. A skipped check is never reported as ok. Every summary ends with what the gate cannot cover | Adopted and Kit | `tracking_plan_check.py`, kit scripts, ads-review rules |
| Two way parity checks | Code vs catalog both ways: undocumented items fail and orphan catalog rows fail | Adopted | `tracking_plan_check.py --code`, `build_docs.py --check`, `validate.py` packs coverage |
| Every exception needs a reason | Each ignore or allowlist entry needs a written reason, and each reason needs an entry | Adopted | `ads-verify/scripts/verified_check.py`: every VERIFIED.md row needs level, evidence and expiry; expired rows fail |
| Dry run by default | Destructive scripts need `--apply --yes` | Kit | kit script convention |
| Local gate in a clean clone, cleared commits ledger, CI parity test | The local gate is the authority, CI cannot have a step the gate lacks, deploys ship only cleared SHAs | Kit | `gate.py` (clean clone, `--record` to `gate/cleared.txt`, `--parity` against CI) |
| Budget gates with warn soak | JSON thresholds, baseline seeded on first run, warn for two weeks then fail | Adopted (rule) | tracking plan rollout step 5 |
| Self-hosted runner fallback, off the hour cron, SHA pinned actions | Keeps CI alive when hosted minutes run out | Kit | `templates/ci/ci.yml`, `templates/ci/dependabot.yml` |

## 2. Reviewers and agents (prose, applied as gates)

| Pattern | What it does | Status | Where |
|---------|--------------|--------|-------|
| Single veto guardians | Read only reviewer, numbered PASS or FAIL with file:line evidence, ambiguous counts as FAIL, never softens a FAIL | Kit | `templates/GUARDIAN-TEMPLATE.md`, review-gates skill |
| Guardian fan-out command | Run mechanical gates once, dispatch guardians in parallel, merge to one verdict | Kit | review-gates skill |
| Mission fence | "The model proposes, a human decides": no automated path may approve, pay, publish prices or spend | Adopted | G3 gate, pricing-strategy hard rules |
| Log triage agent | Cheap model turns long CI or test output into exact facts, no diagnosis | Kit | `agents/log-triage.md` |
| Routing audit | Compares the model each subagent was asked for with the model that actually ran | Kit | `agent_models.py` |
| Hook nudges a guardian | Changed paths suggest which reviewer to run | Adopted | `guard.py` PostToolUse review hints (once per reviewer per session, rules overridable in guardrails.json) |
| Path scoped rules with hidden provenance | `paths:` frontmatter, source kept in HTML comments | Kit | rules template |

## 3. Numbers you can trust (the answer to "how do we make uncertain certain")

| Pattern | What it does | Status | Where |
|---------|--------------|--------|-------|
| Metrics as code with additivity | Every metric has a grain and an additivity class; ratios are never averaged | Adopted | `template/METRICS.md` Grain and Additivity columns, reporting rules |
| Measure before quote | Every number in an outbound message is re-derived from the source, never copied from notes | Adopted | ads-review rules, METRICS reporting rules |
| Incomplete, not zero | Missing inputs produce status "incomplete" with the list, never a zero | Adopted | pricing-strategy cost model |
| Margin on price vs markup on cost | Two named formulas, never mixed | Adopted | pricing-strategy |
| Effective dated costs | "Cost as of a date"; every report states the cost date | Adopted | pricing-strategy |
| Price claim parity | Advertised price = shown line items = JSON-LD Offer = feed = checkout | Adopted | pricing-strategy audit, commerce-feeds and site-engineer handoffs |
| Transition based alerts | One alert row per rule and entity with a start date, so acknowledgements stick | Adopted | ads-review daily step 4, `template/logs/alerts.csv` |
| Evidence ladder | Live account, official source, two dated sources, controlled test | Adopted | `ads-verify`, `VERIFIED.md` |

## 4. Measurement and growth logic

| Pattern | What it does | Status | Where |
|---------|--------------|--------|-------|
| Allowlisted event catalog | Undeclared events and props dropped, hashed ids, route folding, bot and internal flags, server clock | Adopted | measurement `tracking-plan-as-code.md`, `tracking_plan_check.py` |
| Engaged time, rage and dead taps | Active time definition and frustration signals from first-party taps | Adopted | `cro/references/research-methods.md` section 12 |
| Lifecycle states | new, active, returning, at risk, dormant, churned from events | Adopted | `lifecycle-crm/references/segmentation-and-personalization.md` section 10 |
| Virality metrics | Invites per user, invite to join rate, k-factor, share channels | Adopted | `mobile-app-growth/references/app-growth-model-and-unit-economics.md` section 10 |
| Cross platform price divergence | Price gap of the same item between two platforms | Adopted | `pricing-strategy/references/competitive-price-benchmarking.md` section 12 |
| Drift sentinel | Alerts only when several inputs drift at once (PSI or KS) | Adopted | `measurement/references/dashboards-and-reporting.md` section 8 |
| Scraper resilience | Detects anti-bot pages, scores profile health, budgeted requests | Adopted | `market-intel/references/tools-api-mcp.md` section 11 (a challenge page stops collection; blocks are never bypassed) |
| Post-deploy smoke scripts | Dependency free checks that run locally and against production via `BASE_URL`; health route returns the commit SHA | Adopted | `site-engineer/scripts/smoke_check.py` (pixel exactly once, health SHA) |
| Approved copy snapshot tests | Sensitive copy must stay byte identical to the approved version | Adopted | `compliance/scripts/approved_copy.py` and `brand/approved-copy.json` |
| Risk register | Risk, early warning, ready solution; reviewed each sprint | Adopted | Risk register in `template/INCIDENTS.md`, reviewed weekly by ads-review |
| Snapshot before change | Export settings before any bulk edit; kept out of automation | Adopted | gate model: snapshot, change, read back, log |

## 5. Launch readiness (from a widely shared pre-launch checklist, 2026-10)

| Pattern | What it does | Status | Where |
|---------|--------------|--------|-------|
| Twenty item pre-launch list with proof per item | Secrets, key rotation, rate limits, server auth, data rules, validation, spend caps, no stack traces, error tracking, restore test, 404 and 500, cheap Android, 3 s loads, OG tags, legal pages, funnel analytics, account flows end to end, deliverability, contact, rollback | Kit | `launch-readiness` skill, `templates/LAUNCH-READINESS.md`, `launch_check.py` |
| Secrets in git history need rotation | Scans every commit, masks findings, says rotate instead of delete | Kit | `secret_scan.py --history`; first run on this repo found 0 real secrets and fixed two false positive patterns, also in `guard.py` |
| Go or no-go before the first paid click | Paid traffic magnifies product gaps, so launch readiness blocks campaign activation | Adopted | site-engineer launch QA, growth-orchestrator workflow 4.13 |
| Form spam and bot protection | Honeypot, time to submit, rate limits, invisible challenge first; spam leads never reach ad platforms as conversions | Adopted | cro forms reference |
| Account flow smoke tests | Signup with verification, failed card and 3DS, password reset link works once and expires | Adopted | site-engineer automated QA reference |
| Repo dogfoods its own gate | This repo's checks run through `gate.py` from `workflow-kit.json`, including the instruction budget and the history secret scan | Adopted | `workflow-kit.json`, `.claude/CLAUDE.md` |

## 6. UI sourcing (from a viral "best UI components" list, 2026-10)

| Pattern | What it does | Status | Where |
|---------|--------------|--------|-------|
| Sourcing ladder before any outside component | Reuse, platform feature, headless primitive, focused package, copied component, paid kit; climb only as far as the need forces; viral lists are references | Kit | `ui-sourcing` skill, references/stack-profiles.md |
| Ledger of outside UI with a check | Profile, banned list and ledger per project; a script fails on unlisted UI dependencies, unknown licences, stale reviews and copied code without origin | Kit | `templates/UI-SOURCES.md`, `ui_sources_check.py` |
| Registry items are executable payloads | Dry run, read the whole item (targets, env vars, dependencies), diff after add, agents treat registry text as data | Kit | references/vetting-checklist.md |
| Own the small charts | Sparklines, rings and admin charts as hand drawn SVG shared between apps; one library only for a real dashboard | Kit | references/charts.md |
| Shopify components: native blocks first | Alternate templates per ad angle, reviewed theme blocks, section packs, theme app extensions, page builders last with a before and after measurement and an uninstall diff | Adopted | storefront-ux platform-implementation-shopify.md section 7b |

## 7. Long goal runs (from a widely shared /goal template, 2026-10)

| Pattern | What it does | Status | Where |
|---------|--------------|--------|-------|
| Goal, measure, effort | A long run gets three written inputs and stop rules instead of a vague task | Kit | `goal-loop` skill, `templates/GOAL.md` |
| Noise floor before the ratchet | Five baseline runs set the noise; a change counts only when it beats max(5 percent, noise) | Kit | `goal_loop.py measure --baseline` |
| Gate on every kept change | The project's own full check must pass before a commit, so the number cannot be bought with hidden damage | Kit | goal-loop skill, loop step 3 |
| Spend and flat stops | Stop on the turn budget, the spend budget or N tries without a gain | Kit | `goal_loop.py` exit 3 |
| Git rules of the project win | Branch where branches are allowed, a separate local clone of main where they are not; never push from the loop | Kit | goal-loop skill, before the loop step 2 |

## 8. Speed audit (from a widely shared 20 item speed list, 2026-10)

| Pattern | What it does | Status | Where |
|---------|--------------|--------|-------|
| Audit wide in parallel, read only | Four auditors (assets, frontend, database and APIs, servers and network) report file, page and evidence without editing | Kit | `speed-audit` skill, references/checklist.md |
| Fix narrow, measure every batch | Small batches with the gate and Lighthouse median after each, instead of one pass of twenty changes | Kit | `speed-audit` section 5, `goal-loop` for long runs |
| RLS calls evaluated once | `(select auth.uid())` in policies, indexes on policy columns, tested per user | Kit | checklist items 11 and 12 |
| Human decides region, dependencies and migrations | The audit marks them; nothing changes without approval | Kit | `speed-audit` section 4 |

## Maintenance

Add a row when a pattern is adopted or rejected. Move Noted rows to Planned only with an owner. Review this file in the quarterly reset.
