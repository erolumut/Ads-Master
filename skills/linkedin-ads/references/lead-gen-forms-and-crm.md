# Lead Gen Forms and CRM Sync

> Scope: designing LinkedIn lead gen forms for quality and volume, hidden fields and tracking, CRM sync with HubSpot, Salesforce and others, speed to lead, the lead quality feedback loop, and offline conversion return. Implementation of integrations is owned by the measurement agent with the CRM admin.

## 1. Lead gen form anatomy

| Element | Practice | Label |
|---------|----------|-------|
| Form type | Choose between a volume oriented form and a higher intent form that adds a review step before submit where available | [Unverified] for current option names |
| Offer headline and details | Restate the offer and what happens next | [Practitioner consensus] |
| Profile fields (pre-filled) | First name, last name, email, company, job title, seniority, company size, country; use only what sales needs | [Official, 2020] for pre-fill concept |
| Custom questions | Short answer or multiple choice; a small number allowed (historically up to 3) | [Unverified] |
| Hidden fields | Campaign, ad, offer and audience codes for CRM attribution | [Official] concept, verify limits |
| Privacy policy | Required link; optional custom consent checkboxes | [Official] |
| Thank you screen | Message plus link (calendar, content download, next step) | [Official] |
| Lead retention | Leads downloadable from Campaign Manager for a limited period (historically 90 days); sync instead of relying on downloads | [Unverified] |

## 2. Designing for quality vs volume

| Lever | Volume effect | Quality effect | Use when |
|-------|---------------|----------------|----------|
| Fewer pre-filled fields | Up | Slightly down | Top of funnel content |
| One qualifying multiple choice question (timeline, team size, current tool) | Down slightly | Up | Default for demo and high value offers |
| Business email required or work email field | Down | Up | When personal emails flood the CRM |
| Higher intent form option | Down | Up | Lead quality complaints from sales |
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
| Native integration (HubSpot, Salesforce, Microsoft Dynamics, Marketo, Oracle Eloqua and others) | Near real time | Preferred; map fields once; test with a test lead [Official] for integration list, verify current list |
| Integration platforms (Zapier, Make, Tray and similar) | Minutes | Flexible routing and enrichment |
| CSV download | Manual | Last resort; slow follow up kills conversion; leads expire from download after the retention window |
| Marketing API lead sync | Near real time | For custom stacks; see [Tools](tools-api-mcp.md) |

Sync test procedure:
1. Submit a test lead from the form preview or a live test with a colleague.
2. Confirm the lead appears in the CRM within 5 minutes with all fields and hidden fields mapped.
3. Confirm lead source, campaign and owner assignment rules fire.
4. Confirm the SDR alert or sequence triggers.
5. Record the test in MEASUREMENT.md via the measurement agent.

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
| High quality but expensive | Keep; scale through retargeting and lookalike style predictive audiences |
5. Send stage outcomes back to LinkedIn as conversions (CAPI or CRM conversion sync) so optimization and reporting see qualified events. See [Measurement](measurement-capi-and-attribution.md).
6. Write the lead quality review to `ads-master/outputs/linkedin-ads/YYYY-MM-DD_linkedin-ads_lead-quality-review.md`.

## 7. Value model for leads
| Stage | Value |
|-------|-------|
| Lead | lead to won rate x average first year gross profit |
| SQL | SQL to won rate x average first year gross profit |
| Opportunity | win rate x opportunity value x margin |
| Closed won | actual gross profit |
Worked example: first year gross profit $24,000, SQL to won 20%, lead to SQL 15%. SQL value $4,800; lead value $720. If the business accepts a cost per SQL up to 40% of SQL value, max cost per SQL is $1,920 and max CPL is $288. Illustrative only.

## 8. Lead gen form vs landing page: decision tree
```
Is the offer content or an event?
  yes -> lead gen form (document or event ad), qualify lightly, nurture
Is the offer a demo or trial and does the site convert at 5%+ from LinkedIn traffic?
  yes -> test Website conversions vs lead gen form side by side
  no  -> lead gen form with a qualifying question and higher intent option
Is sales capacity the bottleneck?
  yes -> fewer, better leads: higher intent form, stricter audience, demo only
```

## 9. Compliance
- Privacy policy link is mandatory; custom consent checkboxes for marketing permissions where required by law (GDPR and others).
- Store consent text and timestamp in the CRM.
- Do not upload lead gen leads to other platforms as audiences without a lawful basis.
- Respect LinkedIn data use terms for lead data [Unverified] for current specifics.
