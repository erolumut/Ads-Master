# Sources (annotated)

> Compiled 2026-10-15 from the 2026-10-12 game studio research notes (teardowns, web daily puzzles, analytics, store presence, regulation, monetization) and a verification pass on 2026-10-12 that read Apple and Android developer pages in full. Google help pages, Firebase, the vzbv site and the WebKit blog were not reachable from this environment, so their content is known only from search summaries. "URL not recorded" means the notes named the publisher and date but not the link; search by title before relying on it. Vendor reports have commercial interests and non random samples. The research narrative and the verification queue are in `research/game-liveops.md`, which uses the same numbering.

How to read the "Supports" column: it names the claims a source backs and the label they carry. A single source never earns more than [Unverified]; a page seen only as a search summary never earns [Official].

## Apple: official pages read in full (2026-10-12)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | In-App Events | Apple Developer | https://developer.apple.com/app-store/in-app-events/ | page seen 2026-10-12 (no date on page) | 15 approved and 10 published events at a time; 31 days; promoted up to 14 days before; name 30, short 50, long 120 characters; badges and their meanings; purposes; priority; where events show; good and poor candidates (daily tasks and price only promotions are poor); no specific prices in metadata; media specs; deep link guidance [Official, 2026-10] |
| 2 | Overview of In-App Events | App Store Connect Help | https://developer.apple.com/help/app-store-connect/offer-in-app-events/overview-of-in-app-events/ | seen 2026-10-12 | Events in the App Store and Apple Games on iOS and iPadOS 15+; opt in notification when the event starts; roles [Official, 2026-10] |
| 3 | App Review Guidelines | Apple Developer | https://developer.apple.com/app-store/review/guidelines/ | last updated 2026-06-08, read 2026-10-12 | 1.2 filter, report and block for UGC and no random or anonymous chat; 2.3.13 in-app events; 3.1.1 IAP, purchased currencies may not expire, gifting, loot box odds; 4.5.3 no spam via Game Center, push, Live Activities; 4.5.4 push marketing only after opt in, with opt out; 5.1.2(i) no compensation for enabling push [Official, 2026-06] |
| 4 | Apple Games app (developer page) | Apple Developer | https://developer.apple.com/games-app/ | seen 2026-10-12 | Games app pre-installed on iOS 26, iPadOS 26, macOS 26; challenges; multiplayer activities; events on the Home tab, game page, library and search; Top Played; friend score notifications even when uninstalled [Official, 2026-10] |
| 5 | Game Center | Apple Developer | https://developer.apple.com/game-center/ | seen 2026-10-12 | Leaderboard notifications when a friend passes a score; achievements with rarity; Activity and Continue Playing widgets; real time and turn based multiplayer [Official, 2026-10] |
| 6 | Creating engaging challenges from leaderboards | Apple Developer Documentation (GameKit) | https://developer.apple.com/documentation/gamekit/creating-engaging-challenges-from-leaderboards | seen 2026-10-12 | Challenges built on an active leaderboard; daily mini crossword example with a recurring leaderboard restarting daily and a non repeatable challenge; score submission consumes a challenge attempt; submit after a revive is accepted or declined; minimum version [Official, 2026-10] |
| 7 | Creating activities for your game | Apple Developer Documentation (GameKit) | https://developer.apple.com/documentation/gamekit/creating-activities-for-your-game | seen 2026-10-12 | Activities deep link into content (daily puzzle example); party codes; a challenge supports up to 16 players; fallback URL to a web invite page [Official, 2026-10] |
| 8 | Sending web push notifications in web apps and browsers | Apple Developer Documentation | https://developer.apple.com/documentation/usernotifications/sending-web-push-notifications-in-web-apps-and-browsers | seen 2026-10-12 | Web push for Home Screen web apps on iOS 16.4+ and Safari on macOS; permission from a user gesture; no invisible push or the permission is revoked; badging [Official, 2026-10] |

