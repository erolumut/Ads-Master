# Game User Acquisition

> Knowledge as of 2026-10 (research pass 2026-10-12). Apple's AdAttributionKit and EU terms pages were read at the source [Official, 2026-10]; network, CPI and soft launch facts come from search summaries and vendor posts, so they carry [Reported, 2026-10] or [Unverified]. Vendor CPIs are context, never targets. Run the Freshness protocol in SKILL.md before a spend decision rests on any row, and the `ads-verify` skill for [Contested] items.

## 0. Scope and boundary

| Owner | Owns | Reads |
|-------|------|-------|
| `mobile-app-growth` (this module) | Per install economics: CPI, cost per payer, D0, D7, D30 ROAS by campaign, payback, net revenue per install; channel choice, bidding sequence, budgets, soft launch traffic | Curves and gates from `measurement` |
| `game-monetization` | Per DAU and per placement economics: ARPDAU split, impressions per DAU, eCPM by placement, payer conversion, ARPPU, offers | Install cohorts from here |
| `measurement` | Every definition and the curves themselves ([Game KPIs](../../measurement/references/game-kpis.md)); SKAdNetwork and AdAttributionKit implementation ([Game tracking](../../measurement/references/game-tracking.md)) | |
| `game-liveops` | Retention programs, events, difficulty signals for the game repo | Cohort quality by source |
| `creative-strategy`, `video-studio` | Game ad concepts, testing stages, playables and trailers ([Game ad creative](../../creative-strategy/references/game-ad-creative.md), [Playable ads and game trailers](../../video-studio/references/playable-ads-and-game-trailers.md)) | IPM, CPI and D7 ROAS by creative from here |
| The game's own repo | How the game plays (rules, levels, difficulty) | Never changed from here |

Every number in a UA deliverable uses the definitions in [Game KPIs](../../measurement/references/game-kpis.md) and names its source, date range, OS and markets. No spend, launch, bid or budget change happens without a G3 change request.

## 1. When a game is ready to buy traffic

| Gate | Evidence | Who reads |
|------|----------|-----------|
| Tracking passes the release gate | [Game tracking](../../measurement/references/game-tracking.md) section 9; MMP with ad revenue; SKAN and AAK schema live | measurement |
| Retention curve exists | Closed beta or organic cohorts above the minimum size, classic D1 and D7, by source | measurement |
| Monetization proven to exist | ARPDAU split and payer conversion from real players, not a model | game-monetization |
| Store page converts | Product page conversion read by `app-store-optimization`; gameplay first screenshots and preview | app-store-optimization |
| Representative ads | Every concept passes the representativeness test in [Game ad creative](../../creative-strategy/references/game-ad-creative.md) section 1 | creative-strategy, compliance |
| Payback target written | `PROJECT_BRIEF.md` section 3 with the horizon (casual 90 to 180 days, midcore 180 to 365 days, [App growth model](app-growth-model-and-unit-economics.md) section 4.3) | human with growth-orchestrator |

A game that fails a gate buys only test traffic (soft launch, section 4), never scale.

## 2. Networks and fit

| Channel | Fit for games | Optimization path | Notes and evidence |
|---------|---------------|-------------------|--------------------|
| AppLovin (AppDiscovery, AXON) | Default first for casual and hybrid casual; rewarded and playable inventory across MAX mediated games | CPI, then CPE events, then ROAS | One vendor puts its share of iOS ad revenue at 39% in Q1 2026 [Unverified, vendor claim]; network facts in [Meta, TikTok and networks](meta-tiktok-and-network-app-campaigns.md) section 4 |
| Unity Ads (Vector) | Casual and Unity built games | CPI, then ROAS | Playable installs about $0.60 vs video about $2.50 on Android [Unverified, vendor claim]; ironSource Ads demand sunset 2026-04-30 (section 4 of the networks module) |
| Mintegral | Playables, localized creatives, APAC strength | tROAS available | [Reported, 2026-10] |
| Moloco | ML DSP, scaling after the first networks | CPI, ROAS | [Reported, 2026-10] |
| Liftoff (Accelerate) | Games and apps DSP | CPI, CPA, ROAS | [Reported, 2026-10]; listed on Nasdaq in 2026-06 (networks module section 4) |
| Meta Advantage+ app campaigns | Broad reach, cheap creative screening, event and value optimization | Install, app event, value | About 50 optimization events per ad set per 7 days to exit learning [Reported, 2026-10]; account depth in `meta-ads` |
| Google App campaigns | Android scale, YouTube and Play surfaces | Installs (tCPI), in-app action (tCPA), then tROAS | tROAS needs about 30 to 50 weekly events or about 300 historical conversions; sources conflict [Contested]; budgets 50x tCPI, 10x tCPA ([Google App campaigns](google-app-campaigns.md)) |
| TikTok (Smart+ App, TikTok Ad Network) | Gameplay video, younger audiences, demand testing | Install, event, value | iOS game CPI about $2 to $3.50 [Unverified, vendor claim] |
| Apple Ads | Intent from search, brand defense, category terms | CPT or Maximize Conversions | Median games CPI $4.63 (AppTweak, about 2025-07) [Reported, 2026-10] |

