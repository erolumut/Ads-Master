# Feed Tools and Automation

> How to choose the feed stack, which APIs and connectors exist, how to monitor feeds automatically, and copy-paste scripts. Knowledge as of 2026-10. Vendor features and prices change often: confirm with the vendor before recommending a purchase.

## 1. Stack options

| Option | Examples | Strength | Weakness | Fits |
|--------|----------|----------|----------|------|
| Native platform app | Shopify Google and YouTube app, Google for WooCommerce, BigCommerce channels, Meta and TikTok and Pinterest sales channel apps | Free, real-time sync, low maintenance | Limited transformation; per-channel apps drift apart; limited custom labels | Starter and Growth, few channels |
| Feed management platform | Feedonomics (owned by BigCommerce), Productsup, Channable, DataFeedWatch, GoDataFeed, Feedoptimise, Lengow | One master, rules per channel, many destinations including ChatGPT feeds at several vendors, QA and monitoring | Monthly cost; another system to own; rule sprawl | Growth to Enterprise, 3 or more channels or complex catalogs |
| Optimization and label tools | Producthero (feed optimization, performance labels, CSS), similar label tools | Performance-based labels and title tests without engineering | Narrower scope | Google-heavy advertisers |
| Custom pipeline | Scripts or a service on the store database writing files and calling APIs (Merchant API, Meta Batch API, Pinterest Catalogs API, OpenAI SFTP) | Full control, real-time, cheapest at scale | Engineering time, monitoring burden | Custom platforms, Enterprise, unusual data |
| Hybrid (common best answer) | Native app as primary for Google, supplemental source from a script or Sheets, feed tool for other channels | Stable core plus flexible enrichment | Two places to look | Most Growth and Scale stores |

### Decision rules
1. One transformation layer. If a feed tool exists, all channel logic lives there; native apps only push raw data.
2. Do not run two primaries for the same products in one Merchant Center (for example the Shopify app and a feed tool both creating products): duplicates and conflicting updates follow.
3. Price and stock latency target: under 1 hour for fast movers and during sales; daily is acceptable only for slow-moving catalogs.
4. Choose by destinations needed in the next 12 months, catalog size, change frequency, and who will maintain it.

### Vendor evaluation checklist
- Destinations supported today (Google, Microsoft, Meta, TikTok ads catalog, TikTok Shop, Pinterest, Snap, OpenAI, Perplexity, marketplaces).
- Merchant API support (Content API shut down 2026-08-18): ask how they write to Merchant Center now.
- Supplemental source support, rule versioning and rollback, audit log.
- QA: error dashboards per channel, alerting, sample PDP crawl.
- Data inputs: platform connectors, database, PIM, Sheets, custom fields (metafields).
- Price model (SKU count, channels, add-ons) and contract terms.
- Managed service option and response time in peak season.

## 2. APIs and connectors Claude can use

| System | Interface | Read | Write | Notes |
|--------|-----------|------|-------|-------|
| Google Merchant Center | Merchant API v1 (REST and gRPC; client libraries for Python, Java, PHP, Node, .NET, Go, Ruby) | Products, statuses, issues, reports (MCQL), data sources | Product inputs, data sources, local and regional inventories, promotions, reviews | OAuth scope `https://www.googleapis.com/auth/content`; service account with Merchant Center access |
| Google Ads | Google Ads API, Google Ads scripts, GAQL | `shopping_performance_view` by item ID, custom attributes | Listing groups (google-ads agent owns) | Use for label inputs |
| Meta | Marketing API v26.0 | Catalog diagnostics, product sets, items | `items_batch`, `localized_items_batch`, product sets, feeds | System user token with catalog permission |
| Pinterest | API v5 (OpenAPI 5.28.0) | Catalogs, items, product groups | Items batch, feeds | |
| TikTok | Business API (catalog endpoints) | Catalog items | Items upload | Verify current endpoints [Unverified] |
| Microsoft Merchant Center | Content API style service, feed fetch, Google Merchant Center Import tool (scheduled) | Product status | Products | Import carries only approved Google offers [Official, Microsoft Advertising Help]; API details verify in Microsoft Learn |
| OpenAI (ChatGPT) | SFTP file delivery after acceptance; Ads Manager feeds (upload, URL, SFTP); ACP Feed API for agent-hosted feeds | n/a | Feed files | No public product submission API for ads feeds reported in 2026-06 |
| Shopify | Admin GraphQL API | Products, variants, metafields, inventory, orders | Metafields (labels, Google fields) | Platform data is also the AI channel feed |
| WooCommerce | REST API, Google for WooCommerce extension | Products, orders | Product meta | |

