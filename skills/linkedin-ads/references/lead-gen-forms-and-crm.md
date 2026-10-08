# Lead Gen Forms and CRM Sync

> Scope: designing LinkedIn lead gen forms for quality and volume, hidden fields and tracking, CRM sync with HubSpot, Salesforce and others, speed to lead, the lead quality feedback loop, and offline conversion return. Implementation of integrations is owned by the measurement agent with the CRM admin.

## 1. Lead gen form anatomy

| Element | Practice | Label |
|---------|----------|-------|
| Form quality option | Work email validation blocks the most common free email domains; LinkedIn notes it may improve lead quality and lower submission rates. A separate "higher intent" form type was not found in 2026 documentation | [Official, 2026-10]; higher intent option [Unverified] |
| Offer headline and details | Restate the offer and what happens next | [Practitioner consensus] |
| Informational fields (pre-filled) | Up to 12 fields per form; first name, last name and email are pre-selected and count toward the 12 (they can be cleared); use only what sales needs | [Official, 2026-10] |
| Custom questions | Up to 3 custom questions (short answer or multiple choice), counted inside the 12 field total; one community report of a 10 option cap per multiple choice question | [Official, 2026-10]; option cap [Unverified] |
| Hidden fields | Not visible to members, carry no member data; static values or dynamic parameters for campaign, ad, offer and audience codes | [Official, 2026-10] |
| Work email field | Add a separate Work email field when routing or enrichment needs a business address; the standard Email field can return a personal address | [Practitioner consensus, 2026] |
| Privacy policy | Required link; optional custom consent checkboxes | [Official] |
| Thank you screen | Message plus link, or a booking option (native scheduler, Calendly reported since 2025-09; Chili Piper routing with a Booking URL field); booked appointments reported in Campaign Manager from 2026-08-27 with no backfill | [Official, 2026-08] (Chili Piper Help and 2026-09 recap); LinkedIn's 7x post-submission CTR claim [Unverified] |
| Lead download | Campaign Manager > Assets > Lead generation forms > select forms and dates > Download leads (one CSV per form) | [Official, 2026-10] |
| Lead retention | Leads reported to stay downloadable for 90 days; sync instead of relying on downloads | [Unverified] (single third-party source) |
| Event ads | Lead gen forms on event ads (off-platform events too) since 2026-04; the ad's lead gen form is separate from any organic event registration form | [Official, 2026-05] |

## 2. Designing for quality vs volume

| Lever | Volume effect | Quality effect | Use when |
|-------|---------------|----------------|----------|
| Fewer pre-filled fields | Up | Slightly down | Top of funnel content |
| One qualifying multiple choice question (timeline, team size, current tool) | Down slightly | Up | Default for demo and high value offers |
| Work email validation or a Work email field | Down | Up | When personal emails flood the CRM |
| Book an appointment on the thank you screen | Neutral | Up (meetings booked while intent is high) | Demo and consultation offers |
| Offer specificity (assessment vs ebook) | Down | Up | Sales capacity limited |
| Gated document with preview pages | Middle | Middle | Content with proven demand |

Qualifying question examples:
- "When are you planning to change <solution>?" (This quarter, Next 6 months, Later, Just researching)
- "How many <users or seats> would use it?" (1 to 10, 11 to 50, 51 to 200, 200+)
- "What best describes your role in this decision?" (Decision maker, Evaluator, User, Researching)
Route answers in the CRM: hot answers to SDR same day, others to nurture.

## 3. Hidden fields and attribution
| Hidden field | Value pattern | Purpose |
|--------------|---------------|---------|
| utm_source | linkedin | Source in CRM |
| utm_medium | paid_social | Channel grouping |
| utm_campaign | Campaign name from naming convention | Campaign level reporting |
| ad_id or creative code | Ad code | Creative level quality |
| audience_code | ICP segment code | Audience level quality |
| offer | Offer code | Offer level quality |
Map each hidden field to a CRM property. Without hidden fields, lead quality analysis by campaign is guesswork.

## 4. CRM sync options

| Option | Speed | Notes |
|--------|-------|-------|
| Native integration (HubSpot, Salesforce, Microsoft Dynamics, Marketo, Oracle Eloqua and others) | Near real time | Preferred; map fields once; test with a test lead [Official] concept; check the current partner list in Campaign Manager |
| Integration platforms (Zapier, Make, Tray and similar) | Minutes | Flexible routing and enrichment |
| CSV download | Manual | Last resort; slow follow up kills conversion; leads expire from download after the retention window |
| Marketing API lead sync | Near real time | For custom stacks; see [Tools](tools-api-mcp.md) |

Sync test procedure:
1. Submit a test lead from the form preview or a live test with a colleague.
2. Confirm the lead appears in the CRM within 5 minutes with all fields and hidden fields mapped.
3. Confirm lead source, campaign and owner assignment rules fire.
4. Confirm the SDR alert or sequence triggers.
5. Record the test in MEASUREMENT.md via the measurement agent.

### CRM field mapping template
| LinkedIn field or hidden field | HubSpot property (example) | Salesforce field (example) | Notes |
|-------------------------------|---------------------------|---------------------------|-------|
| First name, last name, email | firstname, lastname, email | FirstName, LastName, Email | Dedupe on email |
| Company name | company | Company | Match to account in CRM |
| Job title, seniority | jobtitle, custom seniority | Title, custom field | Used for scoring |
| Company size | custom or numberofemployees | NumberOfEmployees or custom | Picklist alignment |
| Country | country | Country | Routing |
| Qualifying answer | custom property | custom field | Drives routing |
| utm_campaign or campaign code | custom property | Campaign membership | Salesforce: add to the matching Campaign with a member status |
| ad code, audience code, offer | custom properties | custom fields | Quality analysis |
| Lead form ID and submission time | custom properties | custom fields | Troubleshooting and CAPI matching |
| Consent checkbox values | marketing consent properties | consent fields | Store text and timestamp |

