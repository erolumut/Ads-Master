# Crawl, Index and Render

> Scope: how Google and Bing discover, fetch, render and index URLs; rendering strategy (CSR, SSR, SSG, ISR); indexing controls and triage of every Page indexing status; canonicalization; faceted navigation; pagination; crawl budget; log file analysis. Server level settings and framework code are in [technical-seo.md](technical-seo.md).

## 1. The pipeline
1. Discovery: links (`<a href>`), sitemaps, redirects, feeds. URLs found only in JavaScript events or `onclick` handlers are often never discovered.
2. Crawl: Googlebot (smartphone for almost all sites) fetches the URL within the site's crawl capacity and Google's crawl demand.
3. Render: the Web Rendering Service runs an evergreen Chromium, executes JavaScript, and builds the DOM. Rendering may lag the crawl. It does not click, scroll like a user, keep cookies or local storage between loads, or grant permissions.
4. Index: Google evaluates content, picks a canonical among duplicates, and stores signals. Not every crawled page is indexed.
5. Serve: ranking systems choose results per query; AI features (AI Overviews, AI Mode) draw from the same index and require that a page be indexed and eligible for a snippet [Official, AI features doc].

Bing differs: Bingbot renders JavaScript less predictably, puts heavy weight on sitemaps with accurate `lastmod`, accepts IndexNow pushes, and honors `crawl-delay`. Treat raw HTML completeness as mandatory for Bing and AI crawlers.

## 2. Rendering strategy decision
| Mode | What the crawler gets in raw HTML | SEO risk | Use for |
|------|-----------------------------------|----------|---------|
| SSG (static generation) | Full HTML | Lowest; stale content if not rebuilt | Marketing pages, docs, blog, stable categories |
| ISR (incremental static regeneration) | Full HTML, refreshed on a timer or on demand | Low; check revalidation actually fires | Large catalogs, listings, programmatic pages |
| SSR (server render per request) | Full HTML | Low; TTFB and server load risk | Personalized or fast changing pages, search with indexable results |
| Streaming SSR | HTML in chunks | Medium; status code locked at first byte; metadata placement | Complex apps; test 404 and metadata |
| CSR (client side render) | Shell with little content | High; delayed or failed render, invisible to non rendering crawlers | Logged in apps, dashboards, non indexable tools |
| Hybrid (SSR shell plus client data) | Partial | Medium to high; content fetched after hydration is missing in raw HTML | Avoid for indexable content |

Decision rule: any page you want to rank must deliver its primary content, title, meta robots, canonical, hreflang, internal links and JSON-LD in the server HTML. Client side enhancement on top is fine.

JavaScript SEO checklist [Official, Google JavaScript SEO basics]:
- Links are `<a href="/path">`. Buttons with `onclick` navigation are not links.
- Each view has its own URL via the History API. Fragments (`#/route`) are ignored for indexing.
- Do not put noindex in raw HTML and remove it with JS: Google may skip rendering noindex pages.
- Do not change the canonical with JavaScript to a different URL than the raw HTML declares. Set it once, server side.
- Return real HTTP status codes. A client side "not found" view on a 200 is a soft 404.
- Lazy load with native `loading="lazy"` or IntersectionObserver, not scroll events. Content requiring a click (tabs that fetch on click, "load more" without links) may not be seen.
- Do not block JS, CSS or API endpoints needed for rendering in robots.txt.
- Keep HTML payloads lean. Since Google's crawler documentation reorganization (2026-02, expanded 2026-03-31), Googlebot for Google Search fetches only the first 2 MB of an HTML or supported text file (uncompressed, HTTP headers included) and the first 64 MB of a PDF; the 15 MB figure is now the default for Google's other crawlers and fetchers. Anything past the cutoff is not fetched, rendered or indexed, and each referenced resource (CSS, JS) has its own limit [Official, 2026-02]. Google's John Mueller called it a documentation clarification rather than a behavior change, while a Google contact told DebugBear the old documentation was wrong [Contested on whether behavior changed; the limit itself is documented]. Large inline hydration JSON (`__NEXT_DATA__`, Nuxt payloads) can push content past the cutoff; keep the HTML document well under 2 MB and put critical content, links and structured data early in the source.

