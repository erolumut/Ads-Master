# Custom Labels and Product Segmentation

> Custom labels turn business data (margin, stock, season, performance) into fields that ad platforms can split budgets on. The commerce-feeds agent designs and maintains the labels; google-ads, meta-ads, microsoft-ads and tiktok-ads decide how campaigns use them. Knowledge as of 2026-10.

## 1. Limits and mechanics

| Platform | Fields | Limits | Where used |
|----------|--------|--------|-----------|
| Google Merchant Center | `custom_label_0` to `custom_label_4` | Max 100 characters; max 1,000 unique values per label per account [Official] | Shopping and PMax listing groups, Google Ads reporting segments (`segments.product_custom_attribute0..4`), PMax asset group listing groups |
| Microsoft Merchant Center | `custom_label_0` to `custom_label_4` | Same model as Google [Official, verify limits] | Shopping and PMax product groups |
| Meta catalogs | `custom_label_0` to `custom_label_4` (text), `custom_number_0` to `custom_number_4` (integer) | Text labels used in product set filters; numbers allow range filters [Official, API v26.0 field list] | Product sets for Advantage+ catalog ads |
| Pinterest | `custom_label_0` to `custom_label_4`, `custom_number_0` to `custom_number_4` (0 to 4,294,967,295) | [Official, API v5.28] | Product groups |
| TikTok catalogs | Custom label fields available in catalog product sets [Unverified field names] | Verify in Catalog Manager | Product sets for catalog ads |
| OpenAI Ads feeds | Google Shopping schema reused per secondary sources [Unverified] | Verify | Feed campaigns in ChatGPT Ads Manager |

Google Ads also exposes non-label dimensions for listing groups: brand, category, product type (5 levels), item ID, condition, channel. Labels are needed only for business data the feed does not otherwise carry.

## 2. Slot plan (default, adapt to STRATEGY.md)

| Slot | Purpose | Values | Refresh | Owner of the logic |
|------|---------|--------|---------|-------------------|
| `custom_label_0` | Performance tier | `hero`, `sidekick`, `villain`, `zombie`, `new` | Weekly | commerce-feeds computes, google-ads consumes |
| `custom_label_1` | Margin band | `m_high`, `m_mid`, `m_low`, `m_unknown` | Monthly or on cost change | commerce-feeds from COGS |
| `custom_label_2` | Price band vs AOV | `p_under_half_aov`, `p_near_aov`, `p_over_2x_aov` | Monthly | commerce-feeds |
| `custom_label_3` | Lifecycle and stock | `new_30d`, `low_stock`, `overstock`, `core`, `clearance` | Daily or weekly | commerce-feeds from inventory |
| `custom_label_4` | Season or campaign theme | `bfcm_2026`, `winter`, `gifting`, `evergreen` | Per season | Human or growth-orchestrator decision |

Rules:
- Use stable, lowercase values with prefixes so they sort and filter cleanly. Never encode dates that change daily (that explodes cardinality and resets listing groups).
- One concept per slot. Do not mix margin and season in one label.
- Document the definitions in `ads-master/memory/commerce-feeds.md` (once confirmed) and in the delivered spec file.

## 3. Label formulas

### Performance tier (custom_label_0)
Inputs: last 30 to 60 days per item ID: impressions, clicks, cost, conversions, conversion value. Breakeven ROAS = 1 / contribution margin (from PROJECT_BRIEF.md).

| Tier | Rule (defaults, tune per account) | Typical campaign treatment |
|------|-----------------------------------|----------------------------|
| `new` | Created in the last 30 days and fewer than 30 clicks | Own listing group or campaign with a lower ROAS target so it gets exposure |
| `zombie` | Fewer than 50 impressions in the period | Separate campaign or asset group with a low target (or Maximize clicks with a cap in Standard Shopping) to force exposure; fix data first |
| `sidekick` | Has impressions but fewer than 30 clicks, or ROAS within 0.8x to 1.2x of target | Main campaign |
| `hero` | At least 1 conversion and ROAS at or above 1.2x target | Main or dedicated campaign with budget room; protect stock |
| `villain` | 30 or more clicks and zero conversions, or ROAS below 0.8x target | Higher target, lower bids, or exclusion after checking price, page and data |

