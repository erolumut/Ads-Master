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
| Versioning | Monthly versions in YYYYMM format sent in the LinkedIn-Version header; each version supported for a limited window (historically about one year) | [Official, 2023] |
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
Demographic pivots (job function, seniority, company size, industry, company) return approximate and privacy thresholded values and may have data delays [Unverified]; use them for direction, not exact counts.

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

## 4. MCP servers (GitHub search, 2026-10-08)
No official LinkedIn Ads MCP server was found in GitHub search. Community and commercial options:
| Server | Type | Repository description highlights | Created |
|--------|------|-----------------------------------|---------|
| danielpopamd/linkedin-ads-mcp | Community, TypeScript, self hosted (hosted version offered) | 25 tools across campaigns, creatives, audiences, conversions, analytics with write access | 2026-01 |
| Nuraveda/linkedin-ads-mcp | Community, Python, MIT | Campaigns, analytics, creatives | 2026-05 |
| stan-rym/liam-linkedin-ads-MCP | Community, TypeScript | Create campaigns via Claude or CLI | 2026-06 |
| DanielSylvester/linkedin-ads-mcp | Community, TypeScript | Campaigns, creatives, demographics, conversions, lead gen, analytics | 2026-05 |
| CDataSoftware/linkedin-ads-mcp-server-by-cdata | Vendor, read only via JDBC | Read only access | 2025-06 |
| pipeworx-io/mcp-linkedin_ads | Community pack | LinkedIn Ads MCP pack | 2026-04 |
| proxy-intell/linkedin-ads-library-mcp | Community, Python | Searches the LinkedIn Ad Library for competitor creatives | 2026-08 |
| amekala/ads-mcp, adkit/ads-mcp, markifact/markifact-mcp, Synter-Media-AI/mcp-server, PaidSync/paidsync-mcp, opusgrowth connector | Multi platform hosted or open source | Include LinkedIn Ads; some state human in the loop on writes | 2025-10 to 2026-07 |
| jshorwitz/awesome-agentic-advertising | Directory | Curated list of ad MCP servers and tools | 2026-02 |

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
- Hand off systematic competitor analysis to market-intel.

## 6. Connectors and BI
- ETL tools (for example Supermetrics, Funnel, Windsor, Dataslayer) can move LinkedIn data to a warehouse or spreadsheet.
- Keep campaign, creative and demographic pivots daily; join with CRM on campaign codes from hidden fields and UTMs.

## 7. How Claude should use these tools
1. Discover available MCP tools or files in `ads-master/data/imports/`.
2. State source and date range in the deliverable.
3. Read only analysis.
4. Draft changes as a change list (and, where helpful, a bulk sheet).
5. Apply only after explicit approval of that specific change; journal it.
