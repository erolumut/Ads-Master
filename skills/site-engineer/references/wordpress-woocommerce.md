# WordPress and WooCommerce Engineering

> Environments, WP-CLI, themes, page builders, WooCommerce specifics, updates and rollback. Knowledge as of 2026-10. Run the Freshness Protocol before relying on version numbers.

## 1. Current versions and what they change for releases

| Date | Release | Release impact | Label |
|------|---------|----------------|-------|
| 2025-07-07 | WooCommerce 10.0 | Major line; extension compatibility check before upgrade | [Official, changelog] |
| 2025-12-02 | WordPress 6.9 "Gene"; Abilities API in core (machine readable capabilities for plugins, themes and core, exposed under `wp-abilities/v1` when enabled) | Plugins can expose actions to AI agents; review which abilities are exposed and to whom | [Official, 2025-11 and 2025-12] |
| 2025-12-10 | WooCommerce 10.4 | Abilities API integration work; MCP adapter in WooCommerce updated | [Official, changelog] |
| 2026-03-31 | WordPress 7.0 delayed for stability (real time collaboration storage) | Plan upgrades after the first point release, not on day one | [Official and secondary, 2026-04] |
| 2026-05-20 | WordPress 7.0 shipped: AI Client, Abilities API in JavaScript, Connectors hub, minimum PHP 7.4; real time collaboration pulled before launch | Check hosting PHP version and plugin compatibility before upgrading | [Official, 2026-04-22 schedule; secondary for contents] |
| 2026-08-04 | WooCommerce 11.0: removed the product block editor block registry and block templates PHP API (compatibility shims added) | Extensions that used those APIs need testing; watch for fatals in logs | [Official, changelog] |
| 2026-08-19 | WordPress 7.1 "Mary Lou": Notes improvements, Abilities API validation hooks and lifecycle action; real time collaboration still not shipped | Minor for releases | [Official, 2026-07-31; secondary] |
| 2026-09-17 | WordPress 7.1.1 | Maintenance | [Secondary] |
| 2026-10-07 | WooCommerce 11.2.0 (requires WordPress 7.0, tested to 7.1, PHP 7.4 minimum) | Stores still on WordPress 6.x cannot take current WooCommerce security fixes | [Official, readme.txt] |

WooCommerce ships a release about every 4 to 6 weeks (10.0 on 2025-07-07 through 11.2 on 2026-10-07). Treat each as an L2 release on a store, never an auto update on production.

## 2. Environments

| Environment | Tooling | Data | Rules |
|-------------|---------|------|-------|
| Local | `wp-env` (Docker, official), DDEV, LocalWP | Sanitized copy or seeded fixtures | No production customer data on laptops; scrub emails and addresses if a copy is needed |
| Staging | Host staging (WP Engine, Kinsta, Cloudways, SiteGround and similar) or a separate install | Copy of production, refreshed before each L2+ release | Block indexing (`Discourage search engines` plus HTTP auth); disable outgoing email (mail catcher plugin or SMTP sink); switch payment gateways to test mode; disable webhooks to CRM and ERP |
| Production | Host | Live orders and customers | Changes only through the release pipeline; no plugin installs from the admin without a change request |

The WooCommerce staging trap: pushing a staging database to production overwrites orders, customers and stock placed since the copy. Push files and code, not the database. Re-apply settings changes on production by hand or with WP-CLI scripts recorded in the change request. Host "push to live" tools often default to files plus database: select files only.

## 3. WP-CLI command map with gates

