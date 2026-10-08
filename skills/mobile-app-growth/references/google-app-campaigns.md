# Google App Campaigns (ACi, ACe, ACpre, tROAS)

> Knowledge as of 2026-10. Key changes: Target ROAS for iOS App campaigns and expanded on-device conversion measurement (announced 2025-08-14); Integrated Conversion Measurement (ICM) for iOS with app attribution partners and post-install lookback up to 180 days; Web to App Connect extended to YouTube, Demand Gen and Hotel ads, with Search and Shopping now credited for app installs and in-app conversions; Google Ads API AppTopCombinationView for top asset combinations (v23.2); Demand Gen incrementality A/B framework that includes App campaigns. The google-ads agent owns Google Ads accounts in general; this module covers app specific settings. Coordinate with google-ads for shared budgets, brand search and account policy.

## 1. Campaign subtypes and when to use them

| Subtype | Goal | Platforms | Bid options | Budget floor (Google guidance) |
|---------|------|-----------|-------------|-------------------------------|
| App installs (ACi) | New users | Android and iOS | Install volume (target CPI optional), In-app actions (target CPA), In-app action value (target ROAS) | 50x target CPI for tCPI; 10x target CPA for tCPA [Official] |
| App engagement (ACe) | Re-engage existing users with deep links | Android and iOS (iOS needs enough opted-in or modeled audience) | tCPA on an in-app action, Maximize conversions | 15x target CPA [Official] |
| App pre-registration (ACpre) | Pre-registrations before launch | Android only | Pre-registration bidding | 50x bid [Official] |

Inventory: Search, Google Play, YouTube, Discover, Display network and AdMob apps. Placement control is limited; content exclusions and placement exclusions exist but narrow targeting hurts delivery [Official guidance].

## 2. Measurement prerequisites

| Requirement | Android | iOS |
|-------------|---------|-----|
| Conversion source | Firebase (GA4 for Firebase) or app attribution partner (AAP: AppsFlyer, Adjust, Branch, Singular, Kochava and others) linked in Google Ads | Same, plus SKAdNetwork and AdAttributionKit through Google's SDK or the MMP |
| On-device conversion measurement | Not needed | Implement on-device conversion measurement using event data (Firebase SDK minimum version reported as 12.12.1 in newer guidance, 11.14.0 in older; a standalone SDK exists if Firebase is not used) [Official, version numbers Contested] |
| Integrated Conversion Measurement (ICM) | n/a | Requires on-device measurement plus the latest AAP SDK; shows Google attribution inside the MMP dashboard and supports post-install lookback up to 180 days for value bidding [Official] |
| Conversion actions | Primary: the bid event; secondary: everything else | Same; keep iOS conversion actions distinct where the source differs |
| Values | Revenue events with value and currency for tROAS | Same; values must be consistent |

Pick the bid event using Google's rule: if fewer than 10 distinct users complete the most valuable in-app action per day, pick a more common action [Official].

## 3. Bidding path

```
New app or new market
  -> ACi Install volume (target CPI optional) until the bid event reaches ~10 users/day
  -> ACi In-app actions (tCPA) on the bid event; 3 to 4 weeks of stable value data
  -> ACi In-app action value (tROAS) once eligible: at least 10 conversions/day or 300 in 30 days of the bid event [Official]
  Re-engagement in parallel: ACe tCPA with deep links to lapsed users (lists from Firebase or AAP)
```

Settings rules:
- Set targets from trailing actuals, then move toward the goal in steps of 10% to 20%; Google advises keeping budget and bid changes under 20% at a time [Official].
- Do not switch a campaign from Install volume to In-app actions after launch; build a new campaign [Official guidance].
- Expect inflated CPI in the first days or weeks due to conversion lag; judge after the learning period [Official].
- Avoid overlapping App campaigns for the same app, geo and goal; they compete [Official].
- tROAS on iOS is available globally since the 2025 rollout [Official, 2025-08]; one subscription publisher reports no clear advantage for subscriptions over tCPA [Practitioner, single source]. Test it as a split, not a switch.
- Value for subscriptions: send the first payment value or a predicted LTV value (pLTV) from a model; never send the full annual price as revenue on trial start.

## 4. Structure by tier

| Tier | Android | iOS |
|------|---------|-----|
| Starter | 1 ACi Install volume per OS and market cluster; 1 to 2 ad groups | Only with on-device measurement live; otherwise put iOS budget in Apple Ads first |
| Growth | ACi tCPA on bid event; 2 to 3 ad groups by creative theme; ACe for lapsed users if 100k+ installed base | ACi tCPA with ICM; separate iOS campaign |
| Scale | ACi tROAS split tested vs tCPA; per market campaigns where economics differ; ACe; ACpre for new titles | ACi tROAS with ICM; Web to App Connect for web traffic |
| Enterprise | Portfolio by market and OS, pLTV values, Conversion Lift (geo or user based through the rep), MMM calibration | Same |

