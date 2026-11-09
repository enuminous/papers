#!/usr/bin/env python3
"""UNITY-001 Phase 1: offline check of pinned Git blob identities and source transcriptions.

Requires clean local Git clones containing the pinned commits. Does not check
mathematical or physical truth, and does not fetch or modify any repository.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
def git_show(root: Path, repo: str, commit: str, path: str) -> bytes:
    directory = root / repo
    if not (directory / ".git").exists():
        raise FileNotFoundError(f"Local Git clone unavailable: {directory}")
    p = subprocess.run(["git", "-C", str(directory), "show", f"{commit}:{path}"],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
    if p.returncode:
        raise RuntimeError(f"git show failed for {repo}@{commit}:{path}: {p.stderr.decode(errors='replace')}")
    return p.stdout

def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def run(root: Path, skip_all: bool = False) -> int:
    lock = json.loads((HERE / "sources.lock.json").read_text(encoding="utf-8"))
    checked = 0
    try:
        for r in lock["repositories"]:
            files = r["files"] if not skip_all else [f for f in r["files"] if any(x["repo"] == r["repo"] and x["path"] == f["path"] for x in lock["primary_files"])]
            for f in files:
                raw = git_show(root, r["repo"], r["commit"], f["path"])
                actual = git_blob_sha(raw)
                if actual != f["git_blob_sha"]:
                    print("FAIL", r["repo"], f["path"], actual, f["git_blob_sha"])
                    return 1
                checked += 1
        for r in lock["external_original_source_provenance"]["additional_original_repositories"]:
            short = r["repo"].split("/", 1)[1]
            for f in r["files"]:
                raw = git_show(root, short, r["commit"], f["path"])
                if git_blob_sha(raw) != f["git_blob_sha"]:
                    print("FAIL original upstream", short, f["path"])
                    return 1
                checked += 1
        with (HERE / "source-equations.csv").open(encoding="utf-8", newline="") as h:
            rows = list(csv.DictReader(h))
        fs = next(x for x in lock["external_original_source_provenance"]["additional_original_repositories"] if x["repo"].endswith("/FieldSpace"))
        fs_lines = git_show(root, "FieldSpace", fs["commit"], "EFMW_165_field_equations.txt").decode("utf-8").splitlines()
        canonical = next(x for x in lock["external_original_source_provenance"]["additional_original_repositories"] if x["repo"].endswith("/Monolithic-102-Zoo-Lean4"))
        canonical_rows = {x["id"]: x for x in json.loads(git_show(root, "Monolithic-102-Zoo-Lean4", canonical["commit"], "canonical/equations.json"))["equations"]}
        audited = catalogued = 0
        for row in rows:
            if row["claim_class"] == "historical_fieldspace_source":
                line = int(row["source_line"])
                if fs_lines[line - 1].strip() != row["original_statement"].strip():
                    print("FAIL raw FieldSpace text", row["record_id"])
                    return 1
                audited += 1
            elif row["record_id"].startswith("ME-") and row["original_repo"].endswith("/Monolithic-102-Zoo-Lean4"):
                e = canonical_rows.get(row["record_id"])
                if e is None or e["formula"] != row["original_statement"]:
                    print("FAIL raw canonical formula", row["record_id"])
                    return 1
                catalogued += 1
        if audited != 585 or catalogued != 102 or len(rows) != 717:
            print("FAIL unexpected ledger totals", audited, catalogued, len(rows))
            return 1
        print(f"PASS {checked} pinned Git blob objects; FieldSpace {audited}/585; canonical {catalogued}/102; total ledger {len(rows)}.")
        print("NOTE: source identity only — no Lean kernel or empirical validation performed.")
        return 0
    except FileNotFoundError as e:
        print("UNRESOLVED:", e)
        return 2
    except (RuntimeError, UnicodeError, KeyError, ValueError) as e:
        print("UNRESOLVED:", e)
        return 2

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True,
                    help="Folder of local clones named Geometry, Information-Tensor, EFMW-Lagrangian, Standard-Model-Reduction, Monolithic-102-Zoo-Lean4, Monolithic_102_EFMW, FieldSpace")
    ap.add_argument("--primary-only", action="store_true", help="Check only highlighted priority files rather than all 209 priority tree entries")
    args = ap.parse_args()
    sys.exit(run(args.repo_root, args.primary_only))
