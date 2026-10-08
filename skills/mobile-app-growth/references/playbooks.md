# Playbooks: Launch, Optimize, Scale, Recover

> Knowledge as of 2026-10. Every play produces a change list for human approval. Platform entities are created PAUSED or unsubmitted (G2); activation, publishing, bids, budgets, prices and customer facing replies are G3. Respect the project's automation stage in ads-master/GUARDRAILS.md.

## Play 1: Pre-launch to day 90 for a new app

### Weeks minus 8 to minus 1 (pre-launch)
1. Unit economics draft: price points, expected install to paid, payback target ([Unit economics](app-growth-model-and-unit-economics.md)).
2. Measurement level 2 ready: MMP or RevenueCat, SKAN or AAK schema, Firebase or AAP linked to Google, Meta SDK or MMP to Meta, AdServices for Apple Ads ([Measurement](mobile-measurement-skan-aak-mmp.md)).
3. Deep links: universal links and App Links verified; QA matrix passed ([Deep linking](deep-linking-and-web-to-app.md)).
4. ASO baseline: keyword map, name and subtitle, screenshots v1 and v2 for PPO, localization for the top 3 markets, privacy labels and Data safety accurate.
5. Pre-orders (App Store) or pre-registration (Play) with a custom store listing; ACpre if budget allows (50x bid daily).
6. Ratings plan: prompt triggers defined; feedback entry in settings.
7. Paywall v1 and v2 in the paywall tool, remote configurable.
8. Featuring nomination submitted 6 to 8 weeks before launch.
9. Creative pack: 6 to 10 videos across 3 concepts, store screenshots, playable if gaming.

### Days 0 to 14
1. Launch Apple Ads BRAND and CATEGORY exact (G3 activation), Google ACi Install volume per OS where relevant, one Meta or TikTok app campaign per OS at a budget that can reach about 50 install events per week.
2. Daily: crashes, spend pacing, tracking sanity (installs in MMP vs store), first reviews.
3. Reply to all reviews within 72 hours.
4. No metadata changes in the first 7 days unless there is an error (let indexing settle).

### Days 15 to 45
1. First PPO test on screenshots frame 1.
2. Apple Ads DISCOVERY harvest weekly; add COMPETITOR if approved.
3. Paywall test 1 (placement or plan default).
4. Move Meta, TikTok and Google from installs to the bid event when volume allows.
5. First SKAN schema validation against Android or consented cohorts.

### Days 46 to 90
1. Unit economics refresh from real cohorts; set targets per channel.
2. Custom product pages for each Apple Ads theme and the top paid social concepts.
3. Second locale wave.
4. Decide channel 3 or 4 (TikTok, networks, web to app) using payback and measurement readiness.
5. Write the 90 day review (outputs) and the next quarter test plan.

## Play 2: Weekly optimization loop (Growth tier)

| Step | Time | Detail |
|------|------|--------|
| 1. Data sanity | 10 min | QA table in measurement module; stop if bid events broke |
| 2. KPI table | 10 min | Spend, installs, cost per bid event, net revenue per install D7, payback progress by channel and OS; platform vs MMP vs backend |
| 3. Store funnel | 10 min | Conversion rate by source, keyword ranks, ratings, active tests |
| 4. Channel actions | 20 min | Apple Ads harvest and bids; Google targets; Meta and TikTok creative kill and scale; networks publisher blocklists |
| 5. Monetization | 10 min | Paywall test status, trial to paid trend, refunds |
| 6. Experiments | 5 min | Close, log learnings, launch next |
| 7. Change list and journal | 10 min | Approval request, handoffs |

## Play 3: Scale (from Growth to Scale tier)

Entry criteria: payback at or better than target for 4+ weeks in the core channel, measurement level 3, creative throughput of at least 5 new concepts per week, paywall tested at least twice.

1. Budget steps: +20% to +30% per week on campaigns with CPA or ROAS within target and budget capped; duplicate for 2x jumps on Meta and TikTok rather than editing a stable campaign.
2. Expand markets: rank by price parity (store price tiers), ASO opportunity, CPI benchmarks, language support. Launch localized store pages before paid.
3. Add channels in order of fit: Apple Ads placements beyond search results, Google tROAS split test, TikTok AEO or VBO, one ML network or DSP as a test cell (protocol in [Meta, TikTok and networks](meta-tiktok-and-network-app-campaigns.md) section 5).
4. Web to app: for subscription apps with US weight, launch a web funnel test on Meta and an IAP vs link out paywall test.
5. Incrementality: first geo holdout on the largest channel; set calibration factors in MEASUREMENT.md.
6. Creative system: weekly concept testing, playables for games, CPP per winning concept.
7. Watch marginal cost per payer, not average; stop scaling a channel when marginal cost per payer exceeds target for 2 weeks.

