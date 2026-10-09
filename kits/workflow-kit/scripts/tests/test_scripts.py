#!/usr/bin/env python3
"""Tests for the Workflow Kit scripts. Run: python3 -m unittest discover -s scripts/tests"""
from __future__ import annotations

import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent.parent
KIT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

import agent_models  # noqa: E402
import check_instructions  # noqa: E402
import check_workflows  # noqa: E402
import doc_numbers  # noqa: E402
import invariants_check  # noqa: E402
import ledger  # noqa: E402
import os  # noqa: E402
import subprocess  # noqa: E402

P = "ADR-NEW"  # built at runtime so this file never holds a literal placeholder
R = "R-NEW"


def run(fn, argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            code = fn(argv)
        except SystemExit as exc:  # argparse and explicit exits
            code = exc.code if isinstance(exc.code, int) else 1
            buf.write(str(exc.code))
    return code, buf.getvalue()


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.root)

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
        return p


class DocNumbersTest(Base):
    def setUp(self):
        super().setUp()
        shutil.copy(KIT / "templates" / "DECISIONS.md", self.root / "DECISIONS.md")
        self.write("workflow-kit.json", json.dumps({"decisions": {
            "files": ["DECISIONS.md"], "ruleFiles": ["docs/REGRESSIONS.md"]}}))
        self.write("docs/REGRESSIONS.md", "# Regressions\n\n- **R7 (old):** check.\n- **R12 (newer):** check.\n")

    def test_template_passes_check(self):
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--check"])
        self.assertEqual(code, 0, out)

    def test_assign_numbers_in_order_across_files(self):
        dec = self.root / "DECISIONS.md"
        text = dec.read_text()
        text = text.replace("| 001 |", f"| 001 |\n| {P}2 | second | proposed | d |\n| {P}1 | first | proposed | d |")
        text += f"\n## {P}1: first\n\nSee {P}2.\n\n## {P}2: second\n"
        dec.write_text(text)
        self.write("docs/REGRESSIONS.md", (self.root / "docs/REGRESSIONS.md").read_text() + f"- **{R}1 (new):** check. Origin: {P}1.\n")
        self.write("src/notes.md", f"Implements {P}2 and {R}1.\n")

        code, out = run(doc_numbers.main, ["--root", str(self.root), "--check", "--no-placeholders"])
        self.assertEqual(code, 1, out)
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--assign"])
        self.assertEqual(code, 0, out)
        self.assertIn("dry run", out)
        self.assertIn(f"{P}1", dec.read_text())
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--assign", "--apply"])
        self.assertEqual(code, 2, out)
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--assign", "--apply", "--yes"])
        self.assertEqual(code, 0, out)
        self.assertIn("This gate cannot cover:", out)
        dec_text = dec.read_text()
        self.assertIn("## ADR-002: first", dec_text)
        self.assertIn("## ADR-003: second", dec_text)
        self.assertIn("See ADR-003.", dec_text)
        self.assertIn("Implements ADR-003 and R13.", (self.root / "src/notes.md").read_text())
        self.assertIn("**R13 (new):** check. Origin: ADR-002.", (self.root / "docs/REGRESSIONS.md").read_text())
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--check", "--no-placeholders"])
        self.assertEqual(code, 0, out)

    def test_duplicates_and_orphans_fail(self):
        dec = self.root / "DECISIONS.md"
        dec.write_text(dec.read_text() + "\n## ADR-001: again\n\n## ADR-004: no row\n")
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--check"])
        self.assertEqual(code, 1)
        self.assertIn("two entries with ADR-1", out)
        self.assertIn("entry ADR-4 has no index row", out)

    def test_duplicate_rule_fails(self):
        self.write("docs/REGRESSIONS.md", "- **R7 (a):** x\n- **R7 (b):** y\n")
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--check"])
        self.assertEqual(code, 1)
        self.assertIn("two rule definitions with R7", out)

    def test_dry_run_writes_nothing(self):
        self.write("x.md", f"{P}1\n")
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--assign"])
        self.assertEqual(code, 0)
        self.assertIn("would update x.md", out)
        self.assertEqual((self.root / "x.md").read_text(), f"{P}1\n")

    def test_no_decision_file_could_not_run(self):
        (self.root / "DECISIONS.md").unlink()
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--check"])
        self.assertEqual(code, 2, out)
        self.assertIn("COULD NOT RUN", out)

    def test_literal_n_is_not_a_placeholder(self):
        self.write("guide.md", "Write ADR-NEW<n> while working.\n")
        code, out = run(doc_numbers.main, ["--root", str(self.root), "--check", "--no-placeholders"])
        self.assertEqual(code, 0, out)


