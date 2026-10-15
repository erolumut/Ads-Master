# Apple Review Checklist (by guideline)

> Knowledge as of 2026-10. Guideline text was read at the source on 2026-10-15 (App Review Guidelines, last updated 2026-06-08) and is labeled [Official, 2026-06]. App Store Connect Help and Apple Developer pages read on 2026-10-12 to 2026-10-15 without a visible date are labeled [Official, 2026-10]. Apple revises the guidelines several times a year (2025-11-13, 2026-02-06 and 2026-06-08 in the last year): read the current text before every first submission and after every news item that mentions App Review. Privacy rules are in [Apple privacy and SDK requirements](apple-privacy-and-sdk-requirements.md); payments in [Apple payments and subscriptions review](apple-payments-and-subscriptions-review.md); wrappers and games in [Wrapped web apps and games](wrapped-web-apps-and-games.md).

## 1. How App Review behaves

| Fact | What it means for the plan | Evidence |
|------|----------------------------|----------|
| App Review typically reviews at least 50% of submissions in under 24 hours and 90% in under 48 hours | Plan 2 working days per review round, plus one spare round for a first submission | [Official, 2026-10] |
| A complex app or one that presents new issues may need greater scrutiny | First submissions of wrappers, mini game hosts, AI apps and regulated apps take longer | [Official, 2026-06] |
| An app repeatedly rejected for the same guideline, or one that tried to manipulate review, takes longer to review | Repeat rejections cost time on every later submission: the KPI target is zero | [Official, 2026-06] |
| After approval it can take up to 24 hours for the app to appear on all selected storefronts | Never announce a launch hour; announce a day | [Official, 2026-06] |
| A future release date holds the approved app until that date | Use a manual or dated release for launches tied to marketing | [Official, 2026-06] |
| Over 40% of unresolved issues relate to Guideline 2.1 App Completeness (crashes, placeholder content, incomplete information) | Completeness is where first pass approval is won or lost | [Official, 2026-10] (Apple's App Review page; earlier seen only on vendor blogs) |
| 2025 transparency report: 9,100,620 submissions reviewed, 2,093,244 rejected (about 23%), 387,087 approved after an earlier rejection; rejections by section (overlapping): Performance 1,354,418, Legal 495,673, Design 415,532, Business 283,820, Safety 151,159, Other 4,145 | Performance (section 2, which holds 2.1) is the largest group | [Reported, 2026-10] (search result of apple.com/legal/app-store/transparency; the page could not be opened from this environment) |
| App Review offers 30 minute video appointments to discuss guidelines | Book one before a first submission of a borderline app (wrapper, mini games, AI, kids) | [Official, 2026-10] |

## 2. Checklist by guideline

Each row: what the reviewer checks, how we verify before submission, and who fixes it. "Dossier" means a line in `ads-master/SUBMISSION.md` ([template](submission-dossier-template.md)); "script" means `submission_check.py`.

### Safety (section 1)

| Guideline | What the reviewer checks | How we verify | Owner of the fix |
|-----------|--------------------------|---------------|------------------|
| 1.2 User generated content | Apps with UGC or social networking include a filter for objectionable material, a way to report content with timely responses, the ability to block abusive users, and published contact information [Official, 2026-06] | Walk the four controls on a device; dossier line "User generated content controls" | App team |
| 1.2 random or anonymous chat | Apps with random or anonymous chat fall under 1.2 (revised 2026-02-06) [Official, 2026-02] | Same four controls on every chat surface, including in-game chat | App team |
| 1.3 Kids Category | No links out, purchases or other distractions unless behind a parental gate; no sending personal or device information to third parties; no third party analytics or advertising except the limited cases the guideline allows [Official, 2026-06] | SDK data map shows no ad or analytics SDK, or only ones meeting the 1.3 exceptions; parental gate on every link and purchase | App team, compliance |

### Performance (section 2)

| Guideline | What the reviewer checks | How we verify | Owner |
|-----------|--------------------------|---------------|-------|
| 2.1(a) Completeness | Final version, all metadata, fully functional URLs, no placeholder text or empty websites, tested on device, demo account info when there is a login, back end turned on; a demo mode only with Apple's prior approval; no crashes or obvious technical problems [Official, 2026-06] | Release QA on current iOS on device; script flags placeholder purpose strings; dossier sections 2 and 6; every URL opened on the submission day | App team, site-engineer for web backed apps |
| 2.1(b) In-app purchases | Every configured in-app purchase is complete, up to date, visible to the reviewer and functional; if one cannot be found, the review notes explain why [Official, 2026-06] | Buy each product in the sandbox with the demo account; dossier "In-app purchases attached to this version" | App team |
| 2.3.3 Screenshots | Show the app in use, not only title art, a login page or a splash screen [Official, 2026-06] | Check every device size set before upload | app-store-optimization drafts, store-submission checks |
| 2.3.4 Previews | Only video screen captures of the app itself; narration and overlays allowed [Official, 2026-06] | No rendered trailer footage, no live action, no gameplay the build does not have | video-studio, store-submission checks |
| 2.3.7 Metadata | No trademarked terms, popular app names, pricing information or irrelevant phrases to game the system; name up to 30 characters; subtitles make no unverifiable claims and reference no other apps [Official, 2026-06] | `aso_metadata_check.py` (app-store-optimization) plus a read | app-store-optimization |
| 2.3.8 Audience | Icons, screenshots and previews fit a 4+ rating even if the app is rated higher; "For Kids" and "For Children" reserved for the Kids Category [Official, 2026-06] | Visual read of all assets including in-app purchase icons | app-store-optimization |
| 2.3.10 Other platforms | No names, icons or imagery of other mobile platforms or alternative app marketplaces in the app or metadata unless there is approved interactive functionality [Official, 2026-06] | Search screenshots and text for "Android", "Google Play" and their icons; wrappers often leak a "Get it on Google Play" badge from the website | App team, app-store-optimization |
| 2.5.1 Software requirements | Public APIs only; runs on the currently shipping OS; deprecated technologies phased out [Official, 2026-06] | Build with the current SDK (section 4); test on the newest iOS release | App team |
| 2.5.2 Self contained | No downloading, installing or executing code that introduces or changes features or functionality [Official, 2026-06] | Wrappers and live update services: a feature App Review has not seen never ships through a remote bundle. Live update vendors say small fixes are allowed under the Developer Program License Agreement; that is a vendor reading [Unverified] | App team, site-engineer |

### Business (section 3)

Detail in [Apple payments and subscriptions review](apple-payments-and-subscriptions-review.md). Headline checks:

| Guideline | Check |
|-----------|-------|
| 3.1.1 | Digital content and features unlocked in the app use in-app purchase; purchased credits and currencies do not expire; a restore mechanism exists for restorable purchases; loot boxes disclose odds before purchase [Official, 2026-06] |
| 3.1.1(a), 3.1.3 | Buttons and links to web purchases are allowed on the United States storefront without an entitlement; elsewhere only with the regional entitlements [Official, 2026-06] |
| 3.1.2(a), 3.1.2(c) | Auto-renewable subscriptions give ongoing value, last at least 7 days, work on all the user's devices, and the sign-up screen describes what the user gets for the price [Official, 2026-06] |
| 3.1.3(b) | Items bought on another platform may be used in the app if they are also sold as in-app purchases [Official, 2026-06] |

### Design (section 4)

| Guideline | What the reviewer checks | How we verify | Owner |
|-----------|--------------------------|---------------|-------|
| 4.1(c) Copycats | No use of another developer's name or icon (added 2025-11) [Official, 2025-11] | Name and icon read against the category's top apps | app-store-optimization |
| 4.2 Minimum functionality | Features, content and UI that elevate the app beyond a repackaged website [Official, 2026-06] | The native value list in [Wrapped web apps and games](wrapped-web-apps-and-games.md) section 2, visible to the reviewer and named in the notes | App team, site-engineer |
| 4.2.2 | Other than catalogs, not primarily marketing materials, advertisements, web clippings, content aggregators or a collection of links [Official, 2026-06] | The core loop works inside the app, without the browser | App team |
| 4.2.3 | Works on its own without another app; if it downloads resources on first launch, it discloses the size and asks first [Official, 2026-06] | First launch on a clean device on a slow network | App team |
| 4.3(a) Spam | One Bundle ID per app; variations through in-app purchase rather than many near identical apps [Official, 2026-06] | Portfolio check before a second game on the same template | growth-orchestrator, store-submission |
| 4.3(b) Spam | Not indistinguishable from what is already widely available; saturated categories need a meaningfully different experience; repeated submissions of this kind can lead to removal from the program (clarified 2026-06-08) [Official, 2026-06] | State the difference in the notes; for template games, ship real differences in mechanics and content, not reskins | App team |
| 4.5.3 Live Activities | No spam (2026-06) [Official, 2026-06] (from the research pass; text not re-read) | Live Activities only for live state the user asked for | App team |
| 4.7 Mini apps, mini games, streaming games, chatbots, plug-ins, emulators | The app is responsible for all such software; 4.7.1 to 4.7.5 apply [Official, 2026-06] | [Wrapped web apps and games](wrapped-web-apps-and-games.md) section 5 | App team, compliance |
| 4.8 Login services | Apps that use a third party or social login (Facebook Login, Google Sign-In, Log in with X, Sign In with LinkedIn, Login with Amazon, WeChat Login) for the primary account also offer an equivalent login that limits data to name and email, lets users keep their email private, and does not collect interactions for advertising without consent [Official, 2026-06] | script (Google or Facebook sign in without Sign in with Apple fails); dossier "Sign in with Apple" | App team |

4.8 exceptions, verbatim in substance [Official, 2026-06]: the app exclusively uses the company's own account system; it is an alternative app marketplace (or distributed from one) using a marketplace login; it is an education, enterprise or business app requiring an existing education or enterprise account; it uses a government or industry backed citizen identification system or electronic ID; it is a client for a specific third party service where users sign in to their own mail, social media or other account to reach their content. An exception goes into the dossier with the reason and into the review notes; the script then warns instead of failing so a human confirms it.

### Legal (section 5)

Detail in [Apple privacy and SDK requirements](apple-privacy-and-sdk-requirements.md). Headline checks: privacy policy link in App Store Connect and in the app (5.1.1(i)); consent, purpose strings and withdrawal (5.1.1(ii)); data minimization (5.1.1(iii)); no forced consent (5.1.1(iv)); account deletion in the app when accounts can be created (5.1.1(v)); permission before sharing personal data, including with third party AI, and ATT for tracking (5.1.2(i)); kids data (5.1.4) [Official, 2026-06].

## 3. Platform forms in App Store Connect

| Form | Requirement | Evidence | Dossier line |
|------|-------------|----------|--------------|
| Age rating questionnaire | Tiers 4+, 9+, 13+, 16+, 18+ and Unrated; an Unrated app cannot be published on the App Store | [Official, 2026-10] | Age rating questionnaire answered |
| Updated questions | Answers to the updated questions were due by 2026-01-31 to avoid interruption of updates | [Official, 2026-10] | Same |
| Social media capability | Questions about social media capabilities (redistributing, amplifying or interacting with user generated content through a feed or similar discovery method) are required for new apps and updates from September 2026; apps with them show a Social Media descriptor and fall in the Social Media Time Allowance category | [Official, 2026-07] | Social media question answered |
| Social media rating | Social media capability sets a 13+ minimum; "Social media disabled for users under 13" requires at least a Declared Age Range API check before enabling the features; Australia 16+, Brazil A16 | [Official, 2026-10] | Same |
| Capabilities that move the rating | Unrestricted web access 16+ (Brazil A16); advertising 4+ (Brazil A12); user generated content and messaging 4+ (Brazil A6 and A12); parental controls and age assurance 4+ | [Official, 2026-10] | Age rating questionnaire answered |
| Game content that moves the rating | Loot boxes 9+ (Australia 16+, Brazil A18); infrequent simulated gambling 13+ (Australia R 18+, Brazil A12); frequent simulated gambling 18+; gambling 18+ | [Official, 2026-10] | Same |
| Regional ratings | Updates for Australia and Vietnam (news 2026-05-21) and the Republic of Korea (news 2026-08-12) | [Official, 2026-10] (titles read in the news list; detail in mobile-app-growth's policies module) | Same |
| EU DSA trader status | Required to distribute in the EU; apps without it were removed from the EU storefronts from 2025-02-17; updates need it since 2024-10-16; traders verify email, phone and documents and the submission waits until verification is done | [Official, 2026-10] | EU DSA trader status |
| Export compliance | `ITSAppUsesNonExemptEncryption` NO when the app (including linked libraries) uses no encryption or only exempt encryption; encryption built into the OS, such as HTTPS through URLSession, is typically exempt from documentation upload; YES needs documentation and then `ITSEncryptionExportComplianceCode`; without the key, App Store Connect asks the questions on every upload; exempt encryption may still need a year end self classification report | [Official, 2026-10] | Export compliance answered |
| Regulated medical device status | Apps in the EEA, UK and US declare regulated medical device status (news 2026-03-26) | [Official, 2026-03] | Medical device status |
| Brazil betting license | Required for availability of betting apps in Brazil (news 2026-05-08) | [Official, 2026-05] | Regulated documents attached |
| Texas age assurance | New Texas Apple Accounts subject to SB 2420 from 2026-06-04; developers can request age category data through the Declared Age Range API | [Official, 2026-06] | Compliance verdict in the dossier |
| Content rights | Confirm rights to third party content; attach documentation for another party's intellectual property | [Official, 2026-10] for documentation; the exact form field wording [Unverified] | Content rights |

The export compliance answer is a legal statement made by the account holder. `store-submission` drafts it from the SDK data map and the code (custom cryptography, VPN, end to end encryption libraries); the human confirms it, with legal counsel when anything beyond OS provided TLS is in the build.

## 4. Build, SDK and device requirements

| Requirement | Date | Evidence |
|-------------|------|----------|
| Built with Xcode 26 or later using the iOS 26 (or matching platform 26) SDK | Since 2026-04-28 | [Official, 2026-10] |
| iOS and iPadOS apps must target iOS 13 or later | Since 2026-09-09 | [Official, 2026-10] |
| iOS 27 and iPadOS 27 SDK or later (Xcode 27 suggested for the latest SDKs) | From April 2027 | [Official, 2026-09] |
| Minimum deployment target iOS 15 from April 2027 | Recorded in the research notes; not stated in the 2026-09-09 news item read here | [Unverified] |
| Required reason API declarations in privacy manifests | Since 2024-05-01 | [Official, 2026-10] |
| Game Center entitlement and App Store Connect configuration before submitting Game Center features | Since 2023-08-16 | [Official, 2026-10] |
| iPhone Duo screenshots for apps built with the iOS 27.1 SDK or later | From April 2027 | [Official, 2026-10] |

## 5. Screenshots, previews and iPad

| Item | Rule | Evidence |
|------|------|----------|
| Count and format | At least 1 and up to 10 screenshots per device size; `.jpeg`, `.jpg` or `.png`; no alpha channel or transparency | [Official, 2026-10] |
| Required iPhone size | iPhone with Dynamic Island (medium display): 1179 x 2556 or 1206 x 2622 portrait (or the landscape pairs) | [Official, 2026-10] |
| Required iPad size | 13 inch display: 2064 x 2752 or 2048 x 2732 portrait (or landscape), required when the app runs on iPadOS | [Official, 2026-10] |
| Scaling | A consistent UI needs only the highest required resolution; App Store Connect scales down | [Official, 2026-10] |
| iPhone Duo | Outer display 1398 x 2034, inner display 2007 x 2853 (portrait); required from April 2027 for iOS 27.1 SDK builds | [Official, 2026-10] |
| Previews | Up to 3 previews of up to 30 seconds, muted autoplay; screen captures of the app only (2.3.4) | [Official, 2026-10] (count and length from the research pass) |
| iPad layout | A universal app needs a usable iPad layout; a stretched phone UI with broken controls is a 2.1 or 4.0 design rejection risk | [Official, 2026-10] (research pass), guideline number [Unverified] |
| Screenshot guidance and new asset types | Updated 2026-10-05 with the new header and search result assets | [Official, 2026-10]; asset work belongs to app-store-optimization |

## 6. App Review Information

| Field | Rule | Evidence |
|-------|------|----------|
| Sign-in information | A username and password that work at submission; credentials that expire or change before review can get the submission rejected | [Official, 2026-10] |
| Notes | Up to 4,000 bytes; concept and business model for new apps, what changed for updates, purpose and audience, devices and OS versions tested, external services (data providers, authentication, payments, AI), required hardware (a video of the real device, not a screen recording), regional differences | [Official, 2026-10] |
| Attachments | Partnership or authorization documents in the Attachment section, with descriptions in the notes | [Official, 2026-10] |
| Contact | Complete and current, with an international phone number | [Official, 2026-10] |
| Support URL | Real contact information; a support link and a privacy policy link are required for all apps | [Official, 2026-10] |
| Copyright | "Year owner" format | [Official, 2026-10] (research pass) |

Templates: [Review notes and demo accounts](review-notes-and-demo-accounts.md).

## 7. TestFlight before the first App Store submission

| Fact | Evidence |
|------|----------|
| The first build sent to an external tester group goes through Beta App Review | [Official, 2026-10] (research pass) |
| External testing needs a beta description, test instructions and a feedback email | [Official, 2026-10] (research pass) |
| Up to 10,000 external testers; builds expire after 90 days | [Official, 2026-10] (research pass) |

Use Beta App Review as a dress rehearsal: the same demo account, the same notes. A Beta App Review rejection is a free warning, not a KPI event; log it in the journal anyway.

## 8. Run order before every Apple submission

1. Freshness check: App Review Guidelines last updated date, Upcoming Requirements, the last 30 days of Apple Developer News.
2. Build: Xcode and SDK version meet section 4; tested on device on the current iOS.
3. `submission_check.py <project> --dossier ads-master/SUBMISSION.md` (add `--policy` for games): exit 0, or every WARN accepted in dossier section 11.
4. Privacy: App Privacy answers re-compared with the SDK data map; privacy manifests present; purpose strings specific and localized.
5. Payments: every product Ready to Submit and attached to the version; paywall disclosures checked; restore works; odds screen for random items.
6. Forms: age rating with the social media question, export compliance, DSA trader status, content rights, regulated documents.
7. Listing: screenshots per section 5; metadata checked by app-store-optimization with a compliance verdict.
8. App Review Information: demo account tested on the submission day from a clean install, notes pasted, contact current.
9. Change request with the human's approval line; the human presses submit (G3).
10. Log the submission in `ads-master/data/store_submissions.csv` and the journal.
