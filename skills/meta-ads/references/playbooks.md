# Playbooks: Launch, Optimize, Scale, Recover, Seasonality

> Knowledge as of 2026-10. Every play ends in a change list for human approval. Nothing is published, paused or re-budgeted without explicit approval.

## Play 1. New account or new market launch (weeks 0 to 6)

Preconditions: dataset with Pixel and CAPI live, deduplicated, EMQ checked; business portfolio verified; payment method; brand safety set; unit economics in PROJECT_BRIEF.md.

| Week | Actions | Exit criteria |
|------|---------|---------------|
| 0 (prep) | Audit tracking (measurement module), set audience segments, account controls, naming, UTMs. Brief 6 to 10 concepts to `creative-strategy` (or build from existing assets). Write launch plan and change list | Human approval |
| 1 | Launch Core campaign: Advantage+ on, highest volume, deepest event with enough volume; budget >= 7 x target CPA per day if affordable. 4 to 6 concepts | Spend flowing, events recorded |
| 2 | Do not edit except kills of clear losers (2 x CPA spend, 0 conversions, weak leading indicators). Add 2 to 3 concepts at end of week in one batch | 7-day CPA read |
| 3 to 4 | Keep winners, add concepts weekly, consider catalog campaign for ecommerce, consider retargeting only for high consideration | Learning exited or path to it |
| 5 to 6 | First optimization: bid strategy review (value vs volume), first A/B test, first creative testing tool cycle | Stable CPA within 20% of target or a decision to change event or offer |

Launch change list template:
```
| # | Object | Setting | Value | Reason |
| 1 | Campaign US_SALES_ADV+_PURCH_HV_20261010 | Objective / goal | Sales / Maximize conversions (Purchase) | Deepest event with >= 50 per week forecast |
| 2 | Campaign | Budget | Advantage campaign budget, 350 per day | 7 x target CPA of 50 |
| 3 | Ad set | Audience | Advantage+ audience, controls: US, 18+, exclude purchasers 180d | Legal + waste control |
| 4 | Ad set | Placements | Advantage+ placements | Max liquidity |
| 5 | Ads | 5 concepts x 1 to 2 executions | see creative registry | Diversity |
| 6 | Ads | Advantage+ creative enhancements | Text improvements OFF, music ON, others reviewed | Claims risk |
```

## Play 2. Weekly optimization (running accounts)

1. Pull data (API or export) for last 7, 14, 28 days and the same week last year if available. State date ranges and attribution.
2. Check guardrails: CPA or ROAS vs target, MER, new customer share.
3. Decompose changes (CPM, CTR, CVR, AOV).
4. Creative: kill, keep, iterate per kill rules; queue new concepts to fill coverage gaps.
5. Budget: shift toward campaigns with the best marginal returns; step changes per bidding module.
6. Bid goals: adjust cost per result goal or ROAS goal by 10% max per week.
7. Tests: close, log learnings, start next from EXPERIMENTS.md backlog.
8. Write weekly report, change list, journal entry.

## Play 3. Scaling

Scaling methods ranked by risk:
| Method | How | Risk | When |
|--------|-----|------|------|
| Creative-led scaling | Add distinct concepts so retrieval finds new pockets; budget follows | Low | Always first |
| Vertical budget scaling | +15 to 30% every 48 to 72 hours on stable ad sets; +20 to 50% under campaign budget | Medium | CPA at or below target for 7+ days, frequency stable |
| Cost-controlled scaling | Cost per result goal or ROAS goal at target, budget 2 to 5 x expected spend | Low to medium | Volume above about 50 conversions per week, stable values |
| Horizontal: new campaign types | Catalog, click to message, partnership ads, Threads or WhatsApp Status placements included via Advantage+ placements | Medium | Main campaign saturating |
| Horizontal: new geos or languages | New country clusters, translated creative | Medium to high | Product-market fit and logistics in place |
| Horizontal: new offers or products | New hero products, bundles, lead magnets | Medium | Offer fatigue |
| Duplicating ad sets | Copy winning ad set | High (overlap, learning reset) | Avoid; only for a new geo or bid strategy |

Scaling gates (all must be true before a budget increase above 30% per week):
1. 7-day CPA or ROAS within target and backend confirms (MER or new customers moving).
2. At least 3 concepts carrying spend (no single-ad dependence above 50% of spend).
3. Frequency in normal range and CTR not declining.
4. Creative pipeline can deliver the tier's weekly volume.
5. Marginal CPA (bidding module section 7) below allowable CPA.

Creative volume to support scaling: see creative module section 3. If spend doubles, the weekly new concept count should roughly double.

