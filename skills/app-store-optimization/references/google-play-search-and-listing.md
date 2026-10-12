# Google Play Search and Listing

> Knowledge as of 2026-10. Field limits and the Metadata policy are long standing [Official]. Findings dated 2025 to 2026 come from the 2026-10-12 pass, which read Play Console Help, the Android Developers Blog and press through search summaries only: the strongest label they earn is [Reported, 2026-10]. Single sources stay [Unverified]. Google changed Play discovery more in 2026 than in the five years before: Ask Play, review summaries, Play Shorts, Gemini listing tools and a wake lock vital.

Related modules: [Keyword research](keyword-research-and-rank-tracking.md), [Store experiments, CPP and CSL](store-experiments-cpp-csl.md), [Ratings and AI summaries](ratings-reviews-and-ai-summaries.md), [AI surfaces in the stores](ai-surfaces-in-the-stores.md) (Ask Play depth), [Policies](policies-and-metadata-compliance.md).

## 1. How Play search ranks an app

| Signal | What we know | Evidence |
|--------|--------------|----------|
| Text: title, developer name, short and full description | Play Console Help names titles, developer names and descriptions among what search weighs | [Reported, 2026-10] |
| Quality and behavior: ratings, reviews, downloads | Same help pages | [Reported, 2026-10] |
| Placement of key text | Put the most important text in the top half of the description | [Reported, 2026-10] |
| Keyword padding | Discouraged; repetitive or irrelevant keywords can lead to suspension | [Reported, 2026-10] |
| Install velocity, conversion, uninstalls, engagement | Widely observed, weights undisclosed | [Practitioner consensus] |
| Ratings recency | The public rating weights recent ratings more heavily; a new version does not reset it | [Official] |
| Android vitals | Breaching overall bad behavior thresholds likely reduces discoverability; per device breaches affect those devices and may show a warning on the listing | [Official] thresholds; discoverability wording [Reported, 2026-10] |
| Excessive partial wake locks | From 2026-03-01 apps above the threshold may be excluded from prominent discovery surfaces and get a battery warning | [Unverified] (official blog and vitals docs seen in search summaries only) |
| Featuring | No self nominations for Play featuring | [Reported, 2026-10] |

Unlike the App Store, the full description is indexed. Long tail coverage lives there, written as natural sentences.

## 2. Listing fields

| Field | Limit | Indexed | Notes |
|-------|-------|---------|-------|
| App name (title) | 30 characters | Yes, strongest | Brand plus 1 to 2 terms; Metadata policy bans rank or performance claims, price and promotion, and Google Play program references in title, icon and developer name [Official] |
| Short description | 80 characters | Yes | Visible on the listing; a conversion lever |
| Full description | 4,000 characters | Yes | Natural use of primary terms; key text in the top half |
| Character counting | Full width and half width characters count equally | | [Reported, 2026-10] |
| App icon | 512 x 512 PNG | No | Same claim limits as the title |
| Feature graphic | 1024 x 500 | No | One message, no small text |
| Screenshots | 2 to 8 per device type | No | First 3 to 4 visible without scrolling [Practitioner consensus] |
| Promo video | YouTube URL | No | Show the app in the first 2 seconds |
| Developer name | Account level | Yes | Same claim limits as the title |
| Category and tags | One category, up to 5 tags | Discovery and similar apps | Choose tags deliberately [Practitioner consensus] |

Policy details carried from 2021 coverage and still applied (no 2025 to 2026 change found): no emoji, no all caps words unless the brand is written that way, no "free", "best", "#1", "top", "new", "sale", "download now" style terms in the title, icon or developer name [Official, 2021 Metadata policy update via coverage]. `aso_metadata_check.py` FAILs these in the title and WARNs in the short description.

## 3. Keyword and listing procedure

