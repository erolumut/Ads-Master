# Link Building and Digital PR

> Scope: how links and brand mentions matter in 2026, tactics that earn editorial links, outreach process and templates, what to avoid, link risk assessment, disavow policy, and measurement. Brand mentions inside AI answers are a shared outcome with ai-search-optimization.

## 1. Where links stand in 2026
- Link analysis (including PageRank) remains one of Google's documented ranking systems [Official, ranking systems guide].
- Google representatives have said links matter less than in the past and that sites need far fewer links to rank than many assume [Practitioner reports of Google statements, 2023 to 2024; Contested in weight].
- SpamBrain neutralizes manipulative links (link spam update December 2022); purchased links often simply stop counting, so spend on them is wasted even when no penalty follows [Official, 2022-12].
- Brand mentions, reviews and third party coverage also drive AI answer citations and recommendations, which raises the value of digital PR beyond PageRank [Practitioner consensus; see ai-search-optimization].

Working model: links are a multiplier on good pages, not a substitute. Earn them from relevant, real sites people read.

## 2. What a valuable link looks like
| Attribute | Strong | Weak |
|-----------|--------|------|
| Relevance | Same topic or audience | Unrelated niche |
| Real audience | The linking site has organic traffic and readers | No traffic, exists to sell links |
| Editorial | Placed by an editor because it helps readers | Paid insertion, author bio farm |
| Placement | In body content, contextual | Footer, sidebar, sitewide blogroll |
| Target | Money page or a hub that links to money pages | Random blog post with no internal links |
| Indexation | Linking page indexed | Not indexed |
| Uniqueness | First link from that domain | Tenth link from same domain |

Domain Rating or Authority Score are vendor metrics, useful for triage only. Always look at the linking site's traffic trend, topic and outbound link patterns.

## 3. Tactics that work (ranked by typical return for effort)
| Tactic | How | Best for | Effort |
|--------|-----|----------|--------|
| Partner and customer links | Integration partners, suppliers, distributors, manufacturers (where to buy pages), clients' vendor pages, case study swaps | SaaS, B2B, ecommerce brands | Low |
| Unlinked brand mentions | Find mentions without links (Ahrefs or Semrush mention tracking, Google Alerts) and ask for a link | Brands with press | Low |
| Link reclamation | Fix 404s with external links (301 to best match); ask sites linking to old URLs to update | Sites with history, after migrations | Low |
| Digital PR with original data | Surveys, proprietary data analyses, indexes, annual reports with methodology, pitched to journalists | All with data access | Medium to high |
| Expert commentary | Respond to journalist requests (platforms such as Qwoted, Featured, Source of Sources, and journalist requests on X and LinkedIn; the original HARO service shut down in 2024 and platforms change often [Unverified current list]); build an expert bench | Experts in B2B, finance, health, legal | Medium |
| Free tools and calculators | Useful tool that others reference | SaaS, finance, ecommerce niches | High upfront, compounding |
| Resource and directory inclusion | Genuine industry directories, association member lists, curated resource pages | Local, B2B | Low |
| Local links | Sponsorships, events, local news, chambers, schools, charities | Local businesses | Low to medium |
| Podcasts and webinars | Guest appearances with show notes links | B2B, creators | Medium |
| Broken link building | Find dead resources in your niche, offer your equivalent | Content rich sites | Medium |
| Guest contributions on real publications | Expert articles on sites with editorial standards, links only where editorially relevant | B2B thought leadership | Medium |
| Community participation | Helpful answers in forums and communities where you are an expert (links nofollow, value is visibility and AI mentions) | All | Medium |

## 4. Digital PR campaign process
1. Angle: a finding journalists cannot get elsewhere (your data, survey of at least 1,000 respondents via a reputable panel, analysis of public datasets, expert predictions). Tie to news cycles and seasonal stories.
2. Asset: landing page on your site with methodology, key findings, charts, downloadable data, quotes, embed codes for charts.
3. Media list: 50 to 300 journalists who cover the beat, built from recent bylines (not purchased lists).
4. Pitch: short, data led, specific to the journalist's beat; offer an expert for comment; exclusives for top tier outlets.
5. Follow up once after 3 to 5 days.
6. Track: coverage, links (followed, nofollowed, unlinked), referring domains, brand mentions, traffic, branded search lift.
7. Reclaim: ask unlinked coverage for attribution links to the study page.
8. Internal links: from the study page to relevant money pages.

