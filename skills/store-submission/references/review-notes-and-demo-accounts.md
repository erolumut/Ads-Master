# Review Notes and Demo Accounts

> Knowledge as of 2026-10. Apple's requirements for a complete review were read at the source on 2026-10-12 (App Review page and "Provide information for a complete review" help page, [Official, 2026-10]; Guideline 2.1, [Official, 2026-06]). The Google Play App access form could not be read from this environment [Unverified]. Templates are Ads Master's own; fill every `<...>` from the build and the dossier, never from memory.

## 1. What App Review asks for

| Item | Detail | Evidence |
|------|--------|----------|
| General information | New apps: concept and business model. Updates: what changed and where to find significant new content | [Official, 2026-10] |
| Purpose and audience | Who the app is for | [Official, 2026-10] |
| Devices and OS versions tested | The models and OS versions tested before submitting | [Official, 2026-10] |
| External services | Data providers, authentication services, payment processors, AI services the core function uses | [Official, 2026-10] |
| Required hardware | A video of the app on a physical Apple device pairing and working with the hardware (not a screen recording) | [Official, 2026-10] |
| Regional differences | Features or content that differ by region, or a statement that it works the same everywhere | [Official, 2026-10] |
| Demo account | Full access; credentials that work at submission; expiry or changes before review can get the submission rejected | [Official, 2026-10] |
| Several account types | Extra credentials for each type in the notes | [Official, 2026-10] |
| Auto-renewable subscriptions | A demo account with an expired subscription so the whole purchase flow can be reviewed | [Official, 2026-10] |
| One time codes | Include the code or a way past it in the notes; otherwise a call may be needed, typically within 3 to 5 business days | [Official, 2026-10] |
| Demo mode | Allowed instead of an account for sensitive or highly regulated apps; must show the full features with demo data; Guideline 2.1(a) says prior approval by Apple | [Official, 2026-10] and [Official, 2026-06] |
| Documentation | Licenses, clearances and rights documents in the Attachment section, described in the notes | [Official, 2026-10] |
| Back end | Turned on during review | [Official, 2026-06] |
| Notes length | Up to 4,000 bytes | [Official, 2026-10] (research pass) |

## 2. Demo account checklist

