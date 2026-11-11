"""EHP v0.1 unit tests: source-level simulation contracts, not motor safety tests."""
import json
import pathlib
import unittest
from dataclasses import replace
from prototype.efmw_supervisor import (
    MonitorConfig, Observation, OfflineCoherenceMonitor, SafetySnapshot,
    assess_candidate, OfflineAssemblyLedger, EvidenceError,
)
ROOT=pathlib.Path(__file__).resolve().parents[1]
D=json.loads((ROOT/'config/assembly_graph.json').read_text())
F={'tracking_error':0.1,'sensor_innovation':0.1,
   'contact_disagreement':0.1,'thermal_margin_risk':0.1}
GOOD=SafetySnapshot('SIMULATION',True,True,True,False,True,False)

class MonitorTests(unittest.TestCase):
    def test_coherence_bounded_for_long_sequence(self):
        m=OfflineCoherenceMonitor()
        for i in range(1000):
            f={k:float((i+j)%10)/10 for j,k in enumerate(F)}
            r=m.update(Observation(i*0.1,f,i%7==0),now_s=i*0.1)
            self.assertLessEqual(r.coherence,1)
            self.assertGreaterEqual(r.coherence,0)
            self.assertEqual(r.status,'OBSERVED_SIMULATION_ONLY')
    def test_deterministic_state_replay(self):
        a=OfflineCoherenceMonitor();b=OfflineCoherenceMonitor()
        for t in [0.0,0.05,0.1,0.15]:
            ob=Observation(t,F)
            self.assertEqual(a.update(ob,now_s=t),b.update(ob,now_s=t))
    def test_prior_memory_detects_new_observation(self):
        m=OfflineCoherenceMonitor()
        m.update(Observation(0.0,F),now_s=0.0)
        f={key:0.9 for key in F}
        r=m.update(Observation(0.1,f),now_s=0.1)
        self.assertGreater(r.innovation,0.5)
        self.assertTrue(r.recommended_hold)
    def test_duplicate_time_rejected(self):
        m=OfflineCoherenceMonitor()
        m.update(Observation(1,F),now_s=1)
        with self.assertRaises(EvidenceError):m.update(Observation(1,F),now_s=1)
    def test_stale_time_rejected(self):
        with self.assertRaises(EvidenceError):OfflineCoherenceMonitor().update(Observation(1,F),now_s=1.5)
    def test_future_time_rejected(self):
        with self.assertRaises(EvidenceError):OfflineCoherenceMonitor().update(Observation(2,F),now_s=1)
    def test_nonfinite_input_rejected(self):
        for invalid in [float('nan'),float('inf'),-float('inf')]:
            with self.assertRaises(EvidenceError):OfflineCoherenceMonitor().update(Observation(0,{**F,'tracking_error':invalid}),now_s=0)
    def test_invalid_feature_schema_rejected(self):
        with self.assertRaises(EvidenceError):OfflineCoherenceMonitor().update(Observation(0,{'foo':0.1}),now_s=0)
    def test_feature_outside_unit_interval_rejected(self):
        with self.assertRaises(EvidenceError):OfflineCoherenceMonitor().update(Observation(0,{**F,'sensor_innovation':-0.3}),now_s=0)
    def test_config_bounds_rejected(self):
        for conf in [dict(alpha=0),dict(beta=2),dict(k=-1),dict(max_age_s=0)]:
            with self.assertRaises(EvidenceError):MonitorConfig(**conf)

class GateTests(unittest.TestCase):
    def test_simulated_candidate_only(self):
        d=assess_candidate(GOOD,efmw_score=0.8)
        self.assertEqual(d.outcome,'SIMULATED_CANDIDATE_OK')
        self.assertFalse(d.is_physical_motion_authorized)
    def test_all_physical_modes_rejected(self):
        for mode in ['BENCH_LOW_ENERGY','FIXED_BASE_RESTRICTED','HARNESS_RESTRICTED']:
            d=assess_candidate(replace(GOOD,mode=mode,hardware_motion_requested=True),efmw_score=1.0)
            self.assertEqual(d.outcome,'DENIED')
            self.assertFalse(d.is_physical_motion_authorized)
    def test_unsafe_conditions_denied_even_high_coherence(self):
        for kw in [dict(human_authorized=False),dict(sensors_fresh=False),
                   dict(model_version_matches=False),dict(emergency_stop_latched=True),
                   dict(safety_permit=False),dict(hardware_motion_requested=True)]:
            d=assess_candidate(replace(GOOD,**kw),efmw_score=1.0)
            self.assertEqual(d.outcome,'DENIED')
            self.assertFalse(d.is_physical_motion_authorized)
    def test_low_coherence_never_authorizes(self):
        d=assess_candidate(GOOD,efmw_score=0.1)
        self.assertEqual(d.outcome,'DENIED')
        self.assertFalse(d.is_physical_motion_authorized)
        self.assertIn('EFMW_RECOMMENDS_HOLD_ADVISORY',d.reasons)
    def test_nan_score_rejected(self):
        with self.assertRaises(EvidenceError):assess_candidate(GOOD,efmw_score=float('nan'))

