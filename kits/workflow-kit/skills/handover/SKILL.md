---
name: handover
description: End of session handover. Use when a session is ending, context is nearly full, work pauses mid task, the user says wrap up, hand over, write the next session prompt, or "what should the next session do". Writes the handover note, the next session prompt and moves the pointer file, then signs off in the ledger.
---

# Handover

A session ends; the work does not. The next session (or another human) must be able to continue from files alone, without this conversation.

Templates in this kit: `templates/HANDOVER.md` and `templates/NEXT-SESSION-PROMPT.md`.

## The pointer file pattern

- One small file at the repo root, `NEXT-SESSION-PROMPT.md` (configurable as `handover.pointer`), **points** to the prompt the next session should run. It never holds the prompt itself and never holds status.
- The prompts live in `handover.promptsDir` (for example `docs/prompts/`). Status lives only in the tracker.
- Format: the current pointer at the top (one line: name, file path, one line why), then a short closure note of what just finished. Older pointers move down or are deleted; history lives in git and the decision log.
- Moving the pointer is part of the definition of done.

## Ritual (in order)

1. **Make the work durable.** Commit what is finished. Anything unfinished is either committed behind a guard, left in a clearly named WIP state written down in the handover, or reverted. Never leave silent uncommitted changes for the next session to find.
2. **Update the tracker** status for the item.
3. **Decision log.** At least one entry per phase. Decisions made in chat go in now (`decision-log` skill).
4. **Write the handover** (`templates/HANDOVER.md`), either as a section in the next prompt or as `docs/handover/<date>-<slug>.md`:
   - State: HEAD sha, branch, pushed or not, deploy state (pushed is not shipped; say what proves it is live).
   - Done this session (with commits).
   - Left open, in priority order, each with the next concrete action.
   - Landmines: what will bite the next session (flaky tests, half migrated data, a contract change others consume, a stale pin).
   - Contracts the next session consumes and must not change, with file paths.
   - Decisions pending the human, as a list.
5. **Write or update the next session prompt** (`templates/NEXT-SESSION-PROMPT.md`, or a sprint prompt via the `sprint-prompt` skill for planned work). It must stand alone: read order, the task, the plan mode phases, the rules, the verification gate.
6. **Move the pointer** in `NEXT-SESSION-PROMPT.md`.
7. **Ledger SIGN-OFF** (`ledger.py signoff`), including clones and ports cleaned up.
8. **Report to the human** in `language.human`: done, open, pending their decision, where the next prompt is.

## Quality bar

- A reader with no access to this conversation can continue. Test it: would a fresh session know the first command to run?
- Every "done" claim points at a commit or evidence. Every "open" item has a next action.
- No secrets, tokens or personal data in handover files.
- Facts and proposals are separated. Measured numbers name their source and date.
