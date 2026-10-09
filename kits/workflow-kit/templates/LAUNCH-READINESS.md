# Launch Readiness

<!-- Workflow Kit template. Copy to docs/LAUNCH-READINESS.md, delete rows that truly do not apply (mark them NA with a reason instead of deleting when in doubt), and fill Status and Evidence. Check it with: python3 <kit>/scripts/launch_check.py docs/LAUNCH-READINESS.md -->

> Release: `<version or commit>` · Target date: `<YYYY-MM-DD>` · Owner: `<name>`
>
> Status values: `PASS` (proved, Evidence filled), `FAIL`, `OPEN` (not checked yet), `NA` (does not apply; Evidence says why). Severity `Blocker` must be PASS or NA before launch; `Warn` may launch with a named follow up.
> Evidence is something another person can re-check: a command and its output, a file path, a test run, a screenshot path, a dashboard link with a date. "Done" or "looks fine" is not evidence.

| # | Item | Severity | How to prove it | Status | Evidence | Checked on |
|---|------|----------|-----------------|--------|----------|------------|
| 1 | No secret in the frontend bundle or in git | Blocker | `secret_scan.py --history` exits 0; build output grepped for key prefixes; env vars used in the browser are public by design only | OPEN | | |
| 2 | Every key that was ever committed is rotated | Blocker | `secret_scan.py --history` findings each have a rotation date in the provider console; old key revoked, not just removed from git | OPEN | | |
| 3 | Rate limiting on auth, forms, paid APIs and AI endpoints | Blocker | Config or middleware path; a burst test (for example 50 requests in 10 s) returns 429 | OPEN | | |
| 4 | Auth checked on every server route, not only in the UI | Blocker | Route list with the guard each uses; a request without a session or with another user's id returns 401 or 403 | OPEN | | |
| 5 | Database rules: users read and write only their own rows | Blocker | Policy file or row level security list per table; a cross tenant read test fails as expected | OPEN | | |
| 6 | Every input validated on the server | Blocker | Schema validation at each API or action boundary (path list); a malformed payload returns 400, not 500 | OPEN | | |
| 7 | Spend caps on AI providers, ad accounts and paid APIs | Blocker | Provider console caps and alerts with screenshots; budget alerts reach a person | OPEN | | |
| 8 | Errors never show stack traces or internals to users | Blocker | Production build with debug off; a forced error shows the 500 page and a reference id only | OPEN | | |
| 9 | Error tracking alerts you before users complain | Warn | Error tracker connected (release tagged); a test error appears with source maps; alert route to a person | OPEN | | |
| 10 | Backup exists and a restore was actually tested | Blocker | Last restore drill: backup restored into a scratch database, row counts and a sample compared; date and duration | OPEN | | |
| 11 | Designed 404 and 500 pages | Warn | Both URLs return the right status and a branded page with a way back | OPEN | | |
| 12 | Works on a cheap Android phone | Warn | Real device or emulated low end Android (slow 4G, 4x CPU throttle): key flows complete, no layout overflow at 360 px | OPEN | | |
| 13 | Nothing important takes more than 3 s | Warn | Field data or lab run for the top pages and actions: LCP, INP, slowest API calls listed | OPEN | | |
| 14 | Meta tags and OG image so shared links look right | Warn | Title, description, canonical and OG tags on key pages; a share preview check (1200 x 630 image) | OPEN | | |
| 15 | Privacy policy and terms published, cookie consent where required | Blocker | URLs live and linked in the footer and signup; consent banner blocks non essential tags until consent where the law requires it | OPEN | | |
| 16 | Analytics shows where people drop off | Warn | Funnel events from a tracking plan; a test journey appears in the analytics debug view | OPEN | | |
| 17 | Signup, payment and password reset work end to end | Blocker | Automated or scripted run in production like conditions: signup with verification, payment in test mode (failed card and 3DS too), reset link works once and expires | OPEN | | |
| 18 | Emails land in the inbox, not spam | Blocker | SPF, DKIM and DMARC pass for the sending domain; a seed test to Gmail and Outlook; one click unsubscribe on marketing mail | OPEN | | |
| 19 | Users can reach you | Warn | Contact path visible from every page and inside the app; messages arrive in a monitored inbox | OPEN | | |
| 20 | Rollback plan written and rehearsed | Blocker | Steps, owner and the trigger that starts a rollback; previous release still deployable; database migration reversible or a snapshot taken | OPEN | | |

## Decision

- Blockers open: `<n>` · Warns open: `<n>` (each with an owner and date)
- Decision: `GO` or `NO GO`, by `<human name>` on `<date>`. The model proposes, a human decides.