No network publishes a minimum budget for games [Reported, 2026-10]; ask the account manager in writing and record it in memory. Start with 1 to 2 channels; add one network at a time with the test protocol in [Meta, TikTok and networks](meta-tiktok-and-network-app-campaigns.md) section 5.

## 3. The bidding sequence: install, event, ROAS

| Step | Bid on | Move to the next step when | Watch |
|------|--------|----------------------------|-------|
| 1 | Installs (tCPI, CPI bids) | The creative and audience produce installs at a CPI the curve can pay back and D1 by source is readable | Cheap installs that churn: read D1 by campaign before scaling |
| 2 | An in-app event that predicts value: tutorial complete, level N, D1 return, first purchase, ad impression count | The event fires often enough for the platform floor (Meta about 50 per ad set per week; Google 10x tCPA budget) and correlates with D7 revenue in your cohorts | Choose the event from `measurement`'s correlation read, not by habit |
| 3 | Value (tROAS, value optimization), with IAP and ad revenue both sent | Volume clears the platform threshold and value postbacks include ad revenue | Too few events: tROAS starves [Reported, 2026-10, common pitfall] |

Rules:
1. Never start at ROAS on a new game: there is no history to learn from.
2. Send ad revenue to the networks through the MMP before ROAS bidding on a hybrid or ads first game; otherwise the network optimizes for payers only.
3. Bid targets move 10% to 20% per step, from trailing actuals, never from the aspiration (laws in SKILL.md).
4. Split iOS and Android campaigns; iOS value arrives through SKAdNetwork and AdAttributionKit with delay and buckets (section 6).

## 4. Soft launch: markets, traffic and gates

### 4.1 Markets

| Market | Why studios use it | Evidence |
|--------|--------------------|----------|
| Canada | English, behavior close to the US, cheaper traffic | [Reported, 2026-10] |
| Australia, New Zealand | English, tier 1 payers, smaller auctions | [Reported, 2026-10] |
| Philippines | Cheap installs, English, retention read before monetization | [Reported, 2026-10] |
| Nordics | High payers, cheaper than the US | [Reported, 2026-10] |
| Your launch markets' language | Localization test | Practitioner consensus |

Run 1 to 3 markets at a time [Reported, 2026-10]. For a game made for one market (Turkish language, local culture), soft launch in that market with a small budget instead; a proxy market tells you nothing about a local game. Royal Match soft launched in the UK and Canada in July 2021 [Reported, 2026-10].

### 4.2 Traffic design

1. Buy the traffic mix you will scale with: the same channels, the same creative style, the same OS split. A soft launch fed by one cheap network predicts nothing about global scale [Reported, 2026-10, common pitfall].
2. Size: each gate needs a pooled mature cohort of at least 1,000 installs ([Game KPIs](../../measurement/references/game-kpis.md) section 10); about 15,000 users for stable data is reported [Reported, 2026-10]. Budget = installs needed x expected CPI x (1 + 30% buffer).
3. Timing: D7 reads need 7 days after the last cohort day; D30 needs about 60 days for a 30 day install period.
4. One change at a time between soft launch cohorts (build, economy, onboarding), each with a new cohort and an `EXPERIMENTS.md` row.
5. Keep organic and paid cohorts apart in every table.

### 4.3 Gates

The gates come from the game's own curve and archetype, never copied from a blog: [Game KPIs](../../measurement/references/game-kpis.md) section 9 (procedure, rules of thumb, GameAnalytics medians, the daily social game case). `game_kpis.py --gates` gives PASS, FAIL or CANNOT JUDGE. This module adds the economic gate:

