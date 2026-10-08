# Google Merchant Center (2026)

> Scope: Merchant Center (the former "Merchant Center Next" experience, now the only experience), the product data specification, programs, insights reports and the Merchant API. Knowledge as of 2026-10. UI labels move often: confirm menu paths in the account before writing instructions for a human.

## 1. What Merchant Center feeds

| Surface | Reporting context (Merchant API enum) | Paid or free | Feed dependency |
|---------|---------------------------------------|--------------|-----------------|
| Shopping ads (Standard Shopping, Performance Max) | `SHOPPING_ADS` | Paid | Full: titles act as keywords, images are the ad |
| Demand Gen product ads, Discover | `DEMAND_GEN_ADS`, `DEMAND_GEN_ADS_DISCOVER_SURFACE` | Paid | Images, titles, prices |
| YouTube and video ads with products | `VIDEO_ADS`, `YOUTUBE_SHOPPING`, `YOUTUBE_AFFILIATE` | Paid and free | Product cards, affiliate program |
| Display (dynamic remarketing) | `DISPLAY_ADS` | Paid | Feed ID must equal the `items.id` sent by the Google tag |
| Free product listings (Shopping tab, Search, Images, Lens, AI Overviews and AI Mode product units) | `FREE_LISTINGS` | Free | Same feed, policies apply |
| UCP-powered checkout in AI Mode and Gemini | `FREE_LISTINGS_UCP_CHECKOUT` | Free (early access) | Feed plus checkout integration, see [other AI shopping surfaces](other-ai-shopping-surfaces.md) |
| Local inventory ads, free local listings | `LOCAL_INVENTORY_ADS`, `FREE_LOCAL_LISTINGS` | Paid and free | Local inventory data source plus Business Profile |
| Product reviews, merchant reviews | `PRODUCT_REVIEWS`, `MERCHANT_REVIEWS` | Free | Review data sources |

Source for the enum list: `google/shopping/type/types.proto` in googleapis, read 2026-10-08 [Official, 2026-10]. The `FREE_LISTINGS_UCP_CHECKOUT` context is the clearest primary evidence that UCP checkout is a distinct, reportable destination.

## 2. Account setup checklist

1. Business info: legal business name, address, customer service contact (phone and email), and phone verification where prompted. Missing or inconsistent identity data is the top root cause of misrepresentation suspensions [Practitioner consensus].
2. Website: verify and claim the domain (Google tag, HTML file, Search Console, or the platform app). Every `link` must be on the claimed domain or its subdomains.
3. Shipping and returns: configure at account level (Settings, Shipping and returns). Account-level settings are cheaper to maintain than per-item `shipping`; use per-item only for exceptions (oversized, freight).
4. Link Google Ads (Settings, Linked accounts) and accept in Google Ads. Link Business Profile if you have stores.
5. Tax: US tax is configured per account where still required; check the current state for your country before adding a `tax` attribute [Unverified for 2026 changes].
6. Conversion tracking for free listings: Merchant Center can record conversions through the Google tag or a platform app. Turn it on so free listing value is visible.
7. Multi-account (advanced account) for marketplaces, agencies or many brands. Use `external_seller_id` for multi-seller accounts.

## 3. Data sources (how product data gets in)

| Data source type (Merchant API name) | Use it for | Notes |
|--------------------------------------|-----------|-------|
| Primary product data source | The master product list | Input methods: platform app (Shopify, WooCommerce, BigCommerce and others), scheduled file fetch (URL, SFTP), Google Sheets, API, or automatically from website crawl. One product comes from exactly one primary source. |
| Supplemental product data source | Overrides and additions keyed by `id` (titles, custom labels, GTIN fixes, product highlights) | Cannot create products. Must be linked to the primary source. Order of precedence is set in the primary source `default_rule.take_from_data_sources` (earlier entries win). |
| Local inventory data source | `store_code`, `id`, `availability`, `quantity`, `price`, `pickup_method`, `pickup_sla` | File input only through the UI per the API definition; requires feed label and content language. |
| Regional inventory data source | Region-level price and availability | Requires regions defined in shipping settings. |
| Promotion data source | Promotions in bulk | Requires target country and language. |
| Product review and merchant review data sources | Review feeds | Or use an approved review aggregator. |

Source: `datasourcetypes.proto` (Merchant API v1, client libraries added 2025-08-04) [Official, 2025-08].