MCP servers: Google published an open source Google Ads MCP server (read-oriented) in 2025; Shopify offers developer and storefront MCP servers, and ACP (2026-04-17) and UCP both define MCP bindings for checkout and catalog. Community MCP servers for Merchant Center and feed tools appear and change frequently [Unverified: check each one]. Before using any, check the publisher, the scopes it requests, and whether it can write. Prefer read-only scopes for audits [Practitioner consensus].

## 3. Monitoring and alerting design

| Signal | Source | Threshold (default) | Action |
|--------|--------|---------------------|--------|
| Disapproved items share | Merchant API `product_view` or UI | Over 2 percent of items or any top 50 revenue SKU | Alert, open diagnostics runbook |
| Account issues | Merchant API account issues, notifications | Any new account-level issue | Alert human same day |
| Data source fetch failure | Data source status | Any failure | Alert, check URL and credentials |
| Item count drop | Daily product count | Drop over 5 percent day over day | Alert: likely feed truncation or sync break |
| Price mismatch item issues | Item issues | Any increase over 20 percent week over week | Run parity script |
| Feed age | Last successful update | Over 24 hours (over 1 hour in peak season) | Alert |
| Zombie rate | Product performance | Over 30 percent of eligible SKUs with zero impressions in 30 days | Weekly review |
| Meta catalog errors | Catalog diagnostics | New error type | Weekly review |
| Pixel and catalog match | Meta event diagnostics | Match below 90 percent | Hand off to measurement |

Implementation choices: a scheduled job (cron, CI, Cloud Scheduler) calling the Merchant API; a Google Ads script that reads Merchant Center data (Merchant API in scripts since 2026); a feed tool's built-in alerts; or a Claude Code Routine that runs the audit checklist weekly and writes a journal entry.

## 4. Supplemental feed patterns

| Pattern | Columns | Notes |
|---------|---------|-------|
| Title overrides | `id`, `title` | Keep a version column outside the uploaded file for rollback |
| Custom labels | `id`, `custom_label_0` to `custom_label_4` | Weekly from `label_builder.py` |
| Identifier fixes | `id`, `gtin`, `mpn`, `brand`, `identifier_exists` | Only verified values |
| Enrichment | `id`, `product_highlight`, `product_detail`, `material`, `pattern` | Multiple values: repeat the column or use the format the source supports |
| Exclusions | `id`, `excluded_destination` or `pause` | Prefer exclusion over deletion to keep history |
| Lifestyle images | `id`, `lifestyle_image_link`, `additional_image_link` | |

Google Sheets as a supplemental source: header row with attribute names, one row per `id`; Merchant Center fetches on schedule. Good up to tens of thousands of rows; above that use files.

## 5. Script: offline feed QA (`feed_qa.py`)
Tested on 2026-10-08 with TSV input. Standard library only. Reads TSV, CSV or Google RSS XML and writes a markdown report.

