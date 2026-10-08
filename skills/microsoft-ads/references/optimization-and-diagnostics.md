# Optimization and Diagnostics

> Scope: the weekly optimization routine, search term and publisher work, Microsoft vs Google parity analysis, diagnostic trees for common failures, and how to run Experiments.

## 1. Weekly optimization routine (60 to 120 minutes at Growth tier)

| Step | Report (UI name) | Action | Output |
|------|------------------|--------|--------|
| 1 | Campaigns, last 7 and 28 days vs previous | Flag campaigns off target by 15%+ | Watch list |
| 2 | Search term report, last 28 days | Add negatives, promote winners to exact or phrase | Negative list changes |
| 3 | Website URL (publisher) report, last 30 days | Exclude failing publishers | Exclusion list changes |
| 4 | Ad distribution or network segment | Check owned and operated vs partners vs audience share | Distribution note |
| 5 | Impression share and lost IS (budget, rank) | Budget or quality actions | Budget proposals |
| 6 | Ads and assets | Replace low performers, fix disapprovals | Asset tasks |
| 7 | Audiences, age, gender, device, LinkedIn layers (every 2 weeks) | Bid adjustments or exclusions | Adjustment list |
| 8 | PMax: share of voice, search insights, landing page report | Negatives, URL exclusions, asset changes | PMax tasks |
| 9 | Experiments | Read results, stop or apply | EXPERIMENTS.md update |
| 10 | Change history | Confirm nothing unexpected (imports, auto-apply) | Journal if anything found |

## 2. Search term mining

Procedure:
1. Export the search term report (28 to 90 days) with columns: search term, keyword, match type, campaign, ad group, impressions, clicks, spend, conversions, conversion value.
2. Classify each term: relevant converting, relevant not yet converting, irrelevant.
3. Negatives: irrelevant terms with any spend; relevant terms with spend over 2x target CPA and zero conversions (add as exact negatives to the specific ad group, not account wide).
4. Promotions: converting terms not yet keywords become exact or phrase keywords in the right ad group.
5. N-gram pass: split terms into 1, 2 and 3 word grams, aggregate spend and conversions, find wasted grams ("free", "jobs", "salary", "login", "diy", competitor support terms).
6. Add shared negatives for grams that waste spend across campaigns.

N-gram script (Python, runs on an exported CSV in `ads-master/data/imports/`):
```python
import csv, sys
from collections import defaultdict

path = sys.argv[1]  # e.g. ads-master/data/imports/2026-10-01_microsoft_search_terms.csv
stats = defaultdict(lambda: {"spend": 0.0, "conv": 0.0, "clicks": 0})
with open(path, newline="", encoding="utf-8-sig") as f:
    for row in csv.DictReader(f):
        words = row["Search term"].lower().split()
        spend = float(row["Spend"].replace(",", "") or 0)
        conv = float(row["Conversions"].replace(",", "") or 0)
        clicks = int(float(row["Clicks"].replace(",", "") or 0))
        grams = set()
        for n in (1, 2, 3):
            grams.update(" ".join(words[i:i+n]) for i in range(len(words)-n+1))
        for g in grams:
            stats[g]["spend"] += spend
            stats[g]["conv"] += conv
            stats[g]["clicks"] += clicks

rows = sorted(stats.items(), key=lambda kv: kv[1]["spend"], reverse=True)
print("gram,spend,clicks,conversions,cpa")
for g, s in rows[:200]:
    cpa = s["spend"] / s["conv"] if s["conv"] else ""
    print(f'"{g}",{s["spend"]:.2f},{s["clicks"]},{s["conv"]:.1f},{cpa}')
```
Column names vary by export language and report version; map them before running.

## 3. Microsoft vs Google parity report (monthly)

Purpose: decide where Microsoft should diverge.
1. Export keyword level data from both platforms for the same 30 to 90 days, same conversion definition.
2. Join on normalized keyword text plus match type (never on IDs).
3. Compute for each keyword: CPC ratio (MS / G), CTR ratio, CVR ratio, CPA ratio, impression share on each.
4. Segment: brand, non-brand core, discovery.
5. Read:
| Pattern | Meaning | Action |
|---------|---------|--------|
| CPC ratio under 0.8, CVR ratio near 1 | Microsoft cheaper, same quality | Raise Microsoft bids or budget to capture more volume |
| CVR ratio under 0.7 | Traffic quality, device mix, partners or tracking | Check network segment, device, publisher report, UET |
| CPA ratio over 1.3 for 2 months | Microsoft underperforms on these terms | Diverge bids, test partners off, check landing page |
| Microsoft IS much lower than Google on profitable terms | Budget or rank limited | Budget or bid increase |
6. Save as `YYYY-MM-DD_microsoft-ads_parity-report.md`.

## 4. Diagnostic trees

