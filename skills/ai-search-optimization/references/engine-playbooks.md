# Engine Playbooks

> Knowledge as of 2026-10. One playbook per engine: how it picks sources, what to do, how to measure, controls and gotchas. Prioritize engines by the project's own GA4 AI referral mix and by where the buyers are, not by industry hype. Run the Freshness protocol before acting; these products change monthly.

## How to prioritize engines

| Signal | Weight |
|--------|--------|
| Share of AI referral sessions and conversions in the project's GA4 (last 90 days) | Highest |
| Audience fit (B2B buyers skew to ChatGPT and Claude in one 2026 study; consumers to Google AI and ChatGPT) [Study, 2026, secondary] | High |
| Market share of AI referrals overall (Statcounter 2026-08: ChatGPT 79.4%, Gemini 10.9%, Perplexity 4.3%, Copilot 2.8%, Claude 2.6%) [Study, 2026-08, secondary] | Medium |
| Google AI Overview and AI Mode exposure in Search Console Generative AI report | High for any site with organic traffic |
| Effort to influence (Google AI rides SEO; ChatGPT needs off-site and index work) | Medium |

Default order for most projects in 2026: Google AI Overviews and AI Mode, ChatGPT, Gemini, Copilot, Perplexity, Claude, then Meta AI and Grok. Reorder with data.

## 1. Google AI Overviews

| Item | Detail |
|------|--------|
| Source selection | Google index, query fan-out, Gemini models. Indexed and snippet-eligible pages only [Official] |
| Strongest levers | Rank for the head query and its sub-queries; answer-first passages; brand mentions across the web (0.664 correlation in Ahrefs study) [Study, 2025] |
| Measure | Search Console Generative AI performance report (impressions, combined with AI Mode); prompt tracking for AIO presence and citations; Web report clicks for affected pages |
| Controls | nosnippet, data-nosnippet, max-snippet, noindex; Search generative AI control (property level) [Official] |
| Paid | Ads can appear above, below and within AI Overviews (owned by `google-ads`) |

Plays:
1. Pull the pages with the highest AI impressions and the steepest CTR decline in the Web report. Add unique value that the overview cannot hold: calculators, data tables, templates, tools, original research.
2. For informational queries where AIO triggers, aim to be a cited source: Seer data shows cited brands get materially more organic and paid clicks than uncited brands on the same SERP [Study, 2025 to 2026].
3. Fix snippet eligibility issues (accidental nosnippet, poor rendering).
4. Do not chase AIO for queries with no business value. CTR on AIO SERPs fell sharply (Ahrefs: position 1 CTR about 58% lower) [Study, 2026-02].

## 2. Google AI Mode

| Item | Detail |
|------|--------|
| Source selection | Same index, heavier fan-out, multi-turn, Deep Search for research. Cites more unique domains than AI Overviews (one 2026 analysis: 143% more) [Study, 2026-01, secondary] |
| Strongest levers | Coverage of sub-queries across a topic; distinct facets on separate, well-linked pages; third-party mentions; local and product data via Google Business Profile and Merchant Center |
| Measure | Generative AI report (combined); prompt tracking with AI Mode; follow-up turns |
| Controls | Same as AI Overviews |
| Commerce | Agentic checkout via UCP for eligible merchants (see [Agentic commerce](agentic-commerce-visibility.md)) |

Plays:
1. Build the fan-out map for priority prompts and close facet gaps.
2. Track follow-up prompts ("which is cheaper?", "which works for restaurants?"), since AI Mode is conversational.
3. Re-baseline after Gemini model updates in AI Mode (Gemini 3 in 2025-11 [Official]; a newer Flash model reported in 2026-09 [Unverified]).
4. AI Mode answered 97% of sampled People Also Ask answers in a 2026-09 sample [Unverified, secondary]: treat PAA questions as AI Mode sub-queries.

## 3. Gemini app

| Item | Detail |
|------|--------|
| Source selection | Google Search grounding plus model knowledge |
| Strongest levers | Same as Google Search; Google-Extended must not be blocked if you want grounding [Official] |
| Measure | Prompt tracking only; GA4 referrer gemini.google.com |
| Controls | Google-Extended (training and grounding). The Search Console opt-out does not cover the Gemini app [Official, 2026-06] |
| Trend | Gemini's share of AI web traffic and referrals rose sharply through 2025 to 2026 [Study, 2026, secondary] |

## 4. ChatGPT search

| Item | Detail |
|------|--------|
| Source selection | Own index (reported "Labrador") dominant on free tier; scraped Google results dominant on paid tier; news provider feed [Study, 2026-07]. OAI-SearchBot must be allowed [Official] |
| Strongest levers | OAI-SearchBot access; Google rankings for sub-queries (paid tier); third-party mentions on sources ChatGPT cites (Wikipedia historically heavy); clear title and opening facts; freshness |
| Measure | Prompt tracking across free and paid modes; GA4 chatgpt.com referrals with utm_source=chatgpt.com; ChatGPT-User fetches in logs |
| Controls | OAI-SearchBot (search), GPTBot (training), ChatGPT-User (user fetch) |
| Paid | Ads in ChatGPT are owned by `chatgpt-ads` |

