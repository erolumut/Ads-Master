# Briefs and Naming Conventions

> Purpose: brief editors, creators and AI tools so output matches the concept, and name every asset so analysis can attribute results to concepts, angles, personas, hooks and creators. Without the naming convention, creative analytics is guesswork.

## 1. Naming convention (ad name grammar)

```
{launch}_{concept}_{angle}_{persona}_{aware}_{fmt}_{hook}_{creator}_{len}_{ratio}_{ver}[_{flags}]
```

Rules: underscore separates tokens; tokens never contain underscores or spaces; use lowercase codes except IDs; unknown or not applicable = `na`; max about 100 characters.

| Token | Format | Example | Notes |
|-------|--------|---------|-------|
| launch | YYYYMMDD | 20261008 | Launch date of this ad |
| concept | C + 3 digits | C021 | From the concept registry, permanent |
| angle | short code | hcause | From the angle code list below |
| persona | short code | runner | From `AUDIENCE.md` segments |
| aware | unaw, prob, sol, prod, most | prob | Schwartz level |
| fmt | ugc, cre, fdr, demo, test, uvt, list, ps, stat, car, meme, pod, str, gs, ai, cat | ugc | Format code list below |
| hook | H + 2 digits | H03 | Hook ID within the concept |
| creator | cr + 2 digits or na | cr07 | From the creator registry |
| len | seconds + s, or na for statics | 30s | Video length |
| ratio | 916, 45, 11, 169 | 916 | Aspect ratio |
| ver | v + number | v2 | Iteration counter (body or edit change) |
| flags | optional: aiE (Advantage+ or platform AI enhancement on), aiG (AI generated media), aiV (AI voice), wl (whitelisted or partnership), spk (Spark) | aiG-wl | Join multiple flags with hyphen |

Example: `20261008_C021_hcause_runner_prob_ugc_H03_cr07_30s_916_v2_wl`

**Angle codes (extend per account):** pain (problem agitation), hcause (hidden cause), failsol (failed solutions), ident (identity), enemy, uvt (us vs them), transf (transformation), ditl (day in the life), origin (founder origin), auth (authority), proof (social proof), tmon (testimonial outcome), objf (objection first), myth, coi (cost of inaction), price (price reframe), risk (risk reversal), ease, new, time (scarcity or timeliness), gift, sens (ritual or sensory), edu, expalt (expensive alternative), comm (community).

**Format codes:** ugc (UGC), cre (creator led), fdr (founder), demo, test (testimonial), uvt (us vs them), list (listicle), ps (problem solution), stat (static), car (carousel), meme, pod (podcast style), str (street interview), gs (green screen), ai (AI avatar), cat (catalog or DPA).

**Campaign and ad set names** belong to channel agents, but ask them to include a test lane marker (`TEST` or `SCALE`) so creative analysis can split lanes.

**File names** for assets mirror the ad name without the launch date: `C021_hcause_runner_prob_ugc_H03_cr07_30s_916_v2.mp4`.

**Validation regex (Python):**

```python
import re
PAT = re.compile(r"^(\d{8})_(C\d{3})_([a-z]+)_([a-z0-9]+)_(unaw|prob|sol|prod|most)_"
                 r"(ugc|cre|fdr|demo|test|uvt|list|ps|stat|car|meme|pod|str|gs|ai|cat)_"
                 r"(H\d{2}|na)_(cr\d{2}|na)_(\d+s|na)_(916|45|11|169|na)_(v\d+)(_[a-zA-Z0-9-]+)?$")
def check(name): return bool(PAT.match(name))
```

Run it over every ad name in an export; list non-conforming names in the audit.

## 2. Registries (keep in a spreadsheet or Notion, link from outputs)

**Concept registry columns:** concept ID, name, persona, awareness, angle, big idea, VOC sources, status (brief, production, testing, winner, retired), launch date, best CPA or ROAS, evidence level, learnings, links.

**Creator registry columns:** creator ID, handle, platform, niche, rates, usage rights (type, duration, territories, expiry date), whitelisting or Spark authorization status, consent forms, performance summary.

**Hook library columns:** hook ID, concept ID, hook type, text, first frame description, hook rate, CTR, status.

## 3. Concept brief template (strategist to team)

```
# Concept brief: C0xx <short name>
Date: YYYY-MM-DD | Owner: creative-strategy | Priority score: x/25
## Objective
Channel(s), placement(s), campaign lane (TEST or SCALE), KPI and target
## Persona and awareness
Who, in their words; awareness level; trigger moment
## Insight (verbatim VOC + source)
## Angle and big idea (one sentence)
## Why this is a new concept (dimensions that differ from live winners)
## Proof to show
## Mandatory elements
Product shots, claims allowed (from BRAND.md), disclosures, logo rules, offer
## Hooks to produce (3 to 5, each with visual / text / verbal)
## Script or outline (see hooks-and-scripts templates)
## Deliverables
Lengths, ratios (9:16 master, 4:5, 1:1, 16:9), captions, raw footage, thumbnails
## Do not
Claims, words, visuals to avoid; competitor names; AI uses not allowed
## Naming
Ad names to use (pre-filled)
## Deadline and review steps
```

## 4. UGC or creator brief template (strategist to creator)

