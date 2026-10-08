# Tools, API and MCP Servers

> Knowledge as of 2026-10. Official API facts come from developers.openai.com/ads (read via mirrors of the docs index and pages, 2026-09). Community tools are listed with their own claims; review code before installing. The API changed without version bumps during 2026 (community notes report spec 2.3.0 content changing in place) [Unverified]. Always read the live reference before running scripts.

## 1. Official surfaces

| Tool | What it does | Access | Label |
|------|-------------|--------|-------|
| Ads Manager (ads.openai.com) | Campaign creation, bulk upload and bulk edit, billing, users, API keys, conversions, feeds, reporting with table, charts and CSV (cumulative or daily) | Web | [Official, 2026-09] |
| Advertiser API | Programmatic campaigns, ad groups, ads, files, insights, conversions setup, audiences, feeds, audit logs | `https://api.ads.openai.com/v1`, Bearer API key scoped to one ad account | [Official, 2026-09] |
| Conversions API | Server to server events | `https://bzr.openai.com/v1/events?pid=<pixel_id>`, Bearer CAPI key | [Official, 2026-09] |
| Developer docs index | 33 pages incl. quickstart, campaign management, targeting, bidding, reporting, product feeds, delta feeds, hotel feeds, bulk API, troubleshooting, supported events | `https://developers.openai.com/ads/llms.txt` and `llms-full.txt` | [Official, 2026-09] |
| ChatGPT Ads Manager plugin (in ChatGPT) | Create, update and analyze campaigns with prompts; turn a website or brief into a campaign; recommend next steps | ChatGPT; openai.com/business/plugins/chatgpt-ads-manager/ | [Official, 2026-09] |
| `openai-ads-conversions` plugin (Codex) | Official skill to add or review pixel and CAPI in a codebase, with static verification scripts | github.com/openai/plugins | [Official, 2026-09] |
| HubSpot integration | Create ChatGPT Chat Card campaigns, follow up on leads, report contacts and customers next to other ad channels | HubSpot Marketing Hub | [Official, 2026-09] |
| Shopify ChatGPT Ads app | Create and manage campaigns, sync products via Shopify Catalog | Shopify App Store (US 2026-09-16, international 2026-09-23) | [Official, 2026-09] |
| OpenAI Pixel for Shopify | Sends eligible Shopify commerce events to Ads Manager | Shopify | [Official, 2026-09] |
| MMP and measurement partner integrations | AppsFlyer, Adjust (Help Center); Branch, Singular, Kochava, Airbridge, Tenjin; Hightouch, Tealium, LiveRamp; Triple Whale, DV Rockerbox, Northbeam; Fospha, Measured, INCRMNTAL; Haus, WorkMagic; Kantar, Cint | Partner platforms | [Official, 2026-09] and [Official, 2026-10] (secondary summary) |

There is no official OpenAI Ads MCP server documented as of 2026-10 [Unverified] (community authors state none existed when they built theirs).

## 2. Advertiser API essentials [Official, 2026-09] unless labeled

Authentication:
- Ads API keys: Ads Manager > Settings > API keys. One key per ad account. Store as `OPENAI_ADS_API_KEY` in a secret manager.
- Partners and agencies: OAuth flow (`auth.openai.com`, scopes `ads.admin.all.read` and `ads.admin.all.write`, header `OpenAI-Ad-Account`) [Unverified] (community notes; see API Partner Setup page).
- CAPI keys are separate (Conversions area) and only for event sending.

