#!/usr/bin/env python3
"""claims_check.py: screen customer facing copy against the project claims registry.

Dependency free: Python 3.8 or later, standard library only.

What it does
  1. Reads ads-master/brand/CLAIMS.md (tables under the headings Approved,
     Needs review and Blocked).
  2. Optionally reads ads-master/brand/PRODUCT_FACTS.md and flags facts that are
     not verified, have no evidence, are expired or expire within 30 days.
  3. Scans text, files or stdin line by line for:
       registry Blocked patterns        -> BLOCK
       registry Needs review patterns   -> REVIEW
       built-in risk patterns           -> BLOCK, REVIEW or INFO (disable with --no-builtin)
       registry Approved claims         -> APPROVED (built-in hits inside the approved
                                           wording are suppressed; registry Blocked hits
                                           inside it are reported as a registry conflict)
  4. Prints findings as text, JSON or a Markdown table.

Exit codes: 0 nothing to review, 1 review items, 2 blocked items, 3 usage or input error.
Use --fail-on to change which severity makes the exit code non zero.

Registry pattern syntax (first column of each table)
  plain wording     matched case insensitively as whole words, any whitespace between words
  /regex/           a Python regular expression, case insensitive
  a ; b ; c         alternatives for plain wording (not split inside /regex/)
  Backticks around a pattern are ignored.
Markets column: codes such as EU, UK, US, TR, NL, DE, AE, SA, or "all" or empty for every
market. EU rules also apply to EU member state codes (NL, DE, FR and so on).

This is a screening aid, not a legal opinion. A clean result means "no known pattern
matched", never "approved". Every customer facing asset still goes through the review
in the compliance skill, and anything uncertain is NEEDS HUMAN OR LEGAL REVIEW.

Examples
  python3 claims_check.py --claims ads-master/brand/CLAIMS.md drafts/ad_copy.md
  python3 claims_check.py --claims ads-master/brand/CLAIMS.md --market TR --text "Mucizevi sonuç, %40 indirim"
  cat landing.html | python3 claims_check.py --claims ads-master/brand/CLAIMS.md --strip-html -
  python3 claims_check.py --facts ads-master/brand/PRODUCT_FACTS.md --facts-only
"""

import argparse
import datetime as _dt
import html
import json
import os
import re
import sys

SEVERITY_ORDER = {"INFO": 0, "APPROVED": 0, "REVIEW": 1, "BLOCK": 2}
EU_MEMBERS = {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR", "EL", "HU",
    "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE",
}
MARKET_ALIASES = {"GB": "UK", "USA": "US", "TURKEY": "TR", "TURKIYE": "TR", "UAE": "AE", "KSA": "SA"}

