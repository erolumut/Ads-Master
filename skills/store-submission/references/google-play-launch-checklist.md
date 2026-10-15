# Google Play Launch Checklist

> Knowledge as of 2026-10. developer.android.com pages were read at the source: target API (updated 2026-10-01) and the Billing Library deprecation FAQ (updated 2026-09-09) on 2026-10-15, the rest in the 2026-10-12 research pass, all labeled [Official, YYYY-MM]. Play Console Help (support.google.com) could not be opened from this environment, so rules seen only in its search results carry [Reported, 2026-10]: confirm them in the live Play Console, which wins for that account. Declarations and Data safety are in [Google Play declarations and data safety](google-play-declarations-and-data-safety.md).

## 1. Account readiness

| Item | Rule | Evidence |
|------|------|----------|
| Account type | Personal or organization; an organization account needs a D-U-N-S number (free, can take up to 28 days) | [Official, 2026-10] |
| Developer verification | Required for installs on certified Android devices (Android 7 and later) in Brazil, Indonesia, Singapore and Thailand from 2026-09-30; global in 2027; Play registers about 99% of developers automatically; check Play Console | [Official, 2026-10] |
| Account transfer | A transfer workflow with a 7 day cooling off period exists since 2026-05-27 | [Official, 2026-10] |
| Closed test before production (new personal accounts) | Personal accounts created after 2023-11-13 need 12 testers opted in to a closed test for the last 14 days continuously before applying for production access; organizations are exempt | [Reported, 2026-10] |
| Production access decision | About 48 hours after applying | [Reported, 2026-10] |

Closed test failures reported: the opted in count dips below 12 on any day, vague answers to the production access questions, and testers who installed once and never used the app [Reported, 2026-10]. Plan 14 days plus a buffer: recruit 15 to 20 real testers, keep them opted in, ship at least one test build update during the window and answer the questions with what testers did and what changed [Practitioner consensus].

## 2. Build requirements

| Item | Rule | Evidence |
|------|------|----------|
| Format | Android App Bundle required for new apps (since 2021-08) | [Official, 2026-10] |
| Signing | Play App Signing required for new apps; keep the upload key safe and record its fingerprint | [Official, 2026-10] |
| Size | 4 GB compressed download limit; no `.obb` expansion files | [Official, 2026-10] (research pass; read the app bundle page for how the limit is counted) |
| Target API, new apps and updates | Android 16 (API 36) or higher from 2026-08-31; Wear OS and Android Automotive OS 35; Android TV and Android XR 34; extension to 2026-11-01 on request | [Official, 2026-10] |
| Target API, existing apps | Apps must target API 35 or higher to stay available to new users on devices running a newer Android version; older targets are visible only on devices with the same or lower version | [Official, 2026-10] |
| Exception | Permanently private apps restricted to one organization | [Official, 2026-10] |
| Billing Library | Version 8 or later for new apps and updates from 2026-08-31; extension to 2026-11-01; Play Console shows a warning with the extension form; existing apps keep working | [Official, 2026-09] |
| Memory and device migration | New requirements from 2027-02 | [Official, 2026-10] (research pass; read the newsletter before planning) |

`submission_check.py` fails a targetSdk under 36 (phones and tablets) and a declared Billing Library under 8; pass `--min-target-sdk` for other form factors. It warns when the version comes through a variable it cannot resolve.

## 3. Permissions that need declarations or changes

| Permission or API | Rule | Evidence |
|-------------------|------|----------|
| `USE_EXACT_ALARM` | Only for alarm and calendar apps | [Official, 2026-10] |
| Foreground services | Android 14 and later: declare service types in the manifest and in Play Console; `specialUse` needs a justification | [Official, 2026-10] |
| Geofencing as a foreground service use | Removed as a use case on 2027-01-27 | [Official, 2026-10] |
| `READ_CALL_LOG` | Not allowed for verification uses (2027-01-27) | [Official, 2026-10] |
| Photos and videos | Use the photo picker instead of broad media permissions | [Official, 2026-10] |
| Contacts and location | Contact picker and location button as narrow alternatives | [Official, 2026-10] |
| Deadline for the picker changes | Pages showed both 2026-10-28 and 2027-01-27; plan for the earlier date and treat 2027-01-27 as the latest | [Contested] (two official pages disagree) |
| Advertising ID | Apps targeting Android 13 or later declare the `AD_ID` permission to use it; Families apps are restricted | [Official] (mobile-app-growth module) |

