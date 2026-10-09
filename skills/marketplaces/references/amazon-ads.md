# Amazon Ads

> Knowledge as of 2026-10. Amazon Ads ships changes monthly and renames products often (Sponsored Display is now "display ads"; Rufus is now Alexa for Shopping in the US). Check the Amazon Ads "What's new" page and release notes before acting. Cross-marketplace bidding method: [Retail media bidding and structure](retail-media-bidding-and-structure.md).

## 1. Product map (2026)

| Product | Billing | Placement | Targeting | Who can use it |
|---------|---------|-----------|-----------|----------------|
| Sponsored Products (SP) | CPC | Search results, product pages, Alexa for Shopping (Rufus) answers as Sponsored Prompts | Keywords (exact, phrase, broad), products and categories, auto targeting (close, loose, substitutes, complements) | Sellers and vendors; offer must hold the featured offer |
| Sponsored Brands (SB) | CPC or vCPM | Top of search (headline), video in search, Brand Store | Keywords, products, categories | Brand Registry |
| Display ads (formerly Sponsored Display) | CPC or vCPM | On and off Amazon | Contextual (products, categories), audiences (views, purchases, interests) | Brand Registry sellers, vendors; new campaigns via Create campaign > Display [Official page, 2026] |
| Sponsored TV | vCPM | Streaming TV (Prime Video, Fire TV and partners) | Audiences and content | Self service in some markets |
| Amazon DSP | CPM | Amazon and third-party inventory incl. Prime Video, Complete TV partners | Amazon audiences, AMC audiences | Self service or managed; minimums vary |
| Sponsored Prompts (SP and SB prompts) | CPC | Inside Alexa for Shopping conversations | Auto-enrolled from SP and SB campaigns; no prompt level targeting or exclusion | Paid general availability in the US from 2026-03-25 [Secondary, multiple] |

### 2025 to 2026 platform changes that matter

| Date | Change | What to do | Label |
|------|--------|-----------|-------|
| 2025-11-11 to 12 | unBoxed 2025: Ads Agent (AI agent for planning, launching, optimizing, AMC SQL), Creative Agent, unified Campaign Manager joining sponsored ads and DSP, Complete TV, AMC lookback extended from 13 to 25 months | Use Ads Agent suggestions as drafts under the same approval gates | [Official, 2025-11] |
| 2026-01-01 | View attribution moved to "shopping-signal enhanced last-touch" for view-based (vCPM) ads; "all views" metrics keep the old method for comparison | Compare SB vCPM, display and DSP year over year only on the same method | [Secondary, multiple, 2026-01] |
| 2026-02-02 | Amazon Ads MCP Server open beta (closed beta from 2025-11) | Read only use first; writes behind the guard hook | [Secondary, 2026-02] |
| 2026-03-25 | Sponsored Prompts in Rufus paid (CPC) GA in US | Expect new spend in existing SP and SB campaigns; reporting is blended | [Secondary, 2026-03] |
| 2026-05-13 | Rufus renamed Alexa for Shopping in the US | Update naming in reports | [Reported, 2026-10] |
| 2026 | Sponsored Display renamed display ads; existing campaigns continue | New display campaigns via Display flow | [Official page, 2026] |
| Through 2026-12-31 | AMC first-party paid features (Amazon Shopping Insights, Retail Purchases and others) free to query | Opt out before 2027 if not needed or budget for fees | [Secondary citing Official, 2026] |

## 2. Attribution windows and metrics

| Product | Seller attribution | Vendor attribution | Note |
|---------|-------------------|--------------------|------|
| Sponsored Products | 7 day click; advertised and other SKUs | 14 day click | No view-through [Secondary, 2026] |
| Sponsored Brands | 14 day click (plus views for vCPM campaigns) | 14 day | Brand halo included |
| Display ads | 14 day click and views (vCPM) | 14 day | New view model from 2026-01-01 |
| DSP | 14 day default, configurable | Same | AMC for custom windows |

