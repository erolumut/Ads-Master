# How AI Engines Retrieve and Cite

> Knowledge as of 2026-10. Engine internals are mostly undisclosed. Every claim carries an evidence label. Treat anything labeled [Unverified] as a hypothesis to test in your own prompt tracking, never as a fact to sell to a client.

## 1. Two kinds of visibility (never mix them up)

| Layer | What it is | How a brand gets in | How fast it changes | How to test it |
|-------|-----------|---------------------|---------------------|----------------|
| Parametric (training data) | What the model "knows" without searching. Formed from pretraining corpora (Common Crawl, licensed data, Wikipedia, books, code, forums) up to a knowledge cutoff | Be widely and consistently described on the open web, in reference sources and in licensed datasets long before the cutoff | Months to years (next model generation) | Ask the model with web search off (API without search tool, or a chat with search disabled). Record unprompted brand recall and facts it states |
| Retrieval (live grounding, RAG) | Pages the engine fetches or pulls from its index at answer time, then cites | Be crawlable by the engine's crawler, indexed, and among the best matching passages for the sub-queries the engine issues | Hours to weeks | Run the prompt with search on. Record mentions and the cited URLs |

Rules:
1. Citations (linked sources) come almost entirely from the retrieval layer. Unlinked brand recommendations can come from either layer.
2. For new brands, retrieval is the only lever that moves inside a quarter. Parametric presence is a multi-year compounding asset built by the same off-site footprint work.
3. A model can recommend a brand from memory and cite a third-party listicle as the source. Both layers must say the same true things about the brand, or answers become inconsistent.

## 2. The generic answer pipeline

Most AI search products follow the same broad steps. Vendors do not publish the scoring at each step [Practitioner consensus].

| Step | What happens | What you can influence |
|------|-------------|------------------------|
| 1. Intent and need-to-search decision | The system decides whether to answer from memory or search. Fresh, local, commercial, comparison and fact-heavy prompts trigger search more often [Practitioner consensus] | Publish facts that require fresh lookup (prices, availability, specs, dates, data) |
| 2. Query rewriting and fan-out | The prompt is rewritten into several sub-queries (Google calls this query fan-out) [Official, 2025-05]. Memory, location and conversation context can shape the rewrite [Unverified for most engines] | Cover the sub-questions a buyer would ask, not just the head term |
| 3. Retrieval | Each sub-query hits an index: the engine's own, a partner index, or scraped SERPs | Be crawlable by the right bot, indexed, and ranking for the sub-queries |
| 4. Passage selection and reranking | Candidate pages are split into passages. Passages are scored for relevance to the sub-query, often with embeddings plus rerankers [Practitioner consensus] | Write self-contained, specific passages that answer one sub-question each |
| 5. Synthesis | The model writes the answer from selected passages plus its own knowledge | State facts plainly so they survive paraphrase. Provide numbers, names, comparisons |
| 6. Citation attachment | Links are attached to claims, or listed as sources | Be the clearest primary source for a claim. Original data is cited more than rewrites [Practitioner consensus] |
| 7. Personalization and rendering | Memory, location, prior turns and account state alter the final answer and the visible links | Nothing direct. Measure with controlled personas and logged-out runs |

## 3. Engine by engine

### 3.1 Summary matrix

