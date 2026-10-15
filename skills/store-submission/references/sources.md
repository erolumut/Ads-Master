# Sources (annotated)

> Compiled 2026-10-15 for the `store-submission` package from the 2026-10-12 research notes (R9 Apple first pass review, R10 Google Play first launch, R5 store presence, R6 regulation) and from pages read at the source for this build on 2026-10-12 to 2026-10-15. The research narrative and the verification queue are in `research/store-submission.md`, which uses the same numbering.

Label rules used in this package:
- [Official, YYYY-MM]: read at the official source. The date is the page's own date when it shows one (the App Review Guidelines were last updated 2026-06-08, so [Official, 2026-06]; news items carry their posting month), otherwise the month it was read (2026-10).
- "Research pass" after a label: opened at the source by the 2026-10-12 research pass and not re-read for this build.
- [Reported, 2026-10]: seen only in search results, including Play Console Help pages (support.google.com) and apple.com, which could not be opened from this environment.
- [Unverified]: a single weak source, a vendor claim, or knowledge from long standing console use not re-read in 2026. [Contested]: sources disagree; both sides shown.
- [Practitioner consensus]: operating practice without a single authoritative source.

## Apple: read at the source for this build

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | App Review Guidelines | Apple Developer | https://developer.apple.com/app-store/review/guidelines/ | Last updated 2026-06-08; read 2026-10-15 | 1.2, 1.3, 2.1(a)(b), 2.3.3, 2.3.4, 2.3.7, 2.3.8, 2.3.10, 2.5.1, 2.5.2, 3.1.1, 3.1.1(a), 3.1.2(a), 3.1.2(c), 3.1.3, 3.1.3(b), 4.2, 4.2.1 to 4.2.3, 4.3(a)(b), 4.7 to 4.7.5, 4.8 with exceptions, 5.1.1(i) to (v), 5.1.2(i), 5.1.4, After You Submit (timing, release, rejections, appeals, Bug Fix Submissions) [Official, 2026-06] |
| 2 | App Review | Apple Developer | https://developer.apple.com/distribute/app-review/ | Read 2026-10-12 | 50% of submissions in under 24 hours and 90% in under 48 hours; over 40% of unresolved issues are 2.1; common rejection causes; App Review Board basics; expedites; 30 minute appointments [Official, 2026-10] |
| 3 | Provide information for a complete review | App Review Help | https://developer.apple.com/help/app-review/before-submitting-for-review/complete-review | Read 2026-10-12 | Notes content, demo accounts, expired subscription account, codes and calls in 3 to 5 business days, demo mode, documentation by app type [Official, 2026-10] |
| 4 | Appeal to the App Review Board | App Review Help | https://developer.apple.com/help/app-review/after-submitting-for-review/appeal-to-the-app-review-board | Read 2026-10-12 | Reply first, one appeal per app, up to five apps per form, point by point, what not to appeal [Official, 2026-10] |
| 5 | Request expedited review | App Review Help | https://developer.apple.com/help/app-review/after-submitting-for-review/request-expedited-review | Read 2026-10-12 | Only submitted builds, genuine urgency, what to include [Official, 2026-10] |
| 6 | Bug fix submissions | App Review Help | https://developer.apple.com/help/app-review/after-submitting-for-review/bug-fix-submissions | Read 2026-10-12 | Eligibility line, reply without resubmitting, one deferral only [Official, 2026-10] |
| 7 | 5.1.1(ii) Write clear purpose strings | App Review Help | https://developer.apple.com/help/app-review/guideline-reference/5-1-1-purpose-strings | Read 2026-10-12 | Do and do not list, examples, localization, SDK responsibility [Official, 2026-10] |
| 8 | Offering account deletion in your app | Apple Developer Support | https://developer.apple.com/support/offering-account-deletion-in-your-app/ | Read 2026-10-12 | Whole account, guest accounts, Sign in with Apple token revocation, Korea endpoint, subscriptions, timing, no support loops, website step [Official, 2026-10] |
| 9 | Third-party SDK requirements | Apple Developer Support | https://developer.apple.com/support/third-party-SDK-requirements/ | Read 2026-10-12 | 86 SDKs that need a privacy manifest and signature; any version and repackaged SDKs covered [Official, 2026-10] |
| 10 | Privacy manifest files | Apple Developer Documentation | https://developer.apple.com/documentation/bundleresources/privacy-manifest-files | Read 2026-10-12 | File name, keys, tracking domains, target resources [Official, 2026-10] |
| 11 | Describing use of required reason API; NSPrivacyAccessedAPIType | Apple Developer Documentation | https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api | Read 2026-10-12 | Five categories, APIs and reason codes; not accepted since 2024-05-01 [Official, 2026-10] |
| 12 | Protected resources; NSUserTrackingUsageDescription; NSCameraUsageDescription and related keys | Apple Developer Documentation | https://developer.apple.com/documentation/bundleresources/protected-resources | Read 2026-10-12 | Usage description keys; ATT crash without the key; keys required when the APIs are used [Official, 2026-10] |
| 13 | ITSAppUsesNonExemptEncryption; Complying with encryption export regulations | Apple Developer Documentation | https://developer.apple.com/documentation/bundleresources/information-property-list/itsappusesnonexemptencryption and https://developer.apple.com/documentation/security/complying-with-encryption-export-regulations | Read 2026-10-12 | Key meaning, exempt OS encryption, documentation code, questionnaire on each upload without the key, self classification report [Official, 2026-10] |
| 14 | com.apple.developer.applesignin | Apple Developer Documentation | https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.applesignin | Read 2026-10-12 | Sign in with Apple entitlement [Official, 2026-10] |
| 15 | Auto-renewable subscriptions | Apple Developer | https://developer.apple.com/app-store/subscriptions/ | Read 2026-10-12 | Sign-up screen requirements, billed amount most prominent, trials, Terms and Privacy links [Official, 2026-10] |
| 16 | Upcoming requirements | Apple Developer News | https://developer.apple.com/news/upcoming-requirements/ | Read 2026-10-12 | Xcode 26 and iOS 26 SDK since 2026-04-28; iOS 13 minimum target since 2026-09-09; age rating answers by 2026-01-31; DSA trader dates; required reasons since 2024-05-01; Game Center entitlement since 2023-08-16 [Official, 2026-10] |
| 17 | App Store submissions now open for the latest OS releases | Apple Developer News | https://developer.apple.com/news/?id=k1mtkt1k | 2026-09-09 | iOS 27 SDK from April 2027; social media capability declaration; Time Allowances [Official, 2026-09] |
| 18 | Age rating questionnaire now includes social media questions | Apple Developer News | https://developer.apple.com/news/?id=tlur8uvi | 2026-07-09 | Definition; responses required from September 2026; Social Media descriptor [Official, 2026-07] |
| 19 | Age ratings values and definitions | App Store Connect Help | https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions | Read 2026-10-12 | Tiers; loot boxes 9+ (AU 16+, BR A18); simulated gambling; social media 13+; unrestricted web access 16+; advertising, UGC, messaging, parental controls, age assurance [Official, 2026-10] |
| 20 | Screenshot specifications | App Store Connect Help | https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications | Read 2026-10-12 | Counts, formats, required iPhone and iPad sizes, scaling, iPhone Duo from April 2027 [Official, 2026-10] |
| 21 | Updates to App Tracking Transparency in the European Union | Apple Developer News | https://developer.apple.com/news/?id=idsft9ai | 2026-09-16 | Alternative ATT prompt from iOS 27.2; only alternative in DE, FR, IT, PL, RO [Official, 2026-09] |
| 22 | Update: New domain for Sign in with Apple | Apple Developer News | https://developer.apple.com/news/?id=1ptvdtcm | 2026-08-24 | `private.icloud.com` relay addresses; accept both domains [Official, 2026-08] |
| 23 | Get your subscriptions ready for iOS 27 | Apple Developer News | https://developer.apple.com/news/?id=likeohx4 | 2026-09-16 | StoreKit 2, Bundles and Suites, multiseat on by default, Volume Purchasing 2026-10-22 [Official, 2026-09] |
| 24 | Changes for apps in the European Union | Apple Developer News | https://developer.apple.com/news/?id=gmws0jgp | 2026-08-18 | Terms from 2026-10-01: commission changes, alternative payments alongside IAP, child safety protections [Official, 2026-08] |
| 25 | Prepare and submit your apps for iPhone Duo | Apple Developer News | https://developer.apple.com/news/?id=kkphp5qo | 2026-10-05 | iPhone Duo screenshots required from April 2027 [Official, 2026-10] |
| 26 | Apple Developer News (list of 2026 items) | Apple Developer | https://developer.apple.com/news/ | Read 2026-10-12 | Dates and titles: Texas update 2026-06-03 (effective 2026-06-04), Brazil betting license 2026-05-08, random chat under 1.2 2026-02-06, Australia and Vietnam age ratings 2026-05-21, Korea age ratings 2026-08-12, medical devices 2026-03-26, 12 month commitment subscriptions 2026-04-27, age requirements 2026-02-24 [Official, 2026-10] |

