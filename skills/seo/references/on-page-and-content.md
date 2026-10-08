# On-Page and Content

> Scope: page level elements, content quality and information gain, content briefs, refresh and decay, pruning, programmatic SEO with safeguards, AI assisted workflows inside Google's policies, reviews and comparison content, images and video. Policy definitions and E-E-A-T signals are in [eeat-and-quality-policies.md](eeat-and-quality-policies.md).

## 1. On-page elements
| Element | Rule | Notes |
|---------|------|-------|
| `<title>` | Unique, describes the page's main topic and intent, primary term near the start, brand at the end, roughly 50 to 60 characters so it is not truncated | Google generates title links from the title element, H1, prominent headings, anchor text and other sources, and rewrites many titles; a 2021 Zyppy study of about 81,000 titles found over 60% changed [Study, 2021; older data, direction still valid] |
| Meta description | Unique summary with the offer or answer and a reason to click, roughly 140 to 160 characters | Often replaced by page text matching the query; still write it for money pages |
| H1 | One per page, matches the intent and the title's promise | Mismatch between H1 and title increases rewrites |
| H2 and H3 | Logical outline; each section answers a sub-question | Sections that stand alone are easier to quote in snippets and AI features |
| Intro | Answer or value proposition in the first 2 to 3 sentences | Readers and AI systems both use the opening |
| URL | Short, readable, stable | See architecture reference |
| Internal links | Contextual links to hub and related spokes, descriptive anchors | See architecture reference |
| Images | Descriptive file name, alt text describing the image, dimensions set, modern formats, near relevant text | `max-image-preview:large` for Discover |
| Structured data | Matches visible content | See [structured-data.md](structured-data.md) |
| Author and dates | Byline linked to an author page; visible published and updated dates where content is time sensitive | Change "updated" dates only for substantive changes [Official, Google byline dates guidance] |
| Site name | WebSite structured data on the homepage with `name` and `alternateName` | Controls the site name shown in results |

Title formulas that work across intents:
- Category: `[Category] for [Audience or Use] | [Brand]` ("Trail Running Shoes for Women | Acme")
- Comparison: `[A] vs [B]: [Key differentiator] ([Year])` only when the year is maintained
- Guide: `How to [Outcome]: [Specific method or number] [Proof element]`
- Local: `[Service] in [City] | [Brand] ([Differentiator])`
Never stuff multiple keyword variants separated by pipes.

## 2. What "helpful" means operationally
Google's people-first content guidance asks whether content provides original information, reporting, research or analysis; a substantial, complete description of the topic; insight beyond the obvious; and whether it was produced with expertise and effort that a reader would trust [Official, creating helpful content doc]. It also asks you to consider Who created the content, How it was created (including automation), and Why (to help people, or primarily to rank).

Information gain checklist (a page must answer yes to at least two):
- [ ] Includes first-hand experience: we used, tested, measured, visited, or served customers for this.
- [ ] Includes proprietary data: our numbers, survey, benchmark, pricing data, customer outcomes.
- [ ] Includes expert judgment: a named practitioner makes decisions and explains trade-offs.
- [ ] Includes original assets: photos, screenshots, diagrams, calculators, templates, video.
- [ ] Covers sub-questions competitors skip (from sales calls, support tickets, forums, AI Mode follow-ups).
- [ ] Is more current than the competing pages, with sources dated.

If none apply, the page should not be written or should be merged into a page that has them.

## 3. Content brief template (copy and fill)
```markdown
# Brief: <working title>
- Target URL: /path (new | existing)
- Cluster head query: <query> | Supporting queries: <list from cluster>
- Search intent and SERP format: <what the top 3 are: category page, guide, comparison, tool>
- AI features on SERP: AI Overview present? cited domains? Other features (video, forums, PAA, local)
- Audience and stage: <ICP, problem aware or product aware>
- Business goal and CTA: <signup, demo, add to cart, call>; conversion element placement
- Information gain angle: <what we add that the top 10 lack>
- Required first-hand inputs: <data pull, SME interview, product screenshots, test results>
- SME or reviewer: <name, credential> (mandatory for YMYL)
- Outline:
  - H1:
  - Intro (answer first, 2 to 3 sentences):
  - H2s with the question each answers:
- Entities and terms to cover: <products, specs, standards, people, places>
- Questions to answer verbatim (from PAA, sales, support): <list>
- Internal links: to <hub>, <related spokes>; from <existing pages to update>
- Structured data: <Article, Product, BreadcrumbList, VideoObject, etc.>
- Title (max 60 chars) and meta description (max 160 chars) drafts:
- Do not: <claims we cannot make, competitors not to name, compliance notes>
- Measurement: target queries, baseline, check at 4, 8, 12 weeks
```

