---
name: linkedin-ads
description: LinkedIn Ads playbook for B2B paid social in Campaign Manager. Use to audit, plan, launch, optimize, scale or troubleshoot LinkedIn campaigns, covering objectives, campaign groups, Accelerate campaigns, targeting by job title, function, seniority, skills and company, matched audiences, company lists and ABM, predictive audiences, audience expansion and LinkedIn Audience Network settings, single image, carousel, video, document, event, conversation, message and Thought Leader Ads, BrandLink and CTV video, lead gen forms and CRM sync with HubSpot or Salesforce, bidding (Maximum delivery, Cost cap, Manual), qualified leads optimization, budgets and frequency caps, Reserved Ads, Insight Tag, Conversions API, revenue attribution report, Companies tab, lift tests, the LinkedIn Marketing API and LinkedIn Ads MCP servers. Triggers include LinkedIn Ads, Campaign Manager, Sponsored Content, ABM, B2B lead gen, cost per lead, buying committee, 95 5 rule.
---

# LinkedIn Ads

> Knowledge as of 2026-10-08. Platforms change monthly. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark. A live verification pass on 2026-10-08 (57 searches across LinkedIn Help Center pages, Marketing API changelogs, trade press and dated benchmark studies) confirmed or corrected most 2025 to 2026 specifics; what remains open sits in the verification queue below. LinkedIn Help Center and Microsoft Learn pages could not be fetched directly, so official facts were confirmed through search extracts of those pages and dated trade coverage.

> Naming (since 2025-10): Campaign Manager now labels the old **campaign group** as **Campaign** and the old **campaign** as **Ad set**. The Marketing API still uses `campaignGroup` and `campaign`, and dynamic UTM tokens were renamed (for example CAMPAIGN_GROUP_ID became CAMPAIGN_ID) [Official, 2025-10]. This skill writes "campaign group (UI: Campaign)" and "campaign (UI: Ad set)" where the difference matters; use the new UI names in change lists.

## Mission and scope
Run LinkedIn Ads as the B2B channel that reaches defined buying committees, creates demand among the 95% of buyers who are not in market, captures the 5% who are, and proves pipeline in the CRM.

Scope: Campaign Manager and Business Manager setup, objectives and structure, targeting and ABM, formats and creative specifications, Thought Leader Ads, video including BrandLink and CTV, lead gen forms and CRM sync, bidding and budgets, frequency, Insight Tag, Conversions API, revenue attribution, lift and A/B testing, reporting, API and MCP tooling.

Out of scope (hand off): CAPI and CRM engineering (measurement), creative production (creative-strategy), landing pages (cro), target account research (market-intel), organic LinkedIn content strategy beyond ads (ai-search-optimization or creative-strategy as routed by growth-orchestrator).

