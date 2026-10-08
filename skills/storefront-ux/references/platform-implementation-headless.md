# Platform Implementation: Headless (React and Next.js)

Stack choices and minimal, accessible component recipes for headless storefronts (Hydrogen, Next.js Commerce, Medusa, Saleor, custom Next.js). Recipes are original, short and dependency-light; they show structure and accessibility, not a full design system. Release, preview deploys, security review and rollback go through `site-engineer`.

## 1. Stack landscape (checked 2026-10-08)

| Stack | Version or state | Best for | Watch outs | Label |
|-------|------------------|----------|-----------|-------|
| Shopify Hydrogen (skeleton template) | `@shopify/hydrogen` 2026.4.x, skeleton 2026.4.8 on React Router 7.16; Oxygen hosting; `useOptimisticCart`; Customer Account API routes | Shopify brands needing custom UX with Shopify checkout | Skeleton components are scaffolds (Aside drawer lacks focus trap); you own performance budgets | [Official repo, 2026-10] |
| Vercel Next.js Commerce | Next.js 15.6 canary, React 19, Headless UI; Server Actions, `useOptimistic`, Suspense; Vercel maintains the Shopify provider only | Learning App Router commerce patterns | Last commit 2026-06-10; demo-grade UX (disabled sold-out variants, minimal filters) | [Official repo, 2026-06] |
| Medusa Next.js starter | v1.0.3, Next.js 15.3, `[countryCode]` routing with a region map in middleware | Medusa v2 backends, multi-region | Last commit 2026-04-23 | [Official repo, 2026-04] |
| Saleor Paper storefront | Active (2026-10-01); App Router, server-first cart, URL-driven checkout steps, `/{locale}/{channel}` routes, translated slugs | Saleor backends, international by default | FSL-1.1-ALv2 license (no competing commercial use; converts to Apache 2.0 later) | [Official repo, 2026-10] |
| Custom Next.js on Shopify Storefront API | Storefront API 2026-07 and 2026-10 (`@inContext(country, language)`, optional `channelId` per coverage) | Teams with strong frontend engineering | Rebuilding search, filters, SEO and analytics that Liquid gives for free | [Official] [Unverified on channelId] |

Headless is a business decision (cost, team, speed needs), not a UX pattern. Use it when Liquid limits block a measured need; otherwise a well-built Horizon theme is faster to ship and maintain [Practitioner consensus].

## 2. UI primitives (accessibility first)

| Need | Pick | Notes | Label |
|------|------|-------|-------|
| Dialogs, drawers, popovers, menus, selects, tabs, accordions | Base UI (`@base-ui/react` 1.8.0, 1.0 since 2025-12-11; Drawer since 1.2.0 2026-02-12) or Radix Primitives (actively released) or React Aria Components (1.22.0, Apache-2.0) | Pick one family per project | [Official repos, 2026] |
| Toasts | sonner 2.0.8 (MIT, active, 2026-08) | Set duration and position; follow the decision tree in [Notifications](notifications-feedback-and-microinteractions.md) | [Official repo] |
| Mobile bottom sheets | Base UI Drawer or a native `<dialog>`; not vaul for new work | vaul is unmaintained since 2025-10-03; shadcn/ui's Drawer still wraps vaul, so replace it in shadcn projects | [Official repos] |
| Carousels | CSS scroll snap first; Embla (v9 release candidates, MIT) with `embla-carousel-accessibility` when you need controls and loop | Embla sets roles, labels and a live region | [Official repo, 2026-10] |
| Command palette (B2B quick order, internal tools) | cmdk 1.1.1 (MIT, last commit 2025-10) | Not a replacement for consumer search autocomplete | [Official repo] |
| Comboboxes and autocomplete | React Aria `Autocomplete` and `ComboBox`, Base UI `autocomplete` and `combobox` | Hand-rolled comboboxes usually fail screen readers | [Official repos] |
| Styled components on primitives | shadcn/ui (MIT): copies components into your repo on Radix or Base UI | Review each copied component for the storefront rules here | [Official repo] |
| Number transitions | Optional (NumberFlow); off under reduced motion | Decoration only | [Practitioner consensus] |

## 3. Recipes

### H1. Variant picker: radio groups with URL state (Next.js App Router)

