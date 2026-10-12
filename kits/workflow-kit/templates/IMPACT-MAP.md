# Impact map: <task>

<!-- Workflow Kit template (planner-session phase 1b). Fill before any design or edit on legacy or untested code. Scope = the blast radius: touched code plus callers and dependents one to two levels out. -->

Written against HEAD `<sha>` on `<date>` by `<session>`. Verified by: `<verifier run or reviewer>`.

## Touched code

| # | Touched code (`file:line`) | Callers and dependents (`file:line`) | Side effects | Tests protecting it | Evidence |
|---|----------------------------|--------------------------------------|--------------|---------------------|----------|
| 1 | | | | none | PROVEN / GUESS |

## Dead code candidates

| Code (`file:line`) | Proof it is unused (references checked, dynamic entry points checked, config and routes checked) | Delete in commit |
|--------------------|-------------------------------------------------------------------------------------------------|------------------|
| | | |

## Guesses and how each gets settled

| # | Guess | Why it cannot be proven by reading | Settled by (characterization test name, or question for the human) | Status |
|---|-------|------------------------------------|--------------------------------------------------------------------|--------|
| 1 | | dynamic dispatch, reflection, config driven, cron, webhook, external caller | | open |

## Verdict

- PROVEN rows: `<n>`, GUESS rows: `<n>`, all guesses settled: yes / no
- Approved for edits by `<human>` on `<date>`. Until then: no code edits.
