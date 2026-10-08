# Offline and CRM Conversions

For lead gen, B2B, local services and any business where revenue happens after the click (calls, sales teams, in-store, subscriptions), the ad platforms only learn what you send back. This module covers click ID capture and storage, CRM data models, HubSpot, Salesforce and Pipedrive patterns, Google Data Manager, upload rules, stage values, and adjustments.

## 1. Click ID catalog

| Parameter | Platform | Cookie or storage set by the platform tag | Upload use | Notes |
|-----------|----------|-------------------------------------------|-----------|-------|
| gclid | Google Ads (auto-tagging) | _gcl_aw (Conversion Linker) | Offline click conversions | Only one of gclid, gbraid, wbraid per uploaded row |
| gbraid | Google Ads, iOS app-related clicks | _gcl_gb | Offline conversions associated with app conversions from iOS 14+ traffic | Aggregated; no user-level join |
| wbraid | Google Ads, iOS web-related clicks | _gcl_gb | Offline conversions associated with web conversions from iOS 14+ traffic | Aggregated |
| gad_source, gad_campaignid | Google Ads | n/a | Diagnostic only | Do not use as join keys |
| fbclid | Meta | _fbc (as fb.1.<ms>.<fbclid>) | CAPI fbc | Build fbc server-side if cookie missing |
| ttclid | TikTok | _ttp is the browser ID; store ttclid yourself | Events API ttclid | |
| msclkid | Microsoft Ads (auto-tagging) | _uetmsclkid | Offline conversions (90-day window) | |
| li_fat_id | LinkedIn (enhanced conversion tracking) | li_fat_id first-party cookie | CAPI LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID | |
| epik | Pinterest | _epik | CAPI click_id | |
| ScCid | Snap | _scid | CAPI sc_click_id | |
| rdt_cid | Reddit | _rdt_cid, _rdt_uuid | CAPI click_id | |
| oppref | ChatGPT Ads (OpenAI) | First-party cookie set by the OpenAI pixel [Unverified name __oppref] | CAPI | |
| utm_* | All | Store yourself | Reporting, CRM source | Store first touch and last touch |

## 2. Capture and storage pattern

1. On every landing, read the URL parameters above and store each in a first-party cookie (90 days, SameSite=Lax, Secure, on the root domain) and in localStorage as backup. Keep the most recent value per platform plus a first touch copy of UTMs. Code: [Implementation recipes](implementation-recipes.md) recipe 8.
2. On every form (lead, demo, quote, booking, signup), write the stored values into hidden fields. For embedded third-party forms (HubSpot, Typeform, Calendly) use their hidden field or URL parameter features.
3. On server receipt, save them on the lead or contact record, plus client_id, fbp, fbc, IP, user agent, consent flags and the landing page.
4. On conversion to opportunity, copy the original click IDs to the opportunity or deal (CRMs often do not copy custom fields automatically).
5. For phone leads, use call tracking with dynamic number insertion that records gclid and other click IDs per call (CallRail, Invoca, WhatConverts and similar), and import qualified calls.

Fill rate KPI: share of new paid leads with a click ID for their source platform. Target 90% or more for Google (auto-tagging) leads [Practitioner consensus]. Below 70% means the capture is broken (redirects stripping parameters, single page forms, iframes).

## 3. CRM data model

| Object | Fields to add |
|--------|---------------|
| Contact or Lead | gclid, gbraid, wbraid, fbclid, fbc, fbp, ttclid, msclkid, li_fat_id, epik, sccid, rdt_cid, oppref, utm_source, utm_medium, utm_campaign, utm_content, utm_term, first_touch_utm_* , landing_page, ga_client_id, ga_session_id, consent_ads, consent_analytics, lead_created_at (with timezone), hashed_email (optional) |
| Opportunity or Deal | Copies of the click IDs and UTMs from the primary contact, stage, stage_changed_at, amount, expected gross profit, closed_won_at |
| Upload log (table or object) | record ID, platform, conversion action, event_id, sent_at, status, error |

## 4. Stage design and values