```tsx
'use client';
import { useRouter, useSearchParams, usePathname } from 'next/navigation';

type Option = { name: string; values: { value: string; available: boolean }[] };

export function VariantPicker({ options }: { options: Option[] }) {
  const params = useSearchParams();
  const router = useRouter();
  const pathname = usePathname();
  function select(name: string, value: string) {
    const next = new URLSearchParams(params.toString());
    next.set(name.toLowerCase(), value);
    router.replace(`${pathname}?${next.toString()}`, { scroll: false });
  }
  return (
    <>
      {options.map((opt) => {
        const selected = params.get(opt.name.toLowerCase()) ?? '';
        return (
          <fieldset key={opt.name} className="variant-option">
            <legend>{opt.name}{selected ? `: ${selected}` : ''}</legend>
            {opt.values.map(({ value, available }) => {
              const id = `${opt.name}-${value}`.replace(/\s+/g, '-').toLowerCase();
              return (
                <span key={value}>
                  <input type="radio" id={id} name={opt.name} value={value}
                    checked={selected === value} onChange={() => select(opt.name, value)}
                    aria-describedby={available ? undefined : `${id}-status`} />
                  <label htmlFor={id} data-soldout={!available || undefined}>
                    {value}
                    {!available && <span id={`${id}-status`} className="sr-only">, sold out</span>}
                  </label>
                </span>
              );
            })}
          </fieldset>
        );
      })}
    </>
  );
}
```

Keep sold-out values selectable; the buy button then switches to "Notify me". Announce price and stock changes in a `role="status"` element owned by the product form.

### H2. Add to cart: server action, pending state, status region, optimistic count

```tsx
'use client';
import { useActionState } from 'react';
import { addToCart } from './actions'; // server action returning { ok: boolean, message: string }

export function AddToCart({ variantId, productTitle }: { variantId?: string; productTitle: string }) {
  const [state, formAction, pending] = useActionState(addToCart, { ok: false, message: '' });
  return (
    <form action={formAction} aria-busy={pending}>
      <input type="hidden" name="variantId" value={variantId ?? ''} />
      <button type="submit" disabled={pending} aria-describedby="atc-msg">
        {pending ? 'Adding' : 'Add to cart'}
      </button>
      <p id="atc-msg" role="status" className={state.ok ? 'sr-only' : 'form-error'}>
        {state.message || (state.ok ? `${productTitle} added to cart` : '')}
      </p>
    </form>
  );
}
```

On success, open the cart drawer (H3) and move focus to its heading. If no variant is selected, the server action returns a message and the client scrolls to the first unselected option. Optimistic cart totals: wrap the cart in `useOptimistic` (Next.js Commerce `components/cart/cart-context.tsx`) or `useOptimisticCart` (Hydrogen) and reconcile with the server result.

### H3. Cart drawer with Base UI Drawer (or Dialog)

```tsx
import { Drawer } from '@base-ui/react/drawer';

export function CartDrawer({ open, onOpenChange, count, children, footer }: {
  open: boolean; onOpenChange: (o: boolean) => void; count: number;
  children: React.ReactNode; footer: React.ReactNode;
}) {
  return (
    <Drawer.Root open={open} onOpenChange={onOpenChange}>
      <Drawer.Portal>
        <Drawer.Backdrop className="cart-backdrop" />
        <Drawer.Popup className="cart-drawer">
          <Drawer.Title>Your cart ({count})</Drawer.Title>
          <Drawer.Close aria-label="Close cart">x</Drawer.Close>
          <div className="cart-drawer__lines">{children}</div>
          <div className="cart-drawer__footer">{footer}</div>
        </Drawer.Popup>
      </Drawer.Portal>
    </Drawer.Root>
  );
}
```

Check the exact part names and props against the installed Base UI version (the API moved fast through 2026). CSS: `.cart-drawer { height: 100dvh; overscroll-behavior: contain; padding-bottom: env(safe-area-inset-bottom); }`; enter with `transform: translateX(100%)` to `0` over about 280 ms ease-out, mirrored in RTL; reduced motion: no slide. Native alternative: `<dialog>` with `showModal()` gives focus containment, Escape and an inert background without a library.

### H4. Predictive search combobox (hand-rolled minimum; prefer React Aria Autocomplete)

