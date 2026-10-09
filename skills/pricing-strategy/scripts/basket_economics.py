#!/usr/bin/env python3
"""Basket economics: contribution per order by basket size, minimum viable basket
and free delivery threshold check. Standard library only.

Usage:
  python3 basket_economics.py --demo                 # illustrative inputs, labeled as such
  python3 basket_economics.py --config inputs.json   # your own inputs
  python3 basket_economics.py --config inputs.json --csv out.csv
  python3 basket_economics.py --print-template       # empty input template

All money inputs are in one currency. Prices the customer pays are entered
INCLUDING VAT (as shown on the shelf or site); every cost is entered EXCLUDING VAT.
The script removes VAT from revenue, so contribution is a VAT-free figure.

Definitions (match the pricing-strategy cost-to-serve reference):
  net product revenue   = basket price incl VAT / (1 + vat_rate)
  net shipping revenue  = shipping charged incl VAT / (1 + shipping_vat_rate)
  CM1 (gross margin)    = net product revenue - COGS (landed, per unit x units)
  CM2 (contribution)    = CM1 + net shipping revenue - packaging - pick and pack
                          - carrier - payment fees - channel fees - returns allowance
  CM2 % of net revenue  = CM2 / (net product revenue + net shipping revenue)
  Minimum viable basket = smallest basket whose CM2 >= contribution floor
                          (floor = max(floor_amount, floor_pct x net revenue))
Payment fees are charged on the gross amount the customer pays (incl VAT and shipping).
"""
import argparse
import csv
import json
import sys

TEMPLATE = {
    "_note": "Prices incl VAT; costs excl VAT. null = missing (run reports INCOMPLETE). Write 0 only when the cost is truly zero.",
    "cost_as_of": None,
    "currency": "EUR",
    "vat_rate": 0.09,
    "shipping_vat_rate": 0.09,
    "unit_name": "bar",
    "unit_weight_kg": 0.06,
    "cogs_per_unit": None,
    "packaging_per_order": None,
    "packaging_per_unit": 0.0,
    "pick_pack_per_order": None,
    "pick_pack_per_unit": 0.0,
    "carrier_bands": [
        {"max_kg": 2.0, "cost": 0.0, "label": "letterbox parcel"},
        {"max_kg": 10.0, "cost": 0.0, "label": "parcel 0 to 10 kg"},
        {"max_kg": 23.0, "cost": 0.0, "label": "parcel 10 to 23 kg"},
    ],
    "carrier_surcharge_pct": 0.0,
    "order_tare_kg": 0.15,
    "payment_fee_pct": None,
    "payment_fee_fixed": None,
    "channel_fee_pct": 0.0,
    "channel_fee_fixed": 0.0,
    "returns_allowance_pct": None,
    "shipping_charged_incl_vat": None,
    "free_shipping_threshold_incl_vat": None,
    "contribution_floor_amount": 0.0,
    "contribution_floor_pct": 0.0,
    "baskets": [
        {"name": "Single", "units": 1, "price_incl_vat": 0.0},
    ],
    "unit_price_incl_vat": None,
    "scan_units": [1, 2, 3, 4, 6, 8, 12, 16, 24, 36, 48, 72, 96],
    "threshold_candidates_incl_vat": [],
    "retail": {
        "shelf_price_incl_vat": None,
        "retailer_margin_pct": None,
        "trade_spend_pct_of_sell_in": 0.0,
        "logistics_per_unit": 0.0,
    },
}