## Play 4: Plateau (growth stalls with stable costs)

1. Confirm it is a plateau, not a measurement break or seasonality (year over year, store downloads trend).
2. Find the binding constraint:
   - Store conversion below peer benchmark: creative and PPO program.
   - Search share stuck: ASO keyword expansion, CPP keywords, new locales.
   - Paid saturation (rising marginal CPA): new concepts, new channels, new markets.
   - Monetization: price and plan tests, trial length, web checkout.
   - Retention: onboarding and activation (handoff to lifecycle-crm for flows).
3. Pick 2 bets with the highest impact x confidence x ease; run as experiments with stop rules.

## Play 5: Recover from a drop

### 5.1 Installs drop (all sources)
1. Store status: app available in all storefronts, not removed, no review hold, no OS compatibility issue.
2. Crash or ANR spike (Xcode Organizer, Android vitals) after a release.
3. Ranking loss: metadata change, competitor surge, algorithm shift (compare keyword ranks).
4. Featuring ended (browse traffic drop).
5. Paid: spend dropped? Disapprovals, payment issues, budget caps.
6. Act on the cause; log in INCIDENTS.md if a stop condition applies.

### 5.2 Paid installs stable, revenue per install falls
1. Paywall or price change, store price tier change, tax change.
2. Traffic mix shift (more Android, more low ARPU countries, more network traffic).
3. Trial to paid drop (billing issues, App Store payment problems, refunds).
4. Attribution change (SKAN schema, SDK update) that only looks like a drop.

### 5.3 Apple Ads CPA up more than 30% week over week
See [Apple Ads](apple-ads.md) section 11 Recover.

### 5.4 SKAN postbacks or conversion values collapse
1. App update changed the conversion value logic or SDK version.
2. Campaign fragmentation lowered crowd anonymity tiers.
3. Network side change (ask the network).
4. Freeze bid changes on iOS campaigns that bid on SKAN values until fixed; hand off to measurement.

### 5.5 Rating crash
See [Ratings, reviews and in-app events](ratings-reviews-and-in-app-events.md) section 8.

### 5.6 App rejection or policy strike
See [Policies](policies-and-store-compliance.md) section 6.

## Play 6: Web to app launch (subscription app)

1. Feasibility: market mix (US share), plan prices, fee table ([Unit economics](app-growth-model-and-unit-economics.md) section 3), payment provider, tax approach (merchant of record or own).
2. Build: landing or quiz, web paywall, checkout, account creation, redemption link or login, entitlement sync, success page with store links. Mobile web layer checklist passed (site-engineer and cro).
3. Measurement: Pixel plus CAPI StartTrial and Purchase with value and event_id (measurement), MMP web to app, backend truth.
4. Compliance: auto renewal disclosures and cancellation path reviewed (compliance).
5. Test: Meta Sales campaign to the web funnel vs the app install campaign, equal budgets, 3 to 4 weeks; primary metric net revenue per dollar at D30.
6. Decide and scale or stop; log learnings.

## Play 7: New market expansion

1. Market sizing: downloads and revenue for the category (Sensor Tower or AppTweak), CPI ranges, language and payment preferences.
2. Store readiness: localized metadata (50 Apple languages supported), screenshots, prices per storefront, local legal requirements (age ratings, licensing such as Vietnam games, Brazil betting).
3. Measurement: country level cohorts, KVKK or GDPR consent where relevant.
4. Launch: Apple Ads CATEGORY exact in local language, Google ACi, then paid social.
5. Review at day 30 with unit economics per country.

## Play 8: Change list template (all app changes)

| # | Platform | Entity | Change | From | To | Reason with data (source, range) | Expected effect | Risk | Rollback trigger | Gate | Approval |
|---|----------|--------|--------|------|----|----------------------------------|-----------------|------|------------------|------|----------|
| 1 | Apple Ads | AA_US_SR_CATEGORY_budgeting | Max CPT keyword "budget app" | $1.40 | $1.60 | 28d: 410 taps, CPA $2.10 vs target $3.00, impression share 35% | +15% installs on term | CPA rises toward target | CPA over $3.30 for 7 days | G3 | |
| 2 | App Store Connect | CPP-04 Students | Create page (unsubmitted) | none | draft | Meta concept "students" CTR 1.6x median | Higher click to install | none until submitted | n/a | G2 | |

Read back every executed change and log it with a timestamp.
