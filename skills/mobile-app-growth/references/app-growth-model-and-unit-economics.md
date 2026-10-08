# App Growth Model and Unit Economics

> Knowledge as of 2026-10. Store fees changed in the US, EU, UK, Japan, Brazil and China during 2025 and 2026. Re-check the fee table against the Freshness Protocol in SKILL.md before any payback model goes to a human.

## 1. The app growth system in one picture

An app grows through a small number of loops. Diagnose which loop is broken before touching any campaign.

| Loop | Input | Output | Owner here | Usual constraint |
|------|-------|--------|-----------|------------------|
| Paid acquisition | Media spend on Apple Ads, Google App campaigns, Meta, TikTok, networks | Installs, trials, payers | mobile-app-growth (with meta-ads, google-ads, tiktok-ads for channel depth) | Measurement quality and payback |
| Store search | Metadata, ratings, conversion rate, download velocity | Organic installs | mobile-app-growth | Keyword relevance and product page conversion |
| Store browse and featuring | Editorial nominations, in-app events, Today tab stories, Play promotional content | Organic installs and reactivations | mobile-app-growth | Quality bar and event calendar |
| Web to app | Ads and SEO to web funnels, web checkout, deep links | Payers acquired outside the store | mobile-app-growth with cro and site-engineer | Funnel friction, account linking |
| Product virality | Invites, shares, referrals, UGC | New installs | mobile-app-growth with lifecycle-crm | Product hooks |
| Retention and monetization | Onboarding, paywall, pricing, push, email | Revenue per install, LTV | mobile-app-growth (paywall), lifecycle-crm (flows) | Activation and churn |

Rule: paid loops amplify the store and product loops. A paid campaign cannot fix a product page that converts at half the category median or a paywall that converts at 1%. Fix the multiplier first.

## 2. Metric dictionary (use these exact names)

Acronym collisions are common in app growth (CPT is both cost per tap and cost per trial; CPP is both cost per payer and custom product page). Use the names below in every output.

| Metric | Definition | Notes |
|--------|------------|-------|
| Impressions (store) | Times the app appeared in search, browse or featuring | App Store Connect Analytics, Play Console |
| Product page views | Visits to the product page | Apple counts unique devices per day |
| Product page conversion rate | First-time downloads / product page views | Apple: "Conversion rate"; Play: store listing acquisitions / visitors |
| Cost per tap (Apple Ads) | Spend / taps | Call it "CPT (tap)" in tables |
| Tap-through rate | Taps / impressions | Apple Ads TTR |
| CPI | Spend / attributed installs | State the attribution source (MMP, SAN, SKAN/AAK, AdServices) |
| IPM | Installs per 1,000 impressions | Creative quality on networks and TikTok |
| Cost per trial start | Spend / trial starts | Never abbreviate to CPT |
| Cost per paying user | Spend / first paid conversions in the cohort window | Write "cost per payer"; never CPP |
| Install to trial rate | Trial starts / installs (by day N) | RevenueCat uses download to trial by day 30 |
| Trial to paid rate | Paid conversions / trial starts that reached the end of the trial | Exclude trials still running |
| Install to paid rate | First paid conversions / installs by day 35 | RevenueCat definition (day 35) |
| Dn retention | Users active on day N / installs on day 0 | Classic (exact day) unless stated rolling |
| ARPU (n) | Net proceeds by day N / installs | Use net proceeds after store fee, tax, refunds |
| ARPPU | Net proceeds / paying users | |
| LTV (n) | Cumulative net proceeds per install by day N | Always say the horizon: LTV D30, D180, D365 |
| ROAS Dn | Cumulative net proceeds by day N / spend on that cohort | Gross ROAS (before store fee) must be labeled gross |
| Payback days | First day where cumulative net proceeds per install is at least CPI | |
| Refund rate | Refunded transactions / transactions | Hard paywalls refund more (RevenueCat SOSA 2025: 5.8% hard vs 3.4% freemium [Study, 2025-03]) |
| Acquisition investment | Media spend + incentives + incremental discount cost | Matches ads-master/METRICS.md |

## 3. Proceeds math: what you actually keep

Net proceeds per transaction = price x (1 minus tax share) x (1 minus store or processor fee) x (1 minus refund rate).

### 3.1 Store and processor fee table (verify before use)

