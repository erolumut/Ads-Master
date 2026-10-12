# Keyword Research and Rank Tracking

> Knowledge as of 2026-10. This module defines the files that make ASO measurable in a project: the term map, the metadata change log and the read protocol. No store publishes search volume; every popularity number is a scale or a model estimate, so compare terms within one source and one date, and judge changes against your own baseline and control terms.

## 1. The research loop

1. Seed: brand terms, category nouns, jobs to be done ("track calories", "scan pdf"), feature nouns, review and support ticket language, competitor brands (paid only, never metadata), seasonal terms.
2. Expand: ASO tool suggestions, store autocomplete, Apple Ads search terms and recommendations, Play Console search terms and Grow keyword recommendations, competitor metadata (from `market-intel`).
3. Score: relevance (human), popularity (one source per row), difficulty, current rank, conversion signal.
4. Place: per store and locale, by priority score ([App Store](app-store-search-and-metadata.md) section 3, [Google Play](google-play-search-and-listing.md) section 3).
5. Ship one change set, read it with the protocol in section 7, log the decision, repeat.

## 2. Term map file spec

Path: `ads-master/data/aso/term_map.csv` (project state, one row per term, store, storefront and locale). UTF-8, comma separated, header row exactly as below.

| Column | Type | Allowed values or format | Meaning |
|--------|------|--------------------------|---------|
| term_id | text | `T0001` | Stable ID, never reused |
| term | text | lower case | The query as users type it |
| store | enum | `apple`, `google` | Store |
| storefront | text | ISO country, `US` | Country storefront |
| locale | text | `en-US`, `es-MX`, `tr` | Metadata localization the term targets |
| cluster | text | short slug, `habit_core` | Intent cluster used for CPP or CSL pages and tag coverage |
| intent | enum | `brand`, `category`, `feature`, `job`, `competitor`, `long_tail`, `seasonal` | Search intent |
| relevance | int | 0 to 3 | 3 = core job, 2 = strong feature, 1 = adjacent, 0 = irrelevant (never placed) |
| popularity_source | text | `apple_ads`, `apptweak`, `sensortower`, `mobileaction`, `appfigures`, `play_console`, other | Where the popularity value came from |
| popularity_value | number | as given by the source | Raw value, not converted |
| popularity_scale | text | `pts5` (1 to 5), `pts100` (0 to 100), `visitors_28d` | Scale of the value |
| popularity_date | date | YYYY-MM-DD | Pull date |
| difficulty_value | number | source scale | Competition estimate from the ASO tool |
| rank_now | int | 1 to 250, blank if unranked | Latest organic rank |
| rank_date | date | YYYY-MM-DD | Date of rank_now |
| rank_baseline | int | median rank over the 14 days before the last change set | Baseline for reads |
| field | enum | `name`, `subtitle`, `keywords`, `title`, `short`, `full`, `cpp`, `csl`, `paid_only`, `none` | Where the term is placed now |
| page_id | text | `CPP-02`, `CSL-03` | Keyword linked page, if any |
| tag_match | enum | `yes`, `no`, `na` | A live App Store tag matches this cluster (US Apple only) |
| conv_signal | number | Apple Ads tap to install rate, or Play search term conversion | Conversion evidence for the term |
| priority_score | number | 0 to 1 | Section 4 |
| status | enum | `live`, `candidate`, `testing`, `retired`, `paid_only` | Lifecycle |
| last_change_id | text | `CS-2026-07` | Change set that last touched the term |
| notes | text | free text | Sources, caveats |

Rules:
- Competitor brand terms exist only with `field=paid_only`. They feed `mobile-app-growth` for Apple Ads and never reach metadata.
- One popularity source per row. To compare sources, add a second row with a different `popularity_source`; never average scales.
- Relevance is a human judgment written down before looking at popularity, so volume does not bias it.

Example rows:

