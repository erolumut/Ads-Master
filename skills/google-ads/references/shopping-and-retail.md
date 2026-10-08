# Shopping, Retail and Local

> Knowledge as of 2026-10. The feed itself (titles, attributes, Merchant Center diagnostics, Merchant API migration, supplemental feeds) belongs to the commerce-feeds agent. This module covers the Google Ads side: campaign structure, product segmentation, bidding by margin, Merchant Center settings that change ad delivery, and local and store formats.

## 1. Shopping inventory in 2026

| Surface | Served by | Notes |
|---|---|---|
| Shopping ads on Search results and the Shopping tab | Standard Shopping, PMax with feed, AI Max for Shopping (beta) | Core ecommerce revenue |
| Shopping ads in AI Overviews | Shopping and PMax campaigns | English, 12 countries for AI Overviews ads as of 2025-12 [Official via trade press, 2025-12] |
| Shopping in AI Mode | PMax, Shopping, AI Max eligible campaigns | US test; Direct Offers pilot for select US advertisers [Official, 2026] |
| AI-powered Shopping ads (Gemini explains why a product fits the query) | Announced at GML 2026, rolling out in the US over the following months | [Official, 2026-05] |
| YouTube Shopping ads, Demand Gen product ads | Demand Gen, PMax, Video | UCP-powered checkout extending to Shopping ads on YouTube and Demand Gen Direct Offers [Official, 2026-05] |
| Local inventory ads (LIA) | Standard Shopping, PMax with local feed | LIA enabled by default on Standard Shopping campaigns from 2026-08-31 [Practitioner report, 2026-08, verify] |
| Free listings | Merchant Center | Not paid, but affects the product mix seen in Shopping |

Agentic commerce building blocks announced by Google: Universal Commerce Protocol (UCP), Agent Payments Protocol (AP2) and Universal Cart, with UCP expanding to Canada and Australia and then the UK [Official, 2026-05]. Merchant readiness for agentic checkout belongs to commerce-feeds.

## 2. Standard Shopping vs PMax

| Factor | Standard Shopping | PMax with feed |
|---|---|---|
| Inventory | Shopping only | All channels |
| Query control | Negative keywords, priorities | Negatives (up to 10,000), brand exclusions, search terms report |
| Bidding | Manual CPC, Max clicks, tROAS, Max conversion value | Max conversion value with optional tROAS, NCA goals |
| Data needs | Low | Higher (30+ conversions a month) |
| Best for | Low data, new products, precise control, testing a product set | Scale, cross-channel, NCA |
| Priority | Since 2024 PMax does not automatically win over Standard Shopping; Ad Rank decides [Official, 2024] | |

Use Standard Shopping deliberately: a catch-all for zombie products, a low data market, a margin band that needs a manual approach, or a control cell in a test.

## 3. Product segmentation (the profit system)

Ask commerce-feeds to populate custom labels. Recommended label schema:

| Label | Values | Source | Refresh |
|---|---|---|---|
| custom_label_0 margin band | high (above 50%), mid (30% to 50%), low (under 30%) | ERP or Shopify cost data | Weekly |
| custom_label_1 performance tier | hero, sidekick, villain, zombie | Google Ads product report, 30 to 90 days | Weekly |
| custom_label_2 price band | under 25, 25 to 100, 100 to 300, over 300 (account currency) | Feed price | Daily |
| custom_label_3 seasonality or promo | evergreen, seasonal, promo_YYYYMM, clearance | Merchandising | As needed |
| custom_label_4 stock depth or lifecycle | new, core, low_stock, end_of_life | Inventory | Daily |

Performance tiers (define per account, these thresholds are a starting point):
| Tier | Definition (last 30 days) | Action |
|---|---|---|
| Hero | ROAS at or above target and at least 5 conversions | Protect budget, own campaign at Scale tier, consider looser target to grow |
| Sidekick | Conversions present, ROAS between 0.7x and 1x target | Keep in main campaign, improve feed and price competitiveness |
| Villain | Cost above 2x target CPA (or above average order value) with zero conversions | Exclude or move to low target campaign after checking price and landing page |
| Zombie | Under 100 impressions in 30 days | Separate campaign with low target or Standard Shopping to give exposure; check feed quality first |

## 4. Bidding by margin

Breakeven ROAS = 1 / contribution margin. With a 40% contribution margin, breakeven ROAS = 2.5 (250%).
Target ROAS = breakeven ROAS x (1 + required profit buffer), or derived from target POAS.

Worked example:
- Product set A: AOV 80, contribution margin 50%: breakeven ROAS 200%. Target 250% for a 20% buffer.
- Product set B: AOV 120, contribution margin 25%: breakeven ROAS 400%. Target 480%.
- One campaign with a single tROAS of 350% overspends on B and underspends on A. Split by custom_label_0 into two campaigns with their own targets, or pass profit as the conversion value (POAS) so one target works across products.

Profit-based values: when the measurement agent can pass gross profit or contribution as the conversion value (server-side or conversion value rules), a single tROAS based on profit works across the catalog. Hand off implementation to measurement.

New customer acquisition: set "Bid higher for new customers" with a new customer value equal to the incremental lifetime profit of a new customer (for example, 12-month contribution of a new customer minus the first order contribution). Requires a customer list or a conversion-based new customer definition.

## 5. Merchant Center settings that change ad delivery (Google Ads side)

