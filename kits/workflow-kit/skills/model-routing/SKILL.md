---
name: model-routing
description: Routing policy for models and subagents. Use before spawning any subagent, when deciding which model should do a piece of work, when fanning out parallel workers, when a cheaper model's output needs to count, when a worker failed twice, when compacting, or when the user asks which model or agent to use, how to cut cost without cutting quality, or why a result looks cheaper than expected.
---

# Model routing

> **Kit path.** `<kit>` below is `${CLAUDE_PLUGIN_ROOT}` when the kit runs as a plugin, or `.claude/workflow-kit` when it was installed by copy. Every kit script exits 0 pass, 1 fail, 2 could not run; treat 2 as not passed.


The main session is the conductor. It plans, decides, synthesizes, writes decisions and reports, integrates and ships. Workers do bounded pieces and return evidence. This skill says who does what, on which model, and when their output counts.

The kit's agents are namespaced when installed as a plugin (`workflow-kit:scout`); when copied into `.claude/agents/` they keep the bare name.

## 1. Aliases only

- Refer to models by alias: `fable`, `opus`, `sonnet`, `haiku` (or `inherit`). Never a full model id in an agent file, a brief or a doc. An alias follows the newest model of its family as Claude Code updates; a full id silently freezes you on an old one.
- One allowed exception: an env pin in `.claude/settings.json` (`ANTHROPIC_DEFAULT_HAIKU_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_FABLE_MODEL`) when the alias still resolves to an older model than you want. Write a comment in the decision log saying when to drop it, and check it each time `agent_models.py` runs.
- The alias resolves inside the running binary. After a Claude Code update, restart long running sessions.

## 2. The routing table

Fill the "Project specifics" column once in your CLAUDE.md snippet; keep the rest.

| Work | Who | Model | Project specifics |
|---|---|---|---|
| Orchestration, plans, decisions, synthesis, decision log and rule text, commits, push, reports to the human | main session | your strongest daily model (usually `opus`) | |
| Judgment work: multi-file features, user visible design and copy, data model and migrations, security, API or wire contracts, non-trivial debugging | `implementer` | `opus` | <red-line areas> |
| Verification of claims, findings, diffs, "fixed" and "not found" | `verifier` | `opus` | |
| Review against a written checklist before "done" | `reviewer` and its copies | `opus` | <checklists> |
| Bounded non-design edits with a mechanical oracle, inside the allow list | `mechanic` | `sonnet` | `mechanic.allow` in `workflow-kit.json` |
| Web research, one cited question per worker | `researcher` x N | `sonnet` | |
| Locating code, files, call sites | `scout` | `haiku` | |
| Facts from CI, test, build and deploy logs | `log-triage` | `haiku` | |
| Facts and numbers from CSV exports, API dumps, analytics exports | `data-extractor` | `haiku` | |
| Second opinion at critical points | `fable-advisor` | `fable` | <your critical points> |

Critical points for `fable-advisor`: direction before signature or hard-to-reverse work and a polish pass after; alternatives before they go to the human; a decision that supersedes a locked rule; a change to a contract others keep reading (shared schema, public API, protocol version); a problem the main session failed twice. One consult at a time, never fanned out.

## 3. When cheap output counts

- Output from `haiku` or `sonnet` counts only after a **mechanical gate** (an exit code: tests, typecheck, lint, a script) or **verification** by the main session or `verifier`.
- "Not found" from `scout`, `log-triage`, `data-extractor` or `researcher` is never the final word on absence. It goes to `verifier`, never to another locator.
- The main session reads the full diff of every `mechanic` change before staging it.
- A researcher's claim that a decision rests on is re-verified at the source by the main session.

## 4. Escalation

| Event | Next step |
|---|---|
| `mechanic` fails twice | task returns to the main session (or an `implementer`) |
| `implementer` fails twice on the same problem | one `fable-advisor` consult with the failed attempts attached |
| `scout`, `log-triage` or `data-extractor` says "not found" | `verifier` |
| `reviewer` FAIL | `implementer` fixes, `reviewer` re-runs on the new diff |
| Main session stuck on the same failure twice | `fable-advisor`, or the advisor tool if enabled |

