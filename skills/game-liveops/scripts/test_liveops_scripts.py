#!/usr/bin/env python3
"""Tests for liveops_calendar_check.py and level_flags.py (standard library unittest).

Run: python3 -I -m unittest discover -s skills/game-liveops/scripts -p "test_*.py"
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import os
import re
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLES = os.path.join(HERE, "samples")
REFERENCE = os.path.join(os.path.dirname(HERE), "references", "liveops-calendar-and-store-events.md")


def load_module(name: str):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cal = load_module("liveops_calendar_check")
lvl = load_module("level_flags")

HEADER = ("| ID | Name | Format | Scale | Start | End | Audience | Ranked board | Store | Badge | Promo start | "
          "Submit by | Deep link | Reminders | Offer ref | Holdout | KPI | Owner | Status |\n"
          "|----|------|--------|-------|-------|-----|----------|--------------|-------|-------|-------------|"
          "-----------|-----------|-----------|-----------|---------|-----|-------|--------|\n")
META_HEADER = ("| ID | Event name | Short description | Long description | Purpose | Priority |\n"
               "|----|------------|-------------------|------------------|---------|----------|\n")


def row(rid="LO-1", name="Autumn Season", fmt="season", scale="season", start="2026-11-02", end="2026-11-22",
        board="group_season (group)", store="apple", badge="New Season", promo="2026-10-26", submit="2026-10-16",
        link="https://example.com/s", holdout="10%", kpi="Season completion", owner="game-liveops",
        status="planned") -> str:
    return (f"| {rid} | {name} | {fmt} | {scale} | {start} | {end} | all | {board} | {store} | {badge} | {promo} | "
            f"{submit} | {link} | none | none | {holdout} | {kpi} | {owner} | {status} |\n")


def meta(rid="LO-1", name="Autumn Season", short="A new season with your group",
         long_="Three weeks of daily rounds for everyone.", purpose="active users", priority="normal") -> str:
    return f"| {rid} | {name} | {short} | {long_} | {purpose} | {priority} |\n"


class CalendarCase(unittest.TestCase):
    def run_cal(self, body: str, *extra: str, suffix: str = ".md") -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "LIVEOPS_CALENDAR" + suffix)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(body)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = cal.main([path, *extra])
        return code, out.getvalue()

    def calendar(self, rows: str, metas: str = "") -> str:
        text = "# Liveops Calendar\n\n## Calendar\n\n" + HEADER + rows
        if metas:
            text += "\n## Store event metadata\n\n" + META_HEADER + metas
        return text


class TestCalendarCheck(CalendarCase):
    def test_sample_passes(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = cal.main([os.path.join(SAMPLES, "LIVEOPS_CALENDAR.sample.md")])
        self.assertEqual(code, 0, out.getvalue())
        self.assertIn("This check cannot cover:", out.getvalue().strip().splitlines()[-1])

    def test_reference_template_passes(self):
        with open(REFERENCE, encoding="utf-8") as fh:
            text = fh.read()
        section = text.split("## 9. LIVEOPS_CALENDAR template", 1)[1]
        block = re.search(r"```markdown\n(.*?)\n```", section, re.S)
        self.assertIsNotNone(block, "template block not found in the reference")
        code, out = self.run_cal(block.group(1))
        self.assertEqual(code, 0, out)

    def test_clean_apple_season(self):
        code, out = self.run_cal(self.calendar(row(), meta()))
        self.assertEqual(code, 0, out)
        self.assertFalse([l for l in out.splitlines() if l.startswith(("FAIL ", "WARN "))], out)

    def test_end_date_is_inclusive_31_days_ok(self):
        code, out = self.run_cal(self.calendar(row(start="2026-11-01", end="2026-12-01", promo="2026-10-25"), meta()))
        self.assertEqual(code, 0, out)

    def test_apple_duration_over_31_days_fails(self):
        code, out = self.run_cal(self.calendar(row(start="2026-11-01", end="2026-12-02", promo="2026-10-25"), meta()))
        self.assertEqual(code, 1)
        self.assertIn("maximum is 31", out)

    def test_promo_more_than_14_days_ahead_fails(self):
        code, out = self.run_cal(self.calendar(row(promo="2026-10-18", submit="2026-10-10"), meta()))
        self.assertEqual(code, 1)
        self.assertIn("more than 14 days", out)

    def test_submit_after_promo_fails(self):
        code, out = self.run_cal(self.calendar(row(submit="2026-10-28"), meta()))
        self.assertEqual(code, 1)
        self.assertIn("approval cannot land", out)

    def test_missing_badge_and_deep_link_fail(self):
        code, out = self.run_cal(self.calendar(row(badge="", link="none"), meta()))
        self.assertEqual(code, 1)
        self.assertIn("needs a Badge", out)
        self.assertIn("needs a deep link", out)

    def test_price_in_metadata_fails(self):
        code, out = self.run_cal(self.calendar(row(), meta(short="Season pass now $4.99")))
        self.assertEqual(code, 1)
        self.assertIn("specific pricing", out)
        code, out = self.run_cal(self.calendar(row(), meta(long_="Save 50% off the pass this week.")))
        self.assertEqual(code, 1)
        code, out = self.run_cal(self.calendar(row(), meta(long_="Only 49 TL for the season.")))
        self.assertEqual(code, 1)

    def test_tries_wording_is_not_a_price(self):
        code, out = self.run_cal(self.calendar(row(), meta(long_="Two tries a day, 1 try left after a miss.")))
        self.assertEqual(code, 0, out)

    def test_metadata_lengths(self):
        code, out = self.run_cal(self.calendar(row(), meta(name="A Very Long Season Name For The Store")))
        self.assertEqual(code, 1)
        self.assertIn("Event name has", out)

    def test_claims_and_caps_warn(self):
        code, out = self.run_cal(self.calendar(row(), meta(short="The best puzzle game event", long_="HUGE fun!!")))
        self.assertEqual(code, 0, out)
        self.assertIn("unverifiable claims", out)
        self.assertIn("game event", out)
        self.assertIn("all capital", out)
        self.assertIn("exclamation", out)

    def test_eleven_published_apple_events_fail(self):
        rows = "".join(row(rid=f"LO-{i}", fmt="challenge", scale="none", badge="Challenge", holdout="5%")
                       for i in range(11))
        metas = "".join(meta(rid=f"LO-{i}") for i in range(11))
        code, out = self.run_cal(self.calendar(rows, metas))
        self.assertEqual(code, 1)
        self.assertIn("more than 10 events published", out)

    def test_ten_published_apple_events_pass(self):
        rows = "".join(row(rid=f"LO-{i}", fmt="challenge", scale="none", badge="Challenge", holdout="5%")
                       for i in range(10))
        metas = "".join(meta(rid=f"LO-{i}") for i in range(10))
        code, out = self.run_cal(self.calendar(rows, metas))
        self.assertEqual(code, 0, out)

    def test_duplicate_id_fails(self):
        code, out = self.run_cal(self.calendar(row() + row(scale="none", fmt="challenge", badge="Challenge"), meta()))
        self.assertEqual(code, 1)
        self.assertIn("duplicate ID", out)

    def test_same_scale_overlap_warns(self):
        rows = row(store="none") + row(rid="LO-2", start="2026-11-10", end="2026-11-30", store="none")
        code, out = self.run_cal(self.calendar(rows))
        self.assertEqual(code, 0, out)
        self.assertIn("two 'season' events overlap", out)

    def test_competitive_without_board_warns(self):
        code, out = self.run_cal(self.calendar(row(fmt="race", scale="short", board="none", store="none",
                                                   start="2026-11-02", end="2026-11-04")))
        self.assertEqual(code, 0, out)
        self.assertIn("must declare its ranked board", out)

    def test_play_late_submission_warns_not_fails(self):
        code, out = self.run_cal(self.calendar(row(store="play", submit="2026-10-31")))
        self.assertEqual(code, 0, out)
        self.assertIn("at least 4 days ahead", out)

    def test_play_too_early_submission_warns(self):
        code, out = self.run_cal(self.calendar(row(store="play", submit="2026-08-20")))
        self.assertEqual(code, 0, out)
        self.assertIn("the earliest is 60 days", out)

    def test_today_deadline_passed_fails(self):
        code, out = self.run_cal(self.calendar(row(), meta()), "--today", "2026-10-20")
        self.assertEqual(code, 1)
        self.assertIn("has passed", out)

    def test_pressure_words_warn(self):
        code, out = self.run_cal(self.calendar(row(store="none", name="Last chance season")))
        self.assertIn("pressure wording", out)

    def test_freeze_window_warns(self):
        rows = row(store="none") + row(rid="F-1", name="Release freeze", fmt="freeze", scale="none",
                                       start="2026-11-01", end="2026-11-05", store="none", kpi="")
        code, out = self.run_cal(self.calendar(rows))
        self.assertIn("inside freeze window F-1", out)

    def test_offer_not_owned_by_monetization_warns(self):
        code, out = self.run_cal(self.calendar(row(fmt="offer", scale="none", store="none")))
        self.assertIn("owned by game-monetization", out)

    def test_holdout_coverage_warns(self):
        code, out = self.run_cal(self.calendar(row(store="none", holdout="none")))
        self.assertIn("no row has a holdout", out)

    def test_csv_input(self):
        csv_text = ("ID,Name,Format,Scale,Start,End,Store,Badge,Promo start,Submit by,Deep link,Holdout,KPI,Owner,"
                    "Status\nLO-1,Autumn Season,season,season,2026-11-02,2026-11-22,apple,New Season,2026-10-26,"
                    "2026-10-16,https://example.com/s,10%,Completion,game-liveops,planned\n")
        code, out = self.run_cal(csv_text, suffix=".csv")
        self.assertEqual(code, 0, out)

    def test_missing_required_column_cannot_run(self):
        text = "## Calendar\n\n| ID | Name | Start | End |\n|----|------|-------|-----|\n| A | B | 2026-11-01 | 2026-11-02 |\n"
        code, out = self.run_cal(text)
        self.assertEqual(code, 2)
        self.assertIn("misses required columns", out)

    def test_no_table_cannot_run(self):
        code, out = self.run_cal("# Liveops Calendar\n\nNothing here.\n")
        self.assertEqual(code, 2)

    def test_missing_file_cannot_run(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = cal.main(["/nonexistent/LIVEOPS_CALENDAR.md"])
        self.assertEqual(code, 2)
        self.assertIn("This check cannot cover:", out.getvalue())

    def test_bad_date_fails(self):
        code, out = self.run_cal(self.calendar(row(start="02/11/2026", store="none")))
        self.assertEqual(code, 1)
        self.assertIn("must be YYYY-MM-DD", out)

    def test_tables_in_code_fences_are_ignored(self):
        text = "# Doc\n\n```markdown\n" + HEADER + row() + "```\n"
        code, out = self.run_cal(text)
        self.assertEqual(code, 2)


class FlagsCase(unittest.TestCase):
    def run_flags(self, csv_text: str, *extra: str) -> tuple[int, str]:
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "funnel.csv")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(csv_text)
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = lvl.main([path, *extra])
        return code, out.getvalue()

    @staticmethod
    def funnel(n=20, base=10000.0, churn=None, apc=None, quits=None, key="level", alias=False, completed=True):
        churn, apc, quits = churn or {}, apc or {}, quits or {}
        reached_col, churn_col = ("reached", "churned_here") if alias else ("players_reached", "churned")
        cols = [key, reached_col, churn_col] + (["players_completed", "attempts", "quits"] if completed else [])
        lines = [",".join(cols)]
        reached = base
        for k in range(1, n + 1):
            c = churn.get(k, 0.03)
            nxt = reached * (1 - c)
            r, ch = round(reached), round(reached * c * 0.9)
            vals = [str(k), str(r), str(ch)]
            if completed:
                comp = round(nxt)
                att = round(comp * apc.get(k, 2.0))
                vals += [str(comp), str(att), str(round(att * quits.get(k, 0.05)))]
            lines.append(",".join(vals))
            reached = nxt
        return "\n".join(lines) + "\n"


class TestLevelFlags(FlagsCase):
    def test_sample_flags(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = lvl.main([os.path.join(SAMPLES, "level_funnel.sample.csv")])
        text = out.getvalue()
        self.assertEqual(code, 1, text)
        self.assertRegex(text, r"level 14: churn_spike")
        self.assertRegex(text, r"level 22: quit_spike")
        self.assertRegex(text, r"level 30: continue_pressure")
        self.assertRegex(text, r"level 30: attempts_spike")
        self.assertRegex(text, r"level 38: frontier_wall")
        self.assertNotRegex(text, r"level 38: churn_spike")

    def test_clean_funnel_exit_0(self):
        code, out = self.run_flags(self.funnel(), "--frontier", "0")
        self.assertEqual(code, 0, out)
        self.assertIn("No flags.", out)

    def test_churn_spike_exit_1(self):
        code, out = self.run_flags(self.funnel(churn={8: 0.10}), "--frontier", "0")
        self.assertEqual(code, 1)
        self.assertIn("level 8: churn_spike", out)

    def test_small_relative_jump_below_gap_not_flagged(self):
        code, out = self.run_flags(self.funnel(churn={k: 0.002 for k in range(1, 21)} | {8: 0.006}),
                                   "--frontier", "0")
        self.assertEqual(code, 0, out)

    def test_frontier_band_turns_spike_into_wall(self):
        code, out = self.run_flags(self.funnel(churn={18: 0.10}), "--frontier", "5")
        self.assertEqual(code, 0, out)
        self.assertIn("level 18: frontier_wall", out)

    def test_attempts_spike_alone_is_low_and_exit_0(self):
        code, out = self.run_flags(self.funnel(apc={10: 5.0}), "--frontier", "0")
        self.assertEqual(code, 0, out)
        self.assertIn("LOW     level 10: attempts_spike", out)

    def test_alias_columns_from_game_kpis(self):
        code, out = self.run_flags(self.funnel(churn={6: 0.12}, alias=True, completed=False), "--frontier", "0")
        self.assertEqual(code, 1, out)
        self.assertIn("level 6: churn_spike", out)

    def test_daily_key(self):
        code, out = self.run_flags(self.funnel(churn={9: 0.11}, key="day"), "--key", "day", "--frontier", "0")
        self.assertEqual(code, 1, out)
        self.assertIn("day 9: churn_spike", out)

    def test_low_sample_is_info_only(self):
        code, out = self.run_flags(self.funnel(base=150.0, churn={5: 0.2}), "--frontier", "0")
        self.assertEqual(code, 0, out)
        self.assertIn("low_sample", out)
        self.assertNotIn("churn_spike", out)

    def test_inconsistent_funnel_exit_1(self):
        text = ("level,players_reached,players_completed,attempts,churned\n"
                "1,1000,900,2000,30\n2,1200,800,1700,30\n3,700,650,1300,20\n")
        code, out = self.run_flags(text, "--frontier", "0", "--min-reached", "100")
        self.assertEqual(code, 1)
        self.assertIn("funnel_inconsistent", out)

    def test_missing_column_cannot_run(self):
        code, out = self.run_flags("level,players_reached\n1,100\n")
        self.assertEqual(code, 2)
        self.assertIn("missing column churned", out)

    def test_non_numeric_cannot_run(self):
        code, out = self.run_flags("level,players_reached,churned\n1,abc,3\n")
        self.assertEqual(code, 2)

    def run_flags_json(self, data, *extra: str) -> tuple[int, str]:
        import json
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "game_kpis.json")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(data if isinstance(data, str) else json.dumps(data))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = lvl.main([path, *extra])
        return code, out.getvalue()

    def test_game_kpis_json_input(self):
        rows, reached = [], 10000.0
        for level in range(1, 16):
            c = 0.12 if level == 7 else 0.03
            rows.append({"level": level, "reached": round(reached), "churned_here": round(reached * c * 0.9),
                         "rate": None})
            reached *= 1 - c
        data = {"churn_by_level": {"computed": True, "inactive_days": 7, "rows": rows}}
        code, out = self.run_flags_json(data, "--frontier", "0")
        self.assertEqual(code, 1, out)
        self.assertIn("level 7: churn_spike", out)

    def test_game_kpis_json_not_computed_cannot_run(self):
        data = {"churn_by_level": {"computed": False, "reason": "no level column or no level values"}}
        code, out = self.run_flags_json(data)
        self.assertEqual(code, 2)
        self.assertIn("did not compute churn by level", out)

    def test_invalid_json_cannot_run(self):
        code, out = self.run_flags_json("{not json")
        self.assertEqual(code, 2)

    def test_json_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = os.path.join(tmp, "f.csv")
            dst = os.path.join(tmp, "flags.json")
            with open(src, "w", encoding="utf-8") as fh:
                fh.write(self.funnel(churn={8: 0.10}))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                lvl.main([src, "--frontier", "0", "--json", dst])
            import json
            with open(dst, encoding="utf-8") as fh:
                data = json.load(fh)
        self.assertEqual(data["settings"]["churn_ratio"], 2.0)
        self.assertTrue(any(f["flag"] == "churn_spike" and f["key"] == 8 for f in data["flags"]))


if __name__ == "__main__":
    unittest.main()
