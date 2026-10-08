# Measurement and Reporting

> Scope: SEO data sources and their limits, Search Console after num=100 and with AI features, GA4 for organic, brand vs non-brand, KPI tree, monthly report, BigQuery queries, forecasting, SEO testing, alerting, and Bing reporting. Tracking implementation and attribution modeling belong to measurement.

## 1. Data sources and what each can answer
| Source | Answers | Limits |
|--------|---------|--------|
| Search Console Performance (web, image, video, news, Discover, Google News) | Clicks, impressions, CTR, average position by query, page, country, device, search appearance, date | Anonymized queries hidden; UI shows 1,000 rows; API returns a capped number of rows per day per search type; 16 months history; AI features included in totals with no AI filter in the main report |
| Search Console bulk export to BigQuery | Daily rows without UI row limits | Starts from setup date (no backfill); anonymized queries still null; storage cost |
| Search Console Generative AI report (beta 2026; all sites worldwide since 2026-08-31) | AI Overviews and AI Mode impressions combined, by page, country and date (separate report for Discover AI features); search type filter text or multimodal | Impressions only; no clicks, queries or AI Mode vs AI Overviews split; not in the API or BigQuery export as of 2026-10 (UI and CSV only) [Official, 2026-08] |
| Search Console Insights, query groups, branded filter, annotations | Faster analysis | Eligibility limits (query groups for large sites; branded filter for top level properties) |
| GA4 | Organic sessions, engagement, key events, revenue by landing page | Consent mode gaps, (not set) landing pages, AI feature clicks indistinguishable from organic |
| Backend or CRM | Revenue and lead quality truth | Needs landing page or first touch capture |
| Rank tracker | Daily positions and SERP features for a fixed query set | After num=100, deep tracking costs more; positions are a sample (location, device, personalization) |
| Bing Webmaster Tools | Bing clicks, impressions, keywords, backlinks, AI Performance (citations) | Smaller volumes; AI report is citations only |
| Crawlers and logs | Technical state and bot behavior | Snapshots |
| CrUX | Real user CWV | Origin or URL level only when enough traffic |

Always state: property (Domain or URL prefix), search type, date range, filters, and data freshness ("fresh" data for the last 2 to 3 days is preliminary).

## 2. Search Console rules of interpretation
- Clicks are the most stable metric. Use them as the primary SEO volume KPI.
- Impressions and average position changed meaning around 2025-09-10 to 2025-09-15 (num=100). Do not compare across that boundary. Annotate it in every chart.
- Average position is impression weighted and moves when the query mix changes. Report share of priority queries in top 3 and top 10 instead.
- AI Overviews links share the position of the overview block; AI Mode is included in web search totals since June 2025.
- Query level data excludes anonymized queries; page level totals include them. Query sums will not match page totals.
- Use the weekly and monthly aggregation views (December 2025) for trend charts; position is averaged over the period.
- Use custom annotations (late 2025) for releases, updates and migrations.

## 3. Brand vs non-brand
1. Preferred: Performance report > Query filter > branded or non-branded (AI classification; available for top level properties of eligible sites; Google notes it can misclassify) [Official, 2025-11 and 2026-03].
2. Fallback and for BigQuery: regex on queries.
```sql
-- Non-brand clicks by week (bulk export)
SELECT
  DATE_TRUNC(data_date, WEEK(MONDAY)) AS week,
  SUM(IF(REGEXP_CONTAINS(LOWER(query), r'(acme|acmee|ac me|acme crm)'), clicks, 0)) AS brand_clicks,
  SUM(IF(NOT REGEXP_CONTAINS(LOWER(query), r'(acme|acmee|ac me|acme crm)'), clicks, 0)) AS nonbrand_clicks,
  SUM(IF(is_anonymized_query, clicks, 0)) AS anonymized_clicks
FROM `project.searchconsole.searchdata_site_impression`
WHERE search_type = 'WEB'
GROUP BY week
ORDER BY week;
```
Anonymized query clicks are mostly long tail and mostly non-brand; report them separately rather than assigning them.

## 4. KPI tree
| Level | KPI | Cadence |
|-------|-----|---------|
| Business outcome | Organic revenue or qualified leads (backend or CRM), non-brand share | Monthly |
| Channel outcome | Non-brand organic clicks by cluster and page type | Weekly |
| Visibility | Share of priority queries in top 3 and top 10; AI feature impressions; local grid share | Weekly or monthly |
| Health | Indexed share of priority sitemaps; 5xx share; CWV pass by template; structured data errors | Weekly |
| Inputs | Pages shipped or refreshed, internal links added, referring domains earned, fixes deployed | Monthly |

