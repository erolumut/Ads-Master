# ASO for Google Play

> Knowledge as of 2026-10. Google Play changed a lot in 2026: Gemini powered keyword to listing drafts and CSV localization (I/O 2026, 2026-05-19), store listing experiments moved under Store listings with new click based metrics (reported 2026-07, [Contested] details), Engage SDK content on store listings (from 2026-06), Play Shorts and Ask Play discovery surfaces, target API 36 (2026-08-31), developer verification in 4 countries (2026-09-30) and a new fee structure (2026-06-30). Verify against the Freshness Protocol.

## 1. Store listing fields

| Field | Limit | Indexed | Notes |
|-------|-------|---------|-------|
| App name (title) | 30 characters | Yes, highest weight | Policy bans ranking or performance claims ("#1", "best", "top"), price or promo words ("free", "sale") and emoji or repeated special characters in title, icon and developer name [Official, Metadata policy, verify current text] |
| Short description | 80 characters | Yes | Visible on the listing; strong conversion lever |
| Full description | 4,000 characters | Yes | Unlike iOS, the description is indexed. Use primary keywords naturally 3 to 5 times; keyword stuffing violates the Metadata policy |
| App icon | 512 x 512 PNG | No | Same constraints on text in icon (no ranking or promo claims) |
| Feature graphic | 1024 x 500 | No | Shows with the promo video and in some browse placements |
| Screenshots | 2 to 8 per device type (phone, 7 inch, 10 inch, Chromebook, Wear, TV, XR as relevant) | No | First 3 to 4 visible without scrolling |
| Promo video | YouTube URL | No | Ads must be disabled on the video; landscape or portrait accepted [Practitioner consensus, verify] |
| Developer name and page | Account level | Yes | |
| Category and tags | One category, up to 5 tags (tags affect browse and similar apps) | Yes for discovery | Choose tags deliberately; Play shows them as chips [Practitioner consensus] |

## 2. Keyword and listing procedure

1. Build the term map as in [ASO for the App Store](aso-app-store.md) section 2, then adapt: on Play, the full description is indexed, so long tail coverage lives there.
2. Use Play Console > Grow > Store performance > search terms (Play Console shows top search terms that led to store listing visits and installs) [Official].
3. Use the Grow overview keyword recommendations. Since I/O 2026, clicking a keyword recommendation lets Gemini draft a custom store listing tailored to that keyword, deployable in one click [Official, 2026-05]. Review every AI draft against brand/CLAIMS.md before publishing (G3 gate).
4. Localize with the structured file upload (CSV or Google Sheet) that Play Console pre-populates with Gemini translations for review [Official, 2026-05]. Native review is still required for the top 5 markets.
5. Change one listing element at a time per locale, wait 2 to 3 weeks, read store listing acquisitions and conversion by search term.

## 3. Ranking and quality signals

| Signal | Evidence |
|--------|----------|
| Keyword relevance in title, short and full description | [Official guidance + Practitioner consensus] |
| Install velocity, conversion rate, uninstalls and engagement | [Practitioner consensus] |
| Ratings (Google weights recent ratings more heavily; no manual reset) | [Official] |
| Android vitals: bad behavior thresholds of 1.09% user perceived crash rate and 0.47% user perceived ANR rate overall, and 8% on any single phone model; apps above them can lose visibility and show warnings on the listing | [Official, 2023 thresholds, verify current] |
| Target API: new apps and updates must target Android 16 (API 36) since 2026-08-31 (extension to 2026-11-01 on request); existing apps below API 35 stop being discoverable to new users on newer devices | [Official, 2026] |
| Developer verification: from 2026-09-30, installs on certified devices in Brazil, Indonesia, Singapore and Thailand require a verified developer; global in 2027 | [Official, 2026] |

Rule: an Android vitals breach is an ASO incident. Hand the crash and ANR fix to the app team and log it in INCIDENTS.md; no metadata work outranks it.

## 4. Custom store listings

- Up to 50 custom store listings per app, each with its own app name, icon, descriptions and graphics [Official, 2026].
- Targeting options: country, user or buyer state (for example inactive users), search keyword, pre-registration, Google Ads campaigns, and unique listing URLs per campaign [Official].
- Use cases by priority:
  1. Keyword listings for high value search clusters (one listing per intent cluster, message matched to the query).
  2. Country listings where local creative and claims differ.
  3. Lapsed user listings that show what is new (pairs with ACe and lifecycle-crm win-back).
  4. Google Ads campaign listings that match ad creative.
  5. Pre-registration listings with the launch reward.
- Measure each listing on conversion rate and downstream retention (Play Console now offers traffic source breakdowns for engagement, retention and monetization [Official, 2026-05]).

## 5. New 2026 surfaces on Google Play

| Surface | What it is | Action |
|---------|-----------|--------|
| Play Shorts | Full screen portrait short video feed on the store, rolling out to US users and select developers | Prepare 9:16 15 to 45 second videos showing real use; reuse the strongest ad concepts [Official, 2026-05] |
| Ask Play and Ask Play highlights | AI search overlay for conversational queries and summaries on the search results page | Write descriptions that answer "which app for X" questions plainly; keep claims verifiable [Official, 2026-05] |
| AI Q&A on listings | Answers user questions about the app (Google says 95% of user queries answered) | Keep the description and data safety section accurate; wrong answers usually come from vague listings [Official, 2026-05] |
| Gemini app discovery | Gemini suggests apps during searches; later deep links into app content for entertainment | Make sure App Links and content deep links work (see deep linking reference) [Official, 2026-05] |
| Engage SDK on store listings | Existing users see Engage SDK content on your listing (from 2026-06); surfaces reach 80+ markets | Integrate Engage SDK for content and commerce apps; coordinate with lifecycle-crm [Official, 2026-05] |
| Reach metric | Total app visibility on Play including indirect value | Add to the weekly ASO read [Official, 2026-05] |

