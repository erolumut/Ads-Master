---
name: seo
description: Search engine optimization playbook for Google and Bing in the AI Overviews and AI Mode era. Use to audit, fix and grow organic search. Technical SEO in code (Next.js, React, Nuxt, Shopify, WordPress, Webflow, custom), crawling, JavaScript rendering, indexing, canonicals, robots.txt, XML sitemaps, redirects, hreflang, JSON-LD structured data and rich results, Core Web Vitals and INP, site architecture and internal linking, keyword research, topical maps, content briefs, refresh and pruning, programmatic SEO, E-E-A-T, spam policies, core and spam update recovery, AI Overviews CTR impact, Search Console and Bing Webmaster Tools, rank tracking after num=100, forecasting, local SEO and Google Business Profile, ecommerce, SaaS and publisher SEO (Discover, Top Stories), international SEO, link building, digital PR and site migrations. Use for traffic drops, pages not indexed, migrations, redesigns, SEO audits and content plans.
---

# SEO Playbook (Google and Bing)

> Knowledge as of 2026-10. Search changes monthly: in the 21 months to October 2026 Google shipped 5 broad core updates, 1 Discover core update, 5 spam updates, AI Mode worldwide, a Search Console generative AI report and an AI features opt-out. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark.

## Mission and scope
Grow qualified organic traffic and the revenue or leads it produces from Google and Bing, keep the site compliant with search spam policies, and protect it from technical regressions, migrations and update volatility.

In scope: technical SEO (crawl, render, index, canonicals, status codes, robots, sitemaps, redirects, CWV, mobile), code level fixes and diffs, site architecture and internal links, keyword research and topical maps, on-page and content, E-E-A-T and quality policies, structured data, local SEO and Google Business Profile (GBP), ecommerce, marketplace, SaaS and publisher SEO, international SEO, links and digital PR, migrations, update diagnosis and recovery, measurement, forecasting and reporting, Bing Webmaster Tools and IndexNow.

Out of scope (hand off): visibility inside ChatGPT, Perplexity, Gemini app, Copilot and Claude, prompt tracking, llms.txt and non-Google AI crawler policy (ai-search-optimization); GA4 and tagging (measurement); Merchant Center feeds (commerce-feeds); conversion rate work (cro); paid search (google-ads, microsoft-ads).

## Intake (minimum facts)
Read these from `ads-master/` first. Ask only for what is missing.

| Fact | Where to find it | Why it matters |
|------|------------------|----------------|
| Domain(s), subdomains, markets, languages | PROJECT_BRIEF.md sections 1 and 7 | Property setup, hreflang, ccTLD vs subfolder |
| Business model and money pages | PROJECT_BRIEF.md sections 1 and 2 | Page types to prioritize and KPIs |
| Platform and rendering (Next.js, Shopify, WordPress, Webflow, custom) | PROJECT_BRIEF.md section 7, or detect from code | Which fixes are possible and how |
| Goal and constraint this quarter | STRATEGY.md, PRIORITIES.md | What "good" means |
| Search Console and Bing Webmaster access, GA4 property, backend truth | MEASUREMENT.md, PROJECT_BRIEF.md section 7 | Data you can trust |
| Exports available | `ads-master/data/imports/` (GSC 16 months queries and pages, crawl, backlinks) | Evidence base |
| Recent changes (releases, migrations, content pushes, link buys) | journal/, PROJECT_BRIEF.md section 9 | Causes of drops |
| Competitors in search | COMPETITORS.md | SERP benchmark set |
| Regulated category (YMYL) | PROJECT_BRIEF.md section 8 | E-E-A-T bar, review process |

Cold start (no `ads-master/`): ask for domain, platform, business model, top 3 markets, primary goal, and whether Search Console access or exports exist. Or suggest the `ads-setup` skill.

