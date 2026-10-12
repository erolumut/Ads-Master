# Speed and performance: prove it, then fix the biggest cause

Supports items 12 and 13 of `templates/LAUNCH-READINESS.md`. Speed work fails in two ways: fixing things that were never slow, and declaring victory from a lab score while real users wait. So the order is fixed: measure with field data, find the largest cause, fix it, measure again with the same method.

Labels: [Official] vendor documentation, [Practitioner consensus] widely repeated engineering practice, [Unverified] circulating claims without a source.

## 1. Measure first, the right way

| What | Tool | Why it matters |
|------|------|----------------|
| Field data (real users) | Chrome UX Report via PageSpeed Insights or Search Console Core Web Vitals; your own RUM (web-vitals library, analytics) | Google's Core Web Vitals assessment uses field data at the 75th percentile, not the lab score [Official] |
| Lab data (one simulated load) | Lighthouse, PageSpeed Insights lab section, WebPageTest | Repeatable, good for finding causes; a lab score of 95 can still fail in the field [Practitioner consensus] |
| Back end | Server timing headers, APM or logs: p50 and p95 per route, slow query log, query count per request | Front end tools cannot see a slow database |
| AI features | Time to first token and time to last token per call | Users judge AI speed by when text starts appearing |

Targets that matter (75th percentile, mobile): LCP under 2.5 s, INP under 200 ms, CLS under 0.1 [Official]. For APIs set your own p95 budget per route (for example 300 ms for reads, 1 s for writes) and keep it in the repo next to the code.

Rule: every speed claim names the metric, the percentile, the device class and the date range. "It feels faster" is not evidence.

## 2. Front end (the page)

| Fix | Proof it worked | Trap |
|-----|-----------------|------|
| Images as AVIF or WebP, sized to their display box, with width and height attributes | Lighthouse image audits clean; CLS stable | Width and height missing causes layout shift |
| Lazy load images below the fold | Fewer bytes on first load | Never lazy load the LCP image (usually the hero): load it eagerly with `fetchpriority="high"` [Official, web.dev guidance] |
| Fonts: one or two families, the critical one preloaded, `font-display: swap` or `optional`, subset | Font requests on first load; no invisible text | Preloading many files competes with the LCP image |
| Split JavaScript by route; lazy load heavy widgets | Bundle analyzer: first load JS per route | Splitting into dozens of tiny chunks can add requests without saving time |
| Remove unused packages and dead code | Bundle size before and after | AI generated code often imports whole libraries for one function |
| Third party scripts: remove what nobody uses, delay the rest until after interaction or idle | Main thread time, INP | Tag managers hide scripts; audit the live page, not the code |
| Long tasks: break work over 50 ms into smaller pieces, move heavy work to a Web Worker | INP and Total Blocking Time | INP is about every interaction, not just the first load |
| Static files from a CDN with long cache headers and hashed file names | Cache hit rate; repeat view time | Caching HTML that contains user data |
| Skeletons and loading states instead of blank screens | User perceived wait; CLS | Skeletons that do not match the final layout cause layout shift |
| Debounce search and filter inputs (about 200 to 300 ms) and cancel stale requests | Requests per keystroke | Debounce without cancelling still shows stale results |

If Ads Master is installed in the project, the deeper front end playbooks are `cro` (speed and Core Web Vitals) and `site-engineer` (performance and third party scripts).

## 3. Back end (the server and database)

| Fix | How to find it | Proof it worked |
|-----|----------------|-----------------|
| Index the columns you filter, join and sort by | Slow query log; `EXPLAIN` or `EXPLAIN ANALYZE` shows a sequential scan on a large table | `EXPLAIN` shows an index scan; p95 of the route drops |
| Fix N+1 queries (one query per item in a list) | Query count per request in logs or APM grows with list length | Query count per request is constant |
| Paginate lists (cursor based for long or changing lists) | Response size and time grow with data | Fixed page size; p95 flat as data grows |
| Cache responses that rarely change (with a clear invalidation rule) | Same expensive query repeated per request | Cache hit rate; p95 drop; no stale data bugs |
| Move heavy work to background jobs (emails, exports, image processing, AI batch work) | Requests that wait on slow side work | Request returns fast; job queue latency monitored |
| Put the server and database in the same region, near most users | Latency by country; database round trip time | TTFB by region |
| Remove cold starts on main routes (minimum instances, keep warm, smaller bundles, edge where it fits) | First request after idle is much slower | p95 of the first request after idle |
| Stream AI responses instead of waiting for the full answer | Time to first token vs time to last token | Time to first token under about 1 s for chat style features [Practitioner consensus] |
| Set timeouts and limits on every external call (AI, payments, third party APIs) | One slow provider blocks the request | Timeout errors handled; p99 bounded |

Never "fix" speed by caching personalized or authenticated responses in a shared cache: that is a data leak (item 5 of the launch checklist).

## 4. Asking an AI for help, properly

"What makes this app slow?" without data produces guesses. Give the model evidence and a scope:
1. The Lighthouse or WebPageTest trace (or its summary), the bundle analyzer output, and the field metrics with dates.
2. The slowest routes with p95, the slow query log and `EXPLAIN` output for the worst queries.
3. Ask for the top three causes ranked by expected impact, each with the measurement that will prove the fix.
Then fix one cause at a time and re-measure; changes stacked together hide which one worked.

## 5. Claims to treat carefully

| Claim | Status |
|-------|--------|
| "A 1 second delay is a lost signup" | Popular and directionally true, but the exact figures that circulate are old or unsourced [Unverified]. Measure your own funnel by speed bucket instead. |
| "Lighthouse 100 means fast" | Lab only. Field data decides Core Web Vitals [Official]. |
| "Lazy load everything" | Lazy loading the LCP image makes LCP worse [Official, web.dev guidance]. |
| "More caching is always better" | Without invalidation rules it serves stale or private data. |

## 6. What goes into LAUNCH-READINESS.md

| Item | Evidence to paste |
|------|-------------------|
| 12 Cheap Android | Device or emulation profile, the flows tested, the result, the date |
| 13 Under 3 s | Field LCP and INP at p75 (or lab if no field data yet, labelled as lab), p95 of the three slowest routes, time to first token for AI features, each with a date |

Re-check after every release that touches dependencies, images, fonts, third party scripts, database queries or AI calls.
