# Store Creative and Conversion

> Knowledge as of 2026-10. Creative drives the user behavior half of Apple's documented ranking factors (downloads, ratings), and every traffic source pays for weak creative. 2026 added new first impression assets on the App Store: a product page header and a search result asset (image or video), managed in an Asset Library and usable in custom product pages, Product Page Optimization and Apple Ads [Reported, 2026-10]. Exact specs and the storefronts and OS versions that show them are [Unverified]; an Apple Developer News post dated 2026-10-05 (2026-10-08 pass) announced them as live, which the 2026-10-12 pass could not reconfirm.

Owners: this agent writes the creative brief, picks what to test and reads the result. `creative-strategy` owns concepts and angles across channels; `video-studio` produces previews and Play Shorts; `compliance` approves every caption and claim. App ad creative (Meta, TikTok, networks) stays with `mobile-app-growth` ([App creative](../../mobile-app-growth/references/app-creative.md)).

## 1. What each surface shows first

| Surface | What the user sees | Priority |
|---------|-------------------|----------|
| App Store search results | Icon, name, subtitle, rating, first 3 portrait screenshots or the first preview, or the new search result asset where supported; App Store tags (US); ads above and between results | Highest: Apple has long said nearly 65% of App Store downloads happen directly after a search [Official, Apple Ads marketing claim] |
| App Store product page | Header asset (2026), icon, name, subtitle, Get button, rating and count, AI review summary, screenshots, previews, tags, promotional text, description | High |
| App Store browse, Today, Personalized Collections (iOS 27) | Editorial stories, in-app event cards, collections with "App Notes" | Medium; placement of collections undocumented [Reported, 2026-10] |
| Google Play search | Icon, title, developer, rating, sometimes screenshots or video | Highest on Android |
| Google Play listing | Feature graphic or video, icon, title, short description, rating, "Users are saying" summary, screenshots, Ask Play entry | High |
| Play Shorts (US, select developers) | Vertical videos | New, test where eligible [Reported, 2026-10] |

## 2. Icon

1. One symbol, readable at the smallest search result size, no words (words also hit Play claim rules).
2. Distinct from the top 10 results for your core terms: put your icon next to theirs on a grid and squint.
3. Keep recognition across updates. A radical change resets brand recall in search; test it first.
4. Test: Apple PPO can test icons only if the alternate icons ship in the binary [Official]; Play store listing experiments test icons as default graphics [Official].
5. Seasonal icon changes are a release item, not a whim: plan them with the event calendar.

## 3. The first three screenshots

The first three frames appear in search results on iPhone (portrait) and above the fold on Play. They carry most of the decision.

| Frame | Job | Content rules |
|-------|-----|---------------|
| 1 | The core outcome | 3 to 5 word caption with the outcome plus the product in use; no logo wall, no awards collage |
| 2 | The differentiator with proof | Proof only if verified in `brand/PRODUCT_FACTS.md` (rating, users, awards with year) |
| 3 | The second job or "how it works" | The moment users love most in reviews (from `review_themes.py` praise themes) |
| 4 to 10 | Features, trust, privacy, pricing clarity | Subscription apps show what is free and what is paid |

Caption rules:
- 2 lines at most, high contrast, legible at search result size. `aso_metadata_check.py` warns above 50 characters.
- Write for people. Caption text as a ranking input is [Contested]; never bend a caption to fit a keyword.
- Use the words of the term map where they read naturally: they help people match the screenshot to their query whatever the indexing truth is.
- Every claim passes compliance; superlatives need evidence.

Production rules:
- Portrait for most apps; landscape only where the product is landscape (some games) and a test supports it.
- Localize the screenshots for the top revenue storefronts, not only the captions: local UI language, currency, names, faces.
- Check dark mode and every device class; App Store Connect's preview tool shows devices, orientations and dark mode [Reported, 2026-10].
- New device classes: iPhone Duo screenshots are required for submissions from April 2027 [Official, 2026-10] (moved). Plan the set now.

## 4. Previews and video

| Asset | Rules |
|-------|-------|
| App Store app previews | Up to 3, 15 to 30 seconds, captured from the app [Official]; autoplay muted, so the first 3 seconds show the outcome with captions; set the poster frame deliberately |
| Play promo video | YouTube URL with ads disabled; show the app in the first 2 seconds |
| Play Shorts | 9:16 real use; reuse winning ad concepts with store safe claims |
| 2026 header and search result video | Same rule as previews: outcome first, no fake UI; specs [Unverified] until checked in App Store Connect |

One preview per audience custom product page beats one generic preview [Practitioner consensus].

## 5. The 2026 header and search result assets

What is reported [Reported, 2026-10]: announced at WWDC26 (2026-06-08); image or video; usable on custom product pages, in PPO tests and in Apple Ads; managed in an Asset Library that does not require a new app version; a preview tool in App Store Connect. The earlier pass also recorded that assets can be approved ahead of time for seasonal use [Official, 2026-10] (moved).

