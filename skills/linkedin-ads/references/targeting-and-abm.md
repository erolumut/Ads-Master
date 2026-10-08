# Targeting and ABM

> Scope: targeting attributes, job title vs function and seniority vs skills, audience sizing, matched audiences (website, contact, company, engagement), predictive audiences, exclusions, Audience expansion and LinkedIn Audience Network pitfalls, regional restrictions (EU, EEA, UK, Switzerland), and account based marketing with the Companies tab (formerly the company engagement report).

## 1. Targeting attributes (Campaign Manager)

| Category | Attributes | Notes |
|----------|-----------|-------|
| Location | Countries, regions, cities, metro areas | Required; choose recent or permanent location handling deliberately [Unverified] for option names |
| Company | Company names, industries, company size, followers of company, company connections, growth rate, category lists | Industries and sizes come from company pages, so small or new firms can be misclassified |
| Demographics | Member age, member gender | Inferred; restricted for some ad categories and regions; avoid unless justified |
| Education | Degrees, fields of study, schools | Useful for specialist roles (for example clinicians, engineers) |
| Job experience | Job functions, job seniorities, job titles, member skills, years of experience | Core B2B layer |
| Interests and traits | Member interests, member groups, member traits | Lower precision; Group targeting disabled for members in the EU single market on 2024-06-07 after a Digital Services Act complaint and a Commission request for information [Official, 2024-06] |
| Matched audiences | Website, contact lists, company lists, engagement audiences, predictive audiences, Companies tab engagement lists | See section 4 |

Logic: values within one attribute combine with OR; different attributes combine with AND ("narrow audience further"). Exclusions apply across the campaign [Official, 2020].

Audience floor: an ad set needs at least 300 member accounts to serve; smaller segments can be combined in one ad set [Official, 2026-10]. Practical sizes:
| Use | Practical size |
|-----|---------------|
| Retargeting, ABM tier 1 | 300 to 20,000 members |
| ICP cold acquisition, Sponsored Content | 20,000 to 500,000 members [Practitioner consensus] |
| Message or Conversation ads | Smaller lists acceptable; delivery is per send |
| Brand awareness | As large as the ICP allows |

## 2. Job title vs function and seniority vs skills

| Approach | Precision | Scale | Main risk | Best for |
|----------|-----------|-------|-----------|----------|
| Job titles | High when titles are standard | Low to medium | Title sprawl (thousands of variants), misses non standard titles | ABM tier 1, narrow roles (CISO, CFO, VP RevOps) |
| Job function plus seniority | Medium | High | Function misclassification, includes adjacent roles | Cold acquisition at scale, buying committee coverage |
| Skills | Medium | Medium to high | Self reported, includes students and juniors | Practitioners and technical users |
| Function plus seniority plus industry plus company size | Medium high | Medium | Over narrowing | Default ICP build |
| Company list plus function or seniority | Highest relevance | Small | Low match rates | ABM |

Procedure to build a role audience:
1. Start from CRM: titles of contacts on won and late stage deals over 12 to 24 months.
2. Map titles to LinkedIn functions and seniorities; list the top 20 titles separately.
3. Build two candidate audiences: (A) function plus seniority plus firmographics, (B) title list plus firmographics.
4. Compare sizes in the forecast panel. If A is more than 5x B, run both as separate campaigns with the same creative for 3 to 4 weeks.
5. After 2 weeks, check the Demographics report for each: share of impressions on target titles, seniorities and company sizes.
6. Keep the audience with the better cost per qualified lead, not the lower CPL.

Exclusion layer (most accounts):
- Seniority: Unpaid, Training (students, interns) unless relevant.
- Job function: functions outside the buying committee (often HR or Education for software not sold to them).
- Titles: "recruiter", "student", "intern", "assistant" as needed.
- Companies: existing customers (company list), competitors, your own company, partners.
- Contacts: current pipeline if sales prefers a separate sequence.

## 3. Buying committee mapping
B2B purchases involve several roles. Forrester's State of Business Buying 2024 reported 13 people involved on average, with 89% of purchases spanning two or more departments [Study, 2024-12]; Gartner has published 5 to 11 (2024) and 6 to 10 stakeholders [Study, 2024]. Reports of a 2026 Forrester figure of 13 internal plus 9 external influencers were not traced to a primary source [Unverified]. Definitions differ (decision makers only vs everyone with influence), so plan for 6 to 13 roles in mid market and enterprise deals.
| Role | Typical LinkedIn layer | Message focus |
|------|-----------------------|---------------|
| Economic buyer | Seniority: VP, CXO, Owner, Partner in relevant function | Business outcome, risk, ROI |
| Champion | Seniority: Manager, Director in the user function | Day to day pain, career win |
| User | Seniority: Entry, Senior in the user function, skills | Workflow, ease |
| Technical evaluator | Function: IT, Engineering; skills | Security, integration |
| Procurement or finance | Function: Purchasing, Finance | Pricing clarity, terms |
Build one campaign per 1 to 2 roles with role specific creative when budget allows; otherwise one audience with rotating role angles.

