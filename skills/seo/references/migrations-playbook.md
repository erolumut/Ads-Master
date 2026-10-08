# Site Migration Playbook

> Scope: any change that alters URLs, domains, platforms, rendering, templates or site structure at scale. Phases, risk assessment, benchmarks, redirect mapping, staging QA, launch runbook, post launch monitoring, rollback criteria, and platform specific notes. Migrations are where SEO value is most often destroyed; this agent may recommend a no-go.

## 1. Migration types and risk
| Type | Examples | Risk | Typical temporary impact [Practitioner consensus] |
|------|----------|------|------------------------------------------------|
| Protocol or host | HTTP to HTTPS, www to non-www | Low | Minimal if 1:1 redirects |
| Domain change | Rebrand to new domain, ccTLD to .com | High | Dips for weeks to months; Google says moves can take time to process |
| URL structure | New folder paths, slug changes | Medium to high | Depends on share of URLs changed |
| Platform or CMS | Magento to Shopify, WordPress to Next.js, Webflow to custom | High | Template, rendering and URL changes combined |
| Rendering or framework | SSR to CSR, framework upgrade, JS router change | Medium to high | Invisible content or links if mishandled |
| Redesign or template | New navigation, content removed, layout changes | Medium | Internal links and content changes alter rankings |
| Consolidation | Merging sites, subdomain to subfolder | Medium to high | Usually positive long term if done well |
| International restructure | New locales, hreflang changes | Medium | Wrong versions ranking |
| Hosting, CDN, WAF | Provider change | Low to medium | Bot blocking, speed, status code changes |

Combining several types in one launch multiplies risk. Prefer sequencing (for example, replatform with identical URLs first, then restructure).

## 2. Timeline overview
| Phase | When | Output |
|-------|------|--------|
| 0. Scope and go/no-go criteria | T minus 12 to 8 weeks | Migration brief, risk register, success metrics, rollback criteria |
| 1. Benchmark | T minus 8 to 6 weeks | Crawl, GSC and GA4 exports, rankings, backlinks, top pages list, CWV |
| 2. Mapping | T minus 6 to 3 weeks | Complete redirect map, content mapping, metadata mapping |
| 3. Staging build and QA | T minus 4 to 1 weeks | Staging crawl reports, QA sign-off |
| 4. Launch | T | Runbook executed, smoke tests |
| 5. Hypercare | T plus 1 to 14 days | Daily checks, fixes |
| 6. Stabilize | T plus 2 to 12 weeks | Weekly reporting vs benchmark |
| 7. Close | T plus 3 to 6 months | Final report, lessons, redirect retention plan |

Avoid launching in peak season, during a core update rollout if it can be avoided, or right before holidays when the team is unavailable.

## 3. Phase 0: migration brief
```markdown
# Migration brief: <project>
- Type(s): <platform, domain, URL, design>
- Launch window: <date range>, freeze dates, team availability
- Scope: domains, subdomains, languages, URL count by template
- Why: <business reason>
- SEO risks: <list with severity>
- Success metrics: organic clicks and revenue within <x>% of benchmark by <date>; indexation of priority URLs over 95% within <n> weeks; no increase in 404s from external links
- Go/no-go criteria: redirect map complete for 100% of URLs with clicks, links or conversions in last 16 months; staging crawl passes; analytics verified
- Rollback criteria: <e.g., sitewide 5xx over 2% for 1 hour, noindex on production templates, conversion tracking broken>
- Owners: SEO, dev lead, analytics (measurement), content, PR/paid (landing pages)
```

## 4. Phase 1: benchmark
Collect and store in `ads-master/data/imports/` and `ads-master/outputs/seo/`:
1. Full crawl of the current site (all indexable URLs, status, canonicals, titles, H1, meta robots, hreflang, structured data, internal link counts, word counts).
2. Search Console: 16 months of page and query data (API or bulk export); top pages by clicks; Page indexing state; sitemaps.
3. GA4: landing pages from Organic Search with sessions, key events, revenue (last 12 months).
4. Backlinks: all URLs with external referring domains (Ahrefs, Semrush, GSC Links export).
5. Rankings: priority query set (top 20 or 50 depth).
6. Logs: 30 days of Googlebot activity if available.
7. CWV field data per template (CrUX).
8. Paid and email landing pages (google-ads, meta-ads, CRM) that depend on current URLs.

