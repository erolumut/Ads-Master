# Workflow Kit

A plug and play Claude Code plugin that makes any software or growth project easier to develop with Claude. It packages working rituals that grew out of long running, multi session projects and strips them of everything project specific:

- **Model routing and delegation**: which work goes to which agent and model, when cheaper output counts, escalation, fan out with disjoint ownership.
- **Parallel sessions**: a ledger protocol so several sessions share one repo without collisions, plus clone and worktree isolation.
- **Prompt writing**: a 7 block sprint prompt, per phase delegation prompts, depth levels and a finalize ritual.
- **Planning sessions**: explore, design with alternatives, ask in small groups, plan file, approval, then code.
- **Session start and handover**: a read order, big docs by index and offset, a handover note, a next session prompt and a pointer file.
- **Decision logs**: ADR entries, supersede never delete, placeholder numbers assigned at push time.
- **Instruction budgets**: a lean CLAUDE.md, path scoped rules, stale knowledge guards, a check script.
- **Review guardians**: evidence based PASS, a devil's advocate hunt, a regression library that grows with every bug class.

Nothing in the kit assumes a language, framework, product or company. Project facts live in your repo (`workflow-kit.json`, your CLAUDE.md, your docs); the kit holds only the generic method.

## Contents

```
workflow-kit/
├── .claude-plugin/plugin.json
├── agents/          scout, data-extractor, researcher, mechanic, verifier, fable-advisor, implementer, reviewer
├── skills/          model-routing, session-start, parallel-sessions, sprint-prompt, planner-session,
│                    handover, decision-log, instructions-budget, review-gates
├── scripts/         doc_numbers.py, check_instructions.py, ledger.py, agent_models.py (+ tests/)
└── templates/       workflow-kit.json, CLAUDE-snippet.md, settings-snippet.json, PARALLEL-SESSIONS.md,
                     SPRINT-PROMPT.md, DELEGATION-PROMPT.md, HANDOVER.md, NEXT-SESSION-PROMPT.md,
                     DECISIONS.md, REVIEW-CHECKLIST.md, STALE-GUARDS.md
```

## Install

### As a plugin (recommended)

Once the Ads Master marketplace lists the kit:

```
/plugin marketplace add erolumut/Ads-Master
/plugin install workflow-kit@ads-master
```

For a local checkout, load it directly: `claude --plugin-dir /path/to/Ads-Master/kits/workflow-kit`.

Plugin components are namespaced: the agents appear as `workflow-kit:scout`, `workflow-kit:verifier` and so on. Skills and agents can reference kit files through `${CLAUDE_PLUGIN_ROOT}`. That variable is not set inside Bash tool commands, so when you run a script by hand, use the installed path (shown by `/plugin`) or a copy.

### By copy (the Ads Master installer)

```bash
scripts/install.sh --kit workflow /path/to/your-project
```

This copies agents into `.claude/agents/`, skills into `.claude/skills/`, and scripts and templates into the project, where agents keep their bare names (`scout`, `verifier`). Check the installer's help for the exact target folders. Use the copy route when you want to edit the agents per project, or when your agents need `hooks`, `mcpServers` or `permissionMode` frontmatter, which Claude Code ignores for plugin agents.

### Requirements

- Claude Code with subagent `effort` and `disallowedTools` support. `fable` and the advisor tool need Fable access; without it, use `opus` for `fable-advisor` and leave `advisorModel` unset.
- Python 3.9 or later for the scripts. Standard library only.

## What each piece does

### Agents

| Agent | Model | Effort | Role | Edits files |
|---|---|---|---|---|
| `scout` | haiku | medium | WHERE questions: paths, lines, quotes. Never final on absence | no |
| `data-extractor` | haiku | medium | Facts and numbers from logs, CI output, CSV exports, API dumps. No diagnosis | no |
| `researcher` | sonnet | high | One cited, dated web question per spawn. The main session synthesizes | no |
| `mechanic` | sonnet | high | Bounded edits inside the `mechanic.allow` fence with a mechanical oracle. Two failures return the task | yes, fenced |
| `verifier` | opus | xhigh | Adversarial refutation of claims, findings, diffs, "fixed" and "not found" | no |
| `fable-advisor` | fable | xhigh | Second opinion at critical points only. Advises, never implements | no |
| `implementer` | opus | xhigh | Judgment heavy, multi file work with disjoint file ownership. Never commits | yes |
| `reviewer` | opus | xhigh | Guardian template: checklist from `workflow-kit.json`, evidence required, "looks good" banned | no |

Read-only agents carry an explicit `tools` list without `Agent`; editing agents set `disallowedTools: Agent`. Claude Code lets subagents spawn their own subagents by default, and this kit keeps the tree flat: workers report back, the main session spawns.

### Skills

| Skill | Use it when |
|---|---|
| `model-routing` | Spawning any subagent, picking a model, fanning out, escalating, compacting |
| `session-start` | Every new session: read order, parallel check, ledger CHECK-IN |
| `parallel-sessions` | More than one session on a repo; before risky ops; isolating with a clone or worktree |
| `sprint-prompt` | Writing or finalizing a sprint prompt or per phase delegation prompts |
| `planner-session` | Any non-trivial change: plan first, then code |
| `handover` | Ending a session: handover, next session prompt, pointer, SIGN-OFF |
| `decision-log` | Recording or changing a decision; placeholder numbering |
| `instructions-budget` | CLAUDE.md grows, instructions get ignored, rules move to `.claude/rules/` |
| `review-gates` | Before "done": guardians, evidence, devil's advocate, regression library |

