#!/usr/bin/env python3
"""Generate the frozen synthetic EFMW-INT-001 pilot corpus (60 pipelines).

The pilot is an author-built instrument check, not an independent or
confirmatory evaluation. The labels are stored separately from blinded items.
"""
from __future__ import annotations

import csv
import hashlib
import json
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SEED = 20261113
FAMILIES = [
    ("omitted_confounder", 5),
    ("miscovering_nominal_interval", 5),
    ("changed_cited_source", 4),
    ("weak_formal_statement", 4),
    ("withdrawn_authorization", 4),
    ("post_result_benchmark_retuning", 4),
    ("shared_source_repetition", 4),
]


def pair(family: str, n: int) -> tuple[dict, dict]:
    """Return (defect, clean) matched synthetic pipelines."""
    pid = f"PAIR-{family[:3].upper()}-{n:02d}"
    base = {
        "pair_id": pid,
        "domain": ["clinical operations", "materials testing", "public-service analytics", "software assurance"][n % 4],
        "context": "Synthetic teaching example. No real people, organizations, or empirical claims are represented.",
    }
    if family == "omitted_confounder":
        d = {"claim":"A reminder intervention increased appointment attendance by 12 percentage points in the pilot.","evidence":{"intervention_rate":0.72,"comparison_rate":0.60,"sample_size_each":100,"known_variable":"The intervention group was recruited from a weekday clinic; the comparison group was recruited from a weekend clinic. Weekend attendance historically differs by 15 percentage points."},"provenance":{"data":"synthetic table v1","collection":"same calendar month; group assignment not randomized"},"inference_procedure":"Compare raw group proportions and attribute the difference to the reminder intervention."}
        c = {"claim":"A reminder intervention was associated with 12 percentage points higher attendance in this pilot; the data do not isolate a causal effect.","evidence":{"intervention_rate":0.72,"comparison_rate":0.60,"sample_size_each":100,"known_variable":"Groups came from different clinic schedules, which may affect attendance."},"provenance":{"data":"synthetic table v1","collection":"same calendar month; group assignment not randomized"},"inference_procedure":"Report the raw association and state that schedule confounding prevents causal attribution."}
    elif family == "miscovering_nominal_interval":
        d = {"claim":"The interval procedure has its advertised 95% repeated-sampling coverage.","evidence":{"nominal_coverage":0.95,"covered_repetitions":80,"total_repetitions":100,"interval_rule":"Frozen before simulation"},"provenance":{"simulation":"synthetic run table v1","seed":"pilot-seed-07"},"inference_procedure":"Count simulated parameter values inside intervals; compare empirical coverage with the advertised rate."}
        c = {"claim":"The interval procedure is compatible with its advertised 95% coverage in this small synthetic run; uncertainty remains substantial.","evidence":{"nominal_coverage":0.95,"covered_repetitions":95,"total_repetitions":100,"interval_rule":"Frozen before simulation"},"provenance":{"simulation":"synthetic run table v1","seed":"pilot-seed-07"},"inference_procedure":"Count simulated parameter values inside intervals; report the observed rate and sampling uncertainty."}
    elif family == "changed_cited_source":
        d = {"claim":"The cited source supports the statement that the instrument was calibrated to 0.2 units.","evidence":{"quoted_snapshot":"Calibration tolerance: 0.2 units.","current_source":"Calibration tolerance: 2.0 units."},"provenance":{"citation_resolved":"2026-02-01","source_revision_at_citation":"rev-A","source_revision_now":"rev-B","snapshot_archived":False},"inference_procedure":"Use the current source as though its content were unchanged since citation."}
        c = {"claim":"The cited source supports the statement that the instrument was calibrated to 0.2 units at the time of the analysis.","evidence":{"quoted_snapshot":"Calibration tolerance: 0.2 units.","current_source":"Calibration tolerance: 2.0 units."},"provenance":{"citation_resolved":"2026-02-01","source_revision_at_citation":"rev-A","source_revision_now":"rev-B","snapshot_archived":True,"analysis_source":"archived rev-A snapshot"},"inference_procedure":"Use the preserved rev-A snapshot for the historical claim and disclose that the current source has changed."}
    elif family == "weak_formal_statement":
        d = {"claim":"Every submitted record has a unique authorization token.","evidence":{"formal_theorem":"There exists at least one submitted record with an authorization token.","proof_status":"kernel-checked in the stated toy environment"},"provenance":{"formal_source":"synthetic theorem file v1","environment":"toy logic profile A"},"inference_procedure":"Treat the existential theorem as proving the universal prose claim."}
        c = {"claim":"At least one submitted record has an authorization token.","evidence":{"formal_theorem":"There exists at least one submitted record with an authorization token.","proof_status":"kernel-checked in the stated toy environment"},"provenance":{"formal_source":"synthetic theorem file v1","environment":"toy logic profile A"},"inference_procedure":"Translate the existential theorem to the matching existential claim; do not generalize to every record."}
    elif family == "withdrawn_authorization":
        d = {"claim":"The review action was authorized when performed.","evidence":{"authorization_granted":"2026-04-01T09:00:00Z","authorization_withdrawn":"2026-04-10T09:00:00Z","review_action":"2026-04-12T12:00:00Z"},"provenance":{"authorization_log":"synthetic append-only log v1","clock":"UTC"},"inference_procedure":"Check only that authorization was once granted; infer it remained valid."}
        c = {"claim":"The review action was not authorized under the recorded permission state.","evidence":{"authorization_granted":"2026-04-01T09:00:00Z","authorization_withdrawn":"2026-04-10T09:00:00Z","review_action":"2026-04-12T12:00:00Z"},"provenance":{"authorization_log":"synthetic append-only log v1","clock":"UTC"},"inference_procedure":"Compare the action time with the grant and withdrawal times; treat withdrawal as ending authorization."}
    elif family == "post_result_benchmark_retuning":
        d = {"claim":"The system met the frozen acceptance threshold in the evaluation.","evidence":{"initial_threshold":0.90,"observed_score":0.87,"reported_threshold":0.85},"provenance":{"initial_protocol_time":"2026-05-01T00:00:00Z","results_seen":"2026-05-10T00:00:00Z","threshold_changed":"2026-05-11T00:00:00Z","change_disclosed":False},"inference_procedure":"Apply the revised threshold to the already observed score and describe it as the original acceptance rule."}
        c = {"claim":"The system did not meet the preregistered threshold; the later exploratory threshold is reported separately.","evidence":{"initial_threshold":0.90,"observed_score":0.87,"reported_threshold":0.85},"provenance":{"initial_protocol_time":"2026-05-01T00:00:00Z","results_seen":"2026-05-10T00:00:00Z","threshold_changed":"2026-05-11T00:00:00Z","change_disclosed":True},"inference_procedure":"Score against the original threshold for the confirmatory result and label the revised threshold exploratory."}
    elif family == "shared_source_repetition":
        d = {"claim":"Three independent reviews corroborate the safety estimate.","evidence":{"reviews":[{"reviewer":"R1","estimate":0.04,"source":"Report Q"},{"reviewer":"R2","estimate":0.04,"source":"Report Q"},{"reviewer":"R3","estimate":0.04,"source":"Report Q"}]},"provenance":{"source_count":1,"source":"Report Q","independent_measurements":0},"inference_procedure":"Count three reviewers as three independent evidentiary confirmations."}
        c = {"claim":"Three reviewers agree on the estimate, but their agreement traces to one source and is not three independent confirmations.","evidence":{"reviews":[{"reviewer":"R1","estimate":0.04,"source":"Report Q"},{"reviewer":"R2","estimate":0.04,"source":"Report Q"},{"reviewer":"R3","estimate":0.04,"source":"Report Q"}]},"provenance":{"source_count":1,"source":"Report Q","independent_measurements":0},"inference_procedure":"Report reviewer agreement while counting the underlying source once."}
    else:
        raise ValueError(family)
    return ({**base, **d}, {**base, **c})


