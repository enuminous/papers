# MOC-001 — research companion and Unity path

**Paper:** [MOC-001 — Compiling Ontologies Toward a Testable Unity of Physics](../../MOC-001-Compiling-Ontologies-Toward-Testable-Unity-of-Physics-2026-11-08.md)  
**Unity appendix:** [`research/moc-001/UNITY_APPENDIX.md`](UNITY_APPENDIX.md)  
**Date:** 8 November 2026

This folder publishes the research-methods paper's formal unity criteria and provenance notes. **It does not contain the executable compiler ZIP**, and this publication does not imply that the compiler source, upstream source corpora, Lean kernel certificates, or any physical measurements are hosted in `enuminous/papers`.

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
