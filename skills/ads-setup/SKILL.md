---
name: ads-setup
description: Install or refresh the Ads Master project workspace (the ads-master/ folder) in the current project. Scans the codebase for site platform, tracking tags, consent, structured data and SEO files, interviews the human for the minimum business facts, fills PROJECT_BRIEF.md and MEASUREMENT.md, activates the right agents in HEARTBEAT.md and links the workspace from CLAUDE.md. Use when the user says set up Ads Master, onboard a new project or client, initialize the growth workspace, or when any Ads Master agent finds ads-master/ missing.
---

# Ads Setup

Creates the per project brain that every Ads Master agent reads. Takes 10 to 20 minutes with the human. Never overwrites existing files.

## What gets created

```
ads-master/
  PROJECT_BRIEF.md  BRAND.md  AUDIENCE.md  COMPETITORS.md  STRATEGY.md
  MEASUREMENT.md  PRIORITIES.md  EXPERIMENTS.md  HEARTBEAT.md  README.md
  memory/<agent>.md   journal/   data/imports/   outputs/   templates/
```

Template source: `${CLAUDE_SKILL_DIR}/template/`

## Procedure

### Step 1. Detect mode
- If `ads-master/` does not exist: **new install**.
- If it exists: **refresh**. Only add files that are missing. Report what was added. Do not touch filled files.

### Step 2. Copy the template (no overwrite)
```bash
mkdir -p ads-master && cp -Rn "${CLAUDE_SKILL_DIR}/template/." ads-master/
```
If the variable did not expand, locate the template with `find / -path "*ads-setup/template/PROJECT_BRIEF.md" 2>/dev/null | head -1` and copy from its folder.

### Step 3. Protect sensitive data
Customer lists, CRM exports and revenue files must never be committed. Propose adding this to the project `.gitignore` (ask first):
```
ads-master/data/imports/*
!ads-master/data/imports/HOW_TO_EXPORT.md
```

### Step 4. Scan the codebase (auto discovery)
Run these checks and record each finding as "detected in code, not verified live". Skip any that do not apply.

| Check | How |
|-------|-----|
| Site platform | `package.json` deps (next, nuxt, astro, gatsby, remix, react, vue), `layout/theme.liquid` and `config/settings_schema.json` (Shopify theme), `wp-content/` or `functions.php` (WordPress), `composer.json` (Magento, Laravel), Webflow export markers |
| Rendering | Next.js: app router vs pages router, `generateMetadata`, `export const dynamic`, static export. SPA without SSR is an SEO and AI crawler risk: flag it |
| Analytics and tags | grep for `gtag(`, `G-[A-Z0-9]{6,}`, `GTM-[A-Z0-9]+`, `fbq(`, `ttq.`, `uetq`, `lintrk`, `_linkedin_partner_id`, `rdt(`, `pintrk`, `snaptr`, `clarity`, `hotjar`, `posthog`, `segment`, `rudderstack`, `klaviyo` |
| Server side events | grep for `graph.facebook.com`, `/events` with `access_token`, `conversions` uploads, `googleads.googleapis.com`, `business-api.tiktok.com`, `api.linkedin.com/rest/conversionEvents`, server GTM URLs |
| Consent | grep for `gtag('consent'`, `Cookiebot`, `OneTrust`, `CookieYes`, `Usercentrics`, `Iubenda`, `Didomi`, `Complianz`, `klaro` |
| SEO files | `robots.txt` or `robots.ts`, `sitemap.xml` or `sitemap.ts`, canonical tags, `hreflang`, `noindex`, meta titles and descriptions coverage |
| Structured data | grep for `application/ld+json`, schema types used (Organization, Product, Offer, FAQPage, Article, LocalBusiness, BreadcrumbList) |
| AI crawler access | robots rules for GPTBot, OAI-SearchBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Google-Extended, Bingbot; any `llms.txt` |
| Feeds and commerce | Merchant Center feed files, product JSON endpoints, Shopify apps for Google and Meta channels |
| CRM and forms | HubSpot, Salesforce, Pipedrive embeds; form handlers; hidden fields for gclid, fbclid, utm |