Render testing procedure:
1. Raw: `curl -s -A "<Googlebot UA>" URL > raw.html`.
2. Rendered: Search Console URL Inspection > Test live URL > View tested page > HTML. Or headless Chromium (Playwright, Puppeteer, Chrome DevTools MCP) saving `document.documentElement.outerHTML`.
3. Diff: word count, internal link count, title, canonical, robots, hreflang, JSON-LD blocks. Screaming Frog with JavaScript rendering enabled reports "JavaScript content" and "links only in rendered HTML" at scale.
4. Any money template where content or links exist only after rendering is a High severity finding.

## 3. Indexing controls: pick the right tool
| Goal | Use | Do not use |
|------|-----|-----------|
| Remove a page from the index permanently | `noindex` (crawlable) or 404/410 | robots.txt disallow (blocks seeing the noindex) |
| Consolidate duplicates | 301 or 308 redirect; else `rel=canonical` | noindex on duplicates that have links (wastes equity) |
| Save crawl on infinite spaces | robots.txt disallow patterns | noindex (still crawled) |
| Hide quickly in an emergency (leaked data) | Search Console Removals tool (temporary, about 6 months) plus permanent fix | Removals alone |
| Keep staging out | HTTP auth or IP allowlist | robots.txt alone |
| Keep a section out of snippets and AI features | `data-nosnippet`, `max-snippet` | noindex |
| PDFs and files | `X-Robots-Tag` header; `Link: <url>; rel="canonical"` header | Meta tags (impossible in PDFs) |

## 4. Page indexing report triage
Pull the Page indexing report per sitemap (filter by sitemap) and per URL pattern. Sample 20 URLs per reason with URL Inspection (or the URL Inspection API, 2,000 calls per day per property).

| Status | Meaning | Is it a problem? | Action |
|--------|---------|-----------------|--------|
| Crawled, currently not indexed | Google fetched it and chose not to index | Yes if money or unique pages | Raise quality and uniqueness, consolidate near duplicates, add internal links from strong pages, check rendering; noindex if low value |
| Discovered, currently not indexed | Known but not yet crawled | Yes at scale | Reduce URL waste, improve server speed, prioritize with internal links and sitemaps; often a site quality signal for new or low trust sites |
| Duplicate without user-selected canonical | Duplicates with no canonical | Usually | Add self or consolidating canonicals; fix parameter generation |
| Duplicate, Google chose different canonical than user | Your canonical ignored | Yes when you need your choice | Align redirects, internal links, sitemaps, hreflang with your canonical; make content truly identical or truly different |
| Alternate page with proper canonical tag | Working as intended | No | None |
| Excluded by 'noindex' tag | Your noindex | Check for accidents | Crawl sample to confirm intent |
| Blocked by robots.txt | Disallowed | Check for accidents | Confirm pattern intent |
| Indexed, though blocked by robots.txt | Indexed without content | Usually | Allow crawl and noindex, or keep blocked if harmless |
| Page with redirect | Redirecting URL | No unless linked internally or in sitemap | Update links and sitemaps |
| Soft 404 | Looks empty or error | Yes | Real 404 or real content; thin category pages with zero products trigger this |
| Not found (404) | 404 | Only if valuable or linked | Redirect valuable URLs with links; fix internal links |
| Server error (5xx) | Fetch failed | Yes | Server capacity, timeouts, WAF rules blocking Googlebot |
| Redirect error | Loop, chain over 10, bad URL | Yes | Fix chains |
| Blocked due to unauthorized request (401) or access forbidden (403) | Auth or WAF | Yes if public pages | Allow verified Googlebot in WAF and bot management |

WAF and bot management: Cloudflare, Akamai, Fastly and others can challenge or block crawlers. Verify Googlebot by reverse DNS (`googlebot.com`, `google.com`, `googleusercontent.com` for some fetchers) or Google's published IP range files, and allow it. Check the Crawl Stats report for 403 and 429 spikes after any security change.

## 5. Canonicalization
Google picks one canonical per duplicate cluster using signals, strongest first [Official, consolidate duplicate URLs doc; ordering Practitioner consensus]:
1. Redirects (301, 308)
2. `rel=canonical` in HTML or HTTP header
3. Sitemap inclusion
4. Internal links pointing consistently to one version
5. HTTPS over HTTP, cleaner URLs
6. hreflang cluster consistency

