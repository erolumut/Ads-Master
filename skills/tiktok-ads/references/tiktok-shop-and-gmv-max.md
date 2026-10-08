# TikTok Shop and GMV Max

> Knowledge as of 2026-10. GMV Max is the only campaign type for TikTok Shop ads with a Sales objective since July 2025. Several 2026 features (GMV Max Pro, seller-cost-aware optimization, Creative Hub, Spillover reporting, Video upload for LIVE GMV Max, Creative Boost) are in limited rollout or require allowlisting. Confirm in Seller Center and Ads Manager before planning around them.

## 1. What changed and when

| Date | Change | Label |
|------|--------|-------|
| 2024 | GMV Max launched (Product GMV Max and LIVE GMV Max) | [Official] |
| June to July 2025 | Phased migration: new Shop sellers blocked from legacy ad types (reported 2025-06-01), legacy creation removed (reported 2025-06-25), all sellers required on GMV Max (reported 2025-07-15). Official wording: since July 2025 GMV Max is the default and only supported campaign type for TikTok Shop Ads with a Sales objective | [Official, 2025-07]; exact phase dates [Contested] |
| July 2025 onward | Live, Product and Video Shopping Ads with Sales objective and Shop destination can no longer be created, edited or duplicated; existing ones finish delivery | [Official, 2025-07] |
| 2025-10-07 | GMV Max updates bundled with the Smart+ automation announcement | [Official, 2025-10] |
| 2026-02-25 | ROI protection extended to GMV Max campaigns created in Seller Center (PC and mobile) and Ads Manager | [Official, 2026-02] |
| 2026-05-13 | TikTok World: GMV Max Pro (factors coupons, affiliate costs, platform commissions into optimization; limited rollout); GMV Max reporting includes affiliate commissions, coupons and platform fees | [Official, 2026-05] |
| 2026-10-05 | Advertising Week: GMV Max optimization accounts for affiliate commissions, coupons and referral fees when calculating return | [Official, 2026-10] |

What is not affected: Search Ads remain a separate product; campaigns pointing to your own website still use standard, Spark or Smart+ campaigns.

## 2. How GMV Max works

| Element | Advertiser controls | Platform controls |
|---------|--------------------|--------------------|
| Products | Which products (all or selected) or which LIVE room | n/a |
| Budget | Daily budget | Pacing across placements |
| Goal | Target ROI or Max Delivery | Bidding per auction |
| Creative | Can add own videos, authorize posts, exclude some content; Creative Boost for a specific video (allowlist) | Selects among own, Spark-authorized and affiliate videos and product cards |
| Targeting | None (no manual audiences or keywords) | Full automation |
| Placements | None | Feed, Shop surfaces, search, LIVE, product cards |

Types:
- Product GMV Max: promotes selected products using available videos (own, Spark-authorized, affiliate content) and product cards.
- LIVE GMV Max: drives viewers into livestreams while live. Product updates include Live Control, Mega Live Mode and Video-to-LIVE [Official, 2026].
- Seller Scale Up: a lighter option for smaller merchants that optimizes over a 7-day cycle [Unverified, third-party].

## 3. Shop economics and the ROI target

Definitions (TikTok Shop reporting):
- Gross revenue (GMV attributed to the campaign) / Cost = ROI. TikTok uses "ROI" where other platforms say ROAS.
- Cost per order = Cost / Orders.

Breakeven ROI formula:

```
Net margin per $1 of GMV before ads (m) =
    1
  - COGS %
  - referral (platform) fee %
  - affiliate commission % (share of GMV that carries commission x rate)
  - coupon / discount cost % funded by seller
  - shipping subsidy %
  - returns and refunds %
  - payment and fulfillment %

Breakeven ROI = 1 / m
Target ROI    = Breakeven ROI x (1 + required margin buffer), e.g. x 1.2
```

Worked example: COGS 30%, referral fee 8% [illustrative; check current Shop fee schedule for your market], affiliate commission 15% on 60% of GMV = 9%, seller coupons 5%, shipping subsidy 4%, returns 5%, fulfillment 6%. m = 1 minus 0.67 = 0.33. Breakeven ROI = 3.03. Target ROI with 20% buffer = 3.6.

If GMV Max Pro or seller-cost-aware optimization is enabled in your account, confirm which costs the platform already deducts before setting the target, or you will double-count.

## 4. Setup procedure (Product GMV Max)

1. Preconditions: Shop in good standing, products approved, inventory in stock, prices competitive, product listing optimized (title, images, video, reviews). Hand listing quality to commerce-feeds if needed.
2. Product selection: start with products that already sell organically or via affiliates. Group products by margin band if your account allows separate campaigns per product set. Check whether a product can sit in more than one active GMV Max campaign in your account [Unverified].
3. Optimization: for new shops or new products, Max Delivery for the first 3 to 5 days, then Target ROI as the always-on strategy [Official].
4. Target ROI: start at the trailing actual ROI or at breakeven x 1.1 if no history.
5. Budget: enough for at least 20 orders per day if you want ROI protection eligibility (see section 6); otherwise accept that protection does not apply.
6. Creative supply: authorize the brand account, link affiliate content, upload videos. TikTok recommends at least 50 to 70 videos "In queue" for stable creative exploration in LIVE GMV Max [Official]; Product GMV Max also has creative supply guidance [Official].
7. Launch, then do not edit for 3 to 7 days except for stock-outs.