Coordinate with commerce-feeds; check these during an audit:
| Item | Why it matters for ads |
|---|---|
| Account status and policy issues (misrepresentation, unsupported shopping content) | Suspended Merchant Center stops all Shopping and feed-based PMax |
| Product disapprovals and limited performance | Directly reduces eligible spend |
| Price competitiveness and benchmarks | Price is a top driver of Shopping CTR and conversion rate |
| Shipping and returns settings | Shown in ads, affects CTR and eligibility for annotations |
| Product ratings and store ratings | Stars in ads lift CTR |
| Promotions | Promotion annotations; Direct Offers in AI Mode for pilot advertisers |
| Loyalty programs and member pricing | Loyalty annotations; Loyalty Customer Match expanded to AI Mode and Gemini apps in 14 countries [Unverified, trade press 2026-10] |
| Local inventory feed | LIA eligibility |
| Merchant Center linking to Google Ads | Must be linked and accepted |
| Feed labels and country targeting | Determine which products serve in which markets |
| Content API for Shopping to Merchant API migration | API based feed tools must use the Merchant API; Content API retirement planned for 2026 [Unverified exact date, commerce-feeds owns] |

Ask Advisor began rolling out to selected Merchant Center accounts in July 2026 [Practitioner report, 2026-07].

## 6. Shopping query management

- Shopping and PMax do not use keywords. Control comes from feed text (titles, descriptions, product type, Google product category), negatives, brand exclusions and listing groups.
- Weekly: review search terms for Shopping and PMax, add negatives for irrelevant product types and low intent modifiers (free, diy, used if you sell new).
- Brand vs non-brand in Shopping: classic approach uses campaign priority (Standard Shopping high, medium, low with negatives) to separate brand and generic queries. With PMax, use brand exclusions and a separate brand Search campaign.
- Competitor brand queries in Shopping: decide intentionally. If you resell brands, brand queries for those brands are your core traffic. Do not exclude brands you sell.

## 7. AI Max for Shopping (closed beta from 2026-04-30)

- Uses Merchant Center product data to answer longer, conversational queries. [Official, 2026-04]
- If invited: test against the current setup with an experiment, track query length and new query share, compare ROAS and new customer share.
- Feed descriptions and attributes become more important for conversational matching. Hand off feed enrichment to commerce-feeds.

## 8. Local and store formats

| Format | Use | Requirements |
|---|---|---|
| PMax with store goals | Retail with physical stores: store visits, store sales, local actions | Business Profile linked, location assets, store visit eligibility |
| Local inventory ads | Products available in nearby stores | Local inventory feed, store pickup or in-store availability |
| Location assets and affiliate location assets | Show address and distance, required for Maps placements | Business Profile, or chain selection for retailers selling through stores |
| Demand Gen Maps channel | Promoted pins in Maps (Browse, Directions, Place details) | Location asset required, beta [Official, 2026] |
| Local Services Ads | Pay per lead for home services, professional services | Google Screened or Google Guaranteed eligibility; moving into the Google Ads interface for select US advertisers from 2026-08 [Official, 2026-08, verify] |
| Book button (Reserve with Google) | Appointments from Search and PMax ads | Reserve with Google partner integration, on by default for eligible merchants, opt-out in Google Ads, not available for healthcare [Unverified, trade press 2026-09] |
| Call ads and call assets | Phone leads | Call reporting, call conversion minimum duration |
| Automated promotions | Offers extracted from your site and added to eligible Search and PMax campaigns | On by default from 2026-10-12 in eligible accounts; turn off in account-level automated assets if offers are not valid [Unverified, trade press 2026-10] |

Local rules:
1. Location option Presence. Radius matched to the real service or delivery area.
2. Business Profile accurate (hours, categories, phone). Wrong hours cost calls.
3. Call conversions counted only above a duration that predicts a real lead (check against CRM).
4. Store visits are modeled conversions: use them for direction, validate with store sales data or geo tests.
5. Multi-location: location groups in PMax, per-location budgets only when owners need them.

## 9. Retail calendar

| Period | Action |
|---|---|
| 8 weeks before peak (for example Black Friday) | Feed QA, promotions loaded, creative ready, budget plan approved, seasonality adjustment drafted |
| 2 weeks before | Raise budgets gradually, loosen targets 10% to 20% for volume if margin allows |
| Peak days | Seasonality adjustment for 1 to 7 days of expected conversion rate lift (do not use for longer events); monitor hourly pacing; campaign total budgets for fixed flights [Official, 2026-01 open beta] |
| After peak | Remove seasonality adjustment, restore targets, apply data exclusion only for tracking outages, not for normal post-sale dips |

## 10. Diagnostics

| Symptom | Checks | Fixes |
|---|---|---|
| Shopping impressions dropped | Merchant Center diagnostics, disapprovals, price changes, budget, target | Fix feed (commerce-feeds), restore budget, loosen target |
| ROAS dropped with stable traffic | Price competitiveness, stock, shipping changes, landing page | Price benchmarks, stock availability, CRO handoff |
| Spend concentrated on few products | Products report | Split by performance tier, separate targets |
| New products never get impressions | Zombie problem | Separate new product campaign with lower target or Standard Shopping |
| High ROAS but low new customer share | Remarketing and brand dominated | NCA goal, brand exclusions, customer list exclusions |
