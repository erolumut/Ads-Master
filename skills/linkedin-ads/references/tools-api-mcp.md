# Tools, API and MCP Servers

> Scope: ways Claude can read LinkedIn Ads data or prepare actions: Campaign Manager exports, the LinkedIn Marketing API (advertising, reporting, lead sync, conversions, audiences), official client libraries and CAPI templates, MCP servers, the LinkedIn Ad Library and data connectors. Default posture: read only; writes only through an approved change list. Endpoint and field names are patterns to verify against the current API version.

## 1. Tool selection
| Need | Tool | Notes |
|------|------|-------|
| One off analysis | Campaign Manager exports to `ads-master/data/imports/` | Name `YYYY-MM-DD_linkedin_<report>.csv` |
| Recurring reads | MCP server or Marketing API with read scopes | Check scopes and maintenance |
| Lead sync | Native CRM integrations; Lead Sync API for custom stacks | Speed to lead |
| Server-side conversions | Conversions API via CRM connector, GTM server template or CDP | Owned by measurement |
| Competitor creative research | LinkedIn Ad Library (public) | Hand off to market-intel for deep work |
| BI and warehouse | API or third party connectors | Keep daily data 13+ months |

## 2. LinkedIn Marketing API essentials
| Item | Detail | Label |
|------|--------|-------|
| Docs | https://learn.microsoft.com/en-us/linkedin/marketing/ | [Official] |
| Access | Apply for Marketing API products (advertising, lead sync, conversions, audiences) from the LinkedIn developer portal; development and standard access tiers | [Official, 2023] [Unverified] for current tier names |
| Auth | OAuth 2.0 three legged; scopes such as read and write for ads, reporting, lead forms and conversions | [Official] verify scope names |
| Versioning | Monthly versions in YYYYMM format sent in the LinkedIn-Version header; each version is sunset about one year after release (202510 sunsets 2026-10-15; 202609 is the latest as of 2026-10-08) | [Official, 2026-09] |
| Naming gap | The UI renamed campaign groups to Campaigns and campaigns to Ad sets in 2025-10; the API still uses adCampaignGroups and adCampaigns, so map names in reports | [Official, 2025-10] |
| Protocol | Rest.li; send X-Restli-Protocol-Version: 2.0.0 | [Official] |
| Base | https://api.linkedin.com/rest/ | [Official] |

Entities (verify names per version):
| Entity | Endpoint pattern | Use |
|--------|------------------|-----|
| Ad accounts | /rest/adAccounts | Account list and settings |
| Campaign groups | /rest/adAccounts/{id}/adCampaignGroups | Programs and group budgets |
| Campaigns | /rest/adAccounts/{id}/adCampaigns | Targeting, bidding, budgets |
| Creatives | /rest/adAccounts/{id}/creatives | Ads and status |
| Analytics | /rest/adAnalytics | Performance and demographic pivots |
| Conversions | /rest/conversions and /rest/conversionEvents | Conversion rules and CAPI events |
| Lead forms and responses | Lead sync endpoints | Lead retrieval |
| Matched audiences | DMP segment endpoints | Company and contact lists |
| Predictive audiences | Private API; requires existing Matched Audiences API access | Seeded from company or contact lists [Official, 2026] |
| Company Intelligence | accountIntelligence finder | Companies tab data by campaign, campaign group, objective or seniority (202609) |

Reporting call pattern (verify parameters for the version you pin):
```bash
curl -s -G "https://api.linkedin.com/rest/adAnalytics" \
  -H "Authorization: Bearer $LI_TOKEN" \
  -H "LinkedIn-Version: 202609" \
  -H "X-Restli-Protocol-Version: 2.0.0" \
  --data-urlencode "q=analytics" \
  --data-urlencode "pivot=CAMPAIGN" \
  --data-urlencode "timeGranularity=DAILY" \
  --data-urlencode "dateRange=(start:(year:2026,month:9,day:1),end:(year:2026,month:9,day:30))" \
  --data-urlencode "accounts=List(urn%3Ali%3AsponsoredAccount%3A<ACCOUNT_ID>)" \
  --data-urlencode "fields=impressions,clicks,costInLocalCurrency,externalWebsiteConversions,oneClickLeads,dateRange,pivotValues"
```
Demographic pivots (job function, seniority, company size, industry, company) return approximate and privacy thresholded values and may have data delays [Unverified] for current thresholds; use them for direction, not exact counts.

