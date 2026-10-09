# Next session pointer

> This file only points. The prompt lives in <handover.promptsDir>; status lives in <tracker>. The session that finishes a piece of work moves this pointer (definition of done).

## Next: **<ID or name>** · `<docs/prompts/<file>.md>`

<One line on why this is next.>

> **Closed <YYYY-MM-DD>:** <previous item> (<decision ids>). Landmines for the next session: <one line or "none">. Handover: `<docs/handover/<file>.md>`.

---

## Paste-ready prompt (use when no sprint prompt exists)

```
We continue <PROJECT_NAME> together with your previous sessions. Follow these steps exactly.

FIRST (order matters):
1. Read CLAUDE.md.
2. Read <roadmap file>: which phase, what is open, the last commit.
3. Read <decision log>: index + last 5 entries (by offset, never whole).
4. Read <tracker> and the handover: <docs/handover/<file>.md>.
5. Read the rule files for the area: <.claude/rules/<area>.md> (Read tool).
6. Session start ritual: parallel check + ledger CHECK-IN.

THEN FOR THIS WORK (plan first):
A. Explore: map the current code and docs (scout workers for WHERE questions).
B. Design: two or three real alternatives with tradeoffs; pick the simplest production grade one.
C. Questions: ask me in small groups (3 to 4 at most). No empty assumptions.
D. Plan file: write or update <docs/plans/<file>.md>.
E. Approval: wait for my explicit approval, then implement.

TASK:
<what to do, in one paragraph, with the acceptance criteria>

RULES:
- Atomic commits; checks green before each: <TYPECHECK_COMMAND>, <LINT_COMMAND>, <TEST_COMMAND>.
- At least one decision log entry per phase; supersede, never delete; ADR-NEW<n> placeholders until push.
- Review gates before "done": <guardians>. "Looks good" is banned; evidence for every PASS.
- Talk to me in <language.human>.
- At the end: handover, next session prompt, move this pointer, ledger SIGN-OFF.
```