# Illustrative only. Not sourced. Shaped like a Dutch DTC snack bar brand so the
# method can be shown end to end. Replace every value before any decision.
DEMO = {
    "_note": "ILLUSTRATIVE DEMO INPUTS. Not real data for any brand.",
    "cost_as_of": "illustrative",
    "currency": "EUR",
    "vat_rate": 0.09,
    "shipping_vat_rate": 0.09,
    "unit_name": "bar",
    "unit_weight_kg": 0.06,
    "cogs_per_unit": 0.85,
    "packaging_per_order": 0.60,
    "packaging_per_unit": 0.0,
    "pick_pack_per_order": 1.50,
    "pick_pack_per_unit": 0.02,
    "carrier_bands": [
        {"max_units": 6, "cost": 4.55, "label": "letterbox parcel (fits 6 bars)"},
        {"max_units": 96, "cost": 7.00, "label": "parcel up to 10 kg"},
        {"max_units": 192, "cost": 7.40, "label": "parcel 10 to 23 kg"},
    ],
    "carrier_surcharge_pct": 0.0,
    "order_tare_kg": 0.15,
    "payment_fee_pct": 0.006,
    "payment_fee_fixed": 0.27,
    "channel_fee_pct": 0.0,
    "channel_fee_fixed": 0.0,
    "returns_allowance_pct": 0.01,
    "shipping_charged_incl_vat": 4.95,
    "free_shipping_threshold_incl_vat": 50.0,
    "contribution_floor_amount": 8.00,
    "contribution_floor_pct": 0.20,
    "baskets": [
        {"name": "Trial 12", "units": 12, "price_incl_vat": 32.95},
        {"name": "Entry 24", "units": 24, "price_incl_vat": 59.95},
        {"name": "Hero 48", "units": 48, "price_incl_vat": 109.95},
        {"name": "Stock up 96", "units": 96, "price_incl_vat": 199.95},
    ],
    "unit_price_incl_vat": 2.79,
    "scan_units": [1, 2, 3, 4, 6, 8, 10, 12, 16, 18, 20, 24],
    "threshold_candidates_incl_vat": [30.0, 40.0, 50.0, 60.0, 75.0],
    "retail": {
        "shelf_price_incl_vat": 2.99,
        "retailer_margin_pct": 0.30,
        "trade_spend_pct_of_sell_in": 0.10,
        "logistics_per_unit": 0.08,
    },
}


REQUIRED = ["vat_rate", "cogs_per_unit", "packaging_per_order", "pick_pack_per_order",
            "carrier_bands", "payment_fee_pct", "payment_fee_fixed", "returns_allowance_pct",
            "shipping_charged_incl_vat", "cost_as_of"]


def missing_inputs(cfg):
    """Incomplete, not zero: a missing or null required input is reported, never replaced by 0."""
    miss = [k for k in REQUIRED if cfg.get(k) is None or cfg.get(k) == []]
    for i, b in enumerate(cfg.get("baskets") or []):
        if b.get("price_incl_vat") in (None, 0, 0.0):
            miss.append(f"baskets[{i}].price_incl_vat")
    return miss


