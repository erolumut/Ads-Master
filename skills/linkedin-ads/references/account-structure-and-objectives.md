# Account Structure and Objectives

> Scope: Business Manager and ad account setup, campaign hierarchy, objectives and optimization goals, Accelerate campaigns, naming conventions and reference structures by tier. Labels: [Official, YYYY] marks long standing mechanics with the year they were established; [Unverified] marks items to check in Campaign Manager before relying on them.

## 1. Setup checklist (new or inherited account)

| # | Item | Why | How |
|---|------|-----|-----|
| 1 | Business Manager with the company as owner | Central control of ad accounts, pages and people; avoids accounts owned by former staff or agencies | Create Business Manager, add ad accounts and pages, assign roles [Official, 2023] |
| 2 | Ad account owned by the company, billing in the company name | Ownership and invoices | Account settings, billing center |
| 3 | User roles by least privilege | Security | Account manager, campaign manager, creative manager, viewer, billing admin |
| 4 | Company page linked and admins assigned | Ads run from the page; Thought Leader Ads need page and member permissions | Page admin settings |
| 5 | Insight Tag installed site wide | Conversions, retargeting, Demographics of site visitors | GTM or site header; see [Measurement](measurement-capi-and-attribution.md) |
| 6 | Conversion rules created and recording | Optimization and reporting | Campaign Manager > Analyze or Data > Conversion tracking [Unverified] for current menu path |
| 7 | CRM connection for lead sync | Speed to lead, stage feedback | Native integrations (HubSpot, Salesforce, Dynamics and others) |
| 8 | Matched audiences: website retargeting segments, company list, contact list, engagement audiences | Retargeting and ABM foundations | Plan, then upload with approval |
| 9 | Exclusion lists: customers, employees, competitors, partners | Avoid waste | Company and contact lists |
| 10 | Naming convention agreed | Reporting via API and exports | See section 6 |

## 2. Hierarchy

| Level | Holds | Practice |
|-------|-------|----------|
| Ad account | Billing, Insight Tag, conversions, matched audiences, lead forms | One per business unit or region with separate budgets or legal entities |
| Campaign group | Campaigns, optional group budget and schedule, status | Group by program or funnel stage (for example "TOFU thought leadership", "ABM tier 1", "Retargeting", "Lead capture") |
| Campaign | Objective, audience, format, bidding, budget, schedule, conversion tracking | One objective, one audience, one format family per campaign |
| Ad | Creative, copy, destination, lead form | 2 to 4 active ads per campaign |

Format note: a campaign is tied to a format family (for example single image, video, document, carousel, conversation, message, event, text, dynamic). Mixed format testing needs separate campaigns or the format choices the objective allows [Official, 2024].

## 3. Objectives and optimization goals

| Funnel stage | Objective | Typical optimization goals | Use when | KPI |
|--------------|-----------|---------------------------|----------|-----|
| Awareness | Brand awareness | Impressions, reach | Demand creation in the ICP, new category, ABM air cover | Reach in ICP, frequency, lift |
| Consideration | Website visits | Landing page clicks, clicks, impressions | Driving content consumption, retargeting pools | Cost per landing page view, engaged sessions |
| Consideration | Engagement | Engagement clicks, impressions; also used for follower and event growth | Thought Leader Ads, social proof, event promotion | Cost per engagement, retargetable engagers |
| Consideration | Video views | Video views, impressions | Video storytelling, building video retargeting pools | Cost per view, completion rate |
| Conversion | Lead generation | Leads (on platform lead gen forms) | Capturing demand with low friction | Cost per qualified lead |
| Conversion | Website conversions | Conversions, landing page clicks, clicks | Demo or trial on site, gated content on site, events | Cost per conversion, qualified rate |
| Conversion | Talent leads, Job applicants | Leads, applications | Recruiting | Cost per qualified applicant |

Verify the current objective list and goals in Campaign Manager; LinkedIn adds and renames goals over time [Unverified] for 2026 changes.

Choosing between Lead generation and Website conversions:
| Factor | Lead gen forms (Lead generation) | Website conversions |
|--------|----------------------------------|--------------------|
| Volume | Higher (pre-filled forms) | Lower |
| Quality | Often lower without qualifying questions | Often higher (more effort) |
| Speed | Needs CRM sync for speed to lead | Site forms flow into CRM already |
| Data | Profile fields from LinkedIn | Site analytics and CRM |
| Use | Gated content, events, demo requests with qualifying question | Free trial, product led signup, demo with scheduling |
Run both as a test when budget allows (see [B2B strategy playbooks](b2b-strategy-playbooks.md)).

