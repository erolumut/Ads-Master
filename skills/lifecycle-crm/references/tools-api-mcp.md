# Tools, APIs and MCP Servers

The ESP landscape in October 2026, how to choose, how Claude reads data and drafts work through APIs and MCP servers, and how each tool action maps to the Ads Master gates. Verify features and plan gating on the vendor's site before recommending; vendor claims are labeled.

## 1. ESP and messaging landscape

| Tool | Best fit | Channels | 2025 to 2026 changes | AI and agents |
|------|----------|----------|----------------------|---------------|
| Klaviyo | Shopify and DTC ecommerce, Starter to Enterprise B2C | Email, SMS, MMS, RCS (12 markets listed), WhatsApp (non US), push, reviews, forms, Customer Hub | WhatsApp launch (about 2025-10); Conversations API for SMS and WhatsApp (API revision 2026-04-15); custom objects (2025-07 and 2026-07); Flow Actions API (2025-10); billing on active profiles [Official, Klaviyo API changelog; secondary pricing 2026] | Composer (2026-03-24, public beta 2026-06-30) builds campaigns, flows, segments with human approval; Customer Agent across chat, email, SMS, WhatsApp in 100+ languages; K:BOS 2026-09 previewed SQL over account data via Composer and MCP; Klaviyo says it exposes 260+ MCP tools and 490+ APIs [Official newsroom 2026; K:BOS details via secondary] |
| Braze | Enterprise B2C, apps, multi market | Email, push, in-app, SMS, RCS, WhatsApp, content cards, web | OfferFit acquisition completed 2025-06, now BrazeAI Decisioning Studio [Official, Braze] | Decisioning Studio Go (self-serve agents; GA 2026-10-14), Agentic Standards (campaign QA), Operator Connect on the Braze MCP server (OAuth, user permissions), Conversational Agents beta (WhatsApp, SMS, RCS, web) [Official, Braze 2026-09-29] |
| Customer.io | SaaS, PLG, data rich B2C | Email, push, in-app, SMS, WhatsApp and LINE (2026-04) | Agent, LLM actions and goals in beta (spring 2026); MCP v2 (2026-05-04); CLI; Slack agent (2026-08) [Official, Customer.io 2026] | Agent builds and reviews campaigns |
| Iterable | Mid market and enterprise B2C | Email, push, in-app, SMS, RCS (2026-09), WhatsApp (2026-09) | Fall release 2026-09-24 with Integrations Hub, native Salesforce sync [Official, Iterable] | Nova Agent (2026-04-22), Monitoring and Analytics agents, Nova Conversations private beta 2026-10 [Official, Iterable] |
| Mailchimp (Intuit) | SMB, Starter tier | Email, SMS, some social | Marketing Automation Flows (renamed 2025-06); SMS age gating [Official, Intuit 2026-05-28] | Analytics AI (2026-05-28); integrations with Claude, Wix, WooCommerce; AI Segment Builder beta [Official, Intuit] |
| Omnisend | SMB ecommerce (Shopify, WooCommerce) | Email, SMS, push | SMS from $0.007 per message on the Pro plan (2026-05); Forms API beta; send time optimization (2026-08) [Official, Omnisend changelog] | Reports AI (all paid users 2026-08); MCP integration (2026-05, write actions for SMS campaigns, A/B tests and automations from 2026-07) [Official, Omnisend] |
| Attentive | Enterprise SMS and email | SMS, MMS, RCS, email | Visibility AI for RCS and SMS to RCS auto upgrade (2026-05-20); Thread 2026: Brand Voice 2.0, Reporting Agent, predictive analytics [Official, Attentive 2026-05] | Vendor reported RCS lifts [Unverified] |
| Postscript | Shopify SMS | SMS, RCS features | Campaigns 2.0 with message level attribution (reported 2026-02); Q2 2026 release notes [Secondary, 2026] | Shopper AI sales agent in SMS threads [Official, Postscript] |
| HubSpot | B2B and lead gen | Email, SMS (add on), WhatsApp (via integrations), CRM | Lead Scoring tool replaced the legacy HubSpot Score (retired 2025-08-31) [Official, 2025] | Breeze agents; remote MCP server GA 2026-04-13 [Secondary, 2026] |
| Others to know | Bloomreach, Insider (strong in Turkey and MENA), Brevo, MoEngage, CleverTap, OneSignal, Airship, Salesforce Marketing Cloud, Adobe Journey Optimizer | | | |

Subscription, loyalty and reviews tools: see [Replenishment and subscriptions](replenishment-and-subscriptions.md) section 4 and [Loyalty, referral and reviews](loyalty-referral-and-reviews.md) section 4.

## 2. Choosing an ESP