Key metrics: ACoS (spend / attributed sales), ROAS (attributed sales / spend), TACoS (spend / total sales), New-to-brand (NTB) orders and sales, Top of search impression share, Search term impression share, Detail page view rate, Branded searches (Sponsored Brands and display).

## 3. Account structure (Amazon)

```
Portfolio per brand or product line (budget caps per portfolio)
  SP | Brand defense | Exact | per hero product group          (target ACoS: low; impression share goal)
  SP | Category | Exact | top 20 category terms per product    (target ACoS: at or below breakeven)
  SP | Category | Phrase and Broad | harvest                    (target ACoS: breakeven)
  SP | Competitor | Product targeting (ASINs) and competitor brand keywords where allowed (target ACoS: breakeven plus NTB goal)
  SP | Auto | close, loose, substitutes, complements split by ad group (discovery, low bids)
  SP | Defensive product targeting | own ASINs on own detail pages (cross-sell, block competitors)
  SB | Brand | Store or product collection | brand terms
  SB | Category video | category terms (NTB)
  Display | Remarketing views and purchases | own ASINs
  Display | Contextual | competitor and complementary products
```

Naming convention: `MP|AMZ-DE|SP|CAT|EXACT|<product-group>|<yyyymm>`. Keep it identical across marketplaces so reports roll up.

Rules:
- One product group (same price band and margin) per campaign so one ACoS target fits.
- Separate exact match campaigns for top terms so budgets and bids are controllable.
- Negatives: add exact term negatives in discovery campaigns for terms that moved to exact campaigns (prevents internal competition).
- Placement modifiers: Top of search (first page), Rest of search, Product pages. Set modifiers from placement report CVR, not by default.
- Bidding strategies: Dynamic bids down only (safest default for new campaigns), Dynamic up and down (for proven exact terms with good CVR), Fixed bids (tests). Amazon can raise bids up to 100% for top of search under up and down [Official, prior knowledge].
- Rule based bidding and budget rules (Amazon native) can raise bids toward a ROAS goal or budgets on events; treat as G3 automation and set caps.

## 4. Launch play for a new ASIN (private label or new brand product)

| Week | Actions | Targets |
|------|---------|---------|
| 0 (before live) | Listing pack complete, 7 or more images incl. video, A+, backend terms, Vine enrolled (if Brand Registry), price set within corridor, stock for 10 to 12 weeks | Listing quality checklist passes |
| 1 to 2 | SP auto (4 ad groups), SP exact on 10 to 20 high relevance terms, SP product targeting on 10 to 20 competitor ASINs with weaker offers; bids at suggested low end; Dynamic down only | Impressions and clicks; CVR baseline; first Vine reviews |
| 3 to 4 | Harvest search terms (2 or more orders) into exact; negate zero-order terms after 1.5x target CPA spend; add SB once 5 or more ratings | CVR at or above category baseline; ACoS can exceed breakeven within launch budget |
| 5 to 8 | Raise bids on terms with organic rank movement; add display remarketing; review placement CVR | TACoS glidepath from launch level toward target |
| 9 to 12 | Cut terms that do not reach breakeven; shift budget to terms where organic rank holds when ads are reduced | TACoS at target band; organic share rising |

Launch budget is an investment: write the planned TACoS glidepath (for example 35% in month 1, 25% month 2, 15% month 3) and the maximum loss in `DECISIONS.md` before starting. Vendor benchmarks for TACoS at launch (25% to 40%) are single-source [Unverified].

## 5. Brand defense

Arguments for: competitors bid on your brand terms; Sponsored Brands at top of search protect the shelf; brand terms are cheap. Arguments against: brand searchers would find you anyway; cannibalization of organic. Resolve with data:

