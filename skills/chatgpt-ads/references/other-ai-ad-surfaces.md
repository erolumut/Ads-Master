# Other AI Assistant Ad Surfaces: Status, Buying Paths and Strategy

> Knowledge as of 2026-10. This module owns cross surface strategy. Execution: Google surfaces to google-ads, Microsoft surfaces to microsoft-ads, Meta to meta-ads, organic AI visibility to ai-search-optimization, checkout and feeds to commerce-feeds. Amazon Ads has no dedicated roster agent: flag to growth-orchestrator. Many facts here were read via dated captures (2026-09-22 to 2026-09-23) of official pages; re-verify live.

## 1. Surface status at a glance (2026-10)

| Surface | Ad product live? | How to buy | Targeting control | Reporting | Markets | Label |
|---------|-----------------|------------|-------------------|-----------|---------|-------|
| ChatGPT (OpenAI) | Yes: chat cards, product feed ads, carousels, Sponsored Agents (test), visual ads in image generation (US test) | Ads Manager, OpenAI sales, partners, API | Context hints, geo, platform, custom audiences | Full campaign reporting, pixel and CAPI | 60+ countries reported | [Official, 2026-10] |
| Google AI Overviews | Yes: Search, Shopping, PMax, App ads above, below and within AI Overviews | Existing Google Ads campaigns (no separate buy) | None specific: cannot target or opt out of AI Overviews | Counted as Top ads, not separated | Within AIO: 12 English markets; above and below: 200+ markets | [Official, 2026-09] |
| Google AI Mode | Testing and expanding: text and Shopping ads, Direct Offers pilot, new formats announced May 2026 | Existing campaigns (broad match or AI Max for Search, Shopping, PMax); Direct Offers via pilot | None specific | Not separated | US first; expansion not fully documented | [Official, 2026-05] |
| Gemini app | No ads | None | n/a | n/a | n/a | [Official, 2025-12] (Google VP statement) |
| Microsoft Copilot | Yes: multimedia, product, search ads with logo, vertical ads; Offer Highlights | Existing Microsoft Advertising campaigns, auto opted in | Negative keywords apply; no opt out | No Copilot specific metrics | Markets served by Microsoft Advertising; Offer Highlights English speaking | [Official, 2026-09] |
| Amazon Alexa for Shopping (formerly Rufus) | Yes: Sponsored Products and Sponsored Brands prompts | Existing Amazon SP and SB campaigns, CPC | Through existing campaigns | Prompt Ad Extension reports | US | [Official, 2026-03] |
| Perplexity | No (sponsored follow-up questions launched 2024-11, phased out; no plans as of 2026-02) | None | n/a | n/a | n/a | [Official, 2026-02] (executives to FT; TechSpot, Gigazine) |
| Meta AI | No ad unit inside Meta AI; AI chat interactions used to personalize ads on Facebook and Instagram since 2025-12-16 outside EU, UK, South Korea | Regular Meta campaigns | Indirect | Regular Meta reporting | Outside EU, UK, KR | [Official, 2025-10] |
| Claude (Anthropic) | No; committed to remain ad free (2026-02-04) | None | n/a | n/a | n/a | [Official, 2026-02] |
| Grok (xAI on X) | Ads in Grok answers planned (reported 2025-08); current status unconfirmed | Possibly via X Ads | Unknown | Unknown | Unknown | [Unverified] |
| Snapchat My AI | Sponsored Links sold by Microsoft Advertising (2023 page, may be stale) | Microsoft Advertising | Unknown | Unknown | Unknown | [Unverified] |
| AI ad networks in third party chat apps (for example Koah, Kontext) | Vendor networks | Direct with vendor | Vendor specific | Vendor reported | Varies | [Unverified] |

## 2. Google: ads in AI Overviews and AI Mode