API changes from 2026 that matter for tooling [Official, 2026-09]:
| Version | Change |
|---------|--------|
| 202602 | optimizationTargetType MAX_QUALIFIED_LEAD for LEAD_GENERATION in adCampaigns and Ad Budget Pricing |
| 202605 | LEAD_GENERATION objective for event ad campaigns (SPONSORED_UPDATE_EVENT); breaking change around endsAt |
| 2026-07 | creativeSelection defaults to OPTIMIZED for SPONSORED_INMAILS with LEAD_GENERATION (previously rejected unless ROUND_ROBIN); set ROUND_ROBIN explicitly to keep even rotation |
| 202608 | Conversion types MARKETING_QUALIFIED_LEAD and SALES_QUALIFIED_LEAD; one 2026-08 report says each account is capped at 1,000 DMP segments (matched plus predictive), with HTTP 429 SEGMENT_LIMIT_EXCEEDED past it [Unverified] |
| 202609 | accountIntelligence filters (campaignGroup, objectiveType, seniority), adAnalytics pivot MEMBER_DESIGNATED_MARKET_AREA, conversionEvents hashedFirstName and hashedLastName, 180 and 365 day attribution windows for lead, purchase and application types |

Python with the official client (pattern):
```python
# pip install linkedin-api-client   (official: github.com/linkedin-developers/linkedin-api-python-client)
from linkedin_api.clients.restli.client import RestliClient
client = RestliClient()
resp = client.finder(
    resource_path="/adAnalytics",
    finder_name="analytics",
    query_params={"pivot": "CAMPAIGN", "timeGranularity": "DAILY",
                  "dateRange": {"start": {"year": 2026, "month": 9, "day": 1},
                                "end": {"year": 2026, "month": 9, "day": 30}},
                  "accounts": ["urn:li:sponsoredAccount:<ACCOUNT_ID>"],
                  "fields": "impressions,clicks,costInLocalCurrency,oneClickLeads"},
    access_token="<token from secret store>",
    version_string="202609",
)
print(resp.elements[:3])
```
Never commit tokens; store in environment variables or a secret manager. Pin an API version and plan upgrades before it sunsets.

## 3. Official developer repositories (GitHub, checked 2026-10-08)
| Repository | What | Created |
|-----------|------|---------|
| linkedin-developers/linkedin-api-python-client | Official Python client | 2023-01 |
| linkedin-developers/linkedin-api-js-client | JavaScript client | 2022-12 |
| linkedin-developers/linkedin-capi-tag-template | Official GTM server-side tag template for Conversions API | 2023-08 |
| linkedin-developers/reactor-extension-linkedin-edge | Adobe Experience Platform event forwarding extension sending conversions to LinkedIn | 2026-06 |
| linkedin-developers/java-sample-application | Sample code for LinkedIn APIs | 2021-10 |

