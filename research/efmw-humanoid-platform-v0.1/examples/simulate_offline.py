"""Demonstration-only EHP v0.1 memory telemetry and simulated assembly ledger."""
from __future__ import annotations
import pathlib
import sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from prototype.efmw_supervisor import (
    Observation, OfflineCoherenceMonitor, SafetySnapshot, assess_candidate,
    load_assembly_graph,
)
ROOT=pathlib.Path(__file__).resolve().parents[1]
feature_names=('tracking_error','sensor_innovation','contact_disagreement','thermal_margin_risk')
monitor=OfflineCoherenceMonitor()
print('EHP v0.1 — offline-only simulation, no motor actuation')
for n in range(8):
    t=n*0.1
    f={name:float(0.1 if n<5 else 0.9) for name in feature_names}
    result=monitor.update(Observation(t,f,n>=5),now_s=t)
    print(f'event={n} phi={result.coherence:.4f} innovation={result.innovation:.4f} hold_advisory={result.recommended_hold}')
status=assess_candidate(SafetySnapshot(mode='FIXED_BASE_RESTRICTED',
    human_authorized=True,sensors_fresh=True,model_version_matches=True,
    emergency_stop_latched=False,safety_permit=True,hardware_motion_requested=True),
    efmw_score=1.0)
print('Physical motion decision:',status.outcome, ' | '.join(status.reasons))
ledger=load_assembly_graph(str(ROOT/'config/assembly_graph.json'))
for stage_id in ('A0','A1','A2'):
    stage=ledger.stages[stage_id]
    evidence={name:'DEMO-MOCK:'+name for name in stage['required_evidence']}
    print('Simulated assembly documentary stage:', stage_id,
          ledger.promote_simulation_stage(stage_id,evidence=evidence,
                                          human_review='DEMO-HUMAN-APPROVAL-PLACEHOLDER',
                                          frozen_revision='DEMO-FROZEN-REVISION'))
print('Can promote hardware A3?',ledger.promote_simulation_stage('A3',
    evidence={name:'DEMO:'+name for name in ledger.stages['A3']['required_evidence']},
    human_review='DEMO',frozen_revision='DEMO'))
print('Event ledger replay:',ledger.replay())
print('NO hardware permission given. No safety certification. All mock approvals are fictional.')
