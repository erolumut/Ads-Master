# <Area> review checklist

> Used by the `<area>-guardian` (a copy of the Workflow Kit `reviewer`). Every item: PASS, FAIL or N/A, with evidence (`file:line`, command and output, measurement, screenshot path). A PASS without evidence is a FAIL. A skipped item is a FAIL.

## 0. Scope and spec
- [ ] Every named requirement in the spec or brief is listed and marked delivered or not.
- [ ] No change outside the owned files; no scope creep beyond the brief.

## 1. Correctness
- [ ] <behavior> is covered by a test that failed before the change.
- [ ] Edge cases: empty, maximum count, concurrent use, offline or timeout, repeated submission.

## 2. Contracts
- [ ] Public APIs, schemas and protocol fields changed only additively, or with a recorded decision.

## 3. <Area specific category, for example security, accessibility, performance, UX>
- [ ] <check> · detect: <how>

## 4. Honesty
- [ ] Known gaps and placeholders are named in the report, not called done.

## Regression library
Run every entry in `<docs/review/REGRESSIONS.md>`; one line each.

## Devil's advocate
At least three candidate defects, each confirmed or justified in writing.