1. Build the term map with store `google` rows ([Keyword research](keyword-research-and-rank-tracking.md) section 2). Sources: Play Console search terms, the Grow keyword recommendations, ASO tool scores, review language.
2. Title: brand plus the top term. Short description: the outcome plus the second term, readable as copy. Full description: every relevant cluster in natural sentences, the most important in the top half.
3. Keep each primary term to a natural frequency. The checker warns when one word exceeds 3% of words and appears 6 or more times; that is a smell, not a target.
4. Run `aso_metadata_check.py` (limits, Metadata policy terms, emoji, repetition, coverage), then compliance.
5. Change one listing element per locale per change set, wait 2 to 4 weeks, read store listing acquisitions and conversion by search term ([Keyword research](keyword-research-and-rank-tracking.md) section 7).

Gemini in Play Console (I/O 2026):
- Clicking a keyword recommendation on the Grow page lets Gemini draft a custom store listing tailored to that keyword [Reported, 2026-10].
- Structured CSV or Google Sheet upload, with Gemini pre-populating other languages for review [Reported, 2026-10]. Screenshots are not localized by Gemini [Unverified].
- Every Gemini draft is a G1 draft: run the checker and compliance, then a G3 change request. Never publish unreviewed AI drafts.

## 4. Writing the full description for search, people and Ask Play

The full description does three jobs on Play: search text, conversion copy, and a likely input to Ask Play. Vendor tests report that Ask Play answers draw on the Play description, the key features, the app's own website, and also reviews and other Google context [Reported, 2026-10]. Structure:

1. Opening 2 lines: what the app does and for whom, using the top term once.
2. Key features as short labeled paragraphs, each naming a job users search for.
3. Proof that exists in CLAIMS.md.
4. Plans and pricing in plain words.
5. Limits worth stating, privacy summary consistent with the Data safety section, support links.

Never write sentences aimed at AI systems, and never repeat keywords for density. Both read as spam to Play policy review and to people.

## 5. Ranking and quality signals the app team owns

| Signal | Threshold or rule | Evidence | ASO action |
|--------|-------------------|----------|------------|
| User perceived crash rate | 1.09% overall, 8% on any single phone model, 28 day window | [Official] | Breach = ASO incident; hand the fix to the app team, log in INCIDENTS.md |
| User perceived ANR rate | 0.47% overall, 8% per phone model | [Official] | Same |
| Excessive partial wake locks | 2 hours or more in 24 hours in over 5% of sessions; discovery exclusion and battery warning from 2026-03-01 | [Unverified] | Check the metric in Android vitals monthly; treat a breach as an incident until verified otherwise |
| Target API level | API 36 for new apps and updates since 2026-08-31 (extension to 2026-11-01 on request) | [Official, 2026] (moved) | Missing it blocks updates; no metadata work outranks it |
| Developer verification | Required for installs on certified devices in Brazil, Indonesia, Singapore and Thailand from 2026-09-30; global in 2027 | [Official, 2026] (moved) | Mostly affects distribution outside Play |

Rule: an Android vitals breach outranks every listing change. A listing that converts while the app crashes earns 1 star reviews, which then dominate the AI review summary.

## 6. New 2026 surfaces on Google Play

| Surface | What it is | Action | Evidence |
|---------|-----------|--------|----------|
| Ask Play | A Gemini overlay in the store with follow ups and Highlights (I/O 2026); an "Ask Play about this app" box below Install was seen in 2025-05 | Answers come from listing text, features, the website and reviews; keep them consistent. Depth in [AI surfaces in the stores](ai-surfaces-in-the-stores.md) | [Reported, 2026-10]; the 2025-05 box [Unverified]; mostly English devices, EEA later [Unverified] |
| "Users are saying" review summaries | AI paragraph with topic chips, "Summarised by Google AI", for apps with enough reviews | Manage review themes ([Ratings and AI summaries](ratings-reviews-and-ai-summaries.md)) | [Reported, 2026-10] |
| Play Shorts | Vertical video feed in the store, US, select developers | Prepare 9:16 videos of real use; reuse winning ad concepts | [Reported, 2026-10] |
| Apps in the Gemini app | Announced at I/O 2026 for "coming weeks" | Keep App Links and listing facts correct; do not plan on it | [Unverified] rollout |
| AI Q&A on listings | Google said 95% of user queries answered | Keep the description and Data safety accurate | [Official, 2026-05] (moved) |
| Engage SDK on listings | Existing users see Engage SDK content on the listing (from 2026-06) | Content and commerce apps: integrate with lifecycle-crm | [Official, 2026-05] (moved) |
| Reach metric | Total visibility on Play including indirect value | Add to the weekly read | [Official, 2026-05] (moved) |
| AppFunctions | Android 16+ API that exposes app functions to agents such as Gemini; Gemini integration in private preview | App team work: [On-device assistants](on-device-assistants.md) | [Reported, 2026-10] |

