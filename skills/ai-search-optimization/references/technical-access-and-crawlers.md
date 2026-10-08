# Technical Access and Crawlers

> Knowledge as of 2026-10. Access failures are the most common and most expensive AI visibility problem: a CDN toggle or a WAF rule can silently remove a site from ChatGPT, Claude or Perplexity answers. Check access first in every audit. All changes to robots.txt, CDN, WAF or rendering are drafted as a change list and need human approval.

## 1. Bot and token reference

Verify tokens against each vendor's page before editing robots.txt (see Freshness protocol in SKILL.md). Version numbers in user agent strings change.

| Operator | Token | Purpose | Honors robots.txt | Blocking it means |
|----------|-------|---------|-------------------|-------------------|
| OpenAI | OAI-SearchBot | Indexes for ChatGPT search | Yes [Official] | Not shown in ChatGPT search answers (navigational links still possible). Changes take about 24 hours |
| OpenAI | ChatGPT-User | Fetches a page when a user or GPT asks | Robots.txt "may not apply" (user-initiated) [Official] | Fewer live fetches; not used for search eligibility |
| OpenAI | GPTBot | Training crawler | Yes [Official] | Content excluded from future model training; no effect on ChatGPT search |
| OpenAI | OAI-AdsBot | Checks ad landing pages | Policy check bot [Official] | Ad review issues (coordinate with `chatgpt-ads`) |
| Anthropic | Claude-SearchBot | Indexes for Claude search quality | Yes [Official] | Lower visibility in Claude search results |
| Anthropic | Claude-User | Fetches pages for a user's question | Yes [Official] | Claude cannot read the page for users |
| Anthropic | ClaudeBot | Training crawler | Yes [Official] | Excluded from future training |
| Perplexity | PerplexityBot | Indexes for Perplexity answers; not for foundation model training [Official] | Yes | Not in Perplexity index |
| Perplexity | Perplexity-User | User-triggered fetch | Generally no (user-initiated) [Official] | Limited effect via robots.txt; WAF needed to block |
| Google | Googlebot | Search index, also feeds AI Overviews and AI Mode | Yes | Removed from Search and Google AI features |
| Google | Google-Extended | Robots token only (no separate crawler). Controls use of Google-crawled content for Gemini model training and grounding in Gemini apps and Vertex AI [Official] | Yes | Content not used for Gemini training or Gemini app grounding. No effect on Search or AI Overviews ranking or inclusion [Official] |
| Google | GoogleOther, Google-CloudVertexBot | Research and product crawls; Vertex AI agents for site owners | Yes | Minor |
| Microsoft | Bingbot | Bing index, feeds Copilot and Bing AI answers | Yes | Removed from Bing and Copilot grounding |
| Apple | Applebot | Siri, Spotlight, Safari suggestions | Yes | Out of Apple search surfaces |
| Apple | Applebot-Extended | Token only. Controls training use of Applebot data [Official] | Yes | Excluded from Apple model training; Apple search unaffected |
| Meta | Meta-ExternalAgent | Training and indexing for Meta AI [Official, verify] | Yes [Official, verify] | Likely reduced Meta AI visibility [Unverified] |
| Meta | Meta-ExternalFetcher | User-initiated fetches | May not apply [Official, verify] | Limited |
| Meta | facebookexternalhit | Link previews | Partial | Broken link previews on Meta apps |
| Amazon | Amazonbot | Alexa and Amazon AI answers | Yes [Official, verify] | Less Alexa+ coverage |
| Common Crawl | CCBot | Open crawl used in many model training sets | Yes | Less presence in future third-party model training |
| ByteDance | Bytespider | Training (Doubao and others) | Reported inconsistent [Unverified] | Usually safe to block for Western brands |
| DuckDuckGo | DuckAssistBot | DuckAssist answers | Yes [Unverified] | Out of DuckAssist |
| Mistral | MistralAI-User | User fetch for Le Chat | [Unverified] | Limited |

## 2. Decide the policy before writing robots.txt