| Route | Fee as of 2026-10 | Evidence |
|-------|-------------------|----------|
| Apple IAP standard | 30%; 15% Small Business Program, subscriptions after year one, Video and Mini Apps partner programs | [Official] long standing |
| Apple IAP, China storefront | 25% standard, 12% small business and mini apps from 2026-03-15 | [Official, 2026-03] |
| Apple US storefront, link out to web | 0% commission today; Apple proposed 15% standard, 10% partner programs and renewals, 5% Small Business on 2026-08-13; district court has not set a fee; Supreme Court reviewing the contempt standard (No. 25-1311) | [Official court record via coverage, 2026-09] [Contested] |
| Apple EU from 2026-10-01 | IAP 26% (15% small business and programs, and subscriptions after year one); alternative in-app payments 20% (10% programs); link out to web 15% (10% programs); 5% Core Technology Commission on digital sales in apps distributed outside the App Store or on the web; Core Technology Fee, Initial Acquisition Fee and Store Services Fee removed | [Official, 2026-08 newsroom; rates via secondary coverage, verify Attachment 14] |
| Apple Japan | Alternative marketplaces and payments under MSCA from iOS 26.2 (agreement acceptance by 2026-03-17) | [Official, 2025-12] |
| Apple Brazil | Alternative marketplaces and out of IAP payments from iOS 26.5; Core Technology Commission applies | [Official, 2026-06] |
| Google Play US, UK, EEA from 2026-06-30 | Service fee 10% on first $1M annual earnings and on all auto-renewing subscriptions; other transactions above $1M: 20% new installs, 25% existing installs; plus 5% billing fee only when Play Billing is used | [Official, 2026-06] |
| Google Play US alternative billing and external content links programs | Live since 2025-12-09; Google Help says enrolled developers report transactions and pay fees from 2026-10-01; one analysis disputes enforcement; per download fees reported for external links ($2.85 apps, $3.65 games) | [Official Help snippets] [Contested] |
| Google Play Australia, Japan, South Korea, rest of world | Fee split phases in 2026-09-30 (Australia), 2026-12-31 (Japan, Korea), through 2027-09 elsewhere | [Practitioner consensus from Google schedule, verify] |
| Web checkout processor (Stripe, Paddle, RevenueCat Web Billing) | Stripe standard 2.9% + $0.30 in the US; RevenueCat Web Billing adds its plan fee; merchants of record (Paddle) charge more but handle tax | [Official vendor pricing, verify] |

Fixed processor fees punish cheap plans: $0.30 is 6% of a $4.99 charge but 0.3% of a $99.99 charge. Model web checkout per plan, not per app.

### 3.2 Break-even web conversion

Web checkout wins only if web conversion stays above: (in-app net take rate) / (web net take rate) of in-app conversion.

Example: in-app at 15% Small Business fee keeps 85%. Web on Stripe at $59.99 annual keeps about 96.6%. Break-even ratio = 85 / 96.6 = 0.88. Web must convert at least 88% as well as the in-app sheet. RevenueCat's single-app 2025 test (Dipsea) measured web trial start at 18.1% vs 27.0% in-app (67%), which lost money ($0.93 web per $1.00 IAP) even with zero Apple commission [Study, 2025-05]. Most of the loss happened between the payment sheet and purchase.

## 4. LTV curves and payback

### 4.1 Build the curve from cohorts, not averages

1. Pull install cohorts by week, channel, OS and country from the MMP or RevenueCat (or App Store Connect and Play Console for organic).
2. For each cohort, compute cumulative net proceeds per install at D0, D3, D7, D14, D30, D60, D90, D180, D365.
3. Fit a curve only after at least 3 cohorts reach the horizon. Before that, use ratios from older cohorts: LTV D365 / LTV D30 multiplier, by plan mix.
4. Re-fit monthly. Price tests, plan mix shifts (weekly vs annual) and trial length changes break old multipliers.

### 4.2 Subscription curve shape