Pitch template:
```text
Subject: New data: <headline finding with number> (<geo>, <year>)

Hi <first name>,

You covered <their recent story> last week. Our analysis of <dataset/sample> found <finding 1 with number>, and <finding 2>.

Three takeaways for your readers:
- <stat and why it matters>
- <regional or demographic split>
- <surprising contrast>

Full methodology and charts: <URL>. <Expert name, title> is available for comment today.

<Your name>, <title>, <company>, <phone>
```

Unlinked mention request:
```text
Subject: Thanks for mentioning <brand> in <article title>

Hi <name>, thanks for including <brand> in <article>. Would you consider linking our name to <specific URL> so readers can find <the resource or product referenced>? Happy to provide anything else useful for the piece.
```

## 5. What to avoid (and why)
| Practice | Risk |
|----------|------|
| Buying links without `rel="sponsored"` | Link spam policy; links neutralized; manual action for unnatural links |
| PBNs (private blog networks) | Detection and neutralization; manual actions; wasted spend |
| Link insertions into old articles on news and magazine sites (paid "niche edits") | Paid links; often on sites engaged in site reputation abuse |
| Guest post farms (sites that publish anything for a fee) | Low value; patterns detectable |
| Large scale link exchanges and three way swaps | Link scheme |
| Expired domain redirects for link equity | Expired domain abuse and link scheme |
| Hosting your content on a high authority third party domain to borrow its ranking (parasite SEO) | Site reputation abuse |
| Sitewide footer links on client sites with keyword anchors ("Web design by best SEO agency London") | Unnatural links; use brand anchors and nofollow |
| Automated links (comments, profiles, forums) | Spam; worthless |
| Press release distribution for links | Links are nofollow or ignored |
| Widgets or badges with hidden or keyword links | Link scheme |

When a client already bought links: stop, inventory, remove or nofollow where possible, and evaluate manual action risk. Do not file a disavow by default.

## 6. Disavow policy
- Google says most sites do not need to use the disavow tool; its systems ignore most spammy links [Official].
- Use disavow when: (a) you have an "Unnatural links to your site" manual action, or (b) you know of large scale paid or scheme links pointing to you that you cannot remove and you fear a manual action.
- Disavow at domain level (`domain:example.net`) for clear spam sources. Keep the file versioned in `ads-master/outputs/seo/` with reasons. Never upload without human approval.
- Negative SEO (competitors pointing spam at you) rarely has effect; monitor but do not panic [Practitioner consensus].

## 7. Link risk assessment for a profile
1. Export referring domains (Ahrefs, Semrush, Majestic, plus Search Console Links report and Bing Webmaster backlinks).
2. Flag patterns: exact match commercial anchors at high share (over 10% to 20% of anchors is a warning sign [Practitioner consensus]), sudden spikes, links from irrelevant foreign language sites, sites with "write for us" pages and many casino or crypto outbound links, sitewide links, PBN footprints (same IP, theme, ownership).
3. Classify: natural, low quality but harmless, manipulative (bought or schemed).
4. Recommend: continue, remove, nofollow request, disavow only per policy.

## 8. Link targets and internal flow
- Point links at pages that should rank, or at linkable assets that link internally to money pages.
- For ecommerce, PR assets and guides link to categories; for SaaS, tools and studies link to solution and comparison pages.
- Track which pages receive new referring domains each month; pages that receive none should get them via internal links from pages that do.

## 9. Budgets and cadence by tier
| Tier | Approach | Target |
|------|----------|--------|
| Starter | Partner, customer, local and directory links; unlinked mentions; one simple data asset per half year | 3 to 10 relevant referring domains per quarter |
| Growth | Quarterly digital PR campaign; expert commentary program; tool or template | 10 to 40 per quarter |
| Scale | Monthly campaigns, in-house or agency PR, expert bench | 40 to 150 per quarter |
| Enterprise | Always on newsroom style PR across markets, research program | Market specific targets |
These are planning heuristics, not benchmarks; set targets from the gap to the top 3 competitors for priority pages.

## 10. Measurement
| KPI | Source |
|-----|--------|
| New referring domains (relevant, editorial) per month | Ahrefs or Semrush; Search Console Links report |
| Links to money pages or their hubs | Same |
| Coverage and brand mentions (linked and unlinked) | Media monitoring, mention tools |
| Branded search trend | Search Console branded filter, Google Trends |
| Rank and click changes for target pages after link acquisition | Search Console |
| AI mentions and citations | Bing AI Performance, ai-search-optimization reports |
