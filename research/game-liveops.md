# Research Dossier: Game Liveops (why players come back)

> Research pass for the Ads Master `game-liveops` package: research notes dated 2026-10-12 (teardowns of Royal Match, Color Block Jam, Block Blast and Monopoly Go; web daily puzzles; game analytics; store presence; regulation; monetization touchpoints) plus a verification pass the same day that read Apple and Android developer pages in full; package written 2026-10-15. Scope: daily loops and shared dailies, streaks, events and seasons, teams, groups and leagues, content cadence and difficulty signals, the liveops calendar and store events, remote config and experiments, retention diagnostics, player trust. Evidence labels follow docs/AUTHORING_SPEC.md section 7 plus [Reported, 2026-10] (see Method). Numbers in brackets refer to the Sources list at the end, which uses the same numbering as `skills/game-liveops/references/sources.md`.

## Research method and limits

1. Two inputs: the 2026-10-12 game studio research notes (search result level for almost everything outside Apple and Android developer pages), and a verification pass that read in full Apple's In-App Events page, the In-App Events overview in App Store Connect Help, the App Review Guidelines (last updated 2026-06-08), the Games app developer page, the Game Center page, two GameKit articles (challenges, activities), Apple's web push documentation, and three Android developer pages (notification permission, Play Games Services leaderboards and events).
2. Labeling rule: [Official, YYYY-MM] only for facts read at the official page in this pass; [Reported, 2026-10] for facts seen in search summaries, including summaries of official help pages that could not be opened (Play Console Help, Firebase, vzbv, WebKit were blocked from this environment); [Unverified] for single or vendor sources; [Contested] where sources disagree, with both sides shown.
3. Teardown facts describe what one hit did and come from trade press and analyst summaries; they are not forecasts or targets.
4. The fairness rules come from the Game Monetization Contract v0.2 [45], which this package follows (snake_case offer points, typed grants, boards with scope `group` or `everyone`, `streak_protection`).
5. Not covered here: prices and economy (`game-monetization`), KPI computation (`measurement`), sends (`lifecycle-crm`), store copy and nominations (`app-store-optimization`), submission review (`store-submission`).

## Executive summary

