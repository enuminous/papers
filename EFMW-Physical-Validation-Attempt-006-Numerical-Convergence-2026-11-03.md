# EFMW Physical Validation — Attempt 006: Convergence Study

**Date:** 2026-11-03
**Status:** numerical verification of a phenomenological model; no EFMW-specific physical validation.

## Model
For q=1 and s=r/xi, solve
(1+beta f²)(f''+f'/s)+beta f(f')²-f/s²+f(1-f²)=0.
This model was introduced in Attempt 004 as a proposed density-gradient effective energy, **not** derived from canonical EFMW. beta is not independently predicted.

## Computation
Using scipy.integrate.solve_bvp and scipy.optimize.brentq, reran beta=0, 0.1, 0.25, 0.5, 1.0 with outer radii 15, 25, 40, 60, initial nodes 400, 900, 1400, 1800, and solver tolerances 1e-5, 1e-7, 1e-8, 1e-8. Inner radius 0.01, approximate regularity f(smin)=smin f'(smin), outer condition f(S)=1-1/(2 S²). This GP-leading far-field boundary condition is asymptotically valid at leading order for fixed finite beta, but subleading beta dependence remains to be checked.

## Verified results at outer radius 60
| beta | half-density radius / xi | n(xi)/n0 |
|---:|---:|---:|
| 0 | 1.554891505453 | 0.270453812985 |
| 0.1 | 1.550732316179 | 0.273578412081 |
| 0.25 | 1.544707024544 | 0.278103512275 |
| 0.5 | 1.535140901983 | 0.285248343734 |
| 1 | 1.517362050625 | 0.298243997882 |

The beta=1 half-density radius is approximately 2.41% smaller than beta=0. The beta=1 normalized density at s=1 is approximately 10.28% greater in relative terms. These are model-to-model numerical differences, not measured effects. Maximum reported solve_bvp RMS residual at S=60 was below 1e-8 for each run. Variation across S=15 to 60 is substantially smaller than 1e-6 in half-density radius. This is a solver convergence check, not a mathematically certified error bound.

## Interpretation
The numerical result is robust to the tested domain and solver settings. It does not establish beta's origin, physical realizability, uniqueness relative to other GP extensions, or external evidence. In particular, a density-gradient correction is not unique to EFMW and can mimic changes in effective quantum-pressure terms.

## Next gates
1. Obtain a source-derived independent beta or report phenomenological status permanently.
2. Compare with finite-temperature, trap, beyond-mean-field, and imaging point-spread alternatives.
3. Compute independent numerical residual checks, inner-boundary and far-field asymptotic sensitivity.
4. Freeze an observational prediction with a real measurement protocol, then seek held-out external data.
5. Independent replication required for any physics validation claim.

## Source
- https://github.com/enuminous/papers/blob/main/EFMW-Physical-Validation-Attempt-004-Density-Gradient-Coupling-2026-11-03.md
