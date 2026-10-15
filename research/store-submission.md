# Research Dossier: Store Submission (App Store and Google Play review)

> Research pass completed 2026-10-12 (R9 Apple first pass review, R10 Google Play first launch, R5 store presence, R6 regulation notes) and extended on 2026-10-12 to 2026-10-15 by reading the main Apple and Android pages at the source for the `store-submission` package. Scope: what makes a build pass App Review and Google Play review on the first attempt, for native apps, games, subscription apps and Capacitor or TWA wrappers; the forms, privacy declarations and SDK requirements; review notes and demo accounts; rejections, replies and appeals. Evidence labels follow docs/AUTHORING_SPEC.md section 7 plus [Reported, 2026-10] (see Method). Numbers in brackets refer to the Sources list at the end, which uses the same numbering as `skills/store-submission/references/sources.md`.

## Research method and limits

1. The 2026-10-12 pass opened Apple pages on developer.apple.com and Android pages on developer.android.com and recorded them as opened; support.google.com and apple.com were seen only in search results.
2. This build re-read at the source the App Review Guidelines (last updated 2026-06-08), the App Review page and its help pages (complete review, appeals, expedites, Bug Fix Submissions, purpose strings), the account deletion page, the third party SDK list, the privacy manifest, required reason API, protected resource, export compliance and Sign in with Apple documentation, the subscriptions page, Upcoming Requirements, the 2026 news list and seven 2026 news items, the age rating values and screenshot specification help pages, the Android target API and Billing Library deprecation pages, the TWA guides and the assetlinks page. Capacitor plugin requirements were read in the official plugin READMEs on the npm registry.
3. Labels: [Official, YYYY-MM] only for facts read at an official source, dated by the page (guidelines 2026-06, news items by month) or by the read month (2026-10). "Research pass" marks facts opened on 2026-10-12 and not re-read. [Reported, 2026-10] for search result only facts, including every Play Console Help page. [Unverified] for a single weak source, a vendor claim, or long standing console knowledge not re-read. [Contested] where sources disagree.
4. Blocked from this environment by egress policy and not routed around: support.google.com, apple.com, developers.google.com, developer.chrome.com, capacitorjs.com.
5. Not covered here: listing optimization (`research/app-store-optimization.md`), paid UA, store fees and paywall strategy (`research/mobile-app-growth.md`), claims and consumer law (`research/compliance.md`).

## Executive summary

1. Completeness decides first pass approval. Apple states that over 40% of unresolved issues relate to Guideline 2.1 (crashes, placeholders, incomplete information) [2] [Official, 2026-10], and its 2025 transparency report, seen as a search result, put Performance (section 2) as the largest rejection group: 1,354,418 of about 2.09 million rejections among 9.1 million submissions reviewed [36] [Reported, 2026-10]. A working demo account, a live back end, attached in-app purchases and notes that show the reviewer where everything is remove most of that risk.
2. Apple now asks for more context in the notes: concept and business model, devices tested, external services including AI services, regional differences, and a demo account with an expired subscription for subscription apps; codes that block sign in can force a call that takes 3 to 5 business days [3] [Official, 2026-10].
3. Privacy is enforced mechanically at upload: since 2024-05-01 App Store Connect refuses builds that use a required reason API without a declared reason [11] [Official, 2026-10], and 86 listed SDKs (Capacitor, Cordova, Flutter, Firebase, the Facebook SDKs, GoogleSignIn, OneSignal, Unity and others) need their own manifests and signatures [9] [Official, 2026-10]. Capacitor 8 ships empty manifests for its frameworks, so the app still declares what its plugins use (for example UserDefaults `CA92.1` for Preferences) [38] [Official, 2026-10].
4. Purpose strings now have written rules: name the feature, give an example, one sentence, localized, and the developer is responsible for strings SDKs need [7] [Official, 2026-10].
5. Account deletion has detailed rules on Apple: delete the whole account and its data (deactivation is insufficient), include guest accounts, revoke Sign in with Apple tokens, warn about subscriptions, no support loops outside regulated industries [8] [Official, 2026-10]. Google Play adds a web deletion link entered in Data safety [50] [Reported, 2026-10].
6. Forms changed in 2026: the age rating questionnaire gained required social media questions from September 2026 (13+ minimum, Social Media descriptor) [18, 19] [Official, 2026-07 and 2026-10]; unrestricted web access sets 16+, which matters for wrappers [19] [Official, 2026-10].
7. Build minimums: Xcode 26 and the iOS 26 SDK since 2026-04-28, iOS 13 minimum target since 2026-09-09, the iOS 27 SDK from April 2027 [16, 17] [Official]. Google Play: API 36 for new apps and updates since 2026-08-31 (extension to 2026-11-01) [39] and Billing Library 8 [40] [Official, 2026-10 and 2026-09].
8. Wrappers: Apple's 4.2 asks for features beyond a repackaged website [1] [Official, 2026-06], with no official list of what is enough; practitioners report that push, location or sharing alone are not enough [Reported, 2026-10]. A TWA must pass Digital Asset Links with the Play app signing fingerprint, or it opens as a Custom Tab with browser UI [46, 47] [Official, 2026-10].
9. Apple's appeal process is now written down: reply first, one appeal per rejected app covering every cited guideline point by point, up to five apps per form; and Bug Fix Submissions let an eligible update through once while the issue is fixed next time [4, 6] [Official, 2026-10].
10. Google Play's biggest first launch hurdle for new personal accounts is the closed test (12 opted in testers for 14 continuous days) [49] [Reported, 2026-10]; Data safety mismatches with the SDKs in the build lead the reported rejection causes [54] [Reported, 2026-10].