1. Apple In-App Events allow up to 15 approved and 10 published events at a time, each up to 31 days, promoted up to 14 days before the start; names 30, short descriptions 50 and long descriptions 120 characters; specific prices in metadata lead to rejection [Official, 2026-10] [1]. Older guides quote 10 approved and 5 published; the `app-store-optimization` module was updated to 15 and 10 on 2026-10-15.
2. Apple names good event candidates (challenges, competitions, special content launches) and poor ones: repetitive daily tasks or rewards, price promotions without new content, general awareness promotions [Official, 2026-10] [1]. A daily puzzle is not an in-app event; a season, a themed week with new content or a new mini game is.
3. Game Center now gives daily games a native social layer: challenges built on leaderboards with up to 16 players, Apple's own example being a daily mini crossword on a recurring leaderboard that restarts daily; activities deep link into the daily puzzle and support party codes with a web fallback; friends are notified when someone passes their score, even with the game uninstalled; the Games app is pre-installed on iOS 26, iPadOS 26 and macOS 26 [Official, 2026-10] [4, 5, 6, 7].
4. Push rules shape liveops reminders: Apple requires explicit opt in for promotional push with an in-app opt out (4.5.4), forbids spam through Game Center, push and Live Activities (4.5.3), and forbids compensation for enabling push (5.1.2(i)) [Official, 2026-06] [3]; Android 13+ needs the `POST_NOTIFICATIONS` runtime permission [Official, 2026-10] [9]; web push on Apple works for Home Screen web apps on iOS 16.4+ from a user gesture, and an invisible push revokes the permission [Official, 2026-10] [8].
5. Purchased in-game currency may not expire on the App Store (3.1.1) [Official, 2026-06] [3]; event currencies that expire at the end of an event must be earned, not bought.
6. Hits nest events on different clocks: a 1 hour burst, 2 to 3 day cohort events (about 50 players), weekly team chests and a monthly pass [Reported, 2026-10] [25]. Under contract v0.2, a race that ranks levels beaten while boosters are sold for those levels (how such cohort races are commonly described; the scoring is [Unverified]) is a purchasable ranked result; liveops uses milestone forms, collective goals or dedicated event levels instead.
7. Royal Match's store release notes repeat "new levels every two weeks", about 100 levels per update [Reported, 2026-10] [24]: a fixed, announced cadence is the reported hit rhythm for level games.
8. Streak punishment is a regulatory and retention risk: vzbv found manipulative design in five games and platforms in 2025, naming countdowns, daily play incentives and rewards for ads, and objected to purchase offers popping up after app start (Monopoly Go) [Reported, 2026-10] [27, 28]; Deceptive Design lists paid streak repair as a deceptive pattern [Reported, 2026-10] [23]. Duolingo's streak freeze shows that rest days work at scale [Reported, 2026-10] [22].
9. Day boundaries differ across the market: Wordle releases at local midnight and a puzzle finished after local midnight breaks the streak [Reported, 2026-10] [16]; LinkedIn games reset at midnight Pacific [Reported, 2026-10] [18]; Play Games daily leaderboards reset at UTC-7 all year [Official, 2026-10] [10]. Products with an `everyone` board need one server day id.
10. Google Play promotional content (offers, time limited events, major updates) is submitted 4 to 60 days ahead, with approval up to 4 days and 14 days for Partner Program for Games participants; durations for major updates are [Contested] [12, 13, 14]. All Play rules here are search summaries; verify in the console.
11. Benchmarks are wide and vendor based: GameAnalytics medians of about 22% D1, 3.4% to 3.9% D7 and 0.7% D30 (top 10%: 40/12/4) [Reported, 2026-10] [33]; Adjust reports 27% D1 across genres in 2025 [Reported, 2026-10] [34]. Often quoted soft launch gates (D1 above 40%) are top decile numbers [37], and daily social games follow a different curve.
12. Most tests fail: Block Blast reportedly runs more than 50 A/B tests a week with about 97% failing [Unverified] [30]; Firebase recommends at least two weeks per Remote Config experiment and stops experiments after 90 days [Reported, 2026-10] [15]. Uplift needs holdouts; participation is not uplift.

## State of the field in 2026 (with numbers)

| Indicator | Value | Source |
|-----------|-------|--------|
| Apple in-app events at a time | 15 approved, 10 published | [1] [Official, 2026-10] |
| Apple event duration and promotion | Up to 31 days; promoted up to 14 days before the start | [1] [Official, 2026-10] |
| Apple event metadata | Name 30, short 50, long 120 characters | [1] [Official, 2026-10] |
| Game Center challenge size | Up to 16 players | [7] [Official, 2026-10] |
| Play Games leaderboard resets | Daily at UTC-7; weekly between Saturday and Sunday | [10] [Official, 2026-10] |
| Play promotional content timing | Earliest 60 days ahead; approval up to 4 days; Partner Program 14 days | [12] [Reported, 2026-10] |
| Royal Match cadence | About 100 levels every two weeks; 12,400+ levels by 2025-11 | [24, 25] [Reported, 2026-10] |
| Royal Match events | Lightning Rush 1 hour; King's Cup about 2 days, about 50 players, from level 25; Sky Race 3 days | [25] [Reported, 2026-10] |
| Royal Pass | From level 37, about 30 steps a month; +31% revenue in the first 30 days after the June 2021 launch | [25, 26] [Unverified] |
| NYT subscribers (all products, not games only) | 13.35 million in Q2 2026 | [17] [Reported, 2026-10] |
| Puzzmo Plus | About $40 a year (archives, leaderboards, no ads) | [19] [Reported, 2026-10] |
| Mobile game retention medians | D1 about 22%, D7 3.4% to 3.9%, D30 about 0.7% | [33] [Reported, 2026-10] |
| Block Blast testing | 50+ A/B tests a week, about 97% fail | [30] [Unverified] |

## Timeline of changes relevant to liveops