| Situation | Default pick | Why |
|-----------|-------------|-----|
| Shopify DTC, under about 50k profiles, small team | Klaviyo or Omnisend | Native Shopify data, prebuilt flows, reasonable cost |
| Shopify DTC, US SMS heavy | Klaviyo SMS, or Postscript or Attentive alongside the ESP | SMS specialists for conversational and enterprise needs |
| Multi channel app plus web, millions of users | Braze or Iterable | Push, in-app, real time, data scale |
| SaaS and PLG with product events | Customer.io (or Braze) | Event driven journeys, data pipelines |
| B2B lead gen with sales team | HubSpot or Salesforce | CRM, scoring, sales handoff |
| Turkey or MENA market leader | Insider, Bloomreach or Klaviyo with an İYS integration | Local channels, WhatsApp, İYS integrations; verify İYS integrator status |
| Tiny list, tight budget | Mailchimp, Omnisend, Brevo | Cost |

Evaluation checklist: ecommerce or product event depth; catalog and recommendation features; consent model per channel and jurisdiction; İYS or other registry integration; holdout and control group support; reporting API and rate limits; MCP or API for agent access with read only scopes; data residency; pricing model (profiles, active profiles, sends, messages); migration support.

## 3. MCP servers and agent access (verify current docs before connecting)

| Server | Endpoint and auth | Scope notes | Safe default for Ads Master |
|--------|------------------|-------------|------------------------------|
| Klaviyo MCP (remote, recommended) | `https://mcp.klaviyo.com/mcp` (no trailing slash), OAuth; Owner, Admin or Manager role required; add `?core-tools-only=true` to limit to about 40 core tools | Campaigns, flows, profiles, reporting, catalogs, events; a local server option also exists [Official, Klaviyo developer docs 2026] | Use for reporting and drafting; treat any create, update or send tool as G2 or G3 per section 5 |
| Braze MCP server (Operator Connect) | Single URL, OAuth with dashboard login; agents inherit the user's Braze permissions; the 2025 version is deprecated [Official, Braze 2026-09] | | Connect with a read focused user role |
| Customer.io MCP v2 | Remote; exposes Journeys UI API and CDP Data Pipelines API; admins can disable AI and MCP; actions limited by user role [Official, Customer.io 2026-05] | Can perform writes | Use a role without send permissions |
| Iterable MCP (`@iterable/mcp`, open source) | API key stored locally (Keychain on macOS); setup defaults to read only with no PII tools, no writes, no sends; optional flags enable PII, writes and sends separately [Official, Iterable GitHub v1.9.0] | Note: creating a blast campaign schedules it (no draft campaigns in the API) | Keep PII, writes and sends disabled; draft in templates |
| HubSpot remote MCP | `mcp.hubspot.com`, OAuth 2.1 with PKCE via an MCP auth app, respects user permissions; read and write on CRM objects [Secondary, 2026-04] | | Read only usage unless a change request is approved |
| Omnisend MCP | Account connection; write actions for SMS campaigns, email A/B campaigns and automations since 2026-07 [Official, Omnisend changelog] | | Same gate mapping |
| Mailchimp | Integration with Claude announced 2026-05-28 [Official, Intuit] | | Verify scopes |

