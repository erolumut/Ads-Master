---
name: microsoft-ads
description: Microsoft Advertising (Bing Ads) playbook for Bing, Yahoo, AOL, DuckDuckGo, Edge, Microsoft Copilot ad placements and the Microsoft Audience Network. Use to audit, launch, import from Google Ads, schedule syncs, optimize, scale or troubleshoot Search, AI Max, Performance Max, Shopping, Microsoft Merchant Center, Audience ads, LinkedIn profile targeting, bid adjustments, portfolio bidding, search partner exclusions, UET tag, UET consent mode, enhanced conversions, offline conversions by MSCLKID, Conversions API, Clarity, experiments, Microsoft Ads Editor, scripts, the Bing Ads API and Microsoft Ads MCP servers. Triggers include Bing Ads, Microsoft Ads, Copilot ads, Showroom ads, Google import, UET, MSCLKID, Microsoft PMax, Microsoft Shopping, Microsoft Audience Network.
---

# Microsoft Advertising

> Knowledge as of 2026-10. Platforms change monthly. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark. Research for this version was compiled with limited live access: claims carry evidence labels and [Unverified] items must be checked in the account or help center before they drive a decision.

## Mission and scope
Run Microsoft Advertising as a profitable, incremental demand capture channel. Scope: Search campaigns (with AI Max), Performance Max, Shopping and Microsoft Merchant Center, Audience ads on the Microsoft Advertising Network, vertical ads (hotel, property promotion, tours and activities, auto, credit cards), Copilot placements, Google Import and scheduled sync, UET and conversion measurement, bidding, budgets, reporting, API and automation.

Out of scope (hand off): feed engineering (commerce-feeds), tag implementation and server-side pipelines (measurement), landing pages (cro), creative production (creative-strategy), organic Bing and IndexNow (seo), organic Copilot citations (ai-search-optimization).

### Platform state in one table (October 2026)
| Area | State | Label |
|------|-------|-------|
| Copilot ads | A placement served from Search, Shopping, AI Max and PMax; no Copilot campaign type. Showroom ads and brand agents in pilot via account teams. | [Official, 2025-03] [Unverified] for current pilot status |
| AI Max for Search | Generally available, opt-in suite: search term matching, text customization, final URL expansion, brand controls and term exclusions; Google Import carries AI Max settings | [Official, 2026-08] |
| Performance Max | GA since 2024; new customer acquisition goal GA (2026-02); self-serve negative keywords (2026-03, 5,000 terms per list); share of voice metrics (2026-01); landing page report (2026-04); Ad Preview Hub (2026-07); uplift experiments (2026-09) | [Official, 2026-01 to 2026-09] |
| Experiments | Generally available for Search, Shopping, Audience and PMax with a side by side results page | [Official, 2026-09] |
| Bidding | Portfolio bid strategies, cross-account portfolios (2026-05), seasonality adjustments for portfolios and shared budgets (2026-05), data-driven attribution to all advertisers (2026-05) | [Official, 2026-04 to 2026-05] |
| Import | Import Center for Google, Meta and Pinterest (2026-05); PMax with NCA goals imports from Google (2026-04) | [Official, 2026-04 to 2026-05] |
| LinkedIn targeting | Company, industry and job function in Search, Shopping, Audience; PMax audience signal; company lists up to 10,000 names (2026-09); excludes EEA, UK and Swiss users | [Official, 2026-09] |
| Consent | UET consent mode required for EEA, UK, Switzerland since 2025-05-05; Advanced Consent Mode guidance 2026-02-19; modeled conversions since 2025-08 | [Official, 2025-03] [Official, 2026-02] [Contested] on modeling scope |
| Conversions API | Documented 2026-08, beta, enrolled per account by Microsoft | [Official, 2026-08] |
| API | SOAP retires 2027-01-31; REST is the target; SOAP keeps receiving features until retirement | [Official, 2026-09] |
| Microsoft Invest (DSP) | Wound down early 2026; Amazon DSP named preferred partner | [Practitioner consensus] from trade press 2025-10 and 2026-01 |
| Optimization score | Retired starting 2025-04-08 | [Official, 2025-04] |

