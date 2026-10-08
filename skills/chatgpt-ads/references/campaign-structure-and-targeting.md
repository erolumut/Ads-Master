# Campaign Structure and Targeting

> Knowledge as of 2026-10. Sources: OpenAI Help Center (Quickstart 20001224, Launch Campaigns 20001209, Create Campaigns 20001210, Create Ad Groups 20001211, Write Context Hints 20001521, Product Feeds 20001268, Edit Campaigns 20001215), developer docs (Targeting, Location Targeting, Platform Targeting, Custom Audiences, Product Feeds), community API notes (faborsky/chatgpt-ads-app, 2026-09). Re-verify live.

## 1. Hierarchy

| Level | Holds | Immutable after creation |
|-------|-------|--------------------------|
| Campaign | Name, objective (Views, Clicks, Conversions), billing for conversions (oCPC or oCPM), conversion event, budget (daily or campaign total), start and end dates, target countries and locations, platforms, custom audiences, mode (standard or product feed) and linked feed | Objective, billing model, conversion event, mode, feed, budget type (campaign total can switch to daily once; daily cannot switch back) |
| Ad group | Name, context hints, bid strategy and max bid, billing event, product set filters (feed campaigns), audience bid multipliers (fixed bid only) | Billing event follows the objective |
| Ad | Creative: title, description, image, landing page URL (chat card) or product ad template (feed) | Any creative edit triggers a new review |

Account limits: 5,000 campaigns, 5,000 ad groups and 5,000 ads per ad account [Official, 2026-09]. Context hints: up to 2,000 per ad group [Official, 2026-09].

## 2. Structure rules

1. **Campaign per market and objective.** Separate countries when budgets, currency logic or performance differ. Separate objectives always (they cannot share a campaign).
2. **Campaign per business goal.** OpenAI advises separating by objective, region or product category, with clear, consistent naming [Official, 2026-09].
3. **3 to 8 ad groups per campaign** [Practitioner consensus]. Each ad group is one product, service, theme or customer need. OpenAI: keep each ad group focused on one category, theme or intent; do not combine unrelated products [Official, 2026-09].
4. **Split ad groups when messaging or landing pages must differ** [Official, 2026-09].
5. **3 to 5 ads per ad group**, each a different angle (price, speed, outcome, proof, use case). OpenAI: create many distinct variations so the system has more chances to match [Official, 2026-09].
6. **Do not over fragment.** Delivery concentrates: in one test the two largest ad groups took about half of impressions and one or two creatives took most delivery inside each group [Study, 2026-08]. Fewer, well defined groups learn faster.

### Naming convention
`<market>_<objective>_<theme>_<yyyymm>` for campaigns, `<intent>_<hintstyle>_<lp>` for ad groups, `<angle>_<variant>` for ads.
Examples: `US_CPC_RunningShoes_202610`, `beginner-5k_S_lp-beginner-collection`, `price_v1`.
Put the hint style in the ad group name so reports can compare styles (P, S, C, K below).

## 3. Context hints (the main relevance lever)

What they are [Official, 2026-09]:
- Extra details about your business, product or service that help ChatGPT's systems understand when your ads may be relevant.
- Set at the ad group level. Entered as a list (bulk upload uses a JSON array like `["hint 1", "hint 2"]`).
- Not exact match keywords, not targeting rules, not delivery instructions. They do not enforce geography, schedules or exclusions, do not exclude people or conversations, and do not guarantee delivery. The underlying need can match without the exact wording.
- Updating hints replaces the whole list (API and bulk upload); send the full list every time.

How OpenAI says to write them [Official, 2026-09]:
- Cover one or more angles: **What** (features, services, pricing, availability, service area), **Who** (needs, preferences, circumstances), **When** (situations or decisions where the offer is useful).
- One idea per hint, written as a natural phrase. Avoid lists of disconnected keywords.
- Qualities: additional (adds context beyond the ad and landing page), specific, relevant, accurate (update when pricing, promotions, availability or service areas change).
- Base hints on best fit customers and situations that lead to strong business results.

