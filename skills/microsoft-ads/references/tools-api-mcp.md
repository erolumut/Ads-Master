# Tools, API, Scripts and MCP Servers

> Scope: tools that let Claude read Microsoft Advertising data or prepare actions: Microsoft Advertising Editor, scripts, automated rules, the Microsoft Advertising API (REST and SOAP), SDKs, MCP servers and data connectors. Default posture: read only. Writes only through a human approved change list.

## 1. Tool selection

| Need | Best tool | Notes |
|------|-----------|-------|
| One off analysis | CSV exports in `ads-master/data/imports/` | Name files `YYYY-MM-DD_microsoft_<report>.csv` |
| Recurring reads by Claude | MCP server or API with read only credentials | Check maintenance and scopes first |
| Bulk edits prepared by Claude | Microsoft Advertising Editor import file or bulk sheet | Human reviews and posts |
| Scheduled in-account automation | Microsoft Advertising scripts or automated rules | Scripts support PMax since 2025-05 [Official, 2025-05] |
| Data warehouse and BI | Reporting API, Power BI or third party connectors | Keep raw daily data |
| Session behavior | Microsoft Clarity and the official Clarity MCP server | github.com/microsoft/clarity-mcp-server |

## 2. Microsoft Advertising Editor
- Desktop app for Windows and Mac. Download account, edit offline, post changes.
- Ads Studio available inside Editor since 2025-05 [Official, 2025-05].
- Supports Google import and PMax negative keywords (since 2026-03) [Official, 2026-03].
- Workflow for Claude: produce a CSV in Editor's import format with only the changed rows; the human imports, reviews the pending changes panel and posts.

## 3. Scripts and automated rules
- Microsoft Advertising scripts use JavaScript with an API modeled on Google Ads scripts (AdsApp). Not every Google script runs unchanged; check entity and method availability.
- PMax compatible with scripts and automated rules since 2025-05 [Official, 2025-05].
- Automated rules: simple scheduled actions (pause, enable, change bids or budgets, email). Prefer email alert rules over action rules unless the human approves the action rule itself.

Alert script pattern (verify method names in Microsoft scripts docs before use; this script only reads and logs):
```javascript
// Alert: campaigns whose 7 day CPA is above target, or zero conversions with spend above a floor.
var TARGET_CPA = 100;   // from PROJECT_BRIEF.md
var SPEND_FLOOR = 200;  // spend with zero conversions that triggers an alert

function main() {
  var it = AdsApp.campaigns()
    .withCondition("Status = ENABLED")
    .forDateRange("LAST_7_DAYS")
    .get();
  var lines = [];
  while (it.hasNext()) {
    var c = it.next();
    var s = c.getStats();
    var cost = s.getCost();
    var conv = s.getConversions();
    if (conv === 0 && cost >= SPEND_FLOOR) {
      lines.push(c.getName() + ": spend " + cost.toFixed(2) + ", 0 conversions");
    } else if (conv > 0 && cost / conv > TARGET_CPA * 1.25) {
      lines.push(c.getName() + ": CPA " + (cost / conv).toFixed(2) + " vs target " + TARGET_CPA);
    }
  }
  Logger.log(lines.length ? lines.join("\n") : "No campaigns over threshold.");
}
```

## 4. Microsoft Advertising API

| Item | Detail | Label |
|------|--------|-------|
| Services | Customer Management, Campaign Management, Bulk, Reporting, Ad Insight (keyword planner, estimates) | [Official] |
| Protocols | SOAP (v13) and REST | [Official, 2026-04] |
| SOAP retirement | Full retirement 2027-01-31; SOAP continues receiving features until then (earlier plan to make new features REST only from 2026-10-01 was changed) | [Official, 2026-09] |
| Auth | Developer token plus OAuth through the Microsoft identity platform; MFA required for users | [Practitioner consensus] |
| SDKs | Official SDKs for Python, .NET, Java, PHP; PHP REST SDK repository created 2025-06 | GitHub BingAds org, checked 2026-10 |
| Release notes | learn.microsoft.com/en-us/advertising/guides/release-notes?view=bingads-13 | [Official] |
| Recent API additions | Audience breakdown operation (GetAudienceBreakdown), TopicCriterion, multiple campaign and ad group IDs on impression-based remarketing lists (2025-12); annotation opt-out operations and new reports (2025-07) | [Official, 2025-12] [Official, 2025-07] |
| Conversions API | Separate server-side endpoint (capi.uet.microsoft.com), beta, per account | [Official, 2026-08] |

Migration action for any project with custom SOAP integrations: inventory scripts and connectors that call SOAP; plan REST migration before 2026-12; test in sandbox. Hand off engineering to the project's developers; log the deadline in the journal.

Reporting API report types commonly needed (names to verify in the current Reporting service reference): campaign performance, keyword performance, search query performance, publisher usage performance, audience performance, age and gender audience, professional demographics audience (LinkedIn dimensions), share of voice, product partition performance, asset group performance.

