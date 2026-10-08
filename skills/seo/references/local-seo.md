# Local SEO

> Scope: Google Business Profile (GBP), the local pack and Maps, reviews, local landing pages, service area businesses, multi location brands, citations, Bing Places and Apple Business Connect, local tracking and reporting. Local Services Ads and Maps ads belong to google-ads. Visibility of local businesses inside AI assistants belongs to ai-search-optimization.

## 1. How local ranking works
Google states that local results are based on relevance, distance and prominence [Official, GBP Help "Tips to improve your local ranking"]:
- Relevance: how well the profile matches the search (categories, name, services, products, description, reviews content, website content).
- Distance: how far the business (or its hidden address for service area businesses) is from the searcher or the location in the query.
- Prominence: how well known the business is (reviews count and rating, links, mentions, articles, overall web presence, organic ranking of the website).

Practitioner surveys (Whitespark Local Search Ranking Factors, latest edition; verify current ordering) consistently put these near the top for the local pack [Study, Whitespark; ordering Unverified for latest edition]:
1. Primary GBP category
2. Keywords in the GBP business name (effective but a guideline violation unless it is the real name)
3. Proximity of the address to the searcher
4. Physical address in the city searched
5. Removal of spam listings competing with you
6. High star rating and quantity of Google reviews with text
7. Additional categories
8. Dedicated, relevant landing page linked from GBP
9. Open at the time of search (Sterling Sky tests showed closed businesses lose visibility during closed hours) [Study, Sterling Sky]

Local organic (the blue links under the pack) follows classic SEO signals: page relevance, links, internal links, content quality.

## 2. GBP setup and optimization checklist
| Field | Rule | Why |
|-------|------|-----|
| Business name | Exactly the real world name on signage, website, legal documents. No keywords, cities or slogans | Keyword stuffing leads to suspensions and competitor edits |
| Primary category | The most specific category for the core revenue service (for example "Personal injury attorney", not "Lawyer") | Single biggest relevance lever |
| Additional categories | Up to 9 more for real services; review competitors in the top 3 with a category inspection tool | Expands relevance; too many unrelated categories dilutes |
| Address or service area | Storefront: real staffed address with signage. Service area business: hide address, set service areas (cities, regions, postcodes) | Virtual offices and unstaffed co-working are ineligible |
| Hours | Accurate regular, special (holidays) and more hours (delivery, pickup) | Open now affects visibility |
| Phone | Local number; tracking number as primary only if the real number is listed as an additional phone | Keeps NAP consistency and attribution |
| Website link | The relevant location page, not always the homepage, with UTM: `?utm_source=google&utm_medium=organic&utm_campaign=gbp&utm_content=<location>` | Attribution in GA4 |
| Appointment or booking links | Direct booking URLs | Conversion |
| Description | Up to 750 characters, what you do, for whom, where, differentiators; no URLs or promotions | Relevance and conversion |
| Services and products | Full list with descriptions and prices where relevant | Relevance; shows in profile |
| Attributes | All that apply (accessibility, payment, owned by identities, amenities) | Filters and trust |
| Photos and videos | Real photos of exterior, interior, team, work; add monthly; geotagging has no proven effect [Practitioner consensus] | Engagement and trust |
| Posts (updates, offers, events) | Weekly or bi weekly with offers, news, projects | Engagement; conversions; minor relevance |
| Opening date | Set | Trust |

Discontinued features to stop recommending: GBP chat and messaging (ended July 2024), GBP websites built in Business Profile (redirects ended 2024). The Q&A feature has been reported as being phased out and replaced by AI generated answers in some markets [Unverified; check the live profile].

Verification and edits:
- Video verification is the most common method; have the storefront, signage, tools and proof of management ready.
- Significant edits (name, address, category) can trigger re-verification or suspension. Batch edits, document reasons.
- Monitor "Google updates" on the profile (edits suggested by users or Google). Accept or reject promptly.

Suspensions:
| Type | Symptom | Action |
|------|---------|--------|
| Suspended (not visible) | Profile removed from Maps and Search | Fix the guideline issue, submit reinstatement with evidence (business license, utility bill, storefront photos with signage, registration documents) |
| Limited or profile under review | Edits blocked | Wait, then appeal with evidence |
Common causes: keyword stuffing in names, virtual office addresses, multiple profiles for the same business, prohibited industries or practices, sudden mass edits.

## 3. Reviews
Rules [Official, Google review policies; FTC rule on fake reviews effective 2024-10-21; UK DMCC Act consumer provisions effective 2025-04-06]:
- No incentives for reviews (discounts, gifts, contest entries).
- No review gating (asking only happy customers, or filtering by satisfaction before linking to Google).
- No employee, owner or family reviews; no buying reviews; no review swaps.
- Google removes suspected fake reviews and can show warnings or temporarily block new reviews on profiles caught with fake engagement [Official, 2024 to 2025; details Unverified per market].

Review program that works:
1. Ask every customer at the moment of satisfaction (job complete, delivery confirmed), via SMS or email with the direct review link (GBP > Ask for reviews).
2. Make it easy: one tap link, short ask, optional prompts ("mention the service you used and the area").
3. Volume and recency: a steady flow beats bursts. Track reviews per month and days since last review against the top 3 competitors.
4. Respond to every review within 2 business days. Thank, be specific, and for negative reviews acknowledge, take the issue offline, and never disclose personal or health information (regulated industries).
5. Flag policy violating reviews through the profile; escalate with the review management tool in GBP Help.
6. Use review content insights to improve services and on-page copy.

