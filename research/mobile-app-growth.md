# Research Dossier: Mobile App Growth (iOS and Android)

> Research pass completed 2026-10-08. Scope: ASO, store experiments, Apple Ads, Google App campaigns, Meta and TikTok app campaigns, app networks, MMPs, SKAdNetwork and AdAttributionKit, ATT, Android privacy, deep linking, onboarding and paywalls, web to app and external purchase rules, app unit economics, creative and policies. Method: official developer news feeds, help centers and court or regulator records first, then vendor data studies with stated samples, then trade press. Evidence labels follow docs/AUTHORING_SPEC.md section 7. Numbers in brackets refer to the Sources list at the end.

## 1. Executive summary

1. Store fees are now set market by market and partly by courts. In the US, Apple has charged zero commission on link out purchases since the 2025-04-30 contempt ruling; the Ninth Circuit (2025-12-11) allowed a cost based fee, Apple proposed 15% / 10% / 5% on 2026-08-13, and the Supreme Court is reviewing the contempt standard (No. 25-1311) [22, 23, 24, 25, 26]. In the EU, Apple's new terms from 2026-10-01 set IAP at 26%, link outs at 15%, alternative in-app payments at 20% and a 5% Core Technology Commission outside the App Store [31, 32, 33]. Google split its fee into a 10% service fee (first $1M and all auto-renewing subscriptions) plus a 5% billing fee for Play Billing from 2026-06-30 in the US, UK and EEA [35].
2. Web to app is mainstream among top grossing subscription apps (FunnelFox: 82% route payments outside the stores, vendor method) but still small in total revenue (RevenueCat: 3.2% of revenue globally, 4.9% in North America), and the one controlled test found the in-app sheet beat web by 7% on take home revenue [62, 64, 67].
3. Apple Ads changed more in 12 months than in the previous five years: Maximize Conversions with target CPA (beta 2025-12, all advertisers 2026-02), multiple ad positions in search results (from 2026-03-03), the Apple Ads Platform API (2026-08) with v5 off on 2027-01-26, and creative assets for Today tab and search ads (fall 2026) [11, 12, 13, 15, 16, 4].
4. The App Store product page gained new surfaces: product page headers and search result assets with an Asset Library and preview tool (live 2026-10-05), 70 custom product pages with organic keywords (2025-10-29), AI generated App Store Tags (WWDC25) and AI review summaries (iOS 18.4) [2, 3, 1, 8, 9].
5. Google Play moved ASO toward AI and clicks: Gemini drafts custom store listings from keyword recommendations, CSV based localization, Play Shorts and Ask Play discovery, Engage SDK content on listings, and store listing experiments moved under Store listings with reported click based metrics from 2026-07 [36, 41, 42].
6. iOS measurement is stable but fragmented. WWDC26 brought no notable AdAttributionKit or SKAN changes; AAK adoption by networks remains uneven and poorly documented; SKAN 4 remains the workhorse [5, 6, 50, 51].
7. ATT is being redesigned by regulators: Apple will ship an alternative ATT prompt with iOS 27.2 in the EU, mandatory in Germany, France, Italy, Poland and Romania, with a re-ask allowed after one year; opt-in averaged 38% among users shown the prompt in Q1 2026 (Adjust) [17, 18, 19, 47].
8. Google retired Privacy Sandbox on Android; its status page lists the Android APIs as "Deprecate and remove" (2026-08-14). GAID and Play Install Referrer remain the Android basis [44, 45].
9. The vendor landscape consolidated around ML networks and measurement: AppsFlyer raised $1B+ from Moloco, Google, Meta and Unity (2026-06), Unity shut ironSource Ads direct demand (2026-04-30), Liftoff listed on Nasdaq (2026-06), AppLovin opened Axon self-serve (2026-06), and official MCP servers arrived from RevenueCat, AppsFlyer and Singular [56, 75, 76, 77, 78, 57, 58, 59, 60].
10. Monetization benchmarks moved: median hard paywall install to paid by D35 fell from 12.1% to 10.7%, long trials convert at 42.5% vs 25.5% for short ones, weekly plans earn 55.5% of subscription revenue in Adapty's data, and AI apps earn 41% more per user but retain worse [62, 63, 65].

## 2. State of the channel in 2026 (with numbers)

| Indicator | Value | Source |
|-----------|-------|--------|
| Global consumer IAP spend 2025 (App Store and Google Play) | $167B, +10.6%; non-game apps passed games for the first time (about $85B, +21%); game IAP +1.3% | Sensor Tower State of Mobile 2026 [68, 69] [Study, 2026-01] |
| Global downloads 2025 | About 149B, +0.8%; game downloads about -7% | Sensor Tower [68] [Study, 2026-01] |
| Time spent in apps 2025 | About 5.3 trillion hours, +3.8% | Sensor Tower [68] [Study, 2026-01] |
| Generative AI apps 2025 | IAP above $5B (more than tripled); ChatGPT $3.4B IAP | Sensor Tower [68] [Study, 2026-01] |
| Installs and sessions 2025 | Installs +10%, sessions +7% (2024: +8%, +2%); gaming CPI +30% to $0.56 median; finance sessions +21%; ecommerce installs -10% | Adjust Mobile App Trends 2026 [70] [Study, 2026-02] |
| Gaming ad spend H1 2026 | +8% to $7B, impressions +14% | Sensor Tower via Pocketgamer.biz [71] [Study, 2026] |
| ATT opt-in (users shown the prompt) | 38% all apps Q1 2026 (35% Q1 2025); gaming 39% | Adjust [47, 48] [Study, 2026-03] |
| Subscription apps dataset | 115k+ apps, $16B revenue (RevenueCat); 16k+ apps, $3B+ (Adapty) | [62, 65] [Study, 2026] |
| Subscription revenue concentration | Top 10% of apps take 95% of revenue (92.7% in 2023) | Adapty via PPC Land [66] [Study, 2026] |
| Web share of subscription revenue | 3.2% global, 4.9% North America; 41% of top revenue tier apps have web revenue | RevenueCat [62, 63] [Study, 2026-03] |
| Apple Ads search results economics (2025 data) | TTR 9.7%, average CPT $2.25 (top 15 categories), average CPA $3.76 (SplitMetrics); CPA $2.51 (MobileAction); median CPT $0.92 global, $1.91 US; CR 56% (AppTweak) to 62% (Adapty) | [52, 53, 54, 55] [Study, 2026] |
| MMP market | AppsFlyer about $500M ARR and 15,000+ brands; valuation $2.7B post money after a $1B+ Series E | Axios and analysts [56] [Official CEO comment, 2026-06] |
| Unity Vector | Q2 2026 revenue $546M (+24%); Vector above $1B annual run rate | Earnings via coverage [79] [Official, 2026-08] |
| AppLovin | Q2 2026 revenue $1.92B (+53%); Axon self-serve open since 2026-06 | Earnings via coverage [77] [Official, 2026-08] |

