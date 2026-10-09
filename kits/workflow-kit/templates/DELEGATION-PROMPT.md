# <Feature or program>: Phase <X> (<phase name>) delegation prompt

> One phase, one session. Paste the block below into a new session. This phase stays in its own atomic scope and never does a later phase's work. No commit without a green verification gate.

```
<Feature> Phase <X> (<phase name>) starts now.

Read first:
1. <plan file path>: the sections "<architecture section>" and "Phase <X>".
2. <spec or catalog path>: the canonical reference for <what>.
3. CLAUDE.md + the session start ritual (parallel check, ledger CHECK-IN).
4. Reference files to copy patterns from: <path>, <path>.
5. Rule files for the paths you will touch: <.claude/rules/<area>.md> (Read tool, by path).

Pre-flight (required):
- Parallel check: git fetch --all; git log --all --oneline -20; ledger re-read.
- Reserved slots or numbers: <migration slots, placeholders>; verify nobody took them.
- Snapshot before any data change: <SNAPSHOT_COMMAND>.

Task (one atomic commit each):
P1. <type>: <subject>
P2. <type>: <subject>
P3. <type>: <subject>

Verification gate (before every commit):
- <TYPECHECK_COMMAND>
- <LINT_COMMAND>
- <TEST_COMMAND>
- <PHASE_SPECIFIC_CHECK>

Out of scope for Phase <X> (do not do):
- <Phase Y work>
- <Phase Z work>

On completion:
- Push the atomic commits per the project's ship rule.
- Mark "Phase <X> done" in the plan file (a short note).
- Start the Phase <next> session with its prompt from this file.

Ambiguity: ask the human in small groups of questions. Do not guess your way into code.
```
