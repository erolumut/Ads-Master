# Account Structure

> Knowledge as of 2026-10. Structure follows the delivery system. When Meta changes retrieval or ranking, re-check this module against the Freshness Protocol in SKILL.md.

## 1. How Meta delivery works now (the model behind every structure decision)

| Stage | System | What it does | Structural implication |
|-------|--------|--------------|------------------------|
| 1. Eligibility | Targeting controls, policy, budget, frequency | Removes ads that cannot serve to this person (location, minimum age, exclusions, special ad category limits, policy) | Hard controls still matter: location, minimum age, language, custom audience exclusions |
| 2. Retrieval | Andromeda | Narrows tens of millions of eligible ads to a few thousand candidates per impression opportunity, using deep models on user and ad embeddings [Official, 2024-12] | The creative itself (visual, copy, format, persona) decides which people your ad is retrieved for. Creative diversity is the new targeting |
| 3. Ranking | Lattice ranking models with knowledge transferred from GEM | Predicts estimated action rates (click, conversion, value) for each candidate [Official, 2025-11] | One large model learns across objectives and surfaces, so fragmenting your account does not create "custom models" for you, it only splits your signal |
| 4. Auction | Total value auction | Total value = advertiser bid x estimated action rate + ad quality [Official, long-standing] | Your bid strategy and your conversion signal quality both enter the score |
| 5. Pacing | Budget pacing, learning phase | Spreads spend across the day and campaign, explores during learning | Each ad set needs enough conversions to stabilize (about 50 per 7 days) [Official, long-standing] |

Key facts with dates:
- Andromeda (Meta Engineering, 2024-12-02): retrieval model complexity up 10,000x versus the prior system, +6% retrieval recall and +8% ads quality on selected segments, runs on NVIDIA Grace Hopper and Meta MTIA silicon [Official, 2024-12].
- GEM (Generative Ads Recommendation Model, Meta Engineering, 2025-11-10): the largest Meta ads foundation model, too large to serve directly, so its learnings are transferred to the runtime ranking fleet through distillation and other post-training techniques. Meta reported about +5% ad conversions on Instagram and +3% on Facebook Feed in Q2 2025 attributed to GEM [Official, 2025-11].
- Lattice: unified ranking architecture that generalizes across objectives and surfaces instead of many small per-objective models; announced 2023, extended to more stages in 2025. Meta stated it had retired roughly 100 ranking models since 2023 with more consolidation planned (reported via earnings commentary) [Official, 2025; details via secondary sources].

## 2. Entity ID and creative similarity

[Practitioner consensus, 2025 to 2026] Practitioners report, based on Meta guidance shared with agencies, that Andromeda groups visually and semantically similar ads under a shared "entity" for retrieval. Consequences:
- Ten near-identical variations (same video, different headline or color) behave like one retrieval candidate. They do not buy you more reach into new pockets of users.
- Genuinely different concepts (different persona, motivator, format, creator, setting, visual style) are retrieved for different people. That is how you "target" in 2026.
- A Creative Diversity style rating reportedly appeared in Ads Manager in September 2026 [Unverified]. If present, use it as a check, not as a goal.

Rule: count concepts, not ads. An ad set with 30 ads built from 3 concepts has 3 concepts.

## 3. Structural principles

1. Consolidate to the minimum number of ad sets that still respects real business differences. Signal density beats segmentation.
2. Split only for a reason the algorithm cannot see: different optimization event, different margin or value model, different geo or currency or language, different bid strategy or budget owner, legal separation (special ad category), or a deliberate test.
3. Never split by interest, age band, gender or placement. Use breakdowns to observe these, value rules to price them.
4. Keep testing separated from scaling only when the testing method requires it (creative testing tool, A/B test). Otherwise launch new concepts into the main scaling ad set.
5. One conversion event per campaign goal. Optimize for the deepest event that reaches about 50 per ad set per week; if not reachable, move one step up the funnel or consolidate.
6. Avoid auction overlap: ad sets in the same account that target overlapping people compete for the same opportunity and Meta enters only the one with highest total value [Official, long-standing]. Overlap mostly hurts when many small ad sets chase the same audience.
7. Budget per ad set must be able to buy the learning threshold: daily budget >= (50 x target CPA) / 7, about 7 x target CPA per day. If not, consolidate.

## 4. When to split a campaign (decision table)