## 4. Formats that keep earning clicks in the AI Overviews era
| Format | Why it holds value | Example |
|--------|-------------------|---------|
| Tools, calculators, configurators | Users need to interact; AI answers cannot fully replace | Mortgage calculator, size finder, ROI calculator |
| Original data and benchmarks | Cited by journalists and AI systems; earns links | Annual industry report with methodology |
| Templates and downloadable assets | Action oriented | Contract template, spreadsheet model |
| Comparisons with first-hand testing | Commercial intent remains click heavy | "We tested 9 CRMs for real estate teams" |
| Product and category pages | Transactional intent, merchant listings | PLPs with buying guidance |
| Local pages tied to GBP | Local intent | Location page with staff, photos, reviews |
| Video | Video SERP features and YouTube | Demos, how to |
| Opinionated expert content | Perspectives that summaries flatten | Named expert analysis |

Definitional and simple factual content ("what is X") is the most exposed to AI Overviews. Keep it only when it supports a funnel (glossary linked to product pages) or when you are the primary source.

## 5. Content refresh: detect decay and act
Decay definition: a page whose clicks fell more than 20% vs the same period last year (or vs its 3 month peak for seasonal content), excluding sitewide effects.

Search Console bulk export query:
```sql
WITH cur AS (
  SELECT url, SUM(clicks) c, SUM(impressions) i,
         SUM(sum_top_position) / NULLIF(SUM(impressions), 0) + 1 AS pos
  FROM `project.searchconsole.searchdata_url_impression`
  WHERE data_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY) AND DATE_SUB(CURRENT_DATE(), INTERVAL 3 DAY)
    AND search_type = 'WEB'
  GROUP BY url),
prev AS (
  SELECT url, SUM(clicks) c, SUM(impressions) i,
         SUM(sum_top_position) / NULLIF(SUM(impressions), 0) + 1 AS pos
  FROM `project.searchconsole.searchdata_url_impression`
  WHERE data_date BETWEEN DATE_SUB(CURRENT_DATE(), INTERVAL 455 DAY) AND DATE_SUB(CURRENT_DATE(), INTERVAL 368 DAY)
    AND search_type = 'WEB'
  GROUP BY url)
SELECT cur.url, prev.c AS clicks_ly, cur.c AS clicks_now,
       SAFE_DIVIDE(cur.c, prev.c) AS ratio, prev.pos AS pos_ly, cur.pos AS pos_now
FROM cur JOIN prev USING (url)
WHERE prev.c >= 100 AND SAFE_DIVIDE(cur.c, prev.c) < 0.8
ORDER BY prev.c DESC
LIMIT 200;
```
Note: impressions before mid-September 2025 include scraper inflated impressions; compare clicks and positions, not impressions, across that boundary.

Decay diagnosis per page:
| Pattern | Likely cause | Refresh action |
|---------|-------------|----------------|
| Position down, impressions down | Competitors improved, content outdated, intent shifted | Re-check SERP, update facts, add information gain, improve structure, add internal links |
| Position stable, CTR down | SERP layout change (AI Overview, ads, video, forums) or a better competitor snippet | Rewrite title and intro for the remaining click intent, add assets, consider format change |
| Impressions down, position stable | Demand fell (seasonality, trend) | Check Trends; no content fix |
| Ranking URL switched to another of ours | Cannibalization | Consolidate |

Refresh rules:
1. Change what matters: facts, examples, screenshots, data, recommendations, structure for current intent.
2. Keep the URL. Keep what still ranks (sections with query matches in GSC).
3. Update `dateModified` and the visible updated date only with substantive changes.
4. Re-promote: internal links from new content, newsletter, social.
5. Log the refresh date (annotation in Search Console) and check at 4 and 8 weeks.

## 6. Pruning and consolidation
Pruning is not a ranking trick; it helps when it removes or improves content that drags perceived site quality down or wastes crawl [Practitioner consensus; Google has said removing content is not by itself a recovery strategy].

Decision tree for each low performing URL (no meaningful clicks in 12 months):
1. Does it have external links (referring domains) or conversions? Yes: improve it, or merge into a related page and 301.
2. Does it serve users who arrive another way (navigation, email, support)? Yes: keep and noindex if thin.
3. Is the topic in scope and does demand exist? Yes: rewrite with information gain. No: continue.
4. Is there a closely related page? Yes: 301 to it. No: 410 and remove internal links.

Do it in batches (for example 10% to 20% of the affected set), annotate dates, and measure sitewide and cluster clicks for 8 to 12 weeks before the next batch.

## 7. Programmatic SEO done safely
Programmatic pages are template plus data. They are legitimate when each page answers a distinct query with distinct, useful data (integrations, locations with real inventory, product specs, exchange rates, job listings). They violate the scaled content abuse policy when produced primarily to manipulate rankings with little value, whatever the method (AI, templates, scraping) [Official, spam policies, March 2024].

