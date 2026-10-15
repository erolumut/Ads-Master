# Wrapped Web Apps and Games

> Knowledge as of 2026-10. Apple guideline text read at the source on 2026-10-15 ([Official, 2026-06]); age rating values, account deletion and protected resource pages read 2026-10-12 ([Official, 2026-10]); Android Trusted Web Activity and App Links pages read on developer.android.com 2026-10-15 ([Official, 2026-10]); Capacitor plugin facts from the official npm READMEs. Most practitioner claims about what "enough native value" means were seen only in search results and carry [Reported, 2026-10] or [Unverified]. `site-engineer` builds and releases wrappers; this module says what must be true for them to pass review.

## 1. Which route for which store

| Route | Stores | What it is | Main review risk |
|-------|--------|------------|------------------|
| Trusted Web Activity (Bubblewrap or Android Browser Helper) | Google Play | The site runs full screen in the user's browser engine, verified by Digital Asset Links | Verification fails (browser bar shows), webview only minimum functionality, Play Billing for digital goods |
| Capacitor (iOS and Android) | App Store, Google Play | A native shell with a web view and native plugins | Apple 4.2 (repackaged website), purpose strings, privacy manifest, 3.1.1 for digital goods |
| Native or engine build (Swift, Kotlin, Unity, Godot) | Both | Compiled app | Normal checklists; engine SDKs on Apple's privacy manifest list (UnityFramework) |
| PWA only | None (installed from the browser) | No store review | Not a store submission; iOS web push only for Home Screen web apps after a user gesture [Reported, 2026-10] |

Order the proposal recommends for a web first game: web (own payments) first, then the Play TWA, then iOS through Capacitor with Game Center so it clears 4.2.

## 2. Apple 4.2 for wrapped web apps

Rules [Official, 2026-06]:
- 4.2: the app includes features, content and UI that elevate it beyond a repackaged website.
- 4.2.2: other than catalogs, not primarily marketing, ads, web clippings, content aggregators or a collection of links.
- 4.2.3: works on its own; discloses download size before fetching resources on first launch.
- Account deletion page: sending people to the browser to sign in or register is a poor experience and not appropriate under Guideline 4 [Official, 2026-10].

What reviewers are reported to accept: native features that change the experience on the device, used in the core loop. Push, location or sharing alone are reported as not enough [Reported, 2026-10]. There is no official list; the table below is a working list ordered by how much a reviewer can see.

| Native value | How in Capacitor | Notes | Evidence |
|--------------|------------------|-------|----------|
| Game Center: sign in, leaderboards, achievements, challenges, Games app presence | Native code or a plugin (a maintained Capacitor Game Center plugin was not confirmed) | Needs the Game Center entitlement and App Store Connect configuration before submission (since 2023-08-16) | [Official, 2026-10] for the entitlement rule; plugin [Unverified] |
| In-app purchase through StoreKit | Native bridge or a purchases SDK | Required anyway for digital goods (3.1.1) | [Official, 2026-06] |
| Offline play of the core loop | Bundled web assets plus local storage | The app opens and plays without network; say so in the notes | [Practitioner consensus] |
| Native push for the core loop (daily puzzle ready, friend beat your score) | `@capacitor/push-notifications` with the Push capability | Push needs opt in and real value | [Official, 2026-10] for the capability |
| Haptics in play | `@capacitor/haptics` | Small, but visible on every move | [Reported, 2026-10] |
| Native share sheet with a generated image | Share plugin | Share cards that hide answers are a good fit for daily games | [Practitioner consensus] |
| Widgets | Native extension | Higher effort; strong signal of native value | [Reported, 2026-10] |
| Sign in with Apple | Plugin plus entitlement | Needed when Google or Facebook login exists (4.8) | [Official, 2026-06] |
| Native navigation, safe areas, no browser chrome, no pinch zoom of the page | Capacitor config and CSS | A page that scrolls like a website reads as a website | [Practitioner consensus] |
| Local notifications (streak reminder the user set) | Local notifications plugin | User controlled schedule | [Practitioner consensus] |

