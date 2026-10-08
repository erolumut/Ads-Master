# Measurement: Insight Tag, Conversions API and Attribution

> Scope: Insight Tag, conversion rules and windows, enhanced conversion tracking, Conversions API, offline and CRM conversions, the revenue attribution report, company engagement and Demographics reporting, lift and A/B tests, and reconciling LinkedIn numbers with the CRM. Implementation is owned by the measurement agent. Code and field names are patterns to verify against LinkedIn documentation.

## 1. Measurement architecture
```
Browser: Insight Tag (partner ID) -> page and event conversions, website retargeting, visitor demographics
Server:  Conversions API -> online and offline events with hashed identifiers, deduplicated with the tag by event ID
CRM:     Lead gen form sync -> lifecycle stages -> CAPI or CRM conversion sync -> LinkedIn optimization and reporting
Reports: Campaign Manager (conversions, Demographics, Companies tab), revenue attribution report (Business Manager, CRM connected), lift tests
Truth:   CRM opportunities and revenue (MEASUREMENT.md)
```

## 2. Insight Tag
1. Create or locate the Insight Tag (partner ID) in Campaign Manager.
2. Install site wide via GTM (LinkedIn Insight Tag template) or the site header. One tag per ad account; share via Business Manager or account settings if several accounts need it [Unverified] for current sharing mechanics.
3. Consent: in regions requiring consent, load the tag only after marketing consent through the CMP. The Insight Tag does not read Google Consent Mode signals and has no cookieless modeled mode; gate it in GTM with Additional Consent Checks (ad_storage, ad_user_data) or a CMP consent trigger [Practitioner consensus, 2026]. One CMP vendor claims a limited data use fallback; test before relying on it [Unverified]. Expect lower observed conversions where consent rates are low, and use CAPI with consented identifiers where lawful; a client side opt out does not stop server side events unless you build that in.
4. Verify: Campaign Manager shows the tag as active; browser network requests to LinkedIn's tag endpoint fire on page load and on events.

Event conversion pattern (verify syntax in docs):
```javascript
// After a successful form submit (event specific conversion rule)
window.lintrk && window.lintrk('track', { conversion_id: 1234567 });
```
Enhanced conversion tracking: when enabled, LinkedIn appends its first-party click ID (li_fat_id) to landing page URLs so the tag can use first-party cookies, and the click ID can be stored and sent through CAPI [Official, 2026-10]. Without the tag on site, click-through conversions can still flow through CAPI with the click ID; view-through conversions need extra identifiers such as hashed email [Practitioner consensus, 2026]. Enable only with legal approval.

## 3. Conversion rules
| Setting | Options (as known) | Recommendation | Label |
|---------|-------------------|----------------|-------|
| Type | Lead, purchase, sign up, download, key page view, add to cart, submit application, install, other; Qualified lead, plus Marketing qualified lead and Sales qualified lead (API 202608) | Use the true category; send qualified stages as their own rules so they can drive the Qualified leads goal | [Official, 2026-08] |
| Method | Page load (URL rule), event specific (JS), CAPI, offline or CRM | Event specific or CAPI over URL rules for forms | [Official, 2023] |
| Value | Static or dynamic value | Stage value for lead gen | [Official] |
| Post-click window | 1, 7, 30, 90 days (default 30); 365 days for Submit application, Purchase, Add to cart, Qualified lead and Lead (plus MQL and SQL from API 202608) when the rule uses CAPI or CSV upload; API also offers 180 days for those types | LinkedIn's CAPI playbook: 90 click and 90 view for lead and lower funnel events, 30 click and 7 view for website conversions; use 365 only for long cycles | [Official, 2026-09] |
| Post-view window | 1, 7, 30, 90 days (default 7) | Report view-through separately; shorten when comparing channels | [Official, 2026-09] |
| Attribution | Each campaign (credit every ad set with an interaction in the window) or Last campaign (credit only the last) | Each campaign for ad set level optimization; Last campaign to avoid double counting in totals | [Official, 2026-10] |
| Counting | One per click or every conversion | One for leads, every for purchases | [Unverified] for current labels |
| Campaigns | Attach to all relevant campaigns | Check new campaigns get the rule | [Official] |

Reporting caution: LinkedIn view-through conversions inflate results relative to click based channels. Report click and view conversions separately and reconcile with the CRM.

