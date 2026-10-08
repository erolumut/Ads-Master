# ASO for the Apple App Store

> Knowledge as of 2026-10. Apple shipped new creative assets (product page headers, search result assets, Asset Library) in App Store Connect on 2026-10-05, raised custom product pages to 70 with keywords on 2025-10-29, added AI generated App Store Tags in 2025 and added multiple ad slots in search results from 2026-03-03. Verify each against the Freshness Protocol before advising.

## 1. Metadata fields and limits

| Field | Limit | Indexed for search | Edit needs review | Notes |
|-------|-------|--------------------|-------------------|-------|
| App name | 30 characters | Yes, highest weight | Yes (new version) | Brand + 1 to 2 core keywords. No prices, no "#1", no competitor names (Guideline 2.3.7) |
| Subtitle | 30 characters | Yes | Yes | Second strongest field; benefit phrase that carries keywords |
| Keyword field | 100 bytes | Yes | Yes | Comma separated, no spaces after commas, singular or plural once, no words already in name or subtitle, no competitor trademarks |
| Promotional text | 170 characters | No | No (update anytime) | Use for timely offers and events |
| Description | 4,000 characters | No (iOS) | Yes | Write for conversion and for AI answer engines; first 3 lines show before "more" |
| What's New | 4,000 characters | No | Yes | Release notes; mention fixes users asked for in reviews |
| In-app purchase display names | 35 characters each (verify) | Practitioner consensus: yes; promoted IAPs can show in search | Yes | Name IAPs with keywords where truthful |
| Developer name | Account level | Practitioner consensus: yes | No | |
| Category, secondary category | One each | Affects browse and Time Allowances category mapping (iOS 27) | Yes | Time Allowances use the App Store Connect category [Official, 2026-06] |
| Screenshots | Up to 10 per device size | Captions: [Contested] | Yes | First 3 portrait shots show in search results |
| App previews | Up to 3, 15 to 30 seconds | No | Yes | Autoplay muted in search and on the page |
| Product page header (new) | Image or video asset | No | Yes (asset review via Asset Library) | Optional; appears on iOS 27 and iPadOS 27 per secondary reading of the help page [Unverified display requirement] |
| Search results creative asset (new) | Image or video asset | No | Yes | Appears in App Store and Apple Games search results; can be used in Apple Ads Today tab and search ads [Official, 2026-06 WWDC26 guide] |

Apple's own search documentation names the app name, subtitle and keyword field as the metadata fields used for search; descriptions are not indexed on iOS [Official]. Developer name, IAP names and category are commonly reported to matter [Practitioner consensus].

## 2. Keyword research procedure

1. Seed list: brand, category nouns, jobs to be done ("track calories", "scan pdf"), feature nouns, competitor brands (for Apple Ads only, never metadata), long tail phrases from reviews and support tickets.
2. Pull popularity and difficulty from an ASO tool (AppTweak, Sensor Tower, MobileAction, Appfigures, AppFollow) and Apple Ads Search Popularity (Apple Ads Platform API exposes Search Popularity per secondary coverage [Unverified]). Apple Ads search term reports are the best source of real query volume for your app.
3. Score each term: relevance (0 to 3, human judged), popularity, difficulty, current rank, and conversion signal from Apple Ads (tap to install rate by keyword).
4. Place terms: highest value, highest relevance in the name; next in subtitle; the rest in the keyword field; never repeat a word across the three fields (Apple combines words across fields into phrases [Practitioner consensus]).
5. Localize, do not translate: research per storefront. Use cross-localization: some storefronts index more than one localization (for example the US storefront is widely reported to index English (US) plus several other localizations such as Spanish (Mexico)) [Practitioner consensus, verify current mapping with an ASO tool]. Use the secondary localization to add 100 more bytes of keywords for that storefront.
6. Ship, wait 2 to 4 weeks (rankings settle after indexing), measure rank and impressions per term, then rotate low performers.
7. Log every metadata change with date and version in the journal; ranking analysis without a change log is guesswork.

Keyword field rules (copy to the brief):
- Separate with commas, no spaces: `tracker,budget,expense,money,bills`
- No duplicates of name or subtitle words, no app name, no category name ("app", "free", category words are matched already [Practitioner consensus])
- No competitor or celebrity names (rejection risk under 2.3.7 and trademark complaints)
- Use the singular or plural form once; Apple handles basic stemming [Practitioner consensus]

## 3. Ranking factors (what is known vs believed)

| Factor | Evidence |
|--------|----------|
| Keyword presence in name, subtitle, keyword field | [Official] |
| Download velocity and conversion rate for the query | [Practitioner consensus] |
| Ratings volume and average | [Practitioner consensus] |
| App Store Tags (AI generated labels reviewed by humans, visible to users, developers can deselect but not add) | [Official, 2025-06 WWDC25 coverage]; impact on ranking reported by ASO vendors [Practitioner consensus] |
| Screenshot caption text read by OCR for ranking | [Contested]. Vendors date a shift to 2025-06; a test of 64 caption phrases across 8 apps found 36 did not rank and 27 were explained by existing metadata; Phiture reports Apple denied OCR indexing. Write captions for conversion; treat ranking value as a bonus |
| Custom product pages with assigned keywords appear in organic search | [Official, 2025-10 notice: 70 pages with keywords]; vendors date organic CPP visibility to 2025-07 |
| Personalized Collections (Apps, Games, Search tabs, select countries) | [Official, 2026-06]; mechanics undisclosed |
| Apple Ads multiple slots in search results (from 2026-03-03, UK and Japan first, all markets by end of March, iOS 26.2+) | [Official, 2026-01]; expect lower organic tap share for apps that are not rank 1 [Practitioner consensus] |