## Apple: opened in the 2026-10-12 research pass (not re-read)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 27 | App Review Information and app information fields | App Store Connect Help | URL not recorded (developer.apple.com/help/app-store-connect) | 2026-10 | Notes up to 4,000 bytes; international phone; copyright "year owner" [Official, 2026-10] |
| 28 | DSA trader requirements | App Store Connect Help | URL not recorded | 2026-10 | Trader status even outside the EU; verification of email, phone, documents; submission held [Official, 2026-10] |
| 29 | Export compliance overview | App Store Connect Help | URL not recorded | 2026-10 | Questionnaire flow [Official, 2026-10] |
| 30 | TestFlight overview | App Store Connect Help | URL not recorded | 2026-10 | Beta App Review for the first external build, required fields, 10,000 testers, 90 day expiry [Official, 2026-10] |
| 31 | App privacy details | App Store Connect Help | URL not recorded | 2026-10 | Answers include SDK data and match the live version [Official, 2026-10] |
| 32 | Apps in the EU (DMA terms) | Apple Developer Support | URL not recorded (developer.apple.com/support/apps-in-the-eu) | 2026-10 | IAP 26% (15%), alternative payment 20% (10%), link out 15% (10%), CTC 5% from 2026-10-01 [Official, 2026-10] |
| 33 | Games app, Game Center, In-App Events, product page | Apple Developer | developer.apple.com/games-app and related pages (URLs not recorded) | 2026-10 | Games app in iOS 26; leaderboards, challenges, achievements, activities; previews up to 3 x 30 seconds [Official, 2026-10] |
| 34 | 2.3.3 Show your app in use with screenshots | App Review Help | https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots | 2026-10 | Screenshot rejections [Official, 2026-10] |
| 35 | Guideline revision news items | Apple Developer News | Item ids recorded in the notes: a233fmpw, d75yllv4, ey6d8onl, 3d8a9yyh (id to date mapping not recorded) | 2025-11-13, 2026-02-06, 2026-06-08 | 4.1(c), 4.7 mini apps, 5.1.2(i) AI disclosure (2025-11); random chat in 1.2 (2026-02); 4.3 clarified, 4.5.3, kid and teen safety introduction (2026-06) [Official, 2025-11 to 2026-06] |

