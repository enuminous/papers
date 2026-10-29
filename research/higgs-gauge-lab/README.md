# Higgs–Gauge Lab numerical verification

Companion to [Higgs–Gauge Lab and the numerical simulation of a classical Abelian–Higgs field](../../Higgs-Gauge-Lab-Classical-Abelian-Higgs-Simulation.md), Matthew Chenoweth Wright, Monolithic LLC, 29 October 2026.

## Files

- `validate.mjs`: dependency-free Node.js verification harness.
- `results.json`: complete output from Node.js v24.22.1 on Linux x64.

## Reproduce

From the root of an `enuminous/papers` checkout:

```bash
curl --fail --location \
  https://raw.githubusercontent.com/enuminous/Higgs-Gauge-Lab/06056de25e0ad0f5306e6a5d272f983436e54126/index.html \
  --output /tmp/higgs-gauge-pinned.html
node research/higgs-gauge-lab/validate.mjs /tmp/higgs-gauge-pinned.html > /tmp/higgs-gauge-results.json
```

The script rejects any source file that does not match Git blob `cf4482f77fe02086e884e6da905e472b77f3769c`. Exact expected file length: 25,948 bytes. SHA-256: `007d024176506541e62b9d3652014dc0c9512add78eb1664216f2b14b9b4a539`. It exits nonzero if a sanity criterion fails. The supplied JSON records the actual outputs; small floating-point differences across environments are possible.

The application script runs in a Node VM with no-op DOM/canvas functions and disabled animation scheduling. Inspection exports are inserted into its existing closure. The force, step, sample, and initialization functions run verbatim. A seeded Mulberry32 `Math.random` replaces the browser's unseeded generator; only the refinement runs replace `DT=0.045`. No source file is modified on disk. This procedure verifies the numerical core, not browser layout or UI event handling.

## Protocol

Use N=64, spacing 1, lambda=0.5, v=1.25, g=0.75, y=0.65. Set damping to zero except for the explicitly damped run. Set parameters before resetting. Each fresh VM starts its random generator with seed 20261029 and executes the application's normal startup quench. A subsequent preset reset continues that stream; it does not reseed. This startup consumption is part of the exact reproducible sequence.

1. Hold the uniform vacuum for 1,000 steps.
2. Run the deterministic pulse to T=45 at DT=0.045, 0.0225, and 0.01125.
3. Run the vortex and seeded quench presets to T=45 at DT=0.045.
4. Repeat the quench with damping 0.028.
5. At a seeded quench state after 100 steps, apply periodic site phases drawn from [-1,1) using seed 20261030. Check transformed forces, flux, charge, and energy.
6. At a quench state after 50 steps, perturb all coordinate arrays in one direction generated with seed 20261031. Compare central energy derivatives with force contractions for epsilon=1e-4, 1e-5, 1e-6.
7. Evolve a uniform radial perturbation of relative amplitude 1e-4 to T=90. Estimate frequency using interpolated upward vacuum crossings and compare with the continuum and linear Verlet values.

Energy maxima and Gauss maxima are sampled every ten steps, including the final step. State refinement compares all eight arrays at the common final time, with the square root of the mean squared component difference. The scalar pulse has identically zero gauge dynamics; nontrivial gauge checks come from the vortex and quench runs.

## Sanity tolerances

These are implementation-review criteria, not independently preregistered hypotheses or empirical validity thresholds.

| Criterion | Threshold |
|---|---|
| Vacuum state RMS change | <1e-12 |
| Default-step undamped pulse energy deviation | <0.005 relative |
| Undamped vortex energy deviation | <0.005 relative |
| Undamped quench energy deviation | <0.005 relative |
| Sampled Gauss RMS for vortex, quench, and damped quench | <1e-10 |
| Gauge-covariance absolute force/flux/charge errors and relative energy error | <1e-10 |
| Hamiltonian directional derivative | At least one epsilon gives relative error <1e-5 |
| Pulse observed temporal order | Between 1.8 and 2.2 |
| Radial frequency compared with continuum mass | Relative error <0.001 |
| Damped quench endpoint energy | Below its initial energy |

All ten pass in the recorded run. The paper gives the measured errors instead of interpreting a pass as complete validation. There is no spatial-convergence study, quantum dynamics, experimental data, or independent replication in this package.
