# Account Structure and Objectives

> Scope: Business Manager and ad account setup, campaign hierarchy, objectives and optimization goals, Accelerate, Media Planner, naming conventions and reference structures by tier. Labels: [Official, YYYY-MM] marks mechanics confirmed in LinkedIn documentation or dated announcements (verified 2026-10-08); [Unverified] marks items to check in Campaign Manager before relying on them.
>
> Naming: since 2025-10 the Campaign Manager UI calls the old campaign group a **Campaign** and the old campaign an **Ad set** [Official, 2025-10]. The API keeps `campaignGroup` and `campaign`. Below, "campaign group" means UI Campaign and "campaign" means UI Ad set.

## 1. Setup checklist (new or inherited account)

| # | Item | Why | How |
|---|------|-----|-----|
| 1 | Business Manager with the company as owner | Central control of ad accounts, pages and people; avoids accounts owned by former staff or agencies | Create Business Manager, add ad accounts and pages, assign roles [Official, 2023] |
| 2 | Ad account owned by the company, billing in the company name | Ownership and invoices | Account settings, billing center |
| 3 | User roles by least privilege | Security | Account manager, campaign manager, creative manager, viewer, billing admin |
| 4 | Company page linked and admins assigned | Ads run from the page; Thought Leader Ads need page and member permissions | Page admin settings |
| 5 | Insight Tag installed site wide | Conversions, retargeting, Demographics of site visitors | GTM or site header; see [Measurement](measurement-capi-and-attribution.md) |
| 6 | Conversion rules created and recording | Optimization and reporting | Campaign Manager > Measurement (older accounts: Analyze) > Conversion tracking; setup guides from 2025 show both paths [Unverified] for the current label |
| 7 | CRM connection for lead sync and for Business Manager CRM data | Speed to lead, stage feedback, revenue attribution report, qualified leads optimization | Lead sync integrations (HubSpot, Salesforce, Dynamics and others); Business Manager CRM connection supports Salesforce, Dynamics 365 and HubSpot [Official, 2026-10] |
| 8 | Matched audiences: website retargeting segments, company list, contact list, engagement audiences | Retargeting and ABM foundations | Plan, then upload with approval |
| 9 | Exclusion lists: customers, employees, competitors, partners | Avoid waste | Company and contact lists |
| 10 | Naming convention agreed | Reporting via API and exports | See section 6 |

## 2. Hierarchy

| Level | Holds | Practice |
|-------|-------|----------|
| Ad account | Billing, Insight Tag, conversions, matched audiences, lead forms | One per business unit or region with separate budgets or legal entities |
| Campaign (API: campaignGroup; old UI: campaign group) | Ad sets, optional group budget and schedule, Dynamic Group Budget, status | Group by program or funnel stage (for example "TOFU thought leadership", "ABM tier 1", "Retargeting", "Lead capture") |
| Ad set (API: campaign; old UI: campaign) | Objective, audience, format, bidding, budget, schedule, conversion tracking, frequency cap (Brand awareness) | One objective, one audience, one format family per ad set |
| Ad | Creative, copy, destination, lead form | 2 to 4 active ads per ad set; Flexible Ad Creation builds up to 64 combinations from supplied assets [Official, 2026-07] |

Format note: a campaign is tied to a format family (for example single image, video, document, carousel, conversation, message, event, text, dynamic). Mixed format testing needs separate campaigns or the format choices the objective allows [Official, 2024].

## 3. Objectives and optimization goals