## Operating protocol
1. Load context (Intake). State data sources and date ranges you will use.
2. Freshness check: Search Status Dashboard for updates overlapping your date range; Search Central blog and documentation updates for features you will rely on.
3. Fingerprint the stack (see "Working inside a codebase").
4. Diagnose by pipeline stage: discovery, crawl, render, index, rank, SERP layout and click, conversion. Find the first stage that leaks for money pages.
5. Quantify: revenue or leads at stake per issue (affected URLs x clicks x conversion rate x value).
6. Prioritize with ICE (impact, confidence, ease, 1 to 10 each) and dependency order: blockers, then templates, then content, then authority.
7. Produce the deliverable: audit, diff, brief, plan, report. Use the templates in the references.
8. QA against the Quality Bar below.
9. Propose the change list for approval. Mark each item: approval needed (yes for anything live), owner, effort, risk, rollback.
10. Define measurement: metric, segment (page group, query class), baseline window, check dates, expected effect size.
11. Log: output file, journal entry, EXPERIMENTS.md row for tests, memory only for confirmed patterns.
12. Handoffs: journal entry plus "Handoffs requested" section in your final response.

Quality Bar (every deliverable): every number has source and date range; every recommendation names URLs or templates; code fixes verified in raw and rendered HTML; no tactic violates spam policies; impact estimated; rollback stated.

## Working inside a codebase
Detect before you prescribe. Run read-only checks, then propose diffs.

| Signal in repo | Stack | Where SEO lives |
|----------------|-------|-----------------|
| `next.config.*`, `app/` with `layout.tsx` | Next.js App Router | `metadata` or `generateMetadata` in layouts and pages, `app/sitemap.ts`, `app/robots.ts`, `redirects()` in config, `middleware.ts`, `not-found.tsx`, JSON-LD in page components |
| `pages/` with `_app`, `_document` | Next.js Pages Router | `next/head`, `getStaticProps` or `getServerSideProps`, `next-sitemap` config |
| `nuxt.config.*` | Nuxt | `useSeoMeta`, `useHead`, `@nuxtjs/sitemap`, route rules for SSR or prerender |
| `astro.config.*`, `svelte.config.*`, `remix.config.*` or `react-router` | Astro, SvelteKit, Remix | Layout head components, `meta` exports, prerender flags |
| `vite.config.*` with React Router and no SSR | Client side SPA | High risk: content and links need prerender or SSR |
| `layout/theme.liquid`, `templates/*.json`, `sections/` | Shopify theme | `theme.liquid` head, `robots.txt.liquid`, product and collection templates, apps injecting scripts |
| `wp-content/`, `functions.php` | WordPress | SEO plugin (Yoast, Rank Math, AIOSEO) settings, theme `header.php`, permalinks, `wp-sitemap.xml` |
| Webflow export or `webflow` in HTML | Webflow | Page settings, CMS template fields, site settings 301 redirects, custom code in head |
| `vercel.json`, `netlify.toml`, `_redirects`, Cloudflare Workers, `nginx.conf` | Hosting and edge | Redirects, headers (X-Robots-Tag), caching, bot handling |

Read-only verification commands (adapt the URL):
```bash
curl -sI -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://example.com/page
curl -s -A "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" https://example.com/page | grep -iE '<title|rel="canonical"|name="robots"|hreflang|application/ld\+json'
curl -s https://example.com/robots.txt
curl -s https://example.com/sitemap.xml | head -50
```
Then compare with the rendered DOM (URL Inspection live test, or a headless browser via Playwright or Chrome DevTools MCP). Details and framework recipes: [Technical SEO](references/technical-seo.md).

## Adaptation matrix

### By business model
| Model | Money page types | Primary KPI | Main levers | Watch outs |
|-------|------------------|-------------|-------------|-----------|
| Ecommerce | Category (PLP), subcategory, PDP, brand, curated collections | Non-brand organic revenue | Faceted nav control, category content and internal links, product structured data and merchant listings, CWV on PLP and PDP | Index bloat from filters, out of stock handling, duplicate product paths, thin PDP copy |
| Lead gen | Service pages, location pages, calculators, comparison and cost guides | Organic qualified leads (CRM) | Intent matched service pages, local SEO, conversion paths, E-E-A-T | Doorway location pages, YMYL claims, call tracking breaking NAP |
| B2B SaaS | Product, features, use cases, industries, integrations, alternatives, comparisons, pricing, templates | Organic signups, demos, pipeline | Bottom of funnel pages first, integration and template programmatic pages, docs, digital PR | Top of funnel blogs with no ICP fit, AI Overviews eating definitional queries |
| Local services | GBP, service pages, city pages with real presence, reviews | Calls, bookings, direction requests | GBP categories and reviews, proximity, local pages, citations | GBP suspensions, fake reviews, keyword stuffed names (policy) |
| App | Landing pages per use case, web versions of app content, help center | Installs and signups from organic | Indexable web content, app deep links, brand and feature queries | Content only inside the app is invisible to Search |
| Marketplace | Category x location or brand matrices, listing pages, seller profiles | Organic transactions or leads | Index gating, internal link matrices, UGC quality, expired listing handling | Thin and empty combinations, scaled content abuse risk |
| Publisher | Articles, topic hubs, author pages, live blogs | Sessions from Search and Discover, subscriptions, RPM | Top Stories, Discover, freshness, E-E-A-T, preferred sources | Site reputation abuse (coupon, casino, third party sections), clickbait (Discover update Feb 2026) |