### 4.1 Conversions dropped suddenly (day over day or week over week 50%+)
```
Did clicks drop too?
  yes -> go to 4.3 (volume drop)
  no  -> tracking suspected
     Is UET firing on the conversion page? (Tag Helper, bat.bing.com requests)
       no  -> tag removed, GTM change, CMP blocking: hand off to measurement (P1)
       yes -> Is the goal status "Recording conversions"? Was the goal edited (change history)?
            edited -> revert or document
            fine   -> EEA/UK/CH traffic? Run consent test (asc=D then asc=G)
                       failing -> CMP change: hand off to measurement
                       fine    -> offline uploads running? check upload history
```

### 4.2 CPA up 30%+ for 7+ days
```
Check change history: bids, targets, budgets, imports, auto-applied recommendations
  change found -> revert or wait out learning (7 to 14 days) if intentional
Check network segment: partner or audience share up?
  yes -> publisher report, exclude, consider partners off experiment
Check search terms: new irrelevant clusters (broad match or AI Max expansion)?
  yes -> negatives, term exclusions
Check auction insights: new competitor or higher overlap and outranking rate?
  yes -> evaluate bid response vs margin; hand market change to market-intel
Check landing page: speed, errors, form broken, out of stock?
  yes -> fix, hand off to cro
Check CVR by device and time: mobile CVR collapse?
  yes -> device bid adjustment or page fix
```

### 4.3 Clicks or impressions down 25%+
```
Budget exhausted earlier in day? -> IS lost to budget; raise budget if profitable
Disapprovals or asset rejections? -> fix or appeal; bulk edit tool for disapproved assets
Target tightened recently? -> revert in steps
Seasonality or market demand? -> compare to Google and to last year; check Bing search volume
Feed (Shopping, PMax)? -> Merchant Center diagnostics, Product explorer
Billing problem? -> prepay balance, payment failure
Import overwrote settings? -> import history
```

### 4.4 CTR dropped
- Ad position or IS lost to rank up: check quality score components.
- New competitor ads: auction insights.
- Asset disapprovals reduced extensions: asset report.
- Query mix shift (broad, AI Max): search terms.

### 4.5 PMax spend shift
- Search insights and landing page report show non commercial URLs or brand: add URL exclusions, brand exclusions, negatives.
- Audience placements grew: check Ad Preview Hub renders, asset quality; test signals.
- Products: one hero product took the budget; split by custom label.

## 5. Experiments

Status: optimization experiments generally available for Search, Shopping, Audience and PMax since 2026-09, with a side by side results page and the option to apply the winning variant to the original campaign or create a new one [Official, 2026-09]. PMax uplift experiments (incrementality) generally available from 2026-09 [Official, 2026-08].

Design standard:
| Element | Standard |
|---------|----------|
| Hypothesis | If we <change>, then <metric> will <move> because <reason> |
| Split | 50/50 traffic split unless budget is tiny |
| Duration | At least 4 weeks, or until each arm has 50+ conversions; include full weeks |
| Primary metric | CPA or ROAS on the primary goal; for lead gen, qualified stage |
| Guardrails | Spend, IS, brand share |
| Stop rule | Stop early if the test arm CPA is 50%+ worse after 2x target CPA spend with zero to 1 conversions |
| Decision rule | Apply if the primary metric improves and the platform shows significance, or the improvement holds 2 consecutive weeks with no guardrail breach |

Backlog of high value Microsoft tests:
1. AI Max on vs off on top non-brand campaigns.
2. Partners on vs off for non-brand.
3. LinkedIn job function bid adjustments vs none (manual or Enhanced CPC campaigns).
4. tCPA vs Maximize conversions without target at 30 to 60 conversions per month.
5. PMax NCA "bid higher" vs off.
6. PMax vs Standard Shopping on a product split.
7. Data-driven attribution vs last click on the primary goal (measurement owned).
8. Multimedia ads added vs RSA only.
Log each in `ads-master/EXPERIMENTS.md` before launch.

## 6. Recommendations and auto-apply
- Optimization score was retired starting 2025-04-08 [Official, 2025-04]; recommendations still exist.
- Review recommendations weekly; accept only those consistent with the strategy; never enable auto-apply without approval.
- Common recommendations to reject by default: broad match expansion without conversion bidding, budget increases without marginal CPA evidence, removing negatives.

## 7. Reporting set (build once, schedule)
Use the custom report builder (2025-06) to save and schedule [Official, 2025-06]:
| Report | Dimensions | Metrics | Schedule |
|--------|-----------|---------|----------|
| Weekly performance | Campaign, week | Spend, clicks, conversions, CPA, ROAS, IS, lost IS | Weekly |
| Search terms | Search term, keyword, campaign | Spend, conversions | Weekly |
| Publisher | Website URL, campaign | Spend, conversions | Every 2 weeks |
| Network split | Ad distribution, campaign | Spend, conversions | Weekly |
| Demographics | Age, gender, campaign | Spend, conversions | Monthly |
| LinkedIn profile | Company, industry, job function | Spend, conversions | Monthly |
| PMax landing pages | Final URL | Spend, conversions | Weekly |
Custom columns now support conversion metrics such as lifetime value and average order value [Official, 2026-06].
