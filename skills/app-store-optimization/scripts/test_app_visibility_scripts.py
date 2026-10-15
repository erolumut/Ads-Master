#!/usr/bin/env python3
"""Tests for the app visibility scripts: aso_metadata_check.py, review_themes.py (this folder) and
ai_prompt_panel.py, app_entity_check.py (skills/ai-search-optimization/scripts).
Run: python3 -m unittest discover -s skills/app-store-optimization/scripts -p "test_*.py"
"""
import csv
import datetime
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
AI = os.path.join(HERE, "..", "..", "ai-search-optimization", "scripts")
sys.path.insert(0, AI)
import ai_prompt_panel  # noqa: E402


def run(script, *args):
    p = subprocess.run([sys.executable, "-I", script, *args], capture_output=True, text=True, timeout=60)
    return p.returncode, p.stdout


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, text, encoding="utf-8"):
        path = os.path.join(self.d, name)
        with open(path, "w", encoding=encoding) as fh:
            fh.write(text)
        return path


class MetadataTest(Base):
    S = os.path.join(HERE, "aso_metadata_check.py")

    def test_clean_apple_entry_passes(self):
        p = self.write("ok.json", json.dumps([{"store": "apple", "locale": "en-US", "name": "Acme: Habit Tracker",
                                               "subtitle": "Daily goals", "keywords": "routine,planner,streak",
                                               "target_terms": ["habit tracker"]}]))
        code, out = run(self.S, p)
        self.assertEqual(code, 0, out)
        self.assertIn("exact phrase", out)

    def test_play_title_policy_and_competitor(self):
        p = self.write("bad.json", json.dumps([
            {"store": "google", "locale": "en-US", "title": "Acme #1 Best Tracker", "short_description": "free",
             "full_description": "x"},
            {"store": "apple", "locale": "en-US", "name": "Acme", "keywords": "rival,planner"}]))
        c = self.write("c.txt", "Rival\n")
        code, out = run(self.S, p, "--competitors", c)
        self.assertEqual(code, 1)
        self.assertIn("FAIL title", out)
        self.assertIn("WARN short_description", out)
        self.assertIn("competitor names", out)

    def test_bad_store_could_not_run(self):
        self.assertEqual(run(self.S, self.write("x.json", '[{"store": "x"}]'))[0], 2)


class ReviewThemesTest(Base):
    S = os.path.join(HERE, "review_themes.py")

    def rows(self):
        base = datetime.datetime(2026, 10, 12)
        out = [["Star Rating", "Review Text", "Review Submit Date and Time", "Developer Reply Date and Time"]]
        for i in range(40):
            d = base - datetime.timedelta(days=10 + i % 20)
            out.append([5, "love it, very helpful", d.isoformat(), ""])
        for i in range(10):
            d = base - datetime.timedelta(days=i % 5)
            out.append([1, "keeps crashing", d.isoformat(), ""])
        return out

    def test_rising_crash_theme_alerts(self):
        p = os.path.join(self.d, "r.csv")
        with open(p, "w", newline="", encoding="utf-8") as fh:
            csv.writer(fh).writerows(self.rows())
        code, out = run(self.S, p, "--today", "2026-10-12")
        self.assertEqual(code, 1, out)
        self.assertIn("crash_or_bug", out)

    def test_utf16_export_is_read(self):
        p = os.path.join(self.d, "r16.csv")
        with open(p, "w", newline="", encoding="utf-16") as fh:
            csv.writer(fh).writerows(self.rows())
        code, out = run(self.S, p, "--today", "2026-10-12")
        self.assertIn("50 reviews", out)

    def test_missing_columns_could_not_run(self):
        self.assertEqual(run(self.S, self.write("x.csv", "a,b\n1,2\n"))[0], 2)


