#!/usr/bin/env python3
"""daily_report.py: unified daily fact table and daily report (Python 3 standard library only).

Joins platform spend exports with backend orders and writes:
  1. a daily fact table (CSV, one row per date, totals plus spend per channel), and
  2. a Markdown daily report for yesterday, the last 3 days and the last 7 days, with
     FACTS, INTERPRETATION and RECOMMENDATION kept apart, a confidence level and
     green, amber, red status derived from the project's target CPA.

Inputs
  --spend    one or more CSVs: date, channel, spend, impressions, clicks, conversions, conversion_value
  --orders   one CSV: date, order_id, revenue, is_new_customer, discount, shipping_charged,
             shipping_cost, product_cost, bonus_product_cost, refund, utm_source, bundle (or sku_group)

Example
  python3 daily_report.py --spend samples/meta_ads.csv samples/google_ads.csv \
      --orders samples/orders.csv --target-cpa 32 --currency EUR --brand "Example Socks Co." \
      --fact-table fact_daily.csv --out daily_report.md

Definitions follow skills/measurement/references/unified-metrics-and-daily-report.md. The project's
ads-master/METRICS.md wins where it differs; pass the matching flags.

Privacy: only aggregates are written. Order IDs are used for de-duplication and only ever printed
as salted SHA-256 prefixes. Columns that look like personal data (email, name, phone, address)
are ignored and reported as a warning.
"""
import argparse
import csv
import datetime as dt
import hashlib
import os
import sys
from collections import defaultdict

SPEND_COLS = ["date", "channel", "spend", "impressions", "clicks", "conversions", "conversion_value"]
ORDER_COLS = ["date", "order_id", "revenue", "is_new_customer", "discount", "shipping_charged", "shipping_cost",
              "product_cost", "bonus_product_cost", "refund", "utm_source"]
PII_EXACT = {"name", "first_name", "last_name", "full_name", "customer_name", "billing_name", "shipping_name", "telephone",
             "mobile", "address", "address1", "address2", "street", "city_street", "ip", "ip_address", "zip", "postal_code"}
DEFAULT_CHANNEL_MAP = {
    "facebook": "meta", "fb": "meta", "instagram": "meta", "ig": "meta", "meta": "meta", "an": "meta",
    "google": "google", "youtube": "google", "adwords": "google", "gads": "google",
    "bing": "microsoft", "microsoft": "microsoft", "msads": "microsoft",
    "tiktok": "tiktok", "linkedin": "linkedin", "pinterest": "pinterest", "snapchat": "snapchat",
    "reddit": "reddit", "chatgpt": "chatgpt", "openai": "chatgpt",
}
WINDOWS = [("Yesterday", 1), ("Last 3 days", 3), ("Last 7 days", 7)]
TRUE = {"1", "true", "yes", "y", "t", "new"}


def num(v):
    s = str(v or "").strip().replace(" ", "")
    if not s:
        return 0.0
    if "," in s and "." not in s:
        s = s.replace(",", ".")
    else:
        s = s.replace(",", "")
    try:
        return float(s)
    except ValueError:
        raise ValueError("not a number: %r" % v)


def parse_date(v):
    return dt.date.fromisoformat(str(v).strip()[:10])


def div(a, b):
    return a / b if b else None


def fmt_money(v, cur):
    if v is None:
        return "n/a"
    return ("%s %s" % (cur, "{:,.2f}".format(v))).strip()


def fmt_num(v, digits=0):
    if v is None:
        return "n/a"
    return "{:,.{d}f}".format(v, d=digits)


def fmt_pct(v, digits=1):
    return "n/a" if v is None else "{:.{d}f}%".format(v * 100, d=digits)


def fmt_x(v):
    return "n/a" if v is None else "{:.2f}x".format(v)


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        headers = [h.strip().lower() for h in (reader.fieldnames or [])]
        rows = []
        for raw in reader:
            rows.append({(k or "").strip().lower(): (v or "").strip() for k, v in raw.items()})
    return headers, rows


def load_spend(paths, warn):
    data = defaultdict(lambda: defaultdict(float))  # (date, channel) -> metric -> value
    for path in paths:
        headers, rows = read_csv(path)
        missing = [c for c in SPEND_COLS if c not in headers]
        if missing:
            raise SystemExit("%s: missing columns %s" % (path, ", ".join(missing)))
        for i, r in enumerate(rows, 2):
            try:
                d = parse_date(r["date"])
                ch = r["channel"].strip().lower() or "unknown"
                for c in SPEND_COLS[2:]:
                    data[(d, ch)][c] += num(r[c])
            except ValueError as e:
                warn("%s line %d skipped: %s" % (path, i, e))
    return data


