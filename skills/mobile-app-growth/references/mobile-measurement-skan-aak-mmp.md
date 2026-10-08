# Mobile Measurement: MMPs, SKAdNetwork, AdAttributionKit, ATT and Android

> Knowledge as of 2026-10. Key changes: AdAttributionKit configurable attribution windows, cooldown, country code in postbacks, overlapping re-engagement with conversion tags and development postbacks (iOS 18.4, WWDC25); no notable AAK or SKAN changes at WWDC26 (2026-06); alternative ATT prompt in the EU from iOS 27.2, the only allowed version in Germany, France, Italy, Poland and Romania (announced 2026-09-16); Privacy Sandbox on Android retired (announced 2025-10, status page 2026-08-14); Google iOS on-device measurement and ICM (2025 to 2026); AppsFlyer $1B+ minority investment from Moloco, Google, Meta and Unity (2026-06); official MCP servers from RevenueCat, AppsFlyer and Singular. The measurement agent owns the tracking stack across web and app; this module defines what app growth needs from it and how to read it.

## 1. The app measurement stack

| Layer | iOS | Android | Owner |
|-------|-----|---------|-------|
| Store truth | App Store Connect (downloads, proceeds, subscriptions, sources) | Play Console (acquisitions, revenue, subscriptions) | mobile-app-growth reads |
| Revenue truth | RevenueCat, Adapty, Superwall or backend receipts with App Store Server Notifications V2 | Same with Real-time developer notifications (RTDN) | measurement with mobile-app-growth |
| Attribution | MMP (deterministic with ATT consent, AdServices for Apple Ads), SKAdNetwork and AdAttributionKit postbacks, SAN reporting | MMP with Play Install Referrer and GAID, SAN reporting | measurement |
| Product analytics | Firebase (GA4), Amplitude, Mixpanel, PostHog | Same | product team |
| Incrementality | Geo holdouts, platform lift, ghost ads, MMM | Same | measurement |

Rule: revenue truth beats attribution truth. Every report states which layer each number came from.

## 2. Choosing an MMP

| Criterion | Questions |
|-----------|-----------|
| Integrations | Are all current and planned networks integrated, including cost ingestion and SKAN or AAK? |
| iOS privacy | SKAN 4 and AAK support, conversion value tooling (AppsFlyer SKAN Conversion Studio, Adjust Conversion Hub, Singular SKAN tools), modeled reporting method disclosed |
| Fraud | Click injection, click spam, device farms, SDK spoofing protection; rules you can tune |
| Deep linking | Deferred deep links, universal links and app links hosting, QR, web to app attribution |
| Data access | Raw data exports, pull APIs, warehouse sync, an MCP server (read only) |
| Pricing | Per attribution or conversion fees vs flat; public price points are rare. One 2026 comparison lists $0.05 per conversion for Singular vs $0.07 for AppsFlyer [Unverified]; Kochava publishes pricing [Practitioner consensus] |
| Neutrality | Ownership and investors (AppsFlyer took minority stakes from Moloco, Google, Meta and Unity in 2026-06; investors get no preferential treatment per the CEO [Official statement via Axios]); keep your own exports |

Options by stage:
- Starter subscription app: RevenueCat (or Adapty) for revenue plus Apple Ads AdServices attribution plus Meta and Google SDK reporting; add an MMP when paying 2+ paid networks.
- Growth and above: a full MMP (AppsFlyer, Adjust, Branch, Singular, Kochava, Airbridge; Tenjin for cost sensitive game studios).
- Business of Apps reports a concentrated market where AppsFlyer, Adjust, Branch and AppMetrica rank top five on both platforms [Study, 2026].

## 3. SKAdNetwork 4 (still the most used iOS privacy framework)

