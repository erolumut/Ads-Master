# Sources (annotated)

> Knowledge as of 2026-10. Dates are publication or data dates as best established. "Secondary" means the finding was read through trade press or a vendor summary, not the primary document; verify before quoting numbers to a client. Re-check official pages during every Freshness check.

## Official documentation and announcements

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | Overview of OpenAI Crawlers | OpenAI | https://developers.openai.com/api/docs/bots | Living doc, read 2026-10 | OAI-SearchBot, ChatGPT-User, GPTBot, OAI-AdsBot roles; 24 hour robots.txt lag; IP files |
| 2 | Does Anthropic crawl data from the web and how can site owners block the crawler | Anthropic | https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler | Living doc, read 2026-10 | ClaudeBot, Claude-User, Claude-SearchBot; robots.txt and Crawl-delay support |
| 3 | Perplexity crawlers guide | Perplexity | https://docs.perplexity.ai/guides/bots | Living doc | PerplexityBot vs Perplexity-User behavior |
| 4 | AI features and your website | Google Search Central | https://developers.google.com/search/docs/appearance/ai-features | 2025, updated 2026 | Eligibility, fan-out, controls, Search Console reporting |
| 5 | AI Mode in Google Search: updates from Google I/O 2025 | Google | https://blog.google/products-and-platforms/products/search/google-search-ai-mode-update/ | 2025-05 | AI Mode rollout, query fan-out, Deep Search |
| 6 | Generative AI performance report (Search) | Search Console Help | https://support.google.com/webmasters/answer/16984139 | 2026-06, updated 2026-08 | Report scope, metrics, worldwide availability |
| 7 | Search generative AI control | Search Console Help | https://support.google.com/webmasters/answer/16908024 | 2026-06, updated 2026-08 | Opt-out control behavior |
| 8 | Google common crawlers (Google-Extended) | Google Search Central | https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers | Living doc | Google-Extended scope (Gemini training and grounding; not Search) |
| 9 | Introducing AI Performance in Bing Webmaster Tools Public Preview | Microsoft Bing | https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview | 2026-02-10 | Citations, cited pages, grounding queries |
| 10 | Content Independence Day: no AI crawl without compensation | Cloudflare | https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/ | 2025-07-01 | Default AI crawler blocking; pay per crawl |
| 11 | Perplexity is using stealth, undeclared crawlers to evade website no-crawl directives | Cloudflare | https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ | 2025-08-04 | Stealth crawling allegation (disputed) |
| 12 | Introducing ChatGPT search | OpenAI | https://openai.com/index/introducing-chatgpt-search/ | 2024-10-31 | Launch and partner content |
| 13 | llms.txt proposal | llmstxt.org | https://llmstxt.org | 2024-09 | What llms.txt is |
| 14 | IndexNow protocol | IndexNow | https://www.indexnow.org | Living doc | Instant URL submission to Bing and others |

