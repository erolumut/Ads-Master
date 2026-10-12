# App Web Presence for AI

> Knowledge as of 2026-10. When someone asks ChatGPT, Gemini, Perplexity, Copilot or Claude which app to use, the answer is built from the store listings, the app's website and third-party pages. This module is the store side of that work: the store page written for AI readers, the App entity fact sheet, the web-to-store link layer (store links, Smart App Banner, JSON-LD consistency, AASA and assetlinks), and the campaign tokens that make AI installs measurable. The web wide program (app prompt panel, source map, AI-reader brief, website answer pages, apps inside assistants) belongs to `ai-search-optimization`: [Playbooks by business model](../../ai-search-optimization/references/playbooks-by-business-model.md) section 8. Section 9 draws the line.

Evidence note: every 2025 to 2026 finding here was gathered on 2026-10-12 from search result summaries; no official page was read in full, so nothing carries [Official]. `[Reported, 2026-10]` means an official page plus an independent source, or two dated independent sources, agree. `[Study, YYYY-MM]` marks a published study with a method, with its caveats. `[Unverified]` means one source, official ones included. `[Unverified: inference]` marks our own reasoning.

## 1. Why the store page is written for AI readers

The only large study of what ChatGPT cites for app prompts [Study, 2026-05] (AppTweak; 125k+ ChatGPT responses to 9,489 app prompts and about 9k game prompts; US): App Store and Google Play listings were about 47.5% of cited sources for app recommendations, the open web about 27%, and about 22.6% of answers had no citation. The store share swings by category (Weather about 65.8%, Food & Drinks about 29.3%), and citations thin out down the list (about 80 to 85% at the top position, under 25% by position 8). Full table and procedure: [Playbooks by business model](../../ai-search-optimization/references/playbooks-by-business-model.md) section 8.2.

Caveats that travel with every use of these numbers: a vendor that sells ASO tools; ChatGPT only; US only; method partly undisclosed; one period. General citation studies disagree on the open web mix and none is app specific.

How people behave [Study, 2026-09] (AppTweak survey; 1,000 US adults on Prolific; margin of error about 3 points; self-reported): 58% have used AI to find or choose an app, 10% learned of their most recent download from AI, and 59% check the store after an AI recommendation. So for many AI-sent users the store page is both the cited source and the landing page.

What no study shows: a link between store rating, review count or review recency and how often AI recommends an app. Do not promise one.

What we cannot see: whether AI crawlers can fetch and render apps.apple.com and play.google.com, and what they keep. We control only what the page says.

Consequences for ASO:
1. The description is written for the LLM reader; the keyword field is written for Apple search. On the App Store the description is not a search field ([App Store search and metadata](app-store-search-and-metadata.md)), so nothing is lost by making it plain, factual and complete.
2. The store page has to confirm what the answer said: same name, same price model, same platforms. A mismatch between answer and listing costs the install.
3. Store text is the first sprint when your own panel shows store pages as the top cited class (inference from [Study, 2026-05]; check your category).

## 2. Writing the store page for AI readers

### 2.1 Field by field

| Field | Read by store search | Shown on the page | Role for an AI reader | Rule |
|-------|---------------------|-------------------|----------------------|------|
| App name (30 on both stores) | Yes, both | Yes | The entity anchor | Exact name from the fact sheet plus the core job term; the same brand part on both stores |
| Apple subtitle (30) | Yes | Yes | One-line definition | The job in plain words |
| Apple keyword field (100) | Yes | No | None known: it is not on the page | Write for Apple search only ([Keyword research](keyword-research-and-rank-tracking.md)) |
| Play short description (80) | Yes | Yes | One-line definition | Outcome plus a term, readable as a sentence |
| Description (4,000 on both) | Play yes; App Store no | Yes | The largest block of text, the likeliest thing a model reads | Template in 2.2 |
| Apple promotional text (170) | No | Yes | Current facts | An expired offer left in place is a wrong fact |
| Release notes | Not documented | Yes | Dated changes | Plain, dated fixes and price or platform changes |
| In-app purchase display names | Indexed on Apple [Unverified] | Yes, with prices on the App Store | Plan names and prices | Names match the website pricing page and the fact sheet |
| Apple privacy labels, Play Data safety | No | Yes | Answers "is X safe" | Identical to the website privacy page |
| Developer or seller name | Yes, both | Yes | Identity for "is X legit" | Same legal name as the website footer and the fact sheet |
| Screenshot captions | [Contested] on Apple | As image text | Unknown whether models read image text | Write for conversion; never leave a key fact only in an image [Unverified: inference] |
| Review replies | No | Yes | Read alongside reviews | Factual and specific; never aimed at AI systems |
| Apple marketing URL, Play contact website | No | As links | One Ask Play test says the app's website is read | Point to the app's own page, not a generic home page |

