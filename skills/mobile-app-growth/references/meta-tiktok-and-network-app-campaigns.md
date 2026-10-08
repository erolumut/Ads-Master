# Meta, TikTok and Ad Network App Campaigns

> Knowledge as of 2026-10. Key changes: Meta "automation unification" made Advantage+ the default setup for Sales, Leads and App campaigns (2026-02); TikTok Smart+ App in the upgraded modular flow (2025-10), Auto-select creative first on Smart+ App (2026-01), TikTok Ad Network generally available for US campaigns (2026-10-05); Unity sunset ironSource Ads direct demand (2026-04-30); AppLovin opened Axon self-serve sign-ups (2026-06); Liftoff listed on Nasdaq (2026-06); Moloco rebranded (2026-09) and is reported to be preparing an IPO. Channel depth for Meta and TikTok lives in the meta-ads and tiktok-ads packages; this module covers the app specific layer.

## 1. Meta app campaigns

### 1.1 Setup

| Item | Setting | Evidence |
|------|---------|----------|
| Objective | App promotion | [Official] |
| Campaign setup | Advantage+ app campaign is the default build path; audience, placements and budget automation on by default, each can be toggled off | [Official, 2026-02 via developer notice and secondary] |
| Optimization goal | App installs, App events (for example StartTrial, Purchase, CompleteRegistration), Value | [Official] |
| App events source | Meta SDK or MMP (AppsFlyer, Adjust, Branch, Singular, Kochava) sending events to the app dataset in Events Manager | [Official] |
| iOS measurement | SKAdNetwork through the SDK or MMP plus Aggregated Event Measurement (AEM) for apps; Meta developer docs still describe up to 8 prioritized conversion events for apps, while other sources say AEM was automated for web in 2025 | [Official, 2024-10 docs] [Contested on current AEM limits] |
| AdAttributionKit | One 2026 guide says Meta sends AAK postbacks alongside SKAN; not confirmed in Meta docs | [Unverified] |
| Learning | About 50 optimization events per ad set in 7 days, otherwise "Learning limited" | [Official, Meta developer docs] |
| Value optimization eligibility | Reported: at least 30 attributed purchase events with at least 5 distinct values in 14 days (100 for non-purchase events) | [Practitioner consensus via Jon Loomer and Airbridge, verify in the Help Center] |
| Creative enhancements | On by default for new campaigns since 2026-02; review each toggle for claims risk | [Practitioner consensus, 2026-02] |

### 1.2 Structure

- Separate iOS and Android campaigns: blended campaigns let the cheaper OS absorb budget on a metric that hides value [Practitioner consensus].
- Starter and Growth: one Advantage+ app campaign per OS, optimize to install until the bid event reaches 50 per week per ad set, then App events.
- Scale: App events with cost per result goal set from trailing actuals; Value optimization (ROAS goal) for games and apps with real purchase values.
- Do not split into many small ad sets on iOS: SKAN privacy thresholds redact conversion values at low volume per source identifier [Practitioner consensus].
- New winning concepts go in a new ad set or ad when the delivery concentrates on 1 to 2 creatives [Practitioner consensus].

### 1.3 Web to app on Meta

Subscription apps commonly run Meta Sales campaigns to a web funnel (quiz, paywall, checkout) with Pixel plus Conversions API events (StartTrial, Purchase with value), then hand users to the app via deep link or redemption link. Benefits: no SKAN thresholds, richer signal, web checkout economics (see [Deep linking and web to app](deep-linking-and-web-to-app.md)). FunnelFox's 2026 report, based partly on Meta Ads Library parsing, says 82% of top grossing mobile apps route subscriptions or payments outside the stores [Study, 2026, vendor method]. Hand pixel and CAPI work to measurement.

## 2. TikTok app campaigns

| Item | Detail | Evidence |
|------|--------|----------|
| Objective | App promotion: app installs, in-app events (AEO), value (VBO), app retargeting | [Official] |
| Smart+ App | Upgraded modular flow; each module (targeting, budget, placement, creative) can be automated or manual | [Official, 2025-10] |
| Auto-select creative | Recommends the strongest existing ads and eligible TikTok One creator content; Smart+ App first (2026-01) | [Official, 2026-07] |
| Placements | Smart+ App on iOS: TikTok and Lemon8; on Android includes TikTok Ad Network | [Official, Help Center via tiktok-ads package] |
| TikTok Ad Network (formerly Pangle) | Nearly 400,000 apps; generally available for US campaigns from 2026-10-05 as the 48th market | [Official, 2026-10] |
| Measurement | TikTok uses a self attributing network (SAN) model for app measurement with per ad group click, engaged view and view windows; iOS through SKAdNetwork via the MMP | [Official, 2023 to 2025] |
| Learning | About 50 conversions per ad group per week; budget at least 10x target CPA | [Official per tiktok-ads package] |
| Creative | App store screenshots perform poorly; use creator led screen recordings, gameplay and native hooks | [Official guidance + Practitioner consensus] |