OpenAI examples (illustrative) [Official, 2026-09]:
| Business | Hint |
|----------|------|
| Running shoes | Cushioned everyday running shoes for beginners training for their first 5K |
| Local plumber | After-hours residential plumbing in [city], with an $89 service-call fee for urgent repairs |
| Accounting software | Bookkeeping software for growing retailers that need to reconcile online and in-store sales |

Not a hint: "Show this ad only to people in Chicago" (a delivery instruction). Hint version: "Residential plumbing services available in Chicago" [Official, 2026-09].

### Hint styles to test [Practitioner consensus]
| Style | Code | Example (running shoes) | Notes |
|-------|------|------------------------|-------|
| Product description | P | Lightweight trail running shoes with rock plates and grippy lugs for muddy terrain | Closest to OpenAI's examples; safe default |
| Situation or need | S | Runners getting blisters on long downhill trail runs who need a wider toe box | Strong for problem aware users |
| Conversation or question | C | what shoes should I wear for my first trail half marathon | Mirrors how users type |
| Keyword or topic | K | trail running shoes, wide toe box, rock plate | Contradicts OpenAI's guidance, yet one public A/B test reported K beat full questions on impressions, CTR and CPC [Unverified] |

Recommended first test: same ads, one ad group per style (P, S, C, K), separate `utm_content` per group, judge after at least 7 days and 100 clicks per group [Practitioner consensus].

### Hint construction procedure
1. Collect raw demand language: Google Ads search terms (top converting non-brand), Search Console queries, on-site search, sales call notes, support tickets, reviews, competitor comparison pages, and prompts from the ai-search-optimization prompt set.
2. List 8 to 15 situations per ad group in What, Who, When form.
3. Write each in the chosen style with 3 to 5 phrasings. Target 20 to 60 hints per ad group [Practitioner consensus]; the hard limit is 2,000 [Official, 2026-09].
4. Remove any hint that describes an audience label only ("millennials", "small businesses") without a need.
5. Remove sensitive or prohibited contexts (health conditions, political topics, emotional distress). Ads will not serve there anyway and such hints can hurt review.
6. Check accuracy against the landing page (price, service area, availability).
7. Save the hint sheet in `ads-master/outputs/chatgpt-ads/` and version it; bulk edits replace, not merge.

### Hint templates by business model
| Model | What | Who | When |
|-------|------|-----|------|
| Ecommerce | `<product type> with <key feature> at <price band>` | `<user type> who needs <benefit>` | `choosing <product> for <occasion or use>` |
| Lead gen | `<service> in <area> with <price or guarantee>` | `<homeowner or business> dealing with <problem>` | `getting quotes for <service> before <deadline or season>` |
| B2B SaaS | `<software category> that <does job> for <company type>` | `<role> at <company size> struggling with <pain>` | `replacing spreadsheets for <process>` or `evaluating <category> tools` |
| Local services | `<service> available in <city or area> with <hours or fee>` | `<customer> needing <urgent or planned> help` | `after hours`, `same day`, `before moving` |
| App | `<app type> that helps <user> <outcome>` | `<user> who wants <habit or goal>` | `starting <goal> this month` |
| Travel and hotels | `<property type> in <destination> near <landmark> from <price>` | `<traveler type> planning <trip type>` | `booking <season> trip`, `comparing areas to stay` |

## 4. Geographic targeting

