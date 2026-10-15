# Research Dossier: Game Monetization (web, PWA, iOS, Android)

> Research pass completed 2026-10-12 for the Ads Master `game-monetization` package, as part of the Game Studio research (ten questions run in parallel: monetization design, ad tech, user acquisition, analytics, store presence, regulation, teardowns of Royal Match, Color Block Jam, Block Blast and Monopoly Go, web first distribution, Apple review, Google Play review). Scope: economy and catalog, offer points, ad mediation and placement policy, web game monetization, payer segmentation, payment operations, fairness for ranked modes and the per DAU and per placement economics. Evidence labels follow docs/AUTHORING_SPEC.md section 7 plus [Reported, 2026-10] (see Method). Numbers in brackets refer to the Sources list at the end, which uses the same numbering as `skills/game-monetization/references/sources.md`.

## Research method and limits

1. Apple's App Review Guidelines (revision 2026-06-08), Apple's EU terms page, the age ratings values, the subscriptions page and the third party SDK requirements, plus Google's Play Billing, Android vitals, Play policies and TWA pages were opened and read [1 to 9]. Those facts carry [Official, 2026-10].
2. Everything else (mediation shares and terms, eCPMs, portal deals, platform embeds, teardowns, market sizes, almost all regulation) came from search result summaries or vendor material. Labeling rule: [Reported, 2026-10] for official page hits and credible press seen as summaries, or two dated independent sources; [Unverified] for a single source and for vendor claims (marked "vendor claim"); [Contested] where credible sources disagree, with both sides shown.
3. No legal text was read in full in this pass. Regulation is summarized for routing work; `compliance` gives the verdict per market.
4. Provider refund notification names (Stripe, App Store Server Notifications, Play Real-time developer notifications) are written from documentation known before this pass and were not re-read; they are [Unverified] until confirmed.
5. Not covered here: per install economics and UA (`mobile-app-growth`, `game-user-acquisition`), KPI definitions and dashboards (`measurement`, `game-kpis` and `game-tracking`), store presence and featuring (`app-store-optimization`, `game-store-features`), submission (`store-submission`), price points (`pricing-strategy`, `iap-price-points`).

## Executive summary

1. The fair default is clear and checkable: ranked results are never purchasable, and progression modes may sell boosters, extra moves and extra time at a fixed price with a limit per attempt. The contract and `monetization_check.py` enforce it from typed grants and declared boards rather than self declaration (internal). The market sells "+5 moves" continues and pre level boosters in top match games [Reported, 2026-10] [39, 40, 42].
2. Escalating continue prices exist in top games (a reported Royal Match first continue near 900 coins rising above 2,000 after a second fail) [Unverified] [53], and they sit inside the pressure patterns European consumer authorities now target: the CPC key principles on in-game virtual currencies (2025-03-21) ask for real money prices, no forced currency purchases, withdrawal rights and protection of children [Reported, 2026-10] [57, 58, 59].
3. Ad mediation consolidated: AppLovin MAX is reported above 50% mediation share in 2025 [Reported, 2026-10] [29, 30]; AdMob added InMobi, ironSource and Unity bidding on 2025-07-07 [Reported, 2026-10] [30]; AppLovin sued Unity on 2026-09-29 over the Ad Quality SDK in LevelPlay [Reported, 2026-10] [32]. One mediator, bidding first, is the consensus pattern.
4. Interstitial practice converges on holding ads back: first interstitial after level 3 to 8 or 60 to 90 seconds, a 2 to 3 minute cooldown, 4 to 6 per session, a timer reset after rewarded, and tests of 7 days or more judged on ARPDAU with D1 and D7 as constraints [Reported, 2026-10] [45, 54]. Rewarded multipliers are reported as the most popular puzzle placement [Unverified, vendor claim] [45].
5. Consent is a revenue condition, not only a legal one: Google requires certified IAB TCF CMPs in the EEA and UK and TCF v2.3 had a deadline around 2026-03-01 after which non compliant traffic gets Limited Ads [Reported, 2026-10] [30]. CNIL fined a game publisher EUR 3 million in 2023 over identifier use without consent [Reported, 2026-10] [71].
6. Web monetization cannot rely on Google's H5 Games Ads: it is a closed beta with strict rules (opt in rewarded, no value outside the game, `adBreak()` at transitions) [Reported, 2026-10] [13, 14]. Passes, subscriptions and group purchases through Stripe or a merchant of record carry a web first game; selling digital goods to EU and Turkish buyers creates VAT duties per buyer country (internal contract note).
7. Daily puzzle subscriptions work at publisher scale: The New York Times reported 13.35 million subscribers in Q2 2026 and added single product subscribers after paywalling The Mini [Reported, 2026-10] [80]; Puzzmo Plus sells archives, leaderboards and no ads for about $40 a year [Unverified] [81]. This supports a plus style subscription (archive, stats, uncounted replay) for daily games.
8. Loot boxes are the fastest moving legal area: the UK ASA requires "Contains loot boxes" prominently in store listings (enforcement notice 2026-02-26, monitoring from 2026-05-26) [Reported, 2026-10] [64]; Brazil banned paid loot boxes for minors from 2026-03 [Reported, 2026-10] [63]; PEGI defaults new games with paid random items to PEGI 16 from 2026-06-01 [Reported, 2026-10] [74]; Apple requires odds before purchase [Official, 2026-10] [1] and lists loot boxes in its age rating values [Official, 2026-10] [3]. The default is no random paid items.
9. Minors and purchases: the FTC's Genshin Impact settlement (2025-01) bars purchases under 16 without parental consent in the US [Reported, 2026-10] [67]; Turkey Law 7578 (passed 2026-04-22) requires age ratings and parental controls including purchase approval on game platforms, with duties mostly starting after the implementing regulation [Reported, 2026-10] [73].
10. Store fees moved in 2026: Apple's EU terms from 2026-10-01 [Official, 2026-10] [2]; Google Play fee changes from 2026-06-30 in the US, EEA and UK [Reported, 2026-10] [10]; the US link out commission is under Supreme Court review in Epic v Apple [Reported, 2026-10] [77]. Any web shop plan that assumes zero commission is temporary.