CRM notes:
- HubSpot: the native LinkedIn Ads integration in HubSpot syncs lead gen form submissions and can sync audiences; confirm form mapping per form [Practitioner consensus] [Unverified] for current features.
- Salesforce: use Campaign membership with statuses (Responded, MQL, SQL) so campaign influence reports work; map hidden fields to lead fields that convert to contact and opportunity.
- Microsoft Dynamics, Marketo, Eloqua: available as native lead sync integrations historically [Unverified] for the current list.
- Business Manager CRM connection (separate from lead sync): Salesforce, Dynamics 365 or HubSpot connected by a Business Manager admin powers the revenue attribution report and CRM based qualified leads optimization [Official, 2026-10].

## 5. Speed to lead and follow up
- Follow up within 1 business hour for demo or high intent offers; within 24 hours for content leads [Practitioner consensus].
- Content leads go to a nurture sequence first; only engaged or qualifying leads go to SDRs.
- Use the thank you screen to offer a calendar link for high intent offers.
- Agree service levels with sales and measure them monthly; lead quality complaints often trace to slow follow up.

## 6. Lead quality feedback loop (monthly)
1. Export CRM leads from LinkedIn for the last 30 to 90 days with: campaign, ad code, audience code, offer, form answers, lifecycle stage, disqualification reason, opportunity value.
2. Compute per campaign and per offer: lead to MQL, lead to SQL, lead to opportunity, cost per SQL, pipeline per dollar.
3. Read disqualification reasons: students, job seekers, wrong company size, competitors, duplicate, no budget.
4. Act:
| Pattern | Action |
|---------|--------|
| Many students or job seekers | Exclude seniorities and titles; turn off Audience expansion and Audience Network |
| Wrong company size | Tighten company size; add qualifying question |
| Competitors and vendors | Company exclusion list |
| Good fit but slow follow up | Fix routing and SLAs before changing ads |
| High quality but expensive | Keep; scale through retargeting, predictive audiences seeded from SQLs, and the Qualified leads goal |
5. Send stage outcomes back to LinkedIn as conversions (CAPI or Business Manager CRM data) so optimization and reporting see qualified events: conversion types QUALIFIED_LEAD, MARKETING_QUALIFIED_LEAD and SALES_QUALIFIED_LEAD (the last two since API 202608) feed the Qualified leads goal on Lead generation ad sets [Official, 2026-08]. LinkedIn recommends at least 5 qualified leads every two weeks to keep the model trained [Official, 2025-04]. See [Measurement](measurement-capi-and-attribution.md).
6. Write the lead quality review to `ads-master/outputs/linkedin-ads/YYYY-MM-DD_linkedin-ads_lead-quality-review.md`.

## 7. Value model for leads
| Stage | Value |
|-------|-------|
| Lead | lead to won rate x average first year gross profit |
| SQL | SQL to won rate x average first year gross profit |
| Opportunity | win rate x opportunity value x margin |
| Closed won | actual gross profit |
Worked example: first year gross profit $24,000, SQL to won 20%, lead to SQL 15%. SQL value $4,800; lead value $720. If the business accepts a cost per SQL up to 40% of SQL value, max cost per SQL is $1,920 and max CPL is $288. Illustrative only.

## 7a. Lead gen form benchmarks (context, not targets)
| Metric | Value | Source and caveat |
|--------|-------|-------------------|
| Feed form open rate (median) | 0.33% (376 accounts); by format single image 0.39%, document 0.14%, video 0.45%, Thought Leader 0.39% | Kiin, 489 advertisers, $13.6M lead gen spend, 86,051 leads, 12 months to 2026-09 [Study, 2026] |
| Completion and CPL, content offers | Thought Leader 11.4% at $94; video 4.6% at $119 | Same; cells of 8 to 16 accounts |
| CPL, demo offers | Thought Leader $1,025; video $283 | Same; small cells, directional |
| Video vs single image | Video with a form costs about 60% more per lead | Same |
| HR audiences | Document ads 26.7% completion at $123 per lead vs 5.1% and $205 for single image, video and carousel combined | Kiin, 113 accounts, $1.65M [Study, 2026] |
| Sponsored Messaging layered on Sponsored Content lead gen | About 30% better CPL and 3.6x form completion vs Sponsored Content alone | LinkedIn platform claim reported 2026-09 [Unverified] |
| Lead gen forms vs landing pages | SQL rates often 20% to 40% lower from forms | Vendor report [Unverified] |
Use these only to sanity check; set targets from the value model in section 7.

## 8. Lead gen form vs landing page: decision tree
```
Is the offer content or an event?
  yes -> lead gen form (document or event ad), qualify lightly, nurture
Is the offer a demo or trial and does the site convert at 5%+ from LinkedIn traffic?
  yes -> test Website conversions vs lead gen form side by side
  no  -> lead gen form with a qualifying question, work email validation and a booking option
Is sales capacity the bottleneck?
  yes -> fewer, better leads: work email validation, stricter audience, Qualified leads goal, demo only
```

## 9. Compliance
- Privacy policy link is mandatory; custom consent checkboxes for marketing permissions where required by law (GDPR and others).
- Store consent text and timestamp in the CRM.
- Do not upload lead gen leads to other platforms as audiences without a lawful basis.
- Respect LinkedIn data use terms for lead data [Unverified] for current specifics.
- Hidden fields carry no member data; never place personal data in them [Official, 2026-10].
