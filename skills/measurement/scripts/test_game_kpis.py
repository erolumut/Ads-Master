#!/usr/bin/env python3
"""Tests for game_kpis.py against a hand computed golden fixture.
Run: python3 -m unittest discover -s skills/measurement/scripts -p "test_game_kpis.py"
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(HERE, "samples", "game_events.csv")
GOLDEN = os.path.join(HERE, "samples", "game_events_expected.json")
sys.path.insert(0, HERE)
import game_kpis  # noqa: E402


def run(*args):
    """Run the script; return (exit code, stdout, parsed JSON or None)."""
    tmp = tempfile.mkdtemp()
    try:
        out = os.path.join(tmp, "out.json")
        p = subprocess.run([sys.executable, "-I", os.path.join(HERE, "game_kpis.py"), *args, "--json", out],
                           capture_output=True, text=True, timeout=60)
        data = None
        if os.path.exists(out):
            with open(out, encoding="utf-8") as fh:
                data = json.load(fh)
        return p.returncode, p.stdout, data
    finally:
        shutil.rmtree(tmp)


def write(tmp, name, text):
    path = os.path.join(tmp, name)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    return path


BASE = (SAMPLE, "--as-of", "2026-10-10", "--min-cohort", "5")


class GoldenTest(unittest.TestCase):
    def test_matches_hand_computed_golden_exactly(self):
        with open(GOLDEN, encoding="utf-8") as fh:
            expected = json.load(fh)
        expected.pop("_how_computed")
        code, stdout, data = run(*BASE, "--timezone", "UTC")
        self.assertEqual(code, 0, stdout)
        self.assertEqual(data, expected)

    def test_last_line_says_what_it_cannot_cover(self):
        code, stdout, _ = run(*BASE)
        last = [line for line in stdout.splitlines() if line.strip()][-1]
        self.assertTrue(last.startswith("This check cannot cover:"), last)

    def test_pooled_rate_is_ratio_of_sums_not_mean_of_rates(self):
        _, _, data = run(*BASE)
        rates = [c["d1"]["rate"] for c in data["retention"]["cohorts"] if c["d1"]]
        self.assertAlmostEqual(sum(rates) / len(rates), 0.65)
        self.assertEqual(data["retention"]["pooled"]["d1"]["rate"], 0.636364)

    def test_wilson(self):
        self.assertEqual(game_kpis.wilson(7, 11), [0.3538, 0.8483])
        self.assertEqual(game_kpis.wilson(2, 6), [0.0968, 0.7])
        self.assertIsNone(game_kpis.wilson(0, 0))


class DefinitionTrapsTest(unittest.TestCase):
    def test_timezone_moves_a_midnight_install(self):
        # u09 plays 22:30 UTC on 09-30 and 20:00 UTC on 10-01: two calendar days in UTC, one day in +03:00.
        code, _, data = run(*BASE, "--timezone", "+03:00")
        self.assertEqual(code, 0)
        cohorts = {c["install_date"]: c for c in data["retention"]["cohorts"]}
        self.assertNotIn("2026-09-30", cohorts)
        self.assertEqual(cohorts["2026-10-01"]["size"], 3)
        self.assertEqual(cohorts["2026-10-01"]["d1"], {"retained": 1, "rate": 0.333333})
        pooled = data["retention"]["pooled"]
        self.assertEqual((pooled["d1"]["retained"], pooled["d1"]["cohort_users"]), (6, 11))
        self.assertEqual((pooled["d7"]["retained"], pooled["d7"]["cohort_users"]), (5, 9))
        self.assertEqual(pooled["d1"]["ci95"], [0.2801, 0.7873])
        self.assertEqual(data["activity"]["avg_dau_30d"], 0.633333)

    def test_iana_zone_equals_fixed_offset(self):
        try:
            from zoneinfo import ZoneInfo
            ZoneInfo("Europe/Istanbul")
        except Exception:
            self.skipTest("tz database not installed")
        _, _, a = run(*BASE, "--timezone", "+03:00")
        _, _, b = run(*BASE, "--timezone", "Europe/Istanbul")
        a.pop("timezone"), b.pop("timezone")
        self.assertEqual(a, b)

    def test_server_events_do_not_make_a_player_active(self):
        # Counting the refund notification as play would retain u10 on day 1.
        _, _, data = run(*BASE, "--non-activity-events", "")
        self.assertEqual(data["retention"]["pooled"]["d1"]["retained"], 8)
        self.assertEqual(data["activity"]["dau"], 5)
        self.assertEqual(data["input"]["non_activity_rows"], 0)

    def test_default_as_of_skips_the_partial_last_day(self):
        _, _, data = run(SAMPLE, "--min-cohort", "5")
        self.assertEqual(data["as_of"], "2026-10-10")
        self.assertTrue(data["as_of_source"].startswith("default"))

    def test_short_history_does_not_dilute_average_dau(self):
        # The file starts 2026-09-01; an as-of of 2026-09-05 observes 5 days, not 30.
        # Activity: 09-01 u01 u02 u03 u04; 09-02 u01 u02 u04; 09-05 u05 u06 -> 9 player days / 5 days.
        _, stdout, data = run(SAMPLE, "--as-of", "2026-09-05", "--min-cohort", "1")
        self.assertEqual(data["activity"]["days_observed_30d"], 5)
        self.assertEqual(data["activity"]["avg_dau_30d"], 1.8)
        self.assertEqual(data["activity"]["mau"], 6)
        self.assertEqual(data["activity"]["stickiness"], 0.3)
        self.assertIn("Only 5 of the 30 days", stdout)

    def test_cohorts_from_drops_older_installs(self):
        _, _, data = run(*BASE, "--cohorts-from", "2026-09-30")
        pooled = data["retention"]["pooled"]
        self.assertIsNone(pooled["d30"])
        self.assertEqual((pooled["d1"]["retained"], pooled["d1"]["cohort_users"]), (3, 5))

    def test_non_integer_levels_disable_churn_only(self):
        tmp = tempfile.mkdtemp()
        try:
            with open(SAMPLE, encoding="utf-8") as fh:
                text = fh.read().replace("u03,2026-09-01T10:05:00Z,level_failed,,,1,,", "u03,2026-09-01T10:05:00Z,level_failed,,,w1-l1,,")
            path = write(tmp, "events.csv", text)
            code, _, data = run(path, "--as-of", "2026-10-10", "--min-cohort", "5")
            self.assertEqual(code, 0)
            self.assertFalse(data["churn_by_level"]["computed"])
            self.assertEqual(data["retention"]["pooled"]["d1"]["retained"], 7)
        finally:
            shutil.rmtree(tmp)

    def test_game_filter(self):
        tmp = tempfile.mkdtemp()
        try:
            path = write(tmp, "multi.csv", "user_id,ts,event,game\n"
                         "a1,2026-10-01T10:00:00Z,level_started,game_a\n"
                         "a1,2026-10-02T10:00:00Z,level_started,game_a\n"
                         "a1,2026-10-01T11:00:00Z,level_started,game_b\n"
                         "b1,2026-10-02T10:00:00Z,level_started,game_b\n")
            code, _, data = run(path, "--as-of", "2026-10-02", "--min-cohort", "1", "--game", "game_a")
            self.assertEqual(code, 0)
            self.assertEqual(data["input"]["users"], 1)
            self.assertEqual(data["retention"]["pooled"]["d1"]["rate"], 1.0)
            code, _, data = run(path, "--as-of", "2026-10-02", "--min-cohort", "1", "--game", "game_b")
            self.assertEqual(data["retention"]["pooled"]["d1"]["rate"], 0.0)
        finally:
            shutil.rmtree(tmp)


class GatesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def gates(self, obj):
        return write(self.tmp, "gates.json", json.dumps(obj))

    def test_all_pass(self):
        code, stdout, data = run(*BASE, "--gates", self.gates({"d1": 0.40, "D7": 0.20, "d30": 0.05}))
        self.assertEqual(code, 0, stdout)
        self.assertEqual(data["verdict"], "PASS")
        by = {g["metric"]: g for g in data["gates"]}
        self.assertTrue(by["d1"]["threshold_inside_ci95"])     # 0.40 sits inside 0.3538 to 0.8483: fragile
        self.assertFalse(by["d30"]["threshold_inside_ci95"])

    def test_fail(self):
        code, _, data = run(*BASE, "--gates", self.gates({"d1": 0.70}))
        self.assertEqual(code, 1)
        self.assertEqual(data["gates"][0]["status"], "FAIL")

    def test_small_cohort_cannot_be_judged(self):
        code, _, data = run(SAMPLE, "--as-of", "2026-10-10", "--min-cohort", "10",
                            "--gates", self.gates({"d1": 0.40, "d7": 0.20}))
        self.assertEqual(code, 2)
        self.assertEqual(data["verdict"], "CANNOT JUDGE")
        by = {g["metric"]: g["status"] for g in data["gates"]}
        self.assertEqual(by, {"d1": "PASS", "d7": "CANNOT JUDGE"})

    def test_fail_outranks_cannot_judge(self):
        code, _, data = run(SAMPLE, "--as-of", "2026-10-10", "--min-cohort", "10",
                            "--gates", self.gates({"d1": 0.70, "d7": 0.20}))
        self.assertEqual(code, 1)
        self.assertEqual(data["verdict"], "FAIL")

    def test_default_min_cohort_refuses_a_tiny_soft_launch(self):
        code, _, data = run(SAMPLE, "--as-of", "2026-10-10", "--gates", self.gates({"d1": 0.30}))
        self.assertEqual(code, 2)
        self.assertEqual(data["gates"][0]["status"], "CANNOT JUDGE")

    def test_bad_gates_could_not_run(self):
        for bad in ({"d1": 35}, {"d14": 0.1}, {"d1": "0.3"}, []):
            code, stdout, _ = run(*BASE, "--gates", self.gates(bad))
            self.assertEqual(code, 2, (bad, stdout))
            self.assertIn("COULD NOT RUN", stdout)


class BadInputTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def assert_cannot_run(self, text, *extra):
        path = write(self.tmp, "e.csv", text)
        code, stdout, _ = run(path, "--as-of", "2026-10-02", *extra)
        self.assertEqual(code, 2, stdout)
        self.assertIn("COULD NOT RUN", stdout)
        self.assertTrue(stdout.strip().splitlines()[-1].startswith("This check cannot cover:"))

    def test_missing_column(self):
        self.assert_cannot_run("user_id,event\na,level_started\n")

    def test_bad_timestamp(self):
        self.assert_cannot_run("user_id,ts,event\na,yesterday,level_started\n")

    def test_revenue_without_type(self):
        self.assert_cannot_run("user_id,ts,event,revenue\na,2026-10-01T10:00:00Z,purchase_completed,4.99\n")

    def test_two_currencies(self):
        self.assert_cannot_run("user_id,ts,event,revenue,revenue_type,currency\n"
                               "a,2026-10-01T10:00:00Z,purchase_completed,4.99,iap,EUR\n"
                               "b,2026-10-01T11:00:00Z,purchase_completed,4.99,iap,USD\n")

    def test_unknown_timezone(self):
        self.assert_cannot_run("user_id,ts,event\na,2026-10-01T10:00:00Z,level_started\n", "--timezone", "Mars/Olympus")

    def test_game_filter_without_column(self):
        self.assert_cannot_run("user_id,ts,event\na,2026-10-01T10:00:00Z,level_started\n", "--game", "game_a")

    def test_naive_timestamps_are_flagged(self):
        path = write(self.tmp, "n.csv", "user_id,ts,event\na,2026-10-01T10:00:00,level_started\n"
                                        "a,2026-10-02T10:00:00,level_started\n")
        code, stdout, data = run(path, "--as-of", "2026-10-02", "--min-cohort", "1")
        self.assertEqual(code, 0)
        self.assertEqual(data["input"]["naive_timestamps"], 2)
        self.assertIn("read as UTC", stdout)


if __name__ == "__main__":
    unittest.main()
