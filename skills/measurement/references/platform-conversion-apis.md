# Platform Conversion APIs

Server-side conversion APIs (CAPIs) recover events lost in the browser, carry match keys the browser cannot, and let you send offline and delayed events. This module covers the shared rules (dedup, hashing, match keys, timing, consent), then each platform. Payload shapes below are working templates: confirm field names and API versions in the current docs before shipping (see Freshness Protocol in SKILL.md).

## 1. Shared rules

### Deduplication

| Rule | Detail |
|------|--------|
| Same event_id on browser and server copies | Generate once (order ID for purchases, a UUID for leads and other events), push it into the data layer, use it in the pixel call and pass it to the server |
| Same event name | Meta dedups on event_name plus event_id; mismatched names are not deduplicated |
| Time window | Meta deduplicates browser and server events with the same event_id received within 48 hours [Official]; other platforms use similar windows, check docs |
| Server-only events | Still set event_id (order ID) so retries and replays do not double count |
| GA4 | Deduplicates purchases by transaction_id within a property only partly; prevent duplicates at the source |
| Google Ads | order_id (transaction_id) deduplicates conversions for the same conversion action |

### Hashing and normalization

Hash with SHA-256, output lowercase hex. Normalize before hashing; a single character difference produces a non-matching hash.

| Field | General normalization | Platform specifics [Official docs; verify each before shipping] |
|-------|----------------------|------------------------------------------------------------------|
| Email | Trim, lowercase | Google: for gmail.com and googlemail.com, remove dots in the local part for API uploads |
| Phone | Digits only with country code | Meta, Pinterest, Snap: digits only, country code, no plus, no leading zeros. Google and TikTok: E.164 with plus (for example +905321234567) before hashing |
| First and last name | Trim, lowercase, remove punctuation | Meta: UTF-8, lowercase, no punctuation; Google: lowercase, trimmed |
| City | Lowercase, no spaces or punctuation (Meta) | |
| State or region | 2-letter code lowercase (US); ISO subdivision elsewhere | |
| Postal code | Lowercase, no spaces; US 5 digits | Google sends postal code and country in clear in some APIs |
| Country | ISO 3166-1 alpha-2 lowercase | Often sent in clear |
| Date of birth | YYYYMMDD | |
| Gender | f or m | |
| External ID | Your stable customer ID; hashing recommended | Must be identical across browser and server |

Never hash: IP address, user agent, fbc, fbp, click IDs (gclid, ttclid, epik, ScCid, rdt_cid, li_fat_id, msclkid, oppref), event_id, order_id.

### Match keys by priority

| Priority | Key | Notes |
|----------|-----|-------|
| 1 | Click ID or platform cookie (fbc, fbp, ttclid, _ttp, epik, _scid, li_fat_id, msclkid, gclid, oppref) | Deterministic link to the ad interaction |
| 2 | Email (hashed) | Highest match rate personal key |
| 3 | Phone (hashed) | Strong in mobile-first markets (Turkey, LATAM, Asia) |
| 4 | External ID | Joins events from the same customer |
| 5 | IP plus user agent | Required for website events on Meta; improves match |
| 6 | Name plus city plus postal code | Weak alone, useful together |

### Event timing

- Send in real time for website events. Meta rejects website events with event_time older than 7 days [Official]; Google offline click conversions must be within the conversion action's click-through window (up to 90 days) [Official]; check others.
- Use the actual conversion timestamp (order created time), not the send time.
- Retries: exponential backoff, idempotent event_id, dead-letter queue, alert on failure rate over 2%.

### Consent

The server must know the browser consent state. Store it with the order or lead (for example `consent_ads=true`). Do not send ad platform events for users who denied ad consent in opt-in regions; for US opt-outs send with restricted processing flags (Meta LDU) or not at all per policy.

## 2. Meta Conversions API

