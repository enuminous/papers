# MOC-001 — research companion and Unity path

**Paper:** [MOC-001 — Compiling Ontologies Toward a Testable Unity of Physics](../../MOC-001-Compiling-Ontologies-Toward-Testable-Unity-of-Physics-2026-11-08.md)  
**Unity appendix:** [`research/moc-001/UNITY_APPENDIX.md`](UNITY_APPENDIX.md)  
**UNITY-001 action plan:** [Pathway to Physical Unification](../../UNITY-001-Pathway-to-Physical-Unification-Action-Plan-2026-11-08.md)  
**Date:** 8 November 2026

This folder publishes the research-methods paper's formal unity criteria and provenance notes. **It does not contain the executable compiler ZIP**, and this publication does not imply that the compiler source, upstream source corpora, Lean kernel certificates, or any physical measurements are hosted in `enuminous/papers`.


**Phase 1 executed source-freeze audit (2026-11-09):** [UNITY-001 Phase 1 report](../unity-001/phase-1/PHASE1_REPORT.md) and [lockfile](../unity-001/phase-1/sources.lock.json). Bounded pinned-Git provenance; not a new physical proof.  

**Phase 2 typed compilation (2026-11-09):** [Executed Phase 2 report](../unity-001/phase-2/PHASE2_REPORT.md), [typed AST registry](../unity-001/phase-2/typed-registry.json), [verified GitHub CI](https://github.com/enuminous/papers/actions/runs/42619525163). Nine bounded manual type checks out of 717 source records; 708 unresolved, with no physical equivalence asserted.

**Phase 3 reference correspondence (2026-11-09):** [Executed Phase 3 report](../unity-001/phase-3/PHASE3_REPORT.md), [interface contracts](../unity-001/phase-3/interfaces.json), and [verified CI](https://github.com/enuminous/papers/actions/runs/42622880582). Three bounded PASS, two deliberately tested stronger claims FAIL, three UNRESOLVED; no EFMW-specific physical observation established.

**Phase 5 conditional-prediction screen (2026-11-09):** [Executed Phase 5 report](../unity-001/phase-5/PHASE5_REPORT.md), [candidate PREDICTION-001](../unity-001/phase-5/PREDICTION_001.md), and [reproducible CI](https://github.com/enuminous/papers/actions/runs/42633977283). Purely synthetic identifiability test: 4 PASS/1 FAIL/6 UNRESOLVED. No confirmatory-ready EFMW-specific physical prediction.

## Prototype execution, separately performed

- Input: local `Master-Ontology-Compiler-MOC-001-2026-11-08.zip`, SHA-256 `77509faffce09dcbe23d31c4cb956d5e335fbd6c113edfed9cae7e22cbadeb7e`.
- Commands: `PYTHONPATH=src python -m unittest discover -s tests -v` and `PYTHONPATH=src python -m moc compile --out build`.
- Observed result: 16 tests pass; 5 static PASS, 0 FAIL, 35 UNRESOLVED findings.
- Scope: registry syntax/reference and limited SI dimension checks. Not a physical proof.
- Lean 4 replay: not performed. Independent code/experiment replication: not performed.

## Sources inspected at README level only

- [Geometry](https://github.com/enuminous/Geometry)
- [Information-Tensor](https://github.com/enuminous/Information-Tensor)
- [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian)
- [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction)

Next milestone: freeze exact upstream commit SHAs and source file hashes, then import original equations without suppressing contradictions. See [Unity Appendix](UNITY_APPENDIX.md) for acceptance criteria and current UNRESOLVED interfaces.
