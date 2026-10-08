# Research Dossier: LinkedIn Ads

> Compiled 2026-10-08 for the `linkedin-ads` agent. Coverage: January 2025 to October 2026, with the earlier baseline that still shapes decisions.
>
> Method and limits (read first): the first build had no live search. A verification pass on 2026-10-08 ran 57 web searches (extended mode for 2025 to 2026 items) across LinkedIn Help Center pages, the LinkedIn Marketing API changelog on Microsoft Learn, LinkedIn product pages, trade press (Social Media Today, PPC Land, Search Engine Land, MediaPost, Marketing Brew, StreamTV Insider, AdNews), dated benchmark studies (Dreamdata, Kiin, HockeyStack, The Smarketers, Metadata.io), B2B Institute and Forrester material, practitioner sources (B2Linked) and GitHub. Direct page fetching of linkedin.com and learn.microsoft.com was blocked by the environment, so official facts were confirmed through search extracts of those pages and through dated trade coverage of announcements. Labels: [Official, YYYY-MM] is the announcement date or, for standing Help Center rules confirmed in this pass, 2026-10; [Study, YYYY-MM] is a dated study with a disclosed sample; [Contested] means credible sources disagree; [Unverified] means a single weak source or no confirmation. Section 11 lists what is still open.

## 1. Executive summary