Safeguards:
| Gate | Threshold example | Why |
|------|-------------------|-----|
| Demand | At least some search demand for the pattern head terms; long tail allowed if the pattern has proven demand | Avoid pages nobody searches |
| Data uniqueness | Each page has at least N unique data points (for example 5 listings, 3 reviews, unique stats) | Prevents near duplicates and soft 404s |
| Value add | Template includes analysis, comparisons, filters, maps, or tools beyond the raw data | Information gain |
| Index gate | `noindex` until gates are met; auto switch to index when they are | Keeps thin pages out |
| Rollout | Batches of 5% to 10% of the pattern; wait for indexing and performance signal | Detects problems early |
| Monitoring | Indexing ratio per pattern sitemap, clicks per indexed page, "Crawled, currently not indexed" share | Early warning |
| Kill switch | Noindex the pattern if indexing ratio stays under 30% after 8 weeks or clicks per page are near zero | Protect sitewide quality |

Examples by model:
- SaaS: `/integrations/<app>` with real setup steps, screenshots, use cases and limits; `/templates/<type>` with usable templates.
- Marketplace: `/<category>/<city>` only when inventory exists; show counts, price ranges, top rated, map.
- Ecommerce: indexable facets with demand (see faceted navigation).
- Publisher: data pages (stats per country, sports results) with real data and context.

## 8. AI assisted content workflow inside policy
Google's position: using AI is not against guidelines; using automation to generate content primarily to manipulate rankings is spam; content quality is judged regardless of how it is made [Official, Google guidance on AI-generated content, 2023, and generative AI content guidance]. Quality raters are instructed to rate main content that is all or almost all auto generated or AI generated with little effort, originality or added value as Lowest [Official, QRG, January 2025].

Workflow:
1. Human defines the brief with information gain inputs (data, SME notes, product facts).
2. AI may help with research synthesis, outline options, first drafts of non expert sections, summaries, schema drafts, and translation drafts.
3. A subject matter expert edits for accuracy, adds judgment and experience, and removes generic filler.
4. Fact check every claim, number and quote against a primary source. Remove anything unverifiable.
5. Add original assets (screenshots, photos, data).
6. Editorial QA: voice (BRAND.md), compliance (PROJECT_BRIEF.md section 8), links, schema.
7. Publish at a pace your editors can quality check; volume spikes of AI drafted pages are a classic scaled content abuse pattern.
8. Disclose AI use where readers would reasonably expect it (for example, automated summaries), consistent with Google's Who, How, Why framing.
9. AI generated product images in Merchant Center require the IPTC `DigitalSourceType` metadata (`trainedAlgorithmicMedia`) [Official, Merchant Center policy]; hand feed questions to commerce-feeds.

Red flags that the workflow has drifted into spam risk:
- Pages published faster than SMEs can review.
- Pages on topics outside the business's expertise.
- Near identical structure and phrasing across hundreds of pages.
- No first-hand inputs in the brief.
- Indexing ratio falling for new content.

## 9. Reviews, comparisons and "best" lists
Google's reviews guidance asks for evidence of first-hand use (photos, measurements, test results), comparison with alternatives, pros and cons, and explanation of what sets products apart [Official, high quality reviews doc].
- Show the testing method on the page.
- Include your own product fairly in "best" lists, with disclosure, and do not trash competitors with unverifiable claims (legal review for comparative advertising rules in your markets).
- Keep prices and features current; stale comparisons lose trust and rankings.
- Affiliate content needs disclosure and must add value beyond the merchant's own description (thin affiliation policy).

## 10. Images and video
Images:
- Use original images when possible; stock images add no information.
- Alt text describes the image for accessibility, including the product or concept, without stuffing.
- Serve responsive sizes; large images (1200 px wide or more) for Discover eligibility.
- Image structured data (license, creator) when you license images.

Video [Official, video SEO docs]:
- Google indexes videos when the video is the main content of the page (watch pages); a video embedded below an article is often not indexed as a video result.
- Provide VideoObject structured data, a stable thumbnail, and a video sitemap for large libraries.
- Key moments: Clip markup or SeekToAction for chapters.
- YouTube is its own search engine and a frequent SERP feature; coordinate with creative-strategy for production.

## 11. On-page QA checklist before publishing
- [ ] Title and H1 match intent and SERP format.
- [ ] Answer or value proposition in the first 3 sentences.
- [ ] Information gain checklist has at least two yes.
- [ ] Facts checked, sources cited with dates.
- [ ] Author byline with author page; reviewer for YMYL.
- [ ] Internal links: to hub and 2 to 5 related pages; at least 2 existing pages updated to link here.
- [ ] Structured data valid and matching visible content.
- [ ] Images optimized with alt text; LCP image not lazy loaded.
- [ ] Canonical self referencing, indexable, in sitemap.
- [ ] Mobile render checked.
- [ ] CTA present and tracked (hand tracking gaps to measurement).