## Intake (minimum facts needed)
| Fact | Where to find it | Cold start question |
|------|------------------|--------------------|
| Business model, offer, AOV or deal size | `ads-master/PROJECT_BRIEF.md` sections 1 to 3 | What do you sell, to whom, and what is a customer worth? |
| Target CPA, ROAS or POAS, breakeven | PROJECT_BRIEF.md section 3 | What can you pay for a sale or qualified lead? |
| Markets and languages | PROJECT_BRIEF.md section 1 | Which countries? Any EEA, UK or Swiss traffic? |
| Monthly budget and tier | PROJECT_BRIEF.md section 5 | Monthly budget for Microsoft, and is it fixed or can it scale? |
| Google Ads status | PROJECT_BRIEF.md section 6, journal from google-ads | Is Google Ads live and healthy? Can we import from it? |
| Account ID, access level | PROJECT_BRIEF.md section 6 | Microsoft Ads account and customer IDs, and our access role? |
| Conversion definitions and truth | `ads-master/MEASUREMENT.md` | What counts as a conversion and where is the real number? |
| UET status, consent, offline import | MEASUREMENT.md tracking table | Is UET installed, with consent mode? Do you store MSCLKID in the CRM? |
| Feed status (ecommerce) | PROJECT_BRIEF.md section 7 | Is Microsoft Merchant Center set up or importing from Google Merchant Center? |
| Data available | `ads-master/data/imports/`, connectors | Can you export 30 and 90 day campaign, keyword, search term and publisher reports? |

## Operating protocol
1. **Boot.** Read project files and memory. State data sources and date ranges. Run the Freshness Check for any feature in scope.
2. **Measurement gate.** Verify UET (UET Tag Helper or network requests to bat.bing.com), conversion goals status "Recording conversions", consent mode for EEA, UK and Swiss visitors (asc parameter), offline import cadence. If any fail, stop and hand off to measurement with a specific fix list.
3. **Diagnose.** Run the audit in [Audit checklist](references/audit-checklist.md) or the symptom tree in Diagnostics below. Quantify waste and upside in currency.
4. **Prioritize.** Score each fix by impact x confidence x ease (1 to 5 each). Top 5 only.
5. **Draft the change list.** Exact UI names, before and after values, expected impact, risk, rollback. Mark which items need approval (all live changes do).
6. **Plan tests.** Anything with uncertain impact becomes an Experiment with a row in `ads-master/EXPERIMENTS.md`.
7. **QA.** Check against the Quality Bar below.
8. **Deliver and log.** Save the deliverable, write a journal entry, request handoffs, update memory only with confirmed patterns.

### Quality Bar (every deliverable)
- Data source and date range stated. No number without a source.
- Recommendations tied to the project's target CPA, ROAS or pipeline value, not platform defaults.
- Microsoft specific divergence considered (bid adjustments, LinkedIn, partners, audience network, demographics).
- Every live change is in an approval list with rollback.
- Platform features labeled; any [Unverified] feature has a verification step.

### Evidence and data rules
| Label | Meaning in this skill |
|-------|----------------------|
| [Official, YYYY-MM] | Microsoft blog, help center or Microsoft Learn page dated YYYY-MM |
| [Study, YYYY-MM] | Published study with a method |
| [Practitioner consensus] | Widely repeated by credible operators, no hard data |
| [Contested] | Credible sources disagree; both sides in the reference |
| [Unverified] | Single source or not confirmed; verify before it drives a decision |

Data priority: backend or CRM truth (MEASUREMENT.md) > Microsoft account data (export, API, MCP) > Google data on matched keywords > external benchmarks.

## Adaptation matrix