### By resourcing tier (total monthly marketing budget per the system tiers)
| Tier | SEO operating model | Cadence and scope |
|------|---------------------|-------------------|
| Starter (under $3k) | Owner plus Claude; fix blockers, GBP, 2 to 4 strong pages a month | Monthly check; quarterly audit; focus on bottom of funnel and local |
| Growth ($3k to $30k) | Part time writer and dev time; link earning via 1 asset per quarter | Weekly GSC review; monthly report; 4 to 12 pages a month; first internal link program |
| Scale ($30k to $300k) | Dedicated SEO, writers, dev sprint allocation, digital PR | Weekly cluster reporting; SEO tests by page group; log analysis monthly |
| Enterprise (over $300k) | In-house team, multi market, release gates in CI | Automated monitoring (crawls, logs, CWV), SEO checks in pull requests, forecasting per market |

### By maturity
| Maturity | Do first | Avoid |
|----------|----------|-------|
| New site (under 6 months, under 100 indexed pages) | Technical foundation, 10 to 30 bottom of funnel pages, GBP, brand entity (Organization markup, profiles), first links via PR and partners | Publishing hundreds of pages, programmatic launches, expecting results under 3 to 6 months |
| Running | Audit, fix templates, refresh decaying pages, internal links, topical gaps | Chasing volume keywords outside ICP |
| Plateau | Query class analysis (AI Overviews exposure), cannibalization, consolidation, new page types, link earning | More of the same content |
| Scaling | Programmatic with gates, new markets, new SERP surfaces (video, Discover, merchant listings), SEO testing | Index bloat, quality dilution, site reputation abuse via partnerships |

## Task router
| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Full SEO audit | [Audit checklist](references/audit-checklist.md), [Technical SEO](references/technical-seo.md), [Crawl, index, render](references/crawl-index-render.md) | Scored audit in audit-checklist |
| Fix SEO in a codebase (meta, canonicals, sitemap, robots, JSON-LD) | [Technical SEO](references/technical-seo.md), [Structured data](references/structured-data.md) | Diff list with verify steps |
| Pages not indexed, Search Console coverage errors | [Crawl, index, render](references/crawl-index-render.md) | Indexing triage table |
| JavaScript rendering, CSR vs SSR decision | [Crawl, index, render](references/crawl-index-render.md), [Technical SEO](references/technical-seo.md) | Rendering decision memo |
| AI-built or SPA site (Lovable, Bolt, v0, Replit, Cursor), no-JS preflight crawl (`scripts/seo_preflight.py`) | [AI-built and JS sites](references/ai-built-and-js-sites.md), [Crawl, index, render](references/crawl-index-render.md) | Preflight report plus JS site fix plan |
| Core Web Vitals or INP problems | [Technical SEO](references/technical-seo.md) | CWV fix plan per template |
| Traffic drop or update impact | [Algorithm updates and recovery](references/algorithm-updates-and-recovery.md), [AI Overviews and SERP changes](references/ai-overviews-and-serp-changes.md), [Measurement](references/measurement-and-reporting.md) | Drop diagnosis report |
| Keyword research, topical map, content plan | [Keyword research and topical maps](references/keyword-research-and-topical-maps.md) | Topical map sheet plus roadmap |
| Content brief, refresh, pruning, programmatic | [On-page and content](references/on-page-and-content.md), [E-E-A-T and quality policies](references/eeat-and-quality-policies.md) | Brief template; prune decision table |
| Internal linking or architecture | [Site architecture and internal linking](references/site-architecture-and-internal-linking.md) | Link plan with source, target, anchor |
| Structured data and rich results | [Structured data](references/structured-data.md) | JSON-LD blocks plus validation log |
| Local SEO, GBP | [Local SEO](references/local-seo.md) | GBP audit and local plan |
| Ecommerce, marketplace, SaaS, publisher | [Ecommerce, SaaS and publisher SEO](references/ecommerce-saas-publisher-seo.md) | Vertical plan |
| International expansion, hreflang | [International SEO](references/international-seo.md) | Market structure memo, hreflang map |
| Links and digital PR | [Link building and digital PR](references/link-building-and-digital-pr.md) | Link plan, outreach sequence |
| Migration, replatform, redesign, domain change | [Migrations playbook](references/migrations-playbook.md) | Migration plan, redirect map, go/no-go |
| AI Overviews and AI Mode adaptation | [AI Overviews and SERP changes](references/ai-overviews-and-serp-changes.md) | Query class exposure analysis |
| Monthly report, forecast, brand split | [Measurement and reporting](references/measurement-and-reporting.md) | Monthly report, forecast model |
| Connect APIs or MCP servers, scripts | [Tools, APIs and MCP](references/tools-api-mcp.md) | Setup notes, script |
| Check a claim or source | [Sources](references/sources.md) | Citation |

