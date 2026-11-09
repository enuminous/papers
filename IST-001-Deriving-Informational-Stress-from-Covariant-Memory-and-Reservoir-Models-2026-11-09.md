# IST-001 — Deriving Informational Stress from Covariant Memory and Reservoir Models

**Research program:** Matthew Chenoweth Wright / Monolithic LLC  
**Date:** 9 November 2026  
**Preparation:** AI-assisted mathematical research proposal and derivation  
**Status:** **PROPOSED MATHEMATICAL CONSTRUCTION — NOT YET AN EFMW-SPECIFIC PHYSICAL STRESS TENSOR OR A VALIDATED GRAVITATIONAL COUPLING**  
**Companions:** [UNITY-001 Phase 5 identifiability](research/unity-001/phase-5/PHASE5_REPORT.md) · [Frozen source lock](research/unity-001/phase-1/sources.lock.json) · [WITD-002](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/DERIVATION.md) · [C1 candidate](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md)

## Abstract

The most defensible route to a candidate informational stress tensor (IST) is to specify physical degrees of freedom that retain memory, define their metric and interaction dynamics with an action, and calculate their Hilbert stress tensor by metric variation. It is not enough to name a memory statistic “energy,” add a tensor to Einstein’s equation, or choose a coupling after observing gravitational residuals. We first specify a two-real-scalar conservative control, derive the memory-sector stress and its **nonzero exchange current**, and explain why a relaxation equation cannot generally be obtained from that closed two-field action alone. A covariant scalar-field reservoir is then proposed as an explicit conservative parent model; its homogeneous oscillator limit can produce a generalized Langevin memory kernel and, under additional continuum-bath/Markov/overdamped assumptions, the first-order relaxation pattern used in WITD. These constructions are model proposals, not derivations of the historical EFMW equations or evidence of new physical coupling. The path forward requires source-faithful correspondence, full reservoir stress, well-posedness, physically calibrated observables, and a comparison against conventional memory/bath physics.

## 1. Why the existing information tensor is not yet gravitational stress

The frozen Information-Tensor lab defines a displayed tensor \(I_{ab}=T_{ab}[q]+\beta T_{ab}[m]\), with \(m_t=\alpha(q-m)\). In [WITD-002](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/DERIVATION.md), this display does **not** generally equal the energy stored in the interacting \(q,m\) dynamics: a homogeneous two-state counterexample rules out a universal constant \(\beta\) under the given assumptions. WITD supplies a conditional smooth storage balance but **not** a joint covariant action, conserved reservoir momentum or independently calibrated gravitational source. The source-frozen [EFMW-Lagrangian C1](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md) is an effective-action candidate with unmatched literal scalar signs, gauge currents, and gravitational stress identifications. Those deficiencies must be retained.

The Phase 5 [source-only identifiability experiment](research/unity-001/phase-5/PHASE5_REPORT.md) demonstrated a separate obstacle: gravitational response to \(T+\kappa I\) can be exactly mimicked by a co-located conventional mass component when \(T\) is unrestricted. Any proposed IST must have independently constrained degrees of freedom, not just a new name for ordinary matter.

## 2. Conservative mathematical control: two real scalars

Work in four-dimensional Lorentzian spacetime with \((-+++)\), \(c=\hbar=1\), smooth fields \(q,m\), constant real parameters, compactly supported field/metric variations, and an ordinary scalar potential \(V(q)\). Define **a new illustrative model**:

\[
S[q,m,g]=\int d^4x\sqrt{-g}\Big[
-\tfrac12(\nabla q)^2-V(q)
-\tfrac Z2(\nabla m)^2
-\tfrac{\mu_m^2}{2}m^2
-\tfrac K2(q-m)^2\Big],\qquad Z>0.
\tag{IST-1}
\]

For a chosen bookkeeping split \(S=S_q+S_I\), let \(S_I\) contain memory kinetic energy, memory mass and the \(q-m\) interaction. Define the **Hilbert stress of that particular split**:

