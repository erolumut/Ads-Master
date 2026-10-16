"""Tests for pxe_policy_check.py and difficulty_table.py.

Run from the repo root:
  python3 -I -B -m unittest discover -s skills/player-experience/scripts -p "test_*.py"
"""
from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import difficulty_table as dt  # noqa: E402
import pxe_policy_check as pc  # noqa: E402

SAMPLES = HERE / "samples"
VALID = json.loads((SAMPLES / "policy-valid.json").read_text(encoding="utf-8"))
CHECKER = HERE / "pxe_policy_check.py"
TABLE = HERE / "difficulty_table.py"


def run_script(script: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-I", "-B", str(script), *args], capture_output=True, text=True)


def messages(policy: dict, severity: str = "FAIL") -> list[str]:
    return [f"{i['scope']}: {i['message']}" for i in pc.check(policy).items if i["severity"] == severity]


def mutated(fn) -> dict:
    policy = copy.deepcopy(VALID)
    fn(policy)
    return policy


def rule(policy: dict, rid: str) -> dict:
    return next(r for r in policy["rules"] if r["id"] == rid)


class PolicyCheckTests(unittest.TestCase):
    def assertFailsWith(self, policy: dict, *needles: str) -> None:
        found = messages(policy)
        for needle in needles:
            self.assertTrue(any(needle in m for m in found), f"{needle!r} not in {found}")

    def test_valid_policy_passes_with_no_findings(self) -> None:
        self.assertEqual(pc.check(VALID).items, [])

    def test_allowed_names_are_not_forbidden(self) -> None:
        # skill_rating contains 'kill', so input names are matched against the input tokens only.
        for name in pc.ALLOWED_INPUTS:
            self.assertIsNone(pc.forbidden_hit(name, pc.FORBIDDEN_TOKENS), name)
        self.assertEqual(messages(mutated(lambda d: rule(d, "ease_after_fails")["when"].append(
            {"input": "skill_rating", "op": ">", "value": 1200}))), [])
        for name in pc.ALLOWED_ACTIONS:
            self.assertIsNone(pc.forbidden_hit(name, pc.FORBIDDEN_TOKENS + pc.FORBIDDEN_ACTIONS), name)

    def test_forbidden_input_fails(self) -> None:
        p = mutated(lambda d: rule(d, "ease_after_fails")["when"].append({"input": "spend_last_7d", "op": ">=", "value": 1}))
        self.assertFailsWith(p, "input 'spend_last_7d' is forbidden (contains 'spend')")

    def test_separator_and_case_variants_are_caught(self) -> None:
        for name, token in (("adValue", "ad_value"), ("AD-VALUE", "ad_value"), ("Ad Value", "ad_value"),
                            ("ad.value", "ad_value"), ("payer_flag", "payer"), ("PAYER-FLAG", "payer"),
                            ("device-Model", "device_model"), ("user_country_code", "country")):
            p = mutated(lambda d, n=name: rule(d, "ease_after_fails")["when"].append({"input": n, "op": ">=", "value": 1}))
            self.assertFailsWith(p, f"input '{name}' is forbidden (contains '{token}')")

    def test_unknown_input_fails_and_matching_is_exact(self) -> None:
        for name in ("mystery_signal", "Fail_Streak", "fail-streak"):
            p = mutated(lambda d, n=name: rule(d, "ease_after_fails")["when"].append({"input": n, "op": ">=", "value": 1}))
            self.assertFailsWith(p, f"input '{name}' is not an allowed play signal")

    def test_bad_operator_and_value_fail(self) -> None:
        p = mutated(lambda d: rule(d, "ease_after_fails")["when"].append({"input": "fail_streak", "op": "=>", "value": "3"}))
        self.assertFailsWith(p, "operator '=>'", "must be a number")

    def test_rule_on_shared_mode_fails(self) -> None:
        p = mutated(lambda d: rule(d, "ease_after_fails")["modes"].append("daily"))
        self.assertFailsWith(p, "rule ease_after_fails: names shared mode 'daily'")

    def test_rule_with_no_modes_or_undeclared_mode_fails(self) -> None:
        self.assertFailsWith(mutated(lambda d: rule(d, "offer_hint_when_stuck").update(modes=[])), "names no modes")
        self.assertFailsWith(mutated(lambda d: rule(d, "offer_hint_when_stuck").update(modes=["ghost"])),
                             "mode 'ghost' that is not declared")
        self.assertFailsWith(mutated(lambda d: d.update(modes=[])), "no modes declared")

    def test_suggest_mode_must_name_a_non_shared_mode(self) -> None:
        def make(target: str):
            return lambda d: rule(d, "offer_hint_when_stuck").update(then={"action": "suggest_mode", "mode": target})
        self.assertEqual(messages(mutated(make("practice"))), [])
        self.assertFailsWith(mutated(make("daily")), "suggest_mode names shared mode 'daily'")
        self.assertFailsWith(mutated(make("ghost")), "suggest_mode needs a mode")

    def test_forbidden_and_unknown_actions_fail(self) -> None:
        for action, token in (("force_loss", "force_loss"), ("Force-Loss", "force_loss"), ("RIG", "rig"),
                              ("scoreBonus", "score_bonus"), ("harvest_data", "harvest")):
            p = mutated(lambda d, a=action: rule(d, "offer_hint_when_stuck").update(then={"action": a}))
            self.assertFailsWith(p, f"action '{action}' is forbidden (contains '{token}')")
        p = mutated(lambda d: rule(d, "offer_hint_when_stuck").update(then={"action": "send_push"}))
        self.assertFailsWith(p, "action 'send_push' is not an allowed action")

    def test_offset_outside_range_fails(self) -> None:
        p = mutated(lambda d: rule(d, "raise_after_fast_solves").update(then={"action": "difficulty_offset", "value": 2}))
        self.assertFailsWith(p, "value 2 is outside minOffset -1 to maxOffset 1")
        p = mutated(lambda d: rule(d, "ease_after_fails").update(then={"action": "difficulty_offset", "value": -2}))
        self.assertFailsWith(p, "value -2 is outside")

    def test_offsets_wider_than_two_steps_fail(self) -> None:
        p = mutated(lambda d: d["difficulty"].update(minOffset=-3, maxOffset=3))
        self.assertFailsWith(p, "minOffset -3 is wider than 2 steps", "maxOffset 3 is wider than 2 steps")
        self.assertEqual(messages(mutated(lambda d: d["difficulty"].update(minOffset=-2, maxOffset=2))), [])

    def test_two_easing_rules_without_cap_fail(self) -> None:
        extra = {"id": "ease_on_restarts", "modes": ["levels"],
                 "when": [{"input": "restarts_recent", "op": ">=", "value": 3}],
                 "then": {"action": "difficulty_offset", "value": -1}, "reason": "restarting",
                 "explainKey": "pxe.reason.restarting"}
        p = mutated(lambda d: d["rules"].append(dict(extra)))
        self.assertFailsWith(p, "rule ease_on_restarts: easing rule without maxPerSession 1")
        p = mutated(lambda d: d["rules"].append(dict(extra, maxPerSession=2)))
        self.assertFailsWith(p, "rule ease_on_restarts: easing rule without maxPerSession 1")
        p = mutated(lambda d: d["rules"].append(dict(extra, maxPerSession=1)))
        self.assertEqual(messages(p), [])

    def test_two_easing_rules_without_cap_name_both_rules(self) -> None:
        def uncap(d: dict) -> None:
            del rule(d, "ease_after_fails")["maxPerSession"]
            d["rules"].append({"id": "second_ease", "modes": ["levels"],
                               "when": [{"input": "quit_rate_recent", "op": ">", "value": 0.5}],
                               "then": {"action": "difficulty_offset", "value": -1}, "reason": "quitting",
                               "explainKey": "pxe.reason.quitting"})
        found = messages(mutated(uncap))
        self.assertTrue(any("rule ease_after_fails: easing rule without" in m for m in found), found)
        self.assertTrue(any("rule second_ease: easing rule without" in m for m in found), found)

    def test_missing_reason_or_explain_key_fails(self) -> None:
        p = mutated(lambda d: rule(d, "offer_hint_when_stuck").pop("reason"))
        self.assertFailsWith(p, "rule offer_hint_when_stuck: no reason")
        p = mutated(lambda d: rule(d, "offer_hint_when_stuck").update(explainKey=" "))
        self.assertFailsWith(p, "rule offer_hint_when_stuck: no explainKey")

    def test_player_block_requirements(self) -> None:
        self.assertFailsWith(mutated(lambda d: d["player"].update(settings=["easy", "hard"])), "settings must include auto")
        self.assertFailsWith(mutated(lambda d: d["player"].update(settings=["auto"])), "at least one fixed level")
        for key in ("explain", "log", "reset"):
            self.assertFailsWith(mutated(lambda d, k=key: d["player"].update({k: False})), f"{key} must be true")

    def test_score_integrity(self) -> None:
        self.assertFailsWith(mutated(lambda d: d["scores"].update(modifyAfterFact=True)), "modifyAfterFact is true")
        self.assertFailsWith(mutated(lambda d: d["scores"].update(assistedRunsOnSharedBoards=True)),
                             "assisted runs are allowed on shared boards")

    def test_holdout_bounds(self) -> None:
        for bad in (0, 0.5, 21, 50, "5"):
            self.assertFailsWith(mutated(lambda d, b=bad: d["experiment"].update(holdoutPercent=b)), "holdoutPercent")
        for good in (1, 5, 20):
            self.assertEqual(messages(mutated(lambda d, g=good: d["experiment"].update(holdoutPercent=g))), [])
        self.assertFailsWith(mutated(lambda d: d["experiment"].update(primary=[])), "no primary metric")

    def test_engine_parity_rules(self):
        self.assertFailsWith(mutated(lambda d: d["experiment"].update(holdoutPercent=2.5)), "whole number")
        self.assertFailsWith(mutated(lambda d: d["returnReasons"][0].update(quietHours=["9pm", "9am"])), "quietHours must be two")
        self.assertFailsWith(mutated(lambda d: d.pop("difficulty")), "missing section 'difficulty'")
        self.assertFailsWith(mutated(lambda d: d.pop("returnReasons")), "missing section 'returnReasons'")

    def test_holdout_salt_required(self):
        self.assertFailsWith(mutated(lambda d: d["experiment"].pop("holdoutSalt")), "holdoutSalt is missing")
        self.assertFailsWith(mutated(lambda d: d["experiment"].update(holdoutSalt="  ")), "holdoutSalt is missing")

    def test_minors_need_the_strict_tier(self) -> None:
        self.assertFailsWith(mutated(lambda d: d["audience"].update(minimumAge=13, minorsTier="lenient")),
                             "minimumAge 13 includes minors and minorsTier is 'lenient'")
        self.assertEqual(messages(mutated(lambda d: d["audience"].update(minimumAge=18, minorsTier="lenient"))), [])

    def test_strict_tier_blocks_streak_and_loss_return_reasons(self) -> None:
        for source in ("streak", "loss", "Streak"):
            p = mutated(lambda d, s=source: d["returnReasons"][0].update(id="rr", source=s))
            self.assertFailsWith(p, f"returnReason rr: source '{source}' is not allowed in the strict tier")
        # An adult only audience on a lenient tier may use them.
        p = mutated(lambda d: (d["audience"].update(minimumAge=18, minorsTier="lenient"),
                               d["returnReasons"][0].update(source="streak")))
        self.assertEqual(messages(p), [])

    def test_return_reason_needs_cap_and_quiet_hours(self) -> None:
        p = mutated(lambda d: d["returnReasons"][0].pop("maxPerDay"))
        self.assertFailsWith(p, "returnReason daily_ready: no maxPerDay")
        p = mutated(lambda d: d["returnReasons"][0].pop("quietHours"))
        self.assertFailsWith(p, "returnReason daily_ready: no quietHours")

    def test_read_after_days_warns_below_28(self) -> None:
        p = mutated(lambda d: d["experiment"].update(readAfterDays=27))
        self.assertEqual(messages(p), [])
        self.assertTrue(any("readAfterDays 27 is under 28" in m for m in messages(p, "WARN")))
        self.assertEqual(messages(mutated(lambda d: d["experiment"].update(readAfterDays=28)), "WARN"), [])

    def test_only_easing_rules_warn(self) -> None:
        p = mutated(lambda d: d["rules"].remove(rule(d, "raise_after_fast_solves")))
        self.assertEqual(messages(p), [])
        self.assertTrue(any("none raises difficulty" in m for m in messages(p, "WARN")))

    def test_missing_section_fails(self) -> None:
        self.assertFailsWith(mutated(lambda d: d.pop("scores")), "missing section 'scores'", "scores block is missing")

    def test_cli_exit_codes_and_last_line(self) -> None:
        ok = run_script(CHECKER, str(SAMPLES / "policy-valid.json"))
        self.assertEqual(ok.returncode, 0, ok.stdout)
        self.assertIn("Verdict: PASS", ok.stdout)
        bad = run_script(CHECKER, str(SAMPLES / "policy-bad.json"))
        self.assertEqual(bad.returncode, 1, bad.stdout)
        self.assertIn("Verdict: FAIL", bad.stdout)
        for needle in ("FAIL rule ease_for_big_spenders", "FAIL rule daily_adapts: names shared mode 'daily'",
                       "FAIL rule make_them_lose: action 'force_loss'", "FAIL scores: modifyAfterFact is true",
                       "FAIL experiment: holdoutPercent 0", "FAIL audience: minimumAge 13",
                       "FAIL returnReason keep_your_streak"):
            self.assertIn(needle, bad.stdout)
        for res in (ok, bad):
            self.assertTrue(res.stdout.strip().splitlines()[-1].startswith("This check cannot cover:"))

    def test_cli_json_output_shape(self) -> None:
        res = run_script(CHECKER, str(SAMPLES / "policy-bad.json"), "--json")
        self.assertEqual(res.returncode, 1)
        doc = json.loads(res.stdout)
        self.assertEqual(doc["verdict"], "FAIL")
        self.assertEqual(doc["fails"], sum(1 for f in doc["findings"] if f["severity"] == "FAIL"))
        self.assertTrue(set(doc["findings"][0]) >= {"severity", "scope", "message"})
        self.assertTrue(doc["cannotCover"].startswith("This check cannot cover:"))
        self.assertTrue(res.stderr.strip().splitlines()[-1].startswith("This check cannot cover:"))

    def test_unsupported_version_and_unreadable_input_exit_2(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            future = Path(tmp) / "future.json"
            future.write_text(json.dumps(dict(VALID, pxeVersion="0.2")), encoding="utf-8")
            res = run_script(CHECKER, str(future))
            self.assertEqual(res.returncode, 2)
            self.assertIn("pxeVersion 0.2 is not supported", res.stdout)
            self.assertTrue(res.stdout.strip().splitlines()[-1].startswith("This check cannot cover:"))
            missing_version = Path(tmp) / "noversion.json"
            missing_version.write_text(json.dumps({k: v for k, v in VALID.items() if k != "pxeVersion"}), encoding="utf-8")
            self.assertEqual(run_script(CHECKER, str(missing_version)).returncode, 2)
            broken = Path(tmp) / "broken.json"
            broken.write_text("{not json", encoding="utf-8")
            self.assertEqual(run_script(CHECKER, str(broken)).returncode, 2)
            self.assertEqual(run_script(CHECKER, str(Path(tmp) / "absent.json")).returncode, 2)


def load_table(*extra: str) -> dict:
    res = run_script(TABLE, str(SAMPLES / "events.csv"), "--json", *extra)
    assert res.returncode == 0, res.stdout + res.stderr
    return json.loads(res.stdout)


def by_level(doc: dict) -> dict:
    return {r["level"]: r for r in doc["levels"]}


class DifficultyTableTests(unittest.TestCase):
    def test_spike_is_flagged_at_level_7_and_labeled_hard(self) -> None:
        lv = by_level(load_table())
        self.assertIn("spike", lv[7]["flags"])
        self.assertEqual(lv[7]["label"], "hard")
        self.assertEqual([r["level"] for r in lv.values() if "spike" in r["flags"]], [7])

    def test_wall_is_flagged_at_level_10(self) -> None:
        doc = load_table()
        lv = by_level(doc)
        self.assertIn("wall", lv[10]["flags"])
        self.assertEqual([r["level"] for r in lv.values() if "wall" in r["flags"]], [10])
        self.assertGreaterEqual(lv[10]["quit_at_level_rate"], 2 * doc["median_quit_at_level_rate"])

    def test_insufficient_data_label_and_threshold_option(self) -> None:
        lv = by_level(load_table())
        self.assertEqual(lv[11]["label"], "insufficient data")
        self.assertEqual(lv[12]["label"], "insufficient data")
        self.assertEqual(lv[11]["flags"], [])
        lv = by_level(load_table("--min-attempts", "1"))
        self.assertNotEqual(lv[11]["label"], "insufficient data")

    def test_elo_orders_hard_levels_above_easy_ones(self) -> None:
        lv = by_level(load_table())
        self.assertGreater(lv[7]["elo"], lv[1]["elo"])
        self.assertGreater(lv[7]["elo"], lv[6]["elo"])
        self.assertGreater(lv[10]["elo"], lv[9]["elo"])
        self.assertEqual(max(lv.values(), key=lambda r: r["elo"])["level"], 7)

    def test_json_output_shape(self) -> None:
        doc = load_table()
        self.assertTrue({"settings", "events", "players", "levels", "flags", "sawtooth", "cannotCover"} <= set(doc))
        self.assertEqual(doc["players"], 40)
        self.assertEqual(len(doc["levels"]), 12)
        self.assertTrue({"level", "attempts", "players", "pass_rate", "first_try_pass_rate", "median_attempts_to_pass",
                         "quit_at_level_rate", "elo", "label", "flags"} <= set(doc["levels"][0]))
        self.assertEqual(doc["sawtooth"]["hard_levels"], [7, 10])
        self.assertEqual(doc["sawtooth"]["spacing"], [3])
        self.assertAlmostEqual(doc["sawtooth"]["hard_share"], 0.2)
        self.assertTrue(doc["cannotCover"].startswith("This check cannot cover:"))

    def test_text_output_and_out_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "table.txt"
            res = run_script(TABLE, str(SAMPLES / "events.csv"), "--out", str(out))
            self.assertEqual(res.returncode, 0, res.stdout)
            lines = res.stdout.strip().splitlines()
            self.assertTrue(lines[-1].startswith("This check cannot cover:"))
            self.assertTrue(any(l.startswith("FLAG spike level 7") for l in lines))
            self.assertTrue(any(l.startswith("FLAG wall level 10") for l in lines))
            self.assertEqual(out.read_text(encoding="utf-8").strip(), res.stdout.strip())

    def write_csv(self, tmp: str, text: str) -> str:
        path = Path(tmp) / "events.csv"
        path.write_text(text, encoding="utf-8")
        return str(path)

    def test_hand_computed_metrics(self) -> None:
        csv_text = ("player_id,level,result,ts\n"
                    "A,1,fail,1\nA,1,fail,2\nA,1,win,3\nB,1,win,4\nC,1,fail,5\nC,1,quit,6\nA,2,fail,7\n")
        with tempfile.TemporaryDirectory() as tmp:
            res = run_script(TABLE, self.write_csv(tmp, csv_text), "--json", "--min-attempts", "1")
            self.assertEqual(res.returncode, 0, res.stdout)
            lv = by_level(json.loads(res.stdout))
        one = lv[1]
        self.assertEqual((one["attempts"], one["players"], one["wins"]), (6, 3, 2))
        self.assertAlmostEqual(one["pass_rate"], 2 / 6, places=3)
        self.assertAlmostEqual(one["first_try_pass_rate"], 1 / 3, places=3)
        self.assertEqual(one["median_attempts_to_pass"], 2)
        self.assertAlmostEqual(one["quit_at_level_rate"], 1 / 3, places=3)
        self.assertEqual((lv[2]["attempts"], lv[2]["quit_at_level_rate"], lv[2]["median_attempts_to_pass"]), (1, 1.0, None))

    def test_attempts_before_overrides_derived_first_try(self) -> None:
        csv_text = "player_id,level,result,attempts_before\nA,1,win,3\nB,1,win,0\n"
        with tempfile.TemporaryDirectory() as tmp:
            res = run_script(TABLE, self.write_csv(tmp, csv_text), "--json", "--min-attempts", "1")
            row = by_level(json.loads(res.stdout))[1]
        self.assertEqual(row["first_try_pass_rate"], 1.0)
        self.assertEqual(row["median_attempts_to_pass"], 2.5)

    def test_elo_single_win_moves_level_by_four_points(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            res = run_script(TABLE, self.write_csv(tmp, "player_id,level,result\nA,1,win\n"), "--json")
            self.assertEqual(by_level(json.loads(res.stdout))[1]["elo"], 1496.0)
            res = run_script(TABLE, self.write_csv(tmp, "player_id,level,result\nA,1,fail\n"), "--json")
            self.assertEqual(by_level(json.loads(res.stdout))[1]["elo"], 1504.0)

    def test_ts_orders_the_replay(self) -> None:
        late_first = "player_id,level,result,ts\nA,1,win,2026-09-01T10:00:05Z\nA,2,fail,2026-09-01T10:00:01Z\n"
        with tempfile.TemporaryDirectory() as tmp:
            res = run_script(TABLE, self.write_csv(tmp, late_first), "--json", "--min-attempts", "1")
            lv = by_level(json.loads(res.stdout))
        # The player's last event by time is the win on level 1, so nothing counts as a stop at level 2.
        self.assertEqual(lv[2]["quit_at_level_rate"], 0.0)
        self.assertEqual(lv[1]["quit_at_level_rate"], 0.0)

    def test_missing_column_and_bad_values_exit_2(self) -> None:
        cases = {
            "player_id,level\nA,1\n": "missing column result",
            "player_id,level,result\nA,1,draw\n": "result must be win, fail or quit",
            "player_id,level,result\nA,one,win\n": "column level",
            "player_id,level,result\n,1,win\n": "player_id is empty",
            "player_id,level,result,ts\nA,1,win,\n": "ts is empty",
            "player_id,level,result,ts\nA,1,win,yesterday\n": "ts is neither",
            "player_id,level,result\n": "no data rows",
        }
        with tempfile.TemporaryDirectory() as tmp:
            for text, needle in cases.items():
                res = run_script(TABLE, self.write_csv(tmp, text))
                self.assertEqual(res.returncode, 2, text)
                self.assertIn(needle, res.stdout)
                self.assertTrue(res.stdout.strip().splitlines()[-1].startswith("This check cannot cover:"))
            self.assertEqual(run_script(TABLE, str(Path(tmp) / "absent.csv")).returncode, 2)
            ok = self.write_csv(tmp, "player_id,level,result\nA,1,win\n")
            self.assertEqual(run_script(TABLE, ok, "--hard", "0.2", "--super-hard", "0.4").returncode, 2)
            self.assertEqual(run_script(TABLE, ok, "--min-attempts", "0").returncode, 2)

    def test_flags_do_not_change_the_exit_code(self) -> None:
        res = run_script(TABLE, str(SAMPLES / "events.csv"))
        self.assertEqual(res.returncode, 0)
        self.assertIn("[spike]", res.stdout)

    def test_super_hard_threshold(self) -> None:
        lv = by_level(load_table("--super-hard", "0.28", "--hard", "0.45"))
        self.assertEqual(lv[7]["label"], "super hard")
        self.assertEqual(lv[10]["label"], "hard")


if __name__ == "__main__":
    unittest.main()
