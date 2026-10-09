---
name: decision-log
description: Architecture and process decision log (ADR) conventions. Use when a decision is made or changed, when the user says record this, add an ADR, supersede a rule, or when writing a new decision or regression rule while other sessions may also write some. Covers the entry format in DECISIONS.md or LEARNINGS.md, supersede never delete, ADR-NEW placeholder numbering assigned at push time, the index, and the doc_numbers.py check.
---

# Decision log

> **Kit path.** `<kit>` below is `${CLAUDE_PLUGIN_ROOT}` when the kit runs as a plugin, or `.claude/workflow-kit` when it was installed by copy. Every kit script exits 0 pass, 1 fail, 2 could not run; treat 2 as not passed.


One file holds the project's decisions: `DECISIONS.md` (or `LEARNINGS.md` if the project already uses it; set `decisions.files` in `workflow-kit.json`). It is the answer to "why is it like this?" and the place a session checks before changing direction.

Template: `templates/DECISIONS.md`.

## Entry format

```markdown
## ADR-012: <decision in one line>

- **Date:** 2026-10-09 · **Status:** accepted | superseded by ADR-019 | proposed
- **Context:** the problem and the forces, with evidence (`file:line`, numbers with source and date).
- **Decision:** what we do, stated so a reader can follow it.
- **Alternatives:** what else was considered and why not.
- **Consequences:** what gets easier, what gets harder, what to watch.
- **Supersedes:** ADR-007 (if any).
```

And one index row per entry, in the index table at the top:

```markdown
| 012 | Decision in one line | accepted | 2026-10-09 |
```

## Rules

1. **Supersede, never delete.** A changed decision gets a new entry. The old entry's status becomes `superseded by ADR-<new>`; its text stays. History is the point.
2. **Decide before code.** A design or direction change is written (or proposed) in the log first, then implemented.
3. **Nothing is law.** Anyone (human or agent) who sees a better approach proposes it with the tradeoff before implementing. If accepted, it becomes a new entry that supersedes the old one.
4. **At least one entry per phase** of work: a decision, or a learning (a pattern, a pitfall, a bug class).
5. **Big file discipline.** The index stays at the top; sessions read the index and the last five entries by offset, never the whole file.
6. **Owner decisions are quoted.** When the human decides, record who, when, and their words in short.

## Placeholder numbering (ADR-NEW<n>)

Taking "the next number" when you start writing collides with any other session that did the same. The next free number is only known when the work reaches the main branch, so that is when it is given.

1. **While working**, write `ADR-NEW<n>` for new decisions and `R-NEW<n>` for new regression or QA rules, with `n` = 1, 2, 3 in your session: in the heading (`## ADR-NEW<n>: ...`), the index row (`| ADR-NEW<n> | ... |`), the rule line and every reference, code comments included. Prose that describes the syntax writes a literal `<n>`, which the tool ignores.
2. **Right before the push** to the main branch: fetch and integrate the main branch first, then
   ```bash
   python3 <kit>/scripts/doc_numbers.py --assign            # dry run: shows the mapping
   python3 <kit>/scripts/doc_numbers.py --assign --apply --yes  # writes
   ```
   Each placeholder becomes the highest existing number plus 1, plus 2, in `n` order, in every scanned file that names it. Commit, push.
3. **The gate:** `doc_numbers.py --check` fails on duplicate entry numbers, duplicate index rows, an entry without an index row or a row without an entry, and duplicate rule numbers. Add `--no-placeholders` in a pre-push hook or CI so no placeholder reaches the main branch.
4. **Collision anyway** (two sessions numbered in the same minute): the number already on the main branch stays. Turn yours back into a placeholder and run `--assign` again.

The same pattern works for any number that must be unique across sessions (migration slots, rule ids): reserve late, assign at integration.

## Index

Keep the index table between `## Index` and the first entry. The checker reads rows of the form `| 012 |` or `| ADR-NEW<n> |` in that section.
