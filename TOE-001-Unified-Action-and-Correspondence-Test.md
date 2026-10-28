# TOE-001 — A Covariant EFMW-Inspired Unified Action and Correspondence Test

**Date:** 28 October 2026  
**Research:** Matthew Chenoweth Wright / Monolithic LLC, with AI-assisted mathematical and software construction.  
**Status:** **Conditional classical effective-field-theory candidate; NOT a Theory of Everything.**

> This paper specifies a covariant GR + Standard Model + two-scalar action and derives an on-shell conservation identity, classical stability conditions, causal memory representation and a testable *mathematical* response. The original historical EFMW tensor, the observed Standard Model, quantum gravity, and any unique EFMW physical signature are **not** derived.

## 1. Provenance and conventions

The starting point is the separate two-scalar memory candidate in [QST-002](https://github.com/enuminous/QST/blob/main/QST-002.md). This TOE-001 package makes its correspondence and falsification obligations explicit. The classical GR and Standard Model actions are existing physics **inserted as inputs**; the two-scalar construction is conventional and is not claimed as an EFMW discovery. The original source-sign, gauge-current and stress-energy issues remain documented by [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian).

Use a four-dimensional Lorentzian spacetime of signature (-+++), natural units, a reduced Planck mass squared M_Pl² = (8πG)⁻¹, and smooth real scalar fields φ and χ. Assume conventional positive kinetic terms and no direct Standard Model portal.

## 2. Candidate covariant action

Define V(φ,χ) = (m²/2)φ² + (M²/2)χ² + g φχ, where m²>0 and M²>0 are squared masses, and g is a real mass-squared mixing parameter. The metric tensor is denoted g_{μν}, distinct from the mixing parameter g.

$$
\boxed{ S = \int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R+\mathcal L_{\rm SM}-\frac12(\nabla\phi)^2-\frac12(\nabla\chi)^2-V(\phi,\chi)\right]+S_{\rm GHY}. }
$$

Metric variation gives M_Pl² G_{μν}=T_SM,μν+T_scalar,μν. Scalar variation with compatible boundary conditions gives

$$
(\Box_g-m^2)\phi=g\chi,\qquad(\Box_g-M^2)\chi=g\phi.
$$

For the signature chosen, the flat equations are φ̈ − ∇²φ + m²φ + gχ = 0 and χ̈ − ∇²χ + M²χ + gφ = 0.

## 3. Stress-energy and conservation

The scalar stress tensor is

$$
T^{\rm scalar}_{\mu\nu}=\partial_\mu\phi\partial_\nu\phi+\partial_\mu\chi\partial_\nu\chi-g_{\mu\nu}\left[\tfrac12(\nabla\phi)^2+\tfrac12(\nabla\chi)^2+V\right].
$$

Under the stated regularity and variational assumptions, its covariant divergence obeys the identity

$$
\nabla^\mu T^{\rm scalar}_{\mu\nu}=(\Box_g\phi-\partial_\phi V)\nabla_\nu\phi+(\Box_g\chi-\partial_\chi V)\nabla_\nu\chi.
$$

Therefore the total scalar stress is conserved **on solutions of these specific field equations**. With the separately covariant SM action, ∇^μ T_total,μν=0 is compatible with the contracted Bianchi identity. This is a valid conditional conservation derivation for the new model, not a completion of the historical [ME-007-BIANCHI obligation](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md). In particular, no original EFMW informational stress tensor has been identified with this one.

## 4. Linear stability and the flat test system

The mass matrix is K = [[m²,g],[g,M²]], with squared-mass eigenvalues

$$
\lambda_\pm=\frac{m^2+M^2\pm\sqrt{(m^2-M^2)^2+4g^2}}{2}.
$$

**The strict positive-definite stability region is m²>0, M²>0 and g²<m²M².** This excludes tachyonic modes in the quadratic flat scalar sector; it does not establish nonlinear, quantum, or background-independent stability. The principal derivatives are those of ordinary locally hyperbolic Klein–Gordon fields, so nothing here supports superluminal propagation.

For spatially uniform fields the energy

$$
E=\tfrac12\dot\phi^2+\tfrac12\dot\chi^2+\tfrac12m^2\phi^2+\tfrac12M^2\chi^2+g\phi\chi
$$

is conserved by the equations of motion. This identity is checked algebraically at the reduced-ODE level and by a velocity-Verlet numerical integration in the companion software.

## 5. A real but conventional memory term