Response templates:
```text
Positive: "Thanks, <name>. Glad the <service> in <area> went smoothly and that <specific detail> helped. <Team member> will be happy to hear it."
Negative: "<Name>, we are sorry the <issue> fell short. That is not our standard. Please call <manager> at <number> or email <email> so we can make it right."
Regulated (health, legal, finance): "Thank you for your feedback. To protect privacy we cannot discuss details here. Please contact our office at <number>."
```

## 4. Local landing pages
One page per real location; city or area pages for service area businesses only where you actually serve and can show local proof.

Location page template:
- H1: `<Service or brand> in <City>`; unique intro written for that location.
- NAP block matching GBP exactly; embedded map; hours; parking or access notes.
- Services offered at this location with links to service pages.
- Local proof: team members at the location, photos, local projects or case studies, reviews from customers in that area, certifications or licenses for that jurisdiction.
- FAQs specific to the area (permits, regulations, travel times).
- LocalBusiness structured data (most specific subtype) with `@id`, `geo`, hours, `areaServed`.
- Internal links: from location hub (store locator with crawlable links), from service pages ("Areas we serve"), and between nearby locations.

Doorway risk: dozens of city pages that differ only by city name are doorway abuse. Gate each area page on real evidence (jobs completed there, reviews, staff, local content). Otherwise target the region on one strong page.

## 5. Service area businesses (SAB)
- Hide the address; ranking still radiates from the hidden address [Practitioner consensus].
- Service areas do not expand ranking radius much; they mainly describe coverage.
- Grow reach beyond the address radius with organic location or service area pages, reviews mentioning areas, links from local organizations in those areas, and Local Services Ads (google-ads).
- Opening a real, staffed second location is the only reliable way to rank in the pack in a distant city.

## 6. Multi location brands
- One GBP per eligible location; bulk verification for 10 or more locations.
- Consistent naming convention ("Brand City" only if that is the real signage).
- Store locator with crawlable location pages (no JavaScript only map lists).
- Centralized review generation and response with local owners.
- Use the Business Profile APIs or a listing management tool for bulk updates (hours on holidays).
- Practitioners and departments: individual professionals (doctors, lawyers, agents) can have their own profiles per guidelines; departments (service center, sales) only when they have distinct categories and hours.

## 7. Citations and other map platforms
Citations (NAP mentions) matter less than they did but consistency still prevents confusion and supports prominence [Practitioner consensus].

Priority list:
| Platform | Why |
|----------|-----|
| Bing Places | Bing, Copilot; import from GBP |
| Apple Business Connect | Apple Maps, Siri, Spotlight |
| Facebook page | Profile and reviews |
| Yelp (US and some markets) | Reviews, data used by other services |
| Industry directories (Avvo, Healthgrades, Houzz, Angi, TripAdvisor, OpenTable, etc.) | High trust, rank in organic for local queries |
| Data aggregators by country (US examples: Data Axle, Foursquare, Neustar Localeze) | Distribution |
| Local chambers, associations, sponsors | Links and mentions |

Audit: search `"business name" "phone"` and `"old address"` to find inconsistent listings after moves or rebrands; fix the top 30 by authority.

## 8. Tracking local visibility
- Geo grid rank tracking (Local Falcon, BrightLocal, Places Scout, Local Viking or similar): a grid of points around each location (for example 7 x 7 or 9 x 9 at 0.5 to 2 mile spacing depending on density) for 5 to 15 core terms, weekly or monthly. Metrics: average rank, share of points in top 3.
- GBP Performance: searches (queries that showed the profile), views, calls, website clicks, direction requests, bookings, messages where available. Business Profile Performance API for automation.
- GA4: sessions and conversions from `utm_campaign=gbp`.
- Call tracking: calls by source; tie to CRM outcomes (hand to measurement).

Monthly local report:
| Location | Grid avg rank (core term) | Top 3 share | Reviews (new, avg rating) | Calls | Directions | Website clicks | GBP sourced leads | Notes |

## 9. Fighting local spam
Competitors with keyword stuffed names, fake locations or fake reviews take pack positions.
1. Document with screenshots, street view, business registry lookups.
2. Suggest an edit on Maps for names and closed or fake locations.
3. Escalate with the Business Redressal Complaint Form for persistent cases.
4. Report fake reviews on the competitor profile.
5. Track results; removal of spam listings is a ranking factor for you.

## 10. Local SEO playbook by maturity
| Stage | Actions (in order) |
|-------|-------------------|
| New business or location | Create and verify GBP; choose categories; complete every field; photos; location page; Bing Places and Apple Business Connect; first 10 reviews from real customers in 30 days; core citations |
| Running | Weekly posts; review program; respond to all; geo grid baseline; service pages and FAQs; local links (sponsorships, associations, partners) |
| Plateau | Category analysis vs top 3; review velocity vs competitors; landing page upgrades with local proof; spam fighting; new services as categories and pages |
| Scaling (more locations) | Location page template; bulk management; centralized review ops; location level reporting; new location launch checklist |

## 11. Local SEO in AI search
AI Overviews and AI Mode show local results built from GBP data, reviews and websites; review content and complete attributes help those answers match conversational queries ("quiet cafe with outlets near me open late") [Practitioner consensus]. Hand prompt level tracking and assistant visibility (ChatGPT, Perplexity, Apple Intelligence, Copilot) to ai-search-optimization with the list of locations, categories and priority services.
