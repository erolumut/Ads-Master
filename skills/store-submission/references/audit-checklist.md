# Submission Readiness Audit (scored)

> Knowledge as of 2026-10. Use before a first submission, after a rejection, when taking over an app, and quarterly for live apps. Score every item Pass, Partial or Fail with evidence (file, screen, console page, date). An item without evidence is a Fail. Items that do not apply (Play items for an iOS only app, TWA items for a native app) are N/A and leave the denominator. Sources and labels for each rule are in the module named in the Fix column.

Severity weights: Critical 5, High 3, Medium 2, Low 1. Pass earns the full weight, Partial half, Fail 0.

## A. Dossier and process

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | `ads-master/SUBMISSION.md` exists for this version, every key answered | The dossier is the gate | `submission_check.py` dossier lines | Critical | [Dossier template](submission-dossier-template.md) |
| A2 | `submission_check.py` exit 0, or every WARN accepted in dossier section 11 | Mechanical gaps caught before review | Script output pasted in section 10 | Critical | Fix the FAIL lines |
| A3 | Change request approved by the human for the submission | G3 | Journal, change request file | Critical | [Playbooks](playbooks.md) Play 10 |
| A4 | `store_submissions.csv` has a row for each of the last 5 submissions with outcome and guideline | KPIs and repeat detection | File | High | [Rejections and appeals](rejections-and-appeals.md) section 9 |
| A5 | Every past rejection has a root cause and a prevention change | Repeat rejections target zero | Journal | High | Same |

## B. Apple build and privacy

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Built with the required Xcode and SDK; deployment target meets the minimum | Upload refused otherwise | Archive info | Critical | [Apple review checklist](apple-review-checklist.md) section 4 |
| B2 | A purpose string for every protected resource used by code, web view or plugins; each specific and localized | 5.1.1(ii), crashes | Script; read each string | Critical | [Apple privacy](apple-privacy-and-sdk-requirements.md) section 4 |
| B3 | `PrivacyInfo.xcprivacy` in the app target with every required reason category used | Uploads refused since 2024-05-01 | Script; Xcode privacy report | Critical | Same, sections 2 and 3 |
| B4 | Every SDK on Apple's list ships its manifest and signature | Submission requirement | Xcode privacy report | High | Update SDKs |
| B5 | App Privacy answers re-compared with the SDK data map after the last SDK change | Accuracy, enforcement | Dossier dates vs dependency history | High | Same, section 6 |
| B6 | ATT only where tracking starts; nothing withheld when declined | 5.1.2(i) | Device walk | High | Same, section 7 |
| B7 | Account deletion in the app removes the account and data, covers guest accounts, warns about subscriptions, revokes Sign in with Apple tokens | 5.1.1(v) | Device walk with the demo account; server code | Critical | Same, section 8 |
| B8 | Sign in with Apple offered when Google or Facebook login is primary, or a documented 4.8 exception | 4.8 | Script; dossier | Critical | [Apple review checklist](apple-review-checklist.md) section 2 |
| B9 | Third party AI sharing disclosed with explicit permission | 5.1.2(i) | Device walk | High | [Apple privacy](apple-privacy-and-sdk-requirements.md) section 10 |
| B10 | Export compliance declared (`ITSAppUsesNonExemptEncryption` or questionnaire), confirmed by the human | Upload flow, legal statement | Script; dossier | Medium | [Apple review checklist](apple-review-checklist.md) section 3 |

## C. Apple listing and forms

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Screenshots show the app in use; previews are screen captures; required sizes uploaded | 2.3.3, 2.3.4 | App Store Connect media | High | [Apple review checklist](apple-review-checklist.md) section 5 |
| C2 | No other platform names, icons or badges in the app or metadata | 2.3.10 | Search assets and the web view | High | Same, section 2 |
| C3 | Metadata checked by app-store-optimization with a compliance verdict | 2.3.7, 2.3.8, claims | ASO output, compliance log | High | app-store-optimization |
| C4 | Age rating questionnaire answered from the build, including the social media question | Required since 2026-09 | App Store Connect | Critical | Same, section 3 |
| C5 | DSA trader status verified (EU distribution) | EU availability | App Store Connect | Critical | Same, section 3 |
| C6 | iPad layout usable when the app runs on iPad | Rejection risk | Device walk on iPad | Medium | App team |
| C7 | Privacy policy and support URLs live with real contact | 2.1, 5.1.1(i) | Open on submission day | High | Dossier section 3 |

## D. Payments

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Digital unlocks through in-app purchase; external links only where allowed | 3.1.1, 3.1.1(a) | Device walk per storefront | Critical | [Apple payments](apple-payments-and-subscriptions-review.md) sections 1 and 2 |
| D2 | Products Ready to Submit and attached; each bought in the sandbox on the submitted build | 2.1(b) | Console; test log | Critical | Same, section 5 |
| D3 | Restore works for non consumables and subscriptions | 3.1.1 | Fresh install walk | Critical | Same, section 1 |
| D4 | Paywall checklist passed for every paywall and language | 3.1.2 | Screenshots per language | Critical | Same, section 4 |
| D5 | Expired subscription demo account | Apple asks for it | Dossier | High | [Review notes](review-notes-and-demo-accounts.md) section 2 |
| D6 | Odds before every random purchase, or no paid random items; age rating and UK listing label consistent | 3.1.1, Play, ASA | Device walk; listing | Critical | [Apple payments](apple-payments-and-subscriptions-review.md) section 7 |
| D7 | Policy file and dossier agree (`--policy` passes) | Store declarations | Script | High | Same, section 6 |