| Engine | Main retrieval source | Crawler or fetcher tokens | Renders JS? | First-party reporting | Key control |
|--------|----------------------|---------------------------|-------------|----------------------|-------------|
| Google AI Overviews | Google Search index via Googlebot, with query fan-out [Official, 2025-05] | Googlebot | Yes (Googlebot renders) [Official] | Search Console Generative AI performance report, impressions only [Official, 2026-06] | nosnippet, data-nosnippet, max-snippet, noindex; Search generative AI control in Search Console [Official, 2026-06] |
| Google AI Mode | Same index, heavier fan-out, Deep Search issues hundreds of searches [Official, 2025-05] | Googlebot | Yes | Same report, combined with AI Overviews [Official, 2026-06] | Same as above |
| Gemini app | Google Search grounding | Googlebot crawls. Google-Extended token governs use for Gemini training and grounding [Official] | Yes | None for sites | Google-Extended in robots.txt. The Search Console opt-out does not cover the Gemini app [Official, 2026-06] |
| ChatGPT search | Mixed. Own index reported as "Labrador", plus third-party providers. Free tier reported about 75% own index; paid tier about 75% scraped Google results [Study, 2026-07] | OAI-SearchBot (index), ChatGPT-User (user-triggered fetch), GPTBot (training) [Official] | No for OAI bots per 2024 logs study [Study, 2024-12] | None. Referrals carry utm_source=chatgpt.com [Practitioner consensus] | Allow OAI-SearchBot. Robots.txt changes take about 24 hours to apply [Official] |
| ChatGPT shopping | Structured product data from merchant feeds (ACP) and third-party providers [Official, 2025 to 2026] | OAI-SearchBot plus feeds | n/a | None public | Merchant feed via ACP (owned by `commerce-feeds`) |
| Perplexity | Own index built by PerplexityBot, plus live fetches [Official] | PerplexityBot (index, honors robots.txt), Perplexity-User (user fetch, generally does not apply robots.txt) [Official] | No [Study, 2024-12] | None | Allow PerplexityBot. Cloudflare delisted Perplexity as a verified bot in 2025-08 after stealth crawling allegations, which Perplexity disputed [Contested] |
| Microsoft Copilot and Bing AI answers | Bing index | Bingbot | Yes (Bingbot renders) | Bing Webmaster Tools AI Performance: citations, cited pages, grounding queries, citation share [Official, 2026-02 and 2026-06] | Standard robots.txt, IndexNow for freshness |
| Claude | Web search tool plus Anthropic's own crawler index [Official]. Brave Search listed as a web search subprocessor (with TurboPuffer) as of 2026-09-02 [Official, 2026-09]; 86.7% overlap with Brave top results [Study, 2025] | Claude-SearchBot (search index), Claude-User (user fetch), ClaudeBot (training). Anthropic says its bots honor robots.txt [Official] | No for ClaudeBot per 2024 logs study [Study, 2024-12] | None | Allow Claude-SearchBot and Claude-User |
| Meta AI | Reported web search partnerships plus Meta crawlers [Unverified] | Meta-ExternalAgent (training and indexing), Meta-ExternalFetcher (user fetch) [Official, verify current names] | Unknown | None | robots.txt per token. Blocking Meta-ExternalAgent may reduce Meta AI visibility [Unverified] |
| Grok (xAI) | X posts plus web search [Practitioner consensus] | No widely documented crawler token [Unverified] | Unknown | None | Presence on X matters more here than anywhere else |
| Apple (Siri, Spotlight, Apple Intelligence) | Applebot index. Applebot-Extended controls use for training only [Official] | Applebot, Applebot-Extended | Yes (Applebot renders) [Study, 2024-12] | None | Apple Business Connect for local facts |
| Amazon (Alexa for Shopping, formerly Rufus in the US; Alexa+) | Amazon catalog, reviews, plus web [Practitioner consensus] | Amazonbot | Unknown | None | Amazon listing quality and reviews |

### 3.2 Google AI Overviews and AI Mode

Facts from Google's documentation [Official, 2025 to 2026]:
1. Eligibility: a page must be indexed and eligible to show with a snippet. There are no additional technical requirements and no special markup.
2. Both features may use query fan-out: multiple related searches across subtopics and data sources. Supporting pages are identified while the response is generated, so the link set is wider than classic results.
3. AI Overviews appear only where Google judges them additive. AI Mode handles longer, exploratory and follow-up queries. Deep Search in AI Mode can issue hundreds of searches [Official, 2025-05].
4. Traffic from AI features is counted in Search Console Performance under the Web search type. Since 2026-06-03 a separate Generative AI performance report shows impressions for AI Overviews and AI Mode combined (no filter to split them), by page, country and date, with no clicks, no CTR, no position and no queries, and no API or BigQuery export. Data starts 2026-05-18. Worldwide since 2026-08-31 [Official, 2026-08].
5. Snippet controls (nosnippet, data-nosnippet, max-snippet, noindex) apply to AI features. Google-Extended does not affect inclusion in Search or AI Overviews.
6. Search generative AI control (Search Console, Settings): property-level Include or Exclude for AI Overviews, AI Mode and Discover AI features. Default Include. Takes one to two days. Does not cover the Gemini app. Not a ranking signal for classic results. Options are Include, Exclude and Inherit from parent. Page-level control is not yet available (the CMA publisher controls conduct requirement, imposed 2026-06-03, gives Google nine months, about 2027-03) [Official, 2026-06 and 2026-08].