### 2.2 Description template (both stores)

```
<App> is a <category noun> for <audience> that <core job>.          (fact sheet: one_sentence)
Works on <platforms and minimum OS>. <Languages or regions, if limited>.

Use <App> to:
• <job 1, in users' words>
• <job 2>
• <job 3>

Features
• <Feature>: <what it does>. <Its limit, if any>.

Plans
<What the free tier includes>. <Paid plan names, periods and trial length>.
<Amounts only if compliance approves stating them here; otherwise point to the pricing page by name>.

Privacy
<One line that matches the privacy labels or the Data safety form>.

Not included
<What the app does not do: devices, offline, regions, web version>.

Cancel
<Where to cancel on this store, in the store's own menu words>.
```

Play specifics (Ask Play, the metadata policy, key text in the top half): [AI surfaces in the stores](ai-surfaces-in-the-stores.md) section 6.3 and [Google Play search and listing](google-play-search-and-listing.md) section 4. Never on either store: superlatives without proof, competitor names (`aso_metadata_check.py` flags them), claims outside `brand/CLAIMS.md`, or sentences aimed at AI systems.

### 2.3 Turning the AI-reader brief into a listing change

`ai-search-optimization` sends an AI-reader brief through the journal: the panel prompts where store pages are cited, wrong or missing facts in answers with engine, date and run counts, the classes where answers fail, competitor facts that answers state and ours do not, and proposed wording from `brand/PRODUCT_FACTS.md`.

1. Map each finding to a field with the table in 2.1 (a wrong price usually means IAP names, the plans block and the website; a wrong "is it safe" answer means privacy labels and the website privacy page).
2. Draft per store and locale in the `aso_metadata_check.py` format and run `python3 -I <skill>/scripts/aso_metadata_check.py <drafts.json>` (`<skill>` is `skills/app-store-optimization` in this repo or `.claude/skills/app-store-optimization` in a project install). Fix every FAIL.
3. Check every sentence against the App entity sheet (section 7). `compliance` reviews the copy.
4. Bundle into the next metadata release, one change set per locale, and raise the change request (G3).
5. Log one `ads-master/EXPERIMENTS.md` row with two reads: store conversion after 2 to 4 weeks ([Keyword research](keyword-research-and-rank-tracking.md)) and the affected panel classes after 4 to 8 weeks, treatment cluster against a control cluster ([AI search SKILL.md](../../ai-search-optimization/SKILL.md), Experiments and reading results).
6. Reply in the journal so `ai-search-optimization` knows the store side is live and when.

## 3. Prompt classes: what the store side contributes

The classes and their panel shares are defined in [Playbooks by business model](../../ai-search-optimization/references/playbooks-by-business-model.md) section 8.1. Use the same `prompt_class` values as the panel; the keys below are the defaults when none exist yet.

| Class | `prompt_class` | The store page must state | Website requirement ASO sets (built by `seo`) | Store side fix when answers fail |
|-------|---------------|---------------------------|---------------------------------------------|----------------------------------|
| Best X app for Y | `best_app` | Job, audience and platforms in the opening lines; category and tags that fit | One page per core job, linking to both stores | Rewrite the opening lines; tag audit ([AI surfaces in the stores](ai-surfaces-in-the-stores.md) section 3) |
| X vs Y | `versus` | Differentiators as facts; prices identical to the website | A dated, honest comparison page | Correct facts; competitor names stay out of store text |
| Is X safe or legit | `safe_legit` | Developer legal name, accurate privacy labels, a support contact | Privacy and security page matching the labels | Fix labels; reply to trust complaints factually |
| X price or free | `price` | Price model in words; IAP names equal plan names | Pricing page with amounts per market, currency and an "as of" date | Rename IAPs; rewrite the plans block |
| How to cancel X | `cancel` | Where to cancel on this store | Help page with steps for App Store, Google Play and web | Add the cancel line to the description |
| Alternatives to X | `alternatives` | Job and category stated plainly, so the app is grouped with the right peers | An honest alternatives page | Category and tag check; opening lines |

