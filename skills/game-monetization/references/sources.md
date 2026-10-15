# Sources (annotated)

> Compiled 2026-10-12 from the ten Game Studio research notes (monetization design, ad tech, user acquisition, analytics, store presence, regulation, teardowns, web distribution, Apple review, Google Play review). Apple's App Review Guidelines and several developer.apple.com and developer.android.com pages were opened and read; every other source was seen only as a search result summary or a vendor page. "Path from the notes" means the notes recorded a domain and path but not a full link: open it before relying on it. "URL not recorded" means the notes named the publisher only. Vendor studies have commercial interests and non random samples. The research narrative and the verification queue are in `research/game-monetization.md`, which uses the same numbering.

How to read the "Supports" column: it names the claims a source backs and the label they carry in this skill. A single source never earns more than [Unverified]; an official page seen only as a summary never earns [Official].

## Apple and Google: official pages read at the source

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | App Review Guidelines | Apple Developer | https://developer.apple.com/app-store/review/guidelines/ | Revision 2026-06-08, read 2026-10-12 | 2.1(b) IAP attached to the version; 3.1.1 IAP for digital unlocks and loot box odds before purchase; 3.1.1(a) US storefront link outs without an entitlement; 3.1.2 subscription rules; 3.1.3(b) multiplatform items; 4.2; 4.7 HTML5 mini games; 1.3 and 5.1.4 Kids Category [Official, 2026-10] |
| 2 | Apps in the EU (alternative terms) | Apple Developer | Path from the notes: developer.apple.com/support/apps-in-the-eu | Read 2026-10-12 | EU terms from 2026-10-01: IAP 26% (15%), alternative payment 20% (10%), link out 15% (10%), Core Technology Commission 5% [Official, 2026-10] |
| 3 | Age ratings values | App Store Connect Help | URL not recorded (developer.apple.com/help/app-store-connect) | Read 2026-10-12 | Loot boxes listed in the age rating table (9+ tier; Australia and Brazil higher); 13+, 16+, 18+ tiers; social media question required from September 2026 [Official, 2026-10] |
| 4 | Subscriptions | Apple Developer | Path from the notes: developer.apple.com/app-store/subscriptions | Read 2026-10-12 | Paywall disclosures with 3.1.2 [Official, 2026-10] |
| 5 | Third party SDK requirements | Apple Developer | Path from the notes: developer.apple.com/support/third-party-SDK-requirements | Read 2026-10-12 | Privacy manifests and signatures for listed SDKs including Capacitor and Firebase [Official, 2026-10] |
| 6 | Google Play Billing (and subscriptions) | Android Developers | https://developer.android.com/google/play/billing | Read 2026-10-12 | Billing Library 8 or later by 2026-08-31 (extension to 2026-11-01); cancellation keeps access to the period end; trials charge the full price; resubscribers lose trial eligibility [Official, 2026-10] |
| 7 | Android vitals | Android Developers | https://developer.android.com/topic/performance/vitals | Read 2026-10-12 | Crash 1.09% and ANR 0.47% overall bad behavior thresholds [Official, 2026-10] |
| 8 | Play policies hub | Android Developers | Path from the notes: developer.android.com/distribute/play-policies | Read 2026-10-12 | Child directed apps use certified ad SDKs; anonymous chat apps may not target children since 2026-08-26 [Official, 2026-10] |
| 9 | Trusted Web Activity guide | Android Developers and Chrome Developers | URL not recorded | Read 2026-10-12 | Digital Asset Links must match the Play App Signing key, otherwise browser UI shows [Official, 2026-10] |

## Google Play: search summaries

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 10 | Play expanded billing and fee changes | Android Developers Blog | URL not recorded (android-developers.googleblog.com, 2026/06) | 2026-06 | Fees from 2026-06-30 in the US, EEA and UK: 10% on the first $1M plus 5% with Play Billing; later markets [Reported, 2026-10] |
| 11 | Subscription disclosure requirements | Play Console Help 9900533 | https://support.google.com/googleplay/android-developer/answer/9900533 | Seen 2026-10-12 | Terms, price, frequency, auto renewal and trial conversion disclosed; easy online cancellation [Reported, 2026-10] |
| 12 | Families self certified ads SDK program | Play Console Help 12918983 | Path from the notes: support.google.com, answer 12918983 | Seen 2026-10-12 | Self certified SDKs, child directed treatment, ad content rated G at most [Reported, 2026-10] |