Path: install, then AEO when the in-app event reaches about 50 per week per ad group, then VBO. Judge TikTok Ad Network on D7 retention and ROAS, not CPI (strong for gaming installs, weaker for subscription quality [Practitioner consensus]). For account level work (Spark Ads, creators, Smart+ settings), hand off to tiktok-ads.

## 3. Other self attributing and social networks

| Network | Use for apps | Notes |
|---------|-------------|-------|
| Snapchat Ads | App installs and events for 13 to 34 audiences | In Singular ROI Index 2026 core group [Study, 2026-04] |
| X Ads | App installs in some verticals | In Singular core group [Study, 2026-04] |
| Reddit Ads | Niche communities, app installs | Test cell only; verify current app optimization options [Unverified] |
| Apple Ads | Highest intent iOS search | See [Apple Ads](apple-ads.md) |

## 4. Programmatic and app networks (high level)

| Network | Strengths | 2025 to 2026 facts | Evidence |
|---------|-----------|--------------------|----------|
| AppLovin (AppDiscovery, Axon) | Games, rewarded and playable inventory across MAX mediated apps, ROAS bidding | Axon Ads self-serve launched by referral 2025-10-01 and opened to public sign-ups in 2026-06, mainly aimed at web and ecommerce advertisers; Q2 2026 revenue $1.92B (+53%) | [Official earnings via coverage, 2026-08] |
| Unity Ads (Vector) | Games, Unity ecosystem inventory | Unity sunset ironSource Ads (iAds) direct demand on 2026-04-30; advertisers moved to Unity Ads on Vector; ironSource Exchange programmatic and LevelPlay mediation continue; Unity Ads network supports in-app bidding only from 2026-01-31 | [Official, 2026-03 to 2026-08] |
| Mintegral | Playables, APAC strength, games | In Singular core group | [Study, 2026-04] |
| Liftoff (with Vungle) | ML DSP for apps, gaming and non-gaming | IPO priced at $23 on 2026-06-04 (Nasdaq: LFTO) | [Official filing via coverage, 2026-06] |
| Moloco | ML DSP for apps, expanding to CTV and retail media | Rebrand 2026-09; reported IPO preparation with banks (2026-02); minority investor in AppsFlyer (2026-06) | [Official newsroom + Bloomberg, 2026] |
| Digital Turbine, OEM stores (Samsung, Xiaomi, Huawei, Honor) | Android preloads and on-device recommendations | Quality varies; measure retention | [Practitioner consensus] |

Neutrality note: AppsFlyer took minority investments from Moloco, Google, Meta and Unity in a reported $1B+ Series E (2026-06) [Official CEO statement via Axios]. When an MMP is part owned by networks it measures, keep raw postback and cost exports and run your own incrementality tests.

## 5. Protocol to test a new network or DSP

1. Prerequisites: MMP integration active (attribution and cost), fraud suite on, SKAN or AAK conversion schema live, deep links working, creative pack ready (portrait and landscape video, end cards, playable if gaming, static interstitials).
2. Commercials: CPI, CPA or ROAS bidding; minimum spend; payment terms; transparency on publisher IDs (site IDs) and SKAN source app reporting.
3. Test budget: enough for at least 100 bid event conversions or 2 to 4 weeks at the target CPA; put it in EXPERIMENTS.md with a stop rule.
4. KPIs: cost per payer or D7 ROAS vs the account baseline on Meta and Google; IPM; D1 and D7 retention; share of installs flagged as fraud; publisher concentration.
5. Fraud checks: click to install time (CTIT) distribution (very short CTIT suggests injection, very long suggests click spamming), installs per publisher with near zero retention, new device and emulator rates, abnormal click volumes.
6. Publisher management: blocklist losers weekly; allowlists only at Scale tier.
7. Incrementality: run a geo holdout or the network's ghost bid test before scaling past 15% of spend.
8. Decision: scale, hold or stop; log the learning.

## 6. Incentivized and rewarded traffic

- Offerwalls and rewarded installs can drive engaged users for some games but distort store ranking signals and attract low quality users for most apps.
- Store rules forbid manipulating charts, search, reviews or referrals (Apple Developer Code of Conduct, Discovery Fraud 5.6.3; Google Play Store listing and promotion policy) [Official]. Never buy installs to move rank.
- Judge on D7 and D30 revenue per install, not CPI.

