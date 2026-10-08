# Feed Strategy and Architecture

> Product data is a growth lever because every shopping surface (ads, free listings, catalogs, AI assistants) ranks offers from the data you send. This module sets the strategy: which surfaces, which architecture, which IDs, which refresh cadence, and how to sequence the work. Knowledge as of 2026-10.

## 1. Why product data decides performance
| Lever | How data drives it |
|-------|-------------------|
| Query matching | Shopping and PMax have no keywords for products: titles, product types, descriptions and attributes decide which queries you enter |
| Click-through | Image, title, price, ratings, shipping and return annotations are the ad |
| Bidding efficiency | Labels let campaigns spend by margin, stock and performance instead of revenue alone |
| AI shopping visibility | ChatGPT, Google AI Mode, Gemini, Copilot and Perplexity retrieve and compare structured product data; feed retrieval dominated ChatGPT shopping recommendations from July 2026 in Profound's tracked data [Study, 2026-09] |
| Policy risk | One bad pipeline can suspend an account and stop all Shopping revenue |
| Retargeting | Catalog IDs must match pixel IDs or dynamic ads break |

## 2. Surface map (October 2026)

| Surface | Data source | Paid or organic | Owner agent for campaigns |
|---------|-------------|-----------------|---------------------------|
| Google Shopping ads, PMax, Demand Gen, YouTube | Merchant Center | Paid | google-ads |
| Google free listings, AI Overviews and AI Mode product results, Lens, Gemini | Merchant Center plus web | Organic | commerce-feeds (data), ai-search-optimization (web visibility) |
| Google UCP checkout (AI Mode, Gemini) | Merchant Center plus UCP integration | Organic, early access | commerce-feeds plus engineering |
| Microsoft Shopping, PMax, Copilot, Copilot Checkout | Microsoft Merchant Center; Shopify, PayPal, Stripe integrations | Paid and organic | microsoft-ads |
| Meta Advantage+ catalog ads, Shops surfaces | Meta catalog | Paid | meta-ads |
| TikTok catalog ads; TikTok Shop and GMV Max | TikTok ads catalog; Shop products | Paid | tiktok-ads |
| Pinterest shopping ads and Product Pins | Pinterest catalog | Paid and organic | growth-orchestrator decides; creative-strategy for assets |
| Snapchat dynamic product ads | Snap catalog | Paid | growth-orchestrator decides |
| ChatGPT shopping | Shopify or Etsy catalog integration, direct OpenAI feed, web | Organic | commerce-feeds (data), ai-search-optimization (web) |
| ChatGPT ads with product feeds | ChatGPT Ads Manager feeds | Paid (beta) | chatgpt-ads |
| Perplexity shopping | Merchant program, Shopify, PayPal | Organic | commerce-feeds |
| Shopify Catalog AI channels | Shopify product data | Organic | commerce-feeds |

## 3. Reference architecture

```
             +------------------------------+
             | Source of truth              |
             | Commerce platform or PIM/ERP |
             | price, stock, cost, specs    |
             +---------------+--------------+
                             |
             +---------------v--------------+
             | Master product model         |
             | one row per variant          |
             | stable ID, GTIN, attributes  |
             +---------------+--------------+
                             |
        +--------------------+---------------------+
        |                    |                     |
+-------v--------+  +--------v--------+  +---------v---------+
| Enrichment     |  | Business data   |  | QA gate           |
| titles, types, |  | labels: margin, |  | feed_qa, parity,  |
| highlights,    |  | tier, stock,    |  | policy checks     |
| Q&A, images    |  | season          |  |                   |
+-------+--------+  +--------+--------+  +---------+---------+
        +--------------------+---------------------+
                             |
               +-------------v--------------+
               | Channel transforms         |
               | Google, Microsoft, Meta,   |
               | TikTok, Pinterest, Snap,   |
               | OpenAI, ACP, UCP           |
               +-------------+--------------+
                             |
       destinations: Merchant Center (primary + supplemental), Microsoft MC,
       Meta catalog, TikTok catalog, Pinterest, Snap, OpenAI SFTP, Ads feeds
                             |
               +-------------v--------------+
               | Feedback loop              |
               | diagnostics, performance,  |
               | price competitiveness      |
               +----------------------------+
```

Design rules:
1. One master model, many channel views. Channel quirks live in transforms, never in the source data.
2. The PDP and its JSON-LD come from the same source as the feed (see [structured data alignment](structured-data-alignment.md)).
3. Business data (cost, margin, stock velocity) joins the product model so labels can be computed automatically.
4. A QA gate blocks publishing when error rates jump (for example item count drops over 5 percent or GTIN errors double).
5. The feedback loop writes back into enrichment priorities (fix what has click potential first).

