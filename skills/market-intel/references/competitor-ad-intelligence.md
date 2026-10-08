# Competitor Ad Intelligence

How to read every major ad transparency source, pull data where an API exists, and turn competitor ads into decisions for creative-strategy and the channel agents.

Verification note: library behaviors below reflect official documentation as known through mid 2026 and the October 2026 sweep; field lists and regional coverage change. Confirm in the Freshness Protocol before relying on a specific field.

## 1. Source map
| Source | URL | What you can see | Coverage limits | Access |
|--------|-----|------------------|-----------------|--------|
| Meta Ad Library | https://www.facebook.com/ads/library/ | Active ads across Facebook, Instagram, Messenger, Audience Network and Threads, with creative, start date, platforms, variations; filters by country, ad category, advertiser, keyword, media type, platform | Outside the EU and UK only active commercial ads are shown; inactive commercial ads disappear | Public, no login |
| Meta Ad Library (EU, DSA) | Same | For ads delivered in the EU: inactive ads retained (about one year), reach estimates, targeting summary (age, gender, location), payer and beneficiary | EU delivered ads only | Public |
| Meta Ad Library Report and political archive | https://www.facebook.com/ads/library/report/ | Spend on social issue, election and political ads by advertiser and region | Meta stopped these ads in the EU from October 2025 | Public |
| Meta Ad Library API | https://www.facebook.com/ads/library/api/ | Programmatic access to EU delivered ads (all categories) and political or issue ads in covered countries | No API for non EU commercial ads | Developer account, identity confirmation |
| Google Ads Transparency Center | https://adstransparency.google.com/ | Ads from verified advertisers on Search, YouTube, Display, Shopping and other Google surfaces; filter by advertiser or domain, region, format, date range; "last shown" dates and variation counts | Text ads show as served templates; no spend data for commercial ads | Public |
| Google political ads data | Google transparency report and public datasets | Political ad spend and creatives where Google serves political ads | Google stopped political ads in the EU around October 2025 | Public |
| TikTok Creative Center | https://ads.tiktok.com/business/creativecenter/ | Top Ads by region, industry, objective and period; trends (hashtags, songs, creators), keyword insights, top products | Curated inspiration, not a complete library | Public; more with login |
| TikTok Ad Library | https://library.tiktok.com/ | Ads shown in the EU and certain other regions with advertiser, dates, targeting and reach information (Commercial Content Library) | Region limited | Public; research API on application |
| LinkedIn Ad Library | https://www.linkedin.com/ad-library/ | Ads run on LinkedIn in the past year, by advertiser, keyword, country and date; EU served ads add targeting and impression information | No API | Public |
| Microsoft Ad Library | https://adlibrary.ads.microsoft.com/ | Ads served in the EU on Microsoft surfaces with advertiser and date details [Unverified current fields] | EU focus | Public |
| Other DSA repositories | X Ads Repository, Pinterest, Snapchat, Amazon and app store repositories in the EU [Unverified URLs and fields] | EU served ads | EU only | Public |
| AI assistant ads (ChatGPT, AI Mode, AI Overviews) | No public library known [Unverified] | Manual observation as a normal user | Ads in ChatGPT show only to Free and Go users in eligible markets (2026) | Manual |

## 2. Meta Ad Library: step by step
1. Open the library, choose the country (the market you compete in), Ad category "All ads".
2. Search the competitor's page name (not a keyword) and select the page so results are exact.
3. Filters: Active status = Active ads (default view outside the EU); Platform; Media type; Language.
4. Sort mentally by start date. Note the oldest running ads and how many ads share the same creative ("This ad has multiple versions").
5. Open each concept: copy primary text, headline, CTA, landing URL, format, aspect ratio, start date, platforms.
6. EU markets: switch to "All" status and read inactive ads, reach estimates and targeting summary for each ad. This reveals what they tested and stopped.
7. Capture screenshots or snapshot URLs into the swipe file (section 7) with the capture date.

