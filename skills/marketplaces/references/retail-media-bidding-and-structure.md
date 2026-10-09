# Retail Media Bidding and Structure (all marketplaces)

> Knowledge as of 2026-10. The method works on Amazon Ads, bol Sponsored Products, Trendyol and Hepsiburada product ads, Allegro Ads, Walmart Connect, noon Ads and eBay Promoted Listings Priority. Product specific settings: [Amazon Ads](amazon-ads.md), [bol](bol-com.md), [Turkey](trendyol-and-hepsiburada.md), [Other marketplaces](other-marketplaces.md).

## 1. Economics first

```
Contribution before ads per unit (CM2_mp) = net price (ex VAT) - product cost - referral or commission - fulfillment - storage per unit - returns cost per unit - payment and other fees
Breakeven ACoS = CM2_mp / net price            (the ACoS at which ads earn zero contribution)
Target ACoS (profit) = Breakeven ACoS - required margin after ads
TACoS = total ad spend / total marketplace sales (ad + organic)
Max CPC = AOV x CVR x target ACoS              (AOV = average order value from ads; CVR = orders / clicks)
```

Worked example (amazon.de, single SKU) [Illustrative numbers, not benchmarks]:

| Line | EUR |
|------|-----|
| Price incl. VAT | 29.99 |
| Net price ex VAT (19%) | 25.20 |
| Product landed cost | 6.50 |
| Referral fee (15% of gross price incl. VAT) | 4.50 |
| FBA fulfillment | 3.60 |
| Storage and inbound per unit | 0.40 |
| Returns cost per unit (5% return rate x EUR 8 cost per return) | 0.40 |
| CM2_mp | 9.80 |
| Breakeven ACoS = 9.80 / 25.20 | 38.9% |
| Required margin after ads 15% -> target ACoS | 23.9% |
| Ads AOV EUR 25.20 net, CVR 12% -> max CPC = 25.20 x 0.12 x 0.239 | EUR 0.72 |

Note: Amazon reports ACoS on gross sales including VAT in EU stores. Convert targets to the same basis (ACoS on gross = ACoS on net / 1.19 for 19% VAT) or compute from gross consistently. Mixing bases is a common error.

## 2. Targets by intent

| Intent | What | Target logic | Typical role |
|--------|------|--------------|--------------|
| Brand defense | Own brand terms, own ASIN targeting | Low ACoS (often well under breakeven); goal is impression share and blocking | Protect |
| Category core | Generic high relevance terms | At or below target ACoS | Profit and rank |
| Category growth | Broader and long tail terms | Up to breakeven; NTB goal | Reach |
| Competitor conquest | Competitor ASINs and brand terms where allowed | Up to breakeven plus NTB requirement | Share |
| Discovery | Auto and broad | Below breakeven after harvest; low bids | Learning |
| Launch | New ASINs | Above breakeven within a written launch budget and TACoS glidepath | Rank and reviews |

Set targets per product group because margins differ. A single account ACoS target is a mistake.

## 3. TACoS as the control metric

- TACoS links ads to the whole marketplace P and L. Healthy TACoS depends on margin and lifecycle; vendor rule of thumb 10% to 15% for mature brands is not a target [Secondary, 2026; Unverified].
- Diagnose with the 2 x 2:

| Ad sales | Organic sales | Meaning | Action |
|----------|---------------|---------|--------|
| Up | Up | Ads build rank and halo | Keep scaling while CM3 allows |
| Up | Down | Ads cannibalize organic | Cut brand and high organic rank terms; test pauses |
| Down | Up | Organic strength | Hold or reduce ads |
| Down | Down | Demand, price, stock, featured offer or listing issue | Diagnose outside ads first |

## 4. Bid management

### 4.1 Rule set (weekly; 14 to 30 day lookback; minimum data)

| Condition (per target or keyword) | Action |
|-----------------------------------|--------|
| Orders 2 or more and ACoS under target by 20% or more | Raise bid 10% to 20% (if impression share is not already high) |
| Orders 2 or more and ACoS above target by 20% or more | Lower bid toward Max CPC formula |
| Clicks 15 or more and no order, or spend 1.5x target CPA and no order | Lower bid 30% or pause; negate in discovery if irrelevant |
| Impressions low, bid below suggested range | Raise to the low end of suggested range once |
| ASIN out of stock, no featured offer or buybox, under 3.5 stars | Pause ads on the ASIN |
| Event days (Prime Day, 11.11, Black Friday) | Pre-raise budgets, not bids; CPCs rise; CVR also rises; review twice daily |

Adjust by at most 20% per change on proven targets, and do not change the same target more than once every 3 to 7 days (learning and attribution lag: Amazon reports conversions up to 7 to 14 days after the click).

### 4.2 Formula bid
```
New bid = current CPC x (target ACoS / actual ACoS), capped at +-25% per change
```

