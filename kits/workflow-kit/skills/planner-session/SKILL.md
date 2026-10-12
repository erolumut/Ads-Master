---
name: planner-session
description: Plan first workflow for any non-trivial change. Use when the user asks to plan, design, scope or think through a feature or refactor before coding, when a task touches several files or a contract, when requirements are ambiguous, or when a next session prompt says to enter plan mode. Explore, design with alternatives, ask clarifying questions in small groups, write the final plan file, get approval, then implement.
---

# Planner session

Plan before code whenever a change touches more than a couple of files, a contract other code depends on, data, or anything the human will see. The plan is cheap; a wrong implementation is not.

## Phases

### 1. Explore (understand before proposing)
- Run the session start ritual first.
- Map the current code, patterns and docs for the area. Use `scout` workers in parallel for WHERE questions `log-triage` for CI and test output, and `data-extractor` for data dumps. Do the understanding yourself.
- Read the area's `.claude/rules/*.md` and direction docs explicitly with the Read tool: path scoped rules do not load while you plan from docs.
- Do not plan inside the built-in Plan or Explore agents when the plan depends on CLAUDE.md or rules: they skip CLAUDE.md.

### 1b. Legacy code: build an impact map before any design
When the change touches code nobody on the team wrote recently, code without tests, or code the plan cannot explain from a quick read, write an impact map into the plan before proposing anything. Agents skim old repositories, and that is where the guesses hide.

Scope is the blast radius, not the whole repository: the code the task touches, plus its callers and dependents one to two levels out. "Map the entire codebase" produces a skim, which is the failure this step prevents.

| Column | What goes in it |
|--------|-----------------|
| Touched code | `file:line` of each function, component, query, migration or config the task changes |
| Callers and dependents | Found by grep, editor references or the type checker, each listed with `file:line` |
| Side effects | Writes to the database, files, network calls, global or module state, caches, events, scheduled jobs |
| Tests protecting it | Test file and case names; "none" when none |
| Dead code | Only with proof (no references, no dynamic entry point, no config or route pointing at it); delete in its own commit |
| Evidence | `PROVEN` (a line was read that shows it) or `GUESS` (inferred, not read) |

Rules:
- Every row says PROVEN or GUESS. A claim with no line behind it is a GUESS, however likely it sounds.
- Reading code cannot prove everything: dynamic dispatch, reflection, string built queries, config or database driven behaviour, cron jobs, webhooks and other services calling in. Mark those GUESS and list how to settle them.
- Before any edit, each GUESS becomes either a characterization test (a test that pins today's behaviour, even where that behaviour looks wrong, so a change that breaks it fails loudly) or an open question for the human.
- Send the map to a `verifier` before the human sees it: it tries to refute the PROVEN rows and hunts for callers the map missed. A `scout`'s "no other callers" is never final on its own.
- No code edits until the human approves the map and the plan. Plan mode, where available, enforces this.
- Template: `<kit>/templates/IMPACT-MAP.md`.

### 2. Design with alternatives
- Write two or three real alternatives, not one option and two strawmen. For each: what it is, pros, cons, effort, risk, what it closes off later.
- Research market or library practice where it matters (`researcher` workers, one question each). Best practice is the target, not a template: adapt it to this codebase.
- Mark your recommendation and the strongest argument against it.
- For hard-to-reverse choices, consult `fable-advisor` (or the advisor tool) here, before the human sees the options.

### 3. Clarifying questions (small groups)
- Ask in groups of three to four questions at most, in `language.human`. Each question offers concrete options with honest tradeoffs, not a sales pitch.
- Never proceed on an empty assumption. If the human is away, write the open questions into the plan and stop.

### 4. Final plan file
Write or update the plan file (conventions below). Keep the master plan; add detail for the new work only.

### 5. Approval
Present the plan (exit plan mode if you used it) and wait for explicit approval. Approval of a plan is not approval of irreversible operations inside it; those still get announced.

### 6. Implement
Follow the plan. A deviation discovered during implementation is a stop point: update the plan and the decision log, then ask if the deviation changes scope, contracts or user visible behavior.

## Plan file conventions

- Location: `docs/plans/<YYYY-MM-DD>-<slug>.md` (or the project's plan folder). One file per piece of work; a long program has one master plan plus phase files.
- Header: title, date, author session handle, status (`draft`, `approved <date>`, `in progress`, `done`, `superseded by <file>`), the HEAD it was written against.
- Sections, in this order:
  1. **Goal and intent** (why, for whom, how it should feel).
  2. **Current state** (what exists, with `file:line` evidence; for legacy code, the impact map from phase 1b).
  3. **Alternatives considered** (table) and **decision** with reason.
  4. **Scope**: in, out, doors.
  5. **Phases** with owned files per phase, atomic commits, verification gate per phase.
  6. **Risks and rollback**.
  7. **Open questions** (with who answers).
  8. **Decision log entries** to write (`ADR-NEW<n>` placeholders).
- Separate facts (measured, read) from proposals. Never present a proposal as a finding.
- When work spans several sessions, generate the per phase delegation prompts from the plan (`sprint-prompt` skill).
