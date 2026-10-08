# LinkedIn Ads Audit Checklist (scored)

> How to use: mark each item Pass, Fail or N/A. Severity weights: Critical 10, High 5, Medium 3, Low 1. Score = sum of weights for Pass / sum of weights for applicable items x 100. State data sources and date ranges at the top. Save as `ads-master/outputs/linkedin-ads/YYYY-MM-DD_linkedin-ads_audit.md`.

## A. Ownership and measurement (run first)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | Ad account owned by the company via Business Manager | Data and access survive agency changes | Business Manager, account roles | High | Transfer ownership |
| A2 | Insight Tag active on all pages, consent compliant | Conversions and retargeting | Tag status, page checks | Critical | Install, fix CMP integration |
| A3 | Event based conversion rules for key actions, attached to campaigns | Optimization and reporting | Conversion rules, campaign settings | Critical | Create rules, attach |
| A4 | Qualified lead definition agreed with sales and documented | Lead quality decisions | MEASUREMENT.md | Critical (lead gen) | Workshop with sales |
| A5 | Lead gen form leads sync to CRM automatically and fast | Speed to lead | Test lead, sync logs | Critical (lead gen) | Native integration |
| A6 | Hidden fields or UTMs carry campaign, ad, audience, offer codes into the CRM | Quality by segment | CRM fields | High | Add and map |
| A7 | CAPI or CRM conversion sync sends qualified stages back | Optimization to quality | Conversion rules with CAPI or CRM source | High | Build with measurement |
| A8 | Monthly reconciliation of LinkedIn vs CRM | Trust | Reconciliation note | Medium | Start monthly |
| A9 | Conversion windows match sales cycle; click and view conversions reported separately | Avoid inflation | Rule settings, reports | Medium | Adjust |

## B. Structure and settings

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | One objective and one audience per campaign | Readable results | Campaign list | High | Restructure |
| B2 | Campaign groups map to programs or funnel stages | Budget control | Group list | Medium | Regroup |
| B3 | Naming convention consistent | Reporting and API | Names | Low | Rename |
| B4 | Audience expansion off for lead gen and ABM (or tested) | ICP precision | Campaign settings | High | Turn off |
| B5 | LinkedIn Audience Network off for lead gen and ABM (or tested) | Lead quality | Campaign settings | High | Turn off |
| B6 | Campaign count fits budget (each campaign can buy 30+ results per month or has a clear awareness role) | Learning | Budget vs cost per result | Medium | Consolidate |
| B7 | No overlapping audiences across simultaneous campaigns | Self competition, frequency | Audience definitions | Medium | Exclusions |

## C. Targeting and ABM

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | ICP match 70%+ in Demographics report for lead gen and ABM | Paying for the right people | Demographics report | High | Tighten, exclude |
| C2 | Exclusions: customers, employees, competitors, students and job seekers where relevant | Waste | Exclusion settings | High | Add |
| C3 | Audience sizes fit purpose (cold 20k+; retargeting and ABM 300+) | Delivery | Forecast panel | Medium | Resize |
| C4 | Company list match rate 60%+ | ABM reach | List details | Medium | Clean list, add domains and URLs |
| C5 | Retargeting ladder exists (visitors, video viewers, document readers, form openers) | Cheapest high intent pool | Matched audiences | High | Build |
| C6 | Buying committee roles covered for priority accounts | Committee selling | Audience plan, Demographics | Medium | Add role campaigns |
| C7 | Company engagement report reviewed and shared with sales (ABM) | Sales activation | Journal, sales notes | Medium | Weekly routine |
| C8 | Lists refreshed in last 30 days | Accuracy | Upload dates | Low | Refresh |

## D. Creative and offers

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | 2 to 4 active ads per campaign | Testing and fatigue control | Ad list | Medium | Add ads |
| D2 | No ad with CTR down 30%+ from its first 2 weeks still running without refresh plan | Fatigue | Ad trend | Medium | Refresh |
| D3 | Offer matches stage (value for cold, proof for warm, meeting for hot) | Conversion and quality | Offer map | High | Re-map offers |
| D4 | Thought Leader Ads tested (with permissions) | Engagement upside | Campaign history | Medium | Test |
| D5 | Native formats used (document, video) for demand creation | Engagement | Format mix | Medium | Add |
| D6 | Specs and copy lengths fit mobile (no truncated hooks) | Performance | Previews | Low | Edit |

