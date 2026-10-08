# Tools, API and MCP Servers

> Knowledge as of 2026-10. API versions sunset roughly a year after release; the official MCP server was read-only at the time of writing. Verify the current state on the Google Ads API release notes, the sunset dates page and the googleads/google-ads-mcp repository before connecting anything.

## 1. How Claude gets data (in order of preference)

| Route | Read | Write | When to use |
|---|---|---|---|
| MCP connector already installed by the user (official or community Google Ads MCP) | Yes (GAQL) | Official: no. Community: some | First choice when present; state which connector you used |
| Exports in `ads-master/data/imports/` | Yes | No | Always works; ask for the exports listed in HOW_TO_EXPORT.md |
| Google Ads API via a script the user runs | Yes | Yes, with approval | Larger audits, recurring reports |
| Google Ads Scripts pasted by the user into the account | Yes | Yes, with approval | Monitoring and alerts inside the account |
| Google Ads Editor (user operated) | Bulk view | Bulk changes the human posts | Large structural change lists: deliver as CSV for Editor import |
| Screenshots | Partial | No | Last resort; label as low confidence |

Never ask for passwords. Never ask the user to share a developer token or OAuth refresh token in chat; tell them to configure it in their own environment.

## 2. Google Ads UI AI features (2025 to 2026)

| Feature | What it does | Status | Label |
|---|---|---|---|
| Ads Advisor | Gemini-powered agent in Google Ads: campaign ideas, assets, diagnostics; "with your review and approval, it can then apply these changes directly to your account" | Rolled out to English accounts by 2025-12, merged into Ask Advisor in 2026-05 | [Official, Google blog 2025-11] |
| Ads Advisor safety features | Policy violation guidance, account security monitoring (announced as coming), automated certifications | 2026-04 | [Official, 2026-04] |
| Ask Advisor | Unified agent across Google Ads, Google Analytics, Merchant Center and Google Marketing Platform, built from specialist agents. In Google Ads it proposes changes and asks for approval before acting (reported actions: pause campaigns, change daily budgets and locations, update final URLs, appeal disapproved ads) | Beta for English-language accounts, announced 2026-05-20, more languages promised without a date; not available in manager (MCC) accounts as of 2026-09; Merchant Center closed beta for selected US merchants | [Official, Google blog and Google Ads Help "Ask Advisor in Google Ads (beta)", 2026-05; action list and MCC status from LGG Media 2026-09] |
| AI overviews and AI-powered dashboards in Google Ads | Summaries of anomalies and changes; dashboards from text prompts | Introduced 2026-08-10 | [Practitioner report, 2026-08] |
| AI-generated experiment summaries | Recap of goals, findings and next steps in the experiment Summary tab | 2026-10 | [Practitioner report, Search Engine Land 2026-10] |
| AI campaign localization | Gemini translates Search campaign assets, keywords, images and landing pages for new markets | 2026-10 | [Practitioner report, Search Engine Land 2026-10]. Review every translation with a native speaker before approval |
| Missed Opportunities | Missed clicks, conversions, value split by budget or bid limits | Moved into Recommendations 2026-07 (beta) | [Practitioner report, 2026-07] |
| Asset Studio | Image and video generation and editing; Gemini Omni upgrade staged from summer 2026; multimodal video creation GA | 2025 to 2026 | [Official, 2026-05] |
| Data Strength Uplift | Estimates conversions recovered by first-party data setup | 2026-09-10 | [Official claim via trade press, 2026-09] |

Ask Advisor write capability (resolved 2026-10): Google's FAQ says it "makes recommendations and will seek your approval before completing actions or making changes to your account", and the "cannot execute account changes on your behalf" wording refers to acting without that approval [Official, Ask Advisor FAQ and help, 2026]. So it can change a live account once a user clicks approve. Package rule: an approval inside Ask Advisor is not a substitute for the human-approved change list. Never suggest that the user approve agent actions to skip the change list, and log any change made through Ask Advisor in the journal.

## 3. Google Ads API

