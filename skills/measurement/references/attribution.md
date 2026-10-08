# Attribution

Attribution assigns credit for conversions to touchpoints. It does not prove cause. Use it for in-platform optimization and directional cross-channel analysis; calibrate it with experiments ([Incrementality](incrementality-testing.md)) and MMM ([MMM](mmm.md)) before big budget moves.

## 1. Three kinds of attribution

| Kind | Who computes it | Sees | Blind spots | Use for |
|------|-----------------|------|-------------|---------|
| Platform attribution | Each ad platform, using its own clicks, views, modeled conversions | Its own impressions and clicks, including logged-in view-through | Other platforms, organic, offline; grades its own homework | Optimizing inside the platform |
| Analytics attribution | GA4 or warehouse | Sessions with UTMs and click IDs, cross-channel paths | Impressions (mostly), blocked or non-consented users, cross-device without login | Cross-channel trends, funnel, landing pages |
| Causal measurement | Experiments, MMM | Incremental effect | Granularity, speed | Budget allocation, channel value |

## 2. Platform defaults and options (October 2026)

| Platform | Default | Options and notes | Label |
|----------|---------|-------------------|-------|
| Meta | 7-day click and 1-day view (engage-through 1 day reported separately since March 2026) | 1-day click, 7-day click; 1-day view; engage-through (formerly engaged-view, 1 day). 7-day view and 28-day view removed from the Ads Insights API on 2026-01-12 (queries return empty, not errors). From March 2026 click-through counts only link clicks (to website, app, lead form, Messenger); likes, shares, saves, comments moved to engage-through; reported video engaged-view threshold lowered from 10 to 5 seconds. 28-day click availability is reported inconsistently | [Official per Meta business news, 2026-03; secondary for details; Contested on 28-day click] |
| Meta incremental attribution | Optional attribution setting that optimizes and reports incremental conversions using Meta's models | Introduced 2025; compare against standard settings in parallel before switching | [Official, 2025; verify availability] |
| Google Ads | Data-driven attribution for most conversion actions; click-through window 30 days | Click window 1 to 90 days; engaged-view window (YouTube) default 3 days; view-through window default 1 day; rule-based models other than last click were removed in 2023 | [Official] |
| GA4 | Data-driven, lookback 30 days for acquisition key events, 90 days for others | Paid and organic last click, Google paid channels last click; per-conversion attribution settings and conversion attribution analysis report (beta) since January 2026; impression inclusive attribution previewed 2025 | [Official, 2026-01] |
| Microsoft Ads | Click window 30 days; view-through for audience ads | DDA rolling out to all accounts by end of May 2026 per Microsoft product news | [Official per microsoft-ads research, 2026-05] |
| TikTok | 7-day click, 1-day view | Click 1, 7, 14, 28 days; view off, 1 or 7 days; engaged view-through options for video | [verify current defaults] |
| LinkedIn | 30-day click, 7-day view | 1, 7, 30, 90 day options per conversion | [Official, long standing; verify] |
| Pinterest | 30-day click, 30-day engagement, 1-day view | Configurable in reporting | [verify] |
| Snap | 28-day click, 1-day view | Configurable | [verify] |
| Reddit | 28-day click, 1-day view | Configurable | [verify] |
| ChatGPT Ads | Click-through conversions; 30-day window recommended; 1-day view-through reported only | 24 to 48 hour lag | [Unverified, 2026] |

Record each project's actual settings in MEASUREMENT.md (Attribution settings per platform). Platform defaults change; the account's actual settings are what matter.

## 3. The 2026 Meta changes: what to do

| Change | Date | Effect | Action |
|--------|------|--------|--------|
| 7-day view and 28-day view removed from Ads Insights API | 2026-01-12 | Third-party dashboards requesting those windows get empty data; reported conversions fell for awareness and video heavy accounts (secondary sources cite 15% to 40%, unaudited) | Update every API query and connector; annotate; rebaseline targets |
| Click-through limited to link clicks; engage-through category | March 2026 (Meta business news "Simplifying Ad Measurement for a Social-First World") | Click-through conversions drop where engagement clicks used to count; total conversions may look lower with no real change | Report click-through and engage-through as separate columns; keep pre and post March data separate; do not judge creative on the break |

