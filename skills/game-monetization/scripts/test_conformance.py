#!/usr/bin/env python3
"""Tests for monetization_conformance.py (policy vs tracking plan vs store declarations).
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
import monetization_conformance as mc  # noqa: E402

SCRIPT = os.path.join(HERE, "monetization_conformance.py")


def load(name):
    with open(os.path.join(HERE, "samples", name), encoding="utf-8") as fh:
        return json.load(fh)


def aloo():
    return load("aloo-policy.json"), load("aloo-tracking-plan.json"), load("aloo-store-declarations.json")


def progression():
    return load("progression-policy.json"), load("progression-tracking-plan.json"), load("progression-store-declarations.json")


def plan_fails(policy, plan):
    return " | ".join(mc.check_plan(policy, plan)[0])


def plan_warns(policy, plan):
    return " | ".join(mc.check_plan(policy, plan)[1])


def decl_result(policy, decl):
    fails, warns, notes = mc.check_declarations(policy, decl, "declarations test")
    return " | ".join(fails), " | ".join(warns), " | ".join(notes)


def run_cli(*args):
    p = subprocess.run([sys.executable, "-I", SCRIPT, *args], capture_output=True, text=True, timeout=60)
    return p.returncode, p.stdout


class Files:
    """Write policy, plan and declarations to a temp dir and run the CLI on them."""

    def __init__(self, policy, plan, *decls):
        self.dir = tempfile.TemporaryDirectory()
        self.policy = self._write("policy.json", policy)
        self.plan = self._write("plan.json", plan)
        self.decls = [self._write(f"decl{i}.json", d) for i, d in enumerate(decls)]

    def _write(self, name, data):
        path = os.path.join(self.dir.name, name)
        with open(path, "w", encoding="utf-8") as fh:
            if isinstance(data, str):
                fh.write(data)
            else:
                json.dump(data, fh)
        return path

    def run(self):
        args = ["--policy", self.policy, "--tracking-plan", self.plan]
        for d in self.decls:
            args += ["--declarations", d]
        return run_cli(*args)

    def close(self):
        self.dir.cleanup()


class SamplesTest(unittest.TestCase):
    def test_samples_pass_with_no_failures_or_warnings(self):
        for policy, plan, decl in (aloo(), progression()):
            fails, warns = mc.check_plan(policy, plan)
            self.assertEqual(fails, [], policy["product"]["id"])
            self.assertEqual(warns, [], policy["product"]["id"])
            d_fails, d_warns, _ = mc.check_declarations(policy, decl, "d")
            self.assertEqual(d_fails, [], policy["product"]["id"])
            self.assertEqual(d_warns, [], policy["product"]["id"])

    def test_cli_passes_on_samples(self):
        for stem in ("aloo", "progression"):
            code, out = run_cli("--policy", os.path.join(HERE, "samples", f"{stem}-policy.json"),
                                "--tracking-plan", os.path.join(HERE, "samples", f"{stem}-tracking-plan.json"),
                                "--declarations", os.path.join(HERE, "samples", f"{stem}-store-declarations.json"))
            self.assertEqual(code, 0, out)
            self.assertIn("Verdict: PASS", out)
            self.assertIn("Policy check (monetization_check.py): PASS", out)
            self.assertTrue(out.strip().splitlines()[-1].startswith("This check cannot cover:"))


class OfferCoverageTest(unittest.TestCase):
    def test_missing_offer_event_names_every_offer(self):
        policy, plan, _ = aloo()
        del plan["events"]["offer_declined"]
        f = plan_fails(policy, plan)
        self.assertIn("event 'offer_declined' is not in the tracking plan", f)
        for offer in ("encore_at_game_over", "season_pass_at_season_start", "plus_after_practice"):
            self.assertIn(offer, f)

    def test_enum_must_carry_each_offer_value(self):
        policy, plan, _ = aloo()
        plan["events"]["offer_shown"]["props"]["sku"]["values"].remove("encore")
        plan["events"]["offer_accepted"]["props"]["point"]["values"].remove("custom_practice_done")
        plan["events"]["offer_declined"]["props"]["mode_id"]["values"].remove("daily")
        f = plan_fails(policy, plan)
        self.assertIn("offer encore_at_game_over: offer_shown.sku cannot carry 'encore'", f)
        self.assertIn("offer plus_after_practice: offer_accepted.point cannot carry 'custom_practice_done'", f)
        self.assertIn("offer season_pass_at_season_start: offer_declined.mode_id cannot carry 'daily'", f)

    def test_offer_id_values_are_checked(self):
        policy, plan, _ = aloo()
        plan["events"]["offer_shown"]["props"]["offer_id"]["values"].remove("plus_after_practice")
        self.assertIn("offer plus_after_practice: offer_shown.offer_id cannot carry", plan_fails(policy, plan))

    def test_offer_id_required_from_contract_0_2(self):
        policy, plan, _ = aloo()
        for e in mc.OFFER_EVENTS:
            del plan["events"][e]["props"]["offer_id"]
        f = plan_fails(policy, plan)
        for e in mc.OFFER_EVENTS:
            self.assertIn(f"{e}: no 'offer_id' property", f)

    def test_offer_id_optional_under_contract_0_1(self):
        policy, plan, _ = aloo()
        policy["contractVersion"] = "0.1"
        for e in plan["events"].values():
            e["props"]["contract_version"] = {"type": "enum", "values": ["0.1"]}
        for e in mc.OFFER_EVENTS:
            del plan["events"][e]["props"]["offer_id"]
        self.assertNotIn("offer_id", plan_fails(policy, plan))

    def test_missing_identity_property_fails_once_per_event(self):
        policy, plan, _ = aloo()
        del plan["events"]["offer_shown"]["props"]["sku"]
        f = mc.check_plan(policy, plan)[0]
        hits = [x for x in f if x.startswith("offer_shown: no 'sku' property")]
        self.assertEqual(len(hits), 1, f)

    def test_ambiguous_offers_warn_without_offer_id(self):
        policy, plan, _ = progression()
        twin = copy.deepcopy(policy["offers"][2])
        twin["id"] = "coins_in_shop_b"
        policy["offers"].append(twin)
        policy["contractVersion"] = "0.1"
        for e in mc.OFFER_EVENTS:
            del plan["events"][e]["props"]["offer_id"]
        self.assertIn("share sku, mode and point", plan_warns(policy, plan))


class PlacementCoverageTest(unittest.TestCase):
    def test_rewarded_needs_requested_shown_and_rewarded(self):
        for event in mc.REWARDED_EVENTS:
            policy, plan, _ = aloo()
            del plan["events"][event]
            f = plan_fails(policy, plan)
            self.assertIn(f"event '{event}' is not in the tracking plan", f)
            self.assertIn("rewarded_replay", f)

    def test_other_formats_need_only_ad_shown(self):
        policy, plan, _ = progression()
        policy["placements"] = [p for p in policy["placements"] if p["format"] != "rewarded"]
        del plan["events"]["ad_requested"]
        del plan["events"]["ad_rewarded"]
        self.assertEqual(mc.check_plan(policy, plan)[0], [])
        del plan["events"]["ad_shown"]
        f = plan_fails(policy, plan)
        self.assertIn("event 'ad_shown' is not in the tracking plan", f)
        self.assertIn("level_end_interstitial", f)
        self.assertIn("menu_banner", f)

    def test_placement_enum_and_point_coverage(self):
        policy, plan, _ = progression()
        plan["events"]["ad_shown"]["props"]["point"]["values"].remove("on_menu")
        f = plan_fails(policy, plan)
        self.assertIn("placement menu_banner: ad_shown.point cannot carry 'on_menu'", f)
        policy, plan, _ = aloo()
        plan["events"]["ad_rewarded"]["props"]["placement_id"] = {"type": "enum", "values": ["other"]}
        f = plan_fails(policy, plan)
        self.assertIn("placement rewarded_replay: ad_rewarded.placement_id cannot carry 'rewarded_replay'", f)

    def test_id_type_rejects_values_outside_the_pattern(self):
        policy, plan, _ = progression()
        policy["placements"][2]["id"] = "menu banner"
        f = plan_fails(policy, plan)
        self.assertIn("placement menu banner: ad_shown.placement_id cannot carry 'menu banner' (id pattern", f)

    def test_free_string_type_is_not_a_plan_type(self):
        policy, plan, _ = progression()
        plan["events"]["ad_shown"]["props"]["placement_id"] = {"type": "string"}
        self.assertIn("type 'string' is not a tracking plan type", plan_fails(policy, plan))


class CatalogCoverageTest(unittest.TestCase):
    def test_catalog_needs_completed_and_refunded(self):
        for event in mc.PURCHASE_EVENTS:
            policy, plan, _ = aloo()
            del plan["events"][event]
            f = plan_fails(policy, plan)
            self.assertIn(f"event '{event}' is not in the tracking plan", f)
            for sku in ("season_pass", "aloo_plus_monthly", "encore"):
                self.assertIn(sku, f)

    def test_sku_enum_must_list_every_sku(self):
        policy, plan, _ = aloo()
        plan["events"]["purchase_refunded"]["props"]["sku"]["values"].remove("aloo_plus_monthly")
        self.assertIn("sku aloo_plus_monthly: purchase_refunded.sku cannot carry 'aloo_plus_monthly'",
                      plan_fails(policy, plan))

    def test_stale_enum_value_warns(self):
        policy, plan, _ = aloo()
        plan["events"]["purchase_completed"]["props"]["sku"]["values"].append("old_pack")
        self.assertIn("purchase_completed.sku lists ['old_pack']", plan_warns(policy, plan))


class VersionPropertiesTest(unittest.TestCase):
    def test_missing_version_properties_fail(self):
        policy, plan, _ = aloo()
        del plan["events"]["ad_shown"]["props"]["policy_revision"]
        del plan["events"]["offer_accepted"]["props"]["contract_version"]
        del plan["events"]["purchase_completed"]["props"]["policy_revision"]
        f = plan_fails(policy, plan)
        self.assertIn("ad_shown: no 'policy_revision' property", f)
        self.assertIn("offer_accepted: no 'contract_version' property", f)
        self.assertIn("purchase_completed: no 'policy_revision' property", f)

    def test_contract_version_typed_num_fails(self):
        policy, plan, _ = aloo()
        plan["events"]["offer_shown"]["props"]["contract_version"] = {"type": "num", "min": 0, "max": 1}
        self.assertIn("contract_version is typed num", plan_fails(policy, plan))

    def test_contract_version_enum_must_include_the_policy_version(self):
        policy, plan, _ = aloo()
        plan["events"]["ad_shown"]["props"]["contract_version"] = {"type": "enum", "values": ["0.0"]}
        self.assertIn("ad_shown: contract_version cannot carry '0.2'", plan_fails(policy, plan))

    def test_policy_revision_outside_the_declared_range(self):
        policy, plan, _ = aloo()
        policy["policyRevision"] = 12
        for e in plan["events"].values():
            if "policy_revision" in e["props"]:
                e["props"]["policy_revision"] = {"type": "num", "min": 1, "max": 10}
        self.assertIn("policy_revision cannot carry 12 (num range 1 to 10)", plan_fails(policy, plan))

    def test_product_property(self):
        policy, plan, _ = aloo()
        plan["events"]["ad_shown"]["props"]["product"] = {"type": "enum", "values": ["other"]}
        self.assertIn("ad_shown: product cannot carry 'aloo'", plan_fails(policy, plan))
        policy, plan, _ = aloo()
        del plan["events"]["ad_shown"]["props"]["product"]
        self.assertEqual(mc.check_plan(policy, plan)[0], [])
        self.assertIn("ad_shown: no 'product' property", plan_warns(policy, plan))

    def test_recommended_events_warn(self):
        policy, plan, _ = aloo()
        for e in ("purchase_failed", "ad_revenue", "consent_updated"):
            del plan["events"][e]
        self.assertEqual(mc.check_plan(policy, plan)[0], [])
        w = plan_warns(policy, plan)
        for e in ("purchase_failed", "ad_revenue", "consent_updated"):
            self.assertIn(e, w)


class DeclarationsTest(unittest.TestCase):
    def test_ads_present_but_contains_ads_false(self):
        policy, _, decl = aloo()
        decl["containsAds"] = False
        f, _, _ = decl_result(policy, decl)
        self.assertIn("containsAds is false but the policy has ad placements", f)

    def test_random_items_but_loot_boxes_false(self):
        policy, _, decl = progression()
        policy["catalog"][2]["random"] = True
        policy["catalog"][2]["odds"] = {"rocket": 0.5, "bomb": 0.5}
        f, _, _ = decl_result(policy, decl)
        self.assertIn("lootBoxes is false but the policy has random items", f)
        self.assertIn("ageRatingInputs.randomItems is False but the policy says True", f)

    def test_catalog_but_in_app_purchases_false(self):
        policy, _, decl = aloo()
        decl["inAppPurchases"] = False
        self.assertIn("inAppPurchases is false but the policy has catalog items", decl_result(policy, decl)[0])

    def test_disagreement_with_policy_store_declarations(self):
        policy, _, decl = aloo()
        policy["placements"] = []
        policy["storeDeclarations"]["containsAds"] = True
        decl["containsAds"] = False
        decl["ageRatingInputs"]["advertising"] = False
        f, _, _ = decl_result(policy, decl)
        self.assertIn("containsAds is False but policy.storeDeclarations.containsAds is True", f)
        self.assertIn("the policy may be the file to fix", f)

    def test_over_declared_in_both_files_warns(self):
        policy, _, decl = aloo()
        policy["placements"] = []
        decl["ageRatingInputs"]["advertising"] = False
        f, w, _ = decl_result(policy, decl)
        self.assertEqual(f, "")
        self.assertIn("containsAds is true but the policy has no ad placements", w)

    def test_missing_boolean_fails(self):
        policy, _, decl = aloo()
        del decl["lootBoxes"]
        decl["inAppPurchases"] = "yes"
        f, _, _ = decl_result(policy, decl)
        self.assertIn("lootBoxes must be true or false", f)
        self.assertIn("inAppPurchases must be true or false", f)

    def test_age_rating_answers(self):
        policy, _, decl = aloo()
        decl["ageRatingInputs"].update({"advertising": False, "digitalPurchases": False, "madeForKids": True,
                                        "minimumTargetAge": 9})
        f, _, _ = decl_result(policy, decl)
        for s in ("ageRatingInputs.advertising is False", "ageRatingInputs.digitalPurchases is False",
                  "ageRatingInputs.madeForKids is True", "target audience starts at 9"):
            self.assertIn(s, f)

    def test_no_age_rating_answers_warns(self):
        policy, _, decl = aloo()
        del decl["ageRatingInputs"]
        f, w, _ = decl_result(policy, decl)
        self.assertEqual(f, "")
        self.assertIn("no ageRatingInputs", w)

    def test_store_scoped_catalog(self):
        policy, _, decl = aloo()
        for item in policy["catalog"]:
            item["stores"] = ["web"]
            item["storeProductIds"] = {"web": item["storeProductIds"]["web"]}
        decl["inAppPurchases"] = False
        decl["ageRatingInputs"]["digitalPurchases"] = False
        f, _, n = decl_result(policy, decl)
        self.assertEqual(f, "")
        self.assertIn("because store 'google' sells no catalog items", n)

    def test_unknown_store_fails(self):
        policy, _, decl = aloo()
        decl["store"] = "steam"
        self.assertIn("store 'steam' is not declared in policy.stores", decl_result(policy, decl)[0])


class CliTest(unittest.TestCase):
    def assertCannotCover(self, out):
        self.assertTrue(out.strip().splitlines()[-1].startswith("This check cannot cover:"), out)

    def test_failing_plan_exits_1(self):
        policy, plan, decl = aloo()
        del plan["events"]["ad_rewarded"]
        files = Files(policy, plan, decl)
        try:
            code, out = files.run()
        finally:
            files.close()
        self.assertEqual(code, 1)
        self.assertIn("Verdict: FAIL", out)
        self.assertCannotCover(out)

    def test_policy_that_fails_monetization_check_fails_here(self):
        policy, plan, _ = aloo()
        policy["offers"][0]["priceEscalation"] = True
        files = Files(policy, plan)
        try:
            code, out = files.run()
        finally:
            files.close()
        self.assertEqual(code, 1)
        self.assertIn("the policy fails monetization_check.py", out)

    def test_could_not_run_cases_exit_2(self):
        policy, plan, decl = aloo()
        other = dict(decl, product="someone-else")
        cases = [
            Files("{not json", plan),
            Files(dict(policy, contractVersion="0.9"), plan),
            Files({k: v for k, v in policy.items() if k != "contractVersion"}, plan),
            Files(dict(policy, offers={"a": 1}), plan),
            Files(policy, {"version": 1}),
            Files(policy, "[]"),
            Files(policy, plan, other),
            Files(policy, plan, "{oops"),
        ]
        try:
            for files in cases:
                code, out = files.run()
                self.assertEqual(code, 2, out)
                self.assertIn("could not run", out)
                self.assertCannotCover(out)
        finally:
            for files in cases:
                files.close()

    def test_missing_arguments_exit_2_with_cannot_cover(self):
        code, out = run_cli("--policy", os.path.join(HERE, "samples", "aloo-policy.json"))
        self.assertEqual(code, 2)
        self.assertCannotCover(out)

    def test_repeated_declarations(self):
        policy, plan, decl = aloo()
        apple = dict(decl, store="apple")
        bad = dict(decl, store="web", containsAds=False)
        files = Files(policy, plan, apple, bad)
        try:
            code, out = files.run()
        finally:
            files.close()
        self.assertEqual(code, 1)
        self.assertIn("declarations web: containsAds is false", out)
        self.assertNotIn("declarations apple: containsAds", out)


if __name__ == "__main__":
    unittest.main()
