#!/usr/bin/env python3
"""Tests for submission_check.py.
Run: python3 -m unittest discover -s skills/store-submission/scripts -p "test_*.py"
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLES = os.path.join(HERE, "samples")
SCRIPT = os.path.join(HERE, "submission_check.py")
TEMPLATE = os.path.join(HERE, "..", "references", "submission-dossier-template.md")
sys.path.insert(0, HERE)
import submission_check as sc  # noqa: E402

PBX = '// !$*UTF8*$!\n{ objects = { AA /* PrivacyInfo.xcprivacy in Resources */ = {isa = PBXBuildFile; }; }; }\n'
PLIST_HEAD = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" '
              '"http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n<plist version="1.0">\n<dict>\n')
PLIST_TAIL = "</dict>\n</plist>\n"
EMPTY_MANIFEST = (PLIST_HEAD + "<key>NSPrivacyTracking</key><false/>\n<key>NSPrivacyAccessedAPITypes</key><array/>\n"
                  + PLIST_TAIL)


def run(*args):
    p = subprocess.run([sys.executable, "-I", SCRIPT, *args], capture_output=True, text=True, timeout=120)
    return p.returncode, p.stdout


def plist(entries):
    body = "".join(f"<key>{k}</key>\n{v}\n" for k, v in entries.items())
    return PLIST_HEAD + body + PLIST_TAIL


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def copy(self, sample):
        dest = os.path.join(self.d, sample)
        shutil.copytree(os.path.join(SAMPLES, sample), dest)
        return dest

    def write(self, root, rel, text):
        path = os.path.join(root, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path

    def edit(self, path, old, new):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        self.assertIn(old, text, f"fixture text not found in {path}")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text.replace(old, new))

    def native_ios(self, swift, plist_entries, store="apple"):
        """A minimal native iOS project plus the good dossier pointed at one store."""
        root = os.path.join(self.d, "native")
        self.write(root, "Game.xcodeproj/project.pbxproj", PBX)
        entries = {"ITSAppUsesNonExemptEncryption": "<false/>"}
        entries.update(plist_entries)
        self.write(root, "Game/Info.plist", plist(entries))
        self.write(root, "Game/PrivacyInfo.xcprivacy", EMPTY_MANIFEST)
        self.write(root, "Game/GameView.swift", swift)
        with open(os.path.join(SAMPLES, "capacitor-app", "ads-master", "SUBMISSION.md"), encoding="utf-8") as fh:
            dossier = fh.read().replace("- Store: both", f"- Store: {store}")
        self.write(root, "SUBMISSION.md", dossier)
        return root


class SampleTest(Base):
    def test_capacitor_sample_passes(self):
        code, out = run(os.path.join(SAMPLES, "capacitor-app"))
        self.assertEqual(code, 0, out)
        self.assertIn("0 FAIL", out)
        self.assertTrue(out.strip().splitlines()[-1].startswith("This check cannot cover:"))

    def test_twa_sample_passes_and_says_what_it_did_not_see(self):
        code, out = run(os.path.join(SAMPLES, "twa-app"))
        self.assertEqual(code, 0, out)
        self.assertIn("No iOS project found", out)

    def test_gaps_sample_fails_on_every_gap(self):
        code, out = run(os.path.join(SAMPLES, "capacitor-app-gaps"))
        self.assertEqual(code, 1)
        for expected in ("targetSdk 35", "Play Billing Library 7.x", "NSLocationAlwaysAndWhenInUseUsageDescription",
                         "PrivacyInfo.xcprivacy not found", "export compliance not declared",
                         "Google sign in found but no Sign in with Apple", "NSCameraUsageDescription is a placeholder",
                         "'Demo account username'", "'Account deletion path in app'", "'Restore purchases path'",
                         "'Odds shown before purchase at'", "'Age rating questionnaire answered'",
                         "review notes section", "'Privacy policy URL' needs a URL"):
            self.assertIn(expected, out)
        self.assertIn("WARN [ios] NSLocationWhenInUseUsageDescription looks vague", out)

    def test_getusermedia_audio_false_needs_camera_only(self):
        _, out = run(os.path.join(SAMPLES, "capacitor-app-gaps"))
        self.assertNotIn("NSMicrophoneUsageDescription", out)


class TemplateTest(Base):
    def test_template_contains_every_dossier_key(self):
        with open(TEMPLATE, encoding="utf-8") as fh:
            text = fh.read()
        for key in sc.K.values():
            self.assertIn(f"- {key}:", text, key)

    def test_unfilled_template_blocks(self):
        root = self.copy("capacitor-app")
        shutil.copy(TEMPLATE, os.path.join(root, "ads-master", "SUBMISSION.md"))
        code, out = run(root)
        self.assertEqual(code, 1)
        for expected in ("'Store' is missing", "'Features behind sign in' needs a yes or no answer",
                         "review notes section", "'Account creation' needs a yes or no answer",
                         "'Age rating questionnaire answered' must be yes"):
            self.assertIn(expected, out)

    def test_parse_dossier_reads_bold_keys_and_ignores_fenced_lines(self):
        d = sc.parse_dossier("## 1. Submission\n- **Store**: apple\n```text\n- Store: google\n```\n")
        self.assertEqual(d["fields"]["store"], "apple")


class DossierTest(Base):
    def dossier(self, root):
        return os.path.join(root, "ads-master", "SUBMISSION.md")

    def test_missing_dossier_fails(self):
        root = self.copy("capacitor-app")
        shutil.rmtree(os.path.join(root, "ads-master"))
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("no SUBMISSION.md found", out)

    def test_expired_subscription_account_required_for_apple_subscriptions(self):
        root = self.copy("capacitor-app")
        self.edit(self.dossier(root), "- Expired subscription demo account: lapsed@puzzle.example (same password manager folder)",
                  "- Expired subscription demo account: <username>")
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("'Expired subscription demo account'", out)

    def test_review_notes_over_limit_fail(self):
        root = self.copy("capacitor-app")
        self.edit(self.dossier(root), "Account deletion: Settings > Account > Delete account.\n",
                  "Account deletion: Settings > Account > Delete account.\n" + ("More detail for the reviewer. " * 140) + "\n")
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("bytes; App Store Connect takes up to 4000", out)

    def test_review_notes_size_ignores_guidance_lines(self):
        root = self.copy("capacitor-app")
        guidance = "> " + ("Guidance for the person filling the dossier, not pasted. " * 40) + "\n"
        notes = "\n".join("Step %d: open the screen and check the result as described here." % i for i in range(42))
        self.edit(self.dossier(root), "> Guidance lines are not pasted.\n", guidance)
        self.edit(self.dossier(root), "Account deletion: Settings > Account > Delete account.\n",
                  "Account deletion: Settings > Account > Delete account.\n" + notes + "\n")
        code, out = run(root)
        self.assertEqual(code, 0, out)

    def test_thin_review_notes_warn(self):
        root = self.copy("twa-app")
        path = os.path.join(root, "SUBMISSION.md")
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        start = text.index("```text")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text[:start] + "```text\nA word game.\n```\n")
        code, out = run(root)
        self.assertEqual(code, 0, out)
        self.assertIn("review notes are under 200 characters", out)

    def test_restore_na_warns_without_policy(self):
        root = self.copy("capacitor-app")
        self.edit(self.dossier(root), "- Restore purchases path: Paywall > Restore purchases, and Settings > Restore purchases",
                  "- Restore purchases path: n/a, consumables only")
        code, out = run(root)
        self.assertIn("restore marked n/a", out)

    def test_placeholder_store_gives_one_store_fail_and_scope_from_project(self):
        root = self.copy("twa-app")
        self.edit(os.path.join(root, "SUBMISSION.md"), "- Store: google", "- Store: <apple, google or both>")
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertEqual(out.count("'Store' is missing or a placeholder"), 1, out)
        self.assertEqual(sum(1 for ln in out.splitlines() if ln.startswith("FAIL")), 1, out)
        self.assertNotIn("'Export compliance answered'", out)
        self.assertNotIn("'Social media question answered'", out)

    def test_store_flag_overrides_dossier(self):
        root = self.copy("twa-app")
        code, out = run(root, "--store", "both")
        self.assertEqual(code, 1)
        self.assertIn("'Export compliance answered' must be yes", out)


class PolicyTest(Base):
    def policy(self, **decl):
        with open(os.path.join(SAMPLES, "policy-subscription.json"), encoding="utf-8") as fh:
            data = json.load(fh)
        data["storeDeclarations"].update(decl)
        path = os.path.join(self.d, "policy.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
        return path, data

    def test_policy_matches_sample(self):
        code, out = run(os.path.join(SAMPLES, "capacitor-app"), "--policy", os.path.join(SAMPLES, "policy-subscription.json"))
        self.assertEqual(code, 0, out)

    def test_ads_declared_in_policy_but_not_in_dossier_fails(self):
        path, _ = self.policy(containsAds=True)
        code, out = run(os.path.join(SAMPLES, "capacitor-app"), "--policy", path)
        self.assertEqual(code, 1)
        self.assertIn("FAIL [policy] dossier 'Contains ads'", out)

    def test_random_items_in_catalog_need_dossier_answer(self):
        path, data = self.policy()
        data["catalog"][0]["random"] = True
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
        code, out = run(os.path.join(SAMPLES, "capacitor-app"), "--policy", path)
        self.assertEqual(code, 1)
        self.assertIn("'Paid random items'", out)

    def test_restore_na_with_store_subscription_fails(self):
        root = self.copy("capacitor-app")
        self.edit(os.path.join(root, "ads-master", "SUBMISSION.md"),
                  "- Restore purchases path: Paywall > Restore purchases, and Settings > Restore purchases",
                  "- Restore purchases path: n/a")
        code, out = run(root, "--policy", os.path.join(SAMPLES, "policy-subscription.json"))
        self.assertEqual(code, 1)
        self.assertIn("restorable products", out)


class IOSTest(Base):
    def test_att_without_purpose_string_fails_then_passes(self):
        swift = "import AppTrackingTransparency\nfunc ask() { ATTrackingManager.requestTrackingAuthorization { _ in } }\n"
        code, out = run(self.native_ios(swift, {}))
        self.assertEqual(code, 1)
        self.assertIn("missing purpose string NSUserTrackingUsageDescription", out)
        shutil.rmtree(os.path.join(self.d, "native"))
        good = {"NSUserTrackingUsageDescription": "<string>The app uses tracking data to measure which ads bring new players to the game.</string>"}
        code, out = run(self.native_ios(swift, good))
        self.assertEqual(code, 0, out)

    def test_required_reason_api_in_code_needs_manifest_entry(self):
        swift = "import UIKit\nlet started = ProcessInfo.processInfo.systemUptime\n"
        code, out = run(self.native_ios(swift, {}))
        self.assertEqual(code, 1)
        self.assertIn("privacy manifest lacks NSPrivacyAccessedAPICategorySystemBootTime", out)

    def test_build_setting_purpose_strings_count(self):
        root = self.native_ios("import AVFoundation\nAVCaptureDevice.requestAccess(for: .video) { _ in }\n", {})
        os.remove(os.path.join(root, "Game", "Info.plist"))
        self.write(root, "Game.xcodeproj/project.pbxproj", PBX + 'INFOPLIST_KEY_NSCameraUsageDescription = "The app uses the '
                   'camera to scan the code on a board game box and load that game.";\nINFOPLIST_KEY_ITSAppUsesNonExemptEncryption = NO;\n')
        code, out = run(root)
        self.assertEqual(code, 0, out)
        self.assertIn("No Info.plist file", out)

    def test_capture_device_audio_needs_microphone_string_not_camera(self):
        swift = "import AVFoundation\nlet mic = AVCaptureDevice.default(for: .audio)\n"
        mic = {"NSMicrophoneUsageDescription": "<string>The app records your voice so you can read a word aloud and hear it back.</string>"}
        code, out = run(self.native_ios(swift, mic))
        self.assertEqual(code, 0, out)
        self.assertNotIn("NSCameraUsageDescription", out)
        shutil.rmtree(os.path.join(self.d, "native"))
        cam = {"NSCameraUsageDescription": "<string>The app uses the camera so you can scan the code on a board game box.</string>"}
        code, out = run(self.native_ios(swift, cam))
        self.assertEqual(code, 1)
        self.assertIn("missing purpose string NSMicrophoneUsageDescription", out)
        self.assertNotIn("missing purpose string NSCameraUsageDescription", out)

    def test_capture_device_video_still_needs_camera_string(self):
        swift = "import AVFoundation\nlet cam = AVCaptureDevice.default(.builtInWideAngleCamera, for: .video, position: .back)\n"
        mic = {"NSMicrophoneUsageDescription": "<string>The app records your voice so you can read a word aloud and hear it back.</string>"}
        code, out = run(self.native_ios(swift, mic))
        self.assertEqual(code, 1)
        self.assertIn("missing purpose string NSCameraUsageDescription", out)
        self.assertNotIn("missing purpose string NSMicrophoneUsageDescription", out)

    def test_purpose_string_only_in_another_target_does_not_satisfy_the_app(self):
        swift = "import AVFoundation\nAVCaptureDevice.requestAccess(for: .video) { _ in }\n"
        root = self.native_ios(swift, {})
        cam = {"NSCameraUsageDescription": "<string>The widget uses the camera so you can scan the code on a board game box.</string>"}
        self.write(root, "GameWidget/Info.plist", plist(cam))
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("missing purpose string NSCameraUsageDescription", out)

    def test_purpose_string_only_in_test_target_does_not_satisfy_the_app(self):
        swift = "import AVFoundation\nAVCaptureDevice.requestAccess(for: .video) { _ in }\n"
        root = self.native_ios(swift, {})
        cam = {"NSCameraUsageDescription": "<string>The tests use the camera so you can scan the code on a board game box.</string>"}
        self.write(root, "GameUITests/Info.plist", plist(cam))
        self.write(root, "Tests/Info.plist", plist(cam))
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("missing purpose string NSCameraUsageDescription", out)

    def test_unidentified_main_plist_merges_and_warns_with_source_of_each_key(self):
        swift = "import AVFoundation\nAVCaptureDevice.requestAccess(for: .video) { _ in }\n"
        root = self.native_ios(swift, {})
        os.remove(os.path.join(root, "Game", "Info.plist"))
        entries = {"ITSAppUsesNonExemptEncryption": "<false/>",
                   "NSCameraUsageDescription": "<string>The app uses the camera so you can scan the code on a board game box.</string>"}
        self.write(root, "Sources/Info.plist", plist(entries))
        self.write(root, "Other/Info.plist", plist({"CFBundleDisplayName": "<string>Other</string>"}))
        code, out = run(root)
        self.assertEqual(code, 0, out)
        warn = [ln for ln in out.splitlines() if ln.startswith("WARN") and "could not be identified" in ln]
        self.assertEqual(len(warn), 1, out)
        self.assertIn(os.path.join("Sources", "Info.plist"), warn[0])
        self.assertIn("NSCameraUsageDescription from", warn[0])

    def test_siwa_exception_in_dossier_turns_fail_into_warn(self):
        root = self.native_ios("import GoogleSignIn\nfunc go() { GIDSignIn.sharedInstance.signIn(withPresenting: vc) }\n", {})
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("Google sign in found but no Sign in with Apple", out)
        self.edit(os.path.join(root, "SUBMISSION.md"), "- Sign in with Apple: offered next to Google sign in",
                  "- Sign in with Apple: not required because users sign in only with their school account (4.8 exception)")
        code, out = run(root)
        self.assertEqual(code, 0, out)
        self.assertIn("claims a 4.8 exception", out)

    def test_privacy_manifest_not_in_xcode_project_warns(self):
        root = self.native_ios("import UIKit\n", {})
        self.write(root, "Game.xcodeproj/project.pbxproj", "// !$*UTF8*$!\n{ objects = { }; }\n")
        code, out = run(root)
        self.assertEqual(code, 0, out)
        self.assertIn("the Xcode project does not reference it", out)


class AndroidTest(Base):
    def test_twa_wrong_package_fails(self):
        root = self.copy("twa-app")
        self.edit(os.path.join(root, "web", "public", ".well-known", "assetlinks.json"), "app.example.daily", "app.example.other")
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("no handle_all_urls statement for package app.example.daily", out)

    def test_twa_without_assetlinks_fails(self):
        root = self.copy("twa-app")
        shutil.rmtree(os.path.join(root, "web"))
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("without .well-known/assetlinks.json", out)

    def test_twa_single_fingerprint_warns_and_malformed_fails(self):
        root = self.copy("twa-app")
        path = os.path.join(root, "web", "public", ".well-known", "assetlinks.json")
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        data[0]["target"]["sha256_cert_fingerprints"] = data[0]["target"]["sha256_cert_fingerprints"][:1]
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
        code, out = run(root)
        self.assertEqual(code, 0, out)
        self.assertIn("one fingerprint", out)
        data[0]["target"]["sha256_cert_fingerprints"] = ["14:6D:E9"]
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("missing or malformed", out)

    def test_kotlin_dsl_target_and_threshold_flag(self):
        root = self.copy("twa-app")
        os.remove(os.path.join(root, "app", "build.gradle"))
        self.write(root, "app/build.gradle.kts", 'plugins { id("com.android.application") }\nandroid {\n  defaultConfig {\n'
                   '    applicationId = "app.example.daily"\n    targetSdk = 36\n  }\n}\ndependencies {\n'
                   '  implementation("com.google.androidbrowserhelper:androidbrowserhelper:2.6.2")\n}\n')
        self.assertEqual(run(root)[0], 0)
        code, out = run(root, "--min-target-sdk", "37")
        self.assertEqual(code, 1)
        self.assertIn("targetSdk 36", out)

    def test_billing_version_from_catalog(self):
        root = self.copy("twa-app")
        self.write(root, "gradle/libs.versions.toml", '[versions]\nbilling = "7.0.0"\n\n[libraries]\n'
                   'billing = { module = "com.android.billingclient:billing", version.ref = "billing" }\n')
        code, out = run(root)
        self.assertEqual(code, 1)
        self.assertIn("Play Billing Library 7.x", out)


class CouldNotRunTest(Base):
    def test_missing_project(self):
        code, out = run(os.path.join(self.d, "nope"))
        self.assertEqual(code, 2)
        self.assertTrue(out.strip().splitlines()[-1].startswith("This check cannot cover:"))

    def test_missing_explicit_dossier(self):
        self.assertEqual(run(os.path.join(SAMPLES, "twa-app"), "--dossier", os.path.join(self.d, "x.md"))[0], 2)

    def test_invalid_policy(self):
        bad = self.write(self.d, "bad.json", "{ not json")
        self.assertEqual(run(os.path.join(SAMPLES, "twa-app"), "--policy", bad)[0], 2)

    def test_nothing_to_check(self):
        empty = os.path.join(self.d, "empty")
        os.makedirs(empty)
        code, out = run(empty)
        self.assertEqual(code, 2)
        self.assertIn("nothing to check", out)


if __name__ == "__main__":
    unittest.main()