## 4. App content forms (Play Console > Policy > App content)

All must be answered before the first production release [Reported, 2026-10]: privacy policy, app access (how reviewers get in), ads ("Contains ads"), content rating (IARC questionnaire), target audience and content, Data safety, and the declarations that apply (government apps, financial features, health apps). Detail and the cross check with Apple are in [Google Play declarations and data safety](google-play-declarations-and-data-safety.md).

## 5. Store listing checks (owned by app-store-optimization)

| Item | Rule | Evidence |
|------|------|----------|
| Title | 30 characters | [Reported, 2026-10] |
| Short description | 80 characters | [Reported, 2026-10] |
| Title, icon, developer name | No emoji, no "#1", "best", "free" style terms, no rank or price claims | [Reported, 2026-10] |
| Graphics | Screenshots and video represent the app | [Official] (app-store-optimization module) |

This agent reruns `aso_metadata_check.py` output and the compliance verdict before submission; it does not rewrite the listing.

## 6. Quality gates

| Metric | Bad behavior threshold | Evidence |
|--------|------------------------|----------|
| User perceived crash rate | 1.09% overall; 8% on any single phone model | [Official, 2026-10] |
| User perceived ANR rate | 0.47% overall; 8% on any single phone model | [Official, 2026-10] |
| Window and effect | 28 days; above the threshold Play can reduce visibility and show a warning on the listing | [Official, 2026-10] |

Before a launch: run the Play Console pre-launch report on the internal test build and fix crashes it finds [Practitioner consensus]; test on a low end Android phone; record the vitals in the dossier for updates.

## 7. Review and release

| Item | Detail | Evidence |
|------|--------|----------|
| Review time | Hours to about 7 business days; longer for new accounts and sensitive categories | [Reported, 2026-10]; new account effect [Practitioner consensus] |
| Managed publishing | Lets an approved release wait for a manual publish | [Practitioner consensus] (confirm the setting in the console) |
| Staged rollout | Release to a percentage first; halt on a vitals spike | [Practitioner consensus] |
| Tracks | Internal, closed, open, production; the closed track carries the 12 tester requirement for new personal accounts | [Reported, 2026-10] |

Fees changed in 2026 (US, UK and EEA from 2026-06-30; Australia 2026-09-30; Japan and Korea 2026-12-31) [Reported, 2026-10]. They do not change review; they belong to `mobile-app-growth` and `pricing-strategy`.

## 8. Top reasons for rejection and suspension

Reported in 2026 search results [Reported, 2026-10]: Data safety mismatch with the SDKs in the build; a missing or dead privacy policy link; undeclared or unqualified permissions; misleading metadata; impersonation; incentivized installs; crashes; webview apps with no added value; repeated violations leading to termination. Creating a new account while an appeal or suspension is open counts as ban evasion [Reported, 2026-10].

## 9. First launch checklist (Google Play)

| # | Item | Done when |
|---|------|-----------|
| 1 | Account type and verification | Organization D-U-N-S done, or personal account verified; developer verification status read in the console |
| 2 | Closed test (new personal account) | 12 or more testers opted in for 14 continuous days, date recorded in the dossier |
| 3 | App Bundle and Play App Signing | AAB built; app signing enrolled; upload key fingerprint recorded |
| 4 | targetSdk and Billing Library | `submission_check.py` passes (36 and 8) |
| 5 | Permissions | Every sensitive permission has its declaration, or is removed |
| 6 | App content forms | All answered; Data safety from the SDK data map |
| 7 | Account deletion | In-app path and web link ([declarations module](google-play-declarations-and-data-safety.md) section 3) |
| 8 | TWA only | `assetlinks.json` live with the app signing fingerprint; no browser bar on the internal build |
| 9 | Quality | Pre-launch report clean; tested on a low end device |
| 10 | Listing | ASO checker and compliance verdict recorded |
| 11 | App access | Instructions and a demo account when features sit behind sign in |
| 12 | Change request | The human approves and presses submit (G3) |
