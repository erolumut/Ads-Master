# Meta Ads Audit Checklist (scored)

> Knowledge as of 2026-10. Run fully at intake and quarterly; run sections A and G monthly. Each item: check, why, how to verify, severity, fix. Score at the end. State the data sources and date ranges used.

Severity weights: Critical = 10 points, High = 6, Medium = 3, Low = 1.
Result per item: Pass = full points, Partial = half points, Fail = 0, N/A = excluded from the maximum.

## A. Measurement and signal (largest weight)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| A1 | Pixel and Conversions API both send the primary conversion event | Server events recover signal lost in browsers | Events Manager > event > "Received from" Browser and Server | Critical | Implement CAPI (partner integration, Gateway or server-side GTM); hand off to `measurement` |
| A2 | Deduplication works (same event_name and event_id) | Double counting inflates results and misguides bidding | Events Manager dedup status; compare purchases to backend | Critical | Pass identical event_id from browser and server |
| A3 | EMQ for Purchase or Lead is 7+ | Better matching improves delivery and attribution | Events Manager EMQ | High | Add email, phone, external_id, fbp, fbc, IP, user agent |
| A4 | Purchase value and currency correct and consistent with backend definition | Value optimization and ROAS depend on it | Compare 30-day Meta value vs backend (same attribution caveats) | High | Fix value (tax, shipping, discounts policy) |
| A5 | Optimization event is the deepest event with enough volume | Shallow events find shallow buyers | Ad set settings vs weekly event counts | High | Move down the event ladder when volume allows |
| A6 | Lead gen: CRM stages sent back (conversion leads or custom events) | Optimizes for quality, not form fills | Events Manager CRM events, lead stage mapping | High (lead gen) | CAPI for CRM integration |
| A7 | Catalog content_ids match catalog IDs (90%+) | Catalog retargeting and personalization | Commerce Manager match rate | High (catalog) | Align IDs, variants |
| A8 | Data restriction status known (health, finance categories) | Explains blocked events and delivery limits | Events Manager dataset settings | High | Appeal misclassification or adapt plan |
| A9 | Attribution settings documented and reporting pipelines updated for 2026-01-12 and 2026-03-03 changes | Prevents false performance conclusions | MEASUREMENT.md, BI queries | Medium | Update docs and API requests |
| A10 | Backend reconciliation exists (MER, new customer CAC weekly) | Platform numbers alone over-credit | Weekly report | High | Build reconciliation with `measurement` |
| A11 | Incrementality evidence within the last 12 months (lift, geo, holdout) | Calibrates targets to causal value | MEASUREMENT.md Incrementality table | Medium (High at Scale and above) | Plan a lift or GeoLift test |
| A12 | Consent handled per region (EU, UK, Turkey KVKK, US LDU) | Legal risk and data quality | `measurement` consent audit | High | Fix CMP and event gating |

## B. Account structure

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| B1 | Each campaign and ad set has a documented reason to exist | Fragmentation splits signal | Structure map vs decision table in account-structure | High | Consolidate |
| B2 | Under 20% of spend in Learning limited ad sets | Unstable delivery | Delivery column, 28 days | High | Consolidate, raise budget, move event up |
| B3 | No interest, age or placement split ad sets | Advantage+ expands anyway; overlap | Ad set targeting review | Medium | Merge into broad or Advantage+ audience |
| B4 | No significant auction overlap | Self-competition | Delivery insights | Medium | Merge overlapping ad sets |
| B5 | Budget per ad set at least about 7 x target CPA per day (or plan to reach threshold) | Learning threshold | Budget vs CPA | Medium | Consolidate or change event |
| B6 | Naming convention consistent | Analysis and automation | Name sample | Low | Rename at next rebuild |
| B7 | Audience segments defined in ad account settings | New vs existing reporting and controls | Ad account settings | High (ecommerce) | Define with CRM list and events |
| B8 | Account-level controls set (minimum age, excluded employees, brand safety, placement controls) | Compliance and waste | Ad account settings | Medium | Configure |

## C. Campaign settings and bidding

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| C1 | Objective matches the business event | Wrong objective trains the wrong behavior | Campaign objective vs goal | Critical | Rebuild with correct objective |
| C2 | Bid strategy matches maturity and constraint | Tight goals choke delivery; loose ones overspend | Bid strategy vs volume and targets | High | Per bidding module |
| C3 | Cost per result goal or ROAS goal values derived from unit economics | Prevents arbitrary targets | Compare with PROJECT_BRIEF unit economics | High | Recompute targets |
| C4 | Value optimization used where values vary and volume allows | Captures AOV and LTV differences | Performance goal | Medium | A/B test highest value |
| C5 | Advantage+ levers on unless documented reason | Liquidity and automation | Campaign Advantage+ status | Medium | Turn on or document reason |
| C6 | Advantage+ creative enhancements reviewed (no unwanted generative text in regulated verticals) | Brand and claims risk | Ad level settings and previews | High (regulated) | Turn off risky enhancements |
| C7 | Special ad category declared where required | Policy compliance | Campaign settings | Critical (if applicable) | Declare and rebuild |
| C8 | Budget scheduling or lifetime budgets used for planned peaks | Captures demand spikes without manual edits | Campaign settings | Low | Configure before events |
| C9 | Value rules only where backed by backend data | Avoids breakdown-effect mistakes | Value rule list vs evidence | Medium | Remove or justify |
| C10 | No frequent edits (under 1 significant edit per ad set per week) | Learning resets | Activity history | Medium | Batch edits weekly |
| C11 | Existing customer share controlled where acquisition is the goal | Wasted acquisition budget | Audience segment breakdown | Medium (ecommerce) | New customer controls |
| C12 | UTM parameters with ID macros on all ads | Cross-checks in analytics | Ad URL parameters | Medium | Add template |

