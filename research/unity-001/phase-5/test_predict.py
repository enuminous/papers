"""UNITY-001 Phase 5: 25 source, rank, sensitivity and non-promotion checks."""
from __future__ import annotations
import copy
import sys
import unittest
from fractions import Fraction as F
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parent))
import predict as p

class Phase5Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.protocol=p.get_json(p.HERE/"PROTOCOL.json")
        cls.r,cls.s,cls.n0,cls.n1,cls.n2=p.templates(cls.protocol)
        cls.y0,cls.y1,cls.kappa,cls.sigma=p.simulate(cls.protocol,cls.s,cls.n0)

    def test_01_provenance_frozen(self):
        self.assertEqual(p.frozen_source_guard(self.protocol)["source_repos_checked"],3)
    def test_02_phase2_conflicts_still_open(self):
        self.assertEqual(p.frozen_source_guard(self.protocol)["preserved_phase2_conflicts"],8)
    def test_03_eight_distinct_radii(self):
        self.assertEqual(self.r,[F(x) for x in range(1,9)])
    def test_04_spherical_inside_mass(self):
        self.assertEqual(p.enclosed_mass(F(2),F(4)),F(1,8))
    def test_05_spherical_outside_mass(self):
        self.assertEqual(p.enclosed_mass(F(7),F(4)),1)
    def test_06_spherical_continuity_at_boundary(self):
        self.assertEqual(p.enclosed_mass(F(4),F(4)),1)
    def test_07_source_profile_predeclared(self):
        self.assertEqual(self.s[0],F(1,4))
        self.assertEqual(self.s[3],1)
        self.assertEqual(self.s[4],F(16,25))
        self.assertEqual(self.s[7],F(1,4))
    def test_08_illegal_radius_rejected(self):
        with self.assertRaises(ValueError): p.enclosed_mass(0,4)
    def test_09_exact_solve(self):
        self.assertEqual(p.solve([[2,1],[1,1]],[3,2]),[1,1])
    def test_10_rank_deficiency_detected(self):
        with self.assertRaisesRegex(ValueError,"SINGULAR"):
            p.solve([[1,1],[1,1]],[2,2])
    def test_11_projection_baseline_orthogonality(self):
        residual=p.residual(self.n0,self.s)
        for col in self.n0: self.assertEqual(p.dot(col,residual),0)
    def test_12_baseline_fisher_positive(self):
        result=p.profile(self.n0,self.s,self.sigma)
        self.assertGreater(F(result["profile_fisher"]),0)
    def test_13_strong_conventional_fisher_zero(self):
        result=p.profile(self.n1,self.s,self.sigma)
        self.assertEqual(result["status"],"UNIDENTIFIABLE")
        self.assertEqual(result["profile_fisher"],"0")
    def test_14_near_degeneracy_not_exact(self):
        result=p.profile(self.n2,self.s,self.sigma)
        self.assertEqual(result["status"],"IDENTIFIABLE_CONDITIONAL_ON_NUISANCE_FAMILY")
        self.assertGreater(F(result["profile_fisher"]),0)
    def test_15_near_toy_sensitivity_worse(self):
        base=p.profile(self.n0,self.s,self.sigma)
        near=p.profile(self.n2,self.s,self.sigma)
        self.assertGreater(near["sigma_kappa"],100*base["sigma_kappa"])
    def test_16_sigma_rescaling(self):
        base=p.profile(self.n0,self.s,self.sigma)
        large=p.profile(self.n0,self.s,2*self.sigma)
        self.assertEqual(F(large["profile_fisher"]),F(base["profile_fisher"])/4)
    def test_17_zero_sigma_rejected(self):
        with self.assertRaises(ValueError):p.profile(self.n0,self.s,0)
    def test_18_invalid_nuisance_dimensions_rejected(self):
        with self.assertRaises(ValueError):p.project([[1,2]],self.s)
    def test_19_null_and_injection_shift(self):
        null=p.profile(self.n0,self.s,self.sigma,self.y0)
        alt=p.profile(self.n0,self.s,self.sigma,self.y1)
        self.assertEqual(F(alt["fit_kappa"])-F(null["fit_kappa"]),F(1,2))
    def test_20_null_does_not_cross_nominal_threshold(self):
        null=p.profile(self.n0,self.s,self.sigma,self.y0)
        self.assertLess(abs(null["fit_kappa_float"]),null["nominal_5sigma_threshold"])
    def test_21_injection_crosses_narrow_only_threshold(self):
        alt=p.profile(self.n0,self.s,self.sigma,self.y1)
        self.assertGreater(abs(alt["fit_kappa_float"]),alt["nominal_5sigma_threshold"])
    def test_22_exact_colocated_nuisance_absorbs_injected(self):
        null=p.profile(self.n1,self.s,self.sigma,self.y0)
        alt=p.profile(self.n1,self.s,self.sigma,self.y1)
        self.assertEqual(null["status"],"UNIDENTIFIABLE")
        self.assertEqual(alt["status"],"UNIDENTIFIABLE")
    def test_23_full_gate_ledger(self):
        result=p.run()
        self.assertEqual(result["counts"],{"PASS":4,"FAIL":1,"UNRESOLVED":6})
        self.assertEqual(len(result["findings"]),11)
    def test_24_no_physical_promotion(self):
        result=p.run()
        self.assertEqual(result["readiness_verdict"],"NOT_READY_FOR_CONFIRMATORY_PHYSICAL_PREDICTION")
        self.assertEqual(result["efmw_specific_physical_pass"],0)
        self.assertTrue(all(v=="UNRESOLVED" for v in result["physical_readiness"].values()))
    def test_25_fixed_seed_free_simulation_replay(self):
        self.assertEqual(p.run(),p.run())

if __name__=="__main__":
    unittest.main(verbosity=2)
