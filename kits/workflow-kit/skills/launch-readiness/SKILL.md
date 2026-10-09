---
name: launch-readiness
description: Pre-launch go or no-go for any product, site or app. Use before a public launch, before the first paid traffic or ad spend, before opening signups or payments, or when the user asks to check everything before launch. Covers 20 items with proof for each (secrets out of frontend and git, rotating committed keys, rate limiting, server side auth on every route, per user database rules, server side validation, provider spend caps, no stack traces, error tracking, tested backup restore, 404 and 500 pages, cheap Android phones, 3 second loads, meta and OG tags, privacy and terms, funnel analytics, signup, payment and password reset end to end, email deliverability, contact path, rollback plan) and runs secret_scan.py and launch_check.py.
---

# Launch readiness

"Make no mistakes" cannot be checked. A list where every item carries proof can. This skill turns the classic pre-launch list into a gate: each item is PASS with evidence another person can re-check, NA with a reason, or it blocks the launch. The model proposes, a human decides GO.

> **Kit path.** `<kit>` is `${CLAUDE_PLUGIN_ROOT}` in plugin mode or `.claude/workflow-kit` when installed by copy. Scripts exit 0 pass, 1 fail, 2 could not run; 2 is never a pass.

## Procedure

1. **Copy the checklist.** `<kit>/templates/LAUNCH-READINESS.md` to `docs/LAUNCH-READINESS.md`. Fill the release line. Mark items that truly do not apply as NA with the reason (no payments, no database, no email) instead of deleting them.
2. **Run the mechanical checks first** (cheap, exact):
   - Items 1 and 2: `python3 <kit>/scripts/secret_scan.py --history`. Every finding in history needs rotation in the provider console, not only a deletion. Record the rotation date per key.
   - Item 20 and release health: `python3 <kit>/scripts/gate.py --record` on the release commit, so only a cleared commit ships.
   - Items 11, 13, 14 and smoke paths: the project's smoke script against production or preview (in Ads Master projects: `site-engineer/scripts/smoke_check.py` with `BASE_URL`).
   - Item 16: the tracking plan check if the project has one (Ads Master: `measurement/scripts/tracking_plan_check.py`).
3. **Prove the rest with small, targeted tests** (one at a time, write the command and result into Evidence):
   - Rate limits (3): a burst of requests to login, signup, contact form and any paid or AI endpoint returns 429.
   - Auth (4): call each server route without a session and with another user's id; expect 401 or 403. Hiding a button in the UI is not auth.
   - Data rules (5): read and write another tenant's row with a real low privilege session; expect a refusal from the database or API.
   - Validation (6): send a malformed payload to each boundary; expect 400 with a safe message, never 500.
   - Spend caps (7): screenshot the cap and alert settings in each provider console (AI, cloud, ads, SMS).
   - Errors (8, 9): force an error in production mode; the user sees the 500 page with a reference id; the tracker shows it with the release tag.
   - Restore (10): restore last night's backup into a scratch database, compare row counts and a sample, note the time it took. A backup that was never restored is a hope, not a backup.
   - Phones and speed (12, 13): a low end Android profile (360 px, slow 4G, CPU throttled) through the key flows.
   - Legal (15): privacy policy and terms live and linked from footer and signup; consent before non essential tags where the law requires it.
   - Account flows (17): signup with verification, payment in test mode including a failed card and a 3DS challenge, password reset link that works once and expires.
   - Email (18): SPF, DKIM and DMARC pass; seed test to Gmail and Outlook; one click unsubscribe on marketing mail.
   - Contact (19) and rollback (20): a monitored inbox; written rollback steps, owner, trigger, and a rehearsal date.
4. **Review.** Hand the filled file to a `reviewer` or a named guardian (review-gates skill). Evidence that does not reproduce becomes FAIL.
5. **Check and decide.** `python3 <kit>/scripts/launch_check.py docs/LAUNCH-READINESS.md`. Any Blocker not PASS or NA means NOT READY. On READY, a human writes GO or NO GO with name and date at the bottom of the file.

## Rules

- Evidence is re-checkable: a command with output, a file path, a test run, a dated screenshot path or dashboard link. "Done", "ok" and "looks fine" fail the check.
- Evidence expires: a PASS older than 30 days is re-checked before launch (`--max-age`).
- Warn items may launch with an owner and a date; Blocker items may not.
- Paid traffic raises the bar: spend amplifies every gap (bots burn budget without rate limits, a broken reset wastes every paid signup). In Ads Master projects the growth-orchestrator launch workflow requires this gate before the first campaign activation.
- Never paste secrets into the checklist. Reference where they live (secret manager, env var name), never the value.

## Related

`review-gates` (reviewers and guardians), `parallel-sessions` (do not launch while another session holds a risky change), `handover` (record the GO decision and what is open).