## 7. Pre-registration

- Run 2 to 12 weeks of pre-registration before launch with a pre-registration custom store listing and, if approved, a reward [Practitioner consensus].
- Google App campaigns for pre-registration are paid work: `mobile-app-growth`.
- Store listing experiments can target pre-registration clicks [Reported, 2026-10], so the pre-registration page can be tested before launch.
- Launch day: pre-registered users get an install or a notification depending on settings; prepare servers, rating prompts and review replies for the spike.

## 8. Measurement in Play Console

| Report | Use |
|--------|-----|
| Store performance: store listing visitors, acquisitions, conversion rate by source (search, explore, third-party referrals) and by search term | Core ASO funnel |
| Tracked channels (UTM tagged links) | Attribute web, partner and AI answer traffic you link with UTM parameters ([App web presence for AI](app-web-presence-for-ai.md)) |
| Store listing experiments | [Store experiments](store-experiments-cpp-csl.md) section 4 |
| Statistics: installs, uninstalls, acquisition by channel | Trends; historical acquisitions and conversion remain here |
| Android vitals | Crash, ANR, wake locks vs thresholds |
| Ratings and reviews | Average, distribution, replies, rating change with and without replies [Official] |
| Cart conversion, subscriber tenure, churn reasons (I/O 2026) | Monetization context for `mobile-app-growth` and `lifecycle-crm` [Official, 2026-05] (moved) |

## 9. Weekly Play ASO read (15 minutes)

1. Visitors, acquisitions and conversion by source vs the prior 4 weeks.
2. Top 20 search terms by visitors and conversion; high visitor, low conversion terms become custom store listing candidates.
3. Ratings average (7 day), new 1 to 2 star themes, the current "Users are saying" text.
4. Android vitals including wake locks.
5. Experiments and custom store listings status.
6. Competitor listing changes from the ASO tool.
7. Journal entry with findings and change requests.

## 10. Worked example: keyword cluster listing

Situation (illustrative): a budgeting app sees "expense tracker" as a top search term with conversion 30% below the listing average.
1. Draft custom store listing CSL-03 targeted to the search keyword "expense tracker" (G2 draft; Gemini draft allowed as a starting point).
2. Title stays brand plus "Expense Tracker"; short description leads with receipt scanning; first screenshot shows the expense list.
3. Run `aso_metadata_check.py` and compliance; publish only after approval (G3).
4. Read keyword conversion for 3 weeks vs the prior 3 weeks and vs the default listing on similar terms.
5. Keep, iterate or retire; log the result in EXPERIMENTS.md and the CPP and CSL registry.

## 11. Market notes

- Android leads installs in India, Indonesia, Brazil, much of Latin America, Türkiye and Africa; iOS leads revenue share in the US, Japan and parts of Western Europe [Practitioner consensus]. Localize Play listings first for Android heavy growth markets ([Localization](localization-and-market-expansion.md)).
- Custom store listings are not auto translated and only one can target a given country at a time [Reported, 2026-10].
- Price and payment method localization belong to `offer-strategy` and `mobile-app-growth`.

## 12. Mistakes to prevent

1. Title with "Free", "#1", "Best" or emoji: rejection under the Metadata policy.
2. Keyword stuffed full description: policy risk, lower conversion, wrong Ask Play answers.
3. Optimizing screenshots while vitals or wake locks breach thresholds.
4. One global listing when 50 custom store listings are available.
5. Publishing Gemini drafted listings or translations without native and claims review.
6. Running a store listing experiment while a large paid burst hits the same listing.
7. Missing the target API deadline: the listing stays but updates stop.