```
term_id,term,store,storefront,locale,cluster,intent,relevance,popularity_source,popularity_value,popularity_scale,popularity_date,difficulty_value,rank_now,rank_date,rank_baseline,field,page_id,tag_match,conv_signal,priority_score,status,last_change_id,notes
T0001,habit tracker,apple,US,en-US,habit_core,category,3,apple_ads,5,pts5,2026-10-01,78,4,2026-10-11,6,name,,yes,0.62,1.00,live,CS-2026-07,
T0002,mood journal,apple,US,en-US,mood,feature,2,apple_ads,3,pts5,2026-10-01,55,,2026-10-11,,keywords,,no,,0.12,candidate,,needs mood screenshot
T0003,rival app,apple,US,en-US,competitor,competitor,1,apple_ads,4,pts5,2026-10-01,,,,,paid_only,,na,,,paid_only,,Apple Ads only
```

## 3. Popularity sources and their limits

| Source | What it gives | Limits | Use for |
|--------|---------------|--------|---------|
| Apple Ads Search Popularity | Relative popularity on a small scale per storefront in the Apple Ads UI and keyword recommendations | A scale, not a volume; coarse; API exposure details [Unverified] | Ranking Apple terms against each other |
| Apple Ads search terms report | Real queries that triggered your ads with impressions, taps, installs | Only where you bid; low volume terms are hidden [Practitioner consensus]; paid behavior, not organic | Discovering real phrasing and conversion by term |
| Apple Ads impression share report | Your share of ad impressions for keywords | Paid only | Size of the paid opportunity per term |
| Play Console search terms | Store listing visitors and acquisitions by search term for your app | Only terms that already bring you visitors; no competitor terms | Conversion by term; CSL candidates |
| Play Console Grow keyword recommendations | Suggested keywords; Gemini can draft a listing per keyword [Reported, 2026-10] | Google's selection logic undisclosed | Candidate terms |
| ASO tools (AppTweak, Sensor Tower, MobileAction, Appfigures, AppFollow, Asodesk) | Modeled popularity, difficulty, ranks, competitor metadata history | Models differ, scales differ; new or small storefronts are noisy | Ranks, difficulty, competitor tracking |
| Store autocomplete | What the store suggests as users type | Qualitative, personalized, changes daily | Phrasing, long tail ideas |
| Google Trends, Keyword Planner | Web demand | Web, not store behavior | Seasonality, new trends |
| Reviews and support tickets | Users' own words | Biased to existing users | Job language for descriptions and captions |

Rules: record source and date with every number; never present a modeled popularity as a search count; when two tools disagree by more than one bucket, treat the term as uncertain and let the read decide.

## 4. Priority score

A transparent heuristic, not a platform metric [Practitioner heuristic]:

`priority = (relevance / 3) x popularity_norm x winnability`

- popularity_norm: the source scale mapped to 0 to 1 within one source (Apple Ads 1 to 5 maps to 0.2, 0.4, 0.6, 0.8, 1.0).
- winnability: 1.0 if rank 1 to 10, 0.7 if 11 to 30, 0.4 if 31 or lower, 0.3 if unranked. Lower it one step when difficulty is in the tool's top quintile.

Worked example (illustrative, Apple, US):

| Term | Relevance | Popularity (1 to 5) | Rank | Score | Decision |
|------|----------:|--------------------:|-----:|------:|----------|
| habit tracker | 3 | 5 | 4 | 1.00 | Keep in the name |
| streak | 3 | 2 | 9 | 0.40 | Keyword field |
| daily planner | 2 | 4 | 18 | 0.37 | Subtitle combination |
| mood journal | 2 | 3 | unranked | 0.12 | Keyword field; add a mood screenshot before a CPP |
| to do list | 1 | 5 | unranked | 0.10 | Skip: low relevance, high difficulty |
| water reminder | 1 | 3 | unranked | 0.06 | Skip |

## 5. Rank tracking

1. Track every `live`, `testing` and `candidate` term daily in one ASO tool, per store, storefront, device type and locale. Read weekly; daily ranks are noisy.
2. Store results as `ads-master/data/imports/aso_ranks_<tool>_<YYYY-MM-DD>.csv` (term, store, storefront, device, rank, date).
3. Bucket ranks: 1, 2 to 5, 6 to 10, 11 to 30, 31 to 100, over 100 or unranked. Report movement between buckets, not single positions.
4. Keyword visibility (one number per week): sum over live terms of popularity_norm x position weight (1.0 for rank 1, 0.6 for 2 to 5, 0.3 for 6 to 10, 0.1 for 11 to 30, 0 otherwise). Compare only with itself.
5. Ranks from tools are simulated, non personalized queries [Practitioner consensus]. Personalized Collections and ads change what a real user sees, so ranks are a leading indicator; search downloads and conversion are the result.