How each class is won, in one line each:
1. `best_app`: be on the sources the engine cites for the category (often your own store page, then lists) with the job stated plainly.
2. `versus`: be the clearest dated source for both apps' facts; mismatched prices lose this class.
3. `safe_legit`: identity and privacy facts that agree everywhere; unanswered complaints lose it.
4. `price`: one price per market everywhere, with a date.
5. `cancel`: exact steps per platform on a crawlable help page; vague steps generate support load.
6. `alternatives`: correct grouping (category, job words) plus presence on the alternatives lists engines cite.

## 4. The app source map: store side priorities

`ai-search-optimization` runs the source map ([Playbooks by business model](../../ai-search-optimization/references/playbooks-by-business-model.md) section 8.2; outreach rules in [Off-site and community presence](../../ai-search-optimization/references/off-site-and-community-presence.md)). The store side order of work:

| Priority | Source class | Who acts | Action |
|----------|-------------|----------|--------|
| 1 | Own store listings | `app-store-optimization` | Sections 2 and 7; first whenever store pages lead the cited domains |
| 2 | Own website (app page and answer pages) | `ai-search-optimization` brief, `seo` builds, ASO sets the link layer (section 5) | Facts identical to the listing |
| 3 | Lists and review articles cited across many prompts | `ai-search-optimization` | Pitch with facts and a test account; correct wrong prices or features. ASO supplies current screenshots and the fact sheet |
| 4 | Reddit, forums, YouTube | `ai-search-optimization`, `creative-strategy`, `video-studio` | Disclosed, genuine participation; demos with accurate captions |
| 5 | Competitor listings cited for your prompts | `market-intel` | Nothing to edit; record what they state that you do not, as input to section 2 |

Red lines for every row: no seeded threads, no AI-written or fake reviews, no undisclosed paid placements, no review incentives or gating.

## 5. The web-to-store link layer

ASO writes these requirements; `seo` and `site-engineer` build them. Website answer pages themselves follow [Playbooks by business model](../../ai-search-optimization/references/playbooks-by-business-model.md) section 8.4.

| Item | Requirement | Why | Check | Builder |
|------|-------------|-----|-------|---------|
| Store badges | Link through `/go/ios?c=<page>&s=<landing source>` and `/go/android?c=<page>&s=<landing source>` (section 6) | Attribution of web and AI traffic into the stores | Click test on each page; tokens arrive | `site-engineer` |
| Direct store links | One direct, crawlable link per store on the app page (footer, or `installUrl` in the JSON-LD) | Ties the site to the listings for readers and for `app_entity_check.py`, which looks for `id<app_id>` and `id=<package>` in the HTML. Tested 2026-10-12: a page whose only store links are `/go/` badges FAILs both checks; adding `installUrl` passes | `app_entity_check.py` | `seo` |
| Smart App Banner | `<meta name="apple-itunes-app" content="app-id=<app_id>, app-argument=<page URL>">` on app pages | Converts iOS Safari visitors. No evidence that it is an AI signal | `app_entity_check.py` (a wrong app ID FAILs; a missing banner is a NOTE) | `seo` or `site-engineer` |
| JSON-LD | MobileApplication or SoftwareApplication matching the fact sheet (table below) | Consistency, Bing and Copilot; not a citation lever | `app_entity_check.py`; Rich Results Test | `seo` |
| AASA and assetlinks.json | Reachable as JSON at `/.well-known/` | Links open the app when installed | `app_entity_check.py --fetch`; QA matrix in [Deep linking](../../mobile-app-growth/references/deep-linking-and-web-to-app.md) section 3 | `site-engineer` |
| Raw HTML | Name, price model, platforms and store links present without JavaScript | Most AI crawlers do not run JavaScript ([Technical access](../../ai-search-optimization/references/technical-access-and-crawlers.md) section 8) | Rendering test | `seo` |

