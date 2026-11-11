# EFMW Humanoid Platform v0.1 — Publication Notice

**Publication date:** 2026-11-11  
**Research owner:** Matthew Chenoweth Wright / Monolithic LLC  
**Document identifier:** EHP-SYS-001  
**Status:** PUBLIC RESEARCH PROPOSAL · OFFLINE-ONLY REFERENCE IMPLEMENTATION · NO ROBOT CONSTRUCTED OR CERTIFIED

This is a public, source-preserving upload of the previously prepared 18-file EFMW Humanoid Platform engineering package. The original `README.md` says the package was a *private review bundle*; that line records the package's preparation status before its authorized publication here, rather than its current availability. **No file in the original 18-file package has been silently altered in this publication.** The original `MANIFEST.sha256` remains alongside the files so readers can check their integrity.

The full specification is available in two places:
- [Standalone specification at the root of papers](../../EFMW-Humanoid-Platform-System-Engineering-Specification-v0.1-2026-11-11.md)
- [Package-local SPEC.md](SPEC.md)

**The proposed 32-DoF robot has not been fabricated.** The examples implement a read-only EFMW-style monitor and conventional two-link dynamics in an offline demonstration; no ROS stack, robot actuators, real-world safety system or human-protection controls are implemented or evaluated. The observed local `35/35` software tests attest to narrowly specified source invariants, not real-world safety, a viable humanoid, or EFMW-specific control improvement.

## Local replay

From `research/efmw-humanoid-platform-v0.1`:

```sh
sha256sum -c MANIFEST.sha256
python -m unittest discover -s tests -v
python examples/simulate_offline.py
python examples/two_link_offline.py
```

The frozen package contains a preliminary requirements register, hazards register, recursive assembly graph, two-joint toy dynamics, bounded supervisor, tests, source list, Mermaid diagram and dated execution record.

**Safety boundary:** EFMW may be used to recommend experiments, monitor discrepancies and queue decisions for human review. It is **not** a safety-rated control layer and must not drive motor torques, authorize hazardous assembly steps, override E-stops, change protective limits or self-certify a robot.

**Open obligations:** independent source review, hardware bills of materials and force limits, full-body URDF/MJCF model, collision tests, formal review, qualified risk assessment, sensor integration, deterministic hardware control, independent real-world benchmarking, external replication.

This notice is a publication-layer addition, **outside the preserved original manifest**.
