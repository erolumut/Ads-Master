# Tools, APIs and MCP Servers (and the legal limits)

Catalog of data sources Claude can use for market intelligence, how to call them, and where the legal and ethical lines are. Status labels: [Official] documented by the provider; [K] known from prior documentation, re-check before use; [Unverified] could not be confirmed in the October 2026 sweep.

## 1. Built in capabilities
| Capability | Use | Notes |
|------------|-----|-------|
| Web search and web fetch (Claude Code tools) | Read public pages: pricing pages, landing pages, ad library pages that render without login, news, filings | Respect robots rules and terms; fetch at human speed; record capture dates |
| Local scripts (Python) | Clean exports, compute indexes, cluster text | Run with `python3 -I` on downloaded files; keep scripts outside data folders |
| Files in `ads-master/data/imports/` | Exports the human drops (Auction Insights, SEO tool exports, review exports) | Preferred for paid tool data without API |

## 2. Official APIs and datasets
| Source | Endpoint or access | What you get | Access requirements | Status |
|--------|--------------------|--------------|---------------------|--------|
| Meta Ad Library API | `GET https://graph.facebook.com/v<version>/ads_archive` with required `ad_reached_countries` and `search_terms` or `search_page_ids` | EU delivered ads (all categories) and political or issue ads: creative text, dates, platforms, EU reach, targeting summaries, payer and beneficiary | Meta developer account, identity confirmation at facebook.com/ID (government ID, proof of residence), `ads_read` permission, access token; processing time reported from days to weeks | [Official; access steps via 2026 secondary guides] |
| Google Ads API | Auction Insights metrics are not generally available through the API (access has been restricted) [Unverified current status]; use UI or report exports. KeywordPlanIdeaService and keyword historical metrics for volumes | Keyword ideas, volumes, competition, bid ranges | Developer token, account access | [K] |
| Google Search Console API | Search Analytics query | Our queries, clicks, impressions, positions | Property access | [K] |
| Google Trends | UI exports; Trends API alpha announced in 2025 | Relative interest; API gives consistently scaled data | Alpha access [Unverified current status] | [K] |
| Google political ads transparency data | Public datasets (for example BigQuery public data) | Political ad spend where Google serves political ads | Google Cloud account | [K] |
| Google Ads Transparency Center | Web UI | Competitor ads by domain and region | No official commercial ads API; only the political ads BigQuery dataset is official [Practitioner consensus, 2026]; third-party scrapers exist (check terms) | [K] |
| TikTok Commercial Content API | developers.tiktok.com (query ads, ad details, advertisers; docs updated 2026-09-01) | EU/EEA, UK and Swiss commercial content library data (advertiser, dates, targeting, reach) | Application and approval; eligibility reported as researcher focused [Contested] | [Official docs; scope Contested] |
| YouTube Data API | `commentThreads`, `search`, `videos` | Public video metadata and comments | API key, quota | [K] |
| Reddit Data API | OAuth API | Posts and comments | Data API terms: commercial use requires an agreement with Reddit; respect rate limits | [K] |
| App store reviews | Apple App Store Connect API and Google Play Developer API for own apps; public review pages for others | Reviews and ratings | Own app credentials | [K] |
| Trustpilot API | Business units, reviews | Reviews for own business; public data per terms | API key | [K] |
| Wayback Machine (Internet Archive) | `https://web.archive.org/` and CDX API | Historical snapshots of pages | Public, rate limited | [K] |

Example: keyword volumes through the Google Ads API (pseudo code, use the official client library):
```
service = client.get_service("KeywordPlanIdeaService")
request.customer_id = "<CID>"
request.language = "languageConstants/1000"          # English; use the target language constant
request.geo_target_constants = ["geoTargetConstants/2840"]  # United States; use the target market
request.keyword_seed.keywords.extend(["crm for dentists", "dental scheduling software"])
for idea in service.generate_keyword_ideas(request=request):
    print(idea.text, idea.keyword_idea_metrics.avg_monthly_searches, idea.keyword_idea_metrics.competition)
```
Accounts without meaningful spend may see ranges rather than exact volumes [K].

