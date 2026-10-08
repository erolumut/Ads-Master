# Tools, API and MCP Servers

> Knowledge as of 2026-10. How Claude can read TikTok data and draft actions. All write actions (create, edit, pause, budget, bid) require explicit human approval, even when an MCP server or API token allows them.

## 1. Access options ranked

| Rank | Option | Read | Write | Setup effort | Notes |
|------|--------|------|-------|-------------|-------|
| 1 | Official TikTok for Business MCP Server | Yes | Yes (campaign management, audiences, creative operations) | Low to medium | Launched at TikTok World (2026-05); packages about 400 TikTok API for Business endpoints as MCP tools; offered through partners including Claude, Perplexity, Manus, Replit, Snowflake and the IAB Tech Lab Agent Registry [Official, 2026] |
| 2 | TikTok API for Business (Marketing API) v1.3 | Yes | Yes | Medium (developer app, OAuth, access token) | Full control; reporting, management, audiences, Events API |
| 3 | Data connectors (Supermetrics, Funnel, Windsor.ai, Fivetran, Airbyte, Porter Metrics and similar) | Yes | No | Low | Into sheets, BigQuery, Looker Studio; Claude reads the warehouse or sheet |
| 4 | Community MCP servers | Varies | Varies | Medium | Not official; review code and scopes before connecting |
| 5 | CSV exports from Ads Manager and Seller Center | Yes | No | None | Fallback; follow HOW_TO_EXPORT.md naming |

TikTok reports that advertiser use of its MCP connector for campaign activation and management grew more than 200% since launch (internal data, July to September 2026, no base given) [Official, 2026-10].

## 2. Official TikTok for Business MCP Server and Agentic Hub
- Agentic Hub: the discovery layer, a marketplace of AI-powered tools and AI Skills for advertisers and developers [Official, 2026].
- MCP Server: the connectivity layer, a standardized bridge that gives AI agents structured access to TikTok Ads capabilities: campaign management, performance reporting, audience configuration, creative operations [Official, 2026].
- Docs: `business-api.tiktok.com/portal/docs/tiktok-ads-mcp-server/v1.3` and the help center article "About TikTok for Business MCP Server".
- Regional availability, authentication and permissions: verify in the docs and in the user's account. In Europe, TikTok said the MCP changes are available [Unverified, single trade source].

Agent operating rules with any MCP server:
1. Start every session with read-only calls: list advertisers, campaigns, ad groups, ads; pull reports.
2. State which account, date range and attribution setting the data uses.
3. Never call a create, update, pause, delete, budget or bid tool without an approved change list in the conversation. Quote the approved row before each write call.
4. After an approved write, read back the entity to confirm the change and log it in the journal with the timestamp.
5. If a tool returns an error or partial result, stop and report. Do not retry writes blindly.

## 3. Community and third-party MCP servers (verify before use)

| Server | Scope | Label |
|--------|-------|-------|
| ysntony/tiktok-ads-mcp (GitHub) | 6 read-only tools: business centers, ad accounts, campaigns, ad groups, ads, reports | [Unverified, community] |
| AdsMCP TikTok Ads server (listed on PulseMCP, released 2025-09-17) | Campaign management, analytics, creative assets, audience targeting, automated reports | [Unverified, community] |
| Hosted commercial MCP services (several vendors) | Varies | Check data handling and scopes |

Security checklist for non-official servers: read the code, prefer read-only scopes, use a dedicated token with the least privilege, store tokens in environment variables or a secret manager (never in `ads-master/` files), and revoke tokens when done.

## 4. TikTok API for Business (Marketing API) essentials

| Item | Detail |
|------|--------|
| Base URL | `https://business-api.tiktok.com/open_api/v1.3/` [Unverified, confirm current version] |
| Auth | Developer app in the TikTok API for Business portal, advertiser authorization (OAuth), long-lived access token passed in the `Access-Token` header |
| Core objects | advertiser, campaign, adgroup, ad, creative (video, image), audience (DMP), pixel / events, catalog, GMV Max, Smart+ |
| Reporting | Synchronous integrated report endpoint and asynchronous report tasks for large pulls |
| Events API | `event/track/` endpoint for server events (see measurement module) |
| Rate limits | Per app and per endpoint; back off on rate-limit error codes [Unverified values] |

