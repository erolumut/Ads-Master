# Speed checklist (20 items in four groups)

> Knowledge as of 2026-10. Framework and platform specifics change; check current docs before acting on any default or plan feature. Labels: [Official] from the vendor's docs, [Practitioner consensus] widely applied practice.

## Group 1: Images, fonts and third party scripts

| # | Check | How to find it | Typical fix | Watch out |
|---|-------|----------------|-------------|-----------|
| 1 | Images in a modern format (WebP or AVIF) and sized to their displayed size | Lighthouse "Properly size images" and "Serve images in modern formats"; compare intrinsic and rendered size in DevTools | Framework image component (`next/image`, `@unpic`, Astro `<Image>`), responsive `sizes`, pre-encoded AVIF or WebP | Do not upscale; keep a fallback where old browsers matter |
| 2 | Large images served through an optimizer at the right size | Network panel: image bytes on the LCP element | Serve storage images (Supabase Storage, S3) through the framework's image optimizer or the storage provider's transformations | Provider transformations can depend on the plan and are billed; check [Official] docs and cost first |
| 3 | Below the fold images and videos lazy loaded; the hero loaded first | Lighthouse "Defer offscreen images", "Largest Contentful Paint element" | `loading="lazy"` below the fold; the LCP image eager with high fetch priority (`priority` in `next/image`, `fetchpriority="high"`) | Never lazy load the LCP image |
| 4 | Fonts loaded the framework way, one or two families | Network panel font requests; layout shift on load | `next/font` or self hosted fonts with `font-display: swap` and preload of the main face; subset | Every weight and style is a file |
| 5 | Unused third party scripts removed; analytics and chat after load | The tag register (site-engineer performance reference, section 3); Lighthouse "Reduce the impact of third party code" | Remove unused tags; load the rest after load or on interaction (`next/script` `strategy="lazyOnload"`, a facade for chat widgets) | Consent rules still apply; measurement tags removed only with the measurement owner |

## Group 2: Frontend code

| # | Check | How to find it | Typical fix | Watch out |
|---|-------|----------------|-------------|-----------|
| 6 | No oversized packages in the first load | Bundle analyzer (`@next/bundle-analyzer`, `vite-bundle-visualizer`, `source-map-explorer`); the build's route size table | Import only what is used; swap a heavy package for a lighter one or a platform API | Modern bundlers tree shake ES module packages well; per function imports matter mainly for CommonJS packages such as classic `lodash` [Practitioner consensus]. Removing a dependency is a human decision |
| 7 | Heavy components not needed on the first screen load on demand | Analyzer shows charts, editors, maps, PDF or video players in the first load | Dynamic import (`next/dynamic`, `React.lazy`) when the component is needed | Keep a sized placeholder so nothing shifts |
| 8 | First screen data fetched on the server | The page shows an empty shell then fetches in the browser (waterfall in the network panel) | Server components or server side loading so the HTML arrives with content | Per user data stays out of shared caches |
| 9 | AI answers streamed | The user waits for the whole answer | Stream tokens to the client (the AI SDK's streaming, server sent events) | Show partial output accessibly; handle cancel |
| 10 | Skeletons or placeholders while data loads | Blank areas or layout jumps while loading | Skeletons that match the final size; suspense boundaries per section | A skeleton hides slowness, it does not remove it |

## Group 3: Database and APIs (high effort)

| # | Check | How to find it | Typical fix | Watch out |
|---|-------|----------------|-------------|-----------|
| 11 | Columns used to filter, join and sort are indexed, including those in row level security policies (such as `user_id`) | `EXPLAIN ANALYZE` on the slow queries; the database's index advisor or performance report; policies listed with their columns | Add the missing index | A migration under the project's database rules; indexes cost writes and space; never on a shared database without its owner |
| 12 | RLS policies call `auth.uid()` once per query, not once per row | Policies that compare a column to `auth.uid()` directly | Write it as `(select auth.uid())` so Postgres evaluates it once [Official, Supabase RLS performance guidance] | A policy change is a security change: test that each user still sees only their rows |
| 13 | No N+1 queries | Many identical queries per page in logs or the network panel; a loop with a query inside | One query with a join, `in (...)` or a view; batch loading | Check the result shape and permissions stay the same |
| 14 | Long lists paginated | Lists that load every row | Keyset (cursor) pagination for long or live lists, limit and offset for short ones | Counts on large tables are expensive; show "more" instead of totals |
| 15 | Shared responses cached; nothing per user cached in shared caches | Response headers, framework cache settings | Cache responses that are identical for everyone (CDN, framework data cache, `revalidate`) | A per user response in a shared cache leaks data: add a test with two users |
| 16 | Heavy work moved to background jobs | Requests that send email, process images or build reports before responding | A queue or background function; respond first, notify on completion | Retries must be idempotent |

## Group 4: Servers and network

| # | Check | How to find it | Typical fix | Watch out |
|---|-------|----------------|-------------|-----------|
| 17 | Server functions in the same region as the database | Host project settings versus the database region; server timing per request | Move the function region next to the database | Changing the region is a human decision; on Vercel the default region of new projects has been US East, verify the current default and the project setting [Official, check docs] |
| 18 | Pages whose content rarely changes are static or incrementally regenerated | The build output marks routes as dynamic that need not be | Static generation or ISR with a sensible revalidate time | Anything personal stays dynamic |
| 19 | No sequential API calls that could run together | Waterfall in the network panel or server timing | Run independent calls in parallel (`Promise.all`) or merge them into one endpoint | Error handling for partial failure |
| 20 | Main flows checked on a low end Android profile on slow 4G | DevTools: CPU throttling (4x or 6x) and the slow 4G profile; or a real cheap phone | Fix what the walk reveals: long tasks, heavy hydration, oversized assets | Lab throttling approximates; a real device and field data decide |
