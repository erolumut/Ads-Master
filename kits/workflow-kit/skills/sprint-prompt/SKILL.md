---
name: sprint-prompt
description: Write and finalize prompts that start a new session on a sprint, phase or feature, and per phase delegation prompts. Use when the user asks for a sprint prompt, a next session prompt for a planned piece of work, a kickoff brief, a delegation prompt per phase, or when finalizing a draft prompt on the day the work starts. Provides the 7 block template, doors not wings, depth levels, the finalize ritual and a quality checklist.
---

# Sprint prompt

Each sprint runs in its own session. The prompt's first job is **intent transfer**: the new session must understand what the human has in mind and where the project is going. The task list comes second.

Templates in this kit: `templates/SPRINT-PROMPT.md` (the 7 blocks) and `templates/DELEGATION-PROMPT.md` (per phase). Store finished prompts in `handover.promptsDir` (for example `docs/prompts/`) and point to the next one from the handover pointer file.

## The 7 blocks (in order)

| # | Block | Content |
|---|---|---|
| 0 | **Intent** | Two to four paragraphs. What changes for the user or the business when this is done, and how it should feel. What the human cares about most here. The project in one sentence. The principles that apply |
| 1 | **Context reading** | The read order (session start ritual) plus the docs that feed this sprint: specs, research, rule files for the paths |
| 2 | **Plan first** | Verify every `⚠` assumption against the decision log and the real code. Targeted mini research only where needed (library version, API state). A short plan. A deviation from spec is a stop point: propose in the decision log and ask the human |
| 3 | **Scope** | **In**, **Out** (deliberately not done) and **Doors** (cheap hooks this sprint must leave open for later) |
| 4 | **Work list** | In priority order, each item with its own verification (test name, command, evidence type) |
| 5 | **Definition of done and ship** | Checks green; docs updated (tracker status, handover pointer, at least one decision log entry); ship per the project's rule |
| 6 | **Guardrails** | Sprint specific prohibitions plus the standing list from CLAUDE.md. At least one real, sprint specific guardrail |

## Doors, not wings

Leaving a door open is not an excuse for over-engineering.

- **Good door** (cheap, passive, does no work today): a version constant, an empty variants object, an id column ready for a second tenant, a protocol version field, a semantic token layer, a config column, an i18n key discipline.
- **Bad wing** (tomorrow's building built today): a plugin marketplace, a generic rules DSL, microservices, a generic engine with one user, a full CMS, an early payment stack, an abstract UI framework.
- Test: a door is one line, one field or one signature. Whatever makes the diff bigger is a wing. Do not build it; leave a note in the decision log.

## Depth levels

Write future prompts at the depth their certainty allows.

| Level | When | Content |
|---|---|---|
| **FULL** | next one to three sprints | Paste and run. Assumptions are still verified in block 2 |
| **MEDIUM** | the sprints after that | Full skeleton, details deliberately open. `⚠ <dependency>` marks link to earlier sprints' decisions. Finalize on the day |
| **BRIEF** | far horizon | Goal, scope, research directions, doors. Expanded to a full prompt on the day with this skill |

## Finalize ritual (MEDIUM and BRIEF, on the day)

1. Open the prompt; replace every `⚠` with the real decision from the decision log.
2. Read the previous sprints' SIGN-OFF and landmine notes (ledger archive, tracker, decision log).
3. Re-read the intent block. Still true? If not, discuss in the decision log first.
4. Paste the finalized prompt into the new session; move the handover pointer to the next prompt.

## Quality checklist

- [ ] The intent block lets an agent that has never seen the project understand what and why.
- [ ] The one sentence goal matches the tracker.
- [ ] The Out list got as much thought as the In list (the antidote to scope creep).
- [ ] Each door says in one line what it stays open for.
- [ ] Every work item has its verification (test name, command, evidence type).
- [ ] The definition of done includes doc updates (tracker, pointer, decision log).
- [ ] At least one guardrail is specific to this sprint, not a copied list.
- [ ] Every `⚠` is either resolved or explicitly marked for block 2.
- [ ] The language rule is stated (talk to the human in `language.human`; artifacts in `language.artifacts`).

## Delegation prompt variant (per phase sessions)

When a planned feature splits into phases that each run in their own session, write one delegation prompt per phase from `templates/DELEGATION-PROMPT.md`. Each has:

1. **Read first**: the approved plan file and the sections for this phase, the specs, the reference files to copy patterns from.
2. **Pre-flight**: the parallel check, reserved slots or numbers, snapshots before data changes.
3. **Task** as atomic commits (P1, P2, P3), each one commit.
4. **Verification gate** that must be green before every commit (exact commands).
5. **Out of scope**: the later phases' work, named, so this session does not drift into them.
6. **On completion**: push, mark the phase done in the plan, start the next phase's prompt.

Keep phases strictly atomic: a phase never does the next phase's work, even when it is "just one line".