## 4. Accelerate campaigns (AI campaigns)

What it is: LinkedIn's AI driven campaign type, announced 2023-10, that builds the audience (using predictive signals), creative suggestions and bidding from a few inputs, mainly for conversion focused objectives [Official, 2023]. Objective coverage, minimum data requirements and available controls in 2026 are in the verification queue [Unverified].

When to test:
- Insight Tag conversions or lead form leads are recording reliably (aim for 30 or more conversions per month at account level).
- A manual "classic" campaign with the same objective and offer exists as the control.
- The offer is broad enough for the ICP (a demo or trial, not a niche event).

How to test:
1. Create the Accelerate campaign with the same offer and budget as the control.
2. Exclude customers, employees and competitors if the setup allows exclusions [Unverified].
3. Run 4 to 6 weeks or until each side has 30+ results.
4. Compare on CRM qualified leads and pipeline, then CPL. Check Demographics report: who did it reach?
5. Keep the winner; log in EXPERIMENTS.md.

Risk: automated audiences can drift away from the ICP toward cheaper members. The Demographics report and lead quality data are the guardrail.

## 5. Reference structures by tier

### Starter (under $3k per month)
| Campaign group | Campaign | Objective | Audience | Budget share |
|----------------|----------|-----------|----------|--------------|
| Core | ICP cold | Lead generation or Website conversions | Function plus seniority plus industry plus size (ICP), 20k to 80k members | 60% |
| Core | Retargeting | Lead generation | Website visitors 90 days plus engagers | 40% |
Notes: no Audience Network, no expansion, Maximum delivery with daily caps; one offer at a time.

### Growth ($3k to $30k)
| Campaign group | Campaigns | Objective | Budget share |
|----------------|-----------|-----------|--------------|
| Demand creation | Thought Leader Ads, video, document (ungated) to ICP | Engagement, Video views, Brand awareness | 30% to 50% |
| ABM tier 1 | Company list plus buying committee roles | Brand awareness or Website visits, then Lead generation | 15% to 25% |
| Retargeting ladder | Engagers and visitors to next step offers | Lead generation, Website conversions | 20% to 30% |
| Lead capture | ICP to demo or high intent offer | Lead generation with qualifying question | 15% to 25% |

### Scale and Enterprise
- Separate campaign groups per region and ICP segment; consistent naming for API reporting.
- Accelerate tests alongside classic campaigns.
- Video programs (BrandLink or CTV where available) for reach [Unverified].
- Brand and conversion lift studies each half year.
- Business Manager governance: who can launch, who approves.

## 6. Naming convention
```
Campaign group: <Region>_<Program>_<Stage>        e.g. NA_ABM-T1_TOFU
Campaign:      <Region>_<Objective>_<Audience>_<Format>_<Offer>_<YYYYMM>
               e.g. NA_LeadGen_ITDM-Sr_DocAd_Checklist_202610
Ad:            <Angle>_<Hook>_<Version>          e.g. CostOfDowntime_Stat_v2
```
Rules: no spaces in parsed fields, fixed vocabulary for Objective (Awareness, Visits, Engage, Video, LeadGen, WebConv), Audience codes documented in the journal.

## 7. Campaign settings checklist (every new campaign)
- [ ] Objective matches the KPI.
- [ ] Locations: permanent or recent location choice made deliberately [Unverified] for current option names.
- [ ] Audience built and saved; size checked in the forecast panel.
- [ ] Audience expansion off (unless tested).
- [ ] LinkedIn Audience Network off for B2B lead gen and ABM (unless tested).
- [ ] Exclusions applied (customers, employees, competitors, job seekers where relevant).
- [ ] Format chosen; 2 to 4 ads ready.
- [ ] Bidding and budget set per [Bidding](bidding-and-budgets.md); schedule and end date set for tests.
- [ ] Conversion tracking: relevant conversion rules attached.
- [ ] Lead form attached and CRM sync tested (lead gen).
- [ ] UTM parameters on destination URLs for analytics.

## 8. Common structural mistakes
| Mistake | Effect | Fix |
|---------|--------|-----|
| Many tiny campaigns splitting a small budget | No learning, high CPMs | Consolidate to 2 to 5 campaigns at Starter and Growth |
| Mixing cold and retargeting audiences in one campaign | Unreadable results; budget goes to retargeting | Separate campaigns |
| Same audience in several campaigns at once | Self competition, frequency spikes | Exclusions between campaigns or one campaign per audience |
| Objective mismatch (Brand awareness judged on leads) | False negatives | Judge each objective on its KPI |
| Agency owned ad account | Data loss on agency change | Business Manager ownership by the company |
