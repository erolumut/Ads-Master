# Research Dossier: Commerce Feeds (product data, catalogs, AI shopping and agentic commerce)

> Compiled 2026-10-08 for the commerce-feeds agent. Scope: Google Merchant Center and the Merchant API, product data optimization, custom labels, Meta and TikTok catalogs, Microsoft, Pinterest and Snapchat catalogs, ChatGPT shopping and the Agentic Commerce Protocol (ACP), Google's Universal Commerce Protocol (UCP) and AP2, Microsoft Copilot Checkout, Perplexity, Shopify Catalog, Amazon agents, structured data, feed tools.

## Research method and limits
- Primary sources read directly: Google's Merchant API protocol buffers and their commit history (googleapis repository), the ACP specification repository (OpenAI and Stripe), the UCP repository, the AP2 repository, Meta's Business SDK (catalog objects), Pinterest's OpenAPI description, schema.org release notes, the Google for WooCommerce readme. These carry exact field names and commit dates.
- Help centers and vendor sites (support.google.com, developers.openai.com, chatgpt.com, shopify.com, Microsoft and Meta docs) were not reachable from the research environment. Their content was read through search result extracts and is marked "via search" in the sources list. Recheck before quoting in client work.
- The shared web search budget ran out after 14 extended searches, below the 35 planned. Areas with thinner verification: Meta Shops checkout status, TikTok catalog field specifics, Microsoft Merchant Center import options, Snapchat catalogs, feed tool pricing, title optimization effect sizes, 2026 misrepresentation policy changes. These are labeled [Unverified] in the skill.
- Verification pass (2026-10-08): live searches re-checked Meta Shops checkout, TikTok GMV Max requirements, the Microsoft Merchant Center Google import, ChatGPT Ads feed limits, the `native_commerce` attribute and UCP markets, the Google Ads scripts Merchant API date and the Content API shutdown aftermath, the Amazon v. Perplexity case and TikTok catalog fields (sources 78 to 96). Confirmed and corrected facts are dated below.

## 1. Executive summary
1. The Content API for Shopping shut down on 2026-08-18 and requests degrade progressively from 2026-09-01 unless Google approved extended access (the request form offered 2026-10-15 or 2026-12-31); the Merchant API (v1 GA in August 2025; v1beta retired 2026-02-28) is now the only programmatic path into Merchant Center, and Google Ads scripts gained a Merchant API service on 2026-04-22 [Official, 2025 to 2026].
2. Google kept expanding the product specification for AI-era shopping: product-level handling cutoffs and minimum order values, loyalty shipping, `video_link` (2026-04-14), pickup cost in UK, CH and EEA (2026-04-28), Q&A, related products, variant options, popularity rank, item group title and document links (Merchant API 2026-07-13), and offer-level return rules (2026-09-29). The minimum image size rises to 500 x 500 on 2027-01-31 [Official].
3. UCP (announced 2026-01-11) is Google's open protocol for agentic shopping; UCP-powered checkout in AI Mode and Gemini is live for select US merchants, has its own Merchant API reporting context (`FREE_LISTINGS_UCP_CHECKOUT`), and its Merchant Center integration hub is rolling out gradually to selected US merchants (early access, Google selects participants after the technical build), with Canada and Australia moved to 2027 per the October 2026 help page and Search Engine Land (2026-10-06), replacing May's "coming months". Product eligibility is the optional `native_commerce` group attribute with boolean `checkout_eligibility` [Official, 2026-10].
4. OpenAI launched Instant Checkout and ACP on 2025-09-29, then retired standalone Instant Checkout in March 2026: purchases now complete on merchant sites, Shopify and Etsy catalogs are integrated automatically, and other merchants apply for feed access [Official, 2026-03].
5. Feeds became the main retrieval source for ChatGPT shopping: Profound's tracked data shows feed-sourced picks jumping from 8.26 to 61.54 percent on 2026-07-10 and about 65 percent by 2026-09-03, with visibility concentrating in fewer merchants [Study, 2026-09].
6. ACP's 2026-04-17 release added a push-model Feed API (agent-hosted feeds, JSONL ingestion, partial upserts), carts, native orders, 3DS2 delegate authentication and an MCP binding; it is the most complete open description of an agent-ready product object [Official, 2026-04].
7. ChatGPT Ads added product feed campaigns (beta from June 2026), self-serve in Ads Manager; feed products serve ads only during the beta, need `is_ads_eligible` true (default true for feeds created in Ads Manager), and catalog size limits are reported inconsistently (100-product sample, 1,000 minimum or none; 1 million or 2 million maximum) [Official per coverage, 2026-06; limits Contested].
8. Microsoft launched Copilot Checkout (2026-01-08) with PayPal, Stripe and Shopify (auto-enrolled with opt-out) and Brand Agents; checkout reached the Copilot mobile app in April 2026 with a catalog of more than 500,000 merchants [Official, 2026].
9. Shopify became an AI distribution layer: Agentic Storefronts and Shopify Catalog syndicate merchant product data to AI channels by default for eligible stores, so Shopify product data quality is now feed quality for ChatGPT, Copilot, Perplexity and Google AI surfaces [Official per coverage, 2026].
10. schema.org 30.1 (2026-09-16) added retail feed vocabulary (`consumerNotice`, `isOftenBoughtWith`, `itemPopularity`, `minimumOrderValue`) and EU Digital Product Passport types, mirroring the new Merchant Center attributes; Google support for them is not yet documented [Official, 2026-09].

## 2. State of the channel in 2026 (with numbers)