```
LTV needed at the payback horizon = expected CPI at scale x (1 + margin buffer)
D7 LTV needed                     = LTV needed / (LTV horizon / LTV D7 from own cohorts)
D7 ROAS target                    = D7 LTV needed / CPI
```

Worked example (illustrative inputs, not benchmarks): expected iOS CPI at scale $2.00, buffer 20%, own curve LTV D180 / LTV D7 = 4.0. LTV needed at D180 = $2.40; D7 LTV needed = $0.60; D7 ROAS target = 30%. A soft launch at 18% D7 ROAS fails the economic gate even if D1 passes; the fix is monetization or retention (`game-monetization`, `game-liveops`), not bids.

Reported anchors for context only: D7 ROAS 15% to 40% for IAP heavy games and about 7% to 8% for ad monetized games [Reported, 2026-10]; casual D30 ROAS 47% iOS and 15% Android in 2024 [Reported, 2026-10, Liftoff and Singular]; break even ROAS on gross revenue = 1 / share kept (70% kept gives 1.43x) [Reported, 2026-10].

### 4.4 Decision table

| Result | Decision | Change request |
|--------|----------|----------------|
| Retention and economic gates PASS outside the interval | Scale step: budget +20% to 30% per week per channel while CPI and D7 ROAS hold (default heuristic, tune per account) | G3 budget change |
| Gates PASS inside the interval | Hold; buy more installs at the same mix | G3 test budget |
| Retention FAIL | Stop paid scale; hand off to `game-liveops` and the game repo | Pause (G3) |
| Economic FAIL with retention PASS | Hand off to `game-monetization`; keep a small test budget | G3 test budget |
| Two to three iterations without moving the failing gate | Kill or re-concept: the human decides with `growth-orchestrator` | |

## 5. Creative testing and playables

Owned by `creative-strategy` and `video-studio`; this module runs the paid side.

| Stage | Metric | This module's job |
|-------|--------|-------------------|
| Concept screen | Hook rate, 3 second views | Small reach budget only |
| Install efficiency | IPM or CTR | Run on the channel that will scale the winner |
| Cost and quality | CPI at the target geo, D1 by creative | Read D1 by creative only as a red flag at 300 installs or more |
| Value | D7 ROAS | Finalists on event or value bidding |

Facts that shape the plan: video is about 80.9% of game creatives [Unverified, vendor claim]; video to playable hybrids are reported as the fastest growing format [Unverified, vendor claim]; playable fatigue in 7 to 10 days [Unverified, vendor claim]; 85.4% of top playables carry a tutorial prompt [Unverified, vendor claim]; test several end cards [Reported, 2026-10]. Agencies screen 50 to 200 variants a week [Unverified]; a small studio screens 2 to 8 concepts a week sized by budget ([Game ad creative](../../creative-strategy/references/game-ad-creative.md) section 6).

The non negotiable: ads show gameplay a new player meets early. The UK ASA ruled against Playrix (2020-09-30), Rivergame and AppQuantum (2022) and Top Games' Evony (2024) for ads that did not show the core game, and disclaimers did not cure it [Reported, 2026-10]. A creative whose D1 sits 10 points under the account median is a compliance flag before it is a performance problem.

Coordinate a CPP or custom store listing per winning theme with `app-store-optimization`; buy only into pages that show the same gameplay.

## 6. SKAdNetwork and AdAttributionKit for games

The schema and implementation live with `measurement` ([Game tracking](../../measurement/references/game-tracking.md) section 6; the template is the same as [Mobile measurement](mobile-measurement-skan-aak-mmp.md) section 5.2). What UA must do:

1. Consolidate campaigns and ad groups so postbacks stay above crowd anonymity thresholds; many small iOS campaigns null the fine value.
2. Ask every network which framework it uses and verify from postbacks; AdAttributionKit coverage by network is uneven ([Mobile measurement](mobile-measurement-skan-aak-mmp.md) section 4).
3. AdAttributionKit lets the app set shorter attribution windows per network and per click or view, and an attribution cooldown; postbacks can carry a country code at enough volume [Official, 2026-10]. Agree window settings with each network before changing them; a change moves reported installs between networks.
4. Read iOS ROAS from postbacks as delayed and bucketed; compare with Android and consented iOS cohorts before cutting an iOS campaign.
5. Re-engagement campaigns for lapsed players can use AdAttributionKit re-engagement and, from iOS 18.4, overlapping conversions with conversion tags [Official, 2026-10].