| Stage | Example definition | Upload as | Typical role |
|-------|--------------------|-----------|--------------|
| Lead | Valid form or call over 60 seconds | Web conversion (tag) | Secondary once deeper stages have volume |
| Qualified lead (MQL or SAL) | Passes ICP and contactability checks | Offline conversion | Primary for most lead gen until SQL volume is enough |
| SQL or opportunity | Sales accepted, meeting held | Offline conversion | Primary when 30 or more per month per campaign group |
| Closed won | Paid customer | Offline conversion with real value | Primary for value-based bidding at scale; secondary when too sparse |

Stage value formula:

```
value(stage) = P(closed won given stage) x average gross profit per closed deal
```

Example: average gross profit per deal $6,000. Close rates: lead 5%, MQL 12%, SQL 30%, closed won 100%. Values: lead $300, MQL $720, SQL $1,800, closed won $6,000 (or the actual deal gross profit). Recalculate quarterly from CRM data. If you upload several stages to the same platform, mark only one as primary or use a single action with stage-specific values (choose one approach and document it).

## 5. Google Ads: imports in 2026

| Path | Use | Notes |
|------|-----|-------|
| Data Manager (Google Ads UI: Tools > Data manager) | Native connectors for HubSpot, Salesforce, Shopify, Zapier, Google Sheets, BigQuery, Cloud Storage and others | Easiest for Growth tier; schedule daily |
| Data Manager API | Programmatic uploads of offline conversions, enhanced conversions for leads, events and audiences | Primary API after Google moved uploads off the Google Ads API from 2026-06-15 [Official, 2026-05]. Needs its own OAuth scope (datamanager) and Google Cloud project; reported limits 100,000 requests per day, 300 per minute, up to 2,000 events per request [Secondary, 2026; check quotas page] |
| Google Ads API (legacy UploadClickConversions) | Only for allowlisted developer tokens with recent upload history (lookback reported as January to June 2026 by Google Ads Help, or 2025-12-17 to 2026-06-15 by other sources [Contested]); others get CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE | Google calls the legacy access transitional and has published no end date; do not build new integrations on it. Run old and new pipelines in parallel for 2 to 4 weeks and check response bodies, not job status |
| Manual CSV upload | Starter, monthly | Use the template from Google Ads; watch timezone formats |
| Salesforce native integration | Historic native import from Salesforce opportunities | Check whether it now routes through Data Manager in your account |

Upload rules [Official, long standing; verify]:
- Create the conversion action (type Import, from clicks) before the first upload and wait several hours before uploading against it.
- Conversion time must be after the click time and within the action's click-through conversion window (max 90 days).
- conversion_date_time format includes the timezone offset (for example `2026-10-08 14:30:00+03:00`).
- One click ID per row; gclid preferred when present. Enhanced conversions for leads can match on hashed email or phone when the click ID is missing.
- Pass the consent fields for EEA users.
- Use order_id or a unique lead ID to prevent duplicates.
- Check Goals > Conversions > Uploads (or Data Manager history) for diagnostics after each run.

Adjustments: retract (refunds, cancelled deals) and restate (changed value) uploaded or tagged conversions with conversion adjustments (needs order_id on the original conversion) [Official]. Use for refunds over a material threshold and for closed won value corrections.

## 6. Meta: CRM and offline events

- Send CRM stage events through the Conversions API with action_source "system_generated" (or "physical_store" for in-store sales), matching keys (hashed email and phone, lead_id for Meta lead ads, external_id), and event_time of the stage change.
- For Meta lead ads: connect the CRM in Events Manager (CRM integration) and use the Conversion leads optimization goal when the account meets eligibility (volume and stage rate requirements change; check Meta Business Help) [Official; verify thresholds].
- Offline Conversions API (old offline event sets) was discontinued with the Graph API v16.0 expiry in May 2025 (vendors cite 2025-05-01 or 2025-05-14); offline events now go through the Conversions API tied to a dataset [Official, Meta for Developers 2025-05]. Migrate any legacy offline event set uploads and watch accepted event counts after the switch.

## 7. HubSpot

