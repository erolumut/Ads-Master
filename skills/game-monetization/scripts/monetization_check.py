#!/usr/bin/env python3
"""Check a product's monetization-policy.json against the Game Monetization Contract 0.2.

The policy is per product (a store listing or a web app), which may contain
many games; mode ids may be namespaced ("wordgame:daily"). The checker derives
whether something can change a ranked result from typed grants and declared
boards; nothing is self declared.

Fails (exit 1) when:
  - a required key is missing (top level or per object), an id is duplicated,
    or a reference (mode, sku, store, board, virtual currency) does not exist
  - a ranked mode has no countedAttemptsPerDay (an integer or "unlimited") or
    no boards
  - an offer or placement in a ranked mode grants anything that changes play
    (attempt, moves, time, booster, lives, currency, streak_protection)
  - any grant writes to a ranked board unless it is a "round" whose grantsTo
    scope covers every board it writes to (a group round may write only to
    group boards; never to an "everyone" board)
  - a social mode offer grants to the buyer only
  - a rewarded placement has no grants, is not opt in, or does not grant on
    completion; an interstitial lacks grace, cooldown or session cap; a banner
    sits on a point other than on_menu or on_loading; interstitial or app open
    ads in kids mode
  - an offer uses price escalation, or two offers at the same mode and point
    sell the same grant kinds at different prices (escalation by siblings)
  - countdown copy when the audience includes minors or kids mode
  - a moves, time or booster offer has no maxPerAttempt
  - a catalog item lacks a store product id for a declared store, has a non
    integer or non positive basePrice, a subscription lacks a period
  - a random item has no odds, odds do not sum to 1, the store declarations do
    not declare loot boxes, the audience includes minors, or the product sells
    in Belgium (BE)
  - a purchasable virtual currency does not show the real money price
  - ads exist without consent required first; store declarations disagree with
    the file
Warnings: offers without caps, rewarded without a daily cap, app open ads.
Exit 2 when the file cannot be read or the contract version is not supported.

  python3 monetization_check.py policy.json

Standard library only.
"""
from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

SUPPORTED_VERSIONS = {"0.1", "0.2"}
CANNOT_COVER = ("This check cannot cover: whether the code follows the file (each product's conformance test "
                "does), derived boards the file does not declare, live prices in the store consoles, the wording "
                "on screen, tax and merchant of record duties, and laws that changed after the file was written.")
REQUIRED = ["contractVersion", "policyRevision", "product", "stores", "currencies", "modes", "catalog", "offers",
            "placements", "consent", "storeDeclarations", "killSwitch"]
OBJ_REQUIRED = {
    "store": ["id", "provider", "platforms"],
    "mode": ["id", "kind"],
    "catalog": ["sku", "kind", "grants", "basePrice", "storeProductIds", "random"],
    "offer": ["id", "point", "mode", "sku", "grantsTo", "countdown", "priceEscalation"],
    "placement": ["id", "format", "point", "mode"],
}
GRANT_KINDS = {"cosmetic", "access", "pass", "round", "attempt", "moves", "time", "booster", "currency", "lives",
               "streak_protection"}
PLAY_CHANGING = {"attempt", "moves", "time", "booster", "currency", "lives", "streak_protection"}
PER_ATTEMPT = {"moves", "time", "booster"}
SCOPE_RANK = {"buyer": 0, "group": 1, "everyone": 2}
BANNER_POINTS = {"on_menu", "on_loading"}
POINT_RE = re.compile(r"^(on_[a-z0-9_]+|custom_[a-z0-9_]+)$")


def _req(obj: dict, kind: str, tag: str, fails: list[str]) -> bool:
    missing = [k for k in OBJ_REQUIRED[kind] if k not in obj]
    if missing:
        fails.append(f"{tag}: missing {', '.join(missing)}")
    return not missing


def _dupes(items: list[dict], key: str, what: str, fails: list[str]) -> None:
    for value, n in Counter(i.get(key) for i in items).items():
        if n > 1:
            fails.append(f"duplicate {what} id '{value}'")


