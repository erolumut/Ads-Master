# Marketplace Unit Economics

> Knowledge as of 2026-10. Fees in examples are illustrative inputs, not rate cards. Read every fee from the account (rate card, fee preview, settlement report) and write the source and date next to each line. Company level economics (MER, payback, budget) belong to `growth-orchestrator`; price corridor decisions to `pricing-strategy`.

## 1. Cost stack per unit (all marketplaces)

| Line | Amazon | bol | Trendyol, Hepsiburada | Notes |
|------|--------|-----|-----------------------|-------|
| Gross price incl. VAT | Yes | Yes | Yes | EU, TR and Gulf prices include VAT; US prices exclude sales tax |
| VAT | 19% DE, 21% NL, 20% FR and UK, 20% TR (standard rates; reduced rates by category) | 21% NL, 21% BE | 20% standard (lower for some categories) | Use the rate per SKU and country |
| Referral or commission | % of gross price, minimum fee per item, category tiers | Fixed per item + % of price incl. VAT | % by category; base contested (VAT incl. vs excl.) | Read the account |
| VAT on fees | Charged on fees in many EU setups (reverse charge for B2B in other member states) | Yes | VAT added on commission | Recoverable if VAT registered; cash flow effect |
| Fulfillment | FBA by size and weight tier; Low-Price FBA under price thresholds | LVB by size class | Cargo by desi (TEX, HepsiJET); barem rules on low baskets | Includes pick, pack, carrier |
| Storage | Monthly per cubic foot or meter; peak Oct to Dec; aged surcharges | LVB storage | Platform warehouse if used | Allocate per unit by days in stock |
| Inbound | Inbound placement fee, inbound defects, prep (US: seller prep from 2026-01-01) | Inbound fees, booking fees | Transport to warehouse | |
| Returns | Refund admin fee, returns processing fee (some categories), unsellables | Return handling | Return cargo (seller pays), commission refunded on Hepsiburada | Use real return rate per SKU |
| Advertising | Sponsored ads, DSP | Sponsored Products, display | Product ads, store ads | Per unit = ad spend / units sold (TACoS view) |
| Promotions | Coupons (fee plus discount), deals (deal fee), Prime exclusive discounts, Subscribe and Save | Campaign discounts | Campaign discounts, platform funded vs seller funded | Count discount and fees |
| Program fees | Subscription, Vine, Brand Registry tools (free), FBA low inventory fee | Partner fees | Service fee per order | |
| Payment, withholding, taxes | Included in referral on Amazon | Included | 1% e-commerce withholding (TR) on payouts | Withholding is a tax prepayment, not a cost if offset; treat as cash flow |
| Currency | Conversion fees if paid out in another currency | | TRY inflation | |
| Duties and cross-border | US de minimis suspended for all countries from 2025-08-29; EU temporary EUR 3 duty per item type on low value parcels from 2026-07-01 (mainly non-EU sellers) | | | [Official, 2025 to 2026, per offer-strategy research] |

## 2. Formulas

```
Net price (NP) = gross price / (1 + VAT rate)                         (EU, TR, Gulf)
CM1 = NP - landed product cost (incl. freight in, duties)
CM2_mp (before ads) = CM1 - referral - fulfillment - storage per unit - inbound per unit - returns cost per unit - other per unit fees - promo cost per unit
CM3_mp (after ads) = CM2_mp - ad spend per unit
Breakeven ACoS = CM2_mp / NP           (on net basis; convert for gross reporting)
Returns cost per unit = return rate x (refund admin + return shipping + processing + unsellable share x landed cost)
Storage per unit = monthly storage fee per unit volume x unit volume x average months in stock
Monthly marketplace contribution = sum over SKUs (CM3_mp x units) - fixed marketplace costs (subscriptions, tools, agency, staff share)
```

## 3. Worked example A: Amazon US FBA [Illustrative]

| Line | USD |
|------|-----|
| Price (sales tax excluded) | 24.99 |
| Landed cost | 6.00 |
| Referral 15% | 3.75 |
| FBA fulfillment (standard small to large; illustrative) | 4.20 |
| Storage per unit (1.5 months off-peak, 0.1 cubic feet) | 0.12 |
| Inbound placement and prep per unit | 0.35 |
| Returns (4% x USD 9 cost per return) | 0.36 |
| CM2_mp | 10.21 |
| Breakeven ACoS | 40.9% |
| TACoS 12% (USD 3.00 per unit) -> CM3_mp | 7.21 (28.9% of price) |

## 4. Worked example B: bol with LVB [Illustrative]

| Line | EUR |
|------|-----|
| Price incl. 21% VAT | 24.95 |
| NP | 20.62 |
| Landed cost | 6.20 |
| Commission: fixed 0.83 + 13% of 24.95 (illustrative category) | 4.07 |
| LVB fee (size class S, illustrative) | 3.10 |
| Storage and inbound per unit | 0.30 |
| Returns (3% x EUR 6) | 0.18 |
| CM2_mp | 6.77 |
| Breakeven ACoS (net basis) | 32.8% |
| Breakeven ACoS on gross reporting basis | 27.1% |

## 5. Worked example C: Trendyol with TEX [Illustrative, TRY]

