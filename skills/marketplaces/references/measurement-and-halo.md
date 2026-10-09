# Measurement and Halo

> Knowledge as of 2026-10. Marketplace measurement is mostly inside walled gardens. Use their reports for operations, and use experiments for investment decisions. Deep measurement design (geo tests, MMM) is owned by `measurement`; this module covers what the marketplaces agent reads and how it frames tests.

## 1. Data sources by marketplace

| Source | What | Access | Cadence |
|--------|------|--------|---------|
| Amazon Business Reports | Sessions, page views, units, unit session percentage, featured offer % by child ASIN | Seller Central, SP-API Reports (GET_SALES_AND_TRAFFIC_REPORT) | Daily data, weekly review |
| Amazon Brand Analytics | Search Query Performance (brand and ASIN funnel per query: impressions, clicks, cart adds, purchases and your share), Top Search Terms, Search Catalog Performance, Market Basket, Repeat Purchase, Demographics | Brand Registry; SP-API Brand Analytics reports | Weekly |
| Amazon Ads reports | Campaign, search term, placement, targeting, purchased product, NTB | Console, Ads API, Ads MCP server (open beta) | Daily |
| Amazon Marketing Cloud (AMC) | Event level clean room: paths to purchase, NTB, overlap, frequency, audiences | Free for eligible advertisers; 1P paid features free to query through 2026-12-31; lookback 25 months (from 13) | Monthly analyses |
| Amazon Attribution | Off-Amazon traffic (Google, Meta, email, influencers) to Amazon: clicks, detail page views, add to carts, purchases, brand halo | Brand Registry sellers and vendors | Weekly |
| Vendor Retail Analytics | Sales, traffic, inventory, net PPM for 1P | Vendor Central | Weekly |
| bol | Sales, offer insights, performance, Sponsored Products reports (14 day click window) | Seller account, Retailer API v10, advertising reports | Weekly |
| Trendyol, Hepsiburada | Sales, product views, conversion, ad reports, buybox status | Seller panels, APIs, integrators | Weekly |
| External | Keepa price and rank history, rank trackers, Search Console (branded queries), Google Trends | Tools | Monthly |

State the source and date range in every output. Marketplace reports often restate recent days; avoid reading the last 2 to 3 days of ad data as final (attribution lag up to 7 to 14 days).

## 2. Attribution rules to remember

| Item | Rule | Label |
|------|------|-------|
| Amazon Sponsored Products | 7 day click for sellers, 14 day click for vendors; no views | [Secondary, 2026] |
| Amazon SB, display, DSP (view based) | From 2026-01-01, shopping-signal enhanced last-touch view attribution; "all views" metrics retain old method | [Secondary, multiple, 2026-01] |
| Halo sales | Amazon credits other products of the same brand bought after an ad click ("brand halo" in Amazon Attribution and SB) | [Official, prior knowledge] |
| bol Sponsored Products | Conversions within 14 days of a click | [Official, bol help] |
| Turkish marketplaces | Panel attribution windows not public | [Unverified] |

Never compare ROAS across marketplaces without aligning windows and VAT basis.

## 3. Brand Analytics: Search Query Performance (SQP) workflow

1. Pull SQP (brand view) weekly for the top 100 queries by your purchases and top 50 category queries.
2. For each query compute: your impression share, click share, cart add share, purchase share.
3. Funnel diagnosis:

| Pattern | Likely cause | Action |
|---------|-------------|--------|
| Low impression share, good click and purchase share | Not visible enough | Raise bids or improve rank on that query |
| Good impression share, low click share | Main image, price, rating, title weak vs competitors | Listing and price review |
| Good click share, low cart add share | Detail page does not convince (images, bullets, A+, reviews) | Listing optimization, review themes |
| Good cart add share, low purchase share | Price, delivery promise, competitor offers in cart | Price and delivery check |

4. Feed the query list into ads (exact targets) and listing keyword tiers.

## 4. AMC basics (when and what)

Use AMC when Amazon ad spend is meaningful (rule of thumb from about USD 20k to 30k per month across ad types [Practitioner consensus]) or when DSP or Sponsored TV run.

| Question | AMC analysis | Decision |
|----------|-------------|----------|
| Does upper funnel (SB video, display, DSP, Sponsored TV) drive later SP and organic purchases? | Path to purchase, overlap analysis (exposed to both vs one) | Budget split by funnel stage |
| Which campaigns bring new-to-brand customers who repeat? | NTB and repeat purchase by first touch campaign | Shift budget to campaigns with high NTB repeat value |
| How many touches before purchase, optimal frequency? | Frequency distribution vs conversion | Frequency caps in DSP |
| Time to conversion | Time lag analysis | Attribution expectations, test durations |
| Audiences | Cart abandoners, high LTV lookalikes, lapsed buyers (via AMC audiences in display, DSP, and reportedly SP) | Activate with caps; G3 for spend |

Ads Agent can write AMC SQL from natural language (beta since unBoxed 2025) [Official, 2025-11]. Review every generated query: check date ranges, filters, aggregation thresholds and that outputs are aggregated (AMC enforces privacy thresholds).

Opt-out reminder: if 1P paid features are enabled for free in 2026, decide before 2026-12-31 whether to keep them into 2027 at a fee [Secondary citing Official, 2026].

## 5. Halo effects