## 4. Matched audiences

| Type | Source | Window or limits (as known) | Use |
|------|--------|----------------------------|-----|
| Website retargeting | Insight Tag visitors, by URL rules | Lookbacks 30, 60, 90, 180 days; one 2026 guide lists 365 [Contested] | Pricing, demo, product page visitors |
| Contact list | Uploaded emails (hashed by LinkedIn), CRM integrations | 300 matched members minimum to serve; up to 300,000 records per list and 1,000+ recommended for matching per several integration vendors' documentation [Practitioner consensus, 2026] | Pipeline acceleration, customer exclusions, nurture |
| Company list | Uploaded company names, domains or LinkedIn URLs, CRM connection, or ABM platform syncs | 300 to 300,000 companies per list [Practitioner consensus, 2026]; matching can take up to 48 hours [Official, 2026-09] | ABM, customer exclusion |
| Video viewers | People who watched 25%, 50%, 75%, 97% | Lookbacks 30, 60, 90, 180, 365 days [Official, 2024-10 API docs] | Next step after video |
| Lead gen form | Opened or submitted forms | Lookbacks 30, 60, 90, 180, 365 days [Official, 2024-10 API docs] | Re-engage openers who did not submit |
| Event | Event attendees or registrants | Per event | Post event follow up |
| Company page | Page visitors or followers who engaged | Lookbacks 30 to 365 days [Official, 2024-10 API docs] | Warm retargeting |
| Document ad | Readers by depth | Lookbacks vary | Next step after document |
| Conversation ad | Openers and button clickers | Lookbacks vary | Follow up |
| Single image ad engagement | People who engaged with single image ads | Lookbacks 30 to 365 days [Official, 2024-10 API docs] | Engagement retargeting |
| Companies tab list | Companies by engagement level (paid plus organic engagement, website visits) | One click company list creation from engaged companies [Official, 2026-09] | ABM retargeting by engagement stage |
| Predictive audiences | Built by LinkedIn from one source type: contact list, company list, conversion (including CAPI), Lead Gen Form or retargeting audience | Source needs a total of 300+ members (LinkedIn getting started guide); contact list sources 300 to 300,000 rows; only one source type per audience (several sources of the same type can be stacked); refreshes daily [Official, 2024-02]; up to 30 predictive audiences per ad account, not shareable across accounts [Practitioner consensus, 2026] (two agency guides); a reported API cap of 1,000 DMP segments per account (matched plus predictive) from 202608 [Unverified] | Replacement for lookalikes (discontinued 2024-02-29; existing lookalikes froze and unused ones archived after 30 days) |

List hygiene:
- Company lists: include domain and LinkedIn company page URL where available to raise match rates; remove subsidiaries if not targeted; refresh monthly.
- Contact lists: business email plus first and last name, company and title raise matching [Unverified] for current matching fields. Get legal sign off on consent basis before upload.
- Match rate check: matched members or companies / uploaded rows. Investigate any company list under 60% or contact list under 30% [Practitioner consensus].

## 5. Audience expansion and LinkedIn Audience Network
| Setting | What it does | Default stance | When to test on |
|---------|-------------|----------------|-----------------|
| Audience expansion | Adds members similar to your targeting | Off for ABM, lead gen and narrow ICP | Awareness to broad ICP when reach is capped |
| LinkedIn Audience Network | Serves ads on third party apps and sites | Off for lead gen and ABM | Awareness or video views with placement reporting and block lists |

Defaults: LinkedIn Audience Network is automatically enabled for new single image, carousel, document and video ad sets; the checkbox sits in the Placements section [Official, 2026-10]. Audience expansion is reported on by default in many ad sets (B2Linked, 2026-05) and sits as a checkbox in the Audience section [Practitioner consensus, 2026-05]. LinkedIn positions Audience expansion as the lookalike replacement for matched audiences and attribute targeting [Official, 2024-02]. Both lower CPMs and CPLs while lowering ICP match. Always check new ad sets for these toggles and record the decision.

Audience Network quality controls (if you test it): DoubleVerify post-bid measurement (invalid traffic, viewability, brand suitability, geography, site level reporting) went live globally on 2026-05-21 [Official, 2026-05]; Campaign Manager warns when brand safety allowlists, blocklists or suitability settings leave too little Audience Network or CTV inventory (reported 2026-09) [Unverified]. LinkedIn claims Audience Network adds 3.9x monthly impressions and 66% higher conversion rates vs feed only (internal data, 2025-08) [Unverified]; judge on qualified leads, not on these claims.

Test design: duplicate the campaign with the setting on, split budget 50/50, run 4 weeks, judge on qualified leads and the Demographics report share of ICP.