### What is known
- Ads can appear above, below or within AI Overviews. Within-AIO ads are listed for 12 countries in English on mobile and desktop: Australia, Canada, India, Indonesia, Kenya, Malaysia, New Zealand, Nigeria, Pakistan, Philippines, Singapore, United States. Above and below placements cover 200+ markets [Official, 2026-09] (Google Ads Help as captured).
- Eligible campaign types: Search, Shopping, Performance Max, App. Advertisers cannot target AI Overview placements or opt out. Placements report as Top ads. Sensitive verticals are excluded [Official, 2026-09].
- Expansion history: ads in AI Overviews launched on US mobile in 2024 and reached US desktop from Google Marketing Live 2025 (2025-05) [Official, 2025-05]; in 2025-12 Google expanded them to 11 more countries (Australia, Canada, India, Indonesia, Kenya, Malaysia, New Zealand, Nigeria, Pakistan, Philippines, Singapore), mostly English language queries [Official, 2025-12] (relayed by PPC News Feed and trade press; exact day unconfirmed). An ad intelligence vendor first detected within-AIO ads at 0.052% frequency on 2025-11-24 [Study, 2026-04]. Ads are excluded from AI Overviews in sensitive categories (adult, alcohol, gambling, finance, healthcare, politics) per trade summaries [Unverified].
- AI Mode: Google announced ads in AI Mode tests at I/O and GML 2025 (2025-05); Ad Age reported (2025-07) a wider launch planned for Q4 2025, and US and India serving was reported in 2025; Google said in October 2025 it was testing before expanding [Unverified] (exact dates; PPC Land and Ad Age relays). Shopping ads in AI Mode announced 2026-02-11 [Study, 2026-04] (Adthena relay).
- Google Marketing Live, 2026-05-20 [Official, 2026-05]:
  | Format | Surface | Status |
  |--------|---------|--------|
  | Conversational Discovery ads | AI Mode | Testing |
  | Highlighted Answers | AI Mode recommendation lists | Testing; "highly relevant, high-quality ads are eligible" |
  | AI-powered Shopping ads | Search | Coming months |
  | Business Agent for Leads | Search (chat agent in the ad) | Coming months |
  | Direct Offers | AI Mode and shopping | Pilot since January 2026 (Chewy, Gap, L'Oreal named); planned bundles, native checkout for UCP merchants, travel offers with Booking and Expedia |
  Formats labeled "Sponsored". Google advises building on AI Max for Search, AI Max for Shopping and Performance Max.
- Universal Commerce Protocol (UCP) and Business Agent announced 2026-01-11 [Official, 2026-01].
- Gemini app: "There are no ads in the Gemini app and there are no current plans to change that" (Google VP of Global Ads, 2025-12-08) [Official, 2025-12].

### Independent data (vendor panels, not comparable to each other)
- AI Overviews appeared on 18% (US) and 23% (UK) of searches in June 2026 [Study, 2026-06] (Adthena); over 40% of searches per Similarweb [Study, 2026-08].
- Ads appeared on 29.45% of 50,032 AI Mode keywords (SE Ranking) vs 5.8% AI Mode ad frequency (Adthena, July 2026) [Contested].
- Brands cited inside AI Overviews had 7.89% paid CTR vs 4.14% for non-cited brands [Study, 2026-02] (Adthena). Organic citation and paid performance interact on Google; coordinate with ai-search-optimization.

### Strategy
- No separate buy: the lever is campaign type and matching breadth (broad match, AI Max for Search, PMax, Shopping feed quality). Brief google-ads with the AI surface goal and KPIs.
- You cannot isolate AI surface performance in reporting; use Top ads trends, AI Max search terms and landing page segmentation.
- Feed quality (titles, attributes, prices, promotions) drives Shopping in AI Mode and Direct Offers; route to commerce-feeds.

## 3. Microsoft Copilot

### What is known [Official, 2026-09] (Microsoft Learn "About ads in Copilot", updated 2026-09-02)
- Ads serve in varying formats within Copilot responses, created automatically from existing campaign assets.
- Selection considers the whole conversation, not only the last prompt.
- Eligible campaign and ad types are opted in automatically; advertisers cannot opt out; no guarantee of display.
- Eligible formats: Multimedia ads; Product ads (Shopping and PMax); Search ads with logo or business logo automated extensions (Dynamic Search Ads, Responsive Search Ads, PMax search placements); vertical ads (Property promotion, Tours and Activities). Search ads must include a logo to show in Copilot.
- Negative keywords apply in Copilot as on the Microsoft Advertising Network. Ads are not shown in conversations flagged as potentially harmful.
- "Microsoft Advertising does not currently support specific metrics for ads served in Copilot."
- Optimization guidance: Performance Max is the best way to increase Copilot exposure; broad match, auto generated assets, higher bids, Quality Score, multimedia and feed based ads.

Related launches:
- Copilot Checkout (US, Copilot.com and app) from 2026-01-08 with PayPal, Shopify and Stripe; Microsoft takes no commission or affiliate fee; English language merchants selling to US buyers in USD; Shopify merchants auto enrolled after an opt-out window [Official, 2026-09].
- Brand Agents: free site embedded shopping assistants for Shopify merchants (Microsoft Clarity required) [Official, 2026-09].
- Offer Highlights (2026-04-21): promotes product differentiators in Copilot conversations, Edge and Bing product pages; retail, English speaking markets [Official, 2026-04].
- AI Max for Search (Microsoft) open pilot from May 2026, delivering on Copilot Search and Copilot Answers [Official, 2026-05].
- UCP-ready feed support in Microsoft Merchant Center generally available in the US 2026-04-21 [Official, 2026-04].
- Showroom ads and other Copilot formats announced in 2025 [Unverified] (details not re-verified).

### Strategy
- Cheapest AI surface to "test": if Microsoft Ads already runs, add logos, multimedia ads and PMax; no new account or minimums.
- Measure only indirectly (no Copilot breakout). Do not invent Copilot attribution.
- Brief microsoft-ads with: logo extension coverage, multimedia ad coverage, PMax with feed, negative keyword hygiene.

## 4. Amazon Alexa for Shopping (formerly Rufus)

- Sponsored Products and Sponsored Brands prompts moved from open beta to general availability in the US on 2026-03-25 (announced 2026-03-10); billed as part of existing CPC bidding [Official, 2026-03].
- Prompts draw on detail pages, Brand Store content and campaign data; no separate feed upload [Official, 2026-09] (as captured).
- Surfaces: shopping results and product detail pages; clicking may open an Alexa for Shopping conversation [Official, 2026-09].
- Reporting: Prompt Ad Extension reports with performance data including cost per click [Official, 2026-09].
- Rufus was renamed Alexa for Shopping on 2026-05-13 [Official, 2026-05].
- Amazon cites 300M+ customers using Rufus in 2025 and nearly 20% of shoppers continuing the conversation [Official, 2026-09] (company stated, no sample).
- Alexa+ conversational ads exist on Alexa devices; no billing model stated [Official, 2026-09].
- Separate: Amazon Ads sells ChatGPT Ads inventory through Amazon DSP as a managed service to select US advertisers from 2026-09-10 (CPC or CPM, text and image units under responses, product feeds can generate assets, aggregate reporting only, no commission reporting; Delta Vacations named as a tester) (Digiday, Marketing Dive, PPC Land, 2026-09). Amazon reportedly invested in OpenAI in February 2026 [Unverified].

Strategy: for Amazon sellers, ensure SP and SB campaigns are eligible for prompts (US), monitor Prompt Ad Extension reports, and improve detail page content (it feeds prompt generation). No roster agent owns Amazon Ads; request resourcing from growth-orchestrator.

## 5. Perplexity

- Launched ads 2024-11-12: sponsored follow-up questions and paid media beside answers; launch partners included Indeed, Whole Foods Market, Universal McCann, PMG [Official, 2024-11].
- Reported to have phased out ads during 2025; in February 2026 executives said they had no plans to pursue advertising because "a user would just start doubting everything" (FT via PYMNTS, 2026-02-18; also TechSpot and Gigazine) [Official, 2026-02]. The executive framed it as not beneficial "for now", not a permanent ban; shopping listings are documented as not sponsored. Recheck before any plan.
- No advertiser page or ad product found on Perplexity's site in September 2026 [Study, 2026-09] (independent check).
- Strategy: treat Perplexity as organic visibility only (ai-search-optimization). Do not budget paid Perplexity.

## 6. Meta AI, Gemini, Claude, Grok
- Meta: no ad unit inside the Meta AI assistant found; Meta announced on 2025-10-01 that it would use people's text and voice interactions with Meta AI to personalize content and ads across its apps from 2025-12-16 (not EU, UK, South Korea; sensitive topics such as religion, politics, health and sexual orientation excluded; no separate opt-out other than not using Meta AI) [Official, 2025-10]. Implication: no separate buy; meta-ads should expect AI chat derived interest signals in delivery.
- Gemini app: no ads, "no current plans" (2025-12-08) [Official, 2025-12]; watch for change.
- Claude: Anthropic states Claude will remain ad free (2026-02-04) [Official, 2026-02]. Organic only.
- Grok: X planned ads in Grok answers (FT, 2025-08-07) [Unverified]; no confirmed self-serve product found. Check X Ads documentation before planning.

## 7. AI ad networks (ads inside third party AI apps and chatbots)
- Vendors sell ads placed inside third party AI chat apps (examples named in 2026 research: Koah with a claimed 7.5% average CTR; Kontext with CPMs "from just $3") [Unverified] (vendor pages).
- Risks: inventory quality, fraud, brand safety, opaque placement, self reported metrics.
- Rule: only with capped budgets (under 5% of test budget), click-through conversion tracking on your own systems, placement lists, and a kill rule after 2 weeks.

## 8. Prioritization model (score each surface 0 to 3)

| Criterion | 0 | 3 |
|-----------|---|---|
| Reachability | No buying path | Already reachable through running campaigns |
| Audience fit | Buyers not on this surface | Buyers research here before purchase |
| Measurement | No reporting | Campaign level reporting plus pixel or CAPI |
| Control | No targeting or exclusion | Hints, geo, audiences, exclusions |
| Cost to test | High minimums or new account and team | Uses current setup |
| Maturity | Rumored or alpha | Generally available in target market |

Typical outcome for a US business already on Google and Microsoft: (1) Google AI Overviews and AI Mode via existing campaigns (score high on reachability and cost), (2) Microsoft Copilot via logos, multimedia and PMax, (3) ChatGPT Ads as the only surface with dedicated controls and full reporting, tested with a ring fenced budget, (4) Amazon prompts if selling on Amazon US, (5) everything else organic or watch list.

## 9. Monthly surface review template
| Surface | Status change this month (source, date) | Reachable now? | Spend | KPI | Decision | Owner |
|---------|----------------------------------------|----------------|-------|-----|----------|-------|
| ChatGPT Ads | | | | | | chatgpt-ads |
| Google AIO and AI Mode | | | | | | google-ads |
| Microsoft Copilot | | | | | | microsoft-ads |
| Amazon prompts | | | | | | growth-orchestrator to assign |
| Perplexity | | | n/a | n/a | Watch | ai-search-optimization |
| Meta AI signals | | | n/a | n/a | Watch | meta-ads |
| Gemini, Claude, Grok | | | n/a | n/a | Watch | chatgpt-ads |

## 10. Sources to check monthly
- Google Ads Help on ads in AI Overviews and AI Mode; Google Ads and Commerce blog.
- Microsoft Learn "About ads in Copilot" and the Microsoft Advertising blog.
- Amazon Ads news and help for sponsored prompts.
- Perplexity blog; Meta newsroom; Anthropic news; X Ads help.
- Vendor panels (Adthena, Similarweb, SE Ranking, Sensor Tower) for presence data, always labeled [Study] with method caveats.
