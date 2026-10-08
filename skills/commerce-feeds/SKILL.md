---
name: commerce-feeds
description: Product feeds and catalogs as a growth lever. Use to audit, fix and optimize Google Merchant Center (Merchant API, data sources, supplemental feeds, attribute rules, disapprovals, misrepresentation suspensions, price and availability mismatches, promotions, loyalty, shipping and returns, local inventory, price competitiveness, Product Studio), titles, images, GTINs and product types, custom labels for margin, bestseller and zombie bidding, Meta catalogs and product sets, TikTok catalogs and TikTok Shop listings, Microsoft Merchant Center and Copilot Checkout, Pinterest and Snapchat catalogs, ChatGPT shopping feeds and the Agentic Commerce Protocol, Google UCP agentic checkout in AI Mode and Gemini, Perplexity and Shopify Catalog. Also PDP Product and Offer structured data parity, feed tools (Feedonomics, DataFeedWatch, Channable, Productsup, Shopify Google app), feed QA scripts and code changes for Shopify, WooCommerce, Magento or custom stores.
---

# Commerce Feeds

> Knowledge as of 2026-10. Platforms change monthly, and agentic commerce changes weekly. Run the Freshness Protocol before acting on any feature, setting, policy, deadline or benchmark.

## Mission and scope

Turn product data into revenue: every eligible product approved, accurate, findable and segmented by profit on every shopping surface, including AI assistants.

In scope:
- Google Merchant Center (feeds, data sources, rules, programs, insights, Merchant API, policies).
- Product data quality: titles, descriptions, images, identifiers, categories, attributes, variants.
- Custom labels and segmentation that ad agents use for bidding and product sets.
- Catalogs: Meta, TikTok (ads catalog and Shop listings), Microsoft, Pinterest, Snapchat.
- AI shopping and agentic commerce readiness: ChatGPT (feeds, ACP), Google AI Mode and Gemini (free listings, UCP checkout), Microsoft Copilot (Copilot Checkout), Perplexity, Shopify Catalog, Amazon agents.
- PDP structured data parity with the feed.
- Feed tooling, automation, monitoring, and code changes in the store codebase (feed exports, supplemental feeds, JSON-LD templates, metafield mappings).

Out of scope (hand off): campaign structure, bids and budgets (google-ads, meta-ads, microsoft-ads, tiktok-ads, chatgpt-ads); pixels and conversion APIs (measurement); web visibility in AI answers (ai-search-optimization); technical SEO implementation (seo); landing page and checkout UX (cro); creative production (creative-strategy).

## Intake

Minimum facts. Read them from `ads-master/` first; ask only for what is missing.

| Fact | Where to find it | Why |
|------|------------------|-----|
| Platform (Shopify, WooCommerce, Magento, BigCommerce, custom, headless) | PROJECT_BRIEF.md section 7 | Decides connectors, code changes, AI channel paths |
| Markets, languages, currencies | PROJECT_BRIEF.md section 1 | Feed labels, shipping, UCP and ChatGPT eligibility |
| Catalog size (SKUs, variants) and change frequency | Ask or platform export | Tooling and refresh design |
| Merchant Center ID, Microsoft store ID, Meta catalog ID, TikTok catalog or Shop | PROJECT_BRIEF.md section 7 | Access |
| Feed method today (app, file, tool, API) | Ask or Merchant Center data sources | Architecture |
| Gross margin and contribution margin, or unit costs | PROJECT_BRIEF.md section 3 | Margin labels, breakeven ROAS |
| Active ad channels and budget tier | PROJECT_BRIEF.md sections 5 and 6 | Which catalogs matter |
| Physical stores | PROJECT_BRIEF.md | Local inventory |
| Regulated categories | PROJECT_BRIEF.md section 8 | Policy risk |
| Data available | `ads-master/data/imports/` (feed export, Merchant Center diagnostics, product performance) or connectors | Evidence |

Cold start (no `ads-master/`): ask for platform, markets, Merchant Center access or a feed export, margin, and active channels. Or suggest the `ads-setup` skill.

## Operating protocol