## Apple: search results only

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 36 | App Store Transparency Report 2025 | Apple | apple.com/legal/app-store/transparency (not reachable from this environment) | 2026 | 9,100,620 reviewed, 2,093,244 rejected, 387,087 approved after rejection, rejections by section [Reported, 2026-10] |
| 37 | Game Center features submittable separately during review | Apple Developer News via search | URL not recorded | 2025-10 | [Reported, 2026-10] |

## Capacitor (the SDK maker's own documentation)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 38 | @capacitor/camera 8.2.5, @capacitor/geolocation 8.2.3, @capacitor/barcode-scanner 3.1.3, @capacitor/preferences 8.0.1, @capacitor/filesystem 8.1.4, @capacitor/push-notifications 8.1.3 READMEs; @capacitor/ios 8.5.3 package contents | Ionic (Capacitor) via the npm registry | https://registry.npmjs.org/@capacitor/camera (and the same path per package) | Read 2026-10-12 | Purpose string keys per plugin; privacy manifest categories and reasons (UserDefaults CA92.1, FileTimestamp C617.1); Capacitor frameworks ship empty manifests; Push capability [Official, 2026-10] |

## Google: developer.android.com

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 39 | Target API level requirements for Google Play apps | Android Developers | https://developer.android.com/google/play/requirements/target-sdk | Updated 2026-10-01; read 2026-10-15 | API 36 from 2026-08-31 (form factor exceptions), extension to 2026-11-01, existing apps API 35 [Official, 2026-10] |
| 40 | Google Play Billing Library deprecation FAQ | Android Developers | https://developer.android.com/google/play/billing/deprecation-faq | Updated 2026-09-09; read 2026-10-15 | Version 8 or later from 2026-08-31, extension 2026-11-01 (the table lists the version that stops being accepted) [Official, 2026-09] |
| 41 | Android vitals | Android Developers | https://developer.android.com/topic/performance/vitals | 2026-10 (research pass) | 1.09% crash, 0.47% ANR, 8% per phone model, 28 days, visibility effects [Official, 2026-10] |
| 42 | Play App Signing; Android App Bundle | Android Developers | https://developer.android.com/studio/publish/app-signing and https://developer.android.com/guide/app-bundle | 2026-10 (research pass) | AAB since 2021-08, Play App Signing for new apps, 4 GB, no .obb [Official, 2026-10] |
| 43 | Android developer verification and FAQ | Android Developers | https://developer.android.com/developer-verification | 2026-10 (research pass) | 2026-09-30 in BR, ID, SG, TH; global 2027; D-U-N-S up to 28 days [Official, 2026-10] |
| 44 | Foreground service types, exact alarms, photo picker, declare data use | Android Developers | developer.android.com pages (exact URLs not recorded) | 2026-10 (research pass) | Permission rules; Data safety must include SDKs [Official, 2026-10]; picker deadline 2026-10-28 vs 2027-01-27 [Contested] |
| 45 | Play Billing subscriptions | Android Developers | https://developer.android.com/google/play/billing/subscriptions | 2026-10 (research pass) | Access to period end, trial conversion, trial eligibility [Official, 2026-10] |
| 46 | Trusted Web Activities overview and quick start guide | Android Developers | https://developer.android.com/develop/ui/views/layout/webapps/trusted-web-activities and https://developer.android.com/develop/ui/views/layout/webapps/guide-trusted-web-activities-version2 | Read 2026-10-15 | Digital Asset Links trust; Custom Tab fallback; wrong signature as a common cause; browser choice [Official, 2026-10] |
| 47 | Configure the assetlinks.json file | Android Developers | https://developer.android.com/training/app-links/configure-assetlinks | Read 2026-10-15 | File format, HTTPS, JSON content type, no redirects, Play Console fingerprint and snippet [Official, 2026-10] |
| 48 | Play policies; Play policy newsletters 2026 (April, June, July, September) | Android Developers | https://developer.android.com/distribute/play-policies (newsletter URLs not recorded) | 2026-10 (research pass) | Account transfer 2026-05-27; memory and device migration 2027-02; FGS geofencing and READ_CALL_LOG 2027-01-27; anonymous chat and children 2026-08-26 [Official, 2026-10] |

