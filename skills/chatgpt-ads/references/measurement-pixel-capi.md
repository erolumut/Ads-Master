# Measurement: OpenAI Pixel, Conversions API, UTMs and Attribution

> Knowledge as of 2026-10. Sources: developer docs (Measurement Pixel, Conversions API, Conversion Tracking, Supported Events, Reporting, Conversion Setup), Help Center (Conversion Measurement 20001409, Measure Results 20001214, Conversion-optimized Campaigns 20001412, Measurement Partner Integrations 20001416, Mobile Measurement Partner Integrations 20001372, Publisher FAQ), OpenAI's official `openai-ads-conversions` plugin skill (github.com/openai/plugins), October 2026 measurement announcement. Implementation belongs to the measurement agent; this module is the spec. Re-verify syntax against the live docs before shipping code.

## 1. Architecture

```
ChatGPT ad click
  -> landing URL + your static UTMs + ?oppref=<opaque click reference>   (OpenAI appends oppref)
  -> Pixel (browser) stores oppref in first-party cookie __oppref (30 days) and __obref (365 days)
  -> conversion happens
       browser: oaiq("measure", event, data, {event_id})         -> bzr.openai.com
       server:  POST https://bzr.openai.com/v1/events?pid=PIXEL  -> same event id, oppref, hashed user data
  -> OpenAI dedups on Pixel ID + event name + event_id (first received wins)
  -> attribution: click window 7, 14 or 30 days (default 30), optional 1-day view-through (reporting)
  -> Ads Manager "Conversions" and Insights API (24 to 48 hours lag)
```

Labels: every element above is [Official, 2026-09] except the 1-day view-through reporting toggle [Official, 2026-10].

## 2. Setup sequence

| Step | Ads Manager (UI) | API | Notes |
|------|------------------|-----|-------|
| 1. Data source | Tools > Conversions > Data Source tab: create pixel data source; Pixel ID shown under the source name | `POST /v1/conversions/pixels` returns `pixel_id` (for sending events) and `id` (for event settings) | One pixel ID shared by browser and server |
| 2. CAPI key | Conversions area: key icon > Conversion keys > Create new key (shown once) | `POST /v1/conversions/api_keys` | Different from the Ads API key under Settings. Server side only |
| 3. Install pixel | Site code or tag manager | n/a | See section 3 |
| 4. Send server events | Server code, CDP, MMP or partner | `POST https://bzr.openai.com/v1/events?pid=<pixel_id>` with Bearer CAPI key | See section 4 |
| 5. Event settings | Conversion Events tab | `POST /v1/conversions/event_settings` with `event_type`, `attribution_window_days`, exactly one `source_ids` (use the source `id`, not `pixel_id`) | Custom events need event type Custom and exact name match |
| 6. Attach to campaigns | Campaign setup | `conversion_event_setting_ids` on the campaign (update replaces the list) | Attach before traffic starts; conversions do not backfill after a misconfiguration |
| 7. Verify | Event quality diagnostics | `GET /v1/conversions/events?pid=<pixel_id>&limit=50` returns a sample from the last 15 minutes; browser events show `pixel_sdk`, server events `server_to_server` | Use `validate_only: true` for test payloads (not saved) |

Practitioners report step 6 is the one most often forgotten [Practitioner consensus]. Linkrunner documents the UI paths in step 1 and 2 [Unverified] (partner docs, 2026-09).

## 3. Pixel (browser)

Install [Official, 2026-09]:
- Put the official loader snippet near the top of `<head>`. It loads `https://bzrcdn.openai.com/sdk/oaiq.min.js` asynchronously and creates a global `oaiq` queue. Copy the exact snippet from developers.openai.com/ads/measurement-pixel; do not hand write it.
- Initialize once per page or app load: `oaiq("init", { pixelId: "<PIXEL_ID>" })`. Optional `debug: true` logs to the console (testing only).
- Send events: `oaiq("measure", "<event_name>", { type: "<data_shape>", ... }, { event_id: "<id>" })`.