# ---------------------------------------------------------------------------
# Built-in rule pack. Each rule: id, regex (applied to folded lower case text),
# default severity, optional per market severity, citation and fix.
# Citations point to the reference modules of the compliance skill, where the
# full rule, thresholds and sources live. Keep this list conservative: it is a
# net for the reviewer, not a decision engine.
# ---------------------------------------------------------------------------
BUILTIN_RULES = [
    {
        "id": "HLTH-DISEASE",
        "pattern": r"\b(cure[sd]?|curing|heals?|healing|treats?|treating|prevents?|reverses?|fights?)\b[^.\n]{0,40}\b(disease|cancer|diabetes|covid|infection|depression|anxiety|arthritis|alzheimer\w*|illness|hypertension|eczema|psoriasis|acne)\b",
        "severity": "BLOCK",
        "rule": "Disease claim for a non medicine. EU FIC 1169/2011 Art 7(3), UCPD Annex I no.17, US FD&C Act drug claim, TR health claim regulation 2023, UK CAP 12 and 15. See supplements-cosmetics-and-health.md",
        "fix": "Remove the disease reference. Use only an authorised or substantiated claim from CLAIMS.md Approved.",
    },
    {
        "id": "HLTH-DISEASE-TR",
        "pattern": r"(tedavi eder|tedavi edici|iyileştirir|şifa|kansere|hastal\w* (önler|iyi gelir)|depresyona)",
        "severity": "BLOCK",
        "rule": "Hastalık tedavi veya önleme iddiası (TR Sağlık Beyanı Yönetmeliği 2023, Reklam Kurulu takviye edici gıda kararları). See supplements-cosmetics-and-health.md",
        "fix": "Hastalık iddiasını kaldırın; yalnızca TİTCK kılavuzundaki izinli beyanı tam metniyle kullanın.",
    },
    {
        "id": "HLTH-WEIGHT-RATE",
        "pattern": r"\b(lose|drop|shed|burn)\s+(up to\s+)?\d+([.,]\d+)?\s*(kg|kgs|kilos?|lbs?|pounds?|stone|sizes?)\b|\b\d+\s*(kg|lbs?|pounds?)\s+in\s+\d+\s*(days?|weeks?|months?)\b|\d+\s*kilo\s*ver\w*",
        "severity": "BLOCK",
        "rule": "Rate or amount of weight loss. EU 1924/2006 Art 12(b), UK CAP 13, US FTC Gut Check red flags, TR Reklam Kurulu practice. See supplements-cosmetics-and-health.md",
        "fix": "Remove the amount or timeframe. Use an authorised weight claim with its conditions, or a non quantified benefit.",
    },
    {
        "id": "HLTH-SAFETY-ABSOLUTE",
        "pattern": r"\b(no side[- ]effects?|100\s?% safe|completely safe|totally safe|risk[- ]free treatment|harmless)\b|yan etkisi (yok|yoktur)|zararsız",
        "severity": "BLOCK",
        "rule": "Absolute safety claim. Directive 2001/83/EC Art 90 (medicines), UCPD Art 6, UK CAP 12, TR Reklam Kurulu. See supplements-cosmetics-and-health.md",
        "fix": "Delete. Safety statements need regulatory basis and qualification.",
    },
    {
        "id": "HLTH-FDA-APPROVED",
        "pattern": r"\bfda[- ](approved|cleared|certified|registered)\b",
        "severity": "BLOCK",
        "rule": "FDA does not approve supplements or cosmetics; FDA 2026 warning letters cite 'FDA-approved' sourcing language. See supplements-cosmetics-and-health.md",
        "fix": "Use only if PRODUCT_FACTS holds the approval or clearance number and the claim is in CLAIMS.md Approved.",
    },
    {
        "id": "HLTH-PROOF",
        "pattern": r"\b(clinically|scientifically|medically)\s+(proven|tested|shown|validated)\b|\bstudies (show|prove)\b|\bdermatologically tested\b|\blab[- ]tested\b|klinik olarak kanıtlanmış|bilimsel olarak kanıtlanmış",
        "severity": "REVIEW",
        "rule": "Proof claim needs study evidence matched to the exact product and claim. EU 655/2013 (cosmetics), FTC Health Products Compliance Guidance 2022, CAP 3.7. See product-facts-and-evidence.md",
        "fix": "Link the study in PRODUCT_FACTS and state what was tested; otherwise remove.",
    },
    {
        "id": "HLTH-PROFESSIONAL",
        "pattern": r"\b(doctors?|dermatologists?|pharmacists?|dentists?|nutritionists?|experts?)[- ](recommended|approved|endorsed)\b|\brecommended by (doctors|dermatologists|experts|pharmacists)\b|(doktor|hekim|eczacı|diyetisyen) (önerisi|onaylı|tavsiyesi)",
        "severity": "REVIEW",
        "severity_by_market": {"TR": "BLOCK"},
        "rule": "Health professional endorsement. Foods: EU 1924/2006 Art 12(c). TR: supplement ads may not show or imply doctors or pharmacists. See supplements-cosmetics-and-health.md",
        "fix": "Remove for foods and supplements; for other products keep only with a documented, representative survey or named endorsement with consent.",
    },
    {
        "id": "HLTH-GENERAL-BENEFIT",
        "pattern": r"\b(boosts?|supports?|strengthens?)\s+(your\s+)?(immune|immunity|metabolism)\b|\bimmun(e|ity)[- ]boost\w*|\bdetox\w*|\bcleanse\b|\bsuperfood\b|\bfat[- ]burn\w*|\banti[- ]?aging\b|bağışıklı\w* (güçlendir|destekl|artır)\w*",
        "severity": "REVIEW",
        "rule": "General health benefit or unsupported wellness term. EU 1924/2006 Art 10(3) needs an accompanying authorised claim; Meta and OpenAI wellness policies. See food-and-nutrition-claims.md",
        "fix": "Pair with an exact authorised claim from the EU register (or local list) that the product qualifies for, or remove.",
    },
    {
        "id": "FOOD-NUTRITION-CLAIM",
        "pattern": r"\b(source of protein|high[- ]protein|protein[- ]rich|rich in protein|packed with protein|low[- ]fat|fat[- ]free|low[- ]sugars?|sugar[- ]free|zero sugar|no added sugars?|unsweetened|low[- ](salt|sodium)|salt[- ]free|high[- ]fib(re|er)|source of fib(re|er)|reduced (fat|sugar|salt)|low[- ]calorie|energy[- ]free|source of omega[- ]?3|high in omega[- ]?3)\b|(şeker ilavesiz|ilave şeker içermez|protein kaynağı|yüksek protein|düşük yağ|yağsız|şekersiz|lif kaynağı)",
        "severity": "REVIEW",
        "rule": "Nutrition claim. Only the Annex claims of EU 1924/2006 (UK and TR equivalents) are allowed and each has a threshold, for example source of protein needs 12 percent of energy from protein, high protein 20 percent. See food-and-nutrition-claims.md",
        "fix": "Check the nutrition table in PRODUCT_FACTS against the threshold table; keep the exact Annex wording.",
    },
    {
        "id": "FOOD-PERCENT-FAT-FREE",
        "pattern": r"\b\d+([.,]\d+)?\s?%\s?fat[- ]free\b",
        "severity": "BLOCK",
        "severity_by_market": {"US": "REVIEW"},
        "rule": "EU 1924/2006 Annex: claims expressed as 'X % fat-free' are prohibited (UK and TR follow). US 21 CFR 101.62 allows it only for low fat foods. See food-and-nutrition-claims.md",
        "fix": "Use 'low fat' or 'fat-free' if the thresholds are met.",
    },
    {
        "id": "FOOD-PROBIOTIC",
        "pattern": r"\bprobiotics?\b|\bprobiyotik\b",
        "severity": "REVIEW",
        "rule": "EU Commission treats 'probiotic' as a health claim; no authorised probiotic claim exists; a few member states tolerate it. See food-and-nutrition-claims.md",
        "fix": "In the EU use the strain name and quantity only, unless counsel approves the term for the target country.",
    },
    {
        "id": "FOOD-SPECIAL-DIET",
        "pattern": r"\b(vegan|vegetarian|plant[- ]based|gluten[- ]free|lactose[- ]free|dairy[- ]free|organic|keto|halal|kosher)\b|(glutensiz|laktozsuz|organik|vejetaryen|helal)",
        "severity": "REVIEW",
        "rule": "Status claim that needs a certificate or verified recipe fact (gluten-free max 20 mg/kg EU 828/2014 and US 20 ppm; organic needs certification EU 2018/848, USDA NOP, TR 5262; vegan has no EU legal definition). See food-and-nutrition-claims.md",
        "fix": "Confirm a verified PRODUCT_FACTS row with certificate number and expiry.",
    },
    {
        "id": "COSM-FREE-FROM",
        "pattern": r"\b(paraben[- ]free|free from parabens|chemical[- ]free|non[- ]toxic|toxin[- ]free|hypoallergenic|clean beauty|preservative[- ]free)\b|(paraben içermez|kimyasal içermez)",
        "severity": "REVIEW",
        "rule": "Cosmetic free-from or hypoallergenic claim. EU 655/2013 common criteria and the Commission technical document on cosmetic claims (Annex III and IV). See supplements-cosmetics-and-health.md",
        "fix": "Drop denigrating free-from claims; keep hypoallergenic only with allergenic potential evidence.",
    },
    {
        "id": "ENV-GENERIC",
        "pattern": r"\b(eco[- ]friendly|environmentally friendly|environment friendly|planet[- ]friendly|earth[- ]friendly|climate[- ]friendly|green product|good for the planet|nature'?s friend|gentle on the (planet|environment)|ecological)\b|(çevre dostu|doğa dostu|iklim dostu|umweltfreundlich|milieuvriendelijk)",
        "severity": "REVIEW",
        "severity_by_market": {"EU": "BLOCK"},
        "rule": "Generic environmental claim. EU from 2026-09-27: banned unless recognised top environmental performance is shown (UCPD Annex I no.4a via Directive 2024/825). TR from 2026-08-01: not without explanation and documents. UK CMA Green Claims Code. See environmental-claims.md",
        "fix": "Replace with a specific, substantiated claim on one attribute (for example 'packaging made from 80% recycled plastic') backed by PRODUCT_FACTS.",
    },
    {
        "id": "ENV-OFFSET-NEUTRAL",
        "pattern": r"\b(carbon[- ]neutral|climate[- ]neutral|co2[- ]neutral|net[- ]zero|carbon[- ]negative|climate[- ]positive|carbon[- ]free|zero[- ]emissions?)\b|(klimaneutral|klimaatneutraal|co2-neutraal|karbon nötr|sıfır emisyon)",
        "severity": "REVIEW",
        "severity_by_market": {"EU": "BLOCK"},
        "rule": "Neutrality or net zero claim. EU from 2026-09-27: banned when based on offsetting (UCPD Annex I no.4c). DE BGH I ZR 98/23 (2024): explain in the ad itself. TR 2026: requires certification documents. See environmental-claims.md",
        "fix": "Remove product neutrality claims based on offsets; describe actual reductions with scope, baseline and verification.",
    },
    {
        "id": "ENV-SPECIFIC",
        "pattern": r"\b(biodegradable|compostable|recyclable|recycled|plastic[- ]free|sustainable|sustainably sourced|renewable)\b|(geri dönüştürülebilir|sürdürülebilir|nachhaltig|duurzaam|biologisch abbaubar)",
        "severity": "REVIEW",
        "rule": "Specific environmental claim needs scope (whole product or part), standard (for example EN 13432) and evidence. See environmental-claims.md",
        "fix": "Name the component, the percentage and the standard; link the evidence row in PRODUCT_FACTS.",
    },
    {
        "id": "PRICE-REDUCTION",
        "pattern": r"\b\d+([.,]\d+)?\s?%\s?(off|discount|korting|rabatt)\b|\bsave\s+(up to\s+)?\d+|\b(was|previously|regular price|rrp|uvp|statt)\s*[:]?\s*[$€£₺]?\s?\d|\bsale\b|%\s?\d+\s?indirim|\d+\s?%\s?indirim|\bindirimli\b|\bnow only\b",
        "severity": "REVIEW",
        "rule": "Price reduction announcement. EU PID Art 6a: prior price is the lowest price in the 30 days before the reduction (CJEU C-330/23). TR from 2026-08-01: lowest price in the last 10 days, same channel. UK CMA pricing guidance. US 16 CFR 233. See pricing-promotions-and-consumer-law.md",
        "fix": "Attach the price history export proving the reference price; compute the percentage from it.",
    },
    {
        "id": "PRICE-FREE",
        "pattern": r"(?<![-\w])(?<!sugar )(?<!gluten )(?<!fat )(?<!salt )(?<!dairy )(?<!lactose )(?<!cruelty )(?<!paraben )(?<!chemical )(?<!toxin )(?<!plastic )(?<!carbon )(?<!hands )(?<!caffeine )(?<!alcohol )(?<!preservative )\b(free|gratis|kostenlos|gratuit|bedava|ücretsiz)\b(?![- ](from|of)\b)",
        "severity": "REVIEW",
        "rule": "'Free' claim. UCPD Annex I no.20, UK CAP 3.21 to 3.26, US 16 CFR 251, Google dishonest pricing policy. Free shipping and free trials need conditions shown up front. See pricing-promotions-and-consumer-law.md",
        "fix": "Confirm the customer pays nothing beyond the unavoidable delivery cost; state trial length and auto charge next to the claim.",
    },
    {
        "id": "PRICE-URGENCY",
        "pattern": r"\b(only today|today only|ends (tonight|today|soon|at midnight)|last chance|limited time|only \d+ left|while stocks last|hurry|selling fast|almost gone|final hours)\b|(sadece bugün|bugüne özel|son \d+ (adet|ürün)|kaçırma|stoklarla sınırlı|son gün|nur heute|alleen vandaag)",
        "severity": "REVIEW",
        "rule": "Urgency or scarcity. Must be true: UCPD Annex I no.7, UK DMCC Act Schedule 20, CMA urgency investigations 2025 to 2026, TR Ticari Reklam Yönetmeliği. See pricing-promotions-and-consumer-law.md",
        "fix": "Keep only with a real end date or stock figure that the site enforces; never restart timers.",
    },
    {
        "id": "CLAIM-SUPERLATIVE",
        "pattern": r"(#\s?1\b|\bnumber one\b|\bno\.?\s?1\b|\bthe best\b|\bbest[- ](selling|seller|rated|in class)\b|\bworld'?s (first|best|leading|only)\b|\b(market|industry)[- ]leading\b|\bthe leading\b|\bunbeatable\b|\blowest prices?\b|\bcheapest\b|\btestsieger\b|en iyi|bir numara|en ucuz)",
        "severity": "REVIEW",
        "rule": "Superlative or ranking needs objective, current proof (EU comparative advertising Directive 2006/114 Art 4, CAP 3.7 and 3.33, DE Alleinstellungswerbung, Google and Meta misleading claims policies, Google Play metadata policy). See product-facts-and-evidence.md",
        "fix": "Cite the ranking source and date in the copy or footnote, or soften to puffery that is not objectively verifiable.",
    },
    {
        "id": "CLAIM-COMPARATIVE",
        "pattern": r"\b(better than|cheaper than|faster than|stronger than|more effective than|compared (to|with)|versus|vs\.?)\b|\b(than|vs) (any|other|leading|competitors?)\b|(\w+'den daha (iyi|ucuz|etkili))",
        "severity": "REVIEW",
        "rule": "Comparative claim. EU Directive 2006/114 Art 4 conditions, UK CAP 3.33 to 3.44, US Lanham Act 43(a) exposure, TR comparative ad rules. See pricing-promotions-and-consumer-law.md",
        "fix": "Document like for like test, date, method and sample; keep the comparison verifiable by the customer.",
    },
    {
        "id": "CLAIM-GUARANTEE",
        "pattern": r"\b(guaranteed?|risk[- ]free|money[- ]back|no risk)\b|(garantili|garanti|kesin sonuç|kesin çözüm|mucizevi|mucize)",
        "severity": "REVIEW",
        "rule": "Guarantee or certainty claim. Terms must be stated and honoured (UCPD Art 6 and 7, CAP 3.52 to 3.55). TR: 'mucizevi' and 'garantili' are standard Reklam Kurulu findings in health ads. See product-facts-and-evidence.md",
        "fix": "State the guarantee terms next to the claim, or remove certainty language.",
    },
    {
        "id": "HLTH-MIRACLE-TR",
        "pattern": r"(mucizevi|mucize (etki|sonuç|ürün))",
        "severity": "BLOCK",
        "rule": "TR Reklam Kurulu: 'mucizevi' and similar wording in health or supplement ads is treated as misleading. See country-notes.md",
        "fix": "Kaldırın.",
    },
    {
        "id": "FIN-GUARANTEED-RETURN",
        "pattern": r"\b(guaranteed (returns?|profits?|income|yield)|risk[- ]free (investment|returns?|profit)|double your money|get rich|passive income guaranteed|can'?t lose)\b|(garantili (getiri|kazanç)|kesin kazanç|risksiz (yatırım|getiri))",
        "severity": "BLOCK",
        "rule": "Investment or crypto return promise. EU MiCA Art 7 and MiFID II fair, clear, not misleading; UK FCA COBS 4 and crypto promotion rules; TR SPK III-35/B communiqués; all major ad platforms. See regulated-categories.md",
        "fix": "Remove. Financial promotions need regulated approval and risk warnings.",
    },
    {
        "id": "FIN-CREDIT",
        "pattern": r"\b(0\s?%\s?(apr|interest|finance)|interest[- ]free|no credit check|guaranteed approval|instant approval|bad credit (ok|welcome)|buy now,? pay later|bnpl)\b|(faizsiz|sıfır faiz|kefilsiz kredi)",
        "severity": "REVIEW",
        "rule": "Credit promotion. EU CCD2 (Directive 2023/2225) from 2026-11-20: warning 'Borrowing money costs money' and representative example when costs are shown; UK CONC 3 and FCA rules; US Reg Z triggering terms; Meta financial special ad category; Google financial services verification. See regulated-categories.md",
        "fix": "Route to legal review; add the representative example and the required warning for each market.",
    },
    {
        "id": "GAMB-PROMISE",
        "pattern": r"\b(risk[- ]free bet|guaranteed win|sure win|free bets?|no[- ]lose)\b|(bedava bahis|kesin kazanır)",
        "severity": "REVIEW",
        "severity_by_market": {"UK": "BLOCK", "NL": "BLOCK", "TR": "BLOCK"},
        "rule": "Gambling inducement. UK CAP 16 and Gambling Commission rules, NL bonus and advertising limits, TR only state licensed operators may advertise. See regulated-categories.md",
        "fix": "Route to legal review; most markets restrict or ban this wording.",
    },
    {
        "id": "PLAT-PERSONAL-ATTRIBUTE",
        "pattern": r"\b(are you|do you (have|suffer)|struggling with|tired of being|you'?re)\b[^.?!\n]{0,25}\b(overweight|fat|obese|diabetic|depressed|anxious|in debt|broke|bald|balding|single|divorced|infertile|addicted|acne|wrinkles)\b",
        "severity": "REVIEW",
        "rule": "Meta Advertising Standards personal attributes: ads must not assert or imply personal characteristics (health, financial status and others). See platform-ad-policies.md",
        "fix": "Speak about the product or the situation, not the reader's attribute ('For people who want...').",
    },
    {
        "id": "PROOF-RATINGS",
        "pattern": r"\b\d([.,]\d)?\s?(/\s?5|stars?|out of 5)\b|\b\d[\d,.]*\+?\s?(reviews|ratings|happy customers|customers|users|downloads)\b|(\d[\d.]*\+?\s?(yorum|müşteri|kullanıcı)|\d([.,]\d)?\s?yıldız)",
        "severity": "REVIEW",
        "rule": "Rating, review count or customer count. Must match a dated fact; reviews must be genuine (FTC 16 CFR 465, UCPD Annex I 23b and 23c, UK DMCC Schedule 20, TR Ticari Reklam Yönetmeliği 2026). See reviews-endorsements-and-influencers.md",
        "fix": "Cite source and date of the rating; update monthly.",
    },
    {
        "id": "AI-CAPABILITY",
        "pattern": r"\b(ai[- ]powered|powered by ai|uses ai|artificial intelligence|fully automated|replaces? (your )?(staff|employees|team|agents?)|100\s?% accurate)\b|(yapay zeka destekli)",
        "severity": "REVIEW",
        "rule": "AI capability claim. FTC AI washing cases 2024 to 2026 (Workado, Air AI, Growth Cave); substantiate accuracy and scope. See ai-disclosure-and-synthetic-media.md",
        "fix": "Back every performance number with a test on representative data; describe what the AI actually does.",
    },
    {
        "id": "CLAIM-ORIGIN",
        "pattern": r"\b(made in (the )?(usa|u\.s\.a\.|america|germany|italy|uk|turkey|türkiye)|swiss made|yerli üretim|türk malı)\b",
        "severity": "REVIEW",
        "rule": "Origin claim. US FTC Made in USA Labeling Rule (16 CFR 323), EU and TR misleading origin rules. See product-facts-and-evidence.md",
        "fix": "Verify the origin fact (all or virtually all for US unqualified claims).",
    },
    {
        "id": "INFO-NUMBER",
        "pattern": r"\b\d+([.,]\d+)?\s?(%|percent\b|x faster\b|x more\b|times\b)",
        "severity": "INFO",
        "rule": "Numeric claim: every number in customer facing copy must trace to a PRODUCT_FACTS row. See product-facts-and-evidence.md",
        "fix": "Confirm the fact ID or remove the number.",
    },
]


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------
def fold(text):
    """Lower case with Turkish dotted and dotless i folded to 'i'. Keeps length when possible."""
    t = text.replace("İ", "i").replace("I", "i").replace("ı", "i")
    low = t.lower()
    return low if len(low) == len(text) else None