## Android: official pages read in full (2026-10-12)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 9 | Notification runtime permission | Android Developers | https://developer.android.com/develop/ui/views/notifications/notification-permission | seen 2026-10-12 | `POST_NOTIFICATIONS` runtime permission on Android 13+; after "Don't allow" no non exempt notifications [Official, 2026-10] |
| 10 | Leaderboards (Play Games Services) | Android Developers | https://developer.android.com/games/pgs/leaderboards | seen 2026-10-12 | Daily, weekly and all time boards created automatically; daily reset at UTC-7 all year; weekly reset between Saturday and Sunday; social and public boards [Official, 2026-10] |
| 11 | Events (Play Games Services) | Android Developers | https://developer.android.com/games/pgs/events | seen 2026-10-12 | PGS events are analytics counters with premium currency source and sink types, not live events [Official, 2026-10] |

## Google and Firebase: search summaries only

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 12 | Promotional content (answers 12932541 and 12929944) | Play Console Help | https://support.google.com/googleplay/android-developer/answer/12932541 | seen as summaries 2026-10-12 | Types (offers, time limited events, major updates incl. pre-registration); earliest submission 60 days ahead; approval up to 4 days; Partner Program for Games 14 days; preview 14 days; offers limited to new users; no limit per quarter; durations [Reported, 2026-10]; durations [Contested with 14] |
| 13 | Promotional content | Google Play Console program page | https://play.google.com/console/about/programs/promotionalcontent/ | seen as summary 2026-10-12 | Eligibility; lapsed and churned targeting since 2025-03 [Reported, 2026-10]; acquisition lift claims [Unverified, Google marketing] |
| 14 | Promotional content on Google Play (2024) | ASOMobile | https://asomobile.net/en/blog/promotional-content-on-google-play-2024/ | 2024 | Different durations for major updates [Contested] |
| 15 | About Firebase A/B tests | Firebase Documentation | https://firebase.google.com/docs/ab-testing/ab-concepts | seen as summary 2026-10-12 | Two weeks recommended minimum; daily result updates; 90 day processing limit and auto stop [Reported, 2026-10] |

## Daily puzzles, web distribution and habit products

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 16 | Wordle | The New York Times Help Center | https://thenewyorktimeshelpcenter.helpjuice.com/24611727334932-Wordle | seen as summary 2026-10-12 | New puzzle at midnight in the player's time zone; statistics with Current Streak and Max Streak; finishing after local midnight breaks the streak [Reported, 2026-10] |
| 17 | New York Times Company quarterly report (10-Q), Q2 2026 | SEC | URL not recorded (sec.gov) | 2026 | 13.35 million subscribers across all products (not games only); The Mini paywall in Q3 2025 added single product subscribers [Reported, 2026-10] |
| 18 | LinkedIn Games guides | ConnectSafely and others | https://connectsafely.ai/articles/linkedin-games | 2026 | Daily reset at midnight Pacific; streaks; comparisons with connections [Reported, 2026-10]; company and school boards [Unverified, guides disagree] |
| 19 | Puzzmo and Hearst coverage | MediaPost | URL not recorded | 2025 to 2026 | Puzzmo Plus about $40 a year (archives, leaderboards, no ads); Hearst acquisition [Reported, 2026-10] |
| 20 | Discord Activities monetization | Discord Developer Docs | URL not recorded (docs.discord.com) | 2026-05 | Embedded App SDK 2.5.0; SKUs for IAP and subscriptions in some regions; group play fit [Reported, 2026-10] |
| 21 | Reddit Devvit games and Developer Funds | Reddit | URL not recorded | 2025 to 2026 | Daily games encouraged; Developer Funds [Reported, 2026-10] |
| 22 | How the Duolingo streak builds habit | Duolingo Blog | https://blog.duolingo.com/how-duolingo-streak-builds-habit | seen as summary 2026-10-12 | Streak freeze fills a missed day, bought in advance with gems, up to two equipped [Reported, 2026-10] |
| 23 | Duolingo paid streak repair | Deceptive Design | https://www.deceptive.design/articles/when-a-user-uses-duolingo-on-a-series-of-consecutive-days-this-is-called-a-streak-if-users-miss-a-day-they-can-pay-to-repair-it | seen as summary 2026-10-12 | Paid streak repair listed as a deceptive pattern [Reported, 2026-10] |

