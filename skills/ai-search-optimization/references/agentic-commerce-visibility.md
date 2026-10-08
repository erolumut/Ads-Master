# Agentic Commerce Visibility

> Knowledge as of 2026-10. Scope split: `commerce-feeds` owns product feeds, Merchant Center, catalogs and commerce protocols (ACP, UCP) including their technical integration. This agent owns visibility: whether products are recommended in AI shopping answers, why or why not, the content and reputation signals around them, and prompt tracking for shopping. Coordinate through the journal.

## 1. Landscape (dated)

| Date | Event | Evidence |
|------|-------|----------|
| 2025-04 | ChatGPT search adds improved shopping results (product cards with prices, reviews, buy links); results are not ads | [Official, 2025-04] |
| 2025-05 | Google I/O: AI Mode shopping with agentic checkout announced | [Official, 2025-05] |
| 2025-09-29 | OpenAI launches Instant Checkout in ChatGPT with Etsy, built on the Agentic Commerce Protocol (ACP) with Stripe | [Official, 2025-09] |
| 2025-11 | ChatGPT shopping research experience; Perplexity shopping with PayPal in the US | [Official, 2025-11; Perplexity date Unverified] |
| 2026-01-11 | Google announces the Universal Commerce Protocol (UCP) at NRF with partners including Shopify, Etsy, Wayfair, Target, Walmart | [Official, 2026-01] |
| 2026-02 | Forrester tally: about 30 Shopify merchants live on Instant Checkout | [Study, 2026-02, via secondary] |
| 2026-03 | OpenAI says Instant Checkout did not offer the flexibility it wanted and moves to merchant-handled checkout; ACP expanded to product discovery. One source dates removal to 2026-03-04 | [Contested] |
| 2026-03-24 | Revamped ChatGPT shopping focused on discovery; Shopify Agentic Storefronts on by default for eligible merchants | [Secondary, verify] |
| 2026-03 | UCP adds multi-item carts, real-time catalog access and identity linking for loyalty | [Secondary, verify] |
| 2026-05 | UCP checkout reported live on YouTube Shopping for eligible retailers | [Secondary, verify] |
| 2026-10-06 | Merchant Center integration hub for UCP begins gradual US rollout (cart transfer to merchant site, native Google checkout, or merchant account sign-in) | [Unverified, single source] |
| By end of 2026 | UCP planned for Canada, Australia and the UK | [Secondary, verify] |

## 2. How AI shopping answers choose products (best current understanding)

| Input | Engines | Evidence |
|-------|---------|----------|
| Structured product data (title, attributes, GTIN, price, availability, shipping, returns) from merchant feeds and third-party providers | ChatGPT, Google AI Mode, Gemini, Perplexity, Copilot | [Official for feeds; weighting Unverified] |
| Reviews and ratings (merchant and product) | All | [Official that reviews are shown; weighting Unverified] |
| Editorial reviews and "best X" articles | All | [Practitioner consensus] |
| Reddit, YouTube reviews and forums | AI Mode, AIO, Perplexity | [Study for citation mix] |
| Price competitiveness and availability | All shopping surfaces | [Practitioner consensus] |
| Merchant trust signals (policies, returns, shipping speed) | Google (Merchant Center), ChatGPT (feed policy URLs) | [Official for policy fields] |
| User context (budget, size, location, preferences, memory) | All | [Official for memory features; effect Unverified] |

OpenAI has stated that shopping results in ChatGPT are not ads and are selected independently [Official, 2025-04]. Paid placement in ChatGPT is a separate ads product (owned by `chatgpt-ads`).

## 3. Visibility audit for ecommerce

1. Build a shopping prompt set: 30 to 150 prompts by category, need, budget, attributes and use case ("trail running shoes for wide feet under $120", "best espresso machine for a small kitchen").
2. Run across ChatGPT (search and shopping modes), Google AI Mode, Gemini, Perplexity and Copilot; 3 to 5 runs each, fixed geo.
3. Record: products shown, merchant shown, price shown, rating shown, reasons given, cited sources, whether our product or store appears.
4. For each prompt where competitors appear and we do not, diagnose:

| Check | How | Owner |
|-------|-----|-------|
| Is the product in the engine's product data at all? | Search the exact product in the engine; check Merchant Center status; check ACP feed status | `commerce-feeds` |
| Are attributes complete for the prompt's constraints (size, material, use, compatibility)? | Compare feed attributes to prompt constraints | `commerce-feeds` |
| Price and availability competitive and accurate? | Compare shown price to site | `commerce-feeds` |
| Review count and rating vs shown competitors | Product page and platforms | This agent with human |
| Third-party reviews and lists include the product? | Source map of cited domains | This agent |
| Product page states key facts in HTML text? | Rendering test | This agent with `seo` |

