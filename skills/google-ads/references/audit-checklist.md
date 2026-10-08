# Google Ads Audit Checklist (scored)

> Knowledge as of 2026-10. Use with the GAQL queries in [GAQL and scripts](gaql-and-scripts.md). State the data source (connector, export file names) and date range at the top of every audit. Default range: last 30 days for settings and waste, last 90 days for trends, same period last year for seasonality.

## How to score

Severity points: Critical = 10, High = 5, Medium = 3, Low = 1.
- Pass: full points. Partial: half points. Fail: 0. Not applicable: remove from the total possible.
- Score = points earned / points possible x 100.
- Any failed Critical item caps the grade at C regardless of score.

| Grade | Score | Meaning |
|---|---|---|
| A | 90 to 100 | Top tier operation; focus on scale and experiments |
| B | 75 to 89 | Solid; fix High items within 30 days |
| C | 60 to 74 | Material waste or risk; 60-day remediation plan |
| D | 40 to 59 | Major problems; fix measurement and structure before scaling |
| F | under 40 | Rebuild or stop spend until Critical items are fixed |

Report format: score, grade, top 10 issues ranked by estimated monthly impact (currency) and effort, then the full table with status per item.

## A. Measurement and conversion goals

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| A1 | Primary conversions are business outcomes only (purchase, qualified lead, booked call) | Smart Bidding optimizes to primaries | Goals page; Q6 primary_for_goal | Critical | Set micro conversions to secondary |
| A2 | No duplicate primary conversions for the same event (GA4 import plus Google tag) | Double counting inflates results and corrupts bidding | Q6, compare names and categories; Q7 totals vs backend | Critical | Keep one as primary |
| A3 | Primary conversion actions recorded conversions in the last 7 days | Detects broken tags | Q7 by date; Diagnostics | Critical | Escalate to measurement, add data exclusion |
| A4 | Google Ads conversions reconcile with backend within a stable ratio | Trust in data | Backend export vs Q7 for 30 days | High | Measurement investigation |
| A5 | Purchase values dynamic and correct currency, consistent tax and shipping rule | tROAS depends on values | Q6 value settings; sample orders | Critical (ecommerce) | Fix tag value variables |
| A6 | Lead counting set to One; purchases to Every | Lead inflation | Q6 counting_type | High | Change counting |
| A7 | Enhanced conversions on and error-free | Recovers lost conversions | Conversion settings, Diagnostics | High | Enable, fix data fields with measurement |
| A8 | Consent mode v2 active for EEA and UK traffic | Required for EEA features and modeling | Tag diagnostics, measurement confirms | Critical (if EEA traffic) | Measurement implements |
| A9 | Offline conversion import of qualified stages for lead gen and B2B | Lead quality feedback | Conversion actions with import source, last upload date | High (lead gen) | Build OCI through Data Manager with measurement |
| A10 | OCI uploads within 24 to 72 hours and on a supported API version | Late uploads lose value; v22 sunset 2026-10-07 | Upload history, error rate | High | Fix pipeline |
| A11 | Click-through windows match the sales cycle | Undercounting long cycles | Q6 lookback days | Medium | Adjust windows |
| A12 | Attribution model data-driven (unless volume too low) | DDA is default and best supported | Q6 attribution model | Low | Switch |
| A13 | Data exclusions applied for known tracking outages | Prevents bidding on bad data | Shared library, Advanced controls; journal incidents | High | Add exclusions |
| A14 | Conversion value rules documented with a data source | Arbitrary rules distort tROAS | Value rules list vs MEASUREMENT.md | Medium | Remove or document |

