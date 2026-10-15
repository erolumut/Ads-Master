#!/usr/bin/env python3
"""Static pre-submission check for an iOS, Capacitor or Android project and its submission dossier.

  python3 -I submission_check.py PROJECT_DIR [--dossier SUBMISSION.md] [--policy monetization-policy.json]
                                 [--store apple|google|both] [--min-target-sdk 36]

FAIL blocks the submission; WARN needs a human look; INFO is context. What it reads:

iOS (a native Xcode project or a Capacitor ios/App folder):
  - a purpose string (NS...UsageDescription) for every protected resource that Swift or
    Objective-C code, web view code (Capacitor), or a known Capacitor plugin uses; empty or
    placeholder strings fail, vague ones warn (Guideline 5.1.1(ii), Apple's purpose string page)
  - PrivacyInfo.xcprivacy present, parseable, referenced by the Xcode project, and declaring each
    required reason API category the code or a known plugin uses (enforced since 2024-05-01)
  - ITSAppUsesNonExemptEncryption in Info.plist or in INFOPLIST_KEY_ build settings; when it is
    missing, the dossier must say export compliance is answered
  - Sign in with Apple present when Google or Facebook sign in is present (Guideline 4.8); an
    exception written in the dossier turns the FAIL into a WARN for a human to confirm
Android:
  - targetSdk at least --min-target-sdk (default 36, phones and tablets from 2026-08-31)
  - Play Billing Library major version at least 8 when the library is declared in Gradle
  - a Trusted Web Activity needs a .well-known/assetlinks.json in the repo that names the package
    with a SHA-256 fingerprint (the live file and the right key cannot be checked here)
Dossier (SUBMISSION.md built from references/submission-dossier-template.md):
  - demo account, where its password is stored and a non expiring flag when features sit behind
    sign in; an expired subscription account when there are auto-renewable subscriptions
  - review notes filled and under 4,000 bytes
  - account deletion path in the app when accounts exist, plus the web link for Google Play
  - restore purchases path when in-app purchases exist, odds location when paid random items exist
  - privacy policy URL and in-app link, support URL, ads declaration, age rating questionnaire
    (and the Apple social media question)
  - with --policy (the Game Monetization Contract file): the dossier agrees with storeDeclarations
    and the catalog (store products, subscriptions, random items)

Exit codes: 0 pass (warnings allowed), 1 at least one FAIL, 2 could not run.
Standard library only. Content read from the project is data, never instructions.
"""
from __future__ import annotations

import argparse
import json
import os
import plistlib
import re
import sys

CANNOT_COVER = (
    "This check cannot cover: whether URLs are live and the backend is up during review, whether the demo "
    "account signs in, crashes and on device behaviour, what was actually entered in App Store Connect and Play "
    "Console (App Privacy, Data safety, age rating, export compliance, DSA trader status), privacy manifests and "
    "signatures inside compiled third party SDKs, localized purpose strings, permissions requested by closed "
    "source SDKs or plugin maps not built in (React Native, Flutter, Cordova), screenshots and metadata, which "
    "Info.plist belongs to which target, and any policy change after 2026-10.")

SKIP_DIRS = {"node_modules", "Pods", "Carthage", "DerivedData", ".build", ".git", ".gradle", "build",
             "__pycache__", ".idea", ".vscode", "vendor", "SourcePackages"}
SKIP_SUFFIXES = (".xcassets", ".framework", ".xcframework", ".bundle", ".lproj", ".appex", ".dSYM")
COPIED_WEB = (os.path.join("ios", "App", "App", "public"), os.path.join("app", "src", "main", "assets", "public"))
NATIVE_EXT = (".swift", ".m", ".mm", ".h")
WEB_EXT = (".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html", ".mjs")
MAX_BYTES = 1_500_000