Reading signals:
| Signal | What it suggests | Confidence |
|--------|------------------|-----------|
| Ad running 30 to 90+ days with many versions | Likely a scaled winner | Medium [Practitioner consensus] |
| Burst of 20+ new ads in a week | Creative testing push, launch or promotion | Medium |
| Same concept across many formats and languages | Proven concept being rolled out | Medium |
| Mostly catalog or dynamic ads | Retargeting or Advantage+ catalog heavy strategy | Medium |
| EU reach far higher for one concept | Budget concentration on that concept | High (for EU delivery) |
| Very few active ads from a big brand | Spend may sit in other channels, or creative is consolidated | Low |

## 3. Meta Ad Library API (EU delivered ads, political and issue ads)
Setup: a Meta developer account, identity confirmation for the Ad Library API, an app and an access token. Use the current Graph API version.

```bash
# Pull EU delivered ads for one page in Germany, all statuses
curl -G "https://graph.facebook.com/v${GRAPH_VERSION}/ads_archive" \
  --data-urlencode "access_token=${META_TOKEN}" \
  --data-urlencode 'ad_reached_countries=["DE"]' \
  --data-urlencode "ad_active_status=ALL" \
  --data-urlencode "ad_type=ALL" \
  --data-urlencode 'search_page_ids=["<PAGE_ID>"]' \
  --data-urlencode "fields=id,page_name,ad_creation_time,ad_delivery_start_time,ad_delivery_stop_time,ad_creative_bodies,ad_creative_link_titles,ad_creative_link_descriptions,ad_snapshot_url,publisher_platforms,languages,eu_total_reach,target_ages,target_gender,target_locations,beneficiary_payers" \
  --data-urlencode "limit=100"
```
Pagination: follow `paging.next`. Respect rate limits. Field names and availability change between versions [verify in the API docs before running].

```python
# python3 -I longevity.py ads.json   (ads.json = concatenated "data" arrays from the API)
import json, sys, datetime as dt
ads = json.load(open(sys.argv[1]))
today = dt.date.today()
rows = []
for a in ads:
    start = dt.date.fromisoformat(a["ad_delivery_start_time"][:10])
    stop = a.get("ad_delivery_stop_time")
    end = dt.date.fromisoformat(stop[:10]) if stop else today
    body = (a.get("ad_creative_bodies") or [""])[0][:80]
    rows.append(((end-start).days, a.get("eu_total_reach", 0), body))
rows.sort(reverse=True)
for days, reach, body in rows[:25]:
    print(f"{days:4d} days | reach {reach} | {body}")
```
Group near identical bodies to count variants per concept; the longest running high reach concepts are the first candidates for analysis.

## 4. Google Ads Transparency Center: step by step
1. Search by advertiser name or by domain (domain search catches multiple advertiser accounts and resellers).
2. Region = market; Format = Text, Image or Video; Date range = last 30 days for current activity, "Any time" for history.
3. For text ads, record headline and description themes, offers, sitelink themes if visible, and the landing domain.
4. For YouTube and Display, record hook, length, CTA, brand timing.
5. Note "last shown" dates to tell live from paused.
6. For a competitor bidding on your brand, search their domain and look for ads that mention your brand or category comparisons; confirm in Auction Insights (search-and-seo-competitive-analysis.md).
Limits: no spend, no keywords, no targeting outside EU details; ad counts include all variations.

## 5. TikTok sources
- **Creative Center Top Ads**: filter by region, industry, campaign objective, period and format. Use to see what high engagement ads in the category look like (hooks, pacing, creator style, captions). It is curated by TikTok and biased toward strong engagement; it is not a competitor census.
- **Keyword Insights and Trends**: phrases used in top ads, rising hashtags and sounds by region.
- **TikTok Ad Library (Commercial Content Library)**: for EU and other covered regions, search an advertiser to see ads with dates and targeting and reach information.
- **Organic profiles**: many TikTok ads are Spark Ads (boosted organic posts); the competitor's profile shows candidates. Posts with ad style captions and very high views relative to follower count are often boosted [Practitioner consensus].