Schema evidence in one line: in a controlled Ahrefs study, 1,885 pages that added JSON-LD showed no meaningful change in AI citations against 4,000 controls [Study, 2026-05]; Bing said in 2025-03 that it uses schema for its LLMs [Unverified] (one report, Search Engine Land); FAQ rich results stopped showing on 2026-05-07 (`seo` skill, [Structured data](../../seo/references/structured-data.md)). So JSON-LD is for consistency, and FAQ pages are for readers, not rich results. The full MobileApplication example is in [Entity and brand authority](../../ai-search-optimization/references/entity-and-brand-authority.md) section 2.1; add the direct store URLs to it:

```json
"installUrl": [
  "https://apps.apple.com/app/id1234567890",
  "https://play.google.com/store/apps/details?id=com.acme.habits"
]
```

One fact, one value everywhere:

| Fact sheet key | JSON-LD property | App Store field | Google Play field |
|----------------|------------------|-----------------|-------------------|
| `name` | `name` | App name | App name |
| `developer` | `publisher` (Organization `name`) | Seller and developer name | Developer name |
| `category` | `applicationCategory` | Primary category | Category |
| `platforms` | `operatingSystem` | Device support | Device support |
| `prices`, `plans` | `offers` (`price`, `priceCurrency`, `description`) | In-app purchases | In-app products |
| `ios.store_url`, `android.store_url` | `installUrl` | n/a | n/a |
| `website`, `urls` | `url` | Marketing URL, support URL, privacy policy URL | Contact website, privacy policy |
| `one_sentence` | `description` | Description, first line | Short description and first line |

## 6. Campaign tokens and AI installs

The paths an AI-sent install can take, and which ones can be tagged, are in [Measurement and prompt tracking](../../ai-search-optimization/references/measurement-and-prompt-tracking.md) section 11. The key limit: a link from an AI answer straight to a store listing is not taggable by you. Tagging covers only AI visits that reach your website first, so AI-tagged installs are a floor, never the total.

The landing signal: ChatGPT adds `utm_source=chatgpt.com` to the links it sends to websites, while its mobile app often drops the referrer ([Measurement and prompt tracking](../../ai-search-optimization/references/measurement-and-prompt-tracking.md) section 9.2). So read the landing `utm_source` first and the referrer host second; for engines that add no UTM, the referrer host is the only signal and app traffic without one lands in Direct.

### 6.1 Token registry (ASO owns it)

| Part | Values | Example |
|------|--------|---------|
| Source prefix | `ai-<engine>` for AI landings; `web` for other site traffic; `partner-<name>`, `qr-<place>` for offline and partner links | `ai-chatgpt` |
| Engine keys | `chatgpt`, `perplexity`, `gemini`, `copilot`, `claude`; add one when GA4 shows a new AI source (keys match the ai-search redirect spec) | `perplexity` |
| Campaign | Page or placement slug, at most 16 characters | `habit-tracker` |
| Apple `ct` | `<prefix>-<campaign>`, at most 30 characters | `ai-chatgpt-habit-tracker` |
| Play referrer | `utm_source=<AI host or site host>`, `utm_medium=ai_assistant` or `web`, `utm_campaign=<campaign>` | `utm_source=chatgpt.com&utm_medium=ai_assistant&utm_campaign=pricing` |

