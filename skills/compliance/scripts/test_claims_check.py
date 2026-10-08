#!/usr/bin/env python3
"""Tests for claims_check.py. Standard library only.

Run: python3 -m unittest -v test_claims_check   (from this folder)
 or: python3 test_claims_check.py
"""

import datetime as dt
import io
import json
import os
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import claims_check as cc  # noqa: E402

CLAIMS_MD = """# Claims Registry

## Approved
| Claim (exact wording) | Markets | Legal basis or evidence | Conditions (e.g. per product, footnote required) | Approved by | Date |
|-----------------------|---------|-------------------------|---------------------------------------------------|-------------|------|
| Source of protein | EU, UK, TR | EU 1924/2006 Annex: at least 12% of energy from protein; fact F-003 | Only Bar Original 60 g | Jane Doe | 2026-10-01 |
| Vitamin C contributes to the normal function of the immune system | EU | Reg 432/2012; product gives 30% NRV per bar (F-007) | Bar Berry only | Jane Doe | 2026-10-01 |

## Needs review (do not publish)
| Claim | Why it needs review | Reviewer | Status |
|-------|---------------------|----------|--------|
| keeps you full for hours | Satiety claim, no authorised claim, no study | legal | open |

## Blocked
| Claim or pattern | Reason (rule) | Markets |
|------------------|---------------|---------|
| guilt-free | Implies other foods cause guilt; misleading per BRAND.md policy | all |
| /\\bketo[- ]approved\\b/ | No certification exists for this wording | EU |
| doğal şeker | Unverified natural sugar wording | TR |
"""

FACTS_MD = """# Product Facts

| Fact | Exact wording allowed | Applies to (products, markets) | Evidence (document, certificate, lab report, nutrition table) | Source date | Expiry or review date | Owner | Status (verified, pending, expired) |
|------|-----------------------|--------------------------------|---------------------------------------------------------------|-------------|-----------------------|-------|-------------------------------------|
| F-003 Protein 14 g per 100 g, 400 kcal | 14 g protein per 100 g | Bar Original, EU | Lab report LR-2026-014 | 2026-03-01 | 2027-03-01 | Jane | verified |
| F-008 Recycled PET 80% | Bottle made from 80% recycled plastic | Bottle, all | Supplier cert SC-22 | 2025-01-10 | 2026-09-30 | Ops | verified |
| F-009 4.7 stars from 1,200 reviews | Rated 4.7/5 | All | | 2026-09-01 | 2026-10-20 | Growth | pending |
"""


def run(argv):
    buf = io.StringIO()
    code = cc.main(argv, stdout=buf)
    return code, buf.getvalue()


class ClaimsCheckTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp(prefix="claims_check_test_")
        cls.claims = os.path.join(cls.tmp, "CLAIMS.md")
        cls.facts = os.path.join(cls.tmp, "PRODUCT_FACTS.md")
        with open(cls.claims, "w", encoding="utf-8") as fh:
            fh.write(CLAIMS_MD)
        with open(cls.facts, "w", encoding="utf-8") as fh:
            fh.write(FACTS_MD)

    def scan(self, text, market="", builtin=True):
        reg = cc.load_registry(self.claims)
        req = {m for m in market.split(",") if m}
        return cc.scan_text(text, "t", reg, req, use_builtin=builtin)

    def ids(self, findings, severity=None):
        return {f["rule_id"] for f in findings if severity is None or f["severity"] == severity}

    # Registry parsing -----------------------------------------------------
    def test_registry_parsing_counts(self):
        reg = cc.load_registry(self.claims)
        self.assertEqual(len(reg["approved"]), 2)
        self.assertEqual(len(reg["review"]), 1)
        self.assertEqual(len(reg["blocked"]), 3)
        self.assertEqual(reg["blocked"][1]["markets"], {"EU"})

    def test_registry_blocked_literal(self):
        f = self.scan("A guilt-free snack for everyone", builtin=False)
        self.assertIn("REG-BLOCKED", self.ids(f, "BLOCK"))

    def test_registry_regex_and_market_filter(self):
        f_eu = self.scan("The first keto approved bar", market="NL", builtin=False)
        self.assertIn("REG-BLOCKED", self.ids(f_eu, "BLOCK"), "EU rule must apply to NL")
        f_us = self.scan("The first keto approved bar", market="US", builtin=False)
        self.assertNotIn("REG-BLOCKED", self.ids(f_us))

    def test_turkish_case_folding(self):
        f = self.scan("DOĞAL ŞEKER içerir", market="TR", builtin=False)
        self.assertIn("REG-BLOCKED", self.ids(f, "BLOCK"))

    def test_needs_review_pattern(self):
        f = self.scan("It keeps you full for hours.", builtin=False)
        self.assertIn("REG-REVIEW", self.ids(f, "REVIEW"))

    # Approved claims ------------------------------------------------------
    def test_approved_suppresses_builtin_inside_span(self):
        f = self.scan("Source of protein. Vitamin C contributes to the normal function of the immune system.", market="EU")
        self.assertIn("REG-APPROVED", self.ids(f, "APPROVED"))
        self.assertNotIn("FOOD-NUTRITION-CLAIM", self.ids(f), "approved wording must not be flagged again")

    def test_unapproved_variant_still_flagged(self):
        f = self.scan("High protein snack", market="EU")
        self.assertIn("FOOD-NUTRITION-CLAIM", self.ids(f, "REVIEW"))

    # Built-in rules -------------------------------------------------------
    def test_weight_loss_amount_blocked(self):
        f = self.scan("Lose 5 kg in 2 weeks with our tea")
        self.assertIn("HLTH-WEIGHT-RATE", self.ids(f, "BLOCK"))

    def test_disease_claim_blocked(self):
        f = self.scan("This blend helps cure diabetes naturally")
        self.assertIn("HLTH-DISEASE", self.ids(f, "BLOCK"))

    def test_percent_fat_free(self):
        self.assertIn("FOOD-PERCENT-FAT-FREE", self.ids(self.scan("97% fat free yogurt", market="UK"), "BLOCK"))
        self.assertIn("FOOD-PERCENT-FAT-FREE", self.ids(self.scan("97% fat free yogurt", market="US"), "REVIEW"))

    def test_environmental_by_market(self):
        self.assertIn("ENV-GENERIC", self.ids(self.scan("Our eco-friendly bottle", market="DE"), "BLOCK"))
        self.assertIn("ENV-GENERIC", self.ids(self.scan("Our eco-friendly bottle", market="US"), "REVIEW"))
        self.assertIn("ENV-OFFSET-NEUTRAL", self.ids(self.scan("Klimaneutral produziert", market="DE"), "BLOCK"))

    def test_turkish_price_and_miracle(self):
        f = self.scan("Mucizevi etki! %40 indirim sadece bugün", market="TR")
        self.assertIn("HLTH-MIRACLE-TR", self.ids(f, "BLOCK"))
        self.assertIn("PRICE-REDUCTION", self.ids(f, "REVIEW"))
        self.assertIn("PRICE-URGENCY", self.ids(f, "REVIEW"))

    def test_free_not_triggered_by_free_from(self):
        f = self.scan("Gluten-free and free from palm oil")
        self.assertNotIn("PRICE-FREE", self.ids(f))
        f2 = self.scan("Free shipping on all orders")
        self.assertIn("PRICE-FREE", self.ids(f2, "REVIEW"))

    def test_finance_guaranteed_return(self):
        f = self.scan("Guaranteed returns of 12% a year on your crypto")
        self.assertIn("FIN-GUARANTEED-RETURN", self.ids(f, "BLOCK"))

    def test_personal_attribute(self):
        f = self.scan("Are you struggling with being overweight?")
        self.assertIn("PLAT-PERSONAL-ATTRIBUTE", self.ids(f, "REVIEW"))

    def test_clean_line_has_no_findings(self):
        f = self.scan("Order today and get it delivered on Thursday.", market="EU")
        self.assertEqual([x for x in f if x["severity"] in ("BLOCK", "REVIEW")], [])

    # Product facts ----------------------------------------------------------
    def test_facts_expiry_and_status(self):
        f = cc.check_facts(self.facts, dt.date(2026, 10, 8))
        ids = {(x["match"].split(" ")[0], x["rule_id"]) for x in f}
        self.assertIn(("F-008", "FACT-EXPIRED"), ids)
        self.assertIn(("F-009", "FACT-STATUS"), ids)
        self.assertIn(("F-009", "FACT-EVIDENCE"), ids)
        self.assertIn(("F-009", "FACT-EXPIRING"), ids)
        self.assertFalse(any(x["match"].startswith("F-003") and x["severity"] in ("BLOCK", "REVIEW") for x in f))

    # CLI --------------------------------------------------------------------
    def test_cli_exit_codes_and_json(self):
        code, out = run(["--claims", self.claims, "--market", "EU", "--format", "json", "--text", "Lose 3 kg in 7 days"])
        self.assertEqual(code, 2)
        data = json.loads(out)
        self.assertGreaterEqual(data["summary"]["BLOCK"], 1)
        self.assertEqual(data["line_verdicts"][0]["verdict"], "BLOCKED")
        code, _ = run(["--claims", self.claims, "--text", "Free shipping over 50 EUR"])
        self.assertEqual(code, 1)
        code, _ = run(["--claims", self.claims, "--fail-on", "block", "--text", "Free shipping over 50 EUR"])
        self.assertEqual(code, 0)
        code, _ = run(["--claims", self.claims, "--text", "Delivered on Thursday."])
        self.assertEqual(code, 0)

    def test_cli_file_html_and_markdown_output(self):
        page = os.path.join(self.tmp, "page.html")
        with open(page, "w", encoding="utf-8") as fh:
            fh.write("<html><body><h1>Clinically proven</h1>\n<p>Carbon neutral delivery</p></body></html>\n")
        code, out = run(["--claims", self.claims, "--market", "FR", "--format", "md", page])
        self.assertEqual(code, 2)
        self.assertIn("ENV-OFFSET-NEUTRAL", out)
        self.assertIn("HLTH-PROOF", out)
        self.assertNotIn("<h1>", out)

    def test_cli_errors(self):
        code, out = run([])
        self.assertEqual(code, 3)
        code, out = run(["--claims", os.path.join(self.tmp, "missing.md"), "--text", "x"])
        self.assertEqual(code, 3)
        bad = os.path.join(self.tmp, "BAD.md")
        with open(bad, "w", encoding="utf-8") as fh:
            fh.write("## Blocked\n| Claim or pattern | Reason (rule) | Markets |\n|---|---|---|\n| /([unclosed/ | bad | all |\n")
        code, out = run(["--claims", bad, "--text", "x"])
        self.assertEqual(code, 3)
        self.assertIn("invalid regex", out)


if __name__ == "__main__":
    unittest.main(verbosity=2)
