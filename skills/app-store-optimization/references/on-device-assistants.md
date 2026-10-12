# On-Device Assistants

> Knowledge as of 2026-10. Scope: how an installed app exposes its actions and content to Siri, Shortcuts, Spotlight and Visual Intelligence on Apple platforms, and to Gemini and launcher shortcuts on Android; what that does and does not do for discovery; the developer checklist the ASO agent hands to the app team; and how to measure assistant driven usage. The ASO agent specifies and measures. The app team builds and ships, through `site-engineer` or the client's own developers.

Evidence note: every 2025 to 2026 finding here was gathered on 2026-10-12 from search result summaries; no official page was read in full, so nothing carries [Official]. `[Reported, 2026-10]` means an official page plus an independent source, or two dated independent sources, agree. `[Unverified]` means one source, official ones included. `[Unverified: inference]` marks our own reasoning. Long established frameworks (App Intents, Core Spotlight, Android launcher shortcuts) carry `[Practitioner consensus]` and name their L2 documentation; developers read that documentation before building, because APIs change with every OS release.

## 1. Discovery or usage: the honest answer

| Question | Answer | Evidence |
|----------|--------|----------|
| Do Siri or Gemini recommend apps the user has not installed? | No evidence found. Siri acts inside installed apps; Gemini's app actions run in a curated set of partner apps in a beta | No source found in the 2026-10-12 search; Gemini beta [Reported, 2026-10] |
| What do these integrations do? | Let the assistant run an action in the app, open a specific screen, or return a result, without the user opening and navigating the app | [Practitioner consensus] for App Intents and launcher shortcuts; AppFunctions [Reported, 2026-10] |
| Does it help store ranking? | No evidence either way | None found |
| So why does ASO care? | Retention and ratings. An app the user can drive by voice or from Spotlight gets used more often and stays installed; satisfied repeat users are the ones the rating prompt should reach | [Unverified: inference]; measure it (section 7) |

Planning rule: sell this to the client as a usage and retention project with a measurement plan, never as a discovery or ranking project. Priority depends on the app:

| App profile | Priority | Why (judgement, not evidence) |
|-------------|----------|-------------------------------|
| Frequent, short, repeatable tasks (log, start, check status, reorder, navigate, play) | High | Assistant invocation replaces several taps many times a week |
| Utilities that start from something seen (shopping, plants, translation, recipes, identification) | High for Visual Intelligence | The job begins with the camera or screen |
| Content apps with a library (podcasts, reading, video) | Medium | "Play my show" style actions and Spotlight content search |
| Long sessions, rare use (most games, tax filing, travel booking) | Low | Little to shorten; spend the effort on the store page instead |

## 2. Apple: what is reported

| Capability | What it does | Status | Evidence |
|------------|-------------|--------|----------|
| App Intents (framework) | Declares app actions and content (entities) for Siri, Shortcuts and Spotlight | Long established | [Practitioner consensus]; L2: developer.apple.com/documentation/appintents |
| App Shortcuts | App Intents with predefined spoken phrases, available right after install with no user setup; also listed in Spotlight and the Shortcuts app | Long established | [Practitioner consensus]; same documentation |
| App Schemas | WWDC26 sessions 343 and 240 present them, as part of App Intents, as the way apps take part in Siri's Apple Intelligence features | New with WWDC26 | [Unverified] (session pages read as summaries) |
| Siri with Apple Intelligence | Introduced 2026-06-08; Apple's newsroom said in 2026-09 that it "is here"; English first; not in the EU at launch | Shipping, limited languages and regions | [Reported, 2026-10] (Apple newsroom; MacRumors 2026-06-08) |
| Model provider | Apple Foundation Models use Gemini models (joint Google and Apple statement 2026-01) | Context only | [Reported, 2026-10] (joint statement; MacRumors 2026-06-08) |
| Visual Intelligence | Passes what the camera or screen shows to apps through App Intents | Shipping | [Unverified] (Apple Visual Intelligence documentation read as a summary) |
| Spotlight | Indexes app content and shows App Shortcuts in on-device search | Long established | [Practitioner consensus]; L2: Core Spotlight and App Intents documentation |
| SiriKit deprecation | Older intent framework reported as deprecated | Unclear | [Unverified] |

What the model provider fact does not mean: there is no evidence that Google Search, Play or Gemini app signals feed Siri's choices. Do not plan Apple work around Google signals.