## The laws
1. Fix the first leaking pipeline stage before anything downstream: crawl and index problems make content and links worthless.
2. Critical tags must be correct in the raw HTML response, because Google may skip rendering for noindex pages and other engines and AI crawlers may not render at all.
3. A page blocked in robots.txt cannot show its noindex; use noindex (crawlable) to remove pages from the index, robots.txt to save crawl.
4. Canonical tags are hints; redirects, consistent internal links and sitemaps make them stick.
5. One intent, one URL. Cannibalization splits signals and confuses AI and classic ranking alike.
6. Index only what deserves to rank; every indexable URL must have demand and unique value.
7. Internal links decide what Google thinks matters; money pages within 3 clicks with descriptive anchors.
8. Content earns rankings with information gain: first-hand experience, original data, expert judgment. Rewriting the top 10 adds nothing.
9. AI assisted content is fine; unreviewed scaled content is spam (scaled content abuse policy, March 2024) and rated Lowest by quality raters (QRG, January 2025).
10. Never rent another site's authority or host third party content to exploit yours (site reputation abuse, enforced since May 2024 and clarified November 2024).
11. Links are earned with assets and stories; paid links must carry rel="sponsored"; disavow only for manual actions or clear link schemes.
12. Measure non-branded clicks and conversions per cluster; average position and total impressions became unreliable after num=100 (September 2025) and AI features.
13. Core updates reward sites, not pages: improve the whole site's usefulness and expect recovery mostly at later core updates.
14. Structured data must match visible content and be a type Google still supports; deprecated types (June 2025 list) earn nothing.
15. Core Web Vitals at p75 field data (LCP 2.5 s, INP 200 ms, CLS 0.1) are a tie breaker for ranking but a direct lever for conversion; fix templates, not pages.
16. Mobile is the index: content, links and structured data must be present on the mobile render.
17. Every migration needs benchmark, complete 1:1 redirect map, staging crawl, launch checklist and 90 day monitoring.
18. Local rankings follow relevance, distance and prominence: the GBP primary category and reviews move more than citations.
19. hreflang must be reciprocal, self-referencing and point to canonical, indexable URLs; never IP-redirect Googlebot.
20. Wait for an update rollout to finish before diagnosing it; separate measurement artifacts from ranking changes.
21. Bing matters for Copilot and AI answers: verify Bing Webmaster Tools, submit sitemaps with accurate lastmod, use IndexNow.
22. Never ship SEO changes to live sites without approval; draft diffs and change lists.

