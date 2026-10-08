# E-E-A-T and Quality Policies

> Scope: what Google means by quality, how to build E-E-A-T signals that are real, every spam policy that can demote or remove a site, Google's stance on AI generated content, manual actions and reconsideration. Recovery procedures after updates are in [algorithm-updates-and-recovery.md](algorithm-updates-and-recovery.md).

## 1. How quality is assessed
- E-E-A-T (Experience, Expertise, Authoritativeness, Trust) is a framework from the Search Quality Rater Guidelines (QRG). It is not a single ranking factor. Google's ranking systems use many signals that aim to align with what raters would judge as high E-E-A-T. Trust is the most important member [Official, creating helpful content doc and QRG].
- Raters do not change rankings directly. Their ratings evaluate ranking changes before launch.
- YMYL (Your Money or Your Life) topics, those that can affect health, financial stability, safety or society, get the highest bar.
- QRG updates: January 2025 added definitions and examples for generative AI, scaled content abuse, site reputation abuse, expired domain abuse, filler content and exaggerated claims, and told raters to rate main content that is all or almost all AI generated, auto generated or copied with little effort, originality or added value as Lowest [Official, 2025-01]. A September 2025 update refined examples, including AI Overview related examples and YMYL scope [Official, 2025-09; details Unverified].
- Leaked Google Content Warehouse API documentation (May 2024) and the US v. Google trial testimony indicated site level quality signals and click based systems (Navboost) exist. The weight of any single attribute is unknown [Contested: practitioners infer heavily; Google says attributes in docs are not necessarily used].

Practical reading: Google evaluates sites as well as pages. A site with a large share of unhelpful pages can see sitewide suppression, which is why core update impacts often hit entire domains.

## 2. E-E-A-T implementation checklist
Site level:
- [ ] About page that names the company, founders or leadership, history, location, and why it is qualified.
- [ ] Contact information (address, phone, email, support channels) easy to find; customer service and return policies for ecommerce.
- [ ] Editorial policy, review process and corrections policy for content sites; affiliate disclosure where relevant.
- [ ] Organization structured data with `name`, `url`, `logo`, `sameAs` (official profiles, Wikipedia or Wikidata if they exist), `contactPoint`, address; on the homepage or about page.
- [ ] Off-site reputation: reviews on Google, Trustpilot, G2, Capterra, BBB or sector specific platforms; press coverage; awards that can be verified. Run a reputation search (`brand reviews`, `brand complaints`, `brand -site:brand.com`) like a rater would.
- [ ] Secure, functional site without deceptive ads or intrusive interstitials.

Author level:
- [ ] Bylines on articles linking to author pages.
- [ ] Author pages with real bio, credentials, experience, photo, links to profiles (LinkedIn, professional registries), list of articles; ProfilePage structured data.
- [ ] For YMYL: qualified authors or reviewers (licensed physician, CFP, attorney), "Reviewed by" with date and credential.
- [ ] Authors write within their expertise.

Content level:
- [ ] First-hand evidence: original photos, screenshots, test data, case outcomes.
- [ ] Sources cited with links and dates, primary sources preferred.
- [ ] Accurate, current facts; visible update log for living documents.
- [ ] Clear purpose; no misleading titles; no exaggerated claims (QRG January 2025 example category).
- [ ] Ads and affiliate links do not overwhelm main content.