Reading: growth is shifting from games to non-game subscriptions and AI apps; iOS signal is limited but stable; payment routing and store fees are the biggest structural change for unit economics since 2021.

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Impact | Evidence |
|------|--------|--------|----------|
| 2025-01-23 | Apple Advanced Commerce API for large catalogs and add-ons | Creator and catalog apps | [Official, 1] |
| 2025-02-14 | South Korea: extra consent for free to paid trials and discounted offers | Trial flows in Korea | [Official, 1] |
| 2025-02-17 | EU App Store removes apps without DSA trader status | EU distribution | [Official, 1] |
| 2025-03 | iOS 18.4: AI review summaries; AAK configurable windows, cooldown, country code, conversion tags | Ratings and attribution | [Official, 1, 5, 9] |
| 2025-03 (end) | France fines Apple 150 million euros over ATT | ATT redesign pressure | [Official regulator via coverage, 19] |
| 2025-04 | Apple Search Ads renamed Apple Ads; Apple Ads registers with AAK | Naming, attribution | [Practitioner via Singular, 51] |
| 2025-04-30 | Epic v. Apple contempt ruling: no fees or restrictions on US link outs | US web checkout | [Official court record via coverage, 22, 26] |
| 2025-05-01 | Apple guidelines 3.1.1, 3.1.1(a), 3.1.3 updated for the US storefront | Buttons and links to web purchases allowed | [Official, 1, 27] |
| 2025-05-02 | Spotify and Kindle ship purchase links and buttons | Proof of link out route | [28] |
| 2025-05 | RevenueCat IAP vs web test (Dipsea): web $0.93 per $1.00 IAP | Web checkout caution | [Study, 64] |
| 2025-06-09 | WWDC25: App Store Tags, AAK updates, Declared Age Range API, guideline updates | ASO and measurement | [Official, 1, 5, 8] |
| 2025-06-26 | Apple EU DMA terms: external offers with new fees; plan to move to Core Technology Commission | EU economics | [Official, 1] |
| 2025-06 | Google announces end of Play Instant apps (December 2025) | Use deep links instead | [Official via heise, 46] |
| 2025-07 | Custom product pages appear in organic search with assigned keywords (vendor dated) | ASO | [Practitioner; Official notice 2025-10, 1] |
| 2025-07-24 | Apple age ratings add 13+, 16+, 18+; answers due 2026-01-31 | Submission blocker | [Official, 1] |
| 2025-07-31 | Ninth Circuit upholds Epic v. Google injunction | Google US changes | [Official court, 39] |
| 2025-08-14 | Google: tROAS for iOS App campaigns, expanded on-device measurement | iOS value bidding | [Official, 90] |
| 2025-08-25 | Firebase Dynamic Links shut down | Broken legacy links | [Official, 85] |
| 2025-10-01 | AppLovin Axon self-serve opens by referral | New buying route | [Official via coverage, 77] |
| 2025-10 | TikTok Smart+ rebuilt as a modular flow (App included) | TikTok app buying | [Official via tiktok-ads package] |
| 2025-10-17 | Google retires most Privacy Sandbox technologies | No Android Sandbox migration | [Official via coverage, 45] |
| 2025-10-22 | UK CMA designates Apple and Google with strategic market status | UK steering path | [Official, 36] |
| 2025-10-29 | Apple: 70 custom product pages with keywords, offer codes for all IAP types, independent In-App Event submission | ASO and offers | [Official, 1] |
| 2025-11-13 | Apple Mini Apps Partner Program (15%); guidelines 4.7 and 5.1.2(i) | Mini apps, AI disclosure | [Official, 1] |
| 2025-11-17 | Apple price equalization for Türkiye, Poland, Switzerland | Prices | [Official, 1] |
| 2025-12-05 | Apple Ads Maximize Conversions beta spotted | Bidding | [Practitioner, 13] |
| 2025-12-09 | Google Play US alternative billing and external content links programs | US Android payments | [Official, 37] |
| 2025-12-10 | Australia under 16 social media rules | Age gates | [Official, 1] |
| 2025-12-11 | Ninth Circuit affirms Apple contempt, allows cost based commission, remands | Future US fee | [Official court via coverage, 26] |
| 2025-12-17 | Apple Japan changes under MSCA (iOS 26.2) | Alternative marketplaces and payments in Japan | [Official, 1] |
| 2025-12-21 | Official AppsFlyer MCP server listed (beta) | AI data access | [Official listing, 58] |
| 2025-12-22 | Italy fines Apple about 98.6 million euros over ATT | ATT redesign | [Official regulator via coverage, 19] |
| 2025-12-23 | Texas SB2420 implementation paused by injunction | Age assurance | [Official, 1] |
| 2026-01-21 | TikTok Auto-select creative launches on Smart+ App | Creative selection | [Official via tiktok-ads package] |
| 2026-01-22 | Apple details more App Store search ads from March | Organic tap share | [Official via coverage, 11] |
| 2026-01-31 | Apple age rating answers deadline; Unity Ads in-app bidding only | Submissions, monetization | [Official, 1, 75] |
| 2026-02 | Apple Ads Maximize Conversions available to all advertisers; CPA caps to be phased out | Bidding | [Official and Practitioner, 12, 13] |
| 2026-02-13 | Meta "automation unification": Advantage+ default for App campaigns | Meta app buying | [Official via coverage, 73] |
| 2026-02-24 | Apple age requirements for Brazil, Australia, Singapore, Utah, Louisiana (Declared Age Range API beta) | Age gates | [Official, 1] |
| 2026-03-03 | Multiple ad positions in App Store search results start (UK, Japan; all markets by end of March; iOS 26.2+) | Apple Ads reach, organic share | [Official via coverage, 11] |
| 2026-03-15 | China storefront commission 25% and 12% | China economics | [Official, 1] |
| 2026-03-25 | App Store Connect: 100+ new IAP and subscription metrics, cohorts, peer benchmarks | Analytics | [Official, 1] |
| 2026-03-26 | Unity announces ironSource Ads direct demand sunset; Apple IAP promo codes end; medical device declaration notice | Networks, offers, compliance | [Official, 1, 75] |
| 2026-03 | RevenueCat State of Subscription Apps 2026 | Benchmarks | [Study, 62] |
| 2026-03-31 | App Store metadata in 50 languages (+11) | Localization | [Official, 1] |
| 2026-04-01 | CMA commitments from Apple and Google take effect | UK app review fairness | [Official, 36] |
| 2026-04-02 | Apple: Campaign Management API v5 to sunset 2027-01-26; Singular ROI Index 2026 | API migration, network ranking | [Official via coverage, 15; Study, 80] |
| 2026-04-27 | Apple monthly subscriptions with 12-month commitment (iOS 26.4, not US or Singapore) | Pricing | [Official, 1] |
| 2026-04-28 | iOS 26 SDK required for uploads | Release planning | [Official, 1] |
| 2026-04-30 | ironSource Ads direct demand ends; advertisers moved to Unity Vector | Network mix | [Official, 75, 76] |
| 2026-05-19 | Google I/O: Gemini listing tools, Play Shorts, Ask Play, Engage SDK on listings, 60 day recovery, new metrics | Play ASO and churn | [Official, 41] |
| 2026-06-04 | Texas SB2420 in effect for new Texas Apple Accounts; Liftoff IPO priced at $23 | Age gates; networks | [Official, 1; 78] |
| 2026-06-08 | WWDC26: creative assets for App Store and Apple Ads, Asset Library, Retention Messaging, Bundles and Suites, Time Allowances; no notable AAK changes | ASO, retention, measurement | [Official, 3; Practitioner, 6] |
| 2026-06-18 | Apple Brazil changes (iOS 26.5): alternative marketplaces and payments | Brazil economics | [Official, 1] |
| 2026-06-22 | AppsFlyer $1B+ Series E from Moloco, Google, Meta, Unity reported | MMP neutrality | [Official CEO comment via Axios, 56] |
| 2026-06-24 | Google billing choice in UK and EEA and fee split effective 2026-06-30 | Android economics | [Official, 35] |
| 2026-06-30 | Supreme Court grants cert in Apple v. Epic; CMA proposes steering conduct requirements | US and UK link outs | [Official via coverage, 24; 36, 38] |
| 2026-06 | AppLovin Axon open sign-ups | New advertisers on AppLovin | [Official via coverage, 77] |
| 2026-07-09 | Apple age rating questionnaire adds social media capability question (required 2026-09) | Submissions | [Official, 1] |
| 2026-07-10 | Play store listing experiments: new click based metric data start (reported) | Play testing | [Contested, 42] |
| 2026-07-15 | Epic and Google withdraw settlement motion; Google keeps complying with the 2024 order | US Android payments | [Practitioner via docket coverage, 40] |
| 2026-07-22 | Google notice: US program transaction reporting and fees from 2026-10-01 | US Android payments | [Official snippet, 37] [Contested] |
| 2026-08-13 | Apple proffers 15% / 10% / 5% link out commissions; Justice Kagan denies stay | US web checkout | [Official court via coverage, 23] |
| 2026-08-14 | Apple Ads Platform API SDKs published (reported); Privacy Sandbox status page updated | API, Android | [Practitioner, 16; Official, 44] |
| 2026-08-17 | Bundeskartellamt closes ATT case with commitments | EU ATT prompt | [Official regulator via coverage, 19] |
| 2026-08-18 | Apple EU terms announced, effective 2026-10-01 | EU economics | [Official, 31, 32] |
| 2026-08-25 | Apple Maps ads launch in the US and Canada | Local advertisers | [Official via coverage, 14] |
| 2026-08-31 | Google Play target API 36 required (extension to 2026-11-01) | Release planning | [Official, 43] |
| 2026-09-14 | Apple merits brief at the Supreme Court; Moloco rebrand | US fee timeline; networks | [24; 78] |
| 2026-09-16 | Apple alternative ATT prompt in the EU from iOS 27.2; iOS 27 subscription features | ATT, monetization | [Official, 1, 17] |
| 2026-09-30 | Android developer verification starts in 4 countries; Kochava MCP connectors; Play program rate cards; Google fee split in Australia | Distribution, tooling, fees | [Official, 43; 59; 35] |
| 2026-10-01 | Apple EU terms effective; Google US program reporting and fees per Help | Economics | [Official, 31, 37] |
| 2026-10-05 | App Store creative assets and Asset Library live; TikTok Ad Network GA in the US | ASO, TikTok | [Official, 2; 74] |
| Upcoming | 2026-10-22 Apple Volume Purchasing; 2026-10-23 iPhone Duo; 2026-11-13 Epic brief due; 2026-12-31 Google fee split Japan and Korea; 2027-01-26 Apple Ads API v5 off; 2027-04 iOS 27 SDK and iPhone Duo screenshots required | Planning | [Official, 1, 15, 24, 35] |

