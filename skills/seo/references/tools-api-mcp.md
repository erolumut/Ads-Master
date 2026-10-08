# Tools, APIs and MCP Servers

> Scope: the data and action surfaces Claude can use for SEO: Google Search Console API (Search Analytics, URL Inspection, Sitemaps), Indexing API limits, PageSpeed Insights and CrUX APIs, Bing Webmaster API and IndexNow, Business Profile APIs, crawlers (Screaming Frog, Sitebulb), third party SEO platforms (Ahrefs, Semrush, DataForSEO), MCP servers (official and community), and ready to run scripts. Verify endpoints and quotas in current docs before building automations; vendors change them.

## 1. Tool matrix
| Need | First choice | Alternatives | Access |
|------|--------------|--------------|--------|
| Clicks, impressions, queries, pages | Search Console API or bulk export (BigQuery) | Search Console UI exports; Looker Studio connector; community GSC MCP servers | Property access (owner or user) |
| Index status per URL | URL Inspection API | Search Console UI | Property access |
| CWV field data | CrUX API, CrUX History API, CrUX BigQuery | PageSpeed Insights API (includes CrUX) | API key |
| Lab performance | Lighthouse CLI, PSI API, Chrome DevTools MCP traces | WebPageTest | Free |
| Rendering checks | Playwright or Chrome DevTools MCP, URL Inspection live test | Screaming Frog JS rendering | Free |
| Site crawl | Screaming Frog SEO Spider (CLI for automation) | Sitebulb (desktop and cloud), DataForSEO On-Page API, Lumar, Botify, Oncrawl, JetOctopus | License |
| Keyword and competitor data | Ahrefs, Semrush, DataForSEO | Similarweb, Keyword Planner | Subscription or pay as you go |
| SERP data and rank tracking | DataForSEO SERP API, rank trackers (Semrush, Ahrefs, AccuRanker, SE Ranking, Advanced Web Ranking) | | Pay per request |
| Backlinks | Ahrefs, Semrush, Majestic, Moz; Search Console Links; Bing backlinks | DataForSEO Backlinks API | Subscription |
| Bing data and submission | Bing Webmaster Tools and API, IndexNow | | API key |
| Local | Business Profile APIs, geo grid tools | BrightLocal, Local Falcon | Approved API access |
| Analytics | GA4 Data API, Google Analytics MCP (official, read-only) | Looker Studio | Property access |
| Trends | Google Trends, Trends API (alpha since 2025, limited access) | | Application |

## 2. Google Search Console API
Base: `https://www.googleapis.com/webmasters/v3/` (Search Analytics, Sitemaps, Sites) and `https://searchconsole.googleapis.com/v1/urlInspection/index:inspect` (URL Inspection).

Auth: OAuth (user) or a service account added as a user on the property (Search Console > Settings > Users and permissions). Read scope: `https://www.googleapis.com/auth/webmasters.readonly`. Domain properties use `sc-domain:example.com` as `siteUrl`; URL prefix properties use the full URL with trailing slash.

Search Analytics query parameters:
| Parameter | Values | Notes |
|-----------|--------|-------|
| `startDate`, `endDate` | YYYY-MM-DD | Up to 16 months back |
| `dimensions` | `query`, `page`, `country`, `device`, `searchAppearance`, `date`, `hour` | `hour` with hourly data state (added 2025) [Official, 2025-04; verify] |
| `type` | `web`, `image`, `video`, `news`, `discover`, `googleNews` | Default `web` |
| `dimensionFilterGroups` | filters with `equals`, `contains`, `notContains`, `includingRegex`, `excludingRegex` | RE2 regex |
| `aggregationType` | `auto`, `byPage`, `byProperty` | |
| `rowLimit`, `startRow` | Up to 25,000 per request; paginate with `startRow` | Daily row caps apply per property and search type |
| `dataState` | `final`, `all` (includes fresh data), `hourly_all` | |

Quotas (verify current): per site and per user about 1,200 queries per minute for Search Analytics; URL Inspection 2,000 queries per day and 600 per minute per property [Official, Search Console API usage limits].