Consent [Official, 2026-09]:
```js
// Before init when consent is required (GDPR, UK GDPR, similar)
oaiq("consent", false);
oaiq("init", { pixelId: "PIXEL_ID" });
// When the CMP grants consent
oaiq("consent", true);
```
- Consent defaults to true unless set false or a stored denial exists. While false, no pings are sent and blocked events are not replayed. Setting false removes the pixel cookies.
- `opt_out: true` in event options marks events for no user level personalization (OpenAI states it does not currently use pixel data for user level personalization).

User data for matching [Official, 2026-09]:
```js
// After login or when known; never inside measure calls
oaiq("init", { user: {
  email_sha256: "<sha256 of trimmed lowercase email>",
  phone_number_sha256: "<sha256 of digits incl country code, no +>",
  external_id_sha256: "<sha256 of trimmed id, case preserved>",
  first_name_sha256: "...", last_name_sha256: "...",
  country: "US", city: "austin", region: "tx", postal_code: "78701"
}});
```
Normalization: email trim and lowercase; phone with country code, strip formatting and leading + or zeros, 8 to 15 digits; external ID trim only; names lowercase, remove whitespace and ASCII punctuation. Hash with SHA-256, lowercase hex. Never send raw identifiers.

Automatic advanced matching (AAM): when enabled, the pixel detects customer information on the page, hashes it in the browser and attaches it [Official, 2026-09]. OpenAI recommends enabling it for conversion campaigns [Official, 2026-09]. AAM is the default for new web pixels, and OpenAI emailed advertisers (week of 2026-08-03) that it would switch AAM on for existing web pixels on 2026-08-17 unless they opted out per pixel in Ads Manager (Tools > Conversions > Data Source > Edit pixel) [Official, 2026-08] (relayed by PPC Land and Search Engine Land). A 2026-06-16 matching update already used supplied user data and raised reported conversions for some advertisers (agency relays) [Unverified]. Independent research reported that scraped identity outnumbered advertiser supplied identity [Unverified]. Check every pixel's current AAM state; do not assume the pre-August setting. Decide deliberately with legal; document in MEASUREMENT.md.

Content Security Policy [Official, 2026-09]:
| Directive | Allow |
|-----------|-------|
| script-src (and script-src-elem if used) | https://bzrcdn.openai.com plus a per-response nonce |
| connect-src | https://bzr.openai.com, https://bzrcdn.openai.com |
| img-src | https://bzr.openai.com |
Do not add `'unsafe-inline'` for the pixel.

Other pixel facts:
- Image tag alternative for no-JS pages: `https://bzr.openai.com/v1/sdk/events?pid=...&event=...` (render only after consent) [Official, 2026-09].
- Multiple pixels: initialize each; target one with the multiple pixel API [Official, 2026-09].
- `app_installed` and `app_opened` are not supported by the pixel [Official, 2026-09].
- Use integers for `amount` and `quantity`; amounts in minor units (12999 = $129.99).
- Pixel helpers must catch their own errors so analytics never breaks checkout (official plugin guidance) [Official, 2026-09].

## 4. Conversions API (server)