## 4. Conversions API (CAPI)
Status: LinkedIn launched its Conversions API in 2023 with partner integrations; it accepts online and offline events with hashed identifiers [Official, 2023]. LinkedIn maintains an official Google Tag Manager server-side tag template (github.com/linkedin-developers/linkedin-capi-tag-template, created 2023-08) and published an Adobe Experience Platform event forwarding extension repository in 2026-06 [Official, 2026-06]. CAPI now also drives bidding: qualified lead events (QUALIFIED_LEAD, and since 202608 MARKETING_QUALIFIED_LEAD and SALES_QUALIFIED_LEAD) feed the Qualified leads optimization goal [Official, 2026-08].

Key mechanics (as known; verify):
| Item | Detail | Label |
|------|--------|-------|
| Conversion rule | Create a rule with CAPI as a data source; events reference the rule | [Official, 2023] |
| Identifiers | Each event needs at least one of: SHA256_EMAIL (lowercase, trim, unsalted SHA-256 hex), LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID (li_fat_id), ACXIOM_ID, ORACLE_MOAT_ID, or first plus last name; the 2026-04 FAQ also lists PLAINTEXT_IP_ADDRESS, SHA256_IP_ADDRESS and GOOGLE_AID and omits ORACLE_MOAT_ID [Contested] for MOAT. userInfo (first name, last name, company, title, country) improves matching; hashedFirstName and hashedLastName accepted from 202609 (64 character SHA-256 hex after normalizing). Send email hash plus click ID together; only matched events count for attribution and optimization | [Official, 2026-09] |
| Deduplication | Same event ID from Insight Tag and CAPI for the same conversion | [Official, 2023] |
| Event age and attribution | Attribution reaches up to 180 days for most types (90 day conversion timestamp plus 90 day lookback); 180 or 365 day windows for the lead, purchase and application types above; some connectors reject events older than 90 days; the li_fat_id to member mapping is kept 365 days; stored conversion data is erased after 180 days except aggregates (older Help Center wording) | [Official, 2026-09] |
| Auth | OAuth access token with the conversions scope via the Marketing API | [Official] |
| Integrations | GTM server template, Adobe event forwarding, Salesforce Data Cloud connector, Zapier, LiveRamp, Dreamdata, and CDP or server tag vendors (Commanders Act, MetaRouter, Datahash, LeadsBridge); partner integrations pass identifiers through the partner's setup | [Official, 2026-10] for the concept; list from partner docs |

CAPI rollout procedure:
1. Choose the path: native CRM connector (fastest for lifecycle stages), GTM server-side template (web events), CDP (if the stack has one).
2. Define events: lead (online), MQL, SQL, opportunity, closed won (offline from CRM), purchase (ecommerce).
3. Create conversion rules for each, with values from the stage value model.
4. Enable the first-party click ID capture if available; store it with the lead in the CRM.
5. Send events with event IDs; dedupe with the tag for online events.
6. Validate match rates and counts in Campaign Manager over 7 days.
7. Switch Lead generation ad sets to the Qualified leads goal once qualified events arrive steadily (LinkedIn guidance: at least 5 every two weeks; practitioner rule of thumb for stable optimization: 30+ per month per ad set) [Official, 2025-04] [Practitioner consensus]. LinkedIn reported early results of up to 39% lower cost per qualified lead (platform claim); verify with a holdout or A/B test.

## 5. Offline and CRM conversions
- Offline conversions can be uploaded (CSV or integration) and attributed to ad engagement by matching identifiers; CSV uploads also unlock the 365 day window for eligible types [Official, 2026-10].
- Business Manager CRM connections (Salesforce, Dynamics 365, HubSpot) share CRM data for the revenue attribution report and CRM based qualified leads optimization [Official, 2026-10].
- Keep a dedicated CRM property for LinkedIn click IDs and lead gen form IDs to aid matching and troubleshooting.

