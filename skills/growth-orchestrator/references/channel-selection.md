# Channel Selection

Pick the fewest channels that can reach the goal, fund each at its minimum viable budget, and add the next one only when the evidence says so.

## 1. Channel roles
Every channel gets one primary role in `STRATEGY.md`. A channel with no clear role is a candidate for cutting.

| Role | Job | Typical channels | Primary KPI | Guardrail |
|------|-----|------------------|-------------|-----------|
| Demand capture | Convert people already looking | Google and Microsoft Search, Shopping, Amazon Sponsored Products, Apple Ads, ChatGPT ads on high intent prompts, local services ads | CPA, ROAS, POAS | Impression share on core terms |
| Demand creation | Make new people want it | Meta, TikTok, YouTube, CTV, Pinterest, Snapchat, Reddit, creators, LinkedIn (B2B) | nCAC, aMER, incremental conversions | Frequency, CPM, new customer share |
| Retargeting | Close people who engaged | Meta, Google, TikTok, display | Incremental CPA | Share of spend under 10 to 20% [Practitioner consensus] |
| Retention and LTV | Repeat purchase, expansion | Email, SMS, WhatsApp, push, loyalty | Repeat rate, revenue per subscriber | Unsubscribe and complaint rates |
| Visibility | Be found and recommended organically | SEO, AI search optimization, review sites, PR | Non brand clicks, AI share of voice | Content cost per visit |

## 2. Decision trees by business model

### 2.1 Ecommerce
```
Has a product feed and Merchant Center?
  yes -> Start: Google Shopping or PMax (feed based demand capture) + brand search protection.
  no  -> Fix feed (commerce-feeds) unless products are custom or non catalog.
AOV under ~$40 and impulse category (fashion, beauty, gadgets, home decor)?
  yes -> Meta first for demand creation, then TikTok (and TikTok Shop where available).
  no  -> Meta + Google Search on category terms; YouTube and Demand Gen at Growth tier.
Strong repeat purchase (consumables, subscription)?
  yes -> Email/SMS flows from day one; judge acquisition on 90 to 180 day LTV.
Selling on Amazon, Trendyol, Hepsiburada or another marketplace?
  yes -> Marketplace ads (Sponsored Products or local equivalent) protect share of shelf; treat as separate P&L.
Scale tier and above -> add Microsoft (Shopping, PMax), Pinterest (home, fashion, food), affiliates, CTV test.
```

### 2.2 Lead gen (B2C services, finance, education, home services)
```
Is there search demand for the service (Keyword Planner volume in target geo)?
  yes -> Google Search first (exact and phrase on high intent), call extensions or call ads, Microsoft Search second.
  no  -> Meta lead ads or click to message (WhatsApp in MENA, Turkey, LATAM, India).
Can CRM send qualified status back within 7 days?
  yes -> Optimize to qualified lead via offline conversions on every channel.
  no  -> Fix this first (measurement). Optimizing to raw leads buys junk.
Local business?
  yes -> Google Business Profile + Local Services Ads (where available) + local search radius campaigns.
```

### 2.3 B2B SaaS
```
ACV under ~$3k (self serve, PLG)?
  yes -> Google Search (category, problem, competitor terms), review sites (G2, Capterra), Meta and Reddit for niche communities, ChatGPT ads test.
ACV $3k to $25k?
  -> Search + LinkedIn (Thought Leader Ads, lead gen forms to qualified leads) + retargeting.
ACV over $25k (sales led, enterprise)?
  -> ABM on LinkedIn with account lists, intent data, events, partner marketing. Paid search on high intent only.
All: organic and AI visibility on comparison and "best X for Y" prompts is a demand capture channel in 2026.
```

### 2.4 Local services
Google Search + Local Services Ads (where offered) + Google Business Profile optimization, then Meta local awareness and retargeting, then Microsoft. Track calls and booked jobs, not form fills.

### 2.5 App
iOS: Apple Ads (search results first), then Meta and TikTok app campaigns. Android: Google App campaigns first. Measure with SKAdNetwork or AdAttributionKit on iOS plus an MMP; judge on D7 and D30 cohorts.