| Element | Detail |
|---------|--------|
| Postback windows | Window 1: days 0 to 2; Window 2: days 3 to 7; Window 3: days 8 to 35 [Official] |
| Conversion values | Fine value 0 to 63 in window 1 only (subject to crowd anonymity); coarse value low, medium or high in all windows [Official] |
| Crowd anonymity tiers | Tiers 0 to 3 set how much data a postback carries (source identifier digits, fine vs coarse value, source app or domain) [Official] |
| Source identifier | Hierarchical 2 to 4 digits; the network maps campaign structure into it [Official] |
| lockWindow | The app can lock a window early to send its postback sooner [Official] |
| Timers | Window 1 postback arrives 24 to 48 hours after the window closes; windows 2 and 3 add a random 24 to 144 hour delay [Official] |
| Web to app | SKAN 4 supports ads on Safari web pages leading to App Store installs [Official] |

Practical consequences:
- Day 0 to 2 behavior must predict value. Design the app to surface the money moment (trial start, first purchase, level 5) inside 48 hours.
- Small campaigns and many source identifiers lower the crowd anonymity tier and null the fine value. Consolidate.
- Network adoption: one 2026 explainer says most large platforms are still primarily on SKAN 3 behavior with TikTok furthest on SKAN 4; another treats SKAN 4 and AAK as the baseline [Contested]. Ask each network what it uses and verify from postback data.

## 4. AdAttributionKit (AAK)

| Feature | Availability | Evidence |
|---------|--------------|----------|
| Install attribution with JWS signed postbacks, interoperable with SKAN (impressions from either framework count) | iOS 17.4+ | [Official, WWDC24] |
| Alternative marketplaces (EU) and web support | iOS 17.4+ | [Official] |
| Re-engagement attribution | iOS 18+ | [Official] |
| Configurable attribution windows per interaction type and per ad network (default 30 days click, 1 day view) | iOS 18.4+ | [Official, WWDC25] |
| Attribution cooldown | iOS 18.4+ | [Official, WWDC25] |
| Country code in postbacks (subject to crowd anonymity) | iOS 18.4+ | [Official, WWDC25] |
| Overlapping re-engagement conversions with conversion tags (previously one active re-engagement conversion per app) | iOS 18.4+ | [Official, WWDC25] |
| Development postbacks and testing in Developer settings | iOS 18.4+ | [Official, WWDC25] |
| WWDC26 changes | None notable to windows, postbacks, tiers or re-engagement | [Practitioner consensus via Adjust, 2026-06] |

Adoption: Apple Ads registered with AAK in 2025-04 [Practitioner via Singular]. Apple says any network can integrate. A Kochava survey reports negligible AAK traction and a quarter of marketers unaware of it [Study, 2026, vendor survey]. Meta AAK support is reported by one guide only [Unverified]; Google has not clearly documented AAK support [Unverified]. Action: implement AAK alongside SKAN through the MMP SDK, and confirm per network coverage in your own postbacks.

## 5. Conversion value schemas (templates)

Principles:
1. Encode what predicts revenue within 48 hours, aligned to the bid event each network optimizes.
2. Fine value: up to 64 states. Use revenue buckets plus 1 to 2 behavior flags, not 6 independent flags.
3. Coarse values: low = activated, medium = intent (trial, add to cart, level), high = money.
4. Keep the schema stable for at least 4 weeks; coordinate changes with networks (some cache the mapping).
5. Validate monthly: correlation between window 1 value and D30 revenue per user from consented or Android cohorts.

### 5.1 Subscription app

| Window | Value | Meaning |
|--------|-------|---------|
| 1 fine | 0 | Install only |
| 1 fine | 1 to 7 | Onboarding complete, paywall viewed, account created (bit flags) |
| 1 fine | 8 to 15 | Trial started (and whether still active at lock time) |
| 1 fine | 16 to 63 | Paid conversion with revenue buckets (weekly, monthly, annual, by price band) |
| 1 coarse | low / medium / high | Onboarding complete / trial started / paid |
| 2 coarse | low / medium / high | Active on day 3 to 7 / trial active at day 7 / converted or paid |
| 3 coarse | low / medium / high | Active by day 35 / any renewal attempt / renewed or upgraded |

Note: 90% of trial starts happen on day 0 (Adapty 2026) and most trial cancellations happen on day 0 (RevenueCat 2026) [Study, 2026]. "Trial started and not cancelled at lock" is a strong quality signal; lock window 1 around hour 24 to 36 only if that keeps the signal.

### 5.2 Game

