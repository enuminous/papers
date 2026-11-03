# EFMW Physical Validation — Attempt 007: Comparator and Identifiability Audit

Date: 2026-11-03
Status: ANALYTICAL COMPARATOR AUDIT; external evidence NOT TESTED.

## Source basis
- https://github.com/enuminous/papers/blob/main/EFMW-Physical-Validation-Attempt-004-Density-Gradient-Coupling-2026-11-03.md
- https://github.com/enuminous/EFMW-Lagrangian/blob/main/candidate/CANDIDATE.md
- https://github.com/enuminous/EFMW-Lagrangian/blob/main/docs/PHYSICAL_OBLIGATIONS.md

## Hypothesis and comparator
The phenomenological beta correction is an added density-gradient energy, not a term derived from frozen EFMW-Lagrangian-C1. The latter explicitly omits specified matter sources and has unresolved physical coupling identification. Do not conflate these actions.

Write Psi=sqrt(n) exp(i theta). The conventional GP gradient energy splits exactly into
(hbar²/2m)|grad Psi|² = (hbar²/8mn)|grad n|² + (hbar² n/2m)|grad theta|².
The proposed correction adds beta hbar²/(8m n0)|grad n|². Thus the total density-gradient coefficient is
(hbar²/8m)[1/n + beta/n0],
while the phase stiffness stays hbar² n/(2m). This is an effective quantum-pressure modification, not a unique EFMW signature.

At bulk density n=n0, the density-gradient stiffness is multiplied by (1+beta). The local quadratic density-fluctuation dispersion about a homogeneous stationary background (ignoring external trapping) follows
omega² = (g n0/m) k² + [hbar²/(4m²)](1+beta) k^4.
Derivation: the quadratic hydrodynamic energy has (g/2)(delta n)² + [hbar²(1+beta)/(8m n0)]|grad delta n|² + [hbar² n0/(2m)]|grad delta theta|²; continuity and phase equations eliminate delta theta. This is a conditional prediction of the phenomenological model, not canonical EFMW.

## Identifiability insight
The beta-dependent k^4 coefficient is degenerate with uncertainty in effective gradient stiffness and can be confounded by finite-range interactions, beyond-mean-field corrections, calibration of m and n0, finite temperature, trap inhomogeneity and imaging transfer functions. A vortex-profile improvement alone cannot identify beta as a new force or EFMW effect. The dispersion relation provides a **second observable** that could constrain the same beta independently. It must be compared against a microscopic Bogoliubov/GP baseline with realistic corrections and independently calibrated parameters.

## Conditional cross-observable consistency test
1. Calibrate m, g, n0, geometry, temperature and instrument response independently.
2. Fit beta on a training subset of vortex profiles, with a declared uncertainty interval.
3. Freeze beta and predict the k^4 coefficient in independent excitation-spectrum data. Compare to the GP beta=0 prediction and to plausible finite-range or beyond-mean-field models.
4. Reverse the split: fit the spectrum and predict held-out vortex profiles. A shared beta across observables is necessary but not sufficient for physical novelty.
5. Use model complexity penalties and preregistered uncertainty/systematics thresholds. Preserve all null and contradictory outcomes.

## Asymptotic consistency
For a q-vortex, the radial equation
(1+beta f²)(f''+f'/s)+beta f(f')²-q² f/s²+f(1-f²)=0
has large-s leading form f(s)=1-q²/(2s²)+O(s^-4), for fixed finite beta. Therefore the previously used outer boundary f(S)=1-1/(2S²) is leading-order consistent for q=1 even when beta is nonzero. This does not eliminate finite-boundary and inner-core numerical errors.

## Gates
- Explicit strong comparator (GP/Bogoliubov): PASS as a defined analytical baseline, not a data comparison.
- Dimensional consistency of dispersion: PASS; [omega²]=s^-2.
- Second independently measurable observable: PASS as conditional model consequence.
- EFMW-derived beta: UNRESOLVED.
- Uniqueness versus established corrections: UNRESOLVED.
- External data analysis: NOT RUN.
- Independent physical replication: NOT RUN.

## Publication boundary
No new physical effect, independent measurement, or external confirmation is claimed. This document defines a discriminating multi-observable protocol and its confounding alternatives.