Procedure:
1. Check the live specs and supported OS versions in App Store Connect before briefing (Freshness Protocol).
2. Brief 2 concepts: outcome in motion (video) and outcome still (image). Same promise as screenshot frame 1.
3. Submit through the Asset Library as a G2 draft; approval for review is G3.
4. Test against no asset (or the current asset) in PPO when the test supports it; read conversion from search separately, since the asset shows mainly in search.
5. Hand the approved asset IDs to `mobile-app-growth` for Apple Ads use.

## 6. Conversion by traffic source: diagnosis

Conversion only means something per source. Each source brings a different intent, so a blended rate moves when the mix moves.

| Source | Intent | What drives conversion | Check first |
|--------|--------|------------------------|-------------|
| App Store search, Play search | Active need | Rank, icon, first 3 screenshots, rating, subtitle or short description, ads above you | Conversion by term; screenshot frame 1 vs the query |
| App Store browse, Play explore, featuring | Low intent | Icon, header, editorial context | Featuring start or end dates |
| Web referrer and tracked web links | Read about you first | Continuity with the page that sent them | Landing page message vs frame 1 |
| AI referral (chatgpt.com, perplexity.ai, gemini.google.com and their apps as web or app referrers when a referrer is passed; links with a `ct` or UTM value you set) | Already told what the app does | Whether the page confirms what the AI said | Ask the assistant the same question; compare its claims with the page ([App web presence for AI](app-web-presence-for-ai.md)) |
| App referrer (other apps) | Mixed | Continuity with the referring app | Top app referrers list |
| Apple Ads, Google App campaigns | Paid intent per ad group | Custom product page or listing match | Hand off to `mobile-app-growth` with CPP conversion data |

Web to store continuity: a Smart App Banner on the app's website (`<meta name="apple-itunes-app" content="app-id=<id>, app-argument=<deep link>">`) turns iOS Safari visitors into product page views without a redirect [Official]. No evidence was found that it is an AI signal [Unverified]. Implementation sits with `site-engineer`; link tagging with [App web presence for AI](app-web-presence-for-ai.md).

Diagnosis procedure:
1. Pull 8 weeks of views and downloads by source and storefront (App Store Connect, Play Console).
2. Compute conversion per source per week. Flag a source when it falls below its own 8 week low.
3. Check mix: share of views by source this week vs the 8 week average.
4. If no single source fell, the blended drop is mix (worked example below). Report it, do not "fix" the creative.
5. If one source fell, list what changed for it: rank on top terms, ads above you, screenshots, rating, price, AI answer content, the referring page.
6. Compare with App Store Connect peer group benchmarks as context, never as the target.

Worked example (illustrative, one week featuring):

| Source | Week A views | Week A conversion | Week B views | Week B conversion |
|--------|-------------:|------------------:|-------------:|------------------:|
| Search | 10,000 | 35% | 10,000 | 35% |
| Browse | 2,000 | 15% | 8,000 | 15% |
| Web referrer | 1,000 | 50% | 1,000 | 50% |
| Blended | 13,000 | 33.1% (4,300 downloads) | 19,000 | 27.4% (5,200 downloads) |

Every source held, downloads rose 21%, and the blended rate fell 5.7 points. Nothing is broken.

## 7. Screenshot and asset brief template

```
# Store creative brief: <app>, <store>, <locale>, <date>
Goal and metric: conversion from <source> on <default page / CPP-ID / CSL-ID>
Audience and query cluster: <cluster from term_map.csv>
Evidence: top review themes (review_themes.py <date>), term map rows, current conversion by source
Frame 1 promise (one sentence): <outcome>
Frames 2 and 3: <differentiator with proof ID from CLAIMS.md>, <second job>
Captions (draft, under 50 characters each): 1) 2) 3)
Assets: screenshots per device class, preview or header video (specs checked <date>)
Localization: <locales>, native review by <who>
Test plan: PPO or Play experiment, sample per arm, stop rule (store-experiments-cpp-csl.md section 6)
Compliance: caption lines sent, verdicts
Registry: concept ID shared with creative-library/registry.csv
Handoffs: creative-strategy (concept), video-studio (video), compliance (claims)
```

## 8. Mistakes to prevent

1. A feature list in frame 1 instead of the outcome.
2. Claims in captions that are not in CLAIMS.md (rejection, regulator risk, wrong AI answers).
3. Reading a blended conversion rate across a featuring week.
4. One screenshot set for every storefront.
5. Fake UI, device frames that hide the real app, or gameplay the game does not have (Guideline 2.3.3 requires the app in use [Official]).
6. Briefing the 2026 assets from blog specs instead of the live console.
7. Changing icon and screenshots in the same release as metadata: no read is possible.