| Date | Change | Impact | Evidence |
|------|--------|--------|----------|
| 2022-02 | Wordle moves to the NYT; some players lose streaks in the migration | Streak data is part of what players own | [16] [Reported, 2026-10] |
| 2022 | FTC v Epic: USD 245m dark pattern refunds, USD 275m COPPA penalty | Pressure patterns carry enforcement risk | [42] [Reported, 2026-10] |
| 2023 (iOS 16.4) | Web push for Home Screen web apps | Reminders for PWA daily games on iPhone | [8] [Official, 2026-10] |
| 2025-01 | FTC v Cognosphere (Genshin): USD 20m, parental consent under 16 | Minors and purchases | [42] [Reported, 2026-10] |
| 2025-03 | Play promotional content: lapsed and churned targeting reported | Reactivation through store cards | [13] [Reported, 2026-10] |
| 2025-03-21 | EU CPC key principles on in-game virtual currencies | Real money prices, children | [39] [Reported, 2026-10] |
| 2025 (spring to June) | vzbv review of online games incl. Monopoly Go; Scopely cease and desist declaration reported | Countdowns, daily play incentives, pop up offers under scrutiny | [27, 28] [Reported, 2026-10] |
| 2025-07 | DSA Article 28 guidelines on minors | Manipulative design and minors | [40] [Reported, 2026-10] |
| 2025 (WWDC25) to 2025-09 | Games app announced, pre-installed on iOS 26 and macOS 26; challenges and activities | Native social layer for store builds | [4, 6, 7] [Official, 2026-10] |
| 2025-10 | Play Points open to all games | Store reward lever | [13] [Reported, 2026-10] |
| 2026-02 | New York attorney general suit over Monopoly Go paid loot boxes reported | Paid random event rewards | [29] [Reported, 2026-10] |
| 2026-04 | Turkey Law 7578: parental controls including purchase approval | Minors in Turkish markets | [43] [Reported, 2026-10] |
| 2026-06-08 | App Review Guidelines update | 3.1.1, 4.5.3, 4.5.4, 5.1.2(i) current text | [3] [Official, 2026-06] |
| 2026 Q4 (expected) | Digital Fairness Act proposal | Dark patterns, addictive design, currencies | [41] [Reported, 2026-10] |

## Best practice consensus

1. A daily loop that fits one short session with a clear tick and a calm closure; the share artifact spoiler free and plain text first [16, 18] [Practitioner consensus].
2. Streaks with free rest days, permanent best streaks and a welcome back screen; no paid repair by default [22, 23, 27] [Practitioner consensus].
3. Nested event time scales, one event per scale, every event with a free path [25] [Reported, 2026-10].
4. Small, activity matched cohorts for competitions; collective goals (team chests) for social retention [25] [Reported, 2026-10].
5. Fixed, announced content cadence and a content runway ahead of the fastest players [24] [Reported, 2026-10].
6. Flag churn and quit spikes against neighbors on mature cohorts; near miss fails are designed [25, 36] [Practitioner consensus].
7. Remote config with kill switches; tests sized in advance, run in full weeks, read after novelty; holdouts for event uplift [15] [Reported, 2026-10].
8. Store events only for real limited moments; no prices in metadata [1] [Official, 2026-10].
9. Reminders opted in, at the player's habit time, capped and stepped down; no rewards for opt in [3, 9] [Official].

## Contested topics (both sides)

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Apple in-app event limits | 15 approved, 10 published on Apple's page read 2026-10-12 [1] | 10 approved, 5 published in older guides and earlier notes | Use 15 and 10 (the ASO module now matches); re-read after each WWDC |
| Play major update duration | 28 days (one help page summary) [12] | Different durations in a 2024 third party blog [14] | Read the console before planning |
| Paid streak protection | Duolingo sells freezes with gems and the mechanic works at scale [22] | Deceptive Design lists paid repair as a dark pattern [23]; regulators scrutinize daily play incentives [27] | Free and equal by default; selling is a G3 product decision, never for minors, never with a competitive streak |
| Competitive events in progression games | Royal Match style cohort races, commonly described as fed by levels where boosters are sold [25] (scoring [Unverified]) | Contract v0.2: a board that ranks people may not be fed by purchasable play [45] | Milestone forms, team chests or dedicated no booster event levels |
| Day boundary | Local midnight (Wordle) [16] | One global tick (LinkedIn games, Play Games boards at UTC-7) [10, 18] | One server day id when any board has scope `everyone`; local display |
| LinkedIn company and school boards | Some guides describe them | Others say no official board | [Unverified]; not used as evidence |

