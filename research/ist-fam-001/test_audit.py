"""IST-FAM-001 adversarial controls; test coverage is not physical validation."""
import csv
import io
import unittest
import audit

class AuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol, cls.rows = audit.read_locked()
        cls.result = audit.analyze()

    def test_01_original_v1_protocol_immutable(self):
        self.assertEqual(audit.gitblob(audit.PROTOCOL.read_bytes()),audit.EXPECTED_BLOBS["research/ist-fam-001/PROTOCOL.json"])
        self.assertEqual(len(self.protocol["candidate_constraints"]),2)
    def test_02_pre_execution_tightening_present(self):
        s=audit.REVIEW_RULES.read_text()
        self.assertIn("Full source-defined sequence",s)
        self.assertIn("guess",s)
        self.assertIn("PASS is not novel gravity",s)
    def test_03_full_717_source_coverage(self):
        self.assertEqual(len(self.rows),717)
        self.assertEqual(self.result["screening"]["records_examined"],717)
    def test_04_group_counts(self):
        self.assertEqual(self.result["source_lock"]["group_counts"],{"historical_fieldspace_source":585,"canonical":102,"selected_source_pointers":30})
    def test_05_unique_ids(self):
        self.assertEqual(len({r["record_id"] for r in self.rows}),717)
    def test_06_exact_frozen_source_ledger_blob(self):
        self.assertEqual(audit.gitblob(audit.LEDGER.read_bytes()),"aff2302bcbad8759f6302f8b218cf029dfc3de2a")
    def test_07_avoid_candidate_expression_contamination(self):
        self.assertNotIn("audit_candidate_expression",self.result["source_lock"]["source_fields_screened"])
        self.assertIn("audit_candidate_expression",self.result["source_lock"]["excluded_evidence_fields"])
    def test_08_explicit_oscillator_terms_are_detected_if_added(self):
        x=dict(self.rows[0]);x["original_statement"]="reservoir with ordered oscillator bath frequency modes"
        self.assertIn("DIRECT_OSCILLATOR_OR_SPECTRAL_VOCABULARY",audit.classify_row(x)["flags"])
    def test_09_canonical_recursive_frequency_is_not_a_bath_map(self):
        x=next(r for r in self.rows if r["record_id"]=="ME-075")
        y=audit.classify_row(x)
        self.assertIn("FREQUENCY_SYMBOL",y["flags"])
        self.assertNotIn("DIRECT_OSCILLATOR_OR_SPECTRAL_VOCABULARY",y["flags"])
    def test_09b_capital_omega_does_not_count_as_frequency(self):
        cosmic=next(r for r in self.rows if r["record_id"]=="ME-055")
        self.assertNotIn("FREQUENCY_SYMBOL",audit.classify_row(cosmic)["flags"])
        recursive=next(r for r in self.rows if r["record_id"]=="ME-076")
        self.assertIn("FREQUENCY_SYMBOL",audit.classify_row(recursive)["flags"])
    def test_10_golden_scale_is_not_source_defined_bath(self):
        for name in ["ME-041","ME-042","ME-043","ME-044","ME-085"]:
            r=next(x for x in self.rows if x["record_id"]==name)
            self.assertIn("MANUALLY_REVIEWED_NEAR_MISS",audit.classify_row(r)["flags"])
    def test_11_h1_source_support_absent_not_false_theorem(self):
        self.assertEqual(self.result["H1"]["source_support"],"NO_SOURCE_SUPPORT")
        self.assertEqual(self.result["H1"]["full_source_defined_sequence_test"],"NOT_APPLICABLE_MISSING_MAP")
    def test_12_h2_exponent_is_guess_not_derived(self):
        self.assertEqual(self.result["H2"]["source_support"],"NO_SOURCE_SUPPORT")
        self.assertIn("guessed",self.result["H2"]["reason"])
    def test_13_no_physical_promotion(self):
        self.assertEqual(self.result["H1"]["physical_novelty"],"NOT_ESTABLISHED")
        self.assertEqual(self.result["H2"]["physical_novelty"],"NOT_ESTABLISHED")
    def test_14_stop_rule_is_bounded(self):
        self.assertEqual(self.result["bounded_stop_rule"],"INVOKED_NOT_ESTABLISHED_IN_FROZEN_CORPUS")
        self.assertIn("No general impossibility theorem",self.result["beyond_scope"])
    def test_15_row_screen_reaches_all_source_types(self):
        groups={audit.classify_row(r)["group"] for r in self.rows}
        self.assertEqual(len(groups),3)
    def test_16_near_miss_ledger_has_source_coordinates(self):
        self.assertTrue(all(x["original_path"] and x["source_line"] for x in self.result["near_misses"]))
    def test_17_source_lock_commit_coordinates(self):
        self.assertEqual(len({(r["original_repo"],r["original_commit"],r["original_path"]) for r in self.rows}),7)
    def test_18_no_independent_experiment_claim(self):
        self.assertIn("no claim of external peer review",self.result["beyond_scope"])

if __name__=="__main__":
    unittest.main(verbosity=2)