## 4. Best practice consensus

1. Revenue truth from server side subscription events (RevenueCat, Adapty or backend) with store notifications; attribution tools are secondary [Practitioner consensus].
2. ASO before paid: keyword map across name, subtitle and keyword field (iOS) or title, short and full description (Play); first three screenshots carry the outcome; one change at a time [Practitioner consensus; Official field rules].
3. Custom product pages and custom store listings per ad theme and keyword cluster (Apple 70, Google 50) [Official].
4. Apple Ads: Brand, Category, Competitor and Discovery campaigns with exact match, cross-negatives and weekly search term harvest; judge keywords on downstream revenue [Practitioner consensus].
5. Google App campaigns: install volume first, then tCPA on an event with at least 10 users per day, then tROAS at 10 conversions per day or 300 in 30 days; budgets at 50x tCPI or 10x tCPA; changes under 20% [Official].
6. Meta and TikTok app campaigns: separate OS campaigns, about 50 events per week per ad set, creative volume as the main lever [Official thresholds, Practitioner consensus].
7. SKAN 4 and AAK through the MMP SDK; schemas that encode value within 48 hours; consolidation to protect crowd anonymity tiers [Official mechanics, Practitioner consensus].
8. ATT after the first value moment with an honest pre-prompt; no incentives; no fingerprinting [Official rules].
9. Universal links and App Links on your own domain; Firebase Dynamic Links replaced; deep link QA every release [Official, Practitioner consensus].
10. Paywall tests on net revenue per install with refunds as guardrail; trial length and plan mix tested per category [Study context from RevenueCat and Adapty].
11. Incrementality via geo holdouts and brand keyword tests before scaling on platform ROAS [Practitioner consensus].