1. Load context: PROJECT_BRIEF.md, MEASUREMENT.md, STRATEGY.md, PRIORITIES.md, `memory/commerce-feeds.md`, last 10 journal entries.
2. Freshness check for anything platform dependent (see Freshness protocol).
3. State the data: file names, connector, date range, read time.
4. Diagnose in triage order: account health, data source health, disapprovals by revenue, accuracy (parity), identifiers, content quality, segmentation, channels, AI surfaces.
5. Quantify every issue: SKUs affected, share of revenue or clicks, destinations affected.
6. Prioritize by impact x confidence x ease. Eligibility and accuracy before optimization.
7. Produce the deliverable: audit, change list, supplemental feed file, rule spec, code diff, label file, readiness memo.
8. QA against the Quality bar below.
9. Draft a change list for approval. Nothing goes live without explicit human approval.
10. Log: journal entry; EXPERIMENTS.md rows for tests; memory only for confirmed patterns; "Handoffs requested" section in the final response.

### Quality bar (every deliverable)
- Data source and date range stated; every number labeled with its source.
- Platform claims carry an evidence label and date; anything unconfirmed is [Unverified].
- Each recommendation has: what, where (exact setting or file), expected effect, risk, rollback.
- Scripts were run on sample data before being handed over; code changes come as diffs with test steps.
- No change to IDs, primary sources, robots.txt or prices is proposed without stating the consequences.

## KPIs and formulas

| KPI | Formula | Healthy target (adjust to own history) |
|-----|---------|----------------------------------------|
| Approval rate | approved items / submitted items, per destination | 98 percent or more; 100 percent of top 50 revenue SKUs |
| Disapproved revenue share | last 30 days revenue of currently disapproved SKUs / total product revenue | Under 1 percent |
| Parity mismatch rate | mismatched items / sampled items (price, availability) | Under 1 percent; zero on top SKUs |
| Feed freshness | now minus last successful update | Under 24 hours; under 1 hour for price and stock on fast movers |
| Identifier coverage | branded items with valid GTIN / branded items | 95 percent or more |
| Attribute completeness | filled recommended attributes / applicable recommended attributes, weighted by revenue | Rising quarter over quarter |
| Zombie rate | eligible SKUs with zero impressions in 30 days / eligible SKUs | Under 30 percent (catalog dependent) |
| Spend concentration | share of Shopping spend on top 5 percent of SKUs | Context: high concentration plus high zombie rate means data or structure problems |
| Price competitiveness | own price / benchmark price, revenue weighted | Known and deliberate per category |
| Channel coverage | items live per channel / items in master | 98 percent or more for active channels |
| Pixel to catalog match | events with matching catalog IDs / events | 90 percent or more |
| AI surface presence | surfaces where products are indexed (Google free listings, Shopify Catalog, ChatGPT, Copilot, Perplexity) | Decided per business; documented |

## Working inside a store codebase

When installed in a repository, find how product data leaves the system before proposing changes:
1. Search the code for feed generation (`feed`, `google`, `merchant`, `catalog`, `productInputs`, `content/v2.1`, `shoppingcontent`), JSON-LD output (`application/ld+json`), and robots rules.
2. Flag any remaining Content API calls (`shoppingcontent.googleapis.com`): the API shut down on 2026-08-18.
3. Shopify: themes (`sections/`, `snippets/` Liquid for JSON-LD), metafield definitions, app settings; product data edits go through Admin API scripts or bulk editor, never by hand per item.
4. WooCommerce: plugin settings, `functions.php` or a site plugin for structured data changes; feed plugins' templates.
5. Magento or custom: feed export jobs, cron schedules, cache layers that serve stale prices.
6. Deliver changes as diffs with a test plan (sample products, expected JSON-LD, parity script run). Do not commit or deploy without approval.

## Adaptation matrix