5. Output a gap list split by owner and a handoff to `commerce-feeds` for feed fixes.

## 4. Product page content standard (for AI shopping and AI Mode)

| Element | Rule |
|---------|------|
| Title | Brand, product type, key attribute, model or variant |
| First paragraph | Who it is for and the top 3 facts (for example "for wide feet, 8 mm drop, 280 g") |
| Specs table | HTML table with units; matches feed attributes exactly |
| Use cases | Short sections answering "is it good for X?" sub-queries |
| Comparisons | "How it compares to <sibling or competitor>" with honest table |
| Sizing and compatibility | Explicit guidance; AI answers often fail on fit and compatibility |
| Reviews | Rendered in HTML with count and average; review snippets that mention use cases |
| Policies | Shipping, returns, warranty in text and linked |
| Schema | Product with offers, brand, gtin, aggregateRating when visible and compliant |
| Freshness | Price and stock in HTML match the feed |

## 5. Reviews strategy for AI shopping

1. Collect reviews from all customers (no gating), with prompts that ask about use case, fit and comparisons. Use-case language in reviews matches prompt constraints [Practitioner consensus].
2. Syndicate reviews where legitimate (Google product ratings programs, retailer networks) through `commerce-feeds`.
3. Answer common questions on product Q&A sections.
4. Never buy, fabricate or incentivize positive-only reviews (FTC rule effective 2024-10) [Official, 2024].

## 6. Agent readiness (agents that buy)

Agent browsers and protocol-based agents increasingly complete purchases. Visibility is wasted if the agent cannot finish the task.

| Check | Why |
|-------|-----|
| Bot management does not block verified agents (Web Bot Auth signed requests) | Blocks lose real customers using agents [Practitioner consensus] |
| Checkout works without hover-only menus, custom widgets that lack labels, or CAPTCHAs on every step | Agents operate via the DOM and accessibility tree |
| Prices, shipping and taxes visible before the final step | Agents compare totals |
| Guest checkout available | Agents struggle with account creation |
| Order status pages and emails are clear | Agent follow-ups ("where is my order") rely on them; ACP requires order webhooks [Secondary, verify] |
| Protocol support (ACP for ChatGPT, UCP for Google) | Owned by `commerce-feeds`; this agent reports which surfaces show checkout options |

## 7. Measurement for commerce visibility

| Metric | Source |
|--------|--------|
| Product mention rate on shopping prompts by engine | Prompt tracking |
| Share of products shown (our products / all products shown) | Prompt tracking |
| Price accuracy rate (shown price equals current price) | Prompt tracking vs feed |
| AI channel sessions to product and collection pages, add-to-cart rate, revenue | GA4 AI channel |
| Merchant Center performance for AI Mode surfaces where reported | Merchant Center (owned by `commerce-feeds`) |
| Protocol orders (ACP, UCP) | Commerce platform and `commerce-feeds` reports |

## 8. Business model notes

| Model | Focus |
|-------|-------|
| DTC brand with own store | Feed completeness, product page facts, reviews, creator and editorial reviews, Shopify Agentic Storefronts status |
| Multi-brand retailer | Category guides and comparisons that answer constraint-heavy prompts; price competitiveness; store policies |
| Marketplace sellers (Amazon, Etsy, Walmart) | Listing content and reviews on the marketplace; engines often show marketplace listings |
| High-consideration products (furniture, electronics) | Comparisons, specs, expert reviews, YouTube reviews |
| Regulated products (supplements, alcohol, firearms, pharmacy) | Engine policies may exclude categories; check before investing [Unverified per engine] |

## 9. Handoff template to commerce-feeds

```
# Journal: YYYY-MM-DD_HHMM_ai-search-optimization_feed-gaps.md
Date | Agent: ai-search-optimization | Tags: request
## What happened
Shopping prompt audit (<n> prompts, engines, dates) found <x> prompts where competitors appear and our products do not.
## Data (with source)
Tracking export file; list of products, missing attributes, price mismatches.
## Action items
commerce-feeds: verify ACP and Merchant Center status for SKUs <list>; add attributes <list>; fix price mismatch on <list>.
## Related files
ads-master/outputs/ai-search-optimization/<audit file>
```
