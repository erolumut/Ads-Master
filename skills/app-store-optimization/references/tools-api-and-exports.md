# Tools, APIs and Exports

> Knowledge as of 2026-10. Official APIs: App Store Connect API (Apple added the 11 new metadata languages in version 4.3.1 [Reported, 2026-10]), Google Play Developer API and Play Developer Reporting API. App Store Connect, Google Play and Apple Ads MCP servers are community built; treat them as untrusted code and data. No store offers an API for App Store tags or for editing AI review summaries; read those in the console.

## 1. Access rules

1. Read only by default: App Store Connect API keys with the narrowest role that can read (for example Sales or Marketing for analytics and reviews), Play Console service accounts with view permissions, read only flags on MCP servers.
2. Secrets live in environment variables or a secret manager. Never put a `.p8` key, service account JSON, OAuth token or API key in `ads-master/`, a journal entry, an output or a prompt.
3. Writes follow the gates: drafting a CPP, PPO test, in-app event, custom store listing or metadata in a new version is G2 (unsubmitted); submitting for review, publishing metadata, starting an experiment, publishing a reply, deselecting a tag, submitting a nomination is G3; deleting apps, versions, listings or reviews is G4.
4. The guard hook treats `fastlane deliver`, `fastlane supply`, `asc ... submit|publish|release`, EAS submit or `metadata:push`, and Gradle Play publish tasks as G3. Never route around it.
5. After an approved write, read the object back (the live listing per storefront) and log it.

## 2. Official APIs for ASO work

