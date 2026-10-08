# Algorithm Updates and Recovery

> Scope: confirmed Google updates January 2025 to October 2026, how core, spam and Discover updates differ, a step by step traffic drop diagnosis, recovery plays, and stakeholder communication. Always re-check the Search Status Dashboard (https://status.search.google.com/) before using this table; it is the official record.

## 1. Confirmed ranking updates, January 2025 to October 2026
Dates from Google's Search Status Dashboard as reported by Search Engine Journal, Search Engine Land, Search Engine Roundtable and Rank Math trackers. End times vary by a day between sources.

| Update | Start | End | Duration | What Google said | Notes |
|--------|-------|-----|----------|------------------|-------|
| March 2025 core update | 2025-03-13 | 2025-03-27 | 14 days | Regular core update | [Official, 2025-03] |
| June 2025 core update | 2025-06-30 | 2025-07-17 | About 16 days 18 hours | Regular core update | [Official, 2025-06] |
| August 2025 spam update | 2025-08-26 | 2025-09-22 | About 27 days | Spam update, not a link spam update | [Official, 2025-08]; end date reported as 21 or 22 September |
| December 2025 core update | 2025-12-11 | 2025-12-29 | 18 days 2 hours | "Regular update" | [Official, 2025-12] |
| February 2026 Discover core update | 2026-02-05 | 2026-02-27 | About 22 days | First Discover only core update: more locally relevant content from sites in the reader's country, less clickbait and sensationalism, more in-depth, original, timely content from sites with expertise. US English first, other countries and languages "in the coming months" | [Official, 2026-02, Search Central blog]; no expansion beyond US English announced as of 2026-10-08 |
| March 2026 spam update | 2026-03-24 | 2026-03-25 | About 19.5 hours | Global, all languages, no new policies | [Official, 2026-03]; shortest spam update on the dashboard |
| March 2026 core update | 2026-03-27 | 2026-04-08 | About 12 days | Regular update, no companion blog post | [Official, 2026-03] |
| May 2026 core update | 2026-05-21 | 2026-06-02 | About 12 days | Second core update of 2026 | [Official, 2026-05] |
| June 2026 spam update | 2026-06-24 | 2026-06-26 | About 2 days 1 hour | Global, no new policies | [Official, 2026-06] |
| August 2026 spam update | 2026-08-18 | 2026-08-21 | About 2 days 16 hours | Global | [Official, 2026-08] |
| September 2026 spam update | 2026-09-24 (about noon ET) | 2026-10-08 (4:37 am ET) | About 14 days | Global, all languages, no specific target named; Google had said up to two weeks | [Official, 2026-09 and 2026-10]; volatility spikes reported including October 4 to 6 |

Unconfirmed or disputed:
- Late May to early June 2025: reports of deindexing and "crawled, not indexed" spikes; not confirmed by Google [Unverified].
- July 2026 and August 2026 "core updates": several blogs describe them, but the Search Status Dashboard lists no core update after the May 2026 core update (ended 2026-06-02) through 2026-10-08. Treat as unconfirmed volatility. Trade press expects another core update before the year-end holidays; none was announced as of 2026-10-08 [Official, dashboard; forecast Unverified].
- Google states that smaller core updates happen without announcement because they are not widely noticeable [Official].

Related events that change traffic without being ranking updates:
| Date | Event | Effect |
|------|-------|--------|
| 2025-01 | Google began requiring JavaScript to load Search results, disrupting many scrapers | Rank tracker outages and data gaps |
| 2025-05-20 | AI Mode launched to all US users | New surface; later included in Search Console totals (June 2025) |
| 2025-09-10 to 2025-09-15 | `num=100` results parameter stopped working | Search Console impressions fell for most sites, average position improved, query counts fell; rank tracker cost and depth changed |
| 2025-10-07 | AI Mode expanded to 40+ more countries and 35+ languages | Click patterns shift in those markets |
| 2026-01-27 | Gemini 3 became the default model for AI Overviews [Official, 2026-01] | Possible citation pattern shifts; re-baseline |
| 2026-05-07 | FAQ rich results stopped showing in Google Search [Official, 2026-05] | CTR changes on pages that had FAQ snippets; not a ranking change |
| 2026-06 | Search Console AI features opt-out setting and Generative AI performance reports (all sites worldwide from 2026-08-31) | Sites that opt out lose AI feature impressions and clicks |
| 2026-07-22 | AI Overviews and AI Mode launch in France | Click patterns shift for French queries |
| 2026-08 | google.com/goto passthrough links on results | Rank tracker and attribution tooling changes; referrers still pass in tests |

## 2. How update types differ
| Type | What it does | Penalty? | Recovery expectation |
|------|-------------|----------|----------------------|
| Broad core update | Reassesses relevance and quality signals across the index | No; others may simply be judged more helpful | Improvements can be recognized gradually, but large swings usually happen at a later core update. Google has said not to expect quick recovery without significant improvement [Official, core updates guidance] |
| Spam update | Improves spam detection (SpamBrain); demotes or removes violating content | Algorithmic demotion | Remove violations; systems take time, often months, to recognize compliance [Official] |
| Link spam update | Neutralizes manipulative links | Lost link value, not usually a demotion beyond that | Gains from neutralized links do not return; build real authority |
| Discover core update | Reassesses Discover feed selection | No | Fix Discover specific quality (titles, images, expertise, local relevance) |
| Helpful content | Folded into core ranking systems in March 2024; no longer a separate system | n/a | Treat as core |
| Reviews system | Now improved continuously without separate announcements (since 2023) | n/a | Follow reviews guidance |

## 3. Traffic drop diagnosis procedure
Work in this order. Do not start content changes until step 6 is complete.

1. Confirm the drop is real and organic.
   - Search Console (web search) clicks: daily, last 16 months; GA4 Organic Search sessions; backend revenue from organic.
   - If GA4 dropped and Search Console did not: tracking issue (hand off to measurement).
   - If impressions dropped and clicks did not around mid-September 2025: num=100 artifact.
2. Date it precisely. Find the first day of decline. Pull the Search Status Dashboard and the release log (deploys, CMS changes, CDN or WAF changes, plugin updates, migrations).
3. Rule out technical regressions on the date.
   - Crawl the top 500 URLs by clicks; compare to the last known good crawl: status codes, robots meta, canonicals, titles, rendered content, internal links.
   - robots.txt history, sitemap changes, Crawl Stats (5xx, 403, response time).
   - Page indexing: sudden growth in excluded reasons.
4. Segment the loss (last 28 days vs the 28 days before the date, and vs last year).
   - By page type or template (directory regex), by query class (brand vs non-brand, informational vs commercial, AI Overview present vs not), device, country, search appearance.
   - Concentrated in one template: template change or template quality. Concentrated in informational queries with flat positions: SERP layout or AI features. Sitewide across types with position losses: quality reassessment (core) or spam demotion.
5. Inspect SERPs for the top 50 lost queries.
   - Who gained? Forums and UGC, big brands, AI Overviews, video, local packs, marketplaces, government sources.
   - Did the intent change (from guides to products, or the reverse)?
   - Are you cited in AI Overviews or AI Mode where you lost clicks?
6. Classify the cause with confidence levels.

| Evidence pattern | Most likely cause | Confidence boosters |
|------------------|-------------------|---------------------|
| Drop starts on a deploy date, specific templates, tags changed | Technical regression | Crawl diff shows the change |
| Drop aligns with a core update rollout, sitewide, positions fell broadly | Core quality reassessment | Competitors with stronger first-hand content or brands gained |
| Drop aligns with a spam update, concentrated in sections with policy risk | Spam demotion | Third party sections, scaled pages, link schemes present |
| Positions stable, CTR down on informational queries | AI Overviews, SERP features | AIO present on those SERPs; Generative AI report impressions present |
| Gradual decline over months | Content decay, competition, demand shift | Trends data, competitor content newer |
| Brand queries down | Demand or reputation issue, not SEO | Brand search volume in Trends down |
| Manual action message | Manual action | Search Console notification |

7. Quantify impact in business terms: lost clicks x conversion rate x value by segment.
8. Write the diagnosis report (template in section 7) and the recovery plan.

## 4. Recovery plays
### 4.1 Technical regression
- Roll back or hotfix within 24 to 48 hours (with approval). Request recrawl through sitemaps and, for a handful of critical URLs, URL Inspection.
- Recovery after fixing usually follows recrawl, typically days to a few weeks [Practitioner consensus].
- Add a regression test for the failure (see technical reference).

### 4.2 Core update quality loss
1. Run the sitewide quality audit ([eeat-and-quality-policies.md](eeat-and-quality-policies.md) section 10).
2. Compare winners vs your pages on the lost queries: first-hand experience, depth, freshness, brand signals, UX, ads density, author expertise.
3. Prioritize page types with the largest lost value.
4. Improve, merge or remove low quality content at scale; rewrite key pages with information gain; strengthen author and site trust signals.
5. Fix UX and ads heavy layouts on affected templates.
6. Do not chase superficial edits (word count, keyword density, date changes).
7. Expect to measure progress at the next one or two core updates; track leading indicators (indexing ratio, rankings on refreshed pages, engagement).

### 4.3 Spam demotion
1. Identify the violation class (scaled content, site reputation abuse, link schemes, expired domain, doorway).
2. Remove or noindex violating content completely; end link buying; remove or qualify paid links.
3. Document changes (needed if a manual action exists).
4. Expect months before systems re-evaluate. Do not create new domains to escape (policy circumvention).

### 4.4 AI Overviews and SERP layout losses
Not a penalty. Adapt the portfolio: see [ai-overviews-and-serp-changes.md](ai-overviews-and-serp-changes.md). Shift effort to commercial and click-worthy intents, tools and data, brand demand, and AI citations (hand off to ai-search-optimization).

### 4.5 Discover drop (publishers)
- Check titles for sensationalism and clickbait, image size and `max-image-preview:large`, topical expertise, local relevance for the audience, and Discover policy compliance.
- After February 2026, non local publishers covering another country's news may lose share in that country while gaining in their own [Official, 2026-02 goals; NewzDash analysis Study].

## 5. What not to do during or after an update
- Do not make large site changes during a rollout; you cannot separate effects.
- Do not mass disavow links out of fear; most sites do not need disavow [Official].
- Do not change publish dates to look fresh.
- Do not delete large amounts of content without the pruning decision tree.
- Do not blame the update before checking for regressions and measurement artifacts.
- Do not promise recovery dates; give leading indicators and the next update window.

## 6. Monitoring setup
- Annotate every confirmed update in Search Console (custom annotations, available since late 2025) and in your dashboard.
- Weekly: compare cluster level clicks with last year; flag clusters with over 20% decline.
- During rollouts: daily check of top 50 queries and top 100 pages; volatility tools (Semrush Sensor, Mozcast, Advanced Web Ranking, SISTRIX) as context only.
- After rollout completion plus 7 days: run the diagnosis procedure if any segment moved over 10%.

## 7. Drop diagnosis report template
```markdown
# Organic traffic change diagnosis: <site> <date range>
## Summary
- Change: <clicks -x% (GSC web), sessions -y% (GA4), revenue -z% (backend)> from <date> vs <baseline>
- Most likely cause (confidence): <cause> (<high/medium/low>)
- Revenue at risk per month: <value> (method)
## Timeline
| Date | Event (update, deploy, SERP change) | Source |
## Artifacts excluded
- num=100 effect: <checked how>
- Tracking: <GA4 vs GSC vs backend>
- Seasonality and brand demand: <Trends, last year>
## Segment analysis
| Segment | Clicks before | After | Change | Position change | CTR change |
## SERP evidence (top lost queries)
| Query | Our URL | Position before/after | Who gained | AI Overview present | Notes |
## Root cause hypotheses
1. <hypothesis> evidence for / against
## Actions
| Action | Owner | Effort | Expected impact | Approval needed | Check date |
## Communication
- What to tell stakeholders; when the next evaluation point is
```

## 8. Stakeholder communication
- Lead with business impact and what is known vs unknown.
- Explain update mechanics in one paragraph: core updates are reassessments, not penalties; recovery needs real improvement and usually shows at later updates.
- Share the plan with dates for leading indicators (two weeks for technical fixes, 4 to 12 weeks for refreshed pages, next core update for sitewide quality).
- Propose diversification if risk is structural (paid search, email, partnerships, AI visibility) and hand to growth-orchestrator.