def strip_html(text):
    text = re.sub(r"(?is)<(script|style)\b.*?</\1>", lambda m: "\n" * m.group(0).count("\n"), text)
    text = re.sub(r"(?s)<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text)
    text = re.sub(r"<[^>\n]*>", " ", text)
    return html.unescape(text)


def normalize_market(code):
    c = code.strip().upper().replace(".", "")
    return MARKET_ALIASES.get(c, c)


def parse_markets(cell):
    if cell is None:
        return set()
    cell = cell.strip()
    if not cell or cell.lower() in {"all", "any", "global", "*", "-"}:
        return set()
    return {normalize_market(p) for p in re.split(r"[,;/\s]+", cell) if p.strip()}


def expand_markets(markets):
    """Requested markets plus 'EU' when any EU member state is requested."""
    out = set(markets)
    if out & EU_MEMBERS:
        out.add("EU")
    return out


def rule_applies(rule_markets, requested):
    if not rule_markets or not requested:
        return True
    req = expand_markets(requested)
    return bool(rule_markets & req) or ("EU" in rule_markets and bool(req & EU_MEMBERS))


def compile_pattern(raw):
    """Return a list of compiled regexes for a registry cell."""
    raw = raw.strip().strip("`").strip()
    if not raw:
        return []
    if len(raw) > 2 and raw.startswith("/") and raw.rfind("/") > 0:
        end = raw.rfind("/")
        body = raw[1:end]
        try:
            return [re.compile(body, re.IGNORECASE)]
        except re.error as exc:
            raise ValueError("invalid regex %r: %s" % (raw, exc))
    out = []
    for alt in raw.split(";"):
        alt = alt.strip().strip('"').strip("'").strip()
        if not alt:
            continue
        folded = fold(alt) or alt.lower()
        esc = re.escape(folded)
        esc = re.sub(r"(\\ )+", r"\\s+", esc)
        prefix = r"\b" if re.match(r"\w", folded[0]) else ""
        suffix = r"\b" if re.match(r"\w", folded[-1]) else ""
        out.append(re.compile(prefix + esc + suffix, re.IGNORECASE))
    return out


# ---------------------------------------------------------------------------
# Markdown table parsing
# ---------------------------------------------------------------------------
def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    cells, buf, in_code = [], [], False
    for ch in line:
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append("".join(buf).strip())
            buf = []
        else:
            buf.append(ch)
    cells.append("".join(buf).strip())
    return cells


def parse_tables_by_section(text):
    """Return {section_heading_lower: [ {header: value} rows ]} for the first table in each section."""
    sections, current, header, rows = {}, None, None, None
    for line in text.splitlines():
        h = re.match(r"^\s{0,3}#{2,4}\s+(.*)$", line)
        if h:
            current = h.group(1).strip().lower()
            sections.setdefault(current, [])
            header, rows = None, sections[current]
            continue
        if current is None or not line.strip().startswith("|"):
            header = None  # a new table after any non table line starts with its own header row
            continue
        cells = split_row(line)
        if all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in cells if c):
            continue
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if not any(c.strip() for c in cells):
            continue
        row = {header[i] if i < len(header) else "col%d" % i: cells[i] for i in range(len(cells))}
        row["_cells"] = cells
        rows.append(row)
    return sections


