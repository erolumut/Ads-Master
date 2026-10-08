# Homepage and Navigation

Information architecture, header, mega menus, mobile menus, homepage sections and footer. Patterns: P01 to P09 in the [Pattern library](ux-pattern-library.md). Implementation recipes: [Shopify](platform-implementation-shopify.md), [Headless](platform-implementation-headless.md).

## 1. Evidence snapshot

| Finding | Source | Label |
|---------|--------|-------|
| 58% of desktop and 67% of mobile leading sites mediocre or worse on homepage and category navigation; 16,000+ scores, 180+ sites | Baymard Homepage and Navigation UX 2025 | [Study, 2025] |
| 59% of mobile homepages do not provide full scope links | Baymard 2025 | [Study, 2025] |
| 33% of mobile sites do not make product categories the top level items | Baymard (older article) | [Study, pre-2025] |
| Taxonomy, main navigation and intermediary category pages have the most room to improve | Baymard 2025 | [Study, 2025] |
| Hidden navigation is less discoverable and used later (179 participants, 6 sites) | NN/g hamburger study | [Study, NN/g] |
| Hamburger icon now widely recognized, risks of hidden navigation remain; visible or combination navigation preferred when 4 to 5 top options | NN/g 2025 update and mobile navigation primer | [Study, 2025] |
| Mega menus save users time on deep journeys; arrange in columns | NN/g mega menu articles | [Study, NN/g] |
| Horizon mega menu offers several desktop and mobile layouts | Shopify Summer '25 Edition coverage | [Official, 2025-05] |

## 2. Information architecture procedure

1. **Collect the customer vocabulary**: top 200 site search queries, top Google Search Console queries (from `seo`), support ticket wording, competitor nav labels (from `market-intel`).
2. **Card sort the catalog** (open sort with 15 customers, or closed sort with the current tree). For small budgets, use the search log as the proxy.
3. **Choose the primary axis per category**: product type (most stores), need or use case (gifts, sports), audience (women, men, kids), or brand (electronics, beauty). Use one primary axis in the main nav and expose the others as filters or secondary links.
4. **Depth and breadth**: 5 to 8 top level items on desktop; split a category once it holds more than about 10 subcategories [Unverified, secondary summary of Baymard]; avoid a third level unless the catalog has 500+ products per branch.
5. **Each node gets**: a label in customer words, a "Shop all" link, a landing page that is either an intermediary page (subcategory tiles plus bestsellers) or a PLP.
6. **Courtesy navigation**: account, help, store locator, locale selector, wishlist. Keep it out of the product nav.
7. **Write the tree** as a table and get approval before changing live menus (menu edits are live changes, G3).

IA table template:

| Level 1 | Level 2 | Level 3 | Landing type | Collection handle | Filters on this PLP | Search synonyms |
|---------|---------|---------|--------------|-------------------|---------------------|-----------------|

## 3. Header specification

| Element | Desktop | Mobile | Notes |
|---------|---------|--------|-------|
| Logo | Left (start), links home | Center or start | `alt` = store name |
| Main nav | Visible categories, mega menu for deep catalogs | Menu button opens drawer | Disclosure buttons, not ARIA menu |
| Search | Open field for 30+ SKUs | Icon plus visible field on home and PLP | See [Search](search-and-merchandising.md) |
| Account | Icon with text label or tooltip | In drawer and as icon | Link, not button |
| Cart | Icon with count | Icon with count | Count in the accessible name ("Cart, 3 items"); announce changes politely |
| Locale selector | Header utility or footer | Drawer bottom and footer | Country plus currency, language separately |
| Announcement bar | One message, static | Same, one line | No fake urgency |

Sticky header rules: sticky on scroll-up only on mobile, maximum height about 56 px when stuck, never covers focused elements (set `scroll-padding-top` to the header height, WCAG 2.4.11).

## 4. Desktop mega menu specification

Behavior:
- Trigger: top level button toggles the panel on click; on hover, open after about 150 to 250 ms of intent, close after about 300 ms of leaving. Never open on hover without click support.
- Diagonal movement: keep the panel open while the pointer moves toward it (triangle or delay technique).
- Escape closes and returns focus to the trigger. Tab moves through the panel links in visual order, then to the next top level item. Do not trap focus.
- Clicking a top level label that is also a link: split into a link (label) and a disclosure button (chevron), or make the label a button and put "Shop all <category>" first in the panel.

Layout:
- 3 to 5 link columns grouped under headings (Clothing, Shoes, Accessories), alphabetized or ordered by demand, not by stock.
- Optional 1 promo tile with real image and text link, never more than 25% of the panel width.
- Panel height fits a 768 px viewport without scrolling.

Markup outline (disclosure navigation):