1. LinkedIn remains the only major ad platform with self reported professional identity at scale (job title, function, seniority, skills, employer); Microsoft reported 1.2 billion members in 2025-07 and "nearly 1.3 billion" in 2025-10 [Official, 2025-10] (124).
2. The biggest structural change of the period is that lead quality became a bidding input: Qualified leads optimization launched 2025-04-22 for Lead generation, the API added MAX_QUALIFIED_LEAD in 202602, and MQL and SQL conversion types arrived in 202608 [Official, 2026-08] (47, 57, 58). Operators who send CRM stages through CAPI now steer delivery, not only reporting.
3. Campaign Manager renamed its hierarchy in 2025-10: campaign groups are now "Campaigns" and campaigns are "Ad sets"; the API kept the old names and dynamic UTM tokens were renamed, which silently breaks reports that read them [Official, 2025-10] (59, 60).
4. Economics keep rising: Dreamdata's 2026 report (data 2024-08 to 2025-07) shows CPM up from EUR 26.62 to EUR 34.33 and CPC from EUR 5.35 to EUR 5.98, while LinkedIn's attributed ROAS rose to 121% and cost per company influenced fell to EUR 70.11 [Study, 2026] (95). Kiin's 2026 API panel puts US CPM at $84.21 vs $16.60 in APAC [Study, 2026-09] (91).
5. The strategic frame still holds: about 5% of B2B buyers are in market per quarter (95 to 5 rule, 2021) [Study, 2021] (9), and the B2B Institute's 2025-12 "Easy to Find" work adds presence, prominence and portfolio, arguing for owned prominence over rented placements [Study, 2025-12] (121). Journeys are long: 272 days on average in Dreamdata's 2026 data [Study, 2026] (95).
6. Thought Leader Ads are now an established format (expanded to any member's posts in 2024-03, with a Creator Marketplace alpha since 2026-06), but data shows the premium buys engagement, not cheaper clicks: Kiin's paired accounts show $74.71 CPM vs $48.80 for single image at nearly identical landing page CTR [Study, 2026-09] (89, 73, 90).
7. Video moved off the feed and into premium placements: Reserved Ads and First Impression Ads (2025-06), BrandLink pre-roll (renamed from Wire around 2025-05, self serve for select accounts since 2026-03), and CTV Ads bought in Campaign Manager, The Trade Desk (2026-03) or Amazon DSP in the US (2026-05) [Official, 2026-05] (67, 68, 74, 76, 79).
8. Defaults still hurt B2B: Audience Network is enabled automatically on new single image, carousel, document and video ad sets [Official, 2026-10] (125) and Audience expansion is reported on by default in many ad sets [Practitioner consensus, 2026-05] (126). DoubleVerify post-bid measurement on Audience Network (2026-05-21) makes testing it safer [Official, 2026-05] (82).
9. Controls improved: frequency caps for Brand awareness (3 to 30 impressions per member per 7 days, 2025-07), Dynamic Group Budget, Media Planner (2025-03), Companies tab with paid plus organic engagement, booked meeting reporting from lead gen forms (2026-08) and AI creative tools including Flexible Ad Creation (2026-07) [Official, 2026-07] (61, 65, 71, 85, 83, 69).
10. Agentic tooling: no official LinkedIn Ads MCP server exists as of 2026-09-27; the closest official product is a beta, read only LinkedIn Ads app for ChatGPT; at least a dozen community and commercial MCP servers (some write capable) appeared between 2025-06 and 2026-08 [Official, 2026] (118, 119, 120).

## 2. State of the channel in 2026

| Dimension | State | Label |
|-----------|-------|-------|
| Audience | 1.2 billion members (2025-07), nearly 1.3 billion (2025-10); LinkedIn revenue $17.81B in fiscal 2025, up 9%, with Marketing Solutions driving growth | [Official, 2025-10] (124) |
| Hierarchy | Ad account > Campaign (was campaign group) > Ad set (was campaign) > Ad; API names unchanged | [Official, 2025-10] (59) |
| Objectives | Brand awareness; Website visits, Engagement, Video views; Lead generation, Website conversions, Job applicants; Talent leads status unclear | [Official, 2026-09] (51) |
| Optimization goals | Qualified leads for Lead generation (CAPI or Business Manager CRM data) | [Official, 2026-02] (47, 57) |
| AI ad sets | Accelerate vs Classic; Accelerate covers all objectives since 2024-10 per trade coverage | [Official, 2024-10] (114) [Contested] on limits (113) |
| Formats | Single image, carousel, video, document, event, Thought Leader, conversation, message, text, dynamic, Reserved Ads, First Impression Ads, BrandLink, CTV | [Official, 2026-05] |
| Bidding | Maximum delivery, Cost cap, Manual; no new bid strategy in 2025 to 2026 | [Official, 2026-10] |
| Minimums | $10 daily; $100 lifetime for new ad sets then $10 x days; up to 50% daily overspend; audience floor 300 | [Official, 2026-10] (63, 64) |
| Frequency | Brand awareness frequency cap, 3 to 30 per member per 7 days | [Official, 2025-07] (61, 62) |
| Measurement | Insight Tag, CAPI (identifiers expanded in 2026), CRM integrations, revenue attribution report via Business Manager, Companies tab, Demographics, lift tests, DoubleVerify | [Official, 2026-09] (47, 48, 108) |
| Ecosystem | Microsoft Advertising uses LinkedIn profile data in Search and Audience campaigns (company lists up to 10,000, excluding EEA, UK, Switzerland); LinkedIn CTV data via Microsoft Monetize on Amazon DSP | [Official, 2026-09] (26, 79) |
| API | Monthly versions; 202609 latest; 202510 sunsets 2026-10-15 | [Official, 2026-09] (47, 50, 51) |

### 2.1 Feature status after the 2026-10-08 pass
| Feature | Verified status | How the agent uses it |
|---------|-----------------|-----------------------|
| Qualified leads optimization | Live since 2025-04-22 on Lead generation; LinkedIn guidance: send at least 5 qualified leads every two weeks; early results "upwards of 39%" lower cost per qualified lead (platform claim) (57, 58) | Default test once CAPI qualified events flow |
| Accelerate | Announced 2023-10; lead gen and website visits first; expanded 2024-10 to all objectives plus video and document; getting started PDF lists 14 day minimum and $700 or $3,000 lifetime floors (undated) (113, 114, 116) | Test against Classic on cost per SQL; avoid for target account lists |
| Thought Leader Ads | Any member's public post with approval since 2024-03; Brand awareness and Engagement confirmed; Video views listed for video posts in Help Center; lead gen [Contested] (87, 88, 89) | Demand creation and engager pools |
| Reserved Ads and First Impression Ads | Announced 2025-06; Reserved Ads opened to all managed advertisers around 2025-12 (67, 68) | Launch and event moments at Enterprise tier |
| BrandLink | Wire beta 2024-06; renamed around 2025-05 with creators in US and UK; self serve with publishers for select accounts 2026-03; product page still says beta (74, 75, 76, 135) | Awareness with lift studies |
| CTV Ads | Launched 2024-04 (US, Canada; Roku, Samsung Ads; NBCUniversal Premiere); CTV Select with Paramount 2025-06; Trade Desk 2026-03; Amazon DSP (US) 2026-05 (74, 77, 78, 79) | Enterprise awareness with lift |
| Predictive audiences | Lookalike replacement since 2024-02-29; one source type per audience; 300 member source floor confirmed in LinkedIn's getting started guide; daily refresh; 30 per account reported (100, 101, 137) | Scale after ICP ad sets work |
| Companies tab | Replaced the company engagement report; paid plus organic engagement, engagement levels, one click lists (85, 86) | Weekly ABM handoff to sales |
| Revenue attribution report | Business Manager; Salesforce, Dynamics 365, HubSpot; contact based any touch model; lookback [Contested] (108, 109) | Directional influence |
| Conversions API | Identifiers expanded (IP, Google AID, hashed names from 202609); 180 and 365 day windows for lead types (47, 48, 54) | Send qualified stages |
| AI creative tools | Brand Kit, Draft with AI, AI ad variants, Ad personalization, Flexible Ad Creation, self serve 2026-07-01 (69, 70) | Variant volume with brand review |
| LinkedIn's own benchmarks | Platform claims only (no methods); third-party panels used instead (section 8) | Quote with date and source |

### 2.2 How LinkedIn fits with other channels
| Channel | Role vs LinkedIn | Coordination |
|---------|------------------|--------------|
| Google Search | Captures in market demand created partly by LinkedIn | Track branded search and demo requests from target accounts; the B2B Institute cites branded search at $12.99 per $1 vs 68% ROAS for non branded (121) |
| Microsoft Advertising | Search capture with LinkedIn company, industry and job function layers; company lists up to 10,000 | Share company lists and converting job functions; data excludes EEA, UK, Swiss users [Official, 2026-09] (26); no LinkedIn targeting in Microsoft CTV (80) |
| Amazon DSP and The Trade Desk | Off-LinkedIn CTV with LinkedIn audiences | Enterprise awareness; frequency and lift planning (74, 79) |
| Meta | Cheaper reach for some B2B audiences (founders, SMB owners) with weaker professional targeting | Use for SMB ICPs; compare cost per SQL; Dreamdata measured LinkedIn cost per company influenced 70% below Meta in its 2025 edition (96) |
| Email and CRM nurture | Converts LinkedIn leads over time | Sync and sequences, suppression of customers |
| Organic LinkedIn | Thought leadership that Thought Leader Ads amplify; Companies tab counts organic engagement | Promote posts that earn organic traction |
| Events and field | Event ads (including off-platform events since 2026-04) drive registrations | Attendance sync to CRM (72) |

### 2.3 Measurement stack (summary)
| Layer | Role | Weakness |
|-------|------|----------|
| Insight Tag | Web conversions, retargeting, visitor demographics | Consent and browser limits; does not read Google Consent Mode (129) |
| Conversions API | Server-side and offline events with hashed identifiers; feeds Qualified leads goal | Needs engineering or a connector; only matched events count (48, 55) |
| Lead gen form sync | Leads into CRM with profile data; booked meetings reported since 2026-08-27 | Quality depends on form design (83, 84) |
| Revenue attribution report | Influence on pipeline and revenue | Not causal; lookback contested (109) |
| Companies tab | ABM engagement by account, paid plus organic | Rolls up by account, not by ad (85, 86) |
| Demographics report | Who was reached | Thresholded, approximate |
| Lift tests, holdouts, DoubleVerify | Incrementality and media quality | Budget and time (82) |

### 2.4 Targeting evidence and judgement
- Titles: precise but fragmented; many members use non standard titles [Practitioner consensus].
- Function and seniority: inferred classifications with misclassification at the edges; scale is the benefit [Practitioner consensus].
- Skills: self reported; includes juniors and students [Practitioner consensus].
- Company size and industry: from company pages; small and new companies are often misclassified [Practitioner consensus].
- Matched audiences: 300 member floor to serve; lists up to 300,000 records; company list matching can take up to 48 hours [Official, 2026-10] (85).
- Engagement retargeting lookbacks: 30, 60, 90, 180 and 365 days for video, lead gen form, company page and single image audiences [Official, 2024-10].
- Retargeted audiences in Kiin's data produced 25% more engagement and 20% more dwell time per impression than cold audiences at the same CPC, and uploaded lists behaved like cold audiences with an 11% CPM premium [Study, 2026] (127).
- Conclusion: build two competing audience definitions and let the Demographics report and CRM quality decide.

### 2.5 Auction and pricing mechanics
- Delivery depends on bid and predicted engagement; higher predicted engagement lowers the effective price [Official].
- Campaign Manager shows suggested bid ranges based on what competing advertisers for the same audience likely pay; options depend on objective and format [Official, 2026-10].
- Narrow, senior and ABM audiences carry higher CPMs: The Smarketers put narrow C-suite at 1,000+ employee firms at $90 to $150 CPM in North America vs $55 to $85 for broad B2B [Study, 2026] (98).
- Charge types: CPM, CPC, CPV for video, and cost per send for Sponsored Messaging ($0.36 to $0.49 per send in Kiin's panel) [Official] [Study, 2026] (91).
- Implication: creative relevance is a cost lever, and click definitions matter: default clicks include social clicks, so a landing page visit can cost about 4x the reported CPC (91).

### 2.6 Policy and privacy essentials
| Area | Rule | Label |
|------|------|-------|
| Political ads | Not allowed on LinkedIn | [Official, 2020] |
| EU Group targeting | Disabled for the EU single market on 2024-06-07 after a DSA complaint and a Commission request for information (2024-03-14) | [Official, 2024-06] (104, 105) |
| Sponsored Messaging in the EEA and Switzerland | Blocked from 2021-12 and 2022-01 after a CJEU ePrivacy ruling; since mid October 2024 deliverable again, only to members who opted in | [Official, 2024-10] (102, 103) |
| Data sharing with Microsoft for ads | From 2025-11-03 more member data shared with Microsoft for ad personalization in most regions, excluding EU, EEA, UK, Switzerland; opt out in Advertising data settings | [Official, 2025-11] (106, 107) |
| Generative AI training | From 2025-11-03 member data used for AI training by default in EU, EEA, UK, Switzerland, Canada, Hong Kong; opt out available | [Official, 2025-11] (106, 107) |
| Thought Leader Ads | Member approval required for each promoted post | [Official, 2024-03] (87) |
| Lead gen forms | Privacy policy link required; hidden fields carry no member data | [Official, 2026-10] (110, 111) |
| Restricted categories and discrimination rules | Category and region specific | [Unverified] for the current list |

### 2.7 Fit by business model and budget tier
| Model | LinkedIn fit | Note |
|-------|-------------|------|
| B2B SaaS mid market and enterprise | Strong | ABM, Thought Leader, Qualified leads goal, pipeline measurement |
| Professional services and B2B lead gen | Strong when deal values are high | Lead quality controls are essential |
| SMB focused B2B | Mixed | Meta and search can be cheaper; test cost per SQL |
| B2B ecommerce and premium professional products | Niche | Retargeting and narrow professional segments |
| Recruiting | Strong | Job applicants objective, separate from marketing budgets |
| Starter budgets under $3k per month | Limited | One ICP ad set plus retargeting; Dynamic Group Budget suggests $100 daily per campaign |

## 3. Timeline of changes

### 3.1 Baseline still shaping 2025 to 2026 (pre-2025)
| Date | Change | Label (source) |
|------|--------|----------------|
| 2019 | B2B Institute publishes Binet and Field B2B growth principles | [Study, 2019] (10) |
| 2020-10 | Company engagement report launched for ABM | [Official, 2020] (86) |
| 2021 | 95 to 5 rule published (Dawes, for the B2B Institute) | [Study, 2021] (9) |
| 2021-12 to 2022-01 | Sponsored Messaging stops for EU members after CJEU ruling | [Official, 2022] (102) |
| 2023 | Conversions API, Business Manager and revenue attribution report launched; over 1 billion members | [Official, 2023] (15, 16, 17) |
| 2023-06 | Dynamic Group Budget rolls out (approximate month) | [Official, 2023-06] (136) |
| 2023-08 | Official GTM server-side CAPI tag template repository created | [Official, 2023-08] (23) |
| 2023-10 | Accelerate campaigns announced | [Official, 2023-10] (12) |
| 2024-02-29 | Lookalike audiences and the Lookalike API discontinued; predictive audiences and Audience expansion as replacements | [Official, 2024-02] (100) |
| 2024-03 | Thought Leader Ads expanded to any member's posts with approval (announced 2024-03-13); dynamic UTMs roll out | [Official, 2024-03] (89, 134) |
| 2024-04-03 | CTV Ads (US, Canada; Roku, Samsung Ads), LinkedIn Premiere with NBCUniversal, Live Event Ads | [Official, 2024-04] (77) |
| 2024-06-05 | Wire program beta: pre-roll on publisher video | [Official, 2024-06] (135) |
| 2024-06-07 | Group targeting disabled for EU members | [Official, 2024-06] (104, 105) |
| 2024-10 (mid) | Sponsored Messaging returns for opted in EEA and Swiss members; Wire extended to EU publishers | [Official, 2024-10] (103) |
| 2024-10-15 | Accelerate expanded to all objectives and to video and document ads | [Official, 2024-10] (114, 115) |
| 2024 | Companies Hub (Companies tab) replaces the company engagement report | [Official, 2024] (86) |

### 3.2 January 2025 to October 2026
| Date | Change | Label (source) |
|------|--------|----------------|
| 2025-02 | Microsoft Advertising pilots LinkedIn profile targeting as a PMax audience signal | [Official, 2025-02] (27) |
| 2025-03-25 | Campaign Manager update: Media Planner (forecasts for Brand awareness, Video views, Lead generation), ad duplication across ad sets and accounts | [Official, 2025-03] (71) |
| 2025-04 | Event registration conversions move to 30 day click and 30 day view windows | [Official, 2025-04] (54) |
| 2025-04-22 | Qualified leads optimization for Lead generation via CAPI or CRM data | [Official, 2025-04] (57, 58) |
| 2025-05 | Wire renamed BrandLink and opened to creator video in US and UK; LinkedIn claims 130% higher completion | [Official, 2025-05] (76) |
| 2025-05 | Microsoft Advertising expands LinkedIn audience signal in PMax | [Official, 2025-05] (28) |
| 2025-06-04 | CTV Select (renamed Premiere) adds Paramount; VAST tags via Innovid; CTV API with Sprinklr | [Official, 2025-06] (78) |
| 2025-06-05 | First Impression Ads and Reserved Ads announced ahead of Cannes | [Official, 2025-06] (68) |
| 2025-06-23 | CData read only LinkedIn Ads MCP server published | [Verified GitHub] (39) |
| 2025-07 | Frequency capping for Brand awareness ad sets (3 to 30 per 7 days) | [Official, 2025-07] (61, 62) |
| 2025-07 | Revenue attribution report getting started guide v01 published (180 day default lookback) | [Official, 2025-07] (109) |
| 2025-07-21 | Innovid expands LinkedIn CTV integration | [Official, 2025-07] (133) |
| 2025-08 | Thought Leader Ads for posts linking to LinkedIn Events (month per one source) | [Unverified] |
| 2025-09 | LinkedIn announces the hierarchy rename and the 2025-11-03 terms update | [Official, 2025-09] (59, 106) |
| 2025-10 (mid) | Hierarchy rename rolls out: Campaign and Ad set; UTM tokens renamed | [Official, 2025-10] (59, 60) |
| 2025-10-22 | 1.2 billion members milestone publicized; nearly 1.3 billion on the earnings call | [Official, 2025-10] (124) |
| 2025-10-27 | amekala/ads-mcp (multi platform including LinkedIn) created | [Verified GitHub] (32) |
| 2025-11-03 | Expanded data sharing with Microsoft for ads (outside EU, EEA, UK, CH) and default AI training in EU, EEA, UK, CH, Canada, Hong Kong | [Official, 2025-11] (106, 107) |
| 2025-12 | Reserved Ads opened to all managed advertisers (approximate); AI ad variants and Flexible Ad Creation previewed for early 2026 | [Official, 2025-12] (67) |
| 2025-12-02 | B2B Institute "Easy to Find" research (owned vs rented prominence) | [Study, 2025-12] (121) |
| 2026-01-20 | danielpopamd/linkedin-ads-mcp created (write capable community server) | [Verified GitHub] (31) |
| 2026-02 | API 202602: MAX_QUALIFIED_LEAD optimization target for LEAD_GENERATION | [Official, 2026-02] (47) |
| 2026-02-28 | Microsoft Invest DSP shut down; Microsoft Monetize shifts LinkedIn data to Amazon DSP | [Official, 2026-02] (81) |
| 2026-02 to 2026-07 | Wave of multi platform ad MCP servers covering LinkedIn (Synter, markifact, adkit, PaidSync, opusgrowth, Nuraveda, stan-rym) | [Verified GitHub] (33 to 43) |
| 2026-03 | BrandLink with publishers self serve for select accounts; CTV programmatic via The Trade Desk (Microsoft Monetize supply); LinkedIn claims CTV 2.2x more effective than other CTV | [Official, 2026-03] (74) |
| 2026-04-28 | Event Ads for off-platform events, lead gen for event ads, event clipping, measurement updates | [Official, 2026-04] (72) |
| 2026-05 | API 202605: LEAD_GENERATION objective for event ads | [Official, 2026-05] (47, 52) |
| 2026-05 (early) | LinkedIn CTV Ads available through Amazon DSP in the US (deal based) | [Official, 2026-05] (79) |
| 2026-05-14 | Report that Microsoft CTV gains LinkedIn targeting; Microsoft later clarified it is not available | [Official, 2026-05] (80, 81) |
| 2026-05-21 | DoubleVerify global post-bid measurement for LinkedIn Audience Network | [Official, 2026-05] (82) |
| 2026-06-10 | Creator Marketplace (alpha, North America, English) and BrandWorks managed creative service | [Official, 2026-06] (73) |
| 2026-06-24 | LinkedIn developer org publishes Adobe event forwarding extension for conversions | [Verified GitHub] (24) |
| 2026-07 | Sponsored Messaging lead gen ad sets default to OPTIMIZED creative selection | [Official, 2026-07] (47) |
| 2026-07-01 | Brand Kit, Draft with AI, AI ad variants, Ad personalization and Flexible Ad Creation self serve; LinkedIn claims 5+ variants lift CTR over 20% | [Official, 2026-07] (69, 70) |
| 2026-08 | API 202608: MARKETING_QUALIFIED_LEAD and SALES_QUALIFIED_LEAD conversion types | [Official, 2026-08] (47) |
| 2026-08-05 | Community LinkedIn Ad Library MCP server created | [Verified GitHub] (38) |
| 2026-08-27 | Booked appointments from lead gen forms reported in Campaign Manager (Chili Piper mapping), no backfill | [Official, 2026-08] (83, 84) |
| 2026-09 | API 202609: accountIntelligence filters, DMA pivot, hashed first and last names in CAPI, 180 and 365 day windows for lead types | [Official, 2026-09] (47, 48) |
| 2026-09 | Brand safety inventory warnings in Campaign Manager; In-Stream Ads alpha (US) reported | [Unverified] (83) |
| 2026-09-16 | LinkedIn publishes company targeting guidance using the Companies view | [Official, 2026-09] (85) |
| 2026-09-27 | Vendor status check: still no official LinkedIn Ads MCP server | [Practitioner consensus] (120) |
| 2026-09-30 | Microsoft Advertising: LinkedIn company lists up to 10,000 in Search and Audience campaigns; excludes EEA, UK, Swiss users | [Official, 2026-09] (26, 29) |
| 2026-10-15 | Marketing API version 202510 sunsets | [Official, 2026-09] (51) |

## 4. Best practice consensus
1. Agree the qualified lead definition with sales before lead generation; measure on SQLs and pipeline [Practitioner consensus].
2. Send qualified stages (QUALIFIED_LEAD, MQL, SQL) through CAPI and test the Qualified leads goal on Lead generation ad sets [Official, 2026-08] (47, 57).
3. One objective and one audience per ad set; 2 to 4 ads per ad set, or Flexible Ad Creation for structured variant tests [Practitioner consensus].
4. Turn off Audience expansion and LinkedIn Audience Network for lead gen and ABM unless tested; both are on by default in many ad sets [Official, 2026-10] (125, 126).
5. Build ICP audiences from CRM won deal titles; compare function plus seniority with title lists; check the Demographics report after launch [Practitioner consensus].
6. Exclude customers, employees, competitors, students and job seekers [Practitioner consensus].
7. Run a retargeting ladder from engagement audiences (video, document, form openers, visitors, Companies tab engaged lists) [Practitioner consensus].
8. Use Thought Leader Ads, documents and video for demand creation, judged on engagement and engager pools, not landing page CPC [Study, 2026-09] (90).
9. Sync lead gen forms to the CRM in near real time with hidden fields for campaign, ad and audience codes; add a Work email field and a booking option for demo offers [Official, 2026-10] (110, 111, 84).
10. Protect a demand creation budget share and judge it over long windows (272 day average journey) [Study, 2026] (95).
11. Use Manual bidding for small ABM audiences; Maximum delivery to learn, then Cost cap; pace on weekly totals because daily spend can run 50% over [Official, 2026-10] (64, 66).
12. Use the Brand awareness frequency cap for ABM air cover [Official, 2025-07] (62).

## 5. Contested topics

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Lead gen forms vs landing pages | Forms win on volume and mobile friction | Landing pages win on quality; one vendor reports 20% to 40% lower SQL rates from forms | Test both per offer; qualifying questions and work email validation narrow the gap |
| Gated vs ungated content | Gating captures leads now | Ungated content builds memory and engager pools | Ungated to cold, gated to warm retargeting |
| Job titles vs function and seniority | Titles are precise | Function plus seniority scales | Test both; judge on cost per SQL and ICP match |
| Audience expansion | Lowers costs; LinkedIn's lookalike replacement | Dilutes ICP | Off by default, test deliberately |
| Accelerate | Saves time; LinkedIn claims up to 42% lower CPA | Practitioners report lower CPL but higher cost per SQL and ICP drift (116, 117) | Test against Classic with CRM quality as the judge |
| Accelerate limits | Getting started PDF: Website visits and Lead generation only, 14 days, $700 or $3,000 lifetime floors | Trade coverage: all objectives since 2024-10 | Check the setup screen |
| Thought Leader Ads with lead gen forms | Kiin and an agency guide report lead gen forms on Thought Leader Ads | LinkedIn's product page lists only Brand awareness and Engagement | Check the objective menu |
| Thought Leader Ads value | Several times higher engagement, cheaper engagement clicks (ZenABM $2.29 CPC) | Paired data: higher CPM, same landing page CTR (Kiin) | Use for engagement and memory, not traffic |
| Revenue attribution report lookback | 180 days default (LinkedIn guide) | 90 days default, up to 365 (agencies) | Read the setting before quoting |
| CAPI ORACLE_MOAT_ID | Listed in Help Center and the 2025-02 FAQ | Missing from the 2026-04 FAQ list | Do not rely on MOAT IDs; send email hash plus click ID |
| Brand vs activation split in B2B | Near half brand (Binet and Field) | Small ICP startups need more activation | Start from economics and stage; test with holdouts |
| Insight Tag and consent | Tag ignores Google Consent Mode; gate in GTM | One CMP vendor claims a limited data use fallback | Gate the tag; test the vendor claim |

## 6. What top operators do differently
- They start with sales: shared definitions, routing, SLAs and a monthly quality review.
- They send MQL and SQL stages back through CAPI and let the Qualified leads goal learn from them.
- They size budgets per ad set for learning (target cost per result x 30 to 50) and consolidate instead of spreading thin.
- They run Thought Leader programs with multiple credible voices (employees and paid creators) and retarget engagers.
- They review the Demographics report every 2 weeks and compute an ICP match score.
- They treat ABM as a sales program: tiers, plays, weekly Companies tab handoffs, account holdouts.
- They use hidden fields and naming conventions so every lead's campaign, ad, audience and offer is analyzable in the CRM, and they remapped UTM tokens after the 2025-10 rename.
- They protect demand creation budgets and report pipeline influence over the sales cycle, not weekly CPL.
- They pair LinkedIn ABM with Microsoft Advertising LinkedIn profile targeting on search for cheap capture.
- They derive cost caps and CPL ceilings from deal economics, not from benchmarks.
- They read landing page clicks, not all clicks, when comparing traffic costs across channels.
- They separate click and view conversions in reports and reconcile with the CRM monthly.
- They run account holdouts for ABM programs instead of relying on influence reports.
- They use the LinkedIn Ad Library to study competitor offers and Thought Leader usage before briefing creative.
- They use AI for copy variants but keep imagery human made; AJ Wilcox reports AI styled imagery never performed well in B2Linked tests (130) [Practitioner consensus, 2026-08].
- They plan off-feed video (Reserved Ads, BrandLink, CTV) only with a lift study and a frequency cap, and they read DoubleVerify or site level reports before scaling Audience Network (82).

## 7. Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|------------|
| Optimizing to CPL | Cheap unqualified leads; sales distrust | Cost per SQL and pipeline as KPIs; Qualified leads goal |
| Audience expansion and Audience Network left on (defaults) | Off ICP spend, junk leads | Check every new ad set |
| Too many small ad sets | No learning, high CPMs | Consolidate |
| Maximum delivery on tiny ABM lists | Very high CPMs | Manual CPM plus frequency cap |
| CSV lead downloads | Slow follow up, leads lost after the reported 90 day window | Native CRM sync |
| No exclusions | Paying to reach customers, students, competitors | Exclusion lists |
| Same creative for months | Fatigue, rising costs | 4 to 8 week refresh, AI variants reviewed by a human |
| Judging awareness on leads | Cutting future pipeline | Stage appropriate KPIs |
| Agency owned ad account | Data loss | Business Manager ownership |
| Reports broken after the 2025-10 rename | Lost attribution in GA4 and CRM | Remap dynamic UTM tokens |
| Treating Thought Leader Ads as a traffic format | Paying a CPM premium for the same landing page CTR | Use for engagement and engager pools |
| Promoting member posts without documented approval | Policy and trust risk | Approval records |
| Reporting post-view conversions as if they were clicks | Overstated ROI | Separate reporting |
| Leaving API integrations on a sunset version | Broken reporting (202510 sunset 2026-10-15) | Track version sunset dates |
| No hidden fields or UTMs in lead forms | Quality cannot be analyzed by campaign | Hidden field standard |

## 8. Benchmarks

| Metric | Value | Source | Date | Sample and caveat |
|--------|-------|--------|------|-------------------|
| B2B buyers in market per quarter | About 5% | Dawes, Ehrenberg-Bass for LinkedIn B2B Institute (9) | 2021 | Model based on purchase cycles [Study, 2021] |
| Brand vs activation in B2B | Indicative near half brand | Binet and Field for LinkedIn B2B Institute (10) | 2019 | Effectiveness award data [Study, 2019] |
| Buying group size | 13 people; 89% of purchases span 2+ departments | Forrester State of Business Buying 2024 (123) | 2024-12 | Gartner: 5 to 11; definitions vary [Study, 2024-12] |
| CTR (all clicks) | 0.57% | Dreamdata 2026 report (95) | Data 2024-08 to 2025-07 | Dreamdata B2B customers; EUR; mean or median not stated [Study, 2026] |
| CPC | EUR 5.98 (prior EUR 5.35) | Dreamdata (95) | Same | Same |
| CPM | EUR 34.33 (prior EUR 26.62) | Dreamdata (95) | Same | Same |
| Attributed ROAS | 121% (prior 113%) | Dreamdata (95, 96) | Same | Multi touch attribution, not incrementality |
| Journey length | 272 days (prior 211); 320 days first impression to revenue (2025 edition) | Dreamdata (95, 96) | Same | Same |
| Single image | CPM about $48, CTR 0.65%, CPC $6.32, landing page CTR 0.37%, landing page CPC $13.63 | Kiin API panel (91) | 2025-09 to 2026-09 | 774 accounts; Kiin users; pooled [Study, 2026-09] |
| Document | CPM $61.77, CTR 3.32%, landing page CTR 0.06% | Kiin (91) | Same | Engagement clicks dominate |
| Video | CPM $40.93, CTR 0.41% | Kiin (91) | Same | |
| Thought Leader Ads | Median CPM $65, median landing page CTR 0.46%; paired CPM $74.71 vs $48.80 single image | Kiin (90) | Same | 212 accounts [Study, 2026-09] |
| Regional CPM | US $84.21, Canada $65.36, UK $49.69, DACH $38.94, Nordics $30.72, APAC $16.60 | Kiin (91) | Same | US 354 accounts, APAC 39 |
| Lead gen form open rate | Median 0.33% | Kiin (92) | 12 months to 2026 | 376 accounts; 489 advertisers, $13.6M spend, 86,051 leads [Study, 2026] |
| Lead gen CPL, content offers | Thought Leader $94 (11.4% completion); video $119 (4.6%) | Kiin (92) | Same | Cells of 8 to 16 accounts |
| CTV CPM | Median $25.76 | Kiin (93) | 2026 | 31 accounts [Study, 2026] |
| Message ads cost per send | $0.36 content, $0.49 demo | Kiin (91) | 2026 | Panel |
| B2B SaaS CTR and CPC | CTR 0.82% to 0.96%; CPC $10.48 to $15.72 | HockeyStack (97) | 2025 | 70+ B2B SaaS companies [Study, 2025] |
| CPM by region, broad B2B | NA $55 to $85; W. Europe $50 to $80; APAC $35 to $60; up 38% 2022 to 2026 | The Smarketers (98) | Q1 2026 | n=40 campaigns, $8.4M [Study, 2026] |
| CPL (older) | $163; CPM about $70 | Metadata.io (99) | 2021 data | Context only |
| Platform claims | 5+ variants +20% CTR; Accelerate up to 42% lower CPA; QLO up to 39% lower cost per qualified lead; BrandLink +130% completion | LinkedIn (57, 69, 76, 114) | 2024 to 2026 | No method published |
Targets must come from CRM economics; the benchmarks above are sanity checks only.

## 9. Tools, APIs and MCP servers

| Tool | Type | Status | Notes |
|------|------|--------|-------|
| LinkedIn Marketing API | Official | Active; 202609 latest; 202510 sunset 2026-10-15 | adAnalytics, campaigns, creatives, conversions, lead sync, audiences, accountIntelligence (47, 50) |
| linkedin-api-python-client, linkedin-api-js-client | Official | Active | Client libraries (21, 22) |
| linkedin-capi-tag-template | Official | Active | GTM server CAPI (23) |
| reactor-extension-linkedin-edge | Official | New 2026-06 | Adobe event forwarding (24) |
| LinkedIn Ads app for ChatGPT | Official (beta) | Read only | Ad accounts, ad sets, ad performance Q and A (118) |
| LinkedIn Ad Library | Official | Active | Competitor ads (6) |
| Official LinkedIn Ads MCP server | Not available | n/a | GitHub search 2026-10-08; vendor checks 2026-07 and 2026-09-27 (119, 120) |
| Community and commercial MCP servers | Third party | Active | danielpopamd, Nuraveda, stan-rym, DanielSylvester, CData (read only), pipeworx, amekala, markifact, adkit, Synter, PaidSync, opusgrowth (31 to 43) |
| LinkedIn Ad Library MCP | Community | New 2026-08 | proxy-intell (38) |
| CAPI partners | Third party | Active | Salesforce Data Cloud connector, Zapier, LiveRamp, Dreamdata, Commanders Act, MetaRouter, Datahash, LeadsBridge |
| Chili Piper booking | Third party | Rolling out 2026 | Lead gen form booking with routing (84) |
| DoubleVerify | Third party | Live 2026-05-21 | Audience Network post-bid, CTV measurement (82) |
| Microsoft Advertising LinkedIn profile targeting | Adjacent channel | Active | Company lists 10,000 (2026-09) (26) |

## 10. Official sources to monitor

| Source | URL | Cadence | What to look for |
|--------|-----|---------|------------------|
| Recent Marketing API Changes | https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes | Monthly | New objectives, goals, conversion types, version sunsets |
| LinkedIn Marketing Blog | https://www.linkedin.com/business/marketing/blog | Weekly | Product launches, research |
| Help Center (Marketing Solutions) | https://www.linkedin.com/help/lms | On change | Settings, limits, policies |
| Marketing Solutions site and Ads Guide | https://business.linkedin.com/marketing-solutions | Quarterly | Specs, formats, BrandLink and Thought Leader pages |
| Advertising policies | https://www.linkedin.com/legal/ads-policy | Quarterly | Restricted categories |
| LinkedIn developer GitHub | https://github.com/linkedin-developers | Monthly | CAPI templates, clients |
| Microsoft Advertising blog | https://about.ads.microsoft.com/en/blog | Monthly | LinkedIn data in Microsoft search, audience and CTV products |
| Social Media Today LinkedIn topic | https://www.socialmediatoday.com/topic/linkedin/ | Weekly | Fast reporting of launches (confirm officially) |
| B2B Institute research | https://business.linkedin.com/marketing-solutions/b2b-institute | Quarterly | Effectiveness research |

## 11. Open questions and watch list (verify first)
1. Accelerate: whether the 14 day minimum, $700 and $3,000 lifetime floors and single image English copy rules still apply.
2. Thought Leader Ads with Lead generation and lead gen forms (conflicting sources).
3. Predictive audiences account cap (30 per two agency guides) and the reported 1,000 DMP segment cap per account from API 202608 (138).
4. Revenue attribution report default lookback (90, 180 or 365 days).
5. Website retargeting maximum lookback (180 or 365 days) and lead download retention (reported 90 days).
6. Whether a "higher intent" lead gen form option still exists.
7. In-Stream Ads alpha, Creator Marketplace expansion, CTV markets beyond US and Canada, brand safety inventory warnings.
8. Talent leads objective status; current Ads Guide specs for single image, video, document, message and conversation ads.
9. Whether LinkedIn or Microsoft releases an official LinkedIn Ads MCP server or widens the ChatGPT app beyond read only.
10. Restricted category list and discrimination rules by region.
11. LinkedIn's next fiscal results (FY27 Q1, late October 2026) for Marketing Solutions growth.

## 12. Sources
1. LinkedIn Marketing Solutions. LinkedIn. https://business.linkedin.com/marketing-solutions. Rolling.
2. LinkedIn Help Center, Marketing Solutions. LinkedIn. https://www.linkedin.com/help/lms. Rolling.
3. LinkedIn Marketing Blog. LinkedIn. https://www.linkedin.com/business/marketing/blog. Rolling.
4. LinkedIn Marketing API documentation. Microsoft Learn. https://learn.microsoft.com/en-us/linkedin/marketing/. Rolling.
5. LinkedIn Advertising Policies. LinkedIn. https://www.linkedin.com/legal/ads-policy. Rolling.
6. LinkedIn Ad Library. LinkedIn. https://www.linkedin.com/ad-library. Rolling.
7. LinkedIn Campaign Manager. LinkedIn. https://www.linkedin.com/campaignmanager. Rolling.
8. LinkedIn B2B Institute. LinkedIn. https://business.linkedin.com/marketing-solutions/b2b-institute. 2019 to 2025.
9. Advertising effectiveness and the 95-5 rule (John Dawes). Ehrenberg-Bass Institute for the LinkedIn B2B Institute. Via sources 8 and 122. 2021.
10. The 5 Principles of Growth in B2B Marketing (Les Binet, Peter Field). LinkedIn B2B Institute. https://business.linkedin.com/advertise/resources/b2b-institute/marketing-as-growth. 2019.
11. B2B buying journey research (buying group size). Gartner. gartner.com. 2022 to 2024 editions; see 123 for Forrester.
12. Accelerate campaigns announcement. LinkedIn Marketing Blog. Via source 3. 2023-10.
13. Lookalike audiences retirement. Superseded by source 100.
14. Thought Leader Ads expansion. Superseded by source 89.
15. Conversions API launch. LinkedIn. Via sources 3 and 4. 2023.
16. Revenue attribution report. Superseded by sources 108 and 109.
17. Business Manager. LinkedIn Help Center. Via source 2. 2023.
18. BrandLink and CTV announcements. Superseded by sources 74 to 79.
19. EU Group targeting change. Superseded by sources 104 and 105.
20. Member data and AI training terms update. Superseded by sources 106 and 107.
21. linkedin-api-python-client. LinkedIn (GitHub). https://github.com/linkedin-developers/linkedin-api-python-client. 2023-01-12.
22. linkedin-api-js-client. LinkedIn (GitHub). https://github.com/linkedin-developers/linkedin-api-js-client. 2022-12-28.
23. linkedin-capi-tag-template. LinkedIn (GitHub). https://github.com/linkedin-developers/linkedin-capi-tag-template. 2023-08-30.
24. reactor-extension-linkedin-edge. LinkedIn (GitHub). https://github.com/linkedin-developers/reactor-extension-linkedin-edge. 2026-06-24.
25. java-sample-application. LinkedIn (GitHub). https://github.com/linkedin-developers/java-sample-application. 2021-10-08.
26. Less busywork, more growth: What's new in Microsoft Advertising this September. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/september-2026/less-busywork-more-growth-what-new-in-microsoft-advertising-this-september. 2026-09-30.
27. New Performance Max tools and other product updates for February. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/february-2025/new-performance-max-tools-and-other-product-updates-for-february. 2025-02.
28. Ads Studio in Editor and other product updates for May. Microsoft Advertising. https://about.ads.microsoft.com/en/blog/post/may-2025/ads-studio-in-editor-and-other-product-updates-for-may. 2025-05.
29. Microsoft Advertising gains LinkedIn company lists of up to 10,000 firms. PPC Land. https://ppc.land/microsoft-advertising-gains-linkedin-company-lists-of-up-to-10-000-firms. 2026-09.
30. Microsoft Ads experiments GA, plus HubSpot and REST news. Relevant Audience. https://www.relevantaudience.com/digital-marketing-en/microsoft-advertising-optimization-experiments-september-2026/. 2026-09.
31. danielpopamd/linkedin-ads-mcp. GitHub. https://github.com/danielpopamd/linkedin-ads-mcp. 2026-01-20.
32. amekala/ads-mcp. GitHub. https://github.com/amekala/ads-mcp. 2025-10-27.
33. markifact/markifact-mcp. GitHub. https://github.com/markifact/markifact-mcp. 2026-05-03.
34. adkit/ads-mcp. GitHub. https://github.com/adkit/ads-mcp. 2026-05-19.
35. stan-rym/liam-linkedin-ads-MCP. GitHub. https://github.com/stan-rym/liam-linkedin-ads-MCP. 2026-06-14.
36. Nuraveda/linkedin-ads-mcp. GitHub. https://github.com/Nuraveda/linkedin-ads-mcp. 2026-05-29.
37. DanielSylvester/linkedin-ads-mcp. GitHub. https://github.com/DanielSylvester/linkedin-ads-mcp. 2026-05-25.
38. proxy-intell/linkedin-ads-library-mcp. GitHub. https://github.com/proxy-intell/linkedin-ads-library-mcp. 2026-08-05.
39. CDataSoftware/linkedin-ads-mcp-server-by-cdata. GitHub. https://github.com/CDataSoftware/linkedin-ads-mcp-server-by-cdata. 2025-06-23.
40. pipeworx-io/mcp-linkedin_ads. GitHub. https://github.com/pipeworx-io/mcp-linkedin_ads. 2026-04-15.
41. Synter-Media-AI/mcp-server. GitHub. https://github.com/Synter-Media-AI/mcp-server. 2026-01-29.
42. PaidSync/paidsync-mcp. GitHub. https://github.com/PaidSync/paidsync-mcp. 2026-05-11.
43. opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms. GitHub. https://github.com/opusgrowth/Opus-Growth-The-MCP-Connector-for-Ad-Platforms. 2026-07-10.
44. jshorwitz/awesome-agentic-advertising. GitHub. https://github.com/jshorwitz/awesome-agentic-advertising. 2026-02-07.
45. Dataslayer-AI/Marketing-skills. GitHub. https://github.com/Dataslayer-AI/Marketing-skills. 2026-03-19.
46. itallstartedwithaidea/advertising-hub. GitHub. https://github.com/itallstartedwithaidea/advertising-hub. 2026-03-10.
47. Recent Marketing API Changes. Microsoft Learn (LinkedIn). https://learn.microsoft.com/en-us/linkedin/marketing/integrations/recent-changes?view=li-lms-2026-09. 2026-09 (covers 202602 to 202609).
48. Conversions FAQ. Microsoft Learn (LinkedIn). https://learn.microsoft.com/en-us/linkedin/marketing/conversions/conversions-faq?view=li-lms-2026-09. 2026-09.
49. Conversions API. Microsoft Learn (LinkedIn). https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/conversions-api?view=li-lms-2026-08. 2026-08.
50. LMS API Documentation Versioning. Microsoft Learn (LinkedIn). https://learn.microsoft.com/en-us/linkedin/marketing/versioning?view=li-lms-2026-05. 2026-05.
51. Campaign Objectives. Microsoft Learn (LinkedIn). https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/campaign-objectives?view=li-lms-2026-09. 2026-09.
52. Event Ads API. Microsoft Learn (LinkedIn). https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/advertising-targeting/version/event-ads-integrations?view=li-lms-2026-05. 2026-05.
53. Create and Manage LinkedIn Campaigns (frequency cap). Microsoft Learn (LinkedIn). https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads/account-structure/create-and-manage-campaigns?view=li-lms-2025-09. 2025-09.
54. LinkedIn conversion window. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/a426359. Rolling, checked 2026-10.
55. Conversions API best practices. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/a5538676. Rolling, checked 2026-10.
56. Conversions API Playbook (PDF). LinkedIn. https://business.linkedin.com/content/dam/me/business/en-us/marketing-solutions/resources/pdfs/Conversions-API-Playbook.pdf. Undated.
57. LinkedIn Launches Qualified Leads Optimization for Custom Ad Targeting. Social Media Today. https://www.socialmediatoday.com/news/linkedin-qualified-leads-optimization-crm-targeting/746055/. 2025-04.
58. LinkedIn Introduces Qualified Leads Optimization. DestinationCRM. https://www.destinationcrm.com/Articles/CRM-News/CRM-Across-the-Wire/LinkedIn-Introduces-Qualified-Leads-Optimization-169110.aspx. 2025-04-22.
59. LinkedIn Renames Ad Campaign Elements. Social Media Today. https://www.socialmediatoday.com/news/linkedin-updates-advertising-campaign-naming-conventions/761534/. 2025-09.
60. LinkedIn Campaign Manager Rename: Reporting Impact. Dataslayer. https://www.dataslayer.ai/blog/linkedin-campaign-manager-rename-2026. 2026.
61. LinkedIn launches frequency capping for brand awareness campaigns. PPC Land. https://ppc.land/linkedin-launches-frequency-capping-for-brand-awareness-campaigns/. 2025-07.
62. Set a frequency cap for your ad set. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/a6573757. Rolling, checked 2026-10.
63. Maximize your budget (minimum budgets). LinkedIn. https://business.linkedin.com/advertise/ads/best-practices/maximize-your-budget. Rolling, checked 2026-10.
64. Campaign and ad set budgets. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/a422101. Rolling, checked 2026-10.
65. Dynamic Group Budget best practices. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/a1502134. Rolling, checked 2026-10.
66. How budgets work on LinkedIn Ads. B2Linked (AJ Wilcox). https://b2linked.com/blog-page/how-budgets-work-on-linkedin-ads. 2025-08.
67. LinkedIn introduces Reserved Ads, ad personalization, new AI tools. Search Engine Land. https://searchengineland.com/linkedin-rolls-out-tools-to-make-b2b-brand-advertising-more-predictable-466019. About 2025-12.
68. LinkedIn launches First Impression Ads. AdNews. https://www.adnews.com.au/news/linkedin-launches-first-impression-ads. 2025-06-05.
69. LinkedIn advertisers gain 20% higher CTR with 5-plus ad variants. PPC Land. https://ppc.land/linkedin-advertisers-gain-20-higher-ctr-with-5-plus-ad-variants/. 2026-07-01.
70. LinkedIn rolls out new AI-powered promotional tools. Social Media Today. https://www.socialmediatoday.com/news/linkedin-rolls-out-new-ai-powered-promotional-tools/824290/. 2026-07.
71. LinkedIn introduces significant updates to Campaign Manager. PPC Land. https://ppc.land/linkedin-introduces-significant-updates-to-campaign-manager/. 2025-03-25.
72. LinkedIn overhauls event ads with off-platform targeting and lead gen forms. PPC Land. https://ppc.land/linkedin-overhauls-event-ads-with-off-platform-targeting-and-lead-gen-forms/. 2026-04-28.
73. LinkedIn launches Creator Marketplace and BrandWorks for B2B brands. PPC Land. https://ppc.land/linkedin-launches-creator-marketplace-and-brandworks-for-b2b-brands/. 2026-06-10.
74. LinkedIn expands BrandLink Programme and CTV advertising. Social Samosa. https://www.socialsamosa.com/news-2/linkedin-expands-brandlink-programme-ctv-advertising-11248078. 2026-03.
75. BrandLink. LinkedIn. https://business.linkedin.com/advertise/ads/sponsored-content/brandlink. Rolling (beta), checked 2026-10.
76. LinkedIn expands BrandLink, offers video ads with top creators. eCommerceNews. https://ecommercenews.com.au/story/linkedin-expands-brandlink-offers-video-ads-with-top-creators. 2025-05.
77. LinkedIn CTV ads at its Marketing Summit. Marketing Brew. https://marketingbrew.com/stories/2024/04/03/linkedin-ctv-ads-marketing-summit. 2024-04-03.
78. LinkedIn partners with Paramount, levels up emerging CTV ad game. StreamTV Insider. https://www.streamtvinsider.com/advertising/linkedin-partners-paramount-levels-emerging-ctv-ad-game. 2025-06-04.
79. LinkedIn CTV Ads are now available through Amazon DSP. Amazon Ads. https://advertising.amazon.com/library/news/linkedin-ctv-ads-amazon-dsp. 2026-05.
80. LinkedIn Profile Targeting Expands to CTV in Microsoft Ads (with Microsoft clarification). PPC Newsfeed. https://ppcnewsfeed.com/ppc-news/2026-05/linkedin-profile-targeting-expands-ctv-microsoft-ads/. 2026-05.
81. Microsoft Monetize fuses LinkedIn profile data into CTV via three DSPs. PPC Land. https://ppc.land/microsoft-monetize-fuses-linkedin-profile-data-into-ctv-via-three-dsps/. 2026-05.
82. DoubleVerify delivers global media quality measurement for LinkedIn Audience Network. GlobeNewswire. https://www.globenewswire.com/news-release/2026/05/21/3299391/0/en/doubleverify-delivers-global-media-quality-measurement-for-linkedin-audience-network-elevating-transparency-for-b2b-advertisers.html. 2026-05-21.
83. LinkedIn Product Updates: September 2026 Recap. Influent. https://influent.co/blog/linkedin-updates-september-2026. 2026-09.
84. How do I book meetings from LinkedIn Lead Gen Forms? Chili Piper Help Center. https://help.chilipiper.com/hc/en-us/articles/52302755601683-How-do-I-book-meetings-from-LinkedIn-Lead-Gen-Forms. 2026.
85. LinkedIn offers tips on company targeting via Campaign Manager. Social Media Today. https://www.socialmediatoday.com/news/linkedin-offers-tips-on-company-targeting-via-campaign-manager/830615/. 2026-09-16.
86. Measure engagement and reach buyers with insights from LinkedIn's new Companies Hub. CMSWire. https://www.cmswire.com/the-wire/measure-engagement-and-reach-buyers-with-insights-from-linkedins-new-companies-hub. 2024.
87. Thought Leader Ads. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/a1399568. Rolling, checked 2026-10.
88. Thought Leader Ads. LinkedIn. https://business.linkedin.com/advertise/ads/sponsored-content/thought-leader-ads. Rolling, checked 2026-10.
89. LinkedIn expands Thought Leader Ads. PPC Land. https://ppc.land/thought-leader-ads. 2024-03.
90. LinkedIn Thought Leader Ads Benchmarks 2026. Kiin. https://kiin.co/research/linkedin-thought-leader-ads-benchmarks. 2026-09.
91. LinkedIn Ads Benchmarks 2026: CTR, CPC, CPM, CPL. Kiin. https://kiin.co/linkedin-ads-benchmarks. 2026-09.
92. LinkedIn Lead Gen Forms Benchmarks 2026. Kiin. https://kiin.co/research/linkedin-lead-gen-forms-benchmarks. 2026.
93. LinkedIn CTV Ads 2026: Cost, Benchmarks, Specs (31 Accounts). Kiin. https://kiin.co/research/linkedin-ctv-ads-benchmarks. 2026.
94. LinkedIn Ads Benchmarks for HR Audiences 2026 (113 Accounts). Kiin. https://kiin.co/research/linkedin-ads-benchmarks/hr-audience. 2026.
95. Announcing The LinkedIn Ads 2026 Benchmarks Report. Dreamdata. https://dreamdata.io/blog/announcing-linkedin-ads-benchmarks-report-2026. 2026 (data 2024-08 to 2025-07).
96. The 2025 LinkedIn Ads Benchmarks Report has dropped: highlights. Dreamdata. https://dreamdata.io/blog/dreamdata-2025-linkedin-ads-benchmarks-report-highlights. 2025.
97. 2025 LinkedIn Ads Benchmark Report for B2B Marketers. HockeyStack. https://www.hockeystack.com/lab-blog-posts/linkedin-ads-benchmarks. 2025.
98. LinkedIn Ads Benchmarks 2026: CPM, CPC, CTR and CPL. The Smarketers. https://thesmarketers.com/blogs/linkedin-ads-benchmarks-2026/. 2026 (data to Q1 2026).
99. LinkedIn Ad Benchmarks: CTR, CPC, and Conversion Rate. Metadata.io. https://metadata.io/resources/blog/linkedin-ad-benchmarks/. 2021 data.
100. LinkedIn lookalike audiences have been discontinued. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/94287. 2024-02-29.
101. Transform Your LinkedIn Campaigns with Predictive Audiences. Carnegie Higher Ed. https://www.carnegiehighered.com/linkedin-predictive-audiences-for-higher-ed/. Undated (2024 to 2025).
102. Sponsored Messaging. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/71201. Rolling, checked 2026-10.
103. Conversation ads. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/104116. Rolling (EU targeting since 2024-10).
104. LinkedIn to limit targeted ads in EU after complaint over sensitive data use. TechCrunch. https://techcrunch.com/2024/06/07/linkedin-to-limit-targeted-ads-in-eu-after-complaint-over-sensitive-data-use. 2024-06-07.
105. A privacy win! LinkedIn restricts ad targeting after our complaint. Bits of Freedom. https://www.bitsoffreedom.nl/en/2024/06/27/linkedin-restricts-ad-targeting-after-our-complaint/. 2024-06-27.
106. LinkedIn updates terms of service for AI and ad targeting with Microsoft. HR Dive. https://hrdive.com/news/linkedin-updates-terms-of-service-ai-ad-targeting-microsoft/760614. 2025-09.
107. LinkedIn to Tighten Data Rules, Expand Microsoft Ad Sharing and AI Training on November 3. Digital Information World. https://www.digitalinformationworld.com/2025/09/linkedin-to-tighten-data-rules-expand.html. 2025-09.
108. Revenue Attribution Report Overview. LinkedIn. https://business.linkedin.com/marketing-solutions/revenue-attribution-report. Rolling, checked 2026-10.
109. LinkedIn Business Manager Revenue Attribution Report getting started guide v01 (PDF hosted by PPC Land). LinkedIn. https://ppc.land/content/files/2025/07/linkedin-business-manager-revenue-attribution-report-getting-started-guide-v01.pdf. 2025-07.
110. Lead Gen Form fields. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/79852. Rolling, checked 2026-10.
111. Lead Gen Form hidden fields. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/a421421/. Rolling, checked 2026-10.
112. Carousel Ads advertising specifications. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/88137. Rolling, checked 2026-10.
113. Accelerate Getting Started Guide (PDF). LinkedIn. https://business.linkedin.com/content/dam/lem/business/de/advertise/ads/linkedin-accelerate/Accelerate-Getting-Started-Guide.pdf. Undated (about 2024).
114. LinkedIn Unveils Live Event Ads and Accelerate Campaigns for B2B Marketing. Swipe Insight. https://web.swipeinsight.app/posts/linkedin-unveils-live-event-ads-and-accelerate-campaigns-for-b2b-marketing-11753. 2024-10-15.
115. LinkedIn is officially rolling out its own AI-campaign tool. Digiday. https://digiday.com/marketing/linkedin-is-officially-rolling-out-its-own-ai-campaign-tool/. 2024.
116. LinkedIn marketing strategy: How to grow in 2026. Hootsuite. https://blog.hootsuite.com/linkedin-marketing-strategy/. 2026.
117. LinkedIn Accelerate Campaigns: Honest Review (2026). Optimize LinkedIn Ads. https://www.optimizelinkedinads.com/blogs/linkedin-accelerate-review. 2026.
118. LinkedIn Ads plugin for ChatGPT. OpenAI. https://openai.com/business/plugins/linkedin-ads/. 2026 (beta).
119. LinkedIn Ads MCP: No Official Server Yet (July 2026 Guide). The Ad Spend. https://theadspend.com/blog/linkedin-ads-mcp. 2026-07.
120. LinkedIn Ads MCP Server with Full Write Access (status check 2026-09-27). PaidSync. https://paidsync.ai/linkedin-ads-mcp. 2026-09.
121. Why LinkedIn says building "owned prominence" beats rented ads in B2B marketing. PPC Land. https://ppc.land/why-linkedin-says-building-owned-prominence-beats-rented-ads-in-b2b-marketing/. 2025-12.
122. 95-5 Rule. LinkedIn B2B Institute. https://business.linkedin.com/advertise/resources/b2b-institute/b2b-research/trends/95-5-rule. Rolling.
123. Forrester: To master B2B buying mayhem, providers must prioritize (State of Business Buying 2024 release). Stock Titan (Forrester press release). https://www.stocktitan.net/news/FORR/forrester-to-master-b2b-buying-mayhem-providers-must-prioritize-biyipkl01ko0.html. 2024-12.
124. LinkedIn hits 1.2 billion members; Satya Nadella highlights AI driven growth. IANS. https://ianslive.in/linkedin-hits-12-billion-members-microsoft-ceo-satya-nadella-highlights-ai-driven-growth-across-platforms--20251022105445. 2025-10-22.
125. LinkedIn Audience Network. LinkedIn Help Center. https://www.linkedin.com/help/lms/answer/a420372. Rolling, checked 2026-10.
126. 5 pitfalls that are killing your LinkedIn ads performance. B2Linked (AJ Wilcox). https://b2linked.com/blog-page/5-pitfalls-that-are-killing-your-linkedin-ads-performance. 2026-05-20.
127. LinkedIn Campaign Manager Tutorial 2026: Every Setting Explained. Kiin. https://kiin.co/blog/linkedin-campaign-manager. 2026.
128. LinkedIn release notes (aggregator). Releasebot. https://releasebot.io/updates/linkedin. 2026-09.
129. LinkedIn Insight Tag in GTM. Piotr Litwa. https://piotrlitwa.com/articles/en/linkedin-insight-tag-gtm.html. 2026 (undated).
130. LinkedIn Ads Strategy for 2026: Q and A with AJ Wilcox (Part 2). MarketingProfs. https://www.marketingprofs.com/articles/2026/55621/linkedIn-ads-tips-aj-wilcox. 2026-08.
131. What you need to know about advertising on LinkedIn in 2026. Funnel. https://funnel.io/blog/linkedin-advertising-2026. 2026.
132. LinkedIn Ad Specs and Sizes 2026. Kiin. https://kiin.co/blog/linkedin-ad-specs. 2026.
133. Innovid Expands Integration with LinkedIn to Support CTV Ads. Business Wire. https://secure.businesswire.com/news/home/20250721295367/en/Innovid-Expands-Integration-with-LinkedIn-to-Support-CTV-Ads. 2025-07-21.
134. LinkedIn now supports Dynamic UTMs. PPC Land. https://ppc.land/linkedin-now-supports-dynamic-utms/. 2024-03.
135. LinkedIn Launches Wire Program for In-Stream Video Ads On Publisher Content. Lindsey Gamble. https://www.lindseygamble.com/blog/linkedin-launches-wire-program-for-in-stream-video-ads-on-publisher-content. 2024-06.
136. LinkedIn's Dynamic Group Budget is now rolling out. Morten Bie (LinkedIn post). https://www.linkedin.com/posts/morten-bie_linkedins-dynamic-group-budget-is-now-rolling-activity-7069969645146968064-v4Kz. About 2023-06.
137. Predictive Audiences Getting Started Guide (PDF). LinkedIn. https://business.linkedin.com/content/dam/me/business/en-us/marketing-solutions/resources/pdfs/predictive-audiences-getting-started-guide.pdf. Undated (2024).
138. LinkedIn DMP segment cap of 1,000 and audience cleanup. Digital Applied. https://www.digitalapplied.com/blog/linkedin-dmp-segment-cap-1000-audience-cleanup. 2026-08-18.
