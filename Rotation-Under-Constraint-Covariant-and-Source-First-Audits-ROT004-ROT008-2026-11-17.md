# Rotation Under Constraint: A Reproducible Sequence of Covariant and Source-First Tests (ROT-004–ROT-008)

**Matthew Chenoweth Wright**  
Monolithic LLC · eNuminous research program  
**17 November 2026**  
**Research status:** Public, source-linked computational mathematics and falsification report; **not peer-reviewed, not an observational detection, and not a proof of an EFMW-specific physical law**.

**Primary source archive:** [enuminous/Rotation](https://github.com/enuminous/Rotation)  
**Frozen sequence revision:** [06068231be6a1e147e2ebb2267061e041f61fe0d](https://github.com/enuminous/Rotation/tree/06068231be6a1e147e2ebb2267061e041f61fe0d)  
**Final verification:** [GitHub Actions 44174200808](https://github.com/enuminous/Rotation/actions/runs/44174200808)

## Abstract

Rotation appears in classical fluids, spinor representations, complex phases, astrophysical objects, and exact general-relativistic spacetimes. The existence of these distinct structures does not establish a single physical rotation of the universe. We describe five sequential, bounded tests of a proposed positive rotation contribution in the Monolithic 102 cosmological scalar equation. First, we compare the hypothesis with the covariant 1+3 Einstein constraint and independently recompute the classical Gödel rotating, non-expanding dust solution (ROT-004). We then verify a published Korotkii–Obukhov geometry with simultaneous expansion, nonzero physical vorticity, stable causality, and a weak-energy-condition bound for an **effective** stress tensor defined from the Einstein tensor (ROT-005). A source-first analysis excludes several ordinary minimal matter classes as sole sources of the chosen metric by their invariant stress-tensor eigenvalue multiplicities (ROT-006). A minimally coupled real homogeneous scalar plus Maxwell field fails a necessary Einstein trace equation (ROT-007). A subsequent real linear scalar profile \(\phi=ct+dx\) fails an exact scalar wave/einstein-trace compatibility test; both orders of a deterministic recursive proof search reach terminal contradictions after six total proof nodes (ROT-008). We preserve the intermediate negative results, the prediction and stop-rule record, and executable evidence. The findings constrain **specified metrics, actions and ansatz classes**, not every scalar-based theory. They provide neither an EFMW-specific physical mechanism nor evidence that the observed universe rotates.

**Keywords:** cosmological vorticity; 1+3 covariant GR; Gödel spacetime; Korotkii–Obukhov geometry; scalar–Maxwell action; Frobenius theorem; exact symbolic algebra; falsification; bounded recursive proof search; reproducibility.

---

## 1. The question the tests actually address

The Monolithic 102 corpus preserves a proposed cosmic velocity-vorticity relationship, [ME-055](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/055.md), and a Friedmann-like expansion equation, [ME-056](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/056.md),

\[
H^2=\frac{8\pi G\rho+\Lambda}{3}
       -\frac{k}{a^2}+\frac{\Omega_U^2}{a^2}. \tag{1}
\]

The quantity \(\Omega_U\) in (1) was introduced as a proposed rotation parameter, not independently derived from a rotating Lorentzian metric, matter congruence and stress-energy action. It should not automatically be identified with a Euclidean curl, a scalar angular speed, or the invariant vorticity magnitude of a relativistic observer field. ME-056 is a **working hypothesis**, not a proven cosmological field equation.

We distinguish at least three different questions: whether rotation occurs locally (established), whether general relativity permits globally described geometries with rotating matter observers (yes, in mathematical models), and whether the **observed** universe requires a common rotation parameter (not established). A Clifford rotor representing SO(3) or Spin(3), a complex U(1) phase and a physical cosmic vorticity tensor are not interchangeable merely because each uses a rotational algebra.

The investigation therefore asks a limited technical question:

> Under explicit GR geometry, observer and matter-source assumptions, which interpretations or specializations of the proposed ME-056 term survive exact consistency checks?

This paper reports **mathematical testing**, not new experimental astronomy. The related work on geometric algebra and the existing Monolithic 102 Lean modules provide useful background but were not treated as independent observational evidence or as a new Lean formalization of the entire Einstein system.

## 2. Mathematical framework and research protocol

Adopt spacetime signature \((-+++)\), \(c=1\), \(\kappa=8\pi G\), a normalized timelike observer congruence \(u^a u_a=-1\), expansion \(\Theta=\nabla_a u^a\), \(H=\Theta/3\), scalar shear magnitude \(\sigma^2=\tfrac12\sigma_{ab}\sigma^{ab}\), and physical vorticity magnitude \(\omega^2=\tfrac12\omega_{ab}\omega^{ab}\). Let \(\mathcal R\) denote the scalar of the **projected local rest-space connection**. When \(\omega\ne0\), the local rest spaces are not in general the tangent spaces of global observer-orthogonal spatial hypersurfaces. Thus identifying \(\mathcal R\) with \(6k/a^2\) from FLRW cosmology requires additional conditions.

The conventional 1+3 Gauss scalar constraint is [Ellis and van Elst; Danehkar, refs. 1–2]

\[
3H^2=\kappa\rho+\Lambda+\sigma^2-\omega^2
                  -\frac{\mathcal R}{2}. \tag{2}
\]

The bare \(-\omega^2\) contribution in this **constraint** must not be confused with the \(+2\omega^2\) term in the distinct Raychaudhuri **evolution equation** for \(\dot\Theta\). Nor does (2), by itself, determine the net effect of rotation once shear, acceleration, matter evolution and projected curvature are allowed to change.

Equating (1) and (2), with matching \(\rho,\Lambda,H\), yields a **necessary but insufficient** compatibility condition,

\[
\boxed{\frac{3\Omega_U^2}{a^2}
=\sigma^2-\omega^2
-\frac12\left(\mathcal R-\frac{6k}{a^2}\right).} \tag{3}
\]

The right-hand side need not be nonnegative. A successful derivation of ME-056 would have to supply a consistent spacetime, source and normalization that cause (3) and every other Einstein equation to hold. Matching the scalar relation alone would not suffice.

### Research controls

For each ROT stage we retained the existing source equation, pinned the tested metric/field class, and recorded the first necessary condition that succeeded or failed. Exact SymPy identities were tested by symbolic simplification and, for full metric cases, computations from Christoffel symbols and curvature tensors. A specific conditional FAIL was never promoted to a general no-go. In ROT-008, a prediction/stop-rule document was committed before the corresponding new executable; this is **exploratory source discipline, not sealed external preregistration**.

The machine results are reproducible within [Rotation](https://github.com/enuminous/Rotation). The scripts and CI runs are **not independent GR peer review, new telescope data, or kernel-checked Lean proofs of the generic Einstein equations**.

## 3. ROT-004: the Gödel rotating, non-expanding control

The first adversarial case is Gödel's classical Einstein-dust spacetime [3], which rotates but does not expand. A conventional coordinate realization with \(m>0\) is

\[
ds^2=-(dt+e^{mx}dy)^2+dx^2+\frac12 e^{2mx}dy^2+dz^2. \tag{4}
\]

For \(u^a=\delta^a_t\), an independent symbolic calculation reproduced the Einstein/dust equation and

\[
\Theta=0,\quad \sigma^2=0,\quad
\omega^2=\frac{m^2}{2}>0,\quad
\kappa\rho=m^2,\quad \Lambda=-\frac{m^2}{2}. \tag{5}
\]

This model is an exact **counterexample to the general inference that nonzero rotation must generate positive expansion**. The earlier-known solution includes closed timelike curves and is not asserted to describe the observed universe. Assigning \(a=1,k=0,\Omega_U^2=\omega^2\) in (1) gives a mismatch, but those are **extra choices** lacking a canonical mapping from Gödel's non-hypersurface-orthogonal geometry to FLRW's variables. The valid conclusion is narrow: an independently positive universal additive term does not follow merely from vorticity.

**Disposition:** PASS for exact sourced GR tensor checks and the classical negative control; FAIL for the overgeneralized “rotation necessarily adds expansion” interpretation; UNRESOLVED for an EFMW-specific rotating cosmological field equation.

**Reproduction:** [ROT-004 report](https://github.com/enuminous/Rotation/blob/main/research/ROT-004_COVARIANT_BRIDGE.md) · [Gödel tensor script](https://github.com/enuminous/Rotation/blob/main/research/rot004_godel_sympy.py).

## 4. ROT-005: expansion and physical vorticity can coexist

We next selected a representative of the already published Korotkii–Obukhov family [4–5], using \(t>-2\), \(a(t)=1+t/2>0\), and the exact metric

\[
ds^2=-\left(dt+\frac{a(t)e^{x/2}}{10}dy\right)^2
+a(t)^2dx^2+\frac{101}{100}a(t)^2e^xdy^2+a(t)^2dz^2. \tag{6}
\]

The source literature uses related sign and spatial-orientation conventions. This **is not a newly discovered rotating metric**. Its exact symbolic reconstruction with \(u^a=\delta^a_t\) gives

\[
H=\frac1{2a}>0,\qquad
\omega^2=\frac1{1616a^2}>0,\qquad
\sigma^2=0,\qquad
\mathcal R=-\frac{203}{404a^2}. \tag{7}
\]

The inverse metric has \(g^{tt}=-100/101<0\). On the stated coordinate domain, the global time coordinate has a timelike gradient, establishing stable causality there; geodesic completeness is **not** established.

The Einstein tensor was recomputed, and an **effective** source \(T^{\rm eff}_{ab}=G_{ab}/\kappa\) was formed, with \(\kappa=1,\Lambda=0\). Exact conservation, the Gauss constraint and Raychaudhuri relation were checked. For all causal vectors in the coframe used, the constructed source obeys the strict weak-energy-condition lower bound

\[
T^{\rm eff}_{ab}v^av^b/\gamma^2\ge
\frac{400-20\sqrt{101}}{1616a^2}>0. \tag{8}
\]

This is a bounded **mathematical** property of the effective source; it is not a derivation of matter from a standalone Lagrangian. Setting \(T=G/\kappa\) after choosing the metric cannot, by itself, explain what material creates the geometry.

### Testing ME-056

If one explicitly identifies \(k_{\rm ME}=a^2\mathcal R/6\) and \(\Omega_{\rm ME}^2=a^2\omega^2\), then

\[
H_{\rm ME056}^2-H_{\rm GR}^2
=\frac1{1212a^2}>0. \tag{9}
\]

That direct mapping **FAILS**. Yet a retuned scalar curvature parameter \(k_{\rm ME}=-67/808\) exactly reproduces the same scalar expansion curve. This shows a **curvature–rotation identifiability problem**, not an independent detection of rotation. The physical matter congruence in the original GR metric does have vorticity; the failure concerns what can be inferred from the separately proposed scalar equation and its assigned parameters.

**Disposition:** PASS for the existing expanding/rotating causal geometry and effective-source checks; FAIL for the stated direct ME-056 mapping; UNRESOLVED for an independently derived physical source and an identifiable observable.

**Reproduction:** [ROT-005 report](https://github.com/enuminous/Rotation/blob/main/research/ROT-005_KOROTKII_OBUKHOV_BRIDGE.md) · [exact Einstein-tensor code](https://github.com/enuminous/Rotation/blob/main/research/rot005_ko_sympy.py).

## 5. ROT-006: which conventional matter tensors cannot be the sole source?

For the **fixed** metric (6), the mixed effective stress tensor, scaled as \(M=1616a^2T^a{}_b\), has exact characteristic polynomial

\[
\det(zI-M)=(z-3)
\big(z^3+1597z^2+798403z+127206399\big). \tag{10}
\]

The exact greatest common divisor of this polynomial with its derivative is 1: its four algebraic eigenvalues are distinct. Their multiplicity structure is invariant under a change of orthonormal frame.

This immediately rejects several *standalone* source classes for this particular geometry:

- A perfect fluid has a repeated triple pressure eigenvalue, even when tilted.
- A minimally coupled first-derivative real scalar has a mixed tensor of the form \(L\delta^a_b+v^a v_b\), retaining at least three eigenvalues \(L\).
- Two ordinary minimally coupled first-derivative real scalars, including a simple complex scalar, have an at-most-rank-two correction to \(L\delta^a_b\), retaining at least two repeated eigenvalues under the stated action assumptions.
- An ordinary pure Maxwell field in four dimensions has \(T^a{}_cT^c{}_b=C\delta^a_b\), giving paired eigenvalues rather than four distinct ones.

These are exclusions **as sole sources under the stated minimal theory classes**. They do **not** exclude scalar plus vector matter, independent added sources, nonminimal curvature couplings, higher derivatives or different rotating metrics. A separate Frobenius check also established that the prescribed rotating congruence \(u^\flat\) is not proportional to the gradient of a single timelike scalar, since \(u^\flat\wedge du^\flat\ne0\).

**Disposition:** PASS for coordinate-invariant spectral and Frobenius calculations; FAIL for the enumerated sole-source classes; richer coupled models UNRESOLVED.

**Reproduction:** [ROT-006 source audit](https://github.com/enuminous/Rotation/blob/main/research/ROT-006_SOURCE_FIRST_MATTER_AUDIT.md) · [exact algebra](https://github.com/enuminous/Rotation/blob/main/research/rot006_scalar_source_test.py).

## 6. ROT-007: a predeclared scalar–Maxwell action fails a necessary Einstein trace

ROT-007 stopped reconstructing arbitrary matter *after* the fact and fixed the minimal matter action

\[
S=\int d^4x\,\sqrt{-g}
\left[\frac R2
-\frac12g^{ab}\partial_a\phi\partial_b\phi
-\frac14F_{ab}F^{ab}\right], \tag{11}
\]

with \(\kappa=1,\Lambda=0,V(\phi)=0\), real homogeneous scalar \(\phi=\phi(t)\), and Maxwell potential

\[
A=E(t)e^{x/2}dy+B(t)dz. \tag{12}
\]

In four dimensions Maxwell stress is traceless. The canonical scalar trace is \(T^a{}_a=-(\nabla\phi)^2\). The trace of Einstein's equation therefore requires \(R=(\nabla\phi)^2\). But the fixed geometry gives

\[
R=\frac{797}{808a^2}>0,\qquad
g^{tt}=-\frac{100}{101},
\]

while the prescribed real homogeneous scalar gives

\[
(\nabla\phi)^2=-\frac{100}{101}\dot\phi^2\le0. \tag{13}
\]

Thus Einstein's trace forces

\[
\dot\phi^2=-\frac{80497}{80800a^2}<0. \tag{14}
\]

**No real homogeneous scalar can satisfy this necessary condition**, regardless of the unknown Maxwell amplitudes. A contradiction in one necessary field equation is sufficient to reject the complete coupled system **under these precise assumptions**. The other Maxwell equations were **not** claimed to be solved; they cannot overturn a trace impossibility.

**Disposition:** PASS for exact stress and trace calculation; FAIL for the frozen homogeneous real-scalar plus Maxwell candidate; other matter actions and scalar profiles UNRESOLVED.

**Reproduction:** [ROT-007 research report](https://github.com/enuminous/Rotation/blob/main/research/ROT-007_EINSTEIN_SCALAR_MAXWELL_AUDIT.md) · [source-first trace test](https://github.com/enuminous/Rotation/blob/main/research/rot007_einstein_scalar_maxwell.py).

## 7. ROT-008: a finite recursive search terminates at a proof of incompatibility

ROT-008 changed **only** the scalar profile, to

\[
\phi(t,x)=ct+dx,\qquad c,d\in\mathbb R, \tag{15}
\]

while retaining the fixed metric, minimal massless action, Maxwell sector and zero potential. The [prediction and stopping document](https://github.com/enuminous/Rotation/blob/main/research/ROT-008_PREDICTIONS_AND_STOP.md) was committed **before** executing the new source code. This was an exploratory computational audit informed by previous failures, **not** a blinded external preregistration.

### 7.1 The wave equation

Using the explicit inverse metric and determinant, the scalar equation \(\Box\phi=0\) becomes

\[
\Box\phi=
\frac{101d-300c\,a(t)}{202a(t)^2}=0. \tag{16}
\]

Because this must hold for every \(t>-2\), and \(a(t)=1+t/2\) varies with time, differentiate the numerator: \(c=0\). Substitute back: \(d=0\).

### 7.2 The Einstein trace

For the same fixed source, the Einstein trace instead requires

\[
d^2-\frac{100}{101}c^2a(t)^2
=\frac{797}{808}. \tag{17}
\]

With \(c=d=0\), equation (17) is false. Conversely, differentiate (17) over the time interval to force \(c=0\); it then gives \(d^2=797/808>0\), while the wave equation requires \(d=0\). Either ordering yields a contradiction.

### 7.3 The recursive terminal ledger

| Proof path | First condition | Second condition | Terminal condition |
|---|---|---|---|
| Wave → trace | Global wave equation forces \(c=0\) | Wave equation forces \(d=0\) | **FAIL:** Einstein trace requires \(0=797/808\) |
| Trace → wave | Global trace identity forces \(c=0\) | Trace requires \(d^2=797/808\) | **FAIL:** wave requires \(d=0\) |

The reproducible deterministic search visited **two branches, six total proof nodes, and two exact terminal contradictions**; it then stopped. Its termination came from a mathematical unsatisfiability certificate **within the frozen parameter class**, not a time/iteration limit and not an exhaustive search over all theories.

Negative controls distinguished a scalar that satisfies the wave but not the trace, a spatial gradient satisfying the trace but not the wave, and a parameter choice satisfying an equation at one time but not on the entire domain.

**Actual execution record:** [ROT-008 terminal ledger](https://github.com/enuminous/Rotation/blob/main/research/ROT-008_TERMINAL_LEDGER.json), taken from successful [GitHub Actions run 44173109860](https://github.com/enuminous/Rotation/actions/runs/44173109860) at source SHA **e727c93f35cf2d107483081a1020ece8938aa028**. The full series was later verified at [run 44174200808](https://github.com/enuminous/Rotation/actions/runs/44174200808).

### 7.4 Boundary control: linear scalar no-go is not a general scalar no-go

Outside the frozen class, the broader field

\[
\phi(t,x)=\frac{101d}{100}\log a(t)+dx+C,\qquad
d^2=\frac{39850}{30199}, \tag{18}
\]

can satisfy **the scalar wave and Einstein trace equations alone**. That is a useful counterexample to an overgeneralized claim that all nonhomogeneous real scalars fail those two gates. It **does not** establish any solution of the other Einstein tensor components or Maxwell dynamics.

[ROT-009](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_PROTOCOL.md) proposes this new separately labeled ansatz as an input to a full field-equation test. **ROT-009 is not reported as executed in this paper.**

**Disposition:** PASS for the frozen predictive mathematical identities and exact finite recursive termination; FAIL for the \(\phi=ct+dx\) candidate; general scalar profiles, other actions, and physical cosmic rotation UNRESOLVED.

**Reproduction:** [ROT-008 full report](https://github.com/enuminous/Rotation/blob/main/research/ROT-008_RECURSIVE_TERMINAL_REPORT.md) · [recursive source](https://github.com/enuminous/Rotation/blob/main/research/rot008_recursive_search.py).

## 8. Evidence ledger: what was and was not established

| Stage | Verified mathematical/computational result | Failure or unresolved claim |
|---|---|---|
| ROT-004 | Covariant compatibility algebra and exact Gödel GR rotating non-expanding control | No universally independent positive ME-056 term derived; cosmological application UNRESOLVED |
| ROT-005 | Known causal, expanding, rotating metric, exact tensor reconstruction, WEC of a constructed effective source | Chosen direct ME-056 mapping FAIL; independent matter source and uniquely identifiable rotation UNRESOLVED |
| ROT-006 | Exact simple stress-spectrum and Frobenius obstruction | Enumerated single minimal matter classes FAIL as sole sources of the frozen geometry |
| ROT-007 | Source-first scalar/Maxwell trace identities | Homogeneous real-scalar plus Maxwell class FAILS necessary Einstein trace |
| ROT-008 | Two independent proof orders, six executed nodes, two terminal contradictions | Linear \(\phi=ct+dx\) source class FAILS; broader models and astronomy UNRESOLVED |

A mathematical PASS in this ledger **does not transfer** to a physical theory. A conditional model FAIL **does not transfer** to every theory in its family. Neither is a numeric “percentage of universal rotation proved.”

### Computation and provenance limitations

The first two ROT-008 CI attempts failed on two harness assertions comparing structurally different but algebraically equivalent SymPy expressions with direct equality. The assertions were corrected to compare symbolic differences using simplification. No metric, physical source assumption, real-parameter domain or predicted contradiction was changed. Those failed runs remain visible in GitHub history. Green CI attests to reproducible execution of source-pinned calculations, **not** independent GR expert review or a formal proof-assistant kernel certification.

Gödel's and Korotkii–Obukhov's metrics are established literature, **not new discoveries of this paper**. The contribution here is an explicit claim-to-source comparison, exact reproducibility, matter-class selection logic, and preserved negative stopping decisions.

## 9. Observational and scientific interpretation

The presence of real vorticity in a mathematically consistent metric does not prove nonzero universal rotation in **our** universe. Likewise, Clifford geometric algebra, spinor double covering, complex scalar winding and fluid curl are not measurements of the same physical observable.

The Planck Collaboration's analysis of physical Bianchi VIIh models found no evidence for that rotating cosmological family, constraining its present-day rotation ratio to

\[
(\omega/H)_0 < 7.6\times10^{-10}
\quad\text{at 95% confidence}. \tag{19}
\]

This is **model-specific**, not a universal prohibition on every rotating metric [6]. This research sequence did **not** run a Planck likelihood, measure a galaxy-spin axis or make an independently confirmed EFMW-specific prediction.

The outcome is consequently **UNRESOLVED for universal cosmic rotation**, even while particular mathematical compatibility questions have received definitive conditional answers.

## 10. Next falsifiable work

The [separately stated ROT-009 protocol](https://github.com/enuminous/Rotation/blob/main/research/ROT-009_PROTOCOL.md) keeps the source action and metric fixed but tests a specifically declared logarithmic time/spatial scalar profile. It must verify **all Einstein components and matter field equations together**. If a necessary component contradicts the ansatz, stop at a bounded FAIL. Any new potential, cosmological constant, action or metric must be versioned as a **new** hypothesis rather than silently altering ROT-008.

Beyond this, a credible physical theory must define its source \(T_{ab}\) by independent metric variation of a specified action, establish causality/stability and the relevant congruence, and provide an observable distinguishing its nonzero rotation from conventional GR cosmologies, ordinary matter effects and curvature degeneracy. Only then would a frozen observational comparison with independently controlled data be appropriate.

## 11. Conclusion

The ROT-004–ROT-008 sequence demonstrates the value of allowing a physical hypothesis to meet exact obstructions. A proposed scalar rotation term was compared with covariant GR; a known rotating but static metric and a known expanding rotating causal metric supplied adversarial controls; fixed-source eigenvalue structure excluded standalone minimal matter classes; a frozen Einstein–scalar–Maxwell action failed a necessary trace; and a broader linear scalar profile failed a six-node recursively terminating wave/trace search.

**The mathematical program narrowed and the evidence record improved. It did not establish universal rotation.** The canonical ME-056 text remains intact as a historical working hypothesis. More general scalar–vector models may be investigated in new explicitly bounded tests without rewriting the earlier negative results.

The scientific result is not the rhetoric of a universal rotating cosmos; it is an auditable series of exact mathematical boundaries and the discipline to preserve them.

---

## Reproduction and source custody

**Frozen research source:** [enuminous/Rotation, SHA 06068231be6a1e147e2ebb2267061e041f61fe0d](https://github.com/enuminous/Rotation/tree/06068231be6a1e147e2ebb2267061e041f61fe0d).  
**ROT-008 executable proof SHA:** [e727c93f35cf2d107483081a1020ece8938aa028](https://github.com/enuminous/Rotation/commit/e727c93f35cf2d107483081a1020ece8938aa028).  
**Actual terminal execution log:** [GitHub run 44173109860](https://github.com/enuminous/Rotation/actions/runs/44173109860), archived as [ROT-008_TERMINAL_LEDGER.json](https://github.com/enuminous/Rotation/blob/main/research/ROT-008_TERMINAL_LEDGER.json).  
**Final full verification:** [GitHub run 44174200808](https://github.com/enuminous/Rotation/actions/runs/44174200808).  
**Dependencies:** SymPy **1.14.0** for GR jobs; standard-library Python and Node smoke tests for the wider atlas.

From a clean repository checkout, run:

1. `python -m pip install sympy==1.14.0`
2. `python research/rot004_godel_sympy.py`
3. `python research/rot005_ko_sympy.py`
4. `python research/rot006_scalar_source_test.py`
5. `python research/rot007_einstein_scalar_maxwell.py`
6. `python research/rot008_recursive_search.py`
7. `python -m unittest discover -s tests -v`

Each success label applies only to its recorded computation. There is **no independent telescope experiment**, and the prior prediction document is a public time-ordered source commit, **not** an independently administered sealed scientific preregistration.

## References

1. G. F. R. Ellis and H. van Elst, *Cosmological Models* (1998), [arXiv:gr-qc/9812046](https://arxiv.org/abs/gr-qc/9812046).
2. A. Danehkar, *Covariant Evolution of Gravitoelectromagnetism*, **Universe** 8, 318 (2022), [doi:10.3390/universe8060318](https://doi.org/10.3390/universe8060318).
3. K. Gödel, *An Example of a New Type of Cosmological Solutions of Einstein's Field Equations of Gravitation*, **Reviews of Modern Physics** 21, 447 (1949), [doi:10.1103/RevModPhys.21.447](https://doi.org/10.1103/RevModPhys.21.447).
4. V. A. Korotkii and Yu. N. Obukhov, *Kinematic Analysis of Cosmological Models with Rotation*, **Soviet Physics JETP** 72, 11–15 (1991), [original text](https://jetp.ras.ru/cgi-bin/dn/e_072_01_0011.pdf).
5. V. A. Korotky, E. Masár and Yu. N. Obukhov, *In the Quest for Cosmic Rotation*, **Universe** 6, 14 (2020), [doi:10.3390/universe6010014](https://doi.org/10.3390/universe6010014).
6. Planck Collaboration, *Planck 2015 Results. XVIII. Background Geometry and Topology of the Universe*, **Astronomy & Astrophysics** 594, A18 (2016), [doi:10.1051/0004-6361/201525829](https://doi.org/10.1051/0004-6361/201525829).
7. Matthew Chenoweth Wright / Monolithic LLC, [canonical ME-055](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/055.md) and [ME-056](https://github.com/enuminous/Monolithic_102_EFMW/blob/main/056.md), in the Monolithic 102 source corpus.
8. Monolithic LLC, [ROT-004–ROT-008 reports, scripts, evidence ledger and CI history](https://github.com/enuminous/Rotation/tree/main/research) (2026).

### Authorship and evidence disclosure

**Research author/curator:** Matthew Chenoweth Wright (Monolithic LLC). Manuscript drafting, code construction, source comparison and computational execution were assisted by OpenAI GPT-6. The conventional GR identities, Gödel spacetime, Korotkii–Obukhov metric and ordinary scalar/Maxwell algebra belong to the original research literature cited above. No original author, journal, Topher/Christopher Duguay or independent mathematical referee is represented as having reviewed or endorsed this paper. The report is a **public computational research manuscript**, not a journal-accepted article.