| Metric or fact | Value | Source and label |
|----------------|-------|------------------|
| Share of ChatGPT shopping recommendations sourced from feeds (tracked prompts) | 8.26 percent before 2026-07-10; 61.54 percent after; about 65 percent by 2026-09-03 | Profound via SEJ [Study, 2026-09]; sample 1,757,723 prompt runs in July plus 97,725 runs sampled at 10 percent |
| Merchant concentration in ChatGPT shopping after the shift | Top 10 stores' share of references 22.5 to 41.8 percent; unique merchants referenced 13,524 to 10,607 | Profound [Study, 2026-09] |
| Merchants losing visibility at the shift | 450 of 687 tracked merchants lost at least one third of visibility; 67 gained | Profound [Study, 2026-09] |
| ChatGPT carousel products matching Google Shopping data | About 83 percent of 43,000 products across 10 verticals | Search Engine Land analysis via secondary coverage [Study, 2025] |
| Shopify merchants live on ChatGPT Instant Checkout before the pivot | About a dozen to about 30 | Modern Retail, CNBC, Forrester estimate via secondary coverage [Contested, 2026-02] |
| In-chat versus click-out conversion (Walmart, ChatGPT) | In-chat about one third of click-out | Reported in coverage of the March 2026 pivot [Unverified] |
| Copilot Checkout catalog | More than 500,000 merchants | Microsoft via Windows Central [Official claim, 2026-04] |
| Copilot journeys and purchases | 53 percent more purchases within 30 minutes when Copilot was involved | Microsoft via PPC News Feed [Official claim, unaudited, 2026-01] |
| Shopify Catalog conversion claim | AI searches using Catalog convert at 2x scraped data | Shopify via coverage [Official claim, unaudited, 2026] |
| Shopify AI traffic and orders growth | AI traffic 8x, AI search orders nearly 13x year over year | Shopify earnings call via secondhand coverage [Unverified] |
| Perplexity PayPal merchant network | About 5,000 merchants, more via BigCommerce, Shopware, Wix | Coverage of 2025-11 launch [Unverified] |
| ChatGPT Ads feed limits | 1 million SKUs and a 100-product onboarding sample (Digiday via a briefed ad executive, PPC Land) versus 1,000 minimum and 2 million maximum (GoDataFeed citing OpenAI help, Geekseller) versus no published minimum or maximum (Reach, GPT Ads AI reading the feed spec) | [Contested, 2026-06 to 2026-09] |
| Meta Shops checkout | Onsite checkout phased out for US shops from June 2025 (most moved to website checkout by end of August 2025; stores on third-party order management later); 2026 one-tap checkout in Facebook ads runs through payment partners with the merchant as seller | Meta notice via BigCommerce and coverage [Official per coverage, 2025-06 to 2026-04] |
| AP2 backers | 60+ at launch (2025-09), 100+ partners reported later | Google [Official, 2025] |
| Google Merchant Center GTIN capacity per item | Up to 10 GTINs (`gtins`) | Merchant API proto [Official, 2026] |
| Custom label limits | 100 characters, 1,000 unique values per label | Google spec [Official] |


### Platform snapshot (October 2026)

| Platform | What changed most since January 2025 | What it means for feed work |
|----------|--------------------------------------|-----------------------------|
| Google Merchant Center | Merchant API only; spec expanded for shipping precision, video, pickup, conversational attributes and offer-level returns; UCP checkout destination | Re-platform integrations, adopt new attributes, keep shipping and returns exact |
| Google AI Mode and Gemini | Agentic checkout (2025-11), UCP (2026-01), Business Agent, Direct Offers, Flipkart test in India (2026-09) | Free listings quality is the entry ticket; checkout is opt-in early access |
| OpenAI ChatGPT | Instant Checkout launched then retired as standalone (2025-09 to 2026-03); feeds dominate retrieval (2026-07); product feed ads (2026-06) | Feed quality and enrollment path beat checkout engineering |
| ACP | Five dated releases; Feed API push model, carts, orders, MCP (2026-04-17) | Model the product object once; emit flat OpenAI files or ACP JSONL |
| Microsoft | Copilot Checkout and Brand Agents (2026-01), mobile checkout (2026-04) | Microsoft Merchant Center feed and policies matter beyond Bing Shopping |
| Meta | API v26.0 catalog fields include custom numbers, priority fields, AI-generated backgrounds; Shops checkout narrowed (Unverified) | Product sets from labels; pixel ID alignment remains the top failure |
| TikTok | GMV Max centered Shop promotion (Unverified details) | Shop listing quality is the lever commerce-feeds controls |
| Pinterest | API v5.28 adds `ai_disclosures`; `checkout_enabled` no longer supported | Declare AI assets; lifestyle and vertical images |
| Shopify | Agentic Storefronts and Catalog syndicate product data to AI channels by default for eligible stores; supplemental terms 2026-05-25 | Shopify product data is the AI feed; decide channel toggles with the human |
| schema.org | Shipping (29.0), retail feed vocabulary and EU DPP (30.1) | Keep JSON-LD aligned; watch Google support for new properties |

## 3. Timeline of changes, January 2025 to October 2026

