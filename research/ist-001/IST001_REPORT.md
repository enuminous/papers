# IST-001 — Executed Hilbert Memory-Stress and Harmonic-Reservoir Audit

**Research program:** Matthew Chenoweth Wright / Monolithic LLC  
**Date:** 9 November 2026  
**Preparation:** AI-assisted mathematical analysis and software implementation  
**Status:** **BOUNDED MATHEMATICAL CONTROLS PASS — PHYSICAL EFMW-SPECIFIC IST UNRESOLVED**  
**Primary theoretical memo:** [Deriving Informational Stress from Covariant Memory and Reservoir Models](../../IST-001-Deriving-Informational-Stress-from-Covariant-Memory-and-Reservoir-Models-2026-11-09.md)  
**Frozen before executable checks:** [PROTOCOL.json](PROTOCOL.json), [commit b2372f8](https://github.com/enuminous/papers/commit/b2372f8e0928def0b8b25e523420ad39afcd99de).  
**Executable:** [ist.py](ist.py) · [test_ist.py](test_ist.py) · [CI workflow](../../.github/workflows/ist-001.yml) · [complete machine-generated CI result artifact](https://github.com/enuminous/papers/actions/runs/42669567461/artifacts/13697398989) · [CI run](https://github.com/enuminous/papers/actions/runs/42669567461).

## Abstract and primary result

We implemented a reproducible verification scaffold for a **new illustrative classical memory-field action**, its metric-dependent partial Hilbert stress tensor, a conservative two-field exchange identity, and a covariant scalar-reservoir *parent* with a homogeneous oscillator-bath reduction. The results support a **conditional mathematical route** from physical memory degrees of freedom to a stress-energy calculation and a nonlocal memory kernel. They do not establish a new fundamental informational stress tensor, derive the full frozen WITD/EFMW dynamics, establish a controlled irreversible continuum-bath limit, or measure a distinct gravitational effect.

**Executed GitHub Actions outcome:** 24/24 adversarial tests passed; the eight predeclared gate groups are **6 bounded PASS, 0 FAIL, 2 UNRESOLVED**, with **0 EFMW-specific physical PASS**. These metrics must not be combined with the old MOC-001 5/40, Unity Phase 2 9/717, or Phase 5 4/11 ledgers.

The tested results are a deliberately narrow *conventional field-theory control*. A rigorous EFMW-specific scientific claim still requires an independently derivable and physically identifiable departure from conventional matter/bath dynamics.

## 1. Scientific starting point and source fidelity

The pinned [Information-Tensor WITD-002](https://github.com/enuminous/Information-Tensor/blob/b02b04897743d34cdb846e9fac2518cd8faa4399/research/witd-002/DERIVATION.md) model includes \(m_t=\alpha(q-m)\), a chosen memory stress display \(I_{ab}=T_{ab}[q]+\beta T_{ab}[m]\), and additional forced, dissipative and Scalar-23 dynamics. WITD-002 finds that its displayed \(I_{00}\) generally **does not equal** the model's total storage for any one constant \(\beta\) in a defined set of states. The pinned [EFMW-Lagrangian C1](https://github.com/enuminous/EFMW-Lagrangian/blob/83f9d2ec03e055c6cd09aa6359189161ad1571f6/candidate/CANDIDATE.md) supplies a different proposed classical effective action and explicitly retains sign, current and stress-identification mismatches.

The present IST-001 construction is an **additional candidate**. Source commits and Git object hashes are checked against the published [Phase 1 source lock](../unity-001/phase-1/sources.lock.json). No historical source equation was edited, renamed as derived or reclassified as independently validated.

## 2. Conservative parent: stress and exchange

With metric signature \((-+++)\), smooth scalars \(q,m\) and \(Z>0\), consider

\[
\mathcal L_q=-\frac12(\nabla q)^2-V(q),\qquad
\mathcal L_I=-\frac{Z}{2}(\nabla m)^2-\frac{\mu_m^2}{2}m^2-\frac K2(q-m)^2.
\]

As an explicit bookkeeping convention assign the entire \(q-m\) interaction to the memory sector. The Hilbert stress of that partial action is

\[
\boxed{I_{\mu\nu}
=Z\nabla_\mu m\nabla_\nu m+g_{\mu\nu}\mathcal L_I.}
\tag{IST-C1}
\]

The equations are

\[
\Box q-V'(q)-K(q-m)=0,\quad
Z\Box m-\mu_m^2m+K(q-m)=0.
\tag{IST-C2}
\]

Using the product rule and the \(m\) equation,

\[
\nabla^\mu I_{\mu\nu}=-K(q-m)\nabla_\nu q,\qquad
\nabla^\mu T^{(q)}_{\mu\nu}=+K(q-m)\nabla_\nu q.
\tag{IST-C3}
\]

Thus the *total* source is conserved on both equations of motion, whereas the memory contribution is typically **not conserved separately**. This compensating exchange is necessary in a consistent matter coupling to Einstein gravity. **It does not establish that the partial split is uniquely physical.**

**Metric-variation verification:** The [code](ist.py) varies the symmetric inverse metric independently in a \(1+1\) Lorentzian control and checks both the kinetic variation and variation of the metric volume factor. **32/32 exact-rational metric examples** agree with the stated Hilbert tensor, including off-diagonal components.

**Energy-exchange verification:** In homogeneous scalar models with polynomial \(q(t),m(t)\), the code checks

\[
\frac{dE_q}{dt}=\dot q\,\mathcal E_q-K(q-m)\dot q,\qquad
\frac{dE_I}{dt}=\dot m\,\mathcal E_m+K(q-m)\dot q,
\]

and hence \(d(E_q+E_I)/dt=\dot q\,\mathcal E_q+\dot m\,\mathcal E_m\). Here \(\mathcal E_q,\mathcal E_m\) are the unforced equations-of-motion residuals. All **48/48 exact polynomial examples** agree; the on-shell total-energy balance follows algebraically. These are finite symbolic controls and do **not** constitute a clean Lean kernel replay of a general curved manifold theorem.

### A meaningful negative control: IST is not uniquely split

If the interaction density \(W_{\rm int}=K(q-m)^2/2\) is assigned to the ordinary scalar action instead, the named partial tensors shift by \(\pm g_{\mu\nu}W_{\rm int}\), but their sum remains the same. The executable algebra confirms this. Consequently, the internal \(I_{\mu\nu}\) of a coupled model is **conventional unless its component assignment has an additional independently operational definition**. A distinct label is not a distinct gravitational force.

## 3. Physical reservoir parent and finite-bath dynamics

The proposed *covariant local scalar parent* is

\[
\mathcal L_{\rm parent}=\mathcal L_q-\frac Z2(\nabla m)^2
-\frac K2(q-m)^2
-\sum_j\frac{z_j}{2}\left[(\nabla x_j)^2+\omega_j^2(x_j-a_jm)^2\right],
\tag{IST-R1}
\]

where \(z_j,\omega_j^2>0\). This has a well-defined Hilbert stress as an ordinary scalar field theory and, for a compatible potential, positive homogeneous oscillator energy. The actual complete stress includes \(x_j\) kinetic energy and coupling potential, not just \(I_{00}\) from the earlier WITD display.

In its spatially homogeneous, flat-background limit,

\[
Z\ddot m+K(m-q)-\sum_j z_j\omega_j^2a_j(x_j-a_jm)=0,\qquad
\ddot x_j+\omega_j^2(x_j-a_jm)=0.
\tag{IST-R2}
\]

The published code checks **35/35 exact-rational on-shell homogeneous total-energy derivatives**. A velocity-Verlet numerical integration of two bath oscillators, using a frozen parameter set over a two-time-unit toy run, yields relative total-energy errors at step counts \(50,100,200,400\) of approximately:

| Time steps | Relative energy defect (toy) |
|---:|---:|
| 50 | \(7.642\times10^{-5}\) |
| 100 | \(1.916\times10^{-5}\) |
| 200 | \(4.794\times10^{-6}\) |
| 400 | \(1.199\times10^{-6}\) |

The successive ratios are **3.988, 3.997, 3.999**, consistent with second-order finite-step convergence in this one test. These numbers are *not* a claim of spatial/continuum convergence, irreversible thermodynamics, or experimentally measured energy.

### Exact finite-bath memory kernel

In the homogeneous driven-memory problem, eliminating the harmonic bath leads to

\[
Z\ddot m+K(m-q)+\int_0^t\gamma(t-s)\dot m(s)\,ds=\xi(t)
\tag{IST-R3}
\]

with \(\gamma(t)=\sum_j z_j\omega_j^2a_j^2\cos(\omega_jt)\). The initial-condition forcing \(\xi(t)\) is given explicitly in the [theory memo](../../IST-001-Deriving-Informational-Stress-from-Covariant-Memory-and-Reservoir-Models-2026-11-09.md), where it is **not** assumed to be random white noise.

Using an independently manufactured \(m(t)=m_0+vt\) trajectory and prescribed external \(q(t)\), the executable directly compares the eliminated integral equation with the bath ODEs at six frozen times. The **maximum numerical residual is \(1.11\times10^{-16}\)**. This tests the specified manufactured trajectory. It is **not** proof of a general continuum reservoir kernel or an autonomous coupled \(q,m\) solution.

### Why first-order relaxation is still conditional

An additional assumed local drag \(\Gamma\dot m\) and a justified overdamped limit can produce

\[
\dot m\simeq(K/\Gamma)(q-m)=\alpha(q-m).
\tag{IST-R4}
\]

The code verifies a closed-form solution of that reduced **assumed** equation for \(q(t)=t,\alpha=1/2\). This is a **consistency check of the reduced ODE**, not a derivation of Markov friction from the two-oscillator bath. A finite closed bath is time reversible and may recur. Establishing the continuum spectral-density limit, noise statistics and fluctuation–dissipation/KMS constraints remains a separate demanding obligation.

This distinction is essential: first-order relaxation could be **conventional open-system physics**, without a unique informational gravitational interpretation.

## 4. Executed gate results

[GitHub Actions run 42669567461](https://github.com/enuminous/papers/actions/runs/42669567461) completed on [commit 52c0b8d](https://github.com/enuminous/papers/commit/52c0b8d67a3dfc8685686e3080b6d897153b7247), using Python 3.12 and standard-library code. **24/24 tests passed**. The [result manifest](https://github.com/enuminous/papers/actions/runs/42669567461/artifacts/13697398989) was saved by the CI workflow; these are reproducible *software results*, not external physical data.

| Frozen gate | Outcome | Precisely scoped interpretation |
|---|---|---|
| IST-01: metric-derived stress | **PASS** | 32 exact local symmetric-metric variation controls and stated Hilbert split |
| IST-02: conservative exchange | **PASS** | 48 exact homogeneous polynomial residual identities |
| IST-03: finite reservoir energy | **PASS** | 35 exact homogeneous energy identities and one numerical convergence example |
| IST-04: GLE memory elimination | **PASS** | Driven homogeneous manufactured finite-bath check, six time points |
| IST-05: first-order relaxation | **PASS (conditional)** | Assumed Markov/overdamped ODE solution; not derivation of the bath continuum limit |
| IST-06: split convention | **PASS** | Partial interaction stress changes, full stress unchanged |
| IST-07: source-faithful EFMW/WITD dynamics and tensor | **UNRESOLVED** | Scalar-23/coherence, noise, nonlocality, covariant reservoir stress and physical calibration not derived from frozen equations |
| IST-08: unique EFMW gravitation and experimental observation | **UNRESOLVED** | No nondegenerate physical signal, actual instrument, held-out data or independent replication |

**Denominator: six of eight narrowly specified gates passed; zero of the two EFMW-specific physics gates passed.** No new Phase 5 physical readiness or physical prediction claim follows.

## 5. Reproduce and audit

From the root of [enuminous/papers](https://github.com/enuminous/papers), with Python 3.12+ and no third-party packages:

~~~bash
python3 -m unittest discover -s research/ist-001 -p 'test_*.py' -v
python3 research/ist-001/ist.py --out research/ist-001/build/results.json
~~~

The script checks the exact prior C1/WITD commit and blob identities against [Phase 1 \`sources.lock.json\`](../unity-001/phase-1/sources.lock.json), refuses unexplained frozen-protocol gate promotion, and outputs its reported numerical diagnostics and limitations. No time-inappropriate external measurement is fetched.

The executable's output is held as a [CI artifact](https://github.com/enuminous/papers/actions/runs/42669567461/artifacts/13697398989) so users can distinguish generated test evidence from narrative.

## 6. The real next scientific obligations

**First:** construct a controlled **continuum oscillator-bath spectral density** with a defensible Markov/overdamped approximation and quantitative error estimates, including fluctuation–dissipation/thermal or other specified initial-state constraints.

**Second:** derive the **complete on-shell covariant reservoir stress**, including metric variation, physical units, stress exchange, and if needed a stable hyperbolic system under an explicitly stated domain. The local parent action makes such a derivation possible in principle but this run has not mechanized it on a curved manifold.

**Third:** prove or reject an explicit **source-faithful map** from the frozen WITD \((q,m,\Phi,h)\) equations, with their noise, Scalar-23 updates and energy accounting, to the new parent; do not force the map by changing the original source statements. In particular, WITD's numerical energy FAIL gates remain in the historical record.

**Fourth:** distinguish the resulting gravity prediction from all admissible conventional scalar+reservoir matter models and the [Phase 5 co-located mass obstruction](../unity-001/phase-5/PHASE5_REPORT.md) using independently constrained matter and a genuinely specified instrument/measurement.

**Fifth:** obtain independent mathematical and physical evaluation. Without those, do not claim a new informational gravitational sector.

### Program decision

**IST-001 mathematical control package: bounded PASS.**  
**Physically derived and unique EFMW informational stress tensor: UNRESOLVED.**  
**Confirmatory EFMW gravity prediction: NOT READY.**

### External theoretical precedents

- Crossley, Glorioso & Liu, *Effective field theory of dissipative fluids*, JHEP 2017, 95. [DOI](https://doi.org/10.1007/JHEP09(2017)095).
- Glorioso, Crossley & Liu, *Effective field theory of dissipative fluids (II)*, JHEP 2017, 96. [DOI](https://doi.org/10.1007/JHEP09(2017)096).
- [Oscillator-bath generalized Langevin derivation](https://www.tkm.kit.edu/img/mitarbeiter/Er1999-Energy.pdf).

These are conventional field-theory and open-systems precedents, **not** independent validations of EFMW-specific information gravity.
