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
