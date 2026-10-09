#!/usr/bin/env python3
"""Tests for scripts/guard.py. Run: python3 scripts/test_guard.py"""
import json
import os
import subprocess
import sys
import tempfile
import unittest

GUARD = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guard.py")


def run(sub, event, root, policy=None):
    if policy is not None:
        with open(os.path.join(root, "ads-master", "guardrails.json"), "w") as fh:
            json.dump(policy, fh)
    env = dict(os.environ, CLAUDE_PROJECT_DIR=root)
    out = subprocess.run([sys.executable, "-I", GUARD, sub], input=json.dumps(event),
                         capture_output=True, text=True, env=env, timeout=20)
    assert out.returncode == 0, out.stderr
    return json.loads(out.stdout) if out.stdout.strip() else None


def decision(result):
    return result["hookSpecificOutput"]["permissionDecision"] if result else None


class GuardTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name
        os.makedirs(os.path.join(self.root, "ads-master"))
        self.stage(1)

    def tearDown(self):
        self.tmp.cleanup()

    def stage(self, n, cap=None):
        self.policy = {"automation_stage": n, "caps": {"daily_budget_per_campaign": cap}}
        with open(os.path.join(self.root, "ads-master", "guardrails.json"), "w") as fh:
            json.dump(self.policy, fh)

    def pre(self, tool, tool_input):
        return decision(run("pre", {"session_id": "t", "tool_name": tool, "tool_input": tool_input}, self.root))

    def test_reads_pass_through(self):
        self.assertIsNone(self.pre("mcp__meta__get_insights", {"date_preset": "last_7d"}))
        self.assertIsNone(self.pre("mcp__plugin_x_gads__list_campaigns", {}))
        self.assertIsNone(self.pre("Bash", {"command": "ls -la"}))
        self.assertIsNone(self.pre("Bash", {"command": "curl -s https://graph.facebook.com/v26.0/act_1/insights"}))

    def test_stage1_blocks_writes(self):
        self.assertEqual(self.pre("mcp__meta__create_campaign", {"status": "PAUSED"}), "deny")
        self.assertEqual(self.pre("mcp__meta__update_campaign", {"status": "ACTIVE"}), "deny")
        self.assertEqual(self.pre("Bash", {"command": "shopify theme push --unpublished"}), "deny")

    def test_g4_always_denied(self):
        self.stage(5)
        self.assertEqual(self.pre("mcp__meta__delete_campaign", {"id": "1"}), "deny")
        self.assertEqual(self.pre("Bash", {"command": "shopify theme delete -t 1"}), "deny")

    def test_stage2_paused_create_asks(self):
        self.stage(2)
        self.assertEqual(self.pre("mcp__meta__create_ad", {"status": "PAUSED"}), "ask")
        self.assertEqual(self.pre("mcp__meta__upload_ad_image", {"file": "a.png"}), "ask")
        self.assertEqual(self.pre("mcp__meta__update_adset", {"status": "ACTIVE"}), "deny")

    def test_stage4_commit_asks_and_cap_denies(self):
        self.stage(4, cap=20)
        self.assertEqual(self.pre("mcp__meta__update_adset", {"daily_budget": "1500"}), "ask")
        self.assertEqual(self.pre("mcp__meta__update_adset", {"daily_budget": "5000"}), "deny")
        self.assertEqual(self.pre("mcp__gads__mutate_campaign_budgets", {"amount_micros": 50000000}), "deny")
        self.assertEqual(self.pre("Bash", {"command": "shopify theme publish -t 9"}), "ask")
        self.assertEqual(self.pre("mcp__klaviyo__send_campaign", {"id": "c"}), "ask")

    def test_release_commands(self):
        self.stage(4)
        cases = {
            "shopify theme push --publish": "ask",
            "shopify theme push --theme 123456": "ask",
            "SHOPIFY_FLAG_PUBLISH=1 shopify theme push": "ask",
            "vercel promote https://x.vercel.app": "ask",
            "vercel rollback": "ask",
            "shopify store execute --allow-mutations q.graphql": "ask",
            "shopify theme dev --allow-live": "ask",
            "wp @prod option update blogname X": "ask",
            "shopify store bulk execute --allow-mutations q.graphql": "ask",
            "shopify theme push -p": "ask",
            "netlify api restoreSiteDeploy --data x": "ask",
            "wp --ssh=prod.example.com option update home x": "ask",
            "vercel rolling-release start": "ask",
            "shopify store delete --product 1": "deny",
            "wp @prod db reset --yes": "deny",
        }
        for cmd, want in cases.items():
            self.assertEqual(self.pre("Bash", {"command": cmd}), want, cmd)
        self.stage(2)
        self.assertEqual(self.pre("Bash", {"command": "shopify theme push --unpublished"}), "ask")
        self.assertEqual(self.pre("Bash", {"command": "shopify theme push --theme 1"}), "deny")

    def test_extra_ask_pattern_beats_builtin_g2(self):
        self.policy = {"automation_stage": 4, "extra_ask_bash_patterns": [r"vercel\s+deploy"]}
        with open(os.path.join(self.root, "ads-master", "guardrails.json"), "w") as fh:
            json.dump(self.policy, fh)
        out = run("pre", {"session_id": "t", "tool_name": "Bash", "tool_input": {"command": "vercel deploy"}}, self.root)
        self.assertIn("guardrails.json", out["hookSpecificOutput"]["permissionDecisionReason"])

    def test_secrets_blocked_outside_env(self):
        secret = "EAAB" + "x" * 50
        self.assertEqual(self.pre("Write", {"file_path": os.path.join(self.root, "notes.md"), "content": secret}), "deny")
        self.assertIsNone(self.pre("Write", {"file_path": os.path.join(self.root, ".env"), "content": secret}))

    def test_policy_file_edit_asks(self):
        path = os.path.join(self.root, "ads-master", "guardrails.json")
        self.assertEqual(self.pre("Edit", {"file_path": path, "old_string": "1", "new_string": "5"}), "ask")

    def test_repo_clone_named_ads_master_is_not_a_workspace(self):
        with tempfile.TemporaryDirectory() as home:
            os.makedirs(os.path.join(home, "ads-master", "skills"))
            project = os.path.join(home, "projects", "shop")
            os.makedirs(project)
            env = {k: v for k, v in os.environ.items() if k != "CLAUDE_PROJECT_DIR"}
            out = subprocess.run([sys.executable, "-I", GUARD, "pre"], capture_output=True, text=True, env=env,
                                 input=json.dumps({"tool_name": "mcp__meta__delete_campaign", "tool_input": {}, "cwd": project}))
            self.assertEqual(out.stdout.strip(), "")

    def test_no_workspace_is_silent(self):
        with tempfile.TemporaryDirectory() as other:
            env = dict(os.environ, CLAUDE_PROJECT_DIR=other)
            out = subprocess.run([sys.executable, "-I", GUARD, "pre"], capture_output=True, text=True, env=env,
                                 input=json.dumps({"tool_name": "mcp__meta__delete_campaign", "tool_input": {}, "cwd": other}))
            self.assertEqual(out.stdout.strip(), "")

    def test_stop_requires_session_report_after_writes(self):
        self.stage(2)
        run("post", {"session_id": "abc", "tool_name": "mcp__meta__create_ad", "tool_input": {"status": "PAUSED"},
                     "tool_response": {"id": "1"}}, self.root)
        out = run("stop", {"session_id": "abc", "stop_hook_active": False}, self.root)
        self.assertEqual(out["decision"], "block")
        self.assertIsNone(run("stop", {"session_id": "abc", "stop_hook_active": True}, self.root))
        reports = os.path.join(self.root, "ads-master", "logs", "session-reports")
        os.makedirs(reports, exist_ok=True)
        with open(os.path.join(reports, "r.md"), "w") as fh:
            fh.write("session abc")
        self.assertIsNone(run("stop", {"session_id": "abc", "stop_hook_active": False}, self.root))

    def test_review_hint_once_per_reviewer(self):
        ev = {"session_id": "s1", "tool_name": "Edit",
              "tool_input": {"file_path": os.path.join(self.root, "sections", "main-product.liquid")}}
        out = run("post", ev, self.root)
        ctx = out["hookSpecificOutput"]["additionalContext"]
        self.assertIn("site-engineer", ctx)
        self.assertIsNone(run("post", ev, self.root))
        out = run("post", {"session_id": "s1", "tool_name": "Write",
                           "tool_input": {"file_path": "ads-master/outputs/meta-ads/2026-10-09_meta-ads_ad-copy.md"}}, self.root)
        self.assertIn("compliance", out["hookSpecificOutput"]["additionalContext"])
        self.assertIsNone(run("post", {"session_id": "s1", "tool_name": "Write",
                                       "tool_input": {"file_path": "ads-master/journal/2026-10-09_0900_seo_note.md"}}, self.root))
        self.policy["review_hints"] = False
        self.assertIsNone(run("post", {"session_id": "s2", "tool_name": "Edit",
                                       "tool_input": {"file_path": "sections/x.liquid"}}, self.root, self.policy))


if __name__ == "__main__":
    unittest.main(verbosity=1)
