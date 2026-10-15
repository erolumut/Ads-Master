# Store Submission Playbooks

> Knowledge as of 2026-10. Every play ends in a human action: submitting a build, sending a reply, an appeal or an expedite request, publishing a release and changing a store form are G3. Drafts in `ads-master/` are G1. Uploading a build to TestFlight or a Play internal track is also gated by the guard hook (`fastlane pilot`, `xcrun altool --upload-app`, `eas submit`, gradle `publish*` tasks are G3), so the human runs or approves them. Facts and labels are in the modules each step links.

Plays: 1 First App Store submission, 2 Google Play first launch, 3 Update submission, 4 After a rejection, 5 Wrapper first launch, 6 Game first launch with purchases and ads, 7 Hotfix with expedited review, 8 SDK added or changed, 9 Monthly requirements watch, 10 Change request.

## Play 1: First App Store submission

Entry: a release candidate build, PROJECT_BRIEF and PRODUCT_FACTS filled, store listing drafted by `app-store-optimization`.

| Step | When | Action | Owner | Gate |
|------|------|--------|-------|------|
| 1 | 3 weeks before | Freshness check ([SKILL](../SKILL.md) Freshness protocol); book an App Review appointment if the app is borderline (wrapper, mini games, AI, kids) | store-submission | G0 |
| 2 | 3 weeks before | Copy the [dossier template](submission-dossier-template.md) to `ads-master/SUBMISSION.md`; fill sections 1, 3 and 9 (SDK data map) | store-submission | G1 |
| 3 | 3 weeks before | DSA trader status and agreements checked in App Store Connect (verification can hold the submission) | Human | G3 |
| 4 | 2 weeks before | Run `submission_check.py`; hand FAIL lines to the app team | store-submission, App team | G0 |
| 5 | 2 weeks before | App Privacy answers drafted from the SDK data map; export compliance answer drafted; age rating answers drafted with `compliance` | store-submission, compliance | G1 |
| 6 | 2 weeks before | Paywall checklist and products configured; sandbox purchase test | App team, mobile-app-growth | G2 |
| 7 | 10 days before | TestFlight external build with the same notes (Beta App Review as a rehearsal) | Human uploads | G3 |
| 8 | 1 week before | Demo accounts created and seeded (active and expired subscription); notes written from template A, B, C or D | store-submission | G1 |
| 9 | 2 days before | Final run: script exit 0; audit quick items Pass; URLs opened; demo account signs in on a clean install | store-submission | G0 |
| 10 | Day 0 | Change request approved; the human enters forms, pastes notes and credentials, submits | Human | G3 |
| 11 | Day 0 | Row in `store_submissions.csv`; journal entry | store-submission | G1 |
| 12 | Days 1 to 3 | Watch status; answer any message the same day with a draft for the human | store-submission | G1 |
| 13 | Approval | Release as planned (manual or dated); read back the listing in each storefront | Human, app-store-optimization | G3 |

Exit: approved on the first review, or Play 4.

## Play 2: Google Play first launch

Entry: an AAB, a Play Console account, the listing drafted.

1. Account: organization (D-U-N-S up to 28 days) or personal; read developer verification status ([Google Play launch checklist](google-play-launch-checklist.md) section 1).
2. New personal account created after 2023-11-13: start the closed test at least 3 weeks before the target date; recruit 15 to 20 real testers; keep 12 or more opted in for 14 continuous days; ship one test update; record the dates in the dossier.
3. Build: targetSdk 36, Billing Library 8, Play App Signing enrolled; `submission_check.py` passes.
4. App content forms from the dossier and the SDK data map ([Play declarations](google-play-declarations-and-data-safety.md)); account deletion in app and web link.
5. Internal test track: pre-launch report clean; low end device test; TWA shows no browser bar.
6. Apply for production access with concrete answers about testers and changes.
7. Production release with managed publishing or a staged rollout (G3); vitals watched daily for 14 days.

## Play 3: Update submission

1. Read what changed since the last approved version: code, SDKs, products, data collection, accounts, ads.
2. New dossier (archive the old one); copy unchanged sections, re-answer the changed ones.
3. A new SDK or a changed configuration triggers Play 8 before anything else.
4. A new product: create, attach to the version, sandbox test, describe in the notes.
5. A new account feature: account deletion must ship in the same build (both stores).
6. Notes from template E; script; quick audit.
7. Change request; the human submits; log.

## Play 4: After a rejection

| Step | Time | Action | Gate |
|------|------|--------|------|
| 1 | Hour 0 | Save the message to the journal; incident row in INCIDENTS.md; tell the human | G1 |
| 2 | Hour 0 to 2 | Classify each issue ([Rejections and appeals](rejections-and-appeals.md) section 1); check for the Bug Fix Submissions line | G0 |
| 3 | Hour 2 | Information missing: draft the reply and fix the demo account; no new build unless needed | G1 |
| 4 | Day 0 to 2 | Binary or metadata fix: app team fixes; dossier and script rerun; notes from template F | G1 |
| 5 | Day 0 to 2 | Misunderstanding or dispute: reply first with facts and screenshots; appeal only if the reply fails, one appeal covering every cited guideline | G3 |
| 6 | Resubmission | Change request; the human resubmits or sends the reply | G3 |
| 7 | After the outcome | Root cause and prevention change (dossier template, audit item or script check) proposed through the journal; `store_submissions.csv` updated with `repeat_of_previous` | G1 |

