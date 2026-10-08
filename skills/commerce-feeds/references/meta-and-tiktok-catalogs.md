# Meta and TikTok Catalogs

> Catalogs power Meta Advantage+ catalog ads (formerly dynamic ads), catalog formats inside Advantage+ sales campaigns, collaborative ads, Shops surfaces, TikTok catalog ads and TikTok Shop. commerce-feeds owns catalog health and data; meta-ads and tiktok-ads own campaigns. Knowledge as of 2026-10. Items marked [Unverified] were not re-confirmed in October 2026 because live docs were unreachable during research: verify in Commerce Manager or TikTok Catalog Manager before acting.

## Part A: Meta catalogs

### A1. Where things live
| Task | Location |
|------|----------|
| Create and manage catalogs | Commerce Manager, Catalog |
| Data sources (feeds, partner platforms, pixel, Sheets, API) | Commerce Manager, Catalog, Data sources |
| Diagnostics (item errors, warnings, pixel match) | Commerce Manager, Catalog, Issues or Diagnostics |
| Product sets | Commerce Manager, Catalog, Sets |
| Connect pixel or dataset to catalog | Commerce Manager, Catalog, Events (event source connection) |
| Catalog permission for ad accounts | Business settings, Data sources, Catalogs |

### A2. Data source options
| Option | When to use | Notes |
|--------|------------|-------|
| Partner platform (Shopify, WooCommerce, BigCommerce and others) | Default for platform stores | Sync is automatic; check which fields the integration maps (custom labels, GTIN, item group) |
| Scheduled data feed (URL) | Feed tool or custom pipeline | CSV, TSV, XML (RSS/Atom) or Google Sheets; hourly, daily or weekly schedules |
| Supplementary feed | Overrides and extra fields keyed by `id` | Same idea as Merchant Center supplemental sources [Official, verify current UI name] |
| Batch API (`/{catalog_id}/items_batch`, `localized_items_batch`) | Real-time price and stock updates, large catalogs | `allow_upsert`, `item_type`, `requests` list; check status with `check_batch_request_status` [Official, API v26.0] |
| Meta Pixel based catalog | Very small stores without feeds | Uses page microdata or Open Graph; least controllable |
| Manual | Fewer than 50 items | Not scalable |

Meta Marketing API current version: v26.0 (SDK v26.0.2, read 2026-10-08) [Official, 2026-10].

### A3. Fields (e-commerce catalog)
Required: `id` (retailer ID), `title`, `description`, `availability`, `condition`, `price`, `link`, `image_link`, `brand` (or `gtin`/`mpn` per current rules).

High-value optional fields (names from the Meta ProductItem API object, v26.0):

| Field | Use |
|-------|-----|
| `item_group_id` (API `retailer_product_group_id`) | Variant grouping |
| `sale_price`, `sale_price_start_date`, `sale_price_end_date` | Strikethrough in catalog ads |
| `additional_image_link`, `video` | More creative for carousels and dynamic media |
| `custom_label_0` to `custom_label_4` | Text segmentation for product sets |
| `custom_number_0` to `custom_number_4` | Integer fields for range filters in product sets (margin percent, stock days, review count) |
| `product_priority_0` to `product_priority_4` | Merchant-provided priority signals [Official field; usage verify] |
| `google_product_category`, `fb_product_category`, `product_type` | Category matching |
| `gtin`, `mpn`, `brand` | Matching and policy |
| `size`, `color`, `gender`, `age_group`, `material`, `pattern` | Variant and filter data |
| `rich_text_description`, `short_description` | Longer and shorter text |
| `status` (`active`, `archived`) and `visibility` (`published`, `staging`) | Hide items without deleting |
| `quantity_to_sell_on_facebook` | Inventory for onsite checkout where it exists |
| `return_policy_days`, `shipping_weight_*`, `origin_country`, `importer_name`, `manufacturer_info` | Compliance in some markets |
| `generated_background_images` | Meta AI-generated background images for catalog items; controlled through a generated image config on the catalog [Official field, 2026] |

Availability values Meta accepts include `in stock`, `out of stock`, `preorder`, `available for order`, `discontinued`.

### A4. Pixel and Conversions API matching (the most expensive silent failure)
- The `content_ids` (or `contents[].id`) sent with ViewContent, AddToCart and Purchase must equal the catalog `id` of the same variant.
- Check catalog event match in Commerce Manager (Events) and Events Manager diagnostics. A low match rate breaks retargeting product sets and weakens catalog ad delivery.
- Common causes: pixel sends parent product ID while catalog uses variant IDs (or the reverse); Shopify app sends `shopify_US_123_456` style IDs while a custom feed uses SKUs; currency mismatch.
- Decide one ID scheme across Google (`id`), Meta (`id`), TikTok (`sku_id`), Pinterest (`id`) and OpenAI (`item_id`), and make every pixel send that ID. Hand off to measurement for pixel changes.

### A5. Product sets
- Filters on any field: `custom_label_*`, `custom_number_*` ranges, `product_type`, `brand`, `price`, `availability`, `sale_price` presence.
- Standard sets to maintain:
  | Set | Filter | Used by meta-ads for |
  |-----|--------|---------------------|
  | All in stock | availability = in stock | Default catalog ads |
  | Bestsellers | `custom_label_0` = hero | Broad audiences, new customer acquisition |
  | High margin | `custom_label_1` = m_high or `custom_number_0` >= 50 | Value-focused campaigns |
  | New arrivals | `custom_label_3` = new_30d | Retargeting and engaged audiences |
  | On sale | sale price set | Promotions |
  | Exclude low stock | `custom_label_3` != low_stock | All sets |