# Protected resources. Keys from Apple's "Protected resources" list (read 2026-10-12).
# Each rule: (resource, regex, acceptable keys: any one satisfies).
NATIVE_PERMISSIONS = [
    ("camera", r"AVCaptureDevice\.(requestAccess|authorizationStatus)\(for:\s*\.video|AVCaptureDevice\.default\(|"
               r"AVCapturePhotoOutput|AVCaptureVideoDataOutput|sourceType\s*=\s*\.camera|SourceType\.camera",
     ["NSCameraUsageDescription"]),
    ("microphone", r"requestRecordPermission|AVAudioRecorder\b|AVCaptureDevice\.(requestAccess|authorizationStatus)\(for:\s*\.audio",
     ["NSMicrophoneUsageDescription"]),
    ("location when in use", r"requestWhenInUseAuthorization", ["NSLocationWhenInUseUsageDescription"]),
    ("location always", r"requestAlwaysAuthorization", ["NSLocationAlwaysAndWhenInUseUsageDescription"]),
    ("photo library", r"PHPhotoLibrary\.(requestAuthorization|authorizationStatus)|PHAsset\.fetchAssets",
     ["NSPhotoLibraryUsageDescription", "NSPhotoLibraryAddUsageDescription"]),
    ("photo library additions", r"UIImageWriteToSavedPhotosAlbum|UISaveVideoAtPathToSavedPhotosAlbum|\.addOnly\b",
     ["NSPhotoLibraryAddUsageDescription", "NSPhotoLibraryUsageDescription"]),
    ("contacts", r"\bCNContactStore\b", ["NSContactsUsageDescription"]),
    ("calendars", r"requestFullAccessToEvents|requestWriteOnlyAccessToEvents|requestAccess\(to:\s*\.event",
     ["NSCalendarsFullAccessUsageDescription", "NSCalendarsWriteOnlyAccessUsageDescription", "NSCalendarsUsageDescription"]),
    ("reminders", r"requestFullAccessToReminders|requestAccess\(to:\s*\.reminder",
     ["NSRemindersFullAccessUsageDescription", "NSRemindersUsageDescription"]),
    ("tracking (ATT)", r"\bATTrackingManager\b|requestTrackingAuthorization", ["NSUserTrackingUsageDescription"]),
    ("Face ID", r"\bLAContext\b", ["NSFaceIDUsageDescription"]),
    ("speech recognition", r"\bSFSpeechRecognizer\b", ["NSSpeechRecognitionUsageDescription"]),
    ("motion activity", r"\bCMMotionActivityManager\b|\bCMPedometer\b|\bCMAltimeter\b", ["NSMotionUsageDescription"]),
    ("health", r"\bHKHealthStore\b", ["NSHealthShareUsageDescription", "NSHealthUpdateUsageDescription"]),
    ("bluetooth", r"\bCBCentralManager\b|\bCBPeripheralManager\b", ["NSBluetoothAlwaysUsageDescription"]),
    ("local network", r"\bNWBrowser\b|\bNetServiceBrowser\b|\bMCNearbyServiceBrowser\b|\bMCNearbyServiceAdvertiser\b",
     ["NSLocalNetworkUsageDescription"]),
    ("media library", r"\bMPMediaLibrary\b|\bMPMediaQuery\b", ["NSAppleMusicUsageDescription"]),
    ("Game Center friends", r"\bloadFriends\b|loadFriendsAuthorizationStatus", ["NSGKFriendListUsageDescription"]),
    ("Siri", r"requestSiriAuthorization", ["NSSiriUsageDescription"]),
]
# Web code running inside a WKWebView wrapper triggers the same system prompts.
WEB_PERMISSIONS = [
    ("camera (web view getUserMedia)", r"getUserMedia\s*\(\s*\{[^}]*\bvideo\b", ["NSCameraUsageDescription"]),
    ("microphone (web view getUserMedia)", r"getUserMedia\s*\(\s*\{[^}]*\baudio\b", ["NSMicrophoneUsageDescription"]),
    ("location (web view geolocation)", r"navigator\.geolocation\.(getCurrentPosition|watchPosition)",
     ["NSLocationWhenInUseUsageDescription"]),
]
# Official Capacitor plugin READMEs (npm, read 2026-10-12): Info.plist keys and privacy manifest categories.
CAPACITOR_PLUGIN_KEYS = {
    "@capacitor/camera": ["NSCameraUsageDescription", "NSPhotoLibraryUsageDescription", "NSPhotoLibraryAddUsageDescription"],
    "@capacitor/geolocation": ["NSLocationWhenInUseUsageDescription", "NSLocationAlwaysAndWhenInUseUsageDescription"],
    "@capacitor/barcode-scanner": ["NSCameraUsageDescription"],
}
CAPACITOR_PLUGIN_REASONS = {
    "@capacitor/preferences": ("NSPrivacyAccessedAPICategoryUserDefaults", "CA92.1"),
    "@capacitor/filesystem": ("NSPrivacyAccessedAPICategoryFileTimestamp", "C617.1"),
}
# Required reason API categories (Apple, NSPrivacyAccessedAPIType, read 2026-10-12).
REASON_APIS = [
    ("NSPrivacyAccessedAPICategoryUserDefaults", r"\bUserDefaults\b|\bNSUserDefaults\b|@AppStorage\b"),
    ("NSPrivacyAccessedAPICategoryFileTimestamp",
     r"FileAttributeKey\.(creationDate|modificationDate)|\.fileModificationDate\b|contentModificationDateKey|"
     r"creationDateKey|NSFileModificationDate|NSFileCreationDate|\bgetattrlist(bulk)?\b"),
    ("NSPrivacyAccessedAPICategorySystemBootTime", r"\bsystemUptime\b|\bmach_absolute_time\b"),
    ("NSPrivacyAccessedAPICategoryDiskSpace", r"volumeAvailableCapacity|volumeTotalCapacity|NSFileSystemFreeSize|"
                                              r"NSFileSystemSize|\bstatv?fs\("),
    ("NSPrivacyAccessedAPICategoryActiveKeyboards", r"\bactiveInputModes\b"),
]
# A subset of Apple's "SDKs that require a privacy manifest and signature" (86 entries, read 2026-10-12).
LISTED_SDKS = {"Abseil", "AFNetworking", "Alamofire", "AppAuth", "BoringSSL-GRPC", "Capacitor", "Charts", "Cordova",
               "FBAEMKit", "FBLPromises", "FBSDKCoreKit", "FBSDKCoreKit_Basics", "FBSDKLoginKit", "FBSDKShareKit",
               "FirebaseABTesting", "FirebaseAuth", "FirebaseCore", "FirebaseCoreDiagnostics", "FirebaseCoreExtension",
               "FirebaseCoreInternal", "FirebaseCrashlytics", "FirebaseDynamicLinks", "FirebaseFirestore",
               "FirebaseInstallations", "FirebaseMessaging", "FirebaseRemoteConfig", "Flutter", "FMDB",
               "GoogleDataTransport", "GoogleSignIn", "GoogleToolboxForMac", "GoogleUtilities", "GTMAppAuth",
               "GTMSessionFetcher", "hermes", "IQKeyboardManager", "IQKeyboardManagerSwift", "Kingfisher", "leveldb",
               "Lottie", "lottie-ios", "MBProgressHUD", "nanopb", "OneSignal", "OneSignalCore", "OneSignalExtension",
               "OneSignalOutcomes", "OpenSSL", "OrderedSet", "PromisesObjC", "Protobuf", "Reachability", "RealmSwift",
               "RxCocoa", "RxRelay", "RxSwift", "SDWebImage", "SnapKit", "Starscream", "SVProgressHUD", "SwiftyGif",
               "SwiftyJSON", "Toast", "UnityFramework"}

