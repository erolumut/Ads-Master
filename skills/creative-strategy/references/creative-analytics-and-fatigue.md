# Creative Analytics and Fatigue

> Purpose: measure creative at the stage where it fails, roll performance up to concepts, detect fatigue before it costs money, and choose tools. Always state the data source and date range. Business KPIs (CPA, ROAS, qualified pipeline) come from the source of truth in `MEASUREMENT.md`; platform numbers are for relative comparison between ads.

## 1. Metric definitions and formulas

| Metric | Formula | Platform fields | What it tells you |
|--------|---------|-----------------|-------------------|
| Hook rate (thumbstop ratio) | 3-second video plays / impressions | Meta: "3-second video plays" and "Impressions" | First 1 to 3 seconds stop the scroll |
| Hook rate (TikTok) | 2-second video views / impressions | TikTok: "2-second video views" | Same, TikTok definition |
| Hold rate (option A) | ThruPlays / 3-second video plays | Meta: "ThruPlays" (played to completion or at least 15 seconds) | Body keeps viewers who were hooked |
| Hold rate (option B) | ThruPlays / impressions | Meta | Combined hook and hold |
| Hold rate (TikTok) | 6-second video views / 2-second video views | TikTok: "6-second video views" | Same idea |
| Retention curve | Video plays at 25%, 50%, 75%, 95%, 100% / video plays | Meta, TikTok, YouTube | Where viewers drop |
| Average watch time | Platform metric | Meta "Video average play time", TikTok "Average play time per video view" | Pacing quality |
| CTR (link) | Link clicks / impressions | Meta "CTR (link click-through rate)"; prefer "Outbound CTR" | Ad creates intent to act |
| CPC (link) | Spend / link clicks | All | Cost of attention that clicks |
| Landing page view rate | Landing page views / link clicks | Meta "Landing page views" | Page load and click quality |
| CVR | Conversions / landing page views (or link clicks) | Platform or GA4 | Message match, offer, page |
| CPA | Spend / conversions | Use source of truth where possible | Business outcome |
| ROAS | Conversion value / spend | Same | Business outcome |
| CPM | Spend / impressions x 1000 | All | Auction cost; rising CPM on the same audience can signal fatigue or quality issues |
| Frequency | Impressions / reach | All | Exposure per person |
| YouTube view rate | Views / impressions | Google Ads | In-stream hook equivalent |
| LinkedIn video completion | Completions / video starts | Campaign Manager | Hold equivalent |

Name these as custom metrics in Ads Manager (Meta "Custom metrics") so every report shows Hook rate, Hold rate and Outbound CTR next to CPA.

**Benchmarks:** practitioners commonly quote hook rates of roughly 25% to 35%+ as good on Meta video and hold rates (ThruPlay over 3-second plays) in the 20% to 40%+ range, but published figures vary by vertical, placement, length and tool definitions [Practitioner consensus, wide variance, not verified]. Use account percentiles instead: top quartile = strong, bottom quartile = broken, computed per placement group and per format over the last 90 days for ads with 5,000+ impressions.

## 2. The diagnosis tree (read in order, fix the first broken stage)

```
1. Hook rate bottom quartile?
   yes -> Hook problem: new first frame, new text hook, new verbal hook; pattern interrupt; open on outcome or problem.
   no  -> 2
2. Hold rate bottom quartile (or retention drops before 50%)?
   yes -> Body problem: pace, payoff the hook by second 5 to 8, cut filler, add re-hook.
   no  -> 3
3. Outbound CTR bottom quartile?
   yes -> CTA and offer problem: explicit CTA, reason to act now, clearer offer, stronger proof.
   no  -> 4
4. Landing page view rate under about 70% of link clicks?
   yes -> Page speed or accidental clicks: hand off to cro and measurement.
   no  -> 5
5. CVR bottom quartile?
   yes -> Message match or offer: hand off to cro with the ad and LP; test angle matched LP.
   no  -> 6
6. CPA above target despite good stage metrics?
   -> Audience or auction cost (CPM), attribution, or price. Check CPM trend, MEASUREMENT.md, AOV. Involve the channel agent.
```

For statics, skip steps 1 and 2: use CTR as the attention metric and compare within statics only.

## 3. Concept level rollups

