# Commerce Feeds Audit Checklist (scored)

> Run at onboarding, quarterly, and before peak season. Score each item 0 (fail), 1 (partial), 2 (pass), or N/A. Multiply by the weight. State the data used (exports, connectors, date range) at the top of the audit output. Knowledge as of 2026-10.

Severity weights: Critical = 5, High = 3, Medium = 2, Low = 1.

## A. Account health and policy (Merchant Center and peers)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | No account-level suspension or open warning | Suspension stops all Shopping and free listings | Merchant Center account issues; Merchant API account issues | Critical | Diagnostics runbook |
| A2 | Website verified and claimed; all `link` domains match | Required for listings | Business info, website | Critical | Re-verify and claim |
| A3 | Business identity complete and consistent (name, address, phone, email) across site and Merchant Center | Top misrepresentation trigger | Compare site footer, contact page, business info | High | Align everywhere |
| A4 | Shipping and returns configured for every target country | Required; annotations; AI answers quote them | Shipping and returns settings | High | Configure account level |
| A5 | Policy pages (shipping, returns, privacy, terms, contact) linked in footer | Misrepresentation, AI agent trust, OpenAI checkout prerequisites | Crawl footer | High | Publish and link |
| A6 | No restricted products live without the right certification or exclusion | Policy strikes | Policy issues in item list | High | Exclude or certify |
| A7 | Google Ads linked; Microsoft Ads linked to Microsoft Merchant Center | Ads cannot serve otherwise | Linked accounts | Critical (if ads planned) | Link |

## B. Data sources and pipeline

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Exactly one primary source per product set; no duplicate primaries | Duplicates and overwrites | Data sources list; duplicate IDs | High | Consolidate |
| B2 | Last successful update under 24 hours (under 1 hour for price and stock on fast movers) | Mismatches, stale prices | Data source history, feed timestamps | High | Increase frequency or API updates |
| B3 | No Content API integrations left (shut down 2026-08-18) | Broken sync | Ask vendor or developer; check API logs | Critical | Migrate to Merchant API |
| B4 | API-inserted items refreshed within 30 days | Expiry | Product last update dates | High | Scheduled refresh |
| B5 | Supplemental sources used for overrides; rules documented and exported | Maintainability, rollback | Data sources and attribute rules | Medium | Document and export monthly |
| B6 | Item count per channel within 2 percent of master | Silent revenue loss | Compare counts | High | Fix sync filters |
| B7 | Monitoring and alerts exist (disapprovals, counts, fetch failures) | Time to detect | Ask; check tooling | Medium | Implement section 3 of feed tools |

## C. Data accuracy

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Disapproved items under 2 percent and zero top 50 revenue SKUs disapproved | Lost revenue | Product status by revenue | Critical | Fix by revenue order |
| C2 | Price parity mismatch under 1 percent on a 100+ SKU sample | Warnings, suspensions | `pdp_parity.py` | Critical | Fix source and cadence |
| C3 | Availability parity mismatch under 1 percent | Same | `pdp_parity.py` | High | Same |
| C4 | Sale prices scheduled with matching effective dates | Mismatch during sales | Compare to site promotions calendar | Medium | Use `sale_price_effective_date` |
| C5 | Currency and tax treatment correct per country | Mismatch, policy | Feed versus page in target country | High | Country feeds |
| C6 | Automatic item updates on, and rarely triggered | Safety net; frequent triggers mean stale feed | Settings; issue history | Medium | Fix pipeline |

## D. Identifiers and categorization

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | GTIN coverage on branded products at least 95 percent | Matching, eligibility | `feed_qa.py` coverage by brand | High | Source from suppliers, GS1 |
| D2 | Zero invalid GTINs (check digit, restricted prefix) | Disapprovals | `feed_qa.py` | High | Correct or remove |
| D3 | `identifier_exists=no` only for custom, handmade, vintage, unbranded | Misuse hides problems | Filter feed | Medium | Correct |
| D4 | `brand` present and correct (not the store name for third-party goods) | Matching, policy | Feed | High | Fix |
| D5 | `product_type` taxonomy present, 3 or more levels, stable | Listing groups, reporting | Feed | Medium | Build taxonomy |
| D6 | Variants share `item_group_id` and carry distinguishing attributes | Variant policy and display | `feed_qa.py` | High | Fix |
| D7 | IDs identical across Google, Meta, TikTok, Pinterest, OpenAI and pixels | Retargeting and matching | Compare samples; pixel event payloads | High | Align, hand off to measurement |