## 3. Spam policies (what demotes or removes a site) [Official, Google spam policies]
| Policy | What it covers | Common real world trigger | Fix |
|--------|---------------|--------------------------|-----|
| Cloaking | Showing different content to users and search engines | Serving keyword text to Googlebot only; geo or UA based content swaps | Same content for all; if personalizing, Googlebot gets what a typical user gets |
| Doorway abuse | Many pages or sites targeting similar queries funneling users to one destination | City x service pages with swapped names; multiple near identical domains | Consolidate to real location pages with unique value; remove the rest |
| Expired domain abuse | Buying expired domains and using their reputation to host low value content | Buying a dropped news or nonprofit domain to publish affiliate content | Do not; content must fit the domain's prior purpose and serve users |
| Hacked content | Content placed without permission | Injected pages, links, redirects | Clean, patch, request review in Security issues |
| Hidden text and links | Text or links hidden to manipulate rankings | White text, off screen text, tiny links | Remove; accessible hidden content (tabs, accordions) for users is fine |
| Keyword stuffing | Unnatural repetition | City lists, repeated phrases | Rewrite naturally |
| Link spam | Links intended to manipulate rankings | Paid links without qualification, excessive exchanges, PBNs, automated links, widget links, keyword rich footer links on client sites | Remove or qualify with `rel="sponsored"` or `nofollow`; disavow for unnatural link manual actions |
| Machine-generated traffic | Automated queries to Google | Rank checking scrapers against Google's terms | Use APIs and licensed data |
| Malware and malicious practices | Harmful software, unexpected behavior | Compromised scripts, deceptive downloads | Clean, review |
| Misleading functionality | Fake tools or services | "Free" generators that bait into ads | Make the function real |
| Scaled content abuse | Many pages generated primarily to manipulate rankings with little value, by any method (AI, templates, scraping, stitching, low effort human writing) | Mass AI pages, programmatic pages with no unique data, translated copies with no review | Remove or noindex low value sets; rebuild with gates (see programmatic SEO) |
| Scraping | Republishing others' content without added value | Auto blogs, feeds republished | Original content only; clear syndication with canonical |
| Sneaky redirects | Redirecting users to unexpected destinations | Mobile only redirects to spam, conditional redirects | Remove |
| Site reputation abuse | Third party pages published on a host site to exploit its ranking signals | Coupon, casino, payday, CBD, "best" product sections operated by a third party on news, university or government sites | Noindex or remove the third party content; see section 4 |
| Thin affiliation | Affiliate pages copying merchant content without value | Product descriptions copied from the merchant | Add first-hand reviews, comparisons, unique data |
| User-generated spam | Spam in comments, forums, profiles | Profile spam on forums, comment links | Moderation, `rel="ugc"`, noindex empty profiles, anti spam tools |

Other behaviors that lead to demotion or removal: legal removals (high volume of valid copyright removal notices demotes a site), personal information removals (sites with exploitative removal practices), policy circumvention (actions intended to get around policies, such as creating new sites after a manual action), and scam and fraud [Official, spam policies].

## 4. Site reputation abuse in depth
Timeline: policy announced March 2024, enforcement (manual actions) began May 2024, clarified November 2024 to state that first-party involvement or oversight does not make third party content exempt when it exploits the host's ranking signals [Official, 2024-03, 2024-05, 2024-11].

| Likely violation | Usually fine |
|------------------|--------------|
| A news site hosting a coupon section run by a coupon company | A news site's own commerce journalism with its staff and standards, not designed to exploit signals |
| A university subfolder of casino or payday loan "reviews" from a partner | Wire service and syndicated news with clear provenance |
| A medical site hosting third party "best CBD" or supplement listicles for affiliate revenue | Native advertising clearly labeled and not designed to rank on host signals |
| Freelancer platforms within high authority domains publishing unrelated affiliate content | Forums and UGC that are moderated |

Remedies: move the content to its own domain (not a subdomain or subfolder of the host) without redirects that carry signals, or noindex it. Moving it inside the same site does not resolve the issue [Official, 2024-11 FAQ]. For publishers whose commercial sections were hit, hand the business trade-off to growth-orchestrator.

Regulatory note: the European Commission opened a proceeding in late 2025 examining whether Google's application of this policy demotes publishers unfairly [Unverified details; monitor].

## 5. Scaled content abuse in depth
Signals that make a content program look like scaled abuse:
- Large volumes of pages on topics unrelated to the site's expertise.
- Templates where only a keyword or location changes.
- Pages that summarize other pages without adding anything.
- Sudden spikes in publishing volume.
- Auto translated content without review.
- Little or no engagement and low indexing ratio.