## 7. Web shops and the open Epic v Apple fee

A web shop sells the same items outside the store's billing (US link outs, EU link outs, Android external offers). The fees and rules move monthly; the per market table lives in [Deep linking and web to app](deep-linking-and-web-to-app.md) section 4 and the fee math in [App growth model](app-growth-model-and-unit-economics.md) section 3.

| Fact | Status | Evidence |
|------|--------|----------|
| US storefront: links and buttons to web purchases allowed without an entitlement (Guideline 3.1.1(a)) | Live | [Official, 2026-10] |
| US link out commission | Zero today while litigated: the Ninth Circuit upheld contempt in December 2025 and allowed a cost based fee on remand; rehearing denied March 2026; the Supreme Court agreed on 2026-06-30 to review; no rate set as of 2026-08-16 | [Reported, 2026-10] [Contested]; treat 0% as temporary |
| EU from 2026-10-01: link out to web purchases | 15% (10% for Small Business, Mini Apps and Video Partner programs and subscriptions after year one) on sales within 7 days of the link tap | [Official, 2026-10] |
| EU: Apple IAP | 26% (15% programs and subscriptions after year one) | [Official, 2026-10] |
| Google Play US external content links | A per install fee for games of $3.65 ($2.85 for apps) within 24 hours of the link is reported | [Contested] |
| Web shop net per $1 | About $0.92 vs $0.70 through the store | [Unverified, vendor claim] |
| Conversion leaving the app | Can drop up to 45% | [Unverified, vendor claim] |
| Direct to consumer game sales | About $17B, about 15% of mobile game IAP | [Unverified, vendor claim] |
| Web shop providers | Xsolla about 5%, Stash about 10% | [Unverified, vendor claim] |

Decision rule: a web shop pays only if web conversion stays above (in-app net take rate / web net take rate) of in-app conversion ([App growth model](app-growth-model-and-unit-economics.md) section 3.2), modeled per market with a non zero US fee scenario. Test it (in-app vs link out cohorts) before moving offers; the store purchase sheet often converts better. Price parity and currency display rules are in [IAP price points](../../pricing-strategy/references/iap-price-points.md); claims about "cheaper on the web" go to `compliance`.

## 8. CPI benchmarks (context only)

| Segment | CPI | Source | Label | Caveat |
|---------|-----|--------|-------|--------|
| Global blended, gaming, 2025 | $0.56, +30% year over year | Adjust 2026 via FoxData | [Reported, 2026-10] | Blend of genres, countries and networks |
| Tier 1, Q1 2026, hypercasual | iOS $0.85, Android $0.42 | FoxData | [Unverified, vendor claim] | Ranges elsewhere conflict |
| Tier 1, Q1 2026, RPG | iOS $8.70, Android $5.10 | FoxData | [Unverified, vendor claim] | Same |
| Casual, 2025 | iOS $1.41, Android $0.14 | Liftoff casual report | [Reported, 2026-10] | Liftoff network data |
| Apple Ads, games, median | $4.63 | AppTweak, about 2025-07 | [Reported, 2026-10] | Search intent traffic, brand terms included |
| TikTok, iOS games | About $2 to $3.50 | Vendor blog | [Unverified, vendor claim] | Undated range |
| Unity Ads, Android, playable vs video | About $0.60 vs $2.50 | Vendor blog | [Unverified, vendor claim] | Creative mix |

Re-check by 2027-04. Use own trailing CPI by channel, OS and country for every plan; these rows only tell you whether a quote is unusual.

## 9. Organic and community channels

| Channel | Use for games | Evidence |
|---------|---------------|----------|
| TikTok organic | Demand test for hooks before paid stage 0 | [Reported, 2026-10] |
| Reddit | Feedback from genre communities; developer funds for daily games on Reddit's own platform | [Reported, 2026-10] |
| YouTube | Showcase and creators | [Reported, 2026-10] |
| Discord | Community and retention for engaged players | [Reported, 2026-10] |
| Share cards and invites | The game's own loop (share grid, group invites); measured as k ([Game KPIs](../../measurement/references/game-kpis.md) section 6) | [Practitioner consensus] |

A daily social game grows mostly through its share and group loop; paid UA amplifies a loop that already works.

## 10. Web first games

