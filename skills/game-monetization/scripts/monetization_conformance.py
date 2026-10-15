#!/usr/bin/env python3
"""Cross artefact check: a product's monetization policy against its tracking plan and store declarations.

monetization_check.py checks the policy on its own. This script checks that the
other artefacts agree with it, which is where store rejections, broken revenue
reports and consumer fines come from (Game Monetization Contract 0.2, sections 6,
7 and 9).

Inputs:
  --policy           monetization-policy.json (contract 0.2 or 0.1)
  --tracking-plan    the tracking plan in the measurement format
                     ({"events": {name: {"props": {prop: {"type": ...}}}}}, see
                     skills/measurement/references/tracking-plan-as-code.md)
  --declarations     optional, repeatable: one JSON file per store with what the
                     store forms were told: {"product", "store", "containsAds",
                     "inAppPurchases", "lootBoxes", "ageRatingInputs": {
                     "advertising", "randomItems", "digitalPurchases",
                     "madeForKids", "minimumTargetAge", ...}}

Fails (exit 1) when:
  - the policy itself fails monetization_check.py (run it for the details)
  - an offer has no offer_shown, offer_accepted or offer_declined coverage; a
    rewarded placement has no ad_requested, ad_shown or ad_rewarded coverage;
    any other placement has no ad_shown coverage; a catalog item has no
    purchase_completed or purchase_refunded coverage. Coverage means the event
    is declared and its identity properties accept this item's values (offers:
    sku, mode_id, point, and offer_id when declared; placements: placement_id,
    mode_id, point; catalog items: sku)
  - one of those events lacks contract_version or policy_revision, or their
    types cannot carry the policy's values (contract_version typed as a number,
    a policy_revision outside the declared range)
  - a declared product property cannot carry the policy's product id
  - a declarations file disagrees with the policy's storeDeclarations or with
    the policy content: ads present but containsAds false, catalog items but
    inAppPurchases false, random items but lootBoxes false, a missing boolean,
    age rating answers that contradict the policy (advertising, randomItems,
    digitalPurchases, madeForKids, a minimumTargetAge younger than the policy's
    audience), or a store the policy does not declare
Warnings: other contract events missing (purchase_started, purchase_failed,
entitlement_granted, entitlement_revoked, ad_failed, ad_revenue,
consent_updated), no product property, enum values the policy does not know,
offers the data cannot tell apart, over declared labels, no age rating answers.
Exit 2 when a file cannot be read, the contract version is not supported, the
plan has no events object or a declarations file names another product.

  python3 monetization_conformance.py --policy policy.json --tracking-plan plan.json \\
      [--declarations google.json --declarations apple.json]

Standard library only.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

SUPPORTED_VERSIONS = {"0.1", "0.2"}
CANNOT_COVER = ("This check cannot cover: whether the code emits the events the plan declares (run the measurement "
                "skill's tracking_plan_check.py with --code and a payload sample), whether the store consoles still "
                "hold the answers in the declarations files, live prices and product ids in each store, the wording "
                "of labels, odds screens and offers on screen, and rules that changed after these files were written.")
ID_OK = re.compile(r"^[A-Za-z0-9_.:-]{1,64}$")  # same pattern as the measurement tracking_plan_check.py
PLAN_TYPES = ("id", "num", "bool", "enum", "route")
OFFER_EVENTS = ("offer_shown", "offer_accepted", "offer_declined")
REWARDED_EVENTS = ("ad_requested", "ad_shown", "ad_rewarded")
OTHER_AD_EVENTS = ("ad_shown",)
PURCHASE_EVENTS = ("purchase_completed", "purchase_refunded")
IDENTITY = {"offer": ("sku", "mode_id", "point"), "placement": ("placement_id", "mode_id", "point"), "sku": ("sku",)}
RECOMMENDED_IF_CATALOG = ("purchase_started", "purchase_failed", "entitlement_granted", "entitlement_revoked")
RECOMMENDED_IF_ADS = ("ad_failed", "ad_revenue", "consent_updated")
DECLARED_FLAGS = (("containsAds", "ad placements"), ("inAppPurchases", "catalog items"), ("lootBoxes", "random items"))
AGE_BOOL_KEYS = {"advertising": "ads", "randomItems": "random", "digitalPurchases": "iap", "madeForKids": "kids"}
FACT_SOURCE = {"ads": "ad placements", "random": "random items", "iap": "catalog items", "kids": "audience.kidsMode"}
POLICY_LISTS = ("stores", "modes", "catalog", "offers", "placements")


class CouldNotRun(Exception):
    """Raised when an input cannot be read or paired; maps to exit 2."""


class _Parser(argparse.ArgumentParser):
    def error(self, message: str) -> None:  # argparse exits 2 already; add the cannot cover line
        self.print_usage(sys.stderr)
        print(f"could not run: {message}")
        print(CANNOT_COVER)
        sys.exit(2)


def _load(path: str, what: str) -> dict:
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise CouldNotRun(f"cannot read the {what} {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise CouldNotRun(f"the {what} {path} must be a JSON object")
    return data


def _policy_check(policy: dict) -> tuple[list[str], list[str]] | None:
    """Run monetization_check.check() loaded by explicit path (works under python3 -I). None if absent."""
    path = Path(__file__).resolve().parent / "monetization_check.py"
    if not path.is_file():
        return None
    spec = importlib.util.spec_from_file_location("monetization_check", path)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.check(policy)


def accepts(spec: object, value: object) -> tuple[bool, str]:
    """Whether a tracking plan property spec accepts a value. Mirrors measurement's check_value()."""
    if not isinstance(spec, dict):
        return False, "the property spec is not an object"
    kind = spec.get("type")
    if kind == "enum":
        values = spec.get("values", [])
        return value in values, f"enum values {values}"
    if kind == "id":
        ok = isinstance(value, (str, int)) and not isinstance(value, bool) and bool(ID_OK.match(str(value)))
        return ok, "id pattern [A-Za-z0-9_.:-], 1 to 64 characters"
    if kind == "num":
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            return False, "num type, but the value is not a number"
        lo, hi = spec.get("min", float("-inf")), spec.get("max", float("inf"))
        return lo <= value <= hi, f"num range {lo} to {hi}"
    if kind == "bool":
        return isinstance(value, bool), "bool type"
    if kind == "route":
        return isinstance(value, str) and value.startswith("/") and "?" not in value, "route type"
    return False, f"type '{kind}' is not a tracking plan type ({', '.join(PLAN_TYPES)})"