## 5. Contested topics

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Screenshot caption OCR indexing on the App Store | ASO vendors dated a ranking shift to 2025-06 and treat captions as indexed [12 Appfigures] | A test of 64 caption phrases found almost none ranked beyond existing metadata; Apple docs list only name, subtitle and keywords; Phiture reports Apple denied OCR [12 Lomio] | Write captions for conversion; ranking value is a bonus, unproven |
| Web checkout vs IAP | FunnelFox: web LTV beats in-app; vendors report fee savings [67] | RevenueCat controlled test: web trial start 18.1% vs 27.0%, $0.93 per $1.00; Adapty (via Airbridge) finds web LTV about $4 lower after fees [64] | Test per app and plan; judge on net revenue per paywall view |
| Google US program fees from 2026-10-01 | Google Help states reporting and fees start 2026-10-01 [37] | One analysis says fees remain switched off and no Google page shows the date [37 snippet] | Enrolled developers confirm in Play Console now; model both |
| Play store listing experiment metrics | Yellowhead and Phiture: unique install and open clicks replaced first-time installers from 2026-07; single variant; AI declaration [42] | Help Center pages still describe retained first-time installers and up to 3 variants | Check the dropdown in the live console |
| AAK and SKAN 4 adoption by networks | Some guides say Meta sends AAK postbacks and SKAN 4 is baseline | Others say most platforms behave like SKAN 3 and Google has not documented AAK; Kochava survey shows negligible AAK traction [50, 51] | Implement both; verify per network from postbacks |
| Apple Ads Maximize Conversions for deep funnel apps | Apple: automated per query bidding at target CPA, weekly average [12] | Practitioners: install only optimization chases cheap installs; not a CPA cap replacement [13] | Use on uniform quality CATEGORY campaigns; manual elsewhere |
| Short vs long trials | Short trials are growing (46.5% of trials) and convert faster | Long trials convert at 42.5% vs 25.5% [62] | Test; category dependent (Adapty shows trials hurt some categories) |
| Hard paywall vs freemium | Hard paywall converts 5x better by D35 | Year-one retention nearly identical; freemium suits habit products [62] | Choose by product habit loop; test |
| MMP neutrality | AppsFlyer: investors get no preferential treatment [56] | Commentators: measured platforms owning equity raises neutrality questions [56 coverage] | Keep raw exports and independent tests |
| MMM calibration with lift priors | Meta led practice: calibrate MMM with experiments | 2026 preprint: a single lift prior discards time structure; calibration polarizing [Admiral, Sellforte coverage] | Use tests as calibration, not as the only truth |
| Apple Ads custom creative availability | WWDC26 guide: creative assets appear in Apple Ads Today tab and search [3] | One source says Apple Ads custom creative not in the 2026-10-05 release | Check the Apple Ads UI |
| CPA cap removal timing in Apple Ads | Adapty: Maximize Conversions replaced CPA caps in 2026-02 | Apple: caps "will soon be unavailable" [12] | Plan migration; verify date |

## 6. What top operators do differently

| Average | Top 1% |
|---------|--------|
| Optimizes CPI and installs | Optimizes net revenue per install by D7 and D30 and payback, by OS and market |
| Treats ASO as a launch task | Runs a weekly ASO loop, PPO calendar, CPP portfolio with keywords and localization waves |
| Lets Apple Ads Search Match and broad terms mix with exact | Exact match architecture with cross-negatives, keyword level revenue joins, brand incrementality tests |
| Copies paywall patterns | Tests placement, plan default, trial length and price per storefront tier with revenue metrics |
| Sets SKAN once | Validates schema against Android and consented cohorts monthly; consolidates campaigns |
| Uses an MMP dashboard as truth | Triangulates MMP, SAN, SKAN, backend and geo holdouts; writes calibration factors |
| Builds web funnels for the fee saving | Models fees per market and plan, measures net revenue per paywall view, keeps IAP as control |
| Asks for reviews randomly | Prompts after success moments, replies to every low rating within 72 hours, mines reviews for angles |
| Ships creative monthly | Ships concepts weekly, maps each to a store page, registers every asset |
| Reacts to policy changes | Keeps a freshness calendar of court dates, store deadlines (target API, SDK minimums) and regulator decisions |

## 7. Common expensive mistakes

1. Scaling paid UA on installs while the paywall converts under 2% and payback never arrives.
2. Sending full annual price as revenue at trial start to value bidding.
3. Counting Apple Ads brand installs as incremental when the app already ranks first organically.
4. Maximize Conversions on deep funnel apps without keyword level revenue checks.
5. SKAN schemas that encode day 3+ behavior in window 1 values.
6. Fragmented iOS campaigns that push SKAN postbacks below crowd thresholds.
7. App Links verified with the upload key instead of the Play App Signing key.
8. Legacy Firebase Dynamic Links in QR codes and emails after 2025-08-25.
9. Web funnels modeled on zero Apple US fees without a scenario for an approved fee.
10. External purchase links shown on storefronts that do not allow them.
11. Screenshot and ad claims outside the claims registry; misleading gameplay ads.
12. Missing target API 36 (2026-08-31) or SDK minimum deadlines, blocking updates.
13. Gating rating prompts by sentiment or incentivizing reviews (policy and FTC rule).
14. Using v5 based Apple Ads scripts or MCP servers past 2027-01-26.

## 8. Benchmarks (source, date, sample, caveat)

