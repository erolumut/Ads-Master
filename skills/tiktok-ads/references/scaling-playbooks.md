# Playbooks: Launch, Optimize, Scale, Recover

> Knowledge as of 2026-10. Step-by-step plays. Every play produces a change list for human approval; nothing goes live without it. Numbers marked "default" are Ads Master house rules to tune with project data.

## 1. Play: launch a new web account (ecommerce or lead gen)

Preconditions (stop if any fails):
- [ ] Business Center owned by the brand; ad account currency and time zone correct
- [ ] Pixel + Events API live with event_id dedup; test purchase or lead visible in Test Events
- [ ] Primary conversion defined in MEASUREMENT.md with value
- [ ] Landing pages load fast on mobile and match offers
- [ ] 6+ creatives ready (TikTok Smart+ guidance), at least 3 distinct concepts, sound on, 9:16
- [ ] Policy check of category, claims and landing page done

Steps:
1. Week 0: warm the pixel. If the site has organic traffic, let the pixel collect events for a few days before launch. Connect the TikTok account (identity) and catalog if ecommerce.
2. Day 1: launch one manual Sales (or Lead Generation) campaign, one ad group, broad targeting with legal guardrails, Maximum Delivery, 7-day click + 1-day view, TikTok placements only, 3 to 6 ads. Budget: at least 10x target CPA per day if affordable; otherwise optimize to a higher-funnel event that can reach 25+ per week.
3. Days 1 to 7: no edits except fixing rejections or broken links. Daily checks only.
4. Day 8: apply kill/keep rules to ads; add 3 new ads (new hooks on the best concept + 1 new concept).
5. Day 14: if 50+ conversions per week, create a Smart+ campaign (Web or Catalog) with the winners and 6+ creatives at 10x to 30x CPA budget [Official guidance]; keep the manual campaign as the creative testing lane.
6. Day 21 to 28: first triangulation read (platform vs GA4 vs backend vs survey); set calibrated targets; consider Cost Cap on the scaling campaign.
7. Day 30: write the launch review; log learnings to memory only if confirmed by data.

## 2. Play: launch TikTok Shop with GMV Max

1. Shop readiness: products approved, inventory, competitive price, 5+ images and a video per hero product, reviews seeded through samples. Hand listing quality to commerce-feeds.
2. Affiliate seeding: open collaboration at a commission the margin supports; targeted invites to 20 to 50 creators; ship samples to the best 10 to 20.
3. Content supply: brand posts 1 to 3 videos per day on the Shop account; collect affiliate videos.
4. Launch Product GMV Max on Max Delivery for 3 to 5 days for new products [Official], then switch to Target ROI at the trailing actual ROI or breakeven x 1.1.
5. Add LIVE GMV Max once the brand runs regular LIVE sessions (at least weekly) with a trained host.
6. Weekly GMV Max review (template in tiktok-shop-and-gmv-max.md section 10).
7. Month 2: test GMV Max Pro or seller-cost-aware settings if offered; ROI protection eligibility (20+ daily orders).

## 3. Play: launch app campaigns
1. MMP integrated with TikTok, SKAdNetwork configured, in-app events mapped, SAN attribution windows set per ad group.
2. Smart+ App or manual App promotion per OS, optimize to install for the first 1 to 2 weeks unless the in-app event already has 50+ per week.
3. Creative: screen recordings with voiceover, creator demos, gameplay; 6+ assets; Auto-select creative where offered.
4. Week 3: move to AEO on the key event (registration, trial, purchase); test VBO when payers are frequent.
5. TikTok Ad Network as a separate tested cell for gaming; judge on Day 7 retention and ROAS.

## 4. Play: weekly optimization (all accounts)
See optimization-and-diagnostics.md section 4. Output: weekly report + change list.

## 5. Play: scale

### 5.1 Readiness gate (all must be true)
- CPA at or below target (calibrated) for 14 days, or ROI above target for GMV Max
- Measurement health checks pass
- At least 3 creatives with scaling thresholds met in the last 30 days
- Creative pipeline can deliver the refresh cadence of the next tier (creative-for-tiktok.md section 6)
- Unit economics allow higher marginal CPA (marginal CPA usually rises with spend)

### 5.2 Vertical scaling (more budget in what works)

| Campaign type | Step | Cadence | Stop or roll back if |
|---------------|------|---------|---------------------|
| Manual ad group (Maximum Delivery) | +20% to 30% | Every 48 to 72 hours | 3-day CPA > 1.25x target |
| Manual ad group (Cost Cap) | +30% to 50% budget, cap unchanged | Every 48 hours | Spend no longer increases (cap binding): loosen cap 10% or stop |
| Smart+ Lead Generation | Up to +50% per day [Official] | Daily max | CPQL > 1.25x target for 3 days |
| Smart+ Web / Catalog | +20% to 30%; bid edits up to 15% every 2 days after day 7 [Official for bid edits] | Every 48 hours | 3-day CPA > 1.25x target |
| GMV Max | +20% to 30% budget, ROI target unchanged; lower target 5% to 10% for more volume | Every 2 to 3 days, in one daily edit window | ROI < 90% of target for 3 days |

Large jumps (2x or more): duplicate the winning campaign or ad group at the higher budget rather than editing the original, then shut the weaker one after 7 days.