Synchronous report request (illustrative; confirm parameter and metric names in the v1.3 reporting docs):

```bash
curl -G "https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/" \
  -H "Access-Token: $TIKTOK_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=$TIKTOK_ADVERTISER_ID" \
  --data-urlencode "report_type=BASIC" \
  --data-urlencode "data_level=AUCTION_AD" \
  --data-urlencode 'dimensions=["ad_id","stat_time_day"]' \
  --data-urlencode 'metrics=["spend","impressions","clicks","ctr","cpm","conversion","cost_per_conversion","video_watched_2s","video_watched_6s","average_video_play"]' \
  --data-urlencode "start_date=2026-09-01" \
  --data-urlencode "end_date=2026-09-30" \
  --data-urlencode "page_size=1000"
```

Python pattern (read-only, paginated):

```python
import os, json, requests
BASE = "https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/"
HEAD = {"Access-Token": os.environ["TIKTOK_ACCESS_TOKEN"]}
def pull(level="AUCTION_AD", dims=("ad_id", "stat_time_day"), start="2026-09-01", end="2026-09-30"):
    rows, page = [], 1
    while True:
        params = {
            "advertiser_id": os.environ["TIKTOK_ADVERTISER_ID"],
            "report_type": "BASIC", "data_level": level,
            "dimensions": json.dumps(list(dims)),
            "metrics": json.dumps(["spend", "impressions", "clicks", "conversion",
                                   "cost_per_conversion", "video_watched_2s",
                                   "video_watched_6s", "average_video_play"]),
            "start_date": start, "end_date": end, "page": page, "page_size": 1000,
        }
        r = requests.get(BASE, headers=HEAD, params=params, timeout=60).json()
        if r.get("code") != 0:
            raise RuntimeError(r.get("message"))
        data = r["data"]
        rows += data["list"]
        if page >= data["page_info"]["total_page"]:
            return rows
        page += 1
```

Metric names differ between Auction, GMV Max and Smart+ reports and change between versions. Map them once per project and store the mapping in `ads-master/memory/tiktok-ads.md` under account facts.

## 5. TikTok native tools

| Tool | Use |
|------|-----|
| Ads Manager (web and mobile) | Campaign management, reporting, Split Test, automated rules |
| Automated Rules | Rule-based actions (pause, budget changes, notifications) on conditions; any rule that changes spend or status counts as a live change and needs human approval before creation [Unverified current rule options] |
| Events Manager | Pixel, Events API, Test Events, diagnostics, EMQ |
| Creative Center | Top Ads, Keyword Insights, Trend Discovery, Commercial Music Library, Symphony Assistant |
| Symphony Creative Studio | AI video generation, avatars, dubbing, translation [Official, 2026-05] |
| TikTok One | Creators workspace, campaigns, Spark authorization |
| Seller Center | TikTok Shop operations, GMV Max (also in Ads Manager), affiliate center, Shop analytics |
| TikTok Ads Library / Commercial Content Library | Competitor research (EU ads with targeting and reach) |
| Pixel Helper (browser extension) | Debug pixel firing |
| Business Center | Assets, roles, billing |

## 6. Reporting stack patterns

| Tier | Stack |
|------|-------|
| Starter | Ads Manager exports into `ads-master/data/imports/`, spreadsheet with calibrated CPA |
| Growth | Connector to Google Sheets or Looker Studio; weekly pulls; post-purchase survey tool |
| Scale | Warehouse (BigQuery or Snowflake) via connector or API; dbt models joining TikTok spend, backend orders, survey data; MMM-ready daily tables |
| Enterprise | Official MCP or API automation for reads; MMM and lift calendar; multi-account rollups |

Third-party attribution tools (Triple Whale, Northbeam and similar) can provide an independent click and view model for TikTok. Treat them as another lens, not the truth.

## 7. Data handling rules
- Store exports in `ads-master/data/imports/` with date prefixes. Never store access tokens there.
- Hashed customer lists only; never upload raw PII to third-party tools without the human's approval and a data processing agreement.
- When reading creator or customer comments, do not copy personal data into journal or memory files.