| Metric | Value | Source and date | Sample | Caveat |
|--------|-------|-----------------|--------|--------|
| Install to paid by D35, hard paywall median | 10.7% (12.1% prior year); top decile 38.7% | RevenueCat SOSA 2026, 2026-03 [62] | 115k+ apps, $16B revenue, 2025 data | RevenueCat customers; descriptive |
| Install to paid by D35, freemium median | 2.1% | Same | Same | Same |
| Download to trial by D30 | 9.1% Business, 4.4% Gaming medians | Same | Same | Category definitions |
| Trial to paid by trial length | 42.5% (17 to 32 days) vs 25.5% (4 days or less) | RevenueCat 2026 and trial length study 2026-09 [62, 63] | 17,000+ apps for trial study | Selection effects |
| Year-one retention, annual plans | 27% hard paywall, 28% freemium | RevenueCat 2026 [62] | Same | |
| AI apps vs non-AI | +41% revenue per user; annual retention 21.1% vs 30.7% | RevenueCat 2026 [62] | Same | Secondary summaries differ on churn figure |
| Share reaching MRR thresholds | 17.3% reach $1K, 4.6% reach $10K | RevenueCat 2026 [62] | Same | New apps |
| Weekly plan share of revenue | 55.5% (43.3% two years earlier); Utilities 73.6% weekly; Health and Fitness 60.6% annual | Adapty 2026 [65, 66] | 16k+ apps, $3B+, mostly App Store | Adapty customers |
| 12-month LTV weekly plan with vs without trial | $54.50 vs $7.40 | Adapty 2026 [65] | Same | Category mix |
| Trial starts and purchases on day 0 | 90% of trial starts; 44.5% of purchases | Adapty 2026 [65] | Same | |
| Onboarding paywall with trial conversion | 1.35% average | Adapty 2026 [65] | Same | Denominator differs from RevenueCat |
| Web vs IAP (controlled) | Trial start 18.1% web vs 27.0% IAP; trial to paid 26.3% vs 25.0%; $0.93 web per $1.00 IAP | RevenueCat, 2025-05 [64] | One app (Dipsea) | Single test |
| ATT opt-in among users shown prompt | 38% all apps Q1 2026; gaming 39%; publications 26%; ecommerce 34%; India gaming 51%; Europe 36%; North America 33% | Adjust 2026-03 [47, 48] | Adjust data | Denominator: prompt shown |
| ATT opt-in (AppsFlyer framing) | 50% headline; 40% users who see the prompt; 30% broader base | AppsFlyer 2025-04 [49] | AppsFlyer data | Not comparable to Adjust |
| Retention all apps | D1 about 26%, D7 about 13%, D30 about 7%; iOS 27/14/8, Android 24/11/6 | Adjust retention guide [72] | Adjust | Undated, older; 2026 category tables not verified |
| LATAM retention 2025 | D1 16%, D7 about 5%, D30 about 1% | Adjust LATAM 2026 via PPC Land [104] | Regional | Not comparable to global |
| Apple Ads search results TTR | 9.7% | SplitMetrics 2026 [52] | SplitMetrics clients, 2025 | Average |
| Apple Ads CPT | Average $2.25 top 15 categories; Sports $14.41, Finance $6.06; median $0.92 global, $1.91 US | SplitMetrics, AppTweak 2026 [52, 54] | Client data | Median vs average |
| Apple Ads CPA (install) | $3.76 (SplitMetrics), $2.51 (MobileAction; $2.76 in 2024) | 2026 reports [52, 53] | Client data | Methods differ |
| Apple Ads conversion rate | 56% (AppTweak median), 62% (Adapty, 90 countries), 66.2% (SplitMetrics via secondary) | 2026 [52, 54, 55] | | |
| Apple Ads Search tab TTR | 0.29% vs 7.40% search results | AppTweak via Sonar 2026 [105] | | Placement mix |
| US Apple Ads CPT Q2 2026 | Health and Fitness about $1.50, Games $3.02, Finance $3.80, Sports about $16.96 | SplitMetrics 2026-07 [52] | | Quarter specific |
| Gaming CPI 2025 | $0.56 median, +30% | Adjust 2026-02 [70] | Adjust | Global median, genre mix |
| Google Play involuntary churn with 60 day recovery | Up to 18% lower involuntary churn, 9% lower total churn for top developers | Google I/O 2026 [41] | Top developers | Google reported |
| Store search share of downloads | Nearly 65% of App Store downloads happen directly after a search | Apple via coverage 2026-01 [11] | Apple | Apple claim |

## 9. Tools, APIs and MCP servers

| Category | Official | Community or third party | Notes |
|----------|----------|--------------------------|-------|
| App Store Connect | App Store Connect API, Analytics Reports API, App Store Server API, Retention Messaging API (fall 2026) | topcheer App Store Connect MCP (1,200+ operations), zelentsov-dev/asc-mcp, forgeopslabs/appstore-mcp, yuraist/appstoreconnect-mcp, trialanderrorinc analytics server [81, 82] | Use role scoped keys; writes are G2 or G3 |
| Google Play | Play Developer API, Play Developer Reporting API | AgiMaulana google-play-mcp, wiseappsai/play-console-mcp (read only flag), @blocktopus/mcp-google-play, mikusnuz/app-publish-mcp, quartz-labs pabal [83, 84] | Service account scopes |
| Apple Ads | Apple Ads Platform API (2026-08), Campaign Management API v5 (off 2027-01-26), AdServices | AppVisionOS/apple-search-ads-mcp (v5), andrealufino/aapl-ads-mcp (v5, read only), crevas/Apple-Ads-CLI (Platform API) [15, 16, 86, 87] | Migrate v5 tools |
| MMPs | AppsFlyer MCP (beta, read and query), Singular MCP, Adjust MCP (early access, contested), MMP REST APIs | Kochava StationOne connectors for Adjust, AppsFlyer, Branch, Singular (2026-09-30) [58, 59, 60, 61] | Prefer read only |
| Subscriptions | RevenueCat MCP (cloud), RevenueCat REST v2 and webhooks | Superwall, Adapty APIs | RevenueCat MCP can change store prices: G3 [57] |
| Ad platforms | Google Ads API (AppTopCombinationView v23.2), Meta Marketing API, TikTok API for Business and MCP | | See channel packages |

## 10. Official sources to monitor

| Source | URL | Cadence |
|--------|-----|---------|
| Apple Developer News | https://developer.apple.com/news/ | Weekly |
| App Store Connect release notes | https://developer.apple.com/help/app-store-connect/release-notes/ | Weekly |
| App Review Guidelines | https://developer.apple.com/app-store/review/guidelines/ | On each Apple guideline notice |
| Apple Ads news and help | https://ads.apple.com/news | Weekly |
| AdAttributionKit documentation | https://developer.apple.com/documentation/adattributionkit | Monthly and at WWDC |
| User Privacy and Data Use | https://developer.apple.com/app-store/user-privacy-and-data-use/ | Monthly (EU ATT) |
| Android Developers Blog | https://developer.android.com/blog | Weekly |
| Play Console Help policy updates | https://support.google.com/googleplay/android-developer | Monthly |
| Google Play Policy Center | https://play.google.com/about/developer-content-policy/ | Monthly |
| Google Ads Help, App campaigns | https://support.google.com/google-ads/answer/14104492 | Monthly |
| Privacy Sandbox status | https://privacysandbox.google.com/overview/status | Quarterly |
| Android developer verification | https://developer.android.com/developer-verification | Monthly until global rollout |
| Epic v. Apple docket | https://www.courtlistener.com/docket/17442392/epic-games-inc-v-apple-inc/ | Biweekly |
| Epic v. Google docket | https://www.courtlistener.com/docket/17443962/epic-games-inc-v-google-llc/ | Monthly |
| UK CMA mobile platforms | https://www.gov.uk/guidance/the-cmas-programme-of-work-across-mobile-platforms | Monthly |
| RevenueCat changelog | https://www.revenuecat.com/changelog | Monthly |

## 11. Open questions and watch list