| Item | Value |
|------|-------|
| Endpoint | `POST https://graph.facebook.com/<API_VERSION>/<PIXEL_ID>/events?access_token=<TOKEN>` (use the current Graph API version) |
| Token | System user access token from Events Manager (Settings > Conversions API > Generate access token) |
| Required for website events | event_name, event_time, action_source="website", event_source_url, user_data.client_ip_address, user_data.client_user_agent |
| Dedup | event_id equal to the pixel's eventID, same event_name |
| Match keys | em, ph, fn, ln, ct, st, zp, country, db, ge, external_id (hashed); fbc, fbp, client_ip_address, client_user_agent (not hashed) |
| fbc format | `fb.1.<creation_time_ms>.<fbclid>`; build from the fbclid URL parameter if the _fbc cookie is missing |
| Testing | `test_event_code` from Events Manager Test Events tab |
| Quality | Event Match Quality (0 to 10) per event in Events Manager; target 6 or higher on Purchase, 8 or higher is the practitioner goal [Practitioner consensus] |
| Options | CAPI Gateway (Meta-provided server, self-hosted in your cloud or via partners such as Stape), Signals Gateway (routes first-party signals to Meta and other destinations), partner integrations (Shopify Facebook and Instagram app with "Maximum" data sharing, WooCommerce plugin, GTM server templates) |
| Restrictions | Health, wellness and some financial categories face data sharing and optimization limits introduced in 2025 [Official, 2025; verify]; Meta's "Core setup" can limit URL parameters and custom data for restricted categories |

```json
{
  "data": [{
    "event_name": "Purchase",
    "event_time": 1760000000,
    "event_id": "order_100234",
    "action_source": "website",
    "event_source_url": "https://example.com/checkout/thank-you",
    "user_data": {
      "em": ["<sha256 lowercase email>"],
      "ph": ["<sha256 digits with country code>"],
      "external_id": ["<sha256 customer id>"],
      "client_ip_address": "203.0.113.10",
      "client_user_agent": "Mozilla/5.0 ...",
      "fbc": "fb.1.1759990000000.IwAR...",
      "fbp": "fb.1.1759000000000.1234567890"
    },
    "custom_data": {
      "currency": "USD",
      "value": 84.50,
      "order_id": "100234",
      "content_type": "product",
      "contents": [{"id": "SKU-123", "quantity": 1, "item_price": 84.50}]
    }
  }]
}
```

Lead gen: for CRM stage events use action_source "system_generated" and the lead ID from Meta lead forms (lead_id) or your own external_id, and connect the CRM in Events Manager to use the "Conversion leads" optimization goal where eligible [Official; check current eligibility rules].

Attribution changes that affect CAPI reporting: see [Attribution](attribution.md) (7-day and 28-day view windows removed from the Ads Insights API on 2026-01-12; click-through limited to link clicks and engage-through split out in March 2026).

## 3. Google: enhanced conversions, Data Manager, offline imports, GA4 Measurement Protocol

### Enhanced conversions for web

Sends hashed first-party data with the conversion tag so Google can match conversions it would otherwise miss.

| Method | How | Use when |
|--------|-----|---------|
| Automatic (Google tag) | Google tag detects email and phone on the conversion page or form | Quick start, standard forms |
| Manual (CSS selectors or JS variables in Google Ads settings or GTM) | Point to fields | When automatic misses |
| Code | `gtag('set', 'user_data', {...})` before the conversion event, or GTM "User-provided data" variable in the Google Ads conversion tag | Most reliable; recommended |

```js
gtag('set', 'user_data', {
  email: 'jane@example.com',          // or sha256_email_address
  phone_number: '+905321234567',       // E.164 or sha256_phone_number
  address: { first_name: 'jane', last_name: 'doe', postal_code: '34000', country: 'TR' }
});
gtag('event', 'conversion', {
  send_to: 'AW-123456789/AbCdEfGhIjk',
  value: 84.5, currency: 'USD', transaction_id: '100234'
});
```