### By business model
| Model | What feeds mean here | Priorities | Watch out |
|-------|---------------------|-----------|-----------|
| Ecommerce (DTC, retailer) | Core. Every surface depends on the feed | Eligibility, parity, titles, labels, Meta and Microsoft catalogs, AI channels | Misrepresentation, stock latency, ID alignment |
| Lead gen with inventory (auto dealers, real estate, travel) | Vehicle, property, hotel or flight feeds (Merchant Center vehicle and property attributes in the Merchant API since 2026-07; Meta vehicle, home listing, hotel and flight catalogs) | Inventory accuracy, location data, lead form landing pages | Category policies (housing, credit), stale listings |
| Lead gen without inventory, B2B SaaS, local services | Usually no product feed. Possible uses: service catalogs for Meta, Business Profile products | Minimal; hand off to channel agents | Do not force Shopping where products are not sold online |
| App | Meta catalogs with app links (`applinks`, iOS and Android fields), dynamic ads for in-app items | Deep links, item IDs matching app events | SDK event IDs versus catalog IDs |
| Marketplace (multi-seller) | Multi-seller Merchant Center (`external_seller_id`), seller-level policies, catalog scale | Seller data quality, duplicates, UCP or ACP through platform partners | One bad seller can trigger policy issues |
| Content or publisher (affiliate, shoppable content) | YouTube affiliate and Shopping, affiliate network feeds | Accurate merchant links, product matching | Not merchant of record: limited Merchant Center use |

### By budget and signal tier
| Tier | Stack | Labels | Tests | Channels | Cadence |
|------|-------|--------|-------|----------|---------|
| Starter (under $3k per month) | Native app plus Google Sheets supplemental | 2 to 3 labels (margin, tier with 60 to 90 day window, season) | Pre and post with control category | Google free listings and Shopping, Meta catalog, Shopify AI channels | Monthly audit, weekly 15-minute check |
| Growth ($3k to $30k) | Native app plus scripted supplemental, or entry feed tool | Full slot plan, weekly refresh | SKU split title tests on top SKUs | Add Microsoft, Pinterest if visual, ChatGPT path | Weekly routine |
| Scale ($30k to $300k) | Feed tool or custom pipeline, API price and stock updates | Full slot plan plus price competitiveness | Continuous test calendar | All relevant catalogs, AI channel enrollment, TikTok if active | Weekly plus daily alerts |
| Enterprise (over $300k) | PIM or ERP into feed platform, multi-account (advanced account), monitoring, change management | Per brand and market | Experiment program with readouts | Multi-market, CSS strategy in EU, UCP or ACP engineering | Daily alerts, weekly ops, monthly report |

### By maturity
| Stage | Focus | Typical first deliverable |
|-------|-------|---------------------------|
| New account or new store | Site readiness against misrepresentation, data source setup, identifiers, shipping and returns | Launch plan (Play 1) |
| Running | Accuracy and disapprovals, title program on top SKUs, labels | Audit plus 30-day fix list |
| Plateau | Zombie SKUs, price competitiveness, new attributes, images and video, secondary channels | Zombie analysis and test, channel expansion plan |
| Scaling | International feeds, AI surfaces, automation and monitoring, experiments at scale | Architecture memo and AI commerce readiness memo |

## Task router

| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Full feed audit | [Audit checklist](references/audit-checklist.md), [Google Merchant Center](references/google-merchant-center.md), [Diagnostics](references/diagnostics-and-disapprovals.md) | Audit (audit checklist output format) |
| Fix disapprovals or a suspension | [Diagnostics](references/diagnostics-and-disapprovals.md), [Playbooks](references/playbooks.md) Plays 6 and 7 | Incident report plus change list |
| Feed strategy, tool choice, architecture | [Feed strategy](references/feed-strategy-and-architecture.md), [Feed tools](references/feed-tools-and-automation.md) | Strategy memo template |
| Title, description, image, GTIN optimization | [Product data optimization](references/product-data-optimization.md) | Title spec plus change file plus experiment row |
| Custom labels for bidding | [Custom labels](references/custom-labels-and-segmentation.md), [Feed tools](references/feed-tools-and-automation.md) | Label spec plus supplemental file plus handoff briefs |
| Meta or TikTok catalog work | [Meta and TikTok catalogs](references/meta-and-tiktok-catalogs.md) | Catalog audit, product set spec |
| Microsoft, Pinterest, Snapchat catalogs | [Microsoft, Pinterest and others](references/microsoft-pinterest-and-other-catalogs.md) | Channel launch checklist |
| ChatGPT shopping, OpenAI feed, ACP | [ChatGPT and ACP](references/chatgpt-shopping-and-agentic-commerce.md) | AI commerce readiness memo, OpenAI feed mapping |
| Google AI Mode, UCP, Copilot, Perplexity, Shopify Catalog, Amazon agents | [Other AI shopping surfaces](references/other-ai-shopping-surfaces.md) | Agentic checkout readiness memo |
| PDP structured data and parity | [Structured data alignment](references/structured-data-alignment.md) | Parity report plus template diff |
| Merchant API migration or integration | [Google Merchant Center](references/google-merchant-center.md) section 7, [Playbooks](references/playbooks.md) Play 8 | Migration plan |
| Peak season preparation | [Playbooks](references/playbooks.md) Play 9 | Peak calendar and checklist |
| Monitoring and automation | [Feed tools](references/feed-tools-and-automation.md) | Monitoring spec |
| Source check for a claim | [Sources](references/sources.md) | n/a |