| Line | TRY |
|------|-----|
| Price incl. 20% VAT | 899.00 |
| NP | 749.17 |
| Landed cost | 260.00 |
| Commission 21% on NP (if VAT-exclusive base; if VAT-inclusive base use 899) | 157.33 (or 188.79) |
| Cargo 3 desi TEX (about TRY 100.20 plus VAT per a 2026-09 list; VAT recoverable) | 100.20 |
| Service fee per order (illustrative) | 10.00 |
| Returns (10% x (cargo both ways 200 + handling 20)) | 22.00 |
| CM2_mp (VAT-exclusive base) | 199.64 |
| Breakeven ACoS (net) | 26.6% |

Sensitivity: the commission base question alone moves CM2 by about TRY 31 per unit (4 points of NP) in this example. Resolve it from the panel's agreement screen before setting targets.

## 6. Inflation and currency (Turkey and others)

- Refresh landed cost, cargo and fees monthly; Turkish cargo tariffs and commissions change several times per year [Secondary, 2026].
- Compare periods in real terms: deflate TRY by monthly CPI, or compare in a hard currency at the period's average rate, and say which.
- Price increases are needed to hold real margins; check the 10 day prior price rule for any later discount (since 2026-08-01) and the price tag 10 day rule (since 2025-10-11) [Official, via secondary].
- Hepsiburada reports both IAS 29 restated and unadjusted figures; FY2025 GMV growth was 4.3% restated vs 41% unadjusted [Official, 2026-02]. Never compare restated and unadjusted numbers.

## 7. Comparing marketplaces and DTC

| Metric | Formula | Use |
|--------|---------|-----|
| Take rate | (referral + fulfillment + other platform fees) / gross price | Compare platform cost |
| Contribution per unit by channel | CM3 per channel incl. DTC (DTC: payment fees, shipping, returns, acquisition investment) | Channel mix |
| Contribution per customer (DTC only) | First order plus repeat contribution | Marketplace has no customer data for CRM; use repeat estimates from Brand Analytics Repeat Purchase |
| Cash conversion | Days from inventory purchase to payout | Marketplaces pay every 2 weeks (Amazon), on schedule (bol), on contract terms (TR) |

DTC acquisition investment (media plus shipping subsidy plus bonus product cost plus incremental discount cost) vs marketplace TACoS is not apples to apples: marketplace sales include organic demand captured. Use incrementality tests for channel decisions ([Measurement](measurement-and-halo.md)).

## 8. Calculator (Python, standard library)

```python
#!/usr/bin/env python3
"""Marketplace unit economics. Usage: python3 mp_economics.py inputs.csv > output.csv
inputs.csv columns: sku,marketplace,gross_price,vat_rate,landed_cost,referral_pct,referral_on_gross(1/0),
fixed_fee,fulfillment,storage_unit,inbound_unit,return_rate,return_cost,promo_unit,tacos
All fees per unit in the marketplace currency. Every input must have a source in the run notes."""
import csv, sys

def row_calc(r):
    g = float(r["gross_price"]); vat = float(r["vat_rate"])
    npx = g / (1 + vat)
    base = g if r["referral_on_gross"] == "1" else npx
    referral = float(r["referral_pct"]) * base + float(r["fixed_fee"])
    returns = float(r["return_rate"]) * float(r["return_cost"])
    cm2 = (npx - float(r["landed_cost"]) - referral - float(r["fulfillment"])
           - float(r["storage_unit"]) - float(r["inbound_unit"]) - returns - float(r["promo_unit"]))
    ads = float(r["tacos"]) * g
    cm3 = cm2 - ads
    return {"sku": r["sku"], "marketplace": r["marketplace"], "net_price": round(npx, 2),
            "referral": round(referral, 2), "cm2": round(cm2, 2),
            "breakeven_acos_net": round(cm2 / npx, 4) if npx else "",
            "breakeven_acos_gross": round(cm2 / g, 4) if g else "",
            "cm3": round(cm3, 2), "cm3_pct_net": round(cm3 / npx, 4) if npx else ""}

reader = csv.DictReader(open(sys.argv[1], newline="", encoding="utf-8"))
out = [row_calc(r) for r in reader]
w = csv.DictWriter(sys.stdout, fieldnames=list(out[0].keys()))
w.writeheader(); w.writerows(out)
```

Note on ads in the calculator: TACoS is applied to gross sales because most consoles report sales incl. VAT in VAT markets. Keep this consistent with the targets.

## 9. Fee change protocol

1. When a marketplace announces a fee change (Amazon US yearly effective mid January; Amazon EU 2026 cuts from 2026-01-05; noon storage 2026-10-01; bol LVB small sizes 2026-09-09; eBay currency conversion 2026-10-14; Etsy regulatory operating fee 2026-06-22), recompute CM2 and breakeven ACoS for all SKUs.
2. Flag SKUs where CM3 turns negative or breakeven ACoS falls below current ACoS.
3. Propose actions: price change (via `pricing-strategy`), fulfillment change, bundle or pack size change, ad target change, delisting (decision only).
4. Write a journal entry with old and new fee, source, date and impact per month.