Enable in Google Ads: Goals > Conversions > Settings > Enhanced conversions (and accept customer data terms). Google merged the settings in 2026: from April Google Ads accepts user-provided data from tags, Data Manager and API connections at the same time, and from June enhanced conversions for web and for leads are one on or off setting (account level or per conversion action) with the method selection screen removed; existing users who accepted customer data terms were migrated [Official, 2026-04; June step via trade press 2026-06; confirm in the account].

### Enhanced conversions for leads and offline conversion import

- Capture: the tag hashes email or phone at form submit (enhanced conversions for leads), and your form stores gclid, gbraid or wbraid in the CRM.
- Upload: when the lead converts in the CRM, upload the conversion with the click ID and or hashed user identifiers.
- Route as of 2026: Google Ads Data Manager (UI) connectors (HubSpot, Salesforce, Google Sheets, BigQuery, Cloud Storage, others) or the Data Manager API. Google moved offline conversion imports and enhanced conversions for leads uploads from the Google Ads API (ConversionUploadService.UploadClickConversions) to the Data Manager API starting 2026-06-15 (announced 2026-05-15); developer tokens without upload history in the lookback window get CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE, and the window is reported differently by source (January to June 2026, or 2025-12-17 to 2026-06-15) [Official, 2026-05; window Contested]. Legacy access is transitional with no published end date. New users of session attributes and IP address data in Google Ads API imports were blocked from 2026-02-02; Data Manager accepts them [Official, 2026].
- Fields: click ID (only one of gclid, gbraid, wbraid per row), conversion action, conversion date time with timezone, value, currency, order ID, hashed user identifiers, consent (ad user data, ad personalization) for EEA users.

Details and CRM recipes: [Offline and CRM conversions](offline-and-crm-conversions.md).

### GA4 Measurement Protocol

```
POST https://www.google-analytics.com/mp/collect?measurement_id=G-XXXX&api_secret=SECRET
(EU endpoint: region1.google-analytics.com; validate with /debug/mp/collect)
{
  "client_id": "1234567890.1759990000",
  "user_id": "cust_8841",
  "consent": {"ad_user_data": "GRANTED", "ad_personalization": "GRANTED"},
  "events": [{
    "name": "purchase",
    "params": {
      "session_id": "1759990000",
      "engagement_time_msec": 1,
      "transaction_id": "100234",
      "value": 84.5, "currency": "USD",
      "items": [{"item_id": "SKU-123", "item_name": "Tee", "price": 84.5, "quantity": 1}]
    }
  }]
}
```

Rules: capture client_id (from the _ga cookie) and session_id (from the _ga_<container> cookie) at checkout and store them on the order; without them MP events land as Unassigned or break sessions. Timestamps up to 72 hours back. Google recommends the Data Manager API for new server-to-server integrations into Google Ads while keeping MP supported [Official, 2025].

## 4. TikTok Events API

| Item | Value |
|------|-------|
| Endpoint | `POST https://business-api.tiktok.com/open_api/v1.3/event/track/` with header `Access-Token` (generate in Events Manager) [verify version] |
| Dedup | Same event_id in pixel (`ttq.track('CompletePayment', {...}, {event_id: 'order_100234'})`) and server |
| Match keys | email and phone (SHA-256; phone in E.164 with plus before hashing), external_id (hashed), ttclid (URL parameter, store first-party), ttp (_ttp cookie), ip, user_agent |
| Events | ViewContent, AddToCart, InitiateCheckout, AddPaymentInfo, CompletePayment or Purchase (check current naming), PlaceAnOrder, CompleteRegistration, SubmitForm, Contact, Subscribe, Lead events for CRM |
| Gateways | TikTok Events API Gateway, partner integrations (Shopify TikTok app, sGTM templates) |
| Quality | Event quality and match rate diagnostics in Events Manager |

