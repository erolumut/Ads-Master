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
  2. **Current state** (what exists, with `file:line` evidence).
  3. **Alternatives considered** (table) and **decision** with reason.
  4. **Scope**: in, out, doors.
  5. **Phases** with owned files per phase, atomic commits, verification gate per phase.
  6. **Risks and rollback**.
  7. **Open questions** (with who answers).
  8. **Decision log entries** to write (`ADR-NEW<n>` placeholders).
- Separate facts (measured, read) from proposals. Never present a proposal as a finding.
- When work spans several sessions, generate the per phase delegation prompts from the plan (`sprint-prompt` skill).