### Platform model in one table
| Area | What to know | Label |
|------|-------------|-------|
| Hierarchy | Ad account > Campaign (was campaign group) > Ad set (was campaign) > Ad; Business Manager centralizes ad accounts, pages, people and CRM connections | [Official, 2025-10] |
| Objectives | Brand awareness; Website visits, Engagement, Video views; Lead generation, Website conversions, Job applicants. Objective cannot be changed after launch | [Official, 2026-09] (API objective list); Talent leads [Unverified] |
| Qualified leads optimization | Lead generation ad sets can optimize to qualified leads sent via Conversions API or CRM data shared in Business Manager; MQL and SQL conversion types added in API 202608 | [Official, 2025-04] [Official, 2026-08] |
| AI ad sets | Accelerate (AI built audience, creative, bidding) next to Classic; launched for Lead generation and Website visits, expanded to all objectives plus video and document formats | [Official, 2024-10] [Contested] on current limits |
| AI creative | Brand Kit, Draft with AI, AI ad variants, Ad personalization, Flexible Ad Creation (up to 64 asset combinations) | [Official, 2026-07] |
| Audience floor | 300 members minimum to serve | [Official, 2026-10] |
| Lookalikes | Discontinued 2024-02-29; predictive audiences and Audience expansion are the replacements | [Official, 2024-02] |
| Bidding | Maximum delivery, Cost cap, Manual bidding; no new bid strategy found in 2025 to 2026; charge by CPM, CPC, CPV or per send depending on format | [Official, 2026-10] |
| Budgets | $10 daily minimum; $100 lifetime minimum for new ad sets, then $10 x scheduled days; daily spend can run up to 50% over the daily budget on a given day; Dynamic Group Budget shares one budget across up to 50 ad sets | [Official, 2026-10] |
| Frequency cap | Classic Brand awareness ad sets: Default or Customize, 3 to 30 impressions per member per 7 days, across feed, Audience Network and CTV | [Official, 2025-07] |
| Premium placements | Reserved Ads (first sponsored slot in feed), First Impression Ads (full screen vertical video, first ad of the day) | [Official, 2025-06] |
| Measurement | Insight Tag, Conversions API, CRM integrations, revenue attribution report (Salesforce, Dynamics 365, HubSpot via Business Manager), Companies tab (replaced the company engagement report), Demographics report, lift tests | [Official, 2026-10] |
| Thought Leader Ads | Promote public posts from employees, creators and other members with approval; Brand awareness and Engagement confirmed | [Official, 2024-03] [Contested] for lead generation |
| Video expansion | BrandLink pre-roll on publisher and creator video (self serve for select accounts since 2026-03); CTV Ads in Campaign Manager (US, Canada), via The Trade Desk (2026-03) and Amazon DSP (US, 2026-05) | [Official, 2026-05] |
| API | LinkedIn Marketing API, monthly versions in the LinkedIn-Version header, each sunset about one year after release (202510 sunsets 2026-10-15) | [Official, 2026-09] |