- Weekly plans front-load revenue and churn fast; Adapty's 2026 report finds weekly plans at 55.5% of subscription revenue in its 2025 data, 73.6% in Utilities, while Health and Fitness is the only category where annual dominates (60.6%) [Study, 2026].
- Annual plans create a cliff at day 365. Year-one retention for annual subscribers is about 27% (hard paywall) to 28% (freemium) in RevenueCat's 2026 data [Study, 2026-03]. Model the renewal step explicitly.
- AI apps monetize harder and churn faster: RevenueCat 2026 reports 41% more revenue per user and annual retention of 21.1% vs 30.7% for non-AI apps [Study, 2026-03].

### 4.3 Payback rules of thumb (set with the human, then store in PROJECT_BRIEF.md)

| Business | Typical payback target | Why |
|----------|------------------------|-----|
| Subscription, venture funded | 6 to 12 months on net proceeds | Cash runway tolerates it, renewals uncertain |
| Subscription, bootstrapped | 1 to 3 months, weekly plans often D30 | Cash constrained |
| Casual and hybrid casual game | D7 ROAS targets set from D7 to D180 ratio; payback 90 to 180 days | Ad revenue plus IAP, long tail |
| Mid-core and strategy game | 180 to 365 days | Whales arrive late |
| Ecommerce or marketplace app | First order contribution or 90 day contribution | App users repeat more; prove incrementality first |
| Fintech | Cost per funded or active account below 12 month contribution | Compliance gates the funnel |

These are [Practitioner consensus] ranges, not benchmarks. The human sets the target.

## 5. Target CPI and bid derivation

Target CPI = LTV(horizon) x (1 minus margin buffer) x calibration factor.

- LTV(horizon): net proceeds per install at the payback horizon from section 4.
- Margin buffer: 20% to 40% for new channels, 10% to 20% for proven ones.
- Calibration factor: incrementality evidence (lift or geo test) divided by platform-reported results. Without a test, use 1.0 for Apple Ads brand terms only after checking organic rank (brand terms are the least incremental), 0.7 to 0.9 for generic search, and say it is an assumption.

Cost per payer target = target CPI / install to paid rate. Use this for in-app action bidding (Google tCPA, Meta app events, Apple Ads Maximize Conversions targets are install based, so translate back).

### Worked example: subscription app (Growth tier)

Inputs (from PROJECT_BRIEF.md and RevenueCat, labeled per project): annual plan $59.99, 7-day trial, 85% kept after Small Business fee, refunds 4%, install to trial 11%, trial to paid 38%, first year renewal ignored for payback.

1. Net per first annual payment = 59.99 x 0.85 x 0.96 = $48.95 (US, tax excluded for simplicity; add sales tax handling per market).
2. Install to paid = 0.11 x 0.38 = 4.18%.
3. Net proceeds per install by D35 = 48.95 x 0.0418 = $2.05.
4. Payback target D35 with 25% buffer: target CPI = 2.05 x 0.75 = $1.53. Target cost per trial start = 1.53 / 0.11 = $13.9. Target cost per payer = 1.53 / 0.0418 = $36.6.
5. Compare with the market: Apple Ads search results CPA (cost per install) medians were $2.51 to $3.76 in 2025 data depending on source [Study, 2026]. At $1.53 the app is not viable on Apple Ads generic terms without better conversion. Actions: improve trial start rate on the paywall, test a longer trial (RevenueCat 2026: 17 to 32 day trials convert at a 42.5% median vs 25.5% for 4 days or less [Study, 2026-03]), or move payback to D365 with renewal modeling if the human accepts it.

### Worked example: casual game (Scale tier)

1. Historical D7 ROAS to D180 ROAS multiplier = 3.1 (from 6 mature cohorts).
2. Target D180 ROAS = 110% (10% margin over break-even).
3. D7 ROAS target = 110% / 3.1 = 35.5%. Bid tROAS (Google) or ROAS goal (Meta) from trailing actuals near 35%, never from the aspiration.
4. Gaming CPI rose 30% in 2025 to a $0.56 global median in Adjust data, while gaming installs stayed flat [Study, 2026-02]. Expect bid pressure; protect margin with creative IPM, not bids.

## 6. Budget sizing by channel