def pick(row, *keys, default=""):
    for k in keys:
        for h, v in row.items():
            if h != "_cells" and k in h:
                return v
    return default


def load_registry(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    sections = parse_tables_by_section(text)
    reg = {"approved": [], "review": [], "blocked": []}
    for name, rows in sections.items():
        if name.startswith("approved"):
            kind = "approved"
        elif name.startswith("needs review") or name.startswith("needs-review") or name.startswith("review"):
            kind = "review"
        elif name.startswith("blocked") or name.startswith("prohibited"):
            kind = "blocked"
        else:
            continue
        for row in rows:
            cells = row["_cells"]
            claim = cells[0].strip() if cells else ""
            if not claim:
                continue
            entry = {"claim": claim, "row": row}
            if kind == "approved":
                entry["markets"] = parse_markets(pick(row, "market"))
                entry["basis"] = pick(row, "legal basis", "evidence", "basis")
                entry["conditions"] = pick(row, "condition")
            elif kind == "review":
                entry["markets"] = parse_markets(pick(row, "market"))
                entry["reason"] = pick(row, "why", "reason")
                entry["status"] = pick(row, "status")
            else:
                entry["markets"] = parse_markets(pick(row, "market"))
                entry["reason"] = pick(row, "reason", "rule", "why")
            try:
                entry["regexes"] = compile_pattern(claim)
            except ValueError as exc:
                raise ValueError("%s: %s" % (path, exc))
            reg[kind].append(entry)
    return reg


# ---------------------------------------------------------------------------
# Product facts check
# ---------------------------------------------------------------------------
def parse_date(value):
    value = (value or "").strip()
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", value)
    if not m:
        return None
    try:
        return _dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def check_facts(path, today, warn_days=30):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    findings = []
    lines = text.splitlines()
    header = None
    for idx, line in enumerate(lines, 1):
        if not line.strip().startswith("|"):
            header = None
            continue
        cells = split_row(line)
        if all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in cells if c):
            continue
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if not any("status" in h or "evidence" in h for h in header):
            continue
        if not any(cells):
            continue
        row = {header[i] if i < len(header) else "col%d" % i: cells[i] for i in range(len(cells))}
        fact = cells[0] if cells else ""
        if not fact:
            continue
        status = pick(row, "status").lower()
        evidence = pick(row, "evidence")
        expiry = parse_date(pick(row, "expiry", "review date"))
        source_date = parse_date(pick(row, "source date"))
        owner = pick(row, "owner")

        def add(sev, rid, msg):
            findings.append({
                "file": path, "line": idx, "col": 1, "severity": sev, "source": "facts",
                "rule_id": rid, "match": fact, "message": msg,
                "rule": "Every customer facing fact needs evidence, a source date, an owner and an expiry. See product-facts-and-evidence.md",
                "fix": "Update the row with current evidence or stop using the fact in copy.",
            })

        if status and status not in {"verified", "approved"}:
            add("REVIEW", "FACT-STATUS", "status is '%s': cannot be used in public copy" % status)
        if not status:
            add("REVIEW", "FACT-STATUS", "no status: treat as unverified")
        if not evidence.strip():
            add("REVIEW", "FACT-EVIDENCE", "no evidence document recorded")
        if not owner.strip():
            add("INFO", "FACT-OWNER", "no owner recorded")
        if source_date is None:
            add("INFO", "FACT-SOURCE-DATE", "no source date (YYYY-MM-DD)")
        if expiry is None:
            add("INFO", "FACT-EXPIRY", "no expiry or review date (YYYY-MM-DD)")
        elif expiry < today:
            add("BLOCK", "FACT-EXPIRED", "expired on %s: remove from live copy or renew evidence" % expiry.isoformat())
        elif (expiry - today).days <= warn_days:
            add("REVIEW", "FACT-EXPIRING", "expires on %s (within %d days)" % (expiry.isoformat(), warn_days))
    return findings