## 4. ID strategy

| Rule | Why |
|------|-----|
| Variant-level IDs, stable for the life of the product | Performance history, bidding data and approvals attach to the ID |
| Same ID on every channel and in every pixel | Retargeting, catalog matching, cross-channel reporting |
| No characters `/`, `%`, `~`, spaces | API encoding problems (Merchant API requires base64url for such IDs) |
| Max 50 characters | Google limit |
| Never reuse a retired ID for a different product | Wrong history, possible policy flags |
| Keep a mapping table when replatforming | Old ID to new ID; plan a migration (playbook) |

Shopify note: the Google and YouTube app commonly uses `shopify_{country}_{productId}_{variantId}`. If other channels use the SKU, either switch them all to the app format or send pixels the SKU and accept a mapping step. Pick one and document it.

## 5. Refresh cadence

| Data | Target latency | Method |
|------|----------------|--------|
| Price, sale price | Under 1 hour (under 15 minutes in flash sales) | API updates or frequent feed fetch |
| Availability and quantity | Under 1 hour for fast movers | API or inventory feed |
| New products | Same day | Platform sync or daily full feed |
| Titles, descriptions, attributes | Daily | Full feed |
| Custom labels | Weekly (performance), daily (stock) | Supplemental source |
| API-inserted items | Re-insert at least every 30 days (expiry) | Scheduled job |

## 6. Market and language expansion
1. Shipping and returns configured for the new country first.
2. Feed label per country (or per country group), content language per language.
3. Prices in local currency as charged at checkout; do not rely on automatic currency conversion for the main market.
4. Translated titles and descriptions written for local search terms, not literal translation.
5. Local legal attributes: unit pricing, energy labels (EPREL certification), consumer notices, `pickup_cost` (UK, CH, EEA pickup).
6. Landing pages in the local language and currency without IP redirects that hide content from crawlers.
7. Repeat for Meta (country and language feeds) and Microsoft.

## 7. Sequencing the work (impact versus effort)

| Order | Workstream | Typical impact | Effort |
|-------|-----------|----------------|--------|
| 1 | Account health and disapprovals on revenue SKUs | Restores lost revenue directly | Low to medium |
| 2 | Price and availability accuracy (parity) | Prevents warnings, improves trust signals | Medium |
| 3 | Identifiers (GTIN, brand, MPN) | Better matching and eligibility | Low to medium |
| 4 | Title program on top 20 percent of revenue SKUs | More query coverage | Medium |
| 5 | Custom labels and handoff to ad agents | Better budget allocation | Medium |
| 6 | Images (main, additional, lifestyle, video) | CTR | Medium to high |
| 7 | Rich attributes, highlights, Q&A, related products | AI surface readiness, filters | Medium |
| 8 | Secondary channels (Microsoft, Pinterest, TikTok) | Incremental reach | Low to medium |
| 9 | AI commerce enrollment (ChatGPT, Copilot, Perplexity, UCP) | New discovery channels | Low (platform) to high (custom UCP or ACP) |

## 8. Ownership model (RACI)
| Task | commerce-feeds | Ad agents | seo | measurement | Human |
|------|---------------|-----------|-----|-------------|-------|
| Feed pipeline and QA | Responsible | Informed | Consulted | Informed | Accountable |
| Titles and attributes | Responsible | Consulted (query data) | Consulted | | Approves |
| Custom labels | Responsible | Consulted (campaign design) | | | Approves structural changes |
| Listing groups, product sets, bids | Consulted | Responsible | | | Approves spend |
| PDP structured data | Responsible for spec | | Responsible for implementation | | Approves deploy |
| Pixel IDs | Consulted | | | Responsible | Approves |
| AI channel enrollment | Responsible | chatgpt-ads consulted (paid) | ai-search-optimization consulted | Consulted | Accountable |

## 9. Strategy memo template
```
# Feed strategy: <brand> (<date>)
Data used: <files, connectors, date ranges>
1. Current state: channels live, item counts, approval rate, revenue share disapproved, parity rate, zombie rate.
2. Target surfaces next 2 quarters and why (business model, budget tier, audience).
3. Architecture decision: native app | feed tool | custom | hybrid. Reasons, cost, owner.
4. ID scheme and pixel alignment plan.
5. Refresh cadence targets.
6. Workstreams in order with expected impact and effort.
7. Experiments to run (EXPERIMENTS.md rows).
8. Decisions needed from the human.
9. Handoffs requested.
```
