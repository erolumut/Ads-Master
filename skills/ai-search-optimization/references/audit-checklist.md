# AI Search Visibility Audit Checklist (Scored)

> Knowledge as of 2026-10. Run the full audit at onboarding and quarterly; run section A monthly. Score every item, state the evidence used (file, tool, date range), and convert failures into a prioritized change list. Nothing is changed live without approval.

## How to score

| Severity | Weight | Meaning |
|----------|--------|---------|
| Critical | 5 | Blocks visibility or creates legal or reputational risk |
| High | 3 | Large effect on mentions, citations or accuracy |
| Medium | 2 | Meaningful but secondary |
| Low | 1 | Hygiene |

Each item scores Pass (full weight), Partial (half weight), Fail (0) or N/A (excluded). Section score = points earned / points possible. Overall score = sum earned / sum possible across sections, as a percentage.

## A. Access and crawlability

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | robots.txt allows OAI-SearchBot on public content | Required for ChatGPT search [Official] | Read robots.txt; test group matching | Critical | Add explicit allow group |
| A2 | robots.txt allows Claude-SearchBot and Claude-User | Claude visibility [Official] | Same | High | Add allow group |
| A3 | robots.txt allows PerplexityBot | Perplexity index [Official] | Same | High | Add allow group |
| A4 | Googlebot and Bingbot allowed; no accidental disallow of key sections | Google AI and Copilot depend on them | Same plus GSC and BWT robots reports | Critical | Correct rules |
| A5 | Named groups repeat private-path disallows | RFC 9309 group matching | Read file | Medium | Duplicate disallows per group |
| A6 | Training bot policy (GPTBot, ClaudeBot, CCBot, Google-Extended, Applebot-Extended, Meta-ExternalAgent) is a documented decision | Avoid accidental loss of Gemini grounding or future recall | Ask owner; check journal | High | Write decision with trade-offs |
| A7 | CDN or WAF does not block or challenge allowed bots | Silent blocks are common | Logs: status codes per token (30 days); Cloudflare AI Crawl Control | Critical | Allowlist verified bots |
| A8 | Cloudflare 2026-09-15 defaults reviewed (if on Cloudflare) | Agent and training bots blocked by default on ad pages for new and free sites [Official, 2026-07, via trade press] | Cloudflare dashboard bot and AI settings | High | Set explicit per-crawler actions |
| A9 | Key pages return 200 quickly to bots | User-fetch bots time out on slow pages [Practitioner consensus] | curl timing, logs | Medium | Performance fixes |
| A10 | Key content present in raw HTML | AI crawlers do not render JS [Study, 2024-12] | Rendering test script | Critical | SSR, SSG or prerender |
| A11 | No accidental noindex, nosnippet, data-nosnippet or restrictive max-snippet on content to be cited | These exclude content from Google AI features [Official] | Crawl templates; GSC URL Inspection | Critical | Remove directives |
| A12 | Search generative AI control set to Include (or an approved Exclude decision exists) | Exclude removes AIO and AI Mode visibility [Official, 2026-06] | GSC Settings | High | Restore or document |
| A13 | XML sitemaps valid with honest lastmod; IndexNow live | Freshness in Bing and Copilot | Sitemap fetch; IndexNow key file | Medium | Fix generation; implement IndexNow |
| A14 | Canonicals and hreflang correct on key pages | Wrong market prices cited | Crawl | Medium | Correct tags |

## B. Search foundation

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Key pages indexed in Google | Required for AIO and AI Mode [Official] | GSC Pages report, URL Inspection | Critical | Hand off to `seo` |
| B2 | Key pages indexed in Bing | Copilot grounding | BWT URL Inspection | High | Hand off to `seo` |
| B3 | Rankings for priority sub-queries (top 10 Google and Bing) | Ranking feeds AIO, AI Mode and ChatGPT paid citations [Study] | Rank data, GSC | High | Content and SEO plan |
| B4 | GSC and BWT verified, AI reports accessible | First-party AI data | Log in | High | Verify properties |
| B5 | No major technical SEO debt on key templates | Indexing and quality | `seo` audit | Medium | Hand off |