## State of the market in 2026 (with numbers)

| Indicator | Value | Source |
|-----------|-------|--------|
| Mobile game revenue 2025 | About $82 billion (+1%) | Sensor Tower [42] [Reported, 2026-10] |
| Mobile game ad revenue 2025 | About $12 billion; puzzle and arcade over 65% | Sensor Tower via GameDevReports [49] [Reported, 2026-10] |
| H1 2026 direction | Mobile IAP about minus 2% (about $40 billion); game ad spend about plus 8% | PocketGamer.biz [44] [Reported, 2026-10] |
| Mediation share | AppLovin MAX over 50% (2025) | PocketGamer.biz, PPC Land [29, 30] [Reported, 2026-10] |
| Game ad revenue by platform, Q2 2026 | 55% Android, 45% iOS | Tenjin [37] [Unverified, vendor] |
| Rewarded eCPM Q4 2024 | About $13.6 iOS, $9.0 Android | Appodeal [34] [Unverified, vendor report] |
| Payer conversion | 2% to 5% | Unity [45] [Unverified, vendor claim] |
| IAP concentration | 1% to 2% of players drive 50% to 70% of IAP | One source [Unverified] |
| Royal Match lifetime revenue per download | About $34 | Naavik [39] [Unverified] |
| NYT subscribers Q2 2026 | 13.35 million | SEC filing via search [80] [Reported, 2026-10] |

## Timeline of changes, January 2025 to October 2026

