# UNITY-001 — Phase 2 mathematical type compilation

**Date:** 2026-11-09 · **Result:** 9/9 source-linked declared-AST type checks PASS; **708/717 records remain uncompiled**, 8 scientific conflicts unresolved, 0 physical PASS.

[Full executed Phase 2 report](PHASE2_REPORT.md) · [Typed registry](typed-registry.json) · [Conflict register](conflicts.json) · [Source-preserving compiler](compile.py) · [20 adversarial tests](test_compiler.py) · [Verified CI receipt](EXECUTION.json) · [CI-generated manifest](https://github.com/enuminous/papers/actions/runs/42619525163/artifacts/13673897149)

Run from the repository root:

~~~bash
python3 -m unittest discover -s research/unity-001/phase-2 -p 'test_*.py' -v
python3 research/unity-001/phase-2/compile.py compile --out research/unity-001/phase-2/build/manifest.json
~~~

Source of truth remains the immutable [Phase 1 lock](../phase-1/sources.lock.json) and [717-record ledger](../phase-1/source-equations.csv). This project does not automatically parse arbitrary physics notation, verify equations in Lean, prove candidate equivalences, or produce physical measurements. The published nine are manually proposed typed interpretations, never a claim of nine new physical laws.

**Older MOC-001 snapshot:** 5/40 structural PASS and 4/22 dimensional equation examples; unchanged. **Phase 2 subset:** nine newly source-linked typed checks (9/717 coverage), tracked independently.