Python: pull all rows for a date range with pagination.
```python
# pip install google-api-python-client google-auth
import csv, sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

SITE = "sc-domain:example.com"
creds = service_account.Credentials.from_service_account_file(
    "sa.json", scopes=["https://www.googleapis.com/auth/webmasters.readonly"])
svc = build("searchconsole", "v1", credentials=creds, cache_discovery=False)

def pull(start, end, dims=("date", "query", "page"), search_type="web"):
    rows, start_row = [], 0
    while True:
        body = {"startDate": start, "endDate": end, "dimensions": list(dims), "type": search_type,
                "rowLimit": 25000, "startRow": start_row, "dataState": "final"}
        resp = svc.searchanalytics().query(siteUrl=SITE, body=body).execute()
        batch = resp.get("rows", [])
        rows.extend(batch)
        if len(batch) < 25000:
            return rows
        start_row += 25000

if __name__ == "__main__":
    data = pull(sys.argv[1], sys.argv[2])
    w = csv.writer(sys.stdout)
    w.writerow(["date", "query", "page", "clicks", "impressions", "ctr", "position"])
    for r in data:
        w.writerow(r["keys"] + [r["clicks"], r["impressions"], r["ctr"], r["position"]])
```
Pull by day (one request set per date) when you need maximum rows; the API caps rows per day per search type.

URL Inspection batch:
```python
import json, sys, time
insp = svc.urlInspection().index()
for url in (l.strip() for l in sys.stdin if l.strip()):
    res = insp.inspect(body={"inspectionUrl": url, "siteUrl": SITE, "languageCode": "en-US"}).execute()
    r = res["inspectionResult"]["indexStatusResult"]
    print(json.dumps({"url": url, "verdict": r.get("verdict"), "coverage": r.get("coverageState"),
                      "google_canonical": r.get("googleCanonical"), "user_canonical": r.get("userCanonical"),
                      "last_crawl": r.get("lastCrawlTime"), "robots": r.get("robotsTxtState"),
                      "indexing": r.get("indexingState")}))
    time.sleep(0.2)  # stay under per minute quota
```
Bulk data export to BigQuery: Search Console > Settings > Bulk data export; grant the Search Console export service account BigQuery Job User and BigQuery Data Editor on the project (the exact service account name is shown in the setup screen). Data starts from setup date.

## 3. Indexing API (restricted)
Only for pages with `JobPosting` or `BroadcastEvent` embedded in `VideoObject` (livestreams). Google states other use is unsupported and access can be revoked [Official]. Do not use it to force index ordinary pages.

## 4. PageSpeed Insights and CrUX
PageSpeed Insights API v5 (lab plus field):
```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https%3A%2F%2Fwww.example.com%2F&strategy=mobile&category=performance&key=$PSI_KEY" \
  | jq '{field: .loadingExperience.metrics, origin: .originLoadingExperience.overall_category, lab_lcp: .lighthouseResult.audits["largest-contentful-paint"].displayValue}'
```
CrUX API (field data, p75 by form factor):
```bash
curl -s -X POST "https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=$CRUX_KEY" \
  -H "Content-Type: application/json" \
  -d '{"origin":"https://www.example.com","formFactor":"PHONE","metrics":["largest_contentful_paint","interaction_to_next_paint","cumulative_layout_shift"]}' \
  | jq '.record.metrics | map_values(.percentiles.p75)'
```
Use `"url"` instead of `"origin"` for page level data (needs enough traffic). CrUX History API (`records:queryHistoryRecord`) returns weekly collection periods for trend lines (the number of periods was extended in 2025 [Unverified count]). CrUX on BigQuery (`chrome-ux-report` project) has monthly origin level data for market comparisons.

Lighthouse CLI for lab checks in CI:
```bash
npx lighthouse https://staging.example.com/ --only-categories=performance --form-factor=mobile --output=json --output-path=./lh.json --chrome-flags="--headless"
```