URL universe = union of crawl URLs, sitemap URLs, GSC pages with impressions, GA4 landing pages, backlink target URLs, log URLs, paid landing pages. Every URL in the universe needs a mapping decision.

## 5. Phase 2: redirect mapping
Rules:
1. 1:1 to the closest equivalent page. Not to the homepage, not to a parent category unless the content truly merged there.
2. One hop from old URL to final URL. Update old redirects (chains from previous migrations) to point at the new final URL.
3. 301 or 308 (permanent). Never 302 for a permanent move.
4. Preserve query parameters only where they carry meaning (pagination, valid filters); strip tracking.
5. Removed content with no equivalent: 404 or 410, unless it has backlinks or traffic, in which case redirect to the most relevant alternative.
6. Also map images, PDFs and other files with links or image search traffic.
7. Keep redirects at least one year, ideally permanently; for domain changes keep the old domain registered and redirecting indefinitely [Official, site moves guidance].

Redirect map format (CSV):
```csv
old_url,new_url,type,priority,clicks_16m,referring_domains,notes
https://old.example.com/shoes/trail-runner-2.html,https://www.example.com/products/trail-runner-2,301,P1,18420,37,PDP
https://old.example.com/category/trail-running,https://www.example.com/running/trail-shoes/,301,P1,40210,64,Category
https://old.example.com/blog/2019/old-news,,410,P3,0,0,No value
```
Priority: P1 = clicks or conversions or referring domains in top 80% cumulative; P2 = any traffic or links; P3 = none.

Pattern based rules are fine for large sets but test every pattern against a sample, and list exceptions explicitly.

Redirect map validator (run against staging or production after launch):
```python
import csv, sys, requests

def check(old, expected):
    r = requests.get(old, allow_redirects=True, timeout=20, headers={"User-Agent": "migration-check"})
    hops = [h.status_code for h in r.history]
    final = r.url
    ok = (len(hops) == 1 and hops[0] in (301, 308) and final.rstrip('/') == expected.rstrip('/') and r.status_code == 200)
    return ok, hops, final, r.status_code

with open(sys.argv[1]) as f:
    for row in csv.DictReader(f):
        if row["type"] in ("301", "308") and row["new_url"]:
            ok, hops, final, status = check(row["old_url"], row["new_url"])
            if not ok:
                print(f'FAIL {row["old_url"]} hops={hops} final={final} status={status} expected={row["new_url"]}')
```
Run politely (rate limit) and in batches for large maps.

## 6. Phase 3: staging QA
Protect staging with authentication (not robots.txt alone). Crawl staging with credentials.

Checklist:
| Area | Check | Pass criteria |
|------|-------|---------------|
| Indexability | Meta robots, X-Robots-Tag on production config | No noindex on production templates (staging noindex must be environment specific) |
| robots.txt | Production version prepared | No `Disallow: /`; sitemaps declared |
| Canonicals | Self referencing on new URLs, absolute, correct host | 100% on indexable templates |
| Status codes | 200 for live pages, 404 for unknown routes | No soft 404 templates |
| Redirects | Validator on full map | 100% P1, 99% or more P2 |
| Content parity | Main content, headings, word counts vs old for top 500 pages | No unintended loss of copy, FAQs, reviews |
| Internal links | Navigation, breadcrumbs, related modules, footer | Link counts to priority pages not reduced; no links to old URLs |
| Metadata | Titles, descriptions, H1 mapped | Top pages unchanged unless intended |
| Structured data | Same or better coverage | Rich Results Test passes on each template |
| hreflang | Reciprocal and pointing to new URLs | Script passes |
| Rendering | Raw vs rendered parity | Critical content in raw HTML |
| Performance | Lab CWV per template | Not worse than old site |
| Analytics | GA4 tags, key events, consent, cross domain | Measurement agent sign-off |
| Sitemaps | New XML sitemaps with only new canonical URLs | Generated from source of truth |
| Images and files | Paths mapped | Top image URLs redirect or keep paths |
| Pagination and facets | Rules carried over | Same indexability decisions |

