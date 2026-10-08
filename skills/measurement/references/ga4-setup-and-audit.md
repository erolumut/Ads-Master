# GA4 Setup and Audit

GA4 is the cross-channel ruler, the source of Google Ads audiences and often a conversion source for Google Ads. It is not the revenue source of truth. This module covers the settings that matter, event design, limits, consent effects, BigQuery export, the 2025 to 2026 changes and the misconfigurations that cost the most.

## 1. Property architecture

| Situation | Structure |
|-----------|-----------|
| One brand, one site | One property, one web data stream |
| Site plus app | One property, web stream plus iOS and Android streams (Firebase) |
| Several country domains, same brand | One property, one web stream, cross-domain configured; filter by hostname or country |
| Separate brands or legal entities | Separate properties; 360 roll-up property if needed |
| Staging and dev | Separate property or a debug filter; never pollute production |

Keep one Google tag (G-XXXX) per site. If Google Ads, GA4 and Floodlight are on the same site, either one Google tag with several destinations or GTM with one Google tag plus event tags. Never load GA4 twice (gtag in theme plus GTM).

## 2. Admin settings checklist (exact names)

| Setting | Path | Recommended | Why |
|---------|------|-------------|-----|
| Event data retention | Admin > Data collection and modification > Data retention | 14 months (standard); up to 50 months on 360 | Default is 2 months, which limits explorations [Official] |
| Reset user data on new activity | Same page | On | Keeps active users' data |
| Google signals | Admin > Data collection and modification > Data collection | On only if consent covers it; it powers cross-device remarketing | Consent and thresholding implications |
| Granular location and device data | Same page | On unless legal requires off per region | Needed for geo tests and device analysis |
| User-provided data collection | Same page | On when you send hashed user data (enhanced conversions via GA4) | Improves matching with Google Ads |
| Data filters | Admin > Data collection and modification > Data filters | Internal traffic Active, Developer traffic Active | Filters in "Testing" state do not exclude data |
| Define internal traffic | Admin > Data streams > stream > Configure tag settings > Define internal traffic | Office and VPN IPs | Cleaner data |
| List unwanted referrals | Configure tag settings > List unwanted referrals | Payment providers (paypal.com, stripe.com, checkout.stripe.com, klarna.com, adyen.com, mollie.com, iyzico.com, payu, 3D Secure domains), SSO domains | Stops self-referrals stealing purchase credit |
| Configure your domains | Configure tag settings > Configure your domains | Every domain in the journey (site, checkout, booking tool) | Cross-domain linker (_gl parameter) |
| Adjust session timeout | Configure tag settings > Adjust session timeout | 30 minutes default; engaged session timer 10 seconds default (max 60) | Change only with a reason |
| Enhanced measurement | Data streams > stream > Enhanced measurement | Page views (with "Page changes based on browser history events" for SPAs), scrolls, outbound clicks, site search, video, file downloads; consider turning off Form interactions | Form interactions creates noisy form_start and form_submit |
| Reporting identity | Admin > Data display > Reporting identity | Blended if consent mode modeling is eligible, else Observed; Device-based to minimize thresholding | Modeling fills consent gaps |
| Attribution settings | Admin > Data display > Attribution settings | Data-driven; lookback 30 days acquisition key events, 90 days other key events | Match Google Ads windows where possible |
| Channel groups | Admin > Data display > Channel groups | Default plus one custom group with an AI assistants channel and paid platform splits | See [UTM and channels](utm-and-channel-governance.md) |
| Key events | Admin > Data display > Key events | Only business outcomes and documented proxies; counting method "Once per event" for purchase, "Once per session" for leads if duplicates are common | Clean Google Ads import |
| Currency and time zone | Admin > Property details | Match backend reporting currency and timezone | Reconciliation |
| Google Ads links | Admin > Product links > Google Ads links | Linked, personalized advertising on, auto-tagging on in Google Ads | Imports and audiences |
| BigQuery links | Admin > Product links > BigQuery links | Daily export on at Growth tier and above; streaming if near real time is needed | Raw data, no retention limit |
| Search Console links | Admin > Product links > Search Console links | Linked | SEO handoff |
| Consent settings | Admin > Data streams > stream > Consent settings | Confirms consent signals for ads measurement and personalization are received | EEA compliance diagnostics |

## 3. Event design

### Ecommerce recommended events (use exact names)

| Event | Required parameters | Notes |
|-------|--------------------|-------|
| view_item_list | items[], item_list_id or item_list_name | Category and search result pages |
| select_item | items[] | Click from list |
| view_item | currency, value, items[] | Product detail page |
| add_to_cart | currency, value, items[] | Fire on success, not on button click |
| remove_from_cart | currency, value, items[] | |
| view_cart | currency, value, items[] | |
| begin_checkout | currency, value, items[], coupon | |
| add_shipping_info | currency, value, items[], shipping_tier | |
| add_payment_info | currency, value, items[], payment_type | |
| purchase | transaction_id, currency, value, items[], tax, shipping, coupon | value excludes tax and shipping by convention; be consistent with backend |
| refund | transaction_id, currency, value, items[] (partial) | Send from server via Measurement Protocol when refunds happen |

