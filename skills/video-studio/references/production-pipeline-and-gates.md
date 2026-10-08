# Production Pipeline and Gates

> Purpose: turn an approved creative brief into finished, platform ready ad files through a staged pipeline where every stage ends in a human decision gate. Adapted from the seven stage, gate based process in the open source saas-motion-kit (credited in [Sources](sources.md)), rebuilt for performance ads: hook in the first 1 to 2 seconds, many variants, sound off captions, safe zones, PAUSED handoff and a learning loop.

## 1. Why gates

A video looks machine made when every decision is the first idea that came up. Two or three moments of human taste (which message, which treatment, which frame opens the ad) change that. The agent does the production work; the human, or `creative-strategy` acting for the human, decides at the gates. [Practitioner consensus; saas-motion-kit playbook, 2026]

Gates are also the money and truth controls: no paid generation before the budget gate, no delivery before the QA and compliance gate, no upload before the human approves the change list.

Do not confuse production gates (P1 to P9 below) with the guardrail gates G0 to G4 in `docs/GUARDRAILS_MODEL.md`. Production work is G1 (local drafts and renders on disk). Paid API generation is a spend decision and needs an approved cap. Uploading to an ad account library is G2 and belongs to the channel agent.

## 2. The nine stages

| Stage | Name | Agent produces | Gate decision (who) | Exit criteria |
|-------|------|----------------|---------------------|---------------|
| P1 | Brief lock | Production brief card (section 4) from the `creative-strategy` brief | Human or `creative-strategy` confirms the card describes the ad they want | One message, one awareness level, placements, lengths, offer, CTA, truth source, claim IDs from `brand/CLAIMS.md` |
| P2 | Truth and asset inventory | Asset inventory: real footage, product photos, UI capture, logos, fonts, talent releases, music licenses, gaps | Human approves real vs imaginary per component and the gap list | Every proof element maps to a real asset or a truthful imaginary component ([Truth, disclosure and rights](truth-disclosure-and-rights.md)) |
| P3 | Treatment | 2 to 3 treatments from the [Style library](style-library.md), each as one key frame of the proof moment in the brand | Human picks one | Variety ledger check passed (not a repeat of the last 3 ads for this brand on the same dimension) |
| P4 | Script, storyboard, variant plan, budget | Beat sheet by second, hook bank, storyboard stills, variant matrix ([Variants and testing handoff](variants-and-testing-handoff.md)), generation cost estimate | Human approves stills (read with sound off), the matrix and the spend cap | Creative pass done (section 6); budget cap written in the output file |
| P5 | Production | Captured, generated or coded footage; rough cut or composition preview | Human approves the rough cut timing | Hook lands by 2.0 s; product or problem visible by 2.0 s; proof delivered; no unapproved claims |
| P6 | Sound and captions | VO, music, SFX, captions, loudness pass | Human approves the mix with picture | Licensed audio only; captions verbatim to VO; target loudness hit |
| P7 | Versioning and QA | Cut-downs, ratios, languages, end card variants; [QA checklist](qa-checklist.md) results; compliance packet | QA pass plus `compliance` sign-off on claims and disclosure | Zero blockers in QA; every file name parses |
| P8 | Delivery and handoff | Files, upload manifest, registry rows, journal entry, Handoffs requested | Human approves the upload change list; channel agent uploads PAUSED | Read-back by channel agent confirms creative IDs |
| P9 | Learn | Performance readback by second and by variant, iteration brief | `creative-strategy` decides kill, iterate, scale | Learnings in registry and journal; memory only when confirmed |

Mapping to the saas-motion-kit stages: Brief = P1, Components = P2, Theme = P3, Storyboard plus creative pass = P4, Build = P5, Sound = P6, Deliver = P7 and P8. P9 is the performance loop the kit does not have.

## 3. Gate depth by tier