## E. Content quality

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Titles follow a vertical template with product type and key attributes in first 70 chars | Query matching | Sample 50 top SKUs | High | Title program |
| E2 | No promo text, all caps or keyword stuffing in titles | Policy, quality | `feed_qa.py` | Medium | Rules |
| E3 | Descriptions 500+ chars of plain facts on top SKUs | AI answers, relevance | Feed | Medium | Enrich |
| E4 | Main images clean, at least 1,200 px, correct variant | CTR, policy, 500 x 500 floor from 2027-01-31 | Image audit | High | Replace |
| E5 | Additional and lifestyle images on top SKUs | CTR, Demand Gen, Meta | Feed | Low | Add |
| E6 | AI-generated images and text disclosed per platform rules (IPTC metadata, `structured_title`, Pinterest `ai_disclosures`) | Policy | Check metadata and fields | Medium | Fix |
| E7 | Apparel attributes complete where required (color, size, gender, age group) | Required in US, UK, DE, FR, JP, BR | Feed | High | Add |
| E8 | Product highlights and details on top SKUs | Free listings, AI surfaces | Feed | Low | Add |
| E9 | Conversational attributes adopted where supported (Q&A, related products, variant options, documents) | AI Mode and Gemini readiness | Feed | Low | Roadmap |

## F. Segmentation and performance

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Custom labels carry margin and performance data, refreshed automatically | Budget by profit | Feed labels; pipeline | High | Label builder |
| F2 | Each label under 1,000 unique values (practically under 50) | Platform limit, usability | `feed_qa.py` cardinality | Medium | Simplify |
| F3 | Zombie rate (eligible SKUs with zero impressions in 30 days) under 30 percent | Wasted catalog | Product performance | Medium | Data fixes, zombie test |
| F4 | Price competitiveness reviewed monthly for top SKUs | Price drives clicks | Price competitiveness report | Medium | Hand off pricing decisions |
| F5 | `cost_of_goods_sold` or margin labels available for profit bidding | POAS | Feed | Medium | Add |
| F6 | Meta product sets defined from labels and in stock filters | Catalog ads efficiency | Commerce Manager sets | Medium | Build sets |

## G. Programs and free surfaces

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Free listings enabled and tracked | Free traffic, AI surfaces | Programs; conversion settings | High | Enable |
| G2 | Product reviews flowing (feed or aggregator) | Stars, AI ranking | Reviews program | Medium | Set up |
| G3 | Promotions used for real offers, approved before events | CTR | Promotions list | Low | Plan calendar |
| G4 | Loyalty program and member pricing configured if the business has one | Annotations, AI answers | Programs; feed | Low | Configure |
| G5 | Local inventory and free local listings live if stores exist | Store traffic | Local programs | Medium | Set up |

## H. Structured data and site

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | Product JSON-LD server-rendered with price, currency, availability, GTIN, brand | Crawl checks, AI agents | View source, parity script | High | Template fix |
| H2 | One Product or ProductGroup block per PDP (no conflicting duplicates) | Mismatch | View source | Medium | Remove duplicates |
| H3 | Variant URLs preselect the variant server side | Mismatch | Fetch variant URLs | High | Fix |
| H4 | Return policy and shipping in markup (offer or organization level) | Annotations | Rich Results Test | Low | Add |
| H5 | Crawlers allowed (Googlebot, Storebot-Google, Bingbot, OAI-SearchBot, PerplexityBot, Meta) per documented policy | Visibility | robots.txt, CDN logs | High | Agent access policy |

## I. Other channels and AI commerce

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Microsoft Merchant Center feed live and approved (if ecommerce in Microsoft markets) | Cheap reach, Copilot | MMC | Medium | Set up |
| I2 | Meta catalog healthy, pixel match at least 90 percent | Retargeting | Diagnostics | High | Fix IDs |
| I3 | TikTok catalog or Shop listings healthy (if active) | Video commerce | Catalog Manager, Seller Center | Medium | Fix |
| I4 | ChatGPT presence path chosen (Shopify or Etsy, application, or not now) and documented | AI discovery | Journal decision | Medium | Decide |
| I5 | Copilot Checkout, Perplexity, UCP early access decisions documented | Agentic commerce readiness | Journal decision | Low | Decide |
| I6 | AI referral traffic tracked as its own channel | Measurement | Analytics | Medium | Hand off to measurement |

## Scoring rubric

```
Item score = (0, 1 or 2) x weight     (N/A items excluded)
Section score % = sum(item scores) / sum(2 x weight for scored items) x 100
Overall score % = sum(all item scores) / sum(2 x weight for all scored items) x 100
```

| Overall | Grade | Meaning | Next step |
|---------|-------|---------|-----------|
| 90 to 100 | A | Top tier feed operation | Optimize: experiments, AI surfaces, new channels |
| 75 to 89 | B | Solid, some leaks | Fix High items within 30 days |
| 60 to 74 | C | Material revenue at risk | 30-day remediation plan, weekly check-ins |
| under 60 | D | Broken foundation | Stop new channel work; fix Critical and High first |

Override rule: any Critical item scored 0 caps the grade at C, regardless of the total.

## Output format
Save as `ads-master/outputs/commerce-feeds/YYYY-MM-DD_commerce-feeds_audit.md` with:
1. Data used and date range.
2. Score table by section and overall grade.
3. Top 10 issues ranked by revenue at risk (SKU counts, revenue share).
4. Change list for approval (what, where, who, rollback).
5. Experiments proposed.
6. Handoffs requested.