def check(policy: dict) -> tuple[list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []
    missing = [k for k in REQUIRED if k not in policy]
    if missing:
        return [f"missing required keys: {', '.join(missing)}"], warns

    product = policy["product"]
    audience = product.get("audience", {})
    minors = audience.get("minimumAge", 0) < 18
    kids = bool(audience.get("kidsMode"))
    regions = set(product.get("regions", []))

    stores = policy["stores"]
    _dupes(stores, "id", "store", fails)
    store_ids = {s.get("id") for s in stores if _req(s, "store", f"store {s.get('id')}", fails)}

    virtual = {v.get("id"): v for v in policy["currencies"].get("virtual", [])}
    for vid, v in virtual.items():
        if v.get("purchasable") and not v.get("showRealMoneyPrice"):
            fails.append(f"virtual currency {vid}: purchasable but the real money price is not shown (EU CPC principles)")

    modes = policy["modes"]
    _dupes(modes, "id", "mode", fails)
    mode_by_id: dict[str, dict] = {}
    board_scope: dict[str, str] = {}
    ranked_boards: set[str] = set()
    for m in modes:
        tag = f"mode {m.get('id')}"
        if not _req(m, "mode", tag, fails):
            continue
        mode_by_id[m["id"]] = m
        if m["kind"] not in ("ranked", "practice", "social", "progression"):
            fails.append(f"{tag}: unknown kind '{m['kind']}'")
        for b in m.get("boards", []):
            board_scope[b.get("id")] = b.get("scope")
            if m["kind"] == "ranked":
                ranked_boards.add(b.get("id"))
        if m["kind"] == "ranked":
            cap = m.get("countedAttemptsPerDay")
            if not ((isinstance(cap, int) and cap > 0) or cap == "unlimited"):
                fails.append(f"{tag}: ranked mode needs countedAttemptsPerDay (a positive integer or \"unlimited\")")
            if not m.get("boards"):
                fails.append(f"{tag}: ranked mode must declare the boards it writes to")

    def check_grants(grants: list, tag: str, mode_kind: str | None, grants_to: str) -> list[str]:
        kinds = []
        for g in grants:
            if not isinstance(g, dict) or g.get("kind") not in GRANT_KINDS:
                fails.append(f"{tag}: grant {g!r} needs a kind from {sorted(GRANT_KINDS)}")
                continue
            kind = g["kind"]
            kinds.append(kind)
            if kind == "currency" and g.get("id") not in virtual:
                fails.append(f"{tag}: grants currency '{g.get('id')}' that is not in currencies.virtual")
            if mode_kind == "ranked" and kind in PLAY_CHANGING:
                fails.append(f"{tag}: ranked mode grants '{kind}', which changes play; only cosmetic, access, pass or a group round")
            for board in g.get("writesTo", []):
                if board not in board_scope:
                    fails.append(f"{tag}: writes to unknown board '{board}'")
                    continue
                if board in ranked_boards:
                    if kind != "round":
                        fails.append(f"{tag}: '{kind}' writes to ranked board '{board}'; only a round may")
                    elif SCOPE_RANK.get(grants_to, 0) < SCOPE_RANK.get(board_scope[board], 2):
                        fails.append(f"{tag}: a round granted to '{grants_to}' writes to board '{board}' "
                                     f"(scope {board_scope[board]}); it may only write to boards no wider than who receives it")
        return kinds

    catalog = policy["catalog"]
    _dupes(catalog, "sku", "catalog", fails)
    cat_by_sku: dict[str, dict] = {}
    for c in catalog:
        tag = f"sku {c.get('sku')}"
        if not _req(c, "catalog", tag, fails):
            continue
        cat_by_sku[c["sku"]] = c
        bp = c["basePrice"]
        if not (isinstance(bp, dict) and isinstance(bp.get("minor"), int) and bp["minor"] > 0 and bp.get("currency")):
            fails.append(f"{tag}: basePrice must be {{currency, minor}} with a positive integer in minor units")
        sold_in = set(c.get("stores", store_ids))
        for sid in sorted(sold_in - set(c["storeProductIds"])):
            fails.append(f"{tag}: no product id for store '{sid}'")
        for sid in set(c["storeProductIds"]) - store_ids:
            fails.append(f"{tag}: product id for undeclared store '{sid}'")
        if c["kind"] == "subscription" and not c.get("period"):
            fails.append(f"{tag}: subscription needs a period (P1M, P1Y)")
        for cur in c.get("priceInVirtual", {}):
            if cur not in virtual:
                fails.append(f"{tag}: priceInVirtual uses unknown currency '{cur}'")
        if c["random"]:
            odds = c.get("odds") or {}
            if not odds:
                fails.append(f"{tag}: random item without odds (stores require odds before purchase)")
            elif not math.isclose(sum(odds.values()), 1.0, abs_tol=0.001):
                fails.append(f"{tag}: odds sum to {sum(odds.values()):.3f}, not 1")
            if not policy["storeDeclarations"].get("lootBoxes"):
                fails.append(f"{tag}: random item but storeDeclarations.lootBoxes is false (UK listings need the label)")
            if minors:
                fails.append(f"{tag}: random paid item with an audience under 18 (Brazil bans it for minors, EU minors guidelines)")
            if "BE" in regions:
                fails.append(f"{tag}: random paid item sold in Belgium (treated as gambling)")

    offers = policy["offers"]
    _dupes(offers, "id", "offer", fails)
    sibling: dict[tuple, set] = {}
    for o in offers:
        tag = f"offer {o.get('id')}"
        if not _req(o, "offer", tag, fails):
            continue
        mode = mode_by_id.get(o["mode"])
        if mode is None:
            fails.append(f"{tag}: mode '{o['mode']}' is not declared")
        if not POINT_RE.match(str(o["point"])):
            fails.append(f"{tag}: point '{o['point']}' must be snake_case on_* or custom_*")
        item = cat_by_sku.get(o["sku"])
        if item is None:
            fails.append(f"{tag}: sku '{o['sku']}' is not in the catalog")
            continue
        if o["grantsTo"] not in SCOPE_RANK:
            fails.append(f"{tag}: grantsTo must be buyer, group or everyone")
        kinds = check_grants(item["grants"], tag, mode and mode["kind"], o["grantsTo"])
        if mode and mode["kind"] == "social" and o["grantsTo"] == "buyer":
            fails.append(f"{tag}: social mode grants must go to the group or everyone")
        if o["priceEscalation"]:
            fails.append(f"{tag}: price escalation (each retry costs more) is a pressure pattern regulators target")
        if o["countdown"] and (minors or kids):
            fails.append(f"{tag}: countdown or scarcity copy with an audience that includes minors")
        elif o["countdown"]:
            warns.append(f"{tag}: countdown copy; make sure the deadline is real")
        if set(kinds) & PER_ATTEMPT and "maxPerAttempt" not in o:
            fails.append(f"{tag}: moves, time or booster offers need maxPerAttempt")
        if "maxPerDay" not in o and "maxPerAttempt" not in o:
            warns.append(f"{tag}: no maxPerDay or maxPerAttempt cap")
        key = (o["mode"], o["point"], tuple(sorted(kinds)))
        price = item["basePrice"].get("minor") if isinstance(item["basePrice"], dict) else None
        sibling.setdefault(key, set()).add(price)
    for (mid, point, kinds), prices in sibling.items():
        if len(prices) > 1:
            fails.append(f"offers at {mid}/{point} sell {list(kinds)} at different prices {sorted(p for p in prices if p)}: escalation by sibling offers")

    placements = policy["placements"]
    _dupes(placements, "id", "placement", fails)
    for p in placements:
        tag = f"placement {p.get('id')}"
        if not _req(p, "placement", tag, fails):
            continue
        mode = mode_by_id.get(p["mode"])
        if mode is None:
            fails.append(f"{tag}: mode '{p['mode']}' is not declared")
        if not POINT_RE.match(str(p["point"])):
            fails.append(f"{tag}: point '{p['point']}' must be snake_case on_* or custom_*")
        fmt = p["format"]
        check_grants(p.get("grants", []), tag, mode and mode["kind"], "buyer")
        if fmt == "rewarded":
            if not p.get("grants"):
                fails.append(f"{tag}: rewarded placement must declare what it grants")
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
        elif fmt == "banner":
            if p["point"] not in BANNER_POINTS:
                fails.append(f"{tag}: banners only on on_menu or on_loading, never in play")
        elif fmt == "app_open":
            if kids:
                fails.append(f"{tag}: no app open ads in kids mode")
            warns.append(f"{tag}: app open ads have no public evidence for games yet; test against retention")
        elif fmt != "native":
            fails.append(f"{tag}: unknown format '{fmt}'")

    has_ads = bool(placements)
    if has_ads and policy["consent"].get("requiredBeforeAds") is not True:
        fails.append("consent.requiredBeforeAds must be true when the product shows ads")
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
    version = str(policy.get("contractVersion", ""))
    if version and version not in SUPPORTED_VERSIONS:
        print(f"could not run: contract version {version} is not supported by this checker ({sorted(SUPPORTED_VERSIONS)})")
        print(CANNOT_COVER)
        return 2
    fails, warns = check(policy)
    print(f"{policy.get('product', {}).get('id', '?')}: contract {version or '?'}, revision "
          f"{policy.get('policyRevision', '?')}, {len(policy.get('modes', []))} modes, "
          f"{len(policy.get('catalog', []))} skus, {len(policy.get('offers', []))} offers, "
          f"{len(policy.get('placements', []))} placements")
    for f in fails:
        print("FAIL", f)
    for w in warns:
        print("WARN", w)
    print("Verdict: " + ("FAIL" if fails else "PASS"))
    print(CANNOT_COVER)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
