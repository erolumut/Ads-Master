# Other Channels: Quick Guides

Channels without a dedicated Ads Master agent yet. The growth-orchestrator handles them in the strategist role: decide if the channel fits, design the first test, define measurement, and borrow the closest agent for mechanics. When a channel becomes a recurring line item (about 10% of paid media or more than $5k per month), create a dedicated agent (section 13).

Verification note: platform minimums and feature names below were not re-checked live in the October 2026 sweep unless dated. Confirm in each platform's help center before launch.

## 0. Common test template (use for every channel here)
| Field | Default |
|-------|---------|
| Hypothesis | If we add <channel> with <audience and creative>, we will acquire new customers at an incremental CPA within 1.5x target, because <evidence> |
| Budget | Minimum viable budget (channel-selection.md formula) for 8 to 12 weeks |
| Structure | Few campaigns, broad enough for the algorithm to learn; 3 to 5 native concepts |
| Tracking | Pixel or tag + server-side conversions where available + UTMs + post purchase survey option "where did you hear about us" |
| Primary KPI | Incremental CPA or nCAC; for brand led channels, reach in target audience and branded search lift |
| Read | Weeks 3 to 4 leading indicators; weeks 9 to 12 verdict with geo split, holdout, or MER and new customer change |
| Stop rule | CPA over 3x target after spending 3x target CPA x 10 with no improving trend, or brand safety issue |
| Owner of mechanics | Borrowed agent listed per channel |

---

## 1. Reddit Ads
| Aspect | Guidance |
|--------|----------|
| When to use | Niche and enthusiast categories (tech, gaming, finance, fitness, hobbies, B2B software, parenting), high consideration purchases researched in communities; when Reddit threads rank in Google or are cited by AI assistants for your category |
| Avoid when | Mass market impulse products with no community angle; brand cannot tolerate public comments |
| Targeting | Communities (subreddits), interests, keywords and conversation context, custom audiences, lookalikes [Practitioner consensus; verify current options] |
| Formats | Promoted posts (image, video, carousel), conversation placements, product ads from a catalog [Unverified current naming] |
| Measurement | Reddit Pixel + Conversions API; UTMs; post purchase survey (Reddit is under credited by click attribution) |
| First test | $3k to $5k per month for 8 weeks; 2 to 3 ad groups (community bundle, keyword or conversation targeting, interest); native "post like" creative written in the community's voice; comments on with a moderation plan |
| Pitfalls | Polished brand ads get downvoted; ignoring comments; judging on last click only |
| Synergy | market-intel mines Reddit for VoC; ai-search-optimization tracks Reddit as an AI citation source |
| Borrow | meta-ads for paid social mechanics, measurement for CAPI |

## 2. Pinterest Ads
| Aspect | Guidance |
|--------|----------|
| When to use | Home, decor, fashion, beauty, food, weddings, DIY, travel planning; long planning cycles; strong visual catalog |
| Avoid when | B2B, urgent services, low visual appeal products |
| Formats | Standard and video pins, carousels, collections, shopping ads from catalog, Performance+ automated campaigns [Practitioner consensus; verify current names] |
| Measurement | Pinterest tag + Conversions API; longer consideration means longer click windows; compare with backend new customers |
| First test | $3k to $5k per month for 8 to 12 weeks; catalog shopping campaign plus one consideration campaign; seasonal content published 45 to 90 days before the peak (Pinners plan early) [Practitioner consensus] |
| Pitfalls | Judging in 2 weeks; using Meta creative unchanged (Pinterest favors vertical, text overlay, idea style pins) |
| Borrow | commerce-feeds (catalog), meta-ads (paid social mechanics) |

## 3. Snapchat Ads
| Aspect | Guidance |
|--------|----------|
| When to use | Audiences 13 to 34, Gulf markets (Saudi Arabia, UAE, Kuwait) where Snapchat reach is very high, France and UK youth, US Gen Z; app installs; fashion, beauty, gaming, food delivery |
| Formats | Single image or video snap ads, story ads, collection ads, dynamic product ads from catalog, AR lenses, sponsored messages in chat [Unverified current availability by market] |
| Measurement | Snap Pixel + Conversions API; app: MMP + SKAN or AdAttributionKit |
| First test | $3k per month for 6 to 8 weeks per market; full screen vertical native video (no letterboxed TV ads); Arabic creative in the Gulf |
| Platform minimum | Low daily minimum per ad set (about $5 per day historically) [Unverified current value] |
| Pitfalls | Older demographics; recycled horizontal video; ignoring the swipe up landing speed |
| Borrow | tiktok-ads for vertical video mechanics, creative-strategy |

