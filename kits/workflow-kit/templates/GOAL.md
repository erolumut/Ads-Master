# Goal

Copy to `.progress/GOAL.md` (and add `.progress/` to `.gitignore`). The goal-loop skill reads this file at the start of every turn.

- Goal: [the homepage shows up within 2 seconds on a phone]
- Target: [2000] [ms], direction [lower]
- Measure command: [a script that runs Lighthouse in mobile mode once and prints the LCP in ms on its last line]
- Runs per measurement: [3] (baseline: 5)
- Minimum gain to keep: [5]% or the measured noise, whichever is larger
- Gate command (must pass before any commit): [pnpm type-check && pnpm lint && pnpm test && pnpm build]
- Effort: [try boldly within the rules below; prefer the smallest change first]
- Turn budget: [50] turns; stop after [10] tries in a row without a gain
- Spend budget: [stop when the session reaches its usage limit or after N hours]
- Where it runs: [new branch goal/lcp] or [separate local clone of main] (follow the project's git rules); never push
- May not change: features, tests, accessibility, telemetry, CI, the gate, secrets, data, deploys
- Allowed to remove (only if listed): [none]
- Design rules to respect: [path to direction doc or Craft Gate, if any]
- Field check after release: [Chrome UX Report or RUM, which metric]