## 7. Creative requirements by channel (summary)

| Channel | Must have | Notes |
|---------|-----------|-------|
| Meta | 9:16 video, 1:1 and 4:5 static or video, multiple concepts, playable (optional) | Advantage+ creative toggles reviewed |
| TikTok | 9:16 native video with sound, creator content, Spark Ads | Hand off creators to tiktok-ads |
| AppLovin, Unity, Mintegral, Liftoff, Moloco | Portrait and landscape video (15 to 30 seconds), end cards, HTML5 playables (MRAID), interstitial statics | Playables decide gaming performance |
| Google App campaigns | Text, images, portrait, square and landscape video, HTML5 | See [Google App campaigns](google-app-campaigns.md) |

See [App creative](app-creative.md) for briefs and testing.

## 8. Weekly reconciliation

| Source | What it says | Bias |
|--------|-------------|------|
| SAN dashboards (Meta, Google, TikTok, Snap, Apple Ads) | Platform attributed installs and events | Over-credit, view-through, modeled conversions |
| MMP last touch | Deduplicated attribution across networks | Under-credits view and upper funnel; iOS gaps without ATT |
| SKAN and AAK postbacks | Privacy preserving iOS installs and coarse or fine values | Delayed, thresholded, limited values |
| RevenueCat or backend | Real revenue and subscriptions | Truth for money, weak on source |
| Geo or lift tests | Incremental effect | Slow, costly, the only causal read |

Rule: decisions use a triangulated range (MMP, SAN, SKAN modeled, backend), calibrated by tests. Write both platform and calibrated numbers in every report.

## 9. Launch procedure: Meta app campaign

1. Prerequisites: app registered and linked to the ad account and the app dataset; Meta SDK or MMP sending install and bid events with values; SKAN configuration through the SDK or MMP; iOS and Android store IDs verified.
2. Create PAUSED (G2): App promotion objective, Advantage+ app campaign, one per OS, optimization to installs (or the bid event if it already reaches about 50 per week).
3. Creative: 6 to 10 ads across 3 to 5 concepts, 9:16 video first, captions, Advantage+ creative enhancements reviewed one by one.
4. Budget: enough for about 50 optimization events per week (for example cost per event $8 needs about $57 per day).
5. Activation change list (G3); hands off for 7 days except for broken tracking or policy issues.
6. Week 2 onward: creative kill and scale per meta-ads rules; move to app events optimization when volume allows.

## 10. Launch procedure: TikTok app campaign

1. Prerequisites: app added in Events Manager with the MMP integration (SAN), in-app events mapped, iOS SKAN handled by the MMP.
2. Create PAUSED: App promotion, Smart+ App or manual, one per OS; iOS placements limited to TikTok and Lemon8 in Smart+ App.
3. Creative: 4 to 6 native videos for Smart+ App, creator voiceover, real UI.
4. Budget: at least 10x target CPA per ad group per day and a path to about 50 conversions per week.
5. Optimize install first, then AEO on the bid event, then VBO for value; consider TikTok Ad Network as a separate tested cell on Android and for games.

## 11. Diagnostics for social and network app campaigns

| Symptom | Likely causes | Checks | Fixes |
|---------|--------------|--------|-------|
| Spend concentrates on Android or low ARPU countries | Blended campaign, broad geo | Spend and revenue by OS and country | Split campaigns, adjust geo |
| Installs fine, bid events missing on iOS | SKAN value mapping, SDK version, consent | MMP SKAN report, event logs | Fix schema and SDK |
| Network installs with near zero D1 retention | Fraud or misleading creative | CTIT, publisher IDs, creative review | Blocklist publishers, replace creative, claim refunds through the MMP fraud process |
| Learning limited | Too few events per ad set | Events per 7 days | Consolidate, shallower event, budget |
| CPI rises across all social | Creative fatigue, seasonality, auction | IPM and CTR trend, CPM | New concepts, accept seasonal CPM |

## 12. Budget split example (Growth tier subscription app, $20k per month)

| Channel | Share | Reason |
|---------|-------|--------|
| Apple Ads | 35% | Highest intent iOS demand; keyword level revenue visibility |
| Meta (iOS and Android app campaigns plus web funnel test) | 40% | Volume and creative learning |
| Google App campaigns (Android first) | 20% | Android scale and Play search |
| Test cell (TikTok or one network) | 5% | Next channel learning |

This is an illustrative split [Practitioner consensus]; the real split comes from marginal cost per payer by channel and the growth-orchestrator budget plan.
