---
name: instructions-budget
description: Keep CLAUDE.md lean and instructions effective. Use when CLAUDE.md grows past its budget, when instructions are being ignored, when adding a new rule, when restructuring project instructions, when moving area rules into path scoped .claude/rules files, when adding stale training data guards, or when running the check_instructions.py budget check.
---

# Instructions budget

> **Kit path.** `<kit>` below is `${CLAUDE_PLUGIN_ROOT}` when the kit runs as a plugin, or `.claude/workflow-kit` when it was installed by copy. Every kit script exits 0 pass, 1 fail, 2 could not run; treat 2 as not passed.


Every line of CLAUDE.md loads into every session and every subagent. Long files cost context and reduce adherence. The docs recommend under 200 lines per CLAUDE.md; Claude Code warns at startup when a file, or the combined set, runs long.

## Where an instruction belongs

| Kind | Home | Loads |
|---|---|---|
| Applies to every session, every area (language, routing, git, ship rules, invariants) | `CLAUDE.md` | always |
| Applies to one area of the code | `.claude/rules/<area>.md` with `paths:` frontmatter | when a matching file is read or edited |
| Applies everywhere but is long reference | a doc, linked by path from CLAUDE.md | when someone reads it |
| History, reasons, superseded rules | decision log | when someone reads it |
| Procedures (a round, a release, a review) | a skill | when the skill triggers |
| Must be enforced, not just asked | a hook or a check script | always, deterministically |
| Model knowledge known to be stale | the stale guards file (`AGENTS.md` or `docs/STALE-GUARDS.md`), imported from CLAUDE.md | always |

`@path` imports organize a file but do not reduce its cost: imported files load at launch.

## Path scoped rules

```markdown
---
paths:
  - "src/api/**/*.ts"
  - "src/**/*.{ts,tsx}"
---

# API rules
1. ...
```

- A rule with `paths:` loads when Claude reads, writes or edits a matching file (also `cat` or `head` on a single file). A rule without `paths:` loads every session, like CLAUDE.md.
- Rules do not load while planning from docs, and compaction summarizes them away. So briefs name the rule files and workers read them explicitly with the Read tool before the first edit. CLAUDE.md carries a one line index of rule files ("before planning or reviewing an area, read its rule file").
- Brace expansion works (`*.{ts,tsx}`). A pattern with an unbalanced `[` matches nothing.
- Block level HTML comments (`<!-- ... -->`) are stripped before the model sees CLAUDE.md. Use them for provenance notes ("moved from CLAUDE.md on <date>, see ADR-<n>") at zero token cost.

## Stale knowledge guards

A short file of "your training data is out of date here" warnings, one bullet each, for the libraries and platforms the project uses: the current major version, the pattern that changed, the pattern not to write, and where to read the truth (installed package docs, official docs). Date it ("state as of <month year>"). Import it from CLAUDE.md with `@AGENTS.md` or keep it as `AGENTS.md`, which Claude Code can read directly. Review it when dependencies change major versions.

## Restructure procedure

1. Run `check_instructions.py` to see the line count and broken references.
2. Classify every CLAUDE.md block with the table above.
3. Move area blocks into `.claude/rules/<area>.md` with tight `paths:` globs; leave a one line pointer in CLAUDE.md's rule index.
4. Move history and reasons to the decision log; leave the rule, drop the story.
5. Record the restructure as a decision entry.
6. Run the check again and wire it into a pre-commit hook or CI.

## The check script

```bash
python3 <kit>/scripts/check_instructions.py            # report, exit 1 on errors
python3 <kit>/scripts/check_instructions.py --strict   # warnings fail too
```

It checks: the CLAUDE.md line budget (`instructions.maxLines`, default 200, counted without block HTML comments), that every referenced path (backtick spans and `@imports` that look like paths) exists, and that every `.claude/rules/*.md` has valid frontmatter with valid globs. A glob that matches no file is a warning (an error with `--strict`). Paths to ignore go in `instructions.ignorePaths`.