| Reason | Split? | How |
|--------|--------|-----|
| Different conversion event (purchase vs lead vs app install) | Yes | Separate campaigns |
| Different geo with different currency, language, margin or shipping | Yes, if spend per geo can reach learning threshold | Campaign per geo cluster; otherwise one multi-country campaign with value rules or audience controls |
| Product lines with different margins or AOV | Yes, if spend supports it | Separate campaigns or catalog product sets with value optimization |
| New customer acquisition vs retention measured separately | Sometimes | Use audience segments and new customer goals first; split only if finance needs separate budgets |
| Special ad category (housing, employment, financial products and services, social issues) | Required | Separate campaign flagged with the category |
| Different bid strategy needed (e.g. cost per result goal for scale vs highest volume for tests) | Yes | Separate campaign or ad set |
| Interest groups, age bands, genders, placements | No | Observe with breakdowns, adjust with value rules |
| Creative format (video vs static) | No | Mix formats in the same ad set; use flexible format |
| Testing a new concept | Usually no | Add to scaling ad set, or use the creative testing tool for a clean read |
| Testing a structural hypothesis (manual vs Advantage+, bid strategies) | Yes | Experiments A/B test with split audiences |

## 5. Structure templates by budget tier

Tiers follow the Ads Master standard. Monthly figures are Meta spend only.

### Starter (under $3k per month, under 30 conversions per month)
| Campaign | Objective and goal | Budget | Ads |
|----------|-------------------|--------|-----|
| 1. Core | Sales or Leads, Advantage+ on, highest volume, optimize for the deepest event with at least 10 to 15 per week (often Add to cart, Initiate checkout, Lead) | 90 to 100% | 3 to 6 concepts, 1 to 2 executions each |
| 2. Optional retargeting | Only if site traffic > 5k visitors per month and high consideration | 0 to 10% | 2 to 3 proof-heavy ads |
Notes: one campaign is the default. Do not run A/B tests below 30 conversions per cell; use directional reads and concept rotation. Consider click to message or instant forms if website conversion volume is too thin.

### Growth ($3k to $30k per month, 30 to 300 conversions)
| Campaign | Objective and goal | Budget | Ads |
|----------|-------------------|--------|-----|
| 1. Scaling | Advantage+ sales or leads, one ad set (or 2 to 3 ad sets under Advantage campaign budget if creative sets differ), highest volume or cost per result goal | 70 to 85% | 8 to 15 concepts live, 3 to 6 new per week |
| 2. Testing | Creative testing tool inside scaling ad set, or a small ABO testing campaign | 10 to 20% | 3 to 5 new concepts per test cycle |
| 3. Catalog or retention (if ecommerce with catalog) | Advantage+ catalog ads | 5 to 15% | Catalog templates plus 2 to 3 lifestyle frames |

### Scale ($30k to $300k per month, 300 to 3,000 conversions)
| Campaign | Objective and goal | Budget | Ads |
|----------|-------------------|--------|-----|
| 1. Main Advantage+ sales | Highest value or ROAS goal, value rules for known high value segments | 50 to 70% | 20 to 40 concepts live, 10 to 25 new per week |
| 2. Cost-controlled scaler | Cost per result goal or ROAS goal at target, wider budget than needed (spend follows efficiency) | 15 to 30% | Proven winners and new concepts |
| 3. Creative testing | Creative testing tool or ABO sandbox with highest volume | 5 to 15% | Structured concept tests |
| 4. Catalog | Advantage+ catalog ads, product sets by margin tier | 5 to 15% | Catalog plus video catalog formats |
| 5. Geo or line extensions | Separate campaigns only where economics differ | as needed | Localized concepts |

### Enterprise (over $300k per month, multi market)
- Per market cluster: the Scale template.
- Global creative pipeline feeding all markets, localized with translation and dubbing features, plus native local creators.
- Always-on incrementality program: Conversion Lift or GeoLift each quarter on the main campaign, MMM (Robyn or vendor) calibrated with lift results. Hand off design to `measurement`.
- Central naming taxonomy enforced by API; reporting via Marketing API into a warehouse.
- Business portfolio governance: system users, partner access for agencies, brand safety lists, approvals log.

## 6. Structure by business model

| Model | Default structure | Watch outs |
|-------|-------------------|-----------|
| Ecommerce | Advantage+ sales main campaign + catalog + optional cost-controlled scaler | Feed and event to catalog match, existing customer share, BFCM budget schedules |
| Lead gen (B2C) | Leads campaign, instant forms (higher intent) or website, conversion leads optimization once CRM feedback exists | Lead quality decay; never scale on raw lead CPA |
| B2B SaaS | Leads or website conversions optimized to a qualified event via CRM (MQL/SQL) sent through Conversions API; small budget concentrated in one or two campaigns | Low volume; use value or quality events, avoid demo request fragmentation |
| Local services | One Leads or Calls or Messaging campaign per service area cluster, radius targeting, click to message where response is fast | Radius too small kills delivery; staff response time decides outcomes |
| App | Advantage+ app campaign, optimize to install early then app event or value once volume exists; MMP integration | SKAdNetwork and AEM for iOS, separate iOS and Android only when economics differ |
| Marketplace or publisher | Two sided: separate campaigns per side (supply vs demand) with different events; publishers optimize to subscription or registered user events, not clicks | Cheap clicks inflate traffic with low value; value-based events required |