## 6. LinkedIn and Microsoft
- LinkedIn Ad Library: search the company, review formats (single image, document, video, Thought Leader Ads from employee profiles), offers (demo, report, webinar), and the cadence of new ads. For EU served ads, review targeting fields to infer ICP (industries, seniority) [verify field availability].
- Microsoft Ad Library: check EU served search and audience ads for competitors that skip Google or test copy on Bing.

## 7. Swipe file and capture standard
One row per concept (not per ad):
| Field | Example |
|-------|---------|
| Capture date, market, language | 2026-10-08, DE, de |
| Competitor and source | BrandX, Meta Ad Library (EU) |
| Concept ID and name | BX-07 "Doctor explains ingredient" |
| Angle (frame) | Authority or expert |
| Funnel stage | Problem aware |
| Format and length | UGC video 22s, 9:16 |
| Hook (first line or first 3 seconds, verbatim) | "My dermatologist told me to stop doing this" |
| Offer | 20% off first order, free shipping over EUR 40 |
| Proof | Clinical claim, 4.6 stars from 12k reviews |
| CTA and landing page | Shop now, /pages/routine-quiz |
| Longevity and variants | Running 64 days, 9 versions |
| EU reach (if available) | 1.2M |
| Our read (inference) | Scaled concept; quiz funnel likely converts |
| So what (owner) | Test quiz entry page (cro); authority angle with our expert (creative-strategy) |

Store screenshots or snapshot links, not downloaded copies of competitor video files, unless the human approves internal reference use.

## 8. Analysis method (competitor ad teardown)
1. Census: count active ads, new ads in the last 7 and 30 days, concepts, formats, languages, landing pages per competitor.
2. Longevity distribution: share of ads older than 30, 60, 90 days.
3. Concept clustering: group ads into concepts; count variants per concept.
4. Angle and offer coding with the frames in SKILL.md.
5. Gap analysis: angles and pains in our VoC that no competitor uses; offers nobody makes; formats nobody uses in the category.
6. Landing page review for the top 3 concepts per competitor.
7. Recommendations: 3 to 5 concepts for creative-strategy, offer ideas for growth-orchestrator, page ideas for cro, each as a testable hypothesis.

Competitor scorecard (per competitor, monthly):
| Metric | This month | Last month | Change |
|--------|-----------|------------|--------|
| Active ads (Meta, market) | | | |
| New ads last 30 days | | | |
| Concepts | | | |
| Share of ads older than 60 days | | | |
| Dominant angle | | | |
| Dominant format | | | |
| Offer headline | | | |
| Google text ad themes | | | |
| TikTok presence (Top Ads or library) | | | |

## 9. Interpreting volume and cadence
| Pattern | Likely strategy | Response to consider |
|---------|-----------------|----------------------|
| High volume, short lifespans | Aggressive creative testing (often Advantage+ or Smart+ heavy) | Match concept diversity, not volume; mine their survivors |
| Low volume, long lifespans | Few proven winners, possibly under invested in creative | Out test them with new angles |
| Seasonal bursts | Promotion driven | Prepare counter offers ahead of their calendar |
| Many languages and markets | International scaling | Watch for entry into our markets |
| Heavy catalog ads | Retargeting and dynamic product focus | Compete on new customer acquisition creative |

## 10. Pitfalls
- Copying a competitor's winning ad: you inherit their positioning and look like a follower; mine the angle, not the execution.
- Treating Top Ads as competitor intelligence: it is curated inspiration.
- Ignoring markets: the library shows ads per country; an ad absent in one market may run in another.
- Reading longevity as profitability without checking variants and reach.
- Automated scraping of libraries without API permission: may breach terms of service (tools-api-mcp.md).
- Forgetting capture dates: competitor sets change weekly.
