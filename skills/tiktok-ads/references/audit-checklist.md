# TikTok Ads Audit Checklist (scored)

> Knowledge as of 2026-10. Use for new account takeovers, quarterly audits and recovery work. Mark each item Pass, Fail or N/A. State the data source and date range at the top of the audit. Severity weights: Critical = 5, High = 3, Medium = 2, Low = 1.

Audit header:
```
Account: <name / advertiser ID> | Business model: | Tier: | Maturity:
Data used: <exports / connector / MCP>, <date range>, attribution: <setting>
Auditor: tiktok-ads | Date: YYYY-MM-DD
```

## A. Ownership, access and account health

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| A1 | Brand owns the Business Center; agency has partner access only | Asset loss when agencies change | BC settings > owner | Critical | Transfer ownership; re-share assets |
| A2 | At least 2 admins, all users with 2-step verification | Lockouts and hijacks cause suspensions | BC members list | High | Add admin, enforce 2SV |
| A3 | No active suspension, warnings or verification requests | Delivery risk | Account status banner | Critical | Recovery play |
| A4 | Ad account time zone and currency match backend reporting | Reconciliation errors | Account info | Medium | New account if wrong and material |
| A5 | Backup payment method on file | Delivery stops on card failure | Billing | Medium | Add backup |
| A6 | Rejected ad rate under 5% of ads submitted in 90 days | Policy risk accumulates | Ads with rejected status | High | Fix root causes; claims review |
| A7 | Restricted category licenses or certificates on file (if applicable) | Rejections and suspensions | Account qualifications page | High | Submit documents |

## B. Measurement

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| B1 | Pixel installed and firing on all key pages | No signal, no optimization | Events Manager, Pixel Helper | Critical | Install or fix |
| B2 | Events API sending the primary conversion | Browser signal loss | Events Manager source split | Critical | Implement Events API (measurement handoff) |
| B3 | event_id deduplication for events sent by both sources | Double counting inflates results | Test Events, dedup diagnostics | Critical | Shared event_id (order ID) |
| B4 | Purchase values and currency correct (AOV within 10% of backend) | Value bidding and ROAS depend on it | Compare AOV | High | Fix value mapping |
| B5 | Event match quality on Purchase or Lead stable and not low | Attribution and optimization quality | Events Manager EMQ | High | Send hashed email, phone, external_id, ttclid, _ttp, IP, UA |
| B6 | Advanced matching enabled | Match rates | Pixel settings | Medium | Enable |
| B7 | Optimization event is the business's primary conversion (or the deepest event with enough volume) | Optimizing to shallow events buys the wrong users | Ad group settings | High | Move event deeper when volume allows |
| B8 | Attribution windows documented and consistent across compared ad groups | Invalid comparisons | Ad group attribution settings | Medium | Align; record in MEASUREMENT.md |
| B9 | UTMs on all ads | GA4 triangulation | Ad URLs | Medium | Add UTM template with macros |
| B10 | Triangulation in place (survey, GA4, MER or lift) | Platform over-credit | MEASUREMENT.md | High | Add post-purchase survey; plan lift test |
| B11 | App: MMP integrated, SAN windows set, SKAN configured | App measurement | MMP and Ads Manager | Critical (apps) | Fix integration |
| B12 | Lead gen: CRM stages flowing back via Events API | Optimize for quality | Events Manager CRM events | High (lead gen) | Build CRM event pipeline |
| B13 | Consent handling for EEA and UK traffic | Legal and data quality | CMP behavior with pixel | High (EU/UK) | Measurement handoff |

