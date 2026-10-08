# Keyword Research and Topical Maps

> Scope: finding demand, classifying intent, clustering by SERP overlap, scoring opportunities with AI feature exposure, detecting cannibalization, and building a topical map and roadmap. Brief writing and page execution are in [on-page-and-content.md](on-page-and-content.md).

## 1. What changed in 2025 and 2026
- AI Overviews appear mostly on informational queries; Ahrefs found 99.2% of keywords triggering AI Overviews were informational in its April 2025 sample [Study, 2025-04]. Clicks for those queries fell most (see [ai-overviews-and-serp-changes.md](ai-overviews-and-serp-changes.md)). Keyword value now depends on SERP layout, not volume alone.
- Queries are longer and more conversational, especially in AI Mode, and AI Mode fans out one prompt into many sub-queries [Official, Google AI Mode descriptions 2025]. Long tail coverage through comprehensive, well structured pages matters more than one page per keyword variant.
- After Google removed the `num=100` parameter in September 2025, third party tools changed how deep they track and how they model volumes and positions; tool positions beyond page 2 are less reliable and costlier [Study, 2025-09, Search Engine Land analysis of 319 properties].
- Search Console added AI query groups (Insights, October 2025) and an AI branded query filter (November 2025, broader March 2026) that speed up clustering and brand separation [Official, 2025-10 and 2025-11].