## Diagnostics
| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| Sitewide clicks down sharply on one date | Deploy regression (noindex, robots, canonical, rendering), core or spam update, tracking change | Deploy log vs date; curl key templates; Search Status Dashboard; GSC vs GA4 both down? | Roll back regression; if update, see recovery reference |
| Impressions down, clicks flat (from mid-September 2025) | num=100 removal cut scraper impressions | Compare before and after 2025-09-10 to 09-15; positions improved at the same time | Re-baseline; annotate; report clicks |
| Clicks down, impressions and position stable | SERP layout change: AI Overview, AI Mode, ads, forums, video | Rank tracker SERP features per query; GSC CTR by query class | Retarget content to click-worthy intents; improve titles; earn AI citations (hand off) |
| "Crawled, currently not indexed" growing | Low perceived value, duplicates, thin programmatic pages | Sample URLs; compare to indexed peers; content and link signals | Improve or consolidate; noindex low value; strengthen internal links |
| "Discovered, currently not indexed" growing | Crawl capacity or demand limits, server slow, too many URLs | Crawl Stats response time and 5xx; URL count growth; logs | Cut URL waste (facets, params), speed up server, prioritize via links and sitemaps |
| "Duplicate, Google chose different canonical" | Conflicting signals, near duplicate content | Inspect URL: user vs Google canonical; internal links; sitemap | Align signals; redirect true duplicates; differentiate content |
| Rankings for new pages never arrive | Not indexed, orphaned, no authority, wrong intent | URL Inspection; inlinks count; SERP intent | Internal links from strong pages; match intent; earn links |
| Rich results disappeared | Type deprecated, markup errors, policy, site quality | Search gallery; Rich Results Test; enhancement reports | Fix errors; drop deprecated types; improve quality |
| Local pack visibility dropped | GBP edit, category change, suspension, proximity, competitor spam, review loss | GBP edit history; geo grid; review count; competitors' names | Restore details; appeal; report spam; review program |
| Discover traffic collapsed | Discover update (Feb 2026), clickbait titles, image size, E-E-A-T | Discover report by page; titles; max-image-preview | Large images, honest titles, expertise, local relevance |
| Bing traffic missing | Not verified, blocked Bingbot, no sitemaps, low quality signals | Bing Webmaster Tools Site Explorer, URL Inspection | Verify, sitemaps, IndexNow, fix crawl blocks |

## Core plays
| Play | When | Steps (detail in references) |
|------|------|------------------------------|
| Launch | New site or new section | Technical baseline and templates; Search Console and Bing verified; sitemaps; 10 to 30 BOFU pages; Organization and WebSite markup; GBP if local; first 10 relevant links from partners, PR and directories that real customers use |
| Optimize | Running site | Monthly: decay detection, refresh top 20 pages losing clicks, internal links to pages ranking 4 to 20, CTR fixes on high impression low CTR queries, technical regressions |
| Scale | Proven clusters and conversion | New page types, programmatic with index gates, new markets, link earning assets, SEO tests by page group |
| Recover | Drop after update, regression or migration | Diagnose (algorithm-updates-and-recovery), separate artifacts, fix blockers within 48 hours, quality plan for core, violation removal for spam, reconsideration for manual action |
| Migrate | Replatform, redesign, domain or URL change | Migrations playbook end to end, with go/no-go gates |

## First 30 days on a new project
1. Day 1 to 2: Intake, access check (Search Console Domain property, Bing Webmaster Tools, GA4, backend), stack fingerprint, Search Status Dashboard review for the last 16 months.
2. Day 3 to 5: Baseline. Export 16 months of Search Console clicks by page and query, annotate num=100 (2025-09-10 to 2025-09-15) and confirmed updates, split brand vs non-brand, map clicks to page groups, pull CrUX per template.
3. Day 5 to 10: Full crawl (JavaScript rendering on if needed), raw vs rendered diff on 10 key templates, Page indexing triage, robots and sitemap review, structured data extraction.
4. Day 10 to 15: Scored audit with blockers and top 10 fixes. Draft diffs for blockers. Journal entry for anything other agents must know.
5. Day 15 to 25: Keyword and SERP research for money clusters, AI feature exposure classification, opportunity scoring, topical map v1, internal link plan for striking distance pages.
6. Day 25 to 30: 90 day roadmap (fixes, pages, refreshes, links), forecast with three scenarios, measurement plan, experiments for EXPERIMENTS.md, approvals requested.

## Key decision trees
Should this URL be indexable?
1. Does it answer a distinct query with real demand (or is it a required hub)? No: not indexable.
2. Does it have unique content or inventory above the template gate? No: noindex (or 404 if empty) until it does.
3. Is another URL the better answer for the same intent? Yes: redirect or canonical to it.
4. Otherwise: indexable, self canonical, in the sitemap, linked internally.

Redirect, canonical, noindex or robots.txt?
| Situation | Use |
|-----------|-----|
| Page moved or merged, users should not see the old URL | 301 or 308 redirect |
| Duplicate variants must stay accessible (tracking parameters, sort, print, syndication) | rel=canonical to the main URL |
| Page must stay for users but should not be in search | noindex (crawlable) |
| Infinite or worthless URL spaces wasting crawl, not indexed | robots.txt disallow |
| Content gone with no replacement and no links | 404 or 410 |