Python SDK reporting pattern (structure only; class names follow the official BingAds Python SDK, but verify against the SDK version you install and prefer the REST path for new builds):
```python
# pip install bingads   (official SDK, github.com/BingAds/BingAds-Python-SDK)
from bingads.authorization import AuthorizationData, OAuthDesktopMobileAuthCodeGrant
from bingads.service_client import ServiceClient
from bingads.v13.reporting import ReportingServiceManager, ReportingDownloadParameters

auth = OAuthDesktopMobileAuthCodeGrant(client_id="<app id>")
auth.request_oauth_tokens_by_refresh_token("<refresh token from secret store>")
data = AuthorizationData(account_id="<account id>", customer_id="<customer id>",
                         developer_token="<developer token>", authentication=auth)
reporting = ServiceClient("ReportingService", version=13, authorization_data=data)
# Build a SearchQueryPerformanceReportRequest with columns, scope (account) and time (last 30 days),
# then download with ReportingServiceManager(...).download_file(ReportingDownloadParameters(...)).
# Save to ads-master/data/imports/YYYY-MM-DD_microsoft_search_terms.csv and state the range in outputs.
```
Never commit tokens. Store the refresh token, developer token and client ID in environment variables or the project's secret store.

### Export column map (UI exports, used by the analysis snippets)
| Analysis | Required columns |
|----------|------------------|
| Search term mining | Search term, Keyword, Match type, Campaign, Ad group, Impressions, Clicks, Spend, Conversions, Revenue |
| Publisher hygiene | Website URL (publisher), Campaign, Clicks, Spend, Conversions |
| Network split | Ad distribution or Network, Campaign, Clicks, Spend, Conversions |
| Parity report | Keyword, Match type, Clicks, Impressions, Spend, Conversions, Impression share |
| LinkedIn layers | Company or Industry or Job function, Campaign, Clicks, Spend, Conversions |
| PMax landing pages | Final URL, Campaign, Spend, Conversions, Revenue |
Column names vary by language and report version; map before running scripts.

## 5. MCP servers (as found on GitHub, 2026-10-08)

No official Microsoft Advertising MCP server was found. Microsoft publishes an official Clarity MCP server. Community and commercial options:

| Server | Type | Notes from repository description | Created |
|--------|------|-----------------------------------|---------|
| microsoft/clarity-mcp-server | Official (Clarity, not Ads) | MCP server for Microsoft Clarity | 2025-04 |
| shinypebble/microsoft-ads-mcp | Community, Python, FastMCP | Uses the official msads REST SDK; campaign management, keyword research, extensions, bulk, reporting | 2026-06 |
| wvuhskr/mcp-microsoft-ads | Community, Python | Describes itself as unofficial and safety-first | 2026-08 |
| bit-of-a-shambles/microsoft-ads-mcp-server | Community, Python | Create campaigns, ad groups, keywords, ads (Bing, DuckDuckGo) | 2026-01 |
| james-julius/microsoft-ads-mcp | Community, Python | Reporting and campaign management | 2026-06 |
| Insightful-Pipe/microsoft-ads-mcp-server | Hosted remote MCP | Commercial hosted connector | 2026-01 |
| Synter-Media-AI/mcp-server and microsoft-ads-agent | Multi platform | Reporting on many platforms, campaign creation | 2026-01, 2026-03 |
| PaidSync/paidsync-mcp, adkit/ads-mcp, opusgrowth connector | Hosted multi platform | Include Microsoft Advertising among platforms; opusgrowth mentions approval gates | 2026-05 to 2026-07 |
| itallstartedwithaidea/advertising-hub | Directory | Collection of ad platform APIs, MCP servers and agents | 2026-03 |

Evaluation checklist before connecting any MCP server:
- [ ] Maintainer identity and update recency; open issues reviewed.
- [ ] Read only mode available; write tools can be disabled.
- [ ] OAuth scopes limited; developer token stored outside the repo (environment variable or secret store).
- [ ] Hosted servers: data retention and access terms reviewed by the human.
- [ ] Test on a sandbox or low spend account first.
- [ ] Every write still goes through an approved change list; log the action in the journal.

## 6. Data connectors and BI
- Third party ETL connectors (for example Supermetrics, Funnel, Windsor, Dataslayer) can land Microsoft data in a warehouse or spreadsheet. Choose based on the project's existing stack.
- Keep daily granularity at campaign, ad group, keyword, search term and publisher levels for at least 13 months to support year over year analysis.

## 7. How Claude should use these tools
1. Discover: list available MCP tools or check `ads-master/data/imports/` for files.
2. State the data source and date range in the deliverable.
3. Read only queries for analysis.
4. Draft changes as a change list (and, if useful, an Editor import file).
5. After human approval, the human applies changes, or Claude applies them through a write tool only if the human explicitly approves that specific write.
6. Journal entry with what was changed, by whom, when.