What "not in the EU at launch" means for planning: build once, but do not promise EU or non-English users assistant features until Apple's availability page lists their language and region (L2 check before any client commitment).

## 3. Android: what is reported

| Capability | What it does | Status | Evidence |
|------------|-------------|--------|----------|
| AppFunctions | Android 16 and later platform API plus a Jetpack library; apps expose functions that agents such as Gemini can call; the OS indexes each function's schema | Experimental | [Reported, 2026-10] (developer.android.com/ai/appfunctions and the Android 17 post 2026-06; InfoQ and heise coverage of the Gemini beta) |
| Gemini integration with AppFunctions | Private preview with trusted testers, 2026-05 to 2026-06 | Preview, by invitation | [Unverified] (official pages read as summaries) |
| Gemini acting in apps (beta) | Curated food delivery, grocery and rideshare apps, US and Korea, on Galaxy S26 and Pixel 10 | Beta, curated partners | [Reported, 2026-10] (Google 2026-02; InfoQ; heise) |
| How Gemini picks an app or function | Not documented | Unknown | None found |
| App Actions (shortcuts.xml capabilities) | Still used to open app screens from the assistant | Legacy, value unclear | [Unverified] (vendor source) |
| Launcher shortcuts (static in shortcuts.xml, dynamic via ShortcutManager) | Long press menu actions that deep link into the app | Long established | [Practitioner consensus]; L2: developer.android.com app shortcuts guide |

Planning rule: AppFunctions is experimental and Gemini access is curated. Outside the beta categories, treat it as a prototype behind a flag, not a roadmap commitment. Launcher shortcuts and verified App Links are the dependable Android work today.

## 4. Choosing what to expose: the job map

Start from the top 5 jobs in the App entity fact sheet ([App web presence for AI](app-web-presence-for-ai.md) section 7). The same names must appear in the listing, the website and the assistant phrases: one vocabulary everywhere.

1. For each job, write the request a user would actually say or type. Take the words from reviews (`review_themes.py` samples), support tickets and store search terms, not from the marketing team.
2. Score each job on the columns below.
3. Pick the top 3 for P1 (section 5). Anything that spends money, sends a message or deletes data needs an explicit user confirmation in the flow, whatever its score.

| Job (from fact sheet) | User request | Frequency | Completes without the UI? | Parameters | Result shown | Risk | Priority |
|-----------------------|-------------|-----------|---------------------------|-----------|--------------|------|----------|
| Log a habit | "Log my run in Acme Habits" | Daily | Yes | Habit name | "Run logged. 6 day streak." | Low | P1 |
| See today's progress | "How am I doing today in Acme Habits?" | Daily | Yes (spoken summary) | None | Done and remaining counts | Low | P1 |
| Start the morning routine | "Start my morning routine in Acme Habits" | Daily | No (opens the routine screen) | Routine name | Routine screen | Low | P1 |
| Add a new habit | "Add a habit in Acme Habits" | Monthly | No | Name, schedule | Edit screen | Low | P2 |
| Upgrade to Pro | Not exposed | Rare | No | n/a | n/a | Money | Not exposed |

Second worked example (food delivery, a Gemini beta category): "Reorder my last order from Acme Eats" is P1 on both platforms, with a mandatory confirmation step showing items and total before placing the order; "Track my order" is P1 and read only.

## 5. Developer checklist (the hand off)

The ASO agent writes this as a G1 deliverable: `ads-master/outputs/app-store-optimization/YYYY-MM-DD_app-store-optimization_assistant-checklist.md`, then requests the handoff to `site-engineer` or the client's developers. Building it is the app team's release; shipping is a production change on the client's release process (G3).

