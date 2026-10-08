# Microsoft, Pinterest, Snapchat and Other Catalogs

> Secondary catalogs are cheap incremental reach when the master feed is clean. Most accept the Google product specification with small differences. Knowledge as of 2026-10. Items marked [Unverified] could not be re-confirmed against live docs in October 2026.

## 1. Microsoft Merchant Center (Bing Shopping, Microsoft PMax, Copilot)

### 1.1 What it powers
| Surface | Notes |
|---------|-------|
| Microsoft Shopping campaigns | Product groups by category, brand, product type, item ID, condition, custom labels |
| Performance Max on Microsoft Advertising | Uses the same store feed |
| Bing free shopping listings and Bing shopping tab | Organic product listings |
| Copilot shopping and Copilot Checkout | Copilot Checkout launched 2026-01-08 in the US on Copilot.com; Shopify merchants auto-enrolled after an opt-out window; PayPal and Stripe merchants apply; merchants stay merchant of record. Mobile app checkout and a catalog of more than 500,000 merchants announced April 2026 [Official, 2026-01; 2026-04 per coverage] |
| Brand Agents | Retailer-shaped shopping agents in Copilot with Clarity analytics [Official, 2026-01] |

### 1.2 Setup
1. Microsoft Advertising, Tools, Microsoft Merchant Center: create a store, verify and claim the domain (UET tag or other method).
2. Feed options: scheduled file fetch (URL, FTP or SFTP), manual upload, API (Content API style), or the Google Merchant Center Import tool [Official, Microsoft Advertising Help]. Import facts: sign in with Google (standard and multi-client accounts); schedules daily, weekly, monthly or run now, set per import under Imports > Scheduled imports; signing out of Google does not stop a scheduled import (delete it to stop); only approved Google offers are imported (pending and disapproved are skipped); only offers targeting Microsoft Shopping markets come across; since October 2024 imports carry the Google feed label and land in one consolidated feed [Official, 2024-09]. An older guide says imported offers expire after 30 days unless re-imported [Unverified for 2026, keep at least weekly schedules].
3. Format: Microsoft accepts the Google product data specification for most attributes (`id`, `title`, `link`, `price`, `description`, `image_link`, `gtin`, `brand`, `mpn`, `availability`, `condition`, `product_type`, `google_product_category`, `custom_label_0..4`, `item_group_id`, `sale_price`).
4. Catalog review: new feeds go through review; fix errors in the Merchant Center catalog view.
5. Link the store to Shopping or PMax campaigns.

### 1.3 Differences to watch [Practitioner consensus]
- Microsoft has its own policy review and its own disapprovals; a feed that is clean on Google can still have Microsoft errors.
- Microsoft audiences skew older and more desktop; titles with model numbers and specs often matter more.
- Copilot uses product data from merchant feeds and the web; complete attributes and accurate policies help eligibility for shopping answers [Unverified mechanism].
- If you import from Google, transformations made by Google attribute rules may not carry over. Import the output feed of your feed tool, not the raw primary source, when you depend on rules [Unverified, test].

### 1.4 Copilot Checkout readiness
- Shopify: check the Copilot channel or AI channels settings in Shopify admin; decide opt in or opt out with the human.
- PayPal or Stripe merchants: apply through Microsoft's program page linked from the Microsoft Advertising blog (January 2026). Prepare: return policy, shipping policy, customer service contact, product data with GTIN and accurate stock.
- Measurement: orders through Copilot Checkout may not pass through your site analytics. Agree on an order source tag with measurement.

Handoff: microsoft-ads owns campaigns; commerce-feeds owns the store feed, Copilot Checkout readiness and the data quality.

## 2. Pinterest catalogs

### 2.1 What it powers
Shopping ads and catalog-based ads (including Performance+ campaign types), Product Pins, shopping surfaces in search and closeups.