\[
I_{\mu\nu}\equiv-\frac{2}{\sqrt{-g}}\frac{\delta S_I}{\delta g^{\mu\nu}}
=Z\,\nabla_\mu m\nabla_\nu m
-g_{\mu\nu}\left[\tfrac Z2(\nabla m)^2+\tfrac{\mu_m^2}{2}m^2+\tfrac K2(q-m)^2\right].
\tag{IST-2}
\]

The allocation of interaction stress to \(I_{\mu\nu}\) rather than \(T^{(q)}_{\mu\nu}\) is a **convention**; only the stress of the *complete physical action* is independent of that internal bookkeeping choice. This is not proof that nature has an additional universal gravitational charge called “information.”

The Euler–Lagrange equations are

\[
\Box_g q - V'(q)-K(q-m)=0,\qquad
Z\Box_g m-\mu_m^2m+K(q-m)=0.
\tag{IST-3}
\]

By direct product rule and equations of motion,

\[
\nabla^\mu I_{\mu\nu}
=\bigl[Z\Box_g m-\mu_m^2m+K(q-m)\bigr]\nabla_\nu m
-K(q-m)\nabla_\nu q
=-K(q-m)\nabla_\nu q.
\tag{IST-4}
\]

Meanwhile \(\nabla^\mu T_{\mu\nu}^{(q)}=+K(q-m)\nabla_\nu q\). Thus

\[
\boxed{\nabla^\mu(T_{\mu\nu}^{(q)}+I_{\mu\nu})=0}
\tag{IST-5}
\]

**on shell**. Separate conservation of \(I_{\mu\nu}\) is neither expected nor required. An Einstein coupling, if adopted, must account for the **total** source with a documented coefficient and all reservoir stress, consistent with the contracted Bianchi identity.

For homogeneous fields on fixed Minkowski spacetime, the nonnegative energy candidate when \(Z>0,\mu_m^2\ge0,K\ge0,V(q)\ge0\) is
\(E=\frac12\dot q^2+\frac Z2\dot m^2+V(q)+\frac{\mu_m^2}{2}m^2+\frac K2(q-m)^2\). This simple conservative control does **not** produce irreversible exponential relaxation by itself: \(m\) satisfies a second-order equation.

## 3. A covariant reservoir parent, not a claimed WITD derivation

Introduce real bath fields \(x_j\) with scalar positive kinetic weights \(z_j\), positive frequencies \(\omega_j\), and dimensionful couplings \(a_j\). Consider the **new** parent matter action

\[
\begin{aligned}
S_{\rm parent}=\int d^4x\sqrt{-g}\bigg[
&-\tfrac12(\nabla q)^2-V(q)
-\tfrac Z2(\nabla m)^2-\tfrac K2(q-m)^2\\
&-\sum_{j=1}^{N}\frac{z_j}{2}\Big((\nabla x_j)^2+
\omega_j^2(x_j-a_jm)^2\Big)\bigg].
\end{aligned}
\tag{IST-6}
\]

The parent is a classical local diffeomorphism-invariant scalar theory for fixed scalar parameters. Its *total* Hilbert stress is covariantly conserved on shell, provided the gravitational and matter equations of motion and appropriate boundary conditions hold. The memory+reservoir portion has a nonzero exchange current with the q sector analogous to (IST-4).

**Important:** finite closed bath systems are reversible and can exhibit recurrences. A genuine dissipative limit needs a justified large/continuum reservoir, initial-state assumptions, a causal coarse-graining procedure, and thermodynamic/noise constraints. An action with a few oscillator fields alone does not prove irreversible relaxation.

In a spatially homogeneous flat background, holding \(q(t)\) as a prescribed drive and writing \(M=Z,\;c_j=z_j\omega_j^2a_j\), the \(m\) equation and bath modes take the usual oscillator-reservoir form,

