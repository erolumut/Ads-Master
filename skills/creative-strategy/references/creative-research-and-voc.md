# Creative Research and Voice of Customer

> Purpose: produce a VOC bank of verbatim customer language, tagged so it converts directly into angles, hooks and copy. Research is the highest leverage creative activity: concepts built on real words beat concepts built on brainstorms. Boundary: `market-intel` owns full competitive positioning, pricing and market sizing. This module owns research done to generate and validate ad concepts.

## 1. The research sprint (5 to 10 working hours, repeat quarterly)

| Step | Source | Output | Time |
|------|--------|--------|------|
| 1 | Existing `AUDIENCE.md`, `BRAND.md`, `COMPETITORS.md`, memory, last `market-intel` outputs | List of known segments, claims, gaps | 30 min |
| 2 | Own reviews (site, Amazon, Trustpilot, Google Business Profile, app stores, G2 or Capterra) | 50 to 150 tagged quotes | 1 to 2 h |
| 3 | Competitor reviews, especially 2 and 3 star | Unmet needs, switching triggers, objections to the category | 1 h |
| 4 | Reddit, forums, Facebook groups, Discord, Quora | Raw pain language, identity language, "what I tried" lists | 1 to 2 h |
| 5 | Sales calls, demos, support tickets, chat logs, returns reasons | Objections, decision triggers, buyer questions | 1 to 2 h |
| 6 | Search queries (Google Ads search terms, Search Console, autocomplete, People Also Ask) | Intent language, problem framing, comparison queries | 45 min |
| 7 | Ad libraries (Meta, TikTok, Google, LinkedIn) | Competitor angle map, long running ads, format gaps | 1 to 2 h |
| 8 | Post-purchase or on-site survey (if none exists, draft one) | Ongoing quantitative VOC | 30 min to draft |
| 9 | Synthesis | VOC bank, top 10 pains, top 10 desires, top 10 objections, angle candidates | 1 h |

Deliverable: `ads-master/outputs/creative-strategy/YYYY-MM-DD_creative-strategy_voc-bank.md`. Propose additions to `AUDIENCE.md` (Voice of customer section) via a journal entry; never edit it directly.

## 2. Tagging schema (use for every quote)

| Tag | Meaning | Example tag value |
|-----|---------|-------------------|
| `src` | Source and URL or file | `amazon_competitorX_3star`, `gong_2026-08-12_call14` |
| `seg` | Segment or persona | `new_parent`, `ops_manager`, `gift_buyer` |
| `aware` | Awareness level of the speaker | `unaware`, `problem`, `solution`, `product`, `most` |
| `type` | Pain, desire, objection, trigger, alternative, outcome, identity, proof | `objection` |
| `jtbd` | Functional, emotional or social job | `emotional: feel in control` |
| `force` | Push, pull, anxiety, habit (JTBD forces of progress) | `anxiety` |
| `intensity` | 1 to 3 (3 = emotional, specific, vivid) | `3` |
| `phrase` | The exact words worth reusing | "I was rinsing it three times and it still smelled" |

Keep quotes verbatim, including grammar and slang. Paraphrase kills the value. Do not include personal data (names, emails, handles) in outputs; cite the source location only.

## 3. Review mining

**Where:** own site reviews (export from Okendo, Yotpo, Judge.me, Trustpilot, Reviews.io), Amazon (own and competitor ASINs), Google Business Profile, app stores, G2, Capterra, TrustRadius (B2B), Etsy, Sephora or retailer sites.

**Sampling rules**
- Read 5 star reviews for outcomes and identity language ("finally", "I'm the kind of person who").
- Read 3 star reviews for nuanced objections and unmet needs. They are the richest.
- Read 1 and 2 star competitor reviews for switching triggers and "us vs them" angles.
- Sort by most recent first (last 12 months) to stay current, then by most helpful.
- Stop when new reviews stop producing new tags (saturation), usually 80 to 150 reviews per product.

