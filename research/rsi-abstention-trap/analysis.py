#!/usr/bin/env python3
"""Recalculate the RSI-SYNTH-001 abstention critique without network dependencies.

Usage:
  python analysis.py --snapshot-dir /path/to/RSI/examples/frozen_demo
  python analysis.py --self-test

Source: enuminous/RSI at commit 478908589847ab10038a80fd50df35478c0ec95f.
Reads the original archived records; does NOT rerun or amend RSI-SYNTH-001.
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

EXPECTED = {
    "initial": (159, 205),
    "random_search": (349, 35),
    "recursive_candidate": (384, 0),
    "oracle_aware": (384, 0),
    "always_unresolved": (340, 0),
}
LABELS = {"SUPPORTED", "CONTRADICTED", "UNRESOLVED"}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def predict(policy: dict, case: dict) -> str:
    """Mirror the inspectable bounded decision rule in rsi/core.py."""
    if policy["require_provenance"] and not case["provenance_verified"]:
        return "UNRESOLVED"
    if policy["require_bridge"] and not case["bridge_verified"]:
        return "UNRESOLVED"
    yes = case["supports"] >= policy["support_threshold"]
    no = case["contradictions"] >= policy["contradiction_threshold"]
    if yes and no:
        mode = policy["conflict_handling"]
        if mode == "abstain":
            return "UNRESOLVED"
        if mode == "prefer_support":
            return "SUPPORTED"
        if mode == "prefer_contradiction":
            return "CONTRADICTED"
        raise ValueError("Unexpected conflict_handling")
    if yes:
        return "SUPPORTED"
    if no:
        return "CONTRADICTED"
    return "UNRESOLVED"


def summarize(cases: list[dict], predictions: list[str]) -> dict:
    if not cases or len(cases) != len(predictions):
        raise ValueError("Nonempty equal-length cases and predictions required")
    if any(c["truth"] not in LABELS for c in cases):
        raise ValueError("Unexpected truth label")
    if any(p not in LABELS for p in predictions):
        raise ValueError("Unexpected predicted label")
    n = len(cases)
    answerable = sum(c["truth"] != "UNRESOLVED" for c in cases)
    correct = sum(p == c["truth"] for p, c in zip(predictions, cases))
    asserted = sum(p != "UNRESOLVED" for p in predictions)
    correct_assertions = sum(
        p == c["truth"] and p != "UNRESOLVED"
        for p, c in zip(predictions, cases)
    )
    false_assertions = sum(
        p != c["truth"] and p != "UNRESOLVED"
        for p, c in zip(predictions, cases)
    )
    return {
        "n": n,
        "answerable_cases": answerable,
        "unresolved_cases": n - answerable,
        "correct": correct,
        "accuracy": correct / n,
        "assertions": asserted,
        "coverage": asserted / n,
        "correct_assertions": correct_assertions,
        "answerable_recall": correct_assertions / answerable if answerable else None,
        "false_assertions": false_assertions,
        "false_assertion_rate_all_cases": false_assertions / n,
        "false_assertion_rate_among_assertions":
            false_assertions / asserted if asserted else None,
    }


def paired_bootstrap_gain(
    cases: list[dict], candidate: list[str], reference: list[str],
    reps: int = 1000, seed: int = 515,
) -> tuple[float, float]:
    """Reproduce RSI's fixed-index paired bootstrap method for accuracy gain."""
    n = len(cases)
    deltas = [
        int(p == c["truth"]) - int(q == c["truth"])
        for c, p, q in zip(cases, candidate, reference)
    ]
    rng = random.Random(seed)
    resamples = sorted(
        sum(deltas[rng.randrange(n)] for _ in range(n)) / n
        for _ in range(reps)
    )
    return resamples[int(.025 * (reps - 1))], resamples[int(.975 * (reps - 1))]