Endpoint and auth [Official, 2026-09]:
```
POST https://bzr.openai.com/v1/events?pid=<PIXEL_ID>
Authorization: Bearer <CONVERSIONS_API_KEY>
Content-Type: application/json
```
Example body (verify field names against developers.openai.com/ads/conversions-api before use):
```json
{
  "events": [
    {
      "id": "order_100045",
      "type": "order_created",
      "timestamp_ms": 1760000000000,
      "action_source": "web",
      "source_url": "https://shop.example.com/checkout/thank-you",
      "oppref": "<raw value from the __oppref cookie or landing URL>",
      "user": {
        "emails_sha256": ["<sha256>"],
        "external_ids_sha256": ["<sha256>"],
        "ip_address": "203.0.113.7",
        "user_agent": "Mozilla/5.0 ..."
      },
      "data": {
        "type": "contents",
        "amount": 12999,
        "currency": "USD",
        "contents": [{ "id": "SKU-1", "quantity": 1, "amount": 12999 }]
      }
    }
  ]
}
```
Field notes:
- `id` is the dedup key and must equal the pixel `event_id` for the same conversion; reuse it on retries [Official, 2026-09].
- `timestamp_ms` is the real conversion time, no older than 7 days and not more than about 10 minutes in the future [Official, 2026-09] and [Unverified] (10 minutes).
- `action_source`: `web`, `mobile_app`, `offline`, `physical_store`, `phone_call`, `email`, `other` [Official, 2026-09].
- `source_url` is required for web events; send origin plus path only (strip query strings and fragments) [Official, 2026-09] (official plugin).
- `oppref`: CAPI does not capture it automatically. Read the raw `__oppref` cookie server side or pass it from the browser; pass it unchanged, never parse, decode, generate or log it [Official, 2026-09].
- A conversion needs at least one strong identifier (oppref, obref, hashed email or hashed external ID); IP and user agent alone are not enough [Unverified] (PostHog destination docs).
- Batches up to 1,000 events; one invalid event fails the whole batch [Unverified] (community notes and Linkrunner).
- `validate_only: true` at the top level tests without saving [Official, 2026-09].
- `integration_source` identifies partner sends [Unverified].
- Do not use legacy names `event_name`, `event_time_epoch_ms`, `event_source_url`, `event_data` [Official, 2026-09] (official plugin).

Consequence of the 7 day limit: CRM qualification events that happen more than 7 days after the lead cannot be sent as ChatGPT Ads conversions. For B2B, optimize on `lead_created` or `trial_started` and judge quality in the CRM separately.

## 5. Supported events [Official, 2026-09]

| Event | Data shape | Typical use | Optimizable (oCPC) |
|-------|-----------|-------------|-------------------|
| `page_viewed` | contents | Key page views | Standard events only; low value goal, avoid |
| `contents_viewed` | contents | Product or content detail views | Possible, weak |
| `items_added` | contents | Add to cart | Mid funnel option |
| `checkout_started` | contents | Checkout start | Mid funnel option |
| `order_created` | contents | Purchase | Yes, preferred for ecommerce |
| `lead_created` | customer_action | Lead form or contact request | Yes |
| `registration_completed` | customer_action | Account or event signup | Yes |
| `appointment_scheduled` | customer_action | Booking, demo | Yes |
| `subscription_created` | plan_enrollment | Paid subscription start | Yes |
| `trial_started` | plan_enrollment | Free trial start | Yes |
| `app_installed` | customer_action | App install (CAPI only, `action_source: mobile_app`) | Yes via CAPI |
| `app_opened` | customer_action | App open (CAPI only) | Reporting |
| `custom` | custom | Anything else; name 1 to 64 chars, lowercase letters, numbers, underscores, dashes, not a standard name | No (reporting only) |

Content item fields: `id`, `group_id` (CAPI only), `name`, `content_type`, `quantity`, `amount`, `currency`, `variant_dict` (CAPI only). If `amount` is present, `currency` is required.

Event mapping rule: fire on confirmed success (order confirmed, form accepted by backend), never on button clicks unless the click is the conversion [Official, 2026-09] (official plugin).

## 6. Deduplication

- Match key: Pixel ID + event name + event ID (for custom events, `custom_event_name` replaces the event name). First received wins [Official, 2026-09].
- Generate the event ID once (for example order ID or a UUID created at form submit), expose it to the browser and the server.
- For deduped web events the server `source_url` should describe the same page as the browser event [Official, 2026-09].
- Custom event names must match exactly across pixel, CAPI and the event setting, or they will not dedupe [Official, 2026-09].

## 7. oppref handling

