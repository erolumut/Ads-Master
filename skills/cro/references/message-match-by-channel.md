# Message Match and Ad Scent by Channel

> Message match: the landing page continues the exact promise that earned the click. Ad scent: the visual and verbal cues that tell the visitor "you are in the right place". Broken scent is the cheapest conversion problem to fix and one of the most common in paid accounts [Practitioner consensus].

## 1. Four layers of match

| Layer | Question | Score 0 to 2 |
|-------|----------|--------------|
| Promise | Does the H1 restate the ad's core promise or the query's intent? | 0 none, 1 loose, 2 near verbatim |
| Offer | Is the exact offer in the ad (price, discount, free trial, bonus) visible on the first screen? | 0 missing, 1 below fold, 2 first screen |
| Visual | Does the hero show the same product, person, color or scene as the creative? | 0 different, 1 related, 2 same |
| Action | Is the CTA the action the ad promised ("Get quote" ad lands on "Get quote" form)? | 0 different, 1 similar, 2 same |

Score 7 to 8: good. 5 to 6: fix in next sprint. Under 5: fix before scaling spend.

## 2. Audit procedure (paid accounts)
1. Pull the top 20 ads or asset groups by spend for the last 30 days (ask the channel agent or read exports in `ads-master/data/imports/`).
2. For each: screenshot the ad and the landing page first screen on mobile. Save pairs in the audit output.
3. Score the four layers. Note the landing page URL including parameters.
4. Group ads by landing page. One page receiving five different promises is a scent problem; split pages or make the hero dynamic.
5. Rank fixes by spend x (8 minus score).

## 3. Channel playbook

### 3.1 Google Search (and Microsoft Advertising Search)
- Intent: high, explicit. The query is the visitor's words.
- Match: H1 contains the core of the ad group theme. Long tail ad groups can share a page with dynamic H1 text (section 5).
- Quality Score has a "Landing page experience" component rated Above average, Average or Below average per keyword [Official, Google Ads Help]. Below average on high spend keywords is a CRO ticket.
- Google Ads > Landing pages report shows mobile speed score and "Mobile-friendly click rate" per URL (Campaigns > Insights and reports > Landing pages) [Official, verify current UI path].
- Microsoft Advertising traffic skews desktop and older in many markets [Practitioner consensus]; check device split before assuming mobile-first behavior.
- Competitor and comparison keywords: land on a comparison page, not the homepage.

### 3.2 Performance Max and AI Max for Search
- Final URL expansion lets Google choose the landing page and generate headlines from page content. Every indexable page can become a paid landing page.
- Implications for CRO: weak category and blog pages receive paid traffic. Audit the "Landing pages" and search terms data for pages the advertiser did not choose.
- Controls (owned by `google-ads`): URL exclusions, page feeds, URL contains rules, turning off final URL expansion for tight funnels.
- CRO action: make top 20 expansion pages conversion-ready (clear CTA, price, proof), or ask `google-ads` to exclude them.

### 3.3 Google Shopping, PMax feed, Microsoft Shopping, ChatGPT product carousels
- The PDP is the landing page. Title, image, price, sale price and availability must match the feed at all times.
- Mismatched price causes disapprovals and loses trust. Coordinate with `commerce-feeds`.
- Show the same variant (color, size) that was in the listing. Pass the variant ID in the URL and preselect it.

### 3.4 YouTube and Demand Gen
- Intent: low to medium. Visitors watched or scrolled, they did not search.
- Hero repeats the video's hook and shows the same presenter or product shot.
- Treat like Meta cold traffic: more education, stronger proof.