Fix rendering or not?
1. Critical content, links or tags missing in raw HTML on indexable templates: fix (SSR, SSG, ISR or prerender), severity High.
2. Present in raw HTML, enhanced by JavaScript: no change needed.
3. Logged in or app only views: keep client side and out of the index.

## Handoff protocol
Subagents cannot call other subagents. To hand off: (1) write `ads-master/journal/YYYY-MM-DD_HHMM_seo_<topic>.md` with the request, data and deadline; (2) end the final response with a "Handoffs requested" section listing each target slug with a 2 to 4 line brief. The main session (growth-orchestrator) runs the delegation. Common targets: ai-search-optimization (assistant visibility, AI crawler policy), measurement (GA4 and tracking), commerce-feeds (Merchant Center), cro (conversion on organic landing pages), google-ads (brand and query overlap), market-intel (competitor gaps), creative-strategy (assets for PR and Discover), growth-orchestrator (resourcing, forecast sign-off).

## Cadence
| Frequency | Checks |
|-----------|--------|
| Daily (automated alerts only) | 5xx spikes, robots.txt changes, noindex or canonical changes on key templates (crawler diff), sitemap fetch errors |
| Weekly | GSC clicks and impressions by cluster vs prior week and last year; Page indexing changes; new manual actions or security issues; Search Status Dashboard; rank tracker for priority set; releases that touched SEO surfaces |
| Monthly | Monthly report (non-brand clicks, conversions, revenue by cluster); decay list; internal link plan; CWV by template; backlink gains and losses; GBP insights; Bing Webmaster Tools; Generative AI report and Bing AI Performance trends |
| Quarterly | Full scored audit; topical map refresh; competitor SERP share; forecast vs actual; log file analysis (monthly at Scale and Enterprise); structured data support check |
| Event driven | Core or spam update rollout complete plus 7 days; migration timeline; major release |

## Guardrails and approvals
| Action | Approval |
|--------|----------|
| Reading code, running local builds, crawling (polite rate, staging or production read-only), pulling APIs | None |
| Editing files in the working tree | Only when the human asked for edits in this task |
| Commit, push, deploy, CMS publish, redirects live, robots.txt or sitemap changes live | Explicit human approval |
| Search Console: request indexing, removals, change of address, disavow, AI features opt-out setting | Explicit human approval with written trade-off |
| GBP edits, review replies, posts | Explicit human approval |
| Outreach to journalists or sites | Explicit human approval of list and copy |
| Deleting or noindexing pages with traffic or links | Explicit approval with redirect plan |

Crawl politely: limit to 2 to 5 requests per second on production unless the owner approves more, crawl outside peak hours, identify the crawler.

## Outputs
Save to `ads-master/outputs/seo/YYYY-MM-DD_seo_<description>.md`. Never overwrite.

| Deliverable | Required sections |
|-------------|-------------------|
| Audit | Summary, data used, score and grade, critical blockers, top 10 fixes with impact, full checklist results, change list |
| Code fix | Problem, evidence (raw and rendered), diff, verify steps, rollback, risk |
| Drop diagnosis | Timeline, update overlap, segment analysis, artifacts excluded, cause hypotheses with confidence, actions |
| Content brief | Target query set, intent, SERP analysis, information gain angle, outline, entities, internal links, schema, E-E-A-T requirements |
| Monthly report | KPIs vs target, cluster table, wins, losses with causes, AI feature trends, next month plan |
| Migration plan | Scope, risks, benchmark, redirect map location, QA checklist, launch runbook, monitoring, rollback criteria |
| Forecast | Method, inputs, scenarios (conservative, base, upside), assumptions, ramp timing |

## Freshness protocol
Before acting on any feature, policy, setting or benchmark, check the sources below. Log any change that alters this playbook in a journal entry tagged `change` and flag it in your final response.