## Game teardowns and trade press

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 24 | Royal Match release notes archive | APKMirror (store "What's new" text) | https://www.apkmirror.com/apk/dream-games-ltd-2/royal-match/ | 2024 to 2026-04 | "New levels every two weeks", about 100 levels per update, often with a new area or event; uploads roughly two weeks apart [Reported, 2026-10] |
| 25 | Royal Match teardowns | Naavik, FoxData, Sensor Tower, Deconstructor of Fun | URL not recorded | 2021 to 2026 | King's Cup (level 25, about 2 days, about 50 players), Sky Race (3 days), Lightning Rush (1 hour), team chest and in team top 3, boosters taught around level 7, near miss fails as core design, lighter meta test lost to control, 12,400+ levels by 2025-11 [Reported, 2026-10]; Royal Pass from level 37 with about 30 steps a month [Unverified, single source] |
| 26 | Royal Match digest | Naavik | URL not recorded | 2021 | Pass launch in June 2021 with +31% revenue in the first 30 days [Unverified, single source] |
| 27 | Unfair practices and manipulative designs in online games and on gaming platforms | vzbv | https://www.vzbv.de/sites/default/files/2025-04/25-03-11_Paper_vzbv_Manipulative_design_unfair_practices_online_games.pdf | 2025-03 to 2025-04 | Manipulative design in five reviewed titles incl. Monopoly Go: countdowns, daily play incentives, rewards for ads; pop up offers at app start [Reported, 2026-10] (not opened) |
| 28 | Verbraucherschützer: Viele Online-Games manipulieren | heise online | https://www.heise.de/news/Verbraucherschuetzer-Viele-Online-Games-manipulieren-10425557.html | 2025-06 | Coverage of the vzbv review; Scopely cease and desist declaration [Reported, 2026-10] |
| 29 | Monopoly Go coverage | mobilegamer.biz, Pocket Gamer and others | URL not recorded | 2024 to 2026 | Partner events, sticker albums; lifetime revenue above $6B; New York attorney general suit over paid loot boxes reported 2026-02 [Reported, 2026-10] |
| 30 | Block Blast testing and scale coverage | mobilegamer.biz; Business Wire | URL not recorded | 2025 to 2026-01-08 | 50+ A/B tests a week, about 97% fail, 10,000+ tests in 2025 [Unverified, single source]; 70M DAU [Unverified, vendor claim] |
| 31 | Color Block Jam teardown | Segwise; Mobidictum citing AppMagic | URL not recorded | 2025-04 | Little live ops, growth via paid UA; early levels nearly ad free; difficulty tuned for booster purchases [Unverified, vendor source] |
| 32 | Royal Match continue price example | fungies.io | URL not recorded | 2025 | First continue near 900 coins, above 2,000 after a second fail [Unverified, single source] |

## Game analytics

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 33 | GameAnalytics 2025 benchmarks (summary) | GameDev Reports citing GameAnalytics | URL not recorded | 2025 (data to end 2024) | D1 about 22%, D7 3.4% to 3.9%, D30 about 0.7%; top 10% about 40/12/4 [Reported, 2026-10] |
| 34 | Gaming insights 2026 | Adjust | URL not recorded | 2026 | D1 27% across genres in 2025 [Reported, 2026-10] |
| 35 | Retention analysis documentation | Amplitude | URL not recorded | ongoing | Rolling 24 hour windows vs calendar days [Reported, 2026-10] |
| 36 | Event types | GameAnalytics Docs | URL not recorded | ongoing | Progression start, complete and fail events; resource source and sink [Reported, 2026-10] |
| 37 | Soft launch gate guides | Game Growth Advisor (2025-12-16), Bruin | URL not recorded | 2025 | Gates such as D1 above 40% casual; top decile next to medians [Reported, 2026-10] |
| 38 | Deriving D7 targets from the curve | Liftoff | URL not recorded | 2026-04 | Fixed D180 to D7 multipliers go stale [Reported, 2026-10] |

