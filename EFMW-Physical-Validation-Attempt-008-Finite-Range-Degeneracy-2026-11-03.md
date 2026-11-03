# EFMW Physical Validation — Attempt 008: Finite-Range Degeneracy Audit

**Date:** 2026-11-03  
**Status:** analytic comparator result; no empirical confirmation.

## Question
Does the k^4 dispersion correction in the phenomenological density-gradient model uniquely identify EFMW physics?

## Candidate model
Attempt 004 introduced a phenomenological energy density beta*hbar²/(8*m*n0)*|grad n|². It is **not derived from canonical EFMW**. Attempt 007 obtained for homogeneous fluctuations:
omega² = (g*n0/m)*k² + [hbar²/(4*m²)]*(1+beta)*k^4.

## Established comparator
For a weakly interacting homogeneous Bose condensate with a translationally invariant, isotropic finite-range two-body potential whose Fourier transform has the low-momentum expansion Vtilde(k)=g+g2*k²+O(k^4), the standard Bogoliubov formula is
(hbar*omega)² = epsilon_k*(epsilon_k + 2*n0*Vtilde(k)),
epsilon_k=hbar²*k²/(2*m).

Dividing by hbar² and expanding:
omega² = (g*n0/m)*k² + [hbar²/(4*m²) + n0*g2/m]*k^4 + O(k^6).

Thus the two low-k dispersion coefficients agree exactly through k^4 if
g2 = beta*hbar²/(4*m*n0).

Dimensional audit: [g]=J*m³, [g2]=J*m^5, [hbar²/(m*n0)]=J*m^5. PASS.

The equivalence is at the level of the homogeneous linear-response k^4 coefficient. It does NOT establish equality of the full nonlinear vortex profiles, full nonlocal interactions, higher-order k behavior, or thermodynamic stability. Not every beta/g2 combination necessarily comes from a physically admissible microscopic potential; positivity, scattering data, and effective-theory domain must be checked.

## Stronger cross-observable test
1. Independently measure or constrain the two-body interaction and its finite-range expansion g2 using scattering or a distinct calibration channel.
2. Freeze g, g2, m, n0, temperature, geometry and response functions before evaluating held-out excitation spectra.
3. Predict vortex-density profiles using a consistent nonlocal GP functional with the *same* interaction kernel; do not compare against a simplistic contact-only GP baseline.
4. Compare the full dispersion beyond the k^4 coefficient, vortex profiles, and independent interaction measurements jointly. Model selection must account for nuisance parameters and complexity.
5. Derive beta from a pinned EFMW physical equation independently of the same observations; otherwise beta remains a generic effective coefficient.

## Gate verdict
- Correct dimensioned analytic comparator: PASS.
- Non-uniqueness of leading k^4 signal: PASS (degeneracy demonstrated).
- Distinct EFMW-specific prediction: UNRESOLVED.
- Joint nonlinear comparator calculation: NOT RUN.
- External measurements: NOT RUN.
- Independent replication: NOT RUN.

## Sources
- https://github.com/enuminous/papers/blob/main/EFMW-Physical-Validation-Attempt-007-Comparator-Identifiability-2026-11-03.md
- https://github.com/enuminous/EFMW-Lagrangian/blob/main/docs/PHYSICAL_OBLIGATIONS.md

**Conclusion:** A positive k^4 dispersion signal alone cannot establish EFMW-specific physics. The immediate priority is independently constrained microscopic interactions and a source-derived EFMW parameter, not another unconstrained fit.
