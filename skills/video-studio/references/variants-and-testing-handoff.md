# Variants and Testing Handoff

> Purpose: produce variants that answer one question at a time, name them so every result maps back to a hook, body and CTA, register them in `ads-master/creative-library/registry.csv`, hand them to the channel agents for PAUSED upload, and read the results back into the next batch.

## 1. Who does what

| Step | Owner |
|------|-------|
| Hypothesis, test design, cell budget, stop rule, winner rules | `creative-strategy` (rows in `EXPERIMENTS.md`) |
| Variant matrix, production, naming, QA, registry rows, upload manifest | `video-studio` |
| Upload as PAUSED, read back creative IDs, launch after human approval, delivery and spend | `meta-ads`, `tiktok-ads`, `google-ads`, `linkedin-ads` (and `mobile-app-growth` for app campaigns) |
| Claims and disclosure sign-off | `compliance` |
| Performance read by second and by variant, next iteration brief | `video-studio` (craft diagnosis) with `creative-strategy` (decision) |

## 2. Variant families

| Family | What changes | What stays fixed | Typical count per test |
|--------|--------------|------------------|------------------------|
| Hook | First 1.5 to 3 s: first frame, hook text, spoken line, opening shot | Body, CTA, music, caption style | 3 to 6 |
| Body | Proof sequence, order, length of middle, demonstration used | Hook (exact first 2 s), CTA | 2 to 3 |
| CTA and end card | Offer framing, CTA wording, end card design, guarantee line | Hook and body | 2 to 3 |
| Length | 6, 15, 30, 45 s edits of the same concept | Hook and CTA | 2 |
| Format or style | Same message in a different style (S01 vs S21) | Message, offer | This is a new concept in the delivery system's eyes: route through `creative-strategy` |
| Deliverables (not test cells) | Ratios and languages | Everything | As the media plan needs |

One test, one variable family. A hook test holds the body constant; a body test holds the winning hook constant. Ratios and languages are deliverables of the same test cell, not extra cells.

Matrix size: `files = cells x lengths x ratios x languages`, with `cells = hooks` (hook test), `bodies` (body test), `CTAs` (CTA test) or `hooks x bodies x CTAs` (full factorial, rarely affordable). Full factorials need traffic most accounts do not have; keep them for Scale and Enterprise accounts with a dedicated testing lane, and ask `creative-strategy` whether the cell budget can read them.

Cells per batch by tier (planning values, align with the `creative-strategy` testing module):

| Tier | New concepts per batch | Hook cells per concept | Body or CTA cells | Files per batch (2 ratios, 1 to 2 lengths) |
|------|------------------------|------------------------|-------------------|--------------------------------------------|
| Starter | 3 to 4 per month | 2 to 3 | 0 to 1 | 12 to 30 per month |
| Growth | 2 to 6 per batch, biweekly | 3 to 4 | 1 to 2 on winners | 20 to 60 per batch |
| Scale | 4 to 12 per week | 3 to 6 | 2 to 3 on top winners | 40 to 150 per week |
| Enterprise | Per market or line | 4 to 8 | 2 to 4 | 100 to 400 per week across markets |

## 3. Generate the matrix

[variant_matrix.py](../scripts/variant_matrix.py) builds the plan and registry rows from a JSON spec and refuses names that do not parse.

```bash
python3 scripts/variant_matrix.py spec.json --out plan.csv --registry-out registry_rows.csv --created 2026-10-15
python3 scripts/variant_matrix.py spec.json --strategy bodies-first     # hook = winner (first in list)
python3 scripts/variant_matrix.py --validate 20261015_C021_hcause_runner_prob_ugc_H03_cr07_30s_916_v2_aiV-cta2
```

Spec keys: `launch, concept, angle, persona, aware, fmt, creator, hooks, bodies, ctas, lengths, ratios, languages, flags, strategy, cost_per_file, production_mode, claims_ids, music_license, talent_release_ids, source_brief`. The script prints test cells, file count and estimated cost (add generative rerolls separately).

## 4. Naming

Use the `creative-strategy` grammar exactly (single source of truth):