## What top operators do differently

| Average | Top 1% |
|---------|--------|
| Stacks events whenever content is ready | Nests one event per time scale and rotates formats |
| Calls an event a success by participation | Reads uplift against a holdout in the first runs |
| Uses streak loss as the hook | Measures recovery after breaks and keeps rest days free |
| Ships content when it is done | Announces a cadence and keeps a runway of two cycles |
| Tunes difficulty from a dashboard | Flags churn spikes with evidence to the game team, which owns difficulty |
| Runs tests by player for group features | Randomizes by group or team and plans the design effect |
| Submits the daily puzzle as a store event | Saves store events for seasons, premieres and real challenges |
| Sends a daily blast at one time | Sends at each player's habit time, opted in, capped and stepped down |
| Keeps events, offers, pushes and store cards in separate tools | Keeps one calendar that every team reads |

## Common expensive mistakes

1. Streak loss messages and paid repair (trust, regulators, minors).
2. Ranked results influenced by purchases (fairness, contract, reviews).
3. Prices in in-app event metadata (rejection) or events longer than 31 days.
4. Two events on the same clock fighting for the same session.
5. Reading D7 before the cohort is mature; comparing classic and rolling retention.
6. Treating a frontier wall as a difficulty problem.
7. Rewarding notification opt in (Apple 5.1.2(i)).
8. Purchased event currency that expires at the event end (Apple 3.1.1).
9. Applying casual puzzle soft launch gates to a daily social game.
10. Holdouts that cost players rewards without compensation.

## Benchmarks (source, date, sample, caveat)

| Metric | Value | Source and date | Sample | Caveat |
|--------|-------|-----------------|--------|--------|
| D1, D7, D30 medians | About 22%, 3.4% to 3.9%, about 0.7%; top 10% 40/12/4 | GameAnalytics 2025 via a summary [33] | Games using the SDK, data to end 2024 | Vendor; genre mix unknown |
| D1 all genres | 27% (2025) | Adjust 2026 [34] | Adjust clients | Vendor; method differs |
| Soft launch gates | D1 above 40% casual, D7 above 20% casual | Guides [37] | Opinion | Top decile, not medians |
| Session median | 5 to 6 minutes, about 4 a day | Research notes | Unknown | [Unverified] |

Compare a product against its own history first; benchmarks vary by genre, market, platform, traffic source and season.

## Tools and APIs

| Category | Options | Notes |
|----------|---------|-------|
| Store events | App Store Connect In-App Events; Play Console promotional content | G2 drafts, G3 submissions |
| Platform social | Game Center (leaderboards, recurring leaderboards, challenges, activities); Play Games Services (daily and weekly boards) | Store builds only |
| Remote config and tests | Firebase Remote Config and A/B Testing; Unity Gaming Services; GameAnalytics A/B; PostHog, GrowthBook or Statsig for web; own feature flags | Options, not endorsements |
| Analytics | `measurement`'s `game_kpis.py`, GameAnalytics, Firebase with BigQuery, devtodev, PostHog for web | Definitions in METRICS.md |
| Package scripts | `liveops_calendar_check.py`, `level_flags.py` | Standard library; tests beside them |

## Official sources to monitor

