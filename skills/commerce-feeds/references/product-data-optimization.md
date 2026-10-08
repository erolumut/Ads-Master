# Product Data Optimization: titles, descriptions, images, identifiers, categories, experiments

> The feed is the keyword list, the ad copy and the creative of every Shopping, Performance Max, catalog and AI shopping placement. Optimize it like ad copy: with query data, structure and controlled tests. Knowledge as of 2026-10.

## 1. Priority order (do these in sequence)

1. Eligibility: no disapprovals on revenue SKUs, valid identifiers, accurate price and availability. Nothing else matters until this holds.
2. Identifiers: correct GTIN, brand, MPN. They let Google, Meta, Microsoft and AI agents match your offer to the product entity (Shopping Graph, Shopify Catalog, ChatGPT product clusters).
3. Titles: query-matched words in the first 70 characters.
4. Images: correct main image, then additional and lifestyle images, then video.
5. Categorization: `product_type` taxonomy for your own segmentation, Google category only when needed.
6. Rich attributes: color, size, material, pattern, gender, age group, product highlights, product details, Q&A, related products, documents.
7. Descriptions: complete facts, use cases, compatibility, care.
8. Pricing presentation: sale price, unit price, member price, installments.

## 2. Titles

### Rules
- Max 150 characters on Google; most surfaces show 60 to 70. Put the words that decide a click first.
- Use words shoppers search, not internal names. "Merino crew neck sweater" beats "Aurora Knit 2.0".
- One product per title. No promo text ("sale", "free shipping", "best price"), no ALL CAPS, no emoji, no pipes stuffed with keywords, no competitor brands.
- Include the variant attributes that the shopper filters on (color, size, capacity, count).
- Keep titles consistent across channels unless a channel has a different limit (Meta shows less; TikTok and Pinterest truncate earlier).
- Short titles: Merchant API v1 has a `short_title` attribute (added 2026-07) for surfaces with tight space. Fill it with Brand + Product type + key attribute once your specification shows it as supported for your country [Official, 2026-07].

### Attribute order by vertical
Google's title guidance recommends front-loading brand, product type and key attributes, with patterns per vertical [Official, verify the current table in the `title` attribute article]. Working templates:

| Vertical | Template | Example |
|----------|----------|---------|
| Apparel | Brand + Gender + Product type + Key attribute (material, fit) + Color + Size | `Acme Women's Merino Crew Neck Sweater, Relaxed Fit, Navy, M` |
| Footwear | Brand + Gender + Model + Product type + Color + Size | `Acme Men's Trailrunner 3 Waterproof Hiking Shoes, Olive, US 10` |
| Consumables, beauty, grocery | Brand + Product type + Key attribute (scent, formula) + Size or Count | `Acme Vitamin C Serum 15% with Hyaluronic Acid, 30 ml` |
| Hard goods, home | Brand + Product type + Material + Dimensions or Capacity + Color | `Acme Solid Oak Dining Table, Extendable 160 to 200 cm, Natural` |
| Electronics | Brand + Product line + Model + Key spec + Product type + Color | `Acme Nova 14 Laptop, Core Ultra 7, 32 GB RAM, 1 TB SSD, Silver` |
| Parts and accessories | Brand + Part type + Compatibility + Part number | `Acme Replacement Filter for Dyson V11, Part 970013-02` |
| Books and media | Title + Format + Author or Artist + Edition | `The Midnight Garden Hardcover by J. Doe, 2nd Edition` |
| Seasonal and gifts | Occasion + Product type + Key attribute + Brand | `Christmas Advent Calendar with 24 Mini Chocolates, Acme` |
| Private label with no search demand for the brand | Product type + Key attributes + Brand at the end | `Linen Duvet Cover Set, Queen, Stone Washed, Sage, Acme Home` |

Brand first only when the brand has search demand. Check brand query volume (Google Ads search terms, Search Console, Keyword Planner). If the brand is unknown, lead with the product type.

### Query-driven title procedure
1. Collect queries: Google Ads search terms report for Shopping and PMax (search term insights), Search Console queries for product pages, site search logs, Microsoft Ads search terms, Amazon or marketplace terms if available.
2. Map queries to product types. For each product type, list the modifiers that appear in converting queries (materials, sizes, compatibility, use cases).
3. Build a template per product type with an attribute order. Fill from structured attributes, not by hand.
4. Generate titles with rules (feed tool, Merchant Center attribute rules or a script). Use an LLM only to normalize messy source data, never to invent attributes.
5. QA: length 50 to 150, no duplicates within an item group except the variant part, no banned words, attribute values present.
6. Ship to a test cohort first (see experiments below).

### LLM-assisted rewriting with guardrails
- Input: structured attributes only (brand, type, material, color, size, compatibility, count) plus the template. Output: one title.
- Forbid adding facts not present in the input. Reject outputs that contain numbers or nouns not found in the input.
- Submit AI-written text via `structured_title` with `digital_source_type` set to `trained_algorithmic_media` when using Google's API or supported feed fields [Official].
- Keep a diff file of old and new titles in `ads-master/outputs/commerce-feeds/` so you can roll back.