### By business model
| Model | Structure | Bidding | Primary KPI | Microsoft specific levers | Tests to run first |
|-------|-----------|---------|-------------|---------------------------|--------------------|
| Ecommerce | Brand Search, non-brand Search by category, PMax with feed, Standard Shopping for control or hero SKUs | Maximize conversion value with tROAS once 30+ conversions per 30 days | ROAS or POAS on backend revenue | Merchant Center, Product explorer, PMax NCA, local inventory ads, age and gender bid adjustments | PMax vs Standard Shopping on a product split; NCA bid higher vs off |
| Lead gen | Brand, non-brand by service, AI Max on top performers | Maximize conversions with tCPA on qualified lead goal | Cost per qualified lead, then pipeline | Offline conversions by MSCLKID, enhanced conversions for leads, device and schedule adjustments, call assets | Bid to qualified lead vs raw lead goal |
| B2B SaaS | Brand, competitor, problem and category terms, Audience campaigns to LinkedIn segments | Manual or Enhanced CPC at low volume, then tCPA on SQL goal | Cost per SQL, pipeline per dollar | LinkedIn company, industry, job function, company lists up to 10,000; HubSpot integration | LinkedIn job function bid adjustments on Search; Audience ads to company list |
| Local services | Geo campaigns per service area, call focus | Maximize conversions on calls and forms, tCPA after volume | Cost per booked job | Radius targeting, location intent "People in", ad schedule, call assets, Microsoft Places listing | Location intent "People in" vs default |
| App | Search for app intent terms, Audience ads | Maximize conversions on install or in-app event | Cost per activated user | App install ads and app assets where available [Unverified] for current market support | App store vs web landing |
| Marketplace or publisher | Category and long tail Search, AI Max with URL rules, DSA where still available | tROAS on margin or tCPA on signup | Contribution margin per click | Final URL expansion with URL exclusions, page feeds | AI Max on vs off as an experiment |

### By budget and signal tier
| Tier | Monthly Microsoft spend | Structure | Bidding | Cadence | Creative volume |
|------|------------------------|-----------|---------|---------|-----------------|
| Starter | under $3k | Import from Google, keep 2 to 4 campaigns, brand separate, no PMax unless feed and 30+ conversions | Manual CPC, Enhanced CPC or Maximize Clicks with cap | Weekly 30 minutes | 1 RSA per ad group, all assets filled |
| Growth | $3k to $30k | Brand, 3 to 8 non-brand, PMax or Shopping, Audience test | Maximize conversions or value, add targets after 30 conversions | Twice weekly checks, weekly optimization | 2 RSAs per key ad group, multimedia ads, image assets |
| Scale | $30k to $300k | Portfolio bid strategies, shared budgets, AI Max, PMax by margin tier | Portfolios with seasonality adjustments | Daily pacing, weekly optimization, monthly experiments | Asset refresh monthly, Ad Studio, image animation |
| Enterprise | over $300k | Cross-account portfolios, scripts, API reporting, multi market | Value rules, cross-account portfolios | Automated daily anomaly alerts | Market specific assets, brand kits |

### By maturity
| Stage | Focus | Do | Avoid |
|-------|-------|----|-------|
| New account | Clean import and measurement | Import, fix settings, verify UET, 2 weeks of data before bid changes | Turning on Audience Network, PMax and broad match at once |
| Running | Waste and divergence | Search terms, partner publishers, bid adjustments, LinkedIn layers | Re-importing over Microsoft specific changes |
| Plateau | New inventory and signal | AI Max experiment, PMax NCA, offline conversions, Audience ads | Raising targets without IS lost to budget evidence |
| Scaling | Marginal returns | Budget to IS lost to budget, portfolios, experiments | Scaling partners or audience network blindly |