| Source | URL | Cadence |
|--------|-----|---------|
| In-App Events | https://developer.apple.com/app-store/in-app-events/ | Quarterly and before each big event |
| App Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ | On each Apple notice |
| Games app and GameKit | https://developer.apple.com/games-app/ | After WWDC |
| Apple Developer News | https://developer.apple.com/news/ | Weekly |
| Play Console Help (promotional content) | https://support.google.com/googleplay/android-developer | Each quarter's plan |
| Play Games Services | https://developer.android.com/games/pgs | Quarterly |
| Firebase A/B Testing | https://firebase.google.com/docs/ab-testing | When tooling changes |

## Verification queue

Each item names the cheapest check that settles it (L1 = live console read, L2 = official page read in full, L3 = two independent dated sources, L4 = controlled test).

1. Play promotional content: eligibility, types, lead times (60, 4, 14 days), durations, audiences (L1 in Play Console, L2 help pages).
2. Firebase A/B Testing: two week minimum, 90 day limit (L2).
3. vzbv objections to Monopoly Go: full list, including whether absence penalties and opaque currencies are named (L2 on the vzbv paper).
4. Royal Match event facts beyond the cadence; Royal Pass unlock level, steps and revenue lift (L3).
5. LinkedIn games boards (L2 on LinkedIn Help).
6. Apple in-app event approval timing in App Store Connect (L1 on the next submission).
7. Whether the Games app shows Play promotional content equivalents (not applicable) and whether Apple Games app offer badges apply to the product's storefronts (L1, with `app-store-optimization`).
8. Benchmarks: GameAnalytics and Adjust reports read at the source (L2).
9. Turkey Law 7578 secondary regulation dates for game platforms (L2, with `compliance`).

## Claims considered and not relied on

| Claim | Why not used |
|-------|-------------|
| Royal Match "team 30 to 80" | In the notes it most likely refers to the studio's headcount, not team (clan) size; ambiguous |
| Promotional content doubles explore acquisitions | Google marketing claim, single source |
| Block Blast 70M DAU | Vendor claim |
| Color Block Jam revenue figures | Conflicting sources; not a liveops lever |
| Apple News+ puzzles with Game Center streaks | Single mention in the notes |
| Specific session length benchmarks | Single summary |

## Sources

