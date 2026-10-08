# Store Listing Experiments and Custom Pages

> Knowledge as of 2026-10. Apple: 70 custom product pages with keywords (2025-10-29), new creative assets usable in custom product pages and Product Page Optimization (2026-10-05), streamlined submission that bundles IAPs with In-App Events, custom product pages and PPO tests (WWDC26). Google: 50 custom store listings, store listing experiments moved under Store listings with click based metrics (reported 2026-07, [Contested]). Verify before planning.

## 1. Which tool for which question

| Question | Apple | Google |
|----------|-------|--------|
| Which creative converts best on the default page? | Product Page Optimization (PPO) | Store listing experiments |
| Which page converts best for a specific audience, ad or keyword? | Custom product pages (CPP) with Apple Ads ad variations, campaign links and assigned keywords | Custom store listings (by country, keyword, user state, Google Ads campaign or URL) |
| Does this creative change downstream quality? | Compare CPP cohorts by retention and revenue in the MMP or App Store Connect | Store listing experiments results plus traffic source retention breakdowns |

## 2. Apple Product Page Optimization

Settings and rules:
- Up to 3 treatments against the original; set the share of traffic in the test; choose localizations; run up to 90 days [Official].
- Testable: icon (alternate icons must be included in the app binary), screenshots, app previews, and the new creative assets (headers, search result assets) per Apple's 2026 asset release [Official, 2026-10].
- Traffic: PPO applies to users who land on the default product page (search, browse, referrals that use the default page); traffic sent to a CPP does not enter the PPO test [Official].
- One active test per app at a time [Official].
- Plan tests between releases; a new version release can interrupt a running test [Practitioner consensus, verify in App Store Connect Help].
- Results: App Store Connect shows estimated conversion rate, improvement vs original and confidence. Apply the winning treatment to the default page from the results screen.

Procedure:
1. Hypothesis in EXPERIMENTS.md: "If frame 1 shows the outcome instead of the feature list, conversion rate rises at least 8% relative, because search users decide in under 3 seconds."
2. Size the test (section 5). If the app has fewer than about 3,000 product page views per treatment per 2 weeks, test bigger changes (concept, not color).
3. Freeze other changes: no metadata edits, no big paid bursts to the default page, no seasonal campaign switch during the test.
4. Run at least 14 days and a full weekly cycle; stop at the planned sample, not at the first significant read.
5. Read conversion and, for the winner, downstream D7 retention or trial rate of the cohort window if the MMP can split by date.
6. Ship the winner, log the learning in creative-library/registry.csv and memory if confirmed twice.

## 3. Apple custom product pages

Facts:
- Up to 70 custom product pages per app (raised from 35 on 2025-10-29) [Official, 2025-10].
- Each CPP has its own screenshots, app previews, promotional text and the new creative assets, and a unique URL (the `ppid` parameter) [Official].
- Keywords can be assigned to CPPs so they can appear in organic search results for those terms [Official, 2025-10; vendors date the rollout to 2025-07].
- CPPs can carry a deep link so that users who already have the app open the matching content (iOS 18 and later) [Official, 2024-06].
- Apple Ads uses CPPs as ad variations in search results, Search tab and Today tab campaigns [Official]. One third-party guide says Today tab ads require a CPP [Unverified].
- CPPs and In-App Events, IAPs and PPO tests can be submitted together under the streamlined submission flow announced at WWDC26 [Official, 2026-06].

CPP portfolio plan (Growth tier and above):

| CPP | Audience or intent | Used by | Keywords assigned |
|-----|-------------------|---------|-------------------|
| CPP-01 Core outcome | Generic category search | Apple Ads category ad group | Category head terms |
| CPP-02 Feature A | Users searching the feature | Apple Ads feature ad group | Feature terms |
| CPP-03 Competitor switchers | Competitor brand searches (paid only) | Apple Ads competitor campaign | None (never assign competitor brands organically) |
| CPP-04 Persona (for example students) | Paid social creative for that persona | Meta, TikTok, networks via store URL with ppid | Persona terms if relevant |
| CPP-05 Seasonal | Holiday or event | Today tab, in-app event period | Seasonal terms |
| CPP-06 Lapsed users | Re-engagement | Apple Ads returning users, CRM links | None |
| CPP-07 Localized market | Market specific messaging | Market campaigns | Local terms |

Rules:
- Message match: the first frame of the CPP repeats the ad's promise.
- One CPP per ad group or creative concept, not per ad.
- Keep a CPP registry: ID, URL, assets, keywords, deep link, campaigns using it, launch date, conversion rate, status.
- Retire CPPs that convert below the default page after 2 weeks of comparable traffic.

## 4. Google Play store listing experiments and custom store listings

Store listing experiments (state as of 2026-10):
- Experiments are now managed inside Store listings: open the listing to test or use "Set up" from the Store listings overview [Practitioner consensus, 2026].
- Limits: one default graphics experiment (icon, feature graphic, screenshots) or up to five localized experiments per app at a time; localized experiments can test text and graphics [Official help, verify current limits].
- Target metric: older Help pages list "Retained first-time installers" as the recommended default. 2026 reports say Google replaced first-time installers and retained first-time installers with unique user install clicks and unique user open clicks, with data for the new metrics starting 2026-07-10, single variant recommended and an AI asset declaration required [Contested: Yellowhead and Phiture report it, Google has not announced it]. Check the Target metric dropdown in the live Play Console.
- Install clicks count the tap on Install, not a completed install [Practitioner consensus, 2026-08]. Treat click based wins as provisional until retention data agrees.