| Business type | Recommended default | Why |
|--------------|--------------------|-----|
| Brand selling products or services (ecommerce, SaaS, local, B2B) | Allow search bots, user-fetch bots and usually training bots | Visibility and future model recall are worth more than content exclusivity [Practitioner consensus] |
| Publisher monetizing content | Allow search and user-fetch bots; decide training bots by licensing strategy; consider Cloudflare pay per crawl or licensing deals | Training gives no traffic; search gives citations and some clicks |
| Sensitive or gated content (member areas, customer data) | Disallow private paths for all bots; authenticate | Robots.txt is not security |
| Regulated (health, finance) | Allow public educational content; block internal tools | Accuracy in AI answers matters for compliance |

Trade-offs that are often missed:
1. Blocking Google-Extended removes content from Gemini app grounding as well as Gemini training [Official]. A brand that wants Gemini app visibility should not block it.
2. Blocking CCBot reduces presence in many future open and commercial training sets.
3. Blocking Meta-ExternalAgent may reduce Meta AI answers about the brand [Unverified].

## 3. robots.txt templates

Important rule (RFC 9309): a crawler obeys the most specific group that matches its token and ignores the `*` group. Repeat private-path disallows inside every named group.

### 3.1 Template A: brand, maximum visibility

```
User-agent: *
Disallow: /cart
Disallow: /checkout
Disallow: /account
Disallow: /search
Allow: /

Sitemap: https://www.example.com/sitemap.xml
```

### 3.2 Template B: visible in AI search, opted out of training

```
# AI search and user fetch: allowed
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
Disallow: /cart
Disallow: /checkout
Disallow: /account
Allow: /

# Training: disallowed
User-agent: GPTBot
User-agent: ClaudeBot
User-agent: CCBot
User-agent: Applebot-Extended
User-agent: Bytespider
Disallow: /

# Everyone else, including Googlebot and Bingbot
User-agent: *
Disallow: /cart
Disallow: /checkout
Disallow: /account
Allow: /

Sitemap: https://www.example.com/sitemap.xml
```

Decide Google-Extended and Meta-ExternalAgent separately using the trade-offs in section 2. Grouping several `User-agent` lines above one rule set is valid under RFC 9309.

### 3.3 Template C: publisher, selective

Allow search bots on all articles, disallow training bots, and use snippet controls (section 6) or Cloudflare pay per crawl for monetization decisions. Model the traffic impact before applying.

## 4. CDN, WAF and hosting layers (where most silent blocks happen)

| Layer | What to check | Notes |
|-------|--------------|-------|
| Cloudflare | AI Crawl Control dashboard (per-crawler allow or block, requests, robots.txt compliance); Security > Bots settings including the AI bots block setting and Bot Fight Mode; managed robots.txt and Content Signals | Since 2025-07-01 new domains default to blocking AI training crawlers; pay per crawl in beta [Official, 2025-07]. Content Signals (search, ai-input, ai-train) added to managed robots.txt 2025-09-24, default `search=yes, ai-train=no`; major AI vendors have not committed to honoring them [Official, 2025-09; Study, 2026] |
| Cloudflare 2026 defaults | Announced 2026-07-01 ("Your site, your rules"): AI traffic split into Search, Agent and Training classes. From 2026-09-15, Training and Agent are blocked by default on pages that show ads for new domains, new sites of existing customers and existing free plan zones that had not changed their settings; paid customers who had chosen settings keep them; Search stays allowed; owners can change it on every plan. Multi-purpose crawlers (Googlebot, Bingbot, Applebot) are blocked wherever Training is blocked. Pay Per Use launched with Ceramic.ai and You.com [Official, 2026-07] | Check how user-fetch bots are classed on your zone: Cloudflare Radar lists ChatGPT-User as Agent, the AI Crawl Control docs list ChatGPT-User and Claude-User as AI Assistant, and a Free plan user reported Claude-User treated as an AI Crawler despite Agent set to allow (community thread, 2026-10) [Unverified]. If treated as Agent, ad-supported pages stop being fetched live |
| Akamai, Fastly, Imperva, AWS WAF, Vercel firewall, Netlify | Bot management rules, rate limits, JS challenges, geo blocks | Challenges (CAPTCHA, JS) stop bots that do not run JS |
| Shopify, Wix, Squarespace, Webflow, WordPress hosts | Platform-level AI crawler toggles, default robots.txt | Some platforms ship toggles to block AI crawlers; check settings |
| Security plugins (WordPress) | Bot blocking lists | Often block "unknown" bots including new AI tokens |