Write results into `ads-master/MEASUREMENT.md` (Tracking stack status) and a short "Technical findings" list at the end of `PROJECT_BRIEF.md` section 7.

### Step 5. Interview the human (one compact round)
Ask only what the code cannot tell you. Use a single message or the question tool, max 8 questions:
1. Business model and what you sell (one sentence).
2. Primary goal this quarter and the hard constraint (max CPA, min ROAS, or payback).
3. Markets and languages.
4. Monthly paid media budget and current split by channel.
5. Average order value or deal value, gross margin, and repeat purchase or LTV if known.
6. What counts as a conversion and where the revenue or lead truth lives (Shopify, CRM).
7. Which ad accounts and tools exist (and whether connectors or MCP servers are installed).
8. Regulated category or claims to avoid.

Fill `PROJECT_BRIEF.md`. Compute breakeven ROAS (1 divided by contribution margin) and target CPA when the numbers allow, and show the math.

### Step 6. Activate agents
Set the Active column in `HEARTBEAT.md` using these rules, then show the human the list for approval:

| Condition | Activate |
|-----------|----------|
| Always | growth-orchestrator, measurement |
| Has a website | seo, ai-search-optimization, cro |
| Any paid channel active or planned | creative-strategy, market-intel (monthly) |
| Ecommerce or product catalog | commerce-feeds |
| Channel active or planned in the brief | meta-ads, google-ads, microsoft-ads, chatgpt-ads, tiktok-ads, linkedin-ads accordingly |
| B2B with deal size over about $5k | linkedin-ads (consider), microsoft-ads (consider) |
| Starter tier budget | Max two paid channels. Usually google-ads (demand capture) plus one of meta-ads or the channel where the audience lives |

### Step 7. Connect the workspace to Claude
Ask before editing. Append this block to the project `CLAUDE.md` (create the file if missing). Keep the markers so a refresh can update it:
```markdown
<!-- ads-master:start -->
## Growth agents (Ads Master)
Project growth state lives in `ads-master/`. Before any marketing, ads, SEO, AI search, tracking or landing page task, read `ads-master/PROJECT_BRIEF.md` and `ads-master/MEASUREMENT.md`.
For multi channel work, load the `growth-orchestrator` skill and delegate to the specialist agents it names. Specialists: meta-ads, google-ads, microsoft-ads, chatgpt-ads, tiktok-ads, linkedin-ads, seo, ai-search-optimization, measurement, cro, creative-strategy, commerce-feeds, market-intel.
Agents never change live accounts, spend or publish without explicit approval.
<!-- ads-master:end -->
```

### Step 8. Connectors check
List the MCP servers and connectors available in this session. Recommend, but never install without approval, the ones that unlock live data: Google Ads, Google Analytics, Search Console, Meta Ads, Merchant Center, BigQuery, Ahrefs or Semrush, a rank or AI visibility tracker. Without connectors the agents work from CSV exports in `ads-master/data/imports/` (see HOW_TO_EXPORT.md there).

### Step 9. Close out
1. Write `ads-master/outputs/growth-orchestrator/YYYY-MM-DD_growth-orchestrator_setup-report.md`: what was detected, what was filled, gaps, recommended first three actions.
2. Write the first journal entry: `ads-master/journal/YYYY-MM-DD_HHMM_growth-orchestrator_workspace-setup.md`.
3. Recommend the next step. Default: "Run a full growth audit" (growth-orchestrator skill, Full Growth Audit workflow). If tracking looks broken, the measurement audit comes first.

## Quality bar
- No invented facts. Unknown fields stay blank and are listed as gaps.
- Every detected item says where it was found (file path).
- The human approves the active agent list and the CLAUDE.md edit.