| Rule | Detail | Label |
|------|--------|-------|
| Required | Target countries are required at campaign level | [Official, 2026-09] |
| Sub-national | States or regions, cities, markets (DMA) and postal codes where supported by country | [Official, 2026-09] |
| Lists | Up to 2,500 location IDs in inclusion and exclusion lists; IDs from the geo lookup endpoint | [Official, 2026-09] |
| Exclusions | `excluded_locations` supported | [Official, 2026-09] |
| Product feed campaigns | Country level targeting and exclusions only (new campaigns) | [Official, 2026-09] |
| Home country limit | New self-serve accounts may be limited to their home country until verification and home country spend | [Official, 2026-09] |
| Replace semantics | Geo and audience updates replace existing criteria; read first and resend everything | [Official, 2026-09] |
| Valid code is not availability | An ISO code being valid does not mean that market is available | [Official, 2026-09] |

Use sub-national targeting for local businesses and for geo holdout tests (US DMAs or states as test and control cells).

## 5. Platform targeting

Values: iOS app, Android app, web (ChatGPT web on desktop and mobile). Help Center and community notes list granular web options: Desktop web, iOS web, Android web (from about 2026-09-10) [Official, 2026-09] and [Unverified] (date). A browser visit from an iPhone counts as web, not the iOS app [Official, 2026-09]. Omitting platforms at creation means all platforms.

When to split platforms:
- App advertisers: run `ios_app` and `android_app` campaigns separately from web to align with app store destinations and MMP links.
- Desktop heavy B2B: test desktop web separately if the conversion path is long.
- Otherwise leave platforms open until segment data (Insights `segments[]=platform` or `device`) shows a gap of 30% or more in CPA.

## 6. Custom audiences

| Rule | Detail | Label |
|------|--------|-------|
| Uses | Include, exclude, or bid multiplier (fixed bid only) | [Official, 2026-09] |
| Identifiers | Email, phone, SHA-256 hashed email and phone, GAID; UTF-8 CSV with header, up to 500,000,000 bytes | [Official, 2026-09] |
| Minimum size | 25,000 matched users for inclusion and bid multipliers; no minimum for exclusion; remaining included audience after exclusions must still meet the size | [Official, 2026-09] |
| Precedence | Exclusion wins when a user is in both | [Official, 2026-09] |
| Bid multipliers | 0.1x to 10x per ad group reported | [Unverified] |
| EEA and Switzerland | Do not use custom audiences; personalization unavailable | [Official, 2026-09] |
| Readiness | Wait for status ready; uploaded rows are not matched users; counts shown as ranges | [Official, 2026-09] |

Practical uses: exclude existing customers from acquisition campaigns (no minimum size, so even small lists work); bid up lapsed customers with a multiplier if you have 25,000+ matched; never upload lists without a documented legal basis and consent where required.

## 7. Product feed campaigns (catalog advertisers)

Setup [Official, 2026-09]:
1. Ads Manager > Tools > Feeds > Create Feed (name and country list).
2. Import products: CSV or TXT upload (manual), hosted HTTPS URL (scheduled), or SFTP (automated; files in the SFTP root, no nested folders).
3. Items expire after 2 weeks; use hosted URL or SFTP so the feed refreshes at least daily.
4. Products are ads eligible by default in feeds created in Ads Manager unless marked false; in the API schema set `is_ads_eligible: true`.
5. Processing takes minutes to hours; check Upload History.
6. Create a campaign with campaign type **Product feed**, select the feed, apply product filters per ad group, confirm product count.
7. One product ad template per ad group, using macros `{{brand}}`, `{{product.title}}`, `{{product.body}}`, `{{product.price}}`; the product supplies image and URL.
8. Bid strategy defaults to Maximize results for eligible new ad groups.
9. Products tab reporting appears up to 7 hours after delivery starts.

Feed rules:
- Schema is Google Merchant compatible [Unverified] (community notes); product pages and images must be public HTTPS.
- Delta updates for price and availability: `PATCH /v1/feeds/{feed_id}/products` (minor currency units).
- Product set filters: `field`, `operator`, `values`; custom labels via `ads_metadata.<field>` (for example `bidding_tier`, `product_line`, `margin_band`).
- Feed products are used for ads only during the beta and do not appear in organic conversations [Official, 2026-09]. The organic merchant feed is a separate program (see organic and commerce reference).
- Campaign mode, objective and linked feed cannot change after creation.

