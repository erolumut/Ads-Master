#!/usr/bin/env python3
"""Tests for serp_clusters.py (standard library unittest).

Run from the repo root:
  python3 -I -B -m unittest discover -s skills/seo/scripts -p "test_*.py"
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import serp_clusters as sc  # noqa: E402

SCRIPT = os.path.join(HERE, "serp_clusters.py")
SERP = os.path.join(HERE, "samples", "serp_sample.csv")
GSC = os.path.join(HERE, "samples", "gsc_sample.csv")
EXPECTED = os.path.join(HERE, "samples", "serp_clusters_expected.json")
CANNOT = "This check cannot cover:"
SITE = "example-shop.test"


def run_cli(*args):
    return subprocess.run([sys.executable, "-I", "-B", SCRIPT, *args], capture_output=True, text=True, timeout=60)


def last_line(text):
    return text.rstrip("\n").split("\n")[-1]


def serp_text(spec):
    """spec: {keyword: (volume or None, [url, ...])}; positions follow list order."""
    lines = ["keyword,url,position,volume"]
    for kw, (vol, urls) in spec.items():
        for i, u in enumerate(urls, 1):
            lines.append("%s,%s,%d,%s" % (kw, u, i, "" if vol is None else vol))
    return "\n".join(lines) + "\n"


def cluster_by_head(res, head):
    return next(c for c in res["clusters"] if c["head"] == head)


class TmpCase(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="serp_clusters_test_")
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def write(self, name, text):
        path = os.path.join(self.tmp, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path


class NormalizationTests(unittest.TestCase):
    def test_normalize_url(self):
        n = sc.normalize_url
        self.assertEqual(n("HTTPS://WWW.Example.COM/Path/?utm_source=x&a=1&gclid=abc&fbclid=z&UTM_medium=m#frag"),
                         "https://example.com/Path?a=1")
        self.assertEqual(n("http://a.test/"), "http://a.test")
        self.assertEqual(n("https://a.test:443/x/"), "https://a.test/x")
        self.assertEqual(n("https://a.test:8080/x"), "https://a.test:8080/x")
        self.assertEqual(n("a.test/x"), "https://a.test/x")
        self.assertEqual(n("https://a.test/x?utm_source=1"), "https://a.test/x")
        self.assertEqual(n("https://a.test/x?page=2&utm_campaign=c"), "https://a.test/x?page=2")
        # path case is kept: paths are case sensitive
        self.assertNotEqual(n("https://a.test/Shoes"), n("https://a.test/shoes"))
        for variant in ("https://www.a.test/x/", "HTTPS://A.TEST/x#top", "https://a.test/x?gclid=1&utm_x=2"):
            self.assertEqual(n(variant), "https://a.test/x")
        with self.assertRaises(ValueError):
            n("/relative/path")

    def test_classify_path(self):
        c = sc.classify_path
        self.assertEqual(c("https://a.test/blog/post"), "guide")
        self.assertEqual(c("https://a.test/blog"), "guide")  # blog index, trailing slash removed
        self.assertEqual(c("https://a.test/how-to/x"), "guide")
        self.assertEqual(c("https://a.test/products/x"), "commercial")
        self.assertEqual(c("https://a.test/p/x"), "commercial")
        self.assertEqual(c("https://a.test/pricing"), "commercial")
        self.assertEqual(c("https://a.test/about"), "other")
        self.assertEqual(c("https://a.test"), "other")
        self.assertEqual(c("https://a.test/blog/product-reviews"), "other")  # both marker sets match


class ClusterTests(TmpCase):
    def test_threshold_sensitivity_on_sample(self):
        res = sc.analyze(SERP, GSC)
        table = {s["threshold"]: (s["clusters"], s["singletons"]) for s in res["sensitivity"]}
        self.assertEqual(table, {3: (5, 1), 4: (7, 4), 5: (9, 7)})
        self.assertNotEqual(table[3][0], table[5][0])

    def test_primary_added_to_thresholds(self):
        res = sc.analyze(SERP, None, None, thresholds=[3], primary=5)
        self.assertEqual([s["threshold"] for s in res["sensitivity"]], [3, 5])
        self.assertEqual(len(res["clusters"]), 9)

    def test_head_selection(self):
        res = sc.analyze(SERP, GSC)
        self.assertEqual(cluster_by_head(res, "burr coffee grinder")["keywords"][0]["volume"], 2900)
        self.assertEqual([c["head"] for c in res["clusters"]][:3],
                         ["burr coffee grinder", "how to descale a kettle", "trail running shoes"])
        # no volume: most GSC impressions, then alphabetical
        urls = ["https://a.test/x%d" % i for i in range(5)]
        serp = self.write("serp.csv", serp_text({"bbb": (None, urls), "aaa": (None, urls)}))
        gsc = self.write("gsc.csv", "query,page,clicks,impressions\nbbb,https://s.test/p,1,50\naaa,https://s.test/p,1,10\n")
        self.assertEqual(sc.analyze(serp, None, None)["clusters"][0]["head"], "aaa")
        self.assertEqual(sc.analyze(serp, gsc, None)["clusters"][0]["head"], "bbb")
        # volume beats impressions
        serp2 = self.write("serp2.csv", serp_text({"bbb": (10, urls), "aaa": (99, urls)}))
        self.assertEqual(sc.analyze(serp2, gsc, None)["clusters"][0]["head"], "aaa")

    def test_rows_outside_top_10_are_ignored(self):
        res = sc.analyze(SERP, None, SITE)
        self.assertEqual(res["inputs"]["serp_rows_ignored_outside_top10"], 1)
        tr = cluster_by_head(res, "trail running shoes")
        self.assertEqual(tr["keywords"][0]["serp_urls"], 8)
        only_deep = self.write("deep.csv", "keyword,url,position\nk,https://a.test/x,11\n")
        proc = run_cli("--serp", only_deep)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("no organic rows", proc.stderr)

    def test_duplicate_url_rows_keep_best_position(self):
        serp = self.write("dup.csv", "keyword,url,position\nk,https://a.test/x,5\nk,https://www.a.test/x/,2\n")
        loaded = sc.load_serp(serp)
        self.assertEqual(loaded["positions"]["k"], {"https://a.test/x": 2})


class IntentTests(TmpCase):
    def _two_keywords(self, order_a, order_b):
        urls = {
            "g1": "https://a.test/blog/a", "g2": "https://b.test/guide/b",
            "c1": "https://c.test/shop/a", "c2": "https://d.test/products/b",
            "o1": "https://e.test/x1", "o2": "https://f.test/x2",
        }
        spec = {"kw a": (None, [urls[k] for k in order_a]), "kw b": (None, [urls[k] for k in order_b])}
        return self.write("serp.csv", serp_text(spec))

    def test_mixed_intent_flag(self):
        res = sc.analyze(SERP, GSC)
        trail = cluster_by_head(res, "trail running shoes")
        self.assertTrue(trail["mixed_intent"])
        self.assertEqual(trail["intent_counts"], {"guide": 3, "commercial": 3, "other": 0})
        text = sc.render_text(res)
        self.assertIn("MIXED INTENT: likely needs two pages, do not merge", text)
        # exactly 2 guide, 2 commercial, 2 other of 6 top 3 URLs: each is 33 percent
        path = self._two_keywords(["g1", "c1", "o1", "c2", "g2", "o2"], ["g2", "c2", "o2", "g1", "c1", "o1"])
        self.assertTrue(sc.analyze(path)["clusters"][0]["mixed_intent"])

    def test_not_mixed_when_one_side_is_small(self):
        path = self._two_keywords(["c1", "c2", "o1", "g1", "g2", "o2"], ["c2", "c1", "o2", "g2", "g1", "o1"])
        cluster = sc.analyze(path)["clusters"][0]
        self.assertEqual(cluster["intent_counts"], {"guide": 0, "commercial": 4, "other": 2})
        self.assertFalse(cluster["mixed_intent"])
        burr = cluster_by_head(sc.analyze(SERP, GSC), "burr coffee grinder")
        self.assertFalse(burr["mixed_intent"])  # 1 guide of 9 top 3 URLs


class ConsolidationTests(TmpCase):
    def test_keep_url_by_clicks(self):
        res = sc.analyze(SERP, GSC)
        cons = cluster_by_head(res, "burr coffee grinder")["consolidation"]
        self.assertEqual(cons["status"], "merge_candidates")
        self.assertEqual(cons["keep_url"], "https://example-shop.test/collections/burr-grinders")
        self.assertEqual(cons["keep_reason"], "most clicks")
        self.assertEqual([c["url"] for c in cons["candidates"]],
                         ["https://example-shop.test/products/burr-grinder-pro",
                          "https://example-shop.test/collections/coffee-grinders"])
        for cand in cons["candidates"]:
            self.assertIn("candidate to merge into https://example-shop.test/collections/burr-grinders, "
                          "then 301 after site-engineer release QA", cand["action"])
        # page URLs in GSC with www, trailing slash and utm parameter merge with the plain SERP URL
        self.assertEqual(cons["pages"][0]["clicks"], 120)
        # only the candidate with more clicks for a single query gets the WARN
        self.assertEqual(len(cons["candidates"][0]["warnings"]), 1)
        self.assertIn("\"best burr grinder\" (25 vs 10)", cons["candidates"][0]["warnings"][0])
        self.assertEqual(cons["candidates"][1]["warnings"], [])

    def test_no_candidate_on_mixed_cluster(self):
        res = sc.analyze(SERP, GSC)
        cons = cluster_by_head(res, "trail running shoes")["consolidation"]
        self.assertEqual(cons["status"], "review_mixed_intent")
        self.assertIsNone(cons["keep_url"])
        self.assertEqual(cons["candidates"], [])
        self.assertEqual(len(cons["pages"]), 2)
        text = sc.render_text(res)
        self.assertIn("review: mixed intent", text)
        merged = [m["merge_url"] for m in res["draft_change_request"]["merges"]]
        self.assertFalse([u for u in merged if "trail" in u])
        self.assertEqual(res["draft_change_request"]["reviews"][0]["cluster"], 3)

    def test_conversions_override_clicks(self):
        gsc = self.write("gsc.csv", "\n".join([
            "Query,Page,Clicks,Impressions,Conversions",
            "burr coffee grinder,https://example-shop.test/collections/burr-grinders,120,3000,0",
            "burr coffee grinder,https://example-shop.test/collections/coffee-grinders,18,800,5",
        ]) + "\n")
        res = sc.analyze(SERP, gsc, SITE)
        cons = cluster_by_head(res, "burr coffee grinder")["consolidation"]
        self.assertEqual(cons["keep_url"], "https://example-shop.test/collections/coffee-grinders")
        self.assertEqual(cons["keep_reason"], "most conversions")
        self.assertEqual(cons["pages"][0]["conversions"], 5)
        self.assertIn("conversions 5", sc.render_text(res))

    def test_tie_break_by_impressions_then_serp_position(self):
        urls = ["https://s.test/a", "https://x.test/1", "https://x.test/2", "https://x.test/3", "https://s.test/b"]
        serp = self.write("serp.csv", serp_text({"one": (None, urls), "two": (None, urls)}))
        same = self.write("same.csv", "query,page,clicks,impressions\none,https://s.test/a,10,100\none,https://s.test/b,10,100\n")
        cons = sc.analyze(serp, same, "s.test")["clusters"][0]["consolidation"]
        self.assertEqual(cons["keep_url"], "https://s.test/a")  # position 1 beats position 5
        self.assertEqual(cons["keep_reason"], "best SERP position")
        more = self.write("more.csv", "query,page,clicks,impressions\none,https://s.test/a,10,100\none,https://s.test/b,10,300\n")
        cons = sc.analyze(serp, more, "s.test")["clusters"][0]["consolidation"]
        self.assertEqual(cons["keep_url"], "https://s.test/b")
        self.assertEqual(cons["keep_reason"], "most impressions")

    def test_gsc_header_variants(self):
        rows = ("burr coffee grinder", "https://example-shop.test/collections/burr-grinders", "50", "1,000"), \
               ("burr coffee grinder", "https://example-shop.test/collections/coffee-grinders", "5", "400")
        variants = [
            ("Top queries,Landing page,Clicks,Impressions", ","),
            ("QUERY,PAGE,CLICKS,IMPRESSIONS", ","),
            ("Query,Top pages,Click,Impression", ","),
            ("query;page;clicks;impressions", ";"),
        ]
        for i, (header, sep) in enumerate(variants):
            body = "\n".join(sep.join(r) if sep == ";" else ",".join('"%s"' % c for c in r) for r in rows)
            path = self.write("gsc%d.csv" % i, header + "\n" + body + "\n")
            res = sc.analyze(SERP, path, SITE)
            cons = cluster_by_head(res, "burr coffee grinder")["consolidation"]
            self.assertEqual(cons["keep_url"], "https://example-shop.test/collections/burr-grinders", header)
            self.assertEqual(cons["pages"][0]["impressions"], 1000, header)

    def test_site_option_and_inference(self):
        with_site = sc.analyze(SERP, None, "https://www.Example-Shop.test/")
        self.assertEqual(with_site["inputs"]["our_host"], SITE)
        self.assertEqual(with_site["inputs"]["our_host_source"], "from --site")
        self.assertTrue(cluster_by_head(with_site, "trail running shoes")["our_ranking_urls"])
        inferred = sc.analyze(SERP, GSC)
        self.assertEqual(inferred["inputs"]["our_host"], SITE)
        self.assertEqual(inferred["inputs"]["our_host_source"], "inferred from Search Console pages")
        unknown = sc.analyze(SERP)
        self.assertIsNone(unknown["inputs"]["our_host"])
        self.assertTrue([w for w in unknown["warnings"] if "our host unknown" in w])
        wrong = sc.analyze(SERP, None, "other.test")
        self.assertTrue([w for w in wrong["warnings"] if "check --site" in w])

    def test_candidate_page_in_two_clusters_gets_warned(self):
        a = ["https://x.test/%d" % i for i in range(5)]
        b = ["https://y.test/%d" % i for i in range(5)]
        serp = self.write("serp.csv", serp_text({"a one": (None, a), "a two": (None, a), "b one": (None, b)}))
        gsc = self.write("gsc.csv", "\n".join([
            "query,page,clicks,impressions",
            "a one,https://s.test/keep,50,500", "a two,https://s.test/shared,5,100",
            "b one,https://s.test/shared,9,200", ""]))
        res = sc.analyze(serp, gsc, "s.test")
        cand = cluster_by_head(res, "a one")["consolidation"]["candidates"][0]
        self.assertEqual(cand["url"], "https://s.test/shared")
        self.assertTrue([w for w in cand["warnings"] if "also gets impressions in cluster(s)" in w])


class OutputAndCliTests(TmpCase):
    def test_no_gsc_mode(self):
        proc = run_cli("--serp", SERP, "--site", SITE)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn(sc.NO_GSC_LINE, proc.stdout)
        self.assertNotIn("candidate to merge", proc.stdout)
        self.assertIn("Proposal: not assessed", proc.stdout)
        res = sc.analyze(SERP, None, SITE)
        self.assertEqual(res["note"], sc.NO_GSC_LINE)
        self.assertEqual(res["draft_change_request"]["merges"], [])
        self.assertEqual(res["draft_change_request"]["reviews"], [])

    def test_thin_serp_warn(self):
        res = sc.analyze(SERP, GSC)
        thin = [w for w in res["warnings"] if w.startswith("WARN thin SERP")]
        self.assertEqual(len(thin), 1)
        self.assertIn("descale kettle", thin[0])
        # a thin keyword still clusters
        self.assertIn("descale kettle", [k["keyword"] for k in cluster_by_head(res, "how to descale a kettle")["keywords"]])
        self.assertIn("WARN thin SERP", run_cli("--serp", SERP).stdout)

    def test_golden_json(self):
        proc = run_cli("--serp", SERP, "--gsc", GSC, "--json")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        with open(EXPECTED, encoding="utf-8") as fh:
            expected = json.load(fh)
        self.assertEqual(json.loads(proc.stdout), expected)
        # the closing line goes to stderr in JSON mode so that stdout stays valid JSON
        self.assertTrue(last_line(proc.stderr).startswith(CANNOT))

    def test_text_output_shape(self):
        proc = run_cli("--serp", SERP, "--gsc", GSC)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        out = proc.stdout
        self.assertIn("Sensitivity", out)
        self.assertIn("Draft change request (not applied)", out)
        self.assertIn("(gate G3)", out)
        self.assertIn("site-engineer release QA", out)
        self.assertTrue(last_line(out).startswith(CANNOT))
        for item in ("SERP volatility", "personalization and location", "whether pages truly serve the same need",
                     "backlinks and conversion value outside the files", "AI Overview features"):
            self.assertIn(item, last_line(out))

    def test_out_file(self):
        target = os.path.join(self.tmp, "report.txt")
        proc = run_cli("--serp", SERP, "--gsc", GSC, "--out", target)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue(last_line(proc.stdout).startswith(CANNOT))
        with open(target, encoding="utf-8") as fh:
            report = fh.read()
        self.assertIn("Draft change request (not applied)", report)
        self.assertTrue(last_line(report).startswith(CANNOT))

    def test_missing_column_exit_2(self):
        no_position = self.write("nopos.csv", "keyword,url\nk,https://a.test/x\n")
        proc = run_cli("--serp", no_position)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("missing required column(s): position", proc.stderr)
        self.assertTrue(last_line(proc.stderr).startswith(CANNOT))
        no_impr = self.write("noimpr.csv", "query,page,clicks\nk,https://a.test/x,1\n")
        proc = run_cli("--serp", SERP, "--gsc", no_impr)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("impressions", proc.stderr)

    def test_cli_exit_codes(self):
        missing = run_cli("--serp", os.path.join(self.tmp, "nope.csv"))
        self.assertEqual(missing.returncode, 2)
        self.assertIn("not found", missing.stderr)
        empty = self.write("empty.csv", "")
        self.assertEqual(run_cli("--serp", empty).returncode, 2)
        header_only = self.write("header.csv", "keyword,url,position\n")
        proc = run_cli("--serp", header_only)
        self.assertEqual(proc.returncode, 2)
        self.assertIn("no data rows", proc.stderr)
        bad_number = self.write("bad.csv", "keyword,url,position\nk,https://a.test/x,first\n")
        self.assertEqual(run_cli("--serp", bad_number).returncode, 2)
        relative = self.write("rel.csv", "keyword,url,position\nk,/just/a/path,1\n")
        self.assertEqual(run_cli("--serp", relative).returncode, 2)
        for args in (["--serp", SERP, "--thresholds", "3,x"], ["--serp", SERP, "--primary", "11"], [], ["--serp", SERP, "--gsc", empty]):
            proc = run_cli(*args)
            self.assertEqual(proc.returncode, 2, args)
            self.assertTrue(last_line(proc.stderr).startswith(CANNOT), args)
        ok = run_cli("--serp", SERP, "--gsc", GSC)
        self.assertEqual(ok.returncode, 0)

    def test_proposals_are_not_failures(self):
        proc = run_cli("--serp", SERP, "--gsc", GSC)
        self.assertIn("candidate to merge into", proc.stdout)
        self.assertEqual(proc.returncode, 0)

    def test_style_rules_in_owned_files(self):
        banned = [a + b for a, b in (("exc", "el"), ("rob", "ust"), ("hon", "ed"), ("spearhea", "ded"),
                                      ("pros", "pect"), ("reso", "nate"), ("thr", "ive"))]
        dashes = re.compile("[" + chr(0x2013) + chr(0x2014) + "]|" + re.escape(" " + "-" + " "))
        paths = [SCRIPT, os.path.abspath(__file__), SERP, GSC, EXPECTED]
        for path in paths:
            with open(path, encoding="utf-8") as fh:
                for n, line in enumerate(fh, 1):
                    low = line.lower()
                    for word in banned:
                        self.assertNotIn(word, low, "%s:%d" % (os.path.basename(path), n))
                    self.assertIsNone(dashes.search(line), "%s:%d" % (os.path.basename(path), n))


if __name__ == "__main__":
    unittest.main()