| Window | Value | Meaning |
|--------|-------|---------|
| 1 fine | 0 to 7 | Retention and progression (returned on day 1, tutorial complete, level thresholds) |
| 1 fine | 8 to 63 | Combined IAP plus ad revenue buckets (log scaled, for example $0.01 to $0.50, $0.50 to $2, $2 to $5, $5 to $20, $20+) crossed with a D1 return flag |
| 1 coarse | low / medium / high | D1 return / ad revenue above threshold or level X / any IAP |
| 2 and 3 coarse | low / medium / high | Active / cumulative revenue above threshold / payer above high threshold |

### 5.3 Ecommerce or marketplace app

| Window | Value | Meaning |
|--------|-------|---------|
| 1 fine | 1 to 7 | Registration, product view depth, add to cart |
| 1 fine | 8 to 63 | First purchase with order value buckets in local currency bands |
| 2 and 3 coarse | low / medium / high | Active / second session with cart / repeat purchase |

## 6. ATT prompt strategy

Benchmarks: Adjust measured 38% average opt-in among users shown the prompt in Q1 2026 (35% a year earlier), gaming 39%, publications 26%, ecommerce 34%; India gaming 51%, Europe 36%, North America 33% [Study, 2026-03]. AppsFlyer's 2025 framing gives 50% headline, 40% for users who see the prompt and 30% on a broader base [Study, 2025-04]. Denominators differ; never compare vendors directly.

Rules (Apple):
- Use the system prompt with an NSUserTrackingUsageDescription string that says what the user gets.
- A custom explanation screen before the system prompt is allowed. Do not mimic the system alert, do not offer incentives for allowing tracking, do not block features for users who decline (App Review Guidelines 5.1.1 and 5.1.2) [Official].
- Fingerprinting is never allowed, with or without consent [Official, Apple statement].

Timing play:
1. Default: show the prompt after the first value moment (onboarding complete, first result), not at first launch.
2. Games: test at launch with a pre-prompt vs after tutorial.
3. A/B test with the MMP or analytics: opt-in rate by variant and downstream retention (forcing an early prompt can raise drop-off).
4. Do not re-prompt (the system shows it once per install) except where the EU alternative prompt allows a new request one year after the last answer.

EU alternative ATT prompt (iOS 27.2 and iPadOS 27.2):
- Optional across the EU, mandatory (only version available) for apps distributed in Germany, France, Italy, Poland and Romania [Official, 2026-09-16].
- Reported design: no word "track", Allow and Reject buttons, optional "Additional Information" text button that returns notDetermined, full page rather than an alert, and the app may ask again one year after the user's last answer whether Allow or Reject [Official developer documentation via coverage, 2026-09]. The Bundeskartellamt commitments (case closed 2026-08-17) also remove the warning hand symbol and give publishers up to 4,000 characters to explain why personalized ads fund the app [Official regulator via coverage].
- Background: France fined Apple 150 million euros (2025-03, end of March), Italy about 98.6 million euros (2025-12-22) over ATT; Poland and Romania opened cases [Official regulators via coverage].
- Action: prepare explanation copy per language, run it through compliance, track opt-in by country after iOS 27.2 release, and update SKAN vs device level weighting in the EU.

Consent beyond ATT: GDPR, ePrivacy and KVKK consent for SDK data collection is separate from ATT. In the EEA, UK and Switzerland, Google requires a Google certified CMP using IAB TCF for ad serving through its publisher products [Official, 2024-01]. Hand CMP work to measurement and compliance.

## 7. Android measurement

- Google Advertising ID remains; apps targeting Android 13+ must declare the AD_ID permission to read it; users can delete it [Official].
- Play Install Referrer gives deterministic install attribution for Play installs [Official].
- Privacy Sandbox on Android is retired: Google's status page (updated 2026-08-14) lists Attribution Reporting, On-Device Personalization, Protected App Signals, Protected Audience, SDK Runtime and Topics on Android as "Deprecate and remove" [Official, 2026-08]. Do not plan migrations to those APIs.
- Developer verification (from 2026-09-30 in Brazil, Indonesia, Singapore, Thailand; global 2027) affects sideloaded and third party store distribution, not Play attribution [Official].

## 8. Probabilistic modeling: limits