```tsx
'use client';
import { useEffect, useId, useRef, useState } from 'react';

export function SearchAutocomplete({ fetchSuggestions }: { fetchSuggestions: (q: string, s: AbortSignal) => Promise<string[]> }) {
  const [q, setQ] = useState(''); const [items, setItems] = useState<string[]>([]); const [active, setActive] = useState(-1);
  const listId = useId(); const ctrl = useRef<AbortController | null>(null);
  useEffect(() => {
    if (!q.trim()) { setItems([]); return; }
    const t = setTimeout(async () => {
      ctrl.current?.abort(); ctrl.current = new AbortController();
      try { setItems((await fetchSuggestions(q, ctrl.current.signal)).slice(0, 8)); setActive(-1); } catch { /* aborted */ }
    }, 200);
    return () => clearTimeout(t);
  }, [q, fetchSuggestions]);
  const open = items.length > 0;
  return (
    <form role="search" action="/search">
      <label htmlFor={`${listId}-in`} className="sr-only">Search</label>
      <input id={`${listId}-in`} name="q" type="search" enterKeyHint="search" autoComplete="off" value={q}
        role="combobox" aria-expanded={open} aria-controls={listId} aria-autocomplete="list"
        aria-activedescendant={active >= 0 ? `${listId}-${active}` : undefined}
        onChange={(e) => setQ(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'ArrowDown') { e.preventDefault(); const n = Math.min(active + 1, items.length - 1); setActive(n); if (items[n]) setQ(items[n]); }
          if (e.key === 'ArrowUp') { e.preventDefault(); const n = Math.max(active - 1, 0); setActive(n); if (items[n]) setQ(items[n]); }
          if (e.key === 'Escape') { setItems([]); }
        }} />
      <ul id={listId} role="listbox" hidden={!open}>
        {items.map((s, i) => (
          <li key={s} id={`${listId}-${i}`} role="option" aria-selected={i === active}
              onMouseDown={(e) => { e.preventDefault(); setQ(s); }}>{s}</li>
        ))}
      </ul>
      <p role="status" className="sr-only">{open ? `${items.length} suggestions` : ''}</p>
    </form>
  );
}
```

The arrow keys copy the active suggestion into the field (Baymard: 58% of sites do not), Escape closes, stale requests abort. Add product results as a second group and scope suggestions per section 3 of [Search and merchandising](search-and-merchandising.md).

### H5. Filters as a GET form with URL state and announced counts

```tsx
'use client';
import { useRouter, usePathname, useSearchParams } from 'next/navigation';
import { useTransition } from 'react';

export function FilterGroup({ name, label, values, total }: {
  name: string; label: string; values: { value: string; label: string; count: number }[]; total: number;
}) {
  const router = useRouter(); const pathname = usePathname(); const params = useSearchParams();
  const [pending, startTransition] = useTransition();
  const active = params.getAll(name);
  function toggle(v: string, checked: boolean) {
    const next = new URLSearchParams(params.toString());
    next.delete(name); (checked ? [...active, v] : active.filter((x) => x !== v)).forEach((x) => next.append(name, x));
    next.delete('page');
    startTransition(() => router.replace(`${pathname}?${next}`, { scroll: false }));
  }
  return (
    <fieldset aria-busy={pending}>
      <legend>{label}</legend>
      {values.filter((v) => v.count > 0 || active.includes(v.value)).map((v) => (
        <label key={v.value}>
          <input type="checkbox" name={name} value={v.value} checked={active.includes(v.value)}
                 onChange={(e) => toggle(v.value, e.target.checked)} />
          {v.label} <span aria-hidden="true">({v.count})</span><span className="sr-only">, {v.count} products</span>
        </label>
      ))}
      <p role="status" className="sr-only">{pending ? 'Updating results' : `${total} products`}</p>
    </fieldset>
  );
}
```

`startTransition` keeps the input responsive (INP). Render the grid on the server from `searchParams`; keep image dimensions fixed; applied chips above the grid with buttons named "Remove filter: Size M".

### H6. Free shipping progress (text first)

```tsx
export function ShippingProgress({ subtotal, threshold, currency, locale }: {
  subtotal: number; threshold: number | null; currency: string; locale: string;
}) {
  if (!threshold) return null;
  const fmt = new Intl.NumberFormat(locale, { style: 'currency', currency });
  const remaining = Math.max(threshold - subtotal, 0);
  const text = remaining > 0 ? `Add ${fmt.format(remaining)} for free delivery` : 'You get free delivery';
  return (
    <div className="ship-progress">
      <p aria-live="polite">{text}</p>
      <progress max={threshold} value={Math.min(subtotal, threshold)} aria-hidden="true" />
    </div>
  );
}
```

Threshold per market from the commerce backend or CMS (single source with shipping rates); subtotal after discounts in the market currency. Copy approved by `compliance` when it states shipping terms.

### H7. Toaster defaults (sonner)

```tsx
import { Toaster, toast } from 'sonner';
// In the root layout, once:
<Toaster position="bottom-center" duration={6000} closeButton visibleToasts={3} />
// Only for non-critical, out-of-view events with a persistent alternative:
toast('Saved to wishlist', { action: { label: 'View', onClick: () => router.push('/wishlist') } });
```