```
{launch}_{concept}_{angle}_{persona}_{aware}_{fmt}_{hook}_{creator}_{len}_{ratio}_{ver}[_{flags}]
file stem = ad name without {launch}; file = stem + .mp4
```

How video variants map onto it:

| Variant dimension | Token | Example |
|-------------------|-------|---------|
| Hook | `hook` H01 to H99 | H03 |
| Body | `ver` v1, v2 (iteration counter for body or edit change) | v2 |
| Length | `len` | 15s |
| Ratio | `ratio` 916, 45, 11, 169 | 45 |
| CTA or end card variant | flag `ctaN` (cta1 is the default and is omitted) | cta2 |
| Language | flag `L` + ISO 639-1 code (primary language omitted) | Ltr |
| AI generated media, AI voice, platform AI enhancement on, whitelisted, Spark | flags `aiG`, `aiV`, `aiE`, `wl`, `spk` (creative-strategy list) | aiG |
| Synthetic performer on screen (disclosure required) | flag `aiP` (video-studio extension, proposed to `creative-strategy`) | aiP |
| Policy fix re-delivery | flag `fixN` | fix1 |

Flags join with hyphens in a fixed order: AI flags, `ctaN`, `Lxx`, `wl` or `spk`, `fixN`. Example: `20261015_C021_hcause_runner_prob_ugc_H03_cr07_30s_916_v2_aiV-cta2-Ltr`.

If the project's naming spec differs (check `ads-master/outputs/creative-strategy/*naming-spec*`), follow the project spec and note the mapping in the batch output.

## 5. Registry rows

Path: `ads-master/creative-library/registry.csv`. Rules:
1. If the file exists, read its header and write only those columns, in that order. Never reorder, rename or delete columns or rows. Put extra values into a `notes` or `learnings` column if present, and propose schema changes through a journal entry.
2. If it does not exist, create it with the columns below and journal the creation.
3. Append one row per delivered file. Update only the `status`, `file_path`, `platform_creative_ids` and `learnings` of rows you created.

Default columns (produced by `variant_matrix.py --registry-out`, plus delivery fields):

`creative_id, ad_name, concept_id, hook_id, body_ver, cta_id, format, length, ratio, language, flags, test_cell, production_mode, ai_disclosure, claims_ids, music_license, talent_release_ids, file_path, status, created, owner, source_brief, learnings`

Status lifecycle: `planned` → `produced` → `qa_pass` → `approved` (human or compliance) → `uploaded_paused` (channel agent read-back) → `live` → `paused` or `retired`. Add `platform_creative_ids` when the channel agent reports them, if the header has that column.

## 6. Upload manifest (handoff file)

Save as `ads-master/outputs/video-studio/YYYY-MM-DD_video-studio_<batch>_upload-manifest.csv` next to the batch report.

```csv
ad_name,file_path,platform,placement_group,ratio,length_s,primary_text,headline,cta_button,destination_url,utm_template,ai_label_setting,paid_partnership,thumbnail_path,music_license,offer_end_date,claims_ids,notes
20261015_C021_hcause_runner_prob_ugc_H03_cr07_15s_916_v1,deliver/C021_..._916_v1.mp4,meta,Reels+Stories,916,15,"<from creative-strategy>","<headline>",SHOP_NOW,https://example.com/p,utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign}}&utm_content={{ad_name}},platform default,no,deliver/C021_..._916_v1_cover.png,EPI-123456,,CL-004,"pair with 45 version in placement customization"
```

Rules:
- Pair each 9:16 file with its 4:5 or 1:1 sibling in the notes so the channel agent uses placement asset customization.
- Copy text (primary text, headline) comes from `creative-strategy`; the CTA button and URL from the brief; UTM conventions from `measurement` (the template above is a placeholder).
- `ai_label_setting`: what the channel agent should set (for example TikTok AIGC label on, Google AI label on for EU, Meta default). `paid_partnership`: yes for creator content.
- `offer_end_date`: the date the ad must be paused because the offer ends.

## 7. Handoff protocol