## C. Entity and brand

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Brand fact sheet exists and is current | Single source of truth | Outputs folder | High | Create |
| C2 | Organization schema with stable @id, logo, sameAs | Entity disambiguation | Validator | Medium | Implement via `seo` |
| C3 | Product, LocalBusiness, Person, Article schema where relevant and matching visible content | Clarity, rich results | Validator | Medium | Implement |
| C4 | Profiles (LinkedIn, Crunchbase, review platforms, GBP, Bing Places, Apple Business Connect) match the fact sheet | Consistency across sources | Manual check | High | Update profiles |
| C5 | Wikidata item exists (if eligible) and is accurate with references | Reference source for engines | Wikidata search | Medium | Create or correct with sources |
| C6 | Wikipedia article (if exists) accurate; COI process followed | ChatGPT cites Wikipedia heavily [Study, 2025] | Read article, Talk page | Medium | Talk page requests with sources |
| C7 | Knowledge Panel present and claimed (if eligible) | Entity recognition | Brand SERP | Low | Claim and suggest edits |
| C8 | NAP consistent across listings (local) | Local answers | Citation audit | High (local) | Correct listings |

## D. Content engineering

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Public pricing page with numbers and date (or clear ranges) | Pricing prompts; transparency | Visit page | High | Publish or clarify |
| D2 | Comparison pages for top competitors, accurate and dated | "vs" prompts | Content inventory | High | Create or refresh |
| D3 | Alternatives page(s) | Switching prompts | Inventory | Medium | Create |
| D4 | Category guide with honest criteria | "best X" prompts | Inventory | High | Create |
| D5 | Use case or segment pages with proof | Segment prompts | Inventory | Medium | Create |
| D6 | Answer-first sections naming the entity | Passage retrieval | Sample 10 key pages | High | Rewrite openings |
| D7 | Statistics, quotes and sources on key pages, real and dated | GEO paper methods [Study, 2024] | Sample pages | Medium | Add with sources |
| D8 | Tables in HTML for specs and comparisons | Extractable | Sample pages | Medium | Convert |
| D9 | Original data asset published in HTML | Citations and mentions | Inventory | Medium | Plan study |
| D10 | Decision pages refreshed within 90 days with real changes | Freshness [Study, 2025] | Updated dates vs change logs | Medium | Refresh cadence |
| D11 | Fan-out coverage for top 20 prompts at 70% or more of facets | Sub-query coverage | Coverage sheet | High | Content gap briefs |
| D12 | Homepage answers what, who for, price, proof | Rising homepage share of ChatGPT referrals [Study, 2026-05] | Visit homepage | Medium | Rewrite hero and summary |

## E. Off-site footprint

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Source map of cited domains for priority prompts exists (last 90 days) | Targets off-site work | Outputs | High | Build |
| E2 | Brand present and accurate on the top 20 cited third-party pages | Mentions drive AI visibility [Study, 2025] | Source map | High | Outreach and corrections |
| E3 | Review platforms most cited for the category have recent reviews (at least monthly flow) | Recommendation and sentiment | Platform check | High | Review program |
| E4 | YouTube presence answering priority prompts with accurate transcripts | Rising citation source [Study, 2026] | Channel review | Medium | Video plan via `creative-strategy` |
| E5 | Genuine community presence with disclosure where relevant | UGC sources | Search Reddit, forums | Medium | Participation guidelines |
| E6 | No manipulation footprint (fake reviews, sock puppets, undisclosed paid posts) | Legal and platform risk | Review history, ask owner | Critical | Stop and remediate |
| E7 | Digital PR producing mentions on cited domains in last quarter | Mentions | PR log | Medium | PR plan |

## F. Measurement

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Prompt set exists, frozen, with classes and priorities | Trend validity | Outputs | High | Build |
| F2 | Collection uses 3+ runs per prompt, fixed geo, memory off baseline | Variance [Study, 2026] | Tool settings | High | Reconfigure |
| F3 | Metrics reported with intervals and sample sizes | Avoid false trends | Last report | Medium | Use bootstrap script |
| F4 | GA4 AI channel group live and above Referral | AI traffic visibility | GA4 Admin | High | Spec to `measurement` |
| F5 | Self-reported attribution includes AI assistants option | Dark AI traffic | Forms | Medium | Spec to `cro` and `measurement` |
| F6 | GSC Generative AI report reviewed monthly | First-party AIO and AI Mode data | Report log | Medium | Add to cadence |
| F7 | Bing AI Performance and grounding queries reviewed monthly | Fan-out log | Report log | Medium | Add to cadence |
| F8 | User-fetch bot hits tracked from logs | Demand proxy | Log export | Low | Monthly log pull |

