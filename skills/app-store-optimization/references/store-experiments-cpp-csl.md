# Store Experiments, Custom Product Pages and Custom Store Listings

> Knowledge as of 2026-10. Moved from `mobile-app-growth` and updated with the 2026-10-12 pass (search summaries only). Apple PPO rules are long standing [Official]. The custom product page cap is [Contested] (70 vs 35). Play experiment limits and metrics changed in 2026 [Reported, 2026-10].

Ownership: `app-store-optimization` creates, tests and maintains custom product pages (CPP) and custom store listings (CSL), runs PPO and Play experiments, and keeps the registry. `mobile-app-growth` uses the pages in Apple Ads ad variations, Google App campaigns and paid social store links, and reports paid conversion per page back into the registry.

## 1. Which tool answers which question

| Question | Apple | Google |
|----------|-------|--------|
| Which creative converts best on the default page? | Product Page Optimization (PPO) | Store listing experiments |
| Which page converts best for one audience, ad or keyword? | Custom product pages, used by Apple Ads, campaign links and keyword assignment | Custom store listings by country, keyword, user state, buyer segment, campaign or URL |
| Does a change hurt downstream quality? | Compare cohorts by install week (retention, trial rate) | Same, plus Play Console traffic source breakdowns |

## 2. Apple Product Page Optimization

Settings and rules [Official] unless labeled:
- Up to 3 treatments against the original; you set the traffic share and the localizations; one test per app at a time; up to 90 days.
- Testable: icon (alternate icons in the binary), screenshots, app previews, and the 2026 header and search result assets [Reported, 2026-10].
- Traffic: users who land on the default product page. Traffic sent to a custom product page does not enter the test.
- A new app version can interrupt a running test [Practitioner consensus]; schedule tests between releases.
- Results show estimated conversion, improvement vs original and confidence; apply the winner from the results screen.

Procedure:
1. Hypothesis row in EXPERIMENTS.md: "If frame 1 shows the outcome instead of the feature list, conversion from search rises at least 8% relative, because search users decide in seconds."
2. Size the test (section 6). With fewer than about 3,000 product page views per treatment in 2 weeks, test bigger changes (a concept, not a color) and fewer treatments.
3. Freeze everything else on the default page: metadata, paid bursts to the default page, seasonal swaps.
4. Run at least 14 days and full weeks; stop at the planned sample, not at the first significant read.
5. Read conversion, then the downstream signal for the test weeks (D1 retention, trial rate by install week).
6. Apply the winner (G3), log it, register the concept in `creative-library/registry.csv`, write memory only after the pattern repeats.

## 3. Apple custom product pages

| Fact | Evidence |
|------|----------|
| Page count: 70 per app per Apple's 2025-10-29 notice as reported by Adapty and Moburst; some help pages and older guides still say 35 | [Contested]; count the limit shown in App Store Connect before planning past 35 |
| Each page has its own screenshots, previews, promotional text and the 2026 assets, and a unique URL with the `ppid` parameter | [Official] for screenshots, previews, promotional text and URL; 2026 assets [Reported, 2026-10] |
| Keyword linked pages can appear in organic search for assigned keywords since 2025-07-30 | [Reported, 2026-10] |
| The keyword must come from the app's existing keyword field (whether name and subtitle words also qualify is not documented); a keyword can be assigned to only one page; the assignment needs review | [Reported, 2026-10] |
| A page can carry a deep link to matching in-app content for users who have the app (iOS 18 and later) | [Official, 2024-06] (moved) |
| Apple Ads uses pages as ad variations | [Official] |
| Pages, in-app events, IAPs and PPO tests can be submitted together (WWDC26) | [Official, 2026-06] (moved) |

What keyword linked pages do and do not do:
- They raise conversion for a term the app already indexes, by showing a matched page in organic results for that term.
- They do not add keyword coverage: the term must already be in the keyword space (the law "CPP keyword pages use existing keyword space").
- More pages do not mean more organic reach. A page earns its slot only when its term converts better on the matched page.