| Command | Purpose | Gate |
|---------|---------|------|
| `wp core version --extra`, `wp core check-update` | Versions | G0 |
| `wp plugin list --fields=name,status,version,update_version --format=json` | Inventory and pending updates | G0 |
| `wp theme list`, `wp option get siteurl`, `wp cron event list` | Read state | G0 |
| `wp db export backups/$(date +%F_%H%M).sql` | Backup before release (on the server; keep out of git and web root) | G2 |
| `wp plugin update <slug> --dry-run` | Preview updates | G0 |
| `wp plugin update <slug>` on staging | Update on staging | G2 |
| `wp plugin update <slug>` on production | Update live | G3 |
| `wp plugin install <slug> --version=<x.y.z> --force` | Roll back one plugin | G3 on production |
| `wp search-replace 'https://old' 'https://new' --dry-run --report-changed-only` | Preview URL migrations | G0 |
| `wp search-replace ... --all-tables` without dry run | Rewrites the database | G3 (snapshot first) |
| `wp cache flush`, `wp transient delete --expired` | Cache | G2 on staging, G3 on production (can cause load spikes) |
| `wp maintenance-mode activate` | Maintenance page | G3 (customer visible) |
| `wp user list --role=administrator --fields=user_login,user_registered` | Security review | G0 (do not export emails) |
| `wp wc ...` (WooCommerce REST through CLI) | Products, orders, coupons | G0 for list and get; G3 for create, update, delete on production; delete is G4 |
| `wp db import` on production | Restore | G3, and only after exporting orders placed since the backup |

Use aliases so the target is explicit: `wp @staging plugin list`, `wp @prod plugin list` defined in `wp-cli.yml`. Never run write commands without the alias. The Ads Master guard does not yet recognize `wp @prod` writes ([Release process](release-process-and-rollback.md) section 10), so state the gate yourself.

## 4. Themes and builders

| Setup | Where the change lives | Release method | Gotchas |
|-------|-----------------------|----------------|---------|
| Classic theme with child theme | PHP templates in the child theme (`wp-content/themes/<child>`) | Git deploy of the child theme | Never edit the parent theme; parent updates overwrite it |
| Block theme (FSE) | `theme.json`, `templates/*.html`, `parts/*.html` in files, but editor customizations stored in the database (`wp_template`, `wp_template_part`, `wp_global_styles` posts) | Git for files; database edits exported (Site Editor export or copy) and re-applied | A database customization overrides the file. A deploy can appear to "not work" because the database version wins. Check for customized templates before deploying file changes |
| Page builders (Elementor, Divi, Bricks, Beaver Builder) | Layout JSON in post meta in the database | Build on staging, export template, import on production; or rebuild on production in a draft page and publish (G3) | Regenerate builder CSS after import; global widgets and kits affect many pages; builder updates are L4 |
| Gutenberg content | Post content in the database | Create as draft on production, preview, publish with approval | Reusable blocks (synced patterns) change every page that uses them |
| Headless WordPress | Next.js front end, WP as CMS | See [Next.js and headless](nextjs-headless-and-webflow.md) | Preview mode for drafts must be protected |

## 5. WooCommerce specifics

| Area | Engineering rule |
|------|------------------|
| HPOS (High Performance Order Storage) | Confirm HPOS status and compatibility mode before plugin upgrades; extensions reading `wp_posts` for orders break. Check `WooCommerce > Settings > Advanced > Features` |
| Cart and Checkout blocks vs shortcodes | Know which one the store uses. Block checkout extensions use the Store API and Checkout Blocks integration; legacy hooks (`woocommerce_after_checkout_form` and similar) do not run in block checkout |
| Payment gateways | Test mode on staging only; on production, test with the gateway's test or sandbox mode if it supports a test environment, or a real low value order refunded immediately (G3, approval) |
| Store API and caching | Exclude cart, checkout, my account and `?wc-ajax=` endpoints from page cache and CDN cache; confirm `Cache-Control: no-store` on cart fragments |
| Emails | Staging must not send customer emails. Use a mail catcher. Verify on production with a test order to a test inbox |
| Scheduled actions (Action Scheduler) | Large queues after imports or migrations slow sites; check `Tools > Scheduled Actions` failed and pending counts before and after releases |
| Taxes and prices display | Tax inclusive vs exclusive display changes the price shown in ads and feeds; any change is L2 and needs `commerce-feeds` parity check |
| Structured data | WooCommerce outputs Product markup; theme or SEO plugins may duplicate it. Check one Product entity per PDP (hand off to `seo` if wrong). WooCommerce 11.2 fixed filters returning multiple schema types |
| Abilities and MCP | WooCommerce registers domain abilities for product and order management and an MCP adapter (developer feature through 2025 and 2026). Any MCP exposure of order or customer data is a security review item (who can call it, which roles) |