### Verification queue (still open after the 2026-10-08 pass)
1. Accelerate: whether the getting started limits (14 day minimum, lifetime floors of $700 for Website visits and $3,000 for Lead generation, single image English copy) still apply; sources conflict.
2. Thought Leader Ads with Lead generation objective and lead gen forms: LinkedIn's product page lists only Brand awareness and Engagement; benchmark vendors report lead gen form data on Thought Leader Ads.
3. Predictive audiences: account cap (30 per two agency guides) and the reported 1,000 DMP segment cap per account from API 202608; the 300 member source floor is confirmed.
4. Revenue attribution report default lookback (180 days per LinkedIn's getting started guide, 90 days per one agency, up to 365 days per another).
5. Website retargeting maximum lookback (180 or 365 days) and lead download retention (reported 90 days).
6. Whether a lead gen form "higher intent" option still exists; work email validation is the documented quality lever.
7. In-Stream Ads (reported alpha, US, 2026-09), Creator Marketplace availability outside North America, and CTV markets beyond US and Canada.
8. Talent leads objective status and the current Ads Guide specs for single image, video and document ads.
9. Anything LinkedIn ships after 2026-10-08; recheck the Marketing API recent changes page monthly.

### Evidence and data rules
| Label | Meaning in this skill |
|-------|----------------------|
| [Official, YYYY] or [Official, YYYY-MM] | LinkedIn documentation, Help Center, API changelog or announcement (including dated trade coverage of an announcement); date is when the mechanic was announced, or 2026-10 for a standing Help Center rule confirmed in the 2026-10-08 pass |
| [Study, YYYY] or [Study, YYYY-MM] | Published research or benchmark with a disclosed method or sample (B2B Institute, Ehrenberg-Bass, Forrester, Dreamdata, Kiin) |
| [Practitioner consensus] | Widely repeated by credible operators, no hard data |
| [Contested] | Credible sources disagree; both sides in the reference |
| [Unverified] | Not confirmed in the 2026-10-08 pass; verify before it drives a decision |

Data priority: CRM truth (MEASUREMENT.md) > Campaign Manager data (export, API, MCP) > revenue attribution report (influence) > external benchmarks.

### Changes from 2025 to 2026 that alter decisions
| Change | Date | What the agent does differently |
|--------|------|---------------------------------|
| Qualified leads optimization, then MQL and SQL conversion types | 2025-04, 2026-08 | Send qualified stages through CAPI (at least 5 qualified leads every 2 weeks is LinkedIn's guidance) and test the qualified leads goal on Lead generation ad sets |
| Hierarchy rename (Campaign, Ad set) | 2025-10 | Use new UI names in change lists; check UTM and CRM fields that read dynamic UTM tokens |
| Frequency cap for Brand awareness | 2025-07 | Set Customize caps on ABM awareness instead of relying on budget limits alone |
| Reserved Ads and First Impression Ads | 2025-06 to 2025-12 | Consider for launches and events at Enterprise tier; judge on ICP reach and lift, not CPM |
| Companies tab with paid plus organic engagement | 2024 to 2026 | Weekly engaged company export to sales; build retargeting lists from engagement levels |
| Event Ads: off-platform events and Lead generation objective | 2026-04, 2026-05 | Webinars hosted elsewhere can use event ads with lead gen forms |
| AI creative tools and Flexible Ad Creation | 2026-07 | Use AI variants for volume, but review every line against BRAND.md; Flexible ads auto pause losers |
| BrandLink self serve, CTV via The Trade Desk and Amazon DSP | 2026-03, 2026-05 | Enterprise video programs can buy LinkedIn audiences off platform; plan lift measurement |
| DoubleVerify post-bid measurement on Audience Network | 2026-05 | If Audience Network is tested, require DV or site level reports before scaling |
| Sponsored Messaging creative rotation defaults to OPTIMIZED for lead gen | 2026-07 | Set even rotation (API value ROUND_ROBIN) explicitly when testing message variants |
| Data sharing with Microsoft for ads (outside EU, EEA, UK, Switzerland) | 2025-11-03 | Expect members to have new Advertising Data opt outs; do not assume parity across regions |

## Intake (minimum facts needed)
| Fact | Where to find it | Cold start question |
|------|------------------|--------------------|
| ICP: industries, company sizes, regions | `ads-master/AUDIENCE.md`, PROJECT_BRIEF.md | Which companies buy from you, by industry, size and region? |
| Buying committee roles | AUDIENCE.md | Who signs, who uses, who blocks? Titles or functions and seniority |
| Target account list (ABM) | `ads-master/data/imports/` | Do you have a target account list? How many accounts? |
| Deal value, win rate, sales cycle | PROJECT_BRIEF.md section 3 | Average first year deal value, win rate from SQL, cycle length? |
| Qualified lead definition | MEASUREMENT.md | What makes a lead qualified, and who decides? |
| CRM and sync | PROJECT_BRIEF.md section 7, MEASUREMENT.md | HubSpot, Salesforce or other? Can leads sync automatically? |
| Insight Tag and CAPI status | MEASUREMENT.md | Is the Insight Tag installed? Any CAPI? |
| Budget and tier | PROJECT_BRIEF.md section 5 | Monthly LinkedIn budget and how long you will commit before judging? |
| Offer assets | BRAND.md, creative library | What content can we use: reports, demos, webinars, case studies, founder posts? |
| Thought leaders | AUDIENCE.md or ask | Which executives or experts will let us promote their posts? |

## Operating protocol
1. **Boot.** Read project files and memory. State data and date ranges. Run the Freshness Check for features in scope.
2. **Measurement gate.** Insight Tag firing, conversion rules recording, lead gen form sync to CRM working, qualified stages visible in CRM. If any fail, hand off to measurement and limit work to fixes and planning.
3. **Strategy fit.** Confirm the role of LinkedIn in STRATEGY.md: demand creation, demand capture, ABM, recruiting. Map budget share to the 95 to 5 logic in [B2B strategy playbooks](references/b2b-strategy-playbooks.md).
4. **Diagnose or design.** Audit with [Audit checklist](references/audit-checklist.md) or design with [Account structure](references/account-structure-and-objectives.md) and [Targeting and ABM](references/targeting-and-abm.md).
5. **Prioritize.** Impact x confidence x ease (1 to 5 each). Top 5 only.
6. **Draft the change list.** Exact Campaign Manager names, before and after values, risk, rollback, approval.
7. **Plan tests.** A/B tests or holdouts with rows in `ads-master/EXPERIMENTS.md`.
8. **QA, deliver, log.** Quality Bar, save, journal, handoffs, memory only for confirmed patterns.

### Quality Bar (every deliverable)
- Data source and date range stated; CRM outcomes used where available.
- Every audience has an expected size and a rationale tied to the ICP.
- Each campaign has one objective, one audience and a defined KPI (qualified lead, pipeline, reach in target accounts).
- Audience expansion and LinkedIn Audience Network decisions are explicit.
- Live changes listed for approval with rollback. [Unverified] features carry a verification step.

## Adaptation matrix

### By business model
| Model | LinkedIn role | Structure | Primary KPI | Formats that usually fit | Tests to run first |
|-------|---------------|-----------|-------------|--------------------------|--------------------|
| B2B SaaS | Demand creation plus ABM plus lead capture | Campaign groups by funnel stage; ABM group for tier 1 accounts | Pipeline per dollar, cost per SQL | Thought Leader Ads, document, video, lead gen forms, conversation ads for demos | Thought Leader vs company page ads; gated vs ungated document |
| Lead gen (services, finance, education for professionals) | Lead capture with quality control | Audience by role and seniority; lead gen forms | Cost per qualified lead | Single image, document with lead form, event ads | Work email validation vs none; qualifying question vs none |
| Ecommerce (B2B commerce, premium professional products) | Niche reach to professional segments | Few campaigns, retargeting heavy | ROAS on CRM or backend revenue | Single image, carousel, video | Retargeting vs cold by job function |
| Local services (professional, regional B2B) | Regional decision makers | Location plus company size plus function | Cost per qualified enquiry | Single image, lead gen forms | Small audience Manual bidding vs Maximum delivery |
| App (B2B tools with app) | Awareness and trial among roles | Website conversions to trial | Cost per activated account | Video, single image | Trial vs demo offer |
| Marketplace or publisher | Supply side or advertiser acquisition | Role based audiences | Cost per activated supplier or advertiser | Document, event, single image | Role A vs role B |

### By budget and signal tier
| Tier | Monthly LinkedIn spend | Structure | Bidding | Cadence | Creative volume |
|------|------------------------|-----------|---------|---------|-----------------|
| Starter | under $3k | 1 to 2 campaigns (old campaign groups), 2 to 3 ad sets (one core audience, one retargeting); no Audience Network | Maximum delivery with lifetime or daily caps, or Manual CPC for very small audiences | Weekly | 2 to 4 ads per campaign, refresh every 6 to 8 weeks |
| Growth | $3k to $30k | Funnel stage groups, ABM group, retargeting ladder | Maximum delivery to learn, Cost cap once cost per result is known | Twice weekly checks, weekly optimization | 3 to 5 ads per campaign, Thought Leader Ads, monthly refresh |
| Scale | $30k to $300k | Multiple ICP segments and regions, Accelerate tests, video and CTV tests | Cost cap by segment; Manual for tier 1 ABM | Daily pacing, weekly optimization, monthly tests | Ongoing creative pipeline, executive programs |
| Enterprise | over $300k | Multi market, Business Manager governance, BrandLink or CTV, lift studies | Mixed by objective | Automated reporting via API | Always on creative production |

### By maturity
| Stage | Focus | Do | Avoid |
|-------|-------|----|-------|
| New account | Measurement and audience truth | Insight Tag, CRM sync, conversion rules, small ICP test, Demographics report review | Audience expansion, Audience Network, 10 campaigns at once |
| Running | Lead quality and creative | Qualified rate by campaign, creative refresh, retargeting ladder | Optimizing to CPL alone |
| Plateau | New angles and formats | Thought Leader Ads, documents, video, new roles in the buying committee | Narrowing audiences until delivery stalls |
| Scaling | Reach in ICP and pipeline | New segments, regions, predictive audiences, Accelerate tests, lift tests | Scaling budgets on campaigns with falling qualified rates |

## Task router
| Task | Read these references | Output template |
|------|----------------------|-----------------|
| New account or relaunch | [Account structure](references/account-structure-and-objectives.md), [Targeting and ABM](references/targeting-and-abm.md), [Measurement](references/measurement-capi-and-attribution.md) | Launch plan |
| Full audit | [Audit checklist](references/audit-checklist.md), [Optimization](references/optimization-and-diagnostics.md) | Scored audit |
| Audience design, ABM, company lists | [Targeting and ABM](references/targeting-and-abm.md) | Audience plan with sizes |
| Creative and formats | [Formats and creative](references/formats-and-creative.md) | Creative brief and ad specs |
| Lead quality and CRM sync | [Lead gen forms and CRM](references/lead-gen-forms-and-crm.md) | Lead quality memo and form spec |
| Bids, budgets, frequency | [Bidding and budgets](references/bidding-and-budgets.md) | Bid and budget plan |
| Tracking, CAPI, attribution, lift | [Measurement](references/measurement-capi-and-attribution.md) | Measurement spec plus handoff |
| Strategy, 95 to 5, ABM programs | [B2B strategy playbooks](references/b2b-strategy-playbooks.md) | Program plan |
| Weekly optimization or drop | [Optimization](references/optimization-and-diagnostics.md) | Diagnosis memo and change list |
| Reporting automation, API, MCP | [Tools, API, MCP](references/tools-api-mcp.md) | Tooling plan |
| Benchmarks and forecasts | [Benchmarks](references/benchmarks.md) | Forecast with ranges |
| Source checks | [Sources](references/sources.md) | Freshness log update |

## The laws
1. No lead generation without a written qualified lead definition agreed with sales. Otherwise you optimize to noise.
2. Measure on pipeline and revenue in the CRM; CPL is a diagnostic, not a goal.
3. Turn off Audience expansion and LinkedIn Audience Network for B2B lead gen and ABM unless a test proves otherwise. Both dilute ICP precision. Audience Network is enabled by default on new single image, carousel, document and video ad sets [Official, 2026-10], and practitioners report Audience expansion on by default in many ad sets [Practitioner consensus, 2026-05].
4. One objective and one audience per campaign. Mixed campaigns make results unreadable.
5. Size audiences for the job: retargeting and ABM can be small, cold acquisition needs scale. Under delivery is usually an audience problem.
6. Check the Demographics report two weeks after launch; you are paying for who you reached, not who you targeted.
7. Exclude existing customers, employees, competitors and job seekers where relevant. Wasted impressions are expensive at LinkedIn CPMs.
8. Run 2 to 4 ads per campaign and refresh before fatigue (falling CTR at rising frequency). Creative carries most of the result.
9. Use Thought Leader Ads and native formats (document, video) for demand creation. B2B buyers engage with people more than logos [Practitioner consensus].
10. Lead gen forms: minimal fields for volume, one qualifying question for quality; sync to CRM in near real time. Speed to lead decides conversion.
11. Retarget engagers (video viewers, document readers, form openers, page visitors) with a next step offer. Engagement audiences are LinkedIn's cheapest high intent pool.
12. Start with Maximum delivery to learn the market price, then use Cost cap; use Manual bidding for small ABM audiences. Automated bids overpay on tiny audiences. Expect daily spend up to 50% above the daily budget on single days under any strategy [Official, 2026-10].
13. Give campaigns time: B2B cycles are long; judge demand creation on 60 to 90 day pipeline influence, not same week leads.
14. Feed outcomes back through CAPI and CRM integrations so the system optimizes to qualified events. Qualified leads optimization (2025-04) and the MQL and SQL conversion types (API 202608) make this a bidding input, not only a report [Official, 2026-08].
15. Plan for the 95%: protect a demand creation budget share, because only a small share of buyers is in market at any time [Study, 2021]. LinkedIn data shows long paths: Dreamdata measured 272 days from first touch to revenue in its 2026 report [Study, 2026].
16. ABM is a sales program, not a targeting setting: agree account tiers, plays and follow up with sales.
17. Test one variable at a time with Campaign Manager A/B tests or holdouts; log in EXPERIMENTS.md.
18. Compare to the project's own history first and benchmarks second.

## Diagnostics
| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| Campaign not spending | Audience too small, bid too low (Manual or Cost cap), budget too low, ad rejected, payment | Forecast panel, bid vs suggested range, ad status | Widen audience, raise cap, fix ad, Maximum delivery |
| High CPL | Narrow audience, weak offer, long form, poor creative, wrong objective | CTR, form open and completion rates, frequency | New offer, shorter form, new creative, broaden roles |
| Cheap leads, poor quality | Audience expansion on, Audience Network on, broad roles, job seekers, offer too generic | Demographics report, lead fields, CRM stages | Turn off expansion and network, exclude, qualifying question, work email validation, Qualified leads goal |
| CTR falling | Fatigue, frequency too high, stale creative | Frequency, CTR trend per ad | Refresh creative, rotate offers, widen audience |
| Conversions not recording | Insight Tag missing, rule misconfigured, consent, CAPI not deduped | Tag status, conversion rule status, event test | Hand off to measurement |
| Spend concentrated on one ad | Delivery picks early winner | Ad level impressions | Split test properly or accept and refresh |
| Leads not reaching CRM | Integration disconnected, field mapping | Lead sync status, CRM logs | Reconnect, map fields, alert |
| Target accounts not engaging | List match rate low, creative irrelevant, budget too thin | Company list match rate, Companies tab | Clean list, tier accounts, account specific creative |

Detailed trees are in [Optimization and diagnostics](references/optimization-and-diagnostics.md).

## Cadence
| Frequency | Checks |
|-----------|--------|
| Daily (Growth and above) | Spend pacing, rejected ads, lead sync working, no zero lead days on lead gen campaigns |
| Weekly | KPIs by campaign, CTR and frequency by ad, form completion rate, lead quality notes from sales, budget shifts within groups |
| Every 2 weeks | Demographics report review, exclusions, creative rotation decisions |
| Monthly | CRM report: qualified leads, opportunities and pipeline by campaign; Companies tab for ABM; creative refresh plan; freshness check |
| Quarterly | Full audit, revenue attribution review, lift or holdout test, budget split between demand creation and capture, ABM tier review with sales |

## Guardrails and approvals
| Action | Approval needed | Notes |
|--------|-----------------|-------|
| Any budget change or new campaign | Human | Include expected cost per qualified lead |
| Bid strategy or cost cap changes over 15% | Human | |
| Uploading contact or company lists | Human plus legal basis confirmed | Hashing and matching handled by LinkedIn; never share raw lists outside approved tools |
| Thought Leader Ads | Human plus documented member permission | Permission per post in Campaign Manager flow |
| Lead gen form privacy policy and consent text | Human (legal) | Required field in forms |
| Turning on Audience expansion or Audience Network | Human | Only as a test |
| Conversation and message ads | Human | Sender must agree; EEA and Swiss members receive them only if they opted in [Official, 2024-10] |
| CRM integration changes | Human plus measurement | Affects sales workflow |

## Outputs
- Path: `ads-master/outputs/linkedin-ads/YYYY-MM-DD_linkedin-ads_<description>.md`.
- Required sections: Summary, Data used, Findings, Change list (change, why, expected impact, risk, rollback, approval), Tests proposed (EXPERIMENTS.md IDs), Handoffs requested, Next review.
- Common deliverables: `audit`, `launch-plan`, `audience-plan`, `abm-program`, `creative-brief`, `lead-quality-review`, `measurement-spec`, `monthly-pipeline-report`, `budget-plan`.

## Handoffs
Subagents cannot call each other. A handoff is (1) a journal entry in `ads-master/journal/` describing the request and (2) a final section titled "Handoffs requested" in your response listing each target slug with a 2 to 4 line brief. The main session (running the growth-orchestrator skill) executes the delegation. Common targets: measurement (Insight Tag, CAPI, CRM sync), creative-strategy (Thought Leader and document content), cro (landing pages), market-intel (target accounts, competitor ads), growth-orchestrator (budget), microsoft-ads (LinkedIn profile targeting on Bing search).

## Key formulas
| Formula | Use |
|---------|-----|
| Max cost per SQL = average first year gross profit x SQL to won rate x payback share | Ceiling for SQL cost |
| Max CPL = max cost per SQL x lead to SQL rate | Ceiling for CPL by campaign |
| Pipeline per dollar = opportunity value / spend | Channel efficiency |
| Target accounts reached % = accounts with impressions / accounts in list | ABM coverage |
| Frequency = impressions / unique members reached | Fatigue control |
| Form completion rate = leads / form opens | Form friction |
| Required budget for learning = target cost per result x 30 to 50 results per month per campaign | Budget sizing [Practitioner consensus] |

## Freshness protocol
Before acting on a feature, setting, policy or benchmark:
1. LinkedIn Marketing Solutions blog and product news: https://www.linkedin.com/business/marketing/blog
2. LinkedIn Help Center for Campaign Manager: https://www.linkedin.com/help/lms
3. LinkedIn Ads Guide and specs on business.linkedin.com (Marketing Solutions).
4. LinkedIn Marketing API docs and versioning: https://learn.microsoft.com/en-us/linkedin/marketing/ and the Recent Marketing API Changes page: https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes (monthly; this is where 2026 objective, optimization goal and CAPI changes first appeared).
5. LinkedIn Advertising Policies: https://www.linkedin.com/legal/ads-policy
6. Campaign Manager in-product announcements and the objective, bidding and format menus themselves.
7. LinkedIn developer repositories on GitHub (github.com/linkedin-developers) for CAPI templates and client libraries.
8. Trade coverage that reports LinkedIn launches within days: Social Media Today LinkedIn topic (https://www.socialmediatoday.com/topic/linkedin/) and PPC Land; treat as pointers and confirm in the Help Center.
9. Microsoft Advertising blog for LinkedIn data used in Microsoft search, audience and CTV products: https://about.ads.microsoft.com/en/blog
10. Log changes in `ads-master/journal/YYYY-MM-DD_HHMM_linkedin-ads_freshness.md` with URL and date, and flag outdated reference modules.

## Reference index
- [Account structure and objectives](references/account-structure-and-objectives.md): hierarchy, Business Manager, objectives, Accelerate, naming, structures by tier.
- [Targeting and ABM](references/targeting-and-abm.md): attributes, titles vs function and seniority, skills, matched audiences, company lists, predictive audiences, expansion defaults, EU and EEA rules, Companies tab.
- [Formats and creative](references/formats-and-creative.md): every format with specs and use, Thought Leader Ads, BrandLink and CTV, creative system and fatigue.
- [Lead gen forms and CRM](references/lead-gen-forms-and-crm.md): form design, work email validation, hidden fields, booking, HubSpot and Salesforce sync, qualified lead feedback, lead quality loop.
- [Bidding and budgets](references/bidding-and-budgets.md): strategies, cost cap logic, minimums, pacing, frequency, budget sizing.
- [Measurement: CAPI and attribution](references/measurement-capi-and-attribution.md): Insight Tag, conversion rules, windows, CAPI, offline and CRM conversions, revenue attribution, lift tests.
- [B2B strategy playbooks](references/b2b-strategy-playbooks.md): 95 to 5, buying committee, demand creation vs capture, ABM programs, launch, scale and recover plays.
- [Optimization and diagnostics](references/optimization-and-diagnostics.md): weekly routine, diagnostic trees, testing.
- [Tools, API and MCP](references/tools-api-mcp.md): Marketing API, client libraries, CAPI templates, MCP servers, connectors.
- [Benchmarks](references/benchmarks.md): dated ranges with caveats and how to build internal baselines.
- [Audit checklist](references/audit-checklist.md): scored audit with rubric.
- [Sources](references/sources.md): annotated sources and verification status.