Verification procedure:
1. Pull 30 days of server or CDN logs. Count requests and status codes per AI token (script in section 7).
2. Expected: OAI-SearchBot, Claude-SearchBot, PerplexityBot, Googlebot and Bingbot get mostly 200 or 304. ChatGPT-User, Claude-User and Perplexity-User appear when users ask about your pages.
3. Red flags: 403, 429 or 503 for AI tokens; zero requests from OAI-SearchBot over 30 days on a site with organic traffic; challenge pages served (200 with tiny byte size).
4. In Cloudflare, open AI Crawl Control and confirm each crawler's action is Allow for the tokens the policy allows.
5. Draft the change list. Do not change settings without approval.

## 5. Verifying real bots vs spoofers

| Operator | Verification method |
|----------|--------------------|
| Google | Reverse DNS to googlebot.com or google.com, then forward DNS; or match published Googlebot IP ranges JSON [Official] |
| Bing | Reverse DNS to search.msn.com; Bing's Verify Bingbot tool [Official] |
| OpenAI | Match published IP range JSON files for OAI-SearchBot, ChatGPT-User and GPTBot listed on the OpenAI bots page [Official] |
| Perplexity | Published IP JSON files; signed requests (Web Bot Auth) for Perplexity-User [Official] |
| Anthropic | Anthropic advises robots.txt over IP blocking; IP publication status has varied [Official, Contested] |
| Agent browsers | OpenAI's agent signs requests with HTTP message signatures (Web Bot Auth) [Official, 2025]. Cloudflare verifies signed agents |

Spoofed user agents are common. Do not allowlist by user agent alone in a WAF. Allowlist verified bots.

## 6. Snippet and usage controls

| Control | Scope | Effect on AI |
|---------|-------|-------------|
| `noindex` | Page | Out of Google Search and AI features |
| `nosnippet` | Page | No snippet and not used as direct input for AI Overviews and AI Mode [Official] |
| `data-nosnippet` | HTML element | That element is excluded from snippets and AI features [Official] |
| `max-snippet:[n]` | Page | Limits snippet length, also applies to AI features [Official] |
| Search generative AI control (Search Console Settings) | Property | Include or Exclude from AI Overviews, AI Mode and Discover AI features; not Gemini app; not training [Official, 2026-06] |
| Google-Extended | Robots token | Gemini training and Gemini app grounding [Official] |
| Bing `nocache` and `noarchive` meta | Page | Bing documented in 2023 that NOCACHE limits Bing Chat use to URL, title and snippet, and NOARCHIVE excludes the page from it [Official, 2023; verify current Copilot behavior] |

Rule: never apply nosnippet or data-nosnippet to content you want cited. Audit templates for accidental sitewide nosnippet.

## 7. Log analysis scripts

Count AI bot requests and status codes from a combined-format access log:

```bash
LOG=access.log
BOTS='OAI-SearchBot|ChatGPT-User|GPTBot|Claude-SearchBot|Claude-User|ClaudeBot|PerplexityBot|Perplexity-User|Googlebot|bingbot|Applebot|Meta-ExternalAgent|Meta-ExternalFetcher|Amazonbot|CCBot|Bytespider|DuckAssistBot|MistralAI-User'
grep -oE "$BOTS" "$LOG" | sort | uniq -c | sort -rn
# Status codes per bot (status is field 9 in combined log format)
for b in OAI-SearchBot ChatGPT-User Claude-SearchBot Claude-User PerplexityBot Perplexity-User; do
  echo "== $b"; grep "$b" "$LOG" | awk '{print $9}' | sort | uniq -c | sort -rn
done
# Top URLs fetched by user-triggered bots (proxy for pages read inside AI answers)
grep -E 'ChatGPT-User|Claude-User|Perplexity-User' "$LOG" | awk '{print $7}' | sort | uniq -c | sort -rn | head -50
```

Interpretation:
1. User-fetch bot hits on a URL mean an AI answer read it for a user. Rising hits on pricing or comparison pages are an early AI demand signal.
2. Search bot coverage (unique URLs fetched per 30 days) vs sitemap URL count shows index coverage by engine.

## 8. Rendering tests

