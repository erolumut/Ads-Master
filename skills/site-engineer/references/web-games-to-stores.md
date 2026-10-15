# Web Games to Stores

> Knowledge as of 2026-10 (research pass 2026-10-12, Apple and Android pages rechecked 2026-10-12). Apple App Review Guideline text was read at the source (guidelines dated 2026-06-08) and carries [Official, 2026-06]; the Android TWA guide (updated 2026-02-26) and the Play Billing deprecation page (updated 2026-09-09) were read at the source; Play Console Help pages and most wrapper tooling were read only as search results ([Reported, 2026-10]) or not at all ([Unverified]). Store rules change several times a year: run the Freshness protocol before a submission plan rests on any row.

Purpose: take a web game to players in the order that keeps the most control and costs the least: the game's own URL as an installable web app first, Google Play through a Trusted Web Activity second, the App Store through a native wrapper with real native value third. Plus the server side that every leaderboard needs: **score integrity**, because a client score is a claim, not a fact.

Boundary: Ads Master owns how a game earns, is found, keeps players, is measured and passes review; the game's own repo owns how it plays. This module specifies builds, wrappers, release QA and the server checks around scores. It never changes the game's rules; when integrity needs something from the game (a deterministic engine, an input log), it states the requirement for the game repo.

| This module (site-engineer) | Others |
|-----------------------------|--------|
| PWA build, service worker, install flow, TWA and Capacitor wrappers, release QA, score integrity server checks and their tests | Review dossier and submission (`store-submission`), listing text and screenshots (`app-store-optimization`), prices and what is sold (`game-monetization`, Game Monetization Contract v0.2), push logic and copy (`lifecycle-crm`), event taxonomy (`measurement`), policy and consumer law (`compliance`) |

## 1. The ladder

| Step | What it is | Effort | Review risk | Payments for digital goods | Use when |
|------|------------|--------|-------------|----------------------------|----------|
| 1. Own URL as a PWA | The game at its own domain, installable (manifest plus service worker) | Low | None (no store) | Web checkout (Stripe or a merchant of record); VAT duties per buyer country in the EU and Turkey (`compliance` and the human decide before the first sale) | Always first: you own the data, the link, the streaks and the group graph |
| 2. Google Play through a TWA | The PWA in a thin Android app that opens it full screen in Chrome | Low to medium | Medium: a web view with no value is a minimum functionality risk [Reported, 2026-10] | Google Play Billing for digital goods sold in the app | After the web version holds retention; Android players expect a store install |
| 3. App Store through Capacitor (or another native shell) | The game inside a native app with native features | Medium to high | High: guideline 4.2 asks for more than a repackaged website | Apple In-App Purchase for digital unlocks; US storefront links to web purchase allowed | When native features give iOS players something the web cannot (section 4) |

Decision rule: do not start step 3 before step 1 shows retention worth paying a store fee for, and before the game can offer native value that is real, not added to pass review.

## 2. PWA baseline (step 1)