## Web ads and web platforms

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 13 | Ad Placement API (H5 Games Ads) beta docs | Google | Path from the notes: developers.google.cn/ad-placement/docs/beta | Seen 2026-10-12 | Closed beta; `adBreak()` at transitions; rewarded after opt in; grant on the viewed callback [Reported, 2026-10] |
| 14 | H5 games ads policy | Google Publisher Policies | https://support.google.com/publisherpolicies/answer/11975916 | Seen 2026-10-12 | No value outside the game, no money for viewing, no "support us" copy [Reported, 2026-10] |
| 15 | AdSense H5 Games Ads | Google AdSense | URL not recorded | Seen 2026-10-12 | Program status [Reported, 2026-10] |
| 16 | YouTube Playables monetization reference | Google for Developers | Path from the notes: developers.google.com/youtube/gaming/playables/reference/monetization | Seen 2026-10-12 | Ads; revenue share pilot [Reported, 2026-10] |
| 17 | Instant Games rewarded ads and the 2025-07-31 web and Instant Games changes | Meta for Developers | URL not recorded | 2025-07-31 | Audience Network monetization; "Meta Web Games ended 2026-09-30" as recorded [Unverified] |
| 18 | Discord Activities monetization | Discord Developers | Path from the notes: docs.discord.com | Seen 2026-10-12 | Embedded App SDK 2.5.0 (May 2026); SKUs on desktop in the US, UK and EU [Reported, 2026-10]; fee [Contested] |
| 19 | Reddit Devvit Developer Funds | Reddit | URL not recorded | 2025 to 2026 | Up to $167,500 per app; daily games encouraged [Reported, 2026-10] |
| 20 | Telegram Stars | Telegram | URL not recorded | Seen 2026-10-12 | Stars for digital goods bought through store IAP [Reported, 2026-10] |
| 21 | TikTok Growth Max and Mini Games | TikTok for Business | Path from the notes: ads.tiktok.com | 2026-05-13 | Business verification; Growth Max testing [Reported, 2026-10] |
| 22 | WebKit blog posts 13878 (Web Push) and 14112 (badging) | WebKit | URL not recorded | 2023 (iOS 16.4 era) | iOS Web Push for Home Screen web apps only, after a gesture, since 16.4 [Reported, 2026-10] |
| 23 | Web rewarded vendors (AppLixir FAQ, Playgama comparison, Cinevva) | Vendors | URL not recorded | 2026 | Vendor list; US rewarded CPM claims $8 to $28 [Unverified, vendor claim] |

## Portals

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 24 | Poki SDK and deal terms | Poki | Path from the notes: sdk.poki.com | Seen 2026-10-12 | 100% own traffic, 50/50 Poki traffic, web exclusivity, selective [Reported, 2026-10]; exclusivity 5 or 7 years [Contested] |
| 25 | CrazyGames payouts | CrazyGames docs | Path from the notes: docs.crazygames.com/payouts | Seen 2026-10-12 | Basic then Full launch; EUR 100 minimum via Tipalti; split unpublished [Reported, 2026-10] |
| 26 | GameDistribution revenue share | Various | URL not recorded | Seen 2026-10-12 | 33% vs 45% [Contested] |