## 6. Regional and policy constraints
| Constraint | Detail | Label |
|-----------|--------|-------|
| EU Group targeting | Advertisers cannot build audiences from LinkedIn Group membership for members in the EU single market since 2024-06-07 (DSA complaint by EDRi, GFF, Global Witness and Bits of Freedom; Commission request for information 2024-03-14; case closed) | [Official, 2024-06] |
| Sponsored Messaging in the EEA and Switzerland | Blocked for EU members from 2021-12-15 (new) and 2022-01-10 (existing) after a CJEU ePrivacy ruling; since mid October 2024 Message and Conversation ads can target the EEA and Switzerland again, but only members who opted in to Sponsored Messaging receive them. Some localized LinkedIn pages still describe the old ban | [Official, 2024-10] |
| Data sharing with Microsoft for ads | From 2025-11-03 LinkedIn shares more member data (profile details, ad engagement) with Microsoft for ad personalization in most regions, excluding the EU, EEA, UK and Switzerland; members can opt out under Settings > Advertising data | [Official, 2025-11] |
| Generative AI training | From 2025-11-03 member profile and public content is used for AI training by default in the EU, EEA, UK, Switzerland, Canada and Hong Kong (opt out under Data privacy); legal basis legitimate interests in the EEA | [Official, 2025-11] |
| Microsoft Advertising use of LinkedIn data | LinkedIn profile targeting in Microsoft Search and Audience campaigns excludes EEA, UK and Swiss users [Official, 2026-09]; LinkedIn profile targeting is not available for Microsoft CTV campaigns (Microsoft clarification after a 2026-05 report) | [Official, 2026-05] |
| Sensitive categories | Housing, employment and credit carry targeting limits in some regions; age and gender targeting restricted for some categories | [Unverified] for the current list |

## 7. ABM on LinkedIn

### Account tiering
| Tier | Accounts | Approach | Budget logic |
|------|----------|----------|--------------|
| Tier 1 | 10 to 100 named accounts | Account or industry specific creative, all buying committee roles, sales coordinated plays | Highest spend per account; Manual or Cost cap bidding to control CPMs |
| Tier 2 | 100 to 1,000 | Industry or segment creative, key roles | Medium |
| Tier 3 | 1,000 to 10,000+ | ICP level creative, programmatic coverage | Lowest per account |

### ABM program steps
1. Agree the account list and tiers with sales; upload as company lists per tier.
2. Build role layers per tier (function plus seniority).
3. Air cover: Thought Leader Ads, video and document ads to all tiers (Brand awareness or Engagement).
4. Engagement retargeting: people at target accounts who engaged get proof (case studies) and conversation ads or event invites.
5. Conversion: demo or assessment offers to engaged accounts.
6. Sales activation: weekly export of engaged accounts from the Companies tab to sales and SDRs.
7. Measure: account reach %, engagement level changes, meetings, opportunities and pipeline from target accounts (CRM), influenced revenue (revenue attribution report where available).
8. Search complement: share the tier list with microsoft-ads; Microsoft Search and Audience campaigns accept LinkedIn company lists of up to 10,000 companies (outside the EEA, UK and Switzerland) [Official, 2026-09].

### Companies tab (formerly the company engagement report)
LinkedIn replaced the company engagement report with a Companies view (announced as Companies Hub, available globally) under Plan > Companies [Official, 2024]. Verified features [Official, 2026-09]:
- Company level paid and organic engagement plus website visits, with an engagement level (very high, high, medium, low) relative to members targeted.
- Filters by company list, company size, industry, job seniority and engagement level; date ranges reported as 7 to 180 days in 2026 guides (90 days in 2025 guides).
- One click company list creation from engaged companies, to retarget by engagement stage.
- LinkedIn's own 2026-09 guidance: upload a company list or connect the CRM, filter by engagement level, apply the seniority filter to confirm decision makers, and retarget highly engaged companies.
- Limitation: data rolls up by account, not by ad, so it cannot show which message moved an account [Practitioner consensus].
- API: the Company Intelligence API (accountIntelligence) added campaignGroup, objectiveType and seniority filters in 202609; seniority works only with the LAST_90_DAYS window [Official, 2026-09].

Use it to:
- Rank accounts by engagement change month over month.
- Find accounts with rising engagement but no sales activity; send to sales.
- Find tier 1 accounts with no impressions; fix list matching or bids.

ABM platforms (for example Demandbase, 6sense, ZoomInfo and others) integrate with LinkedIn to sync account lists and intent driven segments [Practitioner consensus]; confirm integration status in the project's stack.

## 8. Audience plan template
| Campaign | Stage | Audience definition | Exclusions | Estimated size | Expansion | Network | Rationale |
|----------|-------|---------------------|------------|----------------|-----------|---------|-----------|
| | | | | | Off | Off | |