## Studies and data

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 15 | GEO: Generative Engine Optimization (Aggarwal et al., KDD 2024) | arXiv / ACM KDD | https://arxiv.org/abs/2311.09735 | 2023-11, KDD 2024 | Quotations, statistics, citations raise visibility up to about 40% in a simulated engine |
| 16 | The Princeton GEO study: methodology, results and critique | blck alpaca | https://blckalpaca.at/en/knowledge-base/seo-geo/geo-generative-engine-optimization/the-princeton-geo-study-methodology-results-and-critique.md | 2026 | Critique and transfer limits (secondary) |
| 17 | An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied) | Ahrefs | https://ahrefs.com/blog/ai-overview-brand-correlation/ | 2025 | Branded mentions 0.664, anchors 0.527, branded search 0.392 |
| 18 | AI Overviews Reduce Clicks by 34.5% | Ahrefs | https://ahrefs.com/blog/ai-overviews-reduce-clicks/ | 2025-04 | CTR impact |
| 19 | AI Overviews reduce clicks: update | Ahrefs | https://ahrefs.com/blog/ai-overviews-reduce-clicks-update | 2026-02 | 58% lower CTR for position 1 (secondary read) |
| 20 | AIO Impact on Google CTR: 2026 Update | Seer Interactive | https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update | 2026 | Cited vs uncited brand clicks (secondary read) |
| 21 | Google AI Overviews drive drop in organic and paid CTR | Search Engine Land | https://searchengineland.com/google-ai-overviews-drive-drop-organic-paid-ctr-464212 | 2025-11 | Seer 2025 update figures |
| 22 | 87% of SearchGPT Citations Match Bing's Top Results | Seer Interactive | https://www.seerinteractive.com/insights/87-percent-of-searchgpt-citations-match-bings-top-results | 2024 | Early Bing dependence |
| 23 | Only 40% of ChatGPT Sources Come from Google and Bing for Known Fan-Out Queries | Grow and Convert | https://www.growandconvert.com/ai/fan-out-query-serp-study/ | 2025 | Index divergence |
| 24 | ChatGPT built its own search index | Peec AI | https://peec.ai/blog/chatgpt-built-its-own-search-index | 2026-07 | Labrador source field analysis |
| 25 | Inside ChatGPT's retrieval stack: the index, cache and pages it actually reads | Search Engine Land | https://searchengineland.com/chatgpt-retrieval-stack-index-cache-pages-485036 | 2026 | Free vs paid retrieval mix (secondary) |
| 26 | OpenAI's ChatGPT using SerpApi to scrape Google results | Search Engine Roundtable | https://www.seroundtable.com/chatgpt-serpapi-scrape-google-39989.html | 2025 | Google results inside ChatGPT |
| 27 | What search engine does ChatGPT use? | Falia | https://falia.co/en/insights/ai-visibility/what-search-engine-does-chatgpt-use/ | 2026 | Bing absence in consumer path (vendor) |
| 28 | AI recommendations change with nearly every query (SparkToro) | Search Engine Journal | https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242 | 2026 | Answer variance, under 1% identical lists |
| 29 | AI Platform Citation Patterns | Profound | https://www.tryprofound.com/blog/ai-platform-citation-patterns | 2025 | Source mix by engine |
| 30 | The Data on Reddit and AI Search | Profound | https://www.tryprofound.com/blog/the-data-on-reddit-and-ai-search | 2025 | Reddit citation share (partnership caveat) |
| 31 | AI search engines cite Reddit, YouTube and LinkedIn most | Search Engine Land | https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138 | 2026 | Cross-engine top domains |
| 32 | The AI Citations Report 2026 | OtterlyAI | https://otterly.ai/blog/the-ai-citations-report-2026/ | 2026 | Community vs brand sources |
| 33 | Google Gemini sends more traffic to sites than Perplexity | Search Engine Journal | https://www.searchenginejournal.com/google-gemini-sends-more-traffic-to-sites-than-perplexity-report/570714/ | 2026 | Referral shares |
| 34 | ChatGPT referral traffic near triples overnight | Similarweb | https://www.similarweb.com/blog/insights/ai-news/chatgpt-referral-traffic-triples/ | 2026-05 | Homepage referral shift from 2026-05-07 |
| 35 | AI Referral Traffic by Industry: 2026 Data | Similarweb | https://aisearch.similarweb.com/blog/ai-referral-traffic-by-industry/ | 2026 | Industry referral benchmarks |
| 36 | ChatGPT's AI referral share fell from 89% to 63% | Goodie | https://higoodie.com/blog/ai-search-traffic-report-2026/ | 2026 | Referral share trend (vendor) |
| 37 | AI traffic research study | SE Ranking | https://seranking.com/blog/ai-traffic-research-study/ | 2025 to 2026 | Engine referral comparisons |
| 38 | We serve an llms.txt; AI crawlers never asked for it | Saaslinks | https://saaslinks.net/blog/llms-txt-server-log-study | 2026 | Single-site logs |
| 39 | llms.txt: we publish one, and no AI crawler has ever read it | Prosopo | https://prosopo.io/blog/llms-txt/ | 2026 | Single-site verified-IP logs |
| 40 | The rise of the AI crawler | Vercel | https://vercel.com/blog/the-rise-of-the-ai-crawler | 2024-12 | AI crawlers do not execute JavaScript |
| 41 | Google users are less likely to click on links when an AI summary appears | Pew Research Center | https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ | 2025-07-22 | 8% vs 15% click rates |

