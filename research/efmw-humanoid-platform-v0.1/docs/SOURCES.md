# Research and engineering sources — 2026-11-11 snapshot

This is a source guide to independently maintained standards or documentation, **not** evidence that the proposed humanoid implements those standards or tools. Check version status and licensing before reuse.

## Robotics software and simulation

- ROS 2 supported releases (Jazzy through May 2029; Lyrical through May 2031): https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst
- ros2_control architecture and controller manager: https://control.ros.org/master/doc/ros2_control/doc/index.html
- ros2_control controller manager: https://control.ros.org/master/doc/ros2_control/controller_manager/doc/userdoc.html
- MoveIt 2 motion planning and manipulation: https://moveit.picknik.ai/
- MoveIt planning scene and collision representation: https://moveit.picknik.ai/main/api/html/planning_scene_overview.html
- MuJoCo model format MJCF: https://mujoco.readthedocs.io/en/stable/modeling.html
- NVIDIA Isaac Sim (optional SIL/HIL, no hardware validation here): https://docs.nvidia.com/learning/physical-ai/getting-started-with-isaac-sim/latest/index.html

## Safety / design standards (conditional applicability)

- ISO 12100:2010 — safety of machinery, risk assessment and reduction: https://www.iso.org/standard/51528.html
- ISO 10218-1:2025 — industrial robots, design safety: https://www.iso.org/standard/73933.html
- ISO 10218-2:2025 — industrial robot applications/cells integration: https://www.iso.org/standard/73934.html
- ISO 13849-1:2023 — safety-related parts of control systems: https://www.iso.org/standard/73481.html
- ISO 13482:2014 — personal-care robots: https://www.iso.org/standard/53820.html
- ISO 13482 Edition 2 — *under publication as of November 11, 2026*; do not state as fully published without checking: https://committee.iso.org/standard/83498.html
- ISO 3691-4:2023 — driverless industrial trucks and systems, use only if hardware/use-case fits scope: https://www.iso.org/standard/83545.html

**Not guaranteed applicable to this device:** No robot use case, product classification or competent authority has reviewed the EHP design. ISO abstracts are not complete licensed standards. No certificate has been issued. Full text of standards and jurisdictional requirements must be used by a qualified integrator.

## EFMW research source and comparisons

- Canonical ME-001...102: https://github.com/enuminous/Monolithic_102_EFMW/blob/main/CANONICAL_102.md
- EFMW field meaning and distinction from physical field claim: https://github.com/enuminous/EFMW-Field
- TORTOISE, prospective frozen evidence cycle: https://github.com/enuminous/Tortoise
- RSI evidence-gated recursive strategy improvement (synthetic): https://github.com/enuminous/RSI
- Monolithic Coherence Observatory preliminary baseline results: https://github.com/enuminous/Coherence-Lab
- IST-FAM-001 negative audit: https://github.com/enuminous/papers/blob/main/research/ist-fam-001/AUDIT_REPORT.md

## Interpretation rules

- Conventional multibody equations, control barrier functions, QP/MPC, EKF, camera calibration and motion planning are established engineering methods. This document does not assign their origin to EFMW.
- EFMW's present-state/history/coherence interpretation motivates **an optional engineered monitoring proposal**. No physical novelty is claimed.
- Need to verify actual ROS package version matrix, robot vendor interfaces, safety controllers, all component specifications and calibration procedures before any motion command.