| Priority | Item | Platform | Why | Done when |
|----------|------|----------|-----|-----------|
| P1 | App Intents for the top 3 jobs; each intent completes the job or opens the exact screen | iOS | The base layer for Siri, Shortcuts and Spotlight | Each intent runs from the Shortcuts app on a test device and lands on the right result |
| P1 | App Shortcuts with 2 to 3 natural phrases per intent, each containing the app name, localized for the top markets | iOS | Available right after install, no setup | Phrases work by voice on a US English device with Siri; listed in Spotlight after install |
| P1 | Universal Links and App Links verified (AASA and assetlinks.json) | Both | Every assistant, Spotlight result and web link that opens content depends on them | QA matrix passes ([Deep linking](../../mobile-app-growth/references/deep-linking-and-web-to-app.md) section 3) |
| P1 | An analytics event in every intent, function and shortcut handler (section 7) | Both | Without it the project cannot show value | Events visible in the analytics tool from a test device |
| P1 | Confirmation step for anything that spends money, sends a message or deletes data | Both | An accidental order, message or deletion costs trust and refunds | Manual test shows the confirmation every time |
| P2 | App entities for core content ("my morning routine", "my last order") | iOS | Lets requests refer to the user's own items | Siri resolves the entity by name in a test |
| P2 | Spotlight indexing of the content users look for (routines, saved items, documents) | iOS | On-device search reaches content, not only the app icon | Searching an item's name in Spotlight opens it in the app |
| P2 | App Schemas for intents that match a schema domain | iOS 27 | Reported route into Siri's Apple Intelligence features | The team has read WWDC26 sessions 343 and 240 and the current documentation, and listed which intents match |
| P2 | Static launcher shortcuts for the top 2 to 4 jobs (shortcuts.xml); dynamic shortcuts for personal items | Android | Dependable, one long press away | Long press on the icon shows them; each opens the right screen with a source tag |
| P2 | Visual Intelligence integration if the core job starts from something seen | iOS | The camera or screen becomes an entry point | A test image routes to the right result in the app |
| P3 | AppFunctions prototype behind a remote config flag | Android 16+ | Only valuable once Gemini calls the app | Prototype passes the team's tests; flag off in production until Gemini access exists |
| P3 | App Actions capabilities | Android | Value unclear [Unverified] | Keep existing ones working; build new ones only with a reason |
| P3 | SiriKit inventory and migration plan | iOS | Deprecation [Unverified] | Plan written; migration scheduled once deprecation is confirmed at L2 |

Sketch for the app team (Swift; verify every API against the current App Intents documentation and Xcode before use):

```swift
import AppIntents

struct LogWaterIntent: AppIntent {
    static let title: LocalizedStringResource = "Log Water"

    @Parameter(title: "Glasses", default: 1)
    var glasses: Int

    func perform() async throws -> some IntentResult & ProvidesDialog {
        try await WaterLog.shared.add(glasses: glasses)              // the app's own code
        AppAnalytics.track("assistant_action", ["action": "log_water", "result": "success"])
        return .result(dialog: "Added \(glasses) to today.")
    }
}

struct AcmeShortcuts: AppShortcutsProvider {
    static var appShortcuts: [AppShortcut] {
        AppShortcut(
            intent: LogWaterIntent(),
            phrases: ["Log water in \(.applicationName)", "Add a glass in \(.applicationName)"],
            shortTitle: "Log Water",
            systemImageName: "drop.fill"
        )
    }
}
```

Sketch for a static launcher shortcut (Android; `res/xml/shortcuts.xml`, referenced from the launcher activity with `<meta-data android:name="android.app.shortcuts" android:resource="@xml/shortcuts" />`):

```xml
<shortcuts xmlns:android="http://schemas.android.com/apk/res/android">
    <shortcut
        android:shortcutId="log_water"
        android:enabled="true"
        android:icon="@drawable/ic_shortcut_water"
        android:shortcutShortLabel="@string/shortcut_log_water">
        <intent
            android:action="android.intent.action.VIEW"
            android:targetPackage="com.acme.habits"
            android:targetClass="com.acme.habits.MainActivity"
            android:data="https://acme.com/app/log-water?src=launcher_shortcut" />
    </shortcut>
</shortcuts>
```

The `src` query value is what makes launcher shortcut use measurable; the activity reads it and passes it to the analytics event. No AppFunctions code is given here on purpose: the API is experimental and its surface may change before Gemini access widens. The team works from developer.android.com/ai/appfunctions at build time.

Copy review: phrases, short titles and spoken dialog are customer facing words. They go through `compliance` like any listing copy, and they must match the vocabulary of the listing and the website.

## 6. Acceptance tests

Run on real devices before the release is approved, and again after each OS major release.

| Test | Device and setting | Pass |
|------|-------------------|------|
| Each P1 phrase by voice | iPhone with Siri, US English | The action completes or the right screen opens |
| App Shortcuts appear without setup | Fresh install | Visible in the Shortcuts app and in Spotlight for the app name |
| Spotlight item search | iPhone with indexed content | The item opens in the app |
| Each P1 phrase in every localized language | Devices set to each language Apple supports for the feature | Same as above, or documented as not yet available |
| EU device | iPhone with an EU region | Behavior documented; no promise made in copy |
| Launcher shortcuts | Android phone, long press on the icon | Each shortcut opens the right screen; `src` arrives in analytics |
| Confirmation flows | Both | Money, messages and deletion always ask first |
| Analytics events | Both | One event per invocation, no personal data in properties |