Thresholds scale with traffic: in Starter accounts use 60 to 90 days and a lower click minimum (15 to 20). In Enterprise accounts use 30 days.

Avoid hard loops: a hero that gets less budget becomes a sidekick, then gets budget again, and so on. Smooth with a hysteresis rule: change tier only if the new tier holds for 2 consecutive refreshes.

### Margin band (custom_label_1)
- Gross margin % = (price minus unit cost) / price, using the current selling price (sale price when active).
- Better: contribution margin % = (price minus unit cost minus shipping minus payment fees minus expected returns cost) / price.
- Default bands: high 55 percent or more, mid 35 to 55 percent, low under 35 percent. Set bands from the catalog distribution (terciles) if most products sit in one band.
- Used for: different ROAS targets per band (POAS logic), or value rules. Alternative for Google Ads: send `cost_of_goods_sold` and report gross profit; labels still help structure.

### Price band (custom_label_2)
- Relative to AOV or to the category median price. Low-price items rarely carry the click cost alone; high-price items need longer windows and more data.
- Default: under 0.5x AOV, 0.5x to 2x AOV, over 2x AOV.

### Lifecycle and stock (custom_label_3)
- Days of cover = inventory quantity / (units sold in last 30 days / 30).
- `low_stock`: under 14 days of cover (do not push budget into items about to sell out).
- `overstock`: over 120 days of cover and meaningful quantity (push with lower targets or promotions).
- `new_30d`: created in last 30 days.
- `clearance`: set by merchandising (end of line).

### Seasonality and themes (custom_label_4)
- Values per season or campaign: set them 2 to 4 weeks before the season so campaigns can be built and approved.
- Remove the value after the season ends to avoid dead listing groups.

### Price competitiveness (optional, if a slot is free)
- From the Merchant Center price competitiveness report: `pc_below` (price under benchmark by over 3 percent), `pc_at` (within 3 percent), `pc_above` (over benchmark by more than 3 percent), `pc_none` (no benchmark).
- Lets google-ads lower targets where you are cheap and test bids where you are expensive.

## 4. How the ad agents use labels

### google-ads
- Standard Shopping: subdivide listing groups by `custom_label_0` (tiers) within campaigns split by margin band, with campaign priority settings when running a query sculpting structure.
- Performance Max: listing group filters per asset group (for example, one asset group for heroes, one for the rest), or separate PMax campaigns by margin band with different tROAS targets. PMax campaigns compete for the same product only if they include it: keep each product in exactly one PMax campaign.
- Zombie campaign: products with almost no impressions grouped into their own campaign, often with a lower tROAS or Maximize conversion value without target for a fixed test period.
- Reporting: GAQL with `segments.product_custom_attribute0` etc.

```sql
SELECT
  segments.product_item_id,
  segments.product_title,
  segments.product_custom_attribute0,
  segments.product_custom_attribute1,
  metrics.impressions, metrics.clicks, metrics.cost_micros,
  metrics.conversions, metrics.conversions_value
FROM shopping_performance_view
WHERE segments.date DURING LAST_30_DAYS
```

### meta-ads
- Product sets filtered by `custom_label_*` or by `custom_number_*` ranges (for example margin percent as an integer in `custom_number_0`, then a product set "margin at least 50").
- Typical sets: bestsellers for cold audiences, high margin for broad Advantage+ catalog ads, new arrivals for retargeting, exclude low stock.

### microsoft-ads
- Product groups by custom label in Shopping and PMax, same as Google.

### tiktok-ads
- Product sets for catalog ads (Video Shopping Ads with catalog, Smart+ catalog). TikTok Shop GMV Max uses the Shop product list, not the ads catalog labels [Unverified, check with tiktok-ads].

