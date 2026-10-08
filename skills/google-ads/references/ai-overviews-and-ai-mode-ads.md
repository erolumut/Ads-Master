# Ads in AI Overviews and AI Mode

> Knowledge as of 2026-10. This is the least documented and fastest changing surface in Google Ads. Most 2026 format details come from Google Marketing Live 2026 (2026-05-20) and are rolling out or in test. Verify country and format availability in Google Ads Help ("About ads and AI Overviews") and the Google Ads and Commerce blog before planning.

Ownership: google-ads executes campaigns that serve on these surfaces. Cross-assistant ad strategy (ChatGPT, Perplexity, Copilot) belongs to chatgpt-ads. Organic visibility and citations in AI Overviews and AI Mode belong to ai-search-optimization.

## 1. Surfaces and status

| Surface | Status (as of 2026-10) | Markets | Label |
|---|---|---|---|
| Ads above and below AI Overviews | Standard Search placements | All markets | [Official] |
| Ads within AI Overviews | Launched US mobile 2024-10, desktop and more countries in 2025 | English in Australia, Canada, India, Indonesia, Kenya, Malaysia, New Zealand, Nigeria, Pakistan, Philippines, Singapore and the US (12 countries) as of 2025-12 | [Official via trade press, 2025-12] |
| Ads in AI Mode | Test, US | US only as of 2026-07 to 2026-09 per trackers; India named in some coverage | [Contested: Google frames it as a US test] |
| Highlighted Answers (sponsored options inside AI Mode recommendation lists) | Announced GML 2026 | US first | [Official, 2026-05] |
| Conversational Discovery Ads (adapt to the user's question in real time) | Announced GML 2026 | US first | [Official, 2026-05] |
| Direct Offers (exclusive promotions surfaced in AI Mode, now with native checkout and travel deals) | Pilot since 2026-01 with select US advertisers, expanding through 2026 | US | [Official, 2026] |
| AI-powered Shopping ads (Gemini explains why the product fits the query) | Rolling out in the US over the months after GML 2026 | US | [Official, 2026-05] |
| Universal Cart and UCP checkout | Agentic checkout building blocks; UCP to Canada and Australia, then UK | Expanding | [Official, 2026-05] |

Sensitive verticals: ads do not appear in AI Overviews for sensitive categories such as healthcare, finance, gambling and politics [Practitioner report citing Google documentation, 2025-12; verify the current list].

## 2. Eligibility

Google's AI Overviews help page: text and Shopping ads from existing Search, Shopping and Performance Max campaigns are eligible to show within AI Overviews [Official]. There is no separate campaign type and no opt-in or opt-out placement control. [Practitioner consensus]

What raises eligibility [Practitioner consensus, partly Contested]:
| Campaign setup | AI Overviews | AI Mode |
|---|---|---|
| Search with broad match keywords | Eligible | Eligible per some sources |
| Search with AI Max (search term matching) | Eligible | Eligible |
| Exact and phrase only Search | Limited (queries must match) | Low; AI Mode queries are long and conversational |
| Performance Max | Eligible | Eligible |
| Standard Shopping | Eligible | Eligible per some sources |
| Display, Video, Demand Gen | No | No |

Sources disagree on whether standard Search with broad match qualifies for AI Mode or only PMax and AI Max do [Contested, 2026]. Search Engine Journal ties eligibility to AI-powered targeting plus Smart Bidding. Practical reading: if AI Mode visibility matters, run PMax and AI Max (or broad match with Smart Bidding) with strong feeds and landing pages.

## 3. Reporting reality

- Google states it does not offer segmented reporting for ads shown within AI Overviews [Official wording cited by trade press, 2026-07].
- No dedicated AI Mode placement report is confirmed [Contested: one vendor claims AI Mode data is available for eligible campaigns].
- Proxies:
| Proxy | How |
|---|---|
| Query length | Share of search terms with 6+ words over time (GAQL search terms, word count) |
| Conversational query share | Terms starting with question words or containing "best", "vs", "for", "how" |
| AI Max match source | Keywordless matched terms are more likely to come from conversational surfaces |
| Impression and CTR shifts | On informational queries where AI Overviews appear (check in Search Console with the seo agent) |

Never claim AI Overviews or AI Mode performance numbers that the platform does not report. Label any estimate as an estimate.

## 4. How to prepare an account

1. Measurement first: primary conversions correct, enhanced conversions on, values present. AI surfaces are matched by AI and bid by Smart Bidding.
2. Coverage: at least one route into AI surfaces for each core offer: PMax with feed (ecommerce), AI Max or broad match with Smart Bidding (Search).
3. Landing pages: clear, factual product and service information that can be quoted; specs, prices, comparisons, FAQs. AI systems draw from the page for matching and text customization. Hand off page work to cro and content work to seo.
4. Feed (ecommerce): complete titles, descriptions, attributes, product highlights, GTINs, prices, shipping, returns, ratings. Conversational queries match on attributes. Hand off to commerce-feeds.
5. Offers: promotions in Merchant Center and promotion assets; automated promotions may add offers from your site [Unverified, from 2026-10-12]. Direct Offers pilot (US) if invited.
6. Brand safety: brand exclusions, text guidelines, text disclaimers, URL exclusions. Generated text appears in new contexts.
7. Business Profile and location assets for local queries in AI Mode.
8. Creative: image assets and business logo on Search; strong product imagery for Shopping.

## 5. Strategy implications by business model

| Model | Implication | Action |
|---|---|---|
| Ecommerce | Conversational shopping queries ("best trail running shoes for wide feet under 150") favor rich feeds and PMax or AI Max for Shopping | Feed enrichment, PMax structure by margin, test AI Max for Shopping if invited |
| Lead gen | AI Overviews answer informational queries; clicks concentrate on high intent | Keep exact match on money terms, AI Max experiment on research queries, track lead quality |
| B2B SaaS | Comparison queries ("X vs Y", "best CRM for agencies") rise | Competitor and comparison landing pages, AI Max on category themes with brand controls |
| Local | AI Mode local recommendations | Business Profile quality, location assets, reviews, Book button where eligible |
| Travel | AI Max for Travel consolidation and Direct Offers travel deals | Test if invited |
| Publisher or marketplace | Fewer clicks on informational queries | Focus paid on transactional inventory |

## 6. Measurement approach

1. Track account level conversions and value, not only campaign level, when AI surface exposure grows.
2. Monitor CTR on queries where AI Overviews appear: organic and paid CTR fall on many informational queries when an AI Overview shows. Several third-party studies in 2025 reported large CTR declines on such queries [Study, 2025; magnitudes vary by study and method, treat specific percentages as [Unverified]].
3. Use AI Max experiments and PMax uplift experiments to measure incremental value from AI-matched traffic.
4. Coordinate with ai-search-optimization: organic citations and paid placements on the same query should be planned together.

## 7. Watch list (check monthly)

- AI Mode ads moving from US test to more markets.
- Any AI Overviews or AI Mode segment in reporting (segments or a new placement report).
- Highlighted Answers and Conversational Discovery Ads eligibility and controls.
- Direct Offers availability beyond the pilot and how offers are priced and reported.
- AI-powered Shopping ads rollout and controls.
- Universal Cart and UCP checkout in Shopping ads on YouTube and Demand Gen Direct Offers.
- Business Agent and Business Agent for Leads (conversational agents in ads).
- Policy changes for sensitive verticals on AI surfaces.

## 8. Change list template

```
Goal: increase eligibility for AI Overviews and AI Mode ads for "running shoes" demand.
Evidence: 28% of non-brand search terms now 6+ words (up from 19% in Q1), exact-only campaign coverage limited.
Proposed:
1. AI Max experiment on US_EN_SRCH_NB_Running-Shoes (search term matching on, text customization on with guidelines, URL expansion off).
2. Feed enrichment request to commerce-feeds: product highlights and attributes for top 200 SKUs.
3. Add brand exclusions and text guidelines before launch.
Measurement: AI Max experiment, 6 weeks, primary metric conversion value at ROAS >= 350%.
Approval needed: yes.
```

## 9. Query intent map for AI surfaces

| Query pattern | Example | Likely surface behavior | Paid approach |
|---|---|---|---|
| Short head term | "running shoes" | Classic results, Shopping units, sometimes AI Overview | PMax, Shopping, broad or phrase Search |
| Long conversational need | "best running shoes for flat feet and long distance under 150" | AI Overview or AI Mode likely | PMax with rich feed, AI Max, broad match with Smart Bidding |
| Comparison | "brand A vs brand B" | AI Overview often summarizes | Comparison landing page, competitor campaign with care, AI Max with brand controls |
| Local need | "emergency plumber near me open now" | Local pack, Maps, AI Mode local lists | Location assets, call assets, LSA, Book button where eligible |
| Informational | "how to fix a leaking tap" | AI Overview answers, low click intent | Usually exclude or bid low unless the business sells the fix |
| Navigational brand | "brand login" | Organic result | Brand campaign only if competitors bid; negatives for support terms |

## 10. Client questions and answers (use in reports)

| Question | Answer to give |
|---|---|
| Can we buy ads only in AI Overviews or AI Mode? | No. Eligibility comes from Search, Shopping, PMax and AI Max campaigns; there is no placement targeting or opt-out |
| How much did we spend in AI Overviews? | Google does not provide segmented reporting for ads within AI Overviews; any number is an estimate |
| Are AI Mode ads available in our country? | As of 2026-10, AI Mode ads are a US test per Google's framing; check the help page for updates |
| Should we change our keywords for AI Mode? | Keep exact match for money terms, add AI Max or broad match with Smart Bidding where data allows, and invest in feed and landing page clarity |
| Will AI surfaces reduce our clicks? | On informational queries, likely yes; on commercial queries the effect varies. Track account-level conversions and CTR by query type |
