# Playbooks: Launch, Optimize, Scale, Recover

> Knowledge as of 2026-10. Each play ends with a change list for human approval. The agent never launches, pauses or edits live campaigns itself. Every play states the data used and its date range.

## Play 1. Launch a new Google Ads account (or a new market)

Preconditions (stop if any fails):
1. Conversion tracking for the primary outcome verified with a test conversion (measurement confirms).
2. Enhanced conversions on; consent mode v2 if EEA or UK traffic.
3. Unit economics in PROJECT_BRIEF.md: target CPA or ROAS derived from margin.
4. Landing pages working, fast, policy compliant, with business transparency pages.
5. Advertiser verification started; billing set.

Steps:
| Day | Step |
|---|---|
| 0 | Build structure from the template in [account structure](account-structure.md) for the business model and tier |
| 0 | Brand Search campaign: exact and phrase brand terms, Max clicks with CPC cap or target impression share with cap |
| 0 | Non-brand Search: 1 to 3 campaigns by intent theme. Exact and phrase at Starter tier. Maximize conversions without target (or Max clicks with cap if tracking is new and volume will be very low) |
| 0 | Ecommerce with feed: one PMax with feed for top sellers, brand exclusions, URL expansion off or with exclusions, Maximize conversion value without target |
| 0 | Shared negative lists, account-level negatives, placement exclusions, location option Presence where relevant |
| 0 | Assets: 2 RSAs per ad group (or 1 strong one), sitelinks, callouts, snippets, images, business name and logo, call and location where relevant |
| 0 | AI Max: off at launch unless the account already has 30+ conversions a month; document the decision |
| 1 to 3 | Daily: spend pacing, disapprovals, conversion firing, search terms for obvious waste |
| 7 | First search terms review; negatives; check impression share |
| 14 | Review CPA or ROAS vs target on 14 days; do not set targets yet unless 30+ conversions |
| 21 to 30 | Add tCPA or tROAS at the observed level when the data threshold is met. Plan first experiment |

Budget at launch: enough for at least 10 to 20 clicks a day per non-brand campaign and, for Smart Bidding, ideally 5x to 10x target CPA per day across the account. If the budget cannot buy at least about 30 conversions a month, run fewer campaigns.

Deliverable: `ads-master/outputs/google-ads/YYYY-MM-DD_google-ads_launch-plan.md` with structure, settings, keywords, ads, budgets, bid strategy, tracking checks, change list.

## Play 2. Weekly optimization (60 to 90 minutes)

1. Data: pull Q1, Q2, Q3 (14 days), Q7, Q23 or the matching exports. State the date range.
2. Tracking sanity: conversions per day vs trailing median (stop and escalate if broken).
3. Pacing: projected month spend vs plan.
4. Search terms: negatives, new exact or phrase keywords from converters, AI Max term review.
5. Impression share: budget or rank limits on profitable campaigns.
6. Bidding: targets vs actual; only step targets 10% to 15% when 2 weeks of stable data justify it.
7. PMax: search terms, channel mix shifts, product tiers (every 2 weeks).
8. Ads: disapprovals; assets with low performance (monthly).
9. Experiments: status, guard rails.
10. Journal entry: what changed, why, data, next actions. Change list for anything that needs approval.

## Play 3. Monthly optimization (half day)

1. Full KPI review vs targets and vs last year, brand and non-brand separately.
2. N-gram analysis (script S2) over 90 days; negative list updates.
3. Asset refresh: replace low performers, add a new angle per main ad group and asset group.
4. Budget reallocation proposal by marginal returns (simulators, Missed Opportunities, lost IS).
5. Audience lists refreshed; NCA lists checked.
6. Policy and account health check (verification, certifications, policy change log).
7. Freshness check of platform changes (see SKILL.md Freshness protocol) and journal any change that affects the account.
8. Audit-lite: rerun the High and Critical items from the audit checklist.

## Play 4. Scale (when efficiency is proven)

Entry criteria: CPA or ROAS at or better than target for 4+ weeks, tracking reconciled, incrementality evidence or at least no sign of heavy brand or remarketing dependence.

Levers in order:
| Order | Lever | How | Watch |
|---|---|---|---|
| 1 | Budget on budget-limited profitable campaigns | Raise 15% to 20% every 3 to 7 days | Marginal CPA (compare increments, not averages) |
| 2 | Loosen targets | tCPA up 10% or tROAS down 10% every 2 weeks | Volume response vs efficiency loss |
| 3 | Broaden matching | Broad match on proven themes, AI Max experiment, Smart Bidding Exploration for tROAS | Search term quality, AI Max share |
| 4 | New inventory | PMax for new categories, Demand Gen and YouTube for demand creation, Shopping AI Max beta | Account-level conversions, lift tests |
| 5 | New markets | Copy proven structure per market and language, local landing pages, local currency | Market-specific economics |
| 6 | Value signals | Profit values, NCA values, OCI stages, value rules from LTV | Value accuracy |

Stop scaling when marginal CPA exceeds the breakeven CPA, or marginal ROAS falls below breakeven ROAS, for 2 consecutive weeks.