Item fields: item_id (SKU, same as feed ID), item_name, item_brand, item_category to item_category5, item_variant, price, quantity, discount, coupon, index, item_list_name. Use the same item_id as the Merchant Center and Meta catalog ID so reports join.

### Lead gen recommended events

generate_lead (form or call), qualify_lead, disqualify_lead, working_lead, close_convert_lead, close_unconvert_lead [Official, 2024]. Send the later stages from the server or CRM via Measurement Protocol with the client_id or user_id captured at lead time, or use offline imports in Google Ads directly (preferred for bidding, see [Offline and CRM](offline-and-crm-conversions.md)).

### Other common events

sign_up (method), login, search (search_term), share, generate_lead, begin_trial (custom), subscribe (custom), file_download (enhanced measurement), form_submit (custom, only on success).

### Naming rules

- snake_case, under 40 characters, start with a letter, no reserved prefixes (google_, ga_, firebase_), no reserved names (session_start, first_visit, user_engagement and others).
- Prefer recommended event names; Google products understand them.
- Put variation in parameters (form_name, lead_type) instead of creating new event names.

## 4. Limits (standard properties)

Verify on the "Configuration limits" help page before a big build [Official, long standing values; check for changes]:

| Item | Limit |
|------|-------|
| Distinct event names per app stream | 500 (web streams not capped the same way, but keep the list small) |
| Event name length | 40 characters |
| Parameters per event | 25 |
| Parameter name length | 40 characters |
| Parameter value length | 100 characters (page_location 1,000, page_title 300, page_referrer 420) |
| User properties | 25 |
| Event-scoped custom dimensions | 50 |
| User-scoped custom dimensions | 25 |
| Item-scoped custom dimensions | 10 |
| Custom metrics | 50 |
| Key events | 30 (360: 50) |
| Items per event | 200 |
| Audiences | 100 |
| Event data retention | 2 or 14 months (360 up to 50 months) |
| BigQuery daily export | 1 million events per day for standard properties (streaming not capped the same way, billed by volume) |
| Measurement Protocol | Up to 25 events per request; timestamps up to 72 hours in the past |

## 5. Consent mode effects in GA4

| Consent state | What GA4 receives | Reports |
|---------------|-------------------|---------|
| analytics_storage granted | Full events with cookies | Observed |
| analytics_storage denied, advanced mode | Cookieless pings without client ID | Modeled into reports if eligible for behavioral modeling (Blended identity) |
| analytics_storage denied, basic mode | Nothing (tags blocked until consent) | Gap; no advertiser specific modeling |

Behavioral modeling eligibility [Official, long standing; verify]: at least 1,000 events per day with analytics_storage denied for at least 7 days, and at least 1,000 daily users with analytics_storage granted for at least 7 of the previous 28 days. Below that, no modeling: the EEA gap stays visible.

Diagnose consent impact in BigQuery with `privacy_info.analytics_storage` and `privacy_info.ads_storage` (values Yes, No, null). Report capture rate by region separately; an EEA capture rate of 50% to 80% of backend can be normal under opt-in law [Practitioner consensus, varies with banner design and audience].

## 6. BigQuery export

Setup: Admin > Product links > BigQuery links > Link, choose project, data location (cannot change later), Daily and or Streaming, include advertising identifiers for mobile if needed. Set a budget alert in Google Cloud.

Tables: `events_YYYYMMDD` (daily), `events_intraday_YYYYMMDD` (streaming), `pseudonymous_users_*` and `users_*` (user data export).

Traffic source fields:
- `traffic_source.*`: first user acquisition source (not the session source).
- `collected_traffic_source.*`: UTMs and click IDs collected on the event (manual_source, manual_medium, manual_campaign_name, gclid, dclid, srsltid).
- `session_traffic_source_last_click.*`: session-level last click attribution including Google Ads campaign details (added mid 2024) [Official]. Use it for session channel reporting instead of rebuilding sessionization yourself.

### Query: purchases vs backend, duplicates and missing IDs

```sql
-- GA4 purchases by day with duplicate and missing transaction_id checks
WITH p AS (
  SELECT
    PARSE_DATE('%Y%m%d', event_date) AS d,
    ecommerce.transaction_id AS tid,
    ecommerce.purchase_revenue AS rev
  FROM `project.analytics_123456.events_*`
  WHERE event_name = 'purchase'
    AND _TABLE_SUFFIX BETWEEN '20260901' AND '20260930'
)
SELECT
  d,
  COUNT(*) AS purchase_events,
  COUNT(DISTINCT tid) AS unique_transactions,
  COUNTIF(tid IS NULL OR tid = '' OR tid = '(not set)') AS missing_tid,
  COUNT(*)-COUNT(DISTINCT tid) AS duplicate_events,
  ROUND(SUM(rev), 2) AS revenue
FROM p
GROUP BY d
ORDER BY d;
```