## State of the channel in 2026 (with numbers)

| Indicator | Value | Source |
|-----------|-------|--------|
| Apple review speed | At least 50% of submissions in under 24 hours, 90% in under 48 hours | [2] [Official, 2026-10] |
| Apple submissions reviewed and rejected in 2025 | 9,100,620 reviewed; 2,093,244 rejected (about 23%); 387,087 approved after an earlier rejection | [36] [Reported, 2026-10] |
| Rejections by section in 2025 (overlapping) | Performance 1,354,418; Legal 495,673; Design 415,532; Business 283,820; Safety 151,159; Other 4,145 | [36] [Reported, 2026-10] |
| Share of unresolved Apple issues under 2.1 | Over 40% | [2] [Official, 2026-10] |
| Apple review notes limit | 4,000 bytes | [27] [Official, 2026-10] |
| SDKs that need privacy manifests and signatures | 86 | [9] [Official, 2026-10] |
| Calls to get past sign in codes | Typically 3 to 5 business days | [3] [Official, 2026-10] |
| Google Play closed test for new personal accounts | 12 testers opted in for 14 continuous days; accounts created after 2023-11-13 | [49] [Reported, 2026-10] |
| Google Play production access decision | About 48 hours | [49] [Reported, 2026-10] |
| Google Play review time | Hours to about 7 business days | [54] [Reported, 2026-10] |
| Android vitals bad behavior | Crash 1.09%, ANR 0.47% overall; 8% per phone model; 28 days | [41] [Official, 2026-10] |
| TestFlight | 10,000 external testers; builds expire after 90 days | [30] [Official, 2026-10] |

## Timeline of changes, January 2024 to April 2027