Selecting keywords for pages:
1. From the term map, take live terms with rank 1 to 30, popularity in the top half, and conversion below the default page average (or a clear intent mismatch with the default screenshots).
2. Group by cluster: one page per cluster, each keyword assigned to only one page (Apple allows one page per keyword).
3. Frame 1 repeats the query's job in plain words.
4. Read with the protocol in [Keyword research](keyword-research-and-rank-tracking.md) section 7: conversion for that term before vs after, against control terms.

Portfolio plan (Growth tier and above):

| Page | Audience or intent | Built by | Used by | Keyword assigned |
|------|-------------------|----------|---------|------------------|
| CPP-01 Core outcome | Category head term | app-store-optimization | Apple Ads category ad group; organic | Category head term |
| CPP-02 Feature A | Feature searchers | app-store-optimization | Apple Ads feature ad group; organic | Feature term from the keyword field |
| CPP-03 Competitor switchers | Competitor brand searches (paid only) | app-store-optimization | Apple Ads competitor campaign (`mobile-app-growth`) | None, never a competitor brand |
| CPP-04 Persona | Paid social persona creative | app-store-optimization with creative-strategy | Meta, TikTok, networks via `ppid` links | Persona term if relevant |
| CPP-05 Seasonal | Event or holiday | app-store-optimization | Today tab, in-app event period | Seasonal term in the keyword space |
| CPP-06 Lapsed users | Re-engagement | app-store-optimization | Apple Ads returning users, CRM links | None |
| CPP-07 Market | Market specific message | app-store-optimization | Market campaigns | Local term |

## 4. Google Play store listing experiments

State as of the 2026-10-12 pass [Reported, 2026-10] (Play Console Help answer 12053285 seen in search summaries, plus Yellowhead and Phiture):
- One default graphics experiment, or up to five localized experiments, at a time.
- Up to two variants against the current listing (older help copies said three).
- Target metrics: unique user install clicks, unique user open clicks, pre-registration clicks (older copies said retained first-time installers).
- Confidence level and minimum detectable effect are adjustable.
- Experiments stop automatically after 6 months.
- Experiments are managed inside Store listings [Practitioner consensus, 2026].
- An AI generated asset declaration [Unverified].
- No official minimum run time; 7 to 14 days is the common rule of thumb [Practitioner consensus].

Install clicks count the tap on Install, not a completed install or a retained user. Treat a click based win as provisional until the cohort's D1 retention agrees.

## 5. Google Play custom store listings

| Fact | Evidence |
|------|----------|
| Up to 50 custom store listings per app, each with its own title, icon, descriptions and graphics | [Official] |
| Targeting: country, pre-registered users, search keywords, lapsed or churned users, buyer segments, and Google Ads App campaign ad group IDs | [Reported, 2026-10] (Play Console Help 9867158, Google Ads Help 16742242) |
| Only one custom listing can target a given country at a time | [Reported, 2026-10] |
| Custom listings are not auto translated | [Reported, 2026-10] |
| Gemini can draft a keyword targeted listing from a Grow keyword recommendation | [Reported, 2026-10] |