### 2.6 Marketplace or publisher
Spend on the constrained side only. Supply side often uses LinkedIn, Meta and search on "sell my X" terms; demand side uses search and Meta. Publishers buy traffic only when revenue per visit exceeds cost per visit with margin.

## 3. By budget tier
| Tier | Monthly paid media | Paid channels | Typical mix | Test budget |
|------|--------------------|---------------|-------------|-------------|
| Starter | under $3k | 1 to 2 | 70 to 100% in the best capture channel; rest in one creation channel or retargeting | 0 to 10% (focus) |
| Growth | $3k to $30k | 2 to 4 | Capture 40 to 60%, creation 30 to 50%, retargeting under 15% | 10% |
| Scale | $30k to $300k | 4 to 7 | Diversified; no channel over ~60% unless proven incremental | 10 to 20% |
| Enterprise | over $300k | 6+ | Portfolio managed with MMM and lift tests | 10 to 20% |

Signal tiers (conversions per month per channel): Starter under 30, Growth 30 to 300, Scale 300 to 3,000, Enterprise multi market. Below about 30 per month, optimize to a higher volume event (add to cart, qualified lead, trial start) and consolidate structure.

## 4. By stage and geography
| Stage | Channel guidance |
|-------|------------------|
| Pre product market fit | One channel for learning; buy signal, not scale |
| Early traction | Make one channel profitable at scale before adding the second |
| Scaling | Add channels on diminishing returns evidence (section 6) |
| Mature | Optimize portfolio with incrementality; add brand and new markets |

| Geo | Notable channel facts (verify in the geo module and with market-intel) |
|-----|---------------------------------------------------------------------|
| US | Full stack available, including ChatGPT ads self serve (May 2026), Local Services Ads, CTV marketplaces, retail media networks |
| EU and UK | Consent drives signal loss; Meta less personalized ads option in EU from January 2026; no political or social issue ads on Meta or Google in the EU since October 2025 |
| Turkey | Google dominant in search; Meta, YouTube and TikTok heavy usage; marketplace ads (Trendyol, Hepsiburada, Amazon.com.tr) central for ecommerce; WhatsApp is the default messaging channel; ad spend carries 15% withholding plus reverse charge VAT on foreign invoices (geo module) |
| MENA and GCC | Snapchat and TikTok strong in Saudi Arabia and the Gulf; Arabic and English creative; BNPL (Tabby, Tamara) and cash on delivery matter; Ramadan dominates the calendar |
| Other notable search markets | Naver (Korea), Yahoo! JAPAN and LINE (Japan), Baidu (China), Yandex (Russia), Seznam (Czech Republic) [Practitioner consensus] |

## 5. Minimum viable budget (MVB) per channel
Formula for algorithm driven channels:
```
MVB per month = target CPA x weekly conversions needed to exit learning x 4.3 x number of learning units (ad sets or campaigns)
```
Worked example: Meta, target CPA $40, about 50 optimization events per ad set per week to exit learning, 2 ad sets: 40 x 50 x 4.3 x 2 = $17,200 per month. If that is not affordable: one ad set, optimize to a cheaper upstream event, or accept a slower learning phase and judge over 4 weeks.

