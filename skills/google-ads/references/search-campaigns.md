# Search Campaigns

> Knowledge as of 2026-10. Search changed more between 2025 and 2026 than in the previous five years: AI Max for Search, the removal of manual language targeting, the September 2026 auto-upgrade of broad match and automatically created assets into AI Max, and ads in AI Overviews and AI Mode. Run the Freshness Protocol before acting.

## 1. Match types in 2026

| Match type | Syntax | What it matches now | Use it for |
|---|---|---|---|
| Exact | [running shoes] | Queries with the same meaning or intent, including close variants (misspellings, plurals, reorderings, synonyms, paraphrases, implied words) | Brand, top revenue queries, low data accounts, competitor terms |
| Phrase | "running shoes" | Queries that include the meaning of the keyword, word order matters when it changes meaning | Mid data accounts, themes where intent drifts with broad |
| Broad | running shoes | Any query related to the keyword, using signals such as the landing page, other keywords in the ad group and the user's recent searches | Non-brand themes with Smart Bidding and at least 30 conversions a month |

Facts that drive decisions:
- Close variants apply to all match types, so exact match is not literal. Treat it as "intent identical". [Official]
- Broad match only makes sense with conversion-based Smart Bidding. Broad match with Manual CPC or Maximize clicks buys irrelevant traffic. [Official guidance, Practitioner consensus]
- Query priority: when a query is identical to a keyword in your account, that keyword is preferred over other keywords and over Performance Max and AI Max keywordless matching, if it is eligible and the ad and bid are competitive. Otherwise Ad Rank and relevance decide. [Official, verify current wording in the help article on how keywords are prioritized]
- Campaign-level broad match setting: Search campaigns that used the campaign-level broad match setting were automatically upgraded to AI Max with search term matching only during September 2026 (text customization and final URL expansion stay off). [Official, 2026-09]
- Keyword limits are rarely binding. The real constraint is signal per ad group.

### Match type strategy by data level

| Primary conversions per campaign per month | Recommended Search keyword strategy |
|---|---|
| Under 15 | Exact and phrase only. Tight themes. Manual CPC, Max clicks with cap, or Maximize conversions without target |
| 15 to 50 | Phrase and exact core, broad on the 1 or 2 best themes only, Maximize conversions or tCPA |
| 50 to 300 | Broad match plus tCPA or tROAS on most non-brand themes, exact for brand and top 20 money queries. Test AI Max with an experiment |
| Over 300 | Consolidated broad and AI Max on non-brand with strict negatives and brand controls, exact for brand, competitor campaigns separate |

## 2. Keyword consolidation

- Group by intent theme, not by match type and not by single keyword. One ad group per theme where one landing page and one message fit every query.
- Remove duplicates across ad groups and campaigns. Duplicates split data and make search terms reports misleading.
- Kill keywords with zero impressions in 90 days (they add nothing, AI matching covers them) except brand and competitor exact terms.
- Keep "low search volume" keywords only if they are exact brand or product SKUs.
- Rule of thumb: 5 to 20 keywords per ad group, 3 to 15 ad groups per campaign. Fewer, bigger themes when Smart Bidding is on. [Practitioner consensus]

## 3. Negative keyword strategy

Negative keywords do not match close variants. A negative must list plurals, misspellings and synonyms explicitly. [Official]

| Level | Applies to | Use for |
|---|---|---|
| Ad group negatives | One ad group | Routing traffic between ad groups (sculpting) |
| Campaign negatives | One campaign | Theme exclusion, routing between campaigns |
| Negative keyword lists (shared) | Many campaigns, Search, Shopping and Performance Max | Standard exclusions: jobs, free, DIY, education, competitors you do not want, irrelevant product types |
| Account-level negative keywords | All Search, Shopping and PMax inventory in the account | Brand safety and absolute never-show terms (adult, offensive, legal risk) |
| PMax campaign negatives | Up to 10,000 per PMax campaign, Search and Shopping inventory only [Official, 2025] | PMax query hygiene |

Negative match types:
- Negative exact [term]: blocks only that exact query.
- Negative phrase "term": blocks queries containing the phrase in that order. Default choice for most lists.
- Negative broad term: blocks queries containing all the words in any order. Use for single words like free, jobs, salary.

Standard negative list starters (adapt to the business, never paste blindly):
- Employment: jobs, job, career, careers, salary, hiring, internship, resume, glassdoor, indeed.
- Free and DIY intent (when selling paid products): free, diy, how to make, template (only if not your product), pdf, torrent, crack.
- Education (when not selling courses): course, class, degree, certification (careful in B2B), definition, meaning, wiki.
- Support for existing customers: login, sign in, customer service, phone number, cancel (route to a support page, not ads, unless brand defense is needed).
- Wrong product types or used goods: used, second hand, rental (if you only sell new).