Communicate both to the human and channel agents as measurement breaks, not performance changes. Hand off to meta-ads.

## 4. Why the numbers disagree

| Cause | Direction | Typical magnitude driver |
|-------|-----------|--------------------------|
| Overlapping credit (each platform claims the same order) | Sum of platforms over backend | Number of platforms and retargeting share |
| View-through and engage-through | Platform over GA4 | Video and awareness weight |
| Modeled conversions (consent mode, iOS, AEM) | Platform over observed | EEA and iOS share |
| Attribution windows (7 or 30 days vs GA4 lookback) | Either | Purchase cycle length |
| Conversion date vs click date reporting | Timing differences | Google reports by click date (conversion time column available); Meta by impression or click date depending on report |
| Cross-device and logged-in identity | Platform over GA4 | Meta and Google logged-in reach |
| Blocked and non-consented browsers | GA4 under backend | Ad blocker share, EEA consent rate |
| Timezones and currencies | Daily mismatches | Account settings |
| Duplicates | Platform or GA4 over backend | Tag errors |
| Refunds and cancellations | Platforms over net backend | Category |

Rule: track the ratio (platform reported / backend) per platform monthly. A stable ratio is usable; a moving ratio means something changed (tracking, attribution setting, mix).

## 5. Monthly reconciliation procedure

1. Pull for the same calendar month and timezone: backend orders and revenue (net of refunds and gross), GA4 purchases and revenue by default channel group, each platform's conversions and value with the account's attribution setting, spend.
2. Compute: capture rate (GA4 / backend), platform ratio (platform / backend), sum of platforms / backend, new customer share (backend), MER, aMER, nCAC.
3. Compare to last 3 months. Flag ratios that moved more than 15% relative.
4. Explain each flag (tracking change, attribution change, mix shift, promotion) or open an incident.
5. Publish a reconciliation table in the monthly report and update MEASUREMENT.md "How platform numbers are reconciled".

Template:

| Source | Conversions | Value | Ratio to backend | Last month ratio | Note |
|--------|-------------|-------|------------------|------------------|------|
| Backend (net) | | | 1.00 | 1.00 | |
| GA4 (all channels) | | | | | |
| Google Ads (DDA, 30d click) | | | | | |
| Meta (7d click 1d view) | | | | | |
| TikTok (7d click 1d view) | | | | | |
| Sum of platforms | | | | | |

## 6. Self-reported attribution

- Post-purchase survey ("How did you first hear about us?") and CRM "source" fields capture word of mouth, podcasts, creators, TV, AI assistants and dark social that click based tools miss.
- Compare survey share to platform-attributed share by channel; large positive gaps (survey over platform) flag under credited upper funnel channels; large negative gaps flag channels harvesting existing demand.
- Use it as a third lens, never as cause. Weight by response rate and check for order bias (randomize options).
- Survey design: see [Strategy and KPI tree](measurement-strategy-and-kpi-tree.md) section 8.

## 7. Multi-touch attribution tools

Third-party MTA and attribution tools (pixel based, often Shopify focused, sometimes with built-in MMM or survey modules) can help with ad level reporting across platforms. [Contested]: supporters cite consistent cross-platform rules and first-party pixels; critics note they still cannot see impressions, inherit click bias, and their "incremental" claims vary in method. Require any vendor to show: data sources, identity method, treatment of views, how they validate against experiments. Never use an MTA tool as the sole basis for budget allocation.

## 8. App attribution

