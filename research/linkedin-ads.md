# Research Dossier: LinkedIn Ads

> Compiled 2026-10-08 for the `linkedin-ads` agent. Intended coverage: January 2025 to October 2026.
>
> Method and limits (read first): the shared web search budget for this build was exhausted before LinkedIn specific searches could run, and direct page fetching was blocked by the environment's egress policy. This dossier therefore combines (a) GitHub repository search run on 2026-10-08 (verified), (b) Microsoft Advertising blog items involving LinkedIn data (verified via search extracts), and (c) the author's knowledge of LinkedIn's official documentation and announcements up to mid 2026 (not re-fetched). Every item from (c) that is time sensitive is labeled [Unverified]. Long standing mechanics carry [Official, YYYY] with the year they were established. The June to October 2026 window is a known blind spot; section 11 lists what to verify first. A follow up research pass with live search is recommended before this dossier is treated as current.

## 1. Executive summary

1. LinkedIn remains the only major ad platform with self reported professional identity at scale (job title, function, seniority, skills, employer), which makes it the default channel for reaching B2B buying committees and running ABM [Official, long standing].
2. Its economics are expensive per click and per impression, so the operator's edge is measurement on qualified pipeline, tight ICP targeting, strong creative and patience with demand creation, not CPL chasing [Practitioner consensus].
3. The strategic frame is the 95 to 5 rule: only a small share of buyers is in market in any quarter, so LinkedIn budgets need a protected demand creation share alongside lead capture [Study, 2021].
4. Automation has grown: Accelerate campaigns (launched 2023-10) and predictive audiences (replacing lookalikes retired 2024-02) push toward AI built targeting; both need guardrails via Demographics report checks and CRM quality data [Official, 2023 to 2024] [Unverified] for 2026 scope.
5. Thought Leader Ads (promoting employee and, since 2024, other members' posts with permission) are the most important creative shift of the period for B2B engagement [Official, 2024] [Practitioner consensus].
6. Video expanded beyond the feed through BrandLink (ads with publisher and creator video) and connected TV offerings [Unverified] for 2026 availability, minimums and markets.
7. Measurement matured with the Insight Tag, Conversions API (2023), CRM integrations, the revenue attribution report (2023) and the company engagement report; LinkedIn's official developer org added an Adobe event forwarding extension for CAPI in 2026-06 [Official, 2023] [Verified GitHub, 2026-06].
8. Defaults can hurt B2B: Audience expansion and the LinkedIn Audience Network lower costs while lowering ICP match; top operators turn them off for lead gen and ABM and test them deliberately [Practitioner consensus].
9. LinkedIn data also powers Microsoft Advertising: LinkedIn company, industry and job function targeting on Bing and Copilot search, with company lists raised to 10,000 names in 2026-09 and LinkedIn data excluding EEA, UK and Swiss users [Official, 2026-09]. This creates a cheap search complement for ABM.
10. Agentic tooling arrived: no official LinkedIn Ads MCP server was found, but at least a dozen community and commercial MCP servers (some write capable) appeared between 2025-10 and 2026-08, plus a LinkedIn Ad Library MCP [Verified GitHub, 2026-10].

## 2. State of the channel in 2026

| Dimension | State | Label |
|-----------|-------|-------|
| Audience | LinkedIn has reported over 1 billion members (2023) | [Official, 2023] |
| Core strength | Professional targeting: function, seniority, title, skills, company, industry, size | [Official, long standing] |
| Objectives | Brand awareness; Website visits, Engagement, Video views; Lead generation, Website conversions, Talent leads, Job applicants | [Official, 2024] verify 2026 |
| Formats | Single image, carousel, video, document, event, Thought Leader, conversation, message, text, dynamic, click to message, BrandLink and CTV video | [Official, 2024] [Unverified] for newer formats |
| Bidding | Maximum delivery, Cost cap, Manual | [Official, 2024] |
| Minimums | Historically $10 daily, $100 lifetime per campaign; audience floor 300 members | [Unverified] for budgets, [Official, 2023] for 300 |
| Measurement | Insight Tag, CAPI, CRM conversions, RAR, company engagement, Demographics, A/B tests, brand and conversion lift | [Official, 2023 to 2024] |
| Ownership | Business Manager for multi account governance | [Official, 2023] |
| Ecosystem | Microsoft Advertising uses LinkedIn profile data for search targeting | [Official, 2026-09] |
| API | LinkedIn Marketing API with monthly versions (LinkedIn-Version header) | [Official, 2023] |

### 2.1 Feature notes requested for this build
| Feature | What it is | Status note | How the agent uses it |
|---------|-----------|-------------|-----------------------|
| Accelerate campaigns | AI campaign type that automates audience, creative suggestions and bidding for conversion objectives | Launched 2023-10; objective coverage and controls in 2026 to verify | Test against best classic campaign on CRM quality |
| Thought Leader Ads | Promote member posts as ads | Expanded 2024 to any member with permission; 2026 format and objective support to verify | Core demand creation lever |
| BrandLink and video | Ads alongside premium publisher and creator video | Launched 2024 [Unverified], expansion status to verify | Awareness programs with lift studies |
| Connected TV | Reach LinkedIn audiences on CTV inventory | [Unverified] | Enterprise awareness tests only with lift measurement |
| Predictive audiences | AI audiences seeded by your conversions or lists | Introduced 2024 as lookalike replacement | Scale step after ICP campaigns work |
| Business Manager | Central ownership of ad accounts, pages, people | Launched 2023 | Ownership audit item |
| Revenue attribution report | CRM connected influence report | Launched 2023; CRM coverage to verify | Directional pipeline influence |
| Conversions API | Server-side conversions with hashed identifiers | Launched 2023; GTM server template 2023-08; Adobe extension 2026-06 | Send qualified stages back |
| New objectives or pricing | Unknown for 2025 to 2026 | Verify | Freshness check |
| LinkedIn's own benchmarks | CTR and lead form figures appear in LinkedIn materials | Verify current figures | Quote only with date and source |

### 2.2 How LinkedIn fits with other channels
| Channel | Role vs LinkedIn | Coordination |
|---------|------------------|--------------|
| Google Search | Captures in market demand created partly by LinkedIn | Track branded search and demo requests from target accounts |
| Microsoft Advertising | Search capture with LinkedIn company, industry and job function layers; company lists up to 10,000 | Share company lists and converting job functions; data excludes EEA, UK, Swiss users [Official, 2026-09] |
| Meta | Cheaper reach for some B2B audiences (founders, SMB owners) with weaker professional targeting | Use for SMB ICPs; compare cost per SQL |
| Email and CRM nurture | Converts LinkedIn leads over time | Sync and sequences, suppression of customers |
| Organic LinkedIn | Thought leadership that Thought Leader Ads amplify | Promote posts that earn organic traction |
| Events and field | Event ads and conversation ads drive registrations | Attendance sync to CRM |

### 2.3 Measurement stack (summary)
| Layer | Role | Weakness |
|-------|------|----------|
| Insight Tag | Web conversions, retargeting, visitor demographics | Consent and browser limits |
| Conversions API | Server-side and offline events with hashed identifiers | Needs engineering or a connector |
| Lead gen form sync | Leads into CRM with profile data | Quality depends on form design |
| Revenue attribution report | Influence on pipeline and revenue | Not causal |
| Company engagement report | ABM engagement by account | Directional |
| Demographics report | Who was reached | Thresholded, approximate |
| Lift tests and holdouts | Incrementality | Budget and time |

### 2.4 Targeting evidence and judgement
- Titles: precise but fragmented; LinkedIn standardizes titles, yet many members use non standard titles [Practitioner consensus].
- Function and seniority: inferred classifications with misclassification at the edges; scale is the benefit [Practitioner consensus].
- Skills: self reported; useful for technical practitioners; includes juniors and students [Practitioner consensus].
- Company size and industry: from company pages; small and new companies are often misclassified [Practitioner consensus].
- Matched audiences: match rates vary with list quality; company lists with domains and page URLs match better [Practitioner consensus].
- Conclusion: build two competing audience definitions and let the Demographics report and CRM quality decide.

### 2.5 Auction and pricing mechanics (as known)
- LinkedIn runs an auction where bid and a relevance or engagement estimate determine delivery; higher predicted engagement lowers the effective price [Official, long standing] [Unverified] for current details.
- Campaign Manager shows suggested bid ranges per audience and objective; floors exist by format [Unverified].
- Narrow, senior and ABM audiences carry higher CPMs because of competition for the same members [Practitioner consensus].
- Charge types: CPM, CPC, CPV for video, and cost per send for Sponsored Messaging [Official, 2024].
- Implication: creative relevance (CTR, engagement) is a cost lever, not only a performance metric.

### 2.6 Policy essentials (verify current policy pages)
| Area | Rule as known | Label |
|------|--------------|-------|
| Political ads | Not allowed on LinkedIn | [Official, 2020] |
| Restricted categories | Financial services, healthcare, alcohol, dating and others carry restrictions by region | [Unverified] for current list |
| Discrimination | Ads must not discriminate; housing, employment and credit carry targeting limits in some regions | [Unverified] for current rules |
| Thought Leader Ads | Member permission required for each promoted post | [Official, 2024] |
| Lead gen forms | Privacy policy link required; consent handling per law | [Official] |
| EU transparency | Ad Library shows additional data for EU under the Digital Services Act | [Unverified] for fields |
| Data use | Matched audience uploads require lawful basis and adherence to LinkedIn terms | [Official] |

### 2.7 Fit by business model and budget tier
| Model | LinkedIn fit | Note |
|-------|-------------|------|
| B2B SaaS mid market and enterprise | Strong | ABM, Thought Leader, pipeline measurement |
| Professional services and B2B lead gen | Strong when deal values are high | Lead quality controls are essential |
| SMB focused B2B | Mixed | Meta and search can be cheaper; test cost per SQL |
| B2B ecommerce and premium professional products | Niche | Retargeting and narrow professional segments |
| Recruiting | Strong | Talent objectives, separate from marketing budgets |
| Starter budgets under $3k per month | Limited | One ICP campaign plus retargeting; long learning periods |

## 3. Timeline of changes

### 3.1 Baseline still shaping 2025 to 2026 (pre-2025)
| Date | Change | Label |
|------|--------|-------|
| 2019 | LinkedIn B2B Institute publishes Binet and Field B2B growth principles | [Study, 2019] |
| 2021 | 95 to 5 rule published (Dawes, for the B2B Institute) | [Study, 2021] |
| 2022-12 | LinkedIn JavaScript API client repository created | [Verified GitHub] |
| 2023 | Conversions API launched; Business Manager launched; revenue attribution report introduced | [Official, 2023] |
| 2023-01 | Official Python API client repository created | [Verified GitHub] |
| 2023-08 | Official GTM server-side CAPI tag template repository created | [Verified GitHub] |
| 2023-10 | Accelerate campaigns announced | [Official, 2023] |
| 2023 | LinkedIn reports over 1 billion members | [Official, 2023] |
| 2024-02 | Lookalike audiences retired; predictive audiences as replacement | [Official, 2024] |
| 2024 | Thought Leader Ads expanded to promote any member's posts with permission | [Official, 2024] |
| 2024 | BrandLink video program launched | [Unverified] |
| 2024 | Group based targeting disabled for EU members after Digital Services Act scrutiny | [Unverified] |

### 3.2 January 2025 to October 2026
| Date | Change | Label |
|------|--------|-------|
| 2025-02 | Microsoft Advertising pilots LinkedIn profile targeting as a PMax audience signal in 6 markets | [Official, 2025-02] |
| 2025 | BrandLink and CTV expansion for video advertisers | [Unverified] |
| 2025 | LinkedIn updates terms on member data for generative AI training and data sharing with Microsoft for ads in some regions (effective late 2025) | [Unverified] |
| 2025 | Further Thought Leader Ads and Accelerate expansions (formats, objectives) | [Unverified] |
| 2025-06 | CData read only LinkedIn Ads MCP server published | [Verified GitHub] |
| 2025-10-27 | amekala/ads-mcp (multi platform including LinkedIn) created | [Verified GitHub] |
| 2026-01-20 | danielpopamd/linkedin-ads-mcp created (write capable community server) | [Verified GitHub] |
| 2026-02 to 2026-07 | Wave of multi platform ad MCP servers covering LinkedIn (Synter, markifact, adkit, PaidSync, opusgrowth, Nuraveda, stan-rym) | [Verified GitHub] |
| 2026-06-24 | LinkedIn developer org publishes Adobe Experience Platform event forwarding extension for conversions | [Verified GitHub] |
| 2026-08-05 | Community LinkedIn Ad Library MCP server created | [Verified GitHub] |
| 2026-09-30 | Microsoft Advertising: LinkedIn company lists up to 10,000 names for Search and Audience campaigns; LinkedIn data excludes EEA, UK, Swiss users | [Official, 2026-09] |
| 2026-06 to 2026-10 | LinkedIn product changes in this window not captured | Gap; verify |

## 4. Best practice consensus
1. Agree the qualified lead definition with sales before lead generation; measure on SQLs and pipeline [Practitioner consensus].
2. One objective and one audience per campaign; 2 to 4 ads per campaign [Practitioner consensus].
3. Turn off Audience expansion and LinkedIn Audience Network for lead gen and ABM unless tested [Practitioner consensus].
4. Build ICP audiences from CRM won deal titles; compare function plus seniority with title lists; check the Demographics report after launch [Practitioner consensus].
5. Exclude customers, employees, competitors, students and job seekers [Practitioner consensus].
6. Run a retargeting ladder from engagement audiences (video, document, form openers, visitors) [Practitioner consensus].
7. Use Thought Leader Ads, documents and video for demand creation [Practitioner consensus].
8. Sync lead gen forms to the CRM in near real time with hidden fields for campaign, ad and audience codes [Practitioner consensus].
9. Feed qualified stages back via CAPI or CRM conversions [Official, 2023] [Practitioner consensus].
10. Protect a demand creation budget share and judge it over longer windows [Study, 2021].
11. Use Manual bidding for small ABM audiences; Maximum delivery to learn, then Cost cap [Practitioner consensus].
12. Refresh creative every 4 to 8 weeks in small audiences [Practitioner consensus].

## 5. Contested topics

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Lead gen forms vs landing pages | Forms win on volume and mobile friction | Landing pages win on quality and intent | Test both per offer; qualifying questions narrow the gap |
| Gated vs ungated content | Gating captures leads now | Ungated content builds memory and engagement pools that convert later | Ungated to cold, gated to warm retargeting |
| Job titles vs function and seniority | Titles are precise | Function plus seniority scales and catches non standard titles | Test both; judge on cost per SQL and ICP match |
| Audience expansion | Lowers costs, finds similar members | Dilutes ICP | Off by default, test deliberately |
| Accelerate (AI) campaigns | Saves time, can lower costs | Less control, ICP drift | Test against classic with CRM quality as the judge |
| Revenue attribution report | Shows LinkedIn's pipeline influence | Influence is not causation; overstates | Directional only; holdouts for causality |
| Brand vs activation split in B2B | Near half brand (Binet and Field) | Small ICP startups need more activation | Start from economics and stage; test with holdouts |
| CTR as a quality signal | High CTR means relevance | Click bait and broad audiences inflate CTR | Use CTR for screening only |

## 6. What top operators do differently
- They start with sales: shared definitions, routing, SLAs and a monthly quality review.
- They size budgets per campaign for learning (target cost per result x 30 to 50) and consolidate instead of spreading thin.
- They run Thought Leader programs with multiple credible voices and retarget engagers.
- They review the Demographics report every 2 weeks and compute an ICP match score.
- They treat ABM as a sales program: tiers, plays, weekly engaged account handoffs, account holdouts.
- They use hidden fields and naming conventions so every lead's campaign, ad, audience and offer is analyzable in the CRM.
- They send SQL and opportunity stages back via CAPI so optimization learns from quality.
- They protect demand creation budgets and report pipeline influence over the sales cycle, not weekly CPL.
- They pair LinkedIn ABM with Microsoft Advertising LinkedIn profile targeting on search for cheap capture.
- They derive cost caps and CPL ceilings from deal economics, not from benchmarks.
- They keep a creative pipeline (new angles monthly) because small B2B audiences fatigue fast.
- They separate click and view conversions in reports and reconcile with the CRM monthly.
- They run account holdouts for ABM programs to show incremental pipeline instead of relying on influence reports.
- They use the LinkedIn Ad Library to study competitor offers and Thought Leader usage before briefing creative.

## 7. Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|------------|
| Optimizing to CPL | Cheap unqualified leads; sales distrust | Cost per SQL and pipeline as KPIs |
| Audience expansion and Audience Network left on | Off ICP spend, junk leads | Off by default |
| Too many small campaigns | No learning, high CPMs | Consolidate |
| Maximum delivery on tiny ABM lists | Very high CPMs | Manual CPM |
| CSV lead downloads | Slow follow up, expired leads | Native CRM sync |
| No exclusions | Paying to reach customers, students, competitors | Exclusion lists |
| Same creative for months | Fatigue, rising costs | 4 to 8 week refresh |
| Judging awareness on leads | Cutting future pipeline | Stage appropriate KPIs |
| Agency owned ad account | Data loss | Business Manager ownership |
| Gating everything | Low engagement, small retargeting pools | Ungated to cold audiences |
| Overlapping audiences across campaigns | Self competition and frequency spikes | Exclusions or one campaign per audience |
| Promoting member posts without documented permission | Policy and trust risk | Permission records |
| Reporting post-view conversions as if they were clicks | Overstated ROI | Separate reporting |
| No hidden fields or UTMs in lead forms | Quality cannot be analyzed by campaign | Hidden field standard |

## 8. Benchmarks

| Metric | Value | Source | Date | Sample and caveat |
|--------|-------|--------|------|-------------------|
| B2B buyers in market per quarter | About 5% | Dawes, Ehrenberg-Bass for LinkedIn B2B Institute | 2021 | Model based on purchase cycles [Study, 2021] |
| Brand vs activation in B2B | Indicative near half brand | Binet and Field for LinkedIn B2B Institute | 2019 | Effectiveness award data [Study, 2019] |
| Buying group size | 6 to 10 | Gartner, widely cited | Various | Varies by deal [Study] |
| Sponsored Content CTR | About 0.4% to 0.7% | LinkedIn guidance as commonly quoted, practitioners | Pre-2025 | [Unverified]; varies by format and audience |
| Lead form completion | Around 10% to 15% | LinkedIn materials, practitioners | Pre-2025 | [Unverified] |
| CPC North America | $5 to $15 typical | Practitioners | Ongoing | [Unverified]; seniority and ABM raise it |
| CPM North America | $30 to $100+ | Practitioners | Ongoing | [Unverified] |
| CPL lead gen forms | $50 to $250+ | Practitioners | Ongoing | [Unverified]; offer dependent |
No cross account, method disclosed LinkedIn benchmark study from 2025 to 2026 was verified in this build. Targets must come from CRM economics.

## 9. Tools, APIs and MCP servers

| Tool | Type | Status | Notes |
|------|------|--------|-------|
| LinkedIn Marketing API | Official | Active | Monthly versions; adAnalytics, campaigns, creatives, conversions, lead sync, audiences |
| linkedin-api-python-client, linkedin-api-js-client | Official | Active (updated 2026) | Client libraries |
| linkedin-capi-tag-template | Official | Active | GTM server CAPI |
| reactor-extension-linkedin-edge | Official | New 2026-06 | Adobe event forwarding |
| LinkedIn Ad Library | Official | Active | Competitor ads |
| Official LinkedIn Ads MCP server | Not found | n/a | GitHub search 2026-10-08 |
| Community and commercial MCP servers | Third party | Active | danielpopamd, Nuraveda, stan-rym, DanielSylvester, CData (read only), pipeworx, amekala, markifact, adkit, Synter, PaidSync, opusgrowth |
| LinkedIn Ad Library MCP | Community | New 2026-08 | proxy-intell |
| Microsoft Advertising LinkedIn profile targeting | Adjacent channel | Active | Company lists 10,000 (2026-09) |

## 10. Official sources to monitor

| Source | URL | Cadence | What to look for |
|--------|-----|---------|------------------|
| LinkedIn Marketing Blog | https://www.linkedin.com/business/marketing/blog | Weekly | Product launches, research |
| Help Center (Marketing Solutions) | https://www.linkedin.com/help/lms | On change | Settings, limits, policies |
| Marketing Solutions site and Ads Guide | https://business.linkedin.com/marketing-solutions | Quarterly | Specs, formats |
| Marketing API docs and versioning | https://learn.microsoft.com/en-us/linkedin/marketing/ | Monthly | Version sunsets, new endpoints |
| Advertising policies | https://www.linkedin.com/legal/ads-policy | Quarterly | Restricted categories |
| LinkedIn developer GitHub | https://github.com/linkedin-developers | Monthly | CAPI templates, clients |
| Microsoft Advertising blog | https://about.ads.microsoft.com/en/blog | Monthly | LinkedIn data in Microsoft search ads |

## 11. Open questions and watch list (verify first)
1. All LinkedIn product changes from 2026-06 to 2026-10 (objectives, formats, bidding, pricing).
2. Accelerate campaigns: objective coverage, data thresholds, controls and exclusions in 2026.
3. Thought Leader Ads: supported post types and objectives, lead gen form support.
4. BrandLink and CTV: markets, minimums, measurement options.
5. Predictive audiences: seed minimums and supported objectives.
6. Revenue attribution report: CRMs supported (HubSpot status), lookback options, model.
7. CAPI: accepted identifiers, event lookback, new partner integrations.
8. Budget minimums, daily overspend behavior and frequency caps.
9. Lead gen form limits (custom questions, hidden fields, retention window) and higher intent form option names.
10. EU targeting restrictions and data sharing changes with Microsoft.
11. Message and Conversation ads regional delivery rules.
12. Any LinkedIn published 2025 to 2026 benchmark figures (CTR, CPL, form completion).
13. Whether LinkedIn or Microsoft releases an official LinkedIn Ads MCP server.

## 12. Sources
1. LinkedIn Marketing Solutions. LinkedIn. https://business.linkedin.com/marketing-solutions. Rolling. Known, not re-fetched.
2. LinkedIn Help Center, Marketing Solutions. LinkedIn. https://www.linkedin.com/help/lms. Rolling. Known.
3. LinkedIn Marketing Blog. LinkedIn. https://www.linkedin.com/business/marketing/blog. Rolling. Known.
4. LinkedIn Marketing API documentation. Microsoft Learn. https://learn.microsoft.com/en-us/linkedin/marketing/. Rolling. Known.
5. LinkedIn Advertising Policies. LinkedIn. https://www.linkedin.com/legal/ads-policy. Rolling. Known.
6. LinkedIn Ad Library. LinkedIn. https://www.linkedin.com/ad-library. Rolling. Known.
7. LinkedIn Campaign Manager. LinkedIn. https://www.linkedin.com/campaignmanager. Rolling. Known.
8. LinkedIn B2B Institute. LinkedIn. https://business.linkedin.com/marketing-solutions/b2b-institute. 2019 to 2024. Known.
9. Advertising effectiveness and the 95-5 rule (John Dawes). Ehrenberg-Bass Institute for the LinkedIn B2B Institute. Via source 8. 2021. Known.
10. The 5 Principles of Growth in B2B Marketing (Les Binet, Peter Field). LinkedIn B2B Institute. Via source 8. 2019. Known.
11. B2B buying journey research (buying group size). Gartner. gartner.com. Various editions. Known; edition to verify.
12. Accelerate campaigns announcement. LinkedIn Marketing Blog. Via source 3. 2023-10. Known.
13. Lookalike audiences retirement and predictive audiences. LinkedIn Help Center. Via source 2. 2024-02. Known.
14. Thought Leader Ads expansion. LinkedIn Marketing Blog. Via source 3. 2024. Known.
15. Conversions API launch. LinkedIn. Via sources 3 and 4. 2023. Known.
16. Revenue attribution report. LinkedIn Help Center. Via source 2. 2023. Known.
17. Business Manager. LinkedIn Help Center. Via source 2. 2023. Known.
18. BrandLink and CTV announcements. LinkedIn Marketing Blog. Via source 3. 2024 to 2025. To verify.
19. EU Group targeting change. Press coverage of DSA complaint outcome. 2024. To verify.
20. Member data and AI training terms update. LinkedIn privacy policy and user agreement updates. 2025. To verify.
21. linkedin-api-python-client. LinkedIn (GitHub). https://github.com/linkedin-developers/linkedin-api-python-client. 2023-01-12. Verified.
22. linkedin-api-js-client. LinkedIn (GitHub). https://github.com/linkedin-developers/linkedin-api-js-client. 2022-12-28. Verified.
23. linkedin-capi-tag-template. LinkedIn (GitHub). https://github.com/linkedin-developers/linkedin-capi-tag-template. 2023-08-30. Verified.
24. reactor-extension-linkedin-edge. LinkedIn (GitHub). https://github.com/linkedin-developers/reactor-extension-linkedin-edge. 2026-06-24. Verified.
25. java-sample-application. LinkedIn (GitHub). https://github.com/linkedin-developers/java-sample-application. 2021-10-08. Verified.
26. Less busywork, more growth: What's new in Microsoft Advertising this September. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/september-2026/less-busywork-more-growth-what-new-in-microsoft-advertising-this-september. 2026-09-30. Verified via search extract.
27. New Performance Max tools and other product updates for February. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/february-2025/new-performance-max-tools-and-other-product-updates-for-february. 2025-02. Verified via search extract.
28. Ads Studio in Editor and other product updates for May (LinkedIn as PMax audience signal). Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/may-2025/ads-studio-in-editor-and-other-product-updates-for-may. 2025-05. Verified via search extract.
29. Microsoft Advertising gains LinkedIn company lists of up to 10,000 firms. PPC Land. https://ppc.land/microsoft-advertising-gains-linkedin-company-lists-of-up-to-10-000-firms. 2026. Verified via search extract.
30. Microsoft Ads experiments GA, plus HubSpot and REST news. Relevant Audience. https://www.relevantaudience.com/digital-marketing-en/microsoft-advertising-optimization-experiments-september-2026/. 2026-09. Verified via search extract.
31. danielpopamd/linkedin-ads-mcp. GitHub. https://github.com/danielpopamd/linkedin-ads-mcp. 2026-01-20. Verified.
32. amekala/ads-mcp. GitHub. https://github.com/amekala/ads-mcp. 2025-10-27. Verified.
33. markifact/markifact-mcp. GitHub. https://github.com/markifact/markifact-mcp. 2026-05-03. Verified.
34. adkit/ads-mcp. GitHub. https://github.com/adkit/ads-mcp. 2026-05-19. Verified.
35. stan-rym/liam-linkedin-ads-MCP. GitHub. https://github.com/stan-rym/liam-linkedin-ads-MCP. 2026-06-14. Verified.
36. Nuraveda/linkedin-ads-mcp. GitHub. https://github.com/Nuraveda/linkedin-ads-mcp. 2026-05-29. Verified.
37. DanielSylvester/linkedin-ads-mcp. GitHub. https://github.com/DanielSylvester/linkedin-ads-mcp. 2026-05-25. Verified.
38. proxy-intell/linkedin-ads-library-mcp. GitHub. https://github.com/proxy-intell/linkedin-ads-library-mcp. 2026-08-05. Verified.
39. CDataSoftware/linkedin-ads-mcp-server-by-cdata. GitHub. https://github.com/CDataSoftware/linkedin-ads-mcp-server-by-cdata. 2025-06-23. Verified.
40. pipeworx-io/mcp-linkedin_ads. GitHub. https://github.com/pipeworx-io/mcp-linkedin_ads. 2026-04-15. Verified.
41. Synter-Media-AI/mcp-server. GitHub. https://github.com/Synter-Media-AI/mcp-server. 2026-01-29. Verified.
42. PaidSync/paidsync-mcp. GitHub. https://github.com/PaidSync/paidsync-mcp. 2026-05-11. Verified.
43. opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms. GitHub. https://github.com/opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms. 2026-07-10. Verified.
44. jshorwitz/awesome-agentic-advertising. GitHub. https://github.com/jshorwitz/awesome-agentic-advertising. 2026-02-07. Verified.
45. Dataslayer-AI/Marketing-skills. GitHub. https://github.com/Dataslayer-AI/Marketing-skills. 2026-03-19. Verified.
46. itallstartedwithaidea/advertising-hub. GitHub. https://github.com/itallstartedwithaidea/advertising-hub. 2026-03-10. Verified.
