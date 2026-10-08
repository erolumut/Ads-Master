# ChatGPT Ads Audit Checklist (Scored)

> Knowledge as of 2026-10. Run the Freshness Protocol first; several checks depend on current availability, policy version and API behavior. Record data sources and date ranges at the top of the audit output.

## How to score
- Severity weights: Critical = 10 points, High = 6, Medium = 3, Low = 1.
- Result per item: Pass = full points, Partial = half, Fail = 0, N/A = excluded from the maximum.
- Score = points earned / points possible x 100.
- Any failed Critical item caps the grade at "Fix before spend" regardless of score.

| Grade | Score | Meaning |
|-------|-------|---------|
| A | 90 to 100 | Run and scale under rules |
| B | 75 to 89 | Run; fix Highs within 2 weeks |
| C | 60 to 74 | Limit spend to learning budget until fixed |
| D | under 60 | Pause spend increases; fix plan required |
| Fix before spend | Any Critical failed | Do not launch or scale |

## A. Eligibility and account (max 51)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | Legal entity country is Available in Ads Manager Availability | Self-serve access follows the legal entity | Availability page, account settings | Critical | Partner or sales path, or wait |
| A2 | Category allowed for the advertiser's country under current Ad Policies version | Prohibited categories are refused; restricted only US | Policy page and changelog | Critical | Stop or seek approval (US restricted) |
| A3 | Account country, currency and time zone match reporting and billing needs | Immutable | Settings | High | New account if wrong |
| A4 | Verification complete; account name and logo confirmed; favicon 256x256; brand review approved | Ads do not serve otherwise | Settings > Account info, serving issues | Critical | Complete steps |
| A5 | Billing profile and card valid; no failed payments | Failed payment stops delivery | Billing page | High | Update card |
| A6 | Users have least privilege; client owns the account; agency invited | Control and continuity | Settings > Users | Medium | Adjust roles |
| A7 | API and CAPI keys stored in secret manager, not in repos or docs | Security | Repo and doc search | High | Rotate and move keys |

## B. Measurement (max 72)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Pixel installed once per page, near top of head, consent gated where required | Accurate events, compliance | Page source, tag manager, debug mode | Critical | Reinstall per docs |
| B2 | CAPI sends primary conversions server side | Resilience to browser loss | Recent events endpoint shows `server_to_server` | High | Implement CAPI |
| B3 | Pixel and CAPI share event ID, event name, Pixel ID | Dedup | Code review, event samples | High | Shared ID strategy |
| B4 | `oppref` survives all redirects and is passed to CAPI | Click attribution | Synthetic oppref test, server code | Critical | Fix redirects, read `__oppref` cookie |
| B5 | Standard events used for primary goals; fire on confirmed success | Optimization requires standard events | Event settings, code | High | Remap events |
| B6 | Event settings attached to every campaign | Conversions not counted otherwise; no backfill | Campaign settings | Critical | Attach before traffic |
| B7 | Paid UTMs on every ad; not using `utm_source=chatgpt.com` for paid | Separate paid from organic | Ad URLs | High | Add static UTMs |
| B8 | GA4 channel group separates Paid AI Assistants and organic AI referrals | Reporting clarity | GA4 admin | Medium | Create channel group |
| B9 | Session rate (GA4 sessions / clicks) 70%+ | Detects webview, redirect and consent loss | GA4 vs Ads Manager, 14 days | High | Fix redirects, speed, consent |
| B10 | Backend reconciliation monthly within 20% | Trust in platform numbers | Backend vs click-through conversions | High | Investigate dedup, windows, modeled conversions |
| B11 | Privacy policy discloses the OpenAI pixel; CMP lists it | Compliance | Privacy page | Medium | Update policy |

## C. Structure and context hints (max 33)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | One market and one objective per campaign; naming convention used | Clean budgets and reporting | Campaign list | Medium | Restructure on next build |
| C2 | Each ad group is one intent | Relevance | Ad group review | High | Split |
| C3 | Hints are specific need, situation or offer phrases (What, Who, When), not audience labels or delivery instructions | OpenAI guidance; relevance | Hint sheet | High | Rewrite |
| C4 | 20 to 60 hints per ad group; accurate vs landing page | Coverage and accuracy | Hint counts, spot check | Medium | Expand or prune |
| C5 | Hint style test run or documented | Styles perform differently | EXPERIMENTS.md | Medium | Run head to head |
| C6 | Geo and platform targeting match eligible, served markets; feed campaigns at country level | Delivery and compliance | Targeting settings | High | Correct targeting |
| C7 | Custom audiences only outside EEA and Switzerland, with legal basis | Compliance | Audience use | High (Critical if EEA data uploaded without basis) | Remove |

## D. Bidding and budgets (max 21)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Objective fits event volume (Clicks under 30 conversions per 30 days; Conversions above) | Optimization signal | Conversion counts | High | New campaign with right objective |
| D2 | Fixed bids within guidance or economically justified; `bid_too_low` reviewed | Delivery | Ad group settings, flags | Medium | Adjust in 10% to 20% steps |
| D3 | Budget type deliberate; team understands 2x day and 7x week rules | Avoid surprises | Interview, settings | Medium | Document in plan |
| D4 | Delivery rate 70%+ of budget | Underspend means bid or relevance limits | 7-day spend vs budget | Medium | Delivery diagnostic |
| D5 | Spend inside approved test budget; end dates on flights | Governance | Budgets vs STRATEGY.md | High | Add end dates, campaign totals |