Workflow:
1. Weekly: search terms report sorted by cost, last 14 days, filter conversions = 0 and cost above 1x target CPA. Add negatives or move themes.
2. Monthly: n-gram analysis over 90 days (see [GAQL and scripts](gaql-and-scripts.md)). Words with cost above 2x target CPA and zero conversions become negative phrase candidates.
3. Before adding, check that the negative does not block converting queries (search the converting terms list for the string).
4. Log large negative additions in the journal so other agents know.

## 4. Responsive search ads (RSAs)

Specs [Official]:
- Up to 15 headlines (30 characters each) and 4 descriptions (90 characters each). Minimum 3 headlines and 2 descriptions.
- 2 display path fields (15 characters each).
- Up to 3 enabled RSAs per ad group.
- Ad strength (Poor, Average, Good, Excellent) is a guide to asset variety, not a performance metric. Do not chase "Excellent" at the cost of message quality. Google has said ad strength is not an Ad Rank input. [Official]

Writing system for one RSA:
| Slot | Count | Content |
|---|---|---|
| Keyword headlines | 3 to 4 | The theme term in natural forms |
| Value proposition | 3 | Outcome, differentiator, proof (numbers you can substantiate) |
| Offer and price | 2 | Price point, discount, free shipping, free trial |
| Trust | 2 | Reviews count and rating, years, certifications, guarantees |
| Call to action | 2 | Specific action plus benefit |
| Brand | 1 | Brand name (pin only if legally required) |
| Descriptions | 4 | 1 benefit and proof, 1 offer and CTA, 1 objection handling, 1 differentiator |

Pinning:
- Pin only for legal, compliance or brand requirements (disclaimers, regulated wording). Pinning reduces the combinations the system can test.
- If you must pin position 1, pin 2 or 3 alternatives to the same position to keep some rotation.
- With AI Max final URL expansion on, pinned assets are not used when a more relevant URL is chosen. With text customization, pinning protects your copy from replacement. [Official, 2025]

Testing ads:
- Do not A/B test single headlines in RSAs by intuition. Use the asset report and the combinations report to remove assets rated Low with at least 5,000 impressions, and replace them.
- For a real message test, use ad variations or a custom experiment, or test two RSAs with different angles in the same ad group and compare conversion rate per impression over at least 100 conversions combined.

## 5. Assets (formerly extensions)

| Asset | Key specs | Rule |
|---|---|---|
| Sitelinks | Link text 25 characters, 2 description lines 35 characters each | 6 to 8 per campaign, each to a distinct, useful page |
| Callouts | 25 characters | 6 to 10, benefits not repeated from headlines |
| Structured snippets | Header plus values of 25 characters | 2 headers minimum |
| Image assets | Square 1:1 and landscape 1.91:1 | Add on all eligible campaigns, real product or service photos |
| Business name and logo | Business name 25 characters | Set at account level, must match the domain owner (advertiser verification) |
| Call | Phone number, call reporting on | Use for local and lead gen, schedule to staffed hours |
| Location | Business Profile link | Required for local, Maps and some new features (Demand Gen Maps, automated promotions) |
| Lead form | Native form | Test in lead gen, with qualifying questions and CRM integration |
| Price, promotion | Prices, offers with dates | Promotion assets for sales periods. Automated promotions may be added from your site [Unverified, from 2026-10-12] |
| Text disclaimers | Required disclosure text | New in 2026 for regulated advertisers, works with final URL expansion [Official, 2026-04] |

Account-level automated assets (dynamic sitelinks, dynamic callouts, dynamic structured snippets, dynamic images, automated promotions) are on by default. Review monthly. Turn off any that create inaccurate claims.

## 6. Quality Score and Ad Rank

Quality Score (1 to 10, keyword level, diagnostic only) = expected CTR + ad relevance + landing page experience, each rated Below average, Average or Above average. [Official]

Ad Rank (auction time, what matters) includes your bid, the quality of your ads and landing page, Ad Rank thresholds, the competitiveness of the auction, the context of the search (location, device, time, the other ads and results), and the expected impact of assets and other formats. [Official]

How to use it:
| Component below average | Fix |
|---|---|
| Expected CTR | Tighter ad groups, keyword in headline, stronger offer, more assets, exclude low intent queries |
| Ad relevance | Theme ad groups so headlines match the query intent; split ad groups with mixed intents |
| Landing page experience | Message match, page speed, mobile usability, clear CTA, original content; hand off to cro |

Do not optimize Quality Score as a KPI. Use it to find structural mismatches. Weighted QS (QS weighted by cost) is useful for trend reporting across a theme.

## 7. Brand vs non-brand