## 6. Pre-registration

- Run a pre-registration period of 2 to 12 weeks before launch with a custom store listing and an optional pre-registration reward.
- Google App campaigns for pre-registration (ACpre, Android only) need daily budget at least 50x the bid [Official].
- Launch day: pre-registered users receive an auto install or notification depending on settings; prepare servers and ratings prompts for the spike.

## 7. Promotional content (formerly LiveOps)

- Promotional content cards appear in Play browse surfaces and on the listing for time limited events, offers and major updates [Official].
- Plan a calendar aligned with in-app events on iOS (see [Ratings, reviews and in-app events](ratings-reviews-and-in-app-events.md)).
- Eligibility, submission lead time and card formats change; check the Play Console Help page before planning [Unverified current eligibility rules].

## 8. Graphics and conversion

- First screenshot: outcome plus product in use; Play shows screenshots larger on tablets and Chromebooks, so supply device specific sets.
- Feature graphic: one message, no small text.
- Video: show the app in the first 2 seconds.
- Localize graphics for the top revenue markets.
- Data safety section and ratings display near the top of the listing; inaccurate data safety answers are both a policy and a conversion risk.

## 9. Measurement in Play Console

| Report | Use |
|--------|-----|
| Store performance: store listing visitors, acquisitions, conversion rate by source and search term | Core ASO funnel |
| Store listing experiments results | See [Experiments and custom pages](store-listing-experiments-and-custom-pages.md) |
| Statistics: installs, uninstalls, user acquisition by channel | Trend checks; historical store listing acquisitions and conversion remain here after the 2026 experiment changes [Practitioner consensus, 2026-08] |
| Cart conversion rate, subscriber tenure, churn reasons (new at I/O 2026) | Monetization diagnostics; share with lifecycle-crm [Official, 2026-05] |
| Android vitals | Crash and ANR rates against bad behavior thresholds |
| Ratings and reviews | Average, distribution, replies, rating change with and without replies [Official] |

## 10. Mistakes to prevent

1. Title with "Free", "#1" or emoji: listing rejection under the Metadata policy.
2. Keyword stuffed full description: policy risk and lower conversion.
3. Ignoring Android vitals while optimizing screenshots.
4. One global listing for all countries when custom store listings are free to use.
5. Publishing Gemini drafted listings without a claims review.
6. Running a store listing experiment while launching a big paid campaign to the same listing (traffic mix changes the result).
7. Missing the target API deadline: the app keeps its listing but cannot ship updates until it complies.

## 11. Weekly Play ASO read (15 minutes)

1. Store listing visitors, acquisitions and conversion rate by source (search, explore, external) vs prior 4 weeks.
2. Top 20 search terms by visitors and conversion; terms with high visitors and low conversion get a custom store listing candidate.
3. Ratings average (7 day) and new 1 to 2 star themes.
4. Android vitals vs bad behavior thresholds.
5. Experiments and custom store listings status.
6. Competitor listing changes (ASO tool).
7. Log findings and changes in the journal.

## 12. Worked example: keyword cluster listing

Situation (illustrative): a budgeting app sees "expense tracker" as a top search term with conversion 30% below the listing average.
1. Create custom store listing CSL-03 targeted to the search keyword "expense tracker" (G2 draft).
2. Title stays the brand name plus "Expense Tracker"; short description leads with receipt scanning; first screenshot shows the expense list with categories.
3. Gemini draft reviewed against brand/CLAIMS.md; publish after approval (G3).
4. Measure keyword conversion for 3 weeks vs the prior 3 weeks and vs the default listing on similar terms.
5. Keep, iterate or retire; log the result in EXPERIMENTS.md.

## 13. Market priorities on Android

- Android dominates installs in India, Indonesia, Brazil, much of Latin America, Türkiye and Africa; iOS dominates revenue share in the US, Japan and parts of Western Europe [Practitioner consensus]. Localize Play listings first for Android heavy growth markets.
- Price localization: Play allows local prices per country; review subscription price points after the 2026 fee changes and each currency move.
- Payment methods: carrier billing and local wallets matter in emerging markets; check Play's available forms of payment per country before setting price tests.
- Developer verification (2026-09-30) affects only installs outside Play for most developers, but marketplaces and OEM store distribution in Brazil, Indonesia, Singapore and Thailand now require verification [Official].

## 14. Listing policy checklist (before publishing)

- [ ] Title, icon and developer name free of ranking claims, price or promo words, emoji and repeated special characters.
- [ ] No keyword repetition that reads unnaturally in the full description.
- [ ] Screenshots and video show the real app; no misleading device frames or fake UI.
- [ ] Data safety section matches the SDKs in the current build.
- [ ] Claims in all text and graphics approved in brand/CLAIMS.md.
- [ ] Custom store listings and experiments use only approved assets; AI generated assets declared where Play asks [Unverified requirement].