1. Pull Search Query Performance for brand terms: your brand's share of clicks and purchases.
2. Run a holdout: pause SP brand exact on one marketplace or product group for 14 days while keeping SB, compare total brand term orders vs a control group and the prior period.
3. Keep defense where competitors take more than 10% of clicks on brand terms when you pause, or where total brand orders fall more than the ad spend saved.
4. Product targeting on own ASINs (defensive) blocks competitor ads on your detail pages; test with the same holdout logic.

## 6. Sponsored Prompts and Alexa for Shopping (Rufus)

- How it works: SP and SB campaigns are auto-enrolled; Amazon writes the prompt copy from listing and Brand Store content; billing is CPC; no prompt-level targeting, bidding or exclusion as of research; impressions are blended into standard reports [Secondary, multiple, 2026].
- What you control: listing content quality (answers to common questions in bullets and A+), Q&A, reviews, Brand Store depth, and campaign bids and budgets.
- Optimize for AI shopping answers: state use cases, compatibility, materials, dimensions, who it is for and not for, in plain language in bullets and A+; keep facts consistent across listing, A+ and Brand Store. See [Listing optimization](listing-optimization.md) section 7.
- Measurement: watch CVR and CPC changes in SP after 2026-03-25 by search term type (question-like long tail vs head terms). Do not credit Sponsored Prompts separately until Amazon reports them separately.

## 7. Display ads and DSP basics

| Use | Product | Setup | KPI |
|-----|---------|-------|-----|
| Retarget product page viewers who did not buy | Display ads, views remarketing 7 to 30 days | Own ASINs, exclude purchasers | ROAS, NTB |
| Cross-sell to purchasers of complementary products | Display ads, purchases remarketing | Complement ASINs | ROAS |
| Steal share on competitor pages | Display contextual (product targeting) | Competitor ASINs with weaker ratings or higher price | NTB, CVR |
| Upper funnel with Amazon audiences | DSP | In-market, lifestyle, AMC audiences | Reach, detail page view rate, branded search lift, NTB |
| Streaming TV | Sponsored TV, DSP Prime Video | Audiences | Branded search lift, AMC path to purchase |

DSP is worth testing when Amazon sales exceed roughly USD 100k per month in a category with repeat purchase or high consideration [Practitioner consensus]. Require an AMC or lift based read (see [Measurement and halo](measurement-and-halo.md)); never judge DSP on last-touch ROAS alone.

## 8. Weekly Amazon Ads checklist

| Check | Report | Action |
|-------|--------|--------|
| Spend vs plan and budget caps | Campaign report, portfolios | Fix pacing; budget out before 18:00 local on winners means raise or re-split |
| ACoS by intent vs targets | Campaign report grouped by name tag | Bid changes in steps of 10% to 20% |
| TACoS trend | Ads spend / total sales from Business Reports | If TACoS rises with flat total sales, cut low intent spend |
| Search term harvest | Search term report (60 days) | Exact promotion, negatives |
| Placement CVR | Placement report | Adjust top of search modifier |
| Out of stock or no featured offer ASINs | Business Reports, inventory | Pause ads on affected ASINs |
| Impression share on top terms | Search term impression share | Bid up where CVR is above average and IS below 30% |
| New to brand | NTB report | Keep budget on NTB rich campaigns if CM3 allows |
| Alexa for Shopping effects | SP CPC and CVR trend since 2026-03-25 | Note anomalies in journal |

## 9. Common expensive mistakes

- One campaign for everything with an account-wide ACoS target: hides losers inside winners.
- Running ads on ASINs without the featured offer or out of stock (spend wasted or ads stop and rank drops).
- Judging SP on ACoS while TACoS climbs: ads buying sales that organic would have delivered.
- Default Dynamic up and down on every campaign: Amazon can double bids on top of search.
- No negatives in auto campaigns after months of data.
- Bidding on competitor brand terms with copy or claims that suggest affiliation (policy and trademark risk); keep competitor targeting on product targeting where unsure.
- Comparing 2026 view-attributed ROAS with 2025 without the "all views" metrics.
- Letting Ads Agent or rule-based bidding change bids without caps or approval.