## 5. Spawning rules

- **Spawn named agents.** A named agent carries its pinned model, effort and tools.
- **Pass `model` explicitly on every unnamed spawn** (general purpose agents, ad hoc workers). Without it the worker gets `CLAUDE_CODE_SUBAGENT_MODEL` if set, else the main session's model, which may be far more expensive or far weaker than the work needs.
- **Never pass `model` on a named agent whose tier is the point** (`verifier`, `reviewer`, `implementer`): the per-invocation parameter overrides the frontmatter.
- Model precedence, highest first: the per-invocation `model` parameter, the agent's `model` frontmatter (`inherit` means the main model), `CLAUDE_CODE_SUBAGENT_MODEL`, the main session's model. `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` makes the env var override frontmatter for every subagent; do not set it with this kit.
- **Nesting.** Subagents can spawn their own subagents by default (up to three layers). This kit wants a flat tree: read-only agents list explicit `tools` without `Agent`, and the editing agents set `disallowedTools: Agent`. Workers report "Handoffs requested"; the main session spawns.
- **Do not plan in the built-in Plan or Explore agents** when the plan depends on project rules: they skip CLAUDE.md. Plan in the main session or a named agent.
- **Every brief names**: the goal, owned files, the rule files and direction docs for those paths (the worker reads them first with the Read tool), the oracle, what is out of scope, and the return format.

## 6. Fan out

- Fan out only genuinely independent work. Write **disjoint file ownership** into each brief: one owner per file. A worker that needs another's file stops and asks.
- Read-only workers (scout, log-triage, data-extractor, researcher, verifier, reviewer, guardians) can run in parallel freely. Editing workers (mechanic, implementer) run in parallel only with disjoint ownership.
- Workers never commit, push, stash or reset. The main session stages paths explicitly, never `git add -A` while another session shares the tree.
- A cut worker (usage limit, crash) resumes where it stopped: its brief and ownership let a new spawn continue. Resume in small waves; never restart a batch blind.
- Long batches: three to five parallel workers is a sane ceiling; more increases merge and review cost faster than it saves time.

## 7. Check what actually ran

Silent substitution happens: a missing alias, a stale pin, a parameter that overrode the frontmatter, a usage limit fallback.

- At session sign-off, and whenever a result looks cheaper than its tier, run `python3 <kit>/scripts/agent_models.py` to list each agent's configured model and effort and flag full ids, and `python3 <kit>/scripts/agent_models.py --audit` to compare, per subagent of the latest session, the model requested at spawn, the model configured in frontmatter and the model actually served (read from the local transcripts in `~/.claude/projects/`).
- Compare that with what the session actually used: the model named in the subagent's result or transcript, `/status` for the main session. A mismatch is a finding: record it in the ledger PROGRESS line and fix the cause.

## 8. Advisor tool

- `advisorModel` in `.claude/settings.json` (for example `"fable"`) turns on the advisor tool: the main model may consult a stronger model, with the whole conversation, before committing to an approach, when a failure repeats, and before calling work done. Ask for it at those three moments.
- It does not replace `fable-advisor`, which takes a focused brief and artifacts.
- The advisor must be at least as capable as the main model. Fable as advisor may need a one-time usage-credits consent (`/model fable`); without it, requests go without the advisor.

## 9. Compaction

- Compaction runs on the session's own model; it cannot be delegated. `autoCompactWindow` in settings (tokens, 100000 to 1000000) sets when it fires.
- At a phase boundary, write state into your ledger PROGRESS line first, then run `/compact <focus>`. Prefer that over letting auto compact choose.
- Tell compaction to preserve: active scope, unpushed commits, decision placeholders in flight (`ADR-NEW<n>`), files touched, open gate failures, the human's decisions this session, servers and ports you started, the tree or clone you work in, rule files and docs read (by path, to reopen), advisor touches accepted or declined.
- Path scoped rules and docs you read are summarized away. Reopen the area's rule file and direction doc before resuming work there.
