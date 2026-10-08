# Platform Implementation: Shopify (and Monolith Equivalents)

How to build storefront patterns on Shopify Online Store 2.0 themes in 2026: sections, theme blocks, app blocks, metafields and metaobjects, Liquid recipes, cart and search APIs, standard storefront events and actions, Functions, Markets, Rollouts, and the release gates. Ends with a mapping to WooCommerce, Shopware and Adobe Commerce. Recipes are original minimal examples, not copies of Horizon or Dawn code. Releases, previews, QA and rollback run through `site-engineer`.

## 1. Platform reality (2026-10)

| Topic | State | Label |
|-------|-------|-------|
| Default theme family | Horizon (launched 2025-05-21 with 10 presets; v4.2.0 dated 2026-09-18, repo commit 2026-09-21); nested theme blocks (reported up to 8 levels); AI block generation in the editor | [Official, 2025-05 to 2026-09] |
| Dawn | Still maintained in the open (v16.0.0, last commit 2026-08-10); reported to receive fixes but no new features | [Official repo] [Unverified on roadmap] |
| Horizon license | Derived themes may be delivered to a merchant for that merchant's own store as part of a services engagement; not resold, listed or distributed; Theme Store submissions must start from the Skeleton theme | [Official, license text] |
| Theme blocks | Files in `/blocks`, rendered with `{% content_for 'blocks' %}` or as static blocks with `{% content_for 'block', type: '...', id: '...' %}`; private blocks prefixed with `_` | [Official] |
| Setting types | Include `metaobject` (needs `metaobject_type`), `metaobject_list`, `color_palette`, `color_scheme`, `product_list`, `collection_list`, `text_alignment`, `video` | [Official, theme-liquid-docs 2026-10] |
| Standard storefront events and actions | Spring '26 (2026-06-17): events such as `shopify:product:view`, `shopify:cart:lines-update`, `shopify:search:update`; actions `Shopify.actions.updateCart`, `getCart`, `openCart` on every Liquid storefront; cart attribute support added later; library at `cdn.shopify.com/storefront/standard-events.js` | [Official, 2026-06] |
| Speculation rules | Platform-wide prefetch rules on Liquid storefronts since 2025-06 (conservative eagerness per Shopify), up to 180 ms faster loads | [Official, 2025-06] |
| Checkout | Checkout extensibility only; Scripts stopped 2026-06-30; non-Plus Thank you and Order status pages auto-upgraded 2026-08-26 | [Official, 2026] |
| Customer accounts | Legacy accounts deprecated 2026-02-26; theme without legacy templates triggers upgrade | [Official, 2026-02] |
| Script tags | Reports: apps cannot create or update script tags from 2026-10-01, script tags stop running on storefronts 2027-03-01; use theme app extensions and app embeds | [Unverified, secondary 2026] |
| Rollouts | Native theme and checkout experiments: Grow plan and higher, 50/50 default, 90 day default end, metrics conversion, bounce, reached checkout, add to cart; no custom metrics | [Official, Help Center 2026] |
| Nested cart lines | Ajax Cart API (`parent_id`, `parent_line_key`), Storefront API and Checkout UI 2025-10+; cannot nest under bundles yet | [Official, 2025-10] |
| Functions | Generally available; Cart Transform (expand, merge; up to 150 bundle components), discounts, payment and delivery customization, validation | [Official] |

## 2. Architecture rules for storefront builds

1. JSON templates plus sections everywhere; merchant-editable content lives in section and block settings, metafields or metaobjects, never hardcoded strings (use `t` translation keys).
2. One theme block per reusable PDP element (trust lines, size guide link, delivery promise, GPSR info) so merchants can place it; private `_` blocks for internal pieces.
3. Product-specific content in metafields (product, variant) and shared structured content in metaobjects (size charts, ingredient glossaries, care guides); reference them from blocks with `metaobject` settings or dynamic sources.
4. App functionality through app blocks and app embeds (theme app extensions), not script tags or pasted snippets.
5. Server-render first; JavaScript as progressive enhancement; use the Section Rendering API for partial updates.
6. Every interactive component follows the markup in the [Pattern library](ux-pattern-library.md) and passes [Accessibility](accessibility-and-eaa.md) checks.
7. Budget per template: count app embeds and their JS; anything that does not earn its weight is removed (G3 change, with approval).

## 3. Recipes

### R1. Theme block: trust lines under the buy button