## Task router
| Task | Read these references | Output template |
|------|----------------------|-----------------|
| New account or Google import | [Setup and import](references/account-setup-and-google-import.md), [Measurement](references/measurement-uet-and-conversions.md), [Playbooks](references/playbooks.md) | Launch plan with import settings and post-import fix list |
| Full audit | [Audit checklist](references/audit-checklist.md), [Optimization](references/optimization-and-diagnostics.md) | Scored audit with top 10 fixes |
| Search, AI Max, Copilot eligibility | [Search and Copilot](references/search-and-copilot-placements.md) | Search build sheet, Copilot readiness checklist |
| PMax, Shopping, feed | [PMax and Shopping](references/performance-max-and-shopping.md) | PMax structure and guardrail plan |
| Audience ads, LinkedIn targeting, remarketing | [Audience network and targeting](references/audience-network-and-targeting.md) | Audience plan with targeting matrix |
| Bids, budgets, portfolios, forecasts | [Bidding and budgets](references/bidding-and-budgets.md) | Bid strategy map and budget plan |
| UET, consent, enhanced or offline conversions, CAPI, Clarity | [Measurement](references/measurement-uet-and-conversions.md) | Measurement spec plus handoff to measurement |
| Performance drop or weekly optimization | [Optimization](references/optimization-and-diagnostics.md) | Diagnosis memo and change list |
| Reporting automation, API, scripts, MCP | [Tools, API, MCP](references/tools-api-mcp.md) | Tooling plan or script |
| Benchmarks and forecasts | [Benchmarks](references/benchmarks.md), [Bidding and budgets](references/bidding-and-budgets.md) | Forecast with ranges and sources |
| Source checking | [Sources](references/sources.md) | Updated freshness log |

## The laws
1. Measurement first: no bid or budget change on an account whose primary goal did not record in the last 7 days. Bad data trains bad bidding.
2. Microsoft is a different auction: reset bids, targets and budgets from Microsoft data. Copying Google numbers overpays or underbids.
3. Exclude what you diverged from scheduled imports. A sync that overwrites Microsoft only settings silently undoes work.
4. Set location targeting to "People in your targeted locations" unless the business sells to travelers. The broader default leaks spend.
5. Decide Audience Network exposure deliberately for every Search campaign. Unplanned display traffic dilutes CPA.
6. Review syndicated search partners by publisher every 2 weeks. Partner quality varies by domain, not by network.
7. Use bid adjustments Google no longer offers on Search (age, gender, LinkedIn profile, device down to -100%) only with 30+ days of data per segment.
8. LinkedIn profile targeting on Search is bid only. Targeting narrows volume too far on low volume B2B terms.
9. Fill every asset slot: logo, images, sitelinks, callouts, structured snippets, multimedia ads. Asset richness drives Copilot and right rail eligibility.
10. Smart bidding needs about 30 conversions in 30 days per campaign or portfolio; pool or step down below that.
11. PMax always gets brand exclusions, negative keywords and a landing page review. Unguarded PMax harvests brand and cheap placements.
12. PMax and Standard Shopping compete on the same products by Ad Rank (since 2025-05). Split products deliberately.
13. Lead gen bids to qualified stages via offline import, not form fills. Platform optimizes to what you feed it.
14. EEA, UK and Swiss traffic needs UET consent mode with default denied set before the CMP loads. Non compliance can disable tracking and remarketing.
15. One major change per campaign per 7 to 14 days. Learning periods need clean attribution of cause.
16. Test big changes as Experiments with a stop rule. Experiments are GA across Search, Shopping, Audience and PMax.
17. Copilot is earned through eligible formats, not bought separately. Do not sell Copilot to stakeholders as a line item.
18. Compare to the project's own history first and benchmarks second. Benchmarks vary by vertical, geo and season.

## Diagnostics
| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| Conversions dropped to near zero | UET removed or blocked, consent default stuck on denied, goal edited, offline upload stopped | UET Tag Helper, goal status, asc=G after consent, upload history | Hand off to measurement; pause target changes until fixed |
| CPA rose 30%+ week over week | Partner or audience network spike, new competitor, broad match drift, landing page break | Ad distribution segment, publisher report, auction insights, search terms, landing page | Exclude publishers, add negatives, check page, bid to rank where profitable |
| Spend far below budget | Low search volume, bids or targets too strict, disapprovals, narrow targeting, LinkedIn "target" instead of "bid only" | IS lost to rank, ad status, targeting settings | Loosen target by 10 to 15%, fix disapprovals, switch to bid only |
| Spend jumps after a sync | Scheduled import changed budgets, bids or added campaigns | Import history, change history | Exclude fields from import, revert via change history |
| CVR far below Google on same terms | Different device mix, partner traffic, landing page, tracking gap | Device and network segments, CVR by publisher, UET on all pages | Device adjustments, partner exclusions, landing page fix |
| PMax spend shifts to brand | No brand exclusions, brand terms not negated | Search insights, landing page report | Brand exclusions, negative keyword list on PMax |
| Shopping impressions collapse | Feed disapprovals, Merchant Center sync stopped, PMax took products | Merchant Center diagnostics, Product explorer, auction split | Hand off to commerce-feeds, rebalance product split |
| Ads disapproved in bulk | Policy (trademark, healthcare, financial), asset level review | Policy details per asset | Bulk edit tool for disapproved assets, appeal with evidence |
| Remarketing lists not growing | UET blocked, consent denied, list membership duration short | List size history, consent rate | Fix consent flow, extend duration |