1. Write the batch report (P8 output) with the QA summary, compliance status and the manifest path.
2. Write a journal entry: `ads-master/journal/YYYY-MM-DD_HHMM_video-studio_<batch>-ready.md` (what, which files, which channel agents, open risks).
3. End the final response with "Handoffs requested", for example:

```
Handoffs requested
- meta-ads: upload 24 files from <manifest> as PAUSED in the test campaign named in EXPERIMENTS.md E014; use placement
  customization pairs; set nothing live. Read back creative IDs and add them to the registry rows.
- tiktok-ads: upload 8 files (9:16) as PAUSED; AIGC label ON for files flagged aiG or aiP; Spark not used.
- compliance: confirm claims CL-004 and OF-2026-10 and the "AI-generated presenter" label wording for EU markets.
```

4. The channel agent creates entities PAUSED, reads them back and reports creative IDs. Launch happens only after human approval (G3).

## 8. Reading results back

Data needed (ad level, by ad name, last 7 and 28 days): impressions, spend, 3 s plays (Meta) or 2 s views (TikTok), ThruPlays (Meta) or 6 s views (TikTok), plays at 25, 50, 75, 95 and 100 percent, average play time, link clicks, CTR (link), conversions, CPA or ROAS. YouTube: views, view rate, played to 25/50/75/100 percent. LinkedIn: video views, completion quartiles, CTR. Source: `ads-master/data/imports/` exports or the channel agent's latest output; state the file and date range.

Formulas:
- Hook rate = 3 s plays / impressions (Meta) or 2 s views / impressions (TikTok)
- Hold rate = ThruPlays / 3 s plays (Meta) or 6 s views / 2 s views (TikTok)
- Quartile retention = plays at X percent / 3 s plays
- Body efficiency = link clicks / plays at 50 percent (where the CTA sits late)

Diagnosis by second:

| Pattern | Likely cause | Next variant |
|---------|--------------|--------------|
| Hook rate in the bottom quartile of the account | First frame and first line do not stop or signal | New hooks on the same body (3 to 5); test a different hook frame type |
| Good hook rate, steep drop between 3 and 6 s | Hook not paid off; bridge is slow or off-topic | Keep first 2 s; rebuild seconds 2 to 6 with the payoff earlier |
| Steady decline, no cliff | Pacing and density | Tighter cut, shorter length version, pattern break every 5 s |
| Cliff right before the offer | Offer arrives too late or feels like an ad break | Move offer earlier; test a 15 s cut; CTA family test |
| Good retention, low CTR | CTA weak, offer unclear, end card too short | CTA family test, end card hold 2.5 s, spoken CTA |
| Good CTR, low CVR | Landing page or offer mismatch | Hand off to `cro`; do not keep re-editing the video |
| Strong on TikTok, weak on Reels (or the reverse) | Native grammar or safe zone issues | Platform specific edit, not the same file |

Minimum read before judging a hook: wait until each variant has roughly 1,000 or more impressions for hook rate reads [Practitioner consensus]; use the `creative-strategy` minimums (spend and conversions) for CPA decisions. Early reads can kill a hook, never crown a winner.

Iteration recipes:
- Winner with a late cliff: "keep the first 2 seconds, change the second half" (Play 3 in [Production pipeline and gates](production-pipeline-and-gates.md)).
- Winner fatiguing: new first frames and hook text on the same body, then a new body.
- Two near-misses with different strengths: combine the best hook of one with the best body of the other as a new `ver`, and label it as a hypothesis.

## 9. Learning records

| Where | What |
|-------|------|
| Registry `learnings` column | One line per creative: result and the reason you think it happened, with the data source and dates |
| Journal | Batch results, winners, fatigue alerts, production problems, requests to other agents |
| `ads-master/memory/video-studio.md` | Only patterns confirmed by data (two or more concepts, or one valid test), for example "Text-led question hooks beat face-to-camera hooks on Reels hook rate in 3 of 3 tests (Meta, 2026-08 to 2026-10)" |
| `EXPERIMENTS.md` | Status updates on rows you created; `creative-strategy` owns the test rows it created |
