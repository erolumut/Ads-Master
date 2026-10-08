# Growth System Audit Checklist

Scores the growth system as a whole: goals, economics, measurement, mix, allocation, experimentation, creative supply, organic and AI visibility, operations and governance. Channel level audits belong to each channel agent; this audit uses their outputs as evidence.

How to score: each item is Pass (2), Partial (1) or Fail (0). Severity sets the weight: Critical x3, High x2, Medium x1. Section score = weighted points earned / weighted points possible. Report findings with the AUDIT_REPORT.md template in `ads-master/templates/`.

## A. Strategy and goals
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | One primary quarterly goal with a metric and target in STRATEGY.md | Competing goals produce competing bids and priorities | Read STRATEGY.md | Critical | Draft STRATEGY.md with one objective |
| A2 | Hard constraint stated (max CPA, min ROAS or MER, payback) | Agents need a ceiling to optimize against | PROJECT_BRIEF.md section 4 | Critical | Derive from unit economics |
| A3 | Every channel has a role, budget share, primary and guardrail KPI | A channel without a role cannot be judged | STRATEGY.md channel roles | High | Channel mix plan |
| A4 | "Not doing" list exists | Focus is a decision | STRATEGY.md | Medium | Add with reasons |
| A5 | Targets reviewed in the last 90 days | Economics and markets move | File dates, journal | Medium | Quarterly reset |

## B. Unit economics
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Contribution margin computed with all variable costs | Breakeven ROAS depends on it | PROJECT_BRIEF.md section 3, finance source | Critical | Unit economics sheet |
| B2 | Breakeven ROAS and CPA documented and shared with channel agents | Prevents unprofitable "good ROAS" | PROJECT_BRIEF, agent outputs | Critical | Publish targets |
| B3 | New vs returning customer split available | nCAC and aMER need it | Backend report | High | Measurement request |
| B4 | LTV by cohort (6 and 12 months) | Sets allowable CAC | Cohort data | High | Build cohort table |
| B5 | Lead gen: lead to SQL and SQL to closed won rates by channel | CPL alone misleads | CRM | Critical (lead gen) | CRM reporting + offline conversions |
| B6 | Taxes and fees on media included in CAC (for example Turkey withholding) | True cost differs from platform spend | Finance, geo module | High (where applicable) | True media cost multiplier |
| B7 | Margin passed into conversion values (POAS) where margins vary by product | Revenue bidding over-funds low margin items | Feed custom labels, value rules | Medium | commerce-feeds + measurement |

## C. Measurement foundation (evidence from measurement agent)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Primary conversions verified against backend within 20% | Every bidding algorithm trains on this | measurement health check | Critical | Tracking break workflow |
| C2 | Server-side events (CAPI, enhanced conversions, Events API) with dedup | Signal loss from browsers and consent | measurement output | High | measurement |
| C3 | Consent management and consent signals where required (EU, UK, Turkey KVKK) | Legal and signal quality | CMP check | Critical (regulated geos) | measurement |
| C4 | Offline or CRM conversion import for lead gen | Optimize on quality | measurement output | Critical (lead gen) | measurement |
| C5 | Incrementality test on the largest channel in the last 12 months | Attribution overstates | MEASUREMENT.md incrementality table | High | Lift or geo test |
| C6 | MMM in place at Enterprise tier (or planned at Scale) | Portfolio allocation | MEASUREMENT.md | Medium | Meridian or Robyn project |
| C7 | UTM governance and AI referral channel grouping | Clean attribution and AI visibility tracking | GA4 channel groups | Medium | measurement |

## D. Channel mix
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Channel count fits the tier (Starter 1 to 2, Growth 2 to 4, Scale 4 to 7) | Too many starves learning | Spend by channel | High | Consolidate or add |
| D2 | Each paid channel funded at or above its minimum viable budget | Below it, results are noise | MVB formula vs spend | High | Fund or pause |
| D3 | Demand creation and demand capture both present at Growth tier and above | Capture alone saturates | Channel roles | Medium | Add creation channel |
| D4 | No single channel above about 60% at Scale tier without incrementality proof | Platform risk | Spend share | Medium | Diversify test |
| D5 | Retargeting under about 10 to 20% of paid spend | Low incrementality | Campaign spend | Medium | Cap and test |
| D6 | Marketplace and retail media considered where the client sells on marketplaces | Demand sits there | PROJECT_BRIEF section 6 | Medium | Add test |