### Feed labels and languages
- `feed_label`: up to 20 characters, uppercase letters, digits, hyphen and underscore, no spaces. Use it to split markets or variants of the same catalog (for example `US`, `CA-FR`, `EU-OUTLET`).
- `content_language`: ISO 639-1. The product resource name in Merchant API v1 is `content_language~feed_label~offer_id` (for example `en~US~sku123`). Legacy local-only products carry a `local~` prefix.
- Product IDs that contain `/`, `%` or `~` must be sent as unpadded base64url in API calls (encoded request IDs added 2025-11-11; the output field `base64_encoded_name` added 2026-04-09) [Official, 2026-04]. Better: never use those characters in IDs.

### Attribute rules (no-code transformations)
Open the data source, then the attribute rules tab. Rules can set, extract, find and replace, combine attributes, and use conditions. Use them for: building titles from attributes, mapping product_type, filling `brand` for private label, normalizing color and size, adding `custom_label_*` from conditions. Keep rules documented in `ads-master/outputs/commerce-feeds/` because the UI does not version them.

### Choosing the input method
| Situation | Use |
|-----------|-----|
| Shopify, under 50k SKUs, one market | Shopify Google and YouTube app as primary, Google Sheets or file supplemental for overrides |
| WooCommerce | Google for WooCommerce extension (API sync; version 3.9.5 on 2026-09-29) or a feed tool if you need heavy transforms |
| Many channels (Google, Meta, TikTok, Microsoft, Pinterest, OpenAI) or more than 50k SKUs | Feed management platform as the single transformation layer |
| Custom platform with engineers | Merchant API direct (products, inventories, datasources) plus a scheduled full file as a safety net |
| Price or stock changes many times a day | API updates for price and availability, full refresh daily |

## 4. Product data specification: what matters

Required or conditionally required (most countries):

| Attribute | Rule | Common failure |
|-----------|------|----------------|
| `id` | Unique, stable, max 50 chars. Never recycle IDs. | Changing IDs on replatform resets history and Shopping bidding signals |
| `title` | Max 150 chars, front-load the words people search | Promo text, all caps, keyword stuffing |
| `description` | Max 5,000 chars, plain text facts | Copy from a supplier, HTML, promo text |
| `link` | Claimed domain, https, lands on the exact variant | Redirects to home, geo redirects, variant not preselected |
| `image_link` | See images below | Placeholder, watermark, promo overlay, too small |
| `availability` | `in_stock`, `out_of_stock`, `preorder`, `backorder` (plus `availability_date` for the last two) | Mismatch with the page |
| `price` | Number plus ISO 4217 currency, must match page and checkout | Tax-inclusive mismatch, currency geo switching |
| `brand` | Required for most new products (except movies, books, music) | Store name used as brand for third-party products |
| `gtin` | Required when the manufacturer assigned one. Up to 10 GTINs per item in Merchant API (`gtins`) | Invented, reused, or restricted prefix GTINs |
| `mpn` | When no GTIN | Internal SKU used as MPN |
| `identifier_exists` | `no` only for custom, handmade, vintage or private label without GTIN | Set to `no` to hide missing GTINs on branded goods |
| `condition` | Required for used and refurbished | Missing on refurb |
| `item_group_id` | Required for variants | Each variant missing the shared group ID |
| `color`, `size`, `gender`, `age_group` | Required for apparel in several countries (US, UK, DE, FR, JP, BR) | Size in title only |
| `shipping` | Required unless set at account level | Missing for new countries |

High-impact optional attributes:

| Attribute | Why it matters |
|-----------|---------------|
| `product_type` | Your own taxonomy. Use it for listing groups and reporting. Full path, for example `Women > Knitwear > Sweaters > Merino`. |
| `google_product_category` | Optional; Google assigns one automatically. Override only when Google's choice is wrong and it matters (tax, policy, category-specific requirements). |
| `custom_label_0` to `custom_label_4` | Bidding and reporting segmentation. Max 100 chars, max 1,000 unique values per label per account. See [custom labels](custom-labels-and-segmentation.md). |
| `sale_price`, `sale_price_effective_date` | Strikethrough pricing and sale annotations |
| `additional_image_link` (up to 10), `lifestyle_image_link` | More visuals; lifestyle images used where Google shows in-context imagery |
| `product_highlight`, `product_detail` | Scannable facts that AI surfaces and free listings can use |
| `cost_of_goods_sold` | Enables gross profit reporting in Google Ads when conversions carry cart data |
| `ads_redirect` | Tracking URL for ads only |
| `excluded_destination`, `pause` (`ads`) | Remove from a destination or pause ads without deleting |
| `shopping_ads_excluded_countries` | Exceptions to data source country settings |
| `auto_pricing_min_price` | Floor for automated discounts and dynamic promotions |
| `certification` | EU energy label (EPREL) and other certifications |
| `unit_pricing_measure`, `unit_pricing_base_measure` | Required in some EU countries for certain goods |
| `loyalty_program` | Member price, points, member shipping (see programs) |