### 5.1 Types
| Halo | Description | How to see it |
|------|-------------|---------------|
| Ads to organic (same marketplace) | Ads raise sales velocity, which lifts organic rank and sales | TACoS 2 x 2 ([Retail media bidding](retail-media-bidding-and-structure.md) section 3), rank tracking |
| Brand halo (same marketplace) | Ad for product A leads to purchase of product B | Brand halo metrics in SB and Attribution |
| Off-marketplace to marketplace | Google, Meta, TikTok, TV and PR drive Amazon or bol searches and sales | Amazon Attribution tags, branded search volume in SQP, geo tests |
| Marketplace to DTC and retail | Amazon visibility drives Google brand searches and DTC visits, or retail sales | Branded search in Search Console, DTC direct traffic, geo or time tests |
| Marketplace cannibalization of DTC | Customers who would have bought on DTC buy on marketplace | Holdout or price corridor tests |

### 5.2 Brand Referral Bonus and Amazon Attribution
- Brand Referral Bonus credits about 10% on average (category dependent) of sales driven by external traffic tagged with Amazon Attribution, within 14 days of the click; credited against fees [Secondary, 2026].
- Every external link to Amazon (Google, Meta, TikTok, email, influencers, PR) must use a unique Attribution tag per channel and campaign; untagged links forfeit the bonus.
- Effective cost of external traffic to Amazon = media cost minus bonus credit. Include it when `google-ads` or `meta-ads` evaluate "send traffic to Amazon" campaigns.

### 5.3 Halo test designs

| Design | When | How | Read |
|--------|------|-----|------|
| Geo holdout (DTC and marketplace) | Off-marketplace media in several regions | Run media in test regions, hold out control regions; compare marketplace sales by region (Amazon reports by region are limited; use AMC or vendor geo data where available) | With `measurement` |
| Time based on and off | Single market, limited regions | 2 to 4 week alternating periods, with seasonality control (prior year, control SKUs) | Pre and post with controls |
| Brand term pause | Brand defense value | Pause brand SP in one marketplace or for one product group for 14 days | Total brand orders vs control |
| Marketplace listing presence test | Cannibalization of DTC | Not usually feasible (delisting costs rank); prefer price corridor tests or assortment split tests | Contribution across channels |
| AMC overlap | Upper funnel on Amazon | Compare conversion of users exposed to DSP plus SP vs SP only (not causal; use for direction) | Directional |

Rules: write the test in `EXPERIMENTS.md` before starting; define the primary metric (total brand contribution across channels where possible); minimum duration 2 weeks plus attribution lag; never declare a halo from correlation alone.

## 6. Marketplace in company level measurement

- Report marketplace sales and contribution next to DTC in the weekly review so MER (total revenue / total marketing) includes marketplaces [handoff to `growth-orchestrator`].
- MMM: include marketplace sales as a KPI or as a separate model output; include retail media spend as a channel [handoff to `measurement`].
- AI assistants: track whether Alexa for Shopping answers recommend your products for key questions (monthly prompt check in [Listing optimization](listing-optimization.md) section 8); coordinate with `ai-search-optimization` for off-Amazon AI answers that cite Amazon listings.

## 7. Monthly marketplace report template

```
# Marketplace monthly report | <month> | Data sources and date ranges
## Summary (3 to 5 bullets with contribution impact)
## By marketplace: sales, units, CM2, ad spend, TACoS, CM3, featured offer %, in-stock %, rating, account health
## Organic share: SQP top queries (impression, click, purchase share), rank on priority keywords
## Ads: by intent (spend, ACoS vs target, NTB), harvest, tests
## Halo and external traffic: Attribution results, Brand Referral Bonus credits, branded search trends
## Fees and costs changes this month
## Incidents and account health
## Next month priorities and change requests
## Handoffs requested
```

## 8. Amazon Attribution tag convention

```
Tag name: <channel>_<campaign>_<adgroup or creative>_<marketplace>_<yyyymm>
Examples: google_pmax-brand_hero-serum_de_202610 | meta_reels-launch_ugc03_de_202610 | email_newsletter_oct_de_202610
Rules: one tag per channel and campaign at minimum; one per creative when creative tests matter;
       never reuse tags across marketplaces; record every tag in ads-master/data/attribution_tags.csv (tag, channel, campaign, landing ASIN or Store page, start date)
```

## 9. AMC example: new-to-brand path (illustrative SQL; adapt to the current AMC schema)

```sql
-- Share of new-to-brand purchasers who saw a Sponsored Brands or display impression before their first SP click (last 90 days)
WITH ntb AS (
  SELECT user_id, MIN(conversion_event_dt) AS first_purchase
  FROM amazon_attributed_events_by_conversion_time
  WHERE new_to_brand = TRUE
  GROUP BY user_id
), upper AS (
  SELECT DISTINCT user_id
  FROM dsp_impressions_and_sponsored_ads_traffic  -- replace with the current AMC tables for SB, display and DSP exposure
  WHERE ad_product_type IN ('sponsored_brands', 'sponsored_display')
)
SELECT
  COUNT(DISTINCT ntb.user_id) AS ntb_users,
  COUNT(DISTINCT CASE WHEN upper.user_id IS NOT NULL THEN ntb.user_id END) AS ntb_users_with_upper_funnel_exposure
FROM ntb LEFT JOIN upper ON ntb.user_id = upper.user_id
```

Table and column names differ by AMC version and region. Use the AMC instructional queries library or Ads Agent to generate the current version, then check it line by line. AMC only returns aggregated results above privacy thresholds; never try to extract user level data.