```
# Creator brief: <brand> x <creator> | Concept C0xx
## About the product (3 lines, plain language)
## Who you are talking to (persona, their words)
## The one thing viewers must feel or understand
## Hook options (pick 2 and film both; film each as a separate clip)
1.
2.
3.
## Talking points (in your own words, not a script to read)
- Problem you had
- What you tried before
- First impression of the product
- The result (only what you actually experienced)
- Who you would recommend it to
## Must show
Product in hand within the first 3 seconds; product in use; the result
## Must not
Medical, financial or guaranteed results claims; competitor names; unlicensed music; anything you did not actually experience
## Technical
Vertical 9:16, 4K or 1080p, natural light facing a window, phone at eye level, clean audio (quiet room, no music), 3 takes of each hook, film b-roll: unboxing, close-ups, in-use, reaction
## Disclosure
Organic post: include the platform paid partnership label and #ad as agreed. Paid ads run via partnership ads or Spark Ads with your approval.
## Deliverables and rights
Raw files plus edited cut by DATE. Usage: paid social on Meta and TikTok for N months, territories, whitelisting or Spark authorization for N days (see contract)
## Payment and revisions
Amount, schedule, 1 revision round included
```

## 5. Static brief template

```
# Static brief: C0xx | Static type: (review card, comparison, feature callouts, offer, problem visual, meme)
Headline (max 8 words):
Subhead or supporting line:
Visual: what is in frame, background, product angle, props
Proof element: review quote verbatim (source), rating, number with source
CTA on image (optional):
Primary text (Meta): first 125 characters carry the hook
Headline field (Meta): max about 40 characters
Ratios: 4:5 and 1:1 (Feed), 9:16 (Stories and Reels, keep safe zones)
Variants: 3 headlines x 1 visual = iterations; new visual world = new concept
```

## 6. Iteration brief template (for winners)

```
# Iteration brief: C0xx winner <ad name>
Evidence: CPA $x on y conversions, hook rate z%, hold w% (source, dates)
Rung(s): hooks / first frame / body / length / format / talent
Keep: what made it work (be specific)
Change: exactly what changes in each variant
Variants: names pre-filled with H and v counters
Deadline:
```

## 7. AI production brief template

```
# AI production brief: C0xx
Tool(s): (Advantage+ creative image to video, Asset Studio, Veo, Runway, Kling, Midjourney, HeyGen, ElevenLabs)
Use case: background variations / localization / voiceover draft / b-roll / avatar explainer
Inputs: approved product photos (real), approved script, brand fonts and colors
Prompt (versioned):
Fidelity rules: product shape, color, label text must match real product; no invented features
Prohibited: synthetic customers or testimonials, real person likeness without consent, fake reviews, fake UI or news
Disclosure: platform AI label behavior; C2PA metadata retained; extra disclosure required? (see compliance)
QA reviewer and checklist: see ai-creative-production QA
Naming flag: aiG / aiV / aiE
```

## 8. Production workflow (kanban stages)

| Stage | Owner | Exit criteria |
|-------|-------|---------------|
| 1. Research | Strategist | VOC bank updated |
| 2. Concept | Strategist | Concept card scored, passes new concept test |
| 3. Brief | Strategist | Brief approved by human or brand owner |
| 4. Production | Creator, editor, designer, AI operator | Files delivered per specs |
| 5. Creative QA | Strategist | Script QA, specs, safe zones, captions, naming |
| 6. Compliance QA | Strategist plus human for regulated claims | Compliance checklist passed |
| 7. Ready to launch | Channel agent | Change list approved by human |
| 8. Testing | Channel agent | Read point reached |
| 9. Decision | Strategist | Kill, iterate, scale logged |
| 10. Learnings | Strategist | Tracker, journal, memory if confirmed |

SLA targets (Growth and above): brief to first cut 5 to 7 working days; iteration requests 2 to 3 days; static variants 1 to 2 days. [Practitioner consensus]

## 9. Creative operations by tier

| Tier | Team | Tools | Weekly rhythm | Monthly output |
|------|------|-------|---------------|----------------|
| Starter | Founder or marketer plus freelancer as needed | Phone, CapCut, Canva, platform AI tools, spreadsheet tracker | One 60 minute creative review | 4 to 10 new ads |
| Growth | Strategist (can be part-time), 1 editor, 2 to 6 creators per month | Above plus Foreplay or Atria or Motion, UGC platform | Monday analysis, Tuesday briefs, Thursday launch | 10 to 40 new ads |
| Scale | Strategist, 2 to 4 editors, designer, creator manager, AI operator | Analytics tool, DAM, bulk upload, creator CRM | Two launch days, daily fatigue scan | 40 to 150 new ads |
| Enterprise | Creative ops lead, strategists per market or line, studio partners, localization | Enterprise DAM, analytics, workflow tool, MMM inputs | Per pod cadence, quarterly global concepts | 150 to 600+ new ads |

## 10. Weekly creative meeting agenda (45 to 60 minutes)

1. Last week's numbers by concept (10 min): winners, losers, fatigue watch.
2. Learnings by dimension (10 min): angle, persona, awareness, format, creator.
3. Decisions (10 min): kill, iterate, scale change list.
4. Next slate (15 min): new concepts and iterations, owners, deadlines.
5. Blockers and approvals needed (5 min).
