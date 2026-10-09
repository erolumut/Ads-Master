---
name: parallel-sessions
description: Protocol for running several Claude Code sessions on one repository without collisions. Use when more than one session is or may be active, before risky operations (commit, push, branch switch, migration, shared doc edit), when the user asks to work in parallel, split work across sessions, isolate a session, use a worktree or local clone, or when the ledger file PARALLEL-SESSIONS.md is mentioned.
---

# Parallel sessions

Two sessions on one tree collide in quiet ways: one stages the other's files, one stashes the other's work-in-progress, two take the same migration or decision number, one commits on the wrong branch. Detection (`ps`, branch lists) is not enough. Sessions must **talk** through a shared ledger and, when they must not share a tree, **isolate**.

## 1. The ledger

- File: `PARALLEL-SESSIONS.md` at the repo root (path configurable as `ledger.path` in `workflow-kit.json`). Add it to `.gitignore`. Do not put it under `.claude/`: writes there may trigger permission prompts.
- Template: `templates/PARALLEL-SESSIONS.md` in this kit. Create with `ledger.py init`.
- Sections: **ACTIVE** (one block per live session), **MSG** (messages between sessions), **ARCHIVE** (signed off blocks).
- Append only. Never delete or rewrite another session's block.
- One machine only. A cloud session in a fresh container has no ledger; it coordinates through the tracker's status column and the human.

## 2. Protocol

| Step | When | What |
|---|---|---|
| **CHECK-IN** | session start, before the first edit | Read the ledger, then add your block: handle, timestamp, branch, working dir, scope (files or dirs), intent (one line), risky ops planned, ETA |
| **RE-READ** | before every risky op: commit, push, branch switch, migration or schema change, number assignment, shared doc edit | Re-read the ledger and run `git branch --show-current` and `git status --short` |
| **PROGRESS** | at phase boundaries and before `/compact` | One line under your block: what is done, what is next |
| **MSG** | your lane overlaps another's | `MSG @you -> @them: <what, which files, proposal>`. If no answer and the overlap is real, ask the human |
| **SIGN-OFF** | when you finish | Done, left open, landmines (things the next session must know), clones or ports cleaned up |
| **ARCHIVE** | right after SIGN-OFF | Move your block from ACTIVE to ARCHIVE |

Commands (`${CLAUDE_PLUGIN_ROOT}/scripts/ledger.py`, or the copied path):

```bash
python3 ledger.py init                     # create from the template if missing, add to .gitignore with --gitignore
python3 ledger.py checkin --handle api-fix --scope "src/api/**" --intent "fix pagination" --risky push --eta 2h
python3 ledger.py progress --handle api-fix --note "tests green, docs next"
python3 ledger.py msg --from api-fix --to ui-pass --text "I own src/api/client.ts until 15:00"
python3 ledger.py signoff --handle api-fix --done "pagination fixed" --left "none" --landmines "cache key changed"
python3 ledger.py show
```

`signoff` appends the SIGN-OFF lines and moves the block to ARCHIVE in one step.

## 3. Hard rules while another session is active

- Never `git stash` plus pop automatically: it carries the other session's uncommitted work.
- Stage paths explicitly. Never `git add -A` or `git commit -a`.
- Never reset, checkout or clean files outside your scope.
- Numbers that must be unique (decisions, rules, migrations) are placeholders until the push (`decision-log` skill).
- One session pushes at a time: the one about to push writes `push in progress` in its PROGRESS line.

## 4. Isolation options

Pick by what the project allows. Record the choice in the decision log.

### A. Shared tree, disjoint files
Cheapest. Works when scopes are disjoint and both sessions follow section 3. Fails under heavy churn or when one session runs a formatter over everything.

### B. Local clone, same branch (no branches, no worktrees)
For projects that keep everything on one branch.

1. `git clone <main-checkout> ../<repo>-<handle>`. A plain local clone (hardlinked objects). Never `--shared`: the source's garbage collection can prune objects the clone borrows.
2. `git -C ../<repo>-<handle> remote set-url origin "$(git -C <main-checkout> remote get-url origin)"`, then in the clone `git fetch origin && git reset --hard origin/<main-branch>` (only in the fresh clone).
3. Copy what a clone lacks: local env files, hook config (`git config core.hooksPath <dir>` if the project uses one). Install dependencies.
4. Name the clone in your CHECK-IN. Work, commit and run the gates there. Never edit the other tree.
5. Push from the clone with the normal ritual (fetch, rebase unpublished commits, assign placeholders, one push). The main checkout picks commits up with its own fetch.
6. At SIGN-OFF, delete the clone and any ports or build dirs it used, and say so in the ledger.

### C. Git worktree
For projects that allow short lived branches.

1. `git worktree add ../<repo>-<handle> -b <handle>/<topic>` (or let a subagent use `isolation: worktree`).
2. Record it in CHECK-IN. Merge back with the project's usual method.
3. Whoever finishes removes it in the same turn: `git worktree remove ../<repo>-<handle>`. Check `git worktree list` at every session start; no idle worktrees.

## 5. Conflict playbook

| Symptom | Action |
|---|---|
| Files you need appear in another ACTIVE scope | MSG first; wait or split the file ownership explicitly |
| Uncommitted changes you did not make | Do not touch, stage or stash them; ask in MSG or ask the human |
| Push rejected (non-fast-forward) | Fetch, rebase your unpublished commits, re-run checks, re-assign placeholders, push |
| Same number taken by both | The number already on the main branch stays; revert yours to a placeholder and re-assign |
| A stale ACTIVE block (hours old, process gone) | Ask the human before archiving someone else's block |
