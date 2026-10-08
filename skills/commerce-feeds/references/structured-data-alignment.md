# Structured Data Alignment: PDP, Product and Offer schema, and the feed

> Merchant Center crawls landing pages to verify price and availability. AI agents (Google, OpenAI, Microsoft, Perplexity, Amazon) read the PDP directly. If the page, the JSON-LD and the feed disagree, you get disapprovals, automatic overrides you did not choose, and wrong answers in AI assistants. Knowledge as of 2026-10.

## 1. Principles
1. One source of truth: the commerce platform's product and offer data generates the PDP, the JSON-LD and the feed. Never hand-maintain any of the three.
2. Server-render price, availability and JSON-LD in the initial HTML. Client-only rendering risks crawlers missing it.
3. The URL in `link` must land on the exact variant with that variant's price and availability visible and in JSON-LD.
4. Use the same currency and tax treatment as the feed for the target country. Geo-IP currency switching must not change what Googlebot sees for the feed's country.
5. Keep automatic item updates on in Merchant Center as a safety net, and track how often it fires (frequent updates mean the feed is stale).

## 2. Feed attribute to schema.org mapping

| Feed attribute | schema.org property | Notes |
|----------------|---------------------|-------|
| `id` | `sku` (Product) | Same value as the feed ID |
| `title` | `name` | May differ in wording; must describe the same item |
| `description` | `description` | |
| `link` | `url` (Product or Offer) | Canonical variant URL |
| `image_link` | `image` | Same main image preferred |
| `price` | `offers.price` + `offers.priceCurrency` | Numeric, dot decimal, no currency symbol |
| `sale_price` | `offers.price` (current) plus `priceSpecification` with `priceType` `https://schema.org/StrikethroughPrice` for the original | Show the current price as `price` |
| `availability` | `offers.availability` (`https://schema.org/InStock`, `OutOfStock`, `PreOrder`, `BackOrder`) | |
| `condition` | `offers.itemCondition` (`NewCondition`, `RefurbishedCondition`, `UsedCondition`) | |
| `brand` | `brand` (`Brand` with `name`) | |
| `gtin` | `gtin` (or `gtin8`, `gtin12`, `gtin13`, `gtin14`) | Digits only |
| `mpn` | `mpn` | |
| `item_group_id` | `ProductGroup.productGroupID`, variants via `hasVariant`, `variesBy` | |
| `color`, `size`, `material`, `pattern` | `color`, `size`, `material`, `pattern` | `size` and `pattern` on Product since schema.org 28/29 era |
| `shipping` | `offers.shippingDetails` (`OfferShippingDetails`) or organization-level `hasShippingService` | |
| return policy | `offers.hasMerchantReturnPolicy` or organization-level `hasMerchantReturnPolicy` | |
| `loyalty_program` member price | `UnitPriceSpecification` with `validForMemberTier`; organization `hasMemberProgram` | schema.org 28.0 (2024-09-17) added MemberProgram |
| `unit_pricing_measure` | `priceSpecification.referenceQuantity` | |
| reviews | `aggregateRating`, `review` | Only first-party reviews you actually display |
| `certification` | `hasCertification` (Certification) | |
| `popularity_rank` (feed) | `itemPopularity` (Offer) | Added in schema.org 30.1 (2026-09-16); Google support not confirmed [Unverified] |
| `related_products` often bought with | `isOftenBoughtWith` (Product) | schema.org 30.1; support Unverified |
| consumer notices (Prop 65 and similar) | `consumerNotice` (Product) | schema.org 30.1; support Unverified |
| `minimum_order_value` | `minimumOrderValue` (ShippingRateSettings) | schema.org 30.1 |

schema.org release history relevant here [Official]:
- 28.0 (2024-09-17): loyalty programs: `MemberProgram`, `MemberProgramTier`, `hasMemberProgram`, `validForMemberTier`.
- 29.0 (2025-03-24): shipping: `ShippingService`, `ShippingConditions`, `hasShippingService` (Organization and OfferShippingDetails), `fulfillmentType`, `ServicePeriod` with `cutoffTime` and `businessDays`; deprecated `DeliveryTimeSettings`, `shippingSettingsLink`, `shippingLabel`, `transitTimeLabel`.
- 30.1 (2026-09-16): retail feed vocabulary (`consumerNotice`, `isOftenBoughtWith`, `specification`, `itemPopularity`, `minimumOrderValue`, `MaximumRetailPrice`) and EU Digital Product Passport (`DigitalProductPassport`, `hasDigitalProductPassport`, `importer`, `recycledContentPercentage`, `substanceOfConcern`, `authorizedRepresentative`).

Google Search supports a subset. Check Google's Product (merchant listing) structured data documentation before relying on any new property [Freshness check].

## 3. JSON-LD templates