## G. Accuracy and sentiment

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Brand prompts (what is, pricing, legit, reviews, vs) answered accurately in 80%+ of runs | Wrong facts cost deals | Entity audit runs | High | Correction workflow |
| G2 | No critical misinformation (safety, legal, scam, discontinued) | Severe harm | Entity audit | Critical | Escalate same day |
| G3 | Net sentiment non-negative across engines | Recommendation likelihood | Rubric scoring | Medium | Address root causes |
| G4 | Competitor confusion absent (name collisions) | Wrong attribution | Brand prompts | Medium | Disambiguation content and schema |
| G5 | Open correction tickets tracked with re-test dates | Closure | Outputs | Low | Ticket log |

## H. Commerce (ecommerce and marketplaces only)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | Products appear in AI shopping answers for top category prompts | Revenue | Shopping prompt runs | High | Diagnose with `commerce-feeds` |
| H2 | Merchant Center and ACP feed healthy (owned by `commerce-feeds`) | Product data | Ask `commerce-feeds` | High | Handoff |
| H3 | Product pages state specs, price, availability, policies in HTML | Extraction and accuracy | Rendering test | High | Template fixes |
| H4 | Product reviews rendered in HTML with counts | Recommendations | Page check | Medium | Implement |
| H5 | Shown prices in AI answers match current prices | Trust and policy | Runs vs feed | High | Feed timing fixes |
| H6 | Checkout usable by agent browsers (no blanket bot blocks on checkout for verified agents) | Agentic purchases | Bot settings, manual test | Medium | Adjust rules |

## I. Governance and risk

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | No hidden text, cloaking or AI-targeted instructions on site | Spam and injection risk | Crawl for hidden elements and bot-specific responses | Critical | Remove |
| I2 | Change approval process for robots.txt, CDN, schema and content exists | Prevent silent breakage | Ask owner | High | Define approvers |
| I3 | Claims on comparison pages substantiated and dated | Legal risk | Review pages | High | Add sources or remove |
| I4 | Regulated category claims reviewed by compliance | Legal | Ask owner | Critical (regulated) | Compliance review |
| I5 | Vendor and agency tactics reviewed against anti-patterns | Reputational risk | Contracts, reports | Medium | Stop non-compliant tactics |

## Scoring rubric

| Overall score | Rating | Interpretation | Next step |
|--------------|--------|----------------|-----------|
| 85 to 100% | Strong | Foundations in place; focus on off-site growth and measurement depth | Optimize and scale plays |
| 70 to 84% | Solid | Some gaps in content or off-site footprint | Fix High items within 60 days |
| 50 to 69% | Weak | Visibility limited by structural gaps | 90 day program from week 1 |
| Under 50% | Critical | Access or accuracy problems likely suppress visibility | Fix all Critical items first, then rerun |

Override rule: any failed Critical item in sections A, E6, G2 or I caps the rating at "Weak" regardless of the score, and is listed first in the change list.

## Audit output template

```
# AI Visibility Audit: <brand>
Date: YYYY-MM-DD | Agent: ai-search-optimization
Data used: <files, tools, date ranges>
Overall score: <x%> (<rating>) | Section scores: A <x%>, B <x%>, C <x%>, D <x%>, E <x%>, F <x%>, G <x%>, H <x% or N/A>, I <x%>

## Critical findings (fix first)
| Item | Evidence | Impact | Fix | Owner | Approval needed |

## Change list (ranked by impact x confidence x ease)
| # | Change | Item | Expected effect | Effort | Owner | Status |

## Baseline visibility (prompt set v1)
| Engine | Mention rate (95% CI) | Citation share | SoV | Runs |

## Handoffs requested
```