```python
#!/usr/bin/env python3
"""feed_qa.py: offline QA for a Google-format product feed (TSV, CSV or RSS/Atom XML).

Usage:
  python3 feed_qa.py ads-master/data/imports/2026-10-08_gmc_feed.tsv > report.md
  python3 feed_qa.py feed.xml --country US --max-rows 200000

Checks (no network calls): required fields, duplicate IDs, ID length,
GTIN check digit and prefix, title and description length, promo text,
ALL CAPS, price and sale_price format, availability values, preorder or
backorder dates, image URL format, variant grouping, custom label
cardinality, identifier coverage. Output is a markdown report.
"""
import csv
import re
import sys
import argparse
import collections
import xml.etree.ElementTree as ET

REQUIRED = ["id", "title", "description", "link", "image_link", "availability", "price"]
AVAIL_OK = {"in_stock", "out_of_stock", "preorder", "backorder", "in stock", "out of stock"}
PROMO_RE = re.compile(r"\b(free shipping|sale|% off|discount|buy now|best price|cheapest|limited time|coupon)\b", re.I)
PRICE_RE = re.compile(r"^\s*\d+(\.\d{1,2})?\s+[A-Z]{3}\s*$")
G_NS = "{http://base.google.com/ns/1.0}"


def gtin_ok(raw):
    """Validate a GTIN-8/12/13/14 check digit. Returns (ok, reason)."""
    g = re.sub(r"\D", "", raw or "")
    if not g:
        return False, "empty"
    if len(g) not in (8, 12, 13, 14):
        return False, "length %d" % len(g)
    if set(g) == {"0"}:
        return False, "all zeros"
    padded = g.zfill(14)
    g13_prefix = int(padded[1:4])  # first 3 digits of the GTIN-13 form
    # GS1 restricted circulation (020-029, 040-049, 200-299) and coupons (980-999)
    if 20 <= g13_prefix <= 29 or 40 <= g13_prefix <= 49 or 200 <= g13_prefix <= 299 or g13_prefix >= 980:
        return False, "restricted or in-store prefix"
    digits = [int(c) for c in padded]
    total = 0
    for i, d in enumerate(digits[:-1]):
        total += d * (3 if i % 2 == 0 else 1)
    check = (10-(total % 10)) % 10
    if check != digits[-1]:
        return False, "bad check digit"
    return True, "ok"


def read_rows(path):
    if path.lower().endswith(".xml"):
        tree = ET.parse(path)
        root = tree.getroot()
        items = root.findall(".//item") or root.findall(".//{http://www.w3.org/2005/Atom}entry")
        for it in items:
            row = collections.defaultdict(str)
            for child in it:
                tag = child.tag.replace(G_NS, "").replace("{http://www.w3.org/2005/Atom}", "")
                text = (child.text or "").strip()
                if tag in row and row[tag]:
                    row[tag] += "," + text
                else:
                    row[tag] = text
            yield dict(row)
        return
    with open(path, newline="", encoding="utf-8-sig") as fh:
        sample = fh.read(4096)
        fh.seek(0)
        delim = "\t" if sample.count("\t") > sample.count(",") else ","
        for row in csv.DictReader(fh, delimiter=delim):
            yield {(k or "").strip().lower(): (v or "").strip() for k, v in row.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--max-rows", type=int, default=10**7)
    args = ap.parse_args()

    issues = collections.Counter()
    examples = collections.defaultdict(list)
    ids = collections.Counter()
    label_values = collections.defaultdict(set)
    n = 0
    with_gtin = with_brand = with_mpn = with_gpc = with_ptype = 0
    title_lens = []

    def flag(code, pid, detail=""):
        issues[code] += 1
        if len(examples[code]) < 5:
            examples[code].append("%s %s" % (pid, detail))

    for row in read_rows(args.path):
        n += 1
        if n > args.max_rows:
            break
        pid = row.get("id", "")
        ids[pid] += 1
        for f in REQUIRED:
            if not row.get(f):
                flag("missing_" + f, pid)
        if len(pid) > 50:
            flag("id_over_50_chars", pid)
        t = row.get("title", "")
        title_lens.append(len(t))
        if len(t) > 150:
            flag("title_over_150", pid, str(len(t)))
        if 0 < len(t) < 25:
            flag("title_under_25_chars", pid, t)
        if t and t.upper() == t and re.search(r"[A-Z]{4,}", t):
            flag("title_all_caps", pid, t[:40])
        if PROMO_RE.search(t):
            flag("title_promo_text", pid, t[:60])
        d = row.get("description", "")
        if len(d) > 5000:
            flag("description_over_5000", pid)
        if d and len(d) < 150:
            flag("description_under_150_chars", pid)
        if "<" in d and ">" in d:
            flag("description_contains_html", pid)
        p = row.get("price", "")
        if p and not PRICE_RE.match(p):
            flag("price_format", pid, p)
        sp = row.get("sale_price", "")
        if sp:
            if not PRICE_RE.match(sp):
                flag("sale_price_format", pid, sp)
            else:
                try:
                    if float(sp.split()[0]) >= float(p.split()[0]):
                        flag("sale_price_not_lower", pid, "%s vs %s" % (sp, p))
                except (ValueError, IndexError):
                    pass
        av = row.get("availability", "").lower()
        if av and av not in AVAIL_OK:
            flag("availability_value", pid, av)
        if av in {"preorder", "backorder"} and not row.get("availability_date"):
            flag("missing_availability_date", pid)
        img = row.get("image_link", "")
        if img and not img.startswith("https://"):
            flag("image_not_https", pid, img[:60])
        link = row.get("link", "")
        if link and not link.startswith("https://"):
            flag("link_not_https", pid)
        g = row.get("gtin", "")
        if g:
            with_gtin += 1
            for one in g.split(","):
                ok, why = gtin_ok(one)
                if not ok:
                    flag("gtin_invalid_" + why.replace(" ", "_"), pid, one)
        if row.get("brand"):
            with_brand += 1
        if row.get("mpn"):
            with_mpn += 1
        if row.get("google_product_category"):
            with_gpc += 1
        if row.get("product_type"):
            with_ptype += 1
        if not g and not row.get("mpn") and row.get("identifier_exists", "").lower() not in {"no", "false"}:
            flag("no_identifier_and_identifier_exists_not_false", pid)
        if any(row.get(k) for k in ("color", "size")) and not row.get("item_group_id"):
            flag("variant_attrs_without_item_group_id", pid)
        for i in range(5):
            v = row.get("custom_label_%d" % i, "")
            if v:
                label_values[i].add(v)
                if len(v) > 100:
                    flag("custom_label_over_100", pid)

    dupes = [k for k, c in ids.items() if c > 1]
    out = []
    out.append("# Feed QA report: %s\n" % args.path)
    out.append("Rows checked: %d. Unique IDs: %d. Duplicate IDs: %d.\n" % (n, len(ids), len(dupes)))
    if n:
        out.append("| Coverage | Share |\n|---|---|")
        for name, val in (("gtin", with_gtin), ("brand", with_brand), ("mpn", with_mpn),
                          ("google_product_category", with_gpc), ("product_type", with_ptype)):
            out.append("| %s | %.1f%% |" % (name, 100.0 * val / n))
        title_lens.sort()
        out.append("| median title length | %d chars |" % title_lens[len(title_lens) // 2])
        out.append("")
    out.append("## Issues (count, up to 5 examples)\n")
    out.append("| Issue | Count | Examples |\n|---|---|---|")
    for code, c in issues.most_common():
        out.append("| %s | %d | %s |" % (code, c, "; ".join(examples[code])))
    if dupes:
        out.append("| duplicate_id | %d | %s |" % (len(dupes), "; ".join(dupes[:5])))
    out.append("\n## Custom label cardinality (limit 1,000 unique values per label)\n")
    for i in range(5):
        out.append("- custom_label_%d: %d unique values" % (i, len(label_values[i])))
    print("\n".join(out))


if __name__ == "__main__":
    main()
```