| Need | How |
|------|-----|
| Click ID capture | HubSpot tracking code and forms capture some ad click IDs into contact properties when ad accounts are connected (for example a Google ad click ID property) [verify property names in your portal]; add hidden fields for others |
| Google Ads | HubSpot Ads tool: connect Google Ads, then create ad conversion events from lifecycle stages (Marketing > Ads > Events) which sync as offline conversions; or Google Ads Data Manager HubSpot connector |
| Meta | HubSpot Ads tool sends lifecycle stage events to Meta via CAPI when the Meta ad account is connected |
| LinkedIn | HubSpot Ads tool supports LinkedIn conversion sync |
| Microsoft | Microsoft announced a HubSpot integration (CRM audiences, lead follow-up, pipeline reporting) in September 2026, in beta [Secondary, 2026-09; verify] |
| QA | Compare HubSpot lifecycle counts per day with the platform's uploaded conversion counts |

## 8. Salesforce

1. Add custom fields on Lead (GCLID__c, GBRAID__c, WBRAID__c, FBCLID__c, FBC__c, TTCLID__c, MSCLKID__c, LI_FAT_ID__c, UTM fields, Consent_Ads__c).
2. Map lead fields to Contact and Opportunity on conversion (Lead conversion field mapping), or copy via Flow.
3. Google Ads: Data Manager Salesforce connector (or the legacy native Salesforce import) mapping Opportunity stages to conversion actions; set values from Amount or an expected gross profit field.
4. Meta and LinkedIn: use their CRM integrations or a middleware (sGTM webhook, Hightouch or Census reverse ETL, Zapier, Make) to send stage changes via CAPIs.
5. Schedule daily; log uploads in a custom object.

## 9. Pipedrive and other CRMs

Pipedrive, Zoho, Close, Monday CRM, Bitrix24 and custom CRMs usually lack a native Google Ads offline import [verify in each marketplace]. Options:
1. Store click IDs in custom deal and person fields (hidden form fields or the web forms add-on).
2. Export stage changes daily to Google Sheets or BigQuery and connect them to Google Ads Data Manager.
3. Or webhook on stage change to a small server function (or sGTM data client) that sends to Data Manager API, Meta CAPI, LinkedIn CAPI, Microsoft offline.
4. Or Zapier or Make scenarios with official app connectors; check rate limits and error handling.

## 10. Upload pipeline template (server function)

```
Trigger: CRM webhook on stage change (or nightly batch query: deals changed since last run)
For each record:
  1. Load click IDs, hashed identifiers, consent flags, stage, value, timestamps
  2. Skip if no consent for ads (opt-in regions) or if already uploaded (upload log by record ID plus stage)
  3. Build platform payloads (Google Data Manager, Meta CAPI system_generated, LinkedIn CAPI, Microsoft offline)
  4. Send with retries; write status to the upload log
  5. Alert if failure rate over 2% or zero uploads on a business day
Weekly: fill rate report (click ID present), match rate per platform, latency (stage change to upload)
```

## 11. Value adjustments and refunds

| Business event | Google Ads | Meta | GA4 |
|----------------|-----------|------|-----|
| Full refund | Retraction adjustment on order_id | No retraction API; exclude refunded orders from future value calculations and keep a refund rate factor in reporting | refund event via Measurement Protocol |
| Partial refund | Restatement with new value | Same as above | refund with items |
| Deal value changed | Restatement | Send updated value on later stage event | n/a |
| Subscription renewals | Upload as separate conversion action (secondary) or include in pLTV value | Subscribe or custom event (secondary) | purchase with subscription params or custom |

## 12. QA and monitoring

| Check | Target | How |
|-------|--------|-----|
| Click ID fill rate on paid leads | 90% or more for auto-tagged platforms | CRM report by source |
| Upload success rate | 98% or more | Upload log |
| Match rate (Google Data Manager or upload diagnostics) | Stable, investigate drops over 10 points | Platform diagnostics |
| Latency | Under 24 hours (under 6 hours for value-based bidding) | Upload log |
| Stage counts parity | Platform uploaded conversions equal CRM stage changes with click IDs and consent | Weekly reconciliation |
| Value parity | Sum of uploaded values equals CRM values for uploaded records | Weekly reconciliation |
