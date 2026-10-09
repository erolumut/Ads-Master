---
name: review-gates
description: Guardian and reviewer pattern for calling work done. Use before declaring a deliverable done, before merging or shipping a risky change, when setting up review checklists or named guardians, when a bug escaped and its class must never return, or when the user asks for a review, audit, quality gate or second check. Evidence based PASS, devil's advocate three defect hunt, and a regression library that grows with every new bug class.
---

# Review gates

Green checks prove the code compiles and the tests you wrote pass. They do not prove the work is finished. A review gate is a written checklist plus an independent reviewer that must cite evidence for every PASS.

## Pieces

| Piece | What | Where |
|---|---|---|
| **Checklist** | Written criteria for an area (functional, UX, security, performance, accessibility, scope) | `docs/review/<AREA>-CHECKLIST.md`, registered in `workflow-kit.json` under `reviewers` |
| **Regression library** | One entry per bug class that ever escaped; permanent | `docs/review/REGRESSIONS.md` (`reviewers.regressionLibrary`) |
| **Guardian** | A reviewer agent bound to one checklist | copies of the kit's `reviewer` agent: `security-guardian`, `a11y-guardian` |
| **Gate run record** | The filled checklist with evidence | `docs/review/runs/<date>-<slug>.md` |

Template for the checklist: `templates/REVIEW-CHECKLIST.md`.

## Rules

1. **"Looks good" is banned.** Every PASS cites evidence: `file:line`, a command and its output, a measurement, a screenshot path. A PASS without evidence is a FAIL. A skipped item is a FAIL.
2. **Functional is not finished.** The gate applies even when every check is green.
3. **The written spec beats the reflex.** Reviewer and implementer read the spec and rule files literally before judging; list each named requirement and mark it delivered or not.
4. **Devil's advocate, at least three.** Before delivery, the implementer hunts at least three candidate defects and fixes or justifies each in writing. The reviewer does the same independently. The list is never empty.
5. **Honesty.** A known gap is named, never called done. Placeholders are listed.
6. **Independence.** The reviewer is not the implementer: a separate agent with read-only tools, given the diff and the checklist, not the implementer's reasoning.
7. **Evidence of what ran.** The reviewer's model tier matters: never pass a cheaper `model` to a guardian spawn.

## Running a gate

1. Implementer finishes, runs the checks, writes the devil's advocate list.
2. Main session spawns the guardian(s) for the touched areas, in parallel (read-only), each with: the diff or paths, the checklist path, the rule files for those paths, the acceptance criteria.
3. Each guardian returns PASS or FAIL with a checklist table, a regression table and its own devil's advocate list.
4. Any FAIL: implementer fixes, the guardian re-runs on the new diff. Do not argue a FAIL away in chat; either fix it or record a decision that changes the checklist.
5. Save the run record. Ship only on PASS from every required guardian.

When to run which gate is project policy; put it in the CLAUDE.md snippet (for example: every user visible change runs the UX guardian; every auth or data change runs the security guardian; every release runs the full set).

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