### 3.5 Meta (Facebook, Instagram, Threads)
- Intent: interruptive. Visitors respond to an angle (pain, desire, identity, curiosity).
- One angle per page or per dynamic hero. If ad sets test five angles, the page needs five matching heroes or one hero per angle via URL parameter.
- Lands in the Facebook or Instagram in-app browser for most clicks [Practitioner consensus]: autofill and saved passwords are limited, some payment buttons behave differently, sessions may not persist. Test checkout and forms inside the in-app browser.
- Instant Forms vs website: Instant Forms raise volume and lower quality. "Higher intent" form type adds a review step. Judge on CRM quality, not form CVR (see [Forms](forms-and-lead-capture.md)).
- Meta dynamic URL parameters for scent and analysis: `{{campaign.name}}`, `{{adset.name}}`, `{{ad.name}}`, `{{placement}}`, `{{site_source_name}}` [Official, Meta Business Help]. Use them in UTMs, then map ad name to hero variant server side.
- Optimizing ad delivery for landing page views only helps when the page is fast; Meta drops visitors who leave before the page loads [Practitioner consensus].

### 3.6 TikTok
- Intent: low, entertainment context, very mobile.
- Hero should look native: UGC-style video or the creator from the ad, captions, short copy.
- In-app browser and impatience: page must render the first screen fast on mid-range Android devices.
- TikTok Instant Page and lead forms keep users in-app; compare on downstream quality.
- TikTok Shop traffic converts inside TikTok; site CRO applies only to website campaigns.

### 3.7 LinkedIn
- Intent: professional, role based. Match the job title and company size targeted ("For RevOps leaders at 200 to 2,000 person SaaS companies").
- Lead Gen Forms prefill profile data and usually beat landing pages on form CVR; quality varies. Compare cost per SQL, not cost per lead.
- When using a landing page: the gated asset or demo offer is the hero. Show the asset cover, the 3 things they will learn, and company logos from the same industry.

### 3.8 ChatGPT ads (OpenAI)
- A click on a standard ChatGPT ad card opens the advertiser's landing page [Unverified, secondary sources 2026; check OpenAI help center].
- OpenAI advises sending traffic to a product, collection or content page instead of a generic homepage [Official, OpenAI Help Center 2026].
- Landing pages are reviewed against ad policies; misleading or internally inconsistent pages get rejected. The destination must be on the advertiser's verified domain. Advertisers can add UTMs per creative [Official/secondary, 2026].
- OpenAI's ad review crawler (OAI-AdsBot) must be able to fetch the page. Blocking it in robots.txt or a WAF stalls approval or delivery [Unverified, secondary sources 2026].
- Context: the user just asked a question in a conversation. The page should answer that question within the first screen ("Which running shoe is best for flat feet?" lands on a page that says who the shoe is for and why), then show price and proof.
- Product feed campaigns can show multi-product carousels; each card lands on its PDP [Unverified, Digiday 2026].
- OpenAI is testing "Sponsored Agents" where a click opens a brand-run agent conversation inside ChatGPT instead of a landing page, with select US advertisers [Unverified, 2026]. Watch this: if it scales, the "landing page" becomes an agent prompt and knowledge base. Coordinate with `chatgpt-ads`.

### 3.9 AI referral traffic (organic, unpaid)
- Sources: chatgpt.com, perplexity.ai, copilot.microsoft.com, gemini.google.com, claude.ai. ChatGPT appends `utm_source=chatgpt.com` to many outbound links [Practitioner consensus].
- Visitors arrive pre-informed by an AI answer that may describe your product, price or features. The page must confirm, not contradict, what the assistant said. Check what assistants say (with `ai-search-optimization`).
- Adobe's 2026 data shows AI-referred retail visits converting 42% to 54% better than non-AI traffic, with higher engagement [Study, 2026-03 and 2026-05]. Relative numbers, retail only, United States.
- CRO actions: clear specs, price, comparison and "best for" statements on deep pages; visible add to cart or booking path; fast load.

## 4. Channel matrix

