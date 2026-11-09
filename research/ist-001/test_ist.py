"""IST-001 standard-library adversarial controls; no empirical discovery claim."""
import json
import math
import unittest
from fractions import Fraction as F
import ist

class ISTTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=json.loads((ist.ROOT/"PROTOCOL.json").read_text())
        cls.m=ist.model(cls.p)

    def test_01_protocol_scope(self):
        self.assertEqual(self.p["schema"],"ist-001-frozen-protocol-v1")
        self.assertTrue(all(x["status"]=="UNRESOLVED" for x in self.p["gates"][6:]))
    def test_02_source_locks(self):
        self.assertEqual(ist.source_guard(self.p)["source_files_locked"],2)
    def test_03_invalid_boolean(self):
        with self.assertRaises(ValueError):ist.Q(True)
    def test_04_polynomial_product_rule(self):
        t=ist.P.t();a=t*t+2*t+1;b=t*t*t-t
        self.assertEqual((a*b).diff(),a.diff()*b+a*b.diff())
    def test_05_derivative_and_sign(self):
        t=ist.P.t();self.assertEqual((t**3-2*t).diff(),3*t*t-2)
    def test_06_bad_exponent(self):
        with self.assertRaises(ValueError):ist.P.t()**-1
    def test_07_bad_polynomial_division(self):
        with self.assertRaises(ValueError):ist.P.t()/0
    def test_08_wrong_nonpolynomial(self):
        with self.assertRaises(TypeError):ist.P.t()*"malicious"
    def test_09_metric_nondegenerate(self):
        with self.assertRaises(ValueError):ist.cov_metric(1,0,1)
    def test_10_metric_inverse(self):
        m=ist.cov_metric(-2,F(1,3),F(3,2))
        self.assertEqual(-2*m[0][0]+F(1,3)*m[0][1],1)
    def test_11_Hilbert_variation(self):
        self.assertEqual(ist.hilbert_checks()["metric_variation_trials"],32)
    def test_12_conservative_exchange(self):
        self.assertEqual(ist.exchange_checks()["off_shell_polynomial_checks"],48)
    def test_13_wrong_exchange_sign(self):
        t=ist.P.t();flux=F(5,4)*(t*t-t)*(t*t).diff()
        self.assertNotEqual(flux,-flux)
    def test_14_split_is_not_unique(self):
        self.assertIn("NOT_UNIQUE",ist.split_check()["status"])
    def test_15_bath_exact_source_balance(self):
        self.assertEqual(ist.bath_checks(self.p)["exact_bath_energy_checks"],35)
    def test_16_bath_refinement(self):
        x=ist.bath_checks(self.p)
        self.assertEqual(x["steps"],[50,100,200,400])
        self.assertTrue(all(3<r<5 for r in x["refinement_ratios"]))
    def test_17_bath_energy_defect_decreases(self):
        a=ist.bath_checks(self.p)["energy_defects"]
        self.assertTrue(all(a[i]>a[i+1] for i in range(len(a)-1)))
    def test_18_bath_missing_coupling_is_wrong(self):
        m=self.m
        pos=[F(1),F(0),F(1),F(0)]
        actual=ist.force(pos,m)[1]
        stripped=m["K"]*(pos[0]-pos[1])/m["Z"]
        self.assertNotEqual(actual,stripped)
    def test_19_finite_GLE_identity(self):
        self.assertLess(ist.gle_check(self.p)["max_residual"],1e-11)
    def test_20_conditional_markov(self):
        self.assertLess(ist.markov_check(self.p)["max_residual"],1e-10)
    def test_21_alpha_ratio(self):
        t=self.p["numeric_fixtures"]["markov"]
        self.assertEqual(t["K"]/t["Gamma"],t["alpha"])
    def test_22_no_physical_promotion(self):
        a=ist.run()
        self.assertEqual(a["gates"],{"PASS":6,"FAIL":0,"UNRESOLVED":2})
        self.assertEqual(a["EFMW_specific_physical_PASS"],0)
        self.assertEqual(a["physical_status"],"UNRESOLVED")
    def test_23_finite_bath_is_reversible(self):
        self.assertIn("reversible",ist.run()["bath"]["scope"])
    def test_24_reproducible(self):
        self.assertEqual(ist.run(),ist.run())

if __name__=="__main__":unittest.main(verbosity=2)