With an appropriate retarded Green function for the χ operator,

$$
\chi(x)=\chi_{\rm hom}(x)+g\int d^4y\sqrt{-g(y)}\,G_R(x,y)\phi(y).
$$

Substituting this into the φ equation gives

$$
(\Box_g-m^2)\phi(x)=g\chi_{\rm hom}(x)+g^2\int d^4y\sqrt{-g(y)}\,G_R(x,y)\phi(y).
$$

This is genuinely history-dependent, but is the standard consequence of integrating out a coupled field. It is not a unique EFMW effect; χ's initial data and degrees of freedom remain encoded in the effective description.

## 6. Correspondence and a conditional response test

At φ=χ=0, the new stress vanishes and conventional GR+SM solutions remain solutions: this is a **solution sector**, not a proof that the full extended theory is identical to GR+SM. At g=0 the scalar fields decouple from each other, but they still exist. A physical decoupling limit requires additional analysis.

If one hypothetically probes φ by a small external source Jφ, the *flat-field diagnostic* susceptibility at wave number k and z=(ω+iη)² is

$$
\chi_{\phi\phi}(\omega,k)=\frac{k^2+M^2-z}{(k^2+m^2-z)(k^2+M^2-z)-g^2}.
$$

For nonzero mixing, its two normal-mode poles occur at ω²=k²+λ±; at zero mixing the φ response is single-pole. This is a **mathematical diagnostic**, not yet an observational prediction, because a laboratory source, detector and gauge-invariant portal are unspecified. An ordinary coupled-two-scalar model makes the same prediction, so a conventional two-scalar control is mandatory.

## 7. Reproducible numerical reference

An executable standalone Python 3.10+ package was constructed with no third-party dependencies, including 15 unit tests, a frozen JSON result, an exact two-mode solution, velocity-Verlet integration and the response function. Its archived deliverable was generated and tested in this ChatGPT session. This GitHub markdown is the research record; the complete executable package is distributed separately as TOE-001-Unified-Action-Lab.zip.

Reference parameters (arbitrary dimensionless units): m²=1, M²=4, g=0.25, 20,000 steps at Δt=0.001, initially φ=1 and χ=φ̇=χ̇=0.

| Check | Observed result |
|---|---|
| Python unit tests | 15 / 15 PASS |
| Maximum relative energy drift | 1.2301884583 × 10⁻⁷ |
| Maximum coordinate error vs exact 2-mode solution | 6.7964133554 × 10⁻⁷ |
| Physics verification | No physical experiment or cosmological fit was performed |

## 8. Mandatory closure register

| Gate | Result |
|---|---|
| Covariant candidate action, conditional scalar EOM and conservation identity | PASS — mathematical construction, not independent proof certification |
| Positive linear mass spectrum and flat homogeneous numerical solution | PASS — within model assumptions |
| GR+SM correspondence | PARTIAL — zero-scalar solution sector |
| Original EFMW 102 equations and ME-007 informational tensor derived | **UNRESOLVED** |
| UV-complete quantum gravity / physical quantum spacetime | **UNRESOLVED** |
| Noncircular emergence of observed SM gauge structure | **UNRESOLVED** |
| A physically calibrated, unique EFMW prediction | **UNRESOLVED** |
| Held-out experimental testing and independent replication | **UNRESOLVED** |

**Result: TOE_CLOSED = false.** A successful analytic identity or software unit test cannot promote a conditional sector into a full Theory of Everything.

## 9. The next decisive experiment and theorem

First identify an EFMW source and stress tensor noncircularly and either map them explicitly to this action or reject the identification. Prove conservation in the original EFMW formalism, not merely in a conventional replacement. Specify a physical detector/source coupling and a **quantitative prediction distinct from both GR+SM and a conventional two-scalar EFT** with matched parameters. Freeze error criteria before evaluating independent data. Finally, construct or show an obstruction to a quantum-gravitational completion with a correct 3+1 classical limit.

## Attribution and references

Based on Wright's EFMW research objectives, with the scalar action developed using established classical field-theory machinery and AI assistance. Original GR, SM and effective-field-theory developments are the work of the broader scientific community. The QST-002 precursor and EFMW canonical obligations are referenced above. For standard EFT context see [Isidori, Wilsch & Wyler, Rev. Mod. Phys. 96, 015006 (2024)](https://doi.org/10.1103/RevModPhys.96.015006). Nothing here claims original authorship of the Standard Model or Einstein gravity.