1. Final US Apple link out fee (district court remand) and the Supreme Court outcome in No. 25-1311 (argument not expected before 2027-01).
2. Whether Google is actually invoicing US program fees and download fees from 2026-10-01 and 2026-12-01.
3. iOS 27.2 public release date, final EU ATT prompt wording, and opt-in effects in Germany, France, Italy, Poland and Romania.
4. Apple EU Attachment 14 details: 12 month payment choice lock in, marketplace waivers, Commission's formal DMA compliance decision.
5. UK CMA steering decision and fee framework (late 2026).
6. Play store listing experiments: confirmed metrics and variant limits.
7. Apple Ads: CPA cap removal date, custom creative in Apple Ads UI, Maximize Conversions for deeper events, ad position reporting fields.
8. AAK adoption by Meta, Google and TikTok; any SKAN deprecation signal (none found as of 2026-10).
9. Adjust MCP general availability; neutrality debates after AppsFlyer funding; Moloco IPO.
10. Google rest of world fee phase in to 2027-09 and Japan and Korea fee split on 2026-12-31.
11. Android developer verification behavior in the four launch countries and the 2027 global rollout.
12. Age assurance laws spreading to more US states and countries; App Store Accountability style laws.
13. Türkiye: outcomes of the Rekabet Kurulu investigations into Apple (opened 2024-05-21) and Google Play billing (opened 2025-08-07).
14. Whether screenshot text affects App Store ranking (Apple has not documented it).

## 12. Sources

