# Tools, APIs and MCP Servers

How the measurement agent reads data and inspects setups without a human in the loop for every query. Read access is fine; any write (publish, upload, settings change) needs explicit human approval.

## 1. Order of preference

1. MCP connectors the user has installed (official first, then reviewed community servers).
2. Official CLIs available in the environment (gcloud, bq).
3. Direct REST APIs with tokens the human provides through environment variables.
4. Exports dropped into `ads-master/data/imports/` (see HOW_TO_EXPORT.md).
5. Code inspection in the repository (tags, data layer, webhooks).

Always state which source and date range you used.

## 2. MCP servers

| Server | Publisher | What it does | Status and label |
|--------|-----------|--------------|------------------|
| Google Analytics MCP server (github.com/googleanalytics/google-analytics-mcp) | Google | Read-only GA4 access: account summaries, property details, Google Ads links, custom dimensions and metrics, run_report (Data API), run_realtime_report | Released 2025; runs locally (Python, for example via pipx) with Application Default Credentials and the analytics.readonly scope [Official, 2025; check repo for current tools] |
| Google Ads MCP server (github.com/googleads/google-ads-mcp) | Google | Read-only GAQL search and accessible customer listing | Released 2025 [Official, 2025; verify current tools] |
| MCP Toolbox for Databases (github.com/googleapis/genai-toolbox) | Google | Tools over BigQuery and other databases (list datasets, run SQL) | Open source [Official] |
| Google managed remote MCP servers (BigQuery and other Google Cloud services) | Google | Hosted MCP endpoints for Google Cloud products | Announced late 2025 [Unverified scope; check Google Cloud docs] |
| Shopify Dev MCP (@shopify/dev-mcp) | Shopify | Searches Shopify developer docs and API schemas (useful for Web Pixels and webhooks code) | [Official] |
| Community GTM MCP servers | Various (some from sGTM hosting vendors) | List and edit GTM containers via the GTM API | [Unverified]; review source code and require approval for any write |
| Community Meta Ads, TikTok, LinkedIn MCP servers | Various | Read ad insights, sometimes write | [Unverified]; prefer read-only tokens |

Security rules for MCP and API use:
- Read-only scopes by default (analytics.readonly, adwords read via GAQL only, ads_read for Meta).
- Never paste tokens into chat or files; use environment variables or the host's secret store.
- Review community server code, pin versions, and run them with least privilege credentials.
- Writes (GTM publish, conversion action edits, uploads) only after human approval, and log them in the journal.

## 3. Google APIs

| API | Use for measurement | Notes |
|-----|---------------------|-------|
| GA4 Data API (analyticsdata.googleapis.com) | Reports, realtime, funnel checks | Quotas per property (tokens per day and per hour) |
| GA4 Admin API (analyticsadmin.googleapis.com) | Audit settings: data streams, key events, custom dimensions, data retention, attribution settings, channel groups, Google Ads links, BigQuery links | Some resources only in v1alpha |
| Measurement Protocol | Server events into GA4 | See [Conversion APIs](platform-conversion-apis.md) |
| Tag Manager API v2 (tagmanager.googleapis.com) | Export containers, list tags, triggers, variables, versions; create workspaces and changes for review | Publishing needs approval |
| Google Ads API | Conversion actions, conversion stats by action, diagnostics (GAQL) | Offline uploads moved to Data Manager API from 2026-06-15 |
| Data Manager API (datamanager.googleapis.com) | Offline conversions, enhanced conversions for leads, events and audiences into Google Ads and other Google destinations | Primary for new server-to-server integrations [Official, 2026] |
| BigQuery (bq CLI, API) | GA4 export, marts, monitoring queries | Set cost controls (maximum bytes billed) |
| BigQuery Data Transfer Service for Google Ads | Google Ads data into BigQuery | Native |

### Snippets