## E. Review access and notes

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Demo account signs in on a clean install on the submission day; never expires; no blocking code | 2.1(a) | Test log with date | Critical | [Review notes](review-notes-and-demo-accounts.md) section 2 |
| E2 | Back end live; feature flags match production | 2.1(a) | Status page; flag config | Critical | Same |
| E3 | Notes under 4,000 bytes covering purpose, steps, purchases, deletion, external services, devices tested | Complete review | Dossier section 8 | High | Same, sections 3 and 4 |
| E4 | Required documents attached (licenses, rights) | Complete review | App Store Connect attachments | High | Same, section 7 |

## F. Wrappers and games

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Native value visible in the core loop and named in the notes (iOS wrappers) | 4.2 | Device walk; notes | Critical | [Wrapped web apps and games](wrapped-web-apps-and-games.md) section 2 |
| F2 | Navigation locked to the app origin, or unrestricted web access declared | Age rating 16+ | Device walk | High | Same, section 2 |
| F3 | TWA `assetlinks.json` live with the app signing fingerprint; no browser bar on the internal build | Verification | Script; live URL; device | Critical | Same, section 3 |
| F4 | Game Center entitlement and configuration present when Game Center features ship | Since 2023-08 | Xcode, App Store Connect | High | Same, section 4 |
| F5 | UGC and chat: filter, report, block, contact | 1.2 | Device walk | Critical | Same, section 4 |
| F6 | 4.7 controls when the app hosts downloadable mini games | 4.7.1 to 4.7.5 | Device walk | Critical | Same, section 5 |
| F7 | Minors: compliance verdict reflected in the build and the rating answers | Law, 1.3, Families | Verdict vs build | Critical | Same, section 6 |

## G. Google Play

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | targetSdk 36 (phones and tablets) and Billing Library 8 or later | Upload refused | Script | Critical | [Google Play launch checklist](google-play-launch-checklist.md) section 2 |
| G2 | App Bundle, Play App Signing, upload key fingerprint recorded | Requirement | Console | High | Same |
| G3 | Closed test complete for new personal accounts | Production access | Console testers count over 14 days | Critical | Same, section 1 |
| G4 | Data safety written from the SDK data map, dated after the last SDK change | Top rejection cause | Dossier vs dependency history | Critical | [Play declarations](google-play-declarations-and-data-safety.md) section 2 |
| G5 | Account deletion in the app and a web link entered in Data safety | Requirement | Device; console | Critical | Same, section 3 |
| G6 | Ads, audience, IARC and declarations answered from the build | Policy | Console | High | Same, sections 4 and 5 |
| G7 | Sensitive permissions removed or declared | Policy | Manifest; console | High | Same, section 7 |
| G8 | Vitals under the bad behavior thresholds (updates) | Visibility | Android vitals, 28 days | High | [Google Play launch checklist](google-play-launch-checklist.md) section 6 |

## Audit report template

```
# Submission readiness audit: <app>, <stores>, <version>, <date>
Data used: <dossier, script output, console pages read, dates>; Freshness check: <date>
Score: <overall %>, grade <A to F>; section scores A to G
Critical fails (first)
Top 5 fixes (impact x confidence x ease)
Findings by section (item, result, evidence, fix)
Change requests (G3 lines)
Handoffs requested
Data gaps and [Unverified] items
```

## Quick audit (30 minutes, before a submission that cannot wait)

Score these and list the rest as data gaps: A1, A2, B2, B3, B7, B8, C4, D2, D3, D4, E1, F1 (wrappers), G1, G4, G5.

## Scoring rubric

1. Section score = earned weights / possible weights for applicable items (Pass = weight, Partial = half, Fail = 0).
2. Overall score = earned weights across all sections / possible weights.
3. Grades:

| Overall | Grade | Meaning |
|---------|-------|---------|
| 90% to 100% | A | Ready to submit |
| 75% to 89% | B | Submit only after the High items are fixed or accepted in writing |
| 60% to 74% | C | Do not submit; fix Critical and High items |
| 40% to 59% | D | Dossier and privacy foundations missing |
| under 40% | F | Rebuild the submission process before the next build |

4. Override: any applicable Critical item that is not a Pass (Fail or Partial) blocks the submission, whatever the total. The audit never "passes with exceptions" on a Critical item.

## Scoring example

Section D with D1 (Critical 5, Pass), D2 (Critical 5, Pass), D3 (Critical 5, Partial: restore works on iPhone, not tested on iPad), D4 (Critical 5, Pass), D5 (High 3, Fail), D6 N/A, D7 N/A: earned = 5 + 5 + 2.5 + 5 + 0 = 17.5; possible = 23; section score 76%. D3 Partial on a Critical item still blocks until it is a Pass.
