# Localization and Market Expansion

> Knowledge as of 2026-10. Apple supports metadata in 50 languages since 11 were added on 2026-03-31 (App Store Connect API 4.3.1), across 175 storefronts [Reported, 2026-10]. Which localizations each storefront indexes for search (cross-localization) is not documented by Apple; the only public test of the mapping is from 2022 and predates the 11 new languages [Unverified]. Treat any storefront to locale matrix as stale until you verify it for your app.

## 1. Localization is research, not translation

A translated keyword field targets the words a translator chose, not the words people type. Each locale gets:
1. Native keyword research (term map rows per locale, [Keyword research](keyword-research-and-rank-tracking.md)).
2. Transcreated name, subtitle or short description and description, written for that market's searchers and AI readers.
3. Localized screenshots for markets that matter: UI language, currency, local proof, local faces.
4. Review replies in the review's language.
5. A local custom product page or custom store listing when the message differs.

## 2. Apple cross-localization

Some storefronts index more than one localization: a term placed in a secondary localization's keyword field can rank in that storefront [Practitioner consensus for the mechanism]. The widely circulated mapping comes from a 2022 test by AppTweak and Phiture that found 9 secondary locales indexed for the US storefront, Spanish (Mexico) among them [Unverified, 2022 test]. The 2026-03-31 languages were never tested.

Rules:
- Never plan on a mapping you have not verified for your storefront and app.
- Primary storefront locale first: the main locale of the storefront carries the name and subtitle people see.
- A secondary locale used for extra keywords must still be a real, reviewed localization. Users in that language see it.
- Change one locale per storefront per change set. When two locales are indexed together, changing both at once makes the read impossible.

Verification procedure (canary term):
1. Pick a relevant long tail term the app does not rank for in the target storefront (relevance 2 or 3, so it is honest metadata, never a nonsense string).
2. Add it only to the secondary locale's keyword field, with no other change in that locale, as its own change set.
3. After day 14 and day 28, check the rank for that term in the target storefront with the ASO tool set to that storefront.
4. Ranked: the storefront indexes that locale for your app. Not ranked after 28 days: treat it as not indexed (or the term as too hard; repeat once with a second term).
5. Record the result in `ads-master/memory/app-store-optimization.md` under "locales indexed per storefront" with the date.

## 3. Google Play localization

| Item | Detail | Evidence |
|------|--------|----------|
| Localized listing per language | Title, short and full description, graphics per language | [Official] |
| Gemini pre-populated translations | Upload a CSV or Google Sheet and Gemini pre-populates other languages for review | [Reported, 2026-10] |
| Screenshots | Not localized by Gemini | [Unverified] |
| Custom store listings by country | One custom listing per country at a time; not auto translated | [Reported, 2026-10] |
| Full and half width characters | Count equally toward limits | [Reported, 2026-10] |

Every machine or Gemini translation is a draft. Native review for any market in the top 5 by revenue or growth target; claims review by `compliance` in every market.

## 4. Market prioritization

Score each candidate storefront (one row per store and country):

`market score = demand x value x winnability x readiness`

| Factor | Measure (0 to 1, normalized across candidates) | Source |
|--------|-----------------------------------------------|--------|
| Demand | Category downloads or the summed popularity of your top 20 terms in that locale | ASO tool, market-intel |
| Value | Revenue per download proxy: own data if any, else category revenue per download | App Store Connect, Play Console, ASO tool estimates |
| Winnability | Share of top 20 terms where the top 10 results are weakly localized or rated under 4.3 | ASO tool, manual check |
| Readiness | 1 if product, support, payments and legal work in that language and market; 0.5 if partial; 0 if blocked | Product, `compliance`, `offer-strategy` |

Worked example (illustrative):

| Market | Demand | Value | Winnability | Readiness | Score | Decision |
|--------|-------:|------:|------------:|----------:|------:|----------|
| Germany (de) | 0.8 | 0.9 | 0.5 | 1.0 | 0.36 | Wave 1: L3 |
| Brazil (pt-BR) | 1.0 | 0.4 | 0.8 | 1.0 | 0.32 | Wave 1: L3, Play first |
| Japan (ja) | 0.7 | 1.0 | 0.4 | 0.5 | 0.14 | Wave 2 after support in Japanese |
| Türkiye (tr) | 0.6 | 0.3 | 0.7 | 1.0 | 0.13 | Wave 2: L2 |

## 5. Localization levels