## Trade press and analysis

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 42 | Google Search Console AI performance reports and Search generative AI control rolling out globally | Search Engine Land | https://searchengineland.com/google-search-console-ai-performance-reports-and-search-generative-ai-control-rolling-out-globally-486269 | 2026-08 | Worldwide rollout |
| 43 | Google Search Console AI reports rolled out worldwide | Search Engine Journal | https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/ | 2026-08 | Rollout, limits |
| 44 | Google gives sites AI search opt-out, but not the data to use it | Search Engine Journal | https://www.searchenginejournal.com/google-gives-sites-ai-search-opt-out-but-not-the-data-to-use-it/577978/ | 2026-06 | Opt-out critique |
| 45 | Google's AI opt-out leaves publishers with a difficult choice | Digiday | https://digiday.com/media/googles-ai-opt-out-leaves-publishers-with-a-choice-they-cant-safely-use/ | 2026-06 | Publisher trade-offs |
| 46 | Google AI Overviews opt-out hits Search Console: Gemini excluded | Tech Times | https://www.techtimes.com/articles/317979/20260608/google-ai-overviews-opt-out-hits-search-console-gemini-excluded-publishers-weigh-trade-offs.htm | 2026-06-08 | Gemini not covered |
| 47 | Bing Webmaster Tools AI Performance reports go live | Search Engine Roundtable | https://www.seroundtable.com/bing-webmaster-tools-ai-performance-report-40911.html | 2026-02 | Launch details |
| 48 | Bing Webmaster Tools adds AI citation performance data | Search Engine Journal | https://www.searchenginejournal.com/bing-webmaster-tools-adds-ai-citation-performance-data/566874/ | 2026-02 | Metrics |
| 49 | Query fan-out technique in AI Mode: new details from Google | Search Engine Journal | https://www.searchenginejournal.com/query-fan-out-technique-in-ai-mode-new-details-from-google/552532/ | 2025 | Fan-out mechanics |
| 50 | How to optimize for query fan-out | Search Engine Land | https://searchengineland.com/guide/how-to-optimize-for-query-fan-out | 2025 to 2026 | Practitioner methods |
| 51 | Google's query fan-out technique | Aleyda Solis | https://www.aleydasolis.com/en/ai-search/google-query-fan-out/ | 2025 | Practitioner methods |
| 52 | Google confirms llms.txt has no current implementation | Search Engine Journal | https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/ | 2026 | Google position |
| 53 | Google's Mueller says llms.txt can't help LLMs differentiate sites | Search Engine Journal | https://www.searchenginejournal.com/googles-mueller-says-llms-txt-cant-help-llms-differentiate-sites/579304/ | 2026 | Google position |
| 54 | Google Search team does not endorse llms.txt files | Search Engine Roundtable | https://www.seroundtable.com/google-does-not-endorse-llms-txt-40789.html | 2026 | Google position |
| 55 | Cloudflare blocks mixed-use AI crawlers | Technology.org | https://www.technology.org/2026/07/03/cloudflare-blocks-mixed-use-ai-crawlers/ | 2026-07-03 | 2026-09-15 defaults (secondary) |
| 56 | Cloudflare enters the robots.txt fray with a Content Signals Policy | Search Engine World | https://www.searchengineworld.com/cloudflare-enters-the-robots-txt-fray-with-a-content-signals-policy-for-ai-bots | 2025-09 | Content Signals |
| 57 | Cloudflare accuses Perplexity of stealth crawling | TechRepublic | https://www.techrepublic.com/article/news-cloudflare-accuses-perplexity-stealth-crawling-violations/ | 2025-08 | Allegation and response |
| 58 | Google announces a new protocol to facilitate commerce using AI agents | TechCrunch | https://www.techcrunch.com/2026/01/11/google-announces-a-new-protocol-to-facilitate-commerce-using-ai-agents/ | 2026-01-11 | UCP announcement |
| 59 | Google UCP: merchant guide to agentic commerce | commercetools | https://commercetools.com/blog/google-ucp-merchant-guide-to-agentic-commerce | 2026 | UCP mechanics (vendor) |
| 60 | Google Merchant Center UCP integration hub | UCP Checker | https://ucpchecker.com/blog/google-merchant-center-ucp-integration-hub | 2026-10 | Integration hub rollout (single source) |
| 61 | ChatGPT for ecommerce: what to do now that Instant Checkout is gone | Digital Silk | https://www.digitalsilk.com/digital-trends/digital-trends-chatgpt-ecommerce/ | 2026 | Instant Checkout pivot (secondary) |
| 62 | ChatGPT Instant Checkout: ACP protocol retailer guide | Ekamoira | https://www.ekamoira.com/blog/chatgpt-instant-checkout-agentic-commerce-protocol-2026 | 2026-02 | ACP feed mechanics (secondary) |
| 63 | Google AI Overviews reduce clicks by 58% | MediaNama | https://www.medianama.com/2026/02/223-google-ai-overviews-click-through-rates-58-study/ | 2026-02 | Ahrefs update coverage |
| 64 | Google AI Overviews reduce organic CTR 61%, paid 68% | PPC Land | https://ppc.land/google-ai-overviews-reduce-organic-ctr-61-paid-traffic-68/ | 2025 | Seer coverage |
| 65 | Track your brand visibility in Claude with Yoast AI Brand Insights | Yoast | https://yoast.com/yoast-ai-brand-insights-28-may-2026/ | 2026-05-28 | Claude tracking availability |
| 66 | Google Search Console multimodal search type filter | Search Engine Roundtable | https://www.seroundtable.com/google-search-console-multimodal-search-type-filter-42156.html | 2026 | Search type filter in AI report |