## 2. Process overview
1. Define the business scope: products, services, ICP, markets, what you can credibly be the best answer for.
2. Seed: product and category names, customer language (sales calls, support tickets, reviews), competitors' top pages, existing GSC queries.
3. Expand: tool databases, GSC queries (16 months), People Also Ask, autocomplete, related searches, Reddit and forums, YouTube, AI Mode follow-ups, Keyword Planner.
4. Clean: dedupe, remove irrelevant, normalize spelling, tag brand terms (yours and competitors').
5. Classify intent and funnel stage.
6. Check SERPs: type of results, features (AI Overview, local pack, shopping, video, forums), dominant content format, freshness.
7. Cluster by SERP overlap into page level groups.
8. Score and prioritize.
9. Build the topical map: hubs, spokes, page types, internal links.
10. Roadmap: sequence by score and dependencies; assign briefs.
11. Review quarterly with fresh GSC data.

## 3. Intent classification
| Intent | Signals in query | Typical SERP | Page type to build |
|--------|------------------|--------------|--------------------|
| Transactional (buy, do) | buy, price, near me, deal, coupon, "[product] for [use]" | Shopping, ads, PLPs, PDPs | Category, PDP, service page, pricing |
| Commercial investigation | best, top, vs, alternative, review, compare | Listicles, comparisons, forums, video | Comparison, alternatives, best of with first-hand testing |
| Informational | how, what, why, guide, examples, ideas | AI Overview, PAA, videos, forums | Guide, tool, template, data study |
| Navigational | brand, brand + feature, login | Brand site, sitelinks | Brand pages, feature pages, help |
| Local | near me, city names, implicit local ("plumber") | Local pack, maps, directories | GBP, location and service pages |

Funnel mapping for B2B: problem aware (informational), solution aware (category terms, "software for X"), product aware (comparisons, alternatives, pricing, reviews), customer (integrations, how to in product, docs).

Rule: the SERP decides intent. If the top 10 are category pages, a blog post will not rank for the query no matter how good it is.

## 4. SERP clustering
Two keywords belong on the same page when Google ranks the same URLs for both.

Method:
1. For each keyword, collect top 10 organic URLs (DataForSEO SERP API, Semrush or Ahrefs SERP exports, or your rank tracker).
2. For each keyword pair, count shared URLs.
3. Group keywords where the overlap is 3 or more of 10 (strict: 4 or more). Use the highest volume or most representative keyword as the cluster head.
4. Clusters with mixed intent SERPs (half guides, half product pages) often need two pages; check which format dominates the top 3.

Python sketch (input CSV: keyword, volume, url, position):
```python
import pandas as pd
from itertools import combinations
import networkx as nx

df = pd.read_csv("serps.csv")
top = df[df.position <= 10].groupby("keyword")["url"].apply(set)
g = nx.Graph()
g.add_nodes_from(top.index)
for a, b in combinations(top.index, 2):
    if len(top[a] & top[b]) >= 3:
        g.add_edge(a, b)
vol = df.groupby("keyword")["volume"].max()
rows = []
for i, comp in enumerate(nx.connected_components(g)):
    head = max(comp, key=lambda k: vol.get(k, 0))
    for k in comp:
        rows.append({"cluster": i, "head": head, "keyword": k, "volume": vol.get(k, 0)})
pd.DataFrame(rows).sort_values(["cluster", "volume"], ascending=[True, False]).to_csv("clusters.csv", index=False)
```
Connected components can chain unrelated keywords in very large sets; for over 5,000 keywords, use community detection or require overlap with the head keyword.

## 5. Opportunity scoring
For each cluster:
```
expected_clicks = sum(volume_k) x CTR(target_position, serp_layout)
value = expected_clicks x conversion_rate(page_type) x value_per_conversion
score = value x win_probability / effort
```
Inputs:
| Input | How to set it |
|-------|---------------|
| volume | Tool estimate; prefer GSC impressions for existing rankings |
| CTR(target_position, serp_layout) | Your own GSC CTR curve by position for similar queries, split by AI Overview present vs absent. If you have no curve, start from a public curve (Advanced Web Ranking CTR study) and apply an AI Overview discount (studies range from about 15% to over 60% lower CTR; see the AI reference) |
| conversion_rate | GA4 for the page type (category, comparison, blog) on your site |
| value_per_conversion | PROJECT_BRIEF.md (AOV x margin, lead value) |
| win_probability | 0.2 to 0.8 from: your topical authority in the cluster, competitor strength (referring domains, brand), content gap you can fill |
| effort | Hours or cost to create and promote |

Worked example (B2B SaaS, values illustrative only):
- Cluster "real estate crm": 2,400 searches per month, SERP has no AI Overview, target position 3 with your curve CTR 9%: 216 clicks.
- Demo rate on solution pages 2.5%: 5.4 demos. Value per demo $900 (close rate x ACV x margin): $4,860 per month.
- Win probability 0.5, effort 16 hours: score 152 per hour.
- Cluster "what is a crm": 18,000 searches, AI Overview present, target position 5 with AIO CTR 1.5%: 270 clicks, demo rate 0.2%: 0.54 demos, $486 per month; win probability 0.2; effort 24 hours: score 4 per hour.
Conclusion: the bottom of funnel cluster is about 38 times more valuable per hour despite one seventh of the volume.

## 6. AI feature exposure field
Add to every keyword row:
- `aio_present` (yes, no, sometimes) from rank tracker SERP features or a SERP API.
- `aio_cites_us` (yes, no) and `aio_cited_domains`.
- `other_features` (local pack, shopping, video, forums, PAA, top stories).
Use these to forecast clicks realistically and to choose formats (video for video heavy SERPs, forums engagement for discussion heavy SERPs, merchant listings for shopping heavy SERPs). Hand prompt level AI visibility work to ai-search-optimization.

## 7. Cannibalization detection from Search Console
BigQuery (bulk export) query:
```sql
-- Queries where 2+ of our URLs got impressions in the last 28 days
SELECT
  query,
  COUNT(DISTINCT url) AS urls,
  SUM(impressions) AS impressions,
  SUM(clicks) AS clicks,
  ARRAY_AGG(STRUCT(url, impressions, clicks) ORDER BY impressions DESC LIMIT 5) AS top_urls
FROM `project.searchconsole.searchdata_url_impression`
WHERE data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 28 DAY)
  AND search_type = 'WEB'
  AND is_anonymized_query = FALSE
GROUP BY query
HAVING urls >= 2 AND impressions >= 100
ORDER BY impressions DESC
LIMIT 500;
```
Interpretation: cannibalization is real when the ranking URL flips over time or when the wrong page type ranks. Two URLs both ranking top 5 for a query (host clustering, sitelinks) is not a problem. Resolutions are in [site-architecture-and-internal-linking.md](site-architecture-and-internal-linking.md).

## 8. Brand vs non-brand split
- Preferred: Search Console branded queries filter (AI classification, top level properties only, not all sites eligible) [Official, 2025-11; expanded 2026-03].
- Fallback regex in the Performance report query filter (Custom (regex)) and in BigQuery:
```
(?i)(acme|ac me|acmee|acme\.com|acmecorp|acme crm)
```
Include misspellings, product names and founders' names when people search them. Keep competitor brand terms in a separate tag (they are non-brand for you but signal comparison intent).

## 9. Topical map template
| Hub | Cluster head keyword | Supporting keywords | Intent | Page type | URL | Priority score | Status | Links to | Links from |
|-----|---------------------|---------------------|--------|-----------|-----|---------------|--------|----------|-----------|
| CRM for real estate | real estate crm | crm for realtors, real estate agent crm, best crm for real estate | Commercial | Solution page | /solutions/real-estate | 152 | Live, refresh Q4 | /pricing, /integrations/zillow | /blog/real-estate-lead-follow-up |

Rules for the map:
1. Each cluster maps to exactly one URL.
2. Each hub has 5 to 30 spokes; deeper topics become their own hubs.
3. Cover the full decision journey for your ICP before broad top of funnel topics.
4. Mark clusters you will deliberately not cover (out of ICP, AI Overview saturated with no click value, YMYL beyond your expertise).
5. Topical authority comes from depth and quality in a domain you have real expertise in, not from publishing on every adjacent topic. Sites that expanded into unrelated topics for traffic were frequent losers in 2023 to 2025 updates [Practitioner consensus].

## 10. Data sources and their caveats
| Source | Strength | Caveat |
|--------|----------|--------|
| Search Console | Real impressions and clicks for your site | Only queries you already appear for; anonymized queries hidden; impressions changed after September 2025; AI feature impressions included in totals |
| Google Ads Keyword Planner | Google's own volume data | Ranges unless you run spend; grouped close variants |
| Ahrefs, Semrush, Similarweb, DataForSEO | Competitor and market coverage | Modeled volumes and clicks; validate with GSC where possible |
| Google Trends (and Trends API, alpha since 2025) | Seasonality and relative demand | Relative index, not volume |
| People Also Ask, AlsoAsked, autocomplete | Question discovery | No volume |
| Reddit, forums, reviews, sales calls | Real language and pains | Manual analysis; no volume |
| Bing Webmaster Tools keyword research | Bing demand | Smaller sample |
| AI Mode and AI Overviews follow-ups | Fan-out subtopics | Not stable, not quantified |

## 11. Deliverables
- `YYYY-MM-DD_seo_keyword-research_<scope>.md` with method, data sources and date ranges, cluster table summary, top 30 opportunities with scores, and links to the full CSV in `ads-master/outputs/seo/`.
- Topical map CSV with the template columns.
- 90 day roadmap: weeks, pages, briefs, owners, internal link tasks.
