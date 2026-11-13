#!/usr/bin/env python3
"""Validate corpus structure and frozen-file hashes; does not score audit arms."""
import collections, csv, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
items = [json.loads(x) for x in (ROOT / "items.jsonl").read_text().splitlines()]
with (ROOT / "labels.csv").open(newline="", encoding="utf-8") as f:
    labels = list(csv.DictReader(f))
assert len(items) == 60 == len(labels)
assert len({x["pipeline_id"] for x in items}) == 60
assert {x["pipeline_id"] for x in items} == {x["pipeline_id"] for x in labels}
assert sum(x["ground_truth"] == "DEFECT" for x in labels) == 30
assert sum(x["ground_truth"] == "CLEAN" for x in labels) == 30
pairs = collections.defaultdict(list)
for row in labels:
    pairs[row["pair_id"]].append(row)
assert len(pairs) == 30
assert all(sorted(x["ground_truth"] for x in rows) == ["CLEAN", "DEFECT"] for rows in pairs.values())
expected = {
    "omitted_confounder": 5,
    "miscovering_nominal_interval": 5,
    "changed_cited_source": 4,
    "weak_formal_statement": 4,
    "withdrawn_authorization": 4,
    "post_result_benchmark_retuning": 4,
    "shared_source_repetition": 4,
}
observed = collections.Counter(x["defect_family"] for x in labels if x["ground_truth"] == "DEFECT")
assert dict(observed) == expected
manifest = {}
for line in (ROOT / "SHA256SUMS").read_text().splitlines():
    digest, name = line.split("  ", 1)
    manifest[name] = digest
for name, digest in manifest.items():
    assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
print(json.dumps({
    "construction_status":"PASS",
    "items":len(items),
    "defect_positive":30,
    "clean":30,
    "matched_pairs":30,
    "family_counts":dict(observed),
    "hashes_verified":sorted(manifest),
    "arm_performance_status":"UNRESOLVED_NOT_RUN",
}, indent=2))