class AssemblyTests(unittest.TestCase):
    def setUp(self):self.a=OfflineAssemblyLedger(D)
    def stage_evidence(self,id):return {k:'artifact:'+k for k in self.a.stages[id]['required_evidence']}
    def pass_stage(self,id):
        return self.a.promote_simulation_stage(id,evidence=self.stage_evidence(id),human_review='TEST-REVIEWER-NOT-REAL-SIGNATURE',frozen_revision='test-hash')
    def test_graph_starts_a0(self):self.assertEqual(self.a.suggest_next(),['A0'])
    def test_cannot_skip_prerequisites(self):
        self.assertEqual(self.pass_stage('A2'),'UNRESOLVED')
        self.assertEqual(self.a.accepted,set())
    def test_cannot_promote_without_human_review(self):
        self.assertEqual(self.a.promote_simulation_stage('A0',evidence=self.stage_evidence('A0'),human_review='',frozen_revision='x'),'UNRESOLVED')
    def test_cannot_promote_missing_evidence(self):
        self.assertEqual(self.a.promote_simulation_stage('A0',evidence={},human_review='review',frozen_revision='x'),'UNRESOLVED')
    def test_cannot_promote_unfrozen(self):
        self.assertEqual(self.a.promote_simulation_stage('A0',evidence=self.stage_evidence('A0'),human_review='review',frozen_revision=''),'UNRESOLVED')
    def test_simulation_stages_progress_and_replay(self):
        self.assertEqual(self.pass_stage('A0'),'PASS')
        self.assertEqual(self.a.suggest_next(),['A1'])
        self.assertEqual(self.pass_stage('A1'),'PASS')
        self.assertEqual(self.a.suggest_next(),['A2'])
        self.assertEqual(self.pass_stage('A2'),'PASS')
        self.assertEqual(self.a.suggest_next(),[])
        self.assertTrue(self.a.replay())
    def test_no_physical_stage_even_with_fake_evidence(self):
        for s in self.a.stages.values():
            if s['physical']:
                self.assertEqual(self.pass_stage(s['id']),'FAIL')
        self.assertEqual(self.a.accepted,set())
    def test_tampered_record_replay_fails(self):
        self.pass_stage('A0');self.assertTrue(self.a.replay())
        self.a.events[0]['reason']='FORGED_PASS';self.assertFalse(self.a.replay())
    def test_duplicate_stage_never_promotes_twice(self):
        self.assertEqual(self.pass_stage('A0'),'PASS')
        self.assertEqual(self.pass_stage('A0'),'FAIL')
    def test_cycle_rejected(self):
        copy=json.loads(json.dumps(D))
        copy['stages'][0]['depends_on']=['A2']
        with self.assertRaises(EvidenceError):OfflineAssemblyLedger(copy)
    def test_ranking_only_eligible(self):
        self.assertEqual(self.a.suggest_next({'A0':0.9}),['A0'])
        with self.assertRaises(EvidenceError):self.a.suggest_next({'A0':1.9})

class ConfigTests(unittest.TestCase):
    def test_architecture_32_actuation_dof(self):
        arch=json.loads((ROOT/'config/architecture.json').read_text())
        joints=[name for names in arch['joint_names_by_module'].values() for name in names]
        self.assertEqual(len(joints),32)
        self.assertEqual(len(set(joints)),32)
        self.assertFalse(arch['hardware_motion_authorized'])
    def test_hazards_all_explicitly_open(self):
        hazards=json.loads((ROOT/'config/hazards.json').read_text())['hazards']
        self.assertEqual(len(hazards),12)
        self.assertTrue(all(x['status']=='UNRESOLVED' for x in hazards))
    def test_requirements_unique_and_unresolved(self):
        requirements=json.loads((ROOT/'config/requirements.json').read_text())['requirements']
        self.assertEqual(len(requirements),35)
        self.assertEqual(len({x['id'] for x in requirements}),35)
        self.assertTrue(all(x['status']=='UNRESOLVED' for x in requirements))

if __name__=='__main__':unittest.main()