1. Apple Developer News (2025 to 2026 items). Apple. https://developer.apple.com/news/. 2025-01 to 2026-10.
2. Showcase your apps with new assets on the App Store. Apple. https://developer.apple.com/news/?id=ljpl7kyn. 2026-10-05.
3. WWDC26 App Store guide. Apple. https://developer.apple.com/wwdc26/guides/app-store/. 2026-06.
4. Manage your App Store assets. Apple App Store Connect Help. https://developer.apple.com/help/app-store-connect/manage-app-information/manage-your-app-store-assets/. 2026-10.
5. What's new in AdAttributionKit (WWDC25). Apple. https://developer.apple.com/videos/play/wwdc2025/221/. 2025-06.
6. WWDC26: updates for mobile marketers. Adjust. https://www.adjust.com/blog/WWDC-26/. 2026-06.
7. Meet AdAttributionKit (WWDC24). Apple. https://developer.apple.com/videos/play/wwdc2024/10060/. 2024-06.
8. At WWDC, Apple says it will use AI to tag apps. TechCrunch via Yahoo Finance. https://finance.yahoo.com/news/wwdc-apple-says-ai-tag-181733246.html. 2025-06.
9. iOS 18.4 beta introduces AI powered review summaries. Macworld. https://www.macworld.com/article/2628166/ios-18-4-beta-introduces-ai-powered-review-summaries-in-the-app-store.html. 2025-03.
10. App Review Guidelines. Apple. https://developer.apple.com/app-store/review/guidelines/. Accessed 2026-10.
11. The App Store is getting even more ads in March 2026. AppleInsider. https://appleinsider.com/articles/26/01/22/the-app-store-will-have-even-more-ads-in-march-2026-starting-with-the-uk. 2026-01-22.
12. Maximize Conversions best practices. Apple Ads. https://ads.apple.com/app-store/best-practices/maximize-conversions. 2026.
13. Apple Ads introduces Maximize Conversions. MobileAction. https://www.mobileaction.co/blog/maximize-conversions/. 2025-12.
14. Apple Maps launches ads on iPhone. 9to5Mac. https://9to5mac.com/2026/08/25/apple-maps-launches-ads-on-iphone-heres-whats-new/. 2026-08-25.
15. Apple details plan to sunset Ads Campaign Management API in 2027. 9to5Mac. https://9to5mac.com/2026/04/02/apple-details-plan-to-sunset-ads-campaign-management-api-in-2027/. 2026-04-02.
16. Apple Ads Platform API debuts as old API faces 2027 shutdown. PPC Land. https://ppc.land/apple-ads-platform-api-debuts-as-old-api-faces-2027-shutdown/. 2026-08.
17. iOS 27.2 will apply an alternative App Tracking Transparency system prompt in the EU. AplWire. https://www.aplwire.com/2026/09/16/ios-27-2-will-apply-an-alternative-app-tracking-transparency-system-prompt-in-the-eu/. 2026-09-16.
18. Changes to App Tracking Transparency in the E.U. Daring Fireball. https://daringfireball.net/linked/2026/09/23/changes-to-app-tracking-transparency-in-the-eu. 2026-09-23.
19. 5 EU countries lose Apple's standard tracking prompt for a redesigned one. PPC Land. https://ppc.land/5-eu-countries-lose-apples-standard-tracking-prompt-for-a-redesigned-one/. 2026-09.
20. User Privacy and Data Use. Apple. https://developer.apple.com/app-store/user-privacy-and-data-use/. 2026-09.
21. Apple Ads: understand invoices. Apple Ads Help. https://ads.apple.com/app-store/help/billing/0088-understand-invoices. Accessed 2026-10.
22. Apple's fight over commissions for linked out App Store purchases continues in federal court. Courthouse News. https://www.courthousenews.com/apples-fight-over-commissions-for-linked-out-app-store-purchases-continues-in-federal-court/. 2026.
23. Apple proposes commissions of up to 15% for off-App Store purchases in the US. 9to5Mac. https://9to5mac.com/2026/08/13/apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us/. 2026-08-13.
24. App Store commission limbo enters new phase as Apple's Epic merits brief opens SCOTUS fight. Tech Times. https://www.techtimes.com/articles/327527/20260915/app-store-commission-limbo-enters-new-phase-apples-epic-merits-brief-opens-scotus-fight.htm. 2026-09-15.
25. High Court grants cert in Apple's challenge to Ninth Circuit contempt ruling. IPWatchdog. https://ipwatchdog.com/2026/06/30/high-court-grants-cert-in-apples-challenge-to-ninth-circuit-contempt-ruling-in-app-store-dispute/. 2026-06-30.
26. Ninth Circuit largely upholds ruling in Epic v. Apple. Fenwick. https://www.fenwick.com/insights/publications/ninth-circuit-largely-upholds-ruling-in-epic-v-apple. 2025-12.
27. App Review Guidelines updated for Epic anti-steering. Michael Tsai. https://mjtsai.com/blog/2025/05/02/app-review-guidelines-updated-for-epic-anti-steering. 2025-05-02.
28. Spotify external links app update approved. 9to5Mac. https://9to5mac.com/2025/05/02/spotify-external-links-app-update-approved/. 2025-05-02.
29. Apple Inc. Form 10-Q for the quarter ended 2026-06-27. SEC. https://www.sec.gov/Archives/edgar/data/0000320193/000032019326000020/aapl-20260627.htm. 2026-08.
30. Epic Games v. Apple docket 4:20-cv-05640. CourtListener. https://www.courtlistener.com/docket/17442392/epic-games-inc-v-apple-inc/. Ongoing.
31. Apple announces changes for apps in the European Union. Apple Newsroom. https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/. 2026-08-18.
32. Apple overhauls its EU App Store fees, loosens rules for alternative app stores. TechCrunch. https://techcrunch.com/2026/08/18/apple-overhauls-its-eu-app-store-fees-loosens-rules-for-alternative-app-stores/. 2026-08-18.
33. Apple's new EU App Store fees: what changed for subscription apps. RevenueCat. https://www.revenuecat.com/blog/growth/apple-eu-app-store-fees. 2026-08.
34. Apple's new EU App Store terms take effect October 1: the full rate card. The Mac Observer. https://www.macobserver.com/news/eu-app-store-terms-october-1-rate-card/. 2026.
35. Expanded billing choice and lower fees on Google Play. Android Developers Blog. https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play. 2026-06-24.
36. The CMA's programme of work across mobile platforms. UK Competition and Markets Authority. https://www.gov.uk/guidance/the-cmas-programme-of-work-across-mobile-platforms. 2026.
37. An update regarding Google Play's policies for developers serving users in the US. Play Console Help. https://support.google.com/googleplay/android-developer/answer/15582165. 2025 to 2026.
38. UK agency wants Apple and Google to steer customers to more payment options. MacTech. https://www.mactech.com/2026/06/30/uk-agency-wants-apple-and-google-to-steer-customers-on-app-stores-to-more-payment-options/. 2026-06-30.
39. Epic Games v. Google opinion (Ninth Circuit). US Court of Appeals for the Ninth Circuit. https://cdn.ca9.uscourts.gov/datastore/opinions/2025/07/31/24-6256.pdf. 2025-07-31.
40. Why Epic and Google just walked away from their own settlement. Stash. https://www.stash.gg/blog/why-epic-and-google-just-walked-away-from-their-own-settlement. 2026-07.
41. I/O 2026: What's new in Google Play. Android Developers Blog. https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play. 2026-05-19.
42. New Google Play Console metrics for ASO in 2026. Yellowhead. https://www.yellowhead.com/blog/new-google-play-console-metrics-aso/. 2026-08.
43. Target API level requirements for Google Play apps. Android Developers. https://developer.android.com/google/play/requirements/target-sdk. 2026.
44. Privacy Sandbox feature status. Google. https://privacysandbox.google.com/overview/status. 2026-08-14.
45. Google pulls the plug on Topics, PAAPI and other major Privacy Sandbox APIs. AdExchanger. https://www.adexchanger.com/privacy/google-pulls-the-plug-on-topics-paapi-and-other-major-privacy-sandbox-apis-as-the-cma-says-cheerio/. 2025-10.
46. Google to bury Instant Apps at the end of 2025. heise online. https://heise.de/-10447201. 2025-06.
47. ATT opt-in rates. Adjust. https://www.adjust.com/blog/att-opt-in-rates-2025. Updated 2026.
48. Gaming App Insights Report 2026. Adjust. https://a.storyblok.com/f/47007/x/20551740ee/gaming-app-insights-report-2026.pdf. 2026-03.
49. AppsFlyer data shows market adaptation four years after ATT. AppsFlyer. https://www.appsflyer.com/company/newsroom/pr/post-att-growth/. 2025-04.
50. Your iOS attribution strategy in 2026: a reality check. Kochava. https://www.kochava.com/ko/blog/your-ios-attribution-strategy-2026-reality-check/. 2026.
51. Apple Search Ads adds support for SKAdNetwork, AdAttributionKit. Singular. https://www.singular.net/blog/apple-search-ads-skadnetwork-adattributionkit/. 2025-04.
52. Apple Ads cost: how to evaluate CPT, CPA, CR, TTR. SplitMetrics. https://splitmetrics.com/blog/apple-search-ads-cost/. 2026.
53. Apple Ads 2026 benchmark report. MobileAction. https://www.mobileaction.co/report/apple-ads-2026-benchmark-report/executive-summary/. 2026.
54. Apple Ads benchmarks 2026. AppTweak. https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks. 2026.
55. Apple Ads benchmarks 2026 across 90 countries. Adapty. https://adapty.io/blog/apple-ads-benchmarks-2026/. 2026.
56. AppsFlyer raises $1B from Moloco, Google, Meta and Unity. Axios. https://axios.com/2026/06/22/appsflyer-billion-moloco-google-meta-unity. 2026-06-22.
57. RevenueCat MCP Server. RevenueCat. https://www.revenuecat.com/docs/tools/mcp. 2025 to 2026.
58. Official AppsFlyer MCP Server. PulseMCP. https://www.pulsemcp.com/servers/appsflyer. 2025-12-21.
59. Kochava adds workspaces and MCP connectors for Adjust, AppsFlyer, Branch and Singular. GlobeNewswire. https://www.globenewswire.com/news-release/2026/09/30/3372027/0/en/kochava-adds-workspaces-and-mcp-connectors-for-mmp-providers-on-stationone-for-adjust-appsflyer-branch-and-singular.html. 2026-09-30.
60. Singular MCP. Singular. https://support.singular.net/hc/en-us/articles/37923459892507-Singular-MCP. 2025 to 2026.
61. Best MMP MCP servers in 2026. Tenjin. https://tenjin.com/blog/best-mmp-mcp-servers-in-2026-tenjin-appsflyer-singular-adjust-and-airbridge/. 2026.
62. State of Subscription Apps 2026. RevenueCat. https://www.revenuecat.com/state-of-subscription-apps. 2026-03.
63. How long should your free trial be? Data from 17,000+ apps. RevenueCat. https://www.revenuecat.com/blog/growth/free-trial-length. 2026-09.
64. RevenueCat report suggests in-app purchases perform noticeably better than link outs to the web. Daring Fireball. https://daringfireball.net/linked/2025/05/15/revenuecat-external-purchase-report. 2025-05-15.
65. State of In-App Subscriptions 2026. Adapty. https://adapty.io/state-of-in-app-subscriptions-report/. 2026.
66. 95% of app subscription revenue goes to top 10%: Adapty's 2026 benchmark report. PPC Land. https://ppc.land/95-of-app-subscription-revenue-goes-to-top-10-adaptys-2026-benchmark-report/. 2026.
67. State of Web2App 2026. FunnelFox. https://funnelfox.com/state-of-web2app/. 2026.
68. State of Mobile 2026. Sensor Tower. https://sensortower.com/blog/state-of-mobile-2026. 2026-01.
69. Consumers spent more on mobile apps than games in 2025. TechCrunch. https://techcrunch.com/2026/01/21/consumers-spent-more-on-mobile-apps-than-games-in-2025-driven-by-ai-app-adoption/. 2026-01-21.
70. Adjust: mobile app use grew globally in 2025. Business Wire. https://www.businesswire.com/news/home/20260218837408/en/Adjust-Mobile-App-Use-Grew-Globally-In-2025-With-Continued-Move-To-Multi-Platform. 2026-02-18.
71. Mobile gaming IAP dipped 2% as ad spend climbed in H1 2026. Pocketgamer.biz. https://www.pocketgamer.biz/mobile-gaming-iap-dipped-2-as-ad-spend-climbed-in-h1-2026/. 2026.
72. The app user retention handbook. Adjust. https://www.adjust.com/resources/guides/user-retention/. Undated, older.
73. Follow up on the Meta Advantage+ rollout. UA Ledger. https://ualedger.com/blog/posts/follow-up-meta-advantage-plus-rollout. 2026.
74. TikTok opens ad network of nearly 400,000 apps to US advertisers. PPC Land. https://ppc.land/tiktok-opens-ad-network-of-nearly-400-000-apps-to-us-advertisers/. 2026-10.
75. Sunsetting ironSource Ads. Unity. https://unity.com/products/ironsource-ads-sunset. 2026-03.
76. Unity Software Form 10-Q for the quarter ended 2026-06-30. SEC. https://www.sec.gov/Archives/edgar/data/0001810806/000181080626000043/unity-20260630.htm. 2026-08.
77. AppLovin's $1.84B Q1 beats guidance as Axon platform opens to all in June. PPC Land. https://ppc.land/applovins-1-84b-q1-beats-guidance-as-axon-platform-opens-to-all-in-june/. 2026-05.
78. Blackstone backed Liftoff rises after $437 million US IPO. Bloomberg. https://www.bloomberg.com/news/articles/2026-06-04/blackstone-backed-liftoff-rises-9-1-after-437-million-us-ipo. 2026-06-04.
79. Unity reports record Q2 2026 revenue and Vector growth. Outlook Respawn. https://respawn.outlookindia.com/gaming/gaming-news/unity-records-best-q2-2026-revenue-of-546m-via-vector-ai-growth. 2026-08.
80. Singular ROI Index 2026. Singular. https://www.singular.net/roi-index-2026/. 2026-04-02.
81. App Store Connect MCP Server (yuraist). Glama. https://glama.ai/mcp/servers/yuraist/appstoreconnect-mcp. 2026.
82. AppStore MCP Server (forgeopslabs). mcpservers.org. https://mcpservers.org/servers/forgeopslabs/appstore-mcp. 2026.
83. play-console-mcp (wiseappsai). Drio. https://www.getdrio.com/mcp/io-github-wiseappsai-play-console-mcp/md. 2026.
84. google-play-mcp (AgiMaulana). Claude Marketplaces. https://claudemarketplaces.com/mcp/io.github.agimaulana/google-play-mcp. 2026.
85. Firebase Dynamic Links deprecation FAQ. Firebase. https://firebase.google.com/support/dynamic-links-faq. 2023 to 2025.
86. apple-search-ads-mcp. AppVisionOS on GitHub. https://github.com/AppVisionOS/apple-search-ads-mcp. 2026.
87. Apple-Ads-CLI. crevas on GitHub. https://github.com/crevas/Apple-Ads-CLI. 2026.
88. Best practices for App campaigns. Google Ads Help. https://support.google.com/google-ads/answer/14104492. Accessed 2026-10.
89. About Integrated Conversion Measurement for App campaigns. Google Ads Help. https://support.google.com/google-ads/answer/16203286. 2025 to 2026.
90. 3 new ways to unlock iOS App campaign performance. Google. https://blog.google/products/ads-commerce/3-new-ways-to-unlock-ios-app-campaign-performance/. 2025-08.
91. Optimize your app ad. Meta for Developers. https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad. 2024-10.
92. New requirements for value optimization. Jon Loomer. https://www.jonloomer.com/qvt/new-requirements-for-value-optimization/. 2025.
93. Android developer verification. Android Developers. https://developer.android.com/developer-verification. 2026.
94. Google gradually rolling out Android advanced sideloading ahead of developer verification. 9to5Google. https://9to5google.com/2026/08/18/google-gradually-rolling-out-androids-advanced-sideloading-ahead-of-developer-verification/. 2026-08-18.
95. Turkey's competition watchdog launches probe into Apple on limitations over payment systems. Duvar English. https://www.duvarenglish.com/turkeys-competition-watchdog-launches-probe-into-apple-on-limitations-over-payment-systems-news-64466. 2024-06.
96. Google Play payment system competition investigation. Teknoblog. https://www.teknoblog.com/google-play-odeme-sistemi-rekabet-sorusturma/. 2025-08.
97. Incrementality testing for mobile apps. Admiral Media. https://admiral.media/incrementality-testing-mobile-apps/. 2026.
98. Set up Conversion Lift based on geography. Google Ads Help. https://support.google.com/google-ads/answer/14097193. Accessed 2026-10.
99. Lift studies. Meta for Developers. https://developers.facebook.com/docs/marketing-api/guides/lift-studies. Accessed 2026-10.
100. Do app stores read text in your screenshots? Lomio. https://lomio.io/blog/do-app-stores-read-screenshot-text. 2026.
101. The biggest App Store algorithm change is here. Appfigures. https://appfigures.com/resources/guides/app-store-algorithm-update-2025. 2025-06.
102. Life after Firebase Dynamic Links: three paths. Branch. https://www.branch.io/resources/blog/life-after-firebase-dynamic-links-three-paths-to-a-better-deep-linking-stack/. 2025.
103. RevenueCat Web Billing. RevenueCat. https://www.revenuecat.com/billing. 2026.
104. LATAM mobile apps: finance sessions surge 62%, installs grow 13% in 2025. PPC Land. https://ppc.land/latam-mobile-apps-finance-sessions-surge-62-installs-grow-13-in-2025/. 2026.
105. Apple Search Ads cost: CPT, CPI and indie budgets. Sonar. https://trysonar.app/blog/apple-search-ads-cost. 2026-09.