| Channel | Platform minimum | Learning or signal guidance | Practical minimum test (per month) | Evidence |
|---------|------------------|-----------------------------|------------------------------------|----------|
| Google Search | No platform minimum | Smart Bidding needs steady conversions; tCPA and tROAS work better with 30+ conversions per month per campaign | $1.5k to $3k on high intent terms | [Practitioner consensus]; Google Ads Help bidding docs |
| Google PMax | No minimum | Google guidance: daily budget at least about 3x target CPA | 3 x CPA x 30 | [Official, verify current guidance] |
| Google Demand Gen and YouTube | No minimum | Conversion bidding needs volume; start on clicks or conversions with a generous target | $3k to $5k | [Practitioner consensus] |
| Meta | About $1 per day technical minimum | Learning phase ends after about 50 optimization events per ad set in 7 days | 50 x CPA x 4.3 per ad set; $3k is a common floor | [Official, Meta Business Help Center "About the learning phase"] |
| TikTok | $50 per day campaign, $20 per day ad group | About 50 conversions per ad group per week | $3k to $5k | [Official, TikTok Ads Help] |
| LinkedIn | $10 per day campaign | High CPCs (often $5 to $15+ in competitive B2B) need budget for statistical reads | $3k to $5k | [Official minimum]; CPC range [Practitioner consensus] |
| Microsoft Ads | Low | Imports Google structure; smaller volume | 10 to 20% of Google Search budget | [Practitioner consensus] |
| ChatGPT ads | $25 per day minimum daily budget in self serve (OpenAI help as of 2026-09, per research/chatgpt-ads.md); pilot launched with reported $200k minimum (Feb 2026) | CPM, CPC and conversion bidding; OpenAI suggests $3 to $5 starting CPC bids | $2k to $5k test | [Official, 2026-09 via chatgpt-ads dossier]; chatgpt-ads agent verifies |
| Reddit | Low daily minimum per ad group [Unverified exact value] | Conversion optimization needs pixel + CAPI | $2k to $5k | [Practitioner consensus] |
| Pinterest | Low | Performance+ automation; long consideration | $2k to $5k | [Practitioner consensus] |
| Snapchat | About $5 per day per ad set [Unverified current value] | Pixel + CAPI; young audience | $2k to $5k | [Practitioner consensus] |
| Amazon Sponsored Products | $1 per day | Keyword and ASIN targeting | $1k to $3k per marketplace | [Official, Amazon Ads] |
| Apple Ads | No minimum | Search results campaigns on brand, category, competitor | $1k to $3k | [Practitioner consensus] |
| CTV programmatic | DSP and publisher minimums vary widely | Needs geo lift or MMM to read | $10k to $50k for a readable geo test | [Practitioner consensus] |

All test minimums are priors. Recompute with the MVB formula using the project's target CPA.

## 6. When to add a channel (all must be true)
1. Current channels show diminishing returns: marginal CPA at the last budget step is at least 20% worse than average CPA, or impression share lost to rank, frequency or audience size limits growth, for 2 or more weeks after optimizations.
2. Unit economics allow a learning period: the business can fund MVB for 8 to 12 weeks at a CPA up to about 1.5 times target during learning.
3. Measurement is ready: pixel or SDK, server-side events, conversion definitions and UTMs in place before launch (measurement agent sign off).
4. Creative capacity exists: at least 5 to 10 native concepts for creation channels.
5. The audience is there: market-intel or platform planners confirm reach in the target geo and segment.
6. A success criterion is written in EXPERIMENTS.md: KPI, threshold, read date, and how incrementality will be judged (holdout, geo, or MER change).

## 7. New channel test protocol
| Week | Action |
|------|--------|
| 0 | Measurement setup verified; baseline MER and nCAC recorded; EXPERIMENTS.md row |
| 1 to 2 | Launch at MVB with 3 to 5 concepts; no judgment except tracking sanity |
| 3 to 4 | First read on leading indicators (CTR, CVR, CPA trend); kill only on clear failure (CPA over 3x target with sufficient spend) |
| 5 to 8 | Iterate creative and structure; compare CPA to 1.5x target ceiling |
| 9 to 12 | Verdict: incremental read (geo split, holdout, or MER and new customer change), then scale, iterate one more cycle, or stop |

## 8. When to cut or shrink a channel
- Incrementality test shows iROAS below breakeven after a fair test.
- Marginal CPA above max acceptable marginal CPA for 4 weeks with no fixable cause.
- It duplicates another channel's role with worse economics (for example retargeting on two platforms hitting the same users).
- It cannot be measured at all and is not a deliberate brand bet with a brand KPI.
Shrink in steps (minus 20 to 30% per week) and watch MER and branded search for 2 to 4 weeks before cutting fully. Cuts that hurt demand creation can take weeks to show in search demand.

## 9. Common expensive mistakes
- Starter budgets spread over four channels: every algorithm stays in learning.
- Adding a channel because a competitor is there, without a role or a success criterion.
- Judging a creation channel on last click: it will always look worse than search.
- Launching a new channel during peak season when CPMs are highest and baselines are distorted.
- Retargeting share creeping above 20% of spend: high attributed ROAS, low incrementality.
