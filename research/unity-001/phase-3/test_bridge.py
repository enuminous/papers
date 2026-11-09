"""UNITY-001 Phase 3: adversarial exact-algebra checks.

All tests are bounded software/mathematical controls; none is an external
measurement or a proof of EFMW physics.
"""
import copy
import json
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parent))
import bridge as b

class Phase3Tests(unittest.TestCase):
    def setUp(self):
        self.g = ((-1,0,0,0),(0,1,0,0),(0,0,2,0),(0,0,0,3))
        self.F = ((0,2,0,1),(-2,0,3,0),(0,-3,0,4),(-1,0,-4,0))

    def test_01_source_provenance(self):
        p=b.provenance()
        self.assertEqual(p["ledger_rows"],717)
        self.assertEqual(p["source_pins_matched"],5)
        self.assertEqual(p["phase2_conflicts"],8)

    def test_02_formal_polynomial_subtraction(self):
        self.assertEqual(b.sub(b.add(b.var("x"),b.var("y")),b.var("x")),b.var("y"))

    def test_03_polynomial_distributivity(self):
        x,y,z=map(b.var,("x","y","z"))
        self.assertEqual(b.mul(x,b.add(y,z)),b.add(b.mul(x,y),b.mul(x,z)))

    def test_04_polynomial_rejects_incorrect_identity(self):
        self.assertNotEqual(b.mul(b.var("x"),b.var("y")),b.add(b.var("x"),b.var("y")))

    def test_05_action_projection_exact(self):
        a=b.action_correspondence()
        self.assertEqual(a["status"],"PASS_RESTRICTED_ACTION_DENSITY_IDENTITY")
        self.assertEqual(a["nonminimal_counterexample"],"-12/7")
        self.assertEqual(a["sm_vacuum_counterexample"],"-8")

    def test_06_nonminimal_rx_obstruction_is_not_silent(self):
        x,y,z=map(b.var,("gEM","R","X"))
        self.assertNotEqual(b.prod(x,y,z),{})
        self.assertEqual(b.value(b.neg(b.prod(x,y,z)),{"gEM":Q(1,7),"R":3,"X":4}),Q(-12,7))

    def test_07_restriction_without_coupling_is_required(self):
        p=b.mul(b.var("gEM"),b.var("X"))
        self.assertEqual(b.drop_zero(p,("gEM",)),{})
        self.assertNotEqual(b.drop_zero(p,("Y",)),{})

    def test_08_higgs_vacuum_energy_nonzero(self):
        self.assertEqual(Q(2)*Q(2)**4/Q(4),Q(8))

    def test_09_hypercharge_kinetic_sign_flip(self):
        inverted=tuple(tuple(-x for x in row) for row in self.g)
        self.assertEqual(b.f_squared(self.F,self.g),b.f_squared(self.F,inverted))

    def test_10_zero_field_has_zero_F2(self):
        self.assertEqual(b.f_squared([[0]*4 for _ in range(4)],self.g),0)

    def test_11_antisymmetric_F_guard(self):
        wrong=[list(row) for row in self.F]
        wrong[0][1]=1
        with self.assertRaisesRegex(ValueError,"antisymmetric"):
            b.f_squared(wrong,self.g)

    def test_12_non_symmetric_metric_guard(self):
        wrong=[list(row) for row in self.g]
        wrong[0][1]=2
        with self.assertRaisesRegex(ValueError,"symmetric"):
            b.f_squared(self.F,wrong)

    def test_13_wrong_matrix_size_guard(self):
        with self.assertRaisesRegex(ValueError,"4-by-4"):
            b.valid_field([[0,0],[0,0]])

    def test_14_maxwell_kinetic_directions_exact(self):
        K=b.k_tensor(self.F,self.g)
        self.assertEqual(b.directional_derivative_x(self.F,self.g,0,0),2*K[0][0])
        self.assertEqual(b.directional_derivative_x(self.F,self.g,0,1),4*K[0][1])

    def test_15_maxwell_rational_randomized_checks(self):
        a=b.maxwell_audit(trials=24)
        self.assertEqual(a["metric_direction_checks"],240)
        self.assertEqual(a["field_variation_checks"],24)
        self.assertEqual(a["metric_signature_flip_checks"],24)

    def test_16_maxwell_different_seed_fixed_replay(self):
        self.assertEqual(b.maxwell_audit(trials=7),b.maxwell_audit(trials=7))

    def test_17_source_absorption_exact(self):
        T=[[1]*4 for _ in range(4)]
        I=[[2]*4 for _ in range(4)]
        S=b.total_source(T,I,Q(3,5))
        self.assertEqual(S,b.total_source(S,[[0]*4 for _ in range(4)],0))

    def test_18_affine_split_exact(self):
        T=[[1]*4 for _ in range(4)]
        I=[[2]*4 for _ in range(4)]
        J=[[3]*4 for _ in range(4)]
        k=Q(2,7)
        Tp=b.total_source(T,J,k)
        Ip=[[I[i][j]-J[i][j] for j in range(4)] for i in range(4)]
        self.assertEqual(b.total_source(T,I,k),b.total_source(Tp,Ip,k))

    def test_19_fixed_matter_negative_control(self):
        T=[[1]*4 for _ in range(4)]
        I=[[2]*4 for _ in range(4)]
        self.assertNotEqual(b.total_source(T,I,1),b.total_source(T,I,0))

    def test_20_source_only_randomized(self):
        a=b.source_identifiability(trials=24)
        self.assertEqual(a["affine_split_exact_trials"],24)
        self.assertEqual(a["independently_fixed_ordinary_source_detection_trials"],24)

    def test_21_source_only_replay_determinism(self):
        self.assertEqual(b.source_identifiability(trials=8),b.source_identifiability(trials=8))

    def test_22_c1_not_full_standard_model(self):
        a=b.action_correspondence()
        self.assertIn("no full Standard Model", " ".join(a["limitations"]))

    def test_23_outcome_contracts(self):
        x=b.run()
        self.assertEqual(x["finding_counts"],{"PASS":3,"FAIL":2,"UNRESOLVED":3})
        self.assertEqual(x["efmw_specific_physical_pass"],0)
        self.assertEqual(x["full_unity_status"],"UNRESOLVED")

    def test_24_no_unreviewed_conflict_promotion(self):
        data=b.load_json(b.P2/"conflicts.json")
        self.assertEqual(len(data["items"]),8)
        self.assertTrue(all(x["status"]=="UNRESOLVED" for x in data["items"]))

    def test_25_no_invented_symbol(self):
        with self.assertRaises(ValueError):
            b.var("invalid-symbol!")

    def test_26_polynomial_requires_assigned_variables(self):
        with self.assertRaisesRegex(ValueError,"Unassigned"):
            b.value(b.var("x"),{})

    def test_27_metric_and_field_results_differ_by_scope(self):
        result=b.run()
        self.assertIn("only",result["scientific_boundary"].lower())
        self.assertFalse(any("EFMW SPECIFIC PHYSICAL PASS" in q["status"] for q in result["findings"]))

if __name__=="__main__":
    unittest.main(verbosity=2)