| Date | Platform | Change | Label |
|------|----------|--------|-------|
| 2025-03-24 | schema.org | v29.0: `ShippingService`, `ShippingConditions`, `hasShippingService`, `fulfillmentType`, `ServicePeriod`; deprecates `DeliveryTimeSettings`, `shippingLabel` | [Official] |
| 2025-04 | Amazon | Buy for Me beta: Amazon app buys from brand sites | [Unverified date] |
| 2025-05 | Google | I/O: AI Mode shopping, virtual try-on, agentic checkout preview | [Official] |
| 2025-06 to 2025-09 | Meta | Shops move from onsite checkout to website checkout (most by end of August 2025; BigCommerce cites 2025-09-04); order management and disputes leave the apps | [Official per coverage] |
| 2025-07 to 2025-09-01 | TikTok | GMV Max becomes the default (July 2025) and then the only campaign type for new TikTok Shop ads (2025-09-01); one guide gives a phased June 1 to July 15 schedule | [Contested dates] |
| 2025-08-04/05 | Google | Merchant API v1 client libraries (datasources, products): v1 general availability | [Official] |
| 2025-09-16 | Google | Agent Payments Protocol (AP2) announced with 60+ partners | [Official] |
| 2025-09-29 | OpenAI, Stripe | Instant Checkout in ChatGPT (Etsy first, Shopify announced); ACP open-sourced | [Official] |
| 2025-10-06 | Google | Merchant API adds `carrier_shipping` | [Official] |
| 2025-10-28 | OpenAI | PayPal joins as ACP payment provider | [Official per coverage] |
| 2025-10-31 | Google | Merchant API removes `contains_custom_rules` from primary data sources (breaking) | [Official] |
| 2025-11 (late) | Perplexity | Instant Buy with PayPal expands to free US users | [Official per coverage] |
| 2025-11-11 | Google | Merchant API accepts base64url encoded product IDs | [Official] |
| 2025-11-13 | Google | Agentic checkout ("buy for me" with price tracking) live in US with Wayfair, Chewy, Quince, select Shopify merchants | [Official per coverage] |
| 2025-12-10 | Shopify | Winter '26 Edition announces Agentic Storefronts | [Official per coverage] |
| 2025-12-11/12 | Stripe, ACP | Agentic Commerce Suite; ACP fulfillment enhancements | [Official] |
| 2026-01-08 | Microsoft | Copilot Checkout and Brand Agents (US, Copilot.com) | [Official] |
| 2026-01-11 | Google | UCP announced (NRF) with Shopify, Etsy, Wayfair, Target, Walmart; checkout in AI Mode and Gemini; Business Agent; Direct Offers; new conversational attributes promised | [Official] |
| 2026-01-16/30 | ACP | Capability negotiation; extensions, discounts, payment handlers | [Official] |
| 2026-02-28 | Google | Merchant API v1beta retired | [Official per secondary] |
| 2026-03 | Google | Simplified UCP onboarding through Merchant Center announced, phased | [Official per coverage] |
| 2026-03-06 to 03-24 | OpenAI | Standalone Instant Checkout retired; merchant-owned checkout; discovery focus | [Official] |
| 2026-03-11 | Google | Merchant API: `handling_cutoff_timezone`, shipping business days | [Official] |
| 2026-03-19 | schema.org | v30.0: GS1 equivalences, EU DPP examples | [Official] |
| 2026-03-24 | Shopify | Agentic Storefronts at scale | [Official per coverage] |
| 2026-03-25 | Meta | One-tap checkout in Facebook ads with Stripe and PayPal (Adyen and Shopify payments to follow; Instagram announced) | [Official per TechCrunch] |
| 2026-04 | Google | AP2 v0.2 contributed to FIDO Alliance | [Official] |
| 2026-04 | Microsoft | Copilot Checkout in mobile app; 500,000+ merchant catalog | [Official per coverage] |
| 2026-04-09 | Google | Merchant API `base64_encoded_name` output field | [Official] |
| 2026-04-14 | Google | Spec update phase 1: product-level `handling_cutoff_time`, `minimum_order_value`, loyalty labels in shipping, `video_link` (errors from this date) | [Official] |
| 2026-04-17 | ACP | Release: Feed API (push), carts, orders, delegate authentication, MCP binding, `/.well-known/acp.json`, required Idempotency-Key | [Official] |
| 2026-04-22 | Google | Merchant API available in Google Ads scripts as an Advanced API (announced 2026-04-09); scripts must link a Google Cloud project registered with Merchant Center | [Official, Google Ads Developer Blog 2026-04] |
| 2026-04-28 | Google | `pickup_cost` and pickup minimum order value required in UK, CH, EEA | [Official] |
| 2026-05-20 | Google | Marketing Live: UCP checkout to Canada and Australia "in coming months", UK later | [Official] |
| 2026-05-25 | Shopify | Updated Catalog supplemental terms (no sharing with new AI channels until eligible) | [Official per coverage] |
| 2026-06-02 to 06-11 | OpenAI | Product feed ads in ChatGPT Ads Manager (beta) | [Official per coverage] |
| 2026-06-15 | OpenAI | Merchant Feed Terms of Service published | [Unverified, single source] |
| 2026-06-17 | Shopify | Spring '26 Edition (Catalog API, UCP for developers) | [Official per coverage] |
| 2026-06-30 | Google | `video_link` display and policy review start | [Official] |
| 2026-07-10 | OpenAI | Feed retrieval overtakes web retrieval in ChatGPT shopping (observed) | [Study] |
| 2026-07-13 | Google | Merchant API: Q&A, popularity rank, item group title, document links, variant options, related products, short title, vehicle and property attributes, loyalty in shipping, PickupCost, minimum order value; `archived` product flag | [Official] |
| 2026-08-18 | Google | Content API for Shopping shut down | [Official] |
| 2026-08-25 | UCP | Protocol version 2026-08-25 | [Official] |
| 2026-08-31 and 09-16 | OpenAI | ChatGPT Ads self-serve beta expands to more countries | [Official per coverage] |
| 2026-09-01 | Google | Content API requests without approved extended access begin progressive errors | [Official, release notes] |
| 2026-09-09 | Industry | SEJ publishes Profound's feed retrieval analysis | [Study] |
| 2026-09-16 | schema.org | v30.1: retail feed vocabulary and EU Digital Product Passport | [Official] |
| 2026-09-24 to 10-07 | UCP | Lodging booking draft, media variants, `ask` capability for natural-language Q&A | [Official] |
| 2026-09-26 | Google | Flipkart buy button test in Gemini and AI Mode (India) | [Official per TechCrunch] |
| 2026-09-29 | Google | Merchant API offer-level `returns`; lease terms, warranty units, certification links | [Official] |
| 2026-10-06 to 10-07 | Google | UCP integration hub rolling out gradually to US merchants (early access); Canada and Australia moved to 2027 | [Official, help page and Search Engine Land] |
| 2026-10-15 and 2026-12-31 | Google | Extension deadlines offered on the Content API extended access form | [Press, SERoundtable] |
| 2027-01-31 (scheduled) | Google | Minimum product image 500 x 500 | [Official] |