Deep diagnostic trees live in [Optimization and diagnostics](references/optimization-and-diagnostics.md).

## Cadence
| Frequency | Checks |
|-----------|--------|
| Daily (5 minutes, Growth and above) | Spend pacing vs plan, conversions not zero, disapprovals, budget caps hit, import errors |
| Weekly | Search terms and negatives, publisher report, CPA or ROAS vs target by campaign, IS lost to budget and rank, asset performance, experiment status |
| Every 2 weeks | Bid adjustments by device, age, gender, LinkedIn segments; audience performance; partner exclusions |
| Monthly | Microsoft vs Google parity report (CPC, CVR, CPA on matched keywords), budget reallocation proposal, feed health, Copilot and placement review, freshness check |
| Quarterly | Full audit, incrementality or uplift test plan, structure review, import strategy review |

## Guardrails and approvals
| Action | Approval needed | Notes |
|--------|-----------------|-------|
| Any budget change | Human | Include marginal CPA logic |
| Bid strategy or target change over 15% | Human | Run as Experiment where possible |
| Running a Google Import or editing an import schedule | Human | Show the import options and excluded fields first |
| Launching or pausing campaigns, AI Max, PMax, Audience ads | Human | Include stop rule |
| Uploading customer lists or offline conversions | Human plus confirmation of consent basis | Never upload raw PII; hash where required |
| Accepting platform recommendations or auto-apply | Human | Default to off for auto-apply |
| Changing conversion goals or primary goal | Human plus measurement agent | Affects bidding for every campaign |
| Negative keywords and publisher exclusions | Human approval on the list; low risk | Batch weekly |

Never enable auto-apply recommendations without explicit approval. Never broaden location intent, enable Audience Network or switch match types silently as part of another change.

## Key formulas
| Formula | Use |
|---------|-----|
| Breakeven ROAS = 1 / contribution margin | Floor for tROAS (margin 40% gives 2.5) |
| Max CPA = AOV x contribution margin (ecommerce) or deal value x margin x close rate (lead gen) | Ceiling for tCPA |
| Initial tCPA = trailing 30 day Microsoft CPA x 1.1, capped at max CPA | First target |
| Initial tROAS = trailing 30 day Microsoft ROAS x 0.9, floored at breakeven | First target |
| Bid adjustment = (campaign CPA / segment CPA) minus 1, capped at +/-50% per step | Manual and Enhanced CPC segments |
| Pacing ratio = spend to date / (monthly budget x days elapsed / days in month) | Daily pacing (0.9 to 1.1 fine) |
| Microsoft clicks forecast = Google clicks x volume ratio (start 0.05 to 0.20) | Planning before data exists [Unverified] ranges |
| Marginal CPA = spend / (b x conversions), from conversions = a x spend^b | Budget allocation |

## Common requests and first moves
| Request | First move | Do not |
|---------|-----------|--------|
| "Set up Microsoft Ads for us" | Intake, measurement gate, Import Center plan with post-import fix list | Launch before UET goals record |
| "Why is Microsoft CPA worse than Google?" | Parity report on matched keywords, network and device segments | Copy Google bids again |
| "Should we run Copilot ads?" | Copilot readiness checklist; explain placement model | Promise separate Copilot reporting |
| "Turn on PMax" | Feed and goal checks, guardrails, uplift test plan | Launch without brand exclusions and negatives |
| "We're B2B, is Microsoft worth it?" | LinkedIn profile layers and company list plan, offline SQL goal | Judge on form fills |
| "Scale spend 2x" | IS lost to budget and marginal CPA by campaign | Raise all budgets evenly |
| "Our tracking broke in Europe" | Consent test (asc=D, asc=G), hand off to measurement | Change bids while data is broken |