### 2.2 Data sources
- Data source by URL (CSV, TSV, XML) with scheduled ingestion, platform apps (Shopify, WooCommerce, BigCommerce and others), and the Catalogs API (items batch) in the Pinterest API v5.

### 2.3 Attributes (Pinterest API v5.28.0, read 2026-10-08) [Official, 2026-10]
| Group | Attributes |
|-------|-----------|
| Core | `id`, `title`, `description`, `link`, `image_link`, `price`, `availability`, `condition`, `brand`, `gtin`, `mpn` |
| Variants | `item_group_id`, `color`, `size`, `size_system`, `size_type`, `gender`, `age_group`, `material`, `pattern`, `variant_names`, `variant_values` |
| Pricing | `sale_price`, `sale_price_effective_date`, `installment_price`, `min_ad_price`, `unit_pricing_measure`, `unit_pricing_base_measure`, `tax` |
| Shipping | `shipping`, `shipping_weight`, `shipping_width`, `shipping_height`, `free_shipping_label`, `free_shipping_limit` |
| Media | `additional_image_link`, `video_link` (mp4, mov or m4v, up to 2 GB), `ad_image_0_link` to `ad_image_19_link` with `ad_image_N_tag`, `ad_video_0_link` to `ad_video_2_link` |
| AI disclosure | `ai_disclosures`: declare which AI disclosure types apply to each asset URL (`image_link`, `additional_image_link`, `video_link`) |
| Segmentation | `custom_label_0` to `custom_label_4`, `custom_number_0` to `custom_number_4` (integers 0 to 4,294,967,295), `product_type`, `google_product_category` |
| Tracking and apps | `ad_link` (separate tracking URL for ads), `mobile_link`, `ios_deep_link`, `android_deep_link`, `promotion_id` |
| Reviews | `average_review_rating`, `number_of_ratings`, `number_of_reviews` |
| Deprecated | `checkout_enabled` ("not supported anymore" per the API description) |

### 2.4 Pinterest specifics [Practitioner consensus]
- Visual first: lifestyle and styled images often outperform plain cutouts as the main image on Pinterest. Use `ad_image_*` fields to send ad-specific creative without changing the organic image.
- Vertical (2:3) images display better than square in many placements.
- Product groups in Pinterest Ads Manager filter by labels, product type, brand, price.
- Pinterest tag `product_id` should match the catalog `id`.

## 3. Snapchat catalogs [Unverified details: verify in Snapchat Ads Manager]
- Catalogs in Snapchat Ads Manager (Assets or Catalogs), sourced from a feed URL (CSV, TSV, XML) or Shopify integration.
- Powers Dynamic Product Ads (retargeting and broad) and catalog-based collection formats.
- Required fields mirror the Google core set (`id`, `title`, `description`, `link`, `image_link`, `availability`, `price`, `brand`, `condition`); Snap Pixel and Conversions API `item_ids` must match catalog IDs.
- Snapchat audiences skew younger and mobile; vertical imagery and short titles matter.

## 4. Other destinations

| Destination | Feed relationship | Notes |
|-------------|------------------|-------|
| Google CSS partners (EU, UK, CH) | Use your Merchant Center feed through a CSS account | CSS choice changes the "By" line and can lower CPCs in the EU; feed unchanged |
| Criteo, retail media, affiliate networks | Own feed specs, usually Google-compatible | Map in the feed tool |
| Marketplaces (Amazon, Walmart, eBay, Zalando) | Separate listing systems, not ad feeds | Out of scope for ad feeds; keep IDs and GTINs consistent for entity matching |
| Price comparison sites (idealo, PriceRunner, Kelkoo) | Own feeds | Useful in EU markets |
| Shopify Catalog (AI channels) | Built from Shopify product data; non-Shopify brands can join via Shopify's Agentic plan [Official per secondary coverage, 2026] | See [other AI shopping surfaces](other-ai-shopping-surfaces.md) |
| ChatGPT (OpenAI) | Own spec plus a Google-compatible path | See [ChatGPT shopping](chatgpt-shopping-and-agentic-commerce.md) |
| Perplexity | Merchant program; Shopify and PayPal integrations | See [other AI shopping surfaces](other-ai-shopping-surfaces.md) |