## E. Budget allocation
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Allocation decisions cite marginal evidence (curve, step test, lift, MMM) | Average returns hide saturation | Last budget plan | Critical | Build curves or run step tests |
| E2 | Protected test budget (about 10% at Growth and above) | Future winners | Budget plan buckets | High | 70/20/10 |
| E3 | Monthly cross channel reallocation happens | Stale budgets waste money | Monthly reviews | High | Monthly review |
| E4 | Pacing tracked daily with alerts | Under or overspend | Daily check outputs | Medium | ads-review daily |
| E5 | Seasonality index used for budget weights and forecasts | Peaks need preparation | Forecast file | Medium | Build index |
| E6 | Brand vs performance split set deliberately | Demand creation is not leftover money | STRATEGY.md | Medium | Split recommendation |

## F. Experimentation
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | EXPERIMENTS.md has hypotheses, metrics, designs and stop rules | Tests without them are not tests | Read file | High | Experiment brief |
| F2 | Velocity meets tier target | Learning speed | Count launched per month | Medium | Backlog grooming |
| F3 | Completion rate 80%+ and learnings written | Wasted tests otherwise | Status column | Medium | Weekly review of rows |
| F4 | Backlog scored with ICE or RICE | Prioritization | ICE column | Medium | Score |
| F5 | At least one incrementality test per half year | Allocation truth | Test calendar | High | Plan with measurement |

## G. Creative and offer supply
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Creative refresh cadence meets volume needed at current spend | Fatigue raises CPA | creative-strategy output | High | Volume plan |
| G2 | Concepts sourced from VoC and market-intel | Differentiated angles | Concept slate sources | Medium | VoC mining |
| G3 | Offer differentiation documented vs competitors | Offer is a top lever | market-intel offer matrix | Medium | Offer study |

## H. Organic and AI visibility
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | SEO trend reviewed monthly with revenue at stake | Organic is often the cheapest demand | seo monthly output | Medium | Activate seo |
| H2 | AI share of voice tracked on priority prompts | AI assistants increasingly shape consideration | ai-search-optimization output | Medium | Baseline |
| H3 | Zero click and AI Overviews impact quantified | Explains organic changes | seo output | Medium | Analysis |

## I. Operations and cadence
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Weekly review happens with max 5 priorities | Focus and accountability | Outputs and PRIORITIES.md | High | ads-review weekly |
| I2 | HEARTBEAT.md current (active agents and cadences) | Right agents run | File date and content | Medium | Update |
| I3 | Journal used for decisions and handoffs | Shared memory | Journal folder | Medium | Decision entries |
| I4 | Memory files contain only confirmed patterns with evidence | Prevents false beliefs | Memory files | Medium | Clean up |
| I5 | Forecast accuracy tracked (MAPE) | Planning credibility | Monthly reviews | Medium | Forecast log |
| I6 | Freshness check run monthly | Platform changes move results | Monthly reviews | Medium | Freshness protocol |

## J. Governance and compliance
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| J1 | Change requests approved by the human before execution | Hard rule | Change request files | Critical | Enforce |
| J2 | Geo legal and tax checklist completed for each market | Fines, blocked ads, wrong CAC | Geo module checklists | High | Run checklist |
| J3 | Approved and forbidden claims documented in BRAND.md | Policy and legal risk | BRAND.md | High | Propose claims list |
| J4 | Sensitive data and restricted categories reviewed (health, finance, minors) | Legal exposure | measurement and channel audits | High (where applicable) | Review with counsel |
| J5 | Customer data files excluded from version control | Privacy | .gitignore | High | ads-setup step 3 |

## Scoring rubric
| Section | Weight in total score |
|---------|-----------------------|
| A Strategy and goals | 10% |
| B Unit economics | 15% |
| C Measurement foundation | 20% |
| D Channel mix | 10% |
| E Budget allocation | 15% |
| F Experimentation | 10% |
| G Creative and offer supply | 5% |
| H Organic and AI visibility | 5% |
| I Operations and cadence | 5% |
| J Governance and compliance | 5% |

| Total score | Verdict | Action |
|-------------|---------|--------|
| 85 to 100 | Top tier system | Optimize at the margin; raise test share |
| 70 to 84 | Solid with gaps | Fix High items within 30 days |
| 50 to 69 | Leaking money | Fix Critical and High items before scaling |
| under 50 | Not ready to scale | Measurement and economics first; freeze budget increases |

Override rule: any Fail on a Critical item in sections B, C or J caps the verdict at "Leaking money" regardless of total score.

Audit output: AUDIT_REPORT.md with the section table, the top 5 issues by contribution margin impact, quick wins (this week), structural fixes (this month), experiments to run, handoffs, and the full checklist as an appendix.