## 3. Commercial SEO and market data tools
| Tool | Strengths | API | Notes |
|------|-----------|-----|-------|
| Semrush | Organic and paid keyword databases by country, Keyword Gap, Backlink Gap, Advertising and PLA research, traffic analytics, AI visibility features | Yes (API units) | Estimates; database per country |
| Ahrefs | Backlink index, organic keywords, content gap, Brand Radar (AI mentions) | Yes (API v3) | Estimates |
| Similarweb | Traffic, channel mix, referral sources, audience overlap, app intelligence | Yes | Panel based; weak for small sites |
| SpyFu | Paid keyword and ad copy history (US heavy) | Yes | Estimates |
| DataForSEO | SERP, keyword, backlink and other data APIs priced per request | Yes | Raw data; you build the analysis |
| SerpApi and similar SERP APIs | Structured SERP results, including some Google properties | Yes | Check terms of the underlying sites |
| AI visibility platforms (Profound, Peec AI, Otterly.AI, Scrunch, Evertune and similar) | Prompt tracking, share of voice, citations | Some offer APIs or exports | Methods vary [Unverified feature sets] |
| Price trackers (Prisync, Price2Spy, Competera, Keepa for Amazon) | Price monitoring | Yes for most | Check retailer terms |
| Listening tools (Brandwatch, Talkwalker, Meltwater, Brand24) | Mentions, sentiment, volume | Yes | Licensed data |
| Page monitors (Visualping, Distill, ChangeTower) | Change alerts | Some | Low frequency checks |

## 4. MCP servers (let Claude query tools directly)
| Server | Provider | What it exposes | Status |
|--------|----------|-----------------|--------|
| Ahrefs MCP | Ahrefs (official) | Ahrefs data via API key | [K; verify current availability and plan requirements] |
| Semrush MCP | Semrush (official, remote; launched 2025-09) | Semrush Standard and Trends API data; endpoint `https://mcp.semrush.com/v2/mcp` (streamable HTTP; some guides still list v1); OAuth by default or API key in the Authorization header; consumes API units; official apps in Claude and ChatGPT, Perplexity connector 2026-06 | [Official, developer.semrush.com 2026] |
| Similarweb MCP | Similarweb (official, remote; announced 2025-09-25) | Traffic, channel and market data; endpoint `https://mcp.similarweb.com` (streamable HTTP); needs a plan with API access (API-only, Business or Enterprise) and consumes data credits like API calls | [Official, Similarweb docs 2026] |
| DataForSEO MCP | DataForSEO (official, open source) | SERP, keywords, backlinks, on-page APIs | [K] |
| Apify MCP | Apify (official) | Runs Apify actors, including community scrapers for ad libraries and reviews | [K]; actor use must respect target site terms |
| Firecrawl MCP, Bright Data MCP | Vendors | Page crawling and extraction | [K]; terms and robots apply |
| Playwright MCP | Microsoft (official, open source) | Browser automation | [K]; manual style browsing only; no login bypass |
| Google Search Console MCP servers | Community | GSC data for own properties | [K; review code and permissions] |
| Google Ads MCP server | Google (official, open source, read only, released 2025-10) | Read Google Ads data for own accounts (Auction Insights still comes from UI or report exports [Unverified API coverage]) | [K, per research/google-ads.md] |
| TikTok for Business MCP server | TikTok (official, announced May 2026) | TikTok Ads API endpoints for own accounts | [K, per research/tiktok-ads.md] |
| LinkedIn Ad Library MCP | Community | Query the LinkedIn Ad Library | [K, per research/linkedin-ads.md; review code and terms] |
Rules for MCP use: install only servers the human approves; prefer official servers; review scopes; read only; store keys outside the repo; log which server produced which data.

## 5. Legal and ethical limits
### 5.1 Terms of service and access
- Most platforms prohibit automated collection without permission in their terms (Meta, LinkedIn, Amazon, G2 and others). Use official APIs, licensed tools or manual review [Practitioner consensus].
- Courts in the US have narrowed some anti scraping claims for public data (hiQ Labs v. LinkedIn, Ninth Circuit 2022 on the computer fraud statute; Meta v. Bright Data, N.D. Cal. 2024, on logged out scraping of public data), but breach of contract and other claims remain possible, and outcomes depend on facts and jurisdiction [K; not legal advice].
- Never bypass logins, paywalls, CAPTCHAs, IP blocks or rate limits. Never create fake accounts or use someone else's credentials.
- Respect robots.txt and crawl at low frequency.