Rules:
1. Lowercase, hyphens, no personal data, never reuse a token for a new meaning.
2. Keep `ct` at 30 characters or fewer: the App Store Connect Help limit was read as 30 in a summary [Unverified]. Keep the encoded Play referrer short; its limit was read as 512 characters [Unverified].
3. Apple target: `https://apps.apple.com/app/apple-store/id<APP_ID>?pt=<PROVIDER_TOKEN>&ct=<CT>&mt=8`, where `pt` is your provider token from App Store Connect [Unverified: App Store Connect Help read as a summary; generate one campaign link in App Store Connect to confirm the format].
4. Play target: `https://play.google.com/store/apps/details?id=<PACKAGE>&referrer=<URL-encoded UTM string>`; the app or the MMP reads it with the Play Install Referrer library.
5. Using the AI host as `utm_source` keeps app-side reports aligned with the GA4 AI Assistants channel regex ([Measurement and prompt tracking](../../ai-search-optimization/references/measurement-and-prompt-tracking.md) section 9.1).
6. Record every token with its meaning and start date under store facts in `ads-master/memory/app-store-optimization.md`; announce new tokens in the journal for `measurement`.

### 6.2 Redirect helper for the web team

A framework-neutral sketch (TypeScript; tested with Node 22 on 2026-10-12, longest token exactly 30 characters). The page passes the visit's landing source (first `utm_source` or referrer host) as `s`; how it remembers that value across pages, and whether storing it needs consent, is agreed with `measurement` and `compliance`. The route answers with a 302 to `storeUrl(...)` and logs a GA4 `store_click` event.

```ts
const APP_ID = "1234567890";        // ios.app_id from the fact sheet
const PROVIDER_TOKEN = "123456";    // pt, from App Store Connect
const PACKAGE = "com.acme.habits";  // android.package
const SITE_HOST = "acme.com";

const AI_ENGINES: Readonly<Record<string, string>> = {
  "chatgpt.com": "chatgpt", "chat.openai.com": "chatgpt", "perplexity.ai": "perplexity",
  "gemini.google.com": "gemini", "copilot.microsoft.com": "copilot", "claude.ai": "claude",
};

/** AI host behind the visit, from the landing source passed as `s`; null if none. */
export function aiHost(landingSource: string | null): string | null {
  if (!landingSource) return null;
  const host = landingSource.toLowerCase().replace(/^https?:\/\//, "").replace(/^www\./, "").split("/")[0];
  return host in AI_ENGINES ? host : null;
}

/** Target for GET /go/ios or /go/android; `campaign` is the page or placement (`c`). */
export function storeUrl(platform: "ios" | "android", ai: string | null, campaign: string): string {
  const slug = campaign.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+/, "").slice(0, 16).replace(/-+$/, "");
  if (platform === "ios") {
    const ct = (ai ? `ai-${AI_ENGINES[ai]}-${slug}` : `web-${slug}`).slice(0, 30);
    return `https://apps.apple.com/app/apple-store/id${APP_ID}?pt=${PROVIDER_TOKEN}&ct=${encodeURIComponent(ct)}&mt=8`;
  }
  const referrer = new URLSearchParams({
    utm_source: ai ?? SITE_HOST, utm_medium: ai ? "ai_assistant" : "web", utm_campaign: slug,
  }).toString();
  return `https://play.google.com/store/apps/details?id=${PACKAGE}&referrer=${encodeURIComponent(referrer)}`;
}
```

Never use Firebase Dynamic Links for this: they shut down on 2025-08-25 ([Deep linking](../../mobile-app-growth/references/deep-linking-and-web-to-app.md) section 2.4).

### 6.3 Reading AI installs monthly

| Signal | Where | What it tells you |
|--------|-------|-------------------|
| `ai-*` campaign tokens | App Store Connect campaign data | iOS installs from AI visits that went through the website (floor) |
| `utm_medium=ai_assistant` | Install referrer in the app or the MMP; Play Console tracked channels ([Google Play search and listing](google-play-search-and-listing.md)) | The same for Android |
| `store_click` events in the AI Assistants channel | GA4 | AI visits that headed to a store |
| "ChatGPT or another AI assistant" answers | Onboarding survey (owned by `mobile-app-growth`) | Self-reported share, including store-direct AI installs |
| MMP AI attribution | AppsFlyer reportedly covers 8 AI engines [Unverified]; Branch documents AI attribution [Unverified] | Ask which engines and signals, and whether store-direct clicks are modeled; label modeled numbers as estimates |
| Store page views against panel visibility | App Store Connect, Play Console, the app panel | A correlation to watch, not attribution |

Report the tagged floor next to the self-reported share in the monthly ASO report. Never present the floor as "AI installs".

## 7. The App entity fact sheet (ASO maintains it)

The human-readable sheet is the App entity section of `ads-master/brand/PRODUCT_FACTS.md`, maintained by `app-store-optimization` with `compliance`; the human owns and approves the facts. Field definitions and the "must match" list: [Entity and brand authority](../../ai-search-optimization/references/entity-and-brand-authority.md) section 2.1.

The machine-readable mirror is `ads-master/data/app-entity.json`, created by `ads-setup` from the template `skills/ads-setup/template/data/app-entity.json`:

| Key | Read by `app_entity_check.py` | Notes |
|-----|------------------------------|-------|
| `name`, `developer`, `category`, `website` | Yes | Exact strings as published |
| `ios.app_id`, `android.package` | Yes | Delete a block if the app is not on that store |
| `prices` | Yes | Use the same strings as the JSON-LD offer prices, which are compared exactly ("0" is accepted for free); store pages accept "4.99" and "4,99" alike |
| `currency`, `plans`, `platforms`, `markets`, `languages`, `one_sentence`, `top_jobs`, `not`, `urls`, `claims_ref`, `updated` | No | For people and other agents (store copy, assistant phrases, panel accuracy scoring) |

Update triggers and order:

| Trigger | Update in the sheet | Then |
|---------|--------------------|------|
| Price change in any market | `prices`, `plans` | IAPs and the plans block (G3), website pricing page, JSON-LD offers |
| New platform or minimum OS | `platforms` | Store device support, website, JSON-LD `operatingSystem` |
| Rename or new developer entity | `name`, `developer` | Every surface; plan as a project with a rank read |
| Privacy practice change | Privacy facts in PRODUCT_FACTS.md | Privacy labels, Data safety, website privacy page |
| New market or language | `markets`, `languages` | Localized listings and pages ([Localization](localization-and-market-expansion.md)) |
| Cancel flow change | `urls.cancel_help` | Help page; the cancel line in both descriptions |

Order: the sheet (human approval), then the store listings (G3), then the website and JSON-LD (`seo`), then third-party profiles (`ai-search-optimization`), all within 14 days. Then run the check below and ask `ai-search-optimization` to re-run the panel's price, cancel and safety prompts.

Run it (`<skill>` is `skills/ai-search-optimization` in this repo or `.claude/skills/ai-search-optimization` in a project install):

```
python3 -I <skill>/scripts/app_entity_check.py --facts ads-master/data/app-entity.json \
  --html site.html --store-page apple-us.html --store-page play-us.html --robots robots.txt