## 7. Phase 4: launch runbook
1. Freeze content changes 48 hours before.
2. Deploy; remove staging protections from production config only.
3. Smoke test within 30 minutes: robots.txt, homepage and top 20 URLs (status, canonical, robots meta, title), 50 sample redirects from P1, sitemap URLs return 200, analytics firing.
4. Run the full redirect validator.
5. Submit new sitemaps in Search Console and Bing Webmaster Tools. Keep the old sitemap (listing old URLs) submitted for a few weeks to speed discovery of redirects [Practitioner consensus].
6. Domain change only: use Search Console Change of Address tool (old property to new) after redirects are live, and verify both properties [Official].
7. Update internal and external assets: paid campaigns final URLs (google-ads, microsoft-ads, meta-ads), email templates, GBP website links, social profiles, high value backlinks (outreach to top referring sites).
8. IndexNow ping for changed URLs (Bing and others).
9. Write a journal entry with launch time and known issues.

## 8. Phase 5 and 6: monitoring
| When | Checks |
|------|--------|
| Day 1 to 3 | Crawl Stats (5xx, 404, response time); server logs for Googlebot status codes; Page indexing for new errors; top 100 pages live tests; analytics sanity |
| Day 7 | Redirect validator again; Search Console clicks and impressions vs benchmark (expect turbulence); new URLs being indexed; old URLs showing "Page with redirect" |
| Day 14 to 30 | Rankings for priority set; indexing ratio of new sitemaps; 404s with external links; CWV field data starting to reflect new site |
| Week 6 to 12 | Recovery curve vs benchmark per template; decide on fixes for lagging templates |
| Month 3 to 6 | Final report; keep redirects; schedule backlink outreach for remaining old URL links |

Expected pattern: a temporary dip, often 10% to 30% for 2 to 8 weeks on large changes, then recovery to or above baseline if signals are preserved [Practitioner consensus; varies widely]. Losses that persist beyond 8 to 12 weeks indicate a structural problem (content removed, internal links lost, rendering, wrong redirects).

## 9. Rollback criteria
Roll back or hotfix immediately (with approval) if:
- Production serves noindex or `Disallow: /`.
- Over 2% of requests return 5xx for over an hour.
- P1 redirects fail at over 5%.
- Primary conversion tracking is broken (hand to measurement).
- Rendering fails for money templates (content missing in rendered HTML).

## 10. Platform specific notes
| Move | Notes |
|------|-------|
| To Shopify | URL prefixes are forced (`/products/`, `/collections/`, `/pages/`, `/blogs/<blog>/`); import redirects via Shopify URL redirects (check current limits for very large maps); product and collection handles become slugs; tag and filter URL behavior changes |
| To Next.js or another headless frontend | Recreate canonicals, sitemaps, robots, structured data, hreflang, 404 handling and redirects that the CMS used to provide; choose SSG, ISR or SSR per template; large redirect maps via middleware lookups or host bulk redirects (check host limits) |
| WordPress to anything | Map category, tag, author, date and attachment archives; preserve `/feed/` behavior if used; images in `/wp-content/uploads/` often have links |
| Domain consolidation (many to one) | Map each source domain URL to best target; Change of Address per domain; monitor brand queries for each old brand |
| HTTP to HTTPS | Redirect at server or CDN level; update canonicals, hreflang, sitemaps, internal links; HSTS later |
| Subdomain to subfolder (blog, docs) | Redirect 1:1, merge sitemaps, add to main navigation and internal links |

## 11. Migration report template
```markdown
# Migration status: <project> T+<n> days
- Organic clicks vs benchmark: <x%> (GSC web, same weekdays, excluding brand)
- Organic revenue or leads vs benchmark: <x%> (backend)
- Indexing: new URLs indexed <n>/<total> (<%>); old URLs dropped <n>
- Redirects: validator pass rate P1 <%>, P2 <%>
- Errors: 5xx <%>, 404 with external links <n>
- Templates lagging: <list with cause hypotheses>
- Actions this week: <list, owner, approval>
```