## 4. X (Twitter) Ads
| Aspect | Guidance |
|--------|----------|
| When to use | Real time events, sports, news adjacent, tech and developer audiences, follower and conversation campaigns, markets where X remains a primary news platform |
| Avoid when | Brand safety requirements are strict; conversion tracking is critical and the team has no capacity to validate it |
| Measurement | X Pixel and Conversions API; validate against backend; assume weak last click attribution |
| First test | $1k to $3k per month for 4 to 6 weeks; keyword and follower lookalike targeting; brand safety and adjacency controls on |
| Pitfalls | Brand safety incidents; low conversion rates for cold traffic; volatile product changes [Practitioner consensus] |
| Borrow | meta-ads for paid social mechanics |

## 5. Amazon Ads and retail media networks
| Aspect | Guidance |
|--------|----------|
| When to use | You sell on Amazon or another marketplace (Walmart, Instacart, Target, Noon; in Turkey Trendyol, Hepsiburada, Amazon.com.tr); you are a brand selling through retailers |
| Formats | Sponsored Products, Sponsored Brands, Sponsored Display; Amazon DSP (including Prime Video ads); retailer onsite and offsite ads; Amazon Marketing Cloud for clean room analysis |
| KPIs | ACoS (ad spend / ad sales), TACoS (ad spend / total sales, the health metric), ROAS, new to brand share, organic rank movement |
| Market size | Commerce media reached $63.4 billion in US internet ad revenue in 2025, up 18% [Study, IAB/PwC 2026-04]; dentsu forecasts retail media growth of 12.3% globally in 2026 [Study, 2026-05] |
| First test | $1k to $3k per marketplace per month; Sponsored Products auto campaign (harvest search terms) + manual exact on top 20 terms + brand defense campaign; 4 to 8 weeks; then Sponsored Brands for category terms |
| Pitfalls | Judging on ACoS alone (ignores organic rank lift and new to brand); bidding on own brand without checking competitor presence; price parity issues with own site |
| Borrow | google-ads (Shopping logic), commerce-feeds (listing quality), market-intel (marketplace competitor pricing) |

## 6. Apple Ads (formerly Apple Search Ads)
| Aspect | Guidance |
|--------|----------|
| When to use | Any iOS app; high intent App Store search; brand and competitor defense |
| Placements | Search results (highest intent), Search tab, Today tab, product pages [Practitioner consensus; Apple renamed the product Apple Ads in 2025; verify current placements] |
| Measurement | AdServices attribution API, MMP integration, SKAdNetwork or AdAttributionKit |
| First test | $1k to $3k per month; 4 campaigns in search results: brand, category, competitor, discovery (broad match + search match to mine terms); CPT bids from suggested range; judge on cost per install and cost per trial or purchase over 4 weeks |
| Pitfalls | Only brand terms (cheap but low incrementality if organic rank is first); not separating discovery from exact campaigns |
| Borrow | google-ads (App campaign logic), measurement (MMP and SKAN) |

## 7. YouTube direct deals and reservations
| Aspect | Guidance |
|--------|----------|
| When to use | Enterprise tier brand campaigns needing guaranteed reach in premium inventory, launches, tentpole events |
| Options | Reservation buys at fixed CPM, YouTube Select content packages, masthead, creator partnerships (BrandConnect); auction Video Reach and efficient reach campaigns cover most needs below Enterprise |
| Minimums | Reservation and Select buys go through Google sales or DV360 and carry minimums [Unverified amounts] |
| Measurement | Brand lift, reach and frequency, geo lift on sales, share of search |
| First step | Run auction based Video Reach campaigns via google-ads first; move to reservation only when guaranteed placement or frequency control at scale is required |
| Borrow | google-ads |

## 8. CTV and programmatic
| Aspect | Guidance |
|--------|----------|
| When to use | Scale and Enterprise tiers; brand building with TV like impact; performance CTV in the US with household level targeting and QR or site visit measurement |
| Market | IAB projected US CTV ad spend growth of 15.6% in 2026 (September 2026 revision) [Study, 2026-09]; dentsu projects CTV growth of 11.5% globally in 2026 [Study, 2026-05] |
| Buying paths | YouTube on CTV via Google Ads (easiest), Amazon DSP and Prime Video, DSPs such as DV360 or The Trade Desk (usually via agency), streaming publishers direct, performance CTV platforms (US) |
| Measurement | Geo lift or matched market tests are the standard; platform view through attribution is not proof; MMM at Enterprise tier |
| First test | $10k to $50k over 6 to 8 weeks in a geo split (treatment regions vs control); 15 and 30 second creative with clear brand cues and a call to action; frequency cap 3 to 5 per week [Practitioner consensus] |
| Programmatic display cautions | Made for advertising sites and low quality supply waste budget: use inclusion lists, private marketplaces, supply path optimization. Third party cookies remain in Chrome (Google retired most Privacy Sandbox APIs in October 2025) but consent and browser limits still cut addressability [Study and news, 2025-10] |
| Borrow | google-ads (YouTube and DV360 logic), measurement (geo test design) |