# ---------------------------------------------------------------------------
# Scanning
# ---------------------------------------------------------------------------
def severity_for(rule, requested):
    """Severity for the requested markets: per market override if present, else the default.
    With several markets the strictest wins. With no market given, the strictest of all applies."""
    base = rule["severity"]
    by_market = rule.get("severity_by_market") or {}
    if not by_market:
        return base
    if not requested:
        return max([base] + list(by_market.values()), key=lambda s: SEVERITY_ORDER.get(s, 0))
    levels = []
    for mkt in requested:
        if mkt in by_market:
            levels.append(by_market[mkt])
        elif (mkt == "EU" or mkt in EU_MEMBERS) and "EU" in by_market:
            levels.append(by_market["EU"])
        else:
            levels.append(base)
    return max(levels, key=lambda s: SEVERITY_ORDER.get(s, 0))


def scan_text(text, label, registry, requested, use_builtin=True):
    findings = []
    builtin = []
    if use_builtin:
        for rule in BUILTIN_RULES:
            builtin.append((rule, re.compile(rule["pattern"], re.IGNORECASE)))
    for lineno, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        folded = fold(line)
        hay = folded if folded is not None else line
        approved_spans = []
        line_findings = []
        if registry:
            for entry in registry["approved"]:
                if not rule_applies(entry["markets"], requested):
                    continue
                for rx in entry["regexes"]:
                    for m in rx.finditer(hay):
                        approved_spans.append((m.start(), m.end()))
                        line_findings.append({
                            "file": label, "line": lineno, "col": m.start() + 1, "severity": "APPROVED",
                            "source": "registry", "rule_id": "REG-APPROVED", "match": line[m.start():m.end()],
                            "message": "approved claim; conditions: %s" % (entry.get("conditions") or "none recorded"),
                            "rule": entry.get("basis") or "basis not recorded in CLAIMS.md",
                            "fix": "Check the conditions still hold for this product and market.",
                        })

        def inside_approved(start, end):
            return any(s <= start and end <= e for s, e in approved_spans)

        if registry:
            for kind, sev, rid in (("blocked", "BLOCK", "REG-BLOCKED"), ("review", "REVIEW", "REG-REVIEW")):
                for entry in registry[kind]:
                    if not rule_applies(entry["markets"], requested):
                        continue
                    for rx in entry["regexes"]:
                        for m in rx.finditer(hay):
                            conflict = inside_approved(m.start(), m.end())
                            line_findings.append({
                                "file": label, "line": lineno, "col": m.start() + 1,
                                "severity": "REVIEW" if (conflict and kind == "blocked") else sev,
                                "source": "registry",
                                "rule_id": "REG-CONFLICT" if conflict and kind == "blocked" else rid,
                                "match": line[m.start():m.end()],
                                "message": ("registry conflict: matches both Approved and Blocked; human must resolve. " if conflict and kind == "blocked" else "")
                                + "registry pattern '%s'" % entry["claim"],
                                "rule": entry.get("reason") or "reason not recorded in CLAIMS.md",
                                "fix": "Use approved wording from CLAIMS.md or send to review.",
                            })
        for rule, rx in builtin:
            for m in rx.finditer(hay):
                if inside_approved(m.start(), m.end()):
                    continue
                line_findings.append({
                    "file": label, "line": lineno, "col": m.start() + 1,
                    "severity": severity_for(rule, requested), "source": "builtin",
                    "rule_id": rule["id"], "match": line[m.start():m.end()],
                    "message": "built-in pattern", "rule": rule["rule"], "fix": rule["fix"],
                })
        # de-duplicate identical rule hits at the same position
        seen = set()
        for f in line_findings:
            key = (f["line"], f["col"], f["rule_id"])
            if key in seen:
                continue
            seen.add(key)
            f["text"] = line.strip()[:200]
            findings.append(f)
    return findings