Wrapper rules this agent checks before an iOS submission:
1. The web view never shows a site header, cookie banner meant for browsers, app store badges ("Get it on Google Play" breaks 2.3.10), or links to the website's own checkout.
2. Navigation is locked to the app's own origin. Free browsing of any web page is "Unrestricted web access" in the age rating questionnaire, which sets 16+ (Brazil A16) [Official, 2026-10].
3. Digital goods sold in the web view use in-app purchase, unless the storefront allows a link out (US) or an entitlement applies [Official, 2026-06].
4. Sign in and registration happen inside the app [Official, 2026-10].
5. Remote web bundle updates never introduce features App Review has not seen (2.5.2) [Official, 2026-06].
6. The privacy manifest and purpose strings cover web APIs used inside the web view: `getUserMedia` (camera, microphone) and `navigator.geolocation` trigger the same system prompts as native code; `submission_check.py` scans web code in Capacitor projects for them.
7. The review notes name the native features and where to see each one (template B in [Review notes and demo accounts](review-notes-and-demo-accounts.md)).

## 3. Google Play: Trusted Web Activities

| Rule | Detail | Evidence |
|------|--------|----------|
| Trust | The app and the site are verified as the same developer through Digital Asset Links | [Official, 2026-10] |
| Statement file | `https://<domain>/.well-known/assetlinks.json`, served over HTTPS with content type `application/json`, without redirects; one file per host | [Official, 2026-10] |
| Content | A statement with relation `delegate_permission/common.handle_all_urls`, target namespace `android_app`, `package_name` and `sha256_cert_fingerprints` | [Official, 2026-10] |
| Which key | With Play App Signing, the local `keytool` fingerprint usually does not match devices; take the fingerprint and the ready made JSON from Play Console > Release > Setup > App signing | [Official, 2026-10] |
| Upload key too | Include the upload key fingerprint as well so locally signed test builds verify | [Official, 2026-10] (research pass on the TWA guide) |
| Failure | When verification fails the site opens as a Custom Tab with browser UI at the top; a common cause is the wrong signature | [Official, 2026-10] |
| Browser choice | The TWA uses the default browser if it supports TWAs, else any installed browser that does, else Custom Tabs | [Official, 2026-10] |
| Content quality | TWA content is expected to meet the web install (Add to Home Screen) criteria | [Official, 2026-10] |
| Minimum functionality | Webview only apps that add nothing are flagged under Play's minimum functionality rules (a 2020 policy post) | [Reported, 2026-10] |
| Digital goods | Digital goods in a Play distributed TWA use Play Billing (the Digital Goods API); Billing Library 8 or later applies to the Android build | [Reported, 2026-10] for TWA billing; [Official, 2026-09] for the library version |
| New personal accounts | The 12 tester, 14 day closed test applies to TWAs like any app | [Reported, 2026-10] |

Checks:
1. `submission_check.py` finds a TWA (twa-manifest.json, Android Browser Helper, or the trusted launcher in the manifest) and fails when no `.well-known/assetlinks.json` in the repo names the package with a valid SHA-256 fingerprint. It warns on a single fingerprint so a human confirms it is the app signing key.
2. Live check by a human or `site-engineer` after deploy: open `https://<domain>/.well-known/assetlinks.json` (status 200, no redirect, JSON), then install the Play internal test build and confirm there is no browser bar.
3. Every host the TWA opens has its own file.

## 4. Games on both stores

| Topic | Apple | Google Play |
|-------|-------|-------------|
| Platform game features | Game Center (leaderboards, achievements, challenges built from leaderboards, activities) and the Games app in iOS 26 [Official, 2026-10] (research pass); Game Center features need the entitlement and configuration before submission [Official, 2026-10] | Play Games Services (profile, achievements, leaderboards, events, cloud save) [Official, 2026-10] (research pass) |
| Age rating inputs | Loot boxes, simulated gambling, UGC, messaging and chat, social media, advertising, unrestricted web access ([Apple review checklist](apple-review-checklist.md) section 3) [Official, 2026-10] | IARC questionnaire in Play Console [Reported, 2026-10] |
| Chat | Random or anonymous chat is under 1.2; filter, report, block, contact [Official, 2026-02] | Since 2026-08-26 anonymous chat apps may not target children [Official, 2026-10] (research pass) |
| Kids | Kids Category: parental gate for links and purchases, no third party analytics or ads except as 1.3 allows [Official, 2026-06] | Families policy for child directed apps: certified ad SDKs only [Official] (research pass) |
| Paid random items | Odds before purchase [Official, 2026-06] | Odds before purchase in close proximity [Reported, 2026-10] |
| Simulated gambling | 13+ infrequent, 18+ frequent; Australia R 18+ [Official, 2026-10] | IARC answers; Google Ads social casino certification for advertising (2025-04-14) [Reported, 2026-10] |
| Real money gambling | Licenses per storefront attached for review; Brazil betting license (news 2026-05-08) [Official, 2026-10] | Country licensing (not in scope for our games) |