## 4. Product page conversion: creative system

### 4.1 What users see first

| Surface | What shows | Priority |
|---------|-----------|----------|
| Search results | Icon, name, subtitle, rating, first 3 screenshots or first preview (or the new search result asset on supported OS versions) | Highest: most installs follow search (Apple says nearly 65% of downloads happen directly after a search [Official claim, 2026-01]) |
| Product page top | Header asset (new), icon, name, subtitle, Get button, ratings, awards, first screenshots | High |
| Browse and Today tab | Featured stories, in-app event cards, Today tab ads | Medium |

### 4.2 Screenshot framework (first 3 frames do 80% of the work)

1. Frame 1: the core outcome in 3 to 5 words plus the product in use. No logo walls.
2. Frame 2: the main differentiator with proof (rating, user count, award) only if verified in brand/PRODUCT_FACTS.md.
3. Frame 3: the second job or the "how it works" moment.
4. Frames 4 to 10: features, social proof, privacy and trust, pricing clarity if the app is subscription first.
5. Orientation: portrait for most apps; landscape only for games where gameplay is landscape and it tests better.
6. Captions: 2 lines max, 24 pt minimum equivalent, high contrast; readable at search result size.
7. Localize screenshots for the top 5 revenue storefronts, not just captions: local currency, local UI language, local faces when people appear.
8. Dark mode: the new preview tool in App Store Connect shows Dark Mode, devices and orientations [Official, 2026-10]. Check both.
9. New device classes: iPhone Duo (available 2026-10-23) screenshots become required for submissions from April 2027 [Official, 2026-10]. Plan the asset set now.

### 4.3 App previews

- 15 to 30 seconds, captured on device, first 3 seconds show the outcome (autoplay is muted).
- Poster frame matters when autoplay is off.
- One preview per audience CPP beats one generic preview.

### 4.4 Icon

- Test icons through Product Page Optimization (icons must be in the binary).
- Keep recognizability across updates; a radical icon change resets brand recall in search.

## 5. Localization program

- Apple supports localized metadata in 50 languages since 2026-03-31 (11 added) [Official, 2026-03].
- Prioritize by revenue potential: storefront downloads x ARPU proxy x competition gap.
- For each new locale: native keyword research, translated and culturally adapted screenshots, localized promotional text, local review replies.
- Price localization: Apple applies equalized pricing updates by tax and FX (for example Türkiye, Poland, Switzerland price equalization from 2025-11-17) [Official, 2025-10]. Review price points per storefront after each Apple price notice.

## 6. Analytics in App Store Connect

| Metric | Use |
|--------|-----|
| Impressions, product page views, conversion rate, first-time downloads, redownloads | Store funnel by source (App Store search, browse, app referrer, web referrer, Apple Ads via source type) |
| Peer group benchmarks | Compare conversion rate and retention with similar apps (introduced 2024 [Official]) |
| In-App Purchase and subscription analytics: 100+ new metrics, cohort analysis, peer benchmarks, two subscription reports, up to seven filters | Added 2026-03-25 [Official, 2026-03] |
| Campaign links (pt and ct parameters) | Track web and partner traffic to the product page; ct values are visible in App Store Connect |
| Custom product page performance | Per page impressions, conversion, downloads |

Weekly ASO read (15 minutes): conversion rate by source vs prior 4 weeks, top 20 keyword ranks, new ratings and average, CPP and PPO status, competitor metadata changes (via ASO tool).

## 7. Featuring and editorial

- Submit Featuring Nominations in App Store Connect for launches, major updates and in-app events, 6 to 8 weeks ahead [Practitioner consensus on lead time].
- Apple Games app accepts featured sales and offers via Featuring Nominations, with In-Game Offer, Now On Sale and Try Before You Buy event badges (US first, summer 2026) [Official, 2026-06].
- Editorial criteria are qualitative: design quality, accessibility, localization, use of new platform features, Accessibility Nutrition Labels completeness.

## 8. ASO for AI answer engines and the web

- App descriptions, the app's website and review content feed AI assistants that recommend apps. Keep the description factual, feature complete and consistent with the website. Hand off web and AI visibility work to seo and ai-search-optimization.
- Smart App Banner on the website (`<meta name="apple-itunes-app" content="app-id=..., app-argument=...">`) converts web visitors on iOS Safari.

## 9. Common expensive mistakes

1. Changing name, subtitle and keywords in the same release as a new icon and screenshots: no attribution of cause.
2. Stuffing the keyword field with competitor names: rejection or takedown notices.
3. Repeating words across name, subtitle and keyword field: wasted bytes.
4. Translating keywords literally instead of researching local queries.
5. Judging a metadata change after 3 days.
6. Captions written for OCR rather than for users: lower conversion, unproven ranking gain.
7. Ignoring Apple Ads search term data, which is the cheapest real query data available.
8. Leaving the default page for paid traffic instead of matching a CPP to each ad group.
9. Missing the Asset Library: submitting seasonal assets late, so they miss the season (assets can be approved ahead of time [Official, 2026-10]).

## 10. Deliverable template: ASO audit and change plan

```
# ASO plan: <app>, <storefronts>, <date>
Data used: App Store Connect Analytics <range>, ASO tool <name, date>, Apple Ads search terms <range>
Current: name / subtitle / keywords (bytes used) / rating / conversion rate by source vs peer benchmark
Keyword map: term | popularity | difficulty | relevance | rank now | field | action
Creative: frames 1 to 3 diagnosis, new concepts, PPO test plan
Localization: next 3 locales with rationale
Change list: field | from | to | release | expected effect | measurement date | approval
```