## B. Account settings and structure

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| B1 | Brand and non-brand separated (Search, PMax brand exclusions, AI Max brand exclusions) | Honest reporting, budget protection | Q27, Q18, campaign list | High | Split and exclude |
| B2 | Every bid strategy has 15+ conversions in 30 days or is pooled | Signal density | Q1 with bid strategy | High | Consolidate or portfolio |
| B3 | No query served by 3 or more campaigns | Internal competition | Q3 grouped by search term | Medium | Negatives, consolidation |
| B4 | Location option Presence where the business only serves its area | Waste outside market | Q8 positive_geo_target_type; Q20 targeting_location = FALSE share | High | Change to Presence |
| B5 | Search campaigns not opted into Display Network | Low intent traffic | Q8 target_content_network | High | Turn off |
| B6 | Search partners decision based on data | Quality varies | Segment by network | Low | Keep or remove by CPA |
| B7 | Naming convention consistent and parseable | Reporting and scripts | Campaign list | Low | Rename |
| B8 | Auto-tagging on, account-level tracking template or final URL suffix set | Attribution and analytics | Q25 customer.auto_tagging_enabled; settings | High | Enable |
| B9 | Account-level automated assets reviewed (including Automated promotions from 2026-10-12) | Inaccurate claims or offers | Account settings, Assets | Medium | Turn off inaccurate ones |
| B10 | Language: each campaign's ads and landing pages in one language (manual language targeting removed in 2026-09) | Matching now uses ad and page language | Ad copy and landing pages by campaign | Medium | Split mixed-language campaigns |
| B11 | Admin access limited, 2-step verification, ex-users removed | Security | Access and security page | High | Clean up |

## C. Search keywords, match types and negatives

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| C1 | Zero-conversion search term spend under 15% of Search spend | Waste | Q4 sum / Search cost | High | Negatives and restructuring |
| C2 | Search terms reviewed in the last 14 days | Ongoing hygiene | Journal, negative additions in change history (Q24) | Medium | Weekly routine |
| C3 | Shared negative lists exist and are attached to relevant campaigns | Consistent exclusions | Q17 | Medium | Build lists |
| C4 | Brand terms negative in non-brand campaigns | Brand leakage | Q17, Q3 brand terms in non-brand | High | Add negatives |
| C5 | Broad match only on campaigns with conversion-based Smart Bidding | Broad with manual bids buys junk | Q5 match types vs Q8 bid strategy | High | Change bidding or match type |
| C6 | Converting search terms not covered by an identical keyword are added | Query priority and control | Q3 conversions vs keywords | Medium | Add exact or phrase |
| C7 | Cost-weighted Quality Score 6+ on non-brand | Relevance and CPC | Q5 | Medium | Restructure, landing pages |
| C8 | Ad groups with under 100 impressions in 90 days consolidated | Fragmentation | Q30 | Low | Merge |
| C9 | Negative keywords not blocking converting terms | Self-inflicted loss | Compare negatives with converting terms | High | Remove conflicts |
| C10 | Competitor terms isolated with own budget and kill rule | Cost control | Campaign list | Medium | Separate |

## D. Ads and assets

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| D1 | Every Search ad group has at least 1 RSA with 10+ headlines and 3+ descriptions | Asset variety | Q15, ad export | High | Add assets |
| D2 | Pinning used only for legal or brand needs | Pinning limits learning | Q14 pinned_field counts | Medium | Unpin or pin multiple options |
| D3 | Low performing assets replaced after 5,000 impressions | Continuous improvement | Q14 | Medium | Replace |
| D4 | Sitelinks (4+), callouts (4+), structured snippets, images, business name and logo active | CTR and Ad Rank | Assets report | High | Add |
| D5 | Call and location assets for local and lead gen | Leads and Maps eligibility | Assets report | Medium | Add |
| D6 | No disapproved or limited ads on active ad groups | Delivery | Q16 | High | Fix and appeal within 6 months |
| D7 | Claims in ads substantiated and compliant | Policy and legal risk | Manual review vs BRAND.md | High | Rewrite |
| D8 | Landing pages relevant, fast and working | Conversion rate and QS | Q19 speed_score, manual check | High | Hand off to cro |

