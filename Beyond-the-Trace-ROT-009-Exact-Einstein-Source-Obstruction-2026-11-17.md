# Beyond the Trace: An Exact Einstein-Source Obstruction in an Expanding, Rotating Scalar–Maxwell Model (ROT-009)

**Matthew Chenoweth Wright**  
Monolithic LLC · eNuminous research program  
**17 November 2026**  
**Article type:** Standalone mathematical research paper and source-linked computational no-go  
**Evidence status:** Publicly reproduced symbolic calculation; **not peer-reviewed, not an observation of the universe's global rotation, and not a verified EFMW-specific physical mechanism**.

**Underlying independent research record:** [ROT-009 original protocol](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_PROTOCOL.md) · [exact technical audit](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_FULL_TENSOR_AUDIT.md) · [source-pinned script](https://github.com/enuminous/Rotation/blob/main/research/rot009_source_first_full_tensor.py) · [executed terminal ledger](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_TERMINAL_LEDGER.json).

## Abstract

A scalar field may satisfy its wave equation and the trace of the Einstein field equations while still failing to provide the tensorial stresses required by a curved spacetime. We examine that distinction using a previously published, expanding and rotating, causally admissible Korotkii–Obukhov metric. The ROT-009 candidate retains a fixed canonical Einstein–massless-real-scalar–Maxwell action with zero cosmological constant and scalar potential. A specified logarithmic-in-time, linear-in-space real scalar satisfies both its wave equation and the Einstein trace, a step that the earlier linear candidate ROT-008 did not survive. However, reconstructing the ten symmetric Einstein residual components yields an exact obstruction: the geometry requires a negative spatial component \(G_{xx}=-399/1616\), while the scalar and the chosen real Maxwell potential produce nonnegative \(T_{xx}\). The discrepancy obeys a strictly positive, parameter-independent lower bound \(T_{xx}-G_{xx}\ge 259299/241592\) on the entire declared domain. Both signs of the frozen scalar parameter terminate at this contradiction. These conclusions are symbolically reproducible from the repository's pinned computations, including a machine-captured terminal ledger. The result excludes **one explicitly frozen source and ansatz for one fixed rotating metric**, not arbitrary electromagnetic configurations, other scalar–vector actions, or cosmological rotation in the observed universe. It illustrates why scalar-level consistency is not a sufficient test of a proposed physical field theory.

**Keywords:** rotating cosmology; general relativity; Korotkii–Obukhov spacetime; scalar field; Maxwell stress; Einstein tensor; directional stress; falsification; exact computation; bounded no-go result; EFMW.

---

## 1. Why the trace was the wrong finish line

The existence of an expanding, rotating Lorentzian geometry does not by itself identify the matter responsible for its curvature. A physically specified theory must supply a stress tensor through a declared field action and satisfy its own Euler–Lagrange equations along with all Einstein components. Testing only a scalar projection of those equations leaves directional stresses, momentum fluxes and anisotropies unverified.

The preceding ROT-004–ROT-008 investigation systematically tightened the conditions applied to a proposed positive cosmic-rotation contribution in the Monolithic 102 framework. It compared the hypothesis to 1+3 covariant GR, checked Gödel's non-expanding rotating solution, verified a causal expanding rotating family member, eliminated some conventional sole matter sources by tensor eigenvalue multiplicities, and tested two restricted scalar–Maxwell source models. The immediately preceding ROT-008 model failed because a real linear scalar could not satisfy the wave equation and Einstein trace simultaneously. That sequence is separately published in [Rotation Under Constraint](https://github.com/enuminous/papers/blob/main/Rotation-Under-Constraint-Covariant-and-Source-First-Audits-ROT004-ROT008-2026-11-17.md).

ROT-009 was a deliberately separate follow-up. It chose a nontrivial logarithmic scalar profile that satisfies those two necessary scalar gates, retained the previous ordinary scalar–Maxwell action, and demanded a complete Einstein-tensor source check. The narrow mathematical question was: **Can this predeclared source support the chosen expanding and rotating spacetime without adding new fields or tuning the geometry after inspecting the result?**

The answer is **no**. Importantly, the negative result emerges after the initial scalar tests pass. The issue is a mismatch of a spatial Einstein component, not a failure of algebraic trace matching.

This article synthesizes the original [ROT-009 full-tensor technical audit](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_FULL_TENSOR_AUDIT.md) as a standalone paper, retaining the equation-level proof and exact source boundaries. The underlying geometry and conventional field equations are established prior literature, not new cosmological discoveries of Monolithic LLC.

## 2. Frozen metric, action and source fields

Use signature \((-+++)\), \(\kappa=8\pi G=1\), \(c_{\rm light}=1\), \(\Lambda=0\), and \(\mathcal V(\phi)=0\). On \(t>-2\), let \(a(t)=1+t/2>0\), and take the metric from [ROT-005](https://github.com/enuminous/Rotation/blob/main/research/ROT-005_KOROTKII_OBUKHOV_BRIDGE.md):

\[
ds^2=-\left(dt+\frac{a e^{x/2}}{10}dy\right)^2
+a^2 dx^2+\frac{101}{100}a^2e^xdy^2+a^2dz^2.
\tag{1}
\]

The **unchanged** canonical Einstein–scalar–Maxwell action is

\[
S=\int d^4x\,\sqrt{-g}\left[
\frac R2-\frac12(\nabla\phi)^2-\frac14 F_{ab}F^{ab}
\right],\qquad F=dA.
\tag{2}
\]

Its stress tensor is derived from the declared action:

\[
\begin{aligned}
T^{(\phi)}_{ab}
&=\nabla_a\phi\nabla_b\phi-\tfrac12g_{ab}(\nabla\phi)^2,\\
T^{({\rm EM})}_{ab}
&=F_{ac}F_b{}^c-\tfrac14g_{ab}F_{cd}F^{cd}.
\end{aligned}
\tag{3}
\]

The previously selected [ROT-009 candidate](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_PROTOCOL.md) is

\[
\phi(t,x)=\frac{101d}{100}\ln a(t)+dx,\qquad
d^2=\frac{39850}{30199}>0,\qquad
A=E(t)e^{x/2}dy+B(t)dz,
\tag{4}
\]

where \(d\) has **both real signs**, and \(E(t)\), \(B(t)\) are arbitrary **real** sufficiently differentiable functions. We introduced no scalar potential, cosmological constant, additional field, or new physical parameter.

This metric is from a previously known rotating cosmological family [Korotkii and Obukhov, 1991](https://jetp.ras.ru/cgi-bin/dn/e_072_01_0011.pdf); neither its geometry nor the existence of rotating solutions is claimed as a new discovery.

## 3. The earlier two gates genuinely pass

The scalar profile was chosen because ROT-008's necessary checks became solvable without discarding the frozen action.

Exact computation gives

\[
\Box\phi=0,\qquad
(\nabla\phi)^2=\frac{299d^2}{400a^2}.
\tag{5}
\]

With the fixed \(d^2\), this equals the required Ricci scalar:

\[
R=\frac{797}{808a^2}
=\frac{299d^2}{400a^2}.
\tag{6}
\]

Thus the scalar wave equation and the **trace** of the Einstein equation agree. Standard four-dimensional Maxwell stress remains traceless, and \(F=dA\) guarantees the homogeneous Maxwell Bianchi identity \(dF=0\).

**PASS for these necessary conditions alone.** No prior report stated that passing them would establish a full Einstein–matter solution.

## 4. Exact no-go: the spatial \(xx\) Einstein component

The existing [ROT-005 independent Einstein-tensor computation](https://github.com/enuminous/Rotation/blob/main/research/rot005_ko_sympy.py), recomputed again in the successful ROT-009 CI job, gives

\[
\boxed{G_{xx}=-\frac{399}{1616}<0.}
\tag{7}
\]

For the frozen **real** scalar, direct metric variation and substitution give

\[
\boxed{T^{(\phi)}_{xx}=\frac{501}{800}d^2\ge0.}
\tag{8}
\]

For the declared Maxwell potential, with \(E'=\frac{dE}{dt}\), \(B'=\frac{dB}{dt}\), the exact action-derived stress is

\[
\boxed{
T^{({\rm EM})}_{xx}=
\frac{25\,E(t)^2}{202\,a(t)^2}
+\frac{50}{101}\Big(E'(t)^2+B'(t)^2\Big)\ge0.
}
\tag{9}
\]

Every coefficient is positive, the scale factor is positive, and the field amplitudes and derivatives are real. There is no free sign that can turn these squares into the required negative spatial stress.

Consequently, the exact \(xx\) Einstein residual is

\[
\begin{aligned}
G_{xx}-T^{(\phi)}_{xx}-T^{({\rm EM})}_{xx}
&=-\frac{399}{1616}-\frac{501}{800}d^2\\
&\quad-\frac{25E(t)^2}{202a(t)^2}
-\frac{50}{101}\left(E'(t)^2+B'(t)^2\right)<0.
\end{aligned}
\tag{10}
\]

Substituting the fixed \(d^2=39850/30199\) produces the **strict, global lower bound**

\[
\boxed{
T_{xx}-G_{xx}\ \ge\ \frac{259299}{241592}>0
\quad\text{for every }t>-2,\text{ all real }E,B.
}
\tag{11}
\]

Even the Maxwell null \(E=E'=B'=0\) leaves a strictly positive mismatch. Adding Maxwell amplitudes of the frozen form only increases it.

**FAIL: the \(xx\) Einstein field equation \(G_{xx}=T_{xx}\) cannot hold for this metric and source.** This is a pointwise tensor equation; a contradiction in one component in a fixed coordinate system suffices to exclude a full tensor equality.

### Why the finding is both strong and limited

It is strong because it rules out every permitted real \(E(t)\), \(B(t)\), for **both** signs of \(d\), on the entire declared spacetime domain, rather than ruling out only a numerical parameter fit.

It is limited because \(\eqref{9}\)'s nonnegative Maxwell stress applies to **this frozen potential ansatz**. General electromagnetic fields can have tensile stresses; an arbitrary \(F_{ab}\), another scalar profile or an additional interaction is not analyzed by this argument. The fact that ROT-005's **effective** stress obeyed a weak-energy-condition bound does not guarantee that a particular canonical scalar–Maxwell decomposition can realize it.

## 5. Full-system execution and early stopping

The published SymPy script performs the following checks:

1. Calls the previously independently tested ROT-005 metric computation, which reconstructs Christoffel symbols, Ricci tensor and Einstein tensor from the metric.
2. Constructs the complete four-dimensional metric inverse and obtains the full covariant Einstein tensor in the coordinate basis.
3. Derives the canonical scalar stress tensor from \(\phi\), verifies the wave equation \(\Box\phi=0\), and checks that its trace matches the frozen geometric trace at \(d^2=39850/30199\).
4. Constructs \(F=dA\) with arbitrary symbolic \(E(t),B(t)\), derives all Maxwell stress components, proves its four-dimensional trace vanishes, and verifies \(dF=0\).
5. **Builds all ten symmetric Einstein-equation residual components** and independently extracts the exact \(xx\) residual.
6. Forms all four covariant Maxwell divergences \(\nabla_aF^{ab}\), but does **not** pretend to solve them; such a calculation is unnecessary after the strict Einstein contradiction.
7. Checks two real sign branches \(d=\pm\sqrt{39850/30199}\), both closing at **TERMINAL FAIL**. Several positive-scale and Maxwell-amplitude diagnostics verify arithmetic, but the proof is the exact global sign inequality, not sampled values.

The source first constructs the **entire** stress and Einstein tensors. Its final verdict is **not** a claim that every remaining dynamical equation was solved; the original protocol explicitly permits stopping on a sufficient exact contradiction.

### Recorded machine verdict

The actual GitHub Actions job reports:

| Machine-checked field | Recorded result |
|---|---|
| `verification_status` | `PASS_EXACT_FULL_TENSOR_CONSTRUCTION_AND_BOUNDED_NO_GO` |
| `candidate_verdict` | `FAIL_FROZEN_LOG_SCALAR_PLUS_MAXWELL` |
| `full_einstein_symmetric_components_constructed` | 10 |
| `wave_equation` | 0 |
| `Maxwell_stress_trace` | 0 |
| `allowed_real_branches` | 2 |
| `terminal_fail_branches` | 2 |
| `Einstein_G_xx` | \(-399/1616\) |
| `strict_lower_bound_of_Txx_minus_Gxx` | \(259299/241592\) |
| `termination` | `PROVEN_UNSAT_FOR_TWO_FROZEN_REAL_SIGN_BRANCHES` |

The result was captured from successful [GitHub CI run 44216731940](https://github.com/enuminous/Rotation/actions/runs/44216731940), executing source commit `a40b5cd4b9515af880255efd83f1412b2ff56f44`, then copied to the [archived machine ledger](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_TERMINAL_LEDGER.json). A successful CI run is evidence of reproducible *software execution*, not independent mathematical referee review.

## 6. Zoo-style findings

| ID | Verdict | Exact scope |
|---|---|---|
| ROT009-PROTO-01 | **PASS** | Original action and log-scalar ansatz preserved from the earlier protocol |
| ROT009-GR-01 | **PASS** | Exact previously known KO Einstein tensor reconstructed; \(G_{xx}<0\) |
| ROT009-SCALAR-01 | **PASS** | Frozen real scalar obeys \(\Box\phi=0\) and matches Einstein's necessary trace |
| ROT009-EM-01 | **PASS** | Maxwell stress derived, traceless, \(dF=0\); four dynamic equations formed but not solved |
| ROT009-TENSOR-01 | **PASS** | All ten Einstein residuals constructed, one sign-definite contradiction isolated |
| ROT009-FIELD-01 | **FAIL** | \(G_{xx}=T_{xx}\) has no solution in the fixed source class |
| ROT009-BRANCH-01 | **PASS proof / FAIL model** | Both permitted real \(d\) branches terminate for arbitrary real Maxwell amplitudes |
| ROT009-MICRO-01 | **UNRESOLVED** | Any independently specified richer physical source with correct negative directional stress |
| ROT009-OBS-01 | **UNRESOLVED** | Observable global rotation or any new EFMW-specific cosmological prediction |

## 7. Research consequence and appropriate next gate

ROT-009 closes the **particular logarithmic scalar + standard Maxwell ansatz**. It does **not** justify broadening the word “universal” in a physical conclusion.

The important information gained is that **a matching scalar expansion equation, wave equation, and Einstein trace do not suffice**. One spatial Einstein component can impose a different, sharply discriminating stress requirement. An effective source that satisfies the weak energy condition can still fail to be expressible as the particular canonical fields chosen afterward.

The next research gate should be **source-first physical selection**, not another blind coefficient search: identify an independently justified matter action that permits the required directional stress and momentum flux; derive \(T_{ab}\) by varying that action; and test all field equations and physical admissibility before considering astronomy. If no such source emerges, keep the EFMW physical bridge **UNRESOLVED** rather than force a fit by adding a term post hoc.

A different scalar potential, arbitrary \(F_{ab}\), scalar-vector coupling, imperfect-fluid source, cosmological constant, metric or causal domain must receive its **own separately numbered hypothesis and prior source definition**, not silently amend the failed ROT-009 protocol.

## 8. Reproduction

```bash
git clone https://github.com/enuminous/Rotation.git
cd Rotation
python -m pip install sympy==1.14.0
python research/rot005_ko_sympy.py
python research/rot009_source_first_full_tensor.py
```

Source: [research/rot009_source_first_full_tensor.py](https://github.com/enuminous/Rotation/blob/main/research/rot009_source_first_full_tensor.py).  
Machine ledger: [research/ROT-009_TERMINAL_LEDGER.json](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_TERMINAL_LEDGER.json).  
Exact recorded verification: [GitHub Actions run 44216731940](https://github.com/enuminous/Rotation/actions/runs/44216731940).

The main canonical ME-055/056 equations remain unchanged, as does the original ROT-009 protocol.

## 9. Conclusion

**ROT-009 terminates in a definite bounded failure**: its logarithmic massless scalar and real Maxwell potential pass the scalar-wave and Einstein-trace checks, but cannot supply the negative \(xx\) component of the fixed expanding, rotating GR geometry. The mismatch is exact and uniformly positive in \(T_{xx}-G_{xx}\), independent of electromagnetic amplitudes, for both permitted real scalar branches.

The research conclusion is **not** a detection, a complete physical field theory or a universal scalar–Maxwell no-go. It is a reproducible demonstration of why scalar-level agreement cannot substitute for complete tensor-level consistency.

*Prepared for Matthew Chenoweth Wright / Monolithic LLC with AI-assisted symbolic work. Original literature retains attribution. Neither the original authors nor any outside reviewer has endorsed this computation.*



## 10. Discussion: what the terminated branch actually teaches

ROT-009's critical result is a **one-component impossibility certificate**. The wave equation and Einstein trace each constrain combinations of the fields, but neither guarantees sufficient directional stress. In this example the fixed geometry's negative \(G_{xx}\) cannot be achieved by a scalar plus Maxwell potential whose corresponding spatial stresses are constrained to be nonnegative.

This is stronger than a failed numerical search because it covers **all real functions in the frozen Maxwell ansatz**, not merely a finite grid or particular initial data. Yet it is also narrower than a general theorem excluding scalar–electromagnetic matter: a more general Maxwell field can carry directional tension, and additional matter, nonminimal couplings, new potentials or another metric can change the stress decomposition. Those changes would need their own separately specified experimental protocols, not a retrospective adjustment to ROT-009.

The important scientific outcome is an improved falsification workflow. **A model that reproduces an expansion history, a field wave equation and a trace is not necessarily a solution of Einstein's equations.** Complete tensor-level consistency remains an indispensable gate before promoting a proposed cosmic-rotation mechanism to an observational hypothesis.

No CMB likelihood, redshift survey, measured global axis, independent expert peer review or physical experiment was performed in ROT-009. Its computation establishes the conditional mathematical failure of the candidate, not whether the observed universe rotates.

## References

1. V. A. Korotkii and Yu. N. Obukhov, *Kinematic Analysis of Cosmological Models with Rotation*, **Soviet Physics JETP** 72, 11–15 (1991), [original publication](https://jetp.ras.ru/cgi-bin/dn/e_072_01_0011.pdf). Historical expanding/rotating cosmological metric family.
2. V. A. Korotky, E. Masár and Yu. N. Obukhov, *In the Quest for Cosmic Rotation*, **Universe** 6, 14 (2020), [doi:10.3390/universe6010014](https://doi.org/10.3390/universe6010014). Cosmological rotation review and metric context.
3. G. F. R. Ellis and H. van Elst, *Cosmological Models* (1998), [arXiv:gr-qc/9812046](https://arxiv.org/abs/gr-qc/9812046). Covariant kinematical decomposition and Einstein constraints.
4. M. C. Wright, [*Rotation Under Constraint: A Reproducible Sequence of Covariant and Source-First Tests (ROT-004–ROT-008)*](https://github.com/enuminous/papers/blob/main/Rotation-Under-Constraint-Covariant-and-Source-First-Audits-ROT004-ROT008-2026-11-17.md) (2026). Preceding source-linked research series.
5. M. C. Wright / Monolithic LLC, [*ROT-009 Source-First Logarithmic Scalar Continuation: Exact Spatial Einstein Obstruction*](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_FULL_TENSOR_AUDIT.md) (2026), with [source](https://github.com/enuminous/Rotation/blob/main/research/rot009_source_first_full_tensor.py), [prior frozen protocol](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_PROTOCOL.md), and [CI-executed terminal ledger](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_TERMINAL_LEDGER.json).
6. [ROT-009 original successful GitHub Actions run 44216731940](https://github.com/enuminous/Rotation/actions/runs/44216731940), exact source revision a40b5cd4b9515af880255efd83f1412b2ff56f44; [post-publication full verification run 44217437955](https://github.com/enuminous/Rotation/actions/runs/44217437955).
7. Planck Collaboration, *Planck 2015 Results. XVIII. Background Geometry and Topology of the Universe*, **Astronomy & Astrophysics** 594, A18 (2016), [doi:10.1051/0004-6361/201525829](https://doi.org/10.1051/0004-6361/201525829). Model-dependent observational constraints, **not directly tested in ROT-009**.

### Authorship and evidence disclosure

**Research author and curator:** Matthew Chenoweth Wright, Monolithic LLC. This standalone manuscript adapts the original ROT-009 technical report with OpenAI GPT-6 assistance; the related computational code and documentation were also AI-assisted. All standard general-relativistic identities and the known Korotkii–Obukhov geometry are credited to the literature above. A green CI run is not independent scientific validation; no original metric author, outside referee or collaborator is represented as having endorsed the findings. **This is a public computational research manuscript, not a journal-accepted paper.**