def main() -> None:
    items, labels = [], []
    for family, count in FAMILIES:
        for n in range(1, count + 1):
            defect, clean = pair(family, n)
            items.append(defect)
            labels.append({"pair_id":defect["pair_id"],"ground_truth":"DEFECT","defect_family":family,"exactly_one_planted_defect":True})
            items.append(clean)
            labels.append({"pair_id":clean["pair_id"],"ground_truth":"CLEAN","defect_family":"none","exactly_one_planted_defect":False})
    rng = random.Random(SEED)
    order = list(range(len(items)))
    rng.shuffle(order)
    items = [{"pipeline_id":f"INT001-PILOT-{i+1:03d}", **items[j]} for i,j in enumerate(order)]
    labels = [{"pipeline_id":items[i]["pipeline_id"], **labels[j]} for i,j in enumerate(order)]
    with (ROOT / "items.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for item in items:
            f.write(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n")
    with (ROOT / "labels.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["pipeline_id","pair_id","ground_truth","defect_family","exactly_one_planted_defect"])
        w.writeheader(); w.writerows(labels)
    manifest = []
    for name in ("generate.py","validate.py","items.jsonl","labels.csv","README.md","PILOT-60-RESULTS.md"):
        digest = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
        manifest.append(f"{digest}  {name}")
    (ROOT / "SHA256SUMS").write_text("\n".join(manifest)+"\n", encoding="utf-8")
    counts = {f: sum(1 for x in labels if x["defect_family"] == f) for f,_ in FAMILIES}
    summary = {
        "benchmark":"EFMW-INT-001",
        "release":"pilot-60-v1",
        "status":"FROZEN_SYNTHETIC_PILOT_CORPUS; NOT A SYSTEM PERFORMANCE RESULT",
        "seed":SEED,
        "items":len(items),
        "defect_positive":sum(x["ground_truth"] == "DEFECT" for x in labels),
        "clean":sum(x["ground_truth"] == "CLEAN" for x in labels),
        "matched_pairs":len(labels)//2,
        "defect_family_counts":counts,
        "all_items_synthetic":True,
        "items_and_labels_public_after_release":True,
        "confirmatory":False,
        "arm_scoring":"NOT RUN; no independent custodian or frozen executable arm implementations were available",
        "construction_checks":"PASS; run python3 validate.py to reproduce",
    }
    (ROOT / "freeze.json").write_text(json.dumps(summary, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()