## 6. Update strategy

Evidence: Patchstack counted 11,334 new WordPress ecosystem vulnerabilities in 2025 (up 42% on 2024), 91% in plugins, 9% in themes, six in core; 46% had no patch at disclosure; a weighted median of about five hours from disclosure to mass exploitation for heavily targeted flaws [Study, Patchstack 2026 report via secondary summaries; verify in the whitepaper].

| Update type | Policy |
|-------------|--------|
| Core minor (security) | Allow auto updates (default) and verify with smoke tests the same day |
| Core major | Wait for the first point release unless a security issue forces it; staging first; full smoke tests |
| Plugin with a security fix for an exploited issue | L5 fast track: staging smoke test, then production the same day |
| Plugin feature updates | Weekly batch on staging; production after smoke tests; one plugin per commit in the change log so rollback is per plugin |
| WooCommerce and payment or shipping extensions | L2; staging with test orders; never on Friday or in a sale week |
| Abandoned plugins (no update in 12 months, closed on wordpress.org) | Replace; record in the dependency health log ([UI primitives and dependencies](ui-primitives-and-dependencies.md)) |
| Nulled or pirated premium plugins | Remove; treat the site as potentially compromised and run a security review |

Use a vulnerability feed (Patchstack, Wordfence Intelligence, WPScan) or the host's scanner. Read only checks are G0; applying fixes follows the gates above.

## 7. Caching and CDN

1. Purge order on release: application cache (object cache), page cache plugin, host cache, CDN. Purging all at peak can spike load: purge only changed URLs where possible.
2. Never cache personalized fragments (mini cart, account menu, geo pricing) at the CDN without cache keys that vary correctly.
3. After a price change, verify the price on the live PDP from a clean session (incognito, no admin cookie): admins often bypass the cache and see the new price while customers see the old one.
4. Logged in admin sessions bypass most caches. QA as a logged out visitor.

## 8. Rollback on WordPress

| Failure | Rollback |
|---------|----------|
| Plugin update broke the site | Roll back the plugin version (`wp plugin install <slug> --version=<old> --force`, G3) or deactivate it if not critical. If wp-admin is down, rename the plugin folder over SSH or SFTP (G3) |
| Theme code deploy | Redeploy the previous git tag of the child theme |
| Builder or content change | Restore the post revision (posts have revisions; builder templates may not); re-import the exported template |
| Database migration or search replace | Restore the pre release export after exporting orders and customers created since (WooCommerce) and re-importing them, or restore only the affected tables. Plan this before running the migration |
| Full site compromise | Incident runbook: take a forensic copy, restore from a clean backup, rotate all credentials and salts, update everything, review admin users |

## 9. WordPress QA additions

| Check | How |
|-------|-----|
| PHP error log clean after release | Host log viewer or `wp eval 'error_log("qa marker");'` then tail; look for fatals and deprecations from updated plugins |
| Debug display off in production (`WP_DEBUG_DISPLAY` false) | `wp config get WP_DEBUG_DISPLAY` |
| Forms submit and route to the right inbox or CRM in test mode | Playwright lead form template with the QA header ([Automated QA](automated-qa-and-tests.md)) |
| Checkout works for guest and logged in users, with coupon, with each payment method in test mode | Staging tests |
| `xmlrpc.php` disabled or rate limited if unused; `wp-login.php` protected | Security review |
| No staging URL or `noindex` leaked into production after a push | View source, `wp option get blog_public` |
| Builder CSS regenerated and cached assets refreshed | Visual diff |
