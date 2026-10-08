# AI Visibility Benchmarking

Measure how often AI assistants mention, recommend and cite us versus competitors, and which sources they rely on. market-intel owns the competitive benchmark; ai-search-optimization owns the improvement program.

## 1. Why it matters in 2026
- AI surfaces now sit between buyers and websites: zero click searches reached about 68% of US Google searches in early 2026 (SparkToro) and AI Overviews reduce clicks to organic results (Pew 2025, Seer 2025 to 2026, Ahrefs 2025) [Study].
- Google reported large AI Overviews and AI Mode audiences; WPP counts generative search as a $5.1 billion ad market in 2026 heading to over $100 billion by 2030 [Study, 2026-06].
- ChatGPT added ads in 2026 (self serve in May, 60+ countries by October) [Official and secondary reports], so organic and paid presence in assistants both matter.
- What assistants say about a category is shaped by the sources they retrieve: review sites, community threads, comparison articles, publisher lists and brand pages [Practitioner consensus].

## 2. Engines to cover
| Engine | Surface | Notes for sampling |
|--------|---------|--------------------|
| ChatGPT (with search) | chatgpt.com, apps | Answers vary by account state, memory and location; use a clean logged out or fresh account where possible; note model |
| Google AI Overviews | Google Search | Triggered on many informational queries; record presence and cited links |
| Google AI Mode | Google Search AI Mode tab | Conversational; record brands and links |
| Gemini | gemini.google.com | Similar retrieval to Google; record citations |
| Perplexity | perplexity.ai | Always cites sources; good for citation analysis |
| Microsoft Copilot | copilot.microsoft.com, Bing | Bing index based; record citations |
| Claude | claude.ai with web search | Record when used by the audience (B2B, developers) |
Pick the 3 to 5 engines your audience uses; B2B tech audiences skew to ChatGPT, Perplexity and Claude, mass consumer to Google surfaces and ChatGPT [Practitioner consensus].

## 3. Build the prompt set
| Prompt type | Template | Example |
|-------------|----------|---------|
| Category best | "What are the best <category> for <use case or segment>?" | "best CRM for small real estate teams" |
| Comparison | "<brand A> vs <brand B>" and "<brand> alternatives" | "Brand X alternatives" |
| Problem | "How do I <job to be done>?" | "how to reduce Shopify return rates" |
| Buying criteria | "What should I look for in a <category>?" | |
| Local | "<service> near <city>" or "best <service> in <city>" | |
| Price | "cheapest <category> with <feature>" | |
| Trust | "is <brand> legit" or "<brand> reviews" | |
Sources for prompts: AUDIENCE.md questions, Search Console queries rewritten as natural questions, sales call questions, Reddit thread titles, People Also Ask.
Size: 20 to 50 prompts for Starter and Growth, 100 to 300 for Scale and Enterprise, split by segment and funnel stage. Keep the set stable for trend tracking; add new prompts in a separate cohort.

## 4. Sampling protocol
1. Fix market, language and location (VPN or tool location settings where allowed).
2. Run each prompt at least 3 times per engine per measurement period (answers are probabilistic; repeated runs reduce noise) [Practitioner consensus].
3. Use fresh sessions without memory or personalization when possible; record account state.
4. Record the full answer text, brands mentioned in order, whether each is recommended (positive framing, top pick), sentiment, and every cited URL.
5. Store raw answers with date, engine, model label shown, location.
6. Repeat monthly (weekly for priority prompts at Scale tier or after a major change).

## 5. Metrics
| Metric | Formula | Notes |
|--------|---------|-------|
| Mention rate | Answers mentioning brand / total answers | Core visibility |
| Recommendation rate | Answers recommending brand (top pick or explicit recommendation) / total answers | Closer to revenue |
| Average position | Mean order of first mention when mentioned | Lower is better |
| Share of voice | Brand mentions / all brand mentions in the set | Competitive view |
| Citation share | Answers citing brand's domain / total answers with citations | Source influence |
| Sentiment | Positive, neutral, negative per mention | Use consistent rules |
| Accuracy | Share of mentions with correct facts (price, features, availability) | Errors are fixable leaks |
| Cited domain frequency | Count of citations by domain across all answers | Shows which third party sources to win |

Report per engine and overall, with sample size (prompts x runs).

## 6. Citation source analysis
1. Aggregate cited URLs across engines; group by domain and by type: review platforms (G2, Capterra, Trustpilot), communities (Reddit, Quora), video (YouTube), encyclopedic (Wikipedia), publishers and listicles, marketplaces, brand sites, government or standards bodies.
2. For each high frequency domain, check whether we are present and how we are described (listing quality, review count, rating, thread sentiment).
3. Output a "sources to win" list: domains, current presence, competitor presence, action owner (ai-search-optimization for content and digital PR, seo for links, growth-orchestrator for review programs).