```bash
# GA4 Data API: purchases by day (token from gcloud ADC with analytics.readonly scope)
curl -s -X POST \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  -H "Content-Type: application/json" \
  "https://analyticsdata.googleapis.com/v1beta/properties/${GA4_PROPERTY_ID}:runReport" \
  -d '{"dateRanges":[{"startDate":"28daysAgo","endDate":"yesterday"}],
       "dimensions":[{"name":"date"}],
       "metrics":[{"name":"ecommercePurchases"},{"name":"purchaseRevenue"}]}'

# GA4 Admin API: data retention setting
curl -s -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  "https://analyticsadmin.googleapis.com/v1beta/properties/${GA4_PROPERTY_ID}/dataRetentionSettings"

# GTM API: list tags in the default workspace (read-only review)
curl -s -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  "https://tagmanager.googleapis.com/tagmanager/v2/accounts/${GTM_ACCOUNT}/containers/${GTM_CONTAINER}/workspaces/${GTM_WORKSPACE}/tags"

# BigQuery with a cost guard
bq query --use_legacy_sql=false --maximum_bytes_billed=5000000000 \
  'SELECT event_name, COUNT(*) c FROM `project.analytics_123456.events_20261001` GROUP BY 1 ORDER BY c DESC LIMIT 20'
```

```sql
-- Google Ads (GAQL via MCP or API): conversion actions and their settings
SELECT conversion_action.name, conversion_action.status, conversion_action.type,
       conversion_action.primary_for_goal, conversion_action.category,
       conversion_action.counting_type, conversion_action.attribution_model_settings.attribution_model,
       conversion_action.click_through_lookback_window_days
FROM conversion_action
WHERE conversion_action.status = 'ENABLED'
```

```sql
-- Google Ads: conversions by action for the last 30 days
SELECT segments.conversion_action_name, metrics.all_conversions, metrics.conversions, metrics.conversions_value
FROM customer
WHERE segments.date DURING LAST_30_DAYS
```

## 4. Other platform APIs

| Platform | API | Measurement uses | Notes |
|----------|-----|------------------|-------|
| Meta | Marketing API (Insights), Conversions API, Events Manager diagnostics | Spend and conversions by attribution setting, CAPI sends | 7-day and 28-day view windows removed from Insights API on 2026-01-12; update queries |
| TikTok | Business API (reporting, Events API) | Spend, conversions, event sends | Versioned (v1.3 at time of writing) |
| LinkedIn | Marketing API (versioned by month header), Conversions API | Campaign analytics, conversions | Header LinkedIn-Version required |
| Microsoft Advertising | REST and SOAP APIs (SOAP retirement announced for 2027-01-31 per Microsoft) | Reporting, offline conversion upload | [Official per microsoft-ads research, 2026-09] |
| Pinterest | API v5 | Analytics, Conversions API | |
| Snap | Marketing API, Conversions API v3 | Stats, conversions | |
| Reddit | Ads API (v3 introduced; check deprecations) | Reporting, Conversions API | |
| OpenAI (ChatGPT Ads) | Ads API (community notes cite api.ads.openai.com/v1) and CAPI | Reporting, conversions | [Unverified, 2026] |
| Shopify | Admin GraphQL API, webhooks, Web Pixels API | Orders truth, pixel events | Use API versioning |
| HubSpot, Salesforce, Pipedrive | CRM APIs | Lead stages, click ID fill rates | Read-only tokens for audits |

## 5. Browser and debugging tools

| Tool | Use |
|------|-----|
| Google Tag Assistant (tagassistant.google.com) and GTM Preview | Tag firing, consent state, data layer |
| GA4 DebugView | Event and parameter validation |
| sGTM preview | Incoming requests, outgoing tags, responses |
| Meta Pixel Helper and Events Manager Test Events | Pixel and CAPI events, dedup status |
| TikTok Pixel Helper and Test Events | Same for TikTok |
| Microsoft UET Tag Helper | UET events |
| Pinterest Tag Helper, Snap Pixel Helper | Same |
| Omnibug or similar | Decodes many vendors' requests in one panel |
| Chrome DevTools Network and Application tabs | Requests, cookies, consent parameters (gcs, gcd), first-party serving |
| Safari Web Inspector | ITP effects, cookie expiry on iOS and macOS |

## 6. Automated checks the agent can run

| Check | Tool | Frequency |
|-------|------|-----------|
| Purchases vs backend | BigQuery or GA4 Data API plus backend export | Daily |
| GA4 settings drift (retention, key events, channel groups) | GA4 Admin API | Monthly |
| GTM container diff since last audit | GTM API export and diff | On every publish or monthly |
| Conversion action changes in Google Ads | GAQL | Weekly |
| Meta EMQ and dedup | Events Manager (manual) or API diagnostics where available | Weekly |
| Upload logs | Data Manager history, own logs | Daily |
| Click ID fill rate | CRM API | Weekly |

Save raw pulls to `ads-master/data/imports/YYYY-MM-DD_<source>_<what>.csv` when they support a deliverable, so other agents can reuse them.