## Mediation and ad tech

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 27 | AppLovin payments and ad filtering | AppLovin Support | Path from the notes: support.applovin.com | Seen 2026-10-12 | $100 minimum, Net 15; category filters [Reported, 2026-10] |
| 28 | MAX A/B testing and Ad Review | AppLovin Developers | Path from the notes: developers.applovin.com | Seen 2026-10-12 | Built in A/B tests; creative review tool [Reported, 2026-10] |
| 29 | Mediation market share 2025 | PocketGamer.biz | URL not recorded | 2025 | MAX over 50% mediation share [Reported, 2026-10 with 30] |
| 30 | AdMob bidding partners; TCF 2.3 deadline | PPC Land | URL not recorded | 2025-07-07; 2026 | InMobi, ironSource and Unity bidding in AdMob; TCF v2.3 around 2026-03-01 or Limited Ads [Reported, 2026-10] |
| 31 | LevelPlay mediated networks | Unity docs | Path from the notes: docs.unity.com | Seen 2026-10-12 | Networks, Unity Ads Net 60 and $100 [Reported, 2026-10] |
| 32 | AppLovin sues Unity over the Ad Quality SDK | PPC Land, MobileGamer.biz | URL not recorded | 2026-09-29 | Lawsuit ongoing [Reported, 2026-10] |
| 33 | AdMob Help answer 9760862 | Google AdMob | https://support.google.com/admob/answer/9760862 | Seen 2026-10-12 | Cited in the notes for AdMob setup; topic not recorded [Unverified] |
| 34 | eCPM report Q4 2024 | Appodeal | URL not recorded (PDF) | 2025 | Rewarded, interstitial and banner eCPMs by OS [Unverified, vendor report] |
| 35 | US eCPM benchmarks | MonetizeMore | URL not recorded | Undated | US rewarded eCPM by OS [Unverified] |
| 36 | eCPM by region 2026 | playio citing MWM | URL not recorded | 2026 | Regional eCPM ranges [Unverified] |
| 37 | Game ad revenue by platform | Tenjin | URL not recorded | 2026-08 | Q2 2026 split 55% Android, 45% iOS [Unverified, vendor] |
| 38 | ATT opt in rates | AppsFlyer (Q1 2024), Adjust (Q2 2025), Singular (Q2 2024) | URL not recorded | 2024 to 2025 | 51%, 35%, 13.85% [Contested: methods differ] |

## Monetization design, markets and teardowns

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 39 | Naavik digest and Royal Match deep dive | Naavik | URL not recorded | 2021 to 2025 | Pass +31% first 30 days; about $34 lifetime revenue per download; failed x10 reward test [Unverified] |
| 40 | Royal Match teardown; match 3 notes | FoxData | URL not recorded | 2025 | Royal Pass from level 37, 30 steps per month [Unverified] |
| 41 | Royal Match revenue | Business of Apps | URL not recorded | 2025 | About $1.4 billion in 2024 [Unverified] |
| 42 | Royal Match vs Candy Crush; State of Gaming 2026; top 10 June 2025 | Sensor Tower | URL not recorded | 2025 to 2026 | Paid download shares; $82 billion mobile game revenue 2025 [Reported, 2026-10] |
| 43 | Hybrid casual Q1 2025 (AppMagic data); Gybe | Mobidictum | URL not recorded | 2025 | Color Block Jam IAP $25M Q1 2025, early levels nearly ad free [Unverified]; conflict with 56 [Contested] |
| 44 | Top rewarded placements; H1 2026 IAP dip; Royal Kingdom; Rollic | PocketGamer.biz | URL not recorded | 2025 to 2026 | IAP about minus 2% to about $40 billion and game ad spend about plus 8% in H1 2026 [Reported, 2026-10] |
| 45 | Top 5 rewarded placements; interstitial best practices; IAP guide; webshop business case | Unity | URL not recorded | 2024 to 2026 | Interstitial grace, cooldown and caps (repeated elsewhere, [Reported, 2026-10]); multiplier popularity, payer conversion 2% to 5% [Unverified, vendor claim] |
| 46 | Hybrid casual dos and don'ts | Supersonic | URL not recorded | 2025 | Rewarded small and temporary, IAP larger and permanent; 60% IAP works [Unverified, vendor guidance] |
| 47 | Piggy banks | maf.ad; Heroic Labs | URL not recorded | 2025 | Hexa Sort level 7, $4.99, third top IAP; about 40 of the top 100 [Unverified] |
| 48 | Hybrid monetization (2024-12-09); screw puzzle gold rush; Royal Kingdom (2024-07-01) | Deconstructor of Fun | URL not recorded | 2024 | 70/30 and 60/40 hybrids; IAP first out earns ads first about 4x [Unverified] |
| 49 | Sensor Tower ad monetization; AppMagic hybrid casual; GameAnalytics 2025 benchmarks | GameDevReports | URL not recorded | 2025 to 2026 | $12 billion game ad revenue 2025, puzzle and arcade over 65%; D1, D7, D30 medians; session length [Reported, 2026-10] |
| 50 | Segmentation; Color Block Jam; Screwdom; ad platforms 2026 | Segwise | URL not recorded | 2025 to 2026 | No Ads bundle $11.99; Screwdom over $75M IAP 2025 with an interstitial after every level [Unverified] |
| 51 | Player segmentation | devtodev | URL not recorded | 2025 | Percentile cutoffs [Unverified] |
| 52 | ARPDAU and D7 ROAS guides | playio | URL not recorded | 2026 | ARPDAU ranges [Unverified] |
| 53 | Royal Match continue pricing | fungies.io | URL not recorded | 2025 | About 900 coins rising above 2,000 after a second fail [Unverified] |
| 54 | Monetization summaries | AdReact, Gamigion | URL not recorded | 2025 | Interstitial timing patterns [Unverified] |
| 55 | Block Blast A/B tests; Monopoly Go loot box ads | MobileGamer.biz | URL not recorded | 2025 to 2026 | Test volume; loot box ad disclosure [Reported, 2026-10] |
| 56 | Color Block Jam revenue | Insightrackr | URL not recorded | 2025 | $12.1 million per 30 days [Contested with 43] |

