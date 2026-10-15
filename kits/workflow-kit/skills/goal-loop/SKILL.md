---
name: goal-loop
description: Run a long, unattended, metric driven improvement loop safely. Use when the user wants an agent to keep working for hours or days toward one number (page load under 2 seconds on a phone, bundle under a budget, build or gate under N minutes, Lighthouse or Core Web Vitals scores, test suite time, no horizontal scroll at 360 px, lint warnings to zero), says /goal, "keep going until", "work overnight", or shares a goal template. Writes the goal, the measure, the effort and the stop rules into .progress/GOAL.md, measures the noise first, changes one thing at a time, keeps a change only when it beats the noise and passes the project's own gate, logs every measurement and keeps a progress chart with goal_loop.py.
---

# Goal loop

A long run needs three things written down: the goal, how it is measured, and how hard to try. This skill adds what a bare template misses: the measurement's own noise, the project's full gate on every kept change, a spending stop, and the project's git rules. The number is the target; the product is still the product.

> **Kit path.** `<kit>` is `${CLAUDE_PLUGIN_ROOT}` in plugin mode or `.claude/workflow-kit` when installed by copy. `goal_loop.py` exits 0 keep or goal met, 1 revert, 2 could not run, 3 stop the loop.

## Before the loop (with the human, once)

1. **Fill `.progress/GOAL.md`** from `<kit>/templates/GOAL.md`: goal and target, the measure command, direction, effort, turn budget, spend budget, the gate command, what may not change, and where the run lives. Add `.progress/` to `.gitignore`.
2. **Where it runs.** Follow the project's git rules. Projects that allow branches: a new branch. Projects that work only on `main` (no branches by rule): a separate local clone of `main`, merged back under the project's own rules when the run ends. Never push from inside the loop.
3. **One measure, scripted.** The measure command prints the value on its last line (for example a small wrapper around Lighthouse that prints the LCP in ms). A metric that needs eyes (screenshots at 360 px) is measured by the agent and logged with `record`.
4. **Baseline and noise.** `python3 <kit>/scripts/goal_loop.py init ...` then `measure --baseline --runs 5`. The noise (spread across the five runs) becomes the floor: a gain smaller than the noise is luck, not progress.

## The loop (every turn)

1. Read `.progress/GOAL.md`, `log.csv` and `questions.txt`; pick up where the last turn stopped.
2. Make **one** change, smallest first. Write in the log label what it is.
3. Run the **project's own gate** (tsc, lint, test, build, or `gate.py`). Red gate: revert, log it, next idea. A change that passes the metric but breaks the gate never counts.
4. Measure: `goal_loop.py measure --runs 3 --label "..."`. Verdict KEEP: commit locally with a clear message. REVERT: `git checkout` the change. GOAL MET: stop and write the summary. Exit 3: stop and write where it is stuck.
5. The chart (`.progress/chart.html`) updates after every measurement; one look shows the best so far, the goal line and the gap left.
6. Unsure about anything (a feature trade, a dependency, data, a design change): write it to `.progress/questions.txt` and move to another idea. Never wait, never guess.

## Hard rules

- Never delete or weaken features, tests, checks, accessibility or telemetry to move the number. Removing something counts only when the human listed it as allowed in GOAL.md.
- No deploys, no data deletion, no secrets, no new paid services, no changes to CI or the gate itself.
- Design changes on a user visible surface go through the project's design rules (Craft Gate, direction docs); when in doubt they become a question, not a commit.
- Stop on any of: goal met, turn budget used, spend budget reached, `max_flat` tries in a row without a gain, the gate red twice in a row on unchanged code.
- Lab numbers are not users. When the goal is speed, the closing summary names what field data (Chrome UX Report, RUM, the platform's vitals) should confirm after release.

## Closing summary (`.progress/SUMMARY.md`)

Baseline, best, goal, gap; kept changes in order with their gain; reverted ideas worth remembering; open questions; turns and approximate cost; the merge plan for the human. Then hand over with the `handover` skill if work continues in another session.

## Good first goals

| Project kind | Goal | Measure |
|--------------|------|---------|
| Web app | Homepage LCP under 2.0 s on a mid phone | Lighthouse mobile, median LCP |
| Web app | No horizontal scroll at 360 px on every route | Playwright screenshot plus scrollWidth check per route, count of failing routes |
| Next.js or Vite app | First load JS of the main route under budget | Build output size of the route, KB |
| Any repo | Local gate under N minutes | `time` around the gate, seconds |
| Any repo | Test suite under N seconds without dropping tests | Test runner time, with the test count printed and checked |

The last row shows the pattern for every speed goal: print the guard numbers too (test count, route count, feature flags) so a "faster" result that quietly does less is visible in the log.
