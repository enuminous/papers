#!/usr/bin/env python3
"""UNITY-001 Phase 2: conservative source-linked typed equation compiler.

No eval, no symbolic simplification, no theorem prover, no physical inference.
Original source statements are never rewritten. Only manually declared ASTs
with explicit provenance are checked for local shape and dimensional agreement.
"""
from __future__ import annotations
import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

BASE = Path(__file__).resolve().parent
ALLOWED_SHAPES = {"scalar", "components4", "tensor2_cov"}
ALLOWED_OPERATORS = {"symbol", "number", "add", "sub", "mul", "neg", "pow"}
ZERO = (0, 0, 0)

class TypeFailure(ValueError):
    pass

@dataclass(frozen=True)
class InferredType:
    dimensions: tuple[int, int, int]
    shape: str

def dims(value):
    if not isinstance(value, list) or len(value) != 3 or any(type(x) is not int for x in value):
        raise TypeFailure("Dimension vector must contain exactly three integer exponents [M,L,Q]")
    return tuple(value)

def plus_dims(a, b):
    return tuple(x + y for x, y in zip(a, b))

def mul_dimension(a, scalar):
    return tuple(x * scalar for x in a)

def infer(tree, symbols, *, depth=0):
    if depth > 64:
        raise TypeFailure("Expression AST too deep")
    if not isinstance(tree, list) or not tree or tree[0] not in ALLOWED_OPERATORS:
        raise TypeFailure("Malformed or unsupported expression AST")
    op = tree[0]
    if op == "symbol":
        if len(tree) != 2 or not isinstance(tree[1], str) or tree[1] not in symbols:
            raise TypeFailure("Unknown or malformed symbol")
        sig = symbols[tree[1]]
        shape = sig.get("shape")
        if shape not in ALLOWED_SHAPES:
            raise TypeFailure("Unrecognized shape")
        return InferredType(dims(sig.get("unit")), shape)
    if op == "number":
        if len(tree) != 2 or type(tree[1]) not in (int, float):
            raise TypeFailure("Numeric literals must be finite scalar numbers")
        if isinstance(tree[1], float) and not (-1e300 < tree[1] < 1e300):
            raise TypeFailure("Non-finite or extreme numeric literal")
        return InferredType(ZERO, "scalar")
    if op == "neg":
        if len(tree) != 2:
            raise TypeFailure("Unary negation has exactly one operand")
        return infer(tree[1], symbols, depth=depth+1)
    if op == "pow":
        if len(tree) != 3 or type(tree[2]) is not int or abs(tree[2]) > 16:
            raise TypeFailure("Only bounded integer powers are implemented")
        typ = infer(tree[1], symbols, depth=depth+1)
        if typ.shape != "scalar":
            raise TypeFailure("Tensor powers are unsupported; specify contractions explicitly")
        return InferredType(mul_dimension(typ.dimensions, tree[2]), "scalar")
    if len(tree) != 3:
        raise TypeFailure("Binary AST operator requires two operands")
    left = infer(tree[1], symbols, depth=depth+1)
    right = infer(tree[2], symbols, depth=depth+1)
    if op in {"add", "sub"}:
        if left != right:
            raise TypeFailure(f"Incompatible add/sub operands: {left} vs {right}")
        return left
    if op == "mul":
        if left.shape != "scalar" and right.shape != "scalar":
            raise TypeFailure("Multiplication of two non-scalars needs an explicit contraction map")
        shape = right.shape if left.shape == "scalar" else left.shape
        return InferredType(plus_dims(left.dimensions, right.dimensions), shape)
    raise TypeFailure("Unsupported AST node")

def read_json(path):
    with Path(path).open(encoding="utf-8") as f:
        return json.load(f)