## E. Lead gen forms

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Form fields limited to what sales uses | Completion | Form review | Medium | Remove fields |
| E2 | Qualifying question on high value offers | Quality | Form review | High | Add |
| E3 | Higher intent option considered when quality is poor | Quality | Form settings | Medium | Test |
| E4 | Privacy policy and consent text correct | Compliance | Form | Critical | Legal review |
| E5 | Thank you screen offers next step | Speed to meeting | Form | Low | Add calendar link |
| E6 | Completion rate tracked by form | Friction | Form report | Medium | Track |

## F. Bidding, budgets, frequency

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Bidding fits audience size (Manual for small ABM, Maximum delivery or Cost cap otherwise) | Cost control | Campaign settings | High | Change |
| F2 | Cost caps derived from economics and observed cost | Delivery and profit | Cap vs data | Medium | Reset |
| F3 | Budget per campaign supports learning | Results | Budget vs cost per result | Medium | Consolidate |
| F4 | Pacing within 0.9 to 1.1 of plan | Control | Pacing calc | Medium | Adjust |
| F5 | Frequency monitored; refresh before fatigue | Efficiency | Frequency vs CTR | Medium | Rotate creative |
| F6 | Demand creation share protected and measured on the right KPIs | Future pipeline | Budget split, KPIs | High | Rebalance |

## G. Reporting, testing, governance

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Monthly pipeline report by program from CRM | Business outcome | Reports | High | Start |
| G2 | At least one A/B test per month at Growth tier and above | Learning | EXPERIMENTS.md | Medium | Plan |
| G3 | Lift or holdout test in last 12 months (Scale and above) | Incrementality | Test records | Medium | Plan |
| G4 | Change log matches approved change lists | Governance | Journal vs history | High | Investigate |
| G5 | Thought Leader permissions recorded | Compliance | Records | High (if TLA used) | Record |
| G6 | API or MCP integrations use pinned versions and least privilege | Stability, security | Integration config | Medium | Pin, restrict |

## Scoring rubric

| Score | Grade | Meaning | Next step |
|-------|-------|---------|-----------|
| 90 to 100 | A | Well run | Scale and test plays |
| 75 to 89 | B | Solid with gaps | Fix High items in 2 weeks |
| 60 to 74 | C | Material waste or quality risk | Fix Critical and High; re-audit in 30 days |
| under 60 | D | Unreliable | Pause scaling; rebuild measurement and structure |

Override rule: any failed Critical item caps the grade at C; a failed A2, A3 or E4 caps it at D until fixed.

## Quick audit (20 minutes, when time or access is limited)
Check these 10 items first; they catch most of the waste:
1. A2 Insight Tag active.
2. A4 Qualified lead definition exists.
3. A5 Lead sync to CRM working.
4. B4 Audience expansion off for lead gen and ABM.
5. B5 LinkedIn Audience Network off for lead gen and ABM.
6. C1 ICP match from the Demographics report.
7. C2 Exclusions in place.
8. D2 Fatigued ads still running.
9. F1 Bidding fits audience size.
10. G1 Monthly pipeline report exists.
Report the quick audit as "partial" and schedule the full audit.

## Audit report template
```
# LinkedIn Ads audit: <account>
Date: YYYY-MM-DD | Data: <exports, CRM report>, <ranges>
Score: <n>/100 (<grade>) | Critical fails: <list>
## Top 10 fixes (impact x confidence x ease)
| # | Item | Fix | Expected impact | Effort | Approval |
## Waste quantified (off ICP spend, overlapping audiences, fatigued ads)
## Pipeline view (cost per SQL, pipeline per dollar by program)
## Handoffs requested
## Next audit date
```
