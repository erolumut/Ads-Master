# Search and SEO Competitive Analysis

Who wins the searches that make money, in paid and organic results, and what to do about it. Official auction data first; third party tools for breadth.

## 1. Data sources and what they are good for
| Source | Type | Strength | Weakness | Confidence |
|--------|------|----------|----------|-----------|
| Google Ads Auction Insights (Search, Shopping, PMax where available) | Official, first-party | Exact overlap with competitors in our own auctions | Only auctions we enter; domains, not keywords for others | High |
| Microsoft Ads Auction Insights | Official | Same for Bing and partners | Smaller volume | High |
| Google Search Console | Official, first-party | Our queries, impressions, clicks, positions | No competitor data | High |
| Merchant Center (price competitiveness, best sellers, market insights) | Official | Price position vs market, top products | Ecommerce only; coverage varies by country [verify] | High |
| Google Ads Transparency Center | Official | Competitor ad copy by domain and region | No keywords or spend | High for copy |
| Semrush (Domain Overview, Organic Research, Keyword Gap, Backlink Gap, Advertising Research, PLA research) | Third party estimates | Broad keyword and paid ad history, gap tools | Estimates; databases differ by country | Medium to low |
| Ahrefs (Site Explorer, Organic competitors, Content gap, Paid keywords, Link intersect, Brand Radar for AI) | Third party estimates | Strong backlink index and organic keyword data | Paid data thinner; estimates | Medium |
| Similarweb | Panel plus partner data | Traffic and channel mix estimates, referral and audience overlap | Small sites poorly measured | Medium to low |
| SpyFu | Third party | Long history of paid keywords and ad copy (US heavy) | US centric; estimates | Low to medium |
| Manual SERP sampling | Observation | Ground truth for specific queries, SERP features, AI Overviews | Personalization, location; small samples | High for sampled queries |

Third party tools model traffic from rankings and clickstream panels. Treat absolute numbers as directional; compare competitors within the same tool and database [Practitioner consensus].

## 2. Auction Insights: the official competitor map
Metrics (Google Ads Search):
| Metric | Meaning | Use |
|--------|---------|-----|
| Impression share | Our impressions / eligible impressions | Headroom and pressure |
| Overlap rate | How often a competitor showed when we showed | Who we actually fight |
| Position above rate | How often their ad was above ours when both showed | Aggressiveness |
| Top of page rate | Share of their impressions at the top | Bid and quality strength |
| Absolute top of page rate | Share of their impressions in first position | Same |
| Outranking share | How often we ranked higher or showed when they did not | Our competitiveness |

Procedure:
1. Run Auction Insights at account, campaign and key ad group level for the last 30 days, and the same 30 days a year ago, and week by week for the last 8 weeks.
2. Flag: new domains with overlap above 10%, competitors whose position above rate rose more than 10 points, brand campaign competitors.
3. Cross check new entrants in the Transparency Center (copy and offer) and ad libraries (social activity).
4. Hand to google-ads and microsoft-ads with the evidence; hand offers to growth-orchestrator.

## 3. Paid search competitive analysis
| Question | Method |
|----------|--------|
| Who bids on our brand? | Auction Insights on the brand campaign; manual SERP checks in key cities and devices; Transparency Center by competitor domain |
| Which non brand terms do competitors buy? | Semrush or SpyFu paid keywords (estimates); confirm overlap in Auction Insights |
| What copy and offers win? | Transparency Center text ads, SERP sampling, ad history in SpyFu or Semrush |
| How much do they spend? | Only estimates exist; label low confidence; prefer relative comparisons |
| Shopping position | Merchant Center price competitiveness, Shopping auction insights, manual Shopping SERP checks |

Brand bidding response options (hand to google-ads):
- Defend with a brand campaign at high impression share.
- File a trademark complaint where the platform policy allows restricting trademark use in ad text (keyword bidding on trademarks is generally allowed on Google in most regions) [Practitioner consensus; verify policy per region].
- Affiliate program terms that forbid brand bidding by partners.
- Do not retaliate on their brand without legal review of trademark use in ad text.