Join to a backend orders table (loaded daily from Shopify, Stripe or ERP) on transaction_id to compute capture rate and find which orders are missing, then group missing orders by payment method, device, country and landing page to find the cause.

```sql
-- Capture rate and missing orders by payment method
SELECT
  o.payment_method,
  COUNT(*) AS backend_orders,
  COUNTIF(g.tid IS NOT NULL) AS in_ga4,
  ROUND(COUNTIF(g.tid IS NOT NULL)/COUNT(*), 3) AS capture_rate
FROM `project.backend.orders` o
LEFT JOIN (
  SELECT DISTINCT ecommerce.transaction_id AS tid
  FROM `project.analytics_123456.events_*`
  WHERE event_name = 'purchase' AND _TABLE_SUFFIX BETWEEN '20260901' AND '20261005'
) g ON g.tid = o.order_id
WHERE DATE(o.created_at, 'Europe/Istanbul') BETWEEN '2026-09-01' AND '2026-09-30'
  AND o.is_test = FALSE
GROUP BY 1
ORDER BY backend_orders DESC;
```

### Query: consent share by country

```sql
SELECT
  geo.country,
  COUNTIF(privacy_info.analytics_storage = 'No') AS denied_events,
  COUNTIF(privacy_info.analytics_storage = 'Yes') AS granted_events,
  ROUND(COUNTIF(privacy_info.analytics_storage = 'Yes')/COUNT(*), 3) AS granted_share
FROM `project.analytics_123456.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20260901' AND '20260930'
  AND event_name = 'page_view'
GROUP BY 1
HAVING COUNT(*) > 1000
ORDER BY granted_share;
```

### Query: sessions by session last click source

```sql
SELECT
  session_traffic_source_last_click.manual_campaign.source AS source,
  session_traffic_source_last_click.manual_campaign.medium AS medium,
  COUNT(DISTINCT CONCAT(user_pseudo_id, CAST((SELECT value.int_value FROM UNNEST(event_params) WHERE key = 'ga_session_id') AS STRING))) AS sessions
FROM `project.analytics_123456.events_*`
WHERE _TABLE_SUFFIX BETWEEN '20260901' AND '20260930'
  AND event_name = 'session_start'
