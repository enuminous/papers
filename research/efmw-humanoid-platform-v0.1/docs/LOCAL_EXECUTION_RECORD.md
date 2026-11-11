# Local execution record — EFMW Humanoid Platform v0.1

**Date:** 2026-11-11  
**Environment:** Python 3.13.5 (Linux)  
**Scope:** Python stdlib only. No ROS, MoveIt 2, MuJoCo, physics engine, firmware, robot or safety hardware was run.  
**Claim:** local source-level tests and deterministic toy simulation, not a certified robot.

## Command: `python -m unittest discover -s tests -v`

**Exit code:** 0. **Tests:** 35 passed, 0 failed.

```text
test_cannot_promote_missing_evidence (test_supervisor.AssemblyTests.test_cannot_promote_missing_evidence) ... ok
test_cannot_promote_unfrozen (test_supervisor.AssemblyTests.test_cannot_promote_unfrozen) ... ok
test_cannot_promote_without_human_review (test_supervisor.AssemblyTests.test_cannot_promote_without_human_review) ... ok
test_cannot_skip_prerequisites (test_supervisor.AssemblyTests.test_cannot_skip_prerequisites) ... ok
test_cycle_rejected (test_supervisor.AssemblyTests.test_cycle_rejected) ... ok
test_duplicate_stage_never_promotes_twice (test_supervisor.AssemblyTests.test_duplicate_stage_never_promotes_twice) ... ok
test_graph_starts_a0 (test_supervisor.AssemblyTests.test_graph_starts_a0) ... ok
test_no_physical_stage_even_with_fake_evidence (test_supervisor.AssemblyTests.test_no_physical_stage_even_with_fake_evidence) ... ok
test_ranking_only_eligible (test_supervisor.AssemblyTests.test_ranking_only_eligible) ... ok
test_simulation_stages_progress_and_replay (test_supervisor.AssemblyTests.test_simulation_stages_progress_and_replay) ... ok
test_tampered_record_replay_fails (test_supervisor.AssemblyTests.test_tampered_record_replay_fails) ... ok
test_architecture_32_actuation_dof (test_supervisor.ConfigTests.test_architecture_32_actuation_dof) ... ok
test_hazards_all_explicitly_open (test_supervisor.ConfigTests.test_hazards_all_explicitly_open) ... ok
test_requirements_unique_and_unresolved (test_supervisor.ConfigTests.test_requirements_unique_and_unresolved) ... ok
test_all_physical_modes_rejected (test_supervisor.GateTests.test_all_physical_modes_rejected) ... ok
test_low_coherence_never_authorizes (test_supervisor.GateTests.test_low_coherence_never_authorizes) ... ok
test_nan_score_rejected (test_supervisor.GateTests.test_nan_score_rejected) ... ok
test_simulated_candidate_only (test_supervisor.GateTests.test_simulated_candidate_only) ... ok
test_unsafe_conditions_denied_even_high_coherence (test_supervisor.GateTests.test_unsafe_conditions_denied_even_high_coherence) ... ok
test_coherence_bounded_for_long_sequence (test_supervisor.MonitorTests.test_coherence_bounded_for_long_sequence) ... ok
test_config_bounds_rejected (test_supervisor.MonitorTests.test_config_bounds_rejected) ... ok
test_deterministic_state_replay (test_supervisor.MonitorTests.test_deterministic_state_replay) ... ok
test_duplicate_time_rejected (test_supervisor.MonitorTests.test_duplicate_time_rejected) ... ok
test_feature_outside_unit_interval_rejected (test_supervisor.MonitorTests.test_feature_outside_unit_interval_rejected) ... ok
test_future_time_rejected (test_supervisor.MonitorTests.test_future_time_rejected) ... ok
test_invalid_feature_schema_rejected (test_supervisor.MonitorTests.test_invalid_feature_schema_rejected) ... ok
test_nonfinite_input_rejected (test_supervisor.MonitorTests.test_nonfinite_input_rejected) ... ok
test_prior_memory_detects_new_observation (test_supervisor.MonitorTests.test_prior_memory_detects_new_observation) ... ok
test_stale_time_rejected (test_supervisor.MonitorTests.test_stale_time_rejected) ... ok
test_effort_never_exceeds_declared_torque_limit (test_two_link.ClassicalRobotTests.test_effort_never_exceeds_declared_torque_limit) ... ok
test_gravity_compensation_static_equilibrium (test_two_link.ClassicalRobotTests.test_gravity_compensation_static_equilibrium) ... ok
test_mass_matrix_positive_definite (test_two_link.ClassicalRobotTests.test_mass_matrix_positive_definite) ... ok
test_simulation_determinism (test_two_link.ClassicalRobotTests.test_simulation_determinism) ... ok
test_toy_integration_sensible_small_step (test_two_link.ClassicalRobotTests.test_toy_integration_sensible_small_step) ... ok
test_trace_length_and_time_monotonic (test_two_link.ClassicalRobotTests.test_trace_length_and_time_monotonic) ... ok

----------------------------------------------------------------------
Ran 35 tests in 0.035s

OK
```

## Offline demonstrations

### `python examples/simulate_offline.py`

**Exit code:** 0

```text
EHP v0.1 — offline-only simulation, no motor actuation
event=0 phi=0.5000 innovation=0.0000 hold_advisory=False
event=1 phi=0.5600 innovation=0.0000 hold_advisory=False
event=2 phi=0.6128 innovation=0.0000 hold_advisory=False
event=3 phi=0.6593 innovation=0.0000 hold_advisory=False
event=4 phi=0.7002 innovation=0.0000 hold_advisory=False
event=5 phi=0.5904 innovation=0.8000 hold_advisory=True
event=6 phi=0.5003 innovation=0.6800 hold_advisory=True
event=7 phi=0.4280 innovation=0.5780 hold_advisory=True
Physical motion decision: DENIED HARDWARE_NOT_SUPPORTED_BY_REFERENCE | SIMULATION_MODE_ONLY
Simulated assembly documentary stage: A0 PASS
Simulated assembly documentary stage: A1 PASS
Simulated assembly documentary stage: A2 PASS
Can promote hardware A3? FAIL
Event ledger replay: True
NO hardware permission given. No safety certification. All mock approvals are fictional.
```

### `python examples/two_link_offline.py`

**Exit code:** 0

```text
Offline 2DoF simulated standard arm dynamics; no hardware; not EFMW advantage
t=0.00s error=0.1412rad phi=0.500 [telemetry-only]
t=0.30s error=0.0731rad phi=0.620 [telemetry-only]
t=0.50s error=0.0397rad phi=0.625 [telemetry-only]
t=1.00s error=0.0064rad phi=0.615 [telemetry-only]
t=1.50s error=0.0022rad phi=0.680 [telemetry-only]
Trace rows: 20 Final angle: [0.0999511, -0.0996082]
No control-performance or anomaly-detection claim is made from this example.
```

**Limit:** Documentary A0–A2 demonstration PASS uses explicitly fictitious approval strings, not actual human review or build evidence. No physical stage can be promoted by this code, regardless of inputs. The toy arm is two joints, not a finished humanoid, and its traces are constructed. This is not independent replication or scientific evidence for an EFMW-specific effect.