| Tier | Gates the human attends | Gates the agent self-certifies (logged) | Why |
|------|------------------------|----------------------------------------|-----|
| Starter (under $3k) | P1 plus P3 together (one message, one treatment), P4 (stills and budget), P7 (final watch on a phone) | P2, P5, P6 | Few concepts, the founder is the creative director; 3 meetings per batch max |
| Growth ($3k to $30k) | P1, P3, P4, P7 | P2, P5, P6 with logged checklists | Weekly or biweekly batches |
| Scale ($30k to $300k) | P1 and P4 for new concepts; P7 sampling (1 in 5 files) for iterations on approved templates | P3 skipped when an approved template is reused; P5, P6 | Weekly variant batches; templates carry the approved taste |
| Enterprise (over $300k) | Brand council at P3 for new templates; market reviewers at P7 for localization | Template iterations end to end with logged QA | Volume, localization, legal review per market |

Never skip P7 compliance review for: new claims, health, finance, before and after, comparative claims, AI performers, children, regulated categories.

## 4. Production brief card (P1 output)

```
# Production brief card: C0xx <short name> | batch YYYY-MM-DD
Source brief: ads-master/outputs/creative-strategy/<file> (link)
One message (fits on a sticky note):
Persona and awareness level:
Placement plan: [Reels/Stories 9:16] [Feed 4:5] [TikTok 9:16] [Shorts 9:16] [YouTube 16:9] [LinkedIn 1:1 or 16:9]
Lengths: [6s] [9 to 15s] [15 to 30s] [30 to 60s]
Hook bank (3 to 5, from creative-strategy; each with visual, on-screen text, spoken line):
Proof moment (the one frame someone would screenshot):
Offer and CTA (exact wording from offer-strategy or PROJECT_BRIEF.md; end card text):
Claims used (IDs from brand/CLAIMS.md, status approved only):
Truth source (product page, docs, spec sheet; nothing else):
Mandatory elements (logo rules, disclaimers, legal lines):
Production mode: footage | code-driven | generative | avatar | hybrid
Sound plan: sound on native | sound off captions-first | both
AI use and disclosure flags: aiG / aiV / aiP / none
Budget cap for paid generation (approved by): 
Deadline and gate owners:
```

## 5. Storyboard beat sheet (P4 output)

One row per shot. Time in seconds. Fill before any production.

| # | Start | Dur | Beat | Visual (what we see) | On-screen text (max 6 words) | Spoken or sung | Sound | Transition out | Variant slot | Notes |
|---|-------|-----|------|----------------------|------------------------------|----------------|-------|----------------|--------------|-------|
| 1 | 0.0 | 1.5 | Hook | Product in hand, macro, motion in frame 1 | "Your knees after 5k?" | "If your knees hurt after every run" | Room tone, footstep | Hard cut on action | H01 to H04 | First frame is the thumbnail |
| 2 | 1.5 | 3.0 | Problem | ... | ... | ... | ... | Match cut (shape) | body v1 | ... |
| 3 | 4.5 | 6.0 | Proof | Real test, real product | ... | ... | ... | ... | body v1 | Claim ID CL-004 |
| 4 | 10.5 | 3.0 | Offer and CTA | End card | "20% off first order" | "Tap Shop Now" | Button SFX | Hold 2.5 s | cta1, cta2 | Offer text from offer-strategy |

Rules: the variant slot column shows which rows change per variant (hook rows, body rows, CTA rows). A variant may change only the rows of its family.

## 6. The creative pass (mandatory at P4)

Adapted from the kit's "seven questions" and variety audit, plus performance rules.