## Secondary sources consulted (lower weight, used for leads and cross-checks)

| # | Title | Publisher | URL | Date | Used for |
|---|-------|-----------|-----|------|----------|
| 67 | Search Console now reports AI Overviews and AI Mode impressions | PikaSEO | https://pikaseo.com/articles/google-search-console-ai-performance-reports-2026 | 2026 | Report field details |
| 68 | Google Search Console Generative AI report, explained | LLM Pulse | https://llmpulse.ai/blog/gsc-generative-ai-report/ | 2026 | Report limits (row cap, Web type) |
| 69 | GSC AI performance reports: what they track and the clicks problem | CrawlRaven | https://crawlraven.com/blog/gsc-ai-performance-reports | 2026 | No clicks in report |
| 70 | Query fan-out, AI Mode and bots: reading Search Console in 2026 | iFactory | https://www.ifactory.com/insights/query-fan-out-search-console-2026/ | 2026 | Follow-up query handling claim (Unverified) |
| 71 | What opting out of Google's AI search features means now | Search Engine Journal | https://www.searchenginejournal.com/what-opting-out-of-googles-ai-search-features-means-now/584321/ | 2026 | Opt-out implications |
| 72 | Google just released an AI opt-out feature. Your competitors hope you use it | Search Engine Land | https://searchengineland.com/google-ai-opt-out-feature-competitors-480375 | 2026-06 | Opt-out trade-offs |
| 73 | Google Search Console generative AI tools live | Search Engine Roundtable | https://www.seroundtable.com/google-search-console-generative-ai-tools-live-41984.html | 2026 | Rollout confirmation |
| 74 | Bing Webmaster Tools AI Performance guide | Keytomic | https://keytomic.com/blog/bing-ai-performance-report | 2026 | Feature summary |
| 75 | ChatGPT Labrador search index: what it means for SEO and GEO | Crucible | https://crucible.io/insights/ai/ai-search-optimisation-chatgpt-labrador-index/ | 2026 | Labrador interpretation |
| 76 | ChatGPT has been quietly building its own search engine | ALM Corp | https://almcorp.com/news/chatgpt-has-been-quietly-building-its-own-search-engine/ | 2026 | Index coverage |
| 77 | ChatGPT built its own search index: why Bing visibility isn't a ChatGPT strategy anymore | Blumint | https://blumint.co/blog/chatgpt-search-index | 2026 | Bing overlap figure |
| 78 | OpenAI reportedly pulls Google search results through SerpApi | TMCnet | https://blog.tmcnet.com/blog/rich-tehrani/ai/openai-reportedly-pulls-google-search-results-through-serpapi-for-chatgpt.html | 2025 | Google results in ChatGPT |
| 79 | llms.txt adoption data: server-log analysis | AWRSHIFT | https://wp.awrshift.com/llms-txt-in-practice/ | 2026 | Zero llms.txt fetches |
| 80 | llms.txt: what it is and who actually reads it | Loudface | https://www.loudface.co/blog/llms-txt | 2026 | Claude-User fetched llms.txt twice |
| 81 | llms.txt in 2026: Google says skip it, Lighthouse audits it | PikaSEO | https://pikaseo.com/articles/google-llms-txt-lighthouse-contradiction-2026 | 2026 | Lighthouse audit claim (Unverified) |
| 82 | Cloudflare's September 15 AI crawler wall | fastCRW | https://fastcrw.com/blog/cloudflare-ai-crawler-block-september-2026 | 2026 | Scope for existing sites (Contested) |
| 83 | Cloudflare AI crawler controls: new September 2026 defaults | Shattered | https://shattered.io/cloudflare-ai-crawler-default-20-bots-2026/ | 2026 | Default bot categories |
| 84 | Content Signals in robots.txt: what ai-train=no does | ContextBolt | https://contextbolt.com/blog/content-signals-robots-txt/ | 2026 | Vendor non-adoption |
| 85 | Cloudflare accuses Perplexity of secretly crawling sites despite explicit blocks | The Decoder | https://the-decoder.com/cloudflare-accuses-perplexity-of-secretly-crawling-sites-despite-explicit-blocks/ | 2025-08 | Perplexity response |
| 86 | Wikipedia, TechRadar and Reddit dominate AI citations | Solcrys | https://solcrys.com/wikipedia-techradar-reddit-dominate-ai-citations/ | 2026 | Category citation mix |
| 87 | YouTube now beats Reddit in AI citations | Radyant | https://www.radyant.io/guides/youtube-ai-search-visibility-citation-framework | 2026 | YouTube trend |
| 88 | AEO and AI search citation statistics 2026 | Rise at Seven | https://riseatseven.com/blog/aeo-ai-search-statistics/ | 2026 | Roundup of 2026 stats (Reddit drop, Peec AI 30M sources) |
| 89 | AI referral traffic 2026: Gemini is catching ChatGPT | Digital Applied | https://www.digitalapplied.com/blog/ai-referral-traffic-share-2026-gemini-chatgpt-geo-analysis | 2026 | Gemini share trend |
| 90 | Similarweb 2026 generative AI landscape: what it means | Salience | https://salience.co.uk/insight/similarweb-2026-generative-ai-landscape | 2026 | Similarweb share figures |
| 91 | Google UCP update 2026: cart, catalog, loyalty | Passionfruit | https://www.getpassionfruit.com/blog/what-is-google-s-ucp-update-carts-catalogs-and-loyalty-in-ai-shopping | 2026 | UCP March update |
| 92 | Google's UCP and Merchant Center | ChannelEngine | https://www.channelengine.com/en/blog/google-universal-commerce-protocol-merchant-center-ai-shopping | 2026 | native_commerce attribute |
| 93 | Agentic commerce for Shopify: protocols and priorities | Ask Phill | https://askphill.com/blogs/blog/agentic-commerce-for-shopify-protocols-platforms-and-what-to-prioritize-in-2026 | 2026 | ACP and UCP side by side |
| 94 | Why AI checkout stalled: discover in AI, buy on site | Digital Applied | https://www.digitalapplied.com/blog/ai-agentic-commerce-discover-in-ai-buy-on-site-2026 | 2026 | Checkout pivot |
| 95 | AI recommendations vary, marketers warned on tracking tools | Communicate Online | https://communicateonline.me/news/ai-brand-recommendations-vary-marketers-warned-on-tracking-tools/ | 2026 | SparkToro study coverage |

