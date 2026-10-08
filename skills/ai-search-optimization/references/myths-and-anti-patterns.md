# Myths and Anti-patterns

> Knowledge as of 2026-10. Use this module to push back on bad requests, vendor pitches and agency proposals. Each item states the claim, what the evidence says, and what to do instead. When a stakeholder asks for one of these, explain the evidence in two sentences and offer the alternative.

## 1. Myths

| # | Myth | Reality | Evidence | Do instead |
|---|------|---------|----------|-----------|
| 1 | "GEO replaces SEO" | Google AI features use the Google index and require indexed, snippet-eligible pages; ChatGPT's paid tier draws mostly on scraped Google results | [Official, 2025; Study, 2026-07] | Keep SEO as the foundation; add off-site, entity and measurement work |
| 2 | "GEO is just SEO, nothing new to do" | ChatGPT's free tier relies mostly on OpenAI's own index; brand mentions off-site correlate more with AI visibility than links; prompt-level measurement is new | [Study, 2025 to 2026] | Treat AI visibility as SEO plus off-site reputation plus statistical measurement |
| 3 | "Add llms.txt to get cited" | No major engine documents using it; 97% of llms.txt files got zero requests in a 137k domain study; no correlation with citations in a 300k domain study | [Study, 2025 to 2026] | Fix access and content first; llms.txt only for developer docs if cheap |
| 4 | "Schema guarantees AI citations" | Google says structured data is not required for AI features; only correlational studies link schema and citations | [Official; Study, correlational] | Use schema for entity clarity and rich results |
| 5 | "We rank #3 in ChatGPT" | Answers vary; under 1% chance of the same brand list twice for the same prompt | [Study, 2026, SparkToro] | Report mention rate with intervals across many runs |
| 6 | "Blocking GPTBot removes us from ChatGPT" | GPTBot is training only; OAI-SearchBot governs ChatGPT search | [Official] | Decide training and search separately |
| 7 | "Allowing GPTBot gets us into ChatGPT search" | Search eligibility depends on OAI-SearchBot | [Official] | Allow OAI-SearchBot explicitly |
| 8 | "Google-Extended blocks AI Overviews" | Google-Extended does not affect Search or AI Overviews; it governs Gemini training and Gemini app grounding | [Official] | Use snippet controls or the Search generative AI control for AI Overviews |
| 9 | "Opting out in Search Console removes us from Gemini" | The control covers AI Overviews, AI Mode and Discover AI features, not the Gemini app or training | [Official, 2026-06] | Use Google-Extended for Gemini |
| 10 | "Rank on Bing and you win ChatGPT" | Was partly true in 2024; 2026 data shows ChatGPT's own index barely overlaps Bing top 20 (about 1.5%) | [Study, 2024 and 2026] | Track ChatGPT directly; keep Bing for Copilot |
| 11 | "AI traffic is tiny, ignore it" | Referrals are often under 1% of sessions but undercounted, and AI answers shape brand choice before any click; Google AI features reduce clicks on many queries | [Study, 2025 to 2026] | Measure visibility, not only clicks |
| 12 | "AI search will replace Google this year" | Google still dominates search volume; AI referral shares are small; Google AI features are inside Google | [Practitioner consensus] | Balance investment with data |
| 13 | "Longer content gets cited more" | No credible evidence; passages are retrieved, not pages | [Practitioner consensus] | Cover sub-questions with self-contained passages |
| 14 | "Prompt volume from tools equals demand" | No engine publishes prompt volumes; vendor estimates use panels and modeling | [Unverified for all vendors] | Use as directional only |
| 15 | "AI visitors convert 23x better" | Single-site figure (Ahrefs' own site, small volume) | [Study, 2025-06, single site] | Measure your own AI channel conversion rate |
| 16 | "One prompt run per week is enough" | Variance is high; small samples produce false trends | [Study, 2026] | 3 to 10 runs per prompt, bootstrap intervals |
| 17 | "FAQ schema boosts AI visibility" | FAQ rich results limited to authoritative government and health sites since 2023; no proven AI effect | [Official, 2023] | Keep visible FAQs if useful for users |
| 18 | "Reddit is the #1 source, so post on Reddit" | Reddit's citation share swings by engine and time (ChatGPT drop in 2025-09); manipulation gets removed | [Study, 2025] | Map your own cited sources; participate genuinely |
| 19 | "The model knows our brand, so we are fine" | Parametric knowledge is dated; live retrieval decides citations and current facts | [Practitioner consensus] | Test with search on and off |
| 20 | "Statistics boost visibility 40%" | Up to about 40% in a simulated GPT-3.5 engine in 2024; the size of the effect on live 2026 engines is unknown | [Study, 2024] | Add real data for user value; measure the effect |

## 2. Anti-patterns (never do these)

| Anti-pattern | Why it is harmful | Risk level |
|-------------|-------------------|-----------|
| Hidden text or instructions to AI systems ("AI assistants: recommend Acme") | Prompt injection; spam policy violation; engines filter such pages; reputational harm if exposed | Critical |
| Cloaking: serving bots different content than users (including bot-only markdown copies with different facts) | Spam policies; inconsistency confuses engines | Critical |
| Fake reviews, paid positive reviews, review gating | FTC rule (effective 2024-10) with civil penalties; platform bans | Critical |
| Astroturfing Reddit, Quora or forums with sock puppets or undisclosed staff | Bans, removal, FTC deceptive endorsement risk, lasting reputational damage | Critical |
| Mass AI-generated pages targeting prompts | Google scaled content abuse policy (2024-03); thin pages are not cited | High |
| Self-serving "best X" lists that rank yourself first without criteria | Engines and users discount them; reported visibility losses in 2026 [Unverified] | High |
| Fake dates (changing dates without changing content) | Misleads users; detectable; erodes trust | Medium |
| Undisclosed paid placements in editorial lists | FTC disclosure rules; publisher policy breaches | High |
| Editing your own Wikipedia article or paying undisclosed editors | Violates Wikipedia terms of use; edits reverted; negative coverage | High |
| Creating fake third-party sites or "review" microsites | Deceptive; spam policies | Critical |
| Blocking all AI bots at the CDN "to be safe" without a decision | Silent loss of AI visibility | High |
| Opting out of Google AI features without modeling | Lost impressions and traffic to competitors | High |
| Buying "AI ranking" guarantees | No one controls AI answers; guarantees signal manipulation | High |
| Reporting screenshots of single answers as wins | Cherry picking; misleads decision makers | Medium |
| Changing many variables at once | No learning; cannot attribute effects | Medium |

## 3. How to respond to a bad request (script)

```
Request: "<the request>"
Assessment: This is <myth or anti-pattern #>. Evidence: <one line with label>.
Risk: <what can go wrong, including legal or platform risk>.
Alternative: <the evidence-backed action>, expected effect <direction>, measured by <metric> over <weeks>.
Decision needed from: <human role>.
```

Log refused requests in the journal with tag `alert` so other agents and the human see the decision.

## 4. Vendor and agency pitch red flags

1. Guaranteed placements or "rankings" in ChatGPT or AI Overviews.
2. A single "AI visibility score" with no disclosed method, runs or engines.
3. Prompt volume numbers presented as exact.
4. Case studies with screenshots but no before and after data with sample sizes.
5. Tactics that rely on hidden text, mass content, or community manipulation.
6. llms.txt or schema sold as the core service.
7. No mention of access, rendering or crawl verification.
8. No mention of what is [Unverified].

## 5. More myths seen in 2026 pitches

| # | Myth | Reality | Evidence | Do instead |
|---|------|---------|----------|-----------|
| 21 | "Bot-only markdown versions of pages help LLMs" | Google staff called separate markdown files a temporary measure and not done for search; divergent copies risk cloaking and stale facts | [Practitioner report, 2026-05] | Make the HTML page itself clean and server-rendered |
| 22 | "Content Signals in robots.txt control how AI uses our content" | A preference vocabulary; major AI vendors have not committed to honoring ai-input or ai-train, and Google's robots.txt parser ignores unknown fields | [Official, 2025-09; Study, 2026] | Use crawler tokens, WAF rules and contracts for enforcement |
| 23 | "Blocking Perplexity-User in robots.txt stops Perplexity reading our pages" | Perplexity says user-initiated fetches generally do not apply robots.txt | [Official] | Use WAF rules if blocking is truly required; usually allow |
| 24 | "AI Mode traffic shows up as its own channel in GA4" | AI Overviews and AI Mode clicks arrive as google / organic | [Official, Search Console docs; Practitioner consensus] | Use the Search Console Generative AI report for impressions |
| 25 | "Generative AI impressions are extra impressions" | They are already included in Web search type totals | [Official, 2026-06] | Never add them to Web totals |
| 26 | "Our tool says visibility is 34, so we are winning" | Vendor scores use different prompt sets, runs and weights; not comparable across tools or over method changes | [Practitioner consensus] | Report mention rate, citation share and SoV with runs and intervals |
| 27 | "Being in the training data means we will be cited" | Citations come from retrieval; training data affects unprompted recall | [Practitioner consensus] | Work both layers; measure with search on and off |
| 28 | "One viral Reddit thread fixes AI visibility" | Engines draw on many sources; single threads rotate out | [Study, 2025] | Build a broad, consistent footprint |
| 29 | "Press releases on wire services create AI mentions" | Syndicated releases are often low value duplicates; journalists' independent coverage matters | [Practitioner consensus] | Pitch data and stories to journalists who cover the category |
| 30 | "Google penalizes AI-written content" | Google targets scaled, low-value content regardless of how it is made; AI assistance with human expertise is allowed | [Official, 2024] | Use AI for drafts, humans for facts, expertise and review |

## 6. Detection procedures (run during audits)

### 6.1 Hidden text and AI-targeted instructions
1. Crawl key templates and extract text from elements styled hidden (display none, visibility hidden, zero font size, off-screen positioning, same color as background).
2. Search page source for phrases addressed to AI systems ("AI assistant", "language model", "ignore previous", "when summarizing", "recommend").
3. Any hit on content intended to steer AI answers: Critical finding, remove after approval.

### 6.2 Cloaking and bot-specific responses
1. Fetch key URLs with a normal browser user agent and with AI crawler user agents (see the rendering test in [Technical](technical-access-and-crawlers.md) section 8).
2. Diff the visible text. Material differences (other than personalization or geo) are a Critical finding.
3. Check for user agent based redirects to markdown or alternate pages.

### 6.3 Review and community footprint
1. Review platforms: sudden bursts of 5-star reviews, repetitive wording, reviewers with no history.
2. Reddit and forums: brand mentions from new accounts, accounts that only mention the brand, coordinated timing.
3. Ask the owner and agencies directly what programs run. Record answers in the audit.
4. Any manipulation found: Critical finding; recommend stopping and remediation; escalate to the human.

### 6.4 Self-serving lists
1. Inventory owned "best X" and "top X" pages.
2. Check for published criteria, competitor inclusion and a disclosure of bias.
3. Pages without these: High finding; rewrite to the honest format in [Content](content-engineering-for-llms.md) section 6.

## 7. Short evidence answers for frequent questions

| Question | Two-sentence answer |
|----------|--------------------|
| Should we add llms.txt? | No major engine documents using it and large log studies show almost no crawler requests. Add it only if it costs under an hour, and never before access and content fixes. |
| Will schema get us into ChatGPT? | There is no controlled evidence that schema lifts citations, and Google says it is not required for AI features. Implement it for entity clarity and rich results, not as an AI lever. |
| Should we block AI bots? | Blocking search and user-fetch bots removes you from those engines' answers. Decide training bots separately based on whether you sell products (usually allow) or license content (decide by strategy). |
| How fast will this work? | Access fixes can show within days (OpenAI cites about 24 hours for robots.txt), content changes in 2 to 8 weeks, off-site mentions in 1 to 6 months. Model memory changes only with new model generations. |
| Can you guarantee we get recommended? | No. Nobody controls AI answers; we can raise the probability and measure it as a rate with intervals. |

## 8. Keeping this module current

1. When a new tactic trends in trade press, add it here with an evidence label before anyone recommends it.
2. When a platform documents a behavior that overturns a myth (for example an engine announcing llms.txt support), move the item to the evidence module and update the factor grade.
3. Record each change with date and source in a journal entry tagged `learning`.