1. Message and tone sentence at the top: "I want to say ___ in a ___ tone, so the viewer ___ (stops, believes, taps)."
2. Hook check: is the product or the problem visible in frame 1 to 2? Does the first frame work as a thumbnail with no motion and no sound?
3. Sound off test: read the stills and on-screen text only. Is the message clear?
4. Sound on test: read the spoken lines only. Is the message clear?
5. Repetition check inside the ad: no transition, text entrance or ease used on two consecutive cuts unless it is a deliberate motif (mark `motif:`).
6. Cross ad check (variety ledger, section 7): does this repeat the visual world, talent, opening shot or transition grammar of the last 3 ads for this brand?
7. Surprise: one pattern break every 5 to 8 s in performance ads (a scale change, a cut to silence, a medium change, a reveal). The kit's 10 to 15 s interval is for brand films; performance ads need it sooner. [Practitioner consensus]
8. Proof check: is the proof real (footage, data with source, real review with permission)? Mark each proof element with its asset ID or claim ID.
9. CTA check: one action, matches the landing page and the platform CTA button.
10. Truth check: nothing shows a capability, result, number, customer or review that does not exist ([Truth, disclosure and rights](truth-disclosure-and-rights.md)).

## 7. Variety ledger (cross ad history)

Keep one ledger per brand at `ads-master/outputs/video-studio/variety-ledger.csv` (create on first batch, append only). Columns:

`date, creative_id, concept_id, style_id, visual_world, talent_type, opening_shot, hook_type, transition_signature, palette_lead, music_mood, vo_type, length, ratio, result_tag`

Rules:
- A new concept must differ from every live ad of the same brand on at least 2 of: style_id, visual_world, talent_type, opening_shot, hook_type. This mirrors the `creative-strategy` "new concept" test, so Meta and TikTok treat it as a distinct creative. [Practitioner consensus]
- Iterations keep the ledger row of their parent and change only the variant family.
- Every 10 ads, summarize the ledger: which styles, opening shots and transitions dominate; which have never been tried. Put the summary in the batch output.

## 8. Playbooks

### Play 1: First batch for a new account (Starter or Growth, Stage B)
1. Read the `creative-strategy` concept slate. Pick 3 to 4 maximally different concepts (different style_id and hook_type).
2. P1 cards for each. P2 inventory: what real footage exists? Phone footage plan if none (see [Editing real footage](editing-real-footage.md) section 2).
3. Production mode per concept: one founder or customer phone video, one code-driven product or offer video, one texture or demo macro video, optional one generative b-roll led concept.
4. Variant plan: 3 hooks per concept on one body, 1 CTA, 2 ratios (9:16 and 4:5), 1 length (15 to 30 s). That is 3 to 4 concepts x 3 hooks = 9 to 12 test cells, 18 to 24 files.
5. P7 QA and compliance. P8 handoff to `meta-ads` and or `tiktok-ads` with the manifest.
6. P9 after the channel agent's minimum read window: read hook rate per hook, hold per body.

### Play 2: Weekly variant batch (Scale, Stage C)
1. Monday: import last 7 and 28 days of ad level data with retention points (3 s, 25/50/75/95 percent) from `data/imports/` or the channel agent's output.
2. Rank winners by the KPI in `PROJECT_BRIEF.md`. For each top winner pick one rung: new hooks (body fixed), new body (hook fixed), new CTA or end card, new length, new format.
3. New concepts: produce what `creative-strategy` briefed (target share from its decision tree, usually 30 to 60 percent new concepts).
4. Tuesday to Wednesday: produce from approved templates (code-driven) and footage bins. Generative shots only inside the approved cap.
5. Thursday: QA (sample 1 in 5 for template iterations, 100 percent for new concepts), registry rows, handoff.
6. Keep total files per week inside what the test budget can read (ask `creative-strategy` for the cell budget).

### Play 3: Winner iteration ("keep the first 2 seconds, change the second half")
1. Pull the retention curve of the winner. Locate the biggest drop after second 3.
2. Keep frames 0 to the end of the hook beat exactly (same file segment, same audio). Changing the opening resets the reason it won.
3. Rebuild from the drop point: shorter proof, a different proof asset, a different demonstration, or move the offer earlier.
4. Produce 2 to 3 body variants. Name them as `ver` increments on the same hook ID.
5. In parallel, produce 3 new hooks on the original body (a separate test family).