Never: a new bundle or developer account, hiding the feature from review, resubmitting an unchanged build.

## Play 5: Wrapper first launch (TWA and Capacitor)

1. Decide the route per store ([Wrapped web apps and games](wrapped-web-apps-and-games.md) section 1) and record it.
2. `site-engineer` builds the wrapper and runs release QA on the web build that ships inside it.
3. Play first (TWA): assetlinks with the app signing and upload fingerprints; internal track check for the browser bar; Play 2.
4. iOS (Capacitor): native value list implemented and reachable; Game Center for games; in-app purchase for digital goods; purpose strings for web APIs; privacy manifest with plugin reasons; Sign in with Apple if social logins exist.
5. Lock navigation to the app's origin; remove store badges and web checkout from the wrapped UI.
6. Notes from template B; an App Review appointment for the first iOS wrapper is worth booking.
7. Play 1 from step 4.

## Play 6: Game first launch with purchases and ads

1. `game-monetization` hands over `monetization-policy.json`; `monetization_check.py` passes.
2. `submission_check.py --policy`: the dossier's ads, purchases, subscriptions and random items answers match `storeDeclarations` and the catalog.
3. Age rating and IARC from the build: loot boxes, simulated gambling, chat, social media, advertising ([Apple review checklist](apple-review-checklist.md) section 3).
4. Consent before any ad SDK (contract runbook); ATT only where tracking starts.
5. A seeded demo account reaches the shop in under 2 minutes; odds screen if any random item exists; Restore for non consumables and passes.
6. Chat controls if any chat exists; Kids or Families decision from `compliance`.
7. Notes from template C, which states what money can buy in each mode.
8. Play 1 and Play 2.

## Play 7: Hotfix with expedited review

Trigger: a crash, payment failure, data loss or security issue live for users.

1. Confirm the incident with crash and payment data; incident row; tell the human.
2. App team ships the minimal fix; dossier copied from the last version with the change described.
3. Notes include the steps to reproduce the bug on the current version.
4. The human submits, then files the expedite request (G3).
5. If the previous update is rejected for a non legal, non safety issue with the eligibility line, use Bug Fix Submissions instead of a new review.
6. Google Play: a staged rollout of the fix; halt the bad release if it is still rolling out.
7. Post-incident note; prevention check added.

## Play 8: SDK added, removed or reconfigured

1. Name the change (SDK, version, configuration such as ads or analytics turned on).
2. Read the SDK's privacy manifest, its Data safety guidance and its purpose string needs.
3. Update the SDK data map row and date.
4. Re-compare App Privacy answers and the Data safety form; draft the changes (G1) for the human to apply (G3).
5. Update the privacy policy with `compliance` when the change adds a data type or a recipient.
6. Run `submission_check.py`; check the Xcode privacy report.
7. The next submission's notes mention the new data collection (template E).

## Play 9: Monthly requirements watch

| Source | What to read | Action when something changed |
|--------|--------------|-------------------------------|
| Apple Developer News and Upcoming Requirements | SDK minimums, age rating, privacy, payments, guideline revisions | Journal entry tagged `change`; dossier template or checklist update proposed |
| App Review Guidelines | Last updated date; diff the sections this skill cites | Update labels and rows |
| Android target API, Billing deprecation, Play policy newsletter | Deadlines, new declarations | Same |
| Live apps | Vitals, policy status page, App Store Connect messages | Incident if anything is open |

Output: a dated calendar of requirements due in the next 6 months per live app (`ads-master/outputs/store-submission/YYYY-MM-DD_store-submission_requirements-calendar.md`).

## Play 10: Change request (every submission, reply, appeal or form change)

Use `ads-master/templates/CHANGE_REQUEST.md`. One line per action:

| # | Store | Entity | Action | Current | Proposed | Evidence | Risk | Rollback | Gate | Approve |
|---|-------|--------|--------|---------|----------|----------|------|----------|------|---------|
| 1 | App Store | Version 1.4.0 (212) | Submit for review | Prepare for Submission | Waiting for Review | Dossier 2026-10-19, script exit 0, quick audit A | Rejection under 4.2 (wrapper) | Remove from review before it starts; reply with notes | G3 | |
| 2 | App Store | Age rating | Answer social media question | Not answered | No social media capability | Build has no feed; compliance verdict 2026-10-14 | Wrong answer changes the rating | Re-answer before submission | G3 | |
| 3 | Google Play | Data safety | Add crash data for Crashlytics | Not declared | App info and performance, collected | SDK data map row 4, 2026-10-14 | None | Edit the form | G3 | |

Read back each executed action (status in the console) and log it with a timestamp in the journal.