GROUP BY 1, 2
ORDER BY sessions DESC
LIMIT 50;
```

Field names inside session_traffic_source_last_click have evolved; check the BigQuery export schema page before relying on this query.

## 7. GA4 changes, January 2025 to October 2026

Assembled from Google's What's new, Announcements, Tag Manager release notes and Measurement Protocol changelog, mostly via search extracts [Official unless marked]:

| Date | Change | Impact |
|------|--------|--------|
| 2025 (early) | Annotations in reports | Annotate tracking breaks and attribution changes in the UI |
| 2025-03-19 | First-party mode via Cloudflare (beta) in Tag Manager, renamed Google tag gateway for advertisers in May 2025 | First-party serving of Google tags |
| 2025 (GML, May) | Cross-channel reporting, cost data import from Meta, TikTok, Snap, Reddit and Pinterest; impression inclusive multi-touch attribution previewed | Cross-channel ROAS inside GA4 |
| 2025-05 to 2025-06 | Measurement Protocol: EU collection and validation endpoints, geographic fields, device and user_agent fields | Better server-side events, EU data residency path |
| 2025-06-30 | Tag Manager: scripts served through the web container | Container serving change |
| 2025-08-01 | GTM custom template API readAnalyticsStorage (client and session IDs) | sGTM and templates can read IDs |
| 2025-09 | Campaign Manager 360 splits Floodlight into web and app streams for new GA properties | Floodlight users |
| 2025 | Analytics Advisor (Gemini based assistant in GA4) | Natural language analysis |
| 2025-12-11 | GTM built-in variables Client ID, Session ID, Session Number; MP accepts in_app_purchase for app streams | Easier MP and sGTM stitching |
| 2025 | Google states Measurement Protocol stays supported but recommends the Data Manager API for new server-to-server integrations | Plan new server pipelines on Data Manager where it covers the use case |
| 2026-01-16 | Cross-channel budgeting announced; attribution settings adjustable per conversion; Conversion attribution analysis report (beta) | Planning inside GA4 |
| 2026-02-10 | Cross-channel budgeting (beta) | |
| 2026-04-29 | Task Assistant with configuration recommendations [secondary source mirroring Google notes] | Use as a free audit aid |
| 2026-05-13 | AI Assistant channel in the Default Channel Group (medium ai-assistant, campaign (ai-assistant)); not retroactive; rollout reported broad by 2026-06-07 | See [UTM and channels](utm-and-channel-governance.md) |
| 2026-09-09 | Dashboards (drag and drop KPI views) | Lightweight reporting inside GA4 |
| 2026-09-29 | Improved app conversion management and cross-channel reporting for Google Ads customers | App advertisers |
| 2026 | Cross-channel conversion reporting data in the Data API (alpha) | API access to cross-channel numbers |

## 8. The 25 most expensive misconfigurations

| # | Misconfiguration | Detect | Fix |
|---|------------------|--------|-----|
| 1 | GA4 loaded twice (theme gtag plus GTM) | Network tab shows two collect hits per page_view | Remove one |
| 2 | Purchase fires again on thank you page reload or revisit | Duplicate transaction_id in BigQuery | Guard with order-tracked flag (cookie, localStorage, or server rendered once) |
| 3 | No transaction_id | missing_tid in query above | Pass order ID |
| 4 | Missing currency | Revenue zero or wrong | Always send ISO currency |
| 5 | Payment gateway self-referrals | Referral report shows paypal.com etc. | List unwanted referrals |
| 6 | Cross-domain not configured | Sessions break at checkout or booking domain | Configure your domains; check _gl on links and forms |
| 7 | Data retention left at 2 months | Admin | Set 14 months |
| 8 | Internal traffic filter in Testing | Admin > Data filters | Activate |
| 9 | Key events include page_view or scroll | Admin key events | Remove |
| 10 | GA4 purchase imported into Google Ads as primary alongside the Google Ads purchase tag | Google Ads conversion actions | Keep one primary |
| 11 | SPA counts double page views or none | DebugView on route change | Choose history-based enhanced measurement or manual page_view, not both |
| 12 | Measurement Protocol events without client_id or session_id | Unassigned spikes, sessions with no source | Capture client_id (_ga cookie) and session_id at order time, send both |
| 13 | UTMs on internal links (banners, menus) | Self-attributed sessions | Remove; use internal promotion events |
| 14 | utm_medium values outside channel rules (for example "facebook_paid") | Unassigned or Paid Other | Fix taxonomy |
| 15 | PII in page_location (email in query string) | BigQuery search for @ in page_location | Redact at source, configure data redaction, fix forms (GET to POST) |
| 16 | Wrong timezone or currency vs backend | Daily mismatch patterns | Align |
| 17 | Enhanced measurement form interactions on | Noisy form_submit counts | Turn off; track success events |
| 18 | Consent default fires after GA4 config | Tag Assistant consent tab | Consent Initialization trigger, default first |
| 19 | Google signals on without consent basis | Admin | Turn off or gate |
| 20 | items[] item_id not matching feed IDs | Item reports do not join | Use feed ID |
| 21 | Revenue includes tax and shipping in GA4 but not in Google Ads | Value mismatch | One convention everywhere |
| 22 | Debug traffic in production | debug_mode params in BigQuery | Remove debug flags |
| 23 | Thresholding hides data | Orange warning icon | Device-based identity for analysis, or BigQuery |
| 24 | Audiences rely on events that no longer fire | Audience size dropping | Audit audiences after event changes |
| 25 | No BigQuery export at Growth tier | Admin | Link now (no backfill exists) |

## 9. GA4 audit procedure (90 minutes)

1. Admin sweep with section 2 table; screenshot or export each setting.
2. DebugView and Tag Assistant: walk the main funnel on desktop and mobile, with consent accepted and with consent denied. Record every event and parameter.
3. Reports: Traffic acquisition (session default channel group) last 28 days; note Unassigned, Direct and Referral shares and top referral domains.
4. Key events report vs backend for the same period and timezone.
5. BigQuery queries (section 6) if export exists.
6. Google Ads link and imported conversions check.
7. Score with [Audit checklist](audit-checklist.md) GA4 section.

## 10. GA4 Data API for agents

When the official Google Analytics MCP server is connected (see [Tools, APIs and MCP](tools-api-mcp.md)), use `run_report` with dimensions and metrics such as:

| Need | Dimensions | Metrics |
|------|-----------|---------|
| Channel mix | sessionDefaultChannelGroup | sessions, keyEvents, totalRevenue |
| Source and medium | sessionSource, sessionMedium | sessions, engagedSessions, keyEvents |
| AI assistant traffic | sessionDefaultChannelGroup (filter AI Assistant) or sessionSource regex | sessions, keyEvents |
| Landing pages | landingPagePlusQueryString | sessions, keyEvents, bounceRate |
| Purchases by day | date | ecommercePurchases, purchaseRevenue, transactions |

Data API quotas apply per property (tokens per day and per hour); keep requests small and cache results in `ads-master/data/imports/`.