## 5. Implementation options

| Method | Best for | How |
|--------|---------|-----|
| Google Sheets supplemental data source | Small to mid catalogs, no engineering | Sheet with `id` and label columns; add as supplemental source; set fetch schedule. Script or tool writes the sheet. |
| File supplemental data source (URL or SFTP) | Mid to large catalogs | Scheduled job writes TSV to a URL; Merchant Center fetches daily |
| Merchant Center attribute rules | Simple static logic (price band, brand groups) | Conditions on existing attributes |
| Feed management platform rules | Multi-channel catalogs | One rule set feeds Google, Meta, Microsoft, TikTok, Pinterest |
| Merchant API productInputs into a supplemental source | Frequent updates, engineering available | `productInputs:insert` with only `customLabel*` attributes |
| Third-party label tools | Performance-based labels without building | Tools that compute tiers from Google Ads data (several feed tools and CSS partners offer this) [Practitioner consensus] |
| Platform metafields | Shopify with the Google and YouTube app | Product or variant metafields in the Google namespace map to custom labels [Practitioner consensus, verify field mapping in the app] |

### Label builder script
`label_builder.py` (in [feed tools and automation](feed-tools-and-automation.md)) reads a catalog export (id, price, cost, created_at, inventory, units sold) and a product performance export, and writes a TSV supplemental feed with the slot plan above. Run weekly. Diff the output against the previous week and post a summary of tier moves in the journal.

## 6. Governance
- Change frequency: labels used in listing groups should change at most weekly for performance tiers, so bidding systems are not chasing a moving structure. Stock labels can change daily if campaigns treat them as exclusions only.
- Cardinality: keep each label under 50 values in practice; never near the 1,000 cap.
- Ownership: commerce-feeds owns the definitions and the pipeline; ad agents own targets and budgets. Any change to a label definition is a journal entry tagged `change` addressed to google-ads and meta-ads, because it moves products between campaigns.
- Before a structural change: snapshot current labels per item, so performance can be compared before and after.
- Approval: label pipelines that move products between campaigns change spend. Draft the change list; the human approves before the supplemental source goes live.

## 7. Worked example

Context: apparel store, Growth tier ($18k per month), contribution margin 40 percent, breakeven ROAS 2.5, AOV $80, 1,800 SKUs, one PMax campaign.

Diagnosis from the product report (last 60 days): 22 percent of SKUs have zero impressions; 41 SKUs take 63 percent of spend; 120 SKUs have 30 or more clicks and zero conversions.

Plan:
1. Ship labels: tier, margin band, price band, stock, season.
2. Hand off to google-ads: split into PMax "heroes and high margin" (tROAS near breakeven times 1.2) and PMax "rest" (tROAS higher), plus a 6-week zombie test campaign with Maximize conversion value and a small budget.
3. Hand off to meta-ads: product sets for `m_high` and `hero` for Advantage+ catalog ads; exclude `low_stock`.
4. Review after 4 weeks: share of SKUs with impressions, spend concentration, blended ROAS and gross profit versus the previous 4 weeks and the same period last year.
5. Log the hypothesis in EXPERIMENTS.md before launch.

## 8. Common mistakes
| Mistake | Consequence | Fix |
|---------|-------------|-----|
| Labels computed from platform ROAS without margin | Pushes budget to low margin best sellers | Use contribution margin or POAS |
| Daily tier churn | Listing groups and learning reset constantly | Weekly refresh with hysteresis |
| Labels in the primary feed set by hand | Stale within weeks | Pipeline into a supplemental source |
| Same product in two PMax campaigns | Internal competition, muddled reporting | One product, one PMax campaign |
| Zombie products simply excluded | Lost long tail and lost learning | Fix data, test exposure, then exclude only proven losers |
| Using labels instead of fixing data | Labels cannot fix a bad title or price | Data first, then segmentation |