## 7. Ad account and business portfolio settings that affect structure

| Setting | Where | Recommendation |
|---------|-------|----------------|
| Audience segments (engaged audience, existing customers) | Ad account settings, Advertising settings | Define with website, app, CRM and engagement sources. Required for new versus existing customer reporting and customer acquisition goals in Advantage+ sales |
| Account-level audience controls (minimum age, locations, excluded audiences, employee exclusions) | Ad account settings | Set legal minimum age and excluded employees once, at account level |
| Placement controls (account level) | Ad account settings, Brand safety and suitability | Since August 2026 reports, ad set placement exclusions are being removed in some accounts; account-level placement controls remain the true block [Unverified, 2026-08] |
| Inventory filter, block lists, publisher lists | Brand safety and suitability | Expanded or moderate inventory for most; limited for regulated or sensitive brands |
| Default attribution setting | Ads Manager columns and ad set attribution | Keep the account consistent; document in ads-master/MEASUREMENT.md |
| Spending limit | Payment settings | Set an account spending limit as a safety net for agencies and API automation |
| Two-factor authentication, verified business | Business settings, Security Center | Required for stability and for many policies (see policy module) |
| Datasets (pixel plus CAPI) | Events Manager | One dataset per website or brand, shared to all ad accounts that advertise it |

## 8. Naming convention (copy-paste)

```
Campaign: {Market}_{Objective}_{Type}_{Goal}_{BidStrategy}_{Launch YYYYMMDD}
  e.g.   US_SALES_ADV+_PURCH_VALUE_HV_20261001
         TR_LEADS_MANUAL_CL_CPRGOAL_20260915      (CL = conversion leads)
Ad set:  {AudienceMode}_{Placements}_{Segment or Test}_{YYYYMMDD}
  e.g.   ADVAUD_ADVPLC_BROAD_20261001
         TEST_CONCEPT-PAINRELIEF_20261003
Ad:      {ConceptID}_{Angle}_{Format}_{Creator or Style}_{Hook#}_{Version}
  e.g.   C042_SOCIALPROOF_REEL_UGC-AYSE_H2_V1
```
Keep a concept registry (spreadsheet or ads-master/outputs file) mapping ConceptID to angle, persona, motivator and status. The concept ID lets you aggregate results across ads that share an entity.

## 9. Worked example: consolidating a fragmented account

Situation: ecommerce, $45k per month, 6 campaigns, 27 ad sets (interest stacks, lookalikes, age splits), 140 ads, 82% of ad sets in Learning limited, blended CPA up 30% over 90 days.

1. Pull 90 days ad set data with spend, purchases, CPA, frequency and learning status.
2. Map each ad set to a reason to exist from section 4. 23 of 27 have none.
3. Build the Scale template: one Advantage+ sales campaign (highest value), one cost per result goal campaign at target CPA, one catalog campaign, one testing lane.
4. Move the top 20 ads by spend and CPA (using post IDs to keep social proof) into the new structure. Retire duplicates of the same concept.
5. Launch new structure alongside old, shift budget 30% then 60% then 100% over 7 to 10 days, pausing old ad sets from worst to best.
6. Expected: ad sets exit learning (each now above 50 conversions per week), auction overlap falls, CPM stabilizes. Validate with blended MER and new customer CAC, not only Ads Manager ROAS.
7. Log the change in ads-master/journal and the before and after numbers in the output report.

## 10. Anti-patterns

| Anti-pattern | Why it fails now | Replace with |
|-------------|------------------|-------------|
| One ad set per interest or lookalike | Splits signal, causes auction overlap, Advantage+ audience expands anyway | Broad or Advantage+ audience with suggestions |
| "Dynamic creative" style 1 image x 5 headlines as the only creative input | Same entity, no new retrieval pockets | 5 distinct concepts, each with 1 to 3 executions |
| Separate campaign per placement | Placement is an outcome of auction pricing; manual splits inflate CPM | Advantage+ placements, value rules for price adjustments |
| Duplicating winning ad sets to "scale" | Duplicates compete in the same auction and restart learning | Raise budget on the original, or add new concepts |
| Running dozens of "testing" ad sets at $10 a day | None reach significance, all stay in learning | Fewer, larger tests with the creative testing tool |
| Restructuring every week | Constant learning resets | Change structure at most monthly, creative weekly |