python3 -I <skill>/scripts/app_entity_check.py --facts ads-master/data/app-entity.json --fetch
```

Exit 0 consistent, 1 at least one FAIL, 2 could not run. The check table and known limits are in the entity module. Store side notes, each tested on 2026-10-12 against the current script:
1. Save store pages from a browser (G0); `--fetch` never reads them. Store page prices match in either decimal format (a Dutch page showing "4,99 €" passes against "4.99"), but each storefront page must show every paid price in `prices`, so keep one fact sheet per currency when markets price differently.
2. `/go/` badges alone FAIL the store link checks; keep the direct links or `installUrl` (section 5).
3. Run it after every metadata release, after every website change to app pages, and monthly.

## 8. Reading the app panel (ai-search runs it)

The panel, its JSONL format, config rules and statistics are in [Measurement and prompt tracking](../../ai-search-optimization/references/measurement-and-prompt-tracking.md) section 10.

ASO supplies:
1. The App Store path for each tracked storefront, as it appears in cited URLs (`apps.apple.com/us/app/<slug>`), for the config's owned domains.
2. The Play listing as its exact entry, `play.google.com/store/apps/details?id=<package>`, never the bare path. Tested on 2026-10-12 with a fixture citing both stores and a competitor's Play page: the exact entry gave the true citation share (50%); the bare path counted the competitor's page as owned (75%). Query entries match on parameter values in any order, so `details?hl=en&id=<package>` counts and `id=<package>.pro` does not (fixed in the script on 2026-10-12).
3. The fact sheet for accuracy scoring.

ASO reads:
1. Owned citation and citation share across the website and both store listings.
2. How often apps.apple.com and play.google.com appear in the most cited domains: the store share for your category, compared with the study in section 1.
3. Failures in the `price`, `cancel` and `safe_legit` classes: usually store fixable (section 2).
4. Any wrong fact traced to a store listing: same week fix as a High severity correction ([Entity and brand authority](../../ai-search-optimization/references/entity-and-brand-authority.md) section 8).

## 9. Boundary and handoffs

| Work | Owner | ASO's role |
|------|-------|-----------|
| Store listings, IAP names, privacy labels, tags, review replies, summary reports | `app-store-optimization` | Owner (G3 to publish) |
| App entity fact sheet and its JSON mirror | `app-store-optimization` with `compliance`; human approves | Maintainer |
| Campaign token registry | `app-store-optimization` | Owner |
| App prompt panel, source map, AI-reader brief | `ai-search-optimization` | Supplies store paths and facts; acts on store findings |
| Website answer pages (briefs) | `ai-search-optimization` | Sets the link layer requirements (section 5) |
| Website build, JSON-LD, indexing, rendering | `seo` with `site-engineer` | Supplies the fact sheet mapping |
| `/go/` redirect, AASA, assetlinks | `site-engineer` | Writes the requirement and token scheme |
| GA4 events, AI channel, consent for the landing source | `measurement` with `compliance` | Consumer of the data |
| MMP, install referrer handling, onboarding survey, deep links | `mobile-app-growth` with `measurement` | Consumer of the data |
| Apps and connectors inside ChatGPT, Claude, Gemini, Copilot | `ai-search-optimization` ([Assistant apps and connectors](../../ai-search-optimization/references/assistant-apps-and-connectors.md)) | Supplies the fact sheet and store facts |
| On-device assistants (App Intents, AppFunctions) | App team, specified by ASO ([On-device assistants](on-device-assistants.md)) | Owner of the specification |
| All customer facing copy | `compliance` | Submits drafts |

Handoffs are journal entries plus a "Handoffs requested" section; the main session executes them.

## 10. Worked example (illustrative scenario, not data)

Habit tracker, Growth tier, US and NL. The ai-search panel (60 prompts, 3 runs, ChatGPT and Gemini) shows store pages as the most cited domains for `best_app`, wrong prices in 5 of 12 `price` prompts (a 2025 list article cites last year's yearly price), and generic answers for the 6 `cancel` prompts.

1. Store side: description rewritten with the 2.2 template; yearly IAP renamed from "Premium Plus" to "Pro Yearly" to match the website; cancel line added (G3 after `compliance`).
2. Fact sheet: the yearly price corrected; `app_entity_check.py` exit 1 (the JSON-LD offer still showed the old yearly price), `seo` fixed it, exit 0 on rerun for the US and NL store pages.
3. Link layer: badges moved to `/go/` with `installUrl` added; tokens `ai-chatgpt-pricing` and `ai-gemini-pricing` registered.
4. Off-site: `ai-search-optimization` sent the list article's publisher the current prices with evidence.
5. Reads: store conversion at 3 weeks; at 6 weeks the `price` and `cancel` prompts read as one 18 prompt treatment cluster (no group under 10 prompts is reported alone) against the untouched `alternatives` class (10 prompts) as control; AI-tagged installs reported as a floor next to the onboarding survey share.

## 11. Myths

| Myth | Reality |
|------|---------|
| "Schema or llms.txt will get the app recommended" | Hygiene only; the controlled study found no citation change [Study, 2026-05] |
| "A better rating makes AI recommend us more" | No study shows that link |
| "Write instructions for AI in the description" | Manipulation; banned in this system |
| "The keyword field helps AI answers" | It is not on the page; write it for Apple search only |
| "AI installs show up as direct, so AI sends nothing" | Store-direct AI clicks are not taggable; read the floor plus the survey share |
| "One ChatGPT screenshot proves we rank first" | Answers vary run to run; use the panel with intervals |
| "A listing in an assistant's app directory means AI recommends us" | Directory listing is not recommendation in answers; see [Assistant apps and connectors](../../ai-search-optimization/references/assistant-apps-and-connectors.md) |