## 4. Organic (SEO) competitive analysis
### 4.1 Identify true organic competitors
Use the SEO tool's "organic competitors" report plus a sample of 50 money keywords: count which domains appear in the top 10. Marketplaces, publishers and review sites count; they take clicks even if they do not sell the same thing.

### 4.2 Gap analyses
| Gap | Tool feature | Output |
|-----|--------------|--------|
| Keyword gap | Semrush Keyword Gap, Ahrefs Content gap | Keywords competitors rank for and we do not, with volume, difficulty, intent |
| Content gap | Top pages of competitors | Page types we lack (comparisons, alternatives, calculators, templates, location pages) |
| Backlink gap | Semrush Backlink Gap, Ahrefs Link intersect | Domains linking to 2+ competitors but not to us |
| SERP feature gap | Position tracking with SERP features | Who owns featured snippets, People Also Ask, videos, local packs, AI Overview citations |
| Technical gap | Crawl comparison (speed, indexation, structured data) | Fixes for seo |

Priority score for a gap keyword: monthly volume x commercial intent weight (transactional 1.0, commercial investigation 0.8, informational 0.3) x (1 / difficulty bucket) x AI Overview risk factor (0.6 if an AI Overview usually answers the query) [heuristic].

### 4.3 AI Overviews and zero click in the competitive picture
- Zero click searches reached 68.01% of US Google searches in January to April 2026 (SparkToro clickstream) [Study, 2026]; organic CTR on queries with AI Overviews fell sharply in 2025 with a partial recovery by February 2026 (Seer Interactive) [Study, 2025 to 2026].
- For each priority query, record: AI Overview present (yes or no), brands cited in the AI Overview, ads present above or inside it, competitor ranking. Hand AI citation gaps to ai-search-optimization.

## 5. Traffic and channel mix estimates (Similarweb and peers)
Use to answer "where does a competitor get traffic" (direct, search, social, referral, display, email), not "how much revenue they make".
Rules:
- Compare trends and ratios over 6 to 12 months, not single months.
- Sites under roughly 50k visits per month are often poorly estimated [Practitioner consensus].
- Confirm paid search share with Auction Insights presence and Transparency Center activity.
- Label all numbers low or medium confidence.

## 6. Share of search (brand demand competition)
Share of search = brand's branded search volume / sum of branded search volume for all brands in the category set (Binet, IPA EffWorks 2020). Track monthly with Google Trends (relative) and Keyword Planner or Search Console (absolute anchors). See demand-and-trend-research.md for the procedure.

## 7. Marketplace search (Amazon, Trendyol, Hepsiburada, Noon)
- Sample the top 20 category queries inside each marketplace in the target country; record sponsored vs organic positions by brand, price, rating and review count.
- Amazon sellers can use Brand Analytics (search terms and share) from their own account; third party tools estimate competitor sales [verify ToS].
- Hand findings to growth-orchestrator (marketplace P&L) and commerce-feeds (listings).

## 8. Output: search competition report
1. Summary and decision served.
2. Auction map: competitors by overlap, position above, trend (official data).
3. Brand bidding findings and options.
4. Paid copy and offer themes by competitor (Transparency Center, SERP).
5. Organic gaps: keywords, content, links, SERP features, AI Overview citations; prioritized list.
6. Traffic mix estimates (labeled confidence).
7. Recommendations by owner (google-ads, microsoft-ads, seo, ai-search-optimization, commerce-feeds, growth-orchestrator).

## 9. Pitfalls
- Using one tool's traffic estimate as fact.
- Ignoring publishers and marketplaces as search competitors.
- Comparing data from different country databases.
- Reacting to a competitor's paid keyword list without checking overlap in our own auctions.
- Measuring SEO competition without AI Overview and zero click context.