## Regulation

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 57 | CPC key principles on in-game virtual currencies | European Commission and CPC network, via Mondaq, Baker McKenzie, Reed Smith | URL not recorded | 2025-03-21 | Real money price, no hidden costs or forced currency purchases, withdrawal rights, protect children; national fines cited up to EUR 800k or 6% [Reported, 2026-10] |
| 58 | CPC letters to game companies | PocketGamer.biz | URL not recorded | 2025 | Letters to ten companies [Reported, 2026-10] |
| 59 | CPC action on Star Stable | Scottish Legal News | URL not recorded | 2025-03 | Ads to children, time pressure, currency information [Reported, 2026-10] |
| 60 | Digital Fairness Act status | Lewis Silkin (2026-01-14), privacylaws, digitalfairnessact.com | URL not recorded | 2026-01 to 2026-10 | Not law; proposal expected Q4 2026 [Reported, 2026-10] |
| 61 | DSA Art. 28 minors guidelines | Osborne Clarke | URL not recorded | 2025-07 | Minors and paid random items, non binding [Reported, 2026-10] |
| 62 | Belgium and Netherlands loot boxes | SBC News; Raad van State 202005769 | URL not recorded | 2018; 2022 | Belgium gambling position; Dutch ruling overturned the KSA fine on EA [Reported, 2026-10] |
| 63 | ECA Digital (Law 15.211/2025) | Demarest | URL not recorded | 2025 to 2026 | Paid loot boxes banned for minors, in force 2026-03 [Reported, 2026-10] |
| 64 | ASA and CAP enforcement notice on loot boxes | ASA (PDF); Lewis Silkin 2026-02-27 | URL not recorded | 2026-02-26 | "Contains loot boxes" prominently; monitoring from 2026-05-26; Kabam and Hutch rulings 2025-11 [Reported, 2026-10] |
| 65 | Loot box principles | DCMS and Ukie, via CMS | URL not recorded | 2023 | Voluntary principles [Reported, 2026-10] |
| 66 | FTC v Epic Games | Hunton | URL not recorded | 2022 | USD 245 million dark pattern refunds, USD 275 million COPPA [Reported, 2026-10] |
| 67 | Genshin Impact settlement | FTC blog | URL not recorded (ftc.gov) | 2025-01 | USD 20 million; no purchases under 16 without parental consent; real cost; odds [Reported, 2026-10] |
| 68 | COPPA amendments | White & Case | URL not recorded | 2025 | Compliance date 2026-04-22 [Reported, 2026-10] |
| 69 | App store age laws (Texas SB 2420, Utah) | Pearl Cohen, FKKS, Future of Privacy Forum | URL not recorded | 2026 | Texas enforceable after the Fifth Circuit stay; Utah duties to 2027-05-06 [Reported, 2026-10] |
| 70 | Australian classification of loot boxes | infrastructure.gov.au | URL not recorded | 2024-09-22 | Paid chance loot boxes rated M or higher, simulated gambling R18+ [Reported, 2026-10] |
| 71 | CNIL fine on Voodoo | Usercentrics | URL not recorded | 2023 | EUR 3 million, identifier used for ads without consent [Reported, 2026-10] |
| 72 | AGCM fine on Apple | Not recorded | URL not recorded | 2025-12 | EUR 98.6 million, double consent [Reported, 2026-10] |
| 73 | Turkey Law 7578 | Evrensel, NTV | URL not recorded | 2026-04-22 | Under 15 social media bar; age rating and parental controls including purchase approval on game platforms; fines; local representative [Reported, 2026-10] |
| 74 | PEGI and paid random items | Lewis Silkin | URL not recorded | 2026-03-18 | PEGI 16 default from 2026-06-01; reclassification from 2026-10-01 [Reported, 2026-10] |
| 75 | Odds rules; game mechanics under attack; Ninth Circuit | Fenwick | URL not recorded | 2017 to 2025 | Apple 2017 and Google 2019 odds rules; Epic v Apple [Reported, 2026-10] |
| 76 | Monopoly Go objections and suits | VZBV (2025-06), New York Attorney General (2026-02), BBC | URL not recorded | 2025 to 2026 | Pop up offers, opaque currencies, absence penalties; paid loot box suit [Reported, 2026-10] |