Review notes for games add: how to reach a purchase quickly (a seeded demo account, a level select for review), what modes are ranked and what money can buy in each, where the odds screen is if any, and the chat controls.

## 5. HTML5 mini games and mini apps inside an app (4.7)

When the app offers software that is not embedded in the binary (HTML5 or JavaScript mini games, mini apps, streaming games, chatbots, plug-ins), the developer is responsible for all of it and 4.7.1 to 4.7.5 apply [Official, 2026-06]:

| Rule | What to build | Evidence |
|------|---------------|----------|
| 4.7.1 | The offered software follows the privacy guidelines (5.1), includes filtering, reporting with timely responses and blocking, and sells digital goods under 3.1 | [Official, 2026-06] |
| 4.7.2 | No extending or exposing native platform APIs to the software without Apple's prior permission | [Official, 2026-06] |
| 4.7.3 | No sharing data or privacy permissions with any individual piece of software without explicit consent each time | [Official, 2026-06] |
| 4.7.4 | An index of the software and its metadata, with universal links to every item | [Official, 2026-06] |
| 4.7.5 | A way to identify software above the app's age rating, and an age restriction based on verified or declared age | [Official, 2026-06] |

The Mini Apps Partner Program sets a 15% commission on qualifying purchases in mini apps and requires the Declared Age Range API and the Advanced Commerce API [Official, 2025-11] (from the mobile-app-growth module; read the program page before enrolling).

A platform that hosts many of our own games inside one app (one listing, many games) is a 4.7 case only when the games are downloaded rather than bundled. Bundled games are ordinary app content. Name which one applies in the notes.

## 6. Minors and age laws that change the build

| Law or rule | Build consequence | Owner of the verdict | Evidence |
|-------------|-------------------|----------------------|----------|
| Turkey Law 7578 (passed 2026-04-22) | Under 15s barred from social media; game platforms need age ratings and parental controls including purchase approval; local representative above 100,000 daily Turkish users; most duties about 6 months after the implementing regulation | compliance | [Reported, 2026-10] |
| Brazil ECA Digital (Law 15.211/2025) | No paid loot boxes for minors | compliance | [Reported, 2026-10] |
| Texas SB 2420 | Age category data through the Declared Age Range API for new Texas accounts from 2026-06-04 | compliance, App team | [Official, 2026-06] |
| US COPPA amendments | Compliance date 2026-04-22 | compliance | [Reported, 2026-10] |
| FTC v Cognosphere (Genshin Impact), 2025-01 | USD 20 million; no purchases by under 16s without parental consent; real cost and odds disclosure | compliance | [Reported, 2026-10] |

The monetization contract runbook already requires parental approval where the law asks, no personalized ads for under 13s and no countdown or scarcity copy for minors; this agent checks the build and the age rating answers agree with the `compliance` verdict.

## 7. Wrapper first launch checklist

- [ ] Route chosen per store (TWA for Play, Capacitor for iOS) and recorded in the dossier.
- [ ] Native value list: at least the features in section 2 that the core loop uses, reachable by the reviewer.
- [ ] No browser chrome, store badges or web checkout in the wrapped UI.
- [ ] Navigation locked to the app's origin, or the unrestricted web access answer given.
- [ ] Digital goods through in-app purchase (iOS) and Play Billing (Android), with restore.
- [ ] Purpose strings for web APIs used in the web view; privacy manifest with plugin reasons.
- [ ] `assetlinks.json` live with the Play app signing fingerprint (and the upload key); no browser bar in the internal test build.
- [ ] Sign in and account deletion inside the app.
- [ ] Review notes name the native features and the steps to see them.
- [ ] `site-engineer` release QA passed for the web build that ships inside the wrapper.