## 7. Competitive benchmark table
| Brand | Mention rate | Recommendation rate | Avg position | Citation share | Sentiment (pos/neu/neg) | Accuracy issues |
|-------|--------------|---------------------|--------------|----------------|-------------------------|-----------------|
| Us | | | | | | |
| Competitor A | | | | | | |
| Competitor B | | | | | | |
Plus per engine breakdown and per prompt type breakdown (category, comparison, problem).

## 8. Tools
| Tool | What it does | Notes |
|------|--------------|-------|
| Manual panel (spreadsheet + this protocol) | Small prompt sets, high control | Time consuming; good for Starter |
| Profound, Peec AI, Otterly.AI, Scrunch, Evertune and similar AI visibility platforms | Automated prompt tracking across engines, share of voice, citations | Methods differ (API vs interface sampling, locations); compare like with like [Unverified current feature sets] |
| Semrush AI visibility features, Ahrefs Brand Radar | AI mention and citation tracking inside SEO suites | Database driven; check engines and markets covered [Unverified current scope] |
| Bing Webmaster Tools AI performance reporting | Microsoft surfaced citation data for your own site | First-party, own site only [Unverified details] |
| GA4 AI referral channel group | Sessions from chatgpt.com, perplexity.ai, gemini.google.com, copilot | Own site only; measurement agent sets it up |
Prompt volume: no official prompt volume data exists from assistants; some tools estimate it. Label such numbers low confidence.

## 9. Interpreting results
| Pattern | Likely cause | Owner |
|---------|-------------|-------|
| Competitor mentioned far more on category prompts | Stronger third party presence (reviews, lists, Reddit), clearer category association | ai-search-optimization, seo |
| We are mentioned but rarely recommended | Weak differentiators in sources, mixed reviews | growth-orchestrator (reviews), creative and brand messaging |
| Wrong facts about us | Outdated pages or third party listings | ai-search-optimization, seo |
| Strong on Perplexity, weak on ChatGPT | Index and source differences | ai-search-optimization |
| Competitor ads appear in ChatGPT for our prompts | Paid presence | chatgpt-ads |

## 10. Pitfalls
- Single run per prompt: noise mistaken for trend.
- Logged in personalized sessions: results reflect the tester, not the market.
- Changing the prompt set every month: no trend.
- Treating tool share of voice numbers from different vendors as comparable.
- Ignoring accuracy: a mention with a wrong price can hurt more than no mention.

## 11. Sampling sheet (one row per answer)
| Date | Engine | Model label | Location | Account state | Prompt ID | Prompt | Run | Brands in order | Recommended brand(s) | Sentiment per brand | Cited URLs | Notes |
|------|--------|-------------|----------|---------------|-----------|--------|-----|-----------------|----------------------|---------------------|-----------|-------|

Scoring rules (apply consistently):
- Mentioned: brand name appears anywhere in the answer.
- Recommended: brand is presented as a top pick, "best for", or explicitly suggested for the user's situation.
- Position: order of first mention among brands.
- Sentiment: positive (praise, strengths), neutral (listed), negative (warnings, weaknesses dominate).
- Accuracy: any factual error about price, features, availability or policy.

## 12. Script: compute rates from the sampling sheet
```python
# python3 -I ai_sov.py answers.csv  (columns as in the sampling sheet; brands separated by ";")
import csv, sys, collections as co
rows = list(csv.DictReader(open(sys.argv[1])))
n = len(rows)
mention, recommend, pos = co.Counter(), co.Counter(), co.defaultdict(list)
for r in rows:
    order = [b.strip() for b in r["Brands in order"].split(";") if b.strip()]
    for i, b in enumerate(order):
        mention[b] += 1; pos[b].append(i + 1)
    for b in [x.strip() for x in r["Recommended brand(s)"].split(";") if x.strip()]:
        recommend[b] += 1
total_mentions = sum(mention.values()) or 1
for b, m in mention.most_common():
    print(f"{b}: mention {m/n:.0%}, recommend {recommend[b]/n:.0%}, avg pos {sum(pos[b])/len(pos[b]):.1f}, SOV {m/total_mentions:.0%}")
```

## 13. Worked example
40 prompts x 3 runs x 3 engines = 360 answers. We are mentioned in 126 (35%), recommended in 54 (15%), average position 3.2. Competitor A: mentioned in 252 (70%), recommended in 151 (42%), average position 1.6. Top cited domains when A is recommended: a review platform (88 citations), Reddit (61), a publisher listicle (40). We have 37 reviews on that platform vs A's 1,900. Recommendation to ai-search-optimization and growth-orchestrator: review generation program and inclusion pitches to the cited listicles, then re-measure in 60 days.