## E. Creative and landing pages (max 21)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | 3 to 5 distinct angle ads per ad group | Matching and testing | Ads list | Medium | Add angles |
| E2 | Titles 16 to 24 and descriptions 32 to 48 characters with concrete offer details | Truncation and relevance | Copy sheet | Medium | Rewrite |
| E3 | Images square, simple, readable at thumbnail, not logo only, no ChatGPT UI imitation | Policy and CTR | Image review | Medium | Replace |
| E4 | Landing pages specific to intent, fast on mobile, no login or CAPTCHA | Conversion and review | Page tests | High | Route to cro |
| E5 | Claims substantiated and consistent with landing page | Policy | Claim sources | High (Critical in restricted categories) | Fix claims |

## F. Policy, crawler and brand safety (max 23)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | OAI-AdsBot and OAI-SearchBot allowed in robots.txt and WAF; pages return 200 | Review and serving | robots.txt, curl, WAF logs | Critical | Allow and allowlist |
| F2 | No reserved query parameters (`oppref`, `olref`, `obref`, `oai*`) as custom parameter names | Rejection | Ad URLs | High | Rename |
| F3 | Approval rate 90%+; rejections understood | Policy health | Review status | Medium | Fix and resubmit |
| F4 | Manual placement sampling done in last 30 days; off topic placements addressed | Brand safety | Screenshots | Low | Tighten hints, Negative Phrases if eligible |
| F5 | Policy changelog checked since last change | Policies changed six times in 2026 | Policy page | Medium | Log and adapt |

## G. Reporting, testing and incrementality (max 22)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | KPIs use click-through, backend verified conversions; view-through separate | Avoid over crediting | Reports | High | Change reporting |
| G2 | Every test has hypothesis, metric, stop rule in EXPERIMENTS.md | Decision quality | EXPERIMENTS.md | Medium | Add rows |
| G3 | Kill and scale rules written and followed | Spend discipline | Plan and journal | High | Write rules |
| G4 | Incrementality evidence exists before spend passes 10% of paid or $30k per month | Avoid paying for organic demand | MEASUREMENT.md incrementality table | High (Critical above threshold) | Run geo or partner test |
| G5 | Weekly report and journal entries exist | Shared memory | Journal folder | Low | Start cadence |

## H. Cross surface and organic coordination (max 10)
| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | Coverage matrix of priority intents with organic and paid status | Avoid paying for what organic covers | Matrix file | Medium | Build with ai-search-optimization |
| H2 | Google and Microsoft campaigns reviewed for AI surface eligibility (AI Max, PMax, logos, multimedia) | Cheapest AI reach | Handoff notes | Medium | Brief google-ads and microsoft-ads |
| H3 | Product data consistent across Merchant Center, OpenAI feeds and Ads feed | Product ad quality | Feed diagnostics | Medium (N/A if no catalog) | Brief commerce-feeds |
| H4 | Monthly surface review done | Fast changing landscape | Journal | Low | Schedule |

## Audit output template
```
# ChatGPT Ads Audit: <brand>, <date>
Data used: <exports, API, GA4, backend>, <date range>, <timezone>
Score: <x>/100, Grade: <A to D or Fix before spend>
Critical failures: <list>
Top 5 fixes by impact: <numbered, each with owner slug and approval need>
Section scores (base weights, before N/A and severity upgrades): A <x>/51, B <x>/72, C <x>/33, D <x>/21, E <x>/21, F <x>/23, G <x>/22, H <x>/10 (total 253)
Item table: <#, result, evidence, fix>
Handoffs requested: <slug: brief>
Next audit date: <date>
```

## Evidence to collect before scoring
| Evidence | Where | Used for |
|----------|-------|----------|
| Ads Manager CSV, daily values, last 30 and 90 days, campaign, ad group, ad | Ads Manager three dot menu > Download CSV | B9, B10, D4, E1, G1 |
| Account settings screenshots (account info, users, billing) | Settings | A3 to A7 |
| Campaign settings per campaign (objective, budget type, event settings, targeting) | Ads Manager or `GET /campaigns/{id}` | B6, C1, C6, D1, D3 |
| Hint sheet and ad copy sheet | Ads Manager export or outputs folder | C2 to C5, E2, E5 |
| Recent events sample | `GET /v1/conversions/events?pid=...` | B1 to B3 |
| Synthetic oppref redirect test results | curl or preflight checker | B4 |
| robots.txt and WAF rules for OAI-AdsBot | Site, CDN console | F1 |
| GA4 traffic acquisition with source and medium | GA4 | B7 to B9 |
| Backend orders or CRM leads with UTMs and stored oppref | Backend, CRM | B10, G1 |
| EXPERIMENTS.md, MEASUREMENT.md, journal | ads-master/ | G2 to G5 |

## Quick audit (30 minutes, when time is short)
Score only these items and say the audit is partial: A1, A2, A4, B1, B4, B6, D1, F1, G1, G4. Any failure here is a launch or scale blocker. Follow with the full audit within 2 weeks.