## C. Structure and settings

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| C1 | Number of active conversion ad groups is consistent with budget (each can reach ~50 conversions per 7 days, or at least 25) | Fragmentation keeps ad groups in learning | Conversions per ad group | High | Consolidate |
| C2 | Daily budgets at least 10x target CPA per conversion ad group (Smart+ Web 10x to 30x) | Learning and delivery | Budget vs CPA | High | Raise or consolidate |
| C3 | Separate creative testing lane exists (Growth tier and above) | Testing inside scaling campaigns starves new ads | Campaign list | Medium | Add manual testing campaign |
| C4 | Smart+ used where signal allows; module overrides documented | Automation gains with control where needed | Campaign settings | Medium | Migrate or document |
| C5 | Placements deliberate: TikTok Ad Network / Pangle and Lemon8 tested, not default | Off-platform inventory can waste spend | Placement breakdown | High | Exclude or run as test cell |
| C6 | Automatic Search Placement status known; Search Ads Campaign for brand terms at Scale tier | Captures high-intent demand | Settings and campaign list | Medium | Add Search Ads Campaign |
| C7 | Naming convention consistent | Reporting and automation | Names | Low | Apply convention |
| C8 | No duplicate campaigns competing for the same audience and event without a test reason | Self-competition | Campaign list | Medium | Merge |
| C9 | Dayparting used only with a documented reason | Unneeded dayparting cuts signal | Ad group schedules | Low | Remove |
| C10 | Change log exists for the last 30 days | Explains performance shifts | Journal or history | Medium | Start change log |

## D. Bidding and budgets

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| D1 | Bid strategy matches volume (Maximum Delivery under ~25 conversions per week) | Caps starve learning | Ad group bid settings | High | Switch to Maximum Delivery |
| D2 | Cost Cap or Minimum ROAS set from trailing actuals, not aspirations | Under-delivery | Cap vs trailing CPA or ROAS | High | Reset caps |
| D3 | Targets calibrated to incrementality or triangulation | Over-credit leads to over-spend | Plan documents | High | Calibration procedure |
| D4 | Budget changes follow step limits | Learning resets | History | Medium | Adopt step rules |
| D5 | Spend pacing matches plan within 10% | Budget control | Spend vs plan | Medium | Adjust budgets |
| D6 | Value-based bidding only with accurate values and enough purchases | Value bidding on bad data | B4 and volume | Medium | Return to CPA bidding |

## E. Audiences

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| E1 | Broad or automatic targeting used for scaling; narrow cells justified by tests | Narrow targeting raises CPM | Ad group targeting | Medium | Broaden |
| E2 | Legal guardrails enforced (age, geo) for restricted categories | Compliance | Audience controls | Critical (regulated) | Enforce |
| E3 | Purchaser or customer exclusions set where new customer acquisition is the KPI | Paying for existing customers | Exclusions | Medium | Add Customer File exclusions |
| E4 | Retargeting share within 10% to 20% unless proven incremental | Over-investment in least incremental spend | Spend split | Medium | Reduce or test |
| E5 | Custom audiences refreshed (customer files within 30 to 60 days) | Stale seeds | Audience dates | Low | Refresh |

## F. Creative

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| F1 | All ads 9:16, sound on, native style | Non-native ads underperform | Ad previews | High | Rebuild |
| F2 | Hook visible in first 3 seconds; product by second 3 | Thumb-stop | Previews, hook rate | High | New hooks |
| F3 | New creative cadence meets tier target (creative-for-tiktok.md section 6) | Fatigue | Ads launched per week | High | Creative pipeline |
| F4 | At least 3 distinct concepts live in each scaling campaign | Concentration risk | Concept register | High | Add concepts |
| F5 | Fatigue monitoring in place (CTR and 6s rate vs first 7 days) | Silent decay | Report | Medium | Add to weekly report |
| F6 | Creative register maps ad to concept, hook, creator | Learning compounds | Register | Medium | Build register |
| F7 | Music licensed (CML or original) | Rejections, muting | Ad audio | Medium | Replace audio |
| F8 | AI-generated content disclosed; no fake testimonials | Policy and trust | Review | High | Label or remove |
| F9 | Claims match approved claims in BRAND.md | Rejections, legal | Review | High | Edit |
| F10 | Captions and key text inside safe zones | Readability | Previews | Low | Re-edit |