\[
M\ddot m+K(m-q)+\sum_j\Big(\frac{c_j^2}{z_j\omega_j^2}m-c_jx_j\Big)=0,\qquad
\ddot x_j+\omega_j^2x_j=\frac{c_j}{z_j}m.
\tag{IST-7}
\]

Solving the linear bath equations with specified initial values and substituting gives the generalized Langevin equation,

\[
M\ddot m(t)+K[m(t)-q(t)]
+\int_0^t \gamma(t-s)\dot m(s)\,ds=\xi(t),
\tag{IST-8}
\]

where
\[
\gamma(t)=\sum_j\frac{c_j^2}{z_j\omega_j^2}\cos(\omega_jt),\quad
\xi(t)=\sum_j c_j\Big[(x_j(0)-\frac{c_jm(0)}{z_j\omega_j^2})\cos(\omega_jt)
+\frac{\dot x_j(0)}{\omega_j}\sin(\omega_jt)\Big].
\tag{IST-9}
\]

The \(\xi\) term is a deterministic function of bath initial conditions until a statistical ensemble is specified; **it must not be casually called measured white noise**. If a controlled continuum bath produces an approximately local drag coefficient \(\Gamma>0\), with \(\xi\) negligible in the stated mean/limit and \(M\ddot m\) negligible on slow time scales, then

\[
\dot m\simeq(K/\Gamma)(q-m)=\alpha(q-m).
\tag{IST-10}
\]

This is a **conditional route to the form of** the WITD relaxation law, with \(\alpha=K/\Gamma\), not a demonstration that the historical EFMW law was physically derived, that the continuum bath exists, or that the approximation is valid for a particular device.

For background on reservoir-to-Langevin reduction, see [standard oscillator-bath derivations](https://www.tkm.kit.edu/img/mitarbeiter/Er1999-Energy.pdf). For dissipative effective actions, fluctuations and KMS constraints, see [Crossley, Glorioso & Liu (JHEP 2017)](https://doi.org/10.1007/JHEP09(2017)095) and [Glorioso, Crossley & Liu (JHEP 2017)](https://doi.org/10.1007/JHEP09(2017)096). Those are **conventional precedents**, not evidence of EFMW-specific novelty.

## 4. Physical and mathematical gates

| Gate | What must be established |
|---|---|
| IST-A | Derive the metric stress consistently from a complete covariant action and state exactly which interaction energy belongs in the proposed IST |
| IST-B | Prove on-shell covariant conservation of **total** stress; specify nonzero inter-sector exchange and any bath flux |
| IST-C | Recover the actual WITD/EFMW relaxation in an independently justified coarse-graining limit with declared approximation bounds |
| IST-D | Establish allowed parameter domain, positivity, absence of unstable/ghost degrees of freedom, and causal/well-posed dynamics in the regime claimed |
| IST-E | Reproduce the frozen WITD energy ledger, including its numerical FAIL groups, without treating a new parent as identical by notation |
| IST-F | Demonstrate source-faithful mathematical correspondence to frozen EFMW C1/102/165 equations, preserving prior sign, gauge-current and stress mismatches |
| IST-G | Supply physical units, matter calibration, instrument response, independently constrained conventional alternative, and a non-degenerate observable |
| IST-H | Secure external replication and prospective testing **after** all prerequisites are satisfied |

**Possible outcomes:** PASS, FAIL or UNRESOLVED for each scope. A generic reservoir stress is ordinary gravitational matter stress. A claim of uniquely EFMW-specific information gravity must be shown by an independent effect beyond conventional matter/bath models.

## 5. Work authorization and decision

Proceed to an **IST-001 reproducibility package** containing (1) explicit conservative and reservoir equations, (2) independently executed exact algebra and finite-bath energy tests, (3) a full provenance/conflict ledger, and (4) a neutral research report. **Do not** publish a physical-discovery claim, recast the previously frozen EFMW source equations, or declare Phase 5’s identifiability obstruction resolved.

**Current physics status: UNRESOLVED.**
