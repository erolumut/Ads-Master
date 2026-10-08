# Other AI Shopping Surfaces: Google AI Mode and Gemini (UCP), Microsoft Copilot, Perplexity, Amazon, Shopify Catalog

> Live versus announced matters more here than anywhere. Every row carries a status. Knowledge as of 2026-10-08.

## 1. Status matrix

| Surface | Discovery from feeds | Agentic checkout | Merchant access | Status |
|---------|---------------------|------------------|-----------------|--------|
| Google AI Mode, AI Overviews, Gemini (shopping) | Yes: Merchant Center free listings and the Shopping Graph | UCP-powered checkout with Google Pay | Early access for select merchants; Merchant Center UCP integration hub for US merchants first, Canada and Australia next year | Live (US, select merchants) |
| Google "agentic checkout" with price tracking | Yes | Google buys on the merchant site with Google Pay after the user confirms | Started with Wayfair, Chewy, Quince and select Shopify merchants (2025-11-13) | Live (US) |
| Google in India (Flipkart test) | Yes | Buy button test in Gemini and AI Mode for some users and products | Single partner test, technology not disclosed | Test (2026-09-26) |
| Microsoft Copilot | Yes: merchant feeds and web; catalog of more than 500,000 merchants | Copilot Checkout (PayPal, Stripe, Shopify) | Shopify auto-enrolled with opt-out; PayPal and Stripe merchants apply | Live (US, Copilot.com since 2026-01-08; mobile app since 2026-04) |
| ChatGPT | Yes: feeds dominate retrieval since 2026-07 | Standalone Instant Checkout retired 2026-03 | Shopify and Etsy automatic; others apply | Live (US) for discovery. See [ChatGPT module](chatgpt-shopping-and-agentic-commerce.md) |
| Perplexity | Yes: merchant program (since 2024-11), Shopify and PayPal integrations | Instant Buy with PayPal; expanded to free US users late 2025 | Free to join per launch messaging; no paid placement | Live (US) |
| Amazon Rufus and Buy for Me | Amazon catalog; Buy for Me reads brand websites | Buy for Me purchases on third-party brand sites inside the Amazon app | Brands can opt out [Unverified mechanism] | Live in beta since 2025 [Unverified current scope] |
| Shopify Agentic Storefronts and Catalog | Shopify Catalog syndicates product data to AI channels | Depends on the channel | On by default for eligible stores; non-Shopify brands via an Agentic plan | Live (launched at scale 2026-03-24 per coverage) |

## 2. Google: AI Mode, Gemini, UCP

### 2.1 Timeline
| Date | Event | Label |
|------|-------|-------|
| 2025-05 | Google I/O: AI Mode shopping experience, virtual try-on, agentic checkout preview | [Official, 2025-05] |
| 2025-09-16 | Agent Payments Protocol (AP2) announced with 60+ partners | [Official, 2025-09] |
| 2025-11-13 | Agentic checkout rolls out in the US: track a price, Google buys on the merchant site with Google Pay after confirmation; AI calling to local stores | [Official, 2025-11] |
| 2026-01-11 | Universal Commerce Protocol (UCP) announced at NRF, co-developed with Shopify, Etsy, Wayfair, Target and Walmart, endorsed by 20+ companies including Visa, Stripe and The Home Depot; checkout in AI Mode and Gemini; Business Agent; Direct Offers pilot; "dozens of new" Merchant Center attributes for conversational discovery (answers to product questions, compatible accessories, substitutes) | [Official, 2026-01] |
| 2026-03 | Simpler Merchant Center onboarding path for UCP announced, phased over months | [Official per coverage, 2026-03] |
| 2026-04 | AP2 v0.2 contributed to the FIDO Alliance | [Official, 2026-04] |
| 2026-05-20 | Google Marketing Live: UCP-powered checkout to roll out in Canada and Australia "in the coming months", later the UK | [Official, 2026-05] |
| 2026-07-13 | Merchant API adds Q&A, related products, variant options, popularity rank, item group title, document links | [Official, 2026-07] |
| 2026-08-25 | UCP protocol version 2026-08-25 released | [Official, 2026-08] |
| 2026-10-07 | Merchant Center help page for the UCP integration hub: US first, Australia and Canada next year (conflicts with the May "coming months" wording) | [Official, 2026-10]; timing [Contested] |

### 2.2 How UCP checkout works
- Merchant publishes a UCP profile at `/.well-known/ucp` listing capabilities (for example `dev.ucp.shopping.checkout`, `dev.ucp.shopping.order`, `dev.ucp.common.identity_linking`, catalog search `dev.ucp.shopping.catalog.search` and lookup `dev.ucp.shopping.catalog.lookup`, discounts and fulfillment extensions). Platforms advertise their profile on each request (`UCP-Agent` header or MCP `meta`).
- Transports: REST (OpenAPI), MCP (OpenRPC), A2A (Agent Card), embedded checkout (OpenRPC).
- Versioning by date; the business and platform negotiate the highest mutual version.
- Checkout: the agent creates a merchant-side checkout session; payment uses a token from the payment provider (Google Pay with Google Wallet credentials), so card numbers never pass through the agent. The merchant remains seller of record.
- Integration styles: native (API integration, more engineering, the baseline route) or embedded (merchant checkout rendered in the surface, more customization).
- Merchant Center side: product-level eligibility (reported as a `native_commerce` attribute) plus completed return policies; reporting context `FREE_LISTINGS_UCP_CHECKOUT` in Merchant API [Official enum; attribute name Unverified].
- New capabilities in the repo in late 2026: `ask` capability for natural-language Q&A (2026-10-07), lodging booking (2026-09-24), media variants (image, video, 3D, 2026-09-29) [Official, 2026-10].

