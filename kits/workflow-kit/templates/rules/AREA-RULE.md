---
paths:
  - "<dir>/**/*.{ext1,ext2}"
  - "<other-dir>/**"
---

<!-- Provenance (stripped before the model sees the file, costs no tokens): moved from CLAUDE.md on <YYYY-MM-DD>. Sources: <ADR-<n>, regression R<n>, the human's decision on <date>>. Edit the rule, not this history; history lives in the decision log. -->

# <Area> rules

Loads when Claude reads, writes or edits a file matching `paths`. Briefs for this area name this file, and workers read it with the Read tool before the first edit, because rules do not load while planning from docs and compaction summarizes them away.

1. **<Rule in one line>.** <Why, in one sentence>. Check: <test, script or review item that catches a violation>.
2. **<Rule in one line>.** <Why>. Check: <...>.

## Before you change this area
- Read: <direction doc or spec path>.
- Contracts others consume here: <file paths>. Change them only additively, or record a decision first.