## D. Creative

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| D1 | Number of distinct concepts live meets tier minimum | Diversity drives retrieval reach | Creative registry, ad review | Critical | Brief new concepts (`creative-strategy`) |
| D2 | New concepts launched in the last 14 days (Growth and above) | Fatigue prevention | Ad created dates | High | Weekly creative cadence |
| D3 | Format mix includes 9:16 video, 4:5 static or video, and carousel or catalog where relevant | Placement coverage | Asset review | High | Produce missing formats |
| D4 | Reels and Stories assets respect safe zones | Hidden text and CTAs | Preview in placements | Medium | Re-export |
| D5 | Top ad under 50% of spend | Single point of failure | Spend share | Medium | Scale concept diversity |
| D6 | Creative testing method defined (testing tool, ABO sandbox, BAU) with kill rules | Consistent learning | EXPERIMENTS.md, process doc | Medium | Adopt creative module method |
| D7 | Partnership or creator content tested (where category allows) | Often efficient new concepts | Ads list | Low | Pilot 2 to 3 creators |
| D8 | Fatigue signals monitored (frequency, CTR trend) | Early refresh | Weekly report | Medium | Add to weekly report |
| D9 | Ads comply with claims and personal attributes policy | Disapprovals and restrictions | Ad review vs policy module | High | Rewrite |

## E. Audiences and exclusions

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| E1 | Purchasers or current customers excluded where appropriate | Waste | Custom audience exclusions | Medium | Add exclusions |
| E2 | Customer lists refreshed at least monthly (weekly ideal) | Accurate segments and exclusions | Audience last updated | Medium | Automate sync |
| E3 | Retargeting share of spend justified (5 to 15% typical) | Over-credited spend | Spend split | Medium | Reduce or test incrementality |
| E4 | No reliance on deprecated options (detailed targeting exclusions, removed interests) | Broken campaigns | Ad set warnings | Low | Rebuild |

## F. Lead gen, messaging, catalog specifics (score only relevant items)

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| F1 | Instant forms use higher intent or qualifying questions | Lead quality | Form settings | High (lead gen) | Edit form |
| F2 | Speed to lead under 5 minutes in business hours | Contact and close rate | CRM timestamps | High (lead gen) | Process fix with human |
| F3 | Lead quality KPIs reported (cost per SQL) | Optimizing on wrong KPI | Weekly report | High (lead gen) | Add CRM metrics |
| F4 | Click to message has greeting, ice breakers, response SLA, outcome tracking | Conversations convert only with response | Message template, inbox stats | High (messaging) | Configure |
| F5 | Catalog feed healthy (no blocking errors, stock sync) | Catalog delivery | Commerce Manager diagnostics | High (catalog) | `commerce-feeds` |
| F6 | Product sets aligned with margin and bestsellers | Profit | Product set rules | Medium (catalog) | Custom labels |

## G. Policy and account health

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| G1 | No active restrictions; Account Quality clean | Business continuity | Account Quality | Critical | Policy play |
| G2 | Business verified; 2+ admins with 2FA | Recovery | Business settings | High | Complete |
| G3 | Disapproval rate under 5% of ads in 30 days | Repeated violations escalate | Ads with rejected status | High | Fix patterns |
| G4 | Payment method and backup valid, spending limit headroom | Delivery stops | Billing | High | Update |
| G5 | Brand safety controls set (inventory filter, block lists) | Brand risk | Brand safety settings | Medium | Configure |
| G6 | Regulated category permissions or verification in place (financial services verification, gambling, alcohol, pharma) | Legal and policy | Business settings, written permissions | Critical (if applicable) | Apply |

## H. Reporting and operations

| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| H1 | Weekly report with decomposition and change list exists | Discipline | outputs folder | Medium | Use template |
| H2 | Experiments logged with hypothesis and stop rule | Compounding learning | EXPERIMENTS.md | Medium | Backfill |
| H3 | Changes logged in journal with dates | Root cause analysis | journal | Medium | Adopt protocol |
| H4 | Freshness check done in last 30 days | Platform changes | Journal entries | Low | Run protocol |

## Scoring rubric

```
Score % = (sum of points earned) / (sum of maximum points for applicable items) x 100

Grade:
  90 to 100  A  Top tier. Focus on creative volume, incrementality and scaling.
  75 to 89   B  Solid. Fix High items within 30 days.
  60 to 74   C  Material waste likely. Fix Critical and High items before scaling spend.
  40 to 59   D  Structural problems. Freeze scaling, rebuild measurement and structure.
  under 40   F  Do not increase spend. Rebuild from tracking up.

Override rules:
  Any Critical item failed in section A or G caps the grade at C.
  Two or more Critical fails cap the grade at D.
```

Audit output structure (save as ads-master/outputs/meta-ads/YYYY-MM-DD_meta-ads_audit.md):
1. Summary: grade, score, top 5 issues by impact, estimated impact range and confidence.
2. Data used: sources, date ranges, attribution settings, access level.
3. Scored table by section (ID, result, evidence, fix).
4. Prioritized action plan: impact x confidence x ease, with owners (agent slug or human).
5. Change list for approval.
6. Handoffs requested.