| Date | Change | Impact | Evidence |
|------|--------|--------|----------|
| 2024-05-01 | Required reason APIs must be declared in privacy manifests | Uploads refused otherwise | [11, 16] [Official, 2026-10] |
| 2024-10-16 | DSA trader status required for updates in the EU | EU updates held | [16] [Official, 2026-10] |
| 2025-02-17 | Apps without DSA trader status removed from EU storefronts | EU availability | [16] [Official, 2026-10] |
| 2025-11-13 | Guideline revision: 4.1(c), 4.7 mini apps and mini games, 5.1.2(i) third party AI disclosure, 1.2.1(a) creator age restrictions | AI and mini game apps need new controls | [35] [Official, 2025-11] |
| 2026-01-31 | Answers to the updated age rating questions due | Updates otherwise interrupted | [16] [Official, 2026-10] |
| 2026-02-06 | Random or anonymous chat placed under 1.2 | Chat controls | [26, 35] [Official, 2026-02] |
| 2026-04-28 | Xcode 26 and the 26 SDKs required for uploads | Build pipelines | [16] [Official, 2026-10] |
| 2026-05-08 | Brazilian betting license required for availability | Regulated games | [26] [Official, 2026-05] |
| 2026-06-04 | Texas SB 2420 applies to new Texas Apple Accounts (Declared Age Range API) | Age assurance | [26] [Official, 2026-06] |
| 2026-06-08 | Guidelines revised (4.3 clarified, 4.5.3, kid and teen safety) | Spam and Live Activities checks | [1, 35] [Official, 2026-06] |
| 2026-07-09 | Social media questions added to the age rating questionnaire | Required from September 2026 | [18] [Official, 2026-07] |
| 2026-08-24 | New Sign in with Apple relay domain `private.icloud.com` announced | Email validation and allowlists | [22] [Official, 2026-08] |
| 2026-08-26 | Anonymous chat apps may not target children on Google Play | Families | [48] [Official, 2026-10] (research pass) |
| 2026-08-31 | Google Play: API 36 for new apps and updates; Billing Library 8 | Android builds | [39, 40] [Official] |
| 2026-09-09 | iOS 13 minimum deployment target for uploads | Old targets refused | [16] [Official, 2026-10] |
| 2026-09-16 | EU alternative ATT prompt from iOS 27.2; subscription Bundles and Suites; multiseat on by default | ATT copy, purchase options | [21, 23] [Official, 2026-09] |
| 2026-09-30 | Android developer verification in Brazil, Indonesia, Singapore, Thailand | Installs on certified devices | [43] [Official, 2026-10] |
| 2026-10-01 | Apple EU terms: new commission structure, alternative payments alongside IAP, child safety protections | EU payment routes | [24, 32] [Official] |
| 2026-11-01 | End of the Google Play extensions for API 36 and Billing Library 8 | Last date with an extension | [39, 40] [Official] |
| 2027-01-27 | Geofencing removed as a foreground service use; READ_CALL_LOG not for verification; latest date for the picker changes | Permission declarations | [48, 44] [Official, 2026-10]; picker date [Contested] |
| 2027-04 | iOS 27 SDK required; iPhone Duo screenshots for iOS 27.1 SDK builds | Build and assets | [17, 25] [Official] |

## Best practice consensus

1. Build a dossier per submission and test it on the submission day: demo account from a clean install, every URL opened, every product bought in the sandbox [2, 3] [Official guidance; Practitioner consensus for the dossier form].
2. Write review notes as steps, not marketing: what the app is, how to sign in, where purchases, Restore and deletion are, what external services it uses, what differs by region [3] [Official, 2026-10].
3. Generate the Xcode privacy report and write App Privacy and Data safety from one SDK data map; redo on every SDK change [9, 10, 44] [Official, 2026-10; map method Practitioner consensus].
4. Build account deletion once to Apple's stricter rules and add the web link for Play [8, 50].
5. Put the billed amount first on paywalls, with trial terms, Restore, Terms and Privacy on the same screen [15] [Official, 2026-10].
6. For wrappers, ship native value in the core loop (Game Center for games, offline play, native push, haptics, share) and name it in the notes [1] [Official rule; Practitioner consensus on what counts].
7. Rehearse with TestFlight Beta App Review and Play internal testing before the store review [30] [Official, 2026-10].
8. Reply before appealing; appeal once with point by point reasons [4] [Official, 2026-10].

## Contested topics (both sides)

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| What is "enough" native value for 4.2 | Some practitioners report approvals with push and offline play | Others report push, location or sharing alone are not enough [Reported, 2026-10] | Ship several native features in the core loop; name them in the notes; book an App Review appointment for a first wrapper |
| Live updates of web bundles in Capacitor apps | Vendors say small fixes are allowed under the License Agreement [Unverified] | 2.5.2 forbids downloading code that introduces or changes features [1] [Official, 2026-06] | Fixes only; never a feature App Review has not seen |
| Picker permission deadline on Play | 2026-10-28 on one page | 2027-01-27 on another [44] | Plan for the earlier date |
| Minimum deployment target in April 2027 | iOS 15 per the research notes | Not stated in the 2026-09-09 news item [17] | Treat as [Unverified]; re-read in 2027-01 |
| US link out fees | Zero commission per the 2025-04 order | Cost based fee allowed by the Ninth Circuit; no rate set as of 2026-08-16 [62] [Reported, 2026-10] | Treat zero as temporary; owned by mobile-app-growth |

## What top operators do differently

1. They keep a standing review account set per app (active, expired subscription, second player) that never expires and is tested before every submission.
2. They treat a rejection as a process bug: every one adds a check to the template, the audit or a script, and repeat rejections are tracked as a KPI.
3. They read the guidelines' "Last updated" date and Upcoming Requirements monthly and keep a requirements calendar per app.
4. They write App Privacy and Data safety from a dated SDK inventory, not from the last answers.
5. They book App Review appointments before borderline launches (wrappers, mini game hosts, AI features, kids).
6. They build account deletion, paywall disclosures and privacy flows once to the stricter store's rules.
7. They plan the Play closed test five to six weeks before a first launch on a new personal account.