### 2.3 What commerce-feeds does for Google AI surfaces
1. Free listings on, clean, rich: the cheapest path into AI Mode and Gemini product results.
2. Fill the conversational attributes as they become supported: `product_highlight`, `product_detail`, `questions_and_answers`, `related_products`, `variant_options`, `item_group_title`, `document_links`, `video_link`, offer-level `returns`.
3. Shipping and returns precise per country (AI answers quote delivery speed and return windows).
4. Reviews: product review feed or aggregator.
5. Price competitiveness: AI comparisons surface price differences directly.
6. Platform route for UCP: Shopify and other platforms co-developed UCP; check the platform's AI channel settings first. Custom stacks: request early access through Merchant Center and plan the UCP server work with engineering.
7. Decision with the human: checkout in AI Mode changes the customer relationship (account linking, order emails, returns flow). Draft a readiness memo before enrolling.

### 2.4 AP2 (Agent Payments Protocol)
- Purpose: verifiable proof that a user authorized an agent purchase, through signed mandates. UCP is designed to interoperate with AP2; a merchant can publish a signing key for AP2 merchant authorization in its UCP profile.
- Status: announced 2025-09-16; v0.2 and transfer to FIDO Alliance in April 2026; public deployments in 2026 were pilots (PayPal, Mastercard Agent Pay inside PayPal, a crypto extension) [Official for governance; deployments per secondary sources].
- Merchant action in 2026: none directly in most cases. Payment providers implement AP2. Ask your PSP about agent payment support.

## 3. Microsoft Copilot
- Copilot Checkout: launched 2026-01-08 on Copilot.com (US) with PayPal, Stripe and Shopify. Shopify merchants auto-enrolled after an opt-out window; PayPal and Stripe merchants apply. Merchants remain merchant of record and own customer data [Official, 2026-01].
- Brand Agents: merchants shape a branded shopping agent's tone; analytics through Microsoft Clarity [Official, 2026-01].
- April 2026: checkout in the Copilot mobile app; catalog data from more than 500,000 merchants [Official per coverage, 2026-04].
- Microsoft reported journeys that included Copilot had 53 percent more purchases within 30 minutes [Official claim, unaudited].
- Feed work: Microsoft Merchant Center store feed complete and approved; policy pages; accurate stock. See [Microsoft and other catalogs](microsoft-pinterest-and-other-catalogs.md).

## 4. Perplexity
- Merchant program launched November 2024 to share product data for shopping answers; described as free (no listing fees or commissions) at launch [Official at launch; current terms Unverified].
- Instant Buy with PayPal (and Venmo, cards) for US users; expanded to free users in late November 2025; merchant network about 5,000 PayPal merchants with more via BigCommerce, Shopware and Wix reported [Official per coverage, 2025-11; counts Unverified].
- Shopify notes that Instant Buy orders may not appear in Shopify admin; fulfillment stays with the merchant [Official per Shopify blog].
- No paid placement in shopping results per Perplexity statements [Official per coverage].
- Legal risk: Amazon sued Perplexity in November 2025 over its Comet browser agent shopping on Amazon [Unverified current status].
- Feed work: apply to the merchant program, keep Shopify product data complete, ensure PerplexityBot can crawl PDPs.

## 5. Amazon (Rufus, Buy for Me)
- Rufus answers shopping questions from Amazon catalog data and reviews; for brands selling on Amazon, the listing content (titles, bullets, A+ content, Q&A) is the feed equivalent [Practitioner consensus].
- Buy for Me (beta since 2025) lets Amazon app users buy products from brand websites that Amazon does not sell, with Amazon's agent completing checkout on the brand site [Official at launch, 2025; current scope Unverified].
- Amazon restricts other companies' shopping agents on Amazon.com (robots rules and litigation) [Practitioner consensus].
- Implication for DTC brands: your PDP must be machine-readable (server-rendered price, stock, variants, JSON-LD) because agents from several companies read it. Decide with the human whether to allow or block each agent; document the choice.