def _policy_shape(policy: dict) -> None:
    version = policy.get("contractVersion")
    if version is None:
        raise CouldNotRun("the policy has no contractVersion, so event versions cannot be compared")
    if str(version) not in SUPPORTED_VERSIONS:
        raise CouldNotRun(f"contract version {version} is not supported by this check ({sorted(SUPPORTED_VERSIONS)})")
    if not isinstance(policy.get("product", {}), dict) or not isinstance(policy.get("storeDeclarations", {}), dict):
        raise CouldNotRun("policy.product and policy.storeDeclarations must be objects; run monetization_check.py")
    for key in POLICY_LISTS:
        items = policy.get(key, [])
        if not isinstance(items, list) or not all(isinstance(i, dict) for i in items):
            raise CouldNotRun(f"policy.{key} must be a list of objects; run monetization_check.py")


def check_plan(policy: dict, plan: dict) -> tuple[list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []
    events = plan["events"]
    version = str(policy.get("contractVersion"))
    revision = policy.get("policyRevision")
    product_id = policy.get("product", {}).get("id")
    offers = policy.get("offers", [])
    placements = policy.get("placements", [])
    catalog = policy.get("catalog", [])

    # Who needs which event: (kind, item id, {identity prop: value}).
    needs: dict[str, list[tuple[str, str, dict]]] = {}
    for o in offers:
        ident = {"sku": o.get("sku"), "mode_id": o.get("mode"), "point": o.get("point"), "offer_id": o.get("id")}
        for e in OFFER_EVENTS:
            needs.setdefault(e, []).append(("offer", str(o.get("id")), ident))
    for p in placements:
        ident = {"placement_id": p.get("id"), "mode_id": p.get("mode"), "point": p.get("point")}
        for e in (REWARDED_EVENTS if p.get("format") == "rewarded" else OTHER_AD_EVENTS):
            needs.setdefault(e, []).append(("placement", str(p.get("id")), ident))
    for c in catalog:
        for e in PURCHASE_EVENTS:
            needs.setdefault(e, []).append(("sku", str(c.get("sku")), {"sku": c.get("sku")}))

    for event in sorted(needs):
        users = needs[event]
        if event not in events or not isinstance(events[event], dict):
            by_kind: dict[str, list[str]] = {}
            for kind, item_id, _ in users:
                by_kind.setdefault(kind, []).append(item_id)
            listed = "; ".join(f"{k}s: {', '.join(v)}" for k, v in sorted(by_kind.items()))
            fails.append(f"event '{event}' is not in the tracking plan, so these have no coverage ({listed})")
            continue
        props = events[event].get("props", {})
        if not isinstance(props, dict):
            fails.append(f"{event}: props must be an object")
            continue

        # Version properties: revenue must be attributable to a policy revision.
        if "contract_version" not in props:
            fails.append(f"{event}: no 'contract_version' property (contract section 6)")
        elif isinstance(props["contract_version"], dict) and props["contract_version"].get("type") == "num":
            fails.append(f"{event}: contract_version is typed num; declare it as id or enum so '{version}' stays a "
                         f"string (0.10 would read as 0.1)")
        else:
            ok, why = accepts(props["contract_version"], version)
            if not ok:
                fails.append(f"{event}: contract_version cannot carry '{version}' ({why})")
        if "policy_revision" not in props:
            fails.append(f"{event}: no 'policy_revision' property, so revenue cannot be tied to a policy change "
                         f"(contract section 6)")
        elif revision is not None:
            ok, why = accepts(props["policy_revision"], revision)
            if not ok:
                fails.append(f"{event}: policy_revision cannot carry {revision!r} ({why})")

        if "product" not in props:
            warns.append(f"{event}: no 'product' property (contract section 6); fine only for a single product plan")
        elif product_id is not None:
            ok, why = accepts(props["product"], product_id)
            if not ok:
                fails.append(f"{event}: product cannot carry '{product_id}' ({why})")

        # Identity properties: each item must be reachable by value.
        kinds = sorted({k for k, _, _ in users})
        for kind in kinds:
            # offer_id is required from contract 0.2; under 0.1 it is used when the plan declares it.
            needs_offer_id = kind == "offer" and ("offer_id" in props or version != "0.1")
            idents = list(IDENTITY[kind]) + (["offer_id"] if needs_offer_id else [])
            for prop in idents:
                if prop not in props:
                    fails.append(f"{event}: no '{prop}' property, so {kind} coverage cannot be shown "
                                 f"({', '.join(i for k, i, _ in users if k == kind)})")
                    continue
                for k, item_id, ident in users:
                    if k != kind:
                        continue
                    ok, why = accepts(props[prop], ident.get(prop))
                    if not ok:
                        fails.append(f"{kind} {item_id}: {event}.{prop} cannot carry '{ident.get(prop)}' ({why})")

        # Drift: enum values the policy does not know.
        known = {"sku": {c.get("sku") for c in catalog}, "placement_id": {p.get("id") for p in placements},
                 "offer_id": {o.get("id") for o in offers}}
        for prop, valid in known.items():
            spec = props.get(prop)
            if isinstance(spec, dict) and spec.get("type") == "enum" and valid:
                stale = [v for v in spec.get("values", []) if v not in valid]
                if stale:
                    warns.append(f"{event}.{prop} lists {stale}, which the policy does not declare (stale value?)")

    # Offers the data cannot tell apart.
    shown = events.get("offer_shown", {}).get("props", {}) if isinstance(events.get("offer_shown"), dict) else {}
    if isinstance(shown, dict) and "offer_id" not in shown:
        seen: dict[tuple, list[str]] = {}
        for o in offers:
            seen.setdefault((o.get("sku"), o.get("mode"), o.get("point")), []).append(str(o.get("id")))
        for key, ids in seen.items():
            if len(ids) > 1:
                warns.append(f"offers {', '.join(ids)} share sku, mode and point {list(key)}; add an offer_id property "
                             f"to the offer events to tell them apart")

    recommended = (RECOMMENDED_IF_CATALOG if catalog else ()) + (RECOMMENDED_IF_ADS if placements else ())
    missing = [e for e in recommended if e not in events]
    if missing:
        warns.append(f"contract events not in the plan: {', '.join(missing)} (needed for refunds, fill rate, "
                     f"impression level revenue and consent reads)")
    return fails, warns


def check_declarations(policy: dict, decl: dict, label: str) -> tuple[list[str], list[str], list[str]]:
    fails: list[str] = []
    warns: list[str] = []
    notes: list[str] = []
    store_ids = [s.get("id") for s in policy.get("stores", [])]
    store = decl.get("store")
    scoped = False
    if store is not None:
        if store in store_ids:
            scoped = True
        else:
            fails.append(f"{label}: store '{store}' is not declared in policy.stores {store_ids}; add the store "
                         f"(with product ids) or fix the file")
    items = [c for c in policy.get("catalog", []) if not scoped or store in c.get("stores", store_ids)]
    truth = {
        "ads": bool(policy.get("placements")),
        "iap": bool(items),
        "random": any(c.get("random") is True for c in items),
        "kids": bool(policy.get("product", {}).get("audience", {}).get("kidsMode")),
    }
    content = {"containsAds": truth["ads"], "inAppPurchases": truth["iap"], "lootBoxes": truth["random"]}
    policy_decl = policy.get("storeDeclarations", {})

    for field, what in DECLARED_FLAGS:
        value = decl.get(field)
        if not isinstance(value, bool):
            fails.append(f"{label}: {field} must be true or false (got {value!r}); a missing answer cannot be checked")
            continue
        has = content[field]
        if has and not value:
            fails.append(f"{label}: {field} is false but the policy has {what}"
                         + (" ('No ads' claims while ads run are a consumer law and store policy breach)"
                            if field == "containsAds" else ""))
        elif value != policy_decl.get(field):
            if scoped and field != "containsAds" and value == has:
                notes.append(f"{label}: {field} {value} differs from the product level storeDeclarations "
                             f"because store '{store}' sells {'no' if not has else 'these'} {what}")
            else:
                hint = " (the content has none, so the policy may be the file to fix)" if value == has else ""
                fails.append(f"{label}: {field} is {value} but policy.storeDeclarations.{field} is "
                             f"{policy_decl.get(field)!r}{hint}")
        elif value and not has:
            warns.append(f"{label}: {field} is true but the policy has no {what} (over declared in both files)")

    answers = decl.get("ageRatingInputs")
    if answers is None:
        warns.append(f"{label}: no ageRatingInputs; the age rating answers were not checked")
        return fails, warns, notes
    if not isinstance(answers, dict):
        fails.append(f"{label}: ageRatingInputs must be an object")
        return fails, warns, notes
    for key, fact in AGE_BOOL_KEYS.items():
        if key not in answers:
            continue
        if not isinstance(answers[key], bool):
            fails.append(f"{label}: ageRatingInputs.{key} must be true or false")
        elif answers[key] != truth[fact]:
            fails.append(f"{label}: ageRatingInputs.{key} is {answers[key]} but the policy says {truth[fact]} "
                         f"({FACT_SOURCE[fact]})")
    if "minimumTargetAge" in answers:
        age = answers["minimumTargetAge"]
        policy_age = policy.get("product", {}).get("audience", {}).get("minimumAge")
        if isinstance(age, bool) or not isinstance(age, int) or age < 0:
            fails.append(f"{label}: ageRatingInputs.minimumTargetAge must be a non negative integer")
        elif isinstance(policy_age, int) and age < policy_age:
            fails.append(f"{label}: the store target audience starts at {age} but the policy's audience.minimumAge "
                         f"is {policy_age}; the minors rules were checked against the wrong audience")
    others = sorted(k for k in answers if k not in AGE_BOOL_KEYS and k != "minimumTargetAge")
    if others:
        notes.append(f"{label}: recorded but not cross checked: {', '.join(others)}")
    return fails, warns, notes


def run(policy_path: str, plan_path: str, decl_paths: list[str]) -> int:
    try:
        policy = _load(policy_path, "policy")
        _policy_shape(policy)
        plan = _load(plan_path, "tracking plan")
        if not isinstance(plan.get("events"), dict):
            raise CouldNotRun(f"the tracking plan {plan_path} has no 'events' object (measurement format)")
        declarations = []
        for path in decl_paths:
            decl = _load(path, "declarations file")
            product = decl.get("product")
            if product is not None and product != policy.get("product", {}).get("id"):
                raise CouldNotRun(f"{path} is for product '{product}', the policy is for "
                                  f"'{policy.get('product', {}).get('id')}'")
            declarations.append((path, decl))
    except CouldNotRun as exc:
        print(f"could not run: {exc}")
        print(CANNOT_COVER)
        return 2

    fails: list[str] = []
    warns: list[str] = []
    notes: list[str] = []
    result = _policy_check(policy)
    if result is None:
        warns.append("monetization_check.py not found beside this script; the policy itself was not checked")
        policy_line = "not run"
    else:
        policy_fails = result[0]
        policy_line = "PASS" if not policy_fails else f"FAIL ({len(policy_fails)} failures)"
        if policy_fails:
            fails.append(f"the policy fails monetization_check.py ({len(policy_fails)} failures, first: "
                         f"{policy_fails[0]}); fix it before trusting the cross checks")

    plan_fails, plan_warns = check_plan(policy, plan)
    fails += plan_fails
    warns += plan_warns
    for path, decl in declarations:
        label = f"declarations {decl.get('store') or Path(path).name}"
        d_fails, d_warns, d_notes = check_declarations(policy, decl, label)
        fails += d_fails
        warns += d_warns
        notes += d_notes

    print(f"{policy.get('product', {}).get('id', '?')}: contract {policy.get('contractVersion')}, revision "
          f"{policy.get('policyRevision', '?')}; {len(policy.get('offers', []))} offers, "
          f"{len(policy.get('placements', []))} placements, {len(policy.get('catalog', []))} skus against "
          f"{len(plan['events'])} plan events and {len(declarations)} declarations files")
    print(f"Policy check (monetization_check.py): {policy_line}")
    for line in fails:
        print("FAIL", line)
    for line in warns:
        print("WARN", line)
    for line in notes:
        print("NOTE", line)
    print("Verdict: " + ("FAIL" if fails else "PASS"))
    print(CANNOT_COVER)
    return 1 if fails else 0


def main(argv: list[str] | None = None) -> int:
    parser = _Parser(description="Check a monetization policy against its tracking plan and store declarations.")
    parser.add_argument("--policy", required=True, help="monetization-policy.json")
    parser.add_argument("--tracking-plan", required=True, help="tracking plan JSON in the measurement format")
    parser.add_argument("--declarations", action="append", default=[],
                        help="store declarations JSON (repeat once per store)")
    args = parser.parse_args(argv)
    return run(args.policy, args.tracking_plan, args.declarations)


if __name__ == "__main__":
    sys.exit(main())
