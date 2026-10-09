---
name: session-start
description: Session start ritual. Use at the start of every new session in a project that adopted Workflow Kit, after a resume or compaction that lost context, when the user says start, continue, pick up where we left off, or pastes a next session prompt. Reads the project docs in order, reads big docs by index and offset, checks for parallel sessions and checks in to the ledger before any edit.
---

# Session start

Do these steps in order before the first edit. They cost a few minutes and prevent the two expensive failures: working from stale context and colliding with another session.

## 1. Read order

Read in this order; stop at what does not exist. The project may override the list in its CLAUDE.md snippet.

1. `CLAUDE.md` (auto-loaded; reread the routing and git sections if the session was compacted).
2. The roadmap or status file (`ROADMAP.md` or whatever the project names): the active version and phase.
3. The decision log index plus the **last five entries** (`DECISIONS.md` or `LEARNINGS.md`).
4. The sprint or work tracker: the active item and its status. Status lives in one file only.
5. The handover pointer (`NEXT-SESSION-PROMPT.md`) and the prompt it points to, if you were not handed one.
6. The rule files under `.claude/rules/` and direction docs for the area you will touch, with the Read tool.
7. `AGENTS.md` or the stale knowledge guards file, if the project has one.

## 2. Big docs by index and offset

Never read a large doc whole.

- Find the index: `grep -n "^## " DECISIONS.md | head -50` or the file's index table.
- Read the index, then the entries you need with `Read` and `offset`/`limit` (line numbers from the grep).
- For the last N entries: `grep -n "^## ADR-" DECISIONS.md | tail -5`, then read from the first of those lines.
- Rule of thumb: over about 1,000 lines or 100 KB, index and offset only.

## 3. Parallel check

```bash
git fetch --all --prune
git status --short
git log --all --oneline -20
git log --all --since="2 hours ago" --oneline
git stash list
git worktree list
```

- Uncommitted changes you did not make, recent commits from elsewhere, extra worktrees or clones in the ledger mean another session may be active.
- While another session is active, never run an automatic `git stash` and pop: it carries the other session's work-in-progress.
- Divergent branches or unknown work in progress: ask the human before touching it.

## 4. Ledger check-in

Use the `parallel-sessions` skill. Short version:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/scripts/ledger.py" checkin --handle <you> --scope "<files or dirs>" --intent "<one line>" --risky "<none|push|migration|shared doc>" --eta "<~2h>"
```

The ledger is a git-ignored file at the repo root (`PARALLEL-SESSIONS.md`), not under `.claude/`, which Claude Code treats as protected and may prompt on writes. Cloud sessions in fresh containers have no ledger; they coordinate through the tracker's status instead.

## 5. Confirm and start

Write a three line opening note to the human, in the language set in `workflow-kit.json` (`language.human`):

1. What you read and the active item.
2. Parallel state (alone, or who else is active and their scope).
3. What you will do first, or the plan mode step you are entering (`planner-session` skill).
