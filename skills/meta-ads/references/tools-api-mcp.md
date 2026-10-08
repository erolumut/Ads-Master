# Tools, APIs and MCP Servers

> Knowledge as of 2026-10. Default posture: read-only. Every write (create, update, pause, budget) is drafted as a change list and executed only after explicit human approval, by the human or by a tool call the human approved.

## 1. Data access options (pick the first available)

| Priority | Option | Read | Write | Setup |
|----------|--------|------|-------|-------|
| 1 | Meta Ads MCP connector installed in the user's Claude environment | Yes | Only with approval | User installs and authorizes |
| 2 | Marketing API with a system user token in the user's environment (scripts below) | Yes | Only with approval | Business portfolio admin creates system user and app |
| 3 | Reporting connector exports (Supermetrics, Funnel, Windsor.ai, Porter Metrics, Airbyte, Fivetran) into CSV or warehouse | Yes | No | Existing BI setup |
| 4 | Ads Manager CSV exports dropped in ads-master/data/imports/ | Yes | No | See HOW_TO_EXPORT.md |
| 5 | Screenshots from the human | Limited | No | Last resort |

Always state which source and date range were used in every output.

## 2. Marketing API essentials

Objects: `act_<AD_ACCOUNT_ID>` > campaigns > adsets > ads > adcreatives; `insights` edge on each level; `customaudiences`, `adspixels` (datasets), `product_catalogs`, `adrules_library` (automated rules).

Versioning: new Graph and Marketing API versions ship several times per year and older Marketing API versions are deprecated on their own schedule (check the support end date of the version you use); Advantage+ legacy creation via `smart_promotion_type` was phased out across v24 and v25 (2025 to 2026) [Official, via PPC Land]. Always read https://developers.facebook.com/docs/graph-api/changelog before building.

Permissions: `ads_read` for reporting, `ads_management` for writes, `business_management` for portfolio assets, `leads_retrieval` for lead forms, `catalog_management` for catalogs. Use system user tokens (long-lived) scoped to the needed ad accounts.

Rate limits: Business Use Case (BUC) rate limiting per ad account and app; insights calls are heavier. Use async report runs for large date ranges and many breakdowns; respect `x-business-use-case-usage` headers.

### Read-only query templates

Ad-level performance, daily, last 28 days:
```bash
curl -G "https://graph.facebook.com/v{VERSION}/act_{ACCOUNT}/insights" \
  --data-urlencode "level=ad" \
  --data-urlencode "time_increment=1" \
  --data-urlencode "date_preset=last_28d" \
  --data-urlencode "fields=ad_id,ad_name,adset_name,campaign_name,spend,impressions,reach,frequency,cpm,inline_link_clicks,inline_link_click_ctr,actions,action_values,video_play_actions,video_thruplay_watched_actions,quality_ranking,engagement_rate_ranking,conversion_rate_ranking" \
  --data-urlencode 'action_attribution_windows=["7d_click","1d_view"]' \
  --data-urlencode "limit=500" \
  --data-urlencode "access_token={TOKEN}"
```

Placement breakdown:
```
fields=spend,impressions,actions,action_values&breakdowns=publisher_platform,platform_position
```

Audience segment, age and gender, region, device: `breakdowns=age,gender` or `breakdowns=region` or `breakdowns=impression_device`. Check the current breakdown list in docs for audience segment breakdowns.

Campaign settings snapshot (for audits):
```
GET /act_{ACCOUNT}/campaigns?fields=id,name,objective,status,effective_status,daily_budget,lifetime_budget,bid_strategy,buying_type,special_ad_categories,smart_promotion_type
GET /act_{ACCOUNT}/adsets?fields=id,name,campaign_id,optimization_goal,billing_event,bid_strategy,bid_amount,daily_budget,targeting,attribution_spec,promoted_object,learning_stage_info,status
GET /act_{ACCOUNT}/ads?fields=id,name,adset_id,status,effective_status,creative{id,object_story_spec,asset_feed_spec,degrees_of_freedom_spec},issues_info
```
Field availability changes by version; drop fields that error and log the change.

### Python audit pull (read only)

```python
# pip install facebook_business pandas
import os, pandas as pd
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

FacebookAdsApi.init(access_token=os.environ["META_TOKEN"])
acct = AdAccount(f"act_{os.environ['META_AD_ACCOUNT_ID']}")
fields = ["campaign_name","adset_name","ad_name","ad_id","spend","impressions","cpm",
          "inline_link_clicks","inline_link_click_ctr","actions","action_values","frequency"]
params = {"level": "ad", "date_preset": "last_28d", "time_increment": 7,
          "action_attribution_windows": ["7d_click", "1d_view"]}
rows = [dict(r) for r in acct.get_insights(fields=fields, params=params)]
df = pd.DataFrame(rows)

def action(row, kind, key="actions"):
    for a in row.get(key) or []:
        if a["action_type"] == kind:
            return float(a["value"])
    return 0.0

df["spend"] = df["spend"].astype(float)
df["purchases"] = df.apply(lambda r: action(r, "offsite_conversion.fb_pixel_purchase"), axis=1)
df["revenue"] = df.apply(lambda r: action(r, "offsite_conversion.fb_pixel_purchase", "action_values"), axis=1)
df["cpa"] = df["spend"] / df["purchases"].replace(0, float("nan"))
df["roas"] = df["revenue"] / df["spend"].replace(0, float("nan"))
df.to_csv("ads-master/data/imports/meta_ad_level_last28d.csv", index=False)
```
Action type names vary (for example `purchase`, `omni_purchase`, `offsite_conversion.fb_pixel_purchase`); inspect the `actions` array first and pick consistently.