def load_orders(path, salt, warn):
    headers, rows = read_csv(path)
    missing = [c for c in ORDER_COLS if c not in headers]
    if missing:
        raise SystemExit("%s: missing columns %s" % (path, ", ".join(missing)))
    bundle_col = "bundle" if "bundle" in headers else ("sku_group" if "sku_group" in headers else None)
    pii = [h for h in headers if h not in ORDER_COLS and (h in PII_EXACT or "email" in h or "phone" in h)]
    if pii:
        warn("ignored columns that look like personal data: %s. Remove them from exports (PII rule)." % ", ".join(pii))
    orders, seen, dupes = [], set(), []
    for i, r in enumerate(rows, 2):
        oid = r["order_id"]
        key = hashlib.sha256((salt + oid).encode("utf-8")).hexdigest()[:12]
        if key in seen:
            dupes.append(key)
            continue
        seen.add(key)
        try:
            o = {"date": parse_date(r["date"]), "id_hash": key,
                 "is_new": r["is_new_customer"].strip().lower() in TRUE,
                 "utm_source": r["utm_source"].strip().lower(),
                 "bundle": (r.get(bundle_col) or "unknown").strip() if bundle_col else "unknown"}
            for c in ORDER_COLS[2:]:
                if c not in ("is_new_customer", "utm_source"):
                    o[c] = num(r[c])
        except ValueError as e:
            warn("%s line %d skipped: %s" % (path, i, e))
            continue
        orders.append(o)
    if dupes:
        warn("%d duplicate order rows ignored (hashed ids: %s)" % (len(dupes), ", ".join(dupes[:5])))
    return orders


class Model:
    def __init__(self, args, spend, orders, warn):
        self.a, self.spend, self.orders, self.warn = args, spend, orders, warn
        self.channels = sorted({ch for (_, ch) in spend})
        dates = {d for (d, _) in spend} | {o["date"] for o in orders}
        if not dates:
            raise SystemExit("no data")
        self.report_date = parse_date(args.date) if args.date else max(dates)
        self.first_date, self.last_date = min(dates), max(dates)
        cmap = dict(DEFAULT_CHANNEL_MAP)
        for pair in (args.channel_map or "").split(","):
            if "=" in pair:
                k, v = pair.split("=", 1)
                cmap[k.strip().lower()] = v.strip().lower()
        self.cmap = cmap

    def channel_of(self, utm):
        if not utm or utm in ("(none)", "(direct)", "direct", "none"):
            return None
        for k, v in self.cmap.items():
            if utm == k or utm.startswith(k):
                return v
        return "other:" + utm

    def window_dates(self, days):
        return [self.report_date - dt.timedelta(days=i) for i in range(days)]

    def platform(self, dates, channel=None):
        out = defaultdict(float)
        for (d, ch), m in self.spend.items():
            if d in dates and (channel is None or ch == channel):
                for k, v in m.items():
                    out[k] += v
        return out

    def backend(self, dates):
        a = self.a
        rows = [o for o in self.orders if o["date"] in dates]
        b = defaultdict(float)
        b["orders"] = len(rows)
        for o in rows:
            fee = (o["revenue"] + o["shipping_charged"]) * a.payment_fee_rate + (a.payment_fee_fixed if o["revenue"] else 0)
            subsidy = max(0.0, o["shipping_cost"] - o["shipping_charged"])
            inc_disc = max(0.0, o["discount"] - a.baseline_discount)
            for c in ("revenue", "discount", "shipping_charged", "shipping_cost", "product_cost", "bonus_product_cost", "refund"):
                b[c] += o[c]
            b["payment_fees"] += fee
            b["shipping_subsidy"] += subsidy
            if o["is_new"]:
                b["new_orders"] += 1
                b["new_revenue"] += o["revenue"]
                b["new_refund"] += o["refund"]
                b["new_cm2"] += o["revenue"] - o["refund"] + o["shipping_charged"] - o["product_cost"] - o["bonus_product_cost"] - o["shipping_cost"] - fee
            in_scope = o["is_new"] or a.acq_scope == "all"
            if in_scope:
                b["acq_shipping_subsidy"] += subsidy
                b["acq_bonus_cost"] += o["bonus_product_cost"]
                b["acq_incremental_discount"] += inc_disc
            ch = self.channel_of(o["utm_source"])
            if ch is None:
                b["orders_no_utm"] += 1
            else:
                b["orders_ch:" + ch] += 1
        b["repeat_orders"] = b["orders"] - b["new_orders"]
        b["net_revenue"] = b["revenue"] - b["refund"]
        b["new_net_revenue"] = b["new_revenue"] - b["new_refund"]
        b["cm2"] = b["net_revenue"] + b["shipping_charged"] - b["product_cost"] - b["bonus_product_cost"] - b["shipping_cost"] - b["payment_fees"]
        return b, rows

    def metrics(self, days):
        dates = set(self.window_dates(days))
        p = self.platform(dates)
        b, rows = self.backend(dates)
        spend = p["spend"]
        acq = spend + b["acq_shipping_subsidy"] + b["acq_bonus_cost"] + b["acq_incremental_discount"]
        m = {
            "spend": spend, "impressions": p["impressions"], "clicks": p["clicks"],
            "platform_conversions": p["conversions"], "platform_value": p["conversion_value"],
            "ctr": div(p["clicks"], p["impressions"]), "cpc": div(spend, p["clicks"]),
            "cpm": div(spend * 1000, p["impressions"]),
            "platform_cpa": div(spend, p["conversions"]), "platform_roas": div(p["conversion_value"], spend),
            "blended_cac": div(spend, b["orders"]), "ncac": div(spend, b["new_orders"]),
            "aov": div(b["revenue"], b["orders"]), "new_aov": div(b["new_revenue"], b["new_orders"]),
            "mer": div(b["net_revenue"], spend), "amer": div(b["new_net_revenue"], spend),
            "cm3": b["cm2"] - spend, "poas": div(b["cm2"], spend),
            "acquisition_investment": acq, "first_order_acq_cost": div(acq, b["new_orders"]),
            "first_order_contribution": div(b["new_cm2"], b["new_orders"]),
            "discount_rate": div(b["discount"], b["revenue"] + b["discount"]),
            "refund_rate": div(b["refund"], b["revenue"]),
            "platform_ratio_orders": div(p["conversions"], b["orders"]),
            "platform_ratio_value": div(p["conversion_value"], b["net_revenue"]),
            "no_utm_share": div(b["orders_no_utm"], b["orders"]),
            # completeness: the channel with the fewest days that have spend rows decides
            "days_with_spend": min([len({d for (d, c), mm in self.spend.items() if c == ch and d in dates and mm.get("spend")})
                                    for ch in self.channels] or [0]),
            "days_with_orders": len({o["date"] for o in rows}),
        }
        m.update({k: v for k, v in b.items()})
        m["rows"] = rows
        return m

    def status_cost(self, value):
        """Green at or below target, amber up to target x (1 + band), red above."""
        t = self.a.target_cpa
        if t is None or value is None:
            return "n/a"
        if value <= t:
            return "GREEN"
        if value <= t * (1 + self.a.amber_band):
            return "AMBER"
        return "RED"

    def status_ratio(self, value, target):
        """For ratios where higher is better (aMER, POAS)."""
        if target is None or value is None:
            return "n/a"
        if value >= target:
            return "GREEN"
        if value >= target / (1 + self.a.amber_band):
            return "AMBER"
        return "RED"