`blocks/trust-lines.liquid`:

```liquid
{% doc %}
  Short service facts under the buy buttons (returns, shipping, delivery).
  Text comes from block settings so each market can be translated.
{% enddoc %}
<ul class="trust-lines" {{ block.shopify_attributes }}>
  {%- for i in (1..3) -%}
    {%- assign key = 'line_' | append: i -%}
    {%- if block.settings[key] != blank -%}
      <li class="trust-lines__item">{{ block.settings[key] }}</li>
    {%- endif -%}
  {%- endfor -%}
</ul>
{% schema %}
{
  "name": "Trust lines",
  "settings": [
    { "type": "inline_richtext", "id": "line_1", "label": "Line 1", "default": "Free returns within 30 days" },
    { "type": "inline_richtext", "id": "line_2", "label": "Line 2" },
    { "type": "inline_richtext", "id": "line_3", "label": "Line 3" }
  ],
  "presets": [{ "name": "Trust lines" }]
}
{% endschema %}
```

Copy in defaults must match `brand/PRODUCT_FACTS.md` (returns window) and pass `compliance`.

### R2. Size guide from a metaobject

Create a metaobject definition `size_chart` (fields: `title`, `table` as rich text or JSON, `how_to_measure`, `unit_note`) and a product metafield `custom.size_chart` referencing it.

```liquid
{%- assign chart = product.metafields.custom.size_chart.value -%}
{%- if chart -%}
  <button type="button" class="link" aria-haspopup="dialog" aria-controls="size-guide-{{ block.id }}"
          onclick="document.getElementById('size-guide-{{ block.id }}').showModal()">
    {{ 'products.size_guide' | t }}
  </button>
  <dialog id="size-guide-{{ block.id }}" aria-labelledby="size-guide-title-{{ block.id }}">
    <h2 id="size-guide-title-{{ block.id }}">{{ chart.title }}</h2>
    {{ chart.table }}
    {{ chart.how_to_measure }}
    <form method="dialog"><button>{{ 'actions.close' | t }}</button></form>
  </dialog>
{%- endif -%}
```

Prefer an event listener in a module over the inline `onclick` if the theme has a CSP; native `<dialog>` gives Escape, focus containment and an inert background.

### R3. Variant option as an accessible radio group

```liquid
{%- for option in product.options_with_values -%}
  <fieldset class="variant-option">
    <legend>{{ option.name }}: <span data-selected>{{ option.selected_value }}</span></legend>
    {%- for value in option.values -%}
      {%- capture input_id -%}opt-{{ section.id }}-{{ option.position }}-{{ forloop.index }}{%- endcapture -%}
      <input type="radio" id="{{ input_id }}" name="{{ option.name | handle }}-{{ section.id }}"
             value="{{ value | escape }}" {% if value.selected %}checked{% endif %}
             {% unless value.available %}aria-describedby="{{ input_id }}-status"{% endunless %}>
      <label for="{{ input_id }}">
        {{ value }}
        {%- unless value.available -%}
          <span id="{{ input_id }}-status" class="visually-hidden">, {{ 'products.sold_out' | t }}</span>
        {%- endunless -%}
      </label>
    {%- endfor -%}
  </fieldset>
{%- endfor -%}
```

Do not add `disabled` to sold-out values; style them and keep them selectable so the notify form can appear. Script: on change, resolve the variant, update price, stock, media and the URL `?variant=`, and announce in a `role="status"` element.

### R4. Unit price and price block

```liquid
{%- assign v = product.selected_or_first_available_variant -%}
<div class="price" data-price>
  {%- if v.compare_at_price > v.price -%}
    <span class="visually-hidden">{{ 'products.sale_price' | t }}</span>
    <span class="price__sale"><bdi>{{ v.price | money }}</bdi></span>
    <span class="visually-hidden">{{ 'products.regular_price' | t }}</span>
    <s class="price__regular"><bdi>{{ v.compare_at_price | money }}</bdi></s>
  {%- else -%}
    <span class="price__regular"><bdi>{{ v.price | money }}</bdi></span>
  {%- endif -%}
  {%- if v.unit_price_measurement -%}
    <small class="unit-price"><bdi>{{ v.unit_price | unit_price_with_measurement: v.unit_price_measurement }}</bdi></small>
  {%- endif -%}
  <small class="tax-note">{{ 'products.tax_included' | t }}</small>
</div>
```