Worked example (scale from 30k to 60k per month in 6 weeks, ecommerce):
- Week 1: add 8 new concepts; raise main campaign budget +25%. Launch cost per result goal campaign at target CPA with budget 2 x.
- Week 2: if CPA within 10% of target, +25% again; cost-controlled campaign spend reveals how much volume exists at target.
- Week 3: add catalog product sets by margin tier; add partnership ads from 3 creators.
- Week 4 to 6: continue +20 to 25% steps when gates pass; hold for a week whenever CPA exceeds target by 15% for 3 days.
- Validate every two weeks with MER and new customer CAC.

## Play 4. Recovery from a performance drop

Triage within 24 hours:
1. Is it real? Compare backend revenue and leads with Meta-reported results. Check attribution change dates (2026-01-12, 2026-03-03), Events Manager health, consent changes.
2. Is it Meta-wide? metastatus.com, practitioner communities for delivery incidents on the same dates.
3. Is it self-inflicted? Activity history and journal for edits in the last 14 days (structure, budgets, bid goals, creatives, site, prices, stock).
4. Is it market? Seasonality, competitor promotions (Ad Library check via `market-intel`), CPM inflation.

72-hour plan by root cause:
| Root cause | Action |
|-----------|--------|
| Tracking break | Hand off to `measurement` immediately; switch optimization to a working event temporarily only if the break lasts days; annotate reports |
| Creative fatigue | Launch 3 to 6 new concepts from the backlog; reduce budget on fatigued ads by 30 to 50%; do not edit them |
| Over-editing / learning resets | Freeze edits for 7 days; consolidate |
| Bid goal too tight after CPM rise | Loosen goal 10 to 20% or move part of budget to highest volume |
| Landing page or offer issue | Hand off to `cro` with evidence; consider pausing traffic to the broken page |
| Account restriction or disapprovals | Policy play below |
| Seasonality (Q4 CPMs) | Accept higher CPA within LTV limits or reduce spend; focus on high intent creative and offers |

Do not: restructure the whole account, launch many duplicates, or slash budgets by more than 50% in panic. Recovery should change one lever per day where possible.

## Play 5. Account restriction or mass disapproval

1. Business Support Home / Account Quality: identify the restricted asset (ad account, Page, business portfolio, person) and the policy cited.
2. Stop launching new ads in the affected account until cause is known.
3. Fix root cause (landing page claims, prohibited content, payment, identity verification).
4. Request review with a concise factual statement and evidence (see policy module template).
5. Document in journal; inform human; never create new accounts to evade restrictions (circumvention is grounds for permanent bans).

## Play 6. Seasonality and BFCM (Black Friday, Cyber Monday)

| When | Action |
|------|--------|
| T-75 to T-60 days | Agree offer, margin floor, inventory with the human. Build creative plan: teaser, launch, urgency, last chance, Cyber Monday, post-sale. Brief `creative-strategy` |
| T-60 to T-30 | Grow warm pools (engaged audience) with video and content concepts; test offer framings; check catalog sale_price fields with `commerce-feeds` |
| T-30 to T-14 | Lock structure; no restructuring after this. Load sale creatives as paused drafts for approval. Prepare budget scheduling (percentage increases for event days) |
| T-14 to T-1 | Keep BAU running; raise budgets gradually (CPMs rise late November); ensure payment method limits and spending limits allow peak spend |
| Event days | Budget scheduling active; monitor every 2 to 4 hours for delivery, disapprovals and stock; do not edit winning ad sets; swap creatives via pre-approved plan only |
| T+1 to T+14 | Step budgets down; retention and cross-sell to new buyers; analyze new customer share and post-event MER |

CPMs typically rise through Q4 with a peak around BFCM [Practitioner consensus]; judge on contribution margin, not ROAS alone. Retargeting share can rise during the event but validate with backend.

## Play 7. Plateau breaker (spend flat, CPA rising with each increase)

1. Check concept diversity: count distinct concepts carrying spend. If under 5, the plateau is creative-limited.
2. Check offer: when did the offer last change? Test a new offer or bundle.
3. Check funnel: CVR trend; hand off to `cro`.
4. Expand horizontally: catalog, messaging, partnership ads, new geos.
5. Test value optimization or incremental attribution if volume allows.
6. Consider shifting budget to channels with better marginal returns (handoff to `growth-orchestrator`).

## Play 8. Starter tier (under $3k per month) operating play

- One campaign, one ad set, 3 to 6 concepts, highest volume, optimize to the deepest event with 10+ per week.
- Weekly creative add of 1 to 2 concepts; kill only clear losers.
- No A/B tests; use pre/post with caution and log as directional.
- Messaging or instant forms if website conversion volume is too low.
- Focus energy on offer, landing page and creative, not settings.
