# Market Intelligence Audit Checklist

Scores how well the project's intelligence program supports decisions. Run at onboarding and quarterly. Score each item Pass (2), Partial (1) or Fail (0). Weights: Critical x3, High x2, Medium x1. Section score = weighted points earned / weighted points possible. Use the AUDIT_REPORT.md template in `ads-master/templates/`.

## A. Competitor set and profiles
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | COMPETITORS.md lists direct, search, AI and alternative competitors | Different lists drive different channels | Read COMPETITORS.md | High | Competitor set review (Play 1) |
| A2 | Top 5 competitors have profile cards under 90 days old | Stale intel misleads | Output dates | High | Quarterly refresh |
| A3 | New entrants reviewed each quarter from auctions, ad libraries, AI answers and reviews | Markets shift | Journal, landscape outputs | Medium | Play 8 |
| A4 | Markets and languages covered match PROJECT_BRIEF.md | Intel must match where we sell | Compare | Medium | Add markets |

## B. Ad intelligence
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Ad library teardowns exist for top competitors on our active channels | Creative decisions need them | Outputs | High | Teardown recipe |
| B2 | Swipe file uses the capture standard (date, market, angle, longevity) | Comparable over time | Inspect | Medium | Adopt template |
| B3 | Insights handed to creative-strategy with gaps, not copies | Differentiation | Journal handoffs | Medium | Gap analysis |
| B4 | EU markets use DSA data (inactive ads, reach, targeting) | Richer evidence | Outputs | Medium | Add EU pulls |

## C. Search and SEO competition
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Auction Insights reviewed at least monthly with trends | Official competitor map | Outputs or google-ads reports | High | Monitoring matrix |
| C2 | Brand bidding monitored | Brand cost and leakage | Alerts | High | Brand monitoring |
| C3 | Organic gap analysis prioritized by intent and AI Overview risk | Effort goes to winnable traffic | Search competition output | Medium | Gap method |
| C4 | Third party estimates labeled with confidence | Avoid false precision | Outputs | Medium | Labels |

## D. AI visibility
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Stable prompt set by segment and stage | Trend tracking | Prompt list | High | Build set |
| D2 | Repeated sampling (3+ runs) across 3+ engines | Noise control | Method section | High | Protocol |
| D3 | Citation source analysis with "sources to win" | Actionable | Output | Medium | Section 6 method |
| D4 | Wrong facts about the brand logged and handed off | Fixable leaks | Output | Medium | Accuracy checks |

## E. Offers, pricing and positioning
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Offer matrix with effective prices and capture dates | Price decisions | Output | High | Offer teardown |
| E2 | Price index tracked for hero SKUs or plans | Conversion and Shopping competitiveness | Output | High (ecommerce) | Price corridor recipe |
| E3 | Competitor promo calendar for the last 12 months | Peak planning | Output | Medium | Monitoring |
| E4 | Positioning map validated with VoC | Strategy grounded in buyers | Output | Medium | Positioning method |
| E5 | Win and loss program (B2B, lead gen) or post purchase survey (ecommerce) | Real reasons, not assumptions | Output, survey data | High | Play 7 |

## F. Voice of customer
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | 100+ coded verbatims per core segment from 3+ source types | Angle quality | VoC output | High | Review mining |
| F2 | Language bank shared with creative-strategy and cro | Copy quality | Handoffs | Medium | Deliver |
| F3 | AUDIENCE.md updated (via approval) with quotes and questions | Shared truth | AUDIENCE.md | Medium | Proposal |
| F4 | Personal data stripped from stored samples | Privacy law | Inspect files | Critical | Anonymize |

## G. Demand and market
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Share of search tracked monthly for 12+ months | Leading indicator | Output | Medium | Procedure |
| G2 | Seasonality index delivered to growth-orchestrator | Budget pacing | Output | Medium | Procedure |
| G3 | Market size with two methods and ranges | Planning credibility | Output | Medium | Market sizing |

## H. Monitoring and governance
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | Monthly movement summary delivered on time | Cadence | Output dates | High | Schedule |
| H2 | Alert thresholds defined and tuned | Signal over noise | Monitoring plan, alert outcomes | Medium | Tune |
| H3 | All collection methods comply with terms of service and privacy law | Legal risk | Tools used, methods | Critical | Replace non compliant methods |
| H4 | Insight adoption tracked (accepted recommendations) | Value proof | Journal | Medium | Track |
| H5 | No comparative claims or competitor trademarks used without approval | Legal and policy risk | BRAND.md, ads | Critical | Approval flow |

## Scoring rubric
| Section | Weight |
|---------|--------|
| A Competitor set and profiles | 10% |
| B Ad intelligence | 15% |
| C Search and SEO competition | 15% |
| D AI visibility | 10% |
| E Offers, pricing and positioning | 15% |
| F Voice of customer | 15% |
| G Demand and market | 10% |
| H Monitoring and governance | 10% |

| Total | Verdict | Action |
|-------|---------|--------|
| 85 to 100 | Decision grade intelligence | Maintain cadence; deepen win and loss and AI benchmarks |
| 70 to 84 | Useful with gaps | Fix High items within 30 days |
| 50 to 69 | Anecdotal | Run Play 1 baseline and set monitoring |
| under 50 | Flying blind | Baseline first; no major positioning or pricing decisions without it |

Override rule: any Fail on a Critical item (F4, H3, H5) is reported first and fixed before other work.

## Audit procedure
1. Collect evidence: COMPETITORS.md, AUDIENCE.md, last 3 market-intel outputs, monitoring plan, journal alerts of the last 90 days, list of tools and methods used.
2. Score each item with evidence notes (file name and date).
3. List Critical fails first, then High items by expected impact on decisions in PRIORITIES.md.
4. Propose fixes as plays (playbooks.md) with time estimates.
5. Deliver with AUDIT_REPORT.md; add EXPERIMENTS.md rows for any research test (for example a survey or test campaign).

## Evidence to collect per section
| Section | Evidence |
|---------|----------|
| A | COMPETITORS.md version, profile card dates |
| B | Teardown outputs, swipe file sample |
| C | Auction Insights exports or google-ads reports, alert log |
| D | Prompt set file, method section, benchmark outputs |
| E | Offer matrix, price index, promo calendar, win and loss or survey outputs |
| F | VoC outputs, language bank, AUDIENCE.md history, storage location of raw samples |
| G | Share of search series, seasonality index, market sizing |
| H | Monitoring plan, alert outcomes, adoption log, method notes on legality |

## Common findings and fixes
| Finding | Fix | Effort |
|---------|-----|--------|
| Competitor list is only "direct" brands | Add search, AI and alternative lists | 1 session |
| VoC is paraphrased, no sources | Redo with verbatims and source metadata | 1 to 2 sessions |
| Third party traffic numbers quoted as facts | Add confidence labels, triangulate | Ongoing |
| No AI visibility baseline | Quick check, then a stable prompt set | 1 session |
| Raw review exports with names stored in the repo | Anonymize, delete raw, update .gitignore (ads-setup step 3) | Immediate |
| Alerts ignored | Tune thresholds using outcomes | 1 session |

## Severity definitions
| Severity | Meaning |
|----------|---------|
| Critical | Legal, privacy or policy exposure, or a gap that makes decisions unsafe |
| High | Gap that regularly leads to wrong or late decisions on budget, creative, pricing or search |
| Medium | Gap that reduces quality or speed of decisions |