These are [Practitioner consensus]; no study measured them.

## Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|------------|
| Demo account expired, password rotated or behind a code during review | A rejection round, or a call that takes days [3] | Demo account checklist; codes handled in the notes |
| In-app purchase not attached to the version or not reachable | 2.1(b) rejection [1] | Payments checklist; seeded demo state |
| Social login without Sign in with Apple | 4.8 rejection [1] | `submission_check.py` |
| A new SDK shipped without updating App Privacy or Data safety | Play enforcement, Apple rejection [44, 54] | Play 8 on every SDK change |
| Wrapper that looks like the website, with a "Get it on Google Play" badge inside | 4.2 and 2.3.10 rejections [1] | Wrapper checklist |
| TWA signed with the upload key fingerprint only | Browser bar in production [46, 47] | Fingerprint from Play Console App signing |
| Appeal sent before replying, or one appeal per guideline | Wasted appeal, slower outcome [4] | Reply first; one appeal for all |
| Resubmitting an unchanged build | Longer reviews for repeat rejections [1] | Classify and fix |
| A new developer account after a suspension | Treated as ban evasion [54] | Never |

## Benchmarks (source, date, sample, caveat)

| Benchmark | Value | Source and caveat |
|-----------|-------|-------------------|
| Apple rejection share | About 23% of submissions reviewed in 2025 | [36] search result of Apple's transparency report; all apps worldwide, including spam; a well prepared team should be far below it |
| Approved after an earlier rejection | 387,087 in 2025 | [36] same caveat |
| Apple review time | 50% under 24 hours, 90% under 48 hours | [2] Apple's own statement; varies by season and app complexity |
| Play review time | Hours to about 7 business days | [54] search results; new accounts and sensitive categories slower |
| Production access after closed test | About 48 hours | [49] search result |

Compare a project with its own `store_submissions.csv` history first; these numbers are context only.

## Tools, APIs and scripts

| Tool | Use | Gate |
|------|-----|------|
| `submission_check.py` (this package) | Static checks of the iOS, Capacitor or Android project and the dossier | G0 |
| Xcode privacy report (Archive > Generate Privacy Report) | Aggregated privacy manifests of the app and SDKs | G0 |
| Play Console pre-launch report | Crashes and issues on test devices for an internal or closed build | G0 to read; the upload is G3 |
| Android Studio merged manifest | The real targetSdk and permissions after library merges | G0 |
| fastlane `deliver`, `supply`, `pilot`; `eas submit`; `xcrun altool --upload-app`; gradle `publish*` tasks; `asc ... submit` | Uploads and submissions | G3 in the guard hook |
| Bubblewrap CLI | TWA builds | G1 locally; uploads G3 |

## Official sources to monitor

| Source | URL | Cadence |
|--------|-----|---------|
| App Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ | Monthly (check "Last updated") |
| Upcoming requirements | https://developer.apple.com/news/upcoming-requirements/ | Monthly |
| Apple Developer News | https://developer.apple.com/news/ | Weekly |
| App Review help | https://developer.apple.com/help/app-review/ | Quarterly |
| Third party SDK requirements | https://developer.apple.com/support/third-party-SDK-requirements/ | Before each first submission |
| Target API requirements | https://developer.android.com/google/play/requirements/target-sdk | Monthly from May to November |
| Billing Library deprecation | https://developer.android.com/google/play/billing/deprecation-faq | Quarterly |
| Play policies | https://developer.android.com/distribute/play-policies | Monthly |

## Verification queue

Each item names the cheapest check that settles it (L1 live console read, L2 official page read in full, L3 two independent dated sources, L4 controlled test).