## 9. Affiliate and partnerships
| Aspect | Guidance |
|--------|----------|
| When to use | Ecommerce and SaaS with clear commission economics; content publishers and review sites in the category; B2B referral and partner programs |
| Networks and tools | Impact.com, CJ, Awin, Rakuten Advertising, PartnerStack (SaaS) and local networks [verify per market] |
| Commission logic | Commission at or below contribution margin share you would pay a paid channel for the same new customer; lower rates for coupon and cashback partners |
| Incrementality | Coupon and cashback sites often claim sales that would happen anyway; content and comparison publishers are usually more incremental [Practitioner consensus] |
| First test | Recruit 20 to 50 content partners; 90 day evaluation; new customer commission higher than returning customer commission; brand bidding rules in the program terms |
| Pitfalls | Paying for brand search hijacking by affiliates; double paying with paid channels on the same order; no fraud monitoring |
| Borrow | measurement (dedup and attribution), market-intel (partner discovery) |

## 10. Influencer and creator marketing
| Aspect | Guidance |
|--------|----------|
| When to use | Demand creation in consumer categories; trust building in new categories; creative supply for paid social |
| Models | Gifting and seeding, paid posts, affiliate creators, paid usage of creator content in ads (Meta partnership ads, TikTok Spark Ads) |
| Market | Creator advertising spend reached $37 billion in 2025 with $44 billion projected for 2026 in the US (IAB) [Study, 2026-04] |
| Disclosure | Required in most markets: FTC endorsement guides (US), CMA and ASA (UK), Reklam Kurulu guide (Turkey), licensing in Saudi Arabia and UAE (geo module) |
| First test | 10 to 20 micro creators in one niche; product seeding plus paid posts; amplify the top 20% of content with partnership or Spark ads; measure with unique codes, landing pages and paid amplification CPA |
| Contracts | Usage rights (duration, channels, territories), whitelisting or Spark authorization, exclusivity, disclosure obligations, approval rights |
| Borrow | creative-strategy (briefs), meta-ads and tiktok-ads (amplification), market-intel (creator discovery) |

## 11. Email and SMS lifecycle (the LTV lever)
| Aspect | Guidance |
|--------|----------|
| Why | Retention and repeat purchase raise LTV, which raises the CAC the business can afford on every paid channel |
| Core flows | Welcome, browse abandon, cart abandon, checkout abandon, post purchase and review request, replenishment, cross sell, win back, VIP, sunset |
| Deliverability rules | Gmail and Yahoo bulk sender requirements since February 2024: SPF, DKIM, DMARC, one click unsubscribe, spam complaint rate under 0.3% [Official, 2024]; Microsoft announced similar requirements for high volume senders to Outlook consumer domains in 2025 [Unverified effective details] |
| SMS and messaging consent | US: TCPA consent and carrier 10DLC registration; Turkey: İYS registration; EU and UK: consent under ePrivacy and PECR; WhatsApp Business marketing messages are paid per message and require opt in [Practitioner consensus; verify current pricing model] |
| KPIs | Revenue per recipient, flow revenue share, list growth, unsubscribe and complaint rates, incremental revenue vs holdout |
| First test | Build 5 core flows in 2 weeks; 10% holdout for 60 days to measure incremental revenue; list growth via onsite capture with a clear offer |
| Paid media link | Upload consented lists for exclusions and lookalikes (measurement and channel agents); suppress existing customers from acquisition campaigns where nCAC is the KPI |
| Borrow | cro (capture forms), measurement (consent and events) |

## 12. Other surfaces (watch list)
| Channel | Note |
|---------|------|
| Audio and podcasts | Host read ads for trust; measure with codes and surveys; brand bucket |
| Quora | B2B and tech research queries; small scale tests |
| Telegram | Ads and channels relevant in some markets [verify per market] |
| Yandex, Naver, Seznam, Yahoo! JAPAN | Local search engines where they hold meaningful share |
| Perplexity, Copilot and other AI assistant ads | Owned by chatgpt-ads as AI assistant ad strategy |

## 13. Creating a dedicated agent for one of these channels
Trigger: recurring budget above about 10% of paid media or above $5k per month, or a channel that needs weekly expert operation.
1. Follow `docs/AUTHORING_SPEC.md` section 9 and routing-and-workflows.md section 5.
2. Start from the closest package: reddit, pinterest, snapchat, x from meta-ads; amazon or retail media from google-ads plus commerce-feeds; ctv from google-ads (YouTube) plus measurement; lifecycle (email and SMS) as a new package using cro and measurement modules.
3. Research the channel with the research dossier format (40+ dated sources) before writing the playbook.
4. Required files: `agents/<slug>.md`, `skills/<slug>/SKILL.md`, references including `audit-checklist.md` and `sources.md`, `research/<slug>.md`.
5. Register the slug in the routing table (SKILL.md), AGENT_REGISTRY.md, HEARTBEAT.md template and memory template.
6. Validate with `python3 scripts/validate.py`.