Do not use toasts for add to cart alone, errors or anything the user must act on. Position above the sticky add to cart and safe area on mobile.

### H8. Accessible gallery carousel (Embla)

```tsx
import useEmblaCarousel from 'embla-carousel-react';
import Accessibility from 'embla-carousel-accessibility';

export function Gallery({ images, title, dir }: { images: { src: string; alt: string; w: number; h: number }[]; title: string; dir: 'ltr' | 'rtl' }) {
  const [ref, api] = useEmblaCarousel({ loop: false, direction: dir },
    [Accessibility({ carouselAriaLabel: `${title} images` })]);
  return (
    <div>
      <div className="embla" ref={ref}><div className="embla__container">
        {images.map((img, i) => (
          <div className="embla__slide" key={img.src}>
            <img src={img.src} alt={img.alt} width={img.w} height={img.h}
                 loading={i === 0 ? 'eager' : 'lazy'} fetchPriority={i === 0 ? 'high' : 'auto'} />
          </div>
        ))}
      </div></div>
      <button type="button" onClick={() => api?.scrollPrev()} aria-label="Previous image">Prev</button>
      <button type="button" onClick={() => api?.scrollNext()} aria-label="Next image">Next</button>
    </div>
  );
}
```

Embla v9 is a release candidate as of 2026-10; pin the version and check plugin option names. Pass `dir` from the route locale (no `document` access during server rendering). A CSS scroll-snap track with buttons is often enough and ships zero JS.

### H9. Load more with URL and scroll restore

- Server renders page N from `?page=N` (or cursor); the client "Show 24 more" button fetches the next page, appends, and calls `history.replaceState` (or `router.replace` with `scroll: false`) to `?page=N+1`.
- Store the last clicked product index in `sessionStorage`; on Back, scroll it into view.
- Announce "24 more products loaded"; keep crawlable `?page=` links for bots (`seo`).
- Hydrogen reference: `PaginatedResourceSection.tsx` with `Pagination` (Load more and Load previous).

### H10. Locale and currency

- Route by `/{locale}` or `/{country}` segment; resolve market server-side (Medusa middleware region map; Saleor Paper `/{locale}/{channel}`; Hydrogen i18n via `storefront.i18n` with `@inContext`).
- Format with `Intl.NumberFormat`, `Intl.DateTimeFormat`, `Intl.PluralRules`; set `<html lang dir>` per locale.
- Never guess currency from language; country decides.

## 4. Performance rules for headless

| Rule | Why |
|------|-----|
| Server-render product data (RSC or loaders); hydrate only interactive islands | JS weight drives INP on mid-tier Android |
| LCP image: correct `sizes`, `priority` or `fetchPriority="high"`, no lazy loading | LCP 2.5 s at p75 mobile |
| Use `startTransition` for filter and sort updates | Keeps input responsive |
| Cache product and collection data with tags; revalidate on product webhooks (Next.js Commerce pattern) | Fresh prices without slow pages |
| Prefetch PDP links from PLP on viewport or hover (framework prefetch or speculation rules) | Ray-Ban doubled conversion with prerendering [Study, web.dev] |
| Third-party scripts behind consent and `afterInteractive` or later | Consent and speed |
| Budget per route (for example under 170 KB compressed JS on PDP) | Set your own budget from field data [Practitioner consensus] |

## 5. Security and data boundaries (handoff points)

- Storefront API public tokens only in the browser; private tokens server-side only; never commit tokens (the guard hook blocks common formats). Review with `site-engineer`.
- Checkout stays hosted (Shopify `checkoutUrl`) unless the platform is Medusa or Saleor with an audited payment integration.
- Analytics and pixels through the consent layer agreed with `measurement`.

## 6. Repo map for headless patterns

| Pattern | Look at |
|---------|---------|
| Optimistic cart | Hydrogen `app/components/CartMain.tsx`, Next.js Commerce `components/cart/cart-context.tsx` |
| Add to cart with status | Next.js Commerce `components/cart/add-to-cart.tsx` |
| Variant URL state | Next.js Commerce `components/product/variant-selector.tsx` |
| Predictive search | Hydrogen `SearchFormPredictive.tsx`, `SearchResultsPredictive.tsx` |
| Pagination | Hydrogen `PaginatedResourceSection.tsx` |
| Multi-region routing | Medusa `src/middleware.ts`, Saleor Paper routes |
| URL-driven checkout steps | Saleor Paper `src/app/(checkout)/checkout/` |
| Accessible primitives | Base UI `packages/react/src/*`, Radix `packages/react/*`, React Aria `packages/react-aria-components/src/*` |