### New attributes, January 2025 to October 2026

| Date | Attribute or change | Status and notes | Label |
|------|---------------------|------------------|-------|
| 2025-10-06 | `carrier_shipping` (carrier-calculated rates and transit inside the product) | In Merchant API v1 | [Official, 2025-10] |
| 2026-03-11 | `handling_cutoff_timezone`, `shipping_handling_business_days`, `shipping_transit_business_days` | Merchant API fields | [Official, 2026-03] |
| 2026-04-14 | `handling_cutoff_time` and `minimum_order_value` at product level; loyalty program and tier labels inside `shipping` | Product data specification update 2026, phase 1 | [Official, 2026-04] |
| 2026-04-14 | `video_link` (Merchant API `video_links`) | Errors reported from 2026-04-14; display and policy review from 2026-06-30. A failing video is held back, the listing stays live. | [Official, 2026-04] |
| 2026-04-28 | `pickup_cost` and minimum order value for in-store pickup | Required for pickup offers in the UK, Switzerland and EEA | [Official, 2026-04] |
| 2026-07-13 | `questions_and_answers` (max 30 pairs, 1,000 chars per question or answer, 10,000 total), `popularity_rank` (0 to 100), `item_group_title`, `document_links` (PDF manuals and guides), `variant_options` (name and value pairs), `related_products` (types: part of set, required part, often bought with, substitute, different brand, accessory), `short_title`, vehicle and property attributes | Added to Merchant API v1 ProductAttributes. These match the "dozens of new attributes for conversational discovery" Google announced in January 2026. Check the specification for which surfaces use them in your country. | [Official, 2026-07] |
| 2026-09-29 | Offer-level `returns` (countries, window days, window type, item conditions, methods, outcomes, return shipping fee and type, restocking fee, policy URL) | Merchant API v1; complements account-level return policies and `return_policy_label` | [Official, 2026-09] |
| 2027-01-31 | Minimum image size rises to 500 x 500 px | Undersized images already show warnings. Google may upscale with AI or substitute a higher resolution image to avoid rejection. | [Official, 2026-04] |

Sources: googleapis commit history for `products_common.proto` (2025-08-05 to 2026-09-29) and the Merchant Center "Product data specification update 2026" help article as summarized by secondary coverage. The attribute naming differs between feed files (singular, snake case such as `video_link`) and the Merchant API (repeated, such as `video_links`).

## 5. Images

| Rule | Detail | Label |
|------|--------|-------|
| Formats | JPEG, PNG, WebP, non-animated GIF, BMP, TIFF | [Official] |
| Size today | Minimum 100 x 100 (250 x 250 apparel); maximum 64 megapixels and 16 MB | [Official] |
| Size from 2027-01-31 | Minimum 500 x 500 | [Official, 2026-04] |
| Practical target | 1,200 px or larger on the long side, product fills 75 to 90 percent of the frame | [Practitioner consensus] |
| Main image | Product alone on a plain white, gray or light background for most categories; show the exact variant | [Official] |
| Not allowed | Promotional overlays, watermarks, borders, logos of the store over the product, placeholder images, collage of different products, images of a different variant | [Official] |
| Lifestyle | Send as `lifestyle_image_link` and in `additional_image_link`; never as the only image for categories that need the product clearly visible | [Official] |
| AI-generated or edited images | Allowed if they accurately represent the product. Images created with generative AI must keep the IPTC `DigitalSourceType` metadata value `TrainedAlgorithmicMedia`. Product Studio output carries this metadata. Never add features, colors or accessories the product does not have. | [Official, 2024] verify current wording |
| AI-generated text | Submit AI-written titles and descriptions through `structured_title` and `structured_description` with `digital_source_type` set to `trained_algorithmic_media` (API enum `TRAINED_ALGORITHMIC_MEDIA`) | [Official] |
| Automatic image improvements | Merchant Center can remove promotional overlays automatically. Keep it on, but fix the source images. | [Official] |

## 6. Programs and settings

### Shipping and returns
- Account level: shipping services by country with rates, handling and transit times, cutoff times, free shipping thresholds. Return policies by country with window, fees, methods, restocking fees.
- Product level for exceptions: `shipping`, `shipping_label`, `transit_time_label`, `return_policy_label`, and since 2026-09 offer-level `returns`.
- Accurate fast and free shipping and returns can earn annotations in listings. They also feed the store quality signals (see below).