Objects and endpoints:
| Resource | Endpoints |
|----------|-----------|
| Ad account | `GET /ad_account` (returns currency_code, timezone), branding updates, spend limit windows (some accounts) |
| Campaigns | `GET /campaigns`, `GET /campaigns/{id}`, `POST /campaigns`, `POST /campaigns/{id}`, `POST /campaigns/{id}/activate`, `/pause`, `/archive` |
| Ad groups | `GET /ad_groups?campaign_id=`, `POST /ad_groups`, `POST /ad_groups/{id}`, state endpoints |
| Ads | `GET /ads?ad_group_id=`, `POST /ads`, `POST /ads/{id}`, `POST /ads/{id}/preview` (preview expires after 24 hours), state endpoints |
| Files | `POST /upload` (image by URL or multipart; purpose `account_favicon` for favicons); `POST /uploads` for audience files |
| Insights | `GET /ad_account/insights`, `/campaigns/{id}/insights`, `/ad_groups/{id}/insights`, `/ads/{id}/insights`; `POST /conversions/insights` |
| Conversions | `GET`/`POST /conversions/pixels`, `POST /conversions/api_keys`, `GET`/`POST /conversions/event_settings`, `GET /conversions/events` (sample of last 15 minutes) |
| Audiences | Custom audiences create, membership add, remove, replace (Idempotency-Key required), status polling |
| Feeds | `POST /feeds`, SFTP access, uploads and diagnostics, `PATCH /feeds/{id}/products` (delta price and availability), products query preview |
| Audit logs | Recorded changes to resources in an ad account |
| Bulk API | Limited preview: bulk mutation jobs up to 1,000 operations with `validate_only` [Unverified] (details) |

Conventions:
- Updates use `POST` with partial top level fields; nested objects (`budget`, `bidding_config`, `creative`, `targeting`) must be sent in full. List fields such as `context_hints`, `conversion_event_setting_ids`, `product_set` filters replace on update.
- Create statuses: `active` or `paused` (always create paused). Archive is irreversible; there is no delete.
- Money in micros (1,000,000 = 1 unit). Insights spend, CPC and CPM are in major units.
- Pagination: `limit`, `after` or `before`; lists may be eventually consistent, so verify writes with GET by ID [Unverified].
- Errors: `{"error": {"message", "type", "param", "code"}}`; `x-request-id` header on responses (include in support tickets) [Unverified].
- Idempotency: `Idempotency-Key` header on creates; required for Maximize results ad groups and audience operations; reuse only for retries of the same body.
- Rate limits: 600 requests per minute per endpoint and 1,200 per minute total, per ad account and per IP [Unverified] (community notes); honor `Retry-After`.
- Enums: `bidding_type` `impressions|clicks|conversions`; `billing_event_type` `impression|click`; `strategy` `fixed_bid|maximize_clicks|maximize_conversions`; review status `in_review|approved|rejected`; platforms `ios_app`, `android_app`, `web` (granular `desktop_web`, `ios_web`, `android_web` reported) [Official, 2026-09] and [Unverified] (granular).
- Diagnostics: `include[]=serving_issues`, `include[]=bid_too_low`.
- Removed from the public spec in September 2026 per community notes: lead forms, business agents, negative keywords [Unverified].

Insights parameters:
| Parameter | Values |
|-----------|--------|
| `fields[]` | For example `campaign.id`, `campaign.name`, `campaign.impressions`, `campaign.clicks`, `campaign.spend`, `campaign.ctr`, `campaign.cpc`, `campaign.cpm`; conversion metrics `conversions`, `click_through_conversions`, `view_through_conversions`, `cpa`, `post_click_cvr`, `order_created_attributed_sales`, `order_created_roas` |
| `time_ranges[]` | One JSON encoded range: `date_range`, `unix_range` or `hour_range` |
| `time_granularity` | `hourly`, `daily`, `monthly`, `none` (product reports: daily or none) |
| `aggregation_level` | `ad_account`, `campaign`, `ad_group`, `ad` |
| `segments[]` | One of `country`, `device`, `platform`, `product` |
| `filters[]`, `sort[]` | JSON objects; filter operators `IN`, `GREATER_THAN`, `LESS_THAN` |
| Attribution | `attribution_window_days` 7, 14, 30; `view_through_attribution_window_days` 0 or 1; `attribution_time_basis` |
| Limits | `limit` 1 to 2,000; history 365 days (hourly and product about 30 days); conversions endpoint returns 413 over 2,000 rows |
Array parameters need the `[]` suffix; bare names return 400 [Unverified] (community live test).