class PanelTest(Base):
    S = os.path.join(AI, "ai_prompt_panel.py")

    def test_owned_matching(self):
        dom = ["acme.com", "play.google.com/store/apps/details?id=com.acme", "apps.apple.com/app/acme"]
        cases = [("https://blog.acme.com", True), ("https://acme.community", False),
                 ("https://play.google.com/store/apps/details?hl=en&id=com.acme", True),
                 ("https://play.google.com/store/apps/details?id=com.acme.pro", False),
                 ("https://apps.apple.com/app/acme/id1", True), ("https://apps.apple.com/app/acmepro/id2", False)]
        for url, expected in cases:
            self.assertEqual(ai_prompt_panel.owned(url, dom), expected, url)

    def test_negation_is_not_a_recommendation(self):
        b = ai_prompt_panel.names_re({"name": "Acme"})
        c = {"Rival": ai_prompt_panel.names_re({"name": "Rival"})}
        self.assertEqual(ai_prompt_panel.score_run({"text": "Acme is not the best. Rival is."}, b, c, [])["recommended"], 0)
        self.assertEqual(ai_prompt_panel.score_run({"text": "I recommend Acme over Rival."}, b, c, [])["recommended"], 1)

    def test_first_pick_needs_first_and_recommended(self):
        b = ai_prompt_panel.names_re({"name": "Acme"})
        c = {"Rival": ai_prompt_panel.names_re({"name": "Rival"})}
        score = ai_prompt_panel.score_run
        self.assertEqual(score({"text": "I recommend Acme. Rival is also fine."}, b, c, [])["first_pick"], 1)
        self.assertEqual(score({"text": "Rival is the top choice. Acme is another option."}, b, c, [])["first_pick"], 0)
        self.assertIsNone(score({"text": "No brands here."}, b, c, [])["first_pick"])

    def test_gap_urls_only_when_competitor_named_and_brand_absent(self):
        b = ai_prompt_panel.names_re({"name": "Acme"})
        c = {"Rival": ai_prompt_panel.names_re({"name": "Rival"})}
        urls = ["https://lists.example/best-tools", "https://acme.com/pricing"]
        gap = ai_prompt_panel.score_run({"text": "Rival is best.", "cited_urls": urls}, b, c, ["acme.com"])
        self.assertEqual(gap["gap_urls"], ["https://lists.example/best-tools"])
        self.assertEqual(gap["gap_comps"], ["Rival"])
        both = ai_prompt_panel.score_run({"text": "Rival and Acme.", "cited_urls": urls}, b, c, ["acme.com"])
        self.assertEqual(both["gap_urls"], [])

    def test_report_has_first_pick_and_gap_section(self):
        cfg = self.write("c.json", json.dumps({"brand": {"name": "Acme", "domains": ["acme.com"]},
                                               "competitors": [{"name": "Rival"}]}))
        lines = [json.dumps({"period": "p", "engine": "e", "prompt_id": "x", "run": i, "text": "Rival wins.",
                             "cited_urls": ["https://lists.example/best"]}) for i in range(3)]
        ans = self.write("a.jsonl", "\n".join(lines) + "\n")
        code, out = run(self.S, ans, "--config", cfg)[:2]
        self.assertEqual(code, 0)
        self.assertIn("First pick", out)
        self.assertIn("https://lists.example/best: 3 answers (competitors named: Rival)", out)

    def test_too_few_runs_could_not_run(self):
        cfg = self.write("c.json", json.dumps({"brand": {"name": "Acme"}}))
        ans = self.write("a.jsonl", json.dumps({"period": "p", "engine": "e", "prompt_id": "x", "text": "Acme"}) + "\n")
        self.assertEqual(run(self.S, ans, "--config", cfg)[0], 2)


class EntityTest(Base):
    S = os.path.join(AI, "app_entity_check.py")

    def test_consistent_and_mismatch(self):
        facts = self.write("f.json", json.dumps({"name": "Acme Habits", "developer": "Acme BV", "prices": ["4.99"],
                                                 "ios": {"app_id": "123"}}))
        good = self.write("g.html", '<script type="application/ld+json">{"@type":"MobileApplication","name":"Acme Habits",'
                                    '"operatingSystem":"iOS","offers":{"price":"4.99"}}</script>'
                                    '<a href="https://apps.apple.com/app/x/id123">Acme Habits</a>')
        self.assertEqual(run(self.S, "--facts", facts, "--html", good)[0], 0)
        store = self.write("s.html", "Acme Habits by Acme BV, 4,99 €")
        self.assertEqual(run(self.S, "--facts", facts, "--store-page", store)[0], 0)
        robots = self.write("r.txt", "User-agent: *\nDisallow: /\n\nUser-agent: OAI-SearchBot\nAllow: /\n")
        code, out = run(self.S, "--facts", facts, "--robots", robots)
        self.assertEqual(code, 1)
        self.assertNotIn("blocks OAI-SearchBot", out)
        self.assertIn("blocks PerplexityBot", out)


if __name__ == "__main__":
    unittest.main()
