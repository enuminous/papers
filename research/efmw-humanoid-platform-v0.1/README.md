# EFMW Humanoid Platform — Engineering Specification v0.1

**Status:** DESIGN PROPOSAL / SIMULATION-FIRST / NO PHYSICAL ROBOT CONSTRUCTED OR CERTIFIED.  
**Prepared:** 2026-11-11 | **Research owner:** Matthew Chenoweth Wright / Monolithic LLC  
**Distribution:** private review bundle; not posted to GitHub.  
**Primary deliverable:** [`SPEC.md`](SPEC.md).

This package defines the intended architecture for a modular, 32-DoF humanoid research platform controlled by established robotic methods and supervised by an **optional**, strictly bounded EFMW-style state/history/coherence monitor. It also defines an **EFMW-guided recursive assembly planner** that proposes a next build/test step, freezes the proposed change, and requires evidence and explicit human authorization before it can advance.

**This is not a ready-to-build consumer robot, safety certification, validated locomotion stack, or claim that EFMW is a new physical field.** No design in this bundle may be used as a substitute for qualified mechanical/electrical/safety review.

## Contents

- `SPEC.md` — full systems engineering specification, interfaces, test criteria, design risks and source register.
- `config/requirements.json` — uniquely identified, evidence-gated requirements.
- `config/hazards.json` — preliminary hazard register and blocking mitigations.
- `config/architecture.json` — hardware/control interface budgets and mode definitions.
- `config/assembly_graph.json` — dependency-ordered, human-approved staged build plan.
- `prototype/two_link_dynamics.py` — conventional 2-DoF coupled rigid-body dynamics and PD baseline (offline only).
- `examples/two_link_offline.py` — deterministic toy arm and telemetry trace; not a performance test.
- `prototype/efmw_supervisor.py` — **non-ROS simulation-only** reference algorithm for bounded memory/coherence supervisor, safety veto, frozen assembly gate and event ledger.
- `tests/test_supervisor.py` — stdlib-only tests of invariants, failure handling and frozen stage gates.
- `examples/simulate_offline.py` — deterministic standalone demonstration.
- `docs/TRACEABILITY.md` — evidence and approval workflow.
- `docs/SOURCES.md` — standards, robotics stack and EFMW canonical sources.
- `diagrams/architecture.mmd` — Mermaid architecture for Markdown/graph renderers.

## Replay this reference prototype

From this folder, with Python 3.10+:

```sh
python -m unittest discover -s tests -v
python examples/simulate_offline.py
python examples/two_link_offline.py
```

These commands **do not move a robot**, access ROS or communicate with actuators. The prototype has no hardware drivers, no ROS topics, no motor output, and no autonomous firmware updates.

## Scientific and engineering interpretation

- `PASS` means a specified *simulation or documentary acceptance criterion* has been met with inspectable evidence.
- `FAIL` means a criterion is contradicted; no promotion to the next gate.
- `UNRESOLVED` means no adequate evidence or approval is available; no promotion.
- For actual hardware, independent engineering validation is required for every hazard-related requirement.

**Guiding principle:** The robot's control can learn and adapt within an approved envelope. It cannot rewrite the envelope it depends on to remain safe.
