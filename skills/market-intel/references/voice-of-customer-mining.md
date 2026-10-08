# Voice of Customer Mining

Collect what customers and the category's buyers actually say, code it, count it, and hand the exact words to creative-strategy, cro, seo and ai-search-optimization.

## 1. Sources
| Source | Best for | Access and limits |
|--------|----------|-------------------|
| Our reviews (site, Google Business Profile, Trustpilot, app stores, marketplaces) | Delights, outcomes, language | Own data; export via platform tools or APIs for own profiles |
| Competitor reviews (G2, Capterra, TrustRadius, Trustpilot, Amazon, app stores, marketplaces, Google Maps) | Pains with alternatives, switching reasons, unmet needs | Public pages; read and sample manually or through licensed tools; check terms before automated collection |
| 1 to 3 star competitor reviews | Objections, failures, "I wish" statements | Highest value for angles [Practitioner consensus] |
| 3 star reviews (ours and theirs) | Balanced pros and cons, decision criteria | |
| Reddit and forums | Unfiltered problems, comparisons, recommendations, jargon | Reddit Data API terms limit commercial use; manual reading of public threads is fine; no automated bulk collection without permission |
| YouTube comments, TikTok comments | Reactions to products and demos, objections | YouTube Data API for public comments within quota and terms; TikTok manual |
| Social listening tools (Brandwatch, Talkwalker, Meltwater, Brand24 and similar) | Volume and sentiment over time, mentions across web | Licensed data |
| Support tickets, chat logs | Post purchase problems, confusion | First-party; remove personal data |
| Sales call recordings and notes (Gong and similar) | Objections, decision criteria, competitor mentions | First-party with consent |
| Surveys (post purchase, onboarding, churn, cart abandon) | Quantified reasons and verbatims | First-party |
| Customer interviews (JTBD switch interviews) | Triggers and forces behind switching | First-party, consented |
| Complaint sites (for example Şikayetvar in Turkey) | Category pain points and service failures | Public pages; manual sampling |
| Search queries (Search Console, People Also Ask, autocomplete) | Questions in the buyer's words | Own and public |

## 2. Collection rules
1. Define the decision and segment first (for example "angles for new customer acquisition of busy parents in the UK").
2. Sample deliberately: at least 3 source types per segment; for reviews, aim for 200+ reviews across competitors, weighted to the last 12 months [Practitioner consensus].
3. Copy verbatims exactly; record source, date, rating, product, URL. Strip names, usernames and any personal data.
4. Prefer manual reading or licensed tools; do not bypass logins, paywalls or rate limits; follow each platform's terms (tools-api-mcp.md).
5. Store the raw sample in `ads-master/data/imports/` only if the human approves; otherwise keep coded excerpts in the output.

## 3. Coding frame
| Code | Definition | Example verbatim pattern |
|------|-----------|--------------------------|
| Trigger | Event that started the search | "After my second kid was born..." |
| Pain | Problem in their words | "I was spending every Sunday fixing spreadsheets" |
| Desired outcome | What success looks like | "I just want it to run without me" |
| Objection | Reason to hesitate | "Looked too good to be true" |
| Anxiety | Fear about switching or buying | "Worried my data would not import" |
| Alternative | What they used or considered | "We tried X and Y before" |
| Decision criterion | What decided it | "Support answered in 5 minutes" |
| Delight | Unexpected positive | "Did not expect the handwritten note" |
| Disappointment | Unmet expectation | "Battery died in a week" |
| Exact phrase | Memorable wording worth reusing | "set it and forget it" |
| Segment signal | Who they are | "As a solo dentist..." |

JTBD forces (for switching analysis): push of the current situation, pull of the new solution, anxiety of the new, habit of the present. Code each verbatim to one force where relevant.

## 4. Quantify
| Theme | Mentions | Share of sample | Sources | Example verbatims (2 to 3) | Segment |
|-------|----------|-----------------|---------|-----------------------------|---------|
Rules:
- Report sample size and date range.
- A theme needs at least 5% of mentions or 10+ mentions to be called a pattern; below that it is a signal to watch [heuristic].
- Separate our customers from competitor customers and from category discussions.
- Use LLM assisted clustering only with human review of a random 10% sample of assignments.

## 5. Review mining method (step by step)
1. Pick 3 to 5 competitors and our own product.
2. Pull the most recent 100 reviews per product where available (more for high volume products), plus all 1 to 3 star reviews from the last 12 months.
3. Code each review with the frame (multiple codes allowed).
4. Build three lists: top pains with alternatives, top desired outcomes, top objections.
5. Extract 20 to 40 exact phrases with high specificity (numbers, situations, emotions).
6. Translate into: angles (creative-strategy), objection handling blocks and FAQ (cro), comparison and FAQ content (seo, ai-search-optimization), proof gaps (growth-orchestrator for review programs).

