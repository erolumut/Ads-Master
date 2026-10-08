# Targeting and ABM

> Scope: targeting attributes, job title vs function and seniority vs skills, audience sizing, matched audiences (website, contact, company, engagement), predictive audiences, exclusions, Audience expansion and LinkedIn Audience Network pitfalls, regional restrictions, and account based marketing with the company engagement report.

## 1. Targeting attributes (Campaign Manager)

| Category | Attributes | Notes |
|----------|-----------|-------|
| Location | Countries, regions, cities, metro areas | Required; choose recent or permanent location handling deliberately [Unverified] for option names |
| Company | Company names, industries, company size, followers of company, company connections, growth rate, category lists | Industries and sizes come from company pages, so small or new firms can be misclassified |
| Demographics | Member age, member gender | Inferred; restricted for some ad categories and regions; avoid unless justified |
| Education | Degrees, fields of study, schools | Useful for specialist roles (for example clinicians, engineers) |
| Job experience | Job functions, job seniorities, job titles, member skills, years of experience | Core B2B layer |
| Interests and traits | Member interests, member groups, member traits | Lower precision; Group targeting removed for EU members in 2024 [Unverified] |
| Matched audiences | Website, contact lists, company lists, engagement audiences, predictive audiences | See section 4 |

Logic: values within one attribute combine with OR; different attributes combine with AND ("narrow audience further"). Exclusions apply across the campaign [Official, 2020].

Audience floor: 300 members minimum to run [Official, 2023]. Practical sizes:
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
B2B purchases involve several roles; widely cited research puts typical buying groups at 6 to 10 people [Study, Gartner, as widely cited].
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
| Website retargeting | Insight Tag visitors, by URL rules | Lookback up to 180 days [Unverified] | Pricing, demo, product page visitors |
| Contact list | Uploaded emails (hashed by LinkedIn), CRM integrations | 300 matched members minimum; list size limits apply [Unverified] | Pipeline acceleration, customer exclusions, nurture |
| Company list | Uploaded company names, domains or LinkedIn URLs, or ABM platform syncs | Up to 300,000 companies per list [Unverified] | ABM, customer exclusion |
| Video viewers | People who watched 25%, 50%, 75%, 97% | Lookbacks 30 to 365 days [Unverified] | Next step after video |
| Lead gen form | Opened or submitted forms | Lookbacks 30 to 365 days [Unverified] | Re-engage openers who did not submit |
| Event | Event attendees or registrants | Per event | Post event follow up |
| Company page | Page visitors or followers who engaged | Lookbacks vary | Warm retargeting |
| Document ad | Readers by depth | Lookbacks vary | Next step after document |
| Conversation ad | Openers and button clickers | Lookbacks vary | Follow up |
| Single image ad engagement | People who engaged with single image ads | Lookbacks vary [Unverified] | Engagement retargeting |
| Predictive audiences | Built by LinkedIn from a seed (conversions, leads, contact lists) | Seed minimums apply [Unverified] | Replacement for lookalikes (retired 2024-02) |

List hygiene:
- Company lists: include domain and LinkedIn company page URL where available to raise match rates; remove subsidiaries if not targeted; refresh monthly.
- Contact lists: business email plus first and last name, company and title raise matching [Unverified] for current matching fields. Get legal sign off on consent basis before upload.
- Match rate check: matched members or companies / uploaded rows. Investigate any company list under 60% or contact list under 30% [Practitioner consensus].

## 5. Audience expansion and LinkedIn Audience Network
| Setting | What it does | Default stance | When to test on |
|---------|-------------|----------------|-----------------|
| Audience expansion | Adds members similar to your targeting | Off for ABM, lead gen and narrow ICP | Awareness to broad ICP when reach is capped |
| LinkedIn Audience Network | Serves ads on third party apps and sites | Off for lead gen and ABM | Awareness or video views with placement reporting and block lists |

Pitfalls: both settings are commonly on by default for some objectives [Practitioner consensus]. They lower CPMs and CPLs while lowering ICP match. Always check new campaigns for these toggles and record the decision.

Test design: duplicate the campaign with the setting on, split budget 50/50, run 4 weeks, judge on qualified leads and the Demographics report share of ICP.

## 6. Regional and policy constraints
- EU: LinkedIn removed the ability to target EU members by LinkedIn Group membership in 2024 after regulatory scrutiny under the Digital Services Act [Unverified]. Check the current list of attributes available for EU audiences.
- Sensitive categories (housing, employment, credit) and some regions restrict demographic targeting [Unverified] for current rules.
- Message and Conversation ads have regional delivery restrictions (historically including the EU) [Unverified].
- Data sharing: LinkedIn announced 2025 changes to how member data is used for generative AI training and shared with Microsoft for ads in some regions [Unverified]; check before planning cross platform audiences.

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
6. Sales activation: weekly export of engaged accounts from the company engagement report to sales and SDRs.
7. Measure: account reach %, engagement level changes, meetings, opportunities and pipeline from target accounts (CRM), influenced revenue (revenue attribution report where available).

### Company engagement report
Campaign Manager provides company level engagement (impressions, clicks, engagement level, paid and organic engagement) for companies reached, filterable by company list [Official, 2023] [Unverified] for current metrics. Use it to:
- Rank accounts by engagement change month over month.
- Find accounts with rising engagement but no sales activity; send to sales.
- Find tier 1 accounts with no impressions; fix list matching or bids.

ABM platforms (for example Demandbase, 6sense, ZoomInfo and others) integrate with LinkedIn to sync account lists and intent driven segments [Practitioner consensus]; confirm integration status in the project's stack.

## 8. Audience plan template
| Campaign | Stage | Audience definition | Exclusions | Estimated size | Expansion | Network | Rationale |
|----------|-------|---------------------|------------|----------------|-----------|---------|-----------|
| | | | | | Off | Off | |