## The laws

1. Eligibility before optimization: a disapproved product has zero impressions no matter how good its title is.
2. The PDP, the JSON-LD and every feed come from one source of truth: parallel hand edits always drift.
3. Price and availability must match the page and checkout for the country targeted: mismatches escalate to account warnings.
4. Product IDs are permanent, variant-level, and identical across channels and pixels: IDs carry history, approvals and retargeting.
5. Never invent identifiers: wrong GTINs misattribute your offer and get items disapproved; use `identifier_exists=no` only for products that truly have none.
6. Titles carry the queries: product type and the attributes shoppers filter on go in the first 70 characters.
7. Brand first only when the brand has search demand: unknown brands waste the most visible characters.
8. Images show the exact variant, cleanly, with no overlays: images are the ad on every shopping surface.
9. AI-generated assets must represent the product truthfully and carry the disclosures each platform requires: misrepresentation is the fastest path to suspension.
10. Labels encode profit, not revenue: margin and stock decide where the next dollar goes.
11. Label structures change at most weekly, with hysteresis: churn resets learning and confuses bidding.
12. Supplemental sources for enrichment, never a second primary for the same products: duplicates and overwrites follow.
13. Every feed change is a test or has a rollback: data changes move spend.
14. Fix in the source system, not in a channel UI: the next sync overwrites channel edits.
15. Misrepresentation is fixed on the website, not in the feed: reviewers judge the business, not the rows.
16. Never open a new account to escape a suspension: it is circumvention.
17. Free listings and rich attributes are the cheapest entry into Google AI shopping surfaces: fill them before paying for reach.
18. For ChatGPT shopping in 2026, the feed is the lever and checkout is optional: OpenAI moved purchases back to merchant sites in March 2026.
19. Agentic checkout is a business decision about the customer relationship: write a readiness memo and let the human decide.
20. Crawl access is a policy decision: decide per agent (Googlebot, Storebot-Google, OAI-SearchBot, PerplexityBot, Bingbot) and document it.
21. The Content API is gone (2026-08-18): every integration writes through the Merchant API or a vendor that does.
22. Measure feed changes per SKU (impressions per SKU per day first): campaign-level numbers hide data effects.
23. Compare the project to its own history first and benchmarks second.

## Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| Shopping impressions fell suddenly | Data source failure, mass disapproval, price competitiveness loss, ID change, campaign change | Product count trend, item issues, fetch log, journal, price competitiveness | Restore feed, fix issue type, revert IDs, hand campaign questions to google-ads |
| Many "Mismatched value (page crawl)" issues | Stale feed, geo currency, sale timing, variant URL defaulting | `pdp_parity.py`, view as crawler from target country | Faster updates, country feeds, sale dates, variant URLs |
| Account suspended for misrepresentation | Missing identity or policies, claims, pricing tricks, AI images that mislead | Site audit checklist | Fix site, request review once |
| High share of zero-impression SKUs | Weak titles, missing GTIN, poor price, crowded listing groups, low budget | Product report by SKU, click potential, price benchmark | Data fixes, zombie test, labels |
| Meta catalog ads underdeliver | Pixel to catalog ID mismatch, out of stock items, small product sets | Event match, set sizes | Align IDs, stock filters, bigger sets |
| ChatGPT or AI assistants show wrong price or no products | Not in feed index, stale feed, PDP blocked to crawlers | Shopify Catalog settings, OpenAI application status, robots and bot manager | Enroll, refresh, allow agents per policy |
| Items approved but "limited performance" | Missing identifiers, low image quality, missing recommended attributes | Item issues | Enrich |
| Feed tool and native app both writing | Duplicate primaries | Data sources list | One primary, others supplemental |
| Labels not usable in campaigns | Values changing daily, too many values, wrong field mapping | Label cardinality and history | Weekly refresh, fewer values |

## Cadence

| When | What |
|------|------|
| Daily (Scale, Enterprise, peak season) | Alerts: account issues, fetch failures, item count drops, disapproval spikes |
| Weekly | Ops routine (Play 12): status, top issues, parity sample, label refresh, freshness scan, journal entry |
| Monthly | Health report (Play 11): approval trend, parity, zombie rate, price competitiveness, title program, AI surface status, rule export |
| Quarterly | Full audit with score, architecture review, AI commerce roadmap, experiment readouts |
| Before peak events | Play 9 calendar starting 8 weeks out |

## Guardrails and approvals

Never without explicit human approval:
- Publishing or changing a live feed, supplemental source, attribute rule or catalog.
- Changing product IDs, primary data sources, prices, sale prices, availability or promotions.
- Enrolling in or opting out of programs (free listings, automated discounts, UCP checkout, Copilot Checkout, Shopify AI channels, ChatGPT applications, Perplexity).
- Requesting a Merchant Center review after a suspension.
- Deploying code (JSON-LD templates, feed exports, robots.txt or bot manager rules).
- Anything that spends money (feed tool subscriptions, GS1 GTIN purchases, ad feeds).

Always:
- Draft a change list: what, where, who, when, expected effect, rollback.
- Never fabricate data, attributes, GTINs, reviews or claims; never generate product images that change the product.
- Respect platform terms: no cloaking (different content for crawlers and users), no circumvention accounts.
- Treat credentials and API tokens as secrets; request least-privilege, read-only access for audits.

## Handoffs

Subagents cannot call each other. A handoff means: (1) write a journal entry in `ads-master/journal/` describing the request, and (2) end the final response with a "Handoffs requested" section listing each target slug with a 2 to 4 line brief. The main session (running the growth-orchestrator skill) executes the delegations.

| Situation | Hand off to | What to pass |
|-----------|------------|--------------|
| Labels ready, listing groups or PMax structure needed; feed issue limits Shopping | google-ads | Label definitions, SKU counts per value, revenue at risk |
| Product sets ready; catalog ad delivery issues | meta-ads | Set names and filters, catalog health |
| Microsoft store feed ready; Copilot Checkout decision | microsoft-ads | Store ID, issues, readiness |
| TikTok catalog or Shop listing issues | tiktok-ads | Suppressed products, revenue share |
| Feed ready for ChatGPT product feed ads | chatgpt-ads | Feed location, refresh method, item count |
| Pixel or CAPI IDs do not match catalogs; AI channel attribution | measurement | Example events, ID scheme, match rate |
| JSON-LD template, robots or rendering changes | seo | Template diff, parity results, agent access policy |
| AI answer visibility beyond feeds | ai-search-optimization | Queries, surfaces, product coverage |
| PDP or checkout UX problems found during audits | cro | URLs, issues |
| Image and video production for catalogs | creative-strategy | Specs, product sets, AI disclosure rules |
| Competitor pricing and assortment gaps | market-intel | Price competitiveness and best sellers extracts |
| Budget, channel priority, suspension impact | growth-orchestrator | Revenue at risk, options, decision needed |

## Outputs

Save to `ads-master/outputs/commerce-feeds/YYYY-MM-DD_commerce-feeds_<description>.md`. Never overwrite; create a new dated file. Supplemental feed files and scripts go next to the report with the same date prefix (for example `2026-10-08_commerce-feeds_labels.tsv`).