Ad level analysis misleads: a concept with 6 executions may look mediocre ad by ad but win as a concept. Roll up by the concept ID in the ad name (see [Briefs and naming conventions](briefs-and-naming-conventions.md)).

**Procedure**
1. Export ad level data (section 6) for the last 30 and 90 days.
2. Parse ad names into tokens (concept ID, angle, persona, awareness, format, hook ID, creator, AI flag).
3. Aggregate by concept: spend, impressions, 3-second plays, ThruPlays, link clicks, conversions, value.
4. Compute rates from sums (never average rates across ads).
5. Rank by CPA or ROAS with spend weighting. Flag concepts below the evidence ladder as "insufficient data".
6. Repeat by angle, persona, awareness, format and creator to find patterns.

**pandas script (run with `python3 -I`, file from `ads-master/data/imports/`)**

```python
import sys, pandas as pd, numpy as np
df = pd.read_csv(sys.argv[1])
# Map your export columns to these names first
cols = {"Ad name":"ad_name","Amount spent (USD)":"spend","Impressions":"imps",
        "3-second video plays":"v3","ThruPlays":"thru","Link clicks":"clicks",
        "Purchases":"conv","Purchases conversion value":"value"}
df = df.rename(columns={k:v for k,v in cols.items() if k in df.columns})
tok = df["ad_name"].str.split("_", expand=True)
# Naming grammar: date_concept_angle_persona_aware_format_hook_creator_len_ratio_ver[_aiE]
names = ["launch","concept","angle","persona","aware","fmt","hook","creator","len","ratio","ver"]
for i,n in enumerate(names):
    df[n] = tok[i] if i in tok.columns else np.nan
num = ["spend","imps","v3","thru","clicks","conv","value"]
for c in num:
    if c not in df.columns: df[c] = 0
def roll(by):
    g = df.groupby(by)[num].sum()
    g["hook_rate"] = g.v3 / g.imps
    g["hold_rate"] = g.thru / g.v3.replace(0,np.nan)
    g["ctr"] = g.clicks / g.imps
    g["cvr"] = g.conv / g.clicks.replace(0,np.nan)
    g["cpa"] = g.spend / g.conv.replace(0,np.nan)
    g["roas"] = g.value / g.spend.replace(0,np.nan)
    g["spend_share"] = g.spend / g.spend.sum()
    return g.sort_values("spend", ascending=False)
for by in ["concept","angle","persona","aware","fmt","creator"]:
    print(f"\n== by {by} ==")
    print(roll(by).round(4).to_string())
```

## 4. Fatigue detection

**What fatigue is:** the same people have seen the ad enough that response falls, so cost per result rises. It differs from similarity (many ads that look alike) and from seasonality or auction cost changes.

**Meta native signals** [Official per secondary summaries of Meta Help Center; verify]
- Delivery column can show "Creative limited" (cost per result higher than your past ads for the same optimization event, but less than twice as high) and "Creative fatigue" (cost per result at or above twice past performance). Both are lagging and compare against the account's history. They appear most reliably on ad sets with a single creative.
- Meta can warn before publishing if it predicts fatigue in the first 7 days for some single-creative ad sets.
- A Creative diversity rating (Low, Medium, High) per ad set reportedly appears in some accounts from August 2026 (see diversity module).
- New ads can show "Creative limited" while ramping; wait at least 48 hours before acting on it.

**Leading indicators (act on these first)** [Practitioner consensus]

| Indicator | Fatigue pattern | Check |
|-----------|----------------|-------|
| Hook rate trend | Down 20%+ from the ad's own first 14 day average | Weekly per ad |
| Outbound CTR trend | Down 20%+ from its first 14 days | Weekly per ad |
| CPM on the same ad set | Up 15%+ while account CPM is flat | Weekly |
| Frequency | Rising week over week on a stable audience | Weekly (thresholds vary; Meta states no universal number) |
| CPA | Up 30%+ over its best 7-day window | Weekly |
| Comments | Repeated "I keep seeing this ad" | Weekly scan |

**Fatigue decision rule:** if 2 or more leading indicators fire for 2 consecutive weeks on an ad that carries over 10% of spend, start its replacement now: rung 1 to 3 iterations for a short life extension, plus 2 adjacent new concepts. Propose pausing only the fatigued ad, not the ad set (pausing structures can reset learning; the channel agent decides).