## 6. Reddit and community mining
1. Find relevant subreddits and threads: Google search with `site:reddit.com <category> <problem>`, Reddit search, Reddit Answers where available.
2. Read the top threads of the last 12 to 24 months; note recurring questions, recommended brands, complaints and the vocabulary used.
3. Track which brands get recommended and why (this also shapes AI assistant answers, since AI engines often cite Reddit) [Practitioner consensus].
4. Never post as a fake customer or astroturf. Engagement by the brand must be transparent and follow subreddit rules.

## 7. Outputs and where they go
| Output | Goes to | Format |
|--------|---------|--------|
| Language bank (exact phrases by theme) | creative-strategy, cro, AUDIENCE.md proposal | Table with source and date |
| Pains, outcomes, objections ranked | creative-strategy, cro | Ranked table |
| Questions buyers ask | seo, ai-search-optimization, AUDIENCE.md "Questions they ask" | List with source |
| Competitor weakness map | creative-strategy, growth-orchestrator | Table by competitor |
| Segment signals | growth-orchestrator, channel agents (targeting and messaging) | Segment notes |
| Proof gaps (claims we cannot support yet) | human, BRAND.md proposal | List |

## 8. VoC report structure
1. Summary and decision served.
2. Sample: sources, counts, date ranges, markets, languages.
3. Top themes with frequencies and verbatims (pains, outcomes, objections, triggers, criteria).
4. Competitor weakness map.
5. Language bank (20 to 40 phrases).
6. Recommendations by owner, with hypotheses for EXPERIMENTS.md.
7. Proposed edits to AUDIENCE.md (quotes, segments, questions), for human approval.

## 9. Ethics and privacy
- Customer quotes used in ads require permission from the reviewer when they are presented as testimonials; VoC phrases used as inspiration for copy do not quote people [Practitioner consensus; check local law and platform policy].
- Never fabricate reviews or present paraphrases as quotes. Fake reviews and testimonials are prohibited in the US (FTC rule, 2024), UK (DMCC Act 2024) and EU consumer law [Practitioner consensus].
- Under GDPR and KVKK, collecting identifiable data from public reviews still counts as processing personal data: minimize, anonymize, and keep only what the analysis needs.

## 10. Pitfalls
- Reading only 5 star reviews of our own product.
- Paraphrasing and losing the customer's exact words.
- Over weighting one loud Reddit thread.
- Mixing segments, then writing generic angles.
- Leaving personal data in shared files.

## 11. Survey question bank (first-party VoC)
| Moment | Question | Type |
|--------|----------|------|
| Post purchase | What almost stopped you from buying today? | Open |
| Post purchase | Which other options did you consider? | Multi select + other |
| Post purchase | How did you first hear about us? (include "AI assistant such as ChatGPT", "Reddit or forum", "Creator or influencer") | Single select + other |
| Post purchase | What is the main thing you hope this will do for you? | Open |
| Onboarding (SaaS) | What were you using before, and why did you switch? | Open |
| Cart or exit | What is stopping you from completing your order? | Single select + open |
| Churn | What is the main reason you are leaving? | Single select + open |
| NPS follow up | What is the one thing we could do better? | Open |
Keep surveys to 1 to 3 questions; open questions produce the language bank.

## 12. JTBD switch interview guide (30 to 45 minutes)
1. First thought: when did you first realize you needed something different? What was happening?
2. Passive looking: what did you notice or try before actively searching?
3. Active looking: where did you look (search, AI assistants, friends, reviews, communities)? What did you compare?
4. Deciding: what made you choose? What nearly made you choose something else?
5. Anxieties: what worried you about switching?
6. First use: what happened in the first week? Did it match expectations?
Code answers to the four forces (push, pull, anxiety, habit) and the timeline.

## 13. Worked coding example (illustrative verbatims written for this guide, not real customer quotes)
| Verbatim (anonymized) | Source | Codes |
|-----------------------|--------|-------|
| "We were losing two hours every Monday reconciling bookings across three calendars" | G2 review of competitor, 2026-08 | Pain, exact phrase, segment signal (multi location) |
| "Switched after the third double booking in a week" | Reddit thread, 2026-07 | Trigger, alternative (implied) |
| "I worried our patient data would not import cleanly" | Sales call note, 2026-09 | Anxiety, objection |
| "Support answered in five minutes on a Saturday" | Our Trustpilot, 2026-09 | Decision criterion, delight |
Resulting angle for creative-strategy: "Get your Mondays back" (pain plus outcome), proof needed: time saved data; objection block for cro: data import guarantee.