def line_verdicts(findings):
    by_line = {}
    for f in findings:
        if f["source"] == "facts":
            continue
        key = (f["file"], f["line"])
        by_line.setdefault(key, []).append(f)
    verdicts = []
    for (file, line), fs in sorted(by_line.items()):
        sev = max((SEVERITY_ORDER.get(f["severity"], 0) for f in fs), default=0)
        if any(f["severity"] == "BLOCK" for f in fs):
            v = "BLOCKED"
        elif any(f["severity"] == "REVIEW" for f in fs):
            v = "NEEDS REVIEW"
        elif any(f["severity"] == "APPROVED" for f in fs):
            v = "APPROVED WORDING FOUND"
        else:
            v = "INFO ONLY"
        verdicts.append({"file": file, "line": line, "verdict": v, "rules": sorted({f["rule_id"] for f in fs}), "level": sev})
    return verdicts


def summarize(findings):
    counts = {"BLOCK": 0, "REVIEW": 0, "INFO": 0, "APPROVED": 0}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    return counts


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def fmt_text(findings, verdicts, counts):
    out = []
    order = sorted(findings, key=lambda f: (f["file"], f["line"], -SEVERITY_ORDER.get(f["severity"], 0), f["col"]))
    for f in order:
        out.append("%s:%d:%d %-8s %-24s \"%s\" | %s | fix: %s" % (
            f["file"], f["line"], f["col"], f["severity"], f["rule_id"], f["match"], f["rule"], f["fix"]))
    out.append("")
    out.append("Line verdicts (screening only, the compliance review decides):")
    for v in verdicts:
        out.append("  %s:%d %s [%s]" % (v["file"], v["line"], v["verdict"], ", ".join(v["rules"])))
    out.append("")
    out.append("Summary: %d block, %d review, %d info, %d approved wording matches" % (
        counts["BLOCK"], counts["REVIEW"], counts["INFO"], counts["APPROVED"]))
    return "\n".join(out)


