# Demand and Trend Research

Measure how much demand exists, where it is growing, when it peaks, and how our share of it moves. Feeds forecasts and seasonality (growth-orchestrator), keyword plans (google-ads, seo), content and prompts (ai-search-optimization), and creative timing (creative-strategy).

## 1. Source catalog
| Source | Gives | Caveats |
|--------|-------|---------|
| Google Trends | Relative search interest (0 to 100) by term, topic, region, time; rising and breakout queries | Normalized and sampled; compare max 5 terms at once; small terms show zeros |
| Google Trends API (alpha announced 2025) | Programmatic consistently scaled data [K; Unverified current access] | Limited access; check status |
| Google Ads Keyword Planner | Monthly volume ranges (exact numbers with active spend), forecasts, keyword ideas, CPC ranges | Volumes grouped for close variants; ranges for low spend accounts |
| Google Search Console | Our impressions and clicks by query, page, country, device | Own site only; anonymized queries hidden |
| Microsoft Advertising Keyword Planner | Bing volumes and ideas | Smaller share |
| TikTok Creative Center (Trends, Keyword Insights) | Rising hashtags, sounds, ad keywords by region | Platform specific |
| Pinterest Trends | Seasonal planning searches on Pinterest | Strong for home, fashion, food, events |
| YouTube search and Trends | Video demand | |
| Amazon Brand Analytics (sellers) | Top search terms and click share on Amazon | Own seller account required |
| Marketplace search suggestions (Amazon, Trendyol, Hepsiburada, Noon) | Shopper vocabulary | Manual |
| Third party volume estimators (Semrush, Ahrefs, Glimpse, Exploding Topics) | Absolute estimates, trend discovery | Estimates; label medium or low confidence |
| AI assistant prompt data | No official prompt volume exists; some vendors estimate | Low confidence |
| Statistical offices and industry bodies | Category sales, consumer spending | Lagged; definitions differ |

## 2. Google Trends procedure
1. Use topics (entity) rather than search terms when available to merge spellings and languages; use terms for specific phrasings.
2. Set region and time: 5 years for seasonality and trend; past 12 months for current shape; past 90 days for recent spikes.
3. Choose a category filter if the term is ambiguous.
4. Compare up to 5 items; include a stable anchor term to stitch multiple comparisons together when you need more than 5.
5. Export CSV; record capture date (values can shift slightly between pulls because of sampling).
6. Look at "Related queries: rising" for new modifiers and "breakout" (very large relative growth) for emerging needs.
7. Validate any breakout with a second source (Keyword Planner, TikTok, Reddit volume) before acting.

## 3. Keyword volume research
1. Seed list: product terms, problem terms, use case terms, competitor brands, comparison terms, local terms, AUDIENCE.md questions.
2. Expand with Keyword Planner, Search Console, autocomplete, People Also Ask, marketplace suggestions, SEO tools.
3. Classify intent: transactional, commercial investigation, informational, navigational, local.
4. Group into topics (clusters) with summed volume, average CPC, intent mix, AI Overview frequency (seo agent).
5. Market specific language: in Turkey cover diacritic and non diacritic spellings and suffix forms; in Arabic markets cover Arabic and English and transliterations; in the EU cover each language separately.

Demand sizing from search (addressable search revenue):
```
Addressable revenue per month ~ sum over keywords (volume x expected CTR at target position x site CVR x AOV)
```
Use conservative CTRs on queries with AI Overviews (zero click shares rose to about 68% of US Google searches in early 2026 per SparkToro) [Study, 2026].

## 4. Seasonality index
```
For each week or month m: index_m = demand_m / average demand across the year
Use 2 to 5 years and average the index per period; smooth with a 3 period moving average.
```
Sources in order of preference: own revenue or conversions, Search Console impressions, Google Trends for the category, Keyword Planner monthly volumes. Note moving holidays (Ramadan and Eid move about 11 days earlier each year; Easter moves; Chinese New Year moves). Hand the index to growth-orchestrator for budget weights and forecasts.