### Scripts

Run from the project root (add `--help` for options). All read `workflow-kit.json` when present.

| Script | Does |
|---|---|
| `doc_numbers.py` | `--check` finds duplicate decision numbers, index orphans and duplicate rule numbers; `--no-placeholders` refuses any `ADR-NEW<n>` or `R-NEW<n>`; `--assign` numbers placeholders from the existing max |
| `check_instructions.py` | CLAUDE.md line budget, referenced paths exist, `.claude/rules` frontmatter and globs valid |
| `ledger.py` | `init`, `checkin`, `progress`, `msg`, `signoff` (moves the block to ARCHIVE), `show` |
| `agent_models.py` | Lists agents with pinned model and effort, flags full model ids, unpinned agents and agents that can spawn, shows model settings and env pins |

Tests: `python3 -m unittest discover -s scripts/tests`.

### Templates

| Template | Copy to |
|---|---|
| `workflow-kit.json` | project root, as `workflow-kit.json` |
| `CLAUDE-snippet.md` | paste into your CLAUDE.md |
| `settings-snippet.json` | merge into `.claude/settings.json` by hand. Not a drop-in file: its `"//"` key is a note for you; delete it after merging |
| `PARALLEL-SESSIONS.md` | created by `ledger.py init` |
| `DECISIONS.md` | project root (or merge into your existing LEARNINGS or DECISIONS file) |
| `SPRINT-PROMPT.md`, `DELEGATION-PROMPT.md` | your prompts folder, one per sprint or phase |
| `HANDOVER.md`, `NEXT-SESSION-PROMPT.md` | handover folder and project root |
| `REVIEW-CHECKLIST.md` | `docs/review/<AREA>-CHECKLIST.md`, one per guardian |
| `STALE-GUARDS.md` | `AGENTS.md` or `docs/STALE-GUARDS.md`, imported from CLAUDE.md |

## Adopt it gradually

Each step pays off on its own. Stop wherever the pain stops; add a step when its pain shows up, not before.

1. **Config and snippet.** Copy `workflow-kit.json`, fill the project name, checks and language. Paste `CLAUDE-snippet.md` into CLAUDE.md, keeping only lines for pieces you adopt.
2. **Model routing.** Install the agents. Start spawning `scout` and `data-extractor` for lookups and log reading, `verifier` for anything a decision rests on. Run `agent_models.py` once.
3. **Session start and handover.** Adopt the read order and the pointer file. This is the step that makes multi day work continuous.
4. **Decision log.** Add `DECISIONS.md`; record decisions as they happen; use placeholders from day one if more than one session ever writes.
5. **Planner session and sprint prompts.** Plan first for anything non-trivial; write prompts with the 7 blocks for work that spans sessions.
6. **Review gates.** Write one checklist for the area where bugs hurt most, copy `reviewer` into a named guardian, start the regression library with the last bug that escaped.
7. **Parallel sessions.** When you first run two sessions at once: ledger, then isolation (clone or worktree).
8. **Instruction budget.** When CLAUDE.md passes about 150 lines: move area rules into `.claude/rules/`, wire `check_instructions.py` into a pre-commit hook or CI.
9. **Mechanic and implementer fan out.** Once checklists and gates exist, delegate edits: `mechanic` inside its fence, `implementer` per lane with disjoint ownership.
10. **Gates in hooks or CI.** `doc_numbers.py --check --no-placeholders` before push; `check_instructions.py --strict` and `agent_models.py --strict` in CI.

## Customize

| What | Where | Notes |
|---|---|---|
| Language for talking to the human | `workflow-kit.json` `language.human`, and the first line of the CLAUDE.md snippet | Artifacts (code, docs, commits) stay in `language.artifacts`. Skills tell sessions to read this setting |
| Model table | the snippet's "Project routing specifics" line and the agents' `model` frontmatter | Aliases only. To run without Fable, set `fable-advisor` to `opus` and drop `advisorModel`. When an alias lags, pin through `env` in settings, record why, and drop the pin later |
| Effort | agents' `effort` frontmatter | Levels depend on the model; an unsupported level falls back to the highest supported one at or below it |
| Mechanic fence | `workflow-kit.json` `mechanic.allow` and `mechanic.deny` | Allow list, not deny list: anything not allowed is fenced. Without the key, the fence is exactly the files the brief names |
| Reviewer checklists | `workflow-kit.json` `reviewers` | `default`, one key per area, and `regressionLibrary`. Copy `agents/reviewer.md` to `<area>-guardian.md` and name its checklist in the description |
| Decision files | `workflow-kit.json` `decisions` | `files` for ADR entries and the index, `ruleFiles` for rule definitions, `scan` and `exclude` for placeholders |
| CLAUDE.md budget | `workflow-kit.json` `instructions.maxLines` | Default 200, the documented recommendation |
| Ledger location | `workflow-kit.json` `ledger.path` | Keep it out of `.claude/` and git-ignored |
| Handover pointer | `workflow-kit.json` `handover` | `pointer` file and `promptsDir` |

## Design notes

- **Aliases only.** A full model id freezes an agent on an old model; aliases follow each family's newest model as Claude Code updates.
- **Cheap output counts after a gate.** Haiku and Sonnet work is accepted after an exit code or a verification, never on its own word. "Not found" is never final.
- **Flat agent tree.** The main session is the only spawner, so cost, ownership and review stay visible.
- **Evidence over assertion.** Every PASS, every "done" and every number names its evidence and source.
- **Lean by default.** Adopt a ritual when its pain is known, and record the adoption as a decision.