Observed behavior [Study and Contested, see evidence module]:
1. Overlap between AI Overview citations and the classic top 10 was reported at 76% in 2025 (Ahrefs), while 2026 analyses report far lower overlap for AI Mode (around 12% in a Moz analysis) [Contested].
2. AI Mode cites more unique domains than AI Overviews (one 2026 analysis: 143% more) [Study, 2026-01, secondary].
3. Models change often: Gemini 3 reached AI Mode on 2025-11-18 and became the AI Overviews default on 2026-01-27 [Official]; Gemini 3.5 Flash became the AI Mode default at I/O 2026-05-19 [Official, 2026-05]; Gemini 3.7 Flash (2026-08-14) and 3.8 Flash (2026-09-02) became selectable for paying subscribers [Official, via trade press]. Free users and paid users can therefore see different models. Re-baseline tracking after model changes.

### 3.3 ChatGPT search

Official facts [Official, OpenAI bots documentation]:
1. OAI-SearchBot surfaces sites in ChatGPT search. Sites that disallow it do not appear in search answers, though they can still appear as navigational links.
2. GPTBot is the training crawler. Blocking it does not remove a site from ChatGPT search.
3. ChatGPT-User fetches pages when a user or a GPT asks. It is not an automatic crawler, and because it is user-initiated, robots.txt rules may not apply. It does not decide search eligibility.
4. OpenAI publishes IP range files for its bots and recommends allowing OAI-SearchBot and its IP ranges. Robots.txt updates take about 24 hours to reflect in search.

Reported architecture [Study, 2026-07; vendor research, treat percentages as indicative]:
1. Between 2026-05-21 and 2026-07-21, ChatGPT exposed a source field per result with four values: an internal index (named Labrador) and three external providers. OpenAI has not publicly named Labrador.
2. Free tier (instant and think modes) drew roughly 75% of sources from Labrador, about 3% from scraped Google web results and about 22% from a provider feeding news. Paid mode roughly reversed this: about 75% scraped Google and 25% Labrador (Resoneo analysis reported via Peec AI and Search Engine Land).
3. Only about 1.5% of Labrador URLs appeared in Bing's top 20 for the same fan-out queries. Bing visibility is no longer a sufficient ChatGPT strategy [Study, 2026-07].
4. Earlier evidence pointed to Bing: Seer found 87% of SearchGPT citations matched Bing top results [Study, 2024]. Grow and Convert later found only about 40% of ChatGPT sources came from Google and Bing results for known fan-out queries [Study, 2025]. The index mix has moved over time and differs by tier.
5. A trade report states the free-tier index stores only a page title and about 200 characters of body text per page [Unverified]. Even if imprecise, it supports front-loading the key fact in the title and opening sentence.
6. Profound (about 700k US English ChatGPT conversations, 2025-10 to 2025-12): the first turn of a conversation produces citations at about 2.5 times the rate of turn 10 [Study, 2026] (read via secondary write-ups).
7. Similarweb observed that from 2026-05-07 the share of ChatGPT referrals landing on brand homepages jumped from roughly 26 to 32% to about 60%, with total ChatGPT referrals up 157.7% week over week [Study, 2026-05]. Homepages now carry more AI landing traffic: make them answer "what is this, who is it for, what does it cost, why trust it".

Tier and mode matter: logged-out, free, paid, think mode and agent mode can use different retrieval paths. Track the modes your buyers use.

### 3.4 Perplexity

1. PerplexityBot builds the index and honors robots.txt. Perplexity-User fetches on demand and generally does not apply robots.txt [Official, Perplexity bots guide].
2. Perplexity publishes signed agent keys for Web Bot Auth verification (perplexity-user.json listed in Cloudflare Radar) [Official].
3. Cloudflare reported on 2025-08-04 that Perplexity used undeclared crawlers to evade blocks and delisted it as a verified bot. Perplexity disputed this [Contested]. Practical effect: Cloudflare-protected sites may block Perplexity traffic by default.
4. Perplexity's share of AI referrals fell through 2026 (Statcounter: 4.3% of AI chatbot referrals in 2026-08) [Study, 2026-08, secondary]. Prioritize by your own GA4 data, not by its share of SEO discourse.
5. Perplexity cites heavily from Reddit (Profound: 46.7% of top-source citations in its 2024 to 2025 dataset) [Study, 2025].

### 3.5 Microsoft Copilot and Bing