GOOGLE_SIGNIN = {
    "deps": {"@codetrix-studio/capacitor-google-auth", "@react-native-google-signin/google-signin",
             "@capacitor-firebase/authentication", "@capgo/capacitor-social-login"},
    "pods": {"GoogleSignIn"},
    "code": r"\bGIDSignIn\b|\bGoogleAuthProvider\b|\bsignInWithGoogle\b|\bGoogleAuth\.signIn\b",
}
FACEBOOK_LOGIN = {
    "deps": {"@capacitor-community/facebook-login", "react-native-fbsdk-next"},
    "pods": {"FBSDKLoginKit", "FacebookLogin"},
    "code": r"\bFacebookAuthProvider\b|\bFBSDKLoginManager\b|\bLoginManager\(\)\.logIn|\bFacebookLogin\.login\b",
}
SIWA = {
    "deps": {"@capacitor-community/apple-sign-in", "@invertase/react-native-apple-authentication",
             "expo-apple-authentication"},
    "code": r"\bASAuthorizationAppleIDProvider\b|\bSignInWithAppleButton\b|\bAppleAuthProvider\b|"
            r"OAuthProvider\(\s*['\"]apple\.com|\bSignInWithApple\.authorize\b",
}
PLACEHOLDER = re.compile(r"<[^>]*>|\bTODO\b|\bTBD\b|lorem ipsum|\bFIXME\b", re.I)
VAGUE = re.compile(r"better experience|improve (your|the) experience|needs? (access|permission)|"
                   r"^(this )?app (uses|requires|needs) (the |your )?\w+\.?$|^to use (the |your )?\w+\.?$", re.I)
FINGERPRINT = re.compile(r"^([0-9A-F]{2}:){31}[0-9A-F]{2}$", re.I)
NOTES_LIMIT_BYTES = 4000

# Dossier keys. The template in references/submission-dossier-template.md must contain every one.
K = {
    "store": "Store",
    "behind_sign_in": "Features behind sign in",
    "demo_user": "Demo account username",
    "demo_secret": "Demo account password stored in",
    "demo_non_expiring": "Demo account never expires",
    "demo_expired_sub": "Expired subscription demo account",
    "backend": "Backend live during review",
    "accounts": "Account creation",
    "deletion_path": "Account deletion path in app",
    "deletion_web": "Account deletion web link",
    "privacy_url": "Privacy policy URL",
    "privacy_in_app": "Privacy policy link in app",
    "support_url": "Support URL",
    "ads": "Contains ads",
    "iap": "In-app purchases",
    "subs": "Auto-renewable subscriptions",
    "restore": "Restore purchases path",
    "random": "Paid random items",
    "odds": "Odds shown before purchase at",
    "age_rating": "Age rating questionnaire answered",
    "social_media": "Social media question answered",
    "export": "Export compliance answered",
    "siwa": "Sign in with Apple",
}
NOTES_HEADING = "review notes"


class Report:
    def __init__(self) -> None:
        self.lines: list[tuple[str, str, str]] = []
        self.unseen: list[str] = []

    def add(self, level: str, area: str, msg: str) -> None:
        self.lines.append((level, area, msg))

    def fails(self) -> int:
        return sum(1 for lvl, _, _ in self.lines if lvl == "FAIL")


# ---------- file helpers ----------