- No store, no SKAdNetwork: paid social and search drive to the game URL with UTMs and click ids ([UTM and channel governance](../../measurement/references/utm-and-channel-governance.md)); conversion events go to Meta and Google through their conversion APIs (`measurement`).
- Bid on a qualified event (first game completed, group joined, D1 return as an offline event), not on page views.
- Portals (Poki, CrazyGames) are distribution and monetization deals owned by `game-monetization` and `growth-orchestrator`; exclusivity terms can block later store or web plans.
- A store wrapper later adds installs as a second funnel; keep one player id across web and app so cohorts do not double count.

## 11. Pitfalls

1. Vendor CPIs used as targets.
2. tROAS with too few events.
3. Soft launch traffic mix unlike the global plan.
4. D1 read from under 1,000 installs.
5. Fake or unrepresentative gameplay ads.
6. A web shop business case that assumes zero US commission forever.
7. Too many SKAdNetwork values and campaigns early.
8. Scaling on installs while ARPDAU is unproven.
9. Mixing install definitions (MMP vs analytics) in one cohort table.
10. Cutting iOS on delayed postbacks without the Android and consented comparison.

## 12. Weekly UA loop for a game (45 to 60 minutes)

1. Measurement health: MMP vs store installs, SKAdNetwork null share, ad revenue integration status.
2. KPI table by channel and OS: spend, installs, CPI, D1, D7 ROAS (and D30 as cohorts mature), payback trend, from MMP and backend side by side.
3. Creative: IPM and CPI by concept, kill and graduate per [Game ad creative](../../creative-strategy/references/game-ad-creative.md) section 5.
4. Gates: `game_kpis.py` output for the newest mature cohorts by source.
5. Change list: bids, budgets, new tests, each a G3 line with reason, expected effect, read date and rollback.
6. Handoffs: retention problems to `game-liveops`, ARPDAU problems to `game-monetization`, page problems to `app-store-optimization`.

## 13. Sources

| # | Source | Publisher | Date | Supports |
|---|--------|-----------|------|----------|
| 1 | What's new in AdAttributionKit (WWDC25 session 221) | Apple | 2025-06, read 2026-10-12 | Configurable windows, cooldown, country code, re-engagement [Official, 2026-10] |
| 2 | Measure ad performance with SKAdNetwork (WWDC22 session 10038) | Apple | 2022, read in the research pass | SKAN 4 postbacks [Official] |
| 3 | DMA and apps in the EU | Apple Developer support | Terms effective 2026-10-01, read 2026-10-12 | EU commission rates, 7 day link out window [Official, 2026-10] |
| 4 | App Review Guidelines 3.1.1(a) | Apple | 2026-06-08 version | US link outs [Official, 2026-10] |
| 5 | UA cost report 2026; winning creatives | FoxData | 2026 | CPI by genre, creative format shares [Unverified, vendor] |
| 6 | Soft launch guide (2025-12-16) and CPI article (2026-03-17) | gamegrowthadvisor.com | 2025 to 2026 | Markets, gates, volumes [Reported, 2026-10] |
| 7 | Soft launch gate | getbruin | 2025 to 2026 | Gate rules of thumb [Reported, 2026-10] |
| 8 | D7 ROAS article | playio | 2026 | ROAS ranges [Reported, 2026-10] |
| 9 | Liftoff blog (?p=35616) and casual report | Liftoff | 2025 to 2026-04 | Curve derived targets, casual CPI and ROAS [Reported, 2026-10] |
| 10 | What is ROAS; web shop business case | Unity | ongoing | ROAS basics, web shop economics [Unverified, vendor] |
| 11 | Ad platforms 2026; creative testing | Segwise | 2026 | Network shares, testing volume [Unverified, vendor] |
| 12 | MMP pricing comparison | Airbridge | 2026 | Free tier claims [Contested] |
| 13 | Apple Ads benchmarks | AppTweak | about 2025-07 | Games CPI median [Reported, 2026-10] |
| 14 | Meta Advantage+ app guide | Admiral | 2025 to 2026 | Learning event volume [Reported, 2026-10] |
| 15 | Playrix ads banned; Evony ruling | pocketgamer.biz; mishcon.com | 2020-09-30; 2024 | Representative gameplay rule [Reported, 2026-10] |
| 16 | Apple commissions coverage | courthousenews.com, fenwick.com, thenextweb.com | 2025-12 to 2026-08 | Epic v Apple status [Reported, 2026-10] |
| 17 | Hybrid casual UA | AppSamurai | 2025 | Hybrid casual retention and UA [Reported, 2026-10] |