| Channel | Minimum to learn | Source |
|---------|------------------|--------|
| Apple Ads Maximize Conversions | Daily budget for at least 5 conversions per day; leave 2 weeks before changing target CPA | [Official best practices, 2026] |
| Google App campaigns, installs tCPI and pre-registration | Daily budget at least 50x target CPI | [Official, Google Ads Help] |
| Google App campaigns, installs tCPA | At least 10x target CPA | [Official] |
| Google App campaigns, engagement tCPA | At least 15x target CPA | [Official] |
| Google tROAS (apps) | At least 10 conversions per day or 300 in 30 days of the bid event | [Official] |
| Meta app events | About 50 optimization events per ad set per 7 days | [Official, Meta developer docs, 2024-10] |
| TikTok App promotion | About 50 conversions per ad group per 7 days; budget at least 10x target CPA | [Official per tiktok-ads package] |

If the budget cannot buy those volumes, optimize to a shallower event (install, registration, onboarding complete, trial start) and say so in the plan.

## 7. Channel mix by stage (starting point, not a rule)

| Stage | iOS | Android | Organic |
|-------|-----|---------|---------|
| Pre-launch | Pre-orders (App Store), waitlist web funnel | Pre-registration campaign (Google ACpre), Play pre-registration rewards | Landing page, ASO baseline, press |
| Launch to 90 days | Apple Ads brand + category exact, then Meta or TikTok for volume | Google ACi, then Meta or TikTok | ASO iterations weekly, ratings prompt |
| Growth | Add Apple Ads discovery and competitor, Today tab tests, CPPs per audience | ACi tCPA, ACe for lapsed, tROAS when eligible | CPP keywords, in-app events, localization |
| Scale | Networks (AppLovin, Unity, Moloco, Liftoff, Mintegral) as tested cells, web to app | Same plus networks, DSPs | Featuring nominations, localized creative |
| Enterprise | Geo holdouts per channel, MMM, multi-market CPP and PPO programs | Same | Store experimentation calendar |

Singular's ROI Index 2026 (released 2026-04-02) names a recurring core group across iOS and Android leaderboards: Apple Ads, AppLovin, Google Ads, Liftoff, Meta, Mintegral, Moloco, TikTok, Unity Ads, Snapchat and X [Study, 2026-04]. Use it to shortlist networks, not to set budgets.

## 8. Quick benchmark table (directional only)

Compare a project against its own history first. These carry source, date and caveat; see research/mobile-app-growth.md for detail.

| Metric | Value | Source and caveat |
|--------|-------|-------------------|
| Install to paid by D35, hard paywall median | 10.7% (12.1% prior year) | RevenueCat SOSA 2026, 115k+ apps, 2025 data, RevenueCat customers only [Study, 2026-03] |
| Install to paid by D35, freemium median | 2.1% | Same |
| Trial to paid, 17 to 32 day trials vs 4 days or less | 42.5% vs 25.5% | Same; descriptive, not causal |
| Web share of subscription revenue | 3.2% global, 4.9% North America | Same; FunnelFox reports far higher adoption among top grossing apps (different measure) |
| Weekly plan share of revenue | 55.5% | Adapty 2026, 16k+ apps, mostly App Store [Study, 2026] |
| ATT opt-in among users shown the prompt | 38% all apps, 39% gaming (Q1 2026) | Adjust, denominators differ from AppsFlyer [Study, 2026-03] |
| Apple Ads search results conversion rate (tap to install) | 56% (AppTweak global median) to 62% (Adapty) to 66.2% (SplitMetrics via secondary) | 2025 data, method differs [Study, 2026] |
| Global IAP consumer spend 2025 | $167B, +10.6%; non-game apps passed games | Sensor Tower State of Mobile 2026, App Store and Google Play only, excludes China Android [Study, 2026-01] |
| Global app installs and sessions 2025 | +10% installs, +7% sessions | Adjust Mobile App Trends 2026 [Study, 2026-02] |
| D1 / D7 / D30 retention, all apps | About 26% / 13% / 7% (iOS 27/14/8, Android 24/11/6) | Adjust guide, undated and older; 2026 by category tables not verified [Study, older] |

## 9. Output template: unit economics memo

```
# Unit economics memo: <app>, <date>
Data used: <source, date range, attribution source>
Fee assumptions: <route and fee per market, with evidence label>
| Metric | iOS | Android | Web | Source |
LTV curve: D7, D30, D90, D180, D365 per install (net)
Payback: <days> vs target <days>
Target CPI / cost per trial start / cost per payer by channel
Sensitivity: +/-10% on trial start, trial to paid, price, fee
Decisions requested: <list, each with approval line>
```