- Name sets with the filter logic (`ps_hero_instock`) so meta-ads can read them.

### A6. Catalog ads and creative from the catalog
- Advantage+ catalog ads use the catalog for retargeting (viewed or added to cart) and broad audiences. Inside Advantage+ sales campaigns, catalog ads are one creative option [Official, verify current naming].
- Catalog creative options include carousel, collection, dynamic media (catalog videos), and overlays (price, strikethrough price, percent off, free shipping) [Official, verify].
- Image quality matters more on Meta than on Google: square crops cut product images. Provide a 1:1 friendly main image and additional images; test lifestyle images through a supplementary feed that swaps `image_link` for a product set.
- Localized catalogs: country and language override feeds (or `localized_items_batch`) for multi-market price, currency, text and links.

### A7. Shops and checkout status
Meta has narrowed onsite checkout on Facebook and Instagram Shops in the US since 2024 and steers purchases to the merchant website, while Shops ads and catalog ads continue [Unverified: confirm the current Shops checkout status for each market in Commerce Manager before planning]. Do not build a plan on onsite checkout without confirming eligibility.

### A8. Meta catalog diagnostics
| Issue | Cause | Fix |
|-------|-------|-----|
| Item rejected for policy | Commerce policies (restricted goods, misleading claims) | Edit item or exclude; request review |
| Image could not be downloaded | Bot protection, slow CDN, wrong URL | Allow Meta crawler (facebookexternalhit), stable URLs |
| Missing or invalid price, currency | Format | `19.99 USD` |
| Low pixel or event match rate | ID mismatch | Align IDs (A4) |
| Duplicate IDs across data sources | Two sources sending the same ID | One source per item; supplementary for overrides |
| Out of stock items still advertised | Feed lag | Batch API stock updates or hourly feed |

## Part B: TikTok catalogs and TikTok Shop

### B1. Two separate product systems
| System | Where | Powers | Owner |
|--------|-------|--------|-------|
| Ads catalog | TikTok Ads Manager, Assets, Catalogs (Catalog Manager) | Catalog ads for website traffic and conversions (Video Shopping Ads with catalog, Smart+ catalog ads), dynamic retargeting | commerce-feeds (data), tiktok-ads (campaigns) |
| TikTok Shop products | TikTok Shop Seller Center | Shop product pages, LIVE and video shopping, Shop campaigns (GMV Max) | Seller operations, tiktok-ads for GMV Max |

Do not assume a fix in one fixes the other. Shop listings follow Shop category rules and review; the ads catalog follows the ads catalog spec.

### B2. Ads catalog data sources [Official, verify current options]
- E-commerce platform integration (Shopify, WooCommerce, BigCommerce and others).
- Data feed by URL with a schedule (CSV, TSV, XML, Google Sheets).
- File upload using TikTok's template.
- Catalog API through the TikTok Business API.

### B3. Ads catalog fields [Unverified: confirm the template in Catalog Manager]
Required core: `sku_id`, `title`, `description`, `availability`, `condition`, `price`, `link` (landing page), `image_link`, `brand`.
Recommended: `item_group_id`, `sale_price`, `additional_image_link`, `video_link`, `google_product_category`, `product_type`, `gtin`/`mpn`, custom labels for product sets.
Rule: the TikTok pixel and Events API `content_id` must match `sku_id` for retargeting and catalog optimization (same principle as Meta A4).

### B4. TikTok Shop listing quality [Practitioner consensus]
- Category-specific required attributes and certifications; listings pass a compliance review before going live.
- Titles: product type and key attributes first, no promotional claims; images on clean background with the first image the hero; video assets matter more than on any other channel.
- Price and stock sync from the store platform through the official integration or a connector; oversell causes order cancellations that hurt shop health scores.
- GMV Max became the main and then default campaign type for promoting Shop products during 2025 [Unverified: confirm with tiktok-ads]. GMV Max uses Shop products, so Shop listing quality is the lever commerce-feeds controls.

### B5. TikTok diagnostics
| Issue | Fix |
|-------|-----|
| Catalog items rejected (image, policy) | Replace images, fix restricted items, re-submit |
| Low match between pixel events and catalog | Align `content_id` and `sku_id` |
| Shop product suppressed | Fix category attributes, compliance documents, or prohibited claims in Seller Center |
| Feed fetch failures | Public URL, no auth or IP restriction, stable schedule |

## Part C: Cross-channel catalog rules
1. One ID scheme across channels; pixels send the same IDs.
2. One master feed with channel transforms; never edit items by hand in Commerce Manager or Catalog Manager (the next sync overwrites it).
3. Same price and availability everywhere, updated at least as often as stock moves.
4. Labels and product sets mirror Google listing groups so cross-channel reports line up.
5. Image variants per channel (square crops for Meta and TikTok) via channel-specific image fields or supplementary feeds.
6. Monthly: compare item counts per channel against the master (missing items are lost revenue).

## Handoffs
| Situation | Hand off to | Pass |
|-----------|------------|------|
| Product sets ready, catalog clean | meta-ads | Set names, filters, item counts, label definitions |
| Pixel content_ids do not match catalog | measurement | Example events, catalog IDs, match rate |
| TikTok Shop listing issues affecting GMV Max | tiktok-ads | Suppressed products, revenue share, fixes in progress |
| Creative variants from catalog (AI backgrounds, video) | creative-strategy | Product sets, image rules, brand constraints |
