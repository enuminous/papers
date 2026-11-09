#!/usr/bin/env python3
"""Adversarial source and type-contract tests; no physical claims."""
from __future__ import annotations
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from compile import (TypeFailure, InferredType, compile_registry,
                     infer, check_record, check_dependencies, read_json,
                     source_rows, source_inventory)

REGISTRY = read_json(ROOT / "typed-registry.json")
CONFLICTS = read_json(ROOT / "conflicts.json")
SOURCES = source_rows(ROOT.parent / "phase-1" / "source-equations.csv")
LOCK = read_json(ROOT.parent / "phase-1" / "sources.lock.json")
BY_SOURCE = {s["record_id"]: s for s in SOURCES}
INVENTORY = source_inventory(LOCK)

class Phase2Tests(unittest.TestCase):
    def test_01_inventory_is_unchanged(self):
        self.assertEqual(len(SOURCES), 717)
        self.assertEqual(len(LOCK["repositories"]), 4)
        self.assertEqual(LOCK["files_count"], 209)

    def test_02_bounded_compile(self):
        x = compile_registry(registry=REGISTRY, conflicts=CONFLICTS, sources=SOURCES, lock=LOCK)
        self.assertEqual((x["typed_candidate_count"],x["typed_pass_count"],x["typed_fail_count"]), (9,9,0))
        self.assertEqual(x["not_compiled_count"],708)
        self.assertEqual(x["typed_physical_pass_count"],0)
        self.assertEqual(x["mathematical_equivalence_proved_count"],0)
        self.assertEqual(x["cross_ontology_bridges_closed"],0)
        self.assertEqual(x["open_conflicts"],8)

    def test_03_source_mismatch_rejected(self):
        item = copy.deepcopy(REGISTRY["entries"][0])
        altered = copy.deepcopy(BY_SOURCE[item["source_id"]])
        altered["original_blob_sha"] = "0" * 40
        with self.assertRaisesRegex(TypeFailure,"immutable object lock"):
            check_record(item, altered, INVENTORY)

    def test_04_no_fake_anchor(self):
        item = copy.deepcopy(REGISTRY["entries"][1])
        item["anchor"] = "an imaginary formal statement"
        with self.assertRaisesRegex(TypeFailure,"source anchor"):
            check_record(item, BY_SOURCE[item["source_id"]], INVENTORY)

    def test_05_dimension_conflict(self):
        syms={"x":{"shape":"scalar","unit":[1,0,0]},"y":{"shape":"scalar","unit":[0,1,0]}}
        with self.assertRaisesRegex(TypeFailure, "Incompatible"):
            infer(["add",["symbol","x"],["symbol","y"]],syms)

    def test_06_shape_conflict(self):
        syms={"x":{"shape":"tensor2_cov","unit":[0,0,0]},"y":{"shape":"components4","unit":[0,0,0]}}
        with self.assertRaisesRegex(TypeFailure,"Incompatible"):
            infer(["sub",["symbol","x"],["symbol","y"]],syms)

    def test_07_nonscalar_multiplication_rejected(self):
        syms={"x":{"shape":"tensor2_cov","unit":[0,0,0]},"y":{"shape":"tensor2_cov","unit":[0,0,0]}}
        with self.assertRaisesRegex(TypeFailure,"explicit contraction"):
            infer(["mul",["symbol","x"],["symbol","y"]],syms)

    def test_08_pow_tensor_rejected(self):
        syms={"x":{"shape":"tensor2_cov","unit":[0,0,0]}}
        with self.assertRaisesRegex(TypeFailure,"Tensor powers"):
            infer(["pow",["symbol","x"],2],syms)

    def test_09_unknown_symbol_rejected(self):
        with self.assertRaisesRegex(TypeFailure,"Unknown"):
            infer(["symbol","undefined"],{})

    def test_10_unsupported_ast_and_depth(self):
        with self.assertRaises(TypeFailure):
            infer(["exec","1+1"],{})
        with self.assertRaises(TypeFailure):
            infer(["neg",["neg",["number",1]]],{},depth=65)

    def test_11_unit_vector_validation(self):
        with self.assertRaises(TypeFailure):
            infer(["symbol","x"],{"x":{"shape":"scalar","unit":[1,0]}})
        with self.assertRaises(TypeFailure):
            infer(["symbol","x"],{"x":{"shape":"scalar","unit":[True,0,0]}})

    def test_12_duplicate_typed_id_fails(self):
        data=copy.deepcopy(REGISTRY["entries"])
        data.append(copy.deepcopy(data[0]))
        with self.assertRaisesRegex(TypeFailure,"Duplicate typed equation ID"):
            check_dependencies(data)

    def test_13_cyclic_dependency_fails(self):
        entries=copy.deepcopy(REGISTRY["entries"][:2])
        entries[0]["depends_on"]=[entries[1]["id"]]
        entries[1]["depends_on"]=[entries[0]["id"]]
        with self.assertRaisesRegex(TypeFailure,"Cycle"):
            check_dependencies(entries)

    def test_14_unknown_dependency_fails(self):
        entries=copy.deepcopy(REGISTRY["entries"][:1])
        entries[0]["depends_on"]=["UNKNOWN"]
        with self.assertRaisesRegex(TypeFailure,"Unknown typed dependency"):
            check_dependencies(entries)

    def test_15_bad_ledger_source_id(self):
        registry=copy.deepcopy(REGISTRY)
        registry["entries"][0]["source_id"]="FABRICATED"
        result=compile_registry(registry=registry, conflicts=CONFLICTS, sources=SOURCES, lock=LOCK)
        self.assertEqual(result["typed_fail_count"],1)

    def test_16_claim_inflation_rejected(self):
        item=copy.deepcopy(REGISTRY["entries"][0])
        item["status"]="PHYSICALLY_PROVED"
        with self.assertRaisesRegex(TypeFailure,"silently promoted"):
            check_record(item,BY_SOURCE[item["source_id"]],INVENTORY)

    def test_17_frozen_literal_status_retained(self):
        counts=compile_registry(registry=REGISTRY, conflicts=CONFLICTS, sources=SOURCES, lock=LOCK)["phase1_literal_status_counts"]
        self.assertEqual(counts["FAIL_SIGN"],360)
        self.assertEqual(counts["FAIL_NEUTRAL_SCALAR_CURRENT"],88)
        self.assertEqual(counts["INDEX_REPAIR_REQUIRED"],90)
        self.assertEqual(counts["UNDERDEFINED_STRESS"],45)
        self.assertEqual(counts["UNDERDEFINED_CURRENT"],2)

    def test_18_conflicts_are_all_unresolved(self):
        self.assertEqual(len(CONFLICTS["items"]),8)
        self.assertTrue(all(c["status"]=="UNRESOLVED" for c in CONFLICTS["items"]))

    def test_19_bad_rhs_is_reported_without_promotion(self):
        registry=copy.deepcopy(REGISTRY)
        registry["entries"][1]["rhs"]=["number",3]
        out=compile_registry(registry=registry, conflicts=CONFLICTS, sources=SOURCES, lock=LOCK)
        self.assertEqual(out["typed_fail_count"],1)
        self.assertEqual(out["typed_pass_count"],8)
        self.assertEqual(out["typed_physical_pass_count"],0)

    def test_20_namespaces_are_not_assumed_equivalent(self):
        records=REGISTRY["entries"]
        self.assertNotEqual(records[0]["namespace"],records[3]["namespace"])
        self.assertNotEqual(records[6]["namespace"],records[7]["namespace"])
        self.assertTrue(all("limits" in r and r["limits"] for r in records))

if __name__=="__main__":
    unittest.main(verbosity=2)