def carrier_cost(cfg, units):
    """Carrier cost for the order. Bands use max_units (size driven, for example a
    letterbox parcel that fits N units) or max_kg (weight driven). First match wins."""
    kg = units * cfg.get("unit_weight_kg", 0.0) + cfg.get("order_tare_kg", 0.0)
    bands = cfg["carrier_bands"]
    base = None
    for band in bands:
        if "max_units" in band and units <= band["max_units"]:
            base = band["cost"]
            break
        if "max_kg" in band and "max_units" not in band and kg <= band["max_kg"]:
            base = band["cost"]
            break
    if base is None:
        # Larger than the last band: split into parcels of the last band.
        last = bands[-1]
        if "max_units" in last:
            parcels = int(-(-units // last["max_units"]))
        else:
            parcels = int(-(-kg // last["max_kg"]))
        base = parcels * last["cost"]
    return base * (1 + cfg.get("carrier_surcharge_pct", 0.0)), kg


def shipping_charged(cfg, price_incl_vat, force_free=None):
    """Shipping the customer pays, incl VAT. force_free overrides the policy."""
    if force_free is True:
        return 0.0
    threshold = cfg.get("free_shipping_threshold_incl_vat")
    if force_free is None and threshold is not None and price_incl_vat >= threshold:
        return 0.0
    return cfg.get("shipping_charged_incl_vat", 0.0)


def basket_row(cfg, name, units, price_incl_vat, force_free=None):
    vat = cfg["vat_rate"]
    svat = cfg.get("shipping_vat_rate", vat)
    ship_gross = shipping_charged(cfg, price_incl_vat, force_free)
    net_product = price_incl_vat / (1 + vat)
    net_ship = ship_gross / (1 + svat)
    net_revenue = net_product + net_ship
    cogs = cfg["cogs_per_unit"] * units
    packaging = cfg.get("packaging_per_order", 0.0) + cfg.get("packaging_per_unit", 0.0) * units
    pick = cfg.get("pick_pack_per_order", 0.0) + cfg.get("pick_pack_per_unit", 0.0) * units
    carrier, kg = carrier_cost(cfg, units)
    paid_gross = price_incl_vat + ship_gross
    payment = paid_gross * cfg.get("payment_fee_pct", 0.0) + cfg.get("payment_fee_fixed", 0.0)
    channel = net_product * cfg.get("channel_fee_pct", 0.0) + cfg.get("channel_fee_fixed", 0.0)
    returns = net_product * cfg.get("returns_allowance_pct", 0.0)
    cm1 = net_product - cogs
    cm2 = cm1 + net_ship - packaging - pick - carrier - payment - channel - returns
    floor = max(cfg.get("contribution_floor_amount", 0.0),
                cfg.get("contribution_floor_pct", 0.0) * net_revenue)
    return {
        "basket": name,
        "units": units,
        "price_incl_vat": round(price_incl_vat, 2),
        "price_per_unit_incl_vat": round(price_incl_vat / units, 3) if units else 0.0,
        "shipping_charged_incl_vat": round(ship_gross, 2),
        "net_revenue": round(net_revenue, 2),
        "cogs": round(cogs, 2),
        "cm1": round(cm1, 2),
        "packaging": round(packaging, 2),
        "pick_pack": round(pick, 2),
        "weight_kg": round(kg, 2),
        "carrier": round(carrier, 2),
        "payment": round(payment, 2),
        "channel_fee": round(channel, 2),
        "returns": round(returns, 2),
        "cm2": round(cm2, 2),
        "cm2_pct": round(cm2 / net_revenue, 3) if net_revenue else 0.0,
        "cm2_per_unit": round(cm2 / units, 3) if units else 0.0,
        "floor": round(floor, 2),
        "clears_floor": cm2 >= floor,
    }


def print_table(rows, cols, title):
    print(f"\n## {title}\n")
    print("| " + " | ".join(cols) + " |")
    print("|" + "|".join("---" for _ in cols) + "|")
    for r in rows:
        cells = []
        for c in cols:
            v = r[c]
            if isinstance(v, bool):
                v = "yes" if v else "no"
            elif isinstance(v, float) and c.endswith("pct"):
                v = f"{v * 100:.1f}%"
            elif isinstance(v, float):
                v = f"{v:.2f}"
            cells.append(str(v))
        print("| " + " | ".join(cells) + " |")


def run(cfg, csv_path=None):
    cur = cfg.get("currency", "")
    unit = cfg.get("unit_name", "unit")
    print(f"# Basket economics ({cur}, prices incl VAT, costs and contribution excl VAT)")
    if cfg.get("_note"):
        print(f"\nNote: {cfg['_note']}")
    miss = missing_inputs(cfg)
    if miss:
        print("\nStatus: INCOMPLETE. Missing inputs (not computed as zero): " + ", ".join(miss))
        return 3
    print(f"\nStatus: COMPLETE. Costs as of {cfg['cost_as_of']}. Percentages are margin_on_price (CM2 / net revenue).")

    main_cols = ["basket", "units", "price_incl_vat", "price_per_unit_incl_vat",
                 "shipping_charged_incl_vat", "net_revenue", "cogs", "cm1", "packaging",
                 "pick_pack", "carrier", "payment", "returns", "cm2", "cm2_pct",
                 "cm2_per_unit", "clears_floor"]

    ladder = [basket_row(cfg, b["name"], b["units"], b["price_incl_vat"])
              for b in cfg.get("baskets", [])]
    if ladder:
        print_table(ladder, main_cols, "1. Price ladder under the current delivery policy")
        print("\nLadder check (each rung should earn more CM2 per order than the rung below,"
              " and the per unit price should fall):")
        for lo, hi in zip(ladder, ladder[1:]):
            ok_cm = hi["cm2"] > lo["cm2"]
            ok_ppu = hi["price_per_unit_incl_vat"] < lo["price_per_unit_incl_vat"]
            step = (1 - hi["price_per_unit_incl_vat"] / lo["price_per_unit_incl_vat"]) * 100
            print(f"- {lo['basket']} -> {hi['basket']}: CM2 {lo['cm2']:.2f} -> {hi['cm2']:.2f} "
                  f"({'ok' if ok_cm else 'FAIL'}), per {unit} price step {step:.1f}% "
                  f"({'ok' if ok_ppu else 'FAIL'})")

    scan = []
    p = cfg.get("unit_price_incl_vat")
    if p:
        scan = [basket_row(cfg, f"{n} x {unit}", n, n * p) for n in cfg.get("scan_units", [])]
        print_table(scan, ["basket", "units", "price_incl_vat", "shipping_charged_incl_vat",
                           "net_revenue", "carrier", "cm2", "cm2_pct", "floor", "clears_floor"],
                    f"2. Single {unit} price {p:.2f} x basket size (current delivery policy)")
        paid = [r for r in scan if r["clears_floor"]]
        print("\nMinimum viable basket (current policy): "
              + (f"{paid[0]['units']} {unit}s, {cur} {paid[0]['price_incl_vat']:.2f} incl VAT"
                 if paid else "none of the scanned sizes clears the floor"))
        free = [basket_row(cfg, f"{n} x {unit}", n, n * p, force_free=True)
                for n in cfg.get("scan_units", [])]
        free_ok = [r for r in free if r["clears_floor"]]
        print("Minimum viable basket if delivery is free: "
              + (f"{free_ok[0]['units']} {unit}s, {cur} {free_ok[0]['price_incl_vat']:.2f} incl VAT"
                 if free_ok else "none of the scanned sizes clears the floor"))

    cands = cfg.get("threshold_candidates_incl_vat") or []
    if cands and p:
        print(f"\n## 3. Free delivery threshold candidates (single {unit} price {p:.2f})\n")
        print("| threshold incl VAT | units needed | basket incl VAT | CM2 at threshold (free) "
              "| CM2 % | clears floor | CM2 same basket if shipping charged |")
        print("|---|---|---|---|---|---|---|")
        for t in cands:
            n = int(-(-t // p))
            free_row = basket_row(cfg, "t", n, n * p, force_free=True)
            paid_row = basket_row(cfg, "t", n, n * p, force_free=False)
            print(f"| {t:.2f} | {n} | {n * p:.2f} | {free_row['cm2']:.2f} | "
                  f"{free_row['cm2_pct'] * 100:.1f}% | {'yes' if free_row['clears_floor'] else 'no'} | "
                  f"{paid_row['cm2']:.2f} |")
        print("\nRead: the lowest candidate whose free delivery basket clears the floor is the"
              " economic minimum for the threshold. Set the commercial threshold at or above it,"
              " near the competitor reference and 15 to 30% above current AOV (heuristic, test it).")

    retail = cfg.get("retail") or {}
    if retail.get("shelf_price_incl_vat") and retail.get("retailer_margin_pct") is not None:
        shelf = retail["shelf_price_incl_vat"]
        shelf_ex = shelf / (1 + cfg["vat_rate"])
        sell_in = shelf_ex * (1 - retail["retailer_margin_pct"])
        net_sell_in = sell_in * (1 - retail.get("trade_spend_pct_of_sell_in", 0.0))
        brand_cm = net_sell_in - cfg["cogs_per_unit"] - retail.get("logistics_per_unit", 0.0)
        print(f"\n## 4. Retail channel per {unit} vs DTC ladder\n")
        print(f"- Shelf price incl VAT {shelf:.2f}, ex VAT {shelf_ex:.2f}; retailer margin "
              f"{retail['retailer_margin_pct'] * 100:.0f}% of shelf ex VAT; implied sell-in {sell_in:.2f}; "
              f"after trade spend {net_sell_in:.2f}; brand CM per {unit} in retail {brand_cm:.2f}")
        if ladder:
            print("\n| DTC basket | per unit incl VAT | gap vs shelf | DTC CM2 per unit | vs retail CM per unit |")
            print("|---|---|---|---|---|")
            for r in ladder:
                gap = (r["price_per_unit_incl_vat"] / shelf - 1) * 100
                print(f"| {r['basket']} | {r['price_per_unit_incl_vat']:.2f} | {gap:+.1f}% | "
                      f"{r['cm2_per_unit']:.2f} | {r['cm2_per_unit'] - brand_cm:+.2f} |")
            print("\nRead: a DTC per unit price far below shelf invites channel conflict; a DTC CM per unit"
                  " below retail CM per unit means DTC volume is worth less than retail volume.")

    if csv_path:
        rows = ladder + scan
        if rows:
            with open(csv_path, "w", newline="", encoding="utf-8") as fh:
                w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
                w.writeheader()
                w.writerows(rows)
            print(f"\nCSV written: {csv_path}")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", help="JSON file with inputs (see --print-template)")
    ap.add_argument("--demo", action="store_true", help="run with illustrative demo inputs")
    ap.add_argument("--csv", help="write ladder and scan rows to this CSV path")
    ap.add_argument("--print-template", action="store_true", help="print an input template")
    args = ap.parse_args()
    if args.print_template:
        print(json.dumps(TEMPLATE, indent=2))
        return 0
    if args.demo:
        cfg = DEMO
    elif args.config:
        with open(args.config, encoding="utf-8") as fh:
            cfg = json.load(fh)
    else:
        ap.print_help()
        return 2
    return run(cfg, args.csv)


if __name__ == "__main__":
    sys.exit(main())