| Funnel stage | Objective | Typical optimization goals | Use when | KPI |
|--------------|-----------|---------------------------|----------|-----|
| Awareness | Brand awareness | Impressions, reach | Demand creation in the ICP, new category, ABM air cover | Reach in ICP, frequency, lift |
| Consideration | Website visits | Landing page clicks, clicks, impressions | Driving content consumption, retargeting pools | Cost per landing page view, engaged sessions |
| Consideration | Engagement | Engagement clicks, impressions; also used for follower and event growth | Thought Leader Ads, social proof, event promotion | Cost per engagement, retargetable engagers |
| Consideration | Video views | Video views, impressions | Video storytelling, building video retargeting pools | Cost per view, completion rate |
| Conversion | Lead generation | Leads, or Qualified leads (API: MAX_QUALIFIED_LEAD, needs CAPI qualified lead events or Business Manager CRM data) | Capturing demand with low friction; Event ads can use this objective since API 202605 | Cost per qualified lead |
| Conversion | Website conversions | Conversions, landing page clicks, clicks | Demo or trial on site, gated content on site, events | Cost per conversion, qualified rate |
| Conversion | Job applicants (Talent leads [Unverified] for 2026) | Applications | Recruiting | Cost per qualified applicant |

Objective facts confirmed 2026-10-08:
- The objective cannot be changed after launch; with Dynamic Group Budget neither the group objective nor the budget mode can be changed after launch [Official, 2026-10].
- Qualified leads optimization launched 2025-04-22 for Lead generation; LinkedIn reported "upwards of 39%" lower cost per qualified lead in early results (platform claim, no method published) and recommends sending at least 5 qualified leads every two weeks [Official, 2025-04].
- API 202602 added MAX_QUALIFIED_LEAD as an optimization target for LEAD_GENERATION; API 202608 added MARKETING_QUALIFIED_LEAD and SALES_QUALIFIED_LEAD conversion types that feed the same goal [Official, 2026-08].
- Event ads: off-platform events (webinars hosted elsewhere) and lead gen forms on event ads announced 2026-04-28; Lead generation became a supported objective for event ad campaigns in API 202605; event ads do not deliver on LinkedIn Audience Network [Official, 2026-05].
- Event registration conversions moved to a 30-day click and 30-day view window in 2025-04 [Official, 2025-04].
Recheck the objective menu in Campaign Manager when planning; LinkedIn adds goals through the API changelog first.

Choosing between Lead generation and Website conversions:
| Factor | Lead gen forms (Lead generation) | Website conversions |
|--------|----------------------------------|--------------------|
| Volume | Higher (pre-filled forms) | Lower |
| Quality | Often lower without qualifying questions | Often higher (more effort) |
| Speed | Needs CRM sync for speed to lead | Site forms flow into CRM already |
| Data | Profile fields from LinkedIn | Site analytics and CRM |
| Use | Gated content, events, demo requests with qualifying question | Free trial, product led signup, demo with scheduling |
Run both as a test when budget allows (see [B2B strategy playbooks](b2b-strategy-playbooks.md)).

## 4. Accelerate ad sets (AI campaigns) and planning tools

What it is: LinkedIn's AI driven ad set type, chosen after the objective (Accelerate vs Classic). From a landing page URL it drafts the audience (using predictive signals), creative and bidding [Official, 2023-10 announcement]. Status as verified 2026-10-08:

| Fact | Detail | Label |
|------|--------|-------|
| Objective coverage | Launched for Lead generation and Website visits; global release 2024-10 extended it to all objectives (Brand awareness, Engagement, Website conversions, Video views) and to video and document ads | [Official, 2024-10] |
| Limits in LinkedIn's getting started guide | 14 day minimum run; lifetime budget floors of $700 (Website visits) and $3,000 (Lead generation); single image ads with English copy; third-party tracking unavailable | [Contested]: the PDF is undated and predates the 2024-10 expansion; check the setup screen |
| Data inputs | CAPI conversions can be used as data sources for Accelerate targeting; attribution works as in Classic | [Official, 2024] |
| Platform claim | Up to 42% lower cost per action vs Classic (LinkedIn, no method published); Siemens case study: 2.4x website visits, lead form completion 5.66% vs 2.56% at similar CPL | [Official, 2024] platform claim |
| Practitioner view | Broadens narrow ICPs toward cheaper members; one 2026 review reports lower CPL but higher cost per SQL; advised against for accounts with a target account list | [Practitioner consensus, 2026] |