## 6. Shopify (Agentic Storefronts, Catalog, UCP)
- Agentic Storefronts: announced in the Winter '26 Edition (2025-12-10), launched at scale 2026-03-24; merchants toggle AI channels (ChatGPT, Copilot, Perplexity, Google AI Mode and Gemini per later coverage) in Shopify admin [Official per coverage; channel list Contested across sources].
- Shopify Catalog: structured dataset of products that agents search; infers categories, extracts attributes, consolidates variants, clusters identical items. Catalog API and UCP open to developers. Non-Shopify brands can sync via an Agentic plan [Official per coverage, 2026].
- Updated Shopify supplemental terms effective 2026-05-25: Catalog does not share data with new AI channels until the merchant is flagged eligible [Official per coverage, 2026-05].
- Orders show the AI platform as the traffic source in Shopify admin reports.
- Shopify claims Catalog-powered AI searches convert at 2x scraped data [Official claim, unaudited].
- Feed work on Shopify: the product data in Shopify (titles, descriptions, metafields, variants, GTIN in barcode field, category) is now the feed for AI channels. Fix data at the source; a Google-only supplemental feed does not reach Shopify Catalog.

## 7. Prioritization by business model

| Business | First | Second | Third |
|----------|-------|--------|-------|
| Shopify DTC, US | Shopify product data quality (it syndicates to AI channels) | Google free listings and conversational attributes | Decide AI channel toggles and Copilot Checkout with the human |
| Custom platform DTC, US | Google Merchant Center quality plus PDP structured data | ChatGPT application with OpenAI-format feed | Microsoft store feed for Copilot; UCP early access if engineering capacity exists |
| Marketplace or multi-seller | `external_seller_id` and seller data in Merchant Center | ACP or UCP only through platform partners | Agent access policy for the site |
| Non-US merchant | Google free listings (AI Mode is global for discovery) | Watch UCP country rollout (CA, AU, UK announced) | ChatGPT ads countries if paid feeds fit |
| B2B ecommerce | Complete specs, documents (`document_links`), compatibility in `related_products` | Decimal quantities and B2B carts exist in ACP (2026-04-17) | Pricing visibility rules (login prices block agents) |

## 8. Agent access policy (decide and document)

| Agent or crawler | Purpose | Default recommendation |
|------------------|---------|-----------------------|
| Googlebot, Storebot-Google | Search, Shopping, crawl checks | Allow |
| Google-Extended | Gemini training control | Business decision; does not affect Search |
| OAI-SearchBot | ChatGPT search and shopping | Allow if you want ChatGPT visibility |
| GPTBot | OpenAI training | Business decision |
| ChatGPT-User | User-initiated browsing | Allow for shopping use cases |
| PerplexityBot | Perplexity index | Allow if you want Perplexity visibility |
| Bingbot | Bing, Copilot | Allow |
| facebookexternalhit, Meta crawlers | Catalog images and link previews | Allow |
| Amazon agent (Buy for Me) | Third-party purchase | Business decision |

Hand off robots.txt and bot-manager changes to seo (implementation) and ai-search-optimization (visibility impact). Never change robots.txt or CDN rules without approval.

## 9. Agentic checkout readiness memo (template)

Use before enrolling in UCP checkout, Copilot Checkout, Perplexity Instant Buy or any in-chat checkout.

```
# Agentic checkout readiness: <surface> (<date>)
Data used: <sources, date range>
1. Eligibility: country, platform, payment provider, program status (live, early access, waitlist).
2. Customer relationship: who is merchant of record, account linking, order emails, marketing consent capture.
3. Operations: order ingestion path into OMS, fulfillment SLA, returns and refunds flow, customer service.
4. Payments and risk: PSP support (Google Pay, PayPal, Stripe), fraud screening, chargeback ownership.
5. Data: feed eligibility attributes, price and stock latency, policies (returns, shipping, privacy, terms).
6. Measurement: how orders are tagged (order source), how revenue reaches analytics and ad platforms.
7. Commercials: fees (if any), contract terms, opt-out process.
8. Risks: brand control, data sharing terms, conversion versus click-out (Walmart reported in-chat conversion at about one third of click-outs for ChatGPT in 2026 [Unverified]).
9. Recommendation: enroll, pilot on a subset, or wait. Decision owner: human.
```

## 10. UCP business profile (illustrative shape)

The live schema is in the UCP repository; this sketch shows what engineering will publish at `/.well-known/ucp`. Field names beyond `ucp`, capabilities and `keys` must be taken from the current spec version.

```json
{
  "ucp": {
    "version": "2026-08-25",
    "capabilities": [
      {"name": "dev.ucp.shopping.catalog.search"},
      {"name": "dev.ucp.shopping.catalog.lookup"},
      {"name": "dev.ucp.shopping.checkout"},
      {"name": "dev.ucp.shopping.order"},
      {"name": "dev.ucp.common.identity_linking"}
    ]
  },
  "keys": []
}
```

commerce-feeds role: confirm the catalog data the profile exposes matches the Merchant Center feed (same IDs, prices, availability), and that policies referenced in checkout match the site.

## 11. Watch list (check monthly)
- UCP country rollout dates and the Merchant Center UCP hub requirements.
- Whether OpenAI opens the self-serve merchant platform; any return of checkout in ChatGPT.
- Shopify AI channel list and default sharing rules.
- Copilot Checkout country expansion (Bing, Edge, MSN, Windows were named as planned surfaces).
- Perplexity merchant terms and the Amazon litigation outcome.
- AP2 adoption by PSPs; Visa and Mastercard agent token programs.