## 3. Descriptions
- 500 to 1,500 characters of plain text facts for most products; up to 5,000 allowed on Google.
- First 160 characters: what it is, who it is for, the main differentiator.
- Then: materials and dimensions, compatibility, what is in the box, care, certifications, warranty.
- No HTML (some channels accept it, many strip it), no shipping or promo text, no links, no comparisons to competitors.
- AI shopping surfaces quote descriptions and product highlights. Write facts an assistant can repeat: "Fits 13 and 14 inch laptops", "Dishwasher safe", "Vegan leather (polyurethane)".
- ChatGPT and ACP feeds accept plain text, HTML or markdown descriptions (ACP `Description` object has `plain`, `html`, `markdown`). Send plain text at minimum.

## 4. Product highlights, details, Q&A and relationships

| Attribute | Use | Format |
|-----------|-----|--------|
| `product_highlight` | 4 to 6 short benefit facts | Up to 150 chars each [Official] |
| `product_detail` | Technical specs grouped by section | `section_name:attribute_name:attribute_value` |
| `questions_and_answers` (2026-07) | Real customer and support questions with factual answers | Max 30 pairs, 1,000 chars each, 10,000 total [Official, 2026-07] |
| `related_products` (2026-07) | Accessories, required parts, substitutes, sets, often bought with | Relationship type + ID type (GTIN or feed ID) + ID [Official, 2026-07] |
| `variant_options` (2026-07) | Explicit variant dimensions such as Color, Memory, Length | Name and value pairs [Official, 2026-07] |
| `item_group_title` (2026-07) | The parent product name for a variant group | Text [Official, 2026-07] |
| `document_links` (2026-07) | Manuals, assembly instructions, safety sheets | PDF URLs, ASCII, RFC 3986 [Official, 2026-07] |

Source Q&A from support tickets, PDP reviews and on-site search, not from guesses. AI shopping assistants answer comparison and compatibility questions; these attributes let your data answer them instead of a third-party page.

## 5. Images

### Main image decision
| Category | Main image | Additional images |
|----------|-----------|-------------------|
| Apparel, footwear | Product on plain background or on a model with the full item visible; consistent across variants | Back, detail, on-model, lifestyle |
| Home, furniture | Plain background cutout | Room scene (lifestyle), dimensions graphic without promo text |
| Beauty, consumables | Pack shot | Texture, ingredients, before and after only where policy allows |
| Electronics | Front three-quarter view | Ports, in-use, scale |
| Bundles and multipacks | All items in the bundle, quantity visible | Each item |

Lifestyle as main image: test it, do not assume. Some categories (furniture, decor, apparel on model) can gain CTR; others lose clarity. Use a SKU split test (section 9).

### AI image production
- Product Studio, Meta AI-generated catalog backgrounds (Meta catalog field `generated_background_images`) and third-party tools can make scenes at scale.
- Rules: product pixels unchanged, color accurate, no added accessories, metadata preserved (IPTC `DigitalSourceType` = `TrainedAlgorithmicMedia` where required), human review on a sample of every batch, originals archived.
- Pinterest has an `ai_disclosures` attribute for AI content per asset URL (API v5.28) [Official, 2026].

### Image QA checklist
- Size at least 1,200 px on the long side; never below 500 x 500 after 2027-01-31 on Google.
- No text overlays, watermarks, borders, or "sale" badges.
- URL stable and cache friendly; changing the URL forces a recrawl. Use a new URL only when the image changes.
- Variant image matches the variant color.
- CDN serves to Googlebot, Meta crawlers, and other crawlers without bot challenges.

## 6. Identifiers

| Case | `gtin` | `mpn` | `brand` | `identifier_exists` |
|------|--------|-------|---------|---------------------|
| Branded product with manufacturer barcode | Required | Optional | Required | omit |
| Branded product, no GTIN assigned (some parts, custom) | omit | Required | Required | omit |
| Handmade, custom, vintage, one-off | omit | omit | Your brand or omit | `no` |
| Private label you manufacture | Buy GS1 GTINs if you sell on marketplaces or at scale; else MPN | Your part number | Your brand | omit if GTIN or MPN present |
| Bundle you assembled | GTIN of the main item | | Brand of main item | set `is_bundle` = yes |
| Multipack you assembled | GTIN of the single item | | | set `multipack` = count |

GTIN validation: 8, 12, 13 or 14 digits, valid check digit, not a restricted circulation prefix (020 to 029, 040 to 049, 200 to 299 in GTIN-13 form) or coupon prefix (980 to 999). The QA script in [feed tools and automation](feed-tools-and-automation.md) implements this.

Never invent GTINs or reuse one across different products. Wrong GTINs cause item disapprovals and misattribution to another product's listing cluster. Missing GTINs on branded items cause "Limited performance due to missing identifiers".

## 7. Categorization