| Component | What to know | Label |
|-----------|-------------|-------|
| App Tracking Transparency (ATT) | Since iOS 14.5 (2021) apps need permission to track across apps and sites; IDFA available only with opt-in | [Official] |
| SKAdNetwork 4 | iOS 16.1+: up to 3 postbacks across time windows (roughly 0 to 2, 3 to 7, 8 to 35 days), fine conversion values (0 to 63) only in the first postback, coarse values (low, medium, high), crowd anonymity tiers, lockWindow, hierarchical source identifiers | [Official] |
| AdAttributionKit | Apple's framework introduced in iOS 17.4 (2024), interoperable with SKAdNetwork, supports alternative app marketplaces; later releases added re-engagement attribution and configurable attribution windows and cooldowns (iOS 18 to 18.4); check iOS 26 release notes for additions | [Official; version specifics verify] |
| Conversion value schema | Map revenue or key events into fine (0 to 63) and coarse values; design for the first postback window; revisit when monetization changes | [Practitioner consensus] |
| MMPs | AppsFlyer, Adjust, Branch, Singular, Kochava, Airbridge, Tenjin: deterministic attribution where allowed, SKAN and AdAttributionKit decoding, cost aggregation, fraud protection, incrementality modules | [Practitioner consensus] |
| Firebase and GA4 for apps | Google Ads app campaigns optimize from Firebase or MMP conversions; on-device conversion measurement for iOS uses hashed first-party data with privacy preservation | [Official] |
| Web-to-app | Deep links and deferred deep links; capture click IDs on web landing pages and pass through to app install attribution where supported | [Practitioner consensus] |

App checklist: MMP or Firebase installed with consent handling; SKAN or AdAttributionKit conversion schema documented; postbacks configured to each network; in-app revenue events with currency; server-side subscription events (App Store Server Notifications, Google Play RTDN) feeding revenue truth; ATT prompt strategy tested; reconciliation of MMP installs and revenue to store data monthly.

## 9. Decision rules

1. Use each platform's attribution for its own optimization decisions (ad, ad set, keyword) and keep its settings stable; changing windows resets comparisons and can affect learning.
2. For cross-channel budget decisions use calibrated numbers (incrementality factors) and blended metrics (MER, aMER, nCAC).
3. When a platform changes attribution definitions, rebaseline targets with the channel agent within 2 weeks.
4. Report view-through and engage-through separately from click-through in every dashboard.
5. Brand search and retargeting get the most inflated attribution; test them first.

## 10. Choosing attribution settings per platform

| Platform | Recommended starting setting | Change it when | Watch out |
|----------|------------------------------|----------------|-----------|
| Google Ads | Data-driven, 30-day click for purchases; 90-day click for long B2B cycles; engaged-view default for YouTube | Purchase lag analysis (time to conversion report) shows most conversions outside the window | Changing windows changes reported history going forward, not backward; tell google-ads |
| Meta | 7-day click and 1-day view for ecommerce; 1-day click for impulse or when view inflation is a concern; compare with incremental attribution in a split before adopting | Lift tests show view-through conversions are not incremental for the account | Setting affects optimization, not only reporting; switching resets comparisons |
| TikTok | 7-day click, 1-day view | Same logic as Meta | View-through heavy for upper funnel video |
| LinkedIn | 30-day click, 7-day view for B2B; tie to CRM outcomes | Sales cycle analysis | Long windows overlap with other B2B channels |
| Microsoft | 30-day click, DDA where available | As Google | Imported Google settings may not match |
| GA4 | Data-driven with default lookbacks; compare against paid and organic last click in the model comparison report | Never change just to make a channel look better | Model changes apply to historical reports (no locked history) |

## 11. Worked reconciliation example (September 2026, ecommerce)

| Source | Purchases | Ratio to backend | August ratio | Note |
|--------|-----------|------------------|--------------|------|
| Backend (net of cancellations) | 2,140 | 1.00 | 1.00 | Shopify |
| GA4 (all channels) | 1,862 | 0.87 | 0.88 | Stable; EEA capture 0.71, rest 0.93 |
| Google Ads (DDA, 30d click) | 905 | 0.42 | 0.41 | Stable |
| Meta (7d click 1d view) | 1,120 | 0.52 | 0.61 | Dropped after engage-through split; annotate, not a performance change |
| TikTok (7d click 1d view) | 210 | 0.10 | 0.09 | Stable |
| Sum of platforms | 2,235 | 1.04 | 1.11 | Overlap fell with Meta change |

Reading: GA4 capture is stable, so on-site tracking is healthy. Meta's ratio change is explained by the March 2026 definition change being applied to a new reporting connector this month; rebaseline Meta targets with meta-ads. Next step: geo test on Meta (largest spend) to replace ratios with an incrementality factor. Numbers in this table are illustrative, not benchmarks.
