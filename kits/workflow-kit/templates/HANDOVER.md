# Handover: <work item> · <YYYY-MM-DD>

## State
- HEAD: `<sha>` on `<branch>` · pushed: <yes | no> · live: <evidence that it is deployed, or "not deployed">
- Ledger: signed off as `@<handle>` · clones and ports cleaned: <yes | list>

## Done this session
- <what> · commit `<sha>` · evidence: <test, run record, measurement>

## Left open (priority order)
1. <item> · next action: <the first concrete command or step>
2. <item> · next action: <...>

## Landmines
- <what will bite the next session: flaky test, half migrated data, stale pin, contract change others consume>

## Contracts the next session consumes (do not change)
- <name> · `<file path>` · <one line on the shape>

## Decisions pending the human
- <question> · options: <a | b> · recommendation: <a, because ...>

## Placeholders in flight
- <ADR-NEW<n> / R-NEW<n> in files: ...> (assign at push with doc_numbers.py --assign)