## 5. Share of search
```
Share of search (brand b, month m) = branded search volume of b / sum of branded volume of all brands in the set
```
1. Build the brand set (us plus 3 to 7 competitors) including common misspellings.
2. Pull Google Trends for the set (stitch with an anchor if more than 5); convert to shares per month.
3. Anchor to absolute volumes with Keyword Planner or GSC brand impressions.
4. Track a 12 month rolling average. A rising share tends to lead market share gains and a falling share tends to lead losses (Binet, IPA EffWorks 2020) [Study, 2020].
5. Report monthly in the movement summary; quarterly to growth-orchestrator as a brand KPI.

## 6. Trend validation checklist
A trend is actionable when:
- [ ] It appears in at least two independent sources (for example Trends and TikTok, or Trends and Reddit).
- [ ] It has grown for 3+ consecutive months or shows a repeatable seasonal pattern.
- [ ] It maps to something we sell or can credibly say.
- [ ] There is a channel where we can reach it (keywords, creators, prompts).
- [ ] The economics work (CPC and conversion assumptions inside breakeven).
Fads: sharp spikes with fast decay, usually social driven; use for creative timing only.

## 7. Demand by channel (where the demand lives)
| Signal | Channel implication |
|--------|---------------------|
| High search volume with commercial intent | Google and Microsoft Search, Shopping, SEO |
| High marketplace search, low Google search | Marketplace ads and listings |
| Strong TikTok and Instagram trend, low search | Demand creation channels; search will follow if it sticks |
| Many Reddit and forum questions | Community presence, SEO and AI citation strategy, Reddit ads test |
| Questions asked in AI assistants (from sales or surveys) | AI visibility program, ChatGPT ads test |
| Pinterest planning searches months ahead | Pinterest timing for seasonal categories |

## 8. Output: demand report
1. Summary and decision served.
2. Demand size: topics with volumes (source, range, confidence), addressable revenue estimate.
3. Trend: 5 year and 12 month view, growth rates, rising queries.
4. Seasonality index table and moving holiday notes.
5. Share of search: us vs competitors, trend.
6. Demand by channel.
7. Recommendations by owner, with test hypotheses.

## 9. Pitfalls
- Treating Google Trends values as absolute volumes.
- Comparing Trends exports pulled on different days without an anchor.
- Mixing markets or languages in one volume number.
- Ignoring zero click effects when converting search volume into traffic.
- Acting on a single breakout query.

## 10. Worked example: seasonality index
Illustrative monthly category demand (Search Console impressions, 2 year average):
| Month | Avg impressions | Index (month / annual mean) |
|-------|-----------------|-----------------------------|
| Jan | 80,000 | 0.80 |
| Feb | 85,000 | 0.85 |
| Mar | 95,000 | 0.95 |
| Apr | 100,000 | 1.00 |
| May | 105,000 | 1.05 |
| Jun | 90,000 | 0.90 |
| Jul | 85,000 | 0.85 |
| Aug | 90,000 | 0.90 |
| Sep | 100,000 | 1.00 |
| Oct | 110,000 | 1.10 |
| Nov | 150,000 | 1.50 |
| Dec | 110,000 | 1.10 |
Annual mean = 100,000. November at 1.50 means plan about 50% more demand than an average month; growth-orchestrator uses this for budget weights and forecasts.

## 11. Script: seasonality index and share of search from exports
```python
# python3 -I demand.py trends.csv   (columns: month,brand_us,brand_a,brand_b,category)
import csv, sys, statistics as st
rows = list(csv.DictReader(open(sys.argv[1])))
brands = [c for c in rows[0] if c.startswith("brand_")]
cat = [float(r["category"]) for r in rows]
mean = st.mean(cat)
print("month,season_index," + ",".join(f"sos_{b}" for b in brands))
for r, c in zip(rows, cat):
    total = sum(float(r[b]) for b in brands) or 1.0
    shares = [f"{float(r[b]) / total:.3f}" for b in brands]
    print(f"{r['month']},{c / mean:.2f}," + ",".join(shares))
```
Run on exports pulled the same day, or stitched with an anchor term. Report 12 month rolling averages for share of search.

## 12. Share of search worked example
Illustrative Google Trends values (same pull) for September: us 24, competitor A 48, competitor B 18, competitor C 10. Total 100. Share of search: us 24%, A 48%, B 18%, C 10%. If our 12 month rolling share moved from 21% to 24% while A moved from 52% to 48%, we are gaining mental availability; check market share data or sales trends to confirm.
