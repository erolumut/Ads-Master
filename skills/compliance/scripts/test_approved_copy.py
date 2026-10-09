#!/usr/bin/env python3
"""Tests for approved_copy.py. Run: python3 test_approved_copy.py"""
import os
import subprocess
import sys
import tempfile
import unittest

SCRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "approved_copy.py")


def run(*args, cwd):
    out = subprocess.run([sys.executable, "-I", SCRIPT, *args], capture_output=True, text=True, cwd=cwd, timeout=20)
    return out.returncode, out.stdout


class ApprovedCopyTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = self.tmp.name
        self.reg = os.path.join(self.d, "approved.json")
        code, _ = run("add", "--id", "hero", "--text", "20 g protein per bar", "--by", "QA", "--registry", self.reg,
                      cwd=self.d)
        self.assertEqual(code, 0)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, text):
        path = os.path.join(self.d, name)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path

    def test_identical_copy_passes_with_whitespace_changes(self):
        p = self.write("ad.md", "Intro\n<!-- approved:hero -->20 g  protein\nper bar<!-- /approved -->\n")
        code, out = run("check", p, "--registry", self.reg, cwd=self.d)
        self.assertEqual(code, 0, out)

    def test_changed_number_fails(self):
        p = self.write("ad.md", "<!-- approved:hero -->25 g protein per bar<!-- /approved -->")
        code, out = run("check", p, "--registry", self.reg, cwd=self.d)
        self.assertEqual(code, 1)
        self.assertIn("changed after approval", out)

    def test_unknown_id_fails(self):
        p = self.write("ad.md", "<!-- approved:nope -->anything<!-- /approved -->")
        code, out = run("check", p, "--registry", self.reg, cwd=self.d)
        self.assertEqual(code, 1)
        self.assertIn("unknown approval id", out)

    def test_expired_fails(self):
        run("add", "--id", "old", "--text", "x", "--by", "QA", "--expires", "2000-01-01", "--registry", self.reg,
            cwd=self.d)
        code, out = run("verify", "--registry", self.reg, cwd=self.d)
        self.assertEqual(code, 1)
        self.assertIn("expired", out)

    def test_duplicate_id_needs_replace(self):
        code, _ = run("add", "--id", "hero", "--text", "y", "--by", "QA", "--registry", self.reg, cwd=self.d)
        self.assertEqual(code, 1)

    def test_missing_registry_could_not_run(self):
        code, _ = run("check", self.d, "--registry", os.path.join(self.d, "none.json"), cwd=self.d)
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main(verbosity=1)
