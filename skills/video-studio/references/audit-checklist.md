# Audit Checklist: Video Ad Production System

> Purpose: score how well a brand turns briefs into platform ready video ads and learns from results. Run at onboarding, then quarterly. Inputs: the last 60 to 90 days of live and paused video ads (exports from `data/imports/` or channel agent outputs), 10 sampled ad files, the registry, briefs, licenses and the production log. State the data used and the date range in the report.

How to run it (2 to 4 hours):
1. Pull the ad level export for video ads (last 60 to 90 days) and list every ad name; run the name regex (`variant_matrix.py --validate` in a loop) and count failures.
2. Sample 10 ads: the top 5 by spend and 5 random recent launches. Download or screen-record them (no re-upload anywhere).
3. Run `ffmpeg_deliver.py check` and `overlay` on the sampled files you can access; watch each muted and with sound on a phone.
4. Collect briefs, releases, music licenses, registry rows and batch reports for the sampled ads.
5. Score every item below, write the evidence next to each score, then compute section and total scores.

Scoring: each item scores 0 (missing or failing), 1 (partial) or 2 (in place and working). Multiply by the severity weight (3 = critical, 2 = important, 1 = hygiene). Section score = sum / max. Total score = sum of all weighted scores / maximum possible.

## A. Inputs and briefs

| # | Check | Why it matters | How to verify | Weight | Fix |
|---|-------|----------------|---------------|--------|-----|
| A1 | Every produced video traces to a brief with one message, awareness level, placements and claims | Unbriefed videos test nothing | Sample 10 ads; find their briefs | 3 | Use the production brief card (P1) for every concept |
| A2 | Hook banks exist per concept (3 or more hooks with visual, text and spoken line) | Hooks are the cheapest lever | Briefs and EDLs | 2 | Ask `creative-strategy` for hook banks; produce hook packs |
| A3 | Truth source and approved claims list available (`brand/CLAIMS.md`, `PRODUCT_FACTS.md`) | Prevents unapproved claims | Files present and current | 3 | Hand off to `compliance` to build them |
| A4 | Offer terms come from one owner (`offer-strategy` or PROJECT_BRIEF) | Wrong prices are incidents | Compare end cards with the site | 3 | Single offer source; manifest offer end dates |

## B. Truth and rights

| # | Check | Why | How to verify | Weight | Fix |
|---|-------|-----|---------------|--------|-----|
| B1 | No AI or actor "customers" giving testimonials; real testimonials have releases | FTC 16 CFR 465, platform policy, trust | Review sampled ads and releases | 3 | Remove; replace with real customers or labeled presenters |
| B2 | Product shown is the real product in every ad (no generated product shape, color or label) | Misrepresentation, returns, EU deep fake rule | Compare with product photos | 3 | Composite real product; re-shoot |
| B3 | Software UI is real or truthful imaginary; no invented features or numbers | Deception | Compare with the product | 3 | Clean or imaginary audit (P2) |
| B4 | Every music track has a license covering paid ads in the markets | Label lawsuits against brands (2024 to 2026) | License log per file | 3 | License or replace; take down unlicensed ads via channel agents |
| B5 | Creator and talent usage rights valid through the flight; expiry tracked | Expired rights force takedowns | Creator registry dates | 2 | Track expiries; renew or retire |
| B6 | Reference ads credited and only grammar borrowed | Copying invites legal risk and lookalike grouping | Batch reports | 1 | Reference rows and `ref:` notes |

## C. Production capability

| # | Check | Why | How to verify | Weight | Fix |
|---|-------|-----|---------------|--------|-----|
| C1 | The production mode fits the tier (Starter phone plus code-driven; Scale weekly batches) | Over-production wastes budget; under-production starves testing | Compare volume with the adaptation matrix | 2 | Reset the production plan |
| C2 | Code-driven templates exist for offer, end card, hook pack and the brand's main proof style | Speed and consistency for iterations | Template folder | 2 | Build T1 to T3 first ([Code-driven motion](code-driven-motion.md)) |
| C3 | Footage bin with releases and an intake log | Reusable raw material for new hooks | Bin and log | 2 | Phone footage plan; intake log |
| C4 | Generation spend has caps, estimates and logs | Uncontrolled API spend | Batch outputs and shots.json | 2 | Spend protocol ([Tools, APIs and MCP](tools-api-mcp.md) section 4) |
| C5 | Renders reproducible (versions, seeds, templates recorded) | Re-renders for fixes and localization | Reproducibility records | 1 | Add the record block to batch outputs |

## D. Craft quality (sample 10 live or recent ads)

| # | Check | Why | How to verify | Weight | Fix |
|---|-------|-----|---------------|--------|-----|
| D1 | Product or problem visible by 2.0 s | First 3 seconds drive recall and CTR (TikTok guidance) | Watch with a timer | 3 | Re-hook; hook packs |
| D2 | Frame 1 is not black, a logo card or a fade in | Lost first impressions | `ffmpeg_deliver.py check` | 2 | Rebuild openings |
| D3 | Hook promise paid off by second 5 or 6 | Bait hooks lose hold rate | Watch; retention curves | 2 | Body variants from the drop point |
| D4 | One message per ad | Mixed messages dilute | Watch | 2 | Split into two ads |
| D5 | Captions burned or provided, accurate, readable | Sound off viewers and accessibility | Watch muted | 3 | Caption pipeline |
| D6 | Shot lengths vary; at least one pattern break every 5 to 8 s | Mechanical edits feel generated | Shot list or scene detection | 1 | Variety pass at P4 |
| D7 | No "AI look" tells in generated shots (waxy skin, drift, morphing, gibberish text) | Trust and effectiveness loss (NIQ 2024, Ipsos 2026) | Frame scrub | 2 | Real footage for proof; tighter generated shots; human gates |
| D8 | End card held 2 to 3 s with one CTA that matches the platform button and landing page | CTR and message match | Watch | 2 | End card library |

