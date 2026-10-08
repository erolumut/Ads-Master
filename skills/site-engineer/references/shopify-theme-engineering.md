# Shopify Theme Engineering

> The Shopify dev, preview, QA and release loop with Shopify CLI 4.x (4.9.0 released 2026-10-08), Online Store 2.0 themes, checkout extensibility limits and Shopify's AI tooling. Pattern depth for storefront components belongs to `storefront-ux`; experiment design belongs to `cro`. Knowledge as of 2026-10.

## 1. What changed recently (verify before acting)

| Date | Change | Impact on the release loop | Label |
|------|--------|---------------------------|-------|
| 2025-06 (Summer '25 Edition) | Horizon theme family and theme blocks (nestable blocks in `blocks/`, rendered with `{% content_for 'blocks' %}`, nesting up to 8 levels) | New themes are block based; block files are shared across sections, so one block edit can change many templates | [Official, 2025] |
| 2025-08-28 | Thank you and Order status pages upgraded for Plus stores; `checkout.liquid` and additional scripts gone for Plus | Tracking and post purchase widgets must use web pixels, checkout UI extensions or apps | [Official, 2025] |
| 2026-03-17 | `shopify theme preview --overrides <json>` added to the CLI (JSON overrides, returns a preview URL and preview ID) | Preview template or settings changes without pushing a theme | [Official, repo history] |
| 2026-04-15 | Shopify Scripts editing and publishing locked | No new Script based discounts, shipping or payment rules | [Official changelog, 2025-04] |
| 2026-05-21 | Shopify CLI 4.0.0: removed `shopify theme serve`, dropped Node 20 support | CI images must run a newer Node LTS; scripts using `theme serve` break | [Official, CHANGELOG] |
| 2026-06-16 | CLI 4.2.0: `--standard-events-inspector` flag on `theme dev` injects the Standard Storefront Events inspector into previews; DNS rebinding protection for the local dev server | Use the inspector to see analytics events during development | [Official, CHANGELOG] |
| 2026-06-17 | Summer '26 Edition (150+ updates across themes, checkout, B2B, AI tooling) | Read the Edition before planning L4 work | [Secondary, 2026-06] |
| 2026-06-30 | Shopify Scripts stopped executing | Any discount, shipping or payment logic still on Scripts stopped; replacements are Functions or apps | [Official changelog] |
| 2026-07-01 | `shopify store` commands unhidden (store auth, store execute, store bulk execute, store create dev and preview, store delete) | Agents can read and write Admin GraphQL from the CLI; treat mutations as G3 | [Official, repo history] |
| 2026-07-21 | Liquid July '26 developer preview: Liquid templates instead of JSON, `{% block %}` and `{% partial %}` tags, new Theme Check rules (3.28) | Preview only; tags may change before general release; do not ship to production themes | [Secondary, 2026-07; Unverified details] |
| 2026-07-31 | CLI 4.6.0: `--reconciliation-strategy keep-local|keep-remote|abort` for `theme dev` with `--theme-editor-sync` | Non-interactive conflict handling between local JSON and editor changes | [Official, CHANGELOG] |
| 2026-08-26 | Thank you and Order status pages auto upgraded for Basic, Grow and Advanced stores; scripts and customizations not migrated | Verify purchase tracking with a test order; re-add post purchase widgets as blocks or apps | [Secondary, several sources] |
| 2026-10-07 | CLI change: `--allow-live` required for `theme dev` on a live theme when prompting is unavailable | Non-interactive agent sessions cannot silently develop against the live theme | [Official, commit 22f4455] |
| 2026-10 | Shopify AI Toolkit 2.x plugin for Claude Code and other agents (docs search, schema validation incl. Liquid, store management via `store execute`); telemetry on by default | Opt out before use on client work (section 9) | [Official, repo README] |

## 2. Theme architecture you must understand before editing

| Layer | Files | Who edits it | Release gotcha |
|-------|-------|--------------|----------------|
| Layout | `layout/theme.liquid`, `layout/password.liquid` | Developer | Loads on every page; any script here is a site wide performance and security change (L1 minimum) |
| Templates | `templates/*.json` (OS 2.0), alternates like `product.landing.json` | Merchant in the theme editor and developer | Merchants change JSON templates on the live theme. Pushing your local copy overwrites their edits |
| Sections | `sections/*.liquid` with `{% schema %}`; section groups `sections/header-group.json`, `footer-group.json` | Developer; merchant edits settings | Changing a setting `id` orphans merchant values; renaming breaks saved content |
| Blocks | `blocks/*.liquid` theme blocks (nestable); section local blocks inside schema; app blocks from apps | Developer and apps | Theme blocks are reused across sections; test every template that allows `@theme` blocks |
| Snippets | `snippets/*.liquid` | Developer | Shared; a change in a price or card snippet touches every collection and search page |
| Config | `config/settings_schema.json`, `config/settings_data.json` | Developer (schema), merchant (data) | Never overwrite live `settings_data.json` blindly; pull it first |
| Locales | `locales/*.json`, `*.schema.json` | Developer and translators | Missing keys show raw translation keys; test every published locale |
| Assets | `assets/*` | Developer | Cached on the CDN by URL; use `asset_url` so file names version correctly |
| Data | Metafields, metaobjects (definitions in admin or apps) | Merchant, apps, developer via Admin API | Theme code that assumes a metafield exists breaks on products without it (worst case data) |
| Checkout | Checkout and accounts editor, checkout UI extensions, Functions, web pixels | Apps and Plus developers | Not part of the theme; a theme rollback does not roll back checkout changes |

Rules:
1. Pull before you push. Before any push to an existing theme, `shopify theme pull --theme <id> --only "templates/*.json" --only "sections/*.json" --only "config/settings_data.json"` into the branch and commit, so merchant edits are not lost.
2. Prefer `--nodelete` on pushes to existing themes so files deleted locally do not disappear remotely by accident.
3. Prefer new alternate templates (`product.landing-campaign.json`) for campaign pages over editing the default template, so a rollback is a template assignment change.
4. Keep app code out of theme files. Use app blocks and app embeds; legacy ScriptTag injections and leftover snippets after uninstall are a common source of slow pages and errors.

## 3. CLI 4.x command map with gates

| Command | Purpose | Key flags | Gate |
|---------|---------|-----------|------|
| `shopify theme init` | Scaffold from the Skeleton theme (defaults to stable Skeleton releases since 2026-10) | `[name]` | G1 |
| `shopify theme dev` | Local preview served from a development theme with hot reload | `--store`, `--theme`, `--live-reload hot-reload|full-page|off`, `--theme-editor-sync`, `--reconciliation-strategy`, `--standard-events-inspector`, `--store-password`, `--error-overlay`, `--allow-live` | G2 (creates or updates a development theme); G3 with `--allow-live` |
| `shopify theme check` | Theme Check linting | `--fail-level error`, `--output json`, `--config theme-check:recommended`, `--auto-correct` | G1 |
| `shopify theme list` | List themes and roles | `--role live|unpublished|development`, `--json` | G0 |
| `shopify theme info` | Environment and theme details | `--json` | G0 |
| `shopify theme pull` | Download files | `--theme`, `--live`, `--development`, `--only`, `--ignore`, `--nodelete` | G0 to G1 |
| `shopify theme push` | Upload files | `--unpublished --theme "<new name>"`, `--development`, `--development-context <PR or branch>`, `--theme <id>`, `--nodelete`, `--strict` (Theme Check must pass), `--json`, `--only`, `--ignore`; dangerous: `--live`, `--allow-live`, `--publish` | G2 to an unpublished or development theme; G3 to live or with `--publish` |
| `shopify theme share` | Create a new unpublished theme with a random name and print a preview link | `--listing` | G2 |
| `shopify theme preview` | Apply JSON overrides to a theme and return a preview URL | `--theme`, `--overrides <file>`, `--preview-id`, `--json` | G2 |
| `shopify theme duplicate` | Copy a theme (backup before release) | `--theme`, `--name`, `--force`, `--json` | G2 |
| `shopify theme profile` | Profile Liquid rendering of a page | `--url /products/<handle>`, `--json` | G0 |
| `shopify theme metafields pull` | Pull metafield definitions for local intellisense | none required | G0 |
| `shopify theme console` | Liquid REPL against a store | `--url` | G0 |
| `shopify theme rename` | Rename a theme | `--theme`, `--name` | G2 |
| `shopify theme publish` | Make a theme live | `--theme` | G3 |
| `shopify theme delete` | Delete a theme | `--theme` | G4 (never by an agent) |
| `shopify theme package` | Zip a theme | none | G1 |
| `shopify store auth` | Authenticate an app against a store for store commands with explicit scopes | `--store`, `--scopes` | G2 (grants access; ask the human) |
| `shopify store execute` | Run Admin GraphQL queries; mutations need `--allow-mutations` | `--query`, `--query-file`, `--variables`, `--allow-mutations`, `--json` | G0 for queries; G3 for mutations |
| `shopify store bulk execute` | Bulk operations | `--allow-mutations` | G0 or G3 |
| `shopify store create dev` / `create preview` | New dev or preview store | `--demo-data` | G2 (ask) |
| `shopify store delete` | Delete a dev store | `-s`, `-f` | G4 |

Non-interactive sessions (agents, CI) must pass the target explicitly: one of `--development`, `--live`, `--theme` or `--unpublished` on push and pull, and `--theme` on duplicate. That requirement is a safety feature: always pass `--unpublished --theme "<release name>"` or `--development --development-context <branch>` and read the JSON output for the theme ID and `preview_url`.

Authentication: use a Theme Access app password (`SHOPIFY_CLI_THEME_TOKEN` in the environment, never in files) or a `shopify store auth` session with only the scopes needed. Do not use `--verbose` in shared logs: the CLI warns it may print sensitive data.

## 4. The dev and preview loop (copy and adapt)

```bash
# 0. Context (G0)
shopify version
shopify theme list --store "$STORE" --json > ads-master/outputs/site-engineer/themes-$(date +%F).json   # record live ID

# 1. Backup and sync (G2, ask)
shopify theme duplicate --store "$STORE" --theme "$LIVE_ID" --name "backup $(date +%F)" --force --json
git switch -c release/$(date +%F)-sticky-atc
shopify theme pull --store "$STORE" --live --only "templates/*.json" --only "sections/*.json" --only "config/settings_data.json"
git add -A && git commit -m "Sync merchant JSON from live before release"

# 2. Build locally (G2: creates or updates a development theme)
shopify theme dev --store "$STORE" --standard-events-inspector

# 3. Static checks (G1)
shopify theme check --fail-level error --output json > qa/theme-check.json

# 4. Release candidate on an unpublished theme (G2, ask)
shopify theme push --store "$STORE" --unpublished --theme "rc $(date +%F) sticky-atc" --strict --json > qa/push.json
# read qa/push.json: theme.id and theme.preview_url

# 5. QA against the preview URL (G0): Playwright, Lighthouse, axe, device checks
BASE_URL="$(jq -r .theme.preview_url qa/push.json)" npx playwright test

# 6. Publish (G3): the human publishes in the admin, or runs:
# shopify theme publish --store "$STORE" --theme <rc id>
```

Preview URL behavior: `?preview_theme_id=<id>` sets a preview cookie; Playwright tests should load the preview URL first in each context, then navigate. Some apps and checkout do not reflect unpublished theme code. Checkout always uses the live checkout configuration.

Per pull request previews: `shopify theme push --development --development-context "pr-123" --json` reuses one development theme per PR. Clean up development themes when the PR closes (development themes are ephemeral, but do not delete unpublished themes without approval).

## 5. GitHub integration and environments

| Item | Practice |
|------|----------|
| Shopify GitHub integration | Connect a branch to an unpublished theme. Theme editor changes commit back to the branch; commits deploy to the connected theme. Never connect the production branch to the live theme without a review step, because every merge then goes live |
| Branch model | `main` mirrors the live theme. Feature branches deploy to development themes via CLI. A `release/*` branch connects to the release candidate theme |
| Merchant edit commits | Expect automated commits from the editor on connected branches. Rebase feature branches on them before pushing, or you overwrite merchant content |
| `.shopifyignore` | Exclude files the CLI must never push (for example `config/settings_data.json` when merchants own it, docs, tests) |
| `shopify.theme.toml` | Define environments (`[environments.staging]`, `[environments.production]`) with store and theme so commands run with `-e staging`; keep passwords out of the file and in env vars |
| `.theme-check.yml` | Commit the config; missing configs are reported as user errors since CLI 4.7 |

## 6. Online Store 2.0 build rules (engineering side)

1. Settings `id` values are a contract. Add new settings; deprecate old ones by hiding, never rename.
2. Every section and block declares `presets` if merchants should add it; test the empty state (no settings filled).
3. Every metafield read is guarded: `{% if product.metafields.custom.size_chart != blank %}`. Worst case data tests cover the empty case ([Worst case data](worst-case-data-testing.md)).
4. Use `image_url` with `width` and `image_tag` with `widths` and `sizes`; set `loading: 'lazy'` below the fold and `fetchpriority: 'high'` on the LCP image only.
5. Do not render prices with string concatenation. Use money filters so currency format follows the market settings; test every active market currency.
6. Use `{% render %}` (isolated scope), not `{% include %}`.
7. JavaScript: defer by default, use web components or small modules, no jQuery for new code. Measure with `shopify theme profile` (Liquid) and Lighthouse (JS).
8. App embeds: list them and their load cost before and after a release ([Performance](performance-and-third-party-scripts.md)).
9. Accessibility: semantic buttons for add to cart and variant pickers, announced cart updates (`aria-live`), visible focus. Pattern depth: `storefront-ux`.

## 7. Checkout and post purchase limits (2026)

| Need | Allowed mechanism | Not allowed or gone |
|------|-------------------|---------------------|
| Branding of checkout | Checkout and accounts editor, branding API (Plus for deeper control) | `checkout.liquid` |
| Custom UI in checkout, Thank you, Order status | Checkout UI extensions (Plus for information, shipping and payment steps; Thank you and Order status on all plans), apps | Additional scripts box, script tags on checkout |
| Discounts, shipping and payment logic | Shopify Functions (custom apps on Plus, public apps on any plan) | Shopify Scripts (stopped 2026-06-30) |
| Conversion tracking | Customer events: web pixels (app pixels and custom pixels), server side APIs | Scripts in Additional scripts (removed by the August 2025 and August 2026 upgrades) |
| A/B tests of theme and checkout configuration | Shopify Rollouts (plan gated, limited statistics; design with `cro`) | Editing Liquid inside a theme that is part of a running Rollout |

Engineering rules:
- A theme release never fixes a checkout problem. Diagnose checkout issues in checkout settings, extensions, Functions and apps.
- After any checkout or post purchase change, run a test order (G3 if it uses a real payment; prefer a dev store or the Bogus Gateway on a development store; on a live store, use a 100% discount code on a hidden test product only with approval) and verify events with `measurement`.

## 8. Rollback on Shopify

| What broke | Rollback |
|-----------|----------|
| Theme code | Publish the previous live theme (recorded ID). Takes about a minute. Merchant edits made on the new theme after publish are lost on rollback; tell the merchant |
| A merchant JSON edit on live | Restore the JSON file from the pre release pull in git, push only that file to the live theme (G3) |
| An app embed or app block | Toggle the embed off in the theme editor (G3); uninstalling an app is L4 and may leave code behind |
| Checkout extension or Function | Deactivate in checkout settings or the app (human); not tied to the theme |
| Navigation, markets, shipping, discounts | Re-apply from the pre release snapshot (screenshots or Admin API export saved in outputs) |

## 9. Shopify AI tooling for agents (2026)

| Tool | What it does | Notes |
|------|--------------|-------|
| Shopify AI Toolkit (plugin `shopify-ai-toolkit`, skills `shopify` and `ucp`) | Searches shopify.dev docs and API schemas, validates GraphQL, Liquid and UI extension code, manages a store through `shopify store execute` | Since 2.0 one `shopify` skill with topics (`liquid`, `admin`, `storefront-graphql`, `functions`, `polaris-checkout-extensions`, `use-shopify-cli` and others). The Cursor variant connects to a remote MCP at `setup.shopify.com/mcp` (2.1.0) [Official, repo 2026-10] |
| Shopify Dev MCP (`@shopify/dev-mcp`) | Docs search, schema introspection, `validate_theme` and code block validation with Theme Check | Never touches store data. Theme validation was opt in and marked experimental in earlier versions [Secondary, 2026] |
| Storefront MCP | Public per store endpoint (`https://<shop>.myshopify.com/api/mcp`) for shopping agents | Not a development tool; useful to QA what AI agents see (handoff `ai-search-optimization`, `commerce-feeds`) [Secondary, 2026] |
| Shopify CLI `store` commands | Admin GraphQL from the terminal | Mutations require `--allow-mutations`: G3 |

Telemetry warning (read before installing on client work): the AI Toolkit sends usage events to `https://shopify.dev/mcp/usage` by default. Payloads can include search queries, validated code, file names and theme paths and, on Claude Code, the user's most recent prompt verbatim (up to 2,000 characters) when a Shopify skill activates. Opt out with an empty file at `~/.config/shopify-ai-toolkit/opt-out` (Linux and macOS) or `OPT_OUT_INSTRUMENTATION=true`; the file is the reliable method because subprocesses may not inherit environment variables [Official, README 2026-10]. Ask the human before installing, and record the opt out in `memory/site-engineer.md` setup facts.

## 10. Shopify QA additions (on top of the release checklist)

| Check | How |
|-------|-----|
| Every template type renders on the preview: home, collection (with filters), search (with and without results), PDP (single variant, multi variant, sold out, on sale), cart (empty, one item, many), blog, article, page, 404, password page if used | Playwright route list; screenshot each |
| Variant change updates price, compare at price, availability, URL `?variant=` and the add to cart button state | Playwright on a multi variant product |
| Cart drawer and cart page totals match after quantity changes and discount codes | Playwright; compare to `/cart.js` JSON |
| Checkout handoff reaches checkout with correct line items | Assert navigation to the checkout URL; stop before payment |
| Markets: currency, language and price format per active market | Load with market specific URL or country selector |
| App blocks render and do not throw console errors | `page.on('pageerror')` and console checks |
| Standard events fire in order (page viewed, product viewed, product added to cart, checkout started) | `theme dev --standard-events-inspector` locally; network assertions on preview |
| Theme Check passes with `--fail-level error` | CI |
| Liquid render time on PDP and collection does not regress | `shopify theme profile --url /products/<handle> --json` before and after |