### Play 4: Fatigue refresh without a new concept
1. Signals from the channel agent: CTR and hook rate down 20 percent or more from the ad's best 7 days at stable CPM, or frequency rising in the same audience.
2. Refresh layers in this order: first frame and hook text, talent or setting of the hook shot, music and VO, end card, format (static to motion, talking head to demo).
3. Each refresh is an iteration of the parent concept; log the rung in the registry.

### Play 5: Localization batch
1. Lock the master with text on separate layers (code-driven) or an ASS caption file (footage).
2. Translate on-screen text and VO with a native reviewer; never machine translate claims without review.
3. Use latin-ext or the correct script subsets for fonts; type uppercase manually for Turkish and Azerbaijani dotted and dotless i (see [Code-driven motion](code-driven-motion.md) section 7).
4. AI dubbing or voice cloning only with written consent of the original speaker and the disclosure required in the market.
5. Re-run QA per language: caption timing, safe zones (text length grows 20 to 35 percent in German, Finnish, Turkish [Practitioner consensus]), legal lines in local language.

### Play 6: Offer burst (BFCM, launch, seasonal)
1. Get the offer terms from `offer-strategy` (exact discount, dates, exclusions). Never invent urgency.
2. Build one code-driven offer template with variables: price, discount, deadline date, product image, CTA.
3. Produce the end card in 3 variants (price led, benefit led, deadline led) and attach to the top 3 winners as a CTA family test.
4. Countdown visuals must match the real end date and time zone of the offer; schedule a pull date in the manifest.

### Play 7: Repurpose organic or creator content into ads
1. Confirm paid usage rights, duration and territories in writing (creator registry from `creative-strategy`).
2. Trim the first 2 s to the most arresting moment; add a hook text overlay; captions; end card.
3. Keep the creator's native look; do not over-brand. For Spark Ads or partnership ads, the channel agent needs the original post or authorization code, not a re-upload.

### Play 8: Stage A delivery when no tools are installed
Deliver a production pack instead of files: P1 card, beat sheet, shot list with framing and duration, hook bank with exact text, caption file (SRT), edit decision list (CSV), music brief, generation prompts with model choice and cost estimate, and a CapCut or Premiere step list. See [Tools, APIs and MCP](tools-api-mcp.md) section 5.

### Play 9: Rejected or limited ad recovery
1. Read the rejection reason from the channel agent. Map it to the element: claim, before and after, personal attributes, AI disclosure, music, text, landing page.
2. Fix only that element; re-run P7 QA and `compliance`.
3. Re-deliver as the same `ver` with a new flag `fix1` only when the creative content changed materially; otherwise keep the name and note the fix in the registry.

## 9. Gate log (append to every batch output)

| Gate | Date | Decision | By | Notes (what changed) |
|------|------|----------|----|----------------------|
| P1 | | approved / changes | | |
| P3 | | treatment T2 chosen | | |
| P4 | | stills approved, cap 120 USD | | |
| P7 | | QA pass, compliance pass | | |
| P8 | | upload change list approved | | |

## 10. Time and cost planning values

| Item | Typical effort or cost | Source |
|------|------------------------|--------|
| Code-driven offer or product video from an approved template | 15 to 60 min agent time per variant set | [Practitioner consensus] |
| New code-driven template (HyperFrames or Remotion) | 0.5 to 2 days including gates | [Practitioner consensus] |
| Editing phone or creator footage into 3 hooks x 1 body x 2 ratios | 1 to 3 hours | [Practitioner consensus] |
| Generative video clip, 8 s at 1080p | about 0.64 USD (Veo 3.1 Lite) to 3.20 USD (Veo 3.1 standard) per accepted clip before rerolls | [Official pricing via secondary, 2026-09] |
| Rerolls per accepted generative shot | plan 2 to 4 attempts | [Practitioner consensus] |
| AI avatar video via HeyGen API (Avatar IV) | about 0.05 USD per second | [Official docs via secondary, 2026] |

Always present the cost estimate at P4 and record actual spend in the batch output.