## 3. Read-only scripts (safe for agents to run with a key the human provides)

Check account:
```bash
curl -s https://api.ads.openai.com/v1/ad_account \
  -H "Authorization: Bearer $OPENAI_ADS_API_KEY"
```

List campaigns:
```bash
curl -s "https://api.ads.openai.com/v1/campaigns?limit=100" \
  -H "Authorization: Bearer $OPENAI_ADS_API_KEY"
```

Campaign insights, daily, last 7 days (verify the `time_ranges[]` JSON shape in the live Insights reference before use):
```bash
curl -s -G "https://api.ads.openai.com/v1/ad_account/insights" \
  -H "Authorization: Bearer $OPENAI_ADS_API_KEY" \
  --data-urlencode 'aggregation_level=campaign' \
  --data-urlencode 'time_granularity=daily' \
  --data-urlencode 'time_ranges[]={"type":"date_range","since":"2026-10-01","until":"2026-10-07"}' \
  --data-urlencode 'fields[]=campaign.id' \
  --data-urlencode 'fields[]=campaign.name' \
  --data-urlencode 'fields[]=campaign.impressions' \
  --data-urlencode 'fields[]=campaign.clicks' \
  --data-urlencode 'fields[]=campaign.spend' \
  --data-urlencode 'limit=2000'
```

Python export to CSV (read only):
```python
#!/usr/bin/env python3
"""Export ChatGPT Ads campaign insights to ads-master/data/imports/. Read only.
Usage: OPENAI_ADS_API_KEY=... python3 export_insights.py 2026-10-01 2026-10-07
Verify field and time range shapes against developers.openai.com/ads/api-reference/insights first."""
import csv, json, os, sys, urllib.parse, urllib.request

BASE = "https://api.ads.openai.com/v1"
key = os.environ["OPENAI_ADS_API_KEY"]
since, until = sys.argv[1], sys.argv[2]
fields = ["campaign.id", "campaign.name", "campaign.impressions",
          "campaign.clicks", "campaign.spend", "campaign.ctr", "campaign.cpc"]
params = [("aggregation_level", "campaign"), ("time_granularity", "daily"),
          ("limit", "2000"),
          ("time_ranges[]", json.dumps({"type": "date_range", "since": since, "until": until}))]
params += [("fields[]", f) for f in fields]

rows, after = [], None
while True:
    q = params + ([("after", after)] if after else [])
    req = urllib.request.Request(f"{BASE}/ad_account/insights?{urllib.parse.urlencode(q)}",
                                 headers={"Authorization": f"Bearer {key}"})
    with urllib.request.urlopen(req, timeout=60) as r:
        page = json.load(r)
    rows += page.get("data", [])
    if not page.get("has_more"):
        break
    after = page.get("last_id")

out = f"ads-master/data/imports/{until}_chatgpt-ads_campaign-insights.csv"
keys = sorted({k for row in rows for k in row})
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=keys)
    w.writeheader()
    for row in rows:
        w.writerow({k: json.dumps(v) if isinstance(v, (dict, list)) else v for k, v in row.items()})
print(f"{len(rows)} rows -> {out}")
```

Conversion events sanity check (sample from the last 15 minutes):
```bash
curl -s "https://api.ads.openai.com/v1/conversions/events?pid=$PIXEL_ID&limit=50" \
  -H "Authorization: Bearer $OPENAI_ADS_API_KEY"
```

CAPI validation without saving (server side, test key handling carefully; never commit the key):
```bash
curl -s -X POST "https://bzr.openai.com/v1/events?pid=$PIXEL_ID" \
  -H "Authorization: Bearer $OPENAI_CAPI_KEY" -H "Content-Type: application/json" \
  -d '{"validate_only": true, "events": [{"id": "test-001", "type": "lead_created",
       "timestamp_ms": '"$(date +%s000)"', "action_source": "web",
       "source_url": "https://www.example.com/contact/thanks",
       "data": {"type": "customer_action"}}]}'
```