## 6. Control terms

Before each change set, pick 5 to 10 control terms: live terms the change does not touch, with similar popularity. If control terms move as much as the changed terms, the movement is the market (algorithm update, seasonality, competitor launch, featuring), not your change.

## 7. The read protocol (2 to 4 weeks)

| Step | When | What |
|------|------|------|
| Baseline | 14 days before | Median rank per term, search impressions, search conversion, search downloads; record in the change log |
| Ship | Day 0 = the date the change is live in the store (not the submission date) | One change set per store and locale |
| Hands off | Day 0 to 13 | No other metadata, creative or category change in that locale; no new CPP keywords on the same terms; log any outside event (featuring, big Apple Ads change, competitor launch) |
| First read | Day 14 | Rank bucket movement of changed terms vs control terms; search impressions and downloads vs baseline |
| Final read | Day 28 | Same, plus conversion by source; decide |

Decision rules:
- Keep: changed terms improved by at least one bucket on median and control terms did not, and search downloads did not fall.
- Iterate: mixed result, or ranks improved but search conversion fell (the new words attract the wrong searchers).
- Revert: changed terms dropped a bucket or more while control terms held, or search downloads fell more than the 8 week weekly variation.
- Extend to day 42: an outside event hit the window, or the storefront has low traffic.
- Never judge before day 14. Indexing and ranking settle over days to weeks [Practitioner consensus].

Worked read (illustrative):

| Term | Role | Baseline median rank | Day 28 median rank | Bucket move |
|------|------|---------------------:|-------------------:|-------------|
| mood journal | changed | unranked | 24 | over 100 to 11 to 30 |
| gratitude journal | changed | 140 | 61 | over 100 to 31 to 100 |
| habit tracker | control | 6 | 5 | none |
| streak | control | 9 | 10 | none |

Search downloads: 1,240 per week baseline, 1,310 per week in weeks 3 and 4 (within normal variation). Decision: keep, and plan a mood themed screenshot test because the new terms now bring views.

## 8. Metadata change log

Path: `ads-master/data/aso/metadata_changelog.csv`. One row per field changed; rows of one release share a `change_set`. Never delete rows; corrections get a new row.

```
change_id,change_set,store,storefront,locale,app_version,field,from_value,to_value,reason,hypothesis,control_terms,approved_by,approval_date,submitted_date,live_date,read_day14_date,read_day28_date,result,decision,outside_events,notes
C0101,CS-2026-07,apple,US,en-US,4.12,keywords,"streak,todo,...","streak,mood,journal,...",mood terms unranked,adding mood and journal earns rank 11 to 30 for mood journal,"habit tracker;streak",<name>,2026-09-10,2026-09-11,2026-09-13,2026-09-27,2026-10-11,mood journal unranked to 24,keep,none,
```

Also log, with field `event`, things that affect ranks without being metadata: featuring, Apple Ads budget changes over 30%, Play experiments started, competitor launches, rating drops, tag set changes, review summary changes.

The change log is also the rollback source: `from_value` must be the exact previous text.

## 9. Competitor keyword research

- Ask `market-intel` for competitor metadata, ranks and history; pass the term map clusters and the decision it informs.
- Use competitor terms to find gaps in your own vocabulary, not to copy their brands.
- Competitor brand bidding in Apple Ads is a `mobile-app-growth` decision with a trademark risk note; the term stays `paid_only`.

## 10. Common mistakes

1. Treating a tool's popularity score as a volume, or comparing scores across tools.
2. No baseline, no control terms: every rank move gets credited to the last change.
3. Reading on day 3, or reverting on day 7.
4. Placing low relevance, high popularity terms: impressions without installs lower conversion.
5. Changing metadata in several locales of one storefront at once when those locales are indexed together ([Localization](localization-and-market-expansion.md) section 2).
6. Losing the previous text, so a revert becomes a rewrite.