def source_rows(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        data = list(csv.DictReader(f))
    required = {"record_id", "original_repo", "original_commit", "original_path",
                "original_blob_sha", "original_statement", "literal_status",
                "normalized_status"}
    if not data or not required.issubset(data[0].keys()):
        raise TypeFailure("Phase 1 source ledger missing necessary columns")
    ids = [row["record_id"] for row in data]
    if len(ids) != len(set(ids)):
        raise TypeFailure("Phase 1 source ledger contains duplicate IDs")
    return data

def source_inventory(lock):
    inventory = {}
    for repo in lock["repositories"]:
        for file in repo["files"]:
            key = ("enuminous/" + repo["repo"], repo["commit"], file["path"])
            if key in inventory:
                raise TypeFailure("Duplicate locked source object")
            inventory[key] = file["git_blob_sha"]
    for repo in lock["external_original_source_provenance"]["additional_original_repositories"]:
        for file in repo["files"]:
            key = (repo["repo"], repo["commit"], file["path"])
            inventory[key] = file["git_blob_sha"]
    return inventory

def check_dependencies(entries):
    index = {x["id"]: x for x in entries}
    if len(index) != len(entries):
        raise TypeFailure("Duplicate typed equation ID")
    visited = set()
    visiting = set()
    def walk(ident):
        if ident in visiting:
            raise TypeFailure("Cycle among typed equation dependencies")
        if ident in visited:
            return
        visiting.add(ident)
        for dep in index[ident].get("depends_on", []):
            if dep not in index:
                raise TypeFailure("Unknown typed dependency: " + str(dep))
            walk(dep)
        visiting.remove(ident)
        visited.add(ident)
    for key in index:
        walk(key)

def check_record(record, source, inventory):
    if not record.get("namespace") or not record.get("assumptions") or not record.get("limits"):
        raise TypeFailure("Missing namespace, assumptions or scientific limitations")
    if record.get("status") != "PROPOSED_TYPED_INTERPRETATION":
        raise TypeFailure("Typed candidate must not be silently promoted to a theorem or physical PASS")
    if record.get("translation_kind", "").startswith("human-authored") is False:
        raise TypeFailure("A manual normalization must disclose its source and method")
    for field in ("original_repo", "original_commit", "original_path", "original_blob_sha"):
        if not source.get(field):
            raise TypeFailure("Source ledger lacks immutable source provenance")
    key = (source["original_repo"], source["original_commit"], source["original_path"])
    if inventory.get(key) != source["original_blob_sha"]:
        raise TypeFailure("Source differs from Phase 1 immutable object lock")
    anchor = record.get("anchor")
    if not isinstance(anchor, str) or anchor not in source["original_statement"]:
        raise TypeFailure("Normalized AST does not match its declared original source anchor")
    if record.get("shape") not in ALLOWED_SHAPES:
        raise TypeFailure("Unrecognized declared output shape")
    if record.get("units") not in {"dimensionless", "normalized_Q_L", "natural_mass_dimensions"}:
        raise TypeFailure("Unrecognized or mixed unit system")
    symbols = record.get("symbols")
    if not isinstance(symbols, dict) or not symbols:
        raise TypeFailure("Missing scoped symbol definitions")
    lhs = infer(record["lhs"], symbols)
    rhs = infer(record["rhs"], symbols)
    if lhs.shape != record["shape"] or rhs.shape != record["shape"]:
        raise TypeFailure("Output shape disagrees with declared field type")
    if lhs != rhs:
        raise TypeFailure(f"Dimensional/shape mismatch across equality: {lhs} != {rhs}")
    return {"id": record["id"], "source_id": record["source_id"],
            "namespace": record["namespace"], "source_commit": source["original_commit"],
            "source_blob": source["original_blob_sha"],
            "source_statement": source["original_statement"],
            "declared_type": {"shape": lhs.shape, "dimension": list(lhs.dimensions),
                              "unit_system": record["units"]},
            "result": "PASS_DECLARED_TYPES_ONLY",
            "meaning": "Source anchor, source Git object, declared AST dimensions and shape are consistent; no equivalence derivation, theorem or physical observation was checked."}

def compile_registry(base=BASE, registry=None, sources=None, lock=None, conflicts=None):
    base = Path(base)
    registry = registry if registry is not None else read_json(base / "typed-registry.json")
    sources = sources if sources is not None else source_rows(base.parent / "phase-1" / "source-equations.csv")
    lock = lock if lock is not None else read_json(base.parent / "phase-1" / "sources.lock.json")
    conflicts = conflicts if conflicts is not None else read_json(base / "conflicts.json")
    if len(sources) != 717:
        raise TypeFailure(f"Expected 717 frozen source inventory rows, got {len(sources)}")
    if len(lock["repositories"]) != 4 or lock.get("files_count") != 209:
        raise TypeFailure("Phase 1 source lock version/scope changed without review")
    records = registry["entries"]
    check_dependencies(records)
    by_source = {x["record_id"]: x for x in sources}
    inventory = source_inventory(lock)
    results, errors, source_ids = [], [], set()
    for record in records:
        key = record.get("source_id")
        if key in source_ids:
            errors.append({"id": record.get("id"), "problem": "Duplicate source ID among typed imports"})
            continue
        source_ids.add(key)
        source = by_source.get(key)
        if source is None:
            errors.append({"id": record.get("id"), "problem": "Missing Phase 1 source row"})
            continue
        try:
            results.append(check_record(record, source, inventory))
        except (TypeFailure, KeyError, ValueError) as exc:
            errors.append({"id": record.get("id"), "problem": str(exc)})
    conflict_items = conflicts["items"]
    if len({c["id"] for c in conflict_items}) != len(conflict_items):
        raise TypeFailure("Duplicate conflict IDs")
    if any(c["status"] != "UNRESOLVED" for c in conflict_items):
        raise TypeFailure("Cross-ontology conflicts are not automatically solved by type checking")
    status_counts = Counter(x["literal_status"] for x in sources)
    result = {
        "schema": "unity-001-phase2-compile-manifest-v1",
        "source_inventory": len(sources), "typed_candidate_count": len(records),
        "typed_pass_count": len(results), "typed_fail_count": len(errors),
        "not_compiled_count": len(sources) - len(results),
        "typed_physical_pass_count": 0,
        "mathematical_equivalence_proved_count": 0,
        "cross_ontology_bridges_closed": 0,
        "open_conflicts": len(conflict_items),
        "phase1_literal_status_counts": dict(sorted(status_counts.items())),
        "checks": results, "failures": errors,
        "conflicts": [{"id": c["id"], "status": c["status"], "category": c["category"]}
                      for c in conflict_items],
        "status": "TYPE_CHECK_FAIL" if errors else "BOUNDED_TYPE_CHECK_PASS_PHYSICS_UNRESOLVED",
        "note": "Only source-link and declared AST type/dimension checks ran. All original source strings and literal audit classifications are preserved in the Phase 1 CSV. No original LaTeX or Lean parser, automatic unit reconciliation, theorem proof, or physical inference."
    }
    return result

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["compile", "validate"])
    parser.add_argument("--out", default=str(BASE / "build" / "manifest.json"))
    args = parser.parse_args()
    output = compile_registry()
    if args.action == "compile":
        target = Path(args.out)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in output.items() if k not in {"checks", "conflicts", "phase1_literal_status_counts", "failures"}}, indent=2))
    return 1 if output["typed_fail_count"] else 0

if __name__ == "__main__":
    raise SystemExit(main())