1. Play closed test numbers, the 2023-11-13 cutoff and the production access timing (L1 in a new personal account; L2 Play Console Help 14151465).
2. Play account deletion requirements and the Data safety web link field (L1; L2 answer 13327111).
3. Play App access form wording and Data safety category names (L1).
4. April 2027 minimum deployment target (L2 when Apple publishes the 2027 requirements).
5. 2025 App Store transparency report figures (L2 on apple.com).
6. EU commission rates from 2026-10-01 (L2 on Apple's EU page).
7. Play Billing through the Digital Goods API for digital goods in TWAs (L2 on developer.chrome.com and Play policy).
8. Picker permission deadline (L2 on both pages; L1 policy status page).
9. Whether Game Center features are reviewed separately from the app version (L2; seen only as a search result [37]).
10. Content rights and IPv6 requirements in App Store Connect (L1).

## Claims considered and not relied on

| Claim | Why not used |
|-------|-------------|
| "40% of unresolved issues are 2.1" from vendor blogs | Apple states it on its own page [2]; the vendor version is no longer needed |
| A maintained Capacitor Game Center plugin | Not confirmed |
| Live updates are always allowed | Vendor reading; conflicts with 2.5.2 for features |
| Push alone satisfies 4.2 | Reported as insufficient |
| Fixed Play review times | Single summaries; history and the console win |

## Sources

1. App Review Guidelines. Apple Developer. https://developer.apple.com/app-store/review/guidelines/. Last updated 2026-06-08; read 2026-10-15.
2. App Review. Apple Developer. https://developer.apple.com/distribute/app-review/. Read 2026-10-12.
3. Provide information for a complete review. App Review Help. https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review. Read 2026-10-12.
4. Appeal to the App Review Board. App Review Help. https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board. Read 2026-10-12.
5. Request expedited review. App Review Help. https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review. Read 2026-10-12.
6. Bug fix submissions. App Review Help. https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions. Read 2026-10-12.
7. 5.1.1(ii) Write clear purpose strings. App Review Help. https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings. Read 2026-10-12.
8. Offering account deletion in your app. Apple Developer Support. https://developer.apple.com/support/offering-account-deletion-in-your-app/. Read 2026-10-12.
9. Third-party SDK requirements. Apple Developer Support. https://developer.apple.com/support/third-party-SDK-requirements/. Read 2026-10-12.
10. Privacy manifest files. Apple Developer Documentation. https://developer.apple.com/documentation/bundleresources/privacy-manifest-files. Read 2026-10-12.
11. Describing use of required reason API. Apple Developer Documentation. https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api. Read 2026-10-12.
12. Protected resources. Apple Developer Documentation. https://developer.apple.com/documentation/bundleresources/protected-resources. Read 2026-10-12.
13. ITSAppUsesNonExemptEncryption; Complying with encryption export regulations. Apple Developer Documentation. https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption. Read 2026-10-12.
14. com.apple.developer.applesignin. Apple Developer Documentation. https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.applesignin. Read 2026-10-12.
15. Auto-renewable subscriptions. Apple Developer. https://developer.apple.com/app-store/subscriptions/. Read 2026-10-12.
16. Upcoming requirements. Apple Developer News. https://developer.apple.com/news/upcoming-requirements/. Read 2026-10-12.
17. App Store submissions now open for the latest OS releases. Apple Developer News. https://developer.apple.com/news/?id=k1mtkt1k. 2026-09-09.
18. Age rating questionnaire now includes social media questions. Apple Developer News. https://developer.apple.com/news/?id=tlur8uvi. 2026-07-09.
19. Age ratings values and definitions. App Store Connect Help. https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions. Read 2026-10-12.
20. Screenshot specifications. App Store Connect Help. https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications. Read 2026-10-12.
21. Updates to App Tracking Transparency in the European Union. Apple Developer News. https://developer.apple.com/news/?id=idsft9ai. 2026-09-16.
22. Update: New domain for Sign in with Apple. Apple Developer News. https://developer.apple.com/news/?id=1ptvdtcm. 2026-08-24.
23. Get your subscriptions ready for iOS 27. Apple Developer News. https://developer.apple.com/news/?id=likeohx4. 2026-09-16.
24. Changes for apps in the European Union. Apple Developer News. https://developer.apple.com/news/?id=gmws0jgp. 2026-08-18.
25. Prepare and submit your apps for iPhone Duo. Apple Developer News. https://developer.apple.com/news/?id=kkphp5qo. 2026-10-05.
26. Apple Developer News, list of 2026 items. Apple Developer. https://developer.apple.com/news/. Read 2026-10-12.
27. App Review Information and app information fields. App Store Connect Help. URL not recorded. Research pass 2026-10-12.
28. DSA trader requirements. App Store Connect Help. URL not recorded. Research pass 2026-10-12.
29. Export compliance overview. App Store Connect Help. URL not recorded. Research pass 2026-10-12.
30. TestFlight overview. App Store Connect Help. URL not recorded. Research pass 2026-10-12.
31. App privacy details. App Store Connect Help. URL not recorded. Research pass 2026-10-12.
32. Apps in the EU. Apple Developer Support. URL not recorded. Research pass 2026-10-12.
33. Games app, Game Center, In-App Events and product page pages. Apple Developer. URLs not recorded. Research pass 2026-10-12.
34. 2.3.3 Show your app in use with screenshots. App Review Help. https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots. Research pass 2026-10-12.
35. Guideline revision news items (ids a233fmpw, d75yllv4, ey6d8onl, 3d8a9yyh). Apple Developer News. 2025-11-13 to 2026-06-08.
36. App Store Transparency Report 2025. Apple. apple.com/legal/app-store/transparency. Search result only.
37. Game Center features submittable separately during review. Apple Developer News via search. 2025-10. Search result only.
38. Capacitor plugin READMEs and @capacitor/ios 8.5.3. Ionic via the npm registry. https://registry.npmjs.org/@capacitor/camera (and the same path per package). Read 2026-10-12.
39. Target API level requirements for Google Play apps. Android Developers. https://developer.android.com/google/play/requirements/target-sdk. Updated 2026-10-01; read 2026-10-15.
40. Google Play Billing Library deprecation FAQ. Android Developers. https://developer.android.com/google/play/billing/deprecation-faq. Updated 2026-09-09; read 2026-10-15.
41. Android vitals. Android Developers. https://developer.android.com/topic/performance/vitals. Research pass 2026-10-12.
42. Play App Signing; Android App Bundle. Android Developers. https://developer.android.com/studio/publish/app-signing and https://developer.android.com/guide/app-bundle. Research pass 2026-10-12.
43. Android developer verification and FAQ. Android Developers. https://developer.android.com/developer-verification. Research pass 2026-10-12.
44. Foreground service types, exact alarms, photo picker, declare data use. Android Developers. URLs not recorded. Research pass 2026-10-12.
45. Play Billing subscriptions. Android Developers. https://developer.android.com/google/play/billing/subscriptions. Research pass 2026-10-12.
46. Trusted Web Activities overview and quick start guide. Android Developers. https://developer.android.com/develop/ui/views/layout/webapps/trusted-web-activities. Read 2026-10-15.
47. Configure the assetlinks.json file. Android Developers. https://developer.android.com/training/app-links/configure-assetlinks. Read 2026-10-15.
48. Play policies and the 2026 policy newsletters. Android Developers. https://developer.android.com/distribute/play-policies. Research pass 2026-10-12.
49. App testing requirements for new personal developer accounts (answer 14151465). Play Console Help. https://support.google.com/googleplay/android-developer/answer/14151465. Search result only.
50. Account deletion requirements (answer 13327111). Play Console Help. https://support.google.com/googleplay/android-developer/answer/13327111. Search result only.
51. Subscriptions policy (answer 9900533). Play Console Help. https://support.google.com/googleplay/android-developer/answer/9900533. Search result only.
52. Play Console Help answers 11926878 and 9858738. Play Console Help. https://support.google.com/googleplay/android-developer/answer/11926878. Search result only.
53. Play expanded billing and fees. Android Developers Blog. URL not recorded. 2026-06. Search result only.
54. Play rejection and suspension causes, review times, termination appeals. Play Console Help and coverage. URLs not recorded. 2026. Search results only.
55. Webview apps and minimum functionality. Google policy post. URL not recorded. 2020. Search result only.
56. ASA and CAP enforcement notice on loot box disclosure. ASA; Lewis Silkin. URL not recorded. 2026-02-26. Search result only.
57. Brazil Law 15.211/2025 (ECA Digital). Demarest. URL not recorded. 2025 to 2026. Search result only.
58. Turkey Law 7578. Evrensel, NTV. URL not recorded. 2026-04-22. Search result only.
59. PEGI and paid random items. Lewis Silkin. URL not recorded. 2026-03-18. Search result only.
60. FTC and Cognosphere (Genshin Impact). US Federal Trade Commission. URL not recorded. 2025-01. Search result only.
61. Belgium loot boxes; Netherlands Raad van State 2022. SBC News; raadvanstate.nl. URL not recorded. Search result only.
62. Epic v Apple anti-steering litigation. Fenwick; The Next Web. URL not recorded. 2025-04 to 2026-08. Search result only.
63. COPPA amendments compliance date. White & Case. URL not recorded. 2026-04-22. Search result only.