### 3.1 Single product with offer, shipping and returns
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "sku": "SKU-MC-NAVY-M",
  "name": "Acme Women's Merino Crew Neck Sweater, Navy, M",
  "description": "Midweight 100 percent merino wool crew neck. Machine washable at 30 C.",
  "image": ["https://cdn.example.com/merino-crew-navy-1200.jpg"],
  "brand": {"@type": "Brand", "name": "Acme"},
  "gtin": "00012345600012",
  "color": "Navy",
  "size": "M",
  "material": "Merino wool",
  "offers": {
    "@type": "Offer",
    "url": "https://www.example.com/products/merino-crew?variant=SKU-MC-NAVY-M",
    "price": "89.00",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingRate": {"@type": "MonetaryAmount", "value": "0", "currency": "USD"},
      "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "US"},
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "handlingTime": {"@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY"},
        "transitTime": {"@type": "QuantitativeValue", "minValue": 2, "maxValue": 5, "unitCode": "DAY"}
      }
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": "US",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 30,
      "returnMethod": "https://schema.org/ReturnByMail",
      "returnFees": "https://schema.org/FreeReturn"
    }
  },
  "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": "128"}
}
```
Only include `aggregateRating` when the reviews are visible on the page. The `deliveryTime` structure follows the long-standing Google example; schema.org 29.0 moved the newer shipping model to `ShippingConditions` and `ShippingService`, so check which form Google documents today.

### 3.2 Variants with ProductGroup
```json
{
  "@context": "https://schema.org",
  "@type": "ProductGroup",
  "name": "Acme Women's Merino Crew Neck Sweater",
  "productGroupID": "MC",
  "brand": {"@type": "Brand", "name": "Acme"},
  "variesBy": ["https://schema.org/color", "https://schema.org/size"],
  "hasVariant": [
    {"@type": "Product", "sku": "SKU-MC-NAVY-M", "gtin": "00012345600012", "color": "Navy", "size": "M",
     "image": "https://cdn.example.com/merino-crew-navy-1200.jpg",
     "offers": {"@type": "Offer", "url": "https://www.example.com/products/merino-crew?variant=SKU-MC-NAVY-M",
                "price": "89.00", "priceCurrency": "USD", "availability": "https://schema.org/InStock"}},
    {"@type": "Product", "sku": "SKU-MC-OAT-M", "gtin": "00012345600029", "color": "Oatmeal", "size": "M",
     "image": "https://cdn.example.com/merino-crew-oat-1200.jpg",
     "offers": {"@type": "Offer", "url": "https://www.example.com/products/merino-crew?variant=SKU-MC-OAT-M",
                "price": "89.00", "priceCurrency": "USD", "availability": "https://schema.org/OutOfStock"}}
  ]
}
```
`productGroupID` should equal the feed `item_group_id`. Each variant `sku` equals the feed `id`.

### 3.3 Member price (loyalty)
```json
"offers": {
  "@type": "Offer",
  "price": "89.00",
  "priceCurrency": "USD",
  "priceSpecification": [
    {"@type": "UnitPriceSpecification", "price": "89.00", "priceCurrency": "USD"},
    {"@type": "UnitPriceSpecification", "price": "79.00", "priceCurrency": "USD",
     "validForMemberTier": {"@id": "https://www.example.com/#member-gold"}}
  ]
}
```
Declare the program once on the Organization with `hasMemberProgram` and tiers with `@id` values. Mirror it in Merchant Center loyalty settings and the `loyalty_program` feed attribute.

### 3.4 Organization-level policies (site-wide)
Put return policy, shipping service and member program on the `Organization` (or `OnlineStore`) markup on the home or about page, and override per offer only for exceptions. This reduces per-page markup and mismatch risk.

## 4. Platform implementation notes

| Platform | How JSON-LD is produced | Watch out for |
|----------|------------------------|---------------|
| Shopify | Theme (Liquid) outputs Product JSON-LD; many themes and apps add a second copy | Duplicate or conflicting blocks (theme plus SEO app plus reviews app). Keep one. Variant selection via `?variant=` must update price and availability server side. |
| WooCommerce | WooCommerce core outputs Product structured data; SEO plugins extend it | Variable products: ensure each variant URL renders its own price; cached pages with stale stock |
| Magento (Adobe Commerce) | Theme or extension | Full page cache serving old prices; configurable products default to the parent price |
| Headless (Next.js, Hydrogen, custom) | Component renders JSON-LD | Render on the server (SSR or static with revalidation), not after hydration |
| BigCommerce, Salesforce Commerce Cloud | Theme or cartridge | Same duplicate and cache issues |

Shopify Liquid sketch (one block per page, variant aware):
```liquid
{%- assign v = product.selected_or_first_available_variant -%}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "sku": {{ v.sku | json }},
  "name": {{ product.title | append: ' ' | append: v.title | json }},
  "image": {{ v.featured_image | default: product.featured_image | image_url: width: 1200 | prepend: 'https:' | json }},
  "brand": {"@type": "Brand", "name": {{ product.vendor | json }}},
  {%- if v.barcode != blank -%}"gtin": {{ v.barcode | json }},{%- endif -%}
  "offers": {
    "@type": "Offer",
    "url": {{ shop.url | append: v.url | json }},
    "price": {{ v.price | divided_by: 100.0 | json }},
    "priceCurrency": {{ cart.currency.iso_code | json }},
    "availability": "https://schema.org/{% if v.available %}InStock{% else %}OutOfStock{% endif %}"
  }
}
</script>
```
Adapt to the theme; test with the PDP parity script and Google's Rich Results Test. If the Google and YouTube app feed uses a different ID format than `v.sku`, align the `sku` property to the feed `id` or accept that parity checks must map IDs.

## 5. Parity testing procedure
1. Export the feed (or pull processed products from the Merchant API).
2. Sample 100 to 200 items stratified by revenue (all top 50 revenue SKUs plus a random sample).
3. Run `pdp_parity.py` (section 8): fetches each `link`, extracts JSON-LD, compares price, currency, availability and GTIN.
4. For mismatches, open the page as Googlebot would (no cookies, target country IP, no consent click) and check visible price and stock.
5. Classify the root cause (table below) and fix at the source.
6. Re-run after fixes; record the mismatch rate in the journal.

Targets: under 1 percent mismatch on price and availability for the sample; zero on top revenue SKUs.

## 6. Mismatch root causes

| Symptom | Root cause | Fix |
|---------|-----------|-----|
| Page price differs from feed in some countries | Geo-IP currency or price localization | Feed per country with matching currency and price; give crawlers the country version requested by URL or feed label; do not auto-redirect bots |
| Price differs during sales | Sale scheduled on site but not in feed (or the reverse) | `sale_price_effective_date` matching the site schedule; feed refresh at sale start |
| Stock differs | Feed refreshed daily, stock moves hourly | API or hourly inventory updates for fast movers |
| Variant price wrong | URL lands on default variant | Variant URL parameter that preselects variant server side |
| JSON-LD missing | Client-side rendering, bot protection | Server render; allowlist crawlers |
| Two Product blocks with different prices | Theme plus app duplicates | Remove duplicates |
| Tax-inclusive versus exclusive confusion | US feeds exclude tax; EU feeds include VAT | Follow the country rule consistently on page and feed |
| Member price shown as main price | Loyalty price leaks into `price` | Regular price in `price`, member price via `validForMemberTier` |
| Cookie or consent wall blocks crawler | Interstitial | Allow content behind banners to render |

## 7. Merchant Center signals to watch
- Item issues "Mismatched value (page crawl) [price]" and "[availability]".
- Automatic item updates activity (if visible): frequent updates mean the feed is stale.
- Account-level warnings for price accuracy: fix within the warning window to avoid suspension.

## 8. Parity script (`pdp_parity.py`)

Tested on 2026-10-08 against sample ProductGroup markup. Standard library only. Save as `ads-master/scripts/pdp_parity.py` in the project (or run from the scratch area), never inside a downloaded data folder.

```python
#!/usr/bin/env python3
"""pdp_parity.py: compare feed price, availability and GTIN with PDP JSON-LD.

Usage:
  python3 pdp_parity.py feed.tsv --sample 200 > parity.md
  python3 pdp_parity.py feed.tsv --ids SKU1,SKU2
  python3 pdp_parity.py --html saved_page.html --id SKU1 --price "49.00 USD"

Reads only public pages, sequentially, with a delay. Does not execute
JavaScript: if a PDP renders JSON-LD client side, the script reports
"no_jsonld" (that is itself a finding: Google and AI agents may miss it).
"""
import csv
import json
import random
import re
import sys
import time
import argparse
import urllib.request