def walk(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        rel = os.path.relpath(dirpath, root)
        dirnames[:] = sorted(d for d in dirnames
                             if d not in SKIP_DIRS and not d.endswith(SKIP_SUFFIXES)
                             and not any(os.path.join(rel, d).replace("./", "").endswith(c) for c in COPIED_WEB))
        for name in sorted(filenames):
            yield os.path.join(dirpath, name)


def read(path: str) -> str:
    try:
        if os.path.getsize(path) > MAX_BYTES:
            return ""
        with open(path, encoding="utf-8", errors="ignore") as fh:
            return fh.read()
    except OSError:
        return ""


def load_plist(path: str) -> dict | None:
    try:
        with open(path, "rb") as fh:
            data = plistlib.load(fh)
        return data if isinstance(data, dict) else None
    except Exception:  # noqa: BLE001 (any parse error means "unreadable")
        return None


def package_deps(root: str) -> set[str]:
    deps: set[str] = set()
    for path in walk(root):
        if os.path.basename(path) == "package.json":
            try:
                data = json.loads(read(path) or "{}")
            except json.JSONDecodeError:
                continue
            for key in ("dependencies", "devDependencies"):
                if isinstance(data.get(key), dict):
                    deps.update(data[key])
    return deps


# ---------- iOS ----------

def ios_inventory(root: str) -> dict:
    inv = {"xcodeproj": [], "plists": [], "pbx": [], "manifests": [], "entitlements": [], "native": [], "web": [],
           "pods": set(), "capacitor": False}
    for path in walk(root):
        rel = os.path.relpath(path, root)
        name = os.path.basename(path)
        parts = rel.split(os.sep)
        if any(p.endswith(".xcodeproj") for p in parts[:-1]):
            if name == "project.pbxproj":
                inv["pbx"].append(path)
                inv["xcodeproj"].append(os.path.dirname(path))
            continue
        if any(p.endswith(("Tests", "UITests")) for p in parts[:-1]):
            continue
        if name == "Info.plist":
            inv["plists"].append(path)
        elif name == "PrivacyInfo.xcprivacy":
            inv["manifests"].append(path)
        elif name.endswith(".entitlements"):
            inv["entitlements"].append(path)
        elif name in ("Podfile.lock", "Package.resolved"):
            text = read(path)
            inv["pods"].update(re.findall(r"^\s*-\s+([A-Za-z0-9_+-]+)", text, re.M))
            inv["pods"].update(re.findall(r'"identity"\s*:\s*"([^"]+)"', text))
        elif name.startswith("capacitor.config."):
            inv["capacitor"] = True
        elif name.endswith(NATIVE_EXT):
            inv["native"].append(path)
        elif name.endswith(WEB_EXT):
            inv["web"].append(path)
    return inv


def plist_keys(inv: dict) -> dict[str, object]:
    keys: dict[str, object] = {}
    for path in inv["plists"]:
        data = load_plist(path)
        if data is not None:
            for k, v in data.items():
                keys.setdefault(k, v)
    for path in inv["pbx"]:
        for k, v in re.findall(r"INFOPLIST_KEY_([A-Za-z0-9_]+)\s*=\s*\"?([^\";\n]*)\"?;", read(path)):
            keys.setdefault(k, v)
    return keys


def check_purpose_string(key: str, value: object, rep: Report) -> None:
    text = str(value).strip() if value is not None else ""
    if not text:
        rep.add("FAIL", "ios", f"{key} is empty (Guideline 5.1.1(ii): explain the specific use)")
    elif PLACEHOLDER.search(text):
        rep.add("FAIL", "ios", f"{key} is a placeholder: '{text[:60]}' (Guideline 2.1(a) placeholder content)")
    elif len(text) < 20 or len(text.split()) < 4 or VAGUE.search(text):
        rep.add("WARN", "ios", f"{key} looks vague: '{text[:80]}' (name the feature and give an example, Apple purpose string page)")


def check_ios(root: str, deps: set[str], dossier: dict | None, rep: Report) -> dict:
    inv = ios_inventory(root)
    info = {"present": bool(inv["xcodeproj"] or inv["plists"]), "export_in_plist": False}
    if not info["present"]:
        rep.unseen.append("No iOS project found (no .xcodeproj or Info.plist): iOS checks skipped")
        return info
    keys = plist_keys(inv)
    if not inv["plists"]:
        rep.unseen.append("No Info.plist file: keys were read from INFOPLIST_KEY_ build settings only")
    capacitor = inv["capacitor"] or "@capacitor/ios" in deps or "@capacitor/core" in deps
    native_text = {p: read(p) for p in inv["native"]}
    web_text = {p: read(p) for p in inv["web"]} if capacitor else {}

    # Purpose strings needed by code and plugins.
    needed: dict[tuple[str, ...], list[str]] = {}
    for resource, rx, accepted in NATIVE_PERMISSIONS:
        hits = [os.path.relpath(p, root) for p, t in native_text.items() if re.search(rx, t)]
        if hits:
            needed.setdefault(tuple(accepted), []).append(f"{resource} in {hits[0]}")
    for resource, rx, accepted in WEB_PERMISSIONS:
        hits = [os.path.relpath(p, root) for p, t in web_text.items() if re.search(rx, t)]
        if hits:
            needed.setdefault(tuple(accepted), []).append(f"{resource} in {hits[0]}")
    for dep, plugin_keys in CAPACITOR_PLUGIN_KEYS.items():
        if dep in deps:
            for key in plugin_keys:
                needed.setdefault((key,), []).append(f"plugin {dep}")
    if capacitor and any("getUserMedia" in t for t in web_text.values()) and not any(
            re.search(rx, t) for _, rx, _ in WEB_PERMISSIONS[:2] for t in web_text.values()):
        rep.add("WARN", "ios", "getUserMedia is called with constraints the script cannot read: confirm camera and microphone purpose strings")
    for accepted, why in sorted(needed.items()):
        present = [k for k in accepted if k in keys]
        if not present:
            rep.add("FAIL", "ios", f"missing purpose string {' or '.join(accepted)} (used by {why[0]}; Guideline 5.1.1(ii); "
                                   "the app crashes or is rejected without it)")
        for k in present:
            check_purpose_string(k, keys[k], rep)
    for k in sorted(keys):
        if k.endswith("UsageDescription") and not any(k in acc for acc in needed):
            check_purpose_string(k, keys[k], rep)
            rep.add("INFO", "ios", f"{k} is declared but no use was found in source: remove it if no SDK needs it (Guideline 5.1.1(iii))")

    # Privacy manifest and required reason APIs.
    used: dict[str, str] = {}
    for category, rx in REASON_APIS:
        for p, t in native_text.items():
            if re.search(rx, t):
                used.setdefault(category, f"code in {os.path.relpath(p, root)}")
                break
    for dep, (category, reason) in CAPACITOR_PLUGIN_REASONS.items():
        if dep in deps:
            used.setdefault(category, f"plugin {dep} (recommended reason {reason})")
    app_manifests = [m for m in inv["manifests"] if "node_modules" not in m]
    if not app_manifests:
        rep.add("FAIL", "ios", "PrivacyInfo.xcprivacy not found in the app (privacy manifest; required reason APIs "
                               "must be declared since 2024-05-01)")
    else:
        declared: set[str] = set()
        for m in app_manifests:
            data = load_plist(m)
            if data is None:
                rep.add("FAIL", "ios", f"{os.path.relpath(m, root)} does not parse as a property list")
                continue
            for entry in data.get("NSPrivacyAccessedAPITypes", []) or []:
                if isinstance(entry, dict) and entry.get("NSPrivacyAccessedAPITypeReasons"):
                    declared.add(str(entry.get("NSPrivacyAccessedAPIType")))
            if data.get("NSPrivacyTracking") is True and not data.get("NSPrivacyTrackingDomains"):
                rep.add("WARN", "ios", "NSPrivacyTracking is true but NSPrivacyTrackingDomains is empty")
        for category, why in sorted(used.items()):
            if category not in declared:
                rep.add("FAIL", "ios", f"privacy manifest lacks {category} with a reason (used by {why})")
        pbx_text = " ".join(read(p) for p in inv["pbx"])
        if inv["pbx"] and "PrivacyInfo.xcprivacy" not in pbx_text:
            rep.add("WARN", "ios", "PrivacyInfo.xcprivacy exists but the Xcode project does not reference it: add it to "
                                   "the app target's resources")
    found_sdks = sorted((inv["pods"] | ({"Capacitor"} if capacitor else set())) & LISTED_SDKS)
    if found_sdks:
        rep.add("INFO", "ios", "SDKs on Apple's privacy manifest and signature list: " + ", ".join(found_sdks)
                + " (ship versions that include their manifests; read the Xcode privacy report)")

    # Export compliance.
    if "ITSAppUsesNonExemptEncryption" in keys:
        info["export_in_plist"] = True
        val = str(keys["ITSAppUsesNonExemptEncryption"]).lower()
        if val in ("true", "yes", "1") and "ITSEncryptionExportComplianceCode" not in keys:
            rep.add("WARN", "ios", "ITSAppUsesNonExemptEncryption is YES without ITSEncryptionExportComplianceCode: "
                                   "upload export documentation in App Store Connect first")
    else:
        answered = dossier is not None and yes(dossier["fields"].get(K["export"].lower(), ""))
        if answered:
            rep.add("WARN", "ios", "ITSAppUsesNonExemptEncryption not in Info.plist: App Store Connect will ask the export "
                                   "questions on every upload; add the key")
        else:
            rep.add("FAIL", "ios", "export compliance not declared: no ITSAppUsesNonExemptEncryption key and the dossier does "
                                   "not say the questions are answered")

    # Sign in with Apple (Guideline 4.8).
    all_text = " ".join(native_text.values()) + " " + " ".join(web_text.values())
    social = []
    for label, spec in (("Google", GOOGLE_SIGNIN), ("Facebook", FACEBOOK_LOGIN)):
        if deps & spec["deps"] or inv["pods"] & spec["pods"] or re.search(spec["code"], all_text):
            social.append(label)
    siwa_entitlement = any("com.apple.developer.applesignin" in read(e) for e in inv["entitlements"])
    siwa_code = bool(deps & SIWA["deps"] or re.search(SIWA["code"], all_text))
    if social and not (siwa_entitlement or siwa_code):
        exception = dossier["fields"].get(K["siwa"].lower(), "") if dossier else ""
        if exception and not blank(exception) and re.search(r"not required|exception|exempt", exception, re.I):
            rep.add("WARN", "ios", f"{' and '.join(social)} sign in without Sign in with Apple; dossier claims a 4.8 exception: "
                                   f"'{exception[:80]}' (confirm the exception applies)")
        else:
            rep.add("FAIL", "ios", f"{' and '.join(social)} sign in found but no Sign in with Apple (Guideline 4.8: offer an "
                                   "equivalent privacy preserving login, or record the exception in the dossier)")
    if re.search(r"\bASAuthorizationAppleIDProvider\b", all_text) and not siwa_entitlement:
        rep.add("WARN", "ios", "Sign in with Apple code without com.apple.developer.applesignin in an .entitlements file")
    return info


# ---------- Android ----------

def resolve_number(name: str, texts: list[str]) -> int | None:
    short = name.split(".")[-1]
    for text in texts:
        m = re.search(r"\b" + re.escape(short) + r"\b\s*[=:]?\s*['\"]?(\d{2})['\"]?", text)
        if m:
            return int(m.group(1))
    return None


def check_android(root: str, rep: Report) -> dict:
    gradle, manifests, toml, props, twa_manifest, assetlinks = [], [], [], [], [], []
    for path in walk(root):
        name = os.path.basename(path)
        if name in ("build.gradle", "build.gradle.kts"):
            gradle.append(path)
        elif name == "AndroidManifest.xml":
            manifests.append(path)
        elif name.endswith(".versions.toml") or name in ("variables.gradle", "gradle.properties"):
            (toml if name.endswith(".toml") else props).append(path)
        elif name == "twa-manifest.json":
            twa_manifest.append(path)
        elif name == "assetlinks.json" and os.path.basename(os.path.dirname(path)) == ".well-known":
            assetlinks.append(path)
    info = {"present": bool(gradle or manifests)}
    if not info["present"]:
        rep.unseen.append("No Android project found (no build.gradle or AndroidManifest.xml): Android checks skipped")
        return info
    gtexts = {p: read(p) for p in gradle}
    support = [read(p) for p in props + toml] + list(gtexts.values())
    app_modules = [p for p, t in gtexts.items() if re.search(r"com\.android\.application|applicationId", t)]

    # targetSdk.
    targets: list[tuple[int, str]] = []
    unresolved: list[str] = []
    for p in app_modules or list(gtexts):
        for m in re.finditer(r"targetSdk(?:Version)?\s*(?:=|\s)\s*([\w.()\"']+)", gtexts[p]):
            raw = m.group(1).strip("\"'()")
            num = int(raw) if raw.isdigit() else resolve_number(raw.replace("libs.versions.", ""), support)
            if num is None:
                unresolved.append(f"{raw} in {os.path.relpath(p, root)}")
            else:
                targets.append((num, os.path.relpath(p, root)))
    for p in manifests:
        m = re.search(r"android:targetSdkVersion\s*=\s*\"(\d+)\"", read(p))
        if m:
            targets.append((int(m.group(1)), os.path.relpath(p, root)))
    min_sdk = rep_min_target
    if targets:
        for num, where in sorted(set(targets)):
            if num < min_sdk:
                rep.add("FAIL", "android", f"targetSdk {num} in {where}; Google Play requires {min_sdk} or higher for new apps "
                                           "and updates (phones and tablets, since 2026-08-31; Wear OS and Automotive 35, TV and XR 34)")
    elif unresolved:
        rep.add("WARN", "android", f"targetSdk set through a value the script could not resolve: {', '.join(unresolved)}")
        rep.unseen.append("targetSdk value not resolved: read it in Android Studio or the merged manifest")
    else:
        rep.add("WARN", "android", "no targetSdk found in Gradle files or AndroidManifest.xml")
        rep.unseen.append("targetSdk not found")

    # Play Billing Library.
    all_g = "\n".join(gtexts.values()) + "\n" + "\n".join(read(p) for p in toml)
    versions = [int(v) for v in re.findall(r"com\.android\.billingclient:billing(?:-ktx)?:(\d+)", all_g)]
    for tp in toml:
        ttext = read(tp)
        for ref in re.findall(r"com\.android\.billingclient:billing(?:-ktx)?\"[^\n]*version\.ref\s*=\s*\"([^\"]+)\"", ttext):
            m = re.search(r"^\s*" + re.escape(ref) + r"\s*=\s*\"(\d+)", ttext, re.M)
            if m:
                versions.append(int(m.group(1)))
    for v in sorted(set(versions)):
        if v < 8:
            rep.add("FAIL", "android", f"Play Billing Library {v}.x: new apps and updates need version 8 or later since "
                                       "2026-08-31 (extension to 2026-11-01 on request)")
    if not versions and re.search(r"billingclient|revenuecat|purchases-android|adapty|qonversion", all_g, re.I):
        rep.unseen.append("Billing comes through a wrapper SDK: confirm the Play Billing Library version it bundles")

    # Trusted Web Activity and Digital Asset Links.
    manifest_text = " ".join(read(p) for p in manifests)
    is_twa = bool(twa_manifest) or "com.google.androidbrowserhelper" in all_g or "customtabs.trusted" in manifest_text
    info["twa"] = is_twa
    if is_twa:
        package = None
        for p in twa_manifest:
            try:
                package = json.loads(read(p)).get("packageId") or package
            except json.JSONDecodeError:
                pass
        if not package:
            m = re.search(r"applicationId\s*=?\s*[\"']([\w.]+)[\"']", all_g)
            package = m.group(1) if m else None
        if not assetlinks:
            rep.add("FAIL", "android", "Trusted Web Activity without .well-known/assetlinks.json in the repo: without Digital "
                                       "Asset Links the app opens as a Custom Tab with browser UI")
            rep.unseen.append("If assetlinks.json is served from another repo, check it there and on the live domain")
        else:
            check_assetlinks(assetlinks, package, root, rep)
    return info


def check_assetlinks(paths: list[str], package: str | None, root: str, rep: Report) -> None:
    ok = False
    for path in paths:
        try:
            data = json.loads(read(path))
        except json.JSONDecodeError:
            rep.add("FAIL", "android", f"{os.path.relpath(path, root)} is not valid JSON")
            continue
        for st in data if isinstance(data, list) else []:
            target = st.get("target", {}) if isinstance(st, dict) else {}
            if "delegate_permission/common.handle_all_urls" not in (st.get("relation") or []):
                continue
            if target.get("namespace") != "android_app":
                continue
            if package and target.get("package_name") != package:
                continue
            prints = target.get("sha256_cert_fingerprints") or []
            bad = [f for f in prints if not FINGERPRINT.match(str(f))]
            if not prints or bad:
                rep.add("FAIL", "android", f"assetlinks.json: SHA-256 fingerprints missing or malformed {bad[:1]}")
                continue
            ok = True
            if len(prints) == 1:
                rep.add("WARN", "android", "assetlinks.json has one fingerprint: confirm it is the app signing key from Play "
                                           "Console (Release > Setup > App signing); add the upload key too if you test locally signed builds")
    if not ok and not any(lvl == "FAIL" and "assetlinks" in msg for lvl, _, msg in rep.lines):
        rep.add("FAIL", "android", f"assetlinks.json has no handle_all_urls statement for package {package or '(unknown)'}")


# ---------- dossier ----------

def blank(value: str) -> bool:
    v = (value or "").strip()
    return not v or bool(PLACEHOLDER.search(v)) or v.lower() in {"?", "-", "...", "xxx", "n", "none yet"}


def yes(value: str) -> bool:
    return not blank(value) and value.strip().lower().startswith("yes")


def no(value: str) -> bool:
    return not blank(value) and value.strip().lower().startswith("no")


def na(value: str) -> bool:
    return not blank(value) and value.strip().lower().startswith(("n/a", "not applicable", "not required"))


def parse_dossier(text: str) -> dict:
    fields: dict[str, str] = {}
    sections: dict[str, list[str]] = {}
    current = None
    in_code = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code = not in_code
            if current is not None:
                sections[current].append(line)
            continue
        h = re.match(r"^#{2,3}\s+(.*)$", line)
        if h and not in_code:
            current = re.sub(r"^\d+[.)]?\s*", "", h.group(1)).strip().lower()
            sections.setdefault(current, [])
            continue
        if current is not None:
            sections[current].append(line)
        if in_code:
            continue
        m = re.match(r"^\s*[-*]\s+\**([^:*\n]{2,80}?)\**\s*:\s*(.*)$", line)
        if m:
            key = re.sub(r"\s+", " ", m.group(1).replace("`", "")).strip().lower()
            fields.setdefault(key, m.group(2).strip())
    return {"fields": fields, "sections": {k: "\n".join(v).strip() for k, v in sections.items()}}


def stores_in_scope(store_flag: str | None, fields: dict[str, str], ios: bool, android: bool) -> set[str]:
    if store_flag:
        return {"apple", "google"} if store_flag == "both" else {store_flag}
    value = fields.get(K["store"].lower(), "").lower()
    found = {s for s, words in (("apple", ("apple", "app store", "ios")), ("google", ("google", "play", "android")))
             if any(w in value for w in words)}
    if "both" in value:
        found = {"apple", "google"}
    if not found:
        found = ({"apple"} if ios else set()) | ({"google"} if android else set())
    return found


def check_dossier(d: dict, stores: set[str], policy: dict | None, rep: Report) -> None:
    f = d["fields"]

    def get(name: str) -> str:
        return f.get(K[name].lower(), "")

    def need(name: str, why: str) -> None:
        if blank(get(name)):
            rep.add("FAIL", "dossier", f"'{K[name]}' is missing or a placeholder ({why})")

    def answer(name: str, why: str) -> bool:
        if not (yes(get(name)) or no(get(name)) or na(get(name))):
            rep.add("FAIL", "dossier", f"'{K[name]}' needs a yes or no answer ({why})")
            return False
        return True

    need("store", "which store this submission goes to")
    apple, google = "apple" in stores, "google" in stores
    if answer("behind_sign_in", "decides whether App Review needs a demo account"):
        if yes(get("behind_sign_in")):
            need("demo_user", "Guideline 2.1(a): demo account info")
            need("demo_secret", "name the vault entry; never paste the password into the workspace")
            if not yes(get("demo_non_expiring")):
                rep.add("FAIL", "dossier", f"'{K['demo_non_expiring']}' must be yes (expired credentials get the build rejected)")
            if apple and yes(get("subs")):
                need("demo_expired_sub", "Apple asks for an account with an expired subscription to review the purchase flow")
    if not (yes(get("backend")) or na(get("backend"))):
        rep.add("FAIL", "dossier", f"'{K['backend']}' must be yes, or n/a when the app has no backend (Guideline 2.1(a))")

    notes = next((body for title, body in d["sections"].items() if NOTES_HEADING in title), None)
    if notes is None or blank(re.sub(r"^\s*>.*$", "", notes, flags=re.M)) or PLACEHOLDER.search(notes):
        rep.add("FAIL", "dossier", "review notes section missing, empty or still holding <placeholders>")
    else:
        size = len(notes.encode("utf-8"))
        if size > NOTES_LIMIT_BYTES:
            rep.add("FAIL", "dossier", f"review notes are {size} bytes; App Store Connect takes up to {NOTES_LIMIT_BYTES}")
        elif len(notes) < 200:
            rep.add("WARN", "dossier", "review notes are under 200 characters: say what the app does, how to test it and where")

    if answer("accounts", "decides account deletion duties"):
        if yes(get("accounts")):
            need("deletion_path", "Guideline 5.1.1(v): deletion must start inside the app")
            if google and not get("deletion_web").startswith("https://"):
                rep.add("FAIL", "dossier", f"'{K['deletion_web']}' needs an https URL (Google Play asks for a web deletion link)")
    url = get("privacy_url")
    if not url.startswith(("https://", "http://")):
        rep.add("FAIL", "dossier", f"'{K['privacy_url']}' needs a URL (Guideline 5.1.1(i); Play user data policy)")
    elif url.startswith("http://"):
        rep.add("WARN", "dossier", "privacy policy URL is not https")
    if apple:
        need("privacy_in_app", "Guideline 5.1.1(i): a link inside the app too")
    if not get("support_url").startswith(("https://", "http://")):
        rep.add("FAIL" if apple else "WARN", "dossier", f"'{K['support_url']}' needs a URL with real contact information")
    answer("ads", "Play 'Contains ads' declaration and the Apple age rating advertising question")

    has_iap = yes(get("iap"))
    if answer("iap", "decides restore and paywall checks"):
        if has_iap:
            restore = get("restore")
            if blank(restore):
                rep.add("FAIL", "dossier", f"'{K['restore']}' is missing (Guideline 3.1.1: restore for restorable purchases)")
            elif na(restore):
                rep.add("WARN", "dossier", "restore marked n/a: valid only when every product is a consumable")
            answer("subs", "subscriptions need paywall disclosures")
    if yes(get("subs")) and not has_iap:
        rep.add("FAIL", "dossier", "auto-renewable subscriptions marked yes but in-app purchases marked no")
    if answer("random", "paid random items need odds before purchase") and yes(get("random")):
        need("odds", "Guideline 3.1.1 and Google Play: odds before purchase")
    if not yes(get("age_rating")):
        rep.add("FAIL", "dossier", f"'{K['age_rating']}' must be yes (Apple questionnaire, Google Play IARC)")
    if apple and not yes(get("social_media")):
        rep.add("FAIL", "dossier", f"'{K['social_media']}' must be yes (required on Apple submissions since 2026-09)")
    if policy is not None:
        check_policy(policy, f, rep)


def check_policy(policy: dict, f: dict[str, str], rep: Report) -> None:
    def val(name: str) -> str:
        return f.get(K[name].lower(), "")

    decl = policy.get("storeDeclarations") or {}
    store_ids = {s.get("id") for s in policy.get("stores", []) if isinstance(s, dict) and s.get("provider") in ("apple", "google")}
    store_ids = store_ids or {"apple", "google"}
    catalog = [c for c in policy.get("catalog", []) if isinstance(c, dict)]
    sold = [c for c in catalog if set((c.get("storeProductIds") or {})) & store_ids]
    checks = [
        ("ads", bool(decl.get("containsAds")), "storeDeclarations.containsAds"),
        ("iap", bool(decl.get("inAppPurchases")) or bool(sold), "storeDeclarations.inAppPurchases and store product ids"),
        ("subs", any(c.get("kind") == "subscription" for c in sold), "catalog subscriptions sold in a store"),
        ("random", bool(decl.get("lootBoxes")) or any(c.get("random") for c in catalog), "storeDeclarations.lootBoxes and random items"),
    ]
    for name, truth, source in checks:
        if truth and not yes(val(name)):
            rep.add("FAIL", "policy", f"dossier '{K[name]}' says '{val(name) or 'nothing'}' but the policy has it ({source})")
        elif not truth and yes(val(name)):
            rep.add("WARN", "policy", f"dossier '{K[name]}' says yes but the policy does not ({source}): fix whichever is wrong")
    if any(c.get("kind") in ("non_consumable", "subscription", "season") for c in sold) and na(val("restore")):
        rep.add("FAIL", "policy", "restore marked n/a but the catalog sells restorable products in a store")


# ---------- main ----------

rep_min_target = 36


def main(argv: list[str] | None = None) -> int:
    global rep_min_target
    ap = argparse.ArgumentParser(description="Static pre-submission check for app store review.")
    ap.add_argument("project", help="project root (native iOS, Capacitor, Android or TWA)")
    ap.add_argument("--dossier", help="SUBMISSION.md (default: <project>/ads-master/SUBMISSION.md or <project>/SUBMISSION.md)")
    ap.add_argument("--policy", help="monetization-policy.json to cross check store declarations")
    ap.add_argument("--store", choices=["apple", "google", "both"], help="override the dossier's Store field")
    ap.add_argument("--min-target-sdk", type=int, default=36)
    args = ap.parse_args(argv)
    rep_min_target = args.min_target_sdk

    root = os.path.abspath(args.project)
    if not os.path.isdir(root):
        print(f"ERROR project folder not found: {args.project}")
        print(CANNOT_COVER)
        return 2
    dossier_path = args.dossier
    if dossier_path and not os.path.isfile(dossier_path):
        print(f"ERROR dossier not found: {dossier_path}")
        print(CANNOT_COVER)
        return 2
    if not dossier_path:
        for cand in (os.path.join(root, "ads-master", "SUBMISSION.md"), os.path.join(root, "SUBMISSION.md")):
            if os.path.isfile(cand):
                dossier_path = cand
                break
    policy = None
    if args.policy:
        try:
            with open(args.policy, encoding="utf-8") as fh:
                policy = json.load(fh)
            if not isinstance(policy, dict):
                raise ValueError("not an object")
        except (OSError, ValueError) as exc:
            print(f"ERROR policy file unreadable: {exc}")
            print(CANNOT_COVER)
            return 2

    rep = Report()
    dossier = None
    if dossier_path:
        with open(dossier_path, encoding="utf-8", errors="ignore") as fh:
            dossier = parse_dossier(fh.read())
    deps = package_deps(root)
    ios = check_ios(root, deps, dossier, rep)
    android = check_android(root, rep)
    if not ios["present"] and not android["present"] and dossier is None:
        print("ERROR nothing to check: no iOS project, no Android project and no dossier")
        print(CANNOT_COVER)
        return 2
    if dossier is None:
        rep.add("FAIL", "dossier", "no SUBMISSION.md found: build it from references/submission-dossier-template.md "
                                   "before every submission")
    else:
        stores = stores_in_scope(args.store, dossier["fields"], ios["present"], android["present"])
        check_dossier(dossier, stores, policy, rep)
        if "apple" in stores and not ios["present"]:
            need_export = not yes(dossier["fields"].get(K["export"].lower(), ""))
            if need_export:
                rep.add("FAIL", "dossier", f"'{K['export']}' must be yes for an App Store submission")
    if policy is not None and dossier is None:
        rep.unseen.append("Policy given without a dossier: declarations were not cross checked")

    order = {"FAIL": 0, "WARN": 1, "INFO": 2}
    for level, area, msg in sorted(rep.lines, key=lambda x: (order[x[0]], x[1])):
        print(f"{level} [{area}] {msg}")
    fails = rep.fails()
    warns = sum(1 for lvl, _, _ in rep.lines if lvl == "WARN")
    print(f"\nSummary: {fails} FAIL, {warns} WARN. Project: {root}. Dossier: {dossier_path or 'none'}.")
    if rep.unseen:
        print("Not seen in this run:")
        for item in rep.unseen:
            print(f"  - {item}")
    print(CANNOT_COVER)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