Safe pattern: fewer, better pages with unique inputs; programmatic only behind data and value gates; human expert review; steady publishing cadence.

## 6. Google's guidance on AI generated content
- Appropriate use of AI or automation is not against guidelines. Using it to generate content primarily to manipulate rankings violates the spam policies [Official, 2023-02 guidance on AI-generated content].
- Google rewards quality content however it is produced; consider Who, How and Why disclosures.
- Search Central guidance on using generative AI content stresses accuracy, quality and relevance, metadata (title, description, structured data, alt text) that is accurate, and following ecommerce rules (Merchant Center requires metadata for AI generated images) [Official, generative AI content guidance].
- Quality raters rate low effort AI main content as Lowest (January 2025 QRG).
- Practical policy for this agent: AI drafts only with human expertise, fact checking and added value; never publish AI pages at a pace or scale that bypasses review.

## 7. Manual actions and reconsideration
Find them in Search Console > Security and manual actions > Manual actions. Types include: third-party spam, user-generated spam, spammy free host, structured data issue, unnatural links to your site, unnatural links from your site, thin content with little or no added value, cloaking or sneaky redirects, pure spam, hidden text or keyword stuffing, sneaky mobile redirects, News and Discover policy violations, site reputation abuse.

Process:
1. Read the action: scope (sitewide or partial) and examples.
2. Fix completely across the site, not just the examples.
3. Document: what you found, what you changed, how you prevent recurrence, with lists of URLs or links removed (and outreach logs for links you could not remove).
4. For unnatural links to your site: remove what you can; disavow the rest at domain level in the disavow tool.
5. Submit a reconsideration request. Reviews take days to weeks. Rejected requests explain gaps; fix and resubmit.
6. After revocation, rankings return only to what the site deserves without the spam; do not expect pre-spam levels.

Reconsideration request template:
```text
Summary: We received a manual action for <type> on <date>. We have <removed/fixed> <scope>.
What happened: <honest explanation, including who did it (former agency, vendor) and when>.
What we fixed:
- <action 1 with counts, e.g., removed 1,240 third-party coupon pages, now returning 410>
- <action 2>
Evidence: <link to a shared document or spreadsheet listing URLs, links, outreach attempts>
Prevention: <new policy, review process, vendor contract changes, monitoring>
We request reconsideration.
```

## 8. Algorithmic demotions vs manual actions
| | Manual action | Algorithmic (SpamBrain, core systems) |
|--|--------------|----------------------------------------|
| Notification | Search Console message | None |
| Recovery path | Fix, reconsideration request | Fix; systems re-evaluate over time (spam: can take months; core: often at later core updates) |
| Diagnosis | Explicit | Inferred from timing vs updates and patterns |

## 9. YMYL extra requirements
- Medical: authored or reviewed by qualified clinicians; cite guidelines and peer reviewed sources; no unsupported cure claims; date of last medical review.
- Financial: licensed authors or reviewers where relevant, disclosures, current rates and rules, no guaranteed return claims.
- Legal: jurisdiction specific, reviewed by attorneys, disclaimers.
- Safety and civic information: authoritative sources, rapid updates when facts change.
- Check PROJECT_BRIEF.md section 8 for claims the business must never make.

## 10. Quality audit procedure (sitewide)
1. Inventory all indexable URLs by template and content type with traffic, links and conversions.
2. Sample 30 to 50 URLs per content type; rate each on a 1 to 5 scale for: purpose, information gain, expertise, accuracy, presentation, ads and UX.
3. Compute the share of low rated (1 or 2) pages per type and their share of indexable URLs.
4. Content types with over 30% low rated pages are candidates for consolidation, rewrite or noindex [Practitioner consensus threshold; adjust to site].
5. Check off-site reputation and brand SERP.
6. Check spam policy exposure (third party sections, programmatic patterns, link profile).
7. Produce the quality plan: what to improve, merge, remove, and in what order, with expected timelines (months, not weeks).
