# Sprint <ID>: <name> (<version or milestone>, <area tag>, <FULL | MEDIUM | BRIEF>)

> Language: talk to the human in <language.human>. Code, docs, commits and identifiers in <language.artifacts>.

## 0) Intent: why this sprint exists

<Two to four paragraphs. When this is done, what changes for the user or the business? How should it feel?
What does the human care about most here? The project in one sentence. The principles that apply.>

## 1) Context reading (required, in order)

CLAUDE.md -> <roadmap file> -> <decision log> (index + last 5 entries) -> <tracker>
-> docs that feed this sprint: <specs, research notes, direction docs>
-> rule files for the paths you will touch: <.claude/rules/<area>.md, ...> (Read tool, by path)
-> session start ritual (parallel check + ledger CHECK-IN)

## 2) Plan first (no code yet)

- Verify every `⚠` assumption in this prompt against the decision log and the real code.
- Targeted mini research only where needed (library version, API state). Not broad research.
- Write a short implementation plan. A deviation from spec or plan is a STOP POINT: propose it in the decision log and ask the human.

## 3) Scope

**In:** <the work of this sprint>
**Out:** <deliberately not done; the boundary is explicit>
**Doors:** <cheap hooks this sprint must leave open, one line each: what it stays open for>

## 4) Work list

<In priority order. Each item with its own verification next to it.>

1. <item> · verify: <test name | command | evidence type>
2. <item> · verify: <...>

## 5) Definition of done and ship

- <TYPECHECK_COMMAND>, <LINT_COMMAND>, <TEST_COMMAND>, <BUILD_COMMAND> green.
- Review gates passed with evidence: <guardians that apply>.
- Tracker status updated; handover pointer moved to the next prompt.
- At least one decision log entry (ADR format if a decision was made; `ADR-NEW<n>` placeholders until push).
- Ship per the project rule: <ship rule>.

## 6) Guardrails

- <sprint specific prohibition, at least one real one>
- <standing guardrails from CLAUDE.md that matter most here>
- Read the stale knowledge guards (<AGENTS.md or docs/STALE-GUARDS.md>) before writing code against <libraries>.