### 5.3 Horizontal scaling (new pockets of demand)
1. New concepts and creators (biggest lever).
2. Search Ads Campaign for brand, product and category terms (budget 20x bid) [Official].
3. Smart+ Catalog Ads for wide catalogs.
4. New markets: one campaign per market with localized creators; TikTok Shop where available.
5. New objectives: Video views or Community interaction to build engager pools for retargeting at Scale tier.
6. Brand layer at Scale and Enterprise: TopReach, R&F, Pulse, with a Brand Lift Study.
7. Off-platform: TikTok Ad Network as a tested cell, judged on backend results.

### 5.4 Scale worked example
Account: ecommerce, $45k/month on TikTok, target calibrated CPA $38, current CPA $33 over 14 days, 340 purchases per week. Plan: +25% budget on Smart+ Web every 72 hours for 2 weeks (to about $70k/month run rate), add 12 new creatives per week from 6 creators, launch a Search Ads Campaign at $150/day for brand and category terms, keep manual testing at 15% of spend. Stop rule: 3-day calibrated CPA above $47.50 (1.25x) pauses further increases and triggers a creative review.

## 6. Play: Q4 / peak season
| When | Action |
|------|--------|
| 8 weeks out | Creative production doubles; creator contracts signed; Spark codes cover through January |
| 6 weeks out | Offer and landing pages final; Shop promotions registered; GMV Max targets modeled with promo margins |
| 3 weeks out | Budgets stepped up gradually; Cost Caps loosened 15% to 20% or switched to Maximum Delivery where volume matters |
| Peak week | Daily checks twice; no structural changes; only budget and creative swaps |
| 1 week after | Budgets down in 2 to 3 steps; caps reset to new trailing CPA; post-mortem in journal |

## 7. Play: recover

### 7.1 Performance crash (CPA up 50%+ or ROAS down 33%+ over 3+ days)
1. Tracking check first. If events dropped, open a measurement handoff and pause decisions.
2. Check change log: any edits in the 72 hours before the drop? Revert the largest one.
3. Check external: site down, stock-out, price change, competitor mega sale, platform outage.
4. Decompose CPA into CPM, CTR, CVR (optimization-and-diagnostics.md section 1).
5. If creative-driven: launch 5+ new ads within 72 hours; return 2 to 3 historical winners as fresh ads (new ad IDs).
6. If auction-driven (CPM): accept temporary higher CPA or lower budget; do not chase with bids.
7. If CVR-driven: page or listing; hand to cro or commerce-feeds.
8. Re-evaluate in 5 days. Document in the journal.

### 7.2 Account suspension or ad account disabled
1. Read the suspension reason on the account status page and any email from TikTok. Screenshot both.
2. Identify the trigger: policy violations (ads or landing page), payment issue, suspicious login or activity, association with a previously banned account or BC.
3. Fix the cause before appealing: remove violating ads, fix the landing page, update payment, secure logins.
4. Submit an appeal from Ads Manager (account appeal option) with a short factual explanation and evidence of fixes. One appeal, clear and complete.
5. Do not create new ad accounts or BCs to get around a suspension. Linked assets (payment, domain, BC, identity) can extend the ban [Practitioner consensus].
6. While waiting: shift budget to other channels via growth-orchestrator; keep organic posting on the TikTok account if it is not affected.
7. If the appeal fails: escalate via the TikTok rep (if any) with the case number; review policy-and-account-health.md for category-specific requirements (licenses, certificates).
8. Log the incident in the journal and memory (account facts).

### 7.3 Tracking broken
1. Freeze bid and budget changes.
2. Journal alert + measurement handoff with evidence (event counts by day, Events Manager diagnostics screenshot).
3. If purchases stop recording but sales continue, switch value-based and Cost Cap ad groups to Maximum Delivery temporarily only if the human approves, to avoid starved delivery.
4. After the fix, expect 3 to 7 days of unstable optimization.

### 7.4 Creative collapse (all top ads fatigued at once)
1. Pull the last 90 days of ads; find concepts that worked and have not run for 60+ days; relaunch as new ads.
2. Order emergency UGC from 3 to 5 creators with the best historical briefs (3 to 5 day turnaround).
3. Use Symphony for hook variations and dubbing of existing winners while new content arrives.
4. Lower budgets 20% to 30% until new winners appear rather than forcing spend into fatigued ads.

### 7.5 GMV Max ROI collapse
1. Check Shop health, product status, price competitiveness and stock.
2. Check creative queue count and affiliate post volume in the last 14 days.
3. Lower budget 20% instead of raising the ROI target sharply (sharp target hikes stall delivery).
4. Add new videos and affiliate content; consider a short Max Delivery burst only for a planned sales event.

## 8. Play: market expansion
1. Check product availability, TikTok Shop availability, regulatory category rules and language per market.
2. Localize creative with native creators; AI dubbing only for variations.
3. One campaign per market; separate budgets; local currency where possible.
4. EU: verify DSA ad repository visibility, consent setup and minor protections.
5. Read results on 28-day windows; expect higher CPA in the first month.

## 9. Change list template (attach to every play)

```
Change list: YYYY-MM-DD | Account: <name/ID> | Prepared by: tiktok-ads | Data: <files/connector>, <date range>
| # | Action | Entity | From | To | Reason (data) | Expected impact | Risk | Rollback trigger |
Approval required: yes. Approved by: ______ Date: ______
```