### Write operations (draft only, never execute without approval)

Represent each approved change as a row, then map to API calls:
| Change | API call (illustrative) |
|--------|-------------------------|
| Pause ad | POST /{AD_ID} status=PAUSED |
| Change campaign daily budget | POST /{CAMPAIGN_ID} daily_budget=<minor units> |
| Change cost per result goal | POST /{ADSET_ID} bid_amount=<minor units> (with bid_strategy COST_CAP) |
| New ad from existing post | POST /act_{ID}/ads with creative object_story_id |
Budgets and bids are in the account currency's minor units (cents). Double check currency before any write.

## 3. Conversions API tools

- Events Manager Test events: send test payloads with `test_event_code`.
- Payload helper in developer docs for building and validating payloads.
- Conversions API Gateway and Signals Gateway for hosted server-side setups.
- Partner integrations: Shopify (Meta channel app, data sharing level "Maximum"), WooCommerce plugin, GTM server-side Meta tag, Stape.
- Hand off build to `measurement`.

## 4. Ad Library and Ad Library API

| Tool | Scope | Use |
|------|-------|-----|
| Ad Library (facebook.com/ads/library) | All active ads globally (creative, start date, platforms); EU and UK ads with more detail; political and social issue ads archived with spend ranges | Competitor creative research, our own ad audit, policy checks |
| Ad Library API (`ads_archive` endpoint) | Political and social issue ads globally; ads delivered in the EU with DSA transparency fields | Programmatic research; requires identity confirmation for the API app |
| Ad Library Report | Political spend aggregates | Not for commercial research |
Competitive research belongs to `market-intel`; request with the competitor list and the questions.

## 5. MCP servers

| Server | Type | Notes | Label |
|--------|------|-------|-------|
| Pipeboard Meta Ads MCP (github.com/pipeboard-co/meta-ads-mcp) | Community, open source, also hosted | Reads insights, campaigns, creatives; some write tools; uses Meta OAuth or token | [Unverified current feature set] |
| GoMarble facebook-ads-mcp-server | Community, open source | Read-focused insights and account data | [Unverified current feature set] |
| Other community servers (various GitHub projects, Zapier MCP, Windsor.ai MCP, Supermetrics MCP style connectors) | Community or vendor | Read access through connectors | [Unverified] |
| Official Meta-provided MCP server for ads | Not confirmed as of this writing | Meta AI connecting to ad accounts for reporting was reported in 2026-09 [Unverified] | [Unverified] |

MCP safety rules:
1. Prefer servers that support read-only mode or scoped tokens with `ads_read` only.
2. For write-capable servers: the agent drafts the change list, the human approves explicitly in the conversation, then the agent executes exactly the approved rows and logs results.
3. Never paste access tokens into outputs, journal or memory files.
4. Log the MCP server name and version used in each output.

## 6. Reporting and analytics tools

| Category | Tools | Use |
|----------|-------|-----|
| Native | Ads Manager reports, Ads Reporting (custom reports, scheduled exports), Meta Business Suite insights, Experiments, Events Manager | Daily operations |
| ETL connectors | Supermetrics, Funnel, Windsor.ai, Porter Metrics, Fivetran, Airbyte (Facebook Marketing source) | Warehouse and dashboards |
| Creative analytics | Motion, Atria, Foreplay (swipe file plus briefs), Superads, Triple Whale creative analytics, Segwise | Concept-level performance, hook and hold rates, competitor swipe files |
| Attribution and incrementality | Northbeam, Triple Whale, Rockerbox, Haus, Measured, Recast, Prescient AI, WorkMagic | Cross-channel truth and lift tests (owned by `measurement`) |
| Open source measurement | Robyn (github.com/facebookexperimental/Robyn), GeoLift (github.com/facebookincubator/GeoLift) | MMM and geo tests |
| Automation | Ads Manager automated rules, Birch (formerly Revealbot), Madgicx, AdEspresso, bulk launchers (AdManage, Kitchn and similar) | Rules and bulk launches; rules must be approved like any change |
| Status | metastatus.com | Delivery and API incidents |
| Benchmarks | Varos, Triple Whale benchmarks, Motion creative benchmarks, LocaliQ/WordStream annual Facebook benchmarks | Context only |

## 7. Automated rules (Ads Manager)

Rules can pause, adjust budgets or notify. Treat each rule as a standing change that requires approval. Safe defaults to propose:
| Rule | Condition | Action |
|------|-----------|--------|
| Spend without results alert | Ad spend > 3 x target CPA, results = 0, lifetime | Notify only |
| Frequency alert | Ad set frequency 7d > 4, cold campaign | Notify |
| CPA spike alert | Campaign CPA 3d > 1.5 x target and spend > 2 x target CPA | Notify |
Prefer notify over auto-pause; auto actions can trigger learning resets and conflict with human edits.

## 8. Export checklist when no API is available

Ask for: campaign, ad set and ad level CSVs, daily, last 30 and 90 days, columns: spend, impressions, reach, frequency, CPM, link clicks, CTR (link), landing page views, results, cost per result, purchases or leads, purchase value, ROAS, 3-second video plays, ThruPlays, quality rankings; breakdowns by placement and by age and gender (separate exports); attribution setting stated. File names: YYYY-MM-DD_meta_<level>_<range>.csv.