| Date | Change | Impact | Evidence |
|------|--------|--------|----------|
| 2025-01 | FTC Genshin Impact settlement (USD 20 million) | Parental consent under 16, real cost, odds | [Reported, 2026-10] [67] |
| 2025-03-21 | CPC key principles on in-game virtual currencies | Real money prices, no forced purchases, minors | [Reported, 2026-10] [57] |
| 2025-03 | CPC action on Star Stable | Ads to children, time pressure, currency information | [Reported, 2026-10] [59] |
| 2025-06 | VZBV objects to Monopoly Go (pop ups, opaque currencies, absence penalties) | Pressure patterns named | [Reported, 2026-10] [76] |
| 2025-07 | DSA Art. 28 minors guidelines | Minors kept from paid random items and manipulative design | [Reported, 2026-10] [61] |
| 2025-07 | Apple age ratings add 13+, 16+, 18+ (answers due 2026-01-31) | New questionnaire | [Official, 2026-10] [3] |
| 2025-07-07 | AdMob adds InMobi, ironSource and Unity bidding | AdMob demand | [Reported, 2026-10] [30] |
| 2025-07-31 | Meta developer post on web and Instant Games changes | Web games on Meta uncertain | [Unverified] [17] |
| 2025-11 | ASA rulings against Kabam and Hutch | Loot box disclosure in ads | [Reported, 2026-10] [64] |
| 2025-11-13 | Apple guideline clarifications including 4.7 mini apps | HTML5 game wrappers | [Official, 2026-10] [1] |
| 2025-12 | Ninth Circuit in Epic v Apple; AGCM fines Apple EUR 98.6 million (double consent) | Link out fees; consent design | [Reported, 2026-10] [77, 72] |
| 2026-02 | New York Attorney General sues over Monopoly Go paid loot boxes | US loot box risk | [Reported, 2026-10] [76] |
| 2026-02-26 | ASA and CAP enforcement notice: "Contains loot boxes" in listings | UK label duty, monitoring from 2026-05-26 | [Reported, 2026-10] [64] |
| About 2026-03-01 | TCF v2.3 deadline | Limited Ads for non compliant traffic | [Reported, 2026-10] [30] |
| 2026-03-16 | Brazil ECA Digital in force | Paid loot boxes banned for minors | [Reported, 2026-10] [63] |
| 2026-04-22 | Turkey Law 7578 passed; COPPA amendments compliance date | Parental purchase approval in Turkey; US children's data | [Reported, 2026-10] [73, 68] |
| 2026-05 | Discord Embedded App SDK 2.5.0 with SKUs | Group play monetization | [Reported, 2026-10] [18] |
| 2026-06-01 | PEGI 16 default for new games with paid random items | Ratings | [Reported, 2026-10] [74] |
| 2026-06-08 | App Review Guidelines revision | Current 3.1 and 4.x text | [Official, 2026-10] [1] |
| 2026-06-19 | EU withdrawal function for online contracts with a right of withdrawal | Subscription and purchase flows | Compliance skill (SUB-EU-01) |
| 2026-06-30 | Google Play fee changes (US, EEA, UK); Supreme Court agrees to review Epic v Apple | Fees | [Reported, 2026-10] [10, 77] |
| 2026-08-31 | Play Billing Library 8 required (extension to 2026-11-01) | Wrapper and app updates | [Official, 2026-10] [6] |
| 2026-09 | Apple age rating social media question required | Forms | [Official, 2026-10] [3] |
| 2026-09-29 | AppLovin sues Unity over the Ad Quality SDK in LevelPlay | Mediation choice risk | [Reported, 2026-10] [32] |
| 2026-09-30 | CPC action on virtual currencies against nine game companies (per the compliance skill); "Meta Web Games ended" as recorded | Enforcement; web games on Meta | Compliance skill; [Unverified] [17] |
| 2026-10-01 | Apple EU terms; reported start of PEGI reclassification of existing games with paid random items | Fees; ratings | [Official, 2026-10] [2]; reclassification [Contested] [74] |
| Expected Q4 2026 | Digital Fairness Act proposal (dark patterns, addictive design, virtual currencies, minors) | EU rules ahead | [Reported, 2026-10] [60] |

## Best practice consensus

1. One soft currency with a free path in progression games; real money prices visible; no forced leftovers [Reported, 2026-10] [39, 45, 46, 57].
2. Continues are a choice with a free rewarded path, a fixed price and a per attempt cap; boosters are taught before they are sold [Reported, 2026-10] [39, 40, 45].
3. Starter packs after the first levels and event offers tied to the obstacle; piggy banks later [Reported, 2026-10] [47].
4. One mediator, bidding first, networks added one at a time with tests [Reported, 2026-10] [27 to 31].
5. Interstitials held back early, capped, reset after rewarded; banners only in menus; rewarded opt in, granted on completion and capped daily [Reported, 2026-10] [45, 54].
6. Consent before any ad SDK; certified CMPs in the EEA and UK; ATT after value [Reported, 2026-10] [30, 71].
7. Ad removal keeps optional rewarded ads and says so [Reported, 2026-10].
8. Server side grants with an idempotent ledger and refund revocation (contract runbook; practitioner consensus).
9. Tests run at least a week, judged on ARPDAU with retention as a constraint [Reported, 2026-10] [45, 49].