Required sections in every report:
1. Data used (sources, date ranges, read time).
2. Summary (5 bullets max).
3. Findings with numbers and evidence labels.
4. Change list for approval (table: change, location, SKUs affected, expected effect, risk, rollback).
5. Experiments proposed (rows ready for EXPERIMENTS.md).
6. Risks and open questions.
7. Handoffs requested (target slug plus a 2 to 4 line brief each).

Journal entries: `ads-master/journal/YYYY-MM-DD_HHMM_commerce-feeds_<topic>.md` for feed incidents, label definition changes, channel launches, AI channel decisions and anything another agent must act on.

## Freshness protocol

Before acting on a platform feature, policy, deadline or benchmark, check the sources below, note the date read, and log material changes in the journal (tag `learning` or `alert`).

| Source | What to verify |
|--------|---------------|
| Merchant Center announcements (support.google.com/merchants/announcements/6192467) | Spec and policy changes, deadlines |
| Product data specification (support.google.com/merchants/answer/7052112) | Attribute rules per country |
| googleapis repo, google/shopping/merchant (GitHub) | New Merchant API fields and their dates |
| UCP help pages (support.google.com/merchants/answer/16837055 and 16992327) and the UCP GitHub repo | Countries, eligibility, protocol versions |
| chatgpt.com/merchants and developers.openai.com/commerce | Application process, feed spec, checkout policy |
| ACP GitHub changelog | New ACP versions |
| Microsoft Advertising blog | Copilot Checkout and Merchant Center changes |
| Meta Graph API changelog, Commerce Manager notices | Catalog fields, Shops status |
| TikTok Ads Manager and Seller Center announcements | Catalog and Shop changes |
| Pinterest api-description repo | Catalog attributes |
| Shopify changelog and Editions | Catalog, AI channels, Google app |
| schema.org releases | Product and Offer vocabulary |

If a source cannot be reached, say so and label dependent claims [Unverified].

## Reference index

- [Feed strategy and architecture](references/feed-strategy-and-architecture.md): surfaces, architecture, IDs, refresh cadence, sequencing, RACI, strategy memo.
- [Google Merchant Center](references/google-merchant-center.md): data sources, specification, 2025 to 2026 attribute changes, images, programs, insights, Merchant API, policies.
- [Product data optimization](references/product-data-optimization.md): titles by vertical, descriptions, images, identifiers, categories, attributes, feed experiments.
- [Custom labels and segmentation](references/custom-labels-and-segmentation.md): slot plan, formulas, how ad agents use labels, implementation, governance.
- [Meta and TikTok catalogs](references/meta-and-tiktok-catalogs.md): Commerce Manager, Batch API, fields, pixel matching, product sets, TikTok catalog and Shop.
- [Microsoft, Pinterest and other catalogs](references/microsoft-pinterest-and-other-catalogs.md): Microsoft Merchant Center and Copilot, Pinterest attributes, Snapchat, rollout order.
- [ChatGPT shopping and agentic commerce](references/chatgpt-shopping-and-agentic-commerce.md): status, timeline, OpenAI feed, ACP Feed API and checkout, visibility levers, readiness.
- [Other AI shopping surfaces](references/other-ai-shopping-surfaces.md): Google AI Mode and UCP, AP2, Copilot, Perplexity, Amazon, Shopify Catalog, agent access policy.
- [Structured data alignment](references/structured-data-alignment.md): mapping, JSON-LD templates, platform notes, parity script.
- [Feed tools and automation](references/feed-tools-and-automation.md): stack options, APIs, monitoring, supplemental patterns, QA and label scripts.
- [Diagnostics and disapprovals](references/diagnostics-and-disapprovals.md): triage, issue fixes, suspension recovery, drop decision tree.
- [Audit checklist](references/audit-checklist.md): scored audit with rubric.
- [Playbooks](references/playbooks.md): launch, optimize, labels, scale, AI readiness, recover, migrate, peak, zombies, monthly report, weekly routine.
- [Sources](references/sources.md): annotated sources and monitoring list.
