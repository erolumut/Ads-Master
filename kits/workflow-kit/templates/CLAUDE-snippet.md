<!-- Workflow Kit snippet. Paste into CLAUDE.md and fill the <placeholders>. Keep it short: the details live in the kit's skills. This comment is stripped before the model sees the file. -->

## How we work (Workflow Kit)

- **Language:** talk to the human in <language.human>, every message and question. Code, identifiers, commits, docs and rule files in <language.artifacts>.
- **Nothing here is law:** if you see a better approach, say so before implementing, with the tradeoff. If accepted, record a decision that supersedes the old one.
- **Session start:** skill `session-start`. Read order: CLAUDE.md -> <roadmap> -> <decision log> index + last 5 -> <tracker> -> parallel check -> ledger CHECK-IN (`PARALLEL-SESSIONS.md`, git-ignored). Big docs by index and offset, never whole.
- **Plan first** for anything beyond a small fix: skill `planner-session`.
- **Models:** aliases only (`fable`, `opus`, `sonnet`, `haiku`). Routing, escalation and fan out: skill `model-routing`. Spawn named agents; pass `model` explicitly on any unnamed spawn, never on a reviewer or verifier. Cheaper output counts only after a mechanical gate or verification. "Not found" from a cheaper model goes to `verifier`.
- **Project routing specifics:** red-line areas (always `implementer` on opus): <paths>. Mechanic allow list: `workflow-kit.json` -> `mechanic.allow`. Critical points for `fable-advisor`: <list>.
- **Parallel work:** skill `parallel-sessions`. Isolation: <shared tree | local clone on the same branch | worktree>. Stage paths explicitly; never `git add -A` while another session shares the tree.
- **Decisions:** `<DECISIONS.md>`; supersede, never delete; new numbers as `ADR-NEW<n>` / `R-NEW<n>`, assigned right before the push by `doc_numbers.py --assign`.
- **Done means reviewed:** skill `review-gates`. "Looks good" is banned; every PASS cites evidence. Every new bug class becomes a regression entry.
- **Handover:** skill `handover`. Pointer: `NEXT-SESSION-PROMPT.md`.
- **Instructions budget:** this file stays under <maxLines> lines; area rules live in `.claude/rules/` (read the area's file explicitly before planning or reviewing it): <rule index>. Check: `check_instructions.py`.
- **Checks:** <TYPECHECK_COMMAND> · <LINT_COMMAND> · <TEST_COMMAND> · <BUILD_COMMAND>.