## Contested topics (both sides)

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Rewarded ads as the fair path to an extra counted try | Everyone can watch an ad | Fill, ATT, consent, ad blockers and beta programs make access unequal [Reported, 2026-10] [13, 30] | Rewarded grants only uncounted replays in ranked products |
| ATT opt in rates for games | 51% (AppsFlyer, Q1 2024) | 35% (Adjust, Q2 2025); 13.85% (Singular, Q2 2024) [38] | Methods differ; measure own opt in |
| Poki exclusivity length | 5 years | 7 years [24] | Read the contract |
| GameDistribution revenue share | 33% | 45% [26] | Read the live terms |
| Discord Activities fee | Sources disagree [18] | | Read the developer terms |
| Color Block Jam revenue | $25 million IAP in Q1 2025 (AppMagic via Mobidictum) [43] | $12.1 million per 30 days (Insightrackr) [56] | Do not quote either as fact |
| Interstitial after every level | Screwdom reportedly earned over $75 million IAP in 2025 with it [50] [Unverified] | Teardown notes list it as a pattern not to copy; retention and reviews pay [Reported, 2026-10] | Refuse; test caps instead |
| PEGI reclassification of existing games | Existing games with paid random items are reclassified from 2026-10-01 (the compliance pack row) [74] | Some sources say existing titles keep their rating | Check the PEGI criteria and the game's current rating before answering forms |
| Hidden piggy bank price until full | Common in the market [47] | Transparency under the CPC principles [57] | Show the price from the start |

## What top operators do differently

| Average | Top 1% |
|---------|--------|
| Sells whatever converts at the fail screen | Sells play only in progression, at a fixed price, with caps; never a ranked result |
| Adds interstitials to lift ARPDAU | Holds ads back early, tests caps with D7 guard rails and holdouts |
| Reads eCPM | Reads revenue per DAU per placement and per shown offer |
| Picks a mediator by brand | Tests mediators on own traffic with the built in A/B tools |
| Treats refunds as finance | Revokes in minutes, claws back only what was refunded, reads refund rate by SKU |
| Targets whales | Protects high spenders with fewer interruptions and support priority |
| Hard codes frequencies | Keeps every value in remote config with a kill switch and a policy revision |
| Waits for web ads | Earns on the web with passes, subscriptions and group purchases first |
| Copies benchmark targets | Compares with own history and labels every benchmark |

## Common expensive mistakes

1. Selling or rewarding an extra counted try in a ranked daily game.
2. Escalating continue prices inside one attempt, or sibling offers that do the same.
3. Countdown offers shown to minors.
4. Purchasable currency without its real money price; awkward pack sizes.
5. An ad SDK initialized before consent; ATT before value.
6. Interstitials in the first session or inside an attempt; banners in play.
7. "No ads" claims while rewarded or other formats still run.
8. Client side grants; no refund revocation; locking accounts after disputes.
9. Selling digital goods on the web to EU and Turkish buyers without a tax decision.
10. A web plan that depends on the H5 Games Ads beta or on zero link out commission.
11. Random paid items without odds, labels and age gates; selling them in Belgium.
12. Changing several monetization settings at once without a revision or holdout.

## Benchmarks (source, date, sample, caveat)

| Metric | Value | Source and date | Sample | Caveat |
|--------|-------|-----------------|--------|--------|
| ARPDAU hybrid casual | $0.15 to $0.50 | Vendor material, 2026 | Unknown | [Unverified, vendor claim] |
| ARPDAU casual and puzzle | $0.03 to $0.10 | Vendor material, 2026 | Unknown | [Unverified, vendor claim] |
| Payer conversion | 2% to 5% | Unity [45] | Unknown | [Unverified, vendor claim] |
| Rewarded, interstitial, banner eCPM | $13.6 and $9.0; $10.4 and $9.6; $0.4 and $0.5 (iOS and Android) | Appodeal Q4 2024 [34] | Appodeal traffic | One mediator; seasonality (Q4) |
| Regional eCPM | Western Europe iOS $5 to $12; Brazil Android $1 to $3; India Android $0.30 to $1 | MWM via playio, 2026 [36] | Unknown | Format not always stated |
| Retention context | D1 median about 22%, D7 3.4% to 3.9%, D30 about 0.7% | GameAnalytics 2025 via GameDevReports [49] | GameAnalytics customers | Owned by measurement; daily social games follow their own curve |

Compare a project against its own history first; benchmarks vary by genre, country, platform, season and traffic mix.

## Tools, APIs and scripts