```bash
URL="https://www.example.com/pricing"
# 1. Raw HTML as an AI crawler would get it (UA test only; IP-verified WAF rules still apply to real bots)
curl -sL -A "Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-SearchBot/1.0; +https://openai.com/searchbot" \
  -o page.html -w "status=%{http_code} bytes=%{size_download}\n" "$URL"
# 2. Are the key facts in the raw HTML?
grep -c -i "per employee" page.html
# 3. Strip tags and read what a non-rendering bot sees
sed -e 's/<script[^>]*>.*<\/script>//g' -e 's/<[^>]*>//g' page.html | tr -s ' \n' | head -100
```

Pass criteria: status 200, size consistent with a full page, and every fact you want cited appears in the stripped text. Fail means server-side rendering, static generation or prerendering is needed (hand off to `seo` and the dev team).

Also check: Google Search Console URL Inspection (rendered HTML), Bing Webmaster Tools URL Inspection, and a crawler such as Screaming Frog in text-only mode vs JavaScript mode to diff content at scale.

## 9. Sitemaps, IndexNow and freshness signals

| Item | Rule |
|------|------|
| XML sitemaps | Include all indexable canonical URLs; accurate `lastmod` only when content changes |
| IndexNow | Implement for Bing (and Yandex, Naver, Seznam, Yep). Submits changed URLs instantly. Copilot grounds on Bing, so this speeds Copilot freshness [Official, IndexNow] |
| Bing Webmaster Tools | Verify the site, submit sitemaps, use URL submission for urgent changes, review AI Performance |
| Google Search Console | Verify, submit sitemaps, monitor indexing and the Generative AI performance report |
| Canonicals and hreflang | Consistent; AI engines often cite the canonical; wrong hreflang can surface the wrong market's prices |
| Status hygiene | Key pages return 200 fast; no soft 404s; redirects resolved in one hop |
| Performance | Keep TTFB low on pages likely fetched live (pricing, comparisons, docs) [Practitioner consensus] |

## 10. llms.txt (what is known)

| Question | Answer |
|----------|--------|
| What is it | A proposed markdown file at /llms.txt listing key pages for LLMs (proposal from 2024, llmstxt.org) |
| Does Google use it | No for Search; Google staff compared it to the keywords meta tag and said in 2026 it is not done for search [Practitioner reports, 2025 to 2026] |
| Do AI crawlers fetch it | Rarely. Ahrefs, 137k domains: 97% of files got zero requests in 2026-05. Otterly: about 0.1% of 60,000 AI bot accesses. Several single-site logs show zero fetches [Study, 2026] |
| Does it correlate with citations | SE Ranking, about 300k domains: no significant correlation [Study, 2025] |
| Counter-claim | Profound reported Microsoft and OpenAI linked crawlers fetching llms.txt [Unverified, data not public] |
| Verdict | Optional. Do it only if cheap (developer docs for coding assistants). Never prioritize it over access, content or off-site work. Never sell it as a ranking lever |

## 11. Agent browsers and agentic access

ChatGPT Atlas (2025-10), Perplexity Comet (2025-07) and agentic features in Chrome and other browsers operate sites for users [Official, 2025].
1. Bot challenges and aggressive bot management can block agent sessions that would have bought or booked.
2. Clean semantic HTML, labeled form fields and accessible buttons help agents complete tasks [Practitioner consensus].
3. Prefer verifying signed agents (Web Bot Auth) over blanket blocking.
4. Commerce protocols (ACP, UCP) are owned by `commerce-feeds`; see [Agentic commerce](agentic-commerce-visibility.md).

## 12. Access checklist (copy into audits)

1. robots.txt allows OAI-SearchBot, Claude-SearchBot, Claude-User, PerplexityBot, Googlebot, Bingbot on public content.
2. Named groups repeat private-path disallows.
3. Training bot policy is a documented decision, not an accident.
4. CDN or WAF does not challenge or block allowed bots (logs show 200s).
5. Cloudflare AI Crawl Control and the AI bots setting match the policy; 2026-09-15 defaults reviewed.
6. Key content present in raw HTML.
7. No accidental noindex, nosnippet or data-nosnippet on content to be cited.
8. Search generative AI control is Include (unless an approved decision says otherwise).
9. Sitemaps valid, lastmod honest, IndexNow live.
10. Google Search Console and Bing Webmaster Tools verified with AI reports accessible.