| Item | Requirement | Why |
|------|-------------|-----|
| Manifest | `name`, `short_name`, icons (192 and 512 px plus a maskable icon), `start_url`, `display: standalone`, `theme_color`, `background_color` | Installability and a clean splash |
| Service worker | Offline shell (the game loads without network); content versioned per release | The game opens on a train; the TWA also needs it |
| Update flow | A new version activates at a safe moment (menu, between runs), never in the middle of a run | A forced reload mid run loses an attempt and looks like a bug |
| Install prompt | Android and desktop Chrome: a custom button after a value moment that triggers the saved install prompt; iOS Safari: a short "Add to Home Screen" guide shown after a value moment (Safari has no programmatic install prompt [Practitioner consensus]) | Install is the gate for iOS web push |
| Web push | Section 6 | |
| State | Streaks, attempts, purchases and scores live on the server, not only in browser storage. Safari may clear script written storage for sites the user has not interacted with for a while, with installed Home Screen apps treated differently [Unverified in this pass; check WebKit's storage policy] | A cleared cache must never erase a streak or a purchase |
| Performance | Budgets from [Performance and third party scripts](performance-and-third-party-scripts.md); test on a cheap Android phone per [Mobile web polish](mobile-web-polish.md) | Most players are on mid range phones |
| Ad and analytics SDKs | Load only after consent (EEA, UK) per the contract runbook | Consent first is a release blocker |

## 3. Google Play through a Trusted Web Activity (step 2)

| Item | Detail | Label |
|------|--------|-------|
| Verification | Digital Asset Links: a file on the website at `/.well-known/assetlinks.json` that points to the app, plus metadata in the app that points to the site. "If verification fails, the browser will fall back to displaying your website as a Custom Tab", which means browser UI at the top of the page | [Official, 2026-02] (Android TWA guide) |
| Which key | The guide warns that "a common cause for verification failing is to use the wrong signature" and that Play may create another key depending on how signing is handled. List the SHA-256 fingerprint of the Play App Signing key (Play Console, app integrity) and of the upload or local key used for testing | [Official, 2026-02] for the warning; fingerprint choice per research note 10 (TWA guide read in research) |
| Build | Bubblewrap or an equivalent generator; Android App Bundle required; Play App Signing required for new apps | [Official, 2026-10] (read in research) |
| Target API | From 2026-08-31 new apps and updates target API 36; an extension to 2026-11-01 can be requested | [Official, 2026-10] (read in research) |
| Billing | "By Aug 31, 2026, all new apps and updates to existing apps must use Billing Library version 8 or later", extension until 2026-11-01. Inside a TWA, Play Billing is reached through the web Digital Goods API path documented by Chrome [Unverified in this pass] | [Official, 2026-09] for the Billing Library rule |
| Closed test before production | New personal developer accounts (created after 2023-11-13) need at least 12 testers opted in continuously for the last 14 days before applying for production; organisation accounts are exempt. Failures: the count dipping below 12, vague answers in the production access form, inactive testers | [Reported, 2026-10] |
| Data safety and privacy | Declare every data type the app and its SDKs collect or share; a live privacy policy link; account deletion inside the app and as a web link entered in the form | Data safety [Official, 2026-10]; deletion details [Reported, 2026-10] |
| Vitals | User perceived crash rate under 1.09% overall (8% per phone model) and ANR rate under 0.47% overall (8% per phone model) over 28 days, or reduced visibility and a listing warning | [Official, 2026-10] (read in research) |
| Families | If children may play: Families policy, certified ad SDKs | [Official, 2026-10] |
| Fees | Play's 2026 service fee changes (US, EEA and UK from 2026-06-30, other regions later) are reported with figures that differ between sources | [Contested]; `game-monetization` and `pricing-strategy` read the current Play Console terms |

TWA release QA additions:
- [ ] Opens full screen with no browser bar on a clean device (verification passed); test with the Play signed build from internal testing, not only the local build.
- [ ] `assetlinks.json` served with `Content-Type: application/json`, no redirect, reachable without login, both fingerprints present.
- [ ] Offline launch shows the offline shell, not a browser error page.
- [ ] Back button behaviour inside the game is defined (menu, not exit, in the middle of a run).
- [ ] Purchases go through Play Billing in the Android build; web checkout is not shown inside the Play build for digital goods.
- [ ] Notification permission on Android 13 and later is requested at the value moment ([Game notifications and community](../../lifecycle-crm/references/game-notifications-and-community.md)).

## 4. App Store through Capacitor (step 3)

### 4.1 What the guidelines say (read 2026-10-12)

| Guideline | Text or rule | Label |
|-----------|--------------|-------|
| 4.2 Minimum Functionality | "Your app should include features, content, and UI that elevate it beyond a repackaged website. If your app is not particularly useful, unique, or 'app-like,' it doesn't belong on the App Store." | [Official, 2026-06] |
| 4.2.2 | "Other than catalogs, apps shouldn't primarily be marketing materials, advertisements, web clippings, content aggregators, or a collection of links." | [Official, 2026-06] |
| 4.2.3(ii) | If the app downloads additional resources to function on first launch, disclose the size and prompt before downloading | [Official, 2026-06] |
| 2.5.2 | Apps may not "download, install, or execute code which introduces or changes features or functionality of the app" | [Official, 2026-06] |
| 4.7 | Apps may offer HTML5 and JavaScript mini apps and mini games not embedded in the binary, and are responsible for them. 4.7.1: follow privacy rules, provide filtering, reporting and blocking, and use 3.1 for digital goods. 4.7.2: no native API exposure without Apple's permission. 4.7.3: no data or permission sharing without consent each time. 4.7.4: an index of the software with universal links to each item. 4.7.5: identify software above the app's age rating and restrict access by verified or declared age | [Official, 2026-06] |
| 3.1.1 | In-App Purchase for digital unlocks; odds before purchase for randomized items | [Official, 2026-06] |
| 3.1.1(a) | Entitlements "are not required for developers to include buttons, external links, or other calls to action in their United States storefront apps"; elsewhere links only under specific entitlements | [Official, 2026-06] |
| 3.1.3(b) | Items acquired on other platforms may be used in the app "provided those items are also available as in-app purchases within the app" | [Official, 2026-06] |
| 4.8 | Apps that use a third party or social login for the primary account "must also offer as an equivalent option another login service" with privacy features (Sign in with Apple qualifies) | [Official, 2026-06] |
| 5.1.1(v) | "If your app supports account creation, you must also offer account deletion within the app." | [Official, 2026-06] |

How this applies to one web game in a wrapper: bundle the game's code in the binary and ship feature changes through review (2.5.2). Treat remotely loaded games as 4.7 software only when the app is a catalog of mini games, and then meet 4.7.1 to 4.7.5. Content updates that do not change features (new daily levels as data) are the normal case for daily games; confirm the line with `store-submission` for the specific game.

### 4.2 Native value that answers 4.2

Practitioner reports say push notifications, location or sharing alone are not enough to pass 4.2 [Reported, 2026-10]. Build value a player notices:

| Native feature | What it gives the player | Implementation note | Label |
|----------------|--------------------------|---------------------|-------|
| Game Center | Sign in, leaderboards (friends notified when beaten), challenges built from leaderboards, achievements, activities that deep link into content; games appear in Apple's Games app (iOS 26) | Needs a native plugin or bridge; a maintained Capacitor plugin was not confirmed in research | Features [Official, 2026-10] (Apple games pages read in research); plugin [Unverified] |
| Haptics | Taps, wins and fails felt in the hand | `@capacitor/haptics` | [Reported, 2026-10] |
| Widgets | Today's puzzle, streak or group standing on the Home Screen | WidgetKit through a plugin (for example a Capgo widget kit) or native Swift | [Unverified] |
| Notifications | Native push with per type settings | APNs through the push plugin; logic in `lifecycle-crm` | [Reported, 2026-10] |
| Offline play | The full daily loop without network, synced later | Bundled assets, server reconciliation of attempts | Practitioner consensus |
| Native share | Result sharing to Messages and other apps with a preview | Share sheet plugin; the share text hides answers | Practitioner consensus |
| Sign in with Apple | Required when Google or Facebook login is primary (4.8) | Native plugin; server token handling; revoke on account deletion | [Official, 2026-06] |

### 4.3 Wrapper release checklist (iOS)

- [ ] Privacy manifest (`PrivacyInfo.xcprivacy`) present, with required reason API declarations; Capacitor, Cordova and Firebase SDKs are on Apple's list of SDKs that need manifests and signatures [Official, 2026-10] (read in research).
- [ ] App Privacy answers match the real SDK data map of the build (hand the map to `store-submission`).
- [ ] Built with the iOS 26 SDK or later (required since 2026-04-28; the iOS 27 SDK is expected to be required from April 2027) [Official, 2026-10] (read in research).
- [ ] Account deletion inside the app, removes the account and data, covers guest accounts, revokes Sign in with Apple tokens.
- [ ] In-App Purchase for every digital item; Restore Purchases visible; no web checkout links outside the US storefront unless an entitlement applies.
- [ ] ATT prompt before any IDFA read; CMP before ad SDKs in the EEA and UK.
- [ ] No sign in or registration handed off to a browser.
- [ ] iPad layout usable if the app is universal.
- [ ] Every native feature in section 4.2 that the review notes promise works on a clean device with a demo account.

## 5. Payments by surface

| Surface | Digital goods | Where the server learns of it | Notes |
|---------|---------------|-------------------------------|-------|
| Web or PWA | Stripe Checkout or Payment Element, or a merchant of record | Stripe webhooks (or the merchant of record's) | Stripe is not a merchant of record: VAT per buyer country in the EU and Turkey is a decision for `compliance` and the human before the first sale; EU withdrawal consent at checkout |
| Google Play (TWA or native) | Play Billing (Library 8 or later) | Real-time developer notifications plus server validation | Region programs for alternative billing exist; `game-monetization` decides |
| iOS app | In-App Purchase | App Store Server Notifications plus server validation | US storefront: buttons and links to web purchase allowed without an entitlement; the commission on US link outs is under litigation (Epic v Apple: the Supreme Court agreed on 2026-06-30 to review) and Apple's current practice after 2026-06 is [Unverified]; plan for a fee |
| Every surface | One entitlement log | The server grants, idempotent on (store id, transaction key); refunds revoke; admin compensations are grants in the same log | Game Monetization Contract v0.2, section 5 and runbook |

Never let a client grant value. The client asks whether to show an offer; the server grants after validation.

## 6. Web push limits

| Context | What works | Label |
|---------|-----------|-------|
| iOS and iPadOS Safari | Only for web apps added to the Home Screen, from 16.4, permission requested from a user gesture | [Reported, 2026-10] |
| Android Chrome, desktop browsers | Web push from the site, installed or not | [Practitioner consensus] |
| Inside a TWA | Notifications are shown by the Android app (notification delegation); Android 13 and later needs the runtime notification permission | [Unverified in this pass] |
| Capacitor app | Native push (APNs, FCM), not web push | [Practitioner consensus] |

Implementation rule: one notification service on the server that targets web push subscriptions, FCM tokens and APNs tokens by player and message type, so caps and quiet hours from `lifecycle-crm` apply once across surfaces.

## 7. Score integrity for leaderboards

A leaderboard is only as fair as its weakest submission path. The client is the player's machine: anything it sends (score, time, moves) is a claim. The server is the referee.

### 7.1 Threats

| Threat | Example | Control |
|--------|---------|---------|
| Edited score | Changing a variable in dev tools before submit | Re-simulation (7.4) |
| Forged request | Calling the submit endpoint directly with a made up payload | Run ids issued by the server, session binding (7.2, 7.3) |
| Replayed submission | Sending yesterday's best run again | One use run ids |
| Extra attempts | Reloading before a bad result is submitted to get another try | Count the attempt when the run starts, not when it is submitted |
| Seed shopping | Trying many seeds to find an easy board | The server issues the seed; the client never chooses it |
| Bots and solvers | A script plays perfectly in seconds | Bounds on time and input rate, re-simulation, anomaly review |
| Time manipulation | Pausing or slowing the game clock | Simulated time vs server elapsed time check |
| Multi accounting and collusion | Many guest accounts to fill a group board | Rate limits, device and network signals, anomaly review |
| Version mismatch | A modified client running different rules | Engine version pinned per run; unknown versions rejected |

### 7.2 Run lifecycle (server)

1. `POST /runs/start` with the mode id. The server authenticates the session (guests are real users), checks the attempts left today against the mode's `countedAttemptsPerDay` read from the product's `monetization-policy.json` (a positive integer, or `"unlimited"` for a ladder of matches; never a hard coded number), and in one transaction increments the attempt count and creates the run: `runId` (128 random bits), user id, session id, mode id, the boards the mode declares, `seed` (server random, or the day's seed for a shared daily board), engine version, `issuedAt`, `expiresAt`, status `started`.
2. The response returns `runId`, `seed`, engine version and `expiresAt`. The client plays and records an input log (each input with its simulation tick).
3. `POST /runs/{runId}/submit` with the input log and the client's own score and duration. The server checks: the run exists, belongs to this session's user, is `started`, has not expired, and the engine version is supported.
4. Bounds checks first (cheap), then re-simulation (7.4). The server's score is the score; a client score that disagrees is rejected and flagged.
5. The run becomes `submitted` (single use). The same payload sent again returns the same result (idempotent); a different payload for the same run id is rejected.
6. The result writes only to the boards the mode declares. A group bonus round writes only to group boards and never to an `everyone` board; the global board query excludes those plays (contract section 3).
7. A crash that cost a try is compensated by an admin grant in the entitlement log, never by a silent database edit (contract runbook).

### 7.3 Session binding and rate limits

| Control | Rule (house defaults; tune) |
|---------|-----------------------------|
| Binding | Run id tied to the authenticated session; web requests carry CSRF protection; if runs are stateless, sign them (HMAC over user id, mode id, day, nonce, expiry) and keep a used id list until expiry |
| Expiry | Per mode, a little above the longest legitimate run |
| Rate limits | Run starts per user per minute, submissions per run (one), per device and network address; repeated failed submissions trigger a cooldown |
| Day boundary | Server time in a declared time zone decides the day; a run started before the reset counts for the day it started if submitted before expiry |

### 7.4 Bounds checks are a filter; re-simulation is the proof

Bounds checks (fast, every submission):
- Score at or below the maximum possible for the seed when the game can compute it.
- Moves at or above the minimum needed; no inputs after the end state.
- Simulated duration not longer than the server's elapsed time since `issuedAt` plus a tolerance (a run cannot claim 2 minutes of play in 3 seconds of real time) and not shorter than the fastest plausible human time.
- Input rate within human limits for the game's input type.

Re-simulation (the proof): the server replays the input log from the seed with the same engine version and compares the outcome. This needs a deterministic engine: seeded randomness, a fixed timestep, no wall clock or network inside the simulation. It is the same property that lets trailers render frame by frame from the game ([Playable ads and game trailers](../../video-studio/references/playable-ads-and-game-trailers.md) section 6), so one engineering investment pays twice.

| Game type | Re-simulate |
|-----------|-------------|
| Turn based or puzzle (cheap to replay) | Every ranked submission |
| Real time with physics (costly) | Every submission that would enter the top N of an `everyone` board or beat a percentile threshold, plus a random sample of the rest |

Top scores stay `pending` (visible to the player as "verifying", not on the public board) until re-simulation and anomaly checks pass. Bounds checks alone are not enough for the top of a board: a solver produces scores that are within bounds.

Daily boards with one shared seed: the seed is public once the first player sees the board, so run binding and attempt counting carry the fairness; players sharing answers is a product question for the game repo, not something the server can detect from one run.

### 7.5 Anomaly review

- Flag: completion time far below the board's distribution (for example more than 3 standard deviations), new accounts entering the top 10, many accounts from one device or network in one group, identical input logs across accounts.
- Hold flagged results as pending; a human reviews; the player can appeal; never accuse publicly.
- Log every decision; repeated confirmed abuse blocks submissions for that account.

### 7.6 Tests the product repo carries

| Test | Expected |
|------|----------|
| Submit with an unknown, expired or another user's run id | Rejected |
| Submit the same run twice with the same payload; then with a different payload | Same result; then rejected |
| Start a run, reload, start again after the last attempt | The attempt was counted at start; no extra attempt |
| Client score differs from the re-simulated score | Rejected and flagged |
| Run claims more simulated time than real elapsed time | Rejected |
| A group round result | Appears on group boards only; absent from the global board query |
| Attempts per day | Equal to the policy's `countedAttemptsPerDay`; no purchase, reward, admin grant or round changes it |
| Unknown engine version | Rejected |

Privacy: input logs are gameplay data without personal data; keep them only as long as verification and appeals need (house default 90 days for verified runs) and say so in the privacy policy.

## 8. Handoffs from this module

| Situation | Hand off to | What to pass |
|-----------|-------------|--------------|
| Submission dossier, review notes, rejections and appeals | store-submission | Build ids, native features and how to test them, SDK data map, account deletion path, demo account |
| What is sold where, billing programs, fees | game-monetization | Store build status, billing integration status |
| Listing text, screenshots, previews | app-store-optimization | Native features to show; screen capture rule |
| Push logic, permission timing, caps | lifecycle-crm | Notification service capabilities per surface |
| Score events, run and verification events | measurement | Event names for run start, submit, verified, rejected |
| VAT, merchant of record, consumer rules for web checkout | compliance | Checkout flow, markets, the decision needed |
| The game is not deterministic or has no input log | Human, for the game repo | Section 7.4 requirement as a request, never a rule change |

## Sources for this module

| Source | Date | Supports | Label |
|--------|------|----------|-------|
| Apple App Review Guidelines 2.5.2, 3.1.1, 3.1.1(a), 3.1.3(b), 4.2, 4.2.2, 4.2.3, 4.7, 4.8, 5.1.1(v) (developer.apple.com/app-store/review/guidelines) | 2026-06-08, read 2026-10-12 | Section 4.1, payments | [Official, 2026-06] |
| Android Developers, Trusted Web Activities guide version 2 (developer.android.com) | Updated 2026-02-26, read 2026-10-12 | Digital Asset Links, wrong signature warning, Custom Tab fallback | [Official, 2026-02] |
| Android Developers, Play Billing Library deprecation FAQ | Updated 2026-09-09, read 2026-10-12 | Billing Library 8 by 2026-08-31, extension to 2026-11-01 | [Official, 2026-09] |
| Research note 10 (Play first launch: target API, vitals, AAB, Data safety, closed test) | 2026-10-12 | Section 3 | Opened pages [Official, 2026-10]; support pages [Reported, 2026-10] |
| Research note 09 (Apple first pass review: privacy manifests, SDK list, SDK versions) | 2026-10-12 | Section 4.3 | [Official, 2026-10] |
| Research note 05 (Game Center features, Games app) | 2026-10-12 | Section 4.2 | [Official, 2026-10] |
| Research note 08 (web first distribution: 4.2 reports, haptics, widgets, web push, anti cheat) | 2026-10-12 | Sections 4.2, 6, 7 | [Reported, 2026-10] or [Unverified] as labeled |
| Game Monetization Contract v0.2 (`skills/game-monetization/references/monetization-contract.md`) | 2026-10 | Attempts from the policy, boards and scopes, group rounds, entitlement log, admin grants | Internal contract |