## 5. Monthly report template
```markdown
# SEO monthly report: <site> <YYYY-MM>
Data: GSC <property>, web, <dates>; GA4 <property>; backend <source>; rank tracker <tool>, <n> queries, depth <n>.
## Summary (5 lines)
## Outcomes
| Metric | This month | Last month | Same month last year | Target |
| Non-brand clicks | | | | |
| Organic revenue / leads | | | | |
| Organic conversion rate | | | | |
## Clusters
| Cluster | Clicks | YoY | Top 3 share | AI Overview present share | Notes |
## Wins (with cause) and losses (with cause and action)
## AI features
- Generative AI report impressions (Search, Discover) trend; Bing AI citations trend; pages cited
## Technical health
- Indexing ratio per sitemap; CWV per template; new errors
## Work shipped and next month plan
| Item | Owner | Expected impact | Status |
## Risks and decisions needed
```

## 6. Useful BigQuery queries (Search Console bulk export)
Tables: `searchdata_site_impression` (property level, no URL), `searchdata_url_impression` (URL level with search appearance flags). Average position = `SUM(sum_top_position) / SUM(impressions) + 1`. `search_type` values include WEB, IMAGE, VIDEO, NEWS, DISCOVER, GOOGLE_NEWS.

Clicks by page group:
```sql
SELECT
  CASE
    WHEN REGEXP_CONTAINS(url, r'/products/') THEN 'pdp'
    WHEN REGEXP_CONTAINS(url, r'/collections/|/c/') THEN 'category'
    WHEN REGEXP_CONTAINS(url, r'/blog/|/guides/') THEN 'content'
    ELSE 'other'
  END AS page_group,
  DATE_TRUNC(data_date, MONTH) AS month,
  SUM(clicks) AS clicks,
  SUM(impressions) AS impressions,
  SAFE_DIVIDE(SUM(clicks), SUM(impressions)) AS ctr
FROM `project.searchconsole.searchdata_url_impression`
WHERE search_type = 'WEB' AND data_date >= '2025-09-15'
GROUP BY page_group, month
ORDER BY month, page_group;
```
Striking distance (positions 4 to 20, high impressions):
```sql
SELECT query, url,
  SUM(impressions) AS impressions, SUM(clicks) AS clicks,
  SUM(sum_top_position) / SUM(impressions) + 1 AS avg_position
FROM `project.searchconsole.searchdata_url_impression`
WHERE search_type = 'WEB'
  AND data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 28 DAY)
  AND is_anonymized_query = FALSE
GROUP BY query, url
HAVING avg_position BETWEEN 4 AND 20 AND impressions >= 200
ORDER BY impressions DESC
LIMIT 300;
```
Own CTR curve by position bucket (use for forecasting):
```sql
SELECT
  CAST(FLOOR(sum_top_position / impressions + 1) AS INT64) AS position,
  SUM(clicks) / SUM(impressions) AS ctr,
  SUM(impressions) AS impressions
FROM `project.searchconsole.searchdata_site_impression`
WHERE search_type = 'WEB' AND impressions > 0
  AND data_date >= DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY)
  AND is_anonymized_query = FALSE
GROUP BY position
HAVING position <= 20
ORDER BY position;
```
Split the curve by branded vs non-branded and by AI Overview presence (join a query list with `aio_present` from your rank tracker) for realistic forecasts.

Without BigQuery: Search Console API scripts in [tools-api-mcp.md](tools-api-mcp.md).

## 7. GA4 for organic
- Channel: Default channel group "Organic Search". Session source `google`, medium `organic` includes AI Overviews and AI Mode clicks.
- Landing page report with key events and revenue; build an exploration with landing page group (regex) and session default channel group.
- Link Search Console to GA4 for the Search Console reports collection (query and landing page data inside GA4, with GSC limits).
- Consent mode reduces observed sessions in some markets; compare trends, not absolute totals, and reconcile with backend (hand discrepancies to measurement).
- AI assistant referrals (chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai): custom channel group owned by measurement, reported with ai-search-optimization.

## 8. Forecasting
Never deliver a single number. Deliver conservative, base and upside scenarios with assumptions.