- OpenAI appends `oppref` to the landing page URL; the pixel stores it in `__oppref` (first-party, 30 days, reset when a new non-empty oppref arrives) [Official, 2026-09].
- Preserve it through every redirect, URL normalizer, consent wall and SPA route change. Test: append a synthetic `?oppref=test123` to each landing URL, follow redirects, confirm it reaches the final URL [Practitioner consensus]. A free independent checker exists (chatgpt-ads-tracking-checker.vercel.app) [Unverified].
- Reserved query parameter names you must not use in your own URL parameters: `oppref`, `olref`, `obref` and anything prefixed `oai` [Official, 2026-09] (serving issue `reserved_query_params_present`) and [Unverified] (exact list).
- For server events, read `__oppref` server side (it is a first-party cookie on your domain) or store it with the lead or order record when the session starts.
- For forms: capture `oppref` and UTMs into hidden fields so CRM and offline sends carry it.

## 8. UTMs and GA4

Paid ChatGPT Ads clicks carry only the UTMs you add. Organic ChatGPT search referrals carry `utm_source=chatgpt.com` added automatically by ChatGPT [Official, 2026-09] (publisher FAQ). Keep them separable.

Recommended paid UTM convention [Practitioner consensus]:
```
utm_source=chatgpt&utm_medium=paid_ai&utm_campaign=<campaign_slug>&utm_content=<adgroup_key>&utm_term=<ad_key>
```
- In Ads Manager, static UTMs on destination URLs work; dynamic UTM macros are not supported in the UI as of the Measure Results article [Official, 2026-09].
- Via the API, ad groups accept a `query_string_template` with placeholders such as `{campaign_id}`, `{ad_group_id}`, `{ad_id}`, `{ad_account_id}`, `{oppref}` [Contested] (documented by community API notes and Linkrunner; Search Engine Roundtable reported dynamic URL support in the August 2026 update alongside oCPC and carousels; the UI article captured in 2026-09 still said dynamic macros are not supported). If you need the click reference in your own parameter, use your own name, for example `click_ref={oppref}`.
- Parameter precedence when set at several levels: ad URL, then ad, then ad group, then campaign, then account [Unverified].
- Never use `utm_source=chatgpt.com` for paid traffic; that value is the organic signal.

GA4 custom channel group (place above the default rules):
| Channel | Rule |
|---------|------|
| Paid AI Assistants | Source matches regex `^(chatgpt\|openai)$` AND Medium matches regex `^(paid_ai\|cpc\|paid.*)$` |
| AI Assistants (organic) | Source matches regex `chatgpt\.com\|perplexity\|copilot\|gemini\|claude\.ai` AND Medium is `referral` or `(none)` |

(The backslashes before the pipe characters only escape the table; enter the regex in GA4 with plain `|`.)

Hand GA4 channel group creation to measurement. Without it GA4 tends to file paid ChatGPT traffic under Paid Other or Referral [Practitioner consensus].

Session loss: compare GA4 sessions with Ads Manager clicks by platform. Some ad clicks reportedly open in an in-app view [Unverified] (independent research), and consent rejections, redirects and slow pages all reduce sessions. A session rate under 50% needs investigation.

## 9. Attribution and reporting semantics

| Setting | Values | Default | Label |
|---------|--------|---------|-------|
| Event setting `attribution_window_days` | 30 in docs examples (some docs say must be 30) | 30 | [Official, 2026-09] |
| Insights `attribution_window_days` (click) | 7, 14, 30 | 30 | [Official, 2026-09] |
| `view_through_attribution_window_days` | 0 or 1 | 1 in API; added to Ads Manager reports in October 2026 as an option | [Official, 2026-10] |
| `attribution_time_basis` | `ad_event_time` or `conversion_time` | `ad_event_time` | [Official, 2026-09] |
| Columns | `conversions` (click plus view, click wins when both), `click_through_conversions`, `view_through_conversions`, `cpa`, `post_click_cvr`, `order_created_attributed_sales`, `order_created_roas` | | [Official, 2026-09] |
| UI Conversions column | Standard and custom events combined into one total; no event level breakdown in the table | | [Official, 2026-09] |
| App events | Click-through only; no view-through | | [Official, 2026-09] |
| Modeled conversions | May be included in reported totals where available | | [Official, 2026-09] |
| Latency | Conversions 24 to 48 hours; impressions and clicks about 15 minutes; spend 7 to 8 hours | | [Official, 2026-09] |

