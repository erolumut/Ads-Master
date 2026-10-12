#!/usr/bin/env python3
"""Tests for the game monetization scripts.
Run: python3 -m unittest discover -s skills/game-monetization/scripts -p "test_*.py"
"""
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import monetization_check  # noqa: E402


def load(name):
    with open(os.path.join(HERE, "samples", name), encoding="utf-8") as fh:
        return json.load(fh)


def run(script, *args):
    p = subprocess.run([sys.executable, "-I", os.path.join(HERE, script), *args], capture_output=True, text=True, timeout=60)
    return p.returncode, p.stdout


class MonetizationCheckTest(unittest.TestCase):
    def test_samples_pass(self):
        for name in ("aloo-policy.json", "progression-policy.json"):
            fails, _ = monetization_check.check(load(name))
            self.assertEqual(fails, [], name)

    def test_paid_counted_try_in_ranked_mode_fails(self):
        p = load("aloo-policy.json")
        p["catalog"].append({"sku": "extra_try", "kind": "consumable", "grants": ["attempt:1"],
                             "prices": {c: 0.99 for c in p["currencies"]["realMoney"]},
                             "platformIds": {"stripe": "x", "apple": "x", "google": "x"}, "random": False})
        p["offers"].append({"id": "buy_try", "point": "onAttemptsExhausted", "mode": "daily", "sku": "extra_try",
                            "affectsRankedResult": True, "grantsTo": "buyer", "maxPerDay": 1,
                            "countdown": False, "priceEscalation": False})
        fails, _ = monetization_check.check(p)
        joined = " ".join(fails)
        self.assertIn("affectsRankedResult false", joined)
        self.assertIn("only cosmetics, practice, archive or passes", joined)

    def test_consumer_and_ad_rules(self):
        p = load("progression-policy.json")
        bad = copy.deepcopy(p)
        bad["offers"][0]["priceEscalation"] = True
        bad["offers"][0]["countdown"] = True
        del bad["offers"][1]["maxPerAttempt"]
        bad["catalog"][0]["prices"].pop("EUR")
        bad["catalog"][1]["platformIds"].pop("google")
        bad["currencies"]["virtual"][0]["showRealMoneyPrice"] = False
        del bad["placements"][0]["graceLevels"]
        bad["placements"][1]["optIn"] = False
        bad["placements"][2]["point"] = "onLevelStart"
        bad["consent"]["requiredBeforeAds"] = False
        fails, _ = monetization_check.check(bad)
        joined = " ".join(fails)
        for s in ("price escalation", "countdown", "maxPerAttempt", "no real money price in EUR", "no google id",
                  "real money price is not shown", "first session grace", "must be opt in", "banners only",
                  "consent.requiredBeforeAds"):
            self.assertIn(s, joined)

    def test_random_items_need_odds_and_label(self):
        p = load("progression-policy.json")
        p["catalog"][2]["random"] = True
        fails, _ = monetization_check.check(p)
        self.assertTrue(any("without odds" in f for f in fails))
        self.assertTrue(any("lootBoxes is false" in f for f in fails))
        p["catalog"][2]["odds"] = {"rocket": 0.6, "bomb": 0.3}
        p["storeDeclarations"]["lootBoxes"] = True
        fails, _ = monetization_check.check(p)
        self.assertTrue(any("sum to 0.900" in f for f in fails))

    def test_social_must_grant_group_and_unknown_refs(self):
        p = load("aloo-policy.json")
        p["offers"][0]["grantsTo"] = "buyer"
        p["placements"][0]["mode"] = "nope"
        fails, _ = monetization_check.check(p)
        joined = " ".join(fails)
        self.assertIn("whole group", joined)
        self.assertIn("mode 'nope' is not declared", joined)

    def test_cli_exit_codes(self):
        self.assertEqual(run("monetization_check.py", os.path.join(HERE, "samples", "aloo-policy.json"))[0], 0)
        with tempfile.TemporaryDirectory() as d:
            bad = os.path.join(d, "p.json")
            with open(bad, "w", encoding="utf-8") as fh:
                fh.write("{not json")
            self.assertEqual(run("monetization_check.py", bad)[0], 2)
            with open(bad, "w", encoding="utf-8") as fh:
                json.dump({"contractVersion": "0.1"}, fh)
            code, out = run("monetization_check.py", bad)
            self.assertEqual(code, 1)
            self.assertIn("missing required keys", out)


if __name__ == "__main__":
    unittest.main()