## 4. MCP servers and AI assistant connectors (checked 2026-10-08)
No official LinkedIn Ads MCP server exists: GitHub search on 2026-10-08 found none under linkedin-developers, and vendor status checks dated 2026-07 and 2026-09-27 report no LinkedIn or Microsoft published server and no LinkedIn connector in Claude's directory [Practitioner consensus, 2026-09]. The closest official product is the **LinkedIn Ads app for ChatGPT** (beta): read only access to ad accounts and ad sets the member can see, natural language questions about ad set and ad performance, breakdowns by date range, ad set or ad [Official, 2026]. Community and commercial options:
| Server | Type | Repository description highlights | Created |
|--------|------|-----------------------------------|---------|
| danielpopamd/linkedin-ads-mcp | Community, TypeScript, self hosted (hosted version offered) | 25 tools across campaigns, creatives, audiences, conversions, analytics with write access (needs your own developer app with Advertising API approval) | 2026-01 |
| Nuraveda/linkedin-ads-mcp | Community, Python, MIT | Thin wrapper focused on correct Rest.li encoding; campaigns, analytics, creatives | 2026-05 |
| stan-rym/liam-linkedin-ads-MCP | Community, TypeScript | Create campaigns via Claude or CLI | 2026-06 |
| DanielSylvester/linkedin-ads-mcp | Community, TypeScript | Campaigns, creatives, demographics, conversions, lead gen, analytics | 2026-05 |
| CDataSoftware/linkedin-ads-mcp-server-by-cdata | Vendor, read only via JDBC | Read only access | 2025-06 |
| pipeworx-io/mcp-linkedin_ads | Community pack | LinkedIn Ads MCP pack | 2026-04 |
| proxy-intell/linkedin-ads-library-mcp | Community, Python | Searches the LinkedIn Ad Library for competitor creatives | 2026-08 |
| amekala/ads-mcp, adkit/ads-mcp, markifact/markifact-mcp, Synter-Media-AI/mcp-server, PaidSync/paidsync-mcp, opusgrowth connector | Multi platform hosted or open source | Include LinkedIn Ads; Markifact holds every write until the exact change is approved | 2025-10 to 2026-07 |
| Windsor.ai, Supermetrics, Two Minute Reports, Porter Metrics | Data connectors for ChatGPT and Claude | Some offer pause and budget writes; vendor claims conflict on write support | 2026 |
| jshorwitz/awesome-agentic-advertising | Directory | Curated list of ad MCP servers and tools | 2026-02 |

What the connected member can do limits what any connector can do: a Viewer role can read reports but cannot edit ad sets or ads [Official].

Evaluation checklist before connecting:
- [ ] Maintainer and recency; issues reviewed.
- [ ] Read only mode or ability to disable write tools.
- [ ] Uses the project's own LinkedIn developer app or a vendor app; understand which and what data the vendor stores.
- [ ] OAuth scopes minimal; tokens outside the repo.
- [ ] Test on a low spend account.
- [ ] Every write still goes through an approved change list and a journal entry.

## 5. LinkedIn Ad Library
- Public library of ads run on LinkedIn, searchable by advertiser, keyword, country and date range (https://www.linkedin.com/ad-library) [Official].
- Use: competitor messaging, offers, formats and Thought Leader usage. For EU, additional targeting and reach transparency is shown under the Digital Services Act [Unverified] for fields.
- Third-party release trackers (for example Releasebot) mirror the API changelog; use them as alerts and confirm on Microsoft Learn.
- Hand off systematic competitor analysis to market-intel.

### Rate limits, data delays and versions
- The Marketing API enforces daily application and member level rate limits; batch reporting requests by account and date range [Official] [Unverified] for current values.
- Analytics data can change for several days after the date (late conversions, invalid traffic adjustments); re-pull the trailing 7 to 14 days on each refresh.
- Pin the LinkedIn-Version header and track the sunset date of that version in the journal; upgrade before it sunsets.

## 6. Connectors and BI
- ETL tools (for example Supermetrics, Funnel, Windsor, Dataslayer) can move LinkedIn data to a warehouse or spreadsheet.
- Keep campaign, creative and demographic pivots daily; join with CRM on campaign codes from hidden fields and UTMs.

## 7. How Claude should use these tools
1. Discover available MCP tools or files in `ads-master/data/imports/`.
2. State source and date range in the deliverable.
3. Read only analysis.
4. Draft changes as a change list (and, where helpful, a bulk sheet).
5. Apply only after explicit approval of that specific change; journal it.