### 4.3 Placements
Read placement reports (top of search, rest of search, product pages). Raise top of search modifiers only where CVR there is at least 1.3x rest of search [Practitioner consensus].

## 5. Keyword harvesting and negatives

| Step | Rule |
|------|------|
| Harvest | From auto, broad and phrase search term reports: terms with 2 or more orders (or CVR above ad group average with 20 or more clicks) become exact match targets in a performance campaign |
| Isolation | Add the harvested term as negative exact in the source campaign |
| Negate | Irrelevant terms immediately; relevant non-converting terms after 1.5x target CPA spend |
| ASIN harvest | Converting ASINs from auto into product targeting campaigns |
| N-gram review | Monthly: group search terms by 1, 2, 3 word n-grams to find wasted spend patterns (for example "free", "used", "kids" for an adult product) |

N-gram script (search term report CSV with columns: search_term, clicks, spend, orders, sales):

```python
import csv, sys
from collections import defaultdict
agg = defaultdict(lambda: [0, 0.0, 0, 0.0])  # clicks, spend, orders, sales
with open(sys.argv[1], newline="", encoding="utf-8") as fh:
    for row in csv.DictReader(fh):
        words = row["search_term"].lower().split()
        grams = set()
        for n in (1, 2, 3):
            grams.update(" ".join(words[i:i + n]) for i in range(len(words) - n + 1))
        for g in grams:
            a = agg[g]
            a[0] += int(row["clicks"] or 0); a[1] += float(row["spend"] or 0)
            a[2] += int(row["orders"] or 0); a[3] += float(row["sales"] or 0)
rows = [(g, *v, (v[1] / v[3]) if v[3] else None) for g, v in agg.items() if v[1] > 0]
rows.sort(key=lambda r: r[2], reverse=True)
print("ngram,clicks,spend,orders,sales,acos")
for g, c, s, o, sa, acos in rows[:200]:
    print(f'"{g}",{c},{s:.2f},{o},{sa:.2f},{"" if acos is None else f"{acos:.2%}"}')
```

Run it on files in `ads-master/data/imports/` only; output to the dated outputs folder.

## 6. Budget allocation

1. Budget follows contribution, not ACoS: rank campaigns by incremental contribution per extra euro (use bid and budget steps and observe marginal ACoS).
2. Never let a profitable exact campaign run out of budget before evening while discovery has budget left.
3. Keep 10% to 20% of budget for discovery and tests; 5% to 15% for brand defense depending on competitor pressure (validate with holdouts).
4. Portfolio or campaign group caps per product line to enforce the monthly plan in `STRATEGY.md`.
5. Daily budget changes are G3. Agents propose; humans approve.

## 7. Competitor conquest

- Target competitor ASINs where you win on price, rating, or features. Check their rating and price weekly; pull back when they improve.
- Bidding on competitor brand keywords is allowed on Amazon in most cases but ad copy must not imply affiliation; trademark complaints are possible in some jurisdictions. Prefer product targeting [Practitioner consensus].
- Track NTB share on conquest campaigns; conquest without NTB is just expensive.

## 8. Dayparting and seasonality

- Amazon offers budget rules and schedules; third-party tools offer hourly bids. Use dayparting only with at least 4 weeks of hourly data showing CVR differences of 30% or more [Practitioner consensus].
- Seasonality: raise budgets before demand peaks (rank building pays during the peak). Plan with last year's Search Query Performance volumes.

## 9. Weekly ads review template

```
# Weekly marketplace ads review | <marketplace> | Week <yyyy-ww> | Data: ads console and sales report, <dates>
Spend vs plan | Ad sales | Total sales | ACoS | TACoS | CM3 after ads | NTB %
By intent: brand, category core, growth, conquest, discovery, launch (spend, ACoS vs target, orders)
Top 10 changes proposed (target, current, proposed, reason, expected effect) -> change request
Harvest: n terms promoted, n negatives added
Stock and featured offer issues affecting ads
Tests running (EXPERIMENTS.md IDs)
Risks and incidents
Handoffs requested
```

## 10. Automation and tools

| Option | Use | Guardrail |
|--------|-----|-----------|
| Amazon native rules (rule based bidding, budget rules) | Simple bid toward ROAS goal; budget on events | Caps; logged as G3 automation approval |
| Amazon Ads Agent (beta) | Suggestions, pacing, AMC queries | Suggestions only; same approval gates |
| Third-party bid tools (Perpetua, Pacvue, Skai, Helium 10 Adtomic, Teikametrics and others) | Rule or algorithmic bidding across marketplaces | Review rule logic; cap changes; read logs weekly |
| Amazon Ads API and MCP server | Reports and controlled writes | Narrow operations; PAUSED creation; read back |

Never hand an algorithm an ACoS target without the breakeven calculation and a TACoS guardrail.
