#!/usr/bin/env python3
"""Inspect pinned CL33 release bytes without importing its code or loading weights.

Requires Python 3.10+ and numpy. Fetches only files <= 1 MiB; .pt files are
always excluded. Writes source cache to --cache and an auditable JSON report.
"""
import argparse
import ast
import hashlib
import json
import platform
import sys
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = "mirrorethic/cl33-oplm"
OLD = "0f7d63c4551a15a9bb5b2f35c8d4fe6b111dc2bf"
NEW = "b081c1c8888a857d5dfdd1ec4f1d94b497834473"
LIMIT = 1024 * 1024


def fetch(url):
    with urllib.request.urlopen(url, timeout=45) as response:
        return response.read(LIMIT + 1)


def inspect_revision(rev, cache):
    base = f"https://huggingface.co/{REPO}"
    tree = json.loads(fetch(f"https://huggingface.co/api/models/{REPO}/tree/{rev}"))
    if not isinstance(tree, list):
        raise ValueError("Unexpected tree response")
    inventory = {entry["path"]: entry for entry in tree if entry["type"] == "file"}
    folder = cache / rev
    folder.mkdir(parents=True, exist_ok=True)

    def get(item):
        name, entry = item
        if Path(name).name != name or name in (".", ".."):
            raise ValueError("This verifier only supports flat release trees")
        if entry["size"] > LIMIT or name.endswith(".pt"):
            return None
        data = fetch(f"{base}/resolve/{rev}/{name}")
        if len(data) != entry["size"] or len(data) > LIMIT:
            raise ValueError(f"Unexpected size: {name}")
        (folder / name).write_bytes(data)
        return name, hashlib.sha256(data).hexdigest()

    with ThreadPoolExecutor(max_workers=6) as pool:
        hashes = dict(x for x in pool.map(get, inventory.items()) if x is not None)
    rows = []
    for line in (folder / "SHA256SUMS").read_text().splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        expected, name = line.split(maxsplit=1)
        name = name.lstrip(" *")
        status = ("missing_path" if name not in inventory else
                  "not_downloaded" if name not in hashes else
                  "pass" if hashes[name] == expected else "hash_mismatch")
        row = {"path": name, "expected_sha256": expected, "actual_sha256": hashes.get(name), "status": status}
        if name in inventory and "lfs" in inventory[name]:
            row["published_lfs_sha256"] = inventory[name]["lfs"]["oid"]
            row["manifest_matches_published_lfs_metadata"] = expected == inventory[name]["lfs"]["oid"]
        rows.append(row)
    load_calls = []
    for name in ("repro_bottleneck.py", "repro_reverse_readout.py"):
        parsed = ast.parse((folder / name).read_text())
        for node in ast.walk(parsed):
            if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                    and isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "torch" and node.func.attr == "load"):
                kwargs = {k.arg: ast.literal_eval(k.value) for k in node.keywords
                          if k.arg == "weights_only"}
                load_calls.append({"path": name, "line": node.lineno, **kwargs})
    covered = {r["path"] for r in rows}
    result = {"commit": rev, "tree_url": f"{base}/tree/{rev}", "inventory": tree,
              "downloaded_sha256": hashes, "manifest_checks": rows,
              "manifest_summary": dict(Counter(r["status"] for r in rows)),
              "files_not_listed_in_manifest": sorted(set(inventory) - covered),
              "torch_load_calls": load_calls}
    held = folder / "eval_slice_invert_heldout.npz"
    if held.exists():
        with np.load(held, allow_pickle=False) as data:
            result["heldout_fixture"] = {
                k: {"shape": list(data[k].shape), "dtype": str(data[k].dtype)}
                for k in data.files
            }
            for k in data.files:
                arr = data[k]
                if arr.ndim == 1 and arr.size <= 108:
                    values, counts = np.unique(arr, return_counts=True)
                    result["heldout_fixture"][k]["counts"] = {str(v): int(c) for v, c in zip(values, counts)}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, default=Path("cl33-source-cache"))
    parser.add_argument("--output", type=Path, default=Path("verification.json"))
    args = parser.parse_args()
    old = inspect_revision(OLD, args.cache)
    new = inspect_revision(NEW, args.cache)
    old_tree = {x["path"]: x for x in old["inventory"]}
    new_tree = {x["path"]: x for x in new["inventory"]}
    common = set(old_tree) & set(new_tree)
    changed = sorted(p for p in common if old_tree[p]["oid"] != new_tree[p]["oid"])
    models = ["model.py", "model_v2.py", "so33.py", "wedge.py", "t3v3_wedge_memory.py", "tape_memory.py"]
    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "runtime": {"python": sys.version, "numpy": np.__version__, "platform": platform.platform()},
        "scope": "Static byte and metadata inspection only; no upstream code imported, model inference, probe evaluation, or checkpoint deserialization.",
        "old": old, "new": new,
        "comparison": {
            "changed_existing_paths": changed,
            "added_paths": sorted(set(new_tree) - set(old_tree)),
            "removed_paths": sorted(set(old_tree) - set(new_tree)),
            "model_source_bytes_unchanged": {p: old["downloaded_sha256"][p] == new["downloaded_sha256"][p] for p in models},
            "checkpoint_lfs_ids_unchanged": {p: old_tree[p]["lfs"]["oid"] == new_tree[p]["lfs"]["oid"] for p in common if p.endswith(".pt")},
            "checkpoint_bytes_downloaded": False
        }
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"old": old["manifest_summary"], "new": new["manifest_summary"],
                      "comparison": result["comparison"], "heldout_fixture": new.get("heldout_fixture"),
                      "new_files_not_listed": new["files_not_listed_in_manifest"],
                      "torch_load_calls": {"old":old["torch_load_calls"],"new":new["torch_load_calls"]}}, indent=2))


if __name__ == "__main__":
    main()