class CheckInstructionsTest(Base):
    def test_budget_paths_and_rules(self):
        self.write("src/app.ts", "x")
        self.write("docs/guide.md", "x")
        self.write("CLAUDE.md", "# P\n<!--\nhidden\nlines\n-->\nSee `docs/guide.md` and `docs/missing.md`.\n@AGENTS.md\nRun `npm test`.\n")
        self.write("AGENTS.md", "guards")
        self.write(".claude/rules/api.md", '---\npaths:\n  - "src/**/*.{ts,tsx}"\n  - "lib/**"\n---\n# API\n')
        self.write(".claude/rules/bad.md", '---\npaths:\n  - "photos [2024/**"\n  - "/abs/**"\n---\n# Bad\n')
        self.write(".claude/rules/always.md", "# Always\nline\n")
        code, out = run(check_instructions.main, ["--root", str(self.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("4 effective lines", out)
        self.assertIn("referenced path not found: docs/missing.md", out)
        self.assertNotIn("docs/guide.md", out.split("referenced path not found")[-1])
        self.assertIn("unbalanced [", out)
        self.assertIn("absolute path", out)
        self.assertIn("'lib/**' matches no file", out)
        self.assertIn("no paths, loads every session", out)

    def test_over_budget_and_strict(self):
        self.write("CLAUDE.md", "line\n" * 12)
        code, out = run(check_instructions.main, ["--root", str(self.root), "--max-lines", "10"])
        self.assertEqual(code, 1)
        self.assertIn("over budget", out)
        self.write("CLAUDE.md", "ok\n")
        self.write(".claude/rules/x.md", '---\npaths: "nothing/**"\n---\n')
        code, _ = run(check_instructions.main, ["--root", str(self.root)])
        self.assertEqual(code, 0)
        code, _ = run(check_instructions.main, ["--root", str(self.root), "--strict"])
        self.assertEqual(code, 1)

    def test_brace_expansion(self):
        self.assertEqual(sorted(check_instructions.expand_braces("a/*.{ts,tsx}")), ["a/*.ts", "a/*.tsx"])
        self.assertIsNone(check_instructions.glob_error("src/[ab]/*.ts"))
        self.assertIsNotNone(check_instructions.glob_error("src/{a,b/*.ts"))


class LedgerTest(Base):
    def test_full_cycle(self):
        r = ["--root", str(self.root)]
        self.assertEqual(run(ledger.main, r + ["init", "--gitignore"])[0], 0)
        self.assertIn("PARALLEL-SESSIONS.md", (self.root / ".gitignore").read_text())
        code, out = run(ledger.main, r + ["checkin", "--handle", "api", "--scope", "src/api/**",
                                          "--intent", "fix paging", "--risky", "push", "--eta", "2h", "--branch", "main"])
        self.assertEqual(code, 0, out)
        self.assertNotIn("other active", out)
        code, out = run(ledger.main, r + ["checkin", "--handle", "@ui", "--scope", "src/ui/**", "--intent", "polish"])
        self.assertIn("@api", out)
        self.assertEqual(run(ledger.main, r + ["checkin", "--handle", "api", "--scope", "x", "--intent", "y"])[0], 1)
        run(ledger.main, r + ["progress", "--handle", "api", "--note", "tests green"])
        run(ledger.main, r + ["msg", "--from", "api", "--to", "ui", "--text", "I own client.ts"])
        code, out = run(ledger.main, r + ["signoff", "--handle", "api", "--done", "paging fixed", "--landmines", "cache key"])
        self.assertEqual(code, 0, out)
        text = (self.root / "PARALLEL-SESSIONS.md").read_text()
        active, rest = text.split("## MSG")
        msg, archive = rest.split("## ARCHIVE")
        self.assertNotIn("### @api", active)
        self.assertIn("### @ui", active)
        self.assertIn("MSG @api -> @ui: I own client.ts", msg)
        self.assertIn("### @api", archive)
        self.assertIn("PROGRESS", archive)
        self.assertIn("landmines: cache key", archive)
        run(ledger.main, r + ["signoff", "--handle", "ui", "--done", "done"])
        text = (self.root / "PARALLEL-SESSIONS.md").read_text()
        self.assertIn("_(empty)_", text.split("## MSG")[0])
        code, out = run(ledger.main, r + ["show"])
        self.assertIn("ACTIVE: none", out)
        self.assertIn("ARCHIVE: 2 block(s)", out)

    def test_missing_ledger(self):
        code, _ = run(ledger.main, ["--root", str(self.root), "show"])
        self.assertEqual(code, 2)


class AgentModelsTest(Base):
    def test_kit_agents_are_clean(self):
        code, out = run(agent_models.main, ["--root", str(KIT), "--dir", "agents", "--strict"])
        self.assertEqual(code, 0, out)
        self.assertIn("9 agent(s), 0 flagged", out)
        self.assertIn("This gate cannot cover:", out)

    def test_flags(self):
        self.write(".claude/agents/a.md", "---\nname: a\nmodel: claude-opus-5-5\neffort: huge\ntools: Read\n---\n")
        self.write(".claude/agents/b.md", "---\nname: b\ndescription: >\n  folded\n---\n")
        self.write(".claude/agents/c.md", "---\nname: c\nmodel: sonnet\ndisallowedTools: Agent\n---\n")
        self.write(".claude/settings.json", json.dumps({"advisorModel": "fable",
                                                         "env": {"ANTHROPIC_DEFAULT_HAIKU_MODEL": "x"}}))
        code, out = run(agent_models.main, ["--root", str(self.root), "--strict"])
        self.assertEqual(code, 1)
        self.assertIn("full model id 'claude-opus-5-5'", out)
        self.assertIn("unknown effort 'huge'", out)
        self.assertIn("no model", out)
        self.assertIn("can spawn subagents", out)
        self.assertIn("advisorModel: fable", out)
        self.assertIn("pin: drop when the alias catches up", out)
        self.assertIn("3 agent(s), 2 flagged", out)


    def test_no_agents_could_not_run(self):
        code, _ = run(agent_models.main, ["--root", str(self.root)])
        self.assertEqual(code, 2)

    def test_audit_requested_vs_served(self):
        self.write(".claude/agents/scout.md", "---\nname: scout\nmodel: haiku\ntools: Read\n---\n")
        t = self.root / "transcripts"
        sid = "11111111-2222"
        spawn = lambda tid, typ, model=None: {"type": "assistant", "message": {"model": "claude-opus-5-5", "content": [
            {"type": "tool_use", "id": tid, "name": "Agent",
             "input": {"subagent_type": typ, "prompt": "x", **({"model": model} if model else {})}}]}}
        (t / sid / "subagents").mkdir(parents=True)
        (t / f"{sid}.jsonl").write_text("\n".join(json.dumps(r) for r in [
            spawn("tu1", "scout"), spawn("tu2", "general-purpose"), spawn("tu3", "scout", "sonnet")]))
        served = {"a1": "claude-opus-5-5", "a2": "claude-opus-5-5", "a3": "claude-sonnet-5-5"}
        for aid, tid, typ in (("a1", "tu1", "scout"), ("a2", "tu2", "general-purpose"), ("a3", "tu3", "scout")):
            (t / sid / "subagents" / f"agent-{aid}.meta.json").write_text(json.dumps({"agentType": typ, "toolUseId": tid}))
            (t / sid / "subagents" / f"agent-{aid}.jsonl").write_text(json.dumps(
                {"type": "assistant", "effort": "medium", "message": {"model": served[aid], "content": []}}))
        code, out = run(agent_models.main, ["--root", str(self.root), "--audit", "--transcripts", str(t), "--strict"])
        self.assertEqual(code, 1, out)
        self.assertIn("served claude-opus-5-5 but haiku was expected", out)
        self.assertIn("unnamed spawn without an explicit model", out)
        self.assertIn("spawn parameter 'sonnet' overrode frontmatter 'haiku'", out)
        self.assertIn("3 subagent run(s), 3 flagged", out)
        code, out = run(agent_models.main, ["--root", str(self.root), "--audit", "--transcripts", str(self.root / "nope")])
        self.assertEqual(code, 2)


def git_repo(root):
    for cmd in (["init", "-q"], ["config", "user.email", "t@example.com"], ["config", "user.name", "t"]):
        subprocess.run(["git", "-C", str(root), *cmd], check=True, capture_output=True)


class InvariantsTest(Base):
    def setUp(self):
        super().setUp()
        git_repo(self.root)
        shutil.copy(KIT / "templates" / "invariants.json", self.root / "invariants.json")

    def stage(self, rel, text):
        self.write(rel, text)
        subprocess.run(["git", "-C", str(self.root), "add", rel], check=True)

    def test_staged_violations_and_pass(self):
        self.stage("src/page.tsx", 'const u = "https://x.test/?utm_source=meta";\nconst daily_budget = 50;\n')
        self.stage("src/lib/utm/build.ts", 'export const q = "?utm_source=";\n')
        code, out = run(invariants_check.main, ["--root", str(self.root)])
        self.assertEqual(code, 1, out)
        self.assertIn("INV-UTM: src/page.tsx:1", out)
        self.assertIn("INV-BUDGET: src/page.tsx:2", out)
        self.assertNotIn("src/lib/utm/build.ts", out)
        self.assertIn("This gate cannot cover:", out)

    def test_hook_mode(self):
        self.stage("src/page.tsx", 'x = "?utm_medium=cpc"\n')
        payload = {"tool_name": "Bash", "tool_input": {"command": "git add . && git commit -m 'x'"}, "cwd": str(self.root)}
        stdin = sys.stdin
        try:
            sys.stdin = io.StringIO(json.dumps(payload))
            code, out = run(invariants_check.main, ["--hook"])
            self.assertEqual(code, 0)
            decision = json.loads(out)["hookSpecificOutput"]
            self.assertEqual(decision["permissionDecision"], "deny")
            self.assertIn("INV-UTM", decision["permissionDecisionReason"])
            sys.stdin = io.StringIO(json.dumps({"tool_name": "Bash", "tool_input": {"command": "git status"}}))
            code, out = run(invariants_check.main, ["--hook"])
            self.assertEqual((code, out), (0, ""))
        finally:
            sys.stdin = stdin

    def test_bad_config_could_not_run(self):
        self.write("invariants.json", '{"rules": [{"id": "X", "paths": ["**"], "must_contain": ["("]}]}')
        code, out = run(invariants_check.main, ["--root", str(self.root)])
        self.assertEqual(code, 2, out)


class WorkflowsTest(Base):
    GOOD = """name: ci
on: [push]
permissions:
  contents: read
jobs:
  test:
    if: ${{ always() }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: some/action@0123456789abcdef0123456789abcdef01234567
      - name: run
        env:
          TITLE: ${{ github.event.pull_request.title }}
        run: |
          echo "$TITLE"
"""
    BAD = """name: ci
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    runs-on: windows-latest
    steps:
      - uses: some/action@v2
      - name: echo
        run: |
          echo "${{ github.event.issue.title }}"
      - name: inline
        run: echo ${{ inputs.target }}
      - name: bad status
        continue-on-error: ${{ failure() }}
"""

    def test_good_and_bad(self):
        self.write(".github/workflows/good.yml", self.GOOD)
        code, out = run(check_workflows.main, ["--root", str(self.root)])
        self.assertEqual(code, 0, out)
        self.write(".github/workflows/bad.yml", self.BAD)
        code, out = run(check_workflows.main, ["--root", str(self.root), ".github/workflows/bad.yml"])
        self.assertEqual(code, 1, out)
        self.assertIn("duplicate key 'runs-on'", out)
        self.assertIn("github.event.issue.title }} inside run:", out)
        self.assertIn("inputs.target }} inside run:", out)
        self.assertIn("status function outside if: (failure())", out)
        self.assertIn("not pinned to a commit SHA: some/action@v2", out)
        self.assertIn("no workflow level permissions", out)
        self.assertIn("This gate cannot cover:", out)

    def test_no_files(self):
        code, _ = run(check_workflows.main, ["--root", str(self.root)])
        self.assertEqual(code, 2)


class PrecommitDispatchTest(Base):
    def sh(self, *args):
        return subprocess.run(["bash", str(SCRIPTS / "precommit_dispatch.sh"), *args], cwd=self.root,
                              capture_output=True, text=True)

    def test_dispatch(self):
        git_repo(self.root)
        self.write("precommit.json", json.dumps({"checks": [
            {"name": "py ok", "paths": ["**/*.py"], "command": "true {files}"},
            {"name": "md fails", "paths": ["docs/**"], "command": "false"},
            {"name": "never", "paths": ["nothing/**"], "command": "false"}]}))
        self.write("a/b.py", "x")
        subprocess.run(["git", "-C", str(self.root), "add", "a/b.py"], check=True)
        r = self.sh()
        self.assertEqual(r.returncode, 0, r.stdout)
        self.assertIn("run: py ok", r.stdout)
        self.assertNotIn("never", r.stdout)
        self.write("docs/x.md", "x")
        subprocess.run(["git", "-C", str(self.root), "add", "docs/x.md"], check=True)
        r = self.sh()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn("This gate cannot cover:", r.stdout)
        self.write(".env.local", "SECRET=1")
        self.write(".env.example", "SECRET=")
        subprocess.run(["git", "-C", str(self.root), "add", "-f", ".env.local", ".env.example"], check=True)
        r = self.sh()
        self.assertEqual(r.returncode, 1, r.stdout)
        self.assertIn(".env.local", r.stdout)
        self.assertNotIn("  .env.example", r.stdout)

    def test_outside_repo(self):
        r = self.sh()
        self.assertEqual(r.returncode, 2, r.stdout)


if __name__ == "__main__":
    unittest.main()