Custom store listings: see [ASO for Google Play](aso-google-play.md) section 4 (up to 50, targeting by country, user state, keyword, Google Ads campaign, URL).

## 5. Test sizing and reading

Sample size per arm (two sided, 5% significance, 80% power) for a conversion rate:

n ≈ 16 x p x (1 minus p) / d^2, where p is the baseline conversion rate and d is the absolute lift to detect.

| Baseline conversion | Relative lift to detect | Absolute d | Visitors per arm |
|---------------------|-------------------------|-----------|------------------|
| 30% | 10% | 3.0 pp | 3,733 |
| 30% | 5% | 1.5 pp | 14,933 |
| 50% | 10% | 5.0 pp | 1,600 |
| 15% | 10% | 1.5 pp | 9,067 |

Rules:
- Run at least 7 full days, ideally 14 to 28, to include weekday and weekend mix.
- Do not peek and stop early; platform confidence displays are not a license to stop.
- Watch for traffic mix shifts (featuring, paid bursts, seasonality). If one occurs, extend or restart.
- Read the downstream metric for the winner: a screenshot that over-promises can raise conversion and cut D1 retention.
- Treat a "no difference" result as a learning; log it.

## 6. What to test first (priority order)

| Rank | Element | Why |
|------|---------|-----|
| 1 | First screenshot or first frame of the set (concept level) | Visible in search results; largest effect sizes |
| 2 | Icon | Affects search tap rate and recognition; Apple needs it in the binary |
| 3 | Search result creative asset or header (Apple, iOS 27) | New surfaces; early movers learn first [Practitioner hypothesis] |
| 4 | Screenshot order and social proof frame | Medium effect |
| 5 | App preview presence and first 3 seconds | Can help or hurt; test it |
| 6 | Short description (Play) | Indexed and visible; test copy angles |
| 7 | Color and style tweaks | Small effects; only at Scale tier traffic |

## 7. Experiment row template (append to EXPERIMENTS.md)

| ID | Date | Agent | Hypothesis | Primary metric | ICE | Design | Stop rule | Status |
|----|------|-------|-----------|----------------|-----|--------|-----------|--------|
| E0xx | YYYY-MM-DD | mobile-app-growth | If frame 1 shows <outcome>, then product page conversion rises 8% relative, because <evidence> | PPO conversion rate (default page, US English) | 4/3/5 | PPO, 2 treatments, 50% traffic | 14 days minimum and 3,800 visitors per arm, or 28 days | backlog |

## 8. Mistakes to prevent

1. Testing 3 treatments on low traffic apps: no result for months.
2. Sending paid traffic to the default page during a PPO test, then crediting the creative.
3. Building CPPs without wiring them to ad groups or campaigns.
4. Assigning competitor brand keywords to a CPP (trademark and review risk).
5. Declaring a Play experiment winner on install clicks when D1 retention fell.
6. Forgetting to apply the winning treatment, so the default page keeps the loser.

## 9. CPP and custom listing registry (CSV header)

Keep it at `ads-master/data/cpp_registry.csv` (project state, not in this skill):

```
page_id,store,name,url_or_ppid,audience_or_intent,keywords_assigned,deep_link,assets_version,campaigns_using,launch_date,conversion_rate_28d,default_page_cr_28d,status,notes
CPP-02,ios,Feature receipts,ppid=<id>,feature search,"receipt scanner,scan receipts",app://scan,v3,AA_US_SR_CATEGORY_receipts,2026-09-01,,,live,
CSL-03,android,Expense tracker,listing=<id>,keyword expense tracker,expense tracker,,v1,ACI_US_AND_tCPA_trialstart_outcome_v2,2026-09-15,,,live,
```

## 10. Reading a PPO result (worked example)

Illustrative numbers: original conversion 31.0%, treatment B 33.4% after 21 days, about 9,000 impressions per arm, App Store Connect shows B improving conversion with high confidence.
1. Check traffic stability: no featuring or Apple Ads bursts to the default page during the test window.
2. Absolute lift 2.4 pp on a 31% base needs about 6,000 visitors per arm by the section 5 formula; 9,000 is enough.
3. Check the downstream quality signal for the test weeks (D1 retention, trial rate by install week).
4. Apply B, log it, and plan the next test on the next ranked element.

## 11. Setting up a Play custom store listing (steps)

1. Play Console > Grow > Store presence > Custom store listings > Create listing.
2. Choose the targeting (country, pre-registration, inactive users, search keyword, Google Ads campaign or URL) [Official].
3. Enter the title, short and full description and graphics; reuse approved assets.
4. Save as draft (G2), request approval, publish (G3).
5. For campaign listings, copy the listing URL into the Google Ads campaign or ad network store link.
