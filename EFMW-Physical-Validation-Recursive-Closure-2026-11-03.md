# EFMW Physical Validation — Recursive Closure Review (Attempts 001–008)

**Date:** 2026-11-03  
**Author:** Matthew Chenoweth Wright / Monolithic LLC  
**Status:** CLOSED as an EFMW-specific novelty candidate at second-order density-gradient level; empirical validation remains UNRESOLVED.  
**Type:** mathematical equivalence and research decision, not an experimental paper.

## Abstract

Attempts 001–008 sought a dimensionally specified, noncircular EFMW-specific observable. A phenomenological density-gradient interaction was introduced and its vortex-density and excitation-dispersion consequences calculated. This closure review demonstrates that the proposed interaction is equivalent, at second order in the density-gradient expansion, to an established finite-range interaction term. The observed model-to-model differences against contact-only Gross–Pitaevskii theory therefore do not uniquely identify EFMW. The physical novelty branch is closed unless an independently derived EFMW interaction produces a nondegenerate prediction.

## Recursive audit of the research chain

1. **Phase/current identities (001):** standard polar/Madelung structure; vortex blob is stipulated rather than dynamically derived. PASS mathematical consistency, FAIL as an EFMW-specific derived law.
2. **Core-scale comparator (002):** GP dynamics predict a healing length; EFMW phase identities alone do not determine the core. UNRESOLVED EFMW source.
3. **Canonical action (003):** ME-009/011 do not provide a dimensioned operational map to condensate matter. The EFMW-Lagrangian-C1 audit itself leaves physical sources and currents unresolved.
4. **Candidate interaction (004):** add beta*hbar²/(8*m*n0)*|grad n|² to GP energy; beta dimensionless. This is an invented phenomenological hypothesis, **not a term derived from EFMW**.
5. **Numerical profiles (005–006):** conditional boundary-value solutions vary with beta and show convergence under tested settings. These are calculations, not measurements.
6. **Dispersion (007):** omega²=(g*n0/m)k²+[hbar²/(4*m²)](1+beta)k⁴ for homogeneous linearized dynamics. This is a conditional prediction.
7. **Finite-range comparator (008):** ordinary finite-range interactions produce the same k⁴ coefficient for g2=beta*hbar²/(4*m*n0).
8. **Closure (this document):** the equivalence holds at the level of the truncated effective *energy functional*, not just the linearized spectrum.

## Derivation of the effective-energy equivalence

Let n(x)=|Psi(x)|² be number density in 3D, and suppose an isotropic, translation-invariant two-body potential has a regular low-k Fourier expansion

Vtilde(k)=g+g2*k²+O(k⁴).

The nonlocal interaction energy is

E_int=(1/2) integral d³x d³y n(x) V(x-y) n(y).

Using the Fourier convention in which k is angular wave number and the convolution operator corresponding to k² is -nabla², the gradient expansion gives

E_int=(g/2) integral n² d³x -(g2/2) integral n nabla²n d³x + O(nabla⁴).

For sufficiently decaying fields, periodic boundaries, or boundary conditions eliminating surface terms, integration by parts yields

E_int=(g/2) integral n² d³x +(g2/2) integral |grad n|² d³x + O(nabla⁴).

The proposed Attempt-004 correction is

Delta E_beta= [beta*hbar²/(8*m*n0)] integral |grad n|² d³x.

The coefficients coincide for

**g2=beta*hbar²/(4*m*n0)**.

Dimensions: [g2]=J*m⁵; [hbar²/(m*n0)]=J*m⁵. Thus the two models have the same truncated energy functional and, when subjected to the same variation, the same Euler–Lagrange contributions, including the density-gradient correction to the vortex equation. Matching the two truncated models' vortex profiles and k⁴ dispersion cannot distinguish their interpretation.

**Scope limits:** this is not equality of the complete microscopic nonlocal potential with the truncated local theory; O(k⁴) in Vtilde contributes higher spatial derivatives. Boundary terms, stability, microscopic admissibility, density-dependent effective coefficients, temperature and trapping require separate treatment. The mapping at a fixed reference n0 need not hold unchanged across densities if g2 is a fixed microscopic interaction coefficient and beta is held constant.

## Consequences for the proposed research

- **PASS:** dimensional consistency, analytic effective-energy equivalence at retained gradient order.
- **PASS:** explicit conventional alternative that reproduces both the leading spectrum correction and the local gradient-energy contribution.
- **FAIL:** the density-gradient term is a unique EFMW-specific signature.
- **UNRESOLVED:** whether canonical EFMW predicts an independent, dimensioned physical coupling or a higher-order effect.
- **NOT TESTED:** external data and independent experimental replication.

The phenomenological beta model remains a legitimate generic effective-field-theory parameterization; it must not be presented as a confirmed EFMW physical discovery. Numerical solver convergence is not physical validation.

## Closure decision and reopening criteria

**Close the beta-gradient novelty claim at second-order gradient truncation.** Do not continue iterative parameter sweeps or GP-only fit comparisons as evidence of EFMW novelty. Preserve the calculations as negative/comparator results.

Reopen only upon all of the following:
1. A pinned, independently specified EFMW action or evolution law with units, symmetries, operational variable definitions and a source-derived coupling.
2. A derivation of an observable not degenerate with plausible conventional models under the same information budget and order of approximation.
3. A preregistered quantitative prediction with parameter-identifiability and uncertainty analysis.
4. External held-out measurement and independent replication before any established-physics claim.

If no such source law is available, the scientifically valid final status is **UNRESOLVED physical theory**, with the specific phenomenological novelty branch **CLOSED/NOT UNIQUE**.

## Sources

- https://github.com/enuminous/Monolithic_102_EFMW/blob/main/CANONICAL_102.md
- https://github.com/enuminous/EFMW-Lagrangian/blob/main/candidate/CANDIDATE.md
- https://github.com/enuminous/EFMW-Lagrangian/blob/main/docs/PHYSICAL_OBLIGATIONS.md
- https://github.com/enuminous/Phase-Vorticity-Lab/blob/main/docs/MODEL.md
- https://github.com/enuminous/papers/blob/main/EFMW-Physical-Validation-Attempt-008-Finite-Range-Degeneracy-2026-11-03.md

## Research integrity note

This review is a mathematical and provenance-based audit. No new numerical run or physical experiment was performed for this closure. The conclusion is limited to the defined effective interaction and its retained derivative order; it neither proves nor disproves EFMW as a broader research program.
