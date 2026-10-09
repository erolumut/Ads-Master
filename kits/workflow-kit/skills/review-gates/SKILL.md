---
name: review-gates
description: Guardian and reviewer pattern for calling work done. Use before declaring a deliverable done, before merging or shipping a risky change, when setting up review checklists or named guardians, when a bug escaped and its class must never return, or when the user asks for a review, audit, quality gate or second check. Evidence based PASS, devil's advocate three defect hunt, and a regression library that grows with every new bug class.
---

# Review gates

Green checks prove the code compiles and the tests you wrote pass. They do not prove the work is finished. A review gate is a written checklist plus an independent reviewer that must cite evidence for every PASS. The model proposes, a human decides: a guardian verdict is an input to the human's ship decision, never a replacement for it.

> **Kit path.** `<kit>` below is `${CLAUDE_PLUGIN_ROOT}` when the kit runs as a plugin, or `.claude/workflow-kit` when it was installed by copy. Every kit script exits 0 pass, 1 fail, 2 could not run; treat 2 as not passed, and read the "This gate cannot cover:" line each one prints.

## Pieces

| Piece | What | Where |
|---|---|---|
| **Checklist** | Written criteria for an area (functional, UX, security, performance, accessibility, scope) | `docs/review/<AREA>-CHECKLIST.md`, registered in `workflow-kit.json` under `reviewers` |
| **Regression library** | One entry per bug class that ever escaped; permanent | `docs/review/REGRESSIONS.md` (`reviewers.regressionLibrary`) |
| **Guardian** | A read-only reviewer agent bound to one checklist | `.claude/agents/<area>-guardian.md`, from `templates/GUARDIAN-TEMPLATE.md` (numbered checklist built in) or a copy of the kit's `reviewer` agent (checklist in a separate file) |
| **Mechanical gates** | Checks with an exit code | `precommit_dispatch.sh` (staged paths to checks via `precommit.json`), `invariants_check.py` (`invariants.json`), `check_workflows.py`, `doc_numbers.py`, `check_instructions.py`, `gate.py` (every step on a clean clone of HEAD), the project's own tests and linters |
| **Gate run record** | The filled checklist with evidence | `docs/review/runs/<date>-<slug>.md` |

Templates: `templates/REVIEW-CHECKLIST.md`, `templates/GUARDIAN-TEMPLATE.md`, `templates/invariants.json`, `templates/precommit.json`, `templates/githooks/`, `templates/hooks/invariants-pretooluse.json`.

## Rules

1. **"Looks good" is banned.** Every PASS cites evidence: `file:line`, a command and its output, a measurement, a screenshot path. A PASS without evidence is a FAIL. A skipped item is a FAIL.
2. **Functional is not finished.** The gate applies even when every check is green.
3. **The written spec beats the reflex.** Reviewer and implementer read the spec and rule files literally before judging; list each named requirement and mark it delivered or not.
4. **Devil's advocate, at least three.** Before delivery, the implementer hunts at least three candidate defects and fixes or justifies each in writing. The reviewer does the same independently. The list is never empty.
5. **Honesty.** A known gap is named, never called done. Placeholders are listed. **Ambiguous counts as FAIL**, and a FAIL is never softened into a note.
6. **Independence.** The reviewer is not the implementer: a separate agent with read-only tools, given the diff and the checklist, not the implementer's reasoning.
7. **Evidence of what ran.** The reviewer's model tier matters: never pass a cheaper `model` to a guardian spawn.

## Running a gate (fan out)