1. Copilot grounds on the Bing index. Bing Webmaster Tools AI Performance (public preview 2026-02-10) reports total citations, average cited pages, page-level citations and grounding queries for Copilot, Bing AI summaries and select partners [Official, 2026-02].
2. 2026-06-16 added Intents, Topics, Citation Share and Compare in preview [Official, 2026-06].
3. Grounding queries are phrases the AI generated for retrieval, not what users typed. They are the closest thing to a published fan-out log from any engine. Mine them for content gaps.
4. Data is sampled, has no clicks and no API as of 2026-06. It does not cover ChatGPT, Claude or Perplexity.
5. Bing Search APIs were retired on 2025-08-11 and replaced by Grounding with Bing Search in Azure AI agents [Official, 2025]. Third-party tools that relied on the old API changed their data sources.

### 3.6 Claude

1. Anthropic documents three bots: ClaudeBot (training), Claude-User (fetches pages for a user's question), Claude-SearchBot (indexes for search quality). Anthropic says its bots honor robots.txt and do not bypass CAPTCHAs, and supports Crawl-delay [Official].
2. Blocking Claude-User or Claude-SearchBot reduces visibility in Claude answers [Official].
3. Claude web search launched 2025-03-20 and reached all plans in 2025-05 [Official, 2025]. Anthropic's subprocessor list still names Brave Search under Web Search (2026-09-02) [Official, 2026-09], and cited URLs overlap heavily with Brave's top results [Study, 2025]. Brave Search ranking is a lever; test, do not assume.
4. Claude is a fast-growing referral source in B2B (one B2B study put Claude at 18.5% of measurable B2B AI referrals in 2026) [Study, 2026, secondary]. Check your own GA4 before prioritizing.

### 3.7 Meta AI, Grok, Apple, Amazon, others

| Engine | What matters | Evidence |
|--------|-------------|----------|
| Meta AI (Facebook, Instagram, WhatsApp, meta.ai) | Allow Meta crawlers you want. Strong presence on Facebook and Instagram pages for brand facts. Meta has reported search partnerships | [Unverified] |
| Grok | Active, factual X account; being discussed on X; web presence for its search | [Practitioner consensus] |
| Apple Siri and Spotlight | Applebot access; Apple Business Connect for local; App Store listing for apps. Applebot-Extended only governs training | [Official] |
| Amazon Alexa for Shopping (formerly Rufus) and Alexa+ | Amazon listing content, Q&A, reviews, A+ content | [Practitioner consensus] |
| DuckDuckGo DuckAssist | DuckAssistBot; Bing and own sources | [Unverified] |
| Mistral Le Chat | MistralAI-User fetcher | [Unverified] |
| You.com, Brave | Own indexes; Brave Search index feeds Brave answers | [Practitioner consensus] |

## 4. Query fan-out: what it means operationally

Google confirmed fan-out for AI Overviews and AI Mode [Official, 2025-05]. ChatGPT and Copilot also rewrite prompts into multiple searches (visible in Bing grounding queries and in tool traces) [Study, 2025 to 2026]. Sub-query counts quoted online (8 to 12, up to 16) are third-party estimates [Unverified].

Procedure to build a fan-out map for one priority prompt:
1. Write the prompt as a buyer would ask it (for example "best payroll software for a 20 person company in Texas").
2. Collect sub-queries from four sources:
   1. Bing Webmaster Tools AI Performance grounding queries for your site and the topic.
   2. An LLM asked to list the searches it would run to answer the prompt (label as simulated).
   3. A fan-out simulator (iPullRank Qforia or similar) [Practitioner, 2025].
   4. People Also Ask and related searches for the head term (AI Mode answered 97% of sampled PAA answers in a 2026-09 sample per AlsoAsked) [Unverified, secondary].
3. Cluster sub-queries into facets: definition, criteria, pricing, comparisons, alternatives, use cases, local or segment specifics, risks, reviews, implementation.
4. For each facet, record which URL on your site answers it in one self-contained passage. Missing facets are content gaps.
5. Check who currently ranks in Google and Bing for each sub-query. If neither you nor a page that mentions you ranks, you will rarely be cited.

## 5. Passage-level retrieval

1. Engines retrieve and cite passages, not whole pages [Official for Google: Digiday and Google statements on fan-out; Practitioner consensus elsewhere].
2. Implications:
   1. Each H2 or H3 section should answer one question completely, in its first 1 to 3 sentences, with the entity named (not "it" or "our tool").
   2. Put the key fact, number or verdict in the first sentence of the section.
   3. Keep tables in HTML text, not images. Keep critical text out of tabs that only load on click via JavaScript.
   4. Front-load the page: title, first paragraph and first section should carry the answer. Several 2026 analyses report citations cluster in the top third of pages [Unverified].
3. Long pages are fine if every section stands alone. Thin pages with one generic paragraph lose to specific passages elsewhere.

## 6. JavaScript rendering

1. A 2024 log study (Vercel with MERJ) found that OpenAI, Anthropic, Perplexity and other AI crawlers fetched JavaScript files but did not execute them, while Googlebot and Applebot rendered pages [Study, 2024-12]. No major AI vendor has documented JS rendering for its crawler since [Unverified that anything changed].
2. Rule: any content you want cited must be present in the initial HTML response (server-side rendering, static generation or prerendering). Client-side rendered prices, specs, reviews and FAQs are invisible to most AI crawlers.
3. Test: fetch the URL with JavaScript disabled or with curl and search the HTML for the key facts (commands in [Technical access](technical-access-and-crawlers.md)).

## 7. Memory, personalization and context

| Factor | Effect | Evidence |
|--------|--------|----------|
| ChatGPT memory and chat history | Saved memories and past chats can shape responses and may shape search query rewrites | [Official, 2025-04 for memory across chats; query rewriting effect Unverified] |
| Custom instructions and personas | Change tone, criteria and sometimes brand choice | [Practitioner consensus] |
| Location (IP, stated city) | Changes local results, availability, currency, retailers | [Official for local features; Practitioner consensus] |
| Logged-in vs logged-out | Different models, modes and limits. Logged-out runs are a cleaner baseline but not what most paying users see | [Practitioner consensus] |
| Google personal context | Google has announced personal context features for AI Mode and Gemini that can use Gmail and other apps with permission | [Official, 2025 to 2026; rollout scope Unverified] |
| Conversation turn | Earlier turns are more likely to show citations (about 2.5x at turn 1 vs turn 10) | [Study, 2026] (Profound) |

Measurement consequence: no single run represents "the answer". Answers vary run to run. SparkToro and Gumshoe found less than a 1 in 100 chance that ChatGPT or Google AI returned the same brand list twice for the same prompt, and under 0.1% for the same list in the same order, across 2,961 responses [Study, 2026, fieldwork 2025-11 to 2025-12]. A stable core of category leaders still appeared repeatedly. Track mention frequency across many runs. See [Measurement](measurement-and-prompt-tracking.md).

## 8. Citation behaviors that change strategy

| Behavior | Evidence | Strategy implication |
|----------|----------|---------------------|
| Different engines cite different domains. Only about 11% of domains overlapped between ChatGPT and Perplexity for similar prompts | [Study, 2025, Profound] | Track engines separately. Do not assume a win in one engine transfers |
| ChatGPT leaned on Wikipedia (47.9% of top-10 source share), Perplexity on Reddit (46.7%), AI Overviews on Reddit (21.0%) in 2024 to 2025 data | [Study, 2025, Profound] | Source mix is engine specific and dated. Re-measure for your category |
| YouTube overtook Reddit as a cited social source around 2025-10 in some datasets | [Study, 2026, Bluefish via Adweek; LLM Pulse] | Video with transcripts is a citation asset, not just a channel |
| Reddit's share of ChatGPT citations fell sharply in 2025-09 (one dataset: 3.83% to 0.52% in four days) | [Study, 2025-09, Promptwatch via Search Engine Land; cause Contested] | Do not build a strategy on one platform's citation share |
| Brand-owned vs community share disagrees across studies (Yext: 86% brand-controlled; OtterlyAI: 52.5% community) | [Contested] | Category and prompt type decide. Map your own prompts |
| Cited brands in AI Overviews get more organic and paid clicks than uncited brands on the same SERP | [Study, 2025 to 2026, Seer; correlational] | Being the cited source is the new position 1 for informational queries |

## 9. Checklist: "can this engine use my page?"

1. The engine's search or user-fetch bot is allowed in robots.txt and not blocked at the CDN or WAF (check logs for 200 responses).
2. The page returns 200 with the key content in raw HTML.
3. The page is indexed in Google (for AI Overviews, AI Mode, Gemini, ChatGPT paid tier) and Bing (for Copilot), and is not noindex or nosnippet.
4. The page answers a sub-query in a self-contained passage that names the brand and states the fact.
5. The facts on the page match the facts on third-party pages about the brand.
6. The page is fresh enough for the query class (pricing, comparisons and "best of" queries reward recent updates) [Study, 2025, freshness analyses; see evidence module].