## E. AI Max for Search

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| E1 | Inventory of campaigns with AI Max on, including auto-upgrades of 2026-09 | Unplanned matching changes | Q8b, campaign settings, labels | High | Document state |
| E2 | AI Max campaigns use conversion-based Smart Bidding | Features need it | Q8 | High | Change bid strategy or disable |
| E3 | Brand exclusions on non-brand AI Max campaigns | Brand leakage | Q18 | High | Add brand list |
| E4 | URL exclusions set when final URL expansion is on | Traffic to wrong pages | Q19 expanded URLs, settings | High | Add exclusions |
| E5 | Text customization reviewed with text guidelines; off for regulated or inaccurate sites | Compliance | Generated assets in asset report | High | Guidelines or off |
| E6 | AI Max term performance compared with keyword terms | Incrementality | Q3b or UI match type AI Max | Medium | Negatives, ad group opt-outs, experiment |
| E7 | AI Max decision backed by an experiment or a documented pre-post read | Avoid paying for cannibalized traffic | EXPERIMENTS.md | Medium | Run AI Max experiment |

## F. Bidding and budgets

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| F1 | Bid strategy matches data level (see bidding module) | Stability | Q1, Q8 | High | Change strategy |
| F2 | Targets derived from unit economics and documented | Profitability | PROJECT_BRIEF.md vs Q8 targets | High | Recalculate |
| F3 | Brand uses impression share or capped strategy, non-brand does not use target impression share | Cost control | Q8 | Medium | Change |
| F4 | Profitable campaigns not limited by budget (lost IS budget under 10%) | Missed profit | Q2 | High | Reallocate budget |
| F5 | Budget-limited campaigns beating targets reviewed after the 2026-08 bidding update | Performance drift toward target | Q2, Q8, CPA vs target | Medium | Tighten target or raise budget |
| F6 | No target changes larger than 20% in one step in the last 30 days | Learning resets | Q24 | Medium | Smaller steps |
| F7 | Seasonality adjustments only for short events and removed after | Bidding distortion | Advanced controls | Medium | Remove stale ones |
| F8 | Shared budgets do not mix campaigns with different targets | Budget flows to easy spend | Q8 explicitly_shared | Medium | Split budgets |
| F9 | Monthly pacing within 0.9 to 1.1 of plan | Budget control | Q23, script S4 | Medium | Adjust with approval |
| F10 | NCA goal configured with data-based new customer value where acquisition matters | Acquisition efficiency | Campaign settings | Medium | Configure with customer lists |

## G. Performance Max

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| G1 | Brand exclusions applied (unless PMax is intended for brand) | Cannibalization | Q18, PMax search terms | High | Add brand list |
| G2 | Channel performance reviewed; Display and YouTube share justified by value | Low quality inventory | Channel performance report, Q9 | High | Exclusions, video, feed fixes |
| G3 | Search terms reviewed and negatives applied | Query hygiene | PMax search terms, Q11 | Medium | Negatives |
| G4 | Each asset group has real horizontal and vertical video | Avoid poor auto videos | Q13 asset types | Medium | Upload video |
| G5 | Final URL expansion off or with URL exclusions | Landing page control | Settings, Q19 | High | Exclusions |
| G6 | Account-level placement exclusions applied | Brand safety | Shared library | Medium | Build list from Q10 |
| G7 | Lead gen PMax only with OCI and qualified primary | Junk leads | Goals, CRM data | Critical (lead gen PMax) | Add OCI or pause |
| G8 | Asset groups themed, under 100, each with adequate assets | Relevance | Q12 | Low | Restructure |
| G9 | PMax incrementality evaluated (uplift experiment or account-level pre-post) | Avoid claiming moved conversions | EXPERIMENTS.md | Medium | Run uplift test |
| G10 | Audience signals use first-party data | Faster learning | Asset group signals | Low | Add Customer Match and converters |

## H. Shopping and retail (Google Ads side)

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| H1 | Merchant Center linked, no account-level suspension or misrepresentation | Shopping stops | Merchant Center status | Critical (ecommerce) | Hand off to commerce-feeds |
| H2 | Product disapprovals under 5% of active products | Lost eligibility | Merchant Center diagnostics | High | commerce-feeds |
| H3 | Products segmented by margin or performance via custom labels | Profit bidding | Q22 custom attributes | High | Labels via commerce-feeds |
| H4 | 80%+ of active products received impressions in 30 days | Zombie products | Q22 vs feed | Medium | Zombie campaign |
| H5 | Price competitiveness and shipping reviewed | CTR and conversion | Merchant Center price insights | Medium | Pricing decisions with owner |
| H6 | Standard Shopping has a defined job if it coexists with PMax | Overlap | Campaign list | Low | Define or remove |
| H7 | Local inventory ads intended or disabled (default on in Standard Shopping from 2026-08-31) | Unintended local traffic | Campaign settings | Low | Decide |