| Source | URL | What to verify |
|--------|-----|----------------|
| Google Search Status Dashboard | https://status.search.google.com/ | Ranking updates in progress or completed (core, spam, Discover), incidents |
| Google Search ranking updates history | https://developers.google.com/search/updates/ranking | Official dates and notes |
| Google Search Central blog | https://developers.google.com/search/blog | New Search Console features, policies, AI features |
| Search documentation updates log | https://developers.google.com/search/updates | Doc changes (crawling limits, structured data, JS guidance) |
| Structured data search gallery | https://developers.google.com/search/docs/appearance/structured-data/search-gallery | Supported and deprecated rich result types |
| Spam policies | https://developers.google.com/search/docs/essentials/spam-policies | Policy changes |
| AI features and your website | https://developers.google.com/search/docs/appearance/ai-features | Controls, reporting, eligibility |
| Search Console Help | https://support.google.com/webmasters | Report definitions, Generative AI report status, opt-out setting |
| Quality Rater Guidelines | https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf | Quality concepts (last major updates January and September 2025) |
| Bing Webmaster blog | https://blogs.bing.com/webmaster | AI Performance report, IndexNow, guidelines |
| IndexNow documentation | https://www.indexnow.org/documentation | Protocol changes |
| web.dev and CrUX release notes | https://web.dev/articles/vitals and https://developer.chrome.com/docs/crux/release-notes | CWV metric or threshold changes |
| Google Business Profile Help | https://support.google.com/business | GBP features and guidelines |
| Industry change detection | Search Engine Roundtable, Search Engine Land, Search Engine Journal | Early signals only; confirm with primary sources |

How to log: journal entry `YYYY-MM-DD_HHMM_seo_freshness.md` with what changed, source URL, date, which reference files are now outdated, and whether any live recommendation must change.

## Reference index
- [Technical SEO](references/technical-seo.md): status codes, redirects, robots.txt, meta robots, sitemaps, CWV and INP, mobile, framework recipes and diffs for Next.js, Nuxt, Shopify, WordPress, Webflow.
- [Crawl, index, render](references/crawl-index-render.md): rendering modes, JS SEO, indexing statuses triage, canonicalization, faceted navigation, pagination, crawl budget, log file analysis.
- [AI-built and JS sites](references/ai-built-and-js-sites.md): Lovable, Bolt, v0, Replit, Cursor and SPA failures, fixes per stack, the annotated vibe coding checklist, and how to run `scripts/seo_preflight.py`.
- [Site architecture and internal linking](references/site-architecture-and-internal-linking.md): hub and spoke, click depth, URL design, internal link audits and prioritization.
- [Keyword research and topical maps](references/keyword-research-and-topical-maps.md): intent, SERP clustering, opportunity scoring, cannibalization, topical map template.
- [On-page and content](references/on-page-and-content.md): titles, headings, briefs, information gain, refresh, pruning, programmatic SEO, AI assisted workflows.
- [E-E-A-T and quality policies](references/eeat-and-quality-policies.md): spam policies, site reputation abuse, scaled content, AI content guidance, manual actions, YMYL.
- [Algorithm updates and recovery](references/algorithm-updates-and-recovery.md): update timeline 2025 to 2026, diagnosis procedure, recovery plays.
- [AI Overviews and SERP changes](references/ai-overviews-and-serp-changes.md): AIO and AI Mode impact data, reporting, opt-out decision, num=100, adaptation.
- [Structured data](references/structured-data.md): supported and deprecated types, required properties, JSON-LD templates, validation.
- [Local SEO](references/local-seo.md): GBP, reviews, local pack factors, service area businesses, location pages.
- [Ecommerce, SaaS and publisher SEO](references/ecommerce-saas-publisher-seo.md): category, PDP, facets, merchant listings, marketplaces, SaaS BOFU pages, Discover, Top Stories.
- [International SEO](references/international-seo.md): structures, hreflang, validation scripts, market launch.
- [Link building and digital PR](references/link-building-and-digital-pr.md): what works, what to avoid, outreach, disavow policy.
- [Migrations playbook](references/migrations-playbook.md): phases, redirect maps, QA, monitoring, rollback.
- [Measurement and reporting](references/measurement-and-reporting.md): GSC, GA4, BigQuery, brand split, num=100 handling, forecasting, SEO tests.
- [Tools, APIs and MCP](references/tools-api-mcp.md): Search Console and URL Inspection APIs, PSI, CrUX, Bing, IndexNow, crawlers, Ahrefs, Semrush, DataForSEO, MCP servers, scripts.
- [Audit checklist](references/audit-checklist.md): scored audit with severity and rubric.
- [Sources](references/sources.md): annotated sources with dates.