```json
{
  "event_source": "web",
  "event_source_id": "<PIXEL_CODE>",
  "data": [{
    "event": "CompletePayment",
    "event_time": 1760000000,
    "event_id": "order_100234",
    "user": {
      "email": "<sha256>", "phone": "<sha256 of +905321234567>",
      "external_id": "<sha256>", "ttclid": "E.C.P.abc...", "ttp": "abc123...",
      "ip": "203.0.113.10", "user_agent": "Mozilla/5.0 ..."
    },
    "page": {"url": "https://example.com/checkout/thank-you"},
    "properties": {
      "currency": "USD", "value": 84.5, "order_id": "100234",
      "content_type": "product",
      "contents": [{"content_id": "SKU-123", "quantity": 1, "price": 84.5}]
    }
  }]
}
```

## 5. LinkedIn Conversions API

| Item | Value |
|------|-------|
| Endpoint | `POST https://api.linkedin.com/rest/conversionEvents` with headers `LinkedIn-Version: <YYYYMM>` and `X-Restli-Protocol-Version: 2.0.0`, OAuth token with conversions scope |
| Setup | Create a conversion rule in Campaign Manager with "Conversions API" as the data source; attach to campaigns |
| Match keys | SHA-256 email, LinkedIn first-party ad tracking ID (li_fat_id, appended to landing URLs when enhanced conversion tracking is on), plus first name, last name, company, title, country for matching |
| Dedup | eventId shared with the Insight Tag event |
| Use | B2B lead to pipeline loops: send MQL, SQL, opportunity and closed won from the CRM (native HubSpot and Salesforce integrations exist; check current list) |

```json
{
  "conversion": "urn:lla:llaPartnerConversion:123456",
  "conversionHappenedAt": 1760000000000,
  "conversionValue": {"currencyCode": "USD", "amount": "12000.0"},
  "eventId": "opp_0065g00000XYZ",
  "user": {
    "userIds": [
      {"idType": "SHA256_EMAIL", "idValue": "<sha256>"},
      {"idType": "LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID", "idValue": "<li_fat_id>"}
    ],
    "userInfo": {"firstName": "Jane", "lastName": "Doe", "companyName": "Acme", "countryCode": "US"}
  }
}
```

## 6. Microsoft Advertising (UET, enhanced conversions, offline, CAPI)

| Item | Value |
|------|-------|
| UET tag | Base tag on every page; events via `window.uetq.push('event', 'purchase', {revenue_value: 84.5, currency: 'USD'})` |
| Enhanced conversions | Pass email or phone with UET (`window.uetq.push('set', {pid: {em: '<email>', ph: '<+E164 phone>'}})`), hashed by UET or pre-hashed [Official; verify syntax] |
| Consent | UET consent mode (ad_storage); required for EEA, UK and Swiss traffic |
| Offline conversions | Upload by MSCLKID (stored from the landing URL, 90-day window) via UI, scheduled file or API; enhanced conversions for leads with hashed email or phone |
| Conversions API | Server-side Conversions API in beta: Microsoft provisions it per account (request through the account manager or support), recommends running it alongside UET, and published full documentation in August 2026. A goal must exist for the UET tag and event name, or events return 200 with no conversions recorded [Official docs via trade press, 2026-08]. Do not scope it into a statement of work until the account exposes it |
| Auto-tagging | Turn on MSCLKID auto-tagging in account settings |

## 7. Pinterest Conversions API

| Item | Value |
|------|-------|
| Endpoint | `POST https://api.pinterest.com/v5/ad_accounts/<AD_ACCOUNT_ID>/events` with a conversion access token |
| Events | checkout, add_to_cart, page_visit, signup, lead, search, view_category, watch_video, custom |
| Match keys | em, ph (hashed), external_id, client_ip_address, client_user_agent, click_id (epik parameter or _epik cookie) |
| Dedup | event_id shared with the Pinterest tag `pintrk('track', 'checkout', {event_id: ...})` |

## 8. Snap Conversions API

| Item | Value |
|------|-------|
| Endpoint | Snap Conversions API v3 (`https://tr.snapchat.com/v3/<PIXEL_ID>/events`), Meta-like schema [verify] |
| Match keys | hashed email and phone, IP, user agent, sc_click_id (ScCid URL parameter), sc_cookie1 (_scid cookie) |
| Dedup | event_id (and client_dedup_id in older versions) shared with Snap Pixel |