Recommended feed structure:
| Ad group | Filter | Purpose |
|----------|--------|---------|
| Hero products | `ads_metadata.bidding_tier in [hero]` | Top 10% revenue products, highest bid |
| Core margin | `ads_metadata.margin_band in [high]` | Profitable range |
| Long tail | remaining | Low bid or Maximize results to find demand |
| Exclusions | `availability` out of stock, low margin, policy risk products | Never advertise |

Carousels: OpenAI decides whether a single product or a carousel shows; carousels currently show one retailer [Unverified] (Digiday, 2026-08). Carousel card impressions and clicks are reported separately and card impressions are not billable [Official, 2026-09].

## 8. Bulk upload and edits

- Create > Upload bulk with the campaign schema template. Bulk upload does not support product feed campaigns [Official, 2026-09].
- Required: unique campaign name, max budget, start and end dates (YYYY-MM-DD), objective, target countries; ad group: matching campaign name, unique ad group name, max bid, context hints as JSON array; ads: title, copy, brand name, logo, landing URL, image URL [Official, 2026-09].
- Do not rename tabs or headers. Validate before uploading. Processing finishing does not mean every row succeeded; check each row. Do not replay rows that already succeeded with a blank ad_id (creates duplicates) [Official, 2026-09].
- Bulk edit: select objects > Export for edit > modify > Create > Bulk upload; keep IDs for updates; new children reference parent IDs. Hints are replaced, not merged [Official, 2026-09].

## 9. Launch structure templates

### Template A: first test, single market (Growth tier)
| Campaign | Objective | Budget | Ad groups |
|----------|-----------|--------|-----------|
| `US_CPC_Core_202610` | Clicks, Manual: Max bid | Daily $100 to $300 | 4 ad groups, one per hint style on the top intent, same 4 ads |
| `US_CPC_Intents_202610` | Clicks, Manual: Max bid | Daily $100 to $200 | 3 to 5 ad groups by intent, best style after week 2 |

### Template B: ecommerce with catalog (Growth to Scale)
| Campaign | Objective | Budget | Ad groups |
|----------|-----------|--------|-----------|
| `US_Feed_Clicks_202610` | Product feed, Clicks, Maximize results | Daily | Hero, core margin, long tail |
| `US_CPC_Categories_202610` | Clicks | Daily | Category intents with collection landing pages |
| `US_Feed_oCPC_202611` | Product feed, Conversions (oCPC) on `order_created` | Daily | Created after 30+ purchases in 30 days |

### Template C: lead gen, local
| Campaign | Objective | Budget | Ad groups |
|----------|-----------|--------|-----------|
| `US-TX_CPC_Services_202610` | Clicks, regions or DMAs | Daily | One per service (emergency, install, maintenance), hints with area, hours, fees |

### Template D: app
| Campaign | Objective | Platforms | Notes |
|----------|-----------|-----------|-------|
| `US_CPC_iOS_202610` | Clicks then Conversions on `app_installed` via MMP and CAPI | iOS app | Click-through attribution only; MMP click URL as destination |
| `US_CPC_Android_202610` | Same | Android app | GAID accepted for audiences |

## 10. Structure QA checklist
- [ ] One market and one objective per campaign; names follow the convention.
- [ ] Every ad group is one intent; hints are need or situation phrases; 20 to 60 hints.
- [ ] Hint style encoded in the ad group name and in `utm_content`.
- [ ] 3 to 5 distinct ads per ad group.
- [ ] Geo matches the eligible and served markets; product feed campaigns at country level.
- [ ] Custom audiences only outside EEA and Switzerland, with legal basis.
- [ ] Conversion event setting attached to every campaign.
- [ ] Everything created paused for approval.