## 5. LIVE GMV Max procedure
1. Schedule LIVE sessions in advance; align the campaign with the session windows.
2. Use Video-to-LIVE short clips and creator content that drive into the LIVE room.
3. Creative Boost (allowlist): adds a separate daily budget (minimum $10 or equivalent) to one video, paced alongside the LIVE GMV Max budget; starts immediately or at the next LIVE; default end time 24 hours after start. ROI on the boosted portion is not guaranteed, and reporting shows impressions, cost, CTR and video views only (no GMV, orders or ROI) [Official].
4. Measure per session: viewers, average watch time, product clicks, orders, GMV, ROI, GMV per hour.

## 6. ROI protection [Official, 2026-02]

| Rule | Detail |
|------|--------|
| What | Ad credits issued when a campaign's daily ROI falls below 90% of its target |
| Volume requirement | Generally more than 20 daily orders |
| No edits | The campaign must not have been edited that day beyond stated limits |
| Ineligible days | Manual Target ROI changes beyond limits, pausing or deleting the campaign, campaigns or products using Max Delivery |
| Exclusions | Creative Boost spend is not counted for ROI compensation |
| Caveat | It is conditional compensation in ad credits, not a promise that GMV Max cannot lose money [Contested] |

Operating rule: plan edits in a single daily window, keep a change log, and avoid pausing GMV Max to "save budget" on weak days because it forfeits protection and resets delivery.

## 7. Shop-specific metrics to track

| Metric | Where | Why |
|--------|-------|-----|
| GMV, orders, ROI, cost per order | GMV Max dashboard (Ads Manager or Seller Center) | Core |
| Gross revenue split by source: ads vs organic vs affiliate | Seller Center analytics (Data Compass [Unverified name]) | Cannibalization check |
| Product impressions, product clicks, product CTR, conversion rate | Seller Center product analytics | Listing quality |
| Creative-level: video views, CTR, GMV per creative, creator | GMV Max creative report, Creative Hub (shows top assets and creators) [Official, 2026] | Creative supply decisions |
| Affiliate GMV, commission paid, sample to post rate | Affiliate center | Partner economics |
| LIVE: viewers, watch time, GMV per hour, GPM | LIVE analytics | Session quality |
| Refund and return rate | Seller Center | True margin |
| Spillover sales on other channels | Spillover reporting where available [Unverified] | Halo effect on Amazon or website |
| Shop health score / account health | Seller Center | Violations stop ads and payouts |

## 8. Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|--------------|--------|-------|
| GMV Max not spending | Target ROI too high, too few eligible videos, products not eligible, budget too low | ROI target vs trailing actual; creative queue count; product status | Lower target 10% to 15%, add videos, fix listings |
| ROI falling week over week | Creative fatigue, price no longer competitive, affiliate content dried up, competitors in mega sale | Creative report; price vs competitors; affiliate post count | New creatives, refresh affiliates, adjust offer, temporary Max Delivery during sale events with clear stop date |
| ROI high but total GMV flat | GMV Max claiming organic or affiliate sales | Compare total Shop GMV before and after launch, organic share trend | Holdout test: pause ads in a planned week or reduce budget 50% and watch total GMV [Contested methodology] |
| Spend concentrated on one product | Algorithm found a winner | Product-level ROI and stock | Ensure stock; split hero product into its own campaign if allowed |
| ROI protection credits not appearing | Ineligible day | Edit log, order count | Edit discipline, consolidate to exceed 20 daily orders |
| LIVE GMV Max weak | Host performance, low creative supply, poor timing | Watch time, product clicks per viewer | Host coaching, more clips, test time slots |

## 9. Website plus TikTok Shop: dual-channel rules
1. Decide each product's primary destination. Products that sell better in-app (impulse, under $50, demo-driven) go to Shop; considered purchases, subscriptions and bundles may go to the website.
2. Keep prices aligned or Shop listings may lose eligibility and customers notice.
3. Website campaigns (Smart+ Web, Catalog) and GMV Max compete for the same users. Measure blended: total TikTok-driven revenue (Shop GMV + website revenue attributed and triangulated) vs total TikTok cost.
4. Buy Direct (announced 2026-10-05) lets users buy from a brand inside the feed via Shopify, Salesforce, Shoplazza and Stripe integrations; early access, rollout timing [Contested]. Treat as a test when offered, not a plan.
5. Hand catalog and product data to commerce-feeds (TikTok catalog, Shop listings, product sets).

## 10. Weekly GMV Max review template

```
Week: YYYY-MM-DD to YYYY-MM-DD | Data: GMV Max dashboard export + Seller Center
| Campaign | Type | Budget | Cost | GMV | ROI | Target ROI | Orders | CPO | Protection credits | Edits this week |
Products: top 5 by GMV, bottom 5 by ROI, stock risk
Creatives: top 10 by GMV (own / affiliate / Spark), new creatives added, queue count
Affiliates: new posts, top creators by GMV, commission paid
Total Shop GMV (all sources) vs last 4 weeks; ads share of GMV
Decisions proposed (for approval): ROI target changes, budget changes, creative actions
```