## 5. Bing Webmaster API and IndexNow
IndexNow (Bing, Yandex, Seznam, Naver and other participating engines; Google does not participate):
1. Generate a key (8 to 128 hex characters) and host it at `https://www.example.com/<key>.txt` containing the key.
2. Submit changed, added or deleted URLs:
```bash
curl -s -X POST "https://api.indexnow.org/indexnow" -H "Content-Type: application/json; charset=utf-8" -d '{
  "host": "www.example.com",
  "key": "<key>",
  "keyLocation": "https://www.example.com/<key>.txt",
  "urlList": ["https://www.example.com/products/trail-runner-2", "https://www.example.com/running/trail-shoes/"]
}'
```
Up to 10,000 URLs per POST. Response 200 or 202 means received; 403 key invalid; 422 URLs do not match host; 429 too many requests [Official, IndexNow docs]. Many CMS plugins and CDNs (Cloudflare) integrate it; confirm it fires on updates and deletes.

Bing Webmaster API: generate an API key in Bing Webmaster Tools settings; JSON endpoints under `https://ssl.bing.com/webmaster/api.svc/json/` (for example `GetQueryStats`, `GetPageStats`, `SubmitUrlBatch`, `GetUrlSubmissionQuota`) with `?apikey=`. Verify method names in Microsoft's current API reference. The AI Performance report had no public API at launch [Unverified current state].

## 6. Business Profile APIs
Business Profile APIs (Business Information, Performance, reviews endpoints in the legacy My Business API) require an approved Google Cloud project. Performance API returns daily metrics (impressions by surface, calls, website clicks, direction requests). Use for multi location reporting; edits through API still need human approval under this playbook.

## 7. Crawlers
Screaming Frog SEO Spider:
- Modes: Spider (crawl), List (URL list), SERP (title and description pixel checks).
- JavaScript rendering (Chromium), custom extraction (XPath, CSS, regex), custom JavaScript snippets (including calls to AI APIs for per page classification), structured data validation, near duplicate detection, link score, crawl comparison and change detection, scheduling, API connections (GA4, Search Console, PageSpeed Insights, Ahrefs, Majestic, Moz).
- Headless CLI (Linux binary `screamingfrogseospider`; paid license for full features):
```bash
screamingfrogseospider --crawl https://www.example.com --headless --config ./seo.seospiderconfig \
  --save-crawl --output-folder ./crawls --timestamped-output \
  --export-tabs "Internal:All,Response Codes:Client Error (4xx),Canonicals:Non-Indexable Canonical,Directives:Noindex" \
  --export-format csv
# List mode for a URL file:
screamingfrogseospider --crawl-list ./urls.txt --headless --output-folder ./crawls --export-tabs "Internal:All"
```
- Log File Analyser is a separate product for logs.

Sitebulb: desktop and cloud crawler with prioritized "Hints", JavaScript rendering, crawl maps, accessibility and performance audits. Good for client facing audits.

Enterprise platforms: Lumar, Botify, Oncrawl, JetOctopus (crawl plus logs at scale, monitoring, alerts).

Crawl etiquette: identify the user agent, limit to 2 to 5 URLs per second on production unless approved, crawl outside peaks, and respect robots.txt unless the owner explicitly asks for a full audit crawl.

## 8. Third party SEO platforms
| Platform | API | MCP | Notes |
|----------|-----|-----|-------|
| Ahrefs | API v3 (plan dependent, API units) | Official Ahrefs MCP server launched 2025 [verify setup in Ahrefs docs] | Ahrefs Webmaster Tools free for verified sites (site audit, backlinks); Brand Radar for AI mentions (ai-search-optimization) |
| Semrush | Semrush API (units) | Official Semrush MCP server launched 2025 [verify setup in Semrush docs] | Position tracking, Site Audit, Sensor volatility; AI visibility toolkit (ai-search-optimization) |
| DataForSEO | Pay as you go APIs: SERP, Keywords Data (Google Ads volumes), DataForSEO Labs, Backlinks, On-Page, Content Analysis | Official open source MCP server (GitHub `dataforseo/mcp-server-typescript`) | Best for custom pipelines; SERP depth pricing changed after num=100 [Unverified details] |
| Similarweb | API (enterprise) | [Unverified] | Traffic estimates, zero-click and AI referral studies |
| Moz, Majestic | APIs | Community | Link metrics |

