# UNITY-001 — Phase 3 correspondence and identifiability

**Date:** 2026-11-09 · **Status:** BOUNDED CLASSICAL CORRESPONDENCE PASS; EFMW physical bridge UNRESOLVED.

## Executed result

[Full technical report](PHASE3_REPORT.md) · [Executable bridge audit](bridge.py) · [27 adversarial tests](test_bridge.py) · [Interface contracts](interfaces.json) · [Counterexamples](counterexamples.json) · [CI evidence](EXECUTION.json) · [GitHub run](https://github.com/enuminous/papers/actions/runs/42622880582).

The eight Phase 3 claims had **3 bounded PASS, 2 explicit FAIL, 3 UNRESOLVED**, with **27/27 Python tests passing**. These denominators describe the eight scoped claims, not the existing 717 Phase 1 equations or the original MOC-001 snapshot.

**Positive reference projection:** C1 with eight scalar fields, B gauge field and all pair/triple interactions set zero reduces as a *classical bulk action density* to Einstein–Maxwell. This demonstrates only the presence of a conventional subfamily, not any EFMW-specific phenomenon.

**Negative/counterexample results:** nonzero C1 g_EM R X prevents the unconditional projection; the classical SM's hypercharge-only expression at H=0 retains the Higgs vacuum-energy constant. Geometry's 4×4 source-only model permits absorption of kappa I into unrestricted ordinary T; independently measured matter removes that purely algebraic ambiguity in constructed examples.

## Reproduce

Run from the repository root, with Python 3.12+; no third-party dependencies:

~~~bash
python3 -m unittest discover -s research/unity-001/phase-3 -p 'test_*.py' -v
python3 research/unity-001/phase-3/bridge.py --out research/unity-001/phase-3/build/phase3.json
~~~

Output manifest contains exact provenance checks, symbolic polynomial term lists, 24 seeded rational tensor trials, 24 source-split trials, counterexamples, eight claim statuses, and the statement **EFMW-specific physical PASS = 0**.

## Boundaries

The action projection is conditional and explicitly coupling-restricted. A Maxwell kinetic correspondence does not establish a complete curved SM, chiral physics, causal quantum theory, metric stress conventions or Einstein-Maxwell PDE solutions. Geometry's source-only identifiability theorem is conditional on unrestricted ordinary-source reallocation. There is no new Lean kernel replay, independent physical measurement, or validated kappa_I effect in this study.

**Immutable inputs:** [Phase 1 source lock](../phase-1/sources.lock.json) and [Phase 1 original source ledger](../phase-1/source-equations.csv). [Phase 2 conflicts](../phase-2/conflicts.json) all remain UNRESOLVED.