## G. Spark Ads and creators

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| G1 | Creator or Spark content share of spend at least 30% at Growth tier and above | Native trust drives performance | Spend by identity type | Medium | Creator program |
| G2 | Spark codes valid through planned flights; expiry tracked | Ads stop when codes expire | Creator register | Medium | Renew codes |
| G3 | Creator contracts cover usage, duration, edits, AI rights and disclosure | Legal exposure | Contracts | High | Update template |
| G4 | Branded content disclosure on sponsored creator posts | Regulatory | Post settings | High | Enable disclosure |
| G5 | Spark Ad comments moderated | Brand risk and CVR | Comments | Low | Daily moderation |

## H. TikTok Shop and GMV Max (if applicable)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| H1 | Breakeven ROI computed with all Shop costs | Target ROI too low loses money | Calculation in plan | Critical | Compute (tiktok-shop-and-gmv-max.md section 3) |
| H2 | Target ROI set from trailing actuals and breakeven | Non-delivery or losses | GMV Max settings | High | Reset |
| H3 | Creative supply adequate (LIVE: 50 to 70 videos in queue) | Delivery and fatigue | Creative queue | High | Add videos and affiliates |
| H4 | Edits limited to one daily window; ROI protection eligibility understood | Protection and stability | Change history | Medium | Edit discipline |
| H5 | Affiliate program active with commission fitting margin | Content supply and sales | Affiliate center | Medium | Set up or adjust |
| H6 | Total Shop GMV (all sources) tracked alongside ads GMV | Cannibalization check | Seller Center | High | Add to weekly report |
| H7 | Product listings healthy (images, video, reviews, price) | Conversion | Listing audit | High | commerce-feeds handoff |

## I. Lead generation (if applicable)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| I1 | Leads reach CRM within minutes | Speed to lead | Integration logs | Critical (lead gen) | CRM integration |
| I2 | Qualifying questions on Instant Forms | Lead quality | Form setup | High | Add 2 to 4 questions |
| I3 | Reporting on CPQL and cost per opportunity | Quality optimization | Reports | High | Join CRM data |
| I4 | Off-platform placements excluded or proven | Junk lead risk | Placement breakdown | Medium | Exclude |

## J. Reporting and process

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| J1 | Weekly report with calibrated KPIs exists | Decisions on wrong numbers | Outputs folder | Medium | Start weekly report |
| J2 | Experiments logged with hypothesis, metric and stop rule | Learning | EXPERIMENTS.md | Medium | Log tests |
| J3 | Rep-enabled features and betas recorded | Continuity | Memory file | Low | Record |
| J4 | Freshness check run in the last 30 days | Platform changes | Journal | Low | Run Freshness Protocol |

## Scoring rubric

```
Score = 100 x (sum of weights of Pass items) / (sum of weights of all applicable items)
```

| Score | Grade | Meaning | Next step |
|-------|-------|---------|-----------|
| 90 to 100 | A | Well run; gains come from creative volume and scaling | Scale playbook |
| 75 to 89 | B | Solid with fixable gaps | Fix High items within 2 weeks |
| 60 to 74 | C | Material waste or risk | 30-day remediation plan |
| Under 60 | D | Structural problems | Remediation before any budget increase |

Override rules:
- Any Critical item failed in sections A or B caps the grade at C, regardless of score.
- Two or more Critical fails in any section cap the grade at D.
- Report the top 5 fixes ranked by impact x confidence x ease, each with an owner (tiktok-ads, measurement, creative-strategy, commerce-feeds, cro or human).

Audit output sections: Executive summary (score, grade, top 5 fixes), Findings by section (table with ID, status, evidence, fix), Quick wins (under 1 hour), 30-day plan, Handoffs requested, Data used and gaps.