oppref redirect survival test:
```bash
curl -s -o /dev/null -L -w "%{url_effective}\n" "https://www.example.com/landing?utm_source=chatgpt&oppref=synthetic123"
# Pass if the final URL still contains oppref=synthetic123
```

## 4. Community MCP servers and CLIs (review before use)

| Project | Type | Capabilities | Safety features | Label |
|---------|------|-------------|-----------------|-------|
| trakkr-aisearch/openai-ads-mcp (v0.1.7, public beta) | MCP (Python and Node) | 27 tools: account, campaigns, ad groups, ads (incl. creative upload), insights, audiences, geo search, conversions (manage, send), helpers (build campaign, draft context hints, bulk A/B hint tests) | `OPENAI_ADS_MCP_READONLY=1` removes write tools; creates paused; budget ceiling default $100 with explicit confirm; no key logging | [Unverified] (README) |
| HYPD-AI/openai-ads-mcp | MCP (Node, `npx -y @hypd-ai/openai-ads-mcp`) | 11 read only tools: account, campaigns, ad groups, ads, insights at all levels | Read only by design | [Unverified] (README) |
| Roast-Labs/openai-ads-mcp | MCP (Python) | OpenAI Ads tools | Unknown | [Unverified] |
| Synter-Media-AI/mcp-server | Multi platform MCP | Reporting on 19 platforms, campaign creation on 14 including OpenAI Ads | Unknown | [Unverified] |
| PaidSync/paidsync-mcp | Hosted multi platform MCP | Builds campaigns on ChatGPT Ads among others | Unknown | [Unverified] |
| faborsky/chatgpt-ads-app | Python CLI plus Claude Code skill | About 100 commands: plan-apply from JSON, landing-check, ad-review, pulse, conversion-check, bulk | Dry run by default, `--confirm` to write, paused creates, rate limit budgeting, explicit account selection | [Unverified] (README, 2026-09) |
| wbso-ai/openai-ads-api-skill | Agent skill | Campaigns, ad groups, ads, creatives, budgets, insights | Reads key from env or local file | [Unverified] |
| ShenJun93/ad-measurement-preflight (chatgpt-ads-tracking-checker.vercel.app) | Web checker | Crawler readiness simulation, oppref redirect survival, pixel presence, CSP flags | Simulation only | [Unverified] |
| PostHog CDP "OpenAI Ads" destination | CDP | Sends events to CAPI with default event mapping | Hashing of email and external IDs | [Unverified] |
| Linkrunner, SourceMedium | Attribution and data | App attribution and CAPI postbacks; reporting integration | Vendor | [Unverified] |

Agent usage rules:
1. Default to read only tools or read only mode. Enable writes only after the human approves a specific change list, and only for that session.
2. Never let a tool activate objects; activation is a separate human step.
3. Use dry run or `validate_only` first; verify with GET by ID after writes.
4. Log every write in the journal with object IDs and before and after values.

## 5. Competitive intelligence tools (category monitoring)
| Tool | What it offers | Label |
|------|---------------|-------|
| Adthena (ChatGPT ads intelligence) | Advertiser and ad frequency tracking, ads in AI search reports | [Study] vendor |
| Similarweb AI Ads | Panel based ChatGPT ad data (opened 2026-08-17) | [Study] vendor |
| SE Ranking ads tracker | Prompt based ad and advertiser tracking | [Study] vendor |
| Sensor Tower | Mobile ad intelligence including ChatGPT app ads | [Study] vendor |
Hand ongoing competitor monitoring to market-intel. Vendor panels disagree heavily; use for direction, not precision.

## 6. Data the agent should request when no API access exists
- Ads Manager CSV exports: campaign, ad group and ad level, daily values, last 30 and 90 days (Ads Manager three dot menu > Download CSV > Daily values).
- Products tab export for feed campaigns.
- GA4 traffic acquisition with session source and medium, filtered to `chatgpt` and `chatgpt.com`, same date range and time zone.
- Backend orders or CRM leads with UTM and stored `oppref`.
Drop files in `ads-master/data/imports/` as `YYYY-MM-DD_chatgpt-ads_<what>.csv`.