def analyze(snapshot_dir: Path) -> dict:
    cases = load_json(snapshot_dir / "holdout_cases.json")
    report = load_json(snapshot_dir / "report.json")
    if report.get("experiment_id") != "RSI-SYNTH-001":
        raise ValueError("Unexpected experiment ID")
    policies = {
        "initial": load_json(snapshot_dir / "baseline_policy.json"),
        "random_search": load_json(snapshot_dir / "null_policy.json"),
        "recursive_candidate": load_json(snapshot_dir / "candidate_policy.json"),
        "oracle_aware": load_json(snapshot_dir / "control_policies.json")[
            "oracle_aware_reference"
        ],
    }
    preds = {
        name: [predict(policy, c) for c in cases]
        for name, policy in policies.items()
    }
    preds["always_unresolved"] = ["UNRESOLVED"] * len(cases)
    metrics = {name: summarize(cases, values) for name, values in preds.items()}
    for name, (expected_correct, expected_false) in EXPECTED.items():
        actual = metrics[name]
        if (actual["correct"], actual["false_assertions"]) != (
            expected_correct, expected_false
        ):
            raise ValueError(f"Snapshot differs from documented counts: {name}")
    for name, archive_name in (
        ("initial", "baseline"),
        ("random_search", "random_search_null"),
        ("recursive_candidate", "candidate"),
        ("oracle_aware", "oracle_aware_reference"),
    ):
        archived = report["heldout"][archive_name]
        if metrics[name]["correct"] != archived["correct"]:
            raise ValueError(f"Report mismatch for {name}: correct")
        if metrics[name]["false_assertions"] != archived["false_assertions"]:
            raise ValueError(f"Report mismatch for {name}: false assertions")
    ci = paired_bootstrap_gain(cases, preds["always_unresolved"], preds["initial"])
    gain = (
        metrics["always_unresolved"]["accuracy"]
        - metrics["initial"]["accuracy"]
    )
    orig = report["gate"]["thresholds"]
    would_pass = (
        gain >= orig["minimum_accuracy_gain"]
        and metrics["always_unresolved"]["false_assertion_rate_all_cases"]
        - metrics["initial"]["false_assertion_rate_all_cases"]
        <= orig["maximum_false_assertion_increase"]
        and ci[0] > orig["minimum_ci_lower"]
    )
    return {
        "scope": "EXPLORATORY_REANALYSIS_OF_PUBLIC_ARCHIVE_NOT_NEW_CONFIRMATORY_RUN",
        "source_commit": "478908589847ab10038a80fd50df35478c0ec95f",
        "source_directory": "examples/frozen_demo",
        "metrics": metrics,
        "always_unresolved_vs_initial": {
            "accuracy_gain": gain,
            "paired_bootstrap_95pct": [ci[0], ci[1]],
            "passes_original_gate_counterfactually": would_pass,
            "interpretation": "A new synthetic control, not a search-produced policy.",
        },
        "original_gate_status_preserved": report["gate"]["status"],
        "general_recursive_improvement_established": False,
    }


def self_test() -> None:
    tiny = [
        {"truth": "SUPPORTED"},
        {"truth": "CONTRADICTED"},
        {"truth": "UNRESOLVED"},
        {"truth": "UNRESOLVED"},
    ]
    a = summarize(tiny, ["UNRESOLVED"] * 4)
    assert a["correct"] == 2 and a["assertions"] == 0
    assert a["answerable_recall"] == 0 and a["false_assertions"] == 0
    b = summarize(tiny, ["SUPPORTED", "CONTRADICTED", "UNRESOLVED", "UNRESOLVED"])
    assert b["correct"] == 4 and b["correct_assertions"] == 2
    assert b["answerable_recall"] == 1 and b["coverage"] == .5
    p = {
        "support_threshold": 1, "contradiction_threshold": 1,
        "require_provenance": True, "require_bridge": True,
        "conflict_handling": "abstain",
    }
    assert predict(p, {
        "supports": 1, "contradictions": 0,
        "provenance_verified": True, "bridge_verified": True,
    }) == "SUPPORTED"
    assert predict(p, {
        "supports": 1, "contradictions": 0,
        "provenance_verified": False, "bridge_verified": True,
    }) == "UNRESOLVED"
    print("PASS: analysis self-tests")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--snapshot-dir", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.snapshot_dir is None:
        parser.error("Provide --snapshot-dir, or use --self-test")
    result = analyze(args.snapshot_dir)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