| Item | Detail |
|---|---|
| Protocol | gRPC and REST; client libraries for Python, Java, PHP, .NET, Ruby, Perl |
| Query language | GAQL through GoogleAdsService.Search and SearchStream |
| Versions (2026) | Supported on 2026-10-08: v23, v24, v25 (the official Python client 33.0.0 dropped v21 and v22). v25 released 2026-07-22 (breaking: CustomerLifecycleGoal and CampaignLifecycleGoal removed, replaced by unified Goal and CampaignGoalConfig) [Official via trade press]; v25.1 2026-08-19 (AI Max migration timestamp fields, text disclaimer asset types, loyalty segmentation for conversion value rules); v25.2 2026-09-23 (PMax drafts from Smart campaigns, asset group tracking templates and URL parameters, PMax segments for product data and video usage, percentile benchmarks, bid-too-low recommendations). v25 also adds read-only lift study resources (`lift_measurement_config`) [Official, v25 type definitions] |
| Sunset | v20 sunset 2026-06-10, v21 2026-08-05, v22 2026-10-07 [Official, Google Ads Developer Blog 2026-09-02 reminder]. No sunset dates published for v23 and v24 as of 2026-10; check the sunset dates page each quarter |
| Developer Policies | Renamed from "Google Ads API Policy" and updated in 2026-09: integrations must connect through their own Google Cloud project instead of programmatic proxies [Practitioner report, PPC News Feed 2026-09-04, citing Google]. Check community MCP servers and vendor connectors against it |
| Reporting history | Since 2026-06-01, daily, weekly and hourly data is kept 37 months; monthly, quarterly and yearly aggregates 11 years; reach and frequency 3 years. Older granular queries fail with a date range error [Official, Google Ads Developer Blog 2026-05 and Google Ads Help "Data retention policy"] |
| Access levels | Test account access, Explorer access, Basic access (daily operation limit), Standard access (higher limits). Apply in the API Center of a manager account [Official, verify current limits] |
| Credentials | Developer token (from a manager account), OAuth2 client, refresh token or service account, login-customer-id for manager access |
| Conversion uploads | From 2026-06-15 `UploadClickConversions` (offline click conversions and enhanced conversions for leads) only accepts developer tokens that uploaded before the cutoff; others get CUSTOMER_NOT_ALLOWLISTED_FOR_THIS_FEATURE and must use the Data Manager API. Customer Match uploads through the Google Ads API were restricted the same way from 2026-04-01 [Official, Google Ads Developer Blog 2026-05-15 and API deprecations page] |
| Rate and quota | Per developer token operations per day (by access level) and per-request limits |

API v21 (2025-08) added AI Max ad group controls (disable search term matching per ad group; brand lists, locations and URL rules on ad groups) and the AI Max search term ad combination view [Official]. API v24.2 added ad network segmentation for PMax placement reporting [Practitioner report, 2026-05].

## 4. Data Manager API

- Google's API for sending first-party data (audience members for Customer Match, conversions including offline and enhanced conversions for leads) across Google Ads, Google Analytics and Display and Video 360.
- Launched 2025-12-09. Differences from the Google Ads API: no developer token, quotas per Google Cloud project, optional encryption of user data, IP and session attributes available to all users [Official, Data Manager API docs].
- 2026 milestones: required path for new Customer Match integrations (2026-04-01) and new offline conversion integrations (2026-06-15); v1.7 (2026-05-28) added raw IP ingestion for Customer Match and events to Google Marketing Platform destinations [Official, Google Ads Developer Blog 2026-05]. Data Manager UI extended to Google Analytics and DV360 on 2026-09-10 [Practitioner reports, 2026-09].
- Owner: measurement builds the pipeline; google-ads specifies which conversion actions and lists are needed and checks results in the account.

## 5. MCP servers

| Server | Maintainer | Access | Notes |
|---|---|---|---|
| google-ads-mcp | Google (github.com/googleads/google-ads-mcp), documented on the Google Ads API developer site | Read-only | Open source (Apache 2.0), Python, released 2025-10. Tools include a GAQL `search` tool and account listing or resource metadata tools (the README lists the current set). Needs a developer token and OAuth with the adwords scope. Runs over stdio locally or on Cloud Run. A 2026-07 fix stopped OAuth credentials appearing in logs [Official and trade press, 2025-10 to 2026-07] |
| Community servers (for example cohnen/mcp-google-ads, promobase/google-ads-mcp, getmcpads-com/google-ads-mcp-server) | Third parties | Read, some write | Some include Keyword Planner tools and write tools with preview steps. Review code, scopes and data handling before use [Practitioner] |
| Hosted multi-platform and vendor MCPs (for example Adspirer, Ryze AI, Optmyzr MCP) | Vendors | Read, approval-gated writes | Convenience vs data sharing with a vendor; check terms and security |
| Google Analytics MCP | Google | Read | Useful for GA4 cross-checks; owned by measurement |

Rules for Claude with MCP servers:
1. Prefer read-only access. Run GAQL from the [GAQL module](gaql-and-scripts.md).
2. Even with write-capable servers, never execute a write without explicit human approval of the exact change list (campaign, field, old value, new value).
3. Log the connector name, account ID and date range used in every deliverable.
4. Respect API quotas: batch queries, use SearchStream for large reports, avoid repeated full-account pulls.