```html
<nav aria-label="Main">
  <ul class="nav">
    <li>
      <button type="button" aria-expanded="false" aria-controls="mm-women">Women</button>
      <div id="mm-women" class="mega" hidden>
        <a href="/collections/women">Shop all women</a>
        <section aria-labelledby="mm-women-clothing">
          <h2 id="mm-women-clothing">Clothing</h2>
          <ul><li><a href="/collections/women-dresses">Dresses</a></li></ul>
        </section>
      </div>
    </li>
  </ul>
</nav>
```

Anti patterns: `role="menu"` and `role="menuitem"` for site navigation (forces application-style keyboard handling that users do not expect), panels that render only on hover in JS (invisible to crawlers and keyboard), images without dimensions (CLS), mega menus on 1 to 10 SKU stores.

Reference implementations: Horizon `assets/header-menu.js`, `blocks/_header-menu.liquid`; Radix Navigation Menu; Base UI Navigation Menu; W3C APG disclosure navigation example.

## 5. Mobile menu specification

- Menu button with accessible name "Menu", `aria-expanded`, `aria-controls`.
- Drawer opens from the start edge (left in LTR, right in RTL) as a modal dialog. Use native `<dialog>` with `showModal()` or a primitive (Base UI Drawer since 1.2.0, Radix Dialog). Do not start new work on vaul (unmaintained since 2025-10).
- Level 1: categories as large rows (min 44 px tall), search field at top, then account, help, locale.
- Level 2 and 3: slide-in panel with "Back" button and the level title as heading; first row "Shop all <category>".
- Close button visible at all times; Escape closes; focus returns to the menu button.
- `overscroll-behavior: contain` on the panel; body scroll locked; panel uses `100dvh`; safe area padding at bottom.
- Optional: 4 to 6 visible category chips under the header on home and PLP (combination navigation, NN/g).

## 6. Homepage section jobs

| Section | Job (the question it answers) | When to include | KPI | Common failure |
|---------|-------------------------------|-----------------|-----|----------------|
| Hero | What is this store and why buy here | Always | Hero CTA clicks, bounce | Auto-rotating slides, text in image |
| Shop by category (full scope) | Where do I find X | 10+ SKUs | Category tile CTR | Promo subsets only (P04) |
| Bestsellers or featured collection | What do people buy | Always | Product clicks, ATC from home | 20-item carousels |
| Value propositions (3 to 4) | Why trust this store | Always | Scroll depth past block | Generic "quality" claims; claims not in CLAIMS.md |
| Social proof (reviews, press) | Do others like it | When real proof exists | Engagement | Fabricated or unverifiable logos |
| New arrivals or seasonal | What is new | Fashion, frequent drops | Clicks | Stale seasonal content |
| Editorial or how-to | How do I choose | Considered purchases | Clicks to PLP or PDP | Blog dump |
| Brand story | Who is behind it | DTC brands | Time on section | Above the fold on paid traffic |
| Newsletter | Stay in touch | Always, near footer | Signup rate | Popup on first visit before any content |
| Store locator or pickup | Can I buy nearby | Omnichannel | Clicks | Missing hours |

Order for a typical DTC store: hero, categories, bestsellers, value props, proof, editorial, newsletter. For 1 to 10 SKU stores: hero, product benefits, product selector or comparison, proof, FAQ, guarantee, then a buy section (the homepage often works as a long-form PDP).

Rules:
- One `h1` (the hero headline or a visually hidden store name).
- Every app-injected section has an owner and a KPI, or it is removed (app sections are the main cause of homepage bloat).
- Paid traffic does not land on the homepage by default; `cro` and channel agents choose landing pages.

## 7. Footer specification

Column order: Help (shipping, returns, track order, contact, size guide), Shop (top categories), About (story, sustainability, careers), Legal (terms, privacy, cookie settings, imprint where required, accessibility statement, withdrawal function link for EU), then locale selector, payment icons (methods truly available in the visitor's market) and social links.

EU and German specifics: Impressum link (Germany, Austria), cookie settings re-entry link, accessibility statement (EAA service information), "Withdraw from contract here" entry (EU from 2026-06-19). Wording from `compliance`.

## 8. 404 and empty states

- 404: search field, top categories, bestsellers, contact link; log broken inbound URLs and hand redirects to `seo`.
- Empty collection: explain, show related collections, never a blank grid.

## 9. Measurement for navigation changes

Before/after or test (`cro`) with: navigation click-through by item (event `nav_click` with label and level; spec handed to `measurement`), search usage change (good nav often lowers search exits, not search usage), PLP entry rate, bounce on homepage, RPV. Navigation restructures for 500+ SKU stores are TF unless they fix a defect (missing category, broken links).