## Play 5. Recover from a performance drop

Triage within 24 hours (in this order, because the cheapest explanation is usually right):
| Step | Check | Tool |
|---|---|---|
| 1 | Tracking: did conversions drop while clicks held? | Q7, Diagnostics, journal for site releases |
| 2 | Delivery: impressions down? Disapprovals, budget, billing, policy, Merchant Center | Q1, Q16, notifications |
| 3 | Changes: what changed in 14 days (users, auto-apply, Google migrations such as AI Max auto-upgrade, language setting removal, automated promotions) | Q24, change history |
| 4 | Market: auction insights (new competitor, higher overlap), CPC up, seasonality, news | Auction insights, Q2 |
| 5 | Site: landing page errors, speed, checkout, stock, prices | Q19, cro, commerce-feeds |
| 6 | Query mix: new low-intent terms | Q3, Q3b |
| 7 | Bidding: target changes, learning, the 2026-08 target-based bidding update | Q8, Q24 |

Response rules:
- Tracking broken: fix first, add data exclusions, no bid changes on bad data.
- Delivery issue: fix the blocker (appeal, feed fix, billing), do not raise bids to compensate.
- Google-initiated change (AI Max auto-upgrade): review features, add controls, run experiment before turning off if the data is unclear.
- Market change: adjust targets and budgets with approval; refresh offer and creative with creative-strategy.
- Site or feed issue: hand off with evidence.

Deliverable: incident report in outputs plus a journal entry tagged alert.

## Play 6. Respond to the AI Max auto-upgrade (September 2026)

1. List affected campaigns: those that had ACA or campaign-level broad match on 2026-08-31 (labels, Q8b, change history entries by Google).
2. For each: features now on, brand exclusions, URL exclusions, text guidelines.
3. Compare 4 weeks before and after the upgrade date: conversions, CPA or ROAS, share of AI Max matched spend, landing pages "Selected by".
4. Apply controls first (brand exclusions, URL exclusions, negatives, ad group opt-outs).
5. If performance worsened by more than 15% and controls do not fix it in 2 weeks, propose an AI Max experiment (on vs off) rather than switching off blindly.
6. DSA campaigns: plan the move before the scheduled DSA migration (February 2027 per mid-2026 reports, verify) using AI Max experiments and moving URL targeting into AI Max URL controls.
7. Journal entry so other agents understand trend breaks in September 2026.

## Play 7. Recover from suspension or policy issues

Follow [policy and account health](policy-and-account-health.md) section 10. Additional steps for the google-ads agent:
- Hand off budget reallocation to growth-orchestrator during the outage.
- Hand off site transparency fixes to cro and feed misrepresentation issues to commerce-feeds.
- Never propose new accounts as a workaround.

## Play 8. Fix lead quality (lead gen and B2B)

1. Measure: lead to qualified rate by campaign, keyword theme, device, geo and hour (CRM export joined on GCLID).
2. Quick fixes: negatives for low quality themes, form friction for spam (honeypot, validation, required qualifying fields) via cro, exclude spammy placements (Demand Gen, PMax), turn off Search partners if quality is worse.
3. Structural fix: OCI with qualified stage as primary; values by stage; move bidding to qualified lead tCPA or value-based.
4. If PMax or Demand Gen drive junk: restrict to OCI goals or pause until OCI exists.
5. Measure again after 4 weeks on qualified leads and pipeline value, not raw leads.

## Play 9. Ecommerce profitability reset (ROAS looks fine, profit does not)

1. Get contribution margin by product or category (PROJECT_BRIEF.md, commerce-feeds).
2. Compute breakeven ROAS per margin band; compare to actual by band (Q22 joined with labels).
3. Restructure PMax and Shopping by margin band with separate tROAS, or move to profit-based values with measurement.
4. Add NCA goal if new customer acquisition is the strategy; set the new customer value from data.
5. Check brand and remarketing share in PMax; add brand exclusions.
6. Report POAS weekly.

## Play 10. Reporting (weekly and monthly)

Weekly report sections:
1. Summary (5 bullets): performance vs target, biggest change, biggest risk, decisions needed.
2. KPI table: spend, conversions, CPA or ROAS, value, brand vs non-brand vs PMax vs visual, vs prior week and target.
3. What we changed (from change history) and why.
4. Search terms and negatives summary.
5. Tests: status and reads.
6. Change list awaiting approval.
7. Handoffs requested.

Monthly adds: trend vs last year, budget reallocation proposal, asset refresh plan, platform changes from the Freshness check, audit-lite score.

## Play 11. Cold start (no ads-master folder, minimal info)

Ask only:
1. Business model, website, markets and currency.
2. Primary conversion and its value (or margin and AOV).
3. Monthly budget and current Google Ads status (new or running; account ID if running).
4. Access route: MCP connector, exports, or screenshots.
5. Hard constraints: regulated category, target CPA or ROAS, brand rules.

Then: run the audit (running account) or Play 1 (new account), and suggest the `ads-setup` skill to create the workspace.