- Allowed: aggregated modeling (conversion modeling from consented cohorts, SKAN modeled revenue, MMM, lift).
- Not allowed on iOS: device fingerprinting or IP plus user agent matching to identify ATT denied users [Official]. Some vendors call IP matching "probabilistic attribution"; treat that as fingerprinting for ATT denied iOS traffic and switch it off.
- Privacy manifests: since 2024-05-01 App Store Connect rejects apps that do not declare approved reasons for required reason APIs; SDKs need their own manifests; declared tracking domains are blocked when the user has not allowed tracking [Official].
- Ask the MMP in writing which matching methods run for ATT denied users; store the answer in MEASUREMENT.md.

## 9. Event taxonomy and server events

| Event | Fired from | Notes |
|-------|-----------|-------|
| install, first_open | SDK | MMP install |
| onboarding_complete | App | Activation |
| registration | App or server | |
| paywall_view (with paywall_id, placement) | App | For paywall analytics |
| trial_start | Server (RevenueCat or store notifications) | Use server events to avoid client loss |
| subscription_purchase, renewal, cancellation, refund | Server | Send refunds as negative revenue to the MMP and networks that accept them |
| purchase (IAP, ecommerce) with value and currency | Server preferred | Deduplicate client and server |
| ad_revenue (games) | Mediation SDK (MAX, LevelPlay, AdMob) to MMP | Impression level revenue |

Rules: one name per event across platforms; value always with ISO currency; test events in sandbox and development postbacks before release.

## 10. Weekly data QA (10 minutes)

| Check | Threshold | Action if failed |
|-------|-----------|------------------|
| MMP installs vs App Store Connect first-time downloads and Play acquisitions | Within 10% to 20% after accounting for organic and redownloads | Investigate SDK version, consent, attribution settings |
| RevenueCat or backend revenue vs MMP revenue | Within 5% | Fix server to server integration |
| SKAN postbacks with null conversion value | Stable week over week | Check crowd tiers, campaign fragmentation |
| Event lag | Trial and purchase events arrive within 24 hours | Check webhooks |
| Duplicates | No double purchase events per transaction ID | Deduplicate |
| ATT opt-in rate | Stable or explained | Check prompt changes, OS release |

Any failure that affects bidding events is an incident: freeze bid and budget changes on affected campaigns, write a journal alert, hand off to measurement.

## 11. Incrementality for apps

| Method | When | Notes |
|--------|------|-------|
| Geo holdout (matched markets, ads off in control) | Default for apps; resists signal loss because the unit is a region | Run a power simulation on history first; hold 2 to 4 weeks, longer with trials [Practitioner consensus, 2026] |
| Google Conversion Lift (geo or user based) | App campaigns, through the rep | Not available for all accounts [Official] |
| Meta Conversion Lift | App events with enough volume | Access through a Meta representative; breakdowns need at least 100 conversions in test and control combined to display [Official] |
| Ghost ads or ghost bids | Retargeting and DSPs | Needs a vendor in the middle [Practitioner consensus] |
| Brand keyword pause test | Apple Ads brand | See [Apple Ads](apple-ads.md) section 11 |
| MMM (Meridian, Robyn, PyMC-Marketing) | Enterprise, multi channel | Calibrate with experiments; one 2026 preprint warns that reducing a test to a single lift prior discards time structure [Contested] |

Hand test design and MMM to measurement; mobile-app-growth supplies cohorts, spend and hypotheses.

## 12. Measurement maturity ladder

| Level | Must have | Unlocks |
|-------|-----------|---------|
| 1 | Store analytics, RevenueCat or backend revenue, Apple Ads AdServices | Apple Ads and ASO decisions |
| 2 | MMP with cost ingestion, SKAN schema, Firebase or AAP linked to Google | Multi channel paid UA |
| 3 | Server side subscription and refund events to MMP and networks, AAK, Google ODM and ICM | Deep funnel and value bidding on iOS |
| 4 | Geo holdouts per major channel, calibration factors in MEASUREMENT.md | Budget shifts on incremental returns |
| 5 | MMM calibrated by tests, pLTV values to networks | Enterprise portfolio allocation |