### 5.2 Personal data
- Reviews, comments and profiles contain personal data. GDPR (EU), UK GDPR, KVKK (Turkey) and US state laws apply to collection and storage. Collect the minimum, anonymize, delete raw data after coding unless the human approves retention [K].
- Do not build profiles of individual reviewers or community members.

### 5.3 Competition law and trade secrets
- Do not exchange competitively sensitive information (prices, plans, bids) with competitors directly or through intermediaries.
- Do not solicit confidential information from competitors' employees, former employees, agencies or partners. Public information only.
- Mystery shopping: acting as a normal customer is generally acceptable; misrepresenting identity to obtain non public information is not. Get human approval and check local law [Practitioner consensus].

### 5.4 Using what you find
- Do not reuse competitor creative, copy, images or video; use them as reference for angles only.
- Comparative claims and competitor trademarks in ads: platform trademark policies plus comparative advertising law (EU Directive 2006/114/EC, US FTC standards, Turkey commercial advertising regulation). Human and legal approval required.
- Customer quotes from public reviews cannot be used as testimonials in ads without permission.

## 6. Data handling standard
| Item | Standard |
|------|----------|
| Capture metadata | Source, URL, capture date and time, market, language, device, logged in or out |
| Storage | Coded findings in outputs; raw exports in `ads-master/data/imports/` only with approval; never commit customer or personal data |
| Retention | Raw personal data deleted after coding; coded themes kept |
| Provenance | Every number cites its tool and date; estimates labeled |

## 7. Choosing tools by tier
| Tier | Minimum stack |
|------|---------------|
| Starter | Free sources: ad libraries, Transparency Center, Google Trends, Keyword Planner, Search Console, manual review sampling, manual AI panel |
| Growth | Plus one SEO suite (Semrush or Ahrefs), page change monitor, AI visibility tool or structured manual panel |
| Scale | Plus Similarweb or equivalent, price tracker (ecommerce), listening tool, Meta Ad Library API for EU |
| Enterprise | Plus data APIs into a warehouse, automated monthly dashboards, win and loss program, licensed review data |

## 8. More example calls (public, documented endpoints; verify before use)
Wayback Machine snapshots of a competitor pricing page (CDX API):
```bash
curl -s "https://web.archive.org/cdx/search/cdx?url=competitor.com/pricing&output=json&from=2025&to=2026&filter=statuscode:200&collapse=digest" | head -50
# then open https://web.archive.org/web/<timestamp>/competitor.com/pricing for each changed version
```
Public App Store reviews for any app (Apple customer reviews RSS feed, JSON):
```bash
curl -s "https://itunes.apple.com/us/rss/customerreviews/page=1/id=<APP_ID>/sortby=mostrecent/json"
```
YouTube comments on a public video (YouTube Data API v3, API key, quota applies):
```bash
curl -s "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId=<VIDEO_ID>&maxResults=100&key=${YT_KEY}"
```
Strip author names and channel IDs before storing.

## 9. Decision tree: may I automate this collection?
```
Is there an official API or licensed tool for this data?
  yes -> Use it within its terms and quotas.
  no  -> Is the page public without login, and do robots rules and the site terms allow automated access?
          no  -> Manual review only (human speed, small samples), or ask the human to license a tool.
          yes -> Does the data include personal data?
                  yes -> Collect the minimum, anonymize, document the lawful basis (GDPR, KVKK); get human approval.
                  no  -> Low frequency automated checks are acceptable; log source and capture time.
Never: bypass logins, CAPTCHAs or blocks; use fake accounts; resell or publish collected data.
```

## 10. Costs and approvals
| Item | Typical pricing model | Approval |
|------|-----------------------|----------|
| SEO suites | Monthly subscription plus API units | Human, within tool budget |
| Data APIs (SERP, keywords) | Per request | Human sets a monthly cap |
| AI visibility platforms | Per prompt and engine volume | Human |
| Listening tools | Annual contracts | Human |
| Panels for surveys | Per complete | Human |
Record which paid sources were used in each output's Data used table.