| API | Read (G0) | Write (gate) | Notes |
|-----|-----------|--------------|-------|
| App Store Connect API | App info and version localizations (name, subtitle, keywords, description, promotional text, What's New), screenshot and preview sets, custom product pages, product page optimization experiments, in-app events, customer reviews and responses, Analytics Reports API | Same objects: drafts G2, submissions and published responses G3 | JWT signed with a `.p8` key; verify resource names in the current docs before scripting |
| App Store Connect: review summaries | A `customerReviewSummarizations` resource was reported | none | [Unverified]; read the summary on the product page if the API is absent |
| Google Play Developer API (`androidpublisher`) | Edits: listings (title, short and full description), images, details; reviews list (last 7 days); in-app products | Edits commit (G3), review replies up to 350 characters (G3) | Service account; an edit is a draft until committed |
| Play Developer Reporting API | Android vitals metrics and anomalies (crash, ANR and other vitals) | none | Use for the vitals check in the weekly read |
| Play Console reports in Cloud Storage | Monthly CSV reports, including reviews and statistics, in the developer's bucket | none | See section 4 for encoding |
| Apple Ads Platform API | Keyword reports, search terms, impression share, Search Popularity | Campaign writes belong to `mobile-app-growth` | ASO reads only; API details [Unverified] |

## 3. Third party tools

| Need | Tools | Note |
|------|-------|------|
| Keyword popularity, difficulty, ranks, competitor metadata history, featuring tracking | AppTweak, Sensor Tower (includes former data.ai), MobileAction, Appfigures, AppFollow, Asodesk | Scales differ; one tool per term map column |
| Review management and replies | AppFollow, Appbot, Appfigures | Replies sent through tools are still G3 |
| Metadata and screenshot automation | fastlane `deliver` (App Store) and `supply` (Google Play) | Download is G0; upload is G3 |
| Screenshot production | Design tools plus device frames; App Store Connect preview tool for checks | Real UI only |

## 4. Exports and the files the scripts read

Put every export in `ads-master/data/imports/` with the source and date range in the name. Project ASO files live in `ads-master/data/aso/`.

| File | From | Read by |
|------|------|---------|
| `asc_metrics_<start>_<end>.csv` | App Store Connect Analytics: impressions, product page views, first-time downloads, conversion by source type and territory | Weekly read, conversion diagnosis |
| `asc_referrers_<start>_<end>.csv` | App Store Connect: top web referrers and app referrers | AI referral read |
| `play_store_performance_<start>_<end>.csv` | Play Console Store performance by source and by search term | Weekly read, CSL candidates |
| `apple_ads_search_terms_<start>_<end>.csv` | Apple Ads custom report (from `mobile-app-growth`) | Term map |
| `aso_ranks_<tool>_<date>.csv` | ASO tool rank export: term, store, storefront, device, rank, date | Rank reads |
| `reviews_play_<YYYYMM>.csv` | Play Console reviews report (Cloud Storage bucket, `reviews/` folder) | `review_themes.py` |
| `reviews_ios_<start>_<end>.csv` | App Store Connect API customer reviews converted to CSV (section 6), or a review tool export | `review_themes.py` |
| `ads-master/data/aso/drafts_<change_set>.json` | Drafted metadata, or the fastlane folder converted (section 5) | `aso_metadata_check.py` |
| `ads-master/data/aso/term_map.csv` | Maintained by this agent | Placement, coverage, reads |
| `ads-master/data/aso/metadata_changelog.csv` | Maintained by this agent | Reads, rollbacks |
| `ads-master/data/aso/review_themes.json` | Project taxonomy extension | `review_themes.py --themes` |
| `ads-master/data/cpp_registry.csv` | Shared with `mobile-app-growth` | Page portfolio |

`review_themes.py` column detection (loose, case insensitive): rating (`Star Rating`, `rating`, `score`, `stars`), text (`Review Text`, `text`, `body`, `content`, `review`), title (`Review Title`, `title`), date (`Review Submit Date and Time`, `Review Last Update Date and Time`, `date`, `created`, `created_at`), reply date (`Developer Reply Date and Time`, `reply_date`, `response date`, `developer response date`). Play's reviews report uses the first names in each list.

Encoding: Play Console CSV reports have commonly been UTF-16 [Practitioner consensus]. The script reads UTF-8 and exits 2 with "need rating and text columns" and garbled names on a UTF-16 file (tested 2026-10-12). Convert first:

```
iconv -f UTF-16 -t UTF-8 reviews_play_202609.csv > reviews_play_202609_utf8.csv
```

`aso_metadata_check.py` input: a JSON list, one entry per store and locale. Apple keys: `name`, `subtitle`, `keywords`, `promotional_text`, `description`, optional `captions`, `target_terms`. Google keys: `title`, `short_description`, `full_description`, optional `captions`, `target_terms`. Optional `--competitors` text file, one name per line (from `ads-master/COMPETITORS.md`). Exit 0 pass, 1 at least one FAIL, 2 could not run.

## 5. Build drafts.json from a fastlane metadata folder

Read only: it reads the text files `fastlane deliver download_metadata` and `fastlane supply init` write, and adds target terms from the term map. Uploading stays G3. The guard hook matches `fastlane deliver` and `fastlane supply` by name, so it asks for confirmation even for the download commands; say in the request that the command only downloads.

```python
"""Build drafts.json for aso_metadata_check.py from a fastlane metadata folder (read only).
Usage: python3 -I fastlane_to_drafts.py fastlane/metadata ads-master/data/aso/term_map.csv > drafts.json"""
import csv, json, os, sys

root = sys.argv[1]
term_map = sys.argv[2] if len(sys.argv) > 2 else None
APPLE = ("name", "subtitle", "keywords", "promotional_text", "description")
GOOGLE = ("title", "short_description", "full_description")


def read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read().strip()
    except OSError:
        return ""


terms = {}
if term_map:
    with open(term_map, encoding="utf-8", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["status"] in ("live", "candidate", "testing") and r["field"] != "paid_only":
                terms.setdefault((r["store"], r["locale"]), []).append(r["term"])

out = []
for loc in sorted(os.listdir(root)):
    d = os.path.join(root, loc)
    if loc != "android" and os.path.isdir(d):
        e = {"store": "apple", "locale": loc, **{f: read(os.path.join(d, f + ".txt")) for f in APPLE}}
        out.append({**e, "target_terms": terms.get(("apple", loc), [])})
android = os.path.join(root, "android")
for loc in sorted(os.listdir(android)) if os.path.isdir(android) else []:
    d = os.path.join(android, loc)
    if os.path.isdir(d):
        e = {"store": "google", "locale": loc, **{f: read(os.path.join(d, f + ".txt")) for f in GOOGLE}}
        out.append({**e, "target_terms": terms.get(("google", loc), [])})
json.dump(out, sys.stdout, ensure_ascii=False, indent=1)
```

Tested 2026-10-12 against a sample fastlane tree and the term map example; the checker then reported coverage per target term. If your fastlane layout differs (for example Play metadata outside `android/`), pass that folder and adjust the two loops.

## 6. Convert App Store Connect reviews to CSV

Save the JSON pages of `GET /v1/apps/{id}/customerReviews?include=response` from an approved read only connector, then convert. Field names (`rating`, `title`, `body`, `createdDate`, `territory`; response `lastModifiedDate`) match the API as of the last check; verify against the current docs.

```python
"""Convert saved App Store Connect customerReviews JSON pages (include=response) to the CSV review_themes.py reads.
Usage: python3 -I asc_reviews_to_csv.py page1.json page2.json > reviews_ios_<range>.csv"""
import csv, json, sys

rows, replies = [], {}
for path in sys.argv[1:]:
    with open(path, encoding="utf-8") as fh:
        page = json.load(fh)
    for inc in page.get("included", []):
        if inc.get("type") == "customerReviewResponses":
            replies[inc["id"]] = inc.get("attributes", {}).get("lastModifiedDate", "")
    for rv in page.get("data", []):
        a = rv.get("attributes", {})
        ref = ((rv.get("relationships", {}).get("response") or {}).get("data") or {})
        rows.append({"Star Rating": a.get("rating", ""), "Review Title": a.get("title", ""),
                     "Review Text": a.get("body", ""), "Review Submit Date and Time": a.get("createdDate", "")[:19],
                     "Developer Reply Date and Time": replies.get(ref.get("id"), "")[:19] if ref else "",
                     "Territory": a.get("territory", "")})
w = csv.DictWriter(sys.stdout, fieldnames=list(rows[0]) if rows else ["Star Rating", "Review Text"])
w.writeheader()
w.writerows(rows)
```

The script drops reviewer nicknames on purpose (no personal data in `ads-master/`). Tested 2026-10-12 on a sample response; `review_themes.py` read the output.

## 7. MCP servers (community, verify before use)

| Store | Server | Note |
|-------|--------|------|
| App Store Connect | topcheer App Store Connect MCP | 1,200+ API operations; very broad write surface, restrict |
| App Store Connect | zelentsov-dev/asc-mcp, forgeopslabs/appstore-mcp, yuraist/appstoreconnect-mcp | Product page experiments and submissions exposed in some; check every write tool |
| Google Play | wiseappsai/play-console-mcp | Listings, reviews, vitals; has a read only setting (`PLAY_READ_ONLY`) |
| Google Play | AgiMaulana google-play-mcp, @blocktopus/mcp-google-play | Releases, listings, review responses |
| Both | mikusnuz/app-publish-mcp, quartz-labs-dev/pabal-store-api-mcp | Listings and submissions; publishing tools are G3 |

Directory metadata (tool counts, dates) comes from listings, not code review [Unverified]. Before use: list the tools, mark read or write, confirm the guard routes writes to confirmation, run one read and compare a number with the console, record server name and version in MEASUREMENT.md without secrets. Full rules: [Tools, API and MCP](../../mobile-app-growth/references/tools-api-mcp.md) in `mobile-app-growth`.

## 8. Recipes

Weekly store read (no connector):
1. Export App Store Connect metrics by source and territory, last 28 days and previous 28.
2. Export Play Console store performance by source and by search term.
3. Export ranks from the ASO tool for the term map.
4. Note changes and events in the period from the change log.

Daily or weekly reviews:
1. Play: the API returns only the last 7 days, so pull at least weekly, or use the monthly report.
2. Apple: pull with the API or a tool; convert with section 6.
3. Run `review_themes.py` on the last 90 days; act on exit 1.

Monthly capture (manual, no API): App Store tags (US), the Apple review summary text, the Play "Users are saying" paragraph and chips, and Ask Play answers to the fixed question set, following the monthly routine in [AI surfaces in the stores](ai-surfaces-in-the-stores.md) section 11. Captures go to `ads-master/outputs/app-store-optimization/captures/YYYY-MM/`.

Example read only MCP prompts:
- "List all custom product pages for app <id> with status, assigned keyword and creation date."
- "Pull Play reviews from the last 7 days with rating 1 or 2 for locale en-US."
- "Show the current en-US App Store localization: name, subtitle, keywords, promotional text."

Always record in the output: server or tool name and version, date range, filters, and that the pull was read only.