Run it on every feed export dropped in `ads-master/data/imports/` and attach the report to the audit output. It catches format problems before Merchant Center does; it cannot see policy issues, crawl mismatches or Google's own matching.

## 6. Script: custom label builder (`label_builder.py`)
Tested on 2026-10-08. Produces a supplemental feed with the slot plan in [custom labels](custom-labels-and-segmentation.md).

```python
#!/usr/bin/env python3
"""label_builder.py: build a custom label supplemental feed (id + custom_label_0..4).

Inputs (CSV, header row required):
  --catalog  id,price,cost,created_at(YYYY-MM-DD),inventory_qty,units_sold_30d[,season]
  --perf     item_id,impressions,clicks,cost,conversions,conv_value   (last 30 or 60 days,
             from the Google Ads shopping_performance_view or the Products report)
Options:
  --breakeven-roas 2.5    revenue / ad cost at which contribution is zero (1 / contribution margin)
  --aov 80                average order value, used for price bands
  --today 2026-10-08

Output: TSV to stdout, ready to upload as a Merchant Center supplemental data
source (Google Sheets or file). Slot plan (change it to match STRATEGY.md):
  custom_label_0 performance tier   hero | sidekick | villain | zombie | new
  custom_label_1 margin band        m_low | m_mid | m_high | m_unknown
  custom_label_2 price band         p_under_half_aov | p_near_aov | p_over_2x_aov
  custom_label_3 lifecycle / stock  new_30d | low_stock | overstock | core
  custom_label_4 season or campaign value passed through from catalog (or empty)
"""
import csv
import sys
import argparse
import datetime as dt


def f(x, default=0.0):
    try:
        return float(str(x).replace(",", "").strip() or default)
    except ValueError:
        return default


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--perf", required=True)
    ap.add_argument("--breakeven-roas", type=float, required=True)
    ap.add_argument("--aov", type=float, required=True)
    ap.add_argument("--today", default=dt.date.today().isoformat())
    ap.add_argument("--min-clicks", type=int, default=30, help="clicks needed before judging a SKU")
    args = ap.parse_args()
    today = dt.date.fromisoformat(args.today)
    target = args.breakeven_roas

    perf = {}
    with open(args.perf, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            perf[r["item_id"].strip().lower()] = r

    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerow(["id", "custom_label_0", "custom_label_1", "custom_label_2", "custom_label_3", "custom_label_4"])
    with open(args.catalog, newline="", encoding="utf-8-sig") as fh:
        for r in csv.DictReader(fh):
            pid = r["id"].strip()
            p = perf.get(pid.lower(), {})
            imps, clicks = f(p.get("impressions")), f(p.get("clicks"))
            cost, value, conv = f(p.get("cost")), f(p.get("conv_value")), f(p.get("conversions"))
            created = r.get("created_at") or ""
            age_days = (today-dt.date.fromisoformat(created[:10])).days if created else 9999

            # custom_label_0: performance tier
            if age_days <= 30 and clicks < args.min_clicks:
                tier = "new"
            elif imps < 50:
                tier = "zombie"            # catalog item the auction ignores
            elif clicks < args.min_clicks:
                tier = "sidekick"          # not enough data to judge: keep exposure
            elif conv >= 1 and cost > 0 and value / cost >= target * 1.2:
                tier = "hero"
            elif conv == 0 or (cost > 0 and value / cost < target * 0.8):
                tier = "villain"
            else:
                tier = "sidekick"

            # custom_label_1: margin band from price and COGS
            price, unit_cost = f(r.get("price")), f(r.get("cost"))
            if price > 0 and unit_cost > 0:
                m = (price-unit_cost) / price
                margin = "m_high" if m >= 0.55 else ("m_mid" if m >= 0.35 else "m_low")
            else:
                margin = "m_unknown"

            # custom_label_2: price band relative to AOV
            if price < 0.5 * args.aov:
                band = "p_under_half_aov"
            elif price <= 2 * args.aov:
                band = "p_near_aov"
            else:
                band = "p_over_2x_aov"

            # custom_label_3: lifecycle and stock (days of cover)
            qty, sold30 = f(r.get("inventory_qty")), f(r.get("units_sold_30d"))
            cover = qty / (sold30 / 30.0) if sold30 > 0 else (9999 if qty > 0 else 0)
            if age_days <= 30:
                life = "new_30d"
            elif 0 < cover < 14:
                life = "low_stock"
            elif cover > 120 and qty >= 20:
                life = "overstock"
            else:
                life = "core"

            w.writerow([pid, tier, margin, band, life, (r.get("season") or "").strip().lower()])


if __name__ == "__main__":
    main()
```