When to test:
- Insight Tag conversions or lead form leads are recording reliably (aim for 30 or more conversions per month at account level), ideally with qualified lead events flowing through CAPI.
- A Classic ad set with the same objective and offer exists as the control.
- The offer is broad enough for the ICP (a demo or trial, not a niche event). Not for ABM lists where account precision is the point.

How to test:
1. Create the Accelerate ad set with the same offer and budget as the control.
2. Check which exclusions the setup accepts (customers, employees, competitors) and record what could not be excluded [Unverified] for current exclusion support.
3. Run 4 to 6 weeks or until each side has 30+ results.
4. Compare on CRM qualified leads and pipeline, then CPL. Check the Demographics report: who did it reach?
5. Keep the winner; log in EXPERIMENTS.md.

Risk: automated audiences drift away from the ICP toward cheaper members. The Demographics report and lead quality data are the guardrail.

Planning tools:
- Media Planner (announced 2025-03-25): estimates reach, impressions, leads and cost per key result for Brand awareness, Video views and Lead generation before launch, by audience, placement and budget scenario [Official, 2025-03]. Use it for forecasts in launch plans, label outputs as platform estimates, and replace them with account data after 30 days.
- Ad duplication across ad sets and accounts (2025) [Official, 2025-03].
- Flexible Ad Creation (self serve from 2026-07-01): up to 4 images or videos and up to 5 headlines and descriptions, mixed into up to 64 versions in single image and video Classic ad sets; needs a new campaign with dynamic budget optimization, has a learning phase of about one week and may auto pause weak combinations [Official, 2026-07]. Treat it as a creative test engine, not a replacement for one variable tests.

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
- Accelerate tests alongside Classic ad sets.
- Video programs for reach: BrandLink pre-roll (self serve for select accounts since 2026-03), CTV Ads (Campaign Manager, The Trade Desk, Amazon DSP in the US), Reserved Ads or First Impression Ads for launches [Official, 2026-05].
- Frequency caps on Brand awareness ad sets (3 to 30 impressions per member per 7 days) [Official, 2025-07].
- Brand and conversion lift studies each half year.
- Business Manager governance: who can launch, who approves.

## 6. Naming convention
```
Campaign group: <Region>_<Program>_<Stage>        e.g. NA_ABM-T1_TOFU
Campaign:      <Region>_<Objective>_<Audience>_<Format>_<Offer>_<YYYYMM>
               e.g. NA_LeadGen_ITDM-Sr_DocAd_Checklist_202610
Ad:            <Angle>_<Hook>_<Version>          e.g. CostOfDowntime_Stat_v2
```
Rules: no spaces in parsed fields, fixed vocabulary for Objective (Awareness, Visits, Engage, Video, LeadGen, WebConv), Audience codes documented in the journal. Dynamic UTMs fill account, campaign and creative names automatically (since 2024-03); after the 2025-10 rename the tokens were renamed (CAMPAIGN_GROUP_ID became CAMPAIGN_ID), so map old and new token names in GA4 and CRM fields [Official, 2025-10]. Dynamic UTMs apply to the main destination URL only and do not work on Thought Leader Ads or boosted posts [Practitioner consensus].

## 7. Campaign settings checklist (every new campaign)
- [ ] Objective matches the KPI.
- [ ] Locations: permanent or recent location choice made deliberately [Unverified] for current option names.
- [ ] Audience built and saved; size checked in the forecast panel.
- [ ] Audience expansion off (unless tested).
- [ ] LinkedIn Audience Network off for B2B lead gen and ABM (unless tested); it is on by default for new single image, carousel, document and video ad sets [Official, 2026-10].
- [ ] Exclusions applied (customers, employees, competitors, job seekers where relevant).
- [ ] Format chosen; 2 to 4 ads ready.
- [ ] Bidding and budget set per [Bidding](bidding-and-budgets.md); schedule and end date set for tests; frequency cap set deliberately on Brand awareness ad sets.
- [ ] Qualified leads goal considered for Lead generation when CAPI qualified events reach LinkedIn's guidance (5+ per two weeks).
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