| Level | What ships | When |
|-------|-----------|------|
| L0 | Nothing localized; English listing | Markets you do not target |
| L1 | Translated metadata (reviewed) | Long tail markets, low cost |
| L2 | Native keyword research plus transcreated metadata | Markets with a market score in the top half |
| L3 | L2 plus localized screenshots and previews | Wave 1 markets |
| L4 | L3 plus local CPP or CSL, events, promotional text, review replies in language, local featuring nominations | Core revenue markets |

## 6. Script and length traps

- Apple keyword field bytes: Turkish, Cyrillic, Arabic, Greek and CJK text can exceed 100 UTF-8 bytes while under 100 characters ([App Store search](app-store-search-and-metadata.md) section 3). `aso_metadata_check.py` warns.
- German and Finnish run long: write captions for the longest locale first, or allow 2 lines.
- Right to left (Arabic, Hebrew): mirror screenshot layouts, check numerals and mixed direction strings.
- CJK: no spaces between words; keyword field terms separated by commas carry more meaning per character.
- Local formats: dates, currency symbols and decimal separators in screenshots must match the locale.

## 7. Pricing and legal readiness

- Apple equalizes prices for tax and exchange rates in some storefronts (for example Türkiye, Poland, Switzerland from 2025-11-17) [Official, 2025-10] (moved). Price points per storefront belong to `offer-strategy` and `mobile-app-growth`; this agent makes sure listings and promotional text show the right plan language.
- Age ratings, licensing and category rules differ by market (for example Vietnam game licenses, Brazil gambling licenses, Korean rating overrides). Check with `compliance` before a market wave ([Policies](policies-and-metadata-compliance.md)).
- Support in the market's language is part of readiness: reviews in a language nobody answers drag the rating and the summary.

## 8. New market launch procedure

1. Score candidates (section 4); the human approves the wave.
2. Research: term map rows per locale from native speakers plus tools; competitor listings from `market-intel`.
3. Draft metadata per level; run `aso_metadata_check.py` per locale; `compliance` review per market.
4. Screenshots and previews for L3 and L4 markets (creative brief per locale).
5. Submit as one change set per storefront (G3), then verify the live listing in that storefront.
6. For Apple, run the canary test if you rely on a secondary locale.
7. Read at day 14 and 28: ranks for local terms, impressions, conversion by source vs the English baseline in that storefront.
8. Hand to `mobile-app-growth` for paid launch once conversion holds (paid traffic to an unlocalized page wastes money).

## 9. Reading a new locale (worked example)

Illustrative: German (de-DE) L3 launch on the App Store, live 2026-09-01, read on day 28.

| Metric (Germany storefront) | 28 days before | Days 1 to 28 | Change |
|-----------------------------|---------------:|-------------:|-------:|
| Search impressions | 41,000 | 66,000 | +61% |
| Local terms ranked 1 to 10 (of 25 tracked) | 2 | 9 | +7 |
| Conversion from search | 22% | 29% | +7 points |
| First-time downloads from search | 2,900 | 5,200 | +79% |
| English control terms ranked 1 to 10 (of 10) | 6 | 6 | none |

Reading: control terms held, so the gain is the localization, not the market. Next: a German custom product page for the top cluster and German review replies. Hand the storefront to `mobile-app-growth` for a paid test now that the page converts.

## 10. Review replies and support in the local language

- Reply in the review's language with an approved, native reviewed template set per locale ([Ratings and AI summaries](ratings-reviews-and-ai-summaries.md) section 5).
- Machine translation of a reply is a draft; a native speaker or the support team approves the template once.
- Run `review_themes.py` per locale with a taxonomy that includes local words (the default taxonomy has English and Turkish starter words; extend it in `ads-master/data/aso/review_themes.json`).
- AI review summaries in each storefront follow the local reviews, so a market with unanswered complaints gets a negative summary in its own language.

## 11. Translation QA checklist

- [ ] Native speaker reviewed name, subtitle or short description, keyword field and captions.
- [ ] Terms match the local term map, not a dictionary translation.
- [ ] No English left in screenshots unless the UI is English.
- [ ] Claims and prices approved for that market.
- [ ] Byte and character limits pass the checker.
- [ ] Support link and privacy policy available in the language or clearly marked.
- [ ] Reply templates translated and approved.

## 12. Mistakes to prevent

1. Literal keyword translation.
2. Planning on a 2022 cross-localization matrix for 2026 languages.
3. Gemini or machine translations published without review.
4. Localizing captions but leaving English UI in the screenshots.
5. Changing two locales indexed in the same storefront at once.
6. Launching a market without support in its language.