| # | Check | Why |
|---|-------|-----|
| 1 | Created for review only (no real person's data), on production, with the role a normal user has | The reviewer must see what users see |
| 2 | Signs in on a clean install on the submission day | Credentials that changed get the build rejected [Official, 2026-10] |
| 3 | Never expires: no password rotation, no trial expiry, no inactivity lock while in review | Same |
| 4 | Not behind a one time code; or the notes give the way past it | Avoids a call that takes days [Official, 2026-10] |
| 5 | Has content: seeded progress, friends or group members, a populated feed, a game level where the paywall or shop is reachable in under 2 minutes | The reviewer tests purchases and features fast [Practitioner consensus] |
| 6 | Second account with an expired subscription when the app sells auto-renewable subscriptions | Apple asks for it [Official, 2026-10] |
| 7 | Multiplayer or social apps: a second account (or a bot or a seeded opponent) so the reviewer can see an interaction | Shows the core loop [Practitioner consensus] |
| 8 | Account deletion reachable; if deleting would break the review account, say so and give a disposable account | App Review may test deletion [Practitioner consensus] |
| 9 | Region: the account works from the reviewer's region, or the notes explain region locks | Regional differences must be described [Official, 2026-10] |
| 10 | The password lives in the password manager; the dossier names the entry; the human pastes it into App Store Connect and Play Console | Secrets never enter `ads-master/` |
| 11 | Server feature flags for the account match production | A flag only the reviewer sees is a review risk and a 2.3 accuracy risk [Practitioner consensus] |
| 12 | After approval, the account stays alive: updates are reviewed with it | Next review uses the same credentials |

## 3. Writing rules for notes

1. Plain sentences and numbered steps. No marketing copy, no adjectives about quality.
2. Lead with what the app is and who it is for, in two sentences.
3. Say exactly how to reach each feature the reviewer must judge: purchases and Restore, account deletion, native features (wrappers), chat controls, odds screens, AI features.
4. Name external services (payments, sign in, AI) as Apple asks.
5. Say what is different by region or by account type.
6. Explain anything a reviewer could read as a guideline problem before they find it (for example "the Google sign in button sits next to Sign in with Apple on the first screen", "web purchases are honoured only for items also sold as in-app purchases").
7. Stay under 4,000 bytes; count bytes, not characters, when the notes use non Latin scripts.
8. No instructions that try to steer the review ("please approve quickly", "other apps do this"). Facts only.
9. Keep each submission's notes in the dossier and archive them; a rejection reply quotes them.

## 4. Templates

Each template is a starting point; delete lines that do not apply.

### A. New native app

```text
<App name> is <what it does> for <audience>. It is <free, free with optional in-app purchases, subscription>.

Sign in: use the demo account in the App Review Information fields. It never expires and the back end is live.
How to test:
1. Sign in with the demo account.
2. <Core step: open X and do Y.>
3. <Second core step.>
Purchases: <where the paywall or shop is; product names>. Restore purchases is on <screen>.
Account deletion: <Settings > Account > Delete account>. It deletes the account and its data <immediately or within N days>.
External services: <payments provider, sign in providers, analytics, AI service and what it does>.
Tested on: <iPhone model, iOS version; iPad model, iPadOS version>.
Regional differences: <none, or what differs>.
```

### B. Wrapped web app (Capacitor)

```text
<App name> is <what it does> for <audience>. It is built on web technology inside a native app and uses these native features in its core loop:
- <Game Center: sign in, daily leaderboard and achievements (Profile > Game Center)>
- <Offline play: puzzles download in advance; turn on airplane mode and open today's puzzle>
- <Push: a notification when the daily puzzle is ready, opted in from Settings > Notifications>
- <Haptics on every move; native share sheet for the result card>
Sign in and registration happen inside the app. Purchases use in-app purchase; Restore is on <screen>.
Sign in: demo account in the App Review Information fields; it never expires.
How to test: 1. <step> 2. <step> 3. <step>
Account deletion: <path>.
```

### C. Game with in-app purchases and ads

```text
<Game name> is a <genre> game for <audience age>. One <session length> session: <one sentence on the core loop>.
Modes: <ranked daily mode where every player gets the same number of counted tries; purchases never change ranked results>. <Practice mode is uncounted.>
Purchases (all in-app purchase): <product, type, price shown before purchase>. Restore is on <screen> for <non consumables and subscriptions>.
<Paid random items: none.> or <Odds for every pack are shown on the pack screen before purchase (Shop > Packs > Odds).>
Ads: <rewarded ads only, opt in, after consent; interstitials never during play>.
Chat: <none> or <group chat with filter, report, block and contact in Settings > Help>.
To reach the shop fast: the demo account starts at <level or state>; open <Shop>.
Account deletion: <path>.
```

### D. Subscription app

```text
<App name> helps <audience> <job>. Free features: <list>. The <Plus> subscription adds <list>.
Paywall: <where it appears>. It shows the product name, duration, what is included, the full renewal price as the largest price, the trial length and the price after it, Restore, and links to Terms and Privacy.
Demo accounts in the notes: <account 1: active features>; <account 2: expired subscription to review the purchase flow>.
Cancellation: managed in Apple ID subscriptions; the app links there from <screen>.
Account deletion: <path>; the app warns that billing continues through Apple until the subscription is cancelled.
```

### E. Update

```text
What changed in <version>:
- <User visible change 1 and where to see it.>
- <User visible change 2.>
New in-app purchases: <none, or product and where it appears>.
New data collection or SDKs: <none, or what and why; App Privacy answers updated on <date>>.
Demo account unchanged; it never expires.
```

### F. Resubmission after a rejection

```text
This build answers the review of <date> under Guideline <number>.
What we changed: <exact change, screen and path>.
How to verify: 1. <step> 2. <step>.
<If information was missing:> The demo account and steps are in this submission's App Review Information; <the expired subscription account is the second account in the notes>.
```

### G. Apps with user generated content, chat or AI

```text
User content: <what users can post>. Controls: a filter for objectionable content, Report on every item (we answer within <time>), Block on every profile, and contact details in <Settings > Help>.
AI features: <what the AI does>, provided by <service>. Before any personal data is sent, the app asks for permission on <screen> and says what is shared.
Age: <how age is asked or checked; Declared Age Range API use>; social features are <off for users under 13>.
```

## 5. Google Play: App access and review instructions

| Item | Detail | Evidence |
|------|--------|----------|
| App access form | State whether all functionality is available without special access; otherwise give instructions and credentials | [Unverified] (form from long standing console use; confirm wording) |
| Same account | Use the same review account as Apple when the back end is shared; note platform differences | [Practitioner consensus] |
| Closed test answers | The production access questions after the closed test ask about testers and changes; answer with what testers did and what changed | [Reported, 2026-10] |

## 6. TestFlight Beta App Review

The first build to an external group goes through Beta App Review and needs a beta description, test instructions and a feedback email [Official, 2026-10] (research pass). Reuse template A or B as the test instructions; it rehearses the App Store notes.

## 7. Attachments and documentation by app type

Apple lists documentation by type [Official, 2026-10]: regulatory clearance (FDA, CE, CFDA or a test report) for medical apps that diagnose or treat; an exchange license per region for crypto exchanges; partnership documents with the licensed institution for financial and lending apps; the gambling or lottery license per storefront; trademark or rights documents for another party's intellectual property; IRB approval for health research. Games that license characters, music or brands attach the rights documents and name them in the notes.

## 8. What never goes into notes or the dossier

- Passwords, one time codes that stay valid, API keys, tokens, `.p8` contents, service account files.
- Personal data of real users.
- Claims not in `ads-master/brand/PRODUCT_FACTS.md` or approved in `CLAIMS.md`.
- Text addressed to the reviewer that argues, flatters or pressures.
- Statements about features the build does not have.