## 6. Google Ads Scripts

- JavaScript inside Google Ads; `AdsApp.search` for GAQL, AdsApp entities for changes, SpreadsheetApp, MailApp, UrlFetchApp.
- Runtime limit about 30 minutes; manager account scripts can run across many accounts with executeInParallel [Official, verify limits].
- Use for: anomaly alerts, pacing, disapproval alerts, n-gram reports, link checking, automated reporting.
- Every script that writes must be previewed and approved; keep a changelog sheet that records every change the script makes.

## 7. Google Ads Editor

- Desktop app for bulk edits offline, then post to the account.
- Deliver large change lists as Editor-ready CSV (columns: Campaign, Ad group, Keyword, Criterion Type, Status, etc.) so the human can review and post.
- Check: Editor version supports AI Max, PMax and Demand Gen fields used in the change (Editor lags new features). Editor 2.10 and earlier lose support on 2026-10-19 [Practitioner report, 2026-10]; ask the human to update before posting.

## 8. Reporting and warehouse

| Tool | Use |
|---|---|
| Google Ads Report editor | Custom tables and charts in the UI |
| Looker Studio | Dashboards with the native Google Ads connector |
| BigQuery Data Transfer Service for Google Ads | Daily warehouse of Google Ads tables for long history and joins with backend data. Granular reporting history is limited to 37 months since 2026-06-01 and transfers no longer backfill dates older than that [Official, Google Ads Developer Blog 2026-05], so start warehousing before you need multi-year daily data |
| Google Sheets add-ons | Light reporting |

## 9. Third-party tools

| Tool | Strength | Use for |
|---|---|---|
| Optmyzr | Rule engine, PMax insights, budget pacing, search term and n-gram tools, audits, AI assistant | Agencies and in-house teams managing many accounts |
| Adalysis | Ad testing statistics, Quality Score tracking, audits, alerts | Search-heavy accounts |
| Opteo | Guided improvements and monitoring | Smaller teams |
| Click fraud and invalid traffic tools (for example Lunio, ClickCease) | Detect and exclude invalid traffic | Lead gen with spam problems; validate claims with CRM data |
| Feed tools (Feedonomics, DataFeedWatch, Channable, Productsup) | Feed optimization | Owned by commerce-feeds |
| Call tracking (CallRail, Invoca, WhatConverts) | Call attribution and qualified call import | Lead gen and local |
| Search Ads 360 | Enterprise cross-engine management, bidding, floodlight | Enterprise tier |

Do not cite vendor performance claims as facts. Label them [Unverified] unless a method is published.

## 10. Recommended setup by tier

| Tier | Data route | Automation |
|---|---|---|
| Starter | Exports to `ads-master/data/imports/`, Google Ads UI | Scripts S3, S4, S5 (alerts) |
| Growth | Official MCP (read-only) or exports | Scripts plus a monthly audit with GAQL |
| Scale | MCP plus BigQuery transfer | Scripts, API-based reporting, a rules tool (Optmyzr or similar) |
| Enterprise | API, BigQuery, Search Ads 360 if multi-engine | Governance: change approvals, audit logs, automated QA |

## 11. Connector QA checklist (before trusting MCP or API data)

| Check | How |
|---|---|
| Right account | Run `SELECT customer.id, customer.descriptive_name, customer.currency_code, customer.time_zone FROM customer` and confirm with the brief |
| Right date range and timezone | Account timezone from the query above; state it in the deliverable |
| Totals match the UI | Compare 7-day cost and conversions for one campaign with the UI |
| API version current | The connector should not use a sunset version (v22 ended 2026-10-07) |
| Permissions minimal | Read-only OAuth scope where possible; standard access only when writes are approved |
| Logging | Record connector name, query IDs and date range in the output file |

## 12. Google Ads Editor CSV change list template

```
Action,Campaign,Ad group,Keyword,Criterion Type,Status,Max CPC,Final URL,Comment
Add,US_EN_SRCH_NB_Running-Shoes_tROAS_v3,Trail Running,trail running shoes waterproof,Phrase,Enabled,,https://example.com/trail,From converting search terms 2026-09
Add negative,US_EN_SRCH_NB_Running-Shoes_tROAS_v3,,jobs,Campaign negative broad,Enabled,,,N-gram waste 2026-07 to 2026-09
Pause,US_EN_SRCH_NB_Running-Shoes_tROAS_v3,Old Theme,,,Paused,,,Under 100 impressions in 90 days
```
The human reviews, imports into Google Ads Editor, checks the pending changes and posts. Adapt column names to the current Editor import format.