## 6. Revenue attribution report (RAR)
- What: a Business Manager report that joins LinkedIn ad engagement with CRM opportunities: revenue won, return on ad spend, pipeline amount, leads, opportunities, win rate and average days to close [Official, 2026-10].
- Access and CRMs: Salesforce, Dynamics 365 or HubSpot connected in Business Manager by a Business Manager admin [Official, 2026-10].
- Model: contact based, any touch. A deal is credited when a CRM contact tied to the opportunity engaged (viewed, clicked, liked, shared) with LinkedIn ads inside the lookback window before close. Influence, not causation [Official, 2025-07].
- Lookback: LinkedIn's getting started guide (2025-07) gives 180 days by default with 30, 60, 90 or 180 options; one agency reports a 90 day default and up to 1 year; another reports 365 days in 2026 [Contested]. Read the setting in the report before quoting numbers, and note deals that close after the window are invisible.
- Use: directional proof of influence and to compare campaigns on influenced pipeline; never as the only success metric. Pair with holdouts or lift tests for causality.

## 7. Company engagement and Demographics reports
- Demographics report: who saw and clicked your ads by job title, function, seniority, company, industry, company size and location (thresholds hide small counts) [Official, 2019]. Use it two weeks after every launch to confirm ICP match.
- Companies tab (replaced the company engagement report): paid plus organic engagement and website visits by company, engagement levels, list building (see [Targeting and ABM](targeting-and-abm.md)).
- API 202609 added a DMA pivot (MEMBER_DESIGNATED_MARKET_AREA) to adAnalytics for US market reporting; DMA output must carry the Nielsen registration notice [Official, 2026-09].

ICP match score (compute monthly):
```
ICP match = impressions on target seniorities and functions in target company sizes / total impressions (from the Demographics report)
```
Target 70%+ for lead gen and ABM campaigns [Practitioner consensus]; investigate expansion, Audience Network and broad attributes when lower.

## 8. Lift and A/B testing
| Test | What it measures | When |
|------|------------------|------|
| Campaign Manager A/B test | Difference between creative, audience or placement variants | Ongoing creative and audience decisions |
| Brand lift test | Change in awareness, consideration or ad recall from polling exposed vs control | Awareness and video programs with enough budget (minimums apply) [Unverified] for current minimums |
| Third-party verification | DoubleVerify post-bid on Audience Network (2026-05) and measurement of LinkedIn CTV Ads; iSpot for CTV | Before scaling off-feed placements [Official, 2026-05] |
| Conversion lift test | Incremental conversions from exposed vs holdout | Validating LinkedIn's incremental contribution [Unverified] for availability |
| Geo or account holdout (DIY) | Pipeline difference between targeted and held out accounts or regions | ABM programs; when platform lift tools are unavailable |

Account holdout design for ABM:
1. Randomly split the target account list into test (80%) and holdout (20%), stratified by tier and industry.
2. Run ads only to test accounts for 90 to 180 days.
3. Compare opportunity creation rate and pipeline per account between groups in the CRM.
4. Report the difference with confidence intervals; log in EXPERIMENTS.md.

## 9. Reconciliation
| Comparison | Expected gap | Why |
|-----------|--------------|-----|
| LinkedIn leads (lead gen forms) vs CRM leads | Under 5% | Sync failures, duplicates |
| LinkedIn website conversions vs CRM form submissions from LinkedIn UTMs | Larger; LinkedIn includes view-through and cross device | Attribution differences |
| RAR influenced revenue vs CRM sourced revenue | RAR much higher | Influence vs source |
Write the reconciliation into MEASUREMENT.md via the measurement agent so every agent uses the same truth.

## 10. Consent and privacy
- Insight Tag sets cookies and processes personal data; in the EEA, UK and other consent regimes, fire it only after marketing consent through the CMP.
- CAPI events with hashed identifiers still require a lawful basis; document the basis in MEASUREMENT.md.
- Contact list uploads and CRM sync need a lawful basis and must respect opt-outs; remove opted out contacts from matched audiences monthly.
- Lead gen form consent checkboxes must match the privacy policy and be stored with timestamps in the CRM.
- Expect lower observed conversion counts where consent rates are low; do not compare raw LinkedIn conversion counts across regions with different consent rates.

## 11. Measurement health checklist
- [ ] Insight Tag active, firing on all pages, consent compliant.
- [ ] Event conversion rules for forms; URL rules only where events are impossible.
- [ ] Primary rule attached to every relevant campaign.
- [ ] Lead gen form sync tested this month.
- [ ] CAPI live for at least the qualified lead stage, deduplicated.
- [ ] CRM stores LinkedIn identifiers and hidden field values.
- [ ] Monthly reconciliation done.
- [ ] One lift or holdout test planned per half year at Growth tier and above.