Rules:
- Every indexable page has a self referencing absolute canonical.
- Canonical targets must be 200, indexable, not redirected, and in the sitemap.
- One canonical tag per page. Two conflicting tags (theme plus plugin) means Google may ignore both.
- Do not canonicalize paginated pages to page 1, filtered pages with different content to the unfiltered page (Google may ignore it), or different language versions to each other.
- Cross domain canonicals are allowed for syndicated content; syndication partners should canonicalize to you or noindex, otherwise the partner may outrank you.

## 6. Faceted navigation [Official, Google faceted navigation doc, December 2024]
Facets create combinatorial URL explosions that consume crawl and dilute signals. Decide per facet type:

| Facet type | Demand check | Treatment |
|------------|-------------|-----------|
| Category defining (brand, product type, gender, material, use case) with search demand | Keyword volume and GSC queries exist; inventory at least the gate (for example 6 or more products) | Indexable static URL (`/shoes/running/womens/`), unique title, H1, intro, self canonical, in sitemap, linked from parent |
| Refinements without demand (size, price ranges, color for most catalogs, rating) | No meaningful queries | Not indexable: parameters, disallowed in robots.txt or kept out via fragments (`#`) or POST forms; links `rel="nofollow"` optional |
| Sort orders, view modes, page size | None | Never indexable; disallow pattern |
| Multi select combinations (two or more values in one facet) | Almost never | Disallow |
| Empty combinations (zero results) | None | Return 404, not a 200 empty page |

Implementation rules:
1. Consistent parameter order and casing (always `?color=red&size=9`, never both orders).
2. Indexable facet URLs are path based or whitelisted parameters generated only by internal links you control.
3. Non indexable facets: prefer robots.txt disallow patterns to stop crawl; Google notes that noindex and canonical do not stop crawling.
4. Measure: log share of Googlebot hits on parameter URLs before and after (target: under 10% to 20% of crawl on non indexable URLs for large catalogs [Practitioner consensus]).
5. Never block facets that already drive meaningful traffic without first creating an indexable static equivalent and redirecting.

## 7. Pagination and infinite scroll [Official, Google pagination doc]
- Give each page a unique URL (`?page=2` or `/page/2/`). Google no longer uses `rel=prev/next` (since 2019) but Bing may; harmless to keep.
- Self canonical on each paginated page. Do not canonicalize page 2 to page 1.
- Link pages with crawlable `<a href>` (next, previous, and ideally numbered pages).
- Do not noindex paginated pages by default: products on deeper pages need the crawl path. Exception: noindex deep pages of thin archives only if items are reachable another way.
- Infinite scroll and "load more": back them with paginated URLs, update the URL with `history.pushState` as the user scrolls, and render a link to the next page in HTML.
- Titles on page 2 and later can append "Page 2" to avoid duplicate titles.

## 8. Crawl budget
When it matters [Official, Google large site crawl budget doc]: sites with roughly 1 million or more unique pages changing weekly, or 10,000 or more pages changing daily, or a large share of URLs stuck in "Discovered, currently not indexed". For most sites under 10,000 URLs, crawl budget is not the bottleneck; quality and internal linking are.

Crawl budget = crawl capacity (how much your server can take; reduced by slow responses and errors) x crawl demand (popularity and staleness of URLs).

Levers:
| Lever | Action |
|-------|--------|
| Server speed | Average response time in Crawl Stats trending down; cache HTML for bots and users alike |
| Errors | 5xx and timeouts under 1% of requests |
| URL waste | Disallow infinite spaces; remove session IDs; fix parameter generation; stop linking to redirects |
| Duplicates | Consolidate with redirects |
| Freshness signals | Accurate `lastmod`, `ETag` or `Last-Modified` for 304 responses |
| Priority | Internal links and sitemaps toward money pages; remove links to low value pages from global navigation |
| Soft 404s | Fix; they waste crawl |

Crawl Stats report (Settings > Crawl stats) gives: total requests, download size, average response time, host status (robots.txt fetch, DNS, server connectivity), breakdown by response, file type, purpose (discovery vs refresh) and Googlebot type. Review monthly; export before and after releases.

## 9. Log file analysis
Logs are the only full record of what crawlers actually fetched. Use monthly at Scale and Enterprise, and for any indexing or migration problem.