Plays:
1. Confirm OAI-SearchBot gets 200s in logs and is not blocked at the CDN.
2. Make titles and first sentences carry the entity and the answer (reported limited text stored per page in the free index [Unverified]).
3. Earn mentions on the domains ChatGPT cites for your prompts (from source mapping).
4. Keep pricing, comparison and "best of" pages fresh with real updates.
5. Optimize the homepage as a landing page: ChatGPT sends a growing share of referrals to homepages since 2026-05-07 [Study, 2026-05].
6. Track memory-free runs as baseline; note that real users have memory and history.

## 5. ChatGPT shopping

| Item | Detail |
|------|--------|
| Source selection | Product data from merchant feeds via the Agentic Commerce Protocol and third-party providers; reviews and editorial content for recommendations [Official, 2025 to 2026] |
| Status | Instant Checkout launched 2025-09-29; OpenAI pivoted in 2026-03 to discovery with merchant-side checkout; Shopify Agentic Storefronts on by default for eligible merchants from 2026-03-24 [Contested details; verify] |
| Strongest levers | Complete, accurate feed (owned by `commerce-feeds`); review volume and quality; competitive price and availability; product page facts in HTML; third-party reviews |
| Measure | Shopping prompt tracking; GA4 chatgpt.com sessions to product pages |

See [Agentic commerce](agentic-commerce-visibility.md).

## 6. Perplexity

| Item | Detail |
|------|--------|
| Source selection | Own index (PerplexityBot) plus live fetch; heavy Reddit citation historically (46.7% of top-source citations in 2024 to 2025 data) [Study, 2025] |
| Strongest levers | PerplexityBot access; fresh, specific pages; Reddit and forum presence (genuine); news coverage |
| Measure | Prompt tracking; GA4 perplexity.ai |
| Controls | PerplexityBot honors robots.txt; Perplexity-User generally does not [Official] |
| Risk | Cloudflare delisted Perplexity as a verified bot in 2025-08 [Contested]. Cloudflare sites may block it by default |
| Trend | Referral share declining in 2026 (4.3% in 2026-08) [Study, 2026-08, secondary] |

## 7. Microsoft Copilot and Bing

| Item | Detail |
|------|--------|
| Source selection | Bing index and grounding queries |
| Strongest levers | Bing indexing (IndexNow, sitemaps, Bing Webmaster Tools); structured data (Bing has said schema helps its systems) [Practitioner report, 2025-03]; Bing Places for local |
| Measure | Bing Webmaster Tools AI Performance (citations, cited pages, grounding queries, citation share) [Official, 2026]; GA4 copilot referrals |
| Paid | Copilot ads owned by `microsoft-ads` |

Plays:
1. Verify the site in Bing Webmaster Tools and enable IndexNow.
2. Export grounding queries monthly; each one is a sub-query to cover.
3. Compare citation share by topic with competitors (Compare feature, preview).

## 8. Claude

| Item | Detail |
|------|--------|
| Source selection | Web search tool plus Anthropic search index (Claude-SearchBot); Claude-User fetches pages for users [Official]. External provider reported as Brave Search in 2025 [Unverified for 2026] |
| Strongest levers | Allow Claude-SearchBot and Claude-User; fact-dense pages; documentation and technical content for developer and B2B audiences; if Brave is the provider, Brave Search visibility |
| Measure | Prompt tracking (some tools added Claude tracking in 2026, for example Yoast on 2026-05-28) [Official vendor, 2026-05]; GA4 claude.ai |
| Audience | Strong in B2B and developer segments (18.5% of B2B AI referrals in one 2026 study) [Study, 2026, secondary] |

## 9. Meta AI

| Item | Detail |
|------|--------|
| Source selection | Model knowledge plus web search partners and Meta crawlers [Unverified] |
| Strongest levers | Allow Meta-ExternalAgent if visibility is the goal [Unverified effect]; accurate Facebook and Instagram business profiles; consistent web facts |
| Measure | Prompt tracking where tools support it; GA4 meta.ai |

## 10. Grok

| Item | Detail |
|------|--------|
| Source selection | X posts and web search [Practitioner consensus] |
| Strongest levers | Active, factual X account; executives and customers discussing the brand on X; web presence |
| Measure | Prompt tracking; GA4 grok.com |

## 11. Apple, Amazon and others

| Engine | Levers |
|--------|--------|
| Siri, Spotlight, Apple Intelligence | Applebot access; Apple Business Connect for local; App Store listing quality |
| Amazon Rufus, Alexa+ | Amazon listing completeness, Q&A, reviews, A+ content (hand off listing work to `commerce-feeds`) |
| DuckDuckGo DuckAssist | Bing health plus own site clarity |
| Brave | Brave Search indexing |
| DeepSeek, Mistral and regional engines | Prompt test in the market; usually low priority outside their home markets |

## 12. Cross-engine weekly routine (30 to 60 minutes)

1. Check access: logs or CDN dashboard for 4xx and 5xx on AI tokens.
2. Collect tracking data (automated tool or scheduled DIY runs).
3. Review answers flagged with wrong facts or negative sentiment.
4. Note any engine or model change from the Freshness sources.
5. Log one journal entry if anything changed materially.