## 5. Rollout order for secondary channels

| Business situation | Next catalog after Google | Why |
|--------------------|---------------------------|-----|
| Ecommerce with Google Shopping working, budget Growth or above | Microsoft Merchant Center | Almost zero marginal work; Copilot exposure |
| Visual categories (home, fashion, beauty, weddings, food) | Pinterest | Planning intent, long consideration |
| Paid social active | Meta catalog (usually already exists) | Retargeting and Advantage+ catalog ads |
| Under 35 audience, short video creative | TikTok catalog, then TikTok Shop if fulfillment fits | Video commerce |
| US store on Shopify or with GMC feed | ChatGPT and Copilot via platform toggles or applications | AI shopping discovery |
| Snapchat audience fits (young, mobile) | Snapchat catalog | Retargeting reach |

## 6. Multi-catalog QA
- Item counts per destination versus master, weekly.
- Disapproval reasons per destination in one table (Google, Microsoft, Meta, TikTok, Pinterest, Snap, OpenAI).
- ID match rate between each pixel and its catalog (measurement owns the pixel; commerce-feeds owns the catalog IDs).
- Price and availability parity: sample 50 SKUs per destination per month and compare to the site.

## 7. Transform table: Google master to secondary channels

| Field | Microsoft | Pinterest | Snapchat | Notes |
|-------|-----------|-----------|----------|-------|
| `id` | same | same | same | Never change per channel |
| `title` | same | same, consider shorter | shorter (mobile) | Keep the first 60 chars meaningful everywhere |
| `description` | same | same | same | Plain text |
| `image_link` | same | lifestyle or vertical image if available | vertical crop if available | Use channel image fields, not a different master |
| `price`, `sale_price` | same | same | same | Same currency per market |
| `availability` | same values | same values | same values | Map `preorder` and `backorder` if a channel lacks them |
| `custom_label_*` | same labels | same labels plus `custom_number_*` | verify support | Keep definitions identical so reports line up |
| `link` | same, with channel UTM | `ad_link` for tracked ads URL | same, with UTM | Do not break canonical URLs with parameters that change content |
| `google_product_category` | accepted | accepted | accepted [Unverified] | Use the Google taxonomy ID |
| AI disclosure | n/a | `ai_disclosures` | n/a | Declare generated assets |

## 8. Microsoft troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Store not approved | Domain not verified, policy pages missing | Verify domain; publish policies |
| Many items rejected that pass on Google | Microsoft-specific policy or crawl issue | Read item-level reasons; check that Bingbot can crawl |
| Feed imported but labels missing | Imported raw source without rules | Import the transformed output |
| Product groups empty in campaigns | Labels or product types differ from Google | Align transforms |
| Copilot shows outdated price | Feed refresh lag | Increase fetch frequency; parity check |

## 9. Pinterest and Snap launch checklist
1. Domain claimed (Pinterest) or verified (Snap).
2. Tag or pixel installed with product IDs matching catalog IDs (measurement owns).
3. Catalog ingested; errors under 2 percent of items.
4. Product groups created from labels (bestsellers, high margin, new, in stock).
5. Creative variants available (lifestyle, vertical) through channel image fields.
6. Weekly item count and error review during the first month.

## Handoffs
| Situation | Hand off to | Pass |
|-----------|------------|------|
| Microsoft store feed ready, product groups needed | microsoft-ads | Store ID, label definitions, product type tree |
| Copilot Checkout decision | growth-orchestrator (decision), measurement (order attribution) | Eligibility, policy readiness, risks |
| Pinterest or Snap campaign planning | growth-orchestrator (no dedicated agent) and creative-strategy | Catalog status, image variants available |