1. In-App Events. Apple Developer. https://developer.apple.com/app-store/in-app-events/. Seen 2026-10-12.
2. Overview of In-App Events. App Store Connect Help. https://developer.apple.com/help/app-store-connect/offer-in-app-events/overview-of-in-app-events/. Seen 2026-10-12.
3. App Review Guidelines. Apple Developer. https://developer.apple.com/app-store/review/guidelines/. Last updated 2026-06-08, read 2026-10-12.
4. Apple Games app (developer page). Apple Developer. https://developer.apple.com/games-app/. Seen 2026-10-12.
5. Game Center. Apple Developer. https://developer.apple.com/game-center/. Seen 2026-10-12.
6. Creating engaging challenges from leaderboards. Apple Developer Documentation. https://developer.apple.com/documentation/gamekit/creating-engaging-challenges-from-leaderboards. Seen 2026-10-12.
7. Creating activities for your game. Apple Developer Documentation. https://developer.apple.com/documentation/gamekit/creating-activities-for-your-game. Seen 2026-10-12.
8. Sending web push notifications in web apps and browsers. Apple Developer Documentation. https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers. Seen 2026-10-12.
9. Notification runtime permission. Android Developers. https://developer.android.com/develop/ui/views/notifications/notification-permission. Seen 2026-10-12.
10. Leaderboards (Play Games Services). Android Developers. https://developer.android.com/games/pgs/leaderboards. Seen 2026-10-12.
11. Events (Play Games Services). Android Developers. https://developer.android.com/games/pgs/events. Seen 2026-10-12.
12. Promotional content, answers 12932541 and 12929944. Play Console Help. https://support.google.com/googleplay/android-developer/answer/12932541. Search summaries, 2026-10-12.
13. Promotional content (program page). Google Play Console. https://play.google.com/console/about/programs/promotionalcontent/. Search summary, 2026-10-12.
14. Promotional content on Google Play. ASOMobile. https://asomobile.net/en/blog/promotional-content-on-google-play-2024/. 2024.
15. About Firebase A/B tests. Firebase Documentation. https://firebase.google.com/docs/ab-testing/ab-concepts. Search summary, 2026-10-12.
16. Wordle. The New York Times Help Center. https://thenewyorktimeshelpcenter.helpjuice.com/24611727334932-Wordle. Search summary, 2026-10-12.
17. The New York Times Company, Form 10-Q, Q2 2026. SEC. URL not recorded. 2026.
18. LinkedIn Games guide. ConnectSafely and other guides. https://connectsafely.ai/articles/linkedin-games. 2026.
19. Puzzmo and Hearst coverage. MediaPost. URL not recorded. 2025 to 2026.
20. Discord Activities monetization. Discord Developer Docs. URL not recorded. 2026-05.
21. Reddit Devvit games and Developer Funds. Reddit. URL not recorded. 2025 to 2026.
22. How the Duolingo streak builds habit. Duolingo Blog. https://blog.duolingo.com/how-duolingo-streak-builds-habit. Search summary, 2026-10-12.
23. Duolingo paid streak repair. Deceptive Design. https://www.deceptive.design/articles/when-a-user-uses-duolingo-on-a-series-of-consecutive-days-this-is-called-a-streak-if-users-miss-a-day-they-can-pay-to-repair-it. Search summary, 2026-10-12.
24. Royal Match release notes archive. APKMirror. https://www.apkmirror.com/apk/dream-games-ltd-2/royal-match/. 2024 to 2026-04.
25. Royal Match teardowns. Naavik, FoxData, Sensor Tower, Deconstructor of Fun. URL not recorded. 2021 to 2026.
26. Royal Match digest. Naavik. URL not recorded. 2021.
27. Unfair practices and manipulative designs in online games and on gaming platforms. vzbv. https://www.vzbv.de/sites/default/files/2025-04/25-03-11_Paper_vzbv_Manipulative_design_unfair_practices_online_games.pdf. 2025.
28. Verbraucherschützer: Viele Online-Games manipulieren. heise online. https://www.heise.de/news/Verbraucherschuetzer-Viele-Online-Games-manipulieren-10425557.html. 2025-06.
29. Monopoly Go coverage. mobilegamer.biz, Pocket Gamer and others. URL not recorded. 2024 to 2026.
30. Block Blast testing and scale coverage. mobilegamer.biz; Business Wire. URL not recorded. 2025 to 2026-01-08.
31. Color Block Jam teardown. Segwise; Mobidictum citing AppMagic. URL not recorded. 2025-04.
32. Royal Match continue price example. fungies.io. URL not recorded. 2025.
33. GameAnalytics 2025 benchmarks summary. GameDev Reports. URL not recorded. 2025.
34. Gaming insights 2026. Adjust. URL not recorded. 2026.
35. Retention analysis documentation. Amplitude. URL not recorded. Ongoing.
36. Event types. GameAnalytics Docs. URL not recorded. Ongoing.
37. Soft launch gate guides. Game Growth Advisor (2025-12-16), Bruin. URL not recorded. 2025.
38. Deriving D7 targets from the curve. Liftoff. URL not recorded. 2026-04.
39. CPC key principles on in-game virtual currencies. European Commission and CPC network, via Mondaq and Baker McKenzie. URL not recorded. 2025-03-21.
40. Guidelines on the protection of minors under DSA Article 28. European Commission, via Osborne Clarke. URL not recorded. 2025-07.
41. Digital Fairness Act status. Lewis Silkin; Commissioner McGrath. URL not recorded. 2026.
42. FTC v Epic Games; FTC v Cognosphere. US Federal Trade Commission. URL not recorded. 2022, 2025.
43. Turkey Law 7578 coverage. Evrensel, NTV. URL not recorded. 2026.
44. UK ASA rulings on game ads. ASA via Pocket Gamer and Mishcon de Reya. URL not recorded. 2020 to 2026.
45. Game Monetization Contract v0.2. Ads Master. skills/game-monetization/references/monetization-contract.md. 2026-10.
46. Sample size and design effect arithmetic. This package, references/experiments-and-remote-config.md section 3. 2026-10-15.