**Winner half-life:** days from launch until the ad's 7-day CPA is 30% worse than its best 7-day CPA. Track the median by format and tier. A shrinking half-life means you need more concept volume or a broader audience.

**Not fatigue (rule these out):** seasonality or promo calendar, tracking breaks (check `measurement`), auction cost spikes across all ads (Q4), landing page or stock changes, budget jumps that pushed into more expensive inventory.

## 5. Reporting template (weekly creative report)

```
# Creative report, week of YYYY-MM-DD
Data: Meta ad level export 2026-09-01 to 2026-09-30 (file ...), TikTok ..., backend orders from ...
## Summary (5 lines)
## Concept leaderboard (spend, CPA/ROAS, hook, hold, CTR, CVR, status)
## Winners this week (with evidence level)
## Fatigue watch (ads with 2+ leading indicators)
## Pattern insights (by angle, persona, awareness, format, creator)
## Decisions: kill, iterate, scale (change list for approval)
## Next slate: concepts and iterations with IDs
## Handoffs requested
```

## 6. Exports to request (when no connector is available)

| Platform | Export | Level | Columns | Range |
|----------|--------|-------|---------|-------|
| Meta Ads Manager | Reports > Export | Ad, with daily breakdown | Ad name, ad ID, post ID, spend, impressions, reach, frequency, CPM, 3-second video plays, ThruPlays, video plays at 25/50/75/95/100%, video average play time, link clicks, outbound clicks, landing page views, purchases or leads, conversion value | Last 30 and 90 days |
| TikTok Ads Manager | Reporting | Ad | Ad name, spend, impressions, CPM, 2-second and 6-second video views, average play time, video views at 25/50/75/100%, clicks, CTR, conversions, CPA | Last 30 days |
| Google Ads | Asset report (PMax, Demand Gen, RSA), video report | Asset and ad | Asset, performance label where shown, impressions, views, view rate, clicks, conversions, cost | Last 30 and 90 days |
| LinkedIn | Campaign Manager creative report | Creative | Spend, impressions, clicks, CTR, video views, completions, leads, conversions | Last 90 days |
| Backend | Orders or CRM with UTM ad ID | Order or lead | Order ID, value, UTM campaign, content (ad ID), new vs returning, lead stage | Same range |

Ask the human to add `utm_content={{ad.id}}` (Meta dynamic parameter) or the platform equivalent so backend outcomes can be joined to ads. Coordinate with `measurement`.

## 7. Tools (verify features and pricing before recommending)

| Tool | What it does for creative | Notes |
|------|---------------------------|-------|
| Motion (motionapp.com) | Creative analytics for Meta, TikTok, YouTube, LinkedIn: visual reports, tagging, comparative views, creative research | Popular with DTC creative strategists |
| Atria (tryatria.com) | Ad library inspiration, creative analytics, AI briefs and concept generation | Combines research and analysis |
| Foreplay (foreplay.co) | Swipe file, ad library discovery, competitor tracking, briefs, analytics module | Strong for research and briefing |
| Triple Whale | Creative analytics within an attribution and data platform for Shopify brands | Uses its own attribution |
| Northbeam | Creative level attribution views | Uses its own attribution model |
| Superads (superads.ai) | Creative analytics and reporting | Verify integrations |
| Segwise (segwise.ai) | AI creative tagging and analytics, strong in mobile apps | Auto-tags creative elements |
| Madgicx, Revealbot, AdsUploader | Automation, bulk upload, reporting | Bulk launching supports naming discipline |
| Platform native | Meta Ads Reporting (custom metrics, breakdowns), TikTok Creative Insights, Google asset reports | Free; enough for Starter and Growth with naming conventions |

**Data access for Claude:** use MCP connectors when the user has them (Meta Marketing API based community servers, Google's open source Google Ads MCP server, Google Analytics MCP server; availability and permissions vary; see `research/creative-strategy.md` Tools section) or CSV exports in `ads-master/data/imports/`. Never request write permissions for analysis tasks.

## 8. Analysis QA checklist

- Date range and attribution setting stated.
- Rates computed from summed numerators and denominators.
- Concepts below the evidence ladder labeled "insufficient data".
- Platform CPA compared to backend for top concepts where possible.
- Placement mix checked (a hook rate shift can be a placement mix shift).
- Statics and videos compared separately on attention metrics.
- Any edit history in the period noted (edits reset learning and distort trends).
