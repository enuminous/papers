# EFMW Physical Validation — Attempt 004: Phenomenological Density-Gradient Coupling

**Date:** 2026-11-03  
**Status:** CONDITIONAL MATHEMATICAL DERIVATION; EFMW-SPECIFIC ORIGIN UNRESOLVED; NO EMPIRICAL VALIDATION

## Scientific boundary

This is a newly proposed phenomenological extension motivated by the EFMW research program, **not** an interaction derived from canonical EFMW equations ME-009 or ME-011. Its dimensionless coefficient beta is not currently predicted by EFMW. A fit to vortex data cannot by itself establish EFMW-specific physics.

## Proposed functional

For a nonrelativistic three-dimensional dilute condensate with particle mass m, repulsive interaction g>0, bulk number density n0>0, wavefunction Psi with |Psi|²=n, define

E_beta[Psi] = integral d³x { (hbar²/2m)|grad Psi|² + (g/2)(|Psi|²-n0)² + V_ext |Psi|² + [beta hbar²/(8m n0)]|grad(|Psi|²)|² }.

This is a candidate effective energy, not the original EFMW action. The final term has units J/m³ because [hbar²/m]=J m², [n0]=m^-3 and [grad n]²=m^-8. beta is dimensionless. The density-gradient term is gauge invariant; the ordinary gradient of Psi requires replacement by a gauge-covariant derivative if electromagnetic gauge coupling is included. The energy is bounded against arbitrarily large density gradients only under additional restrictions; for the simplest nonnegative-gradient-penalty case take beta>=0. Even beta>=0 does not establish a valid microscopic effective theory.

## Variation

Write n=Psi*Psi. Functional differentiation with respect to Psi* (assuming appropriate vanishing boundary terms) yields

i hbar partial_t Psi = -(hbar²/2m) nabla² Psi + g(n-n0)Psi + V_ext Psi - [beta hbar²/(4m n0)](nabla² n) Psi.

This uses a background-chemical-potential-subtracted GP convention. The beta term is obtained from delta E_grad / delta n = -beta hbar²/(4m n0) nabla²n. It is not a free coefficient chosen after seeing data.

For a stationary isolated winding-q vortex, Psi=sqrt(n0) f(r) exp(i q phi), set xi=hbar/sqrt(2m g n0), s=r/xi. The radial Euler–Lagrange equation is

(1+beta f²)(f''+f'/s) + beta f(f')² - q² f/s² + f(1-f²)=0,

where primes mean s derivatives. Boundary conditions: f(0)=0 for q !=0, f(infinity)=1; regularity and finite excess energy per unit length require suitable large-radius behavior. A straight vortex in an infinite uniform condensate has logarithmically divergent total kinetic energy per unit length, so any total-energy comparison needs a finite outer radius or a common subtraction convention.

Equivalent reduced radial energy density (up to overall factor) is
(1+beta f²)(f')² + q² f²/s² + (1/2)(1-f²)².

**Check:** beta=0 exactly recovers the standard dimensionless GP vortex ODE.

## Candidate measurable predictions

Primary observable: normalized vortex density n(r)/n0=f(r/xi)². Secondary: imaging-convolved radial contrast and profile residuals. The phase-derived superfluid velocity remains v_phi=hbar q/(mr) outside the core, so this model does **not** predict a changed quantized circulation. Its number current remains j=n v in the absence of a gauge field because the added density-gradient term contains no phase gradient. Do not claim altered circulation from this coupling.

The parameter beta is not identifiable without sufficiently precise, independently calibrated m,g,n0, trap potential, imaging point-spread function, temperature and systematic errors. Fit beta only on calibration data and freeze its value before an independent holdout. Compare beta=0, beta nonzero, and credible alternative GP corrections such as beyond-mean-field, finite-temperature and trap effects. A more flexible model fitting better is not by itself novel physics.

## Falsification protocol

1. Independently specify beta from a separate EFMW equation or calibration experiment not involving the holdout vortex profile; if impossible, label beta as phenomenological.
2. Solve the radial boundary-value problem for q=1 and at least one further winding, with numerical convergence checks and a finite-radius sensitivity study.
3. Freeze curves and uncertainty bands for normalized density versus s, including instrument convolution.
4. Predefine primary likelihood or error metric, model-complexity penalty, minimum detectable deviation, null controls and exclusion rules.
5. Test against externally acquired held-out profiles, with identical nuisance budgets for GP and the proposed model.
6. Obtain independent replication before asserting physical evidence.

## Gate status

| Requirement | Verdict |
|---|---|
| Explicit effective energy and units | PASS (constructed candidate) |
| Euler–Lagrange equation and beta=0 limit | PASS (analytic) |
| EFMW-specific derivation of beta | UNRESOLVED |
| Unique numerical prediction without beta specification | FAIL |
| Numerical BVP solution and frozen curve | NOT RUN |
| Established GP and other comparators on data | NOT RUN |
| External evidence / replication | NOT RUN |

## Source provenance

- Canonical EFMW catalogue: https://github.com/enuminous/Monolithic_102_EFMW/blob/main/CANONICAL_102.md
- Lagrangian audit: https://github.com/enuminous/EFMW-Lagrangian/blob/main/README.md
- Phase-vorticity model: https://github.com/enuminous/Phase-Vorticity-Lab/blob/main/docs/MODEL.md

**Conclusion:** A dimensionally sound candidate correction and its conditional vortex-density prediction have been derived. No source-grounded EFMW value for beta, numerical result, experimental advantage or independent validation has been established.