UA = "Mozilla/5.0 (compatible; feed-parity-check/1.0)"
LD_RE = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)
AVAIL_MAP = {"instock": "in_stock", "outofstock": "out_of_stock", "preorder": "preorder",
             "backorder": "backorder", "soldout": "out_of_stock", "discontinued": "out_of_stock",
             "limitedavailability": "in_stock", "onlineonly": "in_stock", "instoreonly": "out_of_stock"}


def walk(node):
    if isinstance(node, list):
        for n in node:
            yield from walk(n)
    elif isinstance(node, dict):
        yield node
        for v in node.values():
            if isinstance(v, (list, dict)):
                yield from walk(v)


def offers_from_html(html):
    """Return list of dicts: sku, gtin, price, currency, availability, url."""
    found = []
    for block in LD_RE.findall(html):
        try:
            data = json.loads(block.strip())
        except json.JSONDecodeError:
            found.append({"error": "invalid_json"})
            continue
        for node in walk(data):
            t = node.get("@type")
            types = t if isinstance(t, list) else [t]
            if "Product" not in types:
                continue
            offers = node.get("offers") or []
            if isinstance(offers, dict):
                offers = [offers]
            for o in offers:
                if o.get("@type") == "AggregateOffer":
                    price = o.get("lowPrice")
                else:
                    price = o.get("price")
                    if price is None and isinstance(o.get("priceSpecification"), dict):
                        price = o["priceSpecification"].get("price")
                avail = str(o.get("availability", "")).rsplit("/", 1)[-1].lower()
                found.append({
                    "sku": str(node.get("sku") or o.get("sku") or ""),
                    "gtin": str(node.get("gtin") or node.get("gtin13") or node.get("gtin12") or node.get("gtin14") or node.get("gtin8") or ""),
                    "price": str(price) if price is not None else "",
                    "currency": str(o.get("priceCurrency") or ""),
                    "availability": AVAIL_MAP.get(avail, avail),
                })
    return found


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read().decode("utf-8", "ignore")