## Store fees, web shops and daily puzzle subscriptions

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 77 | Epic v Apple | Fenwick, The Next Web, Courthouse News | URL not recorded | 2025-12 to 2026-08 | Ninth Circuit upheld contempt, cost based fee on remand; Supreme Court review 2026-06-30; no rate set as of 2026-08-16 [Reported, 2026-10] |
| 78 | Google Play fee changes | Notebookcheck | URL not recorded | 2026 | External content link install fees $2.85 and $3.65 [Unverified] |
| 79 | Web shop economics (Xsolla, Stash, Unity webshop business case) | Vendors | URL not recorded | 2025 to 2026 | Xsolla about 5%, Stash about 10%; about $0.92 vs $0.70 net; conversion drop up to 45% [Unverified, vendor claim] |
| 80 | The New York Times 10-Q, Q2 2026 | SEC (sec.gov) | URL not recorded | 2026 | 13.35 million subscribers; paywalling The Mini added single product subscribers [Reported, 2026-10] |
| 81 | Puzzmo Plus; Hearst acquires Puzzmo | Puzzmo; MediaPost | URL not recorded | 2025 to 2026 | About $40 a year for archives, leaderboards, no ads [Unverified]; acquisition [Reported, 2026-10] |
| 82 | LinkedIn games help | LinkedIn | URL not recorded | 2026 | Streaks, connection leaderboards, reset at midnight PT [Reported, 2026-10] |

## Internal sources (this repo)

| Source | Supports |
|--------|----------|
| [Monetization contract](monetization-contract.md) v0.1 | Modes, boards, typed grants, the six types, events, policy keys, runbook, conformance test |
| `scripts/monetization-policy.schema.json`, `scripts/monetization_check.py`, `scripts/monetization_conformance.py` and their samples | Structure, mechanical fairness and consumer checks, cross artefact checks |
| The compliance skill (pricing, promotions and consumer law; country notes) | EU withdrawal function SUB-EU-01 from 2026-06-19; EU 30 day and Turkey 10 day price reduction rules; the CPC action of 2026-09-30 on virtual currencies |
| The measurement skill (tracking plan as code; game KPIs) | Tracking plan format and types; metric definitions |