## Law, regulation and enforcement (context; compliance verifies)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 39 | CPC key principles on in-game virtual currencies | European Commission and CPC network, via Mondaq and Baker McKenzie notes | URL not recorded | 2025-03-21 | Real money prices, no forced currency purchases, withdrawal rights, children [Reported, 2026-10] |
| 40 | Guidelines on the protection of minors under DSA Article 28 | European Commission, via Osborne Clarke | URL not recorded | 2025-07 | Minors and manipulative design, paid random items, currencies [Reported, 2026-10] |
| 41 | Digital Fairness Act status | Lewis Silkin (2026-01-14); Commissioner McGrath remarks (2026-10-11) | URL not recorded | 2026 | Proposal expected Q4 2026 [Reported, 2026-10] |
| 42 | FTC v Epic Games (2022); FTC v Cognosphere (2025-01) | US Federal Trade Commission | URL not recorded (ftc.gov) | 2022, 2025 | Dark patterns refunds and COPPA penalty; Genshin settlement terms [Reported, 2026-10] |
| 43 | Turkey Law 7578 coverage | Evrensel, NTV | URL not recorded | 2026-04 to 2026-05 | Age ratings, parental controls incl. purchase approval [Reported, 2026-10] |
| 44 | UK ASA rulings on game ads | ASA, via Pocket Gamer and Mishcon de Reya | URL not recorded | 2020 to 2026 | Ads must show representative gameplay [Reported, 2026-10] |

## Internal

| # | Title | Publisher | Path | Date | Supports |
|---|-------|-----------|------|------|----------|
| 45 | Game Monetization Contract v0.1 | Ads Master | `skills/game-monetization/references/monetization-contract.md` | 2026-10 | Modes, boards with scope, typed grants, `streak_protection`, offer points, admin grants, minors runbook |
| 46 | Sample size and design effect arithmetic | This package | `references/experiments-and-remote-config.md` section 3 | 2026-10-15 | Two proportion sample sizes; unequal holdout totals; design effect examples (computed, not benchmarks) |

## Where the evidence is thin (feeds the verification queue)

- Play promotional content: eligibility, lead times, durations and audiences come from search summaries only.
- Firebase A/B Testing limits come from a search summary.
- vzbv's exact list of objections to Monopoly Go (the notes add opaque currencies and absence penalties; the summaries confirm pop up offers, countdowns and daily play incentives).
- Royal Match event facts beyond the release note cadence; the Royal Pass details and its revenue lift are single source.
- LinkedIn games boards (company and school) are disputed between guides.
- Benchmarks are vendor medians from secondary summaries.

## Source hygiene for this package

1. Before a G3 change rests on a claim marked [Reported], [Unverified] or [Contested], read the source in full or check the live console, and record the result with the `ads-verify` skill in `ads-master/VERIFIED.md`.
2. Teardown facts describe one game's history; never present them as a forecast or a target.
3. When an official page and a vendor disagree, the live console wins for that account, then the official page, then the vendor.
4. Add new sources here with a number, date and the label they support; never renumber existing rows.

## Which sources back which module

| Module | Main sources |
|--------|--------------|
| [Daily loops and streaks](daily-loops-and-streaks.md) | 3, 6, 7, 8, 9, 10, 16, 17, 18, 19, 22, 23, 27, 28, 39, 40, 41, 45 |
| [Events and seasons](events-and-seasons.md) | 1, 3, 24, 25, 26, 29, 31, 45 |
| [Teams, groups and leagues](teams-groups-and-leagues.md) | 3, 4, 5, 6, 7, 10, 11, 18, 25, 29, 45 |
| [Content cadence and difficulty signals](content-cadence-and-difficulty-signals.md) | 16, 24, 25, 31, 33, 36 |
| [Liveops calendar and store events](liveops-calendar-and-store-events.md) | 1, 2, 3, 4, 6, 7, 8, 10, 11, 12, 13, 14, 20, 21 |
| [Experiments and remote config](experiments-and-remote-config.md) | 15, 25, 30, 46 |
| [Retention diagnostics](retention-diagnostics.md) | 33, 34, 35, 37, 38 |
| [Player trust and pressure patterns](player-trust-and-pressure-patterns.md) | 3, 22, 23, 27, 28, 29, 32, 39, 40, 41, 42, 43, 44, 45 |