def compare(row, offers):
    if not offers:
        return ["no_jsonld"]
    if any("error" in o for o in offers) and len(offers) == 1:
        return ["invalid_jsonld"]
    pid = row.get("id", "")
    cand = [o for o in offers if o.get("sku") in (pid, row.get("mpn", ""))] or offers
    o = cand[0]
    problems = []
    fp = row.get("sale_price") or row.get("price") or ""
    parts = fp.split()
    if len(parts) == 2:
        try:
            if abs(float(parts[0])-float(o["price"] or "nan")) > 0.009:
                problems.append("price feed=%s page=%s" % (parts[0], o["price"]))
        except ValueError:
            problems.append("price_unparseable page=%s" % o["price"])
        if o["currency"] and o["currency"] != parts[1]:
            problems.append("currency feed=%s page=%s" % (parts[1], o["currency"]))
    fa = (row.get("availability") or "").replace(" ", "_").lower()
    if o["availability"] and fa and o["availability"] != fa:
        problems.append("availability feed=%s page=%s" % (fa, o["availability"]))
    fg = re.sub(r"\D", "", row.get("gtin", ""))
    pg = re.sub(r"\D", "", o["gtin"])
    if fg and pg and fg.zfill(14) != pg.zfill(14):
        problems.append("gtin feed=%s page=%s" % (fg, pg))
    if fg and not pg:
        problems.append("gtin_missing_on_page")
    return problems or ["ok"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("feed", nargs="?")
    ap.add_argument("--sample", type=int, default=100)
    ap.add_argument("--ids", default="")
    ap.add_argument("--delay", type=float, default=1.5)
    ap.add_argument("--html")
    ap.add_argument("--id", default="")
    ap.add_argument("--price", default="")
    args = ap.parse_args()

    if args.html:
        offers = offers_from_html(open(args.html, encoding="utf-8").read())
        print(json.dumps(offers, indent=2))
        print(compare({"id": args.id, "price": args.price}, offers))
        return

    with open(args.feed, newline="", encoding="utf-8-sig") as fh:
        delim = "\t" if fh.readline().count("\t") else ","
        fh.seek(0)
        rows = [{(k or "").lower(): (v or "") for k, v in r.items()} for r in csv.DictReader(fh, delimiter=delim)]
    if args.ids:
        wanted = set(args.ids.split(","))
        rows = [r for r in rows if r.get("id") in wanted]
    else:
        random.seed(7)
        rows = random.sample(rows, min(args.sample, len(rows)))
    print("| id | link | result |\n|---|---|---|")
    bad = 0
    for r in rows:
        try:
            res = compare(r, offers_from_html(fetch(r["link"])))
        except Exception as e:  # network errors are findings too
            res = ["fetch_error " + type(e).__name__]
        if res != ["ok"]:
            bad += 1
        print("| %s | %s | %s |" % (r.get("id"), r.get("link"), "; ".join(res)))
        time.sleep(args.delay)
    print("\nMismatch or error rate: %d of %d (%.1f%%)" % (bad, len(rows), 100.0 * bad / max(1, len(rows))))


if __name__ == "__main__":
    main()
```

Limits: no JavaScript rendering; one request per item with a delay; respects nothing beyond the delay, so keep samples small and get approval before crawling a production site at volume.

## Handoffs
| Situation | Hand off to | Pass |
|-----------|------------|------|
| Template or theme changes needed | seo (owns technical SEO and structured data in code) | Template file, fields, test results |
| Page speed or variant UX fixes | cro | URLs, issue |
| Robots or bot manager blocks crawlers | seo and ai-search-optimization | Blocked agents, evidence |