Sources: origin server access logs (nginx, Apache), CDN logs (Cloudflare Logpush, Fastly real time logging, Akamai DataStream, Vercel log drains, Netlify log drains). Ask for 30 days minimum, fields: timestamp, IP, method, URL, status, bytes, user agent, response time, host.

Verify bots before analysis: user agents are spoofed. Keep only requests whose IP reverse resolves to Google or Bing domains and forward resolves back, or that fall in the published IP ranges.

Core questions and metrics:
| Question | Metric |
|----------|--------|
| Where does Googlebot spend crawl? | Share of hits by directory, template and parameter pattern |
| Are money pages crawled often enough? | Days since last crawl per priority URL; hits per URL per month |
| Is crawl wasted? | Share of hits on non indexable, redirected, 404 and parameter URLs |
| Are there errors only bots see? | 5xx and 429 by bot, time of day |
| Orphans | URLs crawled by Googlebot but absent from your crawl and sitemaps |
| New page discovery | Days from publish to first Googlebot hit |
| Render resource fetching | Hits on JS and CSS from Googlebot (should exist) |

DuckDB example over a combined log converted to CSV (`ts, ip, method, url, status, bytes, ua, rt_ms`):
```sql
-- Googlebot share of crawl by top level directory and status
SELECT
  regexp_extract(url, '^/([^/?]*)', 1) AS section,
  status,
  count(*) AS hits,
  round(100.0 * count(*) / sum(count(*)) OVER (), 2) AS pct
FROM read_csv_auto('logs_verified_googlebot.csv')
GROUP BY ALL
ORDER BY hits DESC
LIMIT 50;

-- Parameter waste
SELECT
  CASE WHEN url LIKE '%?%' THEN 'parameter' ELSE 'clean' END AS url_type,
  count(*) AS hits
FROM read_csv_auto('logs_verified_googlebot.csv')
GROUP BY ALL;
```
Python bot verification helper:
```python
import socket

def is_google(ip: str) -> bool:
    try:
        host = socket.gethostbyaddr(ip)[0]
    except OSError:
        return False
    if not host.endswith(('.googlebot.com', '.google.com', '.googleusercontent.com')):
        return False
    try:
        return ip in socket.gethostbyname_ex(host)[2]
    except OSError:
        return False
```
Cache results per IP; logs repeat the same IPs. Tools: Screaming Frog Log File Analyser, Botify, Oncrawl, JetOctopus, or the SQL above.

## 10. Getting new and updated URLs crawled
| Method | Engine | Notes |
|--------|--------|-------|
| Internal links from frequently crawled pages (home, hubs, category) | All | Fastest durable method |
| XML sitemap with accurate `lastmod` | Google, Bing | Submit once; keep updated automatically |
| URL Inspection > Request indexing | Google | Manual, low daily quota; use for a few critical URLs only |
| Indexing API | Google | Officially only for JobPosting and BroadcastEvent (livestream) pages. Google warns that other use is not supported and may lose access [Official] |
| IndexNow | Bing, Yandex, Seznam, Naver and other participating engines (not Google) | Push changed URLs on publish, update and delete; see [tools-api-mcp.md](tools-api-mcp.md) |
| Bing URL Submission API and Bing Webmaster Tools | Bing | Quota per site per day shown in Bing Webmaster Tools |

## 11. Duplicate and near duplicate content
- Find exact duplicates by content hash and near duplicates with crawler similarity features (Screaming Frog near duplicates, Sitebulb duplicate content hints).
- Typical sources: HTTP and HTTPS or www variants, trailing slashes, uppercase, parameters, printer pages, session IDs, faceted and sorted views, product variants on separate URLs with identical copy, location pages with swapped city names, syndicated content.
- Fix order: stop generation, redirect, canonical, differentiate content, noindex.

## 12. Bing specific checks
- Verify the site in Bing Webmaster Tools (import from Search Console is the fastest path).
- Submit sitemaps; Bing reports per sitemap processing.
- Bing URL Inspection shows index status and the "Live URL" fetch.
- Site Explorer reveals crawl, index and error state by folder.
- Bing honors `crawl-delay`; do not set it unless the server cannot cope.
- IndexNow integration exists in many CDNs and CMS plugins (Cloudflare Crawler Hints, Yoast and Rank Math IndexNow options); confirm it fires on update and delete.