Rules for every connector: read only scopes first; never paste API keys into files, prompts, outputs or memory (environment variables or the client's secret store only); confirm the account (brand and region) before any action; the guard hook treats unknown write tools as G3.

## 4. Klaviyo API essentials (revision 2026-07-15)

- Base URL `https://a.klaviyo.com/api/`; headers `Authorization: Klaviyo-API-Key <private key>`, `revision: 2026-07-15`, `accept: application/vnd.api+json` [Official, Klaviyo OpenAPI spec].
- Create a private key with read only scopes for analysis (for example `flows:read`, `campaigns:read`, `segments:read`, `metrics:read`, `profiles:read` only if needed).
- Recent additions: Conversations API (SMS and WhatsApp messages, 2026-04-15; plural endpoints from 2026-07-15), custom objects CRUD (2026-07-15), event `backfill` flag that records historical events without triggering flows (2026-07-15), Flow Actions API with update and delete (2025-10 and 2026-07), Forms API, mapped metrics, web feeds and universal content, push tokens, reviews [Official, klaviyo-api-python CHANGELOG].

Rate limits from the OpenAPI spec (revision 2026-07-15):

| Endpoint | Scope | Burst | Steady | Daily |
|----------|-------|-------|--------|-------|
| POST /api/flow-values-reports, /api/flow-series-reports | flows:read | 1/s | 2/m | 225/d |
| POST /api/campaign-values-reports | campaigns:read | 1/s | 2/m | 225/d |
| POST /api/segment-values-reports, /api/form-values-reports | segments:read, forms:read | 1/s | 2/m | 225/d |
| POST /api/metric-aggregates | metrics:read | 3/s | 60/m | |
| GET /api/flows, /api/flows/{id}, /api/flow-actions/{id} | flows:read | 3/s | 60/m | |
| GET /api/campaigns | campaigns:read | 10/s | 150/m | |
| GET /api/segments | segments:read | 75/s | 750/m | |
| POST /api/segments (create) | segments:write | 1/s | 15/m | 100/d |
| POST /api/flows (create) | flows:write | 1/s | 15/m | 100/d |
| GET /api/events | events:read | 350/s | 3500/m | |
| POST /api/campaign-send-jobs (send) | campaigns:write | 10/s | 150/m | |
| POST /api/conversation-messages (send SMS or WhatsApp) | conversations:write | 3/s | 60/m | |
| POST /api/profile-subscription-bulk-create-jobs | lists, profiles, subscriptions write | 75/s | 750/m | |
| POST /api/data-privacy-deletion-jobs | data-privacy:write | 3/s | 60/m | |

Reporting API statistics include `recipients`, `delivered`, `clicks_unique`, `click_rate`, `conversion_uniques`, `conversion_value`, `conversion_rate`, `revenue_per_recipient`, `unsubscribe_rate`, `spam_complaint_rate`, `bounce_rate`, `text_message_spend` and `text_message_roi`; rate statistics are fractions; timeframe keys include `last_7_days`, `last_30_days`, `last_90_days`, `last_365_days` or a custom start and end (max 1 year); `conversion_metric_id` is required (the Placed Order metric ID) [Official, OpenAPI spec].

Example (read only; key from an environment variable, never written to disk):
```bash
curl -s https://a.klaviyo.com/api/flow-values-reports \
  -H "Authorization: Klaviyo-API-Key $KLAVIYO_PRIVATE_KEY" \
  -H "revision: 2026-07-15" -H "accept: application/vnd.api+json" -H "content-type: application/vnd.api+json" \
  -d '{"data":{"type":"flow-values-report","attributes":{
        "statistics":["recipients","clicks_unique","conversion_uniques","conversion_value","revenue_per_recipient","unsubscribe_rate","spam_complaint_rate"],
        "timeframe":{"key":"last_90_days"},
        "conversion_metric_id":"<PLACED_ORDER_METRIC_ID>",
        "group_by":["flow_id","flow_name","flow_message_id","send_channel"]}}}'
```
Find the Placed Order metric ID with `GET /api/metrics`. Because reporting endpoints allow only 2 requests per minute and 225 per day, pull all needed statistics in one request and cache results in `ads-master/data/imports/` as aggregated CSV.

## 5. Gate mapping for lifecycle actions

| Action | Gate | Notes |
|--------|------|------|
| Read reports, flows, segments, metrics, deliverability dashboards | G0 | Aggregates by default |
| Pull profile level data (emails, phones) | G0 but needs a task reason and approver agreement | Avoid; use aggregates |
| Write flow specs, copy, segment definitions, templates as files | G1 | |
| Create a flow, template or campaign in the ESP as Draft or Manual, unscheduled | G2 | Stage 2+; confirm with human per guardrails.json |
| Create or edit a segment definition (no send) | G2 | Segments used by live flows behave like live changes: G3 |
| Set a flow or message Live, schedule or send a campaign, trigger a send via API or MCP | G3 | Change request with approver from GUARDRAILS.md |
| Import or bulk subscribe profiles, change consent or suppression, upload audiences to ad platforms | G3 | Consent evidence required |
| Change discount codes, loyalty rewards or subscription prices | G3 | With offer-strategy |
| Delete flows, lists, profiles or data; change account owners or billing | G4 | Never by an agent (deletion requests for privacy compliance are executed by the human) |

Rollback notes: setting a Klaviyo flow back to Manual or Draft stops new sends, but queued messages may still send unless cancelled; a scheduled campaign can be cancelled before send; a sent message cannot be recalled. Write rollback steps into every change request.

## 6. Data exports without API access

| Data | Where | Range |
|------|-------|-------|
| Flow performance by message | Klaviyo Analytics or flow report export; Braze Canvas analytics; Iterable journey analytics | Last 90 days |
| Campaign performance | ESP campaign report export | Last 90 days |
| List growth and form performance | Signup forms analytics, list growth report | Last 90 days |
| Deliverability | ESP deliverability report; Google Postmaster Tools v2 export; Yahoo Sender Hub | Last 90 days |
| Orders for cohorts | Shopify Analytics or Admin order export; warehouse | Last 24 months |
| Subscription events | Recharge, Skio, Loop exports | Last 12 months |
| SMS costs | ESP billing and carrier fee lines | Last 3 months |

File naming: `ads-master/data/imports/YYYY-MM-DD_<source>_<what>.csv`. State source and date range in every deliverable.

## 7. Other useful APIs

| API | Use |
|-----|-----|
| Google Postmaster Tools API v2 | Compliance status, spam rate, delivery errors by domain (Domain and IP reputation not in v2) [Official, Google] |
| Google Data Manager API | Customer Match and conversion data ingestion (measurement and channel agents) |
| Meta Marketing API custom audiences | Customer list sync (channel agents) |
| İYS API | Consent upload, refusal sync and status checks for Turkey (via the brand's İYS account or an authorized integrator) [Official, iys.org.tr] |
| Shopify Admin GraphQL | Customers, orders, consent fields (email and SMS marketing consent states) |
| Recharge API | Subscription events and churn reasons |