### product_type (your taxonomy)
- Up to several levels, `>` separated, most specific last. Example: `Home > Bedding > Duvet Covers > Linen`.
- Design it for bidding and reporting: the levels should match how you want listing groups and product sets split.
- Keep it stable. Renaming product types breaks listing group structures in Google Ads.

### google_product_category
- Optional. Google assigns it automatically.
- Set it explicitly when: the auto category is wrong in a way that triggers category requirements (apparel attributes, age restricted), or tax rules depend on it, or Meta and Pinterest need a category (both accept Google's taxonomy).
- Use the numeric ID or full path from Google's taxonomy file for the right language.

## 8. Attribute normalization
| Attribute | Normalize to | Why |
|-----------|-------------|-----|
| `color` | Shopper language ("Navy", not "Midnight 402"); up to 3 colors with `/` | Filters and AI matching |
| `size` | The size system the market uses; `size_system`, `size_type` for apparel | Variant grouping, filters |
| `material` | Common names, primary first ("Wool/Cashmere") | Queries use materials |
| `gender`, `age_group` | Spec values (`male`, `female`, `unisex`; `newborn`, `infant`, `toddler`, `kids`, `adult`) | Required in apparel countries |
| `condition` | `new`, `refurbished`, `used` | Required for non-new |
| Units | Metric or imperial per market, consistent | Unit pricing and AI answers |

## 9. Feed experiments: measure the impact of data changes

Merchant Center has no native A/B test for product data. Use controlled designs:

### Design options
| Design | How | When |
|--------|-----|------|
| SKU split (preferred) | Randomly assign comparable SKUs to test and control (stratify by product type and past impressions). Change titles only on test SKUs via a supplemental feed. | 200 or more SKUs with impressions in the category |
| Matched pairs | Pair SKUs by category, price and past impressions; change one of each pair | 40 to 200 SKUs |
| Pre and post with control | Change all SKUs in category A; category B unchanged acts as control; difference in differences | Small catalogs; weaker evidence |
| Channel holdout | Change data on one channel only (for example Microsoft first) | When Google is too risky to touch |

### Metrics and duration
- Primary: impressions per SKU per day (titles mainly change query matching), then CTR, then conversion value per SKU.
- Guardrail: conversion rate and ROAS must not drop; disapprovals must not rise.
- Duration: at least 2 full weeks after the change is live and processed; 4 weeks preferred. Avoid promotional periods and holidays.
- Analysis: difference in differences of log(impressions + 1) per SKU per day, test versus control, before versus after. Report the effect with a confidence interval, not a single number.
- Stop rule: stop early only for a guardrail breach (for example test ROAS 30 percent below control for 7 days with adequate volume).

### Experiment record (append to `ads-master/EXPERIMENTS.md`)
```
| E0xx | 2026-10-08 | commerce-feeds | If we lead apparel titles with gender + product type + material instead of brand, then impressions per SKU rise, because our brand has little search demand | Impressions per SKU per day | 7/6/8 | SKU split, 240 SKUs stratified by product_type | Stop if test ROAS < 0.7x control for 7 days | running | | |
```

### What usually moves results [Practitioner consensus]
- Adding the product type noun and the key attribute to titles that lacked them.
- Fixing GTINs on branded products (unlocks matching to the product cluster).
- Fixing variant image mismatches.
- Adding missing sizes and colors as attributes.
- Removing zombie SKUs from a crowded listing group so budget reaches products that can win.

Vendor case studies (feed tools, CSS partners) report large lifts from title rewrites. Their numbers are not audited and depend on the starting state [Unverified]. Use them to pick hypotheses, then test.

## 10. Pricing presentation
- `sale_price` with `sale_price_effective_date` for scheduled sales; the page must show the same sale price during that window.
- Strikethrough rules vary by country (EU price indication rules reference the lowest price in the prior 30 days). Do not inflate the regular price.
- `unit_pricing_measure` and `unit_pricing_base_measure` for goods sold by weight or volume where required.
- `installment` and `subscription_cost` only where the site offers them at checkout.
- `loyalty_program` member price only for real, joinable programs.
- Price competitiveness: compare to `benchmark_price` monthly; a product priced far above benchmark rarely wins impressions regardless of title quality.

## 11. Channel specific limits (titles and descriptions)

| Channel | Title limit | Description limit | Notes |
|---------|-------------|-------------------|-------|
| Google | 150 | 5,000 | `short_title` available in API (2026-07) |
| Meta | 200 (shorter display) | 9,999 | `rich_text_description` and `short_description` fields exist in the API |
| Microsoft | 150 | 10,000 | Accepts Google format [Unverified limits, verify] |
| Pinterest | 500 | 10,000 | Truncates heavily on Pins [Unverified limits, verify] |
| TikTok catalogs | Verify in Catalog Manager | Verify | Short display on video [Unverified] |
| OpenAI (ChatGPT) | Verify in the live spec | Plain text recommended | See [ChatGPT shopping](chatgpt-shopping-and-agentic-commerce.md) |

Verify limits against each platform's current specification before bulk changes; limits above marked Unverified were not confirmed in October 2026.