1. **Implementer** finishes, runs the checks, writes the devil's advocate list.
2. **Mechanical gates, once**, by the main session (never once per guardian): the project's checks plus `bash <kit>/scripts/precommit_dispatch.sh --config precommit.json` on the staged set. Record each exit code. A 2 (could not run) is fixed or reported as a gap, never read as a pass.
3. **Dispatch guardians in parallel**, one per touched area (read-only, so parallel is safe). Each brief carries: the diff or paths, the checklist path, the rule files for those paths, the acceptance criteria, and the mechanical gate results from step 2 so guardians do not re-run them. Never pass a cheaper `model` to a guardian spawn.
4. **Merge to one verdict.** PASS only if every required guardian returned PASS and every mechanical gate exited 0. List blocking items from all guardians, deduplicated, with their evidence. Conflicting verdicts on the same item resolve to FAIL until a verifier or the human settles it.
5. **Any FAIL:** implementer fixes, then re-run step 2 and only the guardians whose areas the fix touched. Do not argue a FAIL away in chat; fix it, or record a decision that changes the checklist.
6. **Save the run record** and present it to the human. Ship only on the merged PASS, per the project's ship rule.

When to run which guardian is project policy; put it in the CLAUDE.md snippet (for example: every user visible change runs the UX guardian; every auth or data change runs the security guardian; every release runs the full set).

## Wiring the mechanical gates

- **Git hooks.** Copy `templates/githooks/` to `.githooks/` and `templates/precommit.json` to the repo root, then wire once per clone: `git config core.hooksPath .githooks` (or a package.json `"prepare": "git config core.hooksPath .githooks"` script so installs wire it). Pre-commit validates only: it never formats, fixes or re-stages, and it refuses staged `.env` files except `*.example`. Pre-push fetches and blocks when the branch is behind its remote or the push is not a fast forward (no force push), then refuses decision placeholders.
- **Agents never pass `--no-verify`.** A failing hook is a finding to fix.
- **Invariants on commit.** `invariants.json` maps trigger globs to regexes each staged file must or must not contain (for example "UTMs only via lib/utm", "no hardcoded budgets"). Run it from pre-commit, and optionally as a Claude Code PreToolUse hook that fires only on `git commit` (`templates/hooks/invariants-pretooluse.json`): a violation returns a deny decision naming the rule id and file, so the agent sees why.
- **Local gate.** `gate.py` runs `gate.steps` from `workflow-kit.json` on a clean clone of HEAD, so uncommitted files cannot make it pass. `--record` appends cleared SHAs to `gate/cleared.txt` (ship only cleared commits); `--parity` fails when CI runs a command the gate lacks. It is the authority when CI minutes are scarce; CI is the second opinion.
- **CI starter.** `templates/ci/ci.yml` (read only token, SHA pinned actions, docs only pushes skipped, concurrency, off the hour weekly run, `vars.CI_RUNNER` self hosted fallback) and `templates/ci/dependabot.yml` (actions only, monthly, at most 3 PRs).
- **Workflow lint.** `check_workflows.py` on `.github/workflows/**`: duplicate keys, missing `on`, `jobs` or `permissions:`, untrusted `${{ github.event.* }}` or `${{ inputs.* }}` inside `run:`, status functions outside `if:`, third party actions not pinned to a SHA.
- **Destructive scripts** (anything that rewrites files in bulk, such as `doc_numbers.py --assign`) are dry run by default and write only with `--apply --yes`.

## The regression library

Every new bug class becomes a permanent check. A bug class is the general shape ("a decision made before an await and trusted after it", "a cache that outlives its owner", "a gate that cannot fail"), not the single instance.

Entry format:

```markdown
- **R-NEW<n> (<short name>):** <the check, stated as a test a reviewer can run>. Detect: <grep, test, probe or manual step>. Origin: <commit or ADR, date>.
```

- Use `R-NEW<n>` placeholders while working; `doc_numbers.py --assign` numbers them at push time.
- Prefer a mechanical detector (a test, a lint rule, a script) over a manual step. When a detector exists, the entry names it.
- Guardians run the whole library on every review and mark each entry applies or not.
- Never delete an entry. Retire it with a status line and a reason (for example "superseded by lint rule X").

## Pre-mortem audit round (optional, periodic)

Once a month or before a major release: split the repo into lanes, give each lane a read-only auditor (`verifier` or `reviewer` on the strongest model, three at a time at most) hunting latent bugs with proof, verify every finding before touching code, fix each with a test that fails first, turn each class into a regression entry, and ship once through every gate. Zero findings is acceptable for a lane if the lane says what it verified.