### Loyalty programs (member pricing)
- Set up the program in Merchant Center (Growth or programs area, "Loyalty"), with program label and tiers. Then send `loyalty_program` per item: `program_label`, `tier_label`, `price` (member price, must be lower or equal to regular price), `cashback_for_future_use`, `loyalty_points`, `member_price_effective_date`, `shipping_label`.
- Since 2026-04-14 shipping services can carry `loyalty_program_label` and `loyalty_tier_label`, so member-only free shipping is expressible per item.
- Mirror member pricing on the page with schema.org `validForMemberTier` (see [structured data alignment](structured-data-alignment.md)).

### Promotions
- Create in Marketing, Promotions, or with a promotion data source. Each promotion needs a `promotion_id`, title, dates, offer type, applicable products (all or specific via `promotion_id` on items), and must work at checkout exactly as described.
- Review takes time: submit at least several days before launch [Practitioner consensus: 3 to 7 days before peak events].
- Common rejection: code does not work, terms not on site, promotion overlaps sale pricing in a confusing way, minimum spend not stated.

### Product reviews and store ratings
- Product ratings appear when you send reviews through the product review data source or an approved aggregator. Google requires a minimum review volume across the catalog before ratings show [Official, threshold verify].
- Store quality: Merchant Center shows a store quality or shopping experience scorecard in some countries with shipping speed, return policy, website quality signals. Treat it as a checklist of operational improvements.

### Local inventory and free local listings
- Requirements: Business Profile with verified store addresses linked to Merchant Center, local inventory data source with `store_code`, `id`, `quantity` or `availability`, `price`.
- Product IDs: the Merchant API v1 product name no longer carries the channel. Online and in-store versions of the same item share one product unless attributes differ. If price or condition differ between online and in store, use separate IDs or local inventory overrides [Official for naming, 2025-08; enforcement details Unverified].
- Store pickup: `pickup_method` (buy, reserve, ship to store, not supported), `pickup_sla`, and since 2026-04 `pickup_cost` in the UK, CH and EEA.

### Insights reports (Analytics or Insights area; Merchant API Reports)
| Report | What it gives | How to use it |
|--------|--------------|---------------|
| Price competitiveness (`price_competitiveness_product_view`) | Your price versus `benchmark_price` across merchants | Flag SKUs priced above benchmark by more than your tolerance, check margin, consider price or bid changes |
| Price insights (`price_insights_product_view`) | `suggested_price` and predicted change in impressions, clicks, conversions, with `effectiveness` LOW, MEDIUM, HIGH | Test HIGH effectiveness suggestions on a SKU split, never apply blindly to low margin SKUs |
| Best sellers (`best_sellers_product_cluster_view`, `best_sellers_brand_view`) | Popular products and brands by category and country with `relative_demand`, rank changes, and your `inventory_status` | Find in-demand products you do not stock or have out of stock |
| Product view (`product_view`) | Status per reporting context, item issues, `click_potential` and `click_potential_rank` (1 is highest) | Prioritize fixes on items with HIGH click potential |
| Competitive visibility | Share of visibility against competitors | Read with market-intel |

Example Merchant API report query (POST `https://merchantapi.googleapis.com/reports/v1/accounts/{ACCOUNT_ID}/reports:search`, body `{"query": "..."}`):

```sql
SELECT offer_id, title, brand, price, benchmark_price
FROM price_competitiveness_product_view
WHERE report_country_code = 'US'
```

```sql
SELECT offer_id, title, aggregated_reporting_context_status, click_potential, click_potential_rank, item_issues
FROM product_view
WHERE aggregated_reporting_context_status = 'NOT_ELIGIBLE_OR_DISAPPROVED'
```

Field names come from `reports.proto` (v1). Confirm query grammar in the Merchant API reference before automating.

### Product Studio
- AI tools inside Merchant Center (Marketing area) to generate scenes, remove or replace backgrounds, upscale images and suggest text. A Product Studio API exists in alpha (`productstudio/v1alpha`: image and text suggestion services) [Official, 2026].
- Rules: keep the product itself unchanged, keep metadata, review every output, store originals. Use generated scenes for `lifestyle_image_link` and Demand Gen, not as a replacement for an accurate main image.

### Automatic improvements
- Automatic item updates: Merchant Center can update price and availability from your structured data when it detects a mismatch, which prevents disapprovals but hides the root cause. Keep it on as a safety net and still fix the source.
- Automated discounts and dynamic promotions: Google can lower prices for eligible products within limits; set `auto_pricing_min_price` as a floor. Requires the right conversion setup. Decide with the human: it changes the price customers pay.

## 7. Merchant API (replaces the Content API for Shopping)