Contested point: some community notes say `conversions` equals click-through only in practice [Contested]. Always request `click_through_conversions` explicitly and use it as the primary KPI. OpenAI says view-through in reports changes reporting, not optimization [Official, 2026-10]; an early OpenAI analysis found 52.7% of eligible 1-day view-through conversions occurred within an hour of the impression [Official, 2026-10] (read via secondary summary).

Why platform numbers differ from GA4 or backend [Official, 2026-09]: attribution windows, time zones and date boundaries, browser and consent conditions, dedup, configuration, modeled conversions. A difference is not automatically an error. Reconcile weekly on: backend orders with `utm_source=chatgpt` or stored oppref vs platform click-through conversions.

## 10. Apps and partners

- No OpenAI mobile SDK; app events go through CAPI, usually via an MMP [Official, 2026-09].
- MMPs documented in the Help Center: AppsFlyer and Adjust; October 2026 partner list also names Branch, Singular, Kochava, Airbridge, Tenjin [Official, 2026-09] and [Official, 2026-10] (read via secondary summary).
- Attribution for MMP integrations is click based; use the MMP click URL or attribution link as the ad destination [Official, 2026-09]. IDFA is not accepted; iOS matching relies on oppref and hashed identifiers [Unverified] (Linkrunner).
- Measurement and data partners (October 2026): Hightouch, Tealium, LiveRamp (send conversions from existing systems); Triple Whale, DV Rockerbox, Northbeam (attribution); Fospha, Measured, INCRMNTAL (full funnel); Haus, Measured, WorkMagic (geo incrementality, early); Kantar, Cint (brand, early) [Official, 2026-10] (read via secondary summary).
- Partner credentials: Pixel ID plus CAPI key, or a partner specific key (Fospha under Settings > API Keys; Triple Whale and WorkMagic under Settings > General) [Official, 2026-09].
- Shopify: OpenAI Pixel for Shopify connects eligible commerce events; the ChatGPT Ads Shopify app syncs catalog via Shopify Catalog [Official, 2026-09].
- Headless stores: pixel for browser events, CAPI for server events [Official, 2026-09].

## 11. Measurement QA checklist (launch gate)
- [ ] Pixel loads once per page, consent gated where required, CSP updated.
- [ ] Success events fire once on confirmed success; no events in `measure` carry user data.
- [ ] CAPI sends from server only; key in secret manager; never in client bundles or logs.
- [ ] Same event ID from pixel and CAPI; event names identical; custom names identical to event setting.
- [ ] `oppref` survives all redirects (synthetic test passed) and is passed to CAPI.
- [ ] `source_url` sanitized to origin plus path.
- [ ] Event settings created and attached to every campaign before launch.
- [ ] Recent events endpoint shows `pixel_sdk` and `server_to_server` entries.
- [ ] Paid UTMs on every ad; GA4 channel group live; organic `chatgpt.com` separated.
- [ ] Privacy policy discloses OpenAI pixel; CMP vendor list updated.
- [ ] MEASUREMENT.md row "ChatGPT Ads pixel / CAPI" updated with status and date.

The official OpenAI Codex plugin `openai-ads-conversions` (github.com/openai/plugins) includes static checks (`verify_ads_setup.py`, `verify_capi_secret_not_exposed.py`) that check for secret exposure, dedup, oppref and source URL handling; the measurement agent can adapt its checklist [Official, 2026-09].
