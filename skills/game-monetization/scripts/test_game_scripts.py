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


def fails_of(policy):
    return " | ".join(monetization_check.check(policy)[0])


def run(script, *args):
    p = subprocess.run([sys.executable, "-I", os.path.join(HERE, script), *args], capture_output=True, text=True, timeout=60)
    return p.returncode, p.stdout


class MonetizationCheckTest(unittest.TestCase):
    def test_samples_pass(self):
        for name in ("daily-social-policy.json", "progression-policy.json"):
            self.assertEqual(monetization_check.check(load(name))[0], [], name)

    def test_paid_counted_try_in_ranked_mode_fails(self):
        p = load("daily-social-policy.json")
        p["catalog"].append({"sku": "extra_try", "kind": "consumable", "grants": [{"kind": "attempt", "amount": 1, "writesTo": ["global_day"]}],
                             "basePrice": {"currency": "EUR", "minor": 99},
                             "storeProductIds": {"web": "a", "apple": "b", "google": "c"}, "random": False})
        p["offers"].append({"id": "buy_try", "point": "on_attempts_exhausted", "mode": "daily", "sku": "extra_try",
                            "grantsTo": "buyer", "maxPerDay": 1, "countdown": False, "priceEscalation": False})
        f = fails_of(p)
        self.assertIn("ranked mode grants 'attempt'", f)
        self.assertIn("'attempt' writes to ranked board 'global_day'", f)

    def test_encore_cannot_reach_the_global_board(self):
        p = load("daily-social-policy.json")
        p["catalog"][2]["grants"][0]["writesTo"].append("global_day")
        self.assertIn("may only write to boards no wider than who receives it", fails_of(p))

    def test_rewarded_practice_ad_cannot_grant_a_counted_try(self):
        p = load("daily-social-policy.json")
        p["placements"][0]["grants"] = [{"kind": "attempt", "amount": 1, "writesTo": ["group_day"]}]
        self.assertIn("'attempt' writes to ranked board 'group_day'", fails_of(p))

    def test_substring_hole_closed(self):
        p = load("progression-policy.json")
        p["catalog"][3]["grants"] = [{"kind": "moves", "id": "plus_theme", "amount": 5}]
        self.assertIn("ranked mode grants 'moves'", fails_of(p))

    def test_structure_rules(self):
        p = load("daily-social-policy.json")
        p["offers"].append(copy.deepcopy(p["offers"][0]))
        p["modes"][0]["countedAttemptsPerDay"] = 0
        del p["catalog"][1]["period"]
        p["catalog"][0]["storeProductIds"].pop("google")
        p["catalog"][0]["basePrice"] = {"currency": "EUR", "minor": 2.99}
        p["offers"][1]["point"] = "onSeasonStart"
        del p["placements"][0]["grants"]
        f = fails_of(p)
        for s in ("duplicate offer id", "countedAttemptsPerDay", "needs a period", "no product id for store 'google'",
                  "positive integer in minor units", "must be snake_case", "must declare what it grants"):
            self.assertIn(s, f)

    def test_unlimited_ranked_ladder_is_allowed(self):
        p = load("progression-policy.json")
        p["modes"][1]["countedAttemptsPerDay"] = "unlimited"
        self.assertEqual(monetization_check.check(p)[0], [])

    def test_consumer_and_ad_rules(self):
        bad = load("progression-policy.json")
        bad["offers"][0]["priceEscalation"] = True
        bad["offers"][0]["countdown"] = True
        del bad["offers"][1]["maxPerAttempt"]
        bad["currencies"]["virtual"][0]["showRealMoneyPrice"] = False
        del bad["placements"][0]["graceLevels"]
        bad["placements"][1]["optIn"] = False
        bad["placements"][2]["point"] = "on_level_start"
        bad["consent"]["requiredBeforeAds"] = False
        f = fails_of(bad)
        for s in ("price escalation", "countdown", "maxPerAttempt", "real money price is not shown",
                  "first session grace", "must be opt in", "banners only", "consent.requiredBeforeAds"):
            self.assertIn(s, f)

    def test_sibling_escalation(self):
        p = load("progression-policy.json")
        p["catalog"].append({"sku": "extra_moves_2", "kind": "consumable", "grants": [{"kind": "moves", "amount": 5}],
                             "basePrice": {"currency": "USD", "minor": 199},
                             "storeProductIds": {"apple": "x", "google": "y"}, "random": False})
        p["offers"].append({"id": "moves_on_fail_2", "point": "on_fail", "mode": "levels", "sku": "extra_moves_2",
                            "grantsTo": "buyer", "maxPerAttempt": 1, "countdown": False, "priceEscalation": False})
        self.assertIn("escalation by sibling offers", fails_of(p))

    def test_random_items(self):
        p = load("progression-policy.json")
        p["catalog"][2]["random"] = True
        p["product"]["regions"].append("BE")
        f = fails_of(p)
        for s in ("without odds", "lootBoxes is false", "audience under 18", "Belgium"):
            self.assertIn(s, f)

    def test_social_must_grant_group_and_unknown_refs(self):
        p = load("daily-social-policy.json")
        p["offers"][0]["grantsTo"] = "buyer"
        p["placements"][0]["mode"] = "nope"
        p["catalog"][2]["grants"][0]["writesTo"] = ["missing_board"]
        f = fails_of(p)
        self.assertIn("social mode grants must go to the group", f)
        self.assertIn("mode 'nope' is not declared", f)
        self.assertIn("unknown board 'missing_board'", f)

    def test_cli_exit_codes(self):
        self.assertEqual(run("monetization_check.py", os.path.join(HERE, "samples", "daily-social-policy.json"))[0], 0)
        with tempfile.TemporaryDirectory() as d:
            bad = os.path.join(d, "p.json")
            with open(bad, "w", encoding="utf-8") as fh:
                fh.write("{not json")
            self.assertEqual(run("monetization_check.py", bad)[0], 2)
            with open(bad, "w", encoding="utf-8") as fh:
                json.dump({"contractVersion": "0.9"}, fh)
            self.assertEqual(run("monetization_check.py", bad)[0], 2)
            with open(bad, "w", encoding="utf-8") as fh:
                json.dump({"contractVersion": "0.1"}, fh)
            code, out = run("monetization_check.py", bad)
            self.assertEqual(code, 1)
            self.assertIn("missing required keys", out)


if __name__ == "__main__":
    unittest.main()