## I. Demand Gen, YouTube, Display and App

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| I1 | View-through conversions reported separately and validated | VTC optimization default on | Columns segmented by conversion type | Medium | Separate reporting, lift test |
| I2 | Demand Gen budgets at least 15x target CPA per day | Learning | Q1, Q8 | Medium | Raise or consolidate |
| I3 | Video creative follows ABCD and includes vertical for Shorts | Performance | Creative review | Medium | creative-strategy brief |
| I4 | Display campaigns migrated or scheduled for Demand Gen migration | Platform change | Campaign list | Low | Use migration tool |
| I5 | Placement and content exclusions for visual inventory | Brand safety | Shared library | Medium | Add |
| I6 | App campaigns split by OS with budgets sized to targets | Learning | Campaign list | Medium (app) | Restructure |

## J. Audiences and first-party data

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| J1 | Customer Match lists uploaded and refreshed in the last 30 days | Signals, exclusions, NCA | Q26 | High | Automate via Data Manager |
| J2 | Existing customers excluded from acquisition-only campaigns | Waste | Campaign audience exclusions | Medium | Add exclusions |
| J3 | Customer list types classified by you (not left to automatic labeling) | NCA accuracy | Audience manager | Low | Classify |
| J4 | Audience segments added in observation on Search for insight | Reporting | Q26 | Low | Add |
| J5 | No sensitive category data used for lists | Policy | List sources | Critical | Delete lists |
| J6 | Remarketing frequency capped where manual | User experience | Campaign settings | Low | Add caps |

## K. Policy and account health

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| K1 | Advertiser verification completed | Ads pause if not | Policy manager | Critical | Complete |
| K2 | No open suspensions or warnings; decisions under 6 months appealed if wrong | Appeal window | Notifications, Policy manager | Critical | Appeal with evidence |
| K3 | Required certifications in place for the category | Eligibility | Policy manager | High | Apply |
| K4 | Site transparency: contact, address, returns, privacy, terms | Misrepresentation risk | Site review | High | cro and owner fix |
| K5 | Trademark authorizations or restrictions known | Ad text eligibility | Disapproval reasons | Low | File authorization |
| K6 | Payment method and backup in place | Account holds | Billing settings | Medium | Add backup |

## L. Experiments, governance and reporting

| ID | Check | Why | How to verify | Severity | Fix |
|---|---|---|---|---|---|
| L1 | At least one experiment completed or running in the last 90 days (Growth tier and above) | Learning velocity | EXPERIMENTS.md, Experiments page | Medium | Plan tests |
| L2 | Auto-apply recommendations off for keywords, broad match, budgets and targets | Unapproved changes | Q25 subscriptions, Recommendations auto-apply | High | Turn off |
| L3 | Change history shows no unexplained large changes | Governance | Q24 | Medium | Investigate |
| L4 | Weekly and monthly reports separate brand, non-brand, PMax and visual campaigns | Decision quality | Outputs folder | Medium | Report template |
| L5 | Alerts for zero conversions, pacing and disapprovals active | Fast detection | Scripts S3 to S5 or tool | Medium | Install scripts |
| L6 | Incrementality evidence exists for brand and PMax at Scale tier and above | Budget decisions | MEASUREMENT.md incrementality table | Medium | Plan geo or lift tests |

## Impact estimation for the top 10 list

| Issue type | Monthly impact estimate |
|---|---|
| Waste (search terms, placements, geos) | Sum of zero-conversion cost in the period x 0.6 (not all can be cut without losing some conversions) [Practitioner rule] |
| Budget-limited profitable campaigns | Lost IS (budget) share x current conversions x margin, capped by budget simulator estimates |
| Wrong primary conversions | Treat as blocking: no reliable estimate until fixed |
| Brand cannibalization in PMax | Brand-attributed PMax conversions x (1 minus estimated incrementality); state the assumption |

Always show the formula and the data source next to every estimate.