### 8.1 Keyword or cluster model (for new pages and initiatives)
```
monthly_clicks(cluster, month) = volume x CTR(position_target, aio_present, brand) x ramp(month)
revenue = monthly_clicks x CVR(page_type) x value
```
- CTR from your own curve (section 6), split by AI Overview presence.
- Ramp for new pages on an established site: about 0% to 10% of target in month 1 to 2, 30% to 60% by month 3 to 6, near target by month 6 to 12 [Practitioner consensus; slower for new domains and competitive SERPs].
- Scenario multipliers: conservative uses position target plus 3 and the lower CTR; upside uses the target position and full CTR.

Worked example (illustrative): 40 new category pages, combined volume 60,000 per month, target position 5, own non-brand CTR at position 5 without AIO 4.0% (with AIO 2.0%); 25% of volume has AIO. Blended CTR = 0.75 x 4.0% + 0.25 x 2.0% = 3.5%. Steady state clicks = 2,100 per month. CVR 1.8%, AOV $85, contribution margin 40%: 37.8 orders, $3,213 revenue, $1,285 contribution per month at steady state. Conservative (position 8, CTR 2.2% blended): about 1,320 clicks. Ramp to steady state by month 9.

### 8.2 Time series model (for existing traffic)
- Use weekly non-brand clicks from 2025-09-15 onward (clean impressions era) or clicks over a longer history.
- Model trend and seasonality (Prophet, ETS, or seasonal naive with last year's pattern); annotate known events (updates, migrations).
- Report the baseline forecast, then add initiative uplifts from the cluster model.
- Track forecast vs actual monthly; compute MAPE; recalibrate quarterly.

### 8.3 Risk adjustments
Apply explicit discounts for: AI feature expansion in your query classes, core update volatility (sites in sensitive niches), seasonality uncertainty, dependency on dev resources.

## 9. SEO testing
SEO tests change something on a group of pages and measure organic outcomes against a control group (you cannot split users because Googlebot sees one version).

Design:
1. Choose a template with many similar pages (at least 100, ideally 500 or more, with combined traffic of thousands of clicks per week) [Practitioner consensus].
2. Randomly split into control and variant groups balanced on traffic and trend (stratified sampling).
3. Apply the change to the variant group only.
4. Measure clicks (and conversions) for 3 to 6 weeks after Google recrawls the variants.
5. Analyze with a counterfactual model: difference in differences or Bayesian structural time series (CausalImpact) using the control group as predictor.
6. Decide: roll out, revert, or iterate. Log in EXPERIMENTS.md.

Good test candidates: title formulas, intro copy, internal link modules, structured data additions, content blocks (FAQs, specs), image changes.

Small sites: use pre/post with a similar untouched page group as control, and treat results as directional.

Tools: SearchPilot, SplitSignal (Semrush), seoClarity, or in-house BigQuery plus CausalImpact.

Experiment row example for EXPERIMENTS.md:
| E012 | 2026-10-12 | seo | If we add specs tables to PDP intros, then non-brand clicks to PDPs rise 5% or more, because pages match spec queries better | Non-brand clicks per PDP | 6/6/7 | Split test, 600 PDPs, stratified 50/50 | 6 weeks after 90% variants recrawled or significance at 95% | backlog | | |

## 10. Alerting thresholds (automate where possible)
| Signal | Threshold | Action |
|--------|-----------|--------|
| Daily non-brand clicks vs same weekday 4 week average | Down over 25% for 2 days | Run regression checks |
| Priority URL returns non 200 or noindex | Any | Immediate alert to dev and SEO |
| robots.txt content changed | Any | Review diff |
| Indexed pages in priority sitemap | Down over 10% in a week | Inspect samples |
| 5xx share in Crawl Stats or logs | Over 1% | Server investigation |
| CWV template moves from Good to Needs improvement | Any | Performance ticket |
| Manual action or security issue | Any | Immediate escalation |
| Confirmed Google update starts or completes | Any | Annotate; diagnosis after completion plus 7 days |

## 11. Bing reporting
- Bing Webmaster Tools Search Performance: clicks, impressions, CTR, position for Bing.
- AI Performance (public preview since 2026-02): citations, cited pages, grounding queries. Report trend and top cited pages; share with ai-search-optimization.
- Microsoft Clarity (free) can complement GA4 for behavior on organic landing pages; hand configuration to cro or measurement.

## 12. Reporting hygiene
- Every number carries source, date range and filters.
- Compare year over year for seasonality and week over week for incidents.
- Explain changes with evidence, not narratives.
- Separate what SEO controls (pages, links, tech) from what it does not (demand, SERP layout, updates).
- Store reports in `ads-master/outputs/seo/` with dates; never overwrite.
