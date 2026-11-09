# IST-001 — Reproducible Informational Stress / Reservoir Controls

**9 November 2026.** [Foundational theory memorandum](../../IST-001-Deriving-Informational-Stress-from-Covariant-Memory-and-Reservoir-Models-2026-11-09.md) · [Executed technical report](IST001_REPORT.md) · [Frozen protocol](PROTOCOL.json) · [Source code](ist.py) · [Adversarial tests](test_ist.py) · [GitHub CI](https://github.com/enuminous/papers/actions/runs/42669567461) · [Machine-generated artifact](https://github.com/enuminous/papers/actions/runs/42669567461/artifacts/13697398989).

This project verifies bounded control identities for a proposed scalar-memory Hilbert stress and a conservative oscillator reservoir. **24/24 tests PASS. Six of eight prospective gates PASS within their scopes, two remain UNRESOLVED. Zero EFMW-specific physical PASS.**

Reproduce with Python 3.12+ from the repository root:

~~~bash
python3 -m unittest discover -s research/ist-001 -p 'test_*.py' -v
python3 research/ist-001/ist.py --out research/ist-001/build/results.json
~~~

The finite oscillator bath is reversible. The first-order relaxation equation was checked only after independently *assuming* a Markov/overdamped reduction; the run has not derived that limit from a continuum spectral density. The partial memory stress depends on the assignment of interaction energy. The frozen EFMW equations and Phase 5 physical-identifiability obstruction remain open.

**Physical decision:** the illustrative stress and reservoir model are not evidence of a novel gravitational effect or a complete EFMW informational stress tensor.

## Post-publication adversarial review (separate, unexecuted audit)

The [IST-FAM-001 referee synthesis](../../IST-FAM-001-Referee-Review-and-Spectral-Novelty-Audit-2026-11-09.md), [frozen two-hypothesis contract](../ist-fam-001/PROTOCOL.json), and [review ledger](../ist-fam-001/REVIEW_LEDGER.json) record corrections about prescribed external work, the finite-bath counterterm, missing memory mass, anisotropic stress, model-family equivalence, and calibration versus discrimination.

**H1 and H2 are NOT EXECUTED.** This review is separate from the original 24-test CI result; it does not modify the earlier source equations, numerical records, or any EFMW physical status.

## Subsequent complete 717-record source audit — 9 November 2026

The prior section accurately describes the *pre-execution review stage*. The [subsequently executed IST-FAM-001 audit](../ist-fam-001/AUDIT_REPORT.md) has now checked all **717** frozen source records against **seven** original source files, with **19/19 audit software tests passing** in [GitHub CI](https://github.com/enuminous/papers/actions/runs/42676059594). **H1 and H2 both returned NO SOURCE SUPPORT**, because no independently source-defined ordered oscillator-bath frequency/weight map was established. The previously committed bounded stop rule is **invoked for this spectral-novelty route**; the existing IST-001 physical conclusions and its original 24-test execution are unchanged. This is not a new gravitational physical FAIL or an impossibility theorem for all EFMW models.