Weekly routine:
1. Export product performance for the last 30 or 60 days (GAQL in [custom labels](custom-labels-and-segmentation.md) section 4) and the catalog with costs and stock.
2. Run the builder; diff against last week's output; count tier moves.
3. Draft the change list (how many SKUs move between campaigns) for human approval.
4. After approval, publish to the supplemental source (Sheet, file URL or Merchant API).
5. Journal entry tagged `change` for google-ads and meta-ads.

## 7. Platform specifics

### Shopify
- The Google and YouTube app syncs products to Merchant Center (primary source) and supports Google-specific fields through product metafields (custom labels, Google category, gender, age group, condition, MPN, custom product flag) [Practitioner consensus: confirm the namespace and keys in the store, often `mm-google-shopping`].
- Variant IDs in the app feed often look like `shopify_US_{productId}_{variantId}`. Pixels and other channels must use the same format, or you must map IDs.
- Barcode field on the variant is the GTIN source.
- Shopify product data also syndicates to AI channels through Shopify Catalog; fix data in Shopify, not only in a Google supplemental source.

### WooCommerce
- Google for WooCommerce (formerly Google Listings and Ads) syncs through the API; version 3.9.5 on 2026-09-29; recent releases moved product status refresh to paginated product list requests [Official, 2026-09].
- Variable products: confirm each variation syncs as its own item with `item_group_id`.
- Heavy transformations: use a feed plugin or feed tool reading WooCommerce and a supplemental Google source.

### Magento (Adobe Commerce) and custom platforms
- Use a feed extension or a feed tool; for custom builds, write a nightly full export (TSV) plus Merchant API inventory updates.
- After the Content API shutdown, any custom integration must use the Merchant API.

## 8. Change management for feed rules
- Every rule or supplemental change gets: ID, date, author, scope (SKUs affected), expected effect, rollback.
- Export rule configurations monthly to `ads-master/outputs/commerce-feeds/` (feed tools and Merchant Center attribute rules have weak version history).
- Stage changes: apply to a test feed label or a small set of SKUs first when possible.
- Peak-season freeze: no structural feed changes in the 2 weeks before major sale events unless fixing a disapproval.
