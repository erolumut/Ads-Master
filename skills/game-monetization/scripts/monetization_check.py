#!/usr/bin/env python3
"""Check a game's monetization-policy.json against the Game Monetization Contract.

Fails (exit 1) when:
  - a required key is missing, or the contract major version is unknown
  - a ranked mode has no constant countedAttemptsPerDay
  - an offer or placement in a ranked mode can change a ranked result, or a
    ranked mode offer grants to the buyer something other than cosmetics,
    practice, archive or a pass (it must declare affectsRankedResult false)
  - a social mode offer grants to the buyer only (social grants go to the group)
  - an offer uses price escalation, or a countdown when the audience includes
    minors (minimumAge under 18) or the game is in kids mode
  - a progression continue or booster offer has no maxPerAttempt
  - an offer or placement names a mode or sku that does not exist
  - a catalog item lacks a price in a listed real money currency, or a platform
    id for a platform the game sells on (web or pwa: stripe, ios: apple,
    android: google)
  - a random item has no odds, odds do not sum to 1, or storeDeclarations does
    not declare loot boxes
  - a purchasable virtual currency does not show the real money price
  - an interstitial has no grace (levels or seconds), no cooldown or no session
    cap; a rewarded placement is not opt in or does not grant on completion; a
    banner sits on a point other than menu or loading
  - ads exist but consent is not required before ads, or kids mode with
    interstitials or app open ads
  - storeDeclarations disagree with the file (ads or purchases present but not
    declared)
Warnings: offers without a daily cap, rewarded without a daily cap, app open ads.

  python3 monetization_check.py policy.json

Exit codes: 0 pass, 1 fail, 2 could not run. Standard library only.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

CANNOT_COVER = ("This check cannot cover: whether the game's code actually follows the file (each game's "
                "conformance test does), live prices in the store consoles, the wording on screen, and laws "
                "that changed after the file was written.")
REQUIRED = ["contractVersion", "game", "currencies", "modes", "catalog", "offers", "placements", "consent",
            "storeDeclarations", "killSwitch"]
RANKED_SAFE_GRANTS = ("cosmetic", "practice", "archive", "season_pass", "plus", "theme")
BANNER_POINTS = {"onMenu", "onLoading"}
PLATFORM_KEY = {"web": "stripe", "pwa": "stripe", "ios": "apple", "android": "google"}


def check(policy: dict) -> tuple[list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []
    missing = [k for k in REQUIRED if k not in policy]
    if missing:
        return [f"missing required keys: {', '.join(missing)}"], warns
    version = str(policy["contractVersion"])
    if not version.startswith("0."):
        fails.append(f"contractVersion {version}: unknown major version for this checker (0.x)")

    game = policy["game"]
    audience = game.get("audience", {})
    minors = audience.get("minimumAge", 0) < 18
    kids = bool(audience.get("kidsMode"))
    platforms = set(game.get("platforms", []))

    modes = {m.get("id"): m for m in policy["modes"]}
    for mid, m in modes.items():
        if m.get("kind") == "ranked" and not isinstance(m.get("countedAttemptsPerDay"), int):
            fails.append(f"mode {mid}: ranked mode needs a constant integer countedAttemptsPerDay")

    catalog = {c.get("sku"): c for c in policy["catalog"]}
    real = policy["currencies"].get("realMoney", [])
    for sku, c in catalog.items():
        prices = c.get("prices", {})
        for cur in real:
            if not isinstance(prices.get(cur), (int, float)) or prices.get(cur, 0) <= 0:
                fails.append(f"sku {sku}: no real money price in {cur}")
        ids = c.get("platformIds", {})
        for p in sorted(platforms):
            key = PLATFORM_KEY.get(p)
            if key and not ids.get(key):
                fails.append(f"sku {sku}: no {key} id although the game sells on {p}")
        if c.get("random"):
            odds = c.get("odds") or {}
            if not odds:
                fails.append(f"sku {sku}: random item without odds (stores require odds before purchase)")
            elif not math.isclose(sum(odds.values()), 1.0, abs_tol=0.001):
                fails.append(f"sku {sku}: odds sum to {sum(odds.values()):.3f}, not 1")
            if not policy["storeDeclarations"].get("lootBoxes"):
                fails.append(f"sku {sku}: random item but storeDeclarations.lootBoxes is false (UK listings need the label)")
    for v in policy["currencies"].get("virtual", []):
        if v.get("purchasable") and not v.get("showRealMoneyPrice"):
            fails.append(f"virtual currency {v.get('id')}: purchasable but the real money price is not shown (EU CPC principles)")

    def mode_kind(mid: str, what: str) -> str | None:
        if mid not in modes:
            fails.append(f"{what}: mode '{mid}' is not declared in modes")
            return None
        return modes[mid].get("kind")

    for o in policy["offers"]:
        tag = f"offer {o.get('id')}"
        kind = mode_kind(o.get("mode"), tag)
        if o.get("sku") not in catalog:
            fails.append(f"{tag}: sku '{o.get('sku')}' is not in the catalog")
        if o.get("priceEscalation"):
            fails.append(f"{tag}: price escalation (each retry costs more) is a pressure pattern regulators target")
        if o.get("countdown") and (minors or kids):
            fails.append(f"{tag}: countdown or scarcity copy with an audience that includes minors")
        elif o.get("countdown"):
            warns.append(f"{tag}: countdown copy; make sure the deadline is real")
        if "maxPerDay" not in o and "maxPerAttempt" not in o:
            warns.append(f"{tag}: no maxPerDay or maxPerAttempt cap")
        if kind == "ranked":
            if o.get("affectsRankedResult") is not False:
                fails.append(f"{tag}: ranked mode offer must declare affectsRankedResult false")
            grants = catalog.get(o.get("sku"), {}).get("grants", [])
            if o.get("grantsTo") == "buyer" and not all(any(s in g for s in RANKED_SAFE_GRANTS) for g in grants):
                fails.append(f"{tag}: ranked mode offer grants {grants} to the buyer; only cosmetics, practice, archive or passes are allowed")
        if kind == "social" and o.get("grantsTo") != "group":
            fails.append(f"{tag}: social mode grants must go to the whole group")
        if kind == "progression" and "maxPerAttempt" not in o:
            fails.append(f"{tag}: progression offer (continue or booster) needs maxPerAttempt")

    has_ads = bool(policy["placements"])
    for p in policy["placements"]:
        tag = f"placement {p.get('id')}"
        kind = mode_kind(p.get("mode"), tag)
        fmt = p.get("format")
        if kind == "ranked" and p.get("affectsRankedResult") is not False:
            fails.append(f"{tag}: ranked mode placement must declare affectsRankedResult false")
        if fmt == "rewarded":
            if p.get("optIn") is not True:
                fails.append(f"{tag}: rewarded ads must be opt in")
            if p.get("grantOn") != "completed":
                fails.append(f"{tag}: rewarded ads grant only on completion")
            if "dailyCap" not in p:
                warns.append(f"{tag}: rewarded without a daily cap")
        elif fmt == "interstitial":
            if "graceLevels" not in p and "graceSeconds" not in p:
                fails.append(f"{tag}: interstitial needs a first session grace (graceLevels or graceSeconds)")
            if "cooldownSeconds" not in p:
                fails.append(f"{tag}: interstitial needs cooldownSeconds")
            if "sessionCap" not in p:
                fails.append(f"{tag}: interstitial needs a sessionCap")
            if kids:
                fails.append(f"{tag}: no interstitials in kids mode")
        elif fmt == "banner" and p.get("point") not in BANNER_POINTS:
            fails.append(f"{tag}: banners only on menu or loading points, never in play")
        elif fmt == "app_open":
            if kids:
                fails.append(f"{tag}: no app open ads in kids mode")
            warns.append(f"{tag}: app open ads have no public evidence for games yet; test against retention")

    consent = policy["consent"]
    if has_ads and consent.get("requiredBeforeAds") is not True:
        fails.append("consent.requiredBeforeAds must be true when the game shows ads")
    decl = policy["storeDeclarations"]
    if has_ads and not decl.get("containsAds"):
        fails.append("storeDeclarations.containsAds is false but the policy has ad placements")
    if catalog and not decl.get("inAppPurchases"):
        fails.append("storeDeclarations.inAppPurchases is false but the policy has a catalog")
    return fails, warns


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1 or args[0] in ("-h", "--help"):
        print(__doc__)
        return 2
    path = Path(args[0])
    try:
        policy = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"could not run: {path}: {exc}")
        print(CANNOT_COVER)
        return 2
    if not isinstance(policy, dict):
        print("could not run: the policy must be a JSON object")
        print(CANNOT_COVER)
        return 2
    fails, warns = check(policy)
    print(f"{policy.get('game', {}).get('id', '?')}: contract {policy.get('contractVersion', '?')}, "
          f"{len(policy.get('modes', []))} modes, {len(policy.get('catalog', []))} skus, "
          f"{len(policy.get('offers', []))} offers, {len(policy.get('placements', []))} placements")
    for f in fails:
        print("FAIL", f)
    for w in warns:
        print("WARN", w)
    print("Verdict: " + ("FAIL" if fails else "PASS"))
    print(CANNOT_COVER)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