**Claude procedure with an export**
1. Load the CSV from `ads-master/data/imports/`. Confirm columns (rating, date, text, product).
2. Filter to last 12 months. Stratify: up to 50 of 5 star, all 3 star (cap 100), up to 50 of 1 and 2 star.
3. Tag each review with the schema. Extract only phrases with intensity 2 or 3.
4. Cluster by `type` then by theme. Count frequency per theme and record 3 best verbatim quotes each.
5. Output a table: Theme | Type | Count | Share | Best quotes | Angle candidate.

Example of a theme row:

| Theme | Type | Count | Share | Best quotes | Angle candidate |
|-------|------|-------|-------|-------------|-----------------|
| Smell persists after washing | Pain | 23 | 19% | "rinsed it three times and it still smelled" | Problem agitation: "If you rinse twice, this is for you" |

## 4. Reddit, forum and community mining

**Search patterns (paste into Google)**
- `site:reddit.com "<problem phrase>"`
- `site:reddit.com "<competitor>" (alternative OR switched OR "worth it")`
- `site:reddit.com/r/<subreddit> "<category>" "recommend"`
- `"<category>" "anyone else" site:reddit.com`
- `"<product type>" "I wish" OR "I hate" site:reddit.com`
- For B2B: `site:reddit.com/r/<role subreddit> "<task>" "how do you"`

**What to capture**
- The words people use before they know solutions exist (unaware and problem aware language).
- "I tried X, Y, Z and nothing worked" lists. They are ready made "failed solutions" angles.
- Identity statements ("as a nurse on night shifts", "as a solo founder").
- Threads with high upvotes on a complaint: proof of shared pain.
- Myths and misconceptions the category holds (education angles).

**Also mine:** TikTok and YouTube comments on competitor and category videos (questions and objections), Facebook groups, Discord servers, niche forums, Quora, Amazon Q&A, YouTube review videos (titles and comments).

Use communities for language and sentiment, never as statistical evidence.

## 5. Sales call, demo and support ticket mining

**Inputs:** Gong, Chorus, Fireflies, Zoom transcripts; Zendesk, Intercom, Help Scout tickets; live chat logs; returns and cancellation reasons; win/loss notes in the CRM.

**Prompts to run over transcripts (one call or ticket batch at a time)**
1. "List every objection the buyer raised, verbatim, with timestamp."
2. "What triggered them to look for a solution now? Quote."
3. "What alternatives did they mention (competitors, DIY, doing nothing)?"
4. "What outcome did they describe wanting, in their words?"
5. "Which question took the rep longest to answer?"

**Ticket mining:** pull the top 20 ticket categories by volume. Pre-purchase questions become FAQ ads and objection handling statics. Post-purchase "how do I" tickets reveal onboarding friction (and expectation gaps the ads may be creating).

**Lost deal and cancellation reasons** reveal which promises the ads should stop making or must qualify.

## 6. Search query mining

| Source | How | What it gives creative |
|--------|-----|------------------------|
| Google Ads search terms report (last 90 days, converting terms) | Export, sort by conversions | The words buyers use at high intent; RSA headlines; problem language |
| Search Console queries | Export queries with impressions | Questions and comparisons ("X vs Y", "is X worth it") |
| Google autocomplete and People Also Ask | Manual or tool | Question hooks, myth busting angles |
| Amazon search suggestions | Type the category | Feature language buyers filter by |
| TikTok search suggestions | Type the category in TikTok search | Native phrasing for hooks |
| ChatGPT and AI assistant prompts (if `ai-search-optimization` has prompt data) | Read their outputs | Conversational intent phrasing for ChatGPT ads |

Rule: comparison and "alternative to" queries become us vs them concepts; "how to" and "why does" queries become education and problem aware hooks; "best <category> for <segment>" queries become persona concepts.

## 7. Competitor ad library analysis