Compare-at display rules (EU 30-day prior price, Turkey's own rule) come from `compliance`; store the prior-lowest price in a variant metafield if the store must show it.

### R5. Free shipping progress per market

Store the threshold per market as a money metafield on the market (`localization.market.metafields.custom.free_shipping_threshold`) so it matches the market's shipping rates.

```liquid
{%- assign threshold = localization.market.metafields.custom.free_shipping_threshold.value -%}
{%- if threshold -%}
  {%- assign threshold_cents = threshold.amount | times: 100 | round -%}
  {%- assign remaining = threshold_cents | minus: cart.total_price -%}
  <div class="ship-progress" data-ship-progress>
    {%- if remaining > 0 -%}
      {%- assign remaining_formatted = remaining | money -%}
      <p>{{ 'cart.free_shipping_remaining' | t: amount: remaining_formatted }}</p>
    {%- else -%}
      <p>{{ 'cart.free_shipping_unlocked' | t }}</p>
    {%- endif -%}
    <progress max="{{ threshold_cents }}" value="{{ cart.total_price | at_most: threshold_cents }}"
              aria-hidden="true"></progress>
  </div>
{%- endif -%}
```

The text carries the meaning; the bar is hidden from assistive tech. Re-render this snippet through the Section Rendering API after every cart change. `cart.total_price` is in the presentment currency's minor units; confirm the metafield's money currency equals the market currency and verify the money object's shape (`amount`) in your theme before shipping. If discounts apply at checkout only, say "before discounts" or compute from `cart.total_price` after cart-level discounts.

### R6. Add to cart with section rendering and standard events

```js
// Minimal module: add, re-render the cart drawer section, open it, announce.
const status = document.querySelector('[data-cart-status]'); // role="status" element present at load
async function addToCart(form) {
  const body = new FormData(form);
  body.append('sections', 'cart-drawer');
  body.append('sections_url', window.location.pathname);
  const res = await fetch(`${window.Shopify.routes.root}cart/add.js`, { method: 'POST', body, headers: { Accept: 'application/json' } });
  const data = await res.json();
  if (!res.ok) { showInlineError(form, data.description || data.message); return; }
  replaceSection('cart-drawer', data.sections['cart-drawer']);
  status.textContent = `${data.product_title} added to cart`;
  if (window.Shopify?.actions?.openCart) window.Shopify.actions.openCart(); else openDrawer();
}
document.addEventListener('shopify:cart:lines-update', () => refreshCartCount());
```

Notes: verify action and event payload shapes in the current docs before relying on them (events exist only where the theme implements them; actions exist on every Liquid storefront). Keep the button state machine from [Notifications](notifications-feedback-and-microinteractions.md). Refresh the drawer on `pageshow` when `event.persisted` is true.

### R7. Nested add-on (warranty) with the parent

```js
await fetch(`${Shopify.routes.root}cart/add.js`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
  body: JSON.stringify({ items: [
    { id: parentVariantId, quantity: 1 },
    { id: warrantyVariantId, quantity: 1, parent_id: parentVariantId }
  ] })
});
```

Add the parent first (or in the same request); a child before its parent returns an error. For a line already in the cart use `parent_line_key`. Render children indented under the parent in the cart and drawer. Add-ons cannot nest under bundles yet.

### R8. Predictive search request

```js
const url = new URL(`${Shopify.routes.root}search/suggest`, location.origin);
url.searchParams.set('q', term);
url.searchParams.set('resources[type]', 'query,product,collection,page');
url.searchParams.set('resources[limit]', '6');
url.searchParams.set('resources[limit_scope]', 'each');
url.searchParams.set('section_id', 'predictive-search'); // server-rendered results
controller?.abort(); controller = new AbortController();
const html = await (await fetch(url, { signal: controller.signal })).text();
```

Debounce input by about 200 ms, ignore stale responses, render into a `role="listbox"` and manage `aria-activedescendant` (pattern P11).

### R9. Filters with counts and removable chips

```liquid
<form action="{{ collection.url }}" method="get" data-filters>
  {%- for filter in collection.filters -%}
    {%- if filter.type == 'list' or filter.type == 'boolean' -%}
      <fieldset>
        <legend>{{ filter.label }}</legend>
        {%- for value in filter.values -%}
          {%- if value.count > 0 or value.active -%}
            <label>
              <input type="checkbox" name="{{ value.param_name }}" value="{{ value.value }}" {% if value.active %}checked{% endif %}>
              {{ value.label }} <span class="count">({{ value.count }})</span>
            </label>
          {%- endif -%}
        {%- endfor -%}
      </fieldset>
    {%- elsif filter.type == 'price_range' -%}
      <fieldset>
        <legend>{{ filter.label }}</legend>
        <label>{{ 'filters.from' | t }} <input type="number" inputmode="decimal" name="{{ filter.min_value.param_name }}" value="{% if filter.min_value.value %}{{ filter.min_value.value | divided_by: 100.0 }}{% endif %}"></label>
        <label>{{ 'filters.to' | t }} <input type="number" inputmode="decimal" name="{{ filter.max_value.param_name }}" value="{% if filter.max_value.value %}{{ filter.max_value.value | divided_by: 100.0 }}{% endif %}"></label>
      </fieldset>
    {%- endif -%}
  {%- endfor -%}
  <input type="hidden" name="sort_by" value="{{ collection.sort_by | default: collection.default_sort_by }}">
  <button type="submit">{{ 'filters.apply' | t }}</button>
</form>
<ul class="active-filters">
  {%- for filter in collection.filters -%}
    {%- for value in filter.active_values -%}
      <li><a href="{{ value.url_to_remove }}">{{ 'filters.remove' | t }}: {{ filter.label }} {{ value.label }}</a></li>
    {%- endfor -%}
  {%- endfor -%}
</ul>
<p role="status" data-results-count>{{ 'collections.product_count' | t: count: collection.products_count }}</p>
```

The form works without JavaScript (GET submit); enhance with live updates via section rendering and `history.replaceState`. Configure filters in the Search & Discovery app (metafield and variant option filters, swatches). Price inputs use plain decimals (`divided_by: 100.0`) so comma-decimal locales do not corrupt the value; show the formatted range next to the inputs for reading.

### R10. Country and language selector

```liquid
{%- form 'localization', id: 'localization-form', class: 'localization' -%}
  <label for="country-select">{{ 'localization.country' | t }}</label>
  <select id="country-select" name="country_code">
    {%- for country in localization.available_countries -%}
      <option value="{{ country.iso_code }}" {% if country.iso_code == localization.country.iso_code %}selected{% endif %}>
        {{ country.name }} ({{ country.currency.iso_code }})
      </option>
    {%- endfor -%}
  </select>
  <label for="language-select">{{ 'localization.language' | t }}</label>
  <select id="language-select" name="language_code">
    {%- for language in localization.available_languages -%}
      <option value="{{ language.iso_code }}" lang="{{ language.iso_code }}" {% if language.iso_code == localization.language.iso_code %}selected{% endif %}>
        {{ language.endonym_name }}
      </option>
    {%- endfor -%}
  </select>
  <button type="submit">{{ 'localization.update' | t }}</button>
{%- endform -%}
```

RTL: render `<html lang="{{ request.locale.iso_code }}" dir="{{ request.locale.direction }}">` where the theme supports `request.locale.direction` (Horizon 4.2.0); otherwise derive `rtl` for `ar`, `he`, `fa`, `ur`.

### R11. LCP image and speculation rules

```liquid
{{ product.featured_media | image_url: width: 1400 | image_tag:
   loading: 'eager', fetchpriority: 'high',
   widths: '400, 600, 800, 1000, 1200, 1400',
   sizes: '(min-width: 990px) 55vw, 100vw' }}
```

Only the first gallery image gets `eager` and `fetchpriority`; the rest `loading: 'lazy'`. Speculation: Shopify already prefetches; add prerender only for high-confidence collection to product links and never for cart, checkout, account or logout URLs. Prerender runs analytics scripts, so coordinate with `measurement` before enabling it.

```html
<script type="speculationrules">
{ "prefetch": [{ "where": { "and": [
    { "selector_matches": ".product-grid a[href*='/products/']" },
    { "not": { "href_matches": "/cart*" } } ] }, "eagerness": "moderate" }] }
</script>
```

## 4. Search & Discovery and native search setup

1. Filters: Online Store > Navigation > Search & Discovery app: add filters from product options, metafields (category metafields from the Shopify Standard Product Taxonomy), vendor, product type, availability, price. Order by usage.
2. Swatches: use the category metafield color values or `swatch` data so filters and variant pickers share swatches.
3. Synonyms: groups from the zero result report; retest after each change (2026 reports of dropped groups and SKU issues).
4. Product boosts and recommendations: complements and related products per product; exclude items via the app where possible.
5. Run the 12 relevance checks in [Search and merchandising](search-and-merchandising.md) section 4.

## 5. Markets setup touchpoints in the theme

- Prices from Liquid money filters reflect the market currency; never hardcode currency symbols.
- Market-specific content: market metafields (thresholds, delivery promise text), or blocks shown per market with `localization.market.handle` conditions (keep these few).
- Translations: Translate and Adapt app or a TMS; theme strings in locale files; product content per language.
- Payment icons: show only methods available in the market (`shop.enabled_payment_types` lists all store methods; filter per market in settings when needed).

## 6. Development and release workflow (gates)

| Step | Command or action | Gate |
|------|-------------------|------|
| Pull the live theme for reading | `shopify theme pull --theme <id>` into a local branch | G0 or G1 |
| Develop locally against a dev theme | `shopify theme dev --store <store>` | G1 |
| Lint | `shopify theme check` (Theme Check) | G1 |
| Push to an unpublished theme for preview | `shopify theme push --unpublished` | G2 (hook asks) |
| Share preview link and QA | `site-engineer` release checklist, accessibility protocol, worst-case data | G2 |
| Experiment | Rollouts experiment on the unpublished theme with `cro` | G3 (approval) |
| Publish | `shopify theme publish` or Rollouts launch | G3 (approval every time) |
| Delete a theme | Never by an agent | G4 |

Change requests use `ads-master/templates/CHANGE_REQUEST.md` with the theme ID, files changed, screenshots, rollback (republish previous theme ID) and the metric to watch.

## 7. Horizon or Dawn (or a premium theme)?

| Situation | Choice |
|-----------|--------|
| New store or full redesign, services engagement | Horizon (or a Horizon preset); build custom blocks; respect the license |
| Building a theme to sell or list | Skeleton theme (Horizon and Dawn derivatives are not eligible) |
| Stable Dawn store with good metrics | Stay; migrate when a redesign is planned (manual rebuild, no automatic migration) |
| Premium theme with heavy customization | Audit performance and accessibility first; migration only with a business case |

## 8. Mapping to other monolith platforms

| Shopify concept | WooCommerce | Shopware 6 | Adobe Commerce (Magento) |
|-----------------|-------------|------------|--------------------------|
| Sections and theme blocks | Block themes: templates, template parts, patterns, blocks (Site Editor) | Shopping Experiences layouts and CMS blocks, Twig templates | Page Builder, layout XML, Luma or Hyvä templates |
| Metafields and metaobjects | Post meta, product attributes, custom fields plugins | Custom fields, properties | EAV attributes, custom modules |
| Search & Discovery filters | Product Filters block (active filters, attribute, price, rating, status, taxonomy, chips) | Property filters in listing, OpenSearch or Elasticsearch for large catalogs | Layered navigation with OpenSearch |
| Ajax Cart API and standard events | Store API (`/wp-json/wc/store/v1/cart`), Interactivity API stores in blocks | Store API (`/store-api/checkout/cart`), storefront JS plugins | GraphQL cart mutations, customer-data sections |
| Cart drawer | Mini-Cart block | Off-canvas cart (core) | Minicart (Luma), Hyvä off-canvas |
| Variant picker | Add to Cart with Options block (variation selector, grouped selector, quantity) | Variant switch configurator | Configurable product swatches |
| Functions | PHP hooks and filters | Rule builder, Flow builder, apps | Plugins, observers |
| Checkout extensibility | Checkout block with extensibility APIs | Twig overrides, apps | Knockout checkout or Hyvä Checkout |
| Theme Check | PHPCS with WordPress standards, Lighthouse | Shopware CLI tooling, Lighthouse | Static tests, Lighthouse |

Reference code for WooCommerce lives in `woocommerce/plugins/woocommerce/client/blocks/assets/js/blocks/` (product-filters, mini-cart, add-to-cart-with-options). On Adobe Commerce, Luma's JavaScript weight is the usual INP and LCP problem (44.3% of Adobe Commerce origins passed mobile CWV vs 76.5% for Shopify in a June 2026 CrUX analysis, secondary source) [Unverified]; Hyvä or a headless front end are the structural fixes, decided with `site-engineer`.