## 4. Best practice consensus
- One source of truth for feed, PDP and JSON-LD; channel transforms in one layer [Practitioner consensus].
- Variant-level, permanent IDs, identical across channels and pixels [Practitioner consensus; Meta and Google docs on ID matching].
- Eligibility and accuracy before optimization; fix disapprovals by revenue order [Practitioner consensus].
- Front-load product type and key attributes in titles; brand first only with brand demand [Official guidance on title structure; Practitioner consensus].
- Correct GTINs on branded products; `identifier_exists=no` only for truly unidentified goods [Official].
- Clean main images of the exact variant; lifestyle images as additional or lifestyle fields [Official].
- Supplemental sources for enrichment and labels; never two primaries for the same products [Official structure, Practitioner consensus].
- Labels encode margin, performance tier, price band, stock and season; refresh weekly [Practitioner consensus].
- Allow shopping crawlers and agents you want visibility from; document the policy [Practitioner consensus].
- For AI surfaces: complete attributes, policies, reviews and accurate shipping and returns are the controllable levers [Practitioner consensus; supported by Profound's feed findings].

## 5. Contested topics (both sides)

| Topic | Side A | Side B | Resolution for the agent |
|-------|--------|--------|--------------------------|
| Lifestyle versus white background main image | Lifestyle raises CTR in visual categories | Plain images are clearer, safer for policy, better for matching | Test per category with SKU splits; keep plain main images by default |
| Performance-based labels (hero, zombie) | Concentrate budget on proven SKUs; isolate zombies for exposure | Labels based on short windows chase noise and starve the long tail; PMax already optimizes per product | Use with minimum click thresholds, 30 to 60 day windows, hysteresis; test zombie campaigns with a time box |
| In-chat checkout value | Fewer steps, new channel (OpenAI, Google, Microsoft, Perplexity positions) | Lower conversion than click-out (Walmart report), loss of customer relationship, low adoption (dozens of Shopify merchants) | Feed first; checkout only after a readiness memo and human decision |
| UCP rollout timing for Canada and Australia | "Coming months" (2026-05-20) | "Next year" (2026-10-07 help page) | Treat as 2027 until confirmed in the account |
| ChatGPT feed format | Google Shopping schema accepted (Google-compatible path; ads feeds reuse Google schema) | Own CSV or Parquet structure with renamed fields | Both exist: Google-compatible path has search on, checkout off; OpenAI format gives per-item control |
| ChatGPT ads feed size limits | 1 million SKUs, 100-product sample | 1,000 minimum, 2 million maximum | Verify in Ads Manager at setup |
| Feed tools versus native apps | Tools give one transformation layer and many destinations | Native apps are free, real time, and enough for single-channel stores | Decide by channels, catalog size and change frequency |
| Shopify AI channel sharing by default | Free distribution, higher conversion claims | Data sharing terms, brand control | Human decision; document |
| PDP versus feed share in ChatGPT (Bazaarvoice says 88 percent PDP-sourced instances; Profound says feeds dominate) | Different denominators and periods | | Treat both as partial views; do both well |

## 6. What top operators do differently
1. They run the feed as a product with a backlog, owners, QA gates, monitoring and change logs, not as a one-time setup.
2. They join business data (COGS, contribution margin, stock velocity, returns) to product data and compute labels automatically.
3. They measure data changes per SKU with controls, so they know which title and image patterns work in their categories.
4. They use the Merchant API reports (price competitiveness, price insights, best sellers, click potential) to prioritize which SKUs to fix and which to stock.
5. They keep IDs identical across Google, Meta, TikTok, Pinterest and OpenAI, and audit pixel match rates monthly.
6. They treat misrepresentation as a website quality program: identity, policies, claims, pricing honesty.
7. They adopt new attributes early (video, Q&A, related products, returns) because AI surfaces reward completeness.
8. They decide agent access deliberately (which crawlers and agents to allow) and track AI referral revenue as its own channel.
9. They track platform specs from code repositories (protos, OpenAPI files), which show fields weeks before help pages.
10. They freeze structural feed changes before peak events and raise refresh frequency during them.

## 7. Common expensive mistakes
| Mistake | Cost | Prevention |
|---------|------|-----------|
| Changing product IDs during a replatform | Resets history; Shopping performance drops for weeks; broken retargeting | ID mapping plan |
| Two primary sources writing the same products | Duplicates, flip-flopping data, disapprovals | One primary, supplemental for overrides |
| Invented or recycled GTINs | Disapprovals, wrong product clusters | GS1 GTINs or MPN plus brand |
| `identifier_exists=no` on branded goods | Limited performance, policy risk | Fix identifiers |
| Geo-IP currency switching for crawlers | Price mismatches, account warnings | Country feeds, no bot redirects |
| Daily feeds for fast-moving stock | Availability mismatches, wasted clicks on out of stock items | API or hourly updates |
| Content API integrations left running after 2026-08-18 | Silent sync failure | Migrate to Merchant API |
| Labels from revenue ROAS without margin | Budget flows to low-margin best sellers | Contribution margin or POAS labels |
| AI-generated images that alter the product | Misrepresentation, returns | Keep product pixels unchanged; disclose metadata |
| Opening a new Merchant Center account after suspension | Permanent suspension of related accounts | Fix and request review |
| Building in-chat checkout integrations in 2026 without invitation | Engineering cost with little volume | Feed first |
| Blocking AI crawlers unintentionally via bot manager | Invisible in ChatGPT, Perplexity, Copilot answers | Agent access policy and log review |

## 8. Benchmarks (source, date, sample, caveat)

| Benchmark | Value | Source, date | Sample | Caveat |
|-----------|-------|-------------|--------|--------|
| Feed share of ChatGPT shopping picks | About 62 to 65 percent after July 2026 | Profound via SEJ, 2026-09 | 1.76 million prompt runs (July), 97,725 runs (September sample) | Tracked prompts only; not all ChatGPT shopping; no causal proof |
| Merchant concentration in ChatGPT shopping | Top 10 share 41.8 percent | Profound, 2026-09 | Same | Same |
| ChatGPT carousel overlap with Google Shopping | About 83 percent | SEL analysis via secondary, 2025 | 43,000 products, 10 verticals | Pre-feed-shift period |
| Instant Checkout adoption (Shopify) | About 12 to 30 merchants live | Forrester and press, 2026-02 | Estimates | Contested |
| Copilot purchase uplift | 53 percent more purchases within 30 minutes | Microsoft, 2026-01 | Not disclosed | Vendor claim |
| Shopify Catalog conversion | 2x versus scraped data | Shopify, 2026 | Not disclosed | Vendor claim |
| Approval rate target | 98 percent or more | Practitioner consensus | n/a | Depends on catalog and category |
| Parity mismatch target | Under 1 percent | Practitioner consensus | n/a | Sample-based |

No credible public benchmark for title optimization lift was verified in this research cycle; vendor case studies exist but lack method disclosure [Unverified]. Compare each project to its own history first.

## 9. Tools, APIs and MCP servers

| Tool or API | Type | Use | Status |
|-------------|------|-----|--------|
| Google Merchant API v1 | Official API | Products, data sources, inventories, promotions, reviews, reports, notifications, issue resolution, loyalty customers, conversions | GA since 2025-08 |
| Product Studio API | Official API (alpha) | Image and text generation for products | v1alpha |
| Google Ads API and scripts | Official | Product performance by item and custom attribute | Current |
| Google Ads MCP server | Official open source | Read Google Ads data from agents | Released 2025 |
| Meta Marketing API v26.0 | Official | Catalogs, `items_batch`, product sets, diagnostics, generated background images | Current |
| Pinterest API v5 (5.28.0) | Official | Catalog items, product groups, `ai_disclosures` | Current |
| TikTok Business API | Official | Catalog management | Verify endpoints |
| OpenAI commerce file upload | Official | ChatGPT shopping feeds via SFTP | Application required |
| ChatGPT Ads Manager feeds | Official | Product feed ads | Beta |
| ACP (2026-04-17) | Open spec | Feed API, checkout, delegate payment, carts, MCP binding | Stable versions |
| UCP (2026-08-25) | Open spec | Catalog, checkout, orders, identity linking, ask, MCP and A2A bindings | Active |
| AP2 (v0.2) | Open spec, FIDO Alliance | Agent payment mandates | Pilots |
| Feedonomics, Productsup, Channable, DataFeedWatch, GoDataFeed, Feedoptimise, Lengow | Feed platforms | Multi-channel transforms, several support OpenAI feeds | Commercial |
| Producthero | Feed optimization and labels, CSS | Performance labels, title optimization | Commercial |
| Shopify Google and YouTube app; Google for WooCommerce | Native connectors | Merchant Center sync | Current (WooCommerce 3.9.5, 2026-09-29) |
| Shopify Catalog API, Storefront and developer MCP servers | Platform | Agent access to Shopify product data | Current |
| This skill's scripts (`feed_qa.py`, `label_builder.py`, `pdp_parity.py`) | Local scripts | QA, labels, parity | Tested 2026-10-08 |

## 10. Official sources to monitor
- Merchant Center announcements: https://support.google.com/merchants/announcements/6192467
- Product data specification: https://support.google.com/merchants/answer/7052112
- Merchant API protos and commits: https://github.com/googleapis/googleapis/tree/master/google/shopping/merchant
- UCP help: https://support.google.com/merchants/answer/16837055 and onboarding https://support.google.com/merchants/answer/16992327
- UCP repository: https://github.com/Universal-Commerce-Protocol/ucp
- OpenAI merchants: https://chatgpt.com/merchants/ and specs https://developers.openai.com/commerce
- ACP repository: https://github.com/agentic-commerce-protocol/agentic-commerce-protocol
- AP2 repository: https://github.com/google-agentic-commerce/AP2
- Microsoft Advertising blog: https://about.ads.microsoft.com/en/blog
- Meta Graph API changelog: https://developers.facebook.com/docs/graph-api/changelog
- Pinterest API description: https://github.com/pinterest/api-description
- Shopify changelog: https://changelog.shopify.com
- schema.org releases: https://schema.org/docs/releases.html

## 11. Open questions and watch list
1. When in 2027 will UCP checkout reach Canada and Australia, and when the UK? (Eligibility attribute confirmed as `native_commerce` with `checkout_eligibility`.)
2. Will OpenAI open the self-serve merchant platform in 2026, and will organic and ads feeds merge?
3. Which of the July 2026 Merchant API attributes (Q&A, related products, popularity rank) does Google surface in AI Mode, and in which countries?
4. Will Google adopt schema.org 30.1 properties (`itemPopularity`, `isOftenBoughtWith`, `consumerNotice`) in structured data documentation?
5. Meta: whether one-tap ad checkout reaches Instagram and which markets beyond the initial launch (7 new markets were reported for spring 2026) [Unverified].
6. TikTok Shop: official GMV Max thresholds (creative minimums and daily budget floors differ by source: 10 or 20 videos per product, $50 or $100 per day) [Contested].
7. Copilot Checkout expansion to Bing, Edge, MSN, Windows and to non-US markets.
8. Perplexity merchant terms and the remanded Amazon v. Perplexity case (Ninth Circuit vacated the Comet injunction on 2026-08-04; motion to dismiss filed 2026-09-11).
9. Content API full decommission timing (early 2027 reported by one vendor) and HTTP 410 behavior after extension dates lapse [Unverified].
10. Merchant Center enforcement of separate online and in-store IDs when attributes differ.


## 12. Implications for the commerce-feeds playbook
1. The audit now checks Merchant API migration status (B3) and AI surface decisions (I4, I5) as standard items.
2. Title programs include `short_title` and conversational attributes as they reach each country.
3. The ChatGPT module leads with feed enrollment and treats checkout as optional, reflecting the March 2026 pivot.
4. Agentic checkout of any kind requires a readiness memo and a human decision (customer relationship, operations, measurement).
5. The agent reads platform code repositories during freshness checks because they date changes precisely.
6. Agent access (robots and bot managers) is a documented business decision handed to seo for implementation.

## 13. Sources
1. Merchant API products_common.proto. Google (googleapis). https://github.com/googleapis/googleapis/blob/master/google/shopping/merchant/products/v1/products_common.proto. Commits 2025-08-05 to 2026-09-29.
2. Commit history, products_common.proto. Google. https://github.com/googleapis/googleapis/commits/master/google/shopping/merchant/products/v1/products_common.proto. 2026-10-08 read.
3. Commit faa8119 (new attributes including Q&A). Google. https://github.com/googleapis/googleapis/commit/faa8119. 2026-07-13.
4. Commit 08ce6da (offer-level returns). Google. https://github.com/googleapis/googleapis/commit/08ce6da. 2026-09-29.
5. Merchant API products.proto and productinputs.proto. Google. https://github.com/googleapis/googleapis/tree/master/google/shopping/merchant/products/v1. 2026.
6. Merchant API reports.proto. Google. https://github.com/googleapis/googleapis/blob/master/google/shopping/merchant/reports/v1/reports.proto. 2026.
7. Merchant API datasourcetypes.proto. Google. https://github.com/googleapis/googleapis/blob/master/google/shopping/merchant/datasources/v1/datasourcetypes.proto. 2025-08-04 and 2025-10-31.
8. Shopping types.proto. Google. https://github.com/googleapis/googleapis/blob/master/google/shopping/type/types.proto. 2026.
9. Introducing Merchant API. Google Merchant Center Help. https://support.google.com/merchants/answer/16493611?hl=en. 2025 (via search).
10. Merchant Center product data specification update 2026. Google Merchant Center Help. https://support.google.com/merchants/answer/16989427?hl=en. 2026 (via search).
11. Merchant Center announcements change log. Google. https://support.google.com/merchants/announcements/6192467?hl=en. Ongoing (via search).
12. Google Updates Some Merchant Center Product Specifications For 2026. Search Engine Roundtable. https://www.seroundtable.com/google-updates-some-merchant-center-product-spec-41171.html. 2026.
13. Google Merchant API replacing the Content API for Shopping. Search Engine Roundtable. https://www.seroundtable.com/google-merchant-api-content-api-for-shopping-39958.html. 2025.
14. Google launches Merchant API, signals transition from Content API. PPC Land. https://ppc.land/google-launches-merchant-api-signals-transition-from-content-api/. 2024 to 2025.
15. Google is sunsetting the Content API for Shopping. Producthero. https://www.producthero.com/post/google-is-sunsetting-the-content-api-for-shopping-what-you-need-to-know. 2025 to 2026.
16. Google Merchant API migration before the August 2026 deadline. Productsup. https://www.productsup.com/blog/google-merchant-api-migration-what-changes-before-the-august-2026-deadline-and-how-to-prepare/. 2026.
17. Google Merchant API migration. Feedonomics. https://feedonomics.com/blog/google-merchant-api-migration/. 2025 to 2026.
18. Merchant API in Google Ads Scripts: April 22 migration. Digital Applied. https://www.digitalapplied.com/blog/merchant-api-google-ads-scripts-april-22-migration. 2026.
19. Content API for Shopping sunset: extension form. Elsop. https://www.elsop.com/content-api-shopping-sunset/. 2026.
20. GMC multi-channel product ID requirements. Adsroid. https://adsroid.com/google-merchant-center-updates-multi-channel-product-id-requirements/. 2026-01.
21. GMC Product Data Specification 2026 released. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-04/gmc-product-data-specification-2026-released/. 2026-04.
22. Google for WooCommerce readme and changelog. WooCommerce and Google. https://github.com/woocommerce/google-listings-and-ads. 2026-09-29.
23. About UCP and UCP-powered checkout on Google. Google Merchant Center Help. https://support.google.com/merchants/answer/16837055?hl=en. 2026 (via search).
24. How to onboard to the UCP integration hub. Google Merchant Center Help. https://support.google.com/merchants/answer/16992327?hl=en. 2026-10 (via search).
25. Under the Hood: Universal Commerce Protocol. Google Developers Blog. https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/. 2026-01 (via search).
26. New tech and tools for retailers in an agentic shopping era. Google. https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/. 2026-01 (via search).
27. Google Marketing Live 2026 shopping updates (title paraphrased). Google. https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/. 2026-05-20 (via search).
28. UCP repository and commit log. Universal Commerce Protocol. https://github.com/Universal-Commerce-Protocol/ucp. Commits to 2026-10-07.
29. UCP catalog capability. Universal Commerce Protocol. https://github.com/Universal-Commerce-Protocol/ucp/blob/main/docs/specification/shopping/catalog/index.md. 2026.
30. UCP specification overview. Universal Commerce Protocol. https://github.com/Universal-Commerce-Protocol/ucp/blob/main/docs/specification/overview/index.md. 2026.
31. Google rolling out agentic Buy for me. 9to5Google. https://9to5google.com/2025/11/13/google-agentic-shopping/. 2025-11-13.
32. Google rolls out agentic commerce in Search and Gemini. The Register. https://www.theregister.com/2026/01/12/google_gemini_agentic_ai_shopping_protocol/. 2026-01-12.
33. Google Search adds AI try-on, previews agentic checkout. Search Engine Land. https://searchengineland.com/google-search-ai-try-on-agentic-checkout-455716. 2025-05.
34. Canada and Australia face 2027 wait for Merchant Center UCP hub. PPC Land. https://ppc.land/canada-and-australia-face-2027-wait-for-googles-merchant-center-ucp-hub/. 2026-10.
35. Google tests buying from Flipkart through Gemini and AI Mode in India. TechCrunch. https://techcrunch.com/2026/09/26/google-tests-buying-from-walmart-owned-flipkart-through-gemini-and-ai-mode-in-india/. 2026-09-26.
36. Google donates Agent Payments Protocol to FIDO Alliance. Google. https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/. 2026-04 (via search).
37. AP2 repository. Google Agentic Commerce. https://github.com/google-agentic-commerce/AP2. 2026.
38. Agentic commerce solution from PayPal and Google Cloud. Google Cloud Blog. https://cloud.google.com/blog/topics/financial-services/introducing-an-agentic-commerce-solution-for-merchants-from-paypal-and-google-cloud. 2025 (via search).
39. Google's Agent Payments Protocol fleshes out AI agent commerce. Constellation Research. https://www.constellationr.com/insights/news/googles-agent-payments-protocol-fleshes-out-ai-agent-commerce. 2025.
40. Google UCP merchant guide. commercetools. https://commercetools.com/blog/google-ucp-merchant-guide-to-agentic-commerce. 2026.
41. Google UCP and Merchant Center. ChannelEngine. https://www.channelengine.com/en/blog/google-universal-commerce-protocol-merchant-center-ai-shopping. 2026.
42. Agentic Commerce Protocol repository. OpenAI and Stripe. https://github.com/agentic-commerce-protocol/agentic-commerce-protocol. 2026-04-17 stable.
43. ACP changelog 2026-04-17. OpenAI and Stripe. https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/changelog/2026-04-17.md. 2026-04-17.
44. ACP Feed API OpenAPI. OpenAI and Stripe. https://github.com/agentic-commerce-protocol/agentic-commerce-protocol/blob/main/spec/2026-04-17/openapi/openapi.feed.yaml. 2026-04-17.
45. Power product discovery in ChatGPT. OpenAI. https://chatgpt.com/merchants/. 2026 (via search).
46. Commerce products spec (file upload). OpenAI Developers. https://developers.openai.com/commerce/specs/file-upload/products. Undated (via search).
47. Commerce file upload overview. OpenAI Developers. https://developers.openai.com/commerce/specs/file-upload/overview. Undated (via search).
48. OpenAI revamps shopping experience in ChatGPT after struggling with Instant Checkout. CNBC. https://www.cnbc.com/2026/03/24/openai-revamps-shopping-experience-in-chatgpt-after-instant-checkout.html. 2026-03-24.
49. OpenAI's first crack at online shopping stumbled. CNBC. https://www.cnbc.com/2026/03/20/open-ai-agentic-shopping-etsy-shopify-walmart-amazon.html. 2026-03-20.
50. OpenAI's plans to make ChatGPT more like Amazon. TechCrunch. https://techcrunch.com/2026/03/24/openais-plans-to-make-chatgpt-more-like-amazon-arent-going-so-well. 2026-03-24.
51. ChatGPT lets shoppers buy products within the platform. Retail Dive. https://www.retaildive.com/news/openai-chatgpt-instant-checkout-agentic-commerce-etsy-shopify/761442/. 2025-09-29.
52. OpenAI expands agentic commerce push. Digital Commerce 360. https://www.digitalcommerce360.com/2026/02/16/openai-expands-agentic-commerce-push/. 2026-02-16.
53. ChatGPT Ads Manager now supports product feeds. PPC Land. https://ppc.land/chatgpt-ads-manager-now-supports-product-feeds-after-checkout-is-killed/. 2026-06.
54. ChatGPT Ads gains upload product feeds. Search Engine Roundtable. https://www.seroundtable.com/chatgpt-ads-product-feeds-41488.html. 2026-06.
55. ChatGPT product feed ads opening via Ads Manager beta. Geekseller. https://www.geekseller.com/blog/openai-chatgpt-product-feed-ads-are-now-opening-to-more-sellers-via-ads-manager-beta/. 2026-06.
56. ChatGPT Shopping results lean hard on product feeds. Search Engine Journal. https://www.searchenginejournal.com/chatgpt-shopping-results-lean-hard-on-product-feeds/589000/. 2026-09-09.
57. Profound launches shopping analysis. PR Newswire. https://www.prnewswire.com/news-releases/profound-launches-shopping-analysis-as-ai-assistants-become-the-new-front-door-to-retail-302614397.html. 2026.
58. OpenAI launches self-serve Ads Manager for ChatGPT. Search Engine Journal. https://www.searchenginejournal.com/openai-launches-self-serve-ads-manager-for-chatgpt/573971/. 2026.
59. How retail executives will evaluate ChatGPT checkout. Modern Retail. https://www.modernretail.co/technology/how-retail-executives-will-be-evaluating-chatgpt-checkout-this-holiday-season/. 2025-11.
60. Your Google Shopping feed is already powering ChatGPT. Athos Commerce. https://athoscommerce.com/blog/your-google-shopping-feed-is-already-powering-chatgpt/. 2026.
61. How to get ChatGPT to recommend your product. Bazaarvoice. https://www.bazaarvoice.com/blog/how-to-get-featured-on-chatgpt-ai-recommendations/. 2026.
62. Product feeds for AI. Patrick Stox. https://patrickstox.com/ecommerce-seo/ai-commerce/product-feeds-for-ai/. 2026.
63. Conversations that convert: Copilot Checkout and Brand Agents. Microsoft Advertising Blog. https://about.ads.microsoft.com/en/blog/post/january-2026/conversations-that-convert-copilot-checkout-and-brand-agents. 2026-01 (via search).
64. Microsoft launches Copilot Checkout and Brand Agents. Search Engine Land. https://searchengineland.com/microsoft-launches-copilot-checkout-and-brand-agents-467175. 2026-01.
65. Copilot in-app checkout and merchant data from 500,000 sellers. Windows Central. https://www.windowscentral.com/microsoft/windows-11/copilots-shopping-upgrade-brings-checkout-to-the-mobile-app-with-deeper-data-from-half-a-million-merchants. 2026-04.
66. Microsoft and PayPal launch Copilot Checkout. gHacks. https://www.ghacks.net/2026/01/09/microsoft-and-paypal-launch-copilot-checkout-for-in-chat-purchases/. 2026-01-09.
67. Copilot Checkout expands shopping capabilities. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-01/copilot-checkout-expands-shopping-capabilities-in-microsoft-ecosystem/. 2026-01.
68. Perplexity Shopping guide. Shopify Blog. https://www.shopify.com/blog/perplexity-shopping. 2025 to 2026.
69. Perplexity launches free shopping agent. TechBuzz. https://www.techbuzz.ai/articles/perplexity-ai-launches-free-shopping-agent-to-challenge-openai. 2025-11.
70. Spring '26 Edition. Shopify. https://www.shopify.com/news/spring-26-edition-merchant. 2026 (via search).
71. Shopify launches Agentic Storefronts. The Keyword (news site). https://www.thekeyword.co/news/shopify-launches-agentic-storefronts. 2026.
72. Facebook Python Business SDK (ProductItem, ProductCatalog, API v26.0). Meta. https://github.com/facebook/facebook-python-business-sdk. 2026.
73. Pinterest API description (OpenAPI v5.28.0). Pinterest. https://github.com/pinterest/api-description. 2026.
74. schema.org release history (v28.0, v29.0, v30.0, v30.1). schema.org. https://schema.org/docs/releases.html. 2024-09-17 to 2026-09-16.
75. Semrush: Universal Commerce Protocol explained. Semrush. https://www.semrush.com/blog/universal-commerce-protocol/. 2026.
76. Google agentic checkout guide. BigCommerce. https://www.bigcommerce.com/articles/ecommerce/google-agentic-checkout/. 2026.
77. Secure agent commerce with AP2 and UCP codelab. Google. https://codelabs.developers.google.com/next26/adk-agent-commerce. 2026.
78. Native commerce [native_commerce]. Google Merchant Center Help. https://support.google.com/merchants/answer/17251586. Checked 2026-10 (via search).
79. About the Universal Commerce Protocol (UCP) and UCP-powered checkout feature on Google. Google Merchant Center Help. https://support.google.com/merchants/answer/16837055. Checked 2026-10 (via search).
80. How to onboard to the UCP integration hub in Merchant Center. Google Merchant Center Help. https://support.google.com/merchants/answer/16992327. 2026-10 (via search).
81. Google rolls out Merchant Center UCP integration hub in the U.S. Search Engine Land. https://searchengineland.com/google-rolls-out-merchant-center-ucp-integration-hub-in-the-u-s-493889. 2026-10-06.
82. Canada and Australia face 2027 wait for Google's Merchant Center UCP hub. PPC Land. https://ppc.land/canada-and-australia-face-2027-wait-for-googles-merchant-center-ucp-hub/. 2026-10.
83. Merchant API is coming to Google Ads scripts starting April 22, 2026. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/04/merchant-api-is-coming-to-google-ads.html. 2026-04.
84. Content API for Shopping release notes. Google for Developers. https://developers.google.com/shopping-content/guides/rel-notes. Checked 2026-10 (via search).
85. Google Content API for Shopping Extended Access Form. Search Engine Roundtable. https://www.seroundtable.com/google-content-api-extension-41710.html. 2026.
86. Meta phases out Facebook and Instagram shops checkout by August 2025. PPC Land. https://ppc.land/meta-phases-out-facebook-and-instagram-shops-checkout-by-august-2025/. 2025.
87. Updates to Meta Shops checkout for BigCommerce. BigCommerce. https://www.bigcommerce.com/blog/updates-to-meta-shops-checkout-for-bigcommerce/. 2025.
88. Meta turns to AI to make shopping easier on Instagram and Facebook. TechCrunch. https://techcrunch.com/2026/03/25/meta-turns-to-ai-to-make-shopping-easier-on-instagram-and-facebook/. 2026-03-25.
89. TikTok Shop Makes GMV Max Ads Mandatory From Sept 1. CedCommerce. https://cedcommerce.com/blog/tiktok-shop-mandates-gmv-max-use-for-ads-what-this-means-for-your-strategy/. 2025.
90. Import from Google Merchant Center. Microsoft Advertising Help. https://help.ads.microsoft.com/apex/index/3/en/56870. Checked 2026-10 (via search).
91. Microsoft Advertising simplifies Google Merchant Center import. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2024-09/microsoft-advertising-simplifies-google-merchant-center-import/. 2024-09.
92. Feed: How to submit my GoDataFeed feed to ChatGPT Ads? GoDataFeed Help. https://help.godatafeed.com/hc/en-us/articles/51837706971675-Feed-How-to-submit-my-GoDataFeed-feed-to-ChatGPT-Ads. 2026.
93. Amazon.com Services, LLC v. Perplexity AI, Inc. (No. 26-1444). US Court of Appeals for the Ninth Circuit. https://cdn.ca9.uscourts.gov/datastore/opinions/2026/08/04/26-1444.pdf. 2026-08-04.
94. Amazon wins court order to block Perplexity's AI shopping agent. CNBC. https://www.cnbc.com/2026/03/10/amazon-wins-court-order-to-block-perplexitys-ai-shopping-agent.html. 2026-03-10.
95. Catalog Product Parameters. TikTok Ads Help. https://ads.tiktok.com/help/article/catalog-product-parameters. Updated 2025-02 (via search).
96. How to create a Catalog. TikTok Ads Help. https://ads.tiktok.com/help/article/create-manage-catalogs. Updated 2026-01 (via search).