## E. Platform fit

| # | Check | Why | How to verify | Weight | Fix |
|---|-------|-----|---------------|--------|-----|
| E1 | Text, offers and CTAs inside safe zones for each placement | Hidden CTAs and cut text | Overlay frames | 3 | Re-layout; universal 9:16 box |
| E2 | 9:16 and 4:5 (or 1:1) versions delivered for Meta; 9:16 native for TikTok and Shorts; 16:9 for YouTube in-stream | Auto crops hide products | Asset inventory per ad | 3 | Ratio plan per placement |
| E3 | Native grammar per platform (no letterboxed 16:9 on vertical, no watermarks, sound plan right) | Native ads earn more attention | Watch | 2 | Platform specific edits |
| E4 | Loudness and true peak at target | Quiet ads lose sound on viewers; loud ones clip | `check` | 1 | Two-pass loudnorm |
| E5 | Specs verified against live previews in the last 90 days | Overlays and limits change | Dated verification records | 1 | Verification protocol |

## F. Variants and naming

| # | Check | Why | How to verify | Weight | Fix |
|---|-------|-----|---------------|--------|-----|
| F1 | Every ad name parses with the creative-strategy grammar | Concept level analysis depends on it | Regex over the ad export | 3 | Rename going forward; mapping table for old ads |
| F2 | Tests vary one family at a time (hooks, bodies, CTAs) | Confounded tests teach nothing | Compare variants in a test | 3 | Variant matrix strategies |
| F3 | Variant volume fits the test budget (cells can reach a read in 14 days) | Under-read tests waste production | Cells vs spend | 2 | Fewer, sharper cells |
| F4 | Registry rows exist for every delivered file with claims, music, releases and status | Traceability and takedowns | Registry vs ad export | 2 | Registry backfill |

## G. QA and compliance

| # | Check | Why | How to verify | Weight | Fix |
|---|-------|-----|---------------|--------|-----|
| G1 | QA checklist run and recorded per batch | Prevents rejections and incidents | Batch reports | 3 | P7 gate |
| G2 | Compliance sign-off for new claims, regulated categories, AI performers | Legal exposure | Batch reports | 3 | Compliance packet |
| G3 | Rejection rate under 5 percent of uploaded videos in 90 days | Rejections delay learning | Channel agent logs | 2 | Fix root causes by category |
| G4 | Disclosures present where required (synthetic performers, EU deep fakes, paid partnerships) | NY, Hawaii, California, EU, FTC | Watch flagged files | 3 | Disclosure templates |

## H. Delivery and handoff

| # | Check | Why | How to verify | Weight | Fix |
|---|-------|-----|---------------|--------|-----|
| H1 | Upload manifests with copy, URLs, label settings and offer end dates | Upload errors and stale offers | Manifest files | 2 | Manifest template |
| H2 | Channel agents upload PAUSED and read back creative IDs into the registry | Safety and traceability | Registry IDs | 2 | Handoff protocol |
| H3 | Brief to first delivery time meets the tier target (Starter 1 to 2 weeks, Growth 5 to 7 days, Scale 2 to 4 days for iterations) | Speed of learning | Dates in briefs and deliveries | 1 | Templates, footage bins, fewer gates for iterations |

## I. Learning loop

| # | Check | Why | How to verify | Weight | Fix |
|---|-------|-----|---------------|--------|-----|
| I1 | Retention by second and hook rate read for every test and fed into the next batch | Without readback, production repeats mistakes | Batch reports reference prior results | 3 | Weekly readback (Play 2) |
| I2 | Winners iterated with the "keep the first 2 seconds" recipe and hook packs | Scaling winners cheaply | Registry iteration chains | 2 | Iteration recipes |
| I3 | Variety ledger maintained; no style or opening shot dominates more than 50 percent of recent ads | Creative diversity for delivery systems | Ledger summary | 2 | New styles from the library |
| I4 | Memory file holds only data-confirmed patterns with evidence | Avoids folklore | `memory/video-studio.md` | 1 | Prune and cite |

## Scoring rubric

| Total score | Rating | Meaning | Next step |
|-------------|--------|---------|-----------|
| 85 to 100 percent | Strong | System produces, ships and learns reliably | Optimize speed and cost; expand styles and markets |
| 70 to 84 percent | Solid with gaps | Works but leaks learning or risk | Fix every critical item scored 0 or 1 within 2 weeks |
| 50 to 69 percent | Fragile | Volume or quality depends on individuals; risk exposure | 30 day plan: briefs, naming, QA, licenses, templates |
| Under 50 percent | Broken | Ads ship without briefs, rights or QA | Pause new production beyond fixes; Stage A packs and rights cleanup first |

Any critical item (weight 3) scored 0 in sections B or G is an incident candidate: report it to the human immediately and follow `ads-master/INCIDENTS.md` if a live ad is affected (for example unlicensed music or a fake testimonial live).

## Report template

```
# Video production audit: <brand>, <date>
Data used: <exports, files, date range>; sample: <10 ad names>
Total score: X of Y (Z percent), rating
Section scores: A .. I
Critical findings (weight 3, score 0 or 1): numbered, each with evidence and fix
Top 5 fixes by impact x ease, owner, due date
Incidents raised: <none or list>
Handoffs requested: <slugs with briefs>
```