| Library | URL | What you can see | Caveats |
|---------|-----|------------------|---------|
| Meta Ad Library | facebook.com/ads/library | Active ads of any Page, start date, platforms, variations; in the EU, extra data (reach, targeting summary) for ads delivered there | Outside the EU and outside political ads, no spend or performance data. Long running is a weak proxy for winning |
| Meta Ad Library API (`ads_archive`) | developers.facebook.com | Programmatic access for political and EU delivered ads | Commercial ads outside the EU not covered by the API [Practitioner consensus; verify] |
| TikTok Creative Center (Top Ads, Creative Insights, Trends, Keyword Insights) | ads.tiktok.com/business/creativecenter | Top performing ads by region, industry, objective, with some metrics like CTR or likes bands; trending sounds and hashtags | "Top" is TikTok's selection; region and filters vary; requires login for some features |
| TikTok Commercial Content Library | library.tiktok.com | Ads shown in the EU (DSA transparency) | EU only |
| Google Ads Transparency Center | adstransparency.google.com | Ads by advertiser across Search, Display, YouTube, by region and date | No performance data; text ads shown as rendered |
| LinkedIn Ad Library | linkedin.com/ad-library | Ads run on LinkedIn in the last year by company or keyword; targeting and impressions data for EU ads | Limited filtering |

**Procedure**
1. List 3 to 8 competitors from `COMPETITORS.md` plus 2 adjacent brands that sell to the same persona in a different category.
2. For each, capture every active ad: format, hook (first line and first frame), angle, persona, awareness level, offer, CTA, start date.
3. Flag ads active 60+ days and ads with many variations (multiple versions of the same concept often indicate a winner being iterated). Treat both as signals, not proof.
4. Build the competitor angle map: rows = angles, columns = competitors. Empty cells are white space.
5. Note format gaps (no one runs founder story, no one runs comparison statics).
6. Save screenshots or links in a swipe file, not in the repo. Reference by URL.

**Swipe file structure** (Foreplay, Atria, Notion or a folder): brand, URL, capture date, format, hook text, angle, awareness, offer, why it might work, what we would do differently. Never copy a competitor ad. Extract the principle, then rebuild with your own VOC.

## 8. Surveys that feed creative

**Post-purchase survey (ecommerce, 3 questions max)**
1. "What almost stopped you from buying today?" (objections)
2. "What were you using or doing before this?" (alternatives, switching)
3. "How did you first hear about us?" (with options plus "other")

Tools: KnoCommerce, Fairing, Zigpoll, Typeform, Shopify post-purchase extensions.

**B2B onboarding survey:** "What problem made you start looking?", "What else did you evaluate?", "What nearly made you choose them?"

**Lead gen:** add one optional free text field to the form or thank you page: "What is the main thing you want help with?"

## 9. Synthesis outputs

The VOC bank file has these sections:
1. Sources used (with dates and counts)
2. Top pains (theme, count, share, best 3 quotes)
3. Top desires and outcomes
4. Top objections with how each is currently answered (or not)
5. Triggers (what starts the search now)
6. Alternatives and failed solutions
7. Identity language (who they say they are)
8. Competitor angle map and white space
9. Search and question language
10. Angle candidates (each with the quotes that justify it)
11. Proposed edits to `AUDIENCE.md` (for human approval)

## 10. Quality bar for research

- At least 3 independent source types (for example reviews, Reddit, calls).
- At least 50 tagged quotes for a single product business; 30 per segment for multi-segment.
- Every angle candidate cites at least 2 quotes from at least 2 sources.
- Dates recorded for every source; nothing older than 24 months unless evergreen.
- No personal data in outputs.

## 11. Common mistakes

| Mistake | Why it costs money | Fix |
|---------|-------------------|-----|
| Reading only 5 star reviews | Produces bland benefit ads, misses objections | Prioritize 3 star and competitor 1 to 2 star |
| Paraphrasing quotes | Loses the specific language that makes hooks work | Verbatim only |
| Copying competitor ads | Similar concepts, legal risk, no differentiation | Extract principle, rebuild with own VOC |
| Treating long running competitor ads as proven winners | Some brands never prune | Treat as a signal; validate with your own tests |
| Skipping sales calls in B2B | Misses the real objection set | 10 calls minimum per quarter |
| One-off research | VOC goes stale, angles repeat | Quarterly sprint plus ongoing survey |