| Channel | Typical awareness | Default page | Primary CTA | Proof that works | Speed sensitivity |
|---------|-------------------|--------------|-------------|------------------|-------------------|
| Google Search non-brand | Solution aware | Dedicated LP or category page | Buy, quote, book | Ratings, guarantees, comparisons | High |
| Google Search brand | Most aware | Homepage or offer page | Buy, log in, book | Minimal | Medium |
| Shopping, PMax feed | Product aware | PDP | Add to cart | Reviews, delivery date | High |
| Demand Gen, YouTube | Problem aware | LP mirroring the video | Shop, learn | Demonstration, UGC | High |
| Meta cold | Problem aware or unaware | Angle LP, pre-sell, quiz | Shop, take quiz | UGC, reviews, before and after (compliant) | Very high (in-app) |
| Meta retargeting | Product aware | PDP, offer page, cart | Complete purchase | Reviews, guarantee, urgency (real) | High |
| TikTok | Unaware or problem aware | Native-looking LP | Shop | Creator video, comments, UGC | Very high |
| LinkedIn | Solution aware (B2B) | Lead Gen Form or asset LP | Download, book demo | Logos, case studies by industry | Medium |
| ChatGPT ads | Solution aware, question in mind | PDP, collection, or content answering the question | Buy, compare, book | Specs, comparisons, reviews | High |
| AI referrals (organic) | Product aware | Deep page cited by the assistant | Buy, book | Specs, price, reviews | High |
| Email and SMS | Most aware | PDP, offer page | Buy | Minimal | Medium |

## 5. Dynamic message match (implementation)

Use when many ad groups or angles share one page. Server render the variant so there is no flicker and no layout shift.

### 5.1 Parameter design
- Use a short allowlisted key: `?h=flat-feet` or `?angle=pain-back`. Never echo raw `utm_term` or keyword text into the page (injection risk, policy risk, odd queries).
- Map keys to approved copy in a config file:
```json
{
  "default": {"h1": "Running shoes built for your stride", "sub": "Free 60-day trial runs"},
  "flat-feet": {"h1": "Running shoes for flat feet", "sub": "Stability without the stiff feel. Free 60-day trial runs"},
  "wide": {"h1": "Wide running shoes that actually fit", "sub": "2E and 4E widths in every color. Free 60-day trial runs"}
}
```
- Google Ads: set the final URL suffix or tracking template to add `h=` per ad group. ValueTrack parameters such as `{keyword}`, `{matchtype}`, `{campaignid}`, `{adgroupid}`, `{creative}`, `{device}` are for analytics; map IDs to copy server side rather than printing keywords [Official, Google Ads Help].
- Meta: put `angle=` in the URL parameters of each ad, or map `{{ad.name}}` naming conventions to angles server side.

### 5.2 Rendering rules
- Next.js or other SSR: read `searchParams` in the server component and pick copy from the config. See [Build recipes](landing-page-build-recipes.md).
- Shopify: Liquid does not reliably expose arbitrary query parameters to templates, and cached pages are shared. Prefer separate page templates or URLs per angle (`/pages/flat-feet-runners`), or swap copy client side only for elements below the fold.
- Webflow: CMS collection with one item per angle, URL per item.
- WordPress: page per angle from a block pattern, or a server side shortcode reading an allowlisted parameter (bypass cache for that page or use cache variation by parameter).
- Cache: if the CDN caches HTML, add the parameter to the cache key or use edge rendering.
- Analytics: send `lp_variant` as an event parameter so each hero can be analyzed.

## 6. Handoffs triggered by scent audits
| Finding | Hand to | What to pass |
|---------|---------|-------------|
| Ad promises an offer the page does not have | Channel agent (`meta-ads`, `google-ads`, etc.) | Ad ID, mismatch, proposed ad copy or page change |
| Many angles on one page | `creative-strategy` | Angle list, proposed one-page-per-angle plan |
| PMax or AI Max landing on weak pages | `google-ads` | URL list with CVR and spend, exclusion proposal |
| Feed price mismatch with PDP | `commerce-feeds` | SKU list, page price, feed price, timestamp |
| AI assistants describe the product wrongly | `ai-search-optimization` | Prompts, answers, correct facts, target pages |
| UTMs missing or inconsistent | `measurement` | Ad IDs, URLs, proposed UTM template |