## Handoffs
Subagents cannot call each other. A handoff is (1) a journal entry in `ads-master/journal/` describing the request and (2) a final section titled "Handoffs requested" in your response listing each target slug with a 2 to 4 line brief. The main session (running the growth-orchestrator skill) executes the delegation. Typical targets: measurement (UET, consent, offline, CAPI), google-ads (import scope, divergence), commerce-feeds (Merchant Center), cro (landing pages), creative-strategy (assets), growth-orchestrator (budget shifts), linkedin-ads (B2B audience learnings), ai-search-optimization (organic Copilot visibility).

## Outputs
- Path: `ads-master/outputs/microsoft-ads/YYYY-MM-DD_microsoft-ads_<description>.md`.
- Required sections: Summary, Data used, Findings, Change list (change, why, expected impact, risk, rollback, approval), Tests proposed (with EXPERIMENTS.md IDs), Handoffs requested, Next review.
- Common deliverables: `audit`, `import-plan`, `launch-plan`, `weekly-optimization`, `pmax-plan`, `measurement-spec`, `budget-plan`, `parity-report`.

## Freshness protocol
Before acting on a feature, setting, policy or benchmark:
1. Check the Microsoft Advertising blog monthly product roundup: https://about.ads.microsoft.com/en/blog (posts titled "... and other product news for <Month> <Year>").
2. Check the Microsoft Advertising product newsletter (published monthly on LinkedIn since 2026-08).
3. Check API release notes: https://learn.microsoft.com/en-us/advertising/guides/release-notes?view=bingads-13
4. Check help center pages for the feature (help.ads.microsoft.com) and the policy pages for the category.
5. Check consent FAQ: https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_uet_consentfaq
6. For Copilot formats and pilots, ask the account team and look for the feature in the UI; third party guides conflict.
7. Log what changed in a journal entry `YYYY-MM-DD_HHMM_microsoft-ads_freshness.md` with the source URL and date, and flag any reference module that is now wrong.

Priority verification queue (as of 2026-10): Copilot placement reporting labels; whether Search campaigns can opt out of Copilot; Dynamic Search Ads status relative to AI Max; Conversions API availability; HubSpot integration status (beta or GA); modeled conversions scope under Advanced Consent Mode; reports of Max CPC removal for new campaigns; reports of a 7 day gate on offline conversion uploads.

## Reference index
- [Account setup and Google import](references/account-setup-and-google-import.md): account hierarchy, Google Import, scheduled syncs, post-import fix list, when to diverge.
- [Search and Copilot placements](references/search-and-copilot-placements.md): Search build, match types, RSAs, assets, AI Max, DSA status, Copilot formats and eligibility, partner controls.
- [Performance Max and Shopping](references/performance-max-and-shopping.md): Merchant Center, feeds, Shopping, PMax guardrails, NCA, Copilot Checkout readiness.
- [Audience network and targeting](references/audience-network-and-targeting.md): Audience ads, LinkedIn profile targeting, remarketing, customer match, demographics.
- [Bidding and budgets](references/bidding-and-budgets.md): strategies, thresholds, portfolios, seasonality, bid adjustments, forecasting.
- [Measurement: UET and conversions](references/measurement-uet-and-conversions.md): UET, consent mode, enhanced conversions, offline import, CAPI, attribution, Clarity.
- [Optimization and diagnostics](references/optimization-and-diagnostics.md): weekly routine, diagnostic trees, search term and publisher work, experiments.
- [Playbooks](references/playbooks.md): launch, import and diverge, scale, recover, peak season, B2B.
- [Tools, API and MCP](references/tools-api-mcp.md): Editor, scripts, REST and SOAP API, MCP servers, connectors.
- [Benchmarks](references/benchmarks.md): dated benchmark ranges, forecasting from Google, caveats.
- [Audit checklist](references/audit-checklist.md): scored audit with rubric.
- [Sources](references/sources.md): annotated sources with dates.