def md_escape(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def fmt_md(findings, verdicts, counts):
    out = ["| File:line | Severity | Rule ID | Match | Rule | Fix |", "|---|---|---|---|---|---|"]
    order = sorted(findings, key=lambda f: (f["file"], f["line"], -SEVERITY_ORDER.get(f["severity"], 0)))
    for f in order:
        out.append("| %s:%d | %s | %s | %s | %s | %s |" % (
            md_escape(f["file"]), f["line"], f["severity"], f["rule_id"], md_escape(f["match"]), md_escape(f["rule"]), md_escape(f["fix"])))
    out.append("")
    out.append("Summary: %d block, %d review, %d info, %d approved wording matches." % (
        counts["BLOCK"], counts["REVIEW"], counts["INFO"], counts["APPROVED"]))
    return "\n".join(out)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def build_parser():
    p = argparse.ArgumentParser(description="Screen copy against CLAIMS.md and built-in risk patterns.")
    p.add_argument("paths", nargs="*", help="files to scan; use - for stdin")
    p.add_argument("--text", action="append", default=[], help="inline text to scan (repeatable)")
    p.add_argument("--claims", help="path to ads-master/brand/CLAIMS.md")
    p.add_argument("--facts", help="path to ads-master/brand/PRODUCT_FACTS.md (checks status and expiry)")
    p.add_argument("--facts-only", action="store_true", help="only run the product facts check")
    p.add_argument("--market", default="", help="comma separated market codes, for example EU,UK,TR (default: all, strictest)")
    p.add_argument("--no-builtin", action="store_true", help="disable the built-in pattern pack")
    p.add_argument("--strip-html", action="store_true", help="strip HTML tags before scanning (automatic for .html and .htm)")
    p.add_argument("--format", choices=["text", "json", "md"], default="text")
    p.add_argument("--fail-on", choices=["block", "review", "never"], default="review",
                   help="lowest severity that makes the exit code non zero (default review)")
    p.add_argument("--today", help="override today's date (YYYY-MM-DD) for the facts check")
    p.add_argument("--list-rules", action="store_true", help="print the built-in rule pack and exit")
    return p


def main(argv=None, stdout=None):
    stdout = stdout or sys.stdout
    args = build_parser().parse_args(argv)
    if args.list_rules:
        for r in BUILTIN_RULES:
            extra = " (by market: %s)" % r["severity_by_market"] if r.get("severity_by_market") else ""
            stdout.write("%-24s %-6s%s\n    %s\n" % (r["id"], r["severity"], extra, r["rule"]))
        return 0
    requested = {normalize_market(m) for m in args.market.split(",") if m.strip()}
    today = parse_date(args.today) if args.today else _dt.date.today()
    if args.facts_only and not args.facts:
        stdout.write("error: --facts-only needs --facts PATH\n")
        return 3
    if args.today and today is None:
        stdout.write("error: --today must be YYYY-MM-DD\n")
        return 3

    registry = None
    findings = []
    try:
        if args.claims:
            registry = load_registry(args.claims)
        if args.facts:
            findings.extend(check_facts(args.facts, today))
    except (OSError, ValueError) as exc:
        stdout.write("error: %s\n" % exc)
        return 3

    if not args.facts_only:
        inputs = []
        for i, t in enumerate(args.text, 1):
            inputs.append(("text%d" % i, t))
        for path in args.paths:
            try:
                if path == "-":
                    data = sys.stdin.read()
                    label = "stdin"
                else:
                    with open(path, encoding="utf-8", errors="replace") as fh:
                        data = fh.read()
                    label = path
            except OSError as exc:
                stdout.write("error: %s\n" % exc)
                return 3
            if args.strip_html or os.path.splitext(path)[1].lower() in {".html", ".htm"}:
                data = strip_html(data)
            inputs.append((label, data))
        if not inputs and not args.facts:
            stdout.write("error: nothing to scan (give paths, --text or --facts)\n")
            return 3
        for label, data in inputs:
            findings.extend(scan_text(data, label, registry, requested, use_builtin=not args.no_builtin))

    verdicts = line_verdicts(findings)
    counts = summarize(findings)
    if args.format == "json":
        stdout.write(json.dumps({"summary": counts, "markets": sorted(requested), "line_verdicts": verdicts,
                                 "findings": findings}, ensure_ascii=False, indent=2) + "\n")
    elif args.format == "md":
        stdout.write(fmt_md(findings, verdicts, counts) + "\n")
    else:
        stdout.write(fmt_text(findings, verdicts, counts) + "\n")

    if args.fail_on == "never":
        return 0
    if counts["BLOCK"]:
        return 2
    if args.fail_on == "review" and counts["REVIEW"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