def fact_table(model, path):
    dates = []
    d = model.first_date
    while d <= model.last_date:
        dates.append(d)
        d += dt.timedelta(days=1)
    cols = ["date", "spend_total"] + ["spend_" + c for c in model.channels] + \
           ["impressions", "clicks", "platform_conversions", "platform_conversion_value"] + \
           ["platform_conversions_" + c for c in model.channels] + \
           ["orders", "new_customer_orders", "repeat_orders", "revenue", "new_customer_revenue", "refunds", "net_revenue",
            "discounts", "shipping_charged", "shipping_cost", "shipping_subsidy", "product_cost", "bonus_product_cost",
            "payment_fees", "acquisition_investment", "contribution_before_marketing", "contribution_after_marketing",
            "orders_without_utm", "top_bundle"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for d in dates:
            p = model.platform({d})
            b, rows = model.backend({d})
            mix = defaultdict(int)
            for o in rows:
                mix[o["bundle"]] += 1
            top = max(mix.items(), key=lambda kv: kv[1])[0] if mix else ""
            acq = p["spend"] + b["acq_shipping_subsidy"] + b["acq_bonus_cost"] + b["acq_incremental_discount"]
            row = [d.isoformat(), round(p["spend"], 2)]
            row += [round(model.platform({d}, c)["spend"], 2) for c in model.channels]
            row += [int(p["impressions"]), int(p["clicks"]), round(p["conversions"], 2), round(p["conversion_value"], 2)]
            row += [round(model.platform({d}, c)["conversions"], 2) for c in model.channels]
            row += [int(b["orders"]), int(b["new_orders"]), int(b["repeat_orders"]), round(b["revenue"], 2), round(b["new_revenue"], 2),
                    round(b["refund"], 2), round(b["net_revenue"], 2), round(b["discount"], 2), round(b["shipping_charged"], 2),
                    round(b["shipping_cost"], 2), round(b["shipping_subsidy"], 2), round(b["product_cost"], 2),
                    round(b["bonus_product_cost"], 2), round(b["payment_fees"], 2), round(acq, 2), round(b["cm2"], 2),
                    round(b["cm2"] - p["spend"], 2), int(b["orders_no_utm"]), top]
            w.writerow(row)
    return len(dates)


def build_report(model, args, sources):
    cur = args.currency
    W = {label: model.metrics(days) for label, days in WINDOWS}
    y, d3, d7 = W["Yesterday"], W["Last 3 days"], W["Last 7 days"]
    t = args.target_cpa
    implied_amer = div(d7["new_aov"], t) if t else None
    L = []
    title = "# Daily performance report: %s%s" % ((args.brand + ", ") if args.brand else "", model.report_date.isoformat())
    L += [title, ""]
    L.append("Data used: %s. Orders file covers %s to %s. Report date (yesterday) %s. Currency %s. Dates are taken as exported; align platform and backend time zones before trusting day level gaps." % (
        "; ".join(sources), model.first_date, model.last_date, model.report_date, cur or "as exported"))
    L.append("")
    L.append("Target CPA: %s (%s). Status bands: GREEN at or below target, AMBER up to %d%% above, RED beyond. Ratios use the implied target (new customer AOV / target CPA)." % (
        fmt_money(t, cur) if t else "not set", "from --target-cpa; keep it in ads-master/METRICS.md" if t else "pass --target-cpa to enable status", round(args.amber_band * 100)))
    L.append("")

    # confidence
    reasons = []
    level = "High"
    if d7["new_orders"] < 30:
        level = "Medium" if d7["new_orders"] >= 10 else "Low"
        reasons.append("%d new customers in 7 days" % d7["new_orders"])
    if d7["days_with_spend"] < 7 or d7["days_with_orders"] < 7:
        level = "Low" if level == "Low" else "Medium"
        reasons.append("missing days (spend %d of 7, orders %d of 7)" % (d7["days_with_spend"], d7["days_with_orders"]))
    if (d7["no_utm_share"] or 0) > 0.2:
        level = "Low" if level != "High" else "Medium"
        reasons.append("%s of orders without UTM" % fmt_pct(d7["no_utm_share"]))
    if not reasons:
        reasons.append("at least 30 new customers in 7 days, complete days, UTM coverage at least 80%")
    L.append("Confidence: **%s** (%s). Decide on the 3 and 7 day windows; act on a single day only for incidents." % (level, "; ".join(reasons)))
    L.append("")

    L += ["## 1. Status", "", "| Metric | Yesterday | Last 3 days | Last 7 days | Target logic | Status 3d | Status 7d |",
          "|--------|-----------|-------------|-------------|--------------|-----------|-----------|"]
    L.append("| nCAC (media spend / new customers) | %s | %s | %s | at or below target CPA | %s | %s |" % (
        fmt_money(y["ncac"], cur), fmt_money(d3["ncac"], cur), fmt_money(d7["ncac"], cur), model.status_cost(d3["ncac"]), model.status_cost(d7["ncac"])))
    L.append("| Blended first order acquisition cost | %s | %s | %s | at or below target CPA | %s | %s |" % (
        fmt_money(y["first_order_acq_cost"], cur), fmt_money(d3["first_order_acq_cost"], cur), fmt_money(d7["first_order_acq_cost"], cur),
        model.status_cost(d3["first_order_acq_cost"]), model.status_cost(d7["first_order_acq_cost"])))
    L.append("| aMER (new customer net revenue / spend) | %s | %s | %s | at or above %s | %s | %s |" % (
        fmt_x(y["amer"]), fmt_x(d3["amer"]), fmt_x(d7["amer"]), fmt_x(implied_amer), model.status_ratio(d3["amer"], implied_amer), model.status_ratio(d7["amer"], implied_amer)))
    L.append("| MER (net revenue / spend) | %s | %s | %s | trend vs own history | n/a | n/a |" % (fmt_x(y["mer"]), fmt_x(d3["mer"]), fmt_x(d7["mer"])))
    L.append("| POAS (contribution before marketing / spend) | %s | %s | %s | 1.00x is first order breakeven | %s | %s |" % (
        fmt_x(y["poas"]), fmt_x(d3["poas"]), fmt_x(d7["poas"]), model.status_ratio(d3["poas"], 1.0), model.status_ratio(d7["poas"], 1.0)))
    L.append("| Contribution after marketing | %s | %s | %s | above 0 unless STRATEGY.md funds acquisition losses | n/a | n/a |" % (
        fmt_money(y["cm3"], cur), fmt_money(d3["cm3"], cur), fmt_money(d7["cm3"], cur)))
    L.append("")

    L += ["## 2. FACTS", "", "### 2.1 Platform reported, by channel", "",
          "| Channel | Spend 1d | Spend 3d | Spend 7d | CTR 7d | CPC 7d | CPM 7d | Conv. 7d | CPA 1d | CPA 3d | CPA 7d | ROAS 7d | CPA 7d status |",
          "|---------|----------|----------|----------|--------|--------|--------|----------|--------|--------|--------|---------|---------------|"]
    for ch in model.channels:
        r = {}
        for label, days in WINDOWS:
            p = model.platform(set(model.window_dates(days)), ch)
            r[days] = p
        p7 = r[7]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            ch, fmt_money(r[1]["spend"], cur), fmt_money(r[3]["spend"], cur), fmt_money(p7["spend"], cur),
            fmt_pct(div(p7["clicks"], p7["impressions"]), 2), fmt_money(div(p7["spend"], p7["clicks"]), cur),
            fmt_money(div(p7["spend"] * 1000, p7["impressions"]), cur), fmt_num(p7["conversions"], 1),
            fmt_money(div(r[1]["spend"], r[1]["conversions"]), cur), fmt_money(div(r[3]["spend"], r[3]["conversions"]), cur),
            fmt_money(div(p7["spend"], p7["conversions"]), cur), fmt_x(div(p7["conversion_value"], p7["spend"])),
            model.status_cost(div(p7["spend"], p7["conversions"])) + " (platform)"))
    L.append("| **Total** | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
        fmt_money(y["spend"], cur), fmt_money(d3["spend"], cur), fmt_money(d7["spend"], cur), fmt_pct(d7["ctr"], 2),
        fmt_money(d7["cpc"], cur), fmt_money(d7["cpm"], cur), fmt_num(d7["platform_conversions"], 1),
        fmt_money(y["platform_cpa"], cur), fmt_money(d3["platform_cpa"], cur), fmt_money(d7["platform_cpa"], cur),
        fmt_x(d7["platform_roas"]), "sum overstates (see 2.4)"))
    L.append("")

    L += ["### 2.2 Backend observed", "", "| Metric | Yesterday | Last 3 days | Last 7 days |", "|--------|-----------|-------------|-------------|"]
    rows = [("Orders", "orders", "n"), ("New customer orders", "new_orders", "n"), ("Repeat orders", "repeat_orders", "n"),
            ("Revenue (after discounts, ex shipping)", "revenue", "m"), ("Refunds", "refund", "m"), ("Net revenue", "net_revenue", "m"),
            ("New customer revenue", "new_revenue", "m"), ("AOV", "aov", "m"), ("New customer AOV", "new_aov", "m"),
            ("Discounts", "discount", "m"), ("Discount rate", "discount_rate", "p"), ("Shipping charged", "shipping_charged", "m"),
            ("Shipping cost (estimated)", "shipping_cost", "m"), ("Shipping subsidy (cost minus charged)", "shipping_subsidy", "m"),
            ("Product cost", "product_cost", "m"), ("Bonus product cost", "bonus_product_cost", "m"), ("Payment fees (estimated)", "payment_fees", "m"),
            ("Refund rate", "refund_rate", "p"), ("Contribution before marketing", "cm2", "m")]
    for label, key, kind in rows:
        f = {"n": lambda v: fmt_num(v), "m": lambda v: fmt_money(v, cur), "p": lambda v: fmt_pct(v)}[kind]
        L.append("| %s | %s | %s | %s |" % (label, f(y[key]), f(d3[key]), f(d7[key])))
    L.append("")

    L += ["### 2.3 Unit economics", "", "| Metric | Yesterday | Last 3 days | Last 7 days |", "|--------|-----------|-------------|-------------|"]
    econ = [("Media spend", "spend", "m"), ("Acquisition investment (spend + shipping subsidy + bonus cost + incremental discount, %s orders)" % args.acq_scope, "acquisition_investment", "m"),
            ("  of which shipping subsidy", "acq_shipping_subsidy", "m"), ("  of which bonus product cost", "acq_bonus_cost", "m"),
            ("  of which incremental discount", "acq_incremental_discount", "m"),
            ("Blended CAC (spend / all orders)", "blended_cac", "m"), ("nCAC (spend / new customers)", "ncac", "m"),
            ("Blended first order acquisition cost", "first_order_acq_cost", "m"),
            ("First order contribution per new customer", "first_order_contribution", "m"),
            ("MER", "mer", "x"), ("aMER", "amer", "x"), ("POAS", "poas", "x"), ("Contribution after marketing", "cm3", "m")]
    for label, key, kind in econ:
        f = {"m": lambda v: fmt_money(v, cur), "x": fmt_x}[kind]
        L.append("| %s | %s | %s | %s |" % (label, f(y[key]), f(d3[key]), f(d7[key])))
    L.append("")

    L += ["### 2.4 Platform reported vs backend observed", "",
          "| Window | Platform conversions (sum) | Backend orders | Ratio | Platform value (sum) | Backend net revenue | Ratio | Orders without UTM |",
          "|--------|---------------------------|----------------|-------|----------------------|---------------------|-------|-------------------|"]
    for label, _ in WINDOWS:
        m = W[label]
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            label, fmt_num(m["platform_conversions"], 1), fmt_num(m["orders"]), fmt_x(m["platform_ratio_orders"]),
            fmt_money(m["platform_value"], cur), fmt_money(m["net_revenue"], cur), fmt_x(m["platform_ratio_value"]), fmt_pct(m["no_utm_share"])))
    L += ["", "| Channel (7d) | Platform conversions | Backend orders with matching UTM (last click) | Ratio | Deflated CPA (spend / UTM orders) |",
          "|--------------|---------------------|-----------------------------------------------|-------|-----------------------------------|"]
    for ch in model.channels:
        p7 = model.platform(set(model.window_dates(7)), ch)
        bo = d7.get("orders_ch:" + ch, 0)
        L.append("| %s | %s | %s | %s | %s |" % (ch, fmt_num(p7["conversions"], 1), fmt_num(bo), fmt_x(div(p7["conversions"], bo)), fmt_money(div(p7["spend"], bo), cur)))
    other = sorted(k[len("orders_ch:"):] for k in d7 if k.startswith("orders_ch:") and k[len("orders_ch:"):] not in model.channels)
    for ch in other:
        L.append("| %s (no spend file) | n/a | %s | n/a | n/a |" % (ch, fmt_num(d7["orders_ch:" + ch])))
    L += ["", "Gaps between the two are expected. Common causes: attribution windows (click and view), view-through credit, cross device and modeled conversions, consent and ad blockers, missing or stripped UTMs, several platforms claiming the same order, returning customers re-converting, time zone differences. Never sum platform conversions as truth; use backend numbers for MER, aMER and nCAC.", ""]

    L += ["### 2.5 Product and bundle mix (last 7 days)", "", "| Bundle or SKU group | Orders | Share | New customer orders | Revenue | Avg discount | Bonus cost |",
          "|---------------------|--------|-------|---------------------|---------|--------------|------------|"]
    mix = defaultdict(lambda: defaultdict(float))
    for o in d7["rows"]:
        g = mix[o["bundle"]]
        g["orders"] += 1
        g["new"] += 1 if o["is_new"] else 0
        g["revenue"] += o["revenue"]
        g["discount"] += o["discount"]
        g["bonus"] += o["bonus_product_cost"]
    for name, g in sorted(mix.items(), key=lambda kv: -kv[1]["orders"]):
        L.append("| %s | %s | %s | %s | %s | %s | %s |" % (name, fmt_num(g["orders"]), fmt_pct(div(g["orders"], d7["orders"])),
                                                          fmt_num(g["new"]), fmt_money(g["revenue"], cur), fmt_money(div(g["discount"], g["orders"]), cur), fmt_money(g["bonus"], cur)))
    L.append("")

    # incidents (daily)
    L += ["### 2.6 Incident checks (yesterday)", "", "| Check | Result |", "|-------|--------|"]
    alerts = []
    avg7 = d7["spend"] / 7 if d7["spend"] else 0
    checks = [
        ("Spend recorded but zero backend orders", y["spend"] > 0 and y["orders"] == 0),
        ("Backend orders but zero platform conversions (tracking break?)", y["orders"] > 0 and y["platform_conversions"] == 0 and y["spend"] > 0),
        ("Spend over 1.5x the 7 day daily average (pacing)", avg7 > 0 and y["spend"] > 1.5 * avg7),
        ("Spend under 0.5x the 7 day daily average (delivery or billing)", avg7 > 0 and y["spend"] < 0.5 * avg7),
        ("Platform to backend order ratio moved over 50% vs 7 days", y["platform_ratio_orders"] is not None and d7["platform_ratio_orders"] and abs(y["platform_ratio_orders"] / d7["platform_ratio_orders"] - 1) > 0.5),
        ("A channel has no spend recorded for yesterday", any(model.platform({model.report_date}, c)["spend"] == 0 for c in model.channels)),
    ]
    for name, hit in checks:
        L.append("| %s | %s |" % (name, "ALERT" if hit else "ok"))
        if hit:
            alerts.append(name)
    L.append("")

    # interpretation
    L += ["## 3. INTERPRETATION (rule based; verify before acting)", ""]
    interp = []
    s7, s3, s1 = model.status_cost(d7["ncac"]), model.status_cost(d3["ncac"]), model.status_cost(y["ncac"])
    if t:
        interp.append("nCAC is %s over 7 days (%s vs target %s) and %s over 3 days (%s)." % (s7, fmt_money(d7["ncac"], cur), fmt_money(t, cur), s3, fmt_money(d3["ncac"], cur)))
        if s1 == "RED" and s7 == "GREEN":
            interp.append("Yesterday alone is RED while 7 days is GREEN: treat as day level noise unless an incident check fired.")
        if d3["ncac"] and d7["ncac"]:
            change = d3["ncac"] / d7["ncac"] - 1
            if abs(change) > args.amber_band / 2:
                interp.append("Early signal: 3 day nCAC is %s the 7 day value (%s)." % ("above" if change > 0 else "below", fmt_pct(change)))
    else:
        interp.append("No target CPA given, so no status. Set it in ads-master/METRICS.md and pass --target-cpa.")
    if d7["first_order_acq_cost"] and d7["ncac"]:
        share = 1 - d7["spend"] / d7["acquisition_investment"] if d7["acquisition_investment"] else 0
        interp.append("Non media acquisition costs (shipping subsidy, bonus products, incremental discounts) add %s to media spend; first order acquisition cost is %s vs nCAC %s." % (
            fmt_pct(share), fmt_money(d7["first_order_acq_cost"], cur), fmt_money(d7["ncac"], cur)))
    if d7["first_order_contribution"] is not None and d7["first_order_acq_cost"] is not None:
        if d7["first_order_acq_cost"] > d7["first_order_contribution"]:
            interp.append("Acquisition cost (%s) exceeds first order contribution (%s): payback depends on repeat purchases; check cohort LTV before scaling." % (
                fmt_money(d7["first_order_acq_cost"], cur), fmt_money(d7["first_order_contribution"], cur)))
        else:
            interp.append("First order contribution (%s) covers acquisition cost (%s): new customers pay back on the first order." % (
                fmt_money(d7["first_order_contribution"], cur), fmt_money(d7["first_order_acq_cost"], cur)))
    r = d7["platform_ratio_orders"]
    if r is not None:
        if r > 1.3:
            interp.append("Platforms claim %s the backend order count over 7 days: overlapping credit. Use backend metrics for allocation." % fmt_x(r))
        elif r < 0.7:
            interp.append("Platforms report only %s of backend orders: possible tracking loss (pixel, conversion API, consent). Hand off to measurement." % fmt_x(r))
        else:
            interp.append("Platform conversions are %s of backend orders: within the usual overlap range for this report." % fmt_x(r))
    if (d7["no_utm_share"] or 0) > 0.2:
        interp.append("%s of 7 day orders carry no UTM: last click channel splits are unreliable." % fmt_pct(d7["no_utm_share"]))
    if d3["discount_rate"] is not None and d7["discount_rate"] is not None and d3["discount_rate"] - d7["discount_rate"] > 0.02:
        interp.append("Discount rate is rising (3 days %s vs 7 days %s)." % (fmt_pct(d3["discount_rate"]), fmt_pct(d7["discount_rate"])))
    for line in interp:
        L.append("- " + line)
    L.append("")

    # recommendation
    L += ["## 4. RECOMMENDATION (draft; every change needs human approval)", ""]
    rec = []
    if alerts:
        rec.append("Incident: %s. Open an entry in ads-master/INCIDENTS.md and check tracking and delivery before any optimization." % "; ".join(alerts))
    if t:
        if s7 == "RED" and s3 == "RED":
            worst = None
            for ch in model.channels:
                p7 = model.platform(set(model.window_dates(7)), ch)
                bo = d7.get("orders_ch:" + ch, 0)
                v = div(p7["spend"], bo)
                if v is not None and (worst is None or v > worst[1]):
                    worst = (ch, v)
            rec.append("RED on 3 and 7 days: ask the channel agent for %s (highest deflated CPA %s) for a diagnosis and a change proposal. Do not cut budgets from this report alone." % (
                worst[0] if worst else "the largest channel", fmt_money(worst[1], cur) if worst else "n/a"))
        elif s7 == "AMBER" or s3 == "AMBER":
            rec.append("AMBER: hold budgets, watch the 3 day trend tomorrow, check creative fatigue and offer changes.")
        elif s7 == "GREEN" and s3 == "GREEN" and level != "Low":
            rec.append("GREEN on 3 and 7 days with %s confidence: candidate for a controlled scale test on the channel with the lowest deflated CPA, per the scaling rule in STRATEGY.md (growth-orchestrator decides)." % level)
        else:
            rec.append("Mixed or low confidence signal: no change; collect more data.")
    if r is not None and r < 0.7:
        rec.append("Hand off to measurement: reconcile platform conversions with backend orders (capture rate, CAPI, consent).")
    if not rec:
        rec.append("No action. Keep monitoring.")
    for line in rec:
        L.append("- " + line)
    L.append("")
    L += ["## 5. Definitions", "",
          "- CTR = clicks / impressions. CPC = spend / clicks. CPM = spend / impressions x 1000. Platform CPA = spend / platform conversions. Platform ROAS = conversion value / spend.",
          "- Net revenue = revenue (after discounts, ex tax and shipping) minus refunds. MER = net revenue / media spend. aMER = new customer net revenue / media spend.",
          "- Blended CAC = media spend / all orders. nCAC = media spend / new customer orders. AOV = revenue / orders.",
          "- Contribution before marketing = net revenue plus shipping charged, minus product cost, bonus product cost, shipping cost and payment fees. After marketing = before minus media spend. POAS = contribution before marketing / media spend.",
          "- Acquisition investment = media spend + shipping subsidy + bonus product cost + incremental discount cost (%s orders; incremental discount = discount above %s per order). Blended first order acquisition cost = acquisition investment / new customers." % (args.acq_scope, fmt_money(args.baseline_discount, cur)),
          "- Status: cost metrics GREEN at or below target CPA, AMBER up to %d%% above, RED beyond; aMER against new customer AOV / target CPA; POAS against 1.00x." % round(args.amber_band * 100),
          ""]
    return "\n".join(L)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Unified daily fact table and daily report (stdlib only).")
    ap.add_argument("--spend", nargs="+", required=True, help="Platform spend CSV files")
    ap.add_argument("--orders", required=True, help="Backend orders CSV")
    ap.add_argument("--target-cpa", type=float, help="Target cost per new customer from METRICS.md or STRATEGY.md")
    ap.add_argument("--amber-band", type=float, default=0.2, help="Share above target that is still AMBER (default 0.2)")
    ap.add_argument("--date", help="Report date (yesterday), YYYY-MM-DD; default: latest date in the data")
    ap.add_argument("--currency", default="", help="Currency label, for example EUR or TRY")
    ap.add_argument("--brand", default="", help="Brand name for the title")
    ap.add_argument("--acq-scope", choices=["new", "all"], default="new", help="Count subsidy, bonus and discount costs on new customer orders only (default) or all orders")
    ap.add_argument("--baseline-discount", type=float, default=0.0, help="Per order discount that is not acquisition cost (default 0)")
    ap.add_argument("--payment-fee-rate", type=float, default=0.0, help="Payment fee share of revenue plus shipping, for example 0.029")
    ap.add_argument("--payment-fee-fixed", type=float, default=0.0, help="Fixed payment fee per order")
    ap.add_argument("--channel-map", help="Extra utm_source to channel pairs, for example 'newsletter=email,fbads=meta'")
    ap.add_argument("--salt", default=os.environ.get("DAILY_REPORT_SALT", ""), help="Salt for hashing order IDs (or env DAILY_REPORT_SALT)")
    ap.add_argument("--fact-table", help="Write the daily fact table CSV here")
    ap.add_argument("--out", help="Write the Markdown report here (default stdout)")
    args = ap.parse_args(argv)

    warnings = []

    def warn(msg):
        warnings.append(msg)
        print("WARN " + msg, file=sys.stderr)

    spend = load_spend(args.spend, warn)
    orders = load_orders(args.orders, args.salt, warn)
    model = Model(args, spend, orders, warn)
    spend_dates = sorted({d for (d, _) in spend})
    sources = ["spend files %s (%s to %s)" % (", ".join(os.path.basename(p) for p in args.spend),
                                              spend_dates[0] if spend_dates else "n/a", spend_dates[-1] if spend_dates else "n/a"),
               "orders file %s (%d unique orders)" % (os.path.basename(args.orders), len(orders))]
    if args.fact_table:
        n = fact_table(model, args.fact_table)
        print("fact table: %d days written to %s" % (n, args.fact_table), file=sys.stderr)
    report = build_report(model, args, sources)
    if warnings:
        report += "\n## Data warnings\n\n" + "\n".join("- " + w for w in warnings) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report)
    else:
        sys.stdout.write(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