Use third party numbers as estimates and say so; prefer Search Console for your own site.

## 9. MCP servers useful for SEO in Claude Code
| Server | Publisher | What it enables | Status |
|--------|-----------|-----------------|--------|
| Google Analytics MCP | Google (official, read-only) | GA4 reports and admin info for organic analysis | Released 2025 [Official, 2025-07] |
| Chrome DevTools MCP | Google Chrome team (official) | Performance traces (LCP, INP), network, console, rendering checks | Public preview from 2025-09 |
| Playwright MCP | Microsoft (official) | Headless browsing, rendered DOM, screenshots | Stable |
| Search Console MCP | Community servers on GitHub (several) | Search Analytics queries, URL Inspection, sitemaps | No official Google server known as of this writing [Unverified; check] |
| Ahrefs MCP | Ahrefs (official) | Keywords, backlinks, competitors | Plan dependent |
| Semrush MCP | Semrush (official) | Keywords, domains, positions | Plan dependent |
| DataForSEO MCP | DataForSEO (official) | SERP, keywords, backlinks, on-page | Pay per call |
| Bing Webmaster MCP | Community | Bing stats, URL submission | [Unverified] |
| Firecrawl or similar crawl MCPs | Vendors and community | Fetch and parse pages at scale | Check licensing |

Adding servers in Claude Code (generic patterns; follow each vendor's README):
```bash
# local stdio server
claude mcp add <name> -- npx -y <package>@<version>
# remote HTTP server
claude mcp add --transport http <name> <https-url>
```
Rules: keep API keys in environment variables or the client's secret store, never in the repo or in `ads-master/`; prefer read-only scopes; log which connector and date range produced each number.

## 10. Script library (where to find them)
| Script | Location |
|--------|----------|
| GSC Search Analytics pull, URL Inspection batch | This file, section 2 |
| PSI and CrUX checks | This file, section 4 |
| IndexNow submission | This file, section 5 |
| Log parsing, Googlebot verification, DuckDB crawl share | [crawl-index-render.md](crawl-index-render.md) |
| SERP clustering | [keyword-research-and-topical-maps.md](keyword-research-and-topical-maps.md) |
| Cannibalization, decay, CTR curve, brand split SQL | [measurement-and-reporting.md](measurement-and-reporting.md), [on-page-and-content.md](on-page-and-content.md) |
| JSON-LD extraction and required field check | [structured-data.md](structured-data.md) |
| hreflang reciprocity validator | [international-seo.md](international-seo.md) |
| Redirect map validator | [migrations-playbook.md](migrations-playbook.md) |

Sitemap and status sampler:
```python
import random, sys, requests
import xml.etree.ElementTree as ET
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

def urls_from(sitemap_url):
    root = ET.fromstring(requests.get(sitemap_url, timeout=30).content)
    if root.tag.endswith("sitemapindex"):
        for loc in root.findall("sm:sitemap/sm:loc", NS):
            yield from urls_from(loc.text.strip())
    else:
        for loc in root.findall("sm:url/sm:loc", NS):
            yield loc.text.strip()

urls = list(urls_from(sys.argv[1]))
sample = random.sample(urls, min(200, len(urls)))
bad = []
for u in sample:
    r = requests.get(u, allow_redirects=False, timeout=20, headers={"User-Agent": "sitemap-audit"})
    robots = r.headers.get("X-Robots-Tag", "")
    if r.status_code != 200 or "noindex" in robots.lower() or 'name="robots" content="noindex' in r.text.lower():
        bad.append((u, r.status_code, robots))
print(f"{len(urls)} URLs in sitemaps, sampled {len(sample)}, problems {len(bad)}")
for b in bad:
    print(b)
```
