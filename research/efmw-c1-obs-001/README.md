# EFMW-C1-OBS-001 — action to observable

**Completed:** a conditional source-to-observable derivation from the pinned EFMW C1 action, symbolic and numerical verification, and a translation of an existing experimental limit.

**Finding:** one C1 branch predicts scalar–photon conversion and optical regeneration. It is identical to an established scalar–photon model. It does not provide a uniquely EFMW prediction or establish a physical detection.

The original coherence-memory force law did not acquire a source derivation: the supplied action lacks its operational variables, relaxation closure and force-detector coupling.

## Read

- **DERIVATION.md** — full action, variations, approximation, measurement formula, example and evidence status.
- **EXPERIMENT_CONTRACT.md** — a concrete conditional measurement and analysis contract.
- **AUDIT.md** — fixed scope, operations, assumptions, negative results and checks.
- **predictions.png** — calculated trends, clearly separated from measurements.
- **results/example.json** — numerical illustration and units.
- **results/existing_bound_translation.json** — published-limit mapping, with assumptions.
- **results/mass_scan.csv** — 401 theoretical predictions, not empirical data.

## Reproduce

The calculation uses Python 3.12, NumPy 2.3.5, SciPy 1.17.0 and SymPy 1.14.0. The plot uses Matplotlib 3.10.8.

~~~sh
python -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python calculate.py --out results_reproduction
python render_figure.py
python verify_package.py
~~~

Use a fresh output directory; calculate.py refuses to overwrite an existing result directory. It verifies the locked source and scope before and after calculation.

The scope was locally fixed after screening sources, before symbolic/numerical checks. It is not an independent preregistration. All code and final outputs have hashes in MANIFEST.sha256; source copies additionally match their Git blob hashes.

The included calculation performs 35 forward-model checks against matrix exponentiation and amplitude integration, verifies the Lagrangian reduction, Euler–Lagrange equations, wave determinant, units, polarization and scaling limits, and records every result. These are implementation and mathematical checks, not physical validation or independent replication.

## Scientific boundaries

- The coupling and mass in the numerical example are chosen inputs.
- C1 has no laboratory matter action; instrument identification and calibration are explicit added assumptions.
- Weak background, relativistic propagation, negligible depletion and scalar transmission through the barrier are required.
- The two-mode formula is exact only for its approximate forward equation.
- Global stability of the full C1 family is not established.
- The published-limit mapping concerns one scalar branch under matching assumptions.
- The full EFMW theory is neither proved nor globally excluded by this work.
- No upstream repository, original benchmark or existing evidence package was changed.

Prepared for Matthew Chenoweth Wright / Monolithic LLC with AI assistance, 14 November 2026.