## 9. Reddit Conversions API

| Item | Value |
|------|-------|
| Endpoint | Reddit Ads API conversions endpoint for the ad account or pixel (v2.0 and newer v3 paths exist; check current docs) |
| Match keys | click_id (rdt_cid URL parameter), hashed email, IP, user agent, uuid (_rdt_uuid cookie) |
| Dedup | conversion_id shared with the Reddit Pixel event |
| Events | PageVisit, ViewContent, Search, AddToCart, AddToWishlist, Purchase, Lead, SignUp, Custom |

## 10. ChatGPT Ads (OpenAI) pixel and Conversions API

Status (as gathered from OpenAI help center article titles, press coverage and community API notes; treat specifics as [Unverified] until checked in the OpenAI Ads help center):
- OpenAI began testing ads in ChatGPT in the US in January to February 2026; self-serve Ads Manager beta (ads.openai.com) with pixel and Conversions API launched around 2026-05-05; conversion-optimized campaigns began rolling out in June 2026; availability expanded to 60+ countries by late September 2026 [Secondary, 2026].
- Pixel plus CAPI with event ID deduplication (first event received wins); click parameter `oppref` appended to landing URLs and stored by the pixel in a first-party cookie; include it in CAPI events. Community notes describe cookies `__oppref` (30 days) and `__obref` (365 days) and a CAPI endpoint at `bzr.openai.com/v1/events` [Unverified].
- Conversion optimization uses standard events only; event quality score in Ads Manager; 24 to 48 hour reporting lag; automatic advanced matching hashes form data in the browser.
- Attribution: conversions are click-through; 30-day window recommended; 1-day view-through reported only [Unverified].
- Integrations: OpenAI Pixel for Shopify app; MMPs (Adjust, Airbridge, AppsFlyer, Branch, Kochava, Singular, Tenjin); measurement partners announced in 2026.
- Consent: the pixel exposes a consent call (community notes); not available for custom audiences in EEA and Switzerland.

Hand off campaign questions to chatgpt-ads; measurement owns pixel, CAPI, oppref capture and dedup.

## 11. Rollout procedure (any platform)

1. Event spec: event names, parameters, event_id rule, values, consent behavior.
2. Browser: pixel events with event_id from the data layer.
3. Server: sender module (see [Implementation recipes](implementation-recipes.md)) or sGTM template or native integration; read access token from environment variables or secret manager, never from code.
4. Test: platform test tool (Meta Test Events, TikTok Test Events, Pinterest and Snap test tools, LinkedIn test conversions, Google Tag Assistant and Ads diagnostics), confirm dedup ("Deduplicated" labels in Meta), match quality, values and currency.
5. Ship behind a feature flag; compare counts for 7 days: backend orders vs browser events vs server events vs platform reported.
6. Monitor: daily server success rate, dedup ratio, EMQ trend; alert on drops.
7. Document in MEASUREMENT.md tracking stack table with "Last verified" date.

## 12. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Meta shows server events but no dedup | event_id differs (prefix, type), or event_name differs (Purchase vs purchase) | Same string, same case |
| Meta overcounts after CAPI launch | Browser events without eventID | Add eventID to every pixel event |
| Low EMQ | Only IP and UA sent | Add em, ph, external_id, fbc, fbp |
| TikTok events rejected | Old API version, wrong token, phone not E.164 before hashing | Update version, regenerate token, fix normalizer |
| Google enhanced conversions "Needs attention" | Data not detected, formatting errors, terms not accepted | Code method, normalize, accept terms |
| Offline uploads fail since June 2026 | Legacy Google Ads API path blocked | Move to Data Manager API or a Data Manager connector |
| LinkedIn CAPI 400 errors | Missing LinkedIn-Version header or wrong URN | Add header, check conversion rule ID |
| Values off by 100x | Cents vs units | Send decimals in currency units |
