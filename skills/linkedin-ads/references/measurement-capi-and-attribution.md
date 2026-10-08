# Measurement: Insight Tag, Conversions API and Attribution

> Scope: Insight Tag, conversion rules and windows, enhanced conversion tracking, Conversions API, offline and CRM conversions, the revenue attribution report, company engagement and Demographics reporting, lift and A/B tests, and reconciling LinkedIn numbers with the CRM. Implementation is owned by the measurement agent. Code and field names are patterns to verify against LinkedIn documentation.

## 1. Measurement architecture
```
Browser: Insight Tag (partner ID) -> page and event conversions, website retargeting, visitor demographics
Server:  Conversions API -> online and offline events with hashed identifiers, deduplicated with the tag by event ID
CRM:     Lead gen form sync -> lifecycle stages -> CAPI or CRM conversion sync -> LinkedIn optimization and reporting
Reports: Campaign Manager (conversions, Demographics, company engagement), revenue attribution report (CRM connected), lift tests
Truth:   CRM opportunities and revenue (MEASUREMENT.md)
```

## 2. Insight Tag
1. Create or locate the Insight Tag (partner ID) in Campaign Manager.
2. Install site wide via GTM (LinkedIn Insight Tag template) or the site header. One tag per ad account; share via Business Manager or account settings if several accounts need it [Unverified] for current sharing mechanics.
3. Consent: in regions requiring consent, load the tag only after marketing consent through the CMP. The tag does not have a Microsoft or Google style consent mode with modeling [Unverified]; expect lower observed conversions where consent rates are low, and use CAPI with consented identifiers where lawful.
4. Verify: Campaign Manager shows the tag as active; browser network requests to LinkedIn's tag endpoint fire on page load and on events.

Event conversion pattern (verify syntax in docs):
```javascript
// After a successful form submit (event specific conversion rule)
window.lintrk && window.lintrk('track', { conversion_id: 1234567 });
```
Enhanced conversion tracking (collecting hashed first-party data such as email from forms with consent) exists as a setting [Unverified] for 2026 behavior; enable only with legal approval.

## 3. Conversion rules
| Setting | Options (as known) | Recommendation | Label |
|---------|-------------------|----------------|-------|
| Type | Lead, purchase, sign up, download, key page view, add to cart, install, other | Use the true category; set a primary qualified event | [Official, 2022] |
| Method | Page load (URL rule), event specific (JS), CAPI, offline or CRM | Event specific or CAPI over URL rules for forms | [Official, 2023] |
| Value | Static or dynamic value | Stage value for lead gen | [Official] |
| Post-click window | 1, 7, 30, 90 days | 30 or 90 days for B2B with long cycles | [Official, 2022] [Unverified] for current options |
| Post-view window | 1, 7, 30 days | 7 days default; shorten for awareness heavy accounts when comparing channels | [Official, 2022] [Unverified] |
| Attribution | Last touch each campaign, or last touch last campaign | Last touch each campaign for campaign level optimization; understand double counting across campaigns | [Unverified] |
| Counting | One per click or every conversion | One for leads, every for purchases | [Unverified] |
| Campaigns | Attach to all relevant campaigns | Check new campaigns get the rule | [Official] |

Reporting caution: LinkedIn view-through conversions inflate results relative to click based channels. Report click and view conversions separately and reconcile with the CRM.

## 4. Conversions API (CAPI)
Status: LinkedIn launched its Conversions API in 2023 with partner integrations; it accepts online and offline events with hashed identifiers [Official, 2023]. LinkedIn maintains an official Google Tag Manager server-side tag template (github.com/linkedin-developers/linkedin-capi-tag-template, created 2023-08) and published an Adobe Experience Platform event forwarding extension repository in 2026-06 [Official, GitHub 2026-06].

Key mechanics (as known; verify):
| Item | Detail | Label |
|------|--------|-------|
| Conversion rule | Create a rule with CAPI as a data source; events reference the rule | [Official, 2023] |
| Identifiers | SHA-256 hashed email; LinkedIn first-party ad tracking ID (li_fat_id click parameter when enabled); other IDs and user info such as first name, last name, company, title, country improve matching | [Unverified] for the 2026 list |
| Deduplication | Same event ID from Insight Tag and CAPI for the same conversion | [Official, 2023] |
| Event age | Events must be recent (historically within 90 days of the conversion) | [Unverified] |
| Auth | OAuth access token with the conversions scope via the Marketing API | [Official] |
| Integrations | GTM server, CDPs and CRM connectors (HubSpot, Salesforce, Dynamics and others), Zapier style tools | [Unverified] for current list |

CAPI rollout procedure:
1. Choose the path: native CRM connector (fastest for lifecycle stages), GTM server-side template (web events), CDP (if the stack has one).
2. Define events: lead (online), MQL, SQL, opportunity, closed won (offline from CRM), purchase (ecommerce).
3. Create conversion rules for each, with values from the stage value model.
4. Enable the first-party click ID capture if available; store it with the lead in the CRM.
5. Send events with event IDs; dedupe with the tag for online events.
6. Validate match rates and counts in Campaign Manager over 7 days.
7. Switch campaign optimization to the qualified event only when it reaches enough volume (30+ per month per campaign as a rule of thumb) [Practitioner consensus].

## 5. Offline and CRM conversions
- Offline conversions can be uploaded (CSV or integration) and attributed to ad engagement by matching identifiers [Official, 2022] [Unverified] for current upload formats.
- Native CRM connections can sync lifecycle stages as conversions [Unverified] for supported CRMs and stages.
- Keep a dedicated CRM property for LinkedIn click IDs and lead gen form IDs to aid matching and troubleshooting.

## 6. Revenue attribution report (RAR)
- What: a Campaign Manager report that connects to the CRM and shows pipeline and revenue influenced by LinkedIn ads, plus metrics like return on ad spend and deal velocity [Official, 2023].
- CRMs: launched with Salesforce and Microsoft Dynamics; HubSpot support has been reported since [Unverified].
- Model: influence based (members at accounts on opportunities who engaged with ads within a lookback); not causal [Practitioner consensus]. Check the current lookback options and model description in the report [Unverified].
- Use: directional proof of influence and to compare campaigns on influenced pipeline; never as the only success metric. Pair with holdouts or lift tests for causality.

## 7. Company engagement and Demographics reports
- Demographics report: who saw and clicked your ads by job title, function, seniority, company, industry, company size and location (thresholds hide small counts) [Official, 2019]. Use it two weeks after every launch to confirm ICP match.
- Company engagement report: engagement by company for ABM (see [Targeting and ABM](targeting-and-abm.md)).

ICP match score (compute monthly):
```
ICP match = impressions on target seniorities and functions in target company sizes / total impressions (from the Demographics report)
```
Target 70%+ for lead gen and ABM campaigns [Practitioner consensus]; investigate expansion, Audience Network and broad attributes when lower.

## 8. Lift and A/B testing
| Test | What it measures | When |
|------|------------------|------|
| Campaign Manager A/B test | Difference between creative, audience or placement variants | Ongoing creative and audience decisions |
| Brand lift test | Change in awareness, consideration or ad recall from polling exposed vs control | Awareness and video programs with enough budget (minimums apply) [Unverified] |
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