## Google: Play Console Help and blog (search results only)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 49 | App testing requirements for new personal developer accounts (answer 14151465) | Play Console Help | https://support.google.com/googleplay/android-developer/answer/14151465 | 2026 | 12 testers, 14 days, accounts after 2023-11-13, about 48 hours to a decision [Reported, 2026-10] |
| 50 | Account deletion requirements (answer 13327111) | Play Console Help | https://support.google.com/googleplay/android-developer/answer/13327111 | 2026 | In app and web link; deactivation does not count [Reported, 2026-10] |
| 51 | Subscriptions policy (answer 9900533) | Play Console Help | https://support.google.com/googleplay/android-developer/answer/9900533 | 2026 | Disclosure and cancellation [Reported, 2026-10] |
| 52 | Two further Play Console Help answers (11926878, 9858738) cited by the research notes | Play Console Help | https://support.google.com/googleplay/android-developer/answer/11926878 (and 9858738) | 2026 | App content forms and review timing as summarized in the notes; topics per answer not recorded [Reported, 2026-10] |
| 53 | Play expanded billing and fees | Android Developers Blog | URL not recorded (android-developers.googleblog.com, 2026-06) | 2026-06 | Fee changes from 2026-06-30 [Reported, 2026-10] |
| 54 | Play rejection and suspension causes; review times; termination appeals | Search results across Play Console Help and coverage | URLs not recorded | 2026 | Data safety mismatch, privacy policy, permissions, metadata, impersonation, incentivized installs, crashes, webview apps; hours to 7 business days; 180 day termination appeal; ban evasion [Reported, 2026-10] |
| 55 | Webview apps and minimum functionality | Android Developers Blog or Play policy post | URL not recorded | 2020 | Webview only apps flagged [Reported, 2026-10] |