Ad groups in App campaigns separate creative themes and audience signals, not keywords. Use 2 to 4 ad groups per campaign at most.

## 5. Assets

| Asset | Recommended | Notes |
|-------|-------------|-------|
| Headlines | Up to 5, 30 characters | One promise per headline; include the brand in one [Practitioner consensus on counts] |
| Descriptions | Up to 5, 90 characters | |
| Images | Up to 20 (landscape, square, portrait) | Real UI or gameplay, no tiny text |
| Videos | Up to 20, YouTube hosted; supply landscape, square and portrait; at least 10 seconds for ACe | Portrait first for Shorts and YouTube; 15 to 30 seconds |
| HTML5 playables | Supported for some inventory | Strong for games |
| Ad strength | At least "Good"; at least one approved asset per type [Official] | |

Rules:
- Wait 2 to 3 weeks before judging a new asset [Official].
- Replace "Low" performance assets in batches, not one by one daily.
- Use AppTopCombinationView (Google Ads API v23.2) to see top asset combinations [Official, 2026].
- Custom store listings on Play can be tied to App campaigns for message match (see [ASO for Google Play](aso-google-play.md)).

## 6. Web to App Connect

- Purpose: send web campaign clicks (Search, Shopping, Performance Max, and now YouTube, Demand Gen and Hotel) straight into the app when installed, and credit web campaigns for app installs and in-app conversions [Official, 2025 to 2026].
- Requires: working App Links and universal links, the app linked in Google Ads, app conversion tracking, and deep link validation in Google Ads [Official].
- Reporting: "unified conversions" combine web and app events [Practitioner consensus wording, verify].
- Google Marketing Live 2026: AI agents that build app deep links in minutes were announced [Official claim via secondary coverage].
- A third-party claim of 2x higher conversion on YouTube with Web to App Connect is unverified.

## 7. Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|--------------|--------|-------|
| Not spending | Target too tight, budget below the ratio, too few assets, policy | Budget vs 50x or 10x rule, asset approvals, policy center | Loosen target 10% to 15%, raise budget, add assets |
| CPI fine, bid event cost bad | Wrong bid event, event firing late or not deduplicated, poor creative to store match | Event timing in Firebase or MMP, event counts by source | Change event (new campaign), fix tracking, match store listing |
| iOS performance collapses | On-device measurement missing, SKAN or AAK conversion values not mapped, SDK outdated | Google Ads diagnostics for iOS, MMP SKAN dashboard | Implement ODM and ICM, update SDKs |
| Spend shifts to one network (for example Display or YouTube) | Asset mix, cheap inventory | Network and asset reports | Add portrait video, refresh images, check content exclusions |
| Sudden drop after edit | Big target or budget change | Change history | Revert, change in 10% to 20% steps |
| tROAS volatile | Value data sparse or inconsistent | Conversions per day, value variance | Go back to tCPA; send cleaner values |

## 8. Measurement and incrementality

- Compare Google reported conversions with MMP attributed conversions weekly; differences of 10% to 30% are common because of attribution windows and modeled conversions [Practitioner consensus].
- Conversion Lift based on geography supports App campaigns and can include web and app conversions; Conversion Lift is not available for all accounts and user based lift for App campaigns goes through the account representative [Official].
- Demand Gen incrementality A/B tests can measure the added value of Demand Gen on top of App campaigns [Official, 2026, via secondary].
- Hand lift design and MMM calibration to measurement.

## 9. Policies to watch

- Misrepresentation and unreliable claims in app ads (fake gameplay, fake system warnings) [Official policy].
- App must comply with Google Play policies for Android promotion; iOS apps must comply with App Store rules.
- Deep link landing pages must exist and match the ad.
- Children's apps and Families policy restrict personalized ads.

## 10. Change list template (Google App campaigns)

| # | Campaign | Setting | From | To | Reason with data | Expected effect | Risk | Rollback trigger | Approval |
|---|----------|---------|------|----|------------------|-----------------|------|------------------|----------|
| 1 | ACi_US_Android_tCPA | Target CPA | $18.00 | $19.80 | 14-day CPA $19.40 on 420 trials, budget capped 6 of 7 days | +10% to 15% volume | Higher CPA | CPA over $22 for 5 days | |