| Date | Event | Label |
|------|-------|-------|
| 2024 | Merchant API beta announced as successor to Content API | [Official] |
| 2025-08 | Merchant API v1 general availability (v1 client libraries published 2025-08-04 and 2025-08-05) | [Official, 2025-08] |
| 2026-02-28 | Merchant API v1beta retired | [Official per secondary sources, 2026] |
| 2026-08-18 | Content API for Shopping shut down. Google offered an extended access request form for teams that needed more time. | [Official, 2025] |
| After 2026-08-18 | Reports of failing Content API calls and full decommission planned for 2027 | [Unverified] |

What changed for builders:
- Sub-APIs: accounts, conversions, datasources, inventories (local and regional), issueresolution, lfp, loyaltycustomers, notifications, ordertracking, products, productstudio (alpha), promotions, quota, reports, reviews, youtube.
- Products: you write `productInputs` into a specific data source (`productInputs:insert?dataSource=accounts/{a}/dataSources/{d}`) and read processed `products` (after rules and supplemental sources). Updates use `PATCH` with an `updateMask`. It can take several minutes for the processed product to reflect a change.
- Product inputs inserted by API expire if not refreshed within 30 days. Re-insert at least every 30 days (daily is normal).
- `version_number` lets you prevent an older update from overwriting a newer one.
- The `channel` field is gone from v1 names; legacy local-only products use the `local~` prefix.
- Notifications sub-API can push product status changes instead of polling.
- Google Ads scripts that read Merchant Center data moved to the Merchant API in 2026 [Unverified exact date: secondary source cites April 22].

Minimal insert (REST, OAuth scope `https://www.googleapis.com/auth/content`):

```bash
curl -X POST \
  "https://merchantapi.googleapis.com/products/v1/accounts/${ACCOUNT_ID}/productInputs:insert?dataSource=accounts/${ACCOUNT_ID}/dataSources/${SUPPLEMENTAL_DS_ID}" \
  -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json" \
  -d '{
    "offerId": "SKU123",
    "contentLanguage": "en",
    "feedLabel": "US",
    "productAttributes": {
      "customLabel0": "hero",
      "customLabel1": "m_high",
      "productHighlights": ["100 percent merino wool", "Machine washable at 30 C"]
    }
  }'
```

Write to a supplemental data source for enrichment so the platform app keeps owning the primary data. Never write to a primary source that a platform app also writes to.

## 8. Policies and account health

| Area | What triggers trouble | Prevention |
|------|----------------------|-----------|
| Misrepresentation (account suspension) | Missing or hidden contact details, no physical address where expected, unclear return or refund terms, unrealistic discounts, claims you cannot prove, fake urgency, missing business identity, site that looks unfinished, payment method oddities, mismatched business name | Complete About, Contact, Shipping, Returns, Terms, Privacy pages linked in the footer; consistent business name across site, Merchant Center, payment descriptor; no invented reviews or badges |
| Price and availability accuracy | Feed differs from page or checkout | Structured data parity, fast updates, automatic item updates as a net |
| Landing page | 404, redirect to home, blocked crawl (robots, bot protection, geo block), slow or broken mobile | Allow Googlebot and Storebot-Google; test with a US IP if you geo-redirect |
| Restricted content | Healthcare, weapons, adult, alcohol, gambling, financial | Category review before upload; use `excluded_destination` or country exclusions |
| Counterfeit and trademark | Unauthorized brand use | Brand authorization documentation |
| Unsupported shopping content | Services, real estate (outside dedicated programs), digital goods in many countries | Exclude from feed |

Warnings: Merchant Center often issues an account-level warning with a fixed window (commonly 28 days) before suspension for policy issues [Official, verify per notice]. Suspensions for misrepresentation usually have no warning.

Recovery steps live in [diagnostics and disapprovals](diagnostics-and-disapprovals.md) and in the playbooks.

## 9. Free listings
- Free listings are on by default for eligible products in eligible countries. Check the Free listings program status.
- They feed AI Overviews and AI Mode product experiences and Google Lens results. Treat them as an organic channel with its own reporting (Merchant Center performance, filtered by free listings).
- Free listings are the cheapest way to be present in Google AI shopping surfaces today. Rich attributes, competitive price, accurate shipping and returns, and reviews are the levers.

## 10. Operating cadence for Merchant Center
| Cadence | Check |
|---------|-------|
| Daily (peak season) or 3x per week | Needs attention count and disapproved revenue share; account issues; data source fetch status |
| Weekly | Price competitiveness top 50 revenue SKUs; new item issues; promotions approval; zombie rate |
| Monthly | Attribute completeness; best sellers gaps; title program progress; label refresh audit |
| Quarterly | Full audit with [audit checklist](audit-checklist.md); specification change log review |