## 7. Measuring assistant driven usage

Neither App Store Connect nor Play Console reports assistant usage. It lives in product analytics, so the event spec is part of the hand off.

Event spec:

| Event | Properties | Notes |
|-------|-----------|-------|
| `assistant_action` | `action` (intent or function id), `surface` (`launcher_shortcut`, `appfunction`, `app_intent`, `unknown`), `result` (`success`, `cancelled`, `error`), `platform`, `app_version` | Never log what the user said, item names or other personal data |
| `assistant_entry_open` | `action`, `surface` | When the action opened a screen instead of completing |

The system may not tell the app which surface (Siri, Shortcuts, Spotlight, Visual Intelligence) invoked an App Intent. Log `app_intent` and do not guess the surface [Unverified: inference; the developer checks the current documentation]. Launcher shortcuts carry their own `src` value, and AppFunctions calls are logged inside the function.

KPIs (weekly, from the analytics tool):

| KPI | Definition | Read |
|-----|-----------|------|
| Assistant action users | Weekly active users with at least one `assistant_action` | Adoption |
| Assistant share of completed jobs | Jobs completed via `assistant_action` / all completions of the same jobs | Depth |
| Retention gap | D30 retention of users with an assistant action in week 1 minus users without | Correlational only: heavy users self-select into assistant use |
| Error rate | `result = error` / all `assistant_action` | Quality; above the app's normal error rate is a bug |

Causal reads:
1. Android dynamic shortcuts and AppFunctions can sit behind remote config. Hold out a random 10% of users, compare D30 retention and job frequency after 4 to 8 weeks, and log the test in `ads-master/EXPERIMENTS.md`.
2. iOS App Shortcuts are declared in the app binary and are hard to hold out per user. Use a pre and post comparison against users still on the previous version, call it a quasi-experiment, and never present the retention gap as lift.
3. Report both kinds of number with their limits, in the monthly ASO report, under "Assistant usage".

## 8. Gates and ownership

| Step | Owner | Gate |
|------|-------|------|
| Job map, phrases, checklist, event spec | ASO agent | G1 |
| Phrase and dialog copy | `compliance` | Review before release |
| Implementation and tests | App team via `site-engineer` or the client's developers | Their branch, then the client's release process |
| App release with the integration | Human on the client side | G3 |
| Event and KPI setup in analytics | `measurement` with the app team | G3 for production tracking changes |
| ChatGPT, Claude, Gemini or Copilot app and connector directories | `ai-search-optimization` | G3 for every submission. Not part of this module: those are web assistants, not on-device integrations |

## 9. Myths

| Myth | Reality |
|------|---------|
| "Siri will recommend our app to people who do not have it" | No evidence found |
| "Adding App Intents lifts App Store ranking" | No evidence either way |
| "Gemini will start using our app once we ship AppFunctions" | Gemini acts in a curated set of apps in a beta; selection is undocumented |
| "Apple uses Gemini models, so Google signals decide Siri" | No evidence; the model provider says nothing about what Siri reads |
| "Siri AI works for all our users" | English first and not in the EU at launch [Reported, 2026-10] |
| "More phrases mean more usage" | Two or three natural phrases per action beat long lists; test them by voice |
| "One retention chart proves the feature works" | Assistant users self-select; use a holdout where you can |

## 10. Handoffs

| Situation | Hand off to | What to pass |
|-----------|-------------|--------------|
| Build the checklist | `site-engineer` or the client's developers | Checklist file, job map, phrases, event spec, acceptance tests |
| AASA or assetlinks failing | `site-engineer` | Failing URLs, QA matrix results |
| Event and dashboard setup | `measurement` | Event spec, KPIs, holdout design |
| Phrase and dialog copy | `compliance` | Copy file, languages, fact rows |
| Assistant users as a lifecycle segment (tips, onboarding nudges) | `lifecycle-crm` | Segment definition, consent status |
| Web assistant directories (ChatGPT, Claude, Gemini, Copilot) | `ai-search-optimization` | App entity sheet, top jobs, privacy and support URLs |