| Category | Official | Third party | Notes |
|----------|----------|-------------|-------|
| Mediation | AppLovin MAX, Google AdMob, Unity LevelPlay (each with reporting APIs) | | Ad unit names equal policy placement ids |
| Web ads | Google Ad Placement API (H5 Games Ads, closed beta) | Portal SDKs (Poki, CrazyGames), web rewarded vendors | Consent first |
| Payments | StoreKit and App Store Server API, Play Billing and the Play Developer API, Stripe | Merchants of record (Paddle, Lemon Squeezy), web shop vendors (Xsolla, Stash) | Server side grants |
| Analytics | | GameAnalytics, Firebase, devtodev, PostHog (measurement's choice) | Definitions in `game-kpis` |
| Package scripts | `monetization_check.py`, `monetization_conformance.py` | | Standard library; exit 0, 1, 2 |

## Official sources to monitor

| Source | Where | Cadence |
|--------|-------|---------|
| App Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ | On each Apple notice |
| Apple Developer News | https://developer.apple.com/news/ | Weekly |
| Google Play Billing | https://developer.android.com/google/play/billing | Monthly |
| Play Console Help and Policy Center | https://support.google.com/googleplay/android-developer | Monthly |
| Google publisher policies for H5 games | https://support.google.com/publisherpolicies/answer/11975916 | Monthly |
| Mediation docs and payment terms | AppLovin, AdMob, Unity support sites | Monthly |
| EU consumer protection (CPC network, Digital Fairness Act) | European Commission | Monthly |
| UK ASA rulings | asa.org.uk | Monthly |
| PEGI | pegi.info | Quarterly |
| Turkey Official Gazette and BTK | Official sites | Monthly until the Law 7578 regulation lands |

## Verification queue

Each item names the cheapest check that settles it (L1 = live console or contract read, L2 = official page read in full, L3 = two independent dated sources, L4 = controlled test).

1. H5 Games Ads: beta status, admission and rules (L2).
2. Apple US link out commission after the Supreme Court review (L2, court records).
3. Google Play fee tiers above $1M and outside the first markets; external content link install fees (L2, L1 in the console).
4. AppLovin MAX share and terms; AdMob and LevelPlay payout terms (L1 in each live account).
5. AppLovin v Unity: effect on LevelPlay adapters (L3).
6. Provider refund notification names and Apple consumption requests (L2 in each provider's docs).
7. Turkey Law 7578: implementing regulation, start dates, parental approval details (L2, Official Gazette).
8. CPC virtual currency principles: full text and the 2026-09-30 action (L2).
9. UK loot box label wording and placement (L2, ASA notice).
10. PEGI paid random item rules and reclassification scope (L2).
11. EU digital content withdrawal exception wording after the Omnibus amendments (L2, EUR-Lex).
12. Poki exclusivity, CrazyGames split, GameDistribution share, Discord fee (L1, contracts).
13. Meta Instant Games and web games status after 2026-09-30 (L2).
14. Interstitial starting values on the game's own traffic (L4).
15. Payer conversion and ARPDAU ranges for the game's genre (own data; benchmarks stay context).

## Claims considered and not relied on

| Claim | Why not used |
|-------|-------------|
| Escalating continues are a best practice because top games use them | Single source [53]; regulators target the pattern; the contract forbids it |
| A rewarded ad makes an extra counted try fair | Unequal access; buys a ranked result |
| Whales should get more offers | Manipulation risk; concentration is read, not pushed |
| Vendor rewarded CPMs of $8 to $28 for web games | Sales material [23] |
| Web shops convert up to 45% worse and net $0.92 vs $0.70 | Vendor claims [79] |
| App open ads lift game revenue | No public evidence found for games |
| Hidden piggy bank prices until full are acceptable because common | Transparency principle |
| Lives and energy as a default mechanic | A gating mechanic; left to each game repo's design |
| Interstitial after every level, because it earned for one hit | Single source; trades retention and trust |

## Sources

1. App Review Guidelines. Apple Developer. https://developer.apple.com/app-store/review/guidelines/. Revision 2026-06-08, read 2026-10-12.
2. Apps in the EU (alternative terms). Apple Developer. Path from the notes: developer.apple.com/support/apps-in-the-eu. Read 2026-10-12.
3. Age ratings values. App Store Connect Help. URL not recorded. Read 2026-10-12.
4. Subscriptions. Apple Developer. Path from the notes: developer.apple.com/app-store/subscriptions. Read 2026-10-12.
5. Third party SDK requirements. Apple Developer. Path from the notes: developer.apple.com/support/third-party-SDK-requirements. Read 2026-10-12.
6. Google Play Billing (and subscriptions). Android Developers. https://developer.android.com/google/play/billing. Read 2026-10-12.
7. Android vitals. Android Developers. https://developer.android.com/topic/performance/vitals. Read 2026-10-12.
8. Play policies hub. Android Developers. Path from the notes: developer.android.com/distribute/play-policies. Read 2026-10-12.
9. Trusted Web Activity guide. Android Developers and Chrome Developers. URL not recorded. Read 2026-10-12.
10. Play expanded billing and fee changes. Android Developers Blog. URL not recorded. 2026-06.
11. Subscription disclosure requirements, answer 9900533. Play Console Help. https://support.google.com/googleplay/android-developer/answer/9900533. Seen 2026-10-12.
12. Families self certified ads SDK program, answer 12918983. Play Console Help. Path from the notes: support.google.com, answer 12918983. Seen 2026-10-12.
13. Ad Placement API (H5 Games Ads) beta docs. Google. Path from the notes: developers.google.cn/ad-placement/docs/beta. Seen 2026-10-12.
14. H5 games ads policy. Google Publisher Policies. https://support.google.com/publisherpolicies/answer/11975916. Seen 2026-10-12.
15. AdSense H5 Games Ads. Google AdSense. URL not recorded. Seen 2026-10-12.
16. YouTube Playables monetization reference. Google for Developers. Path from the notes: developers.google.com/youtube/gaming/playables/reference/monetization. Seen 2026-10-12.
17. Instant Games rewarded ads and web and Instant Games changes. Meta for Developers. URL not recorded. 2025-07-31.
18. Discord Activities monetization. Discord Developers. Path from the notes: docs.discord.com. Seen 2026-10-12.
19. Reddit Devvit Developer Funds. Reddit. URL not recorded. 2025 to 2026.
20. Telegram Stars. Telegram. URL not recorded. Seen 2026-10-12.
21. TikTok Growth Max and Mini Games. TikTok for Business. Path from the notes: ads.tiktok.com. 2026-05-13.
22. WebKit blog posts 13878 and 14112. WebKit. URL not recorded. 2023.
23. Web rewarded vendors (AppLixir FAQ, Playgama comparison, Cinevva). Vendors. URL not recorded. 2026.
24. Poki SDK and deal terms. Poki. Path from the notes: sdk.poki.com. Seen 2026-10-12.
25. CrazyGames payouts. CrazyGames docs. Path from the notes: docs.crazygames.com/payouts. Seen 2026-10-12.
26. GameDistribution revenue share. Various. URL not recorded. Seen 2026-10-12.
27. AppLovin payments and ad filtering. AppLovin Support. Path from the notes: support.applovin.com. Seen 2026-10-12.
28. MAX A/B testing and Ad Review. AppLovin Developers. Path from the notes: developers.applovin.com. Seen 2026-10-12.
29. Mediation market share 2025. PocketGamer.biz. URL not recorded. 2025.
30. AdMob bidding partners; TCF 2.3 deadline. PPC Land. URL not recorded. 2025-07-07 and 2026.
31. LevelPlay mediated networks. Unity docs. Path from the notes: docs.unity.com. Seen 2026-10-12.
32. AppLovin sues Unity over the Ad Quality SDK. PPC Land and MobileGamer.biz. URL not recorded. 2026-09-29.
33. AdMob Help answer 9760862. Google AdMob. https://support.google.com/admob/answer/9760862. Seen 2026-10-12.
34. eCPM report Q4 2024. Appodeal. URL not recorded (PDF). 2025.
35. US eCPM benchmarks. MonetizeMore. URL not recorded. Undated.
36. eCPM by region 2026. playio citing MWM. URL not recorded. 2026.
37. Game ad revenue by platform. Tenjin. URL not recorded. 2026-08.
38. ATT opt in rates. AppsFlyer, Adjust, Singular. URL not recorded. 2024 to 2025.
39. Naavik digest and Royal Match deep dive. Naavik. URL not recorded. 2021 to 2025.
40. Royal Match teardown and match 3 notes. FoxData. URL not recorded. 2025.
41. Royal Match revenue. Business of Apps. URL not recorded. 2025.
42. Royal Match vs Candy Crush; State of Gaming 2026; top 10 June 2025. Sensor Tower. URL not recorded. 2025 to 2026.
43. Hybrid casual Q1 2025 (AppMagic data); Gybe. Mobidictum. URL not recorded. 2025.
44. Top rewarded placements; H1 2026 IAP dip; Royal Kingdom; Rollic. PocketGamer.biz. URL not recorded. 2025 to 2026.
45. Top 5 rewarded placements; interstitial best practices; IAP guide; webshop business case. Unity. URL not recorded. 2024 to 2026.
46. Hybrid casual dos and don'ts. Supersonic. URL not recorded. 2025.
47. Piggy banks. maf.ad and Heroic Labs. URL not recorded. 2025.
48. Hybrid monetization (2024-12-09); screw puzzle gold rush; Royal Kingdom (2024-07-01). Deconstructor of Fun. URL not recorded. 2024.
49. Sensor Tower ad monetization; AppMagic hybrid casual; GameAnalytics 2025 benchmarks. GameDevReports. URL not recorded. 2025 to 2026.
50. Segmentation; Color Block Jam; Screwdom; ad platforms 2026. Segwise. URL not recorded. 2025 to 2026.
51. Player segmentation. devtodev. URL not recorded. 2025.
52. ARPDAU and D7 ROAS guides. playio. URL not recorded. 2026.
53. Royal Match continue pricing. fungies.io. URL not recorded. 2025.
54. Monetization summaries. AdReact and Gamigion. URL not recorded. 2025.
55. Block Blast A/B tests; Monopoly Go loot box ads. MobileGamer.biz. URL not recorded. 2025 to 2026.
56. Color Block Jam revenue. Insightrackr. URL not recorded. 2025.
57. CPC key principles on in-game virtual currencies. European Commission and CPC network via Mondaq, Baker McKenzie and Reed Smith. URL not recorded. 2025-03-21.
58. CPC letters to game companies. PocketGamer.biz. URL not recorded. 2025.
59. CPC action on Star Stable. Scottish Legal News. URL not recorded. 2025-03.
60. Digital Fairness Act status. Lewis Silkin, privacylaws, digitalfairnessact.com. URL not recorded. 2026-01 to 2026-10.
61. DSA Art. 28 minors guidelines. Osborne Clarke. URL not recorded. 2025-07.
62. Belgium and Netherlands loot boxes. SBC News; Raad van State 202005769. URL not recorded. 2018 and 2022.
63. ECA Digital (Law 15.211/2025). Demarest. URL not recorded. 2025 to 2026.
64. ASA and CAP enforcement notice on loot boxes. ASA; Lewis Silkin. URL not recorded. 2026-02-26 and 2026-02-27.
65. Loot box principles. DCMS and Ukie via CMS. URL not recorded. 2023.
66. FTC v Epic Games. Hunton. URL not recorded. 2022.
67. Genshin Impact settlement. FTC blog. URL not recorded. 2025-01.
68. COPPA amendments. White & Case. URL not recorded. 2025.
69. App store age laws (Texas SB 2420, Utah). Pearl Cohen, FKKS, Future of Privacy Forum. URL not recorded. 2026.
70. Australian classification of loot boxes. infrastructure.gov.au. URL not recorded. 2024-09-22.
71. CNIL fine on Voodoo. Usercentrics. URL not recorded. 2023.
72. AGCM fine on Apple. Source not recorded. URL not recorded. 2025-12.
73. Turkey Law 7578. Evrensel and NTV. URL not recorded. 2026-04-22.
74. PEGI and paid random items. Lewis Silkin. URL not recorded. 2026-03-18.
75. Odds rules; game mechanics under attack; Ninth Circuit. Fenwick. URL not recorded. 2017 to 2025.
76. Monopoly Go objections and suits. VZBV, New York Attorney General, BBC. URL not recorded. 2025 to 2026.
77. Epic v Apple. Fenwick, The Next Web, Courthouse News. URL not recorded. 2025-12 to 2026-08.
78. Google Play fee changes. Notebookcheck. URL not recorded. 2026.
79. Web shop economics (Xsolla, Stash, Unity webshop business case). Vendors. URL not recorded. 2025 to 2026.
80. The New York Times 10-Q, Q2 2026. SEC. URL not recorded. 2026.
81. Puzzmo Plus; Hearst acquires Puzzmo. Puzzmo; MediaPost. URL not recorded. 2025 to 2026.
82. LinkedIn games help. LinkedIn. URL not recorded. 2026.