## Regulation and game rules (search results only)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 56 | ASA and CAP enforcement notice on loot box disclosure | ASA (PDF), Lewis Silkin coverage | URL not recorded (asa.org.uk) | 2026-02-26 | "Contains loot boxes" in listings; monitoring from 2026-05-26 [Reported, 2026-10] |
| 57 | Brazil Law 15.211/2025 (ECA Digital) | Demarest coverage | URL not recorded | 2025 to 2026 | Paid loot boxes banned for minors from 2026-03 [Reported, 2026-10] |
| 58 | Turkey Law 7578 | Evrensel, NTV coverage | URL not recorded | 2026-04-22 | Under 15 social media bar; game platform ratings and parental purchase approval [Reported, 2026-10] |
| 59 | PEGI and paid random items | Lewis Silkin | URL not recorded | 2026-03-18 | PEGI 16 default from 2026-06-01 [Reported, 2026-10] |
| 60 | FTC and Cognosphere (Genshin Impact) settlement | US Federal Trade Commission blog | URL not recorded (ftc.gov) | 2025-01 | USD 20 million; under 16 purchases need parental consent; odds [Reported, 2026-10] |
| 61 | Belgium loot boxes; Netherlands Raad van State 2022 | SBC News, raadvanstate.nl | URL not recorded | 2018, 2022 | Belgium treats paid loot boxes as gambling; Netherlands no ban [Reported, 2026-10] |
| 62 | Epic v Apple anti-steering litigation | Fenwick, The Next Web | URL not recorded | 2025-04 to 2026-08 | Zero commission order, Ninth Circuit ruling, rehearing denial, Supreme Court review, no rate set [Reported, 2026-10] |
| 63 | COPPA amendments compliance date | White & Case | URL not recorded | 2026-04-22 | [Reported, 2026-10] |

## Source hygiene for this package

1. Before a G3 action rests on a [Reported] or [Unverified] rule (most Play Console Help rows), read the page in full or check the live console, and record the result with the `ads-verify` skill in `ads-master/VERIFIED.md`.
2. The live console wins for that account, then the official page, then coverage.
3. Add new sources with the next number; never renumber.
4. When Apple updates the guidelines, re-read every guideline this package quotes and update the label month.

## Where the evidence is thin (feeds the verification queue)

- Google Play closed testing: 12 testers, 14 days, the 2023-11-13 cutoff and the 48 hour decision were seen only in Play Console Help search results.
- Google Play account deletion: the web link requirement and "deactivation does not count" come from search results; Apple's equivalent rules were read at the source.
- Play Data safety category names and the App access form wording are from long standing console use, not a 2026 read.
- Apple's minimum deployment target for April 2027 (iOS 15 in the research notes) is not stated in the news item read on 2026-10-12.
- The 2025 App Store transparency report figures are from search results; apple.com could not be opened.
- What Apple accepts as enough native value for a wrapper (4.2) has no official list; practitioner reports only.
- Whether Play requires Play Billing through the Digital Goods API for digital goods in TWAs was seen only in search results.
- Picker permission deadline: two official pages gave 2026-10-28 and 2027-01-27.
- EU commission rates from 2026-10-01 were read once in the research pass; the 2026-08-18 news item confirms the changes but not the numbers.

## Claims considered and not relied on

| Claim | Why not used |
|-------|-------------|
| "40% of unresolved issues are 2.1" as a vendor statistic | Replaced by Apple's own App Review page, which states it [Official, 2026-10] |
| A maintained Capacitor Game Center plugin exists | Not confirmed in the research pass; native code is the safe plan |
| Capgo widget kit as a route to widgets in Capacitor apps | A vendor tool seen in search results and not evaluated; widgets are native extensions either way |
| Live updates of web bundles are always allowed | Vendor reading of the License Agreement; 2.5.2 forbids features added through downloaded code |
| Push, location or sharing make a wrapper pass 4.2 | Reported as not enough on their own |
| "Level Up" program for Play games | Unverified in the research pass |
| Specific review times for Play beyond "hours to about 7 business days" | Single summaries; the live console and history win |
