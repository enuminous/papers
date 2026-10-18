# Universe 003 — Reproducible statistical audit

October 18, 2026. Exploratory simulation, **not** a validation of EFMW or cosmic rotation.

## Methods

`recursion_run3.py` retains Universe 002's random hierarchical pairing, assigned mass-energy loss of 0.5–2.5% per merger, and assigned angular-momentum loss of 3–15% per merge. It repeats the population using 128 distinct deterministic seeds, each containing 100,000 starting objects with lognormal toy masses and randomized spin orientations. It separately runs 32 positive controls in which a direction is inserted explicitly into the initial spin distribution; those controls must not be interpreted as a physical prediction. The final rebound is excluded from the statistical test because no physical transition equation is available.

The preregistered diagnostic within this code is the cosine of the final remnant angular-momentum direction to a fixed z axis. Under isotropy its distribution is uniform over [-1, 1], and the one-sided exceedance for the absolute alignment statistic is p = 1 - |cos(theta)|. A rank-based comparison against the other null simulations is also computed. There is no observed CMB axis in this simulation and therefore no model-versus-CMB match test.

## Results

- Original seeded Universe 002 results reproduced: 15 pairing rounds, four remnants, retained mass fraction 0.8016231, final net J magnitude 70.34008.
- Mean absolute reference-axis cosine across 128 null realizations: 0.45708 (isotropic expectation: 0.5).
- Null signed cosine mean: -0.02895; standard deviation: 0.53786 (isotropic expectations: 0 and ~0.57735).
- First-run absolute alignment: 0.46568; exact fixed-axis null p = 0.53432; empirical rank p = 0.453125.
- 32 injected-axis positive controls: mean cosine 0.999385 and all 32 positive, showing sensitivity to a large deliberately introduced anisotropy.
- Maximum observed relative mass-energy ledger error: 2.75e-16; maximum relative angular-momentum ledger error: 5.38e-14. These are constructed bookkeeping equalities.

## Limits and next iterations

1. The **four-remnant stopping condition is imposed**, not an emergent gravitational outcome.
2. There are no positions, velocities, merger cross sections, gravitational torques, ejections, or dynamical spacetime evolution.
3. Conservation is imposed by allocation to bookkeeping ledgers; full GR stress-energy conservation is not tested.
4. The rebound has no action-derived mechanism, metric solution, or valid physical conservation map.
5. A claimed match “within 6 sigma” is undefined without a specified target observable, measured uncertainty, null hypothesis, and comparison protocol. A small discrepancy measured in sigma units does not prove a discovery; conversely a >6σ rejection of isotropy would be a different claim and would require control of systematics and model selection.
6. To compare with the CMB Axis of Evil, freeze the cosmological physical mechanism, derive the predicted *sky* multipoles and orientation, and use independent observation data with a prespecified statistic and systematic-error model. Do not adjust parameters against the same data used to claim significance.

## Reproduction

Run `python recursion_run3.py` (NumPy required). The script writes `recursion_run3_results.json` in `/mnt/data` under this environment. Results are seeded but floating-point rounding can vary slightly by platform/NumPy version.