- Brand campaign: exact and phrase brand terms and misspellings, Brand exclusions are not applied here. Bidding: target impression share (absolute top or top, 90% to 95%) with a max CPC cap, or Maximize clicks with cap, or tCPA if brand is competitive.
- Non-brand campaigns: add the brand as negative phrase keywords (all spellings) and, for AI Max and PMax, add your brand list as a brand exclusion.
- Brand incrementality: brand search is often less incremental than reported because organic would catch much of it. Test with a geo holdout or a time-based on/off in a low-risk period when competitors are not bidding on your brand. Check auction insights first: if competitors appear on your brand terms, pausing brand is expensive. [Practitioner consensus]
- Report brand ROAS separately. Never let blended ROAS justify non-brand spend.

## 8. Competitor terms

- Allowed: bidding on competitor names as keywords is generally permitted. Using a competitor's trademark in ad text can be restricted after a trademark complaint. [Official, see policy module]
- Structure: separate campaign, separate budget, separate target. Expect low CTR, low QS (ad relevance), high CPC.
- Message: comparison angle on your own claims ("Switching from X? Get ..."), landing page with a fair comparison. Do not imply affiliation.
- Do not use AI Max text customization on competitor ad groups (it may generate text that references the competitor). Disable text customization for that campaign or use text guidelines.
- Kill rule: if CPA after 60 days is above 2x the non-brand target and no assisted value is proven, pause.

## 9. Settings that still matter

| Setting | Recommended | Why |
|---|---|---|
| Networks: Search partners | Off at launch, test later with segment data | Quality varies by vertical |
| Networks: Display Network in Search | Off | Display expansion in Search campaigns dilutes intent and reporting |
| Locations | "Presence: People in or regularly in your included locations" for local, lead gen, legally restricted, shipping-limited businesses | Default "Presence or interest" sends traffic from outside your market |
| Location exclusions | Same option set to presence | Prevents unwanted geos |
| Language | Manual language targeting is being removed from Search, AI Max and the Search portion of PMax; matching uses ad and landing page language and Google's understanding of the user (late September 2026) [Official, 2026-09 via Google Ads Liaison]. Keep each campaign's ads and landing pages in one language | The setting no longer filters |
| Ad schedule | All hours unless staffed calls or legal reasons; Smart Bidding adjusts by time | Manual schedule bid adjustments are ignored by Smart Bidding (except device -100%) |
| Device | No manual adjustments with Smart Bidding. A -100% device adjustment still excludes the device; on tCPA a device adjustment acts as a target adjustment [Official, verify] | Smart Bidding sets device bids per auction |
| Ad rotation | Optimize | Rotation evenly is a legacy option |
| Auto-tagging | On | Required for GCLID, offline imports, GA4 |
| Final URL suffix | UTM template at account level | Consistent analytics |

## 10. Dynamic Search Ads (legacy)

- DSA is being replaced by AI Max. Google's September 2026 auto-upgrade covered automatically created assets and campaign-level broad match. The DSA auto-migration was delayed to February 2027 [Contested: Google's 2026 announcement said September 2026, mid-June 2026 coverage reports a delay to February 2027 and creation removal around January 2027]. Check Google Ads Help and your account notifications.
- When DSA migrates, all three AI Max features turn on and legacy URL targeting is preserved as URL controls. [Official, 2026]
- Action now: test AI Max on a copy of the DSA traffic through an AI Max experiment before forced migration, and move page feeds and URL exclusions into AI Max URL controls.

## 11. Search campaign launch checklist

1. Conversion goal set to the business outcome, verified firing (see conversion module).
2. Brand terms excluded (negative phrase) from non-brand campaigns; brand list exclusion on AI Max.
3. Networks: Search partners off, Display off.
4. Location option set to Presence where relevant; geo exclusions added.
5. 1 to 2 RSAs per ad group with 12 to 15 headlines and 4 descriptions; Ad strength Good or better.
6. Sitelinks, callouts, snippets, image, business name and logo at campaign or account level.
7. Shared negative lists attached.
8. Bid strategy matched to data level (section 1 table). Budget sized at least 5x to 10x target CPA per day for learning [Practitioner consensus].
9. AI Max decision documented (on, off, or experiment) with reasons.
10. Change logged in the journal and the launch date recorded for learning period analysis.

## 12. Search terms review procedure (weekly, 20 minutes)

1. Pull search terms for the last 14 days (GAQL query Q3 in the GAQL module). Include match type and match source columns (keyword, AI Max, PMax).
2. Sort by cost. For each term above 1x target CPA with zero conversions: add a negative, or route it to a better ad group, or improve the landing page if the intent is right.
3. Sort by conversions. Add converting terms that are not covered by an identical keyword as exact or phrase keywords in the right ad group (gives you query priority and bid control).
4. Check AI Max terms separately: share of spend, CPA and ROAS vs keyword-matched terms.
5. Record what you added in the journal: number of negatives, top excluded themes, expected savings.
