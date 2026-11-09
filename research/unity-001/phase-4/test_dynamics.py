"""Phase 4 adversarial tests: exact rational finite polynomial checks only."""
import copy
import json
import sys
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parent))
import dynamics as d

class TestDynamics(unittest.TestCase):
    def setUp(self):
        self.t,self.x,self.y,self.z=(d.Poly.variable(i) for i in range(4))
        self.A=d.vec(0,self.t**2,self.x*self.t,0)

    def test_01_phase_1_source_guard(self):
        s=d.source_guard()
        self.assertEqual(s["phase2_held_conflicts"],8)
        self.assertIn("C1_candidate",s["sources"])

    def test_02_fraction_coercion(self):
        self.assertEqual(d.Poly.const(Fraction(1,2))+Fraction(1,2),1)

    def test_03_product_rule(self):
        f=self.t**3+self.t*self.x
        g=self.t**2+self.x
        self.assertEqual((f*g).diff(0),f.diff(0)*g+f*g.diff(0))

    def test_04_commuting_partials(self):
        p=self.t**3*self.x*self.y+self.z**2*self.x
        self.assertEqual(p.diff(0).diff(1),p.diff(1).diff(0))

    def test_05_polynomial_evaluation(self):
        self.assertEqual((self.t*self.x+Fraction(1,2)).evaluate([2,3,0,0]),Fraction(13,2))

    def test_06_negative_exp_rejected(self):
        with self.assertRaises(ValueError):
            d.Poly({(-1,0,0,0):1})

    def test_07_bad_noninteger_exp_rejected(self):
        with self.assertRaises(ValueError):
            d.Poly({(True,0,0,0):1})

    def test_08_bad_variable_axis(self):
        with self.assertRaises(ValueError):
            d.Poly.variable(4)

    def test_09_bad_exponent_pow(self):
        with self.assertRaises(ValueError):
            self.t**-1

    def test_10_no_nonconstant_division(self):
        with self.assertRaises(ValueError):
            self.t/(self.t+1)

    def test_11_gauge_invariance_explicit(self):
        chi=self.t*self.x**2+self.y**3
        self.assertEqual(d.field(d.gauge_shift(self.A,chi)),d.field(self.A))

    def test_12_Bianchi_explicit(self):
        self.assertTrue(all(not x for x in d.bianchi(d.field(self.A))))

    def test_13_maxwell_sourceful_divergence(self):
        F=d.field(d.vec(0,self.t**2,0,0))
        self.assertTrue(any(d.maxwell_current(F)))
        self.assertTrue(any(d.stress_divergence(d.stress(F))))

    def test_14_stress_force_identity(self):
        F=d.field(self.A)
        self.assertEqual(d.stress_divergence(d.stress(F)),
                         d.lorentz_force(F,d.maxwell_current(F)))

    def test_15_wrong_force_sign_rejected(self):
        F=d.field(d.vec(0,self.t**2,0,0))
        lhs=d.stress_divergence(d.stress(F))
        rhs=d.lorentz_force(F,d.maxwell_current(F))
        self.assertNotEqual(lhs,tuple(-v for v in rhs))

    def test_16_wrong_stress_trace_rejected(self):
        F=d.field(d.vec(0,self.t**2,0,0))
        stress=[list(row) for row in d.stress(F)]
        stress[0][0]+=self.t**2
        self.assertNotEqual(d.stress_divergence(stress),
                            d.lorentz_force(F,d.maxwell_current(F)))

    def test_17_sourcefree_plane_wave(self):
        a=d.vec(0,0,(self.t-self.x)**3,0)
        F=d.field(a)
        self.assertFalse(any(d.maxwell_current(F)))
        self.assertFalse(any(d.stress_divergence(d.stress(F))))

    def test_18_maxwell_deterministic(self):
        self.assertEqual(d.maxwell_checks(5),d.maxwell_checks(5))

    def test_19_maxwell_complete_bounded_trials(self):
        r=d.maxwell_checks()
        self.assertEqual(r["Bianchi_component_checks"],768)
        self.assertEqual(r["off_shell_stress_divergence_checks"],48)
        self.assertEqual(r["gauge_shift_checks"],12)
        self.assertGreater(r["sourceful_random_examples"],0)

    def test_20_nonconserved_neutral_current_counterexample(self):
        result=d.scalar_current_counterexample()
        self.assertEqual(result["divergence"],"-1")
        self.assertTrue(result["status"].startswith("FAIL_"))

    def test_21_WITD_frozen_h_balance(self):
        b=d.witd_manufactured_balance(False)
        self.assertTrue(b["exact_polynomial_residual_zero_with_required_work"])
        self.assertFalse(b["energy_defect_if_h_work_omitted"])

    def test_22_WITD_h_changing_work(self):
        b=d.witd_manufactured_balance(True)
        self.assertTrue(b["exact_polynomial_residual_zero_with_required_work"])
        self.assertTrue(b["energy_defect_if_h_work_omitted"])

    def test_23_WITD_tensor_storage_counterexample(self):
        b=d.witd_tensor_obstruction()
        self.assertIn("3/2",b["second_witness_q_zero_m_one"])
        self.assertTrue(b["status"].startswith("FAIL_"))

    def test_24_C1_cubic_unbounded(self):
        b=d.c1_scalar_stability()
        self.assertEqual(b["negative_ray_witnesses"]["16"],"-3712")
        self.assertTrue(b["status"].startswith("FAIL_"))

    def test_25_C1_negative_trend(self):
        vals=[Fraction(v) for v in d.c1_scalar_stability()["negative_ray_witnesses"].values()]
        self.assertTrue(all(vals[i+1]<vals[i] for i in range(len(vals)-1)))

    def test_26_all_claims_scoped(self):
        r=d.run()
        self.assertEqual(r["counts"],{"PASS":4,"FAIL":3,"UNRESOLVED":5})
        self.assertEqual(len(r["findings"]),12)
        self.assertEqual(r["efmw_specific_physical_pass"],0)

    def test_27_no_curved_metric_pretence(self):
        r=d.run()
        self.assertIn("UNRESOLVED",r["phase4_disposition"])
        self.assertTrue(any("curved" in v["scope"] for v in r["findings"] if v["status"]=="UNRESOLVED"))

    def test_28_algebra_does_not_promote_prior_conflicts(self):
        c=d.source_guard()
        self.assertEqual(c["phase2_held_conflicts"],8)

    def test_29_no_false_independent_experiment(self):
        r=d.run()
        self.assertFalse(any("PHYSICAL PASS" in f["status"] for f in r["findings"]))
        self.assertEqual(r["efmw_specific_physical_pass"],0)

if __name__=="__main__":
    unittest.main(verbosity=2)