Priority of use:
1. Keyword listings for high value search clusters with weak conversion (Play's version of keyword linked pages).
2. Country listings where creative or claims differ.
3. Lapsed or churned user listings that show what is new (pairs with `lifecycle-crm` win-back and paid re-engagement).
4. Ad group listings that match paid creative (`mobile-app-growth` links them).
5. Pre-registration listings with the launch reward.

Setup steps:
1. Play Console > Grow > Store presence > Custom store listings > Create listing.
2. Choose the targeting; for keyword targeting, pick the cluster's head term from the term map.
3. Enter title, short and full description and graphics from approved assets; translate by hand where needed.
4. Run `aso_metadata_check.py` and compliance; save as draft (G2); request approval; publish (G3).
5. For ad group listings, give the listing ID to `mobile-app-growth`.

## 6. Test sizing and reading

Sample size per arm (two sided, 5% significance, 80% power) for a conversion rate:

`n ≈ 16 x p x (1 minus p) / d^2`, where p is the baseline conversion and d is the absolute lift to detect.

| Baseline conversion | Relative lift | Absolute d | Visitors per arm |
|---------------------|--------------:|-----------:|-----------------:|
| 30% | 10% | 3.0 points | 3,733 |
| 30% | 5% | 1.5 points | 14,933 |
| 50% | 10% | 5.0 points | 1,600 |
| 15% | 10% | 1.5 points | 9,067 |

Rules:
- Full weeks: at least 7 days, ideally 14 to 28.
- No peeking and stopping on a platform confidence badge.
- Watch traffic mix (featuring, paid bursts, seasonality); if mix shifts, extend or restart.
- Read the downstream metric for the winner: an over-promising screenshot can raise conversion and cut D1 retention.
- A "no difference" result is a learning; log it.
- Low traffic apps: fewer arms, bigger changes, or sequential before and after reads with control terms (weaker evidence; label it).

## 7. What to test first

| Rank | Element | Why |
|------|---------|-----|
| 1 | First screenshot or the concept of frames 1 to 3 | Visible in search results; largest effects [Practitioner consensus] |
| 2 | Icon | Search tap rate and recognition |
| 3 | 2026 search result asset or header (Apple) | New surface; specs [Unverified] [Practitioner hypothesis] |
| 4 | Screenshot order and the proof frame | Medium effect |
| 5 | Preview presence and its first 3 seconds | Can help or hurt |
| 6 | Play short description | Indexed and visible; test angles in localized experiments |
| 7 | Color and style | Small effects; only with Scale tier traffic |

## 8. Experiment row template (EXPERIMENTS.md)

| ID | Date | Agent | Hypothesis | Primary metric | ICE | Design | Stop rule | Status |
|----|------|-------|-----------|----------------|-----|--------|-----------|--------|
| E0xx | YYYY-MM-DD | app-store-optimization | If frame 1 shows <outcome>, conversion from search rises 8% relative, because <evidence> | PPO conversion, default page, US English | 4/3/5 | PPO, 2 treatments, 50% traffic | 14 days minimum and 3,800 visitors per arm, or 28 days | backlog |

## 9. CPP and CSL registry

Path: `ads-master/data/cpp_registry.csv` (shared with `mobile-app-growth`; each agent updates its own columns).

```
page_id,store,name,url_or_ppid,audience_or_intent,keyword_assigned,keyword_in_keyword_space,deep_link,assets_version,campaigns_using,launch_date,organic_cr_28d,paid_cr_28d,default_page_cr_28d,status,owner_notes
CPP-02,ios,Feature receipts,ppid=<id>,feature search,receipt scanner,yes,app://scan,v3,AA_US_SR_CATEGORY_receipts,2026-09-01,,,,live,
CSL-03,android,Expense tracker,listing=<id>,keyword expense tracker,expense tracker,na,,v1,ACI_US_AND_tCPA_trialstart_outcome_v2,2026-09-15,,,,live,
```

Retire a page that converts below the default page for 2 weeks of comparable traffic; keep the row with status `retired`.

## 10. Reading a PPO result (worked example)

Illustrative: original 31.0%, treatment B 33.4% after 21 days, about 9,000 impressions per arm, App Store Connect shows B ahead with high confidence.
1. Traffic stable: no featuring or Apple Ads bursts to the default page in the window.
2. Sample: 2.4 points on a 31% base needs about 6,000 visitors per arm by the section 6 formula (16 x 0.31 x 0.69 / 0.024 squared ≈ 5,942); 9,000 is enough.
3. Downstream: D1 retention and trial rate by install week unchanged.
4. Apply B (G3), log it, plan the next test on the next ranked element.

## 11. Mistakes to prevent

1. Three treatments on a low traffic app: no answer for months.
2. Sending paid traffic to the default page during a PPO test, then crediting the creative.
3. Building pages nobody links: every page needs an ad group, a link or a keyword.
4. Assigning a keyword that is not in the keyword space, or a competitor brand.
5. Declaring a Play winner on install clicks while D1 retention fell.
6. Forgetting to apply the winner, so the default page keeps the loser.
7. Planning 70 pages before checking the live cap.