## Sources by module

| Module | Primary sources (numbers above) |
|--------|-------------------------------|
| how-ai-engines-retrieve-and-cite | 1 to 5, 8, 9, 11, 22 to 28, 34, 40 |
| evidence-and-ranking-factors | 15 to 23, 28 to 37, 41, 52 to 54 |
| content-engineering-for-llms | 4, 15, 16, 40 |
| entity-and-brand-authority | 4, 17, 29 |
| off-site-and-community-presence | 29 to 32, 86 to 88 |
| technical-access-and-crawlers | 1 to 4, 8, 10, 11, 13, 14, 38 to 40, 55 to 57, 79 to 85 |
| measurement-and-prompt-tracking | 6, 7, 9, 28, 34, 42 to 48, 67 to 69 |
| engine-playbooks | 1 to 9, 24, 25, 29, 33, 65 |
| agentic-commerce-visibility | 58 to 62, 91 to 94 |
| playbooks-by-business-model | 6, 7, 10, 44, 45, 71, 72 |
| myths-and-anti-patterns | 1, 4, 8, 13, 15, 28, 52 to 56 |
| tools-api-mcp | 6, 9, 24, 32, 65 |

## Known gaps

1. Kevin Indig (Growth Memo), iPullRank, BrightEdge, Conductor and Semrush 2026 studies were not read in primary form during this research cycle (search budget exhausted). Claims attributed to them in this package are labeled [Unverified] or dated 2025 from prior knowledge.
2. OpenAI help center pages on ChatGPT search, shopping and merchants were not re-read in 2026-10. Verify feed fields and checkout status with `commerce-feeds`.
3. Cloudflare's own 2026-07-01 post was not read; the 2026-09-15 default details come from trade press.
