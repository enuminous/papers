# RHC-001: An EFMW-Based Candidate Formalization of Rahasya's Pulsating-Substrate Pressure Cycle

**Status:** Candidate mathematical model; **not** a verified derivation of quantum mechanics, particle physics, gravity, or consciousness  
**Date:** 27 October 2026  
**Repository:** [enuminous/papers](https://github.com/enuminous/papers)  
**Model designation:** RHC-001 (Rahasya–EFMW pressure-cycle candidate), version 0.1  
**Research and mathematical formulation:** Matthew Chenoweth Wright, Monolithic LLC, with AI-assisted derivation and editorial drafting  
**Source ontology and physical conjecture:** Swami Rahasya, *Physics Paradigm Correction*  
**Authorship/provenance:** The originating philosophical and cavitation-pressure hypothesis is Rahasya's, not Wright's. The mathematical closure, equations, and audit plan below are proposed independently as a response to his text; they are **not** claimed to have been written, reviewed, endorsed, or accepted by Rahasya.

> **Epistemic notice.** This is an exploratory model with explicit assumptions and conditional derivations. An exact solution to an assumed equation is not evidence that the equation describes nature. No Lean verification, numerical benchmark against experimental data, independent replication, or peer review is reported for RHC-001.

## Abstract

Swami Rahasya proposes that a single underlying substance undergoes an all-pervading pulsation that alternately permits and suppresses vortex-driven cavitations, conjectured to underlie matter and gravity. We translate the pressure-cycle portion of that ontology into a mathematically explicit toy model, beginning with a specific EFMW scalar source equation. A **newly postulated linear source closure** reduces the EFMW-form equation to a Klein–Gordon-type wave equation. Its homogeneous periodic solution supplies a candidate pressure field. A threshold gate then defines low-pressure “Moments” and yields an exact duty-cycle formula. Finite-rate cavitation occupancy dynamics give closed-form periodic-state extrema. An optional relaxation-memory variable supplies a testable EFMW-inspired recursive extension. We report conserved mathematical energy for the unforced scalar sector and enumerate major physical obstructions: dimensional and covariance requirements for the EFMW source, an unestablished substrate, vortex topology, the Born rule, energy exchange during cavitation, emergent gravity, preferred-frame constraints, and the observational consequences of a proposed Stoney-scale period. No unification, particle derivation, or gravity derivation is established.

## 1. The claim under examination

Rahasya's *Physics Paradigm Correction* proposes, in summary:

1. An undivided “Singular Substance” undergoing an all-pervading pulsation.
2. Alternating high- and low-pressure conditions.
3. Momentary, pressure-permitted, vortex-driven cavitations associated with apparent matter.
4. Cavitation collapse during high pressure as a proposed mechanism of gravity.
5. A possible fundamental period comparable to the Stoney time.
6. A suggested affinity with J. N. Nielsen's proposed Topological Unified Field Theory (TUFT).

The attached 24-page elaboration provided for this exercise also speculates about tunnelling, consciousness, and holography. Those are **outside the derivations here**. In particular, it would be an error to equate the experimentally controlled which-path distinguishability in a double-slit apparatus with the two phases of a conjectured universal pressure cycle; the former does not establish the latter.

**Question:** Can the pressure-cycle part be expressed as a consistent and falsifiable set of equations without assuming the desired physical conclusion?

**Answer:** Yes, conditionally, by specifying an explicit closure and a pressure-to-cavitation coupling. Those constitutive choices are assumptions, not derived theorems about nature.

## 2. Notation, units, and EFMW input

The EFMW-form equation considered in this note is

$$
\boxed{
\nabla^2\phi-\frac{1}{c^2}\partial_t^2\phi
=\frac{4\pi}{c^2}(E+cP)
}
\tag{1}
$$

This is **one displayed EFMW source-equation variant**, not a claim of compatibility with every operator, sign convention, or coefficient in the larger EFMW catalogue. That reconciliation remains an independent provenance task.

Let $J:=E+cP$. A consistent *candidate* dimensional interpretation is $E$ as energy density and $P$ as a selected component of momentum density, so that $[E]=[cP]=\mathrm{Pa}$ and $[\phi]=\mathrm{kg\,m^{-1}}$. In this convention $[J]=\mathrm{kg\,m^{-1}\,s^{-2}}$.

**Critical issue:** A selected energy-density-plus-momentum-density combination is not generally a Lorentz scalar. Writing Eq. (1) as a scalar-field equation does **not** make its original source prescription covariant. Covariance requires a justified transformation law and physical identification of all terms. Moreover, the letter $P$ in Eq. (1) must **not** be silently identified with Rahasya's physical pressure $p$.

For a constant reference field $\phi_0$, define

$$
u(\mathbf x,t)=\phi(\mathbf x,t)-\phi_0.
$$

The reference must satisfy the relevant background source condition; in the simplest constant background of Eq. (1), that condition is $J_0=0$.

## 3. Explicit source closure (new assumption)

Postulate the **effective** restoring-source law

$$
\boxed{
J_{\mathrm{eff}}=\frac{\omega_0^2}{4\pi}\,u
}
\tag{2}
$$

with $\omega_0>0$ a new model parameter. Equation (2) is **not derived from Rahasya, Nielsen's TUFT, or the established EFMW source ontology**. It is the constitutive assumption responsible for the restoring oscillation.

Substitution into Eq. (1) gives

$$
\nabla^2u-c^{-2}u_{tt}
=c^{-2}\omega_0^2u,
$$

hence

$$
\boxed{
u_{tt}-c^2\nabla^2u+\omega_0^2u=0.
}
\tag{3}
$$

This is a linear Klein–Gordon-type scalar equation. It is not, by itself, a model of a hydrodynamic fluid, gauge interactions, or quantum measurement.

For a spatially uniform mode ($\nabla^2u=0$),

$$
\ddot u+\omega_0^2u=0,
\qquad
\boxed{u(t)=A\cos(\omega_0t+\delta).}
\tag{4}
$$

$A$ and $\delta$ are initial-data constants. The period is $T=2\pi/\omega_0$.

### Mathematical checks

For plane waves $u\propto \exp[i(\mathbf k\cdot\mathbf x-\omega t)]$,

$$
\boxed{\omega^2=c^2|\mathbf k|^2+\omega_0^2.}
\tag{5}
$$

The group velocity is $v_g=c^2|\mathbf k|/\omega<c$ for nonzero $\omega_0$. This is an ordinary dispersion property of Eq. (3), **not** a faster-than-light information channel.

For smooth solutions on space with sufficient decay or on a periodic spatial domain, Eq. (3) conserves

$$
\boxed{
\mathcal E_u=\frac12\int
\big(u_t^2+c^2|\nabla u|^2+\omega_0^2u^2\big)\,d^3x .
}
\tag{6}
$$

Indeed, differentiating, integrating the gradient term by parts, and inserting Eq. (3) yields $d\mathcal E_u/dt=0$ with vanishing boundary flux. This is a positive quadratic mathematical invariant; it is **not automatically physical energy in joules** without a specified action normalization.

A nonzero spatially homogeneous oscillating solution also defines a preferred rest-frame description even though the free differential operator is Lorentz covariant. Its observable consequences must be addressed.

## 4. Pressure as a separate observable-like variable

**New pressure map:**

$$
\boxed{
p(\mathbf x,t)=p_0+\chi u(\mathbf x,t),
}
\tag{7}
$$

where $p$ is physical pressure, $p_0$ is reference pressure, and $\chi>0$ is a constitutive coupling with dimensions $\mathrm{s^{-2}}$ under the normalization above. The mapping is an independent model assumption. In a real fluid, additional density, modulus, stress, and flow equations would be required.

For the homogeneous mode Eq. (4),

$$
\boxed{p(t)=p_0+\Delta p\cos(\omega_0t+\delta),\quad \Delta p=\chi A>0.}
\tag{8}
$$

This is a two-regime oscillation with a continuous pressure range, not a claim that pressure takes only two numerical values.

## 5. Cavitation threshold and exact Moment duty cycle

Let $p_{\rm crit}$ denote a threshold below which cavitation is *permitted*, not guaranteed. Define

$$
\boxed{C(t)=H\!\left(p_{\rm crit}-p(t)\right).}
\tag{9}
$$

$H$ denotes a Heaviside step. Then $C=1$ is the low-pressure permission window and $C=0$ is the high-pressure suppressed window. Values exactly at the threshold are immaterial to the cycle fraction.

Define the dimensionless threshold

$$
\eta=\frac{p_{\rm crit}-p_0}{\Delta p}.
$$

Because $\cos(\omega_0t+\delta)<\eta$ during the permitted phase, the fraction of a cycle spent in that phase is

$$
\boxed{
D(\eta)=
\begin{cases}
0 & \eta\le -1,\\
1-\pi^{-1}\arccos(\eta) & -1<\eta<1,\\
1 & \eta\ge1.
\end{cases}
}
\tag{10}
$$

Thus the low-pressure duration is $T_{\rm low}=DT$ and the high-pressure duration is $T_{\rm high}=(1-D)T$.

**Exact examples:** $\eta=0\Rightarrow D=1/2$; $\eta=-1/2\Rightarrow D=1/3$; $\eta=+1/2\Rightarrow D=2/3$.

These are analytic consequences of the assumed sine wave and threshold, **not measurements of a universal “Moment.”**

## 6. Finite-rate cavity formation and collapse

A permission gate alone cannot describe the formation or disappearance of a cavity. Introduce an occupancy proxy $n(\mathbf x,t)\in[0,1]$ and positive rate constants $\Gamma_{\rm on},\Gamma_{\rm off}$, measured in inverse seconds:

$$
\boxed{
\partial_tn=
\Gamma_{\rm on}C(1-n)-
\Gamma_{\rm off}(1-C)n.
}
\tag{11}
$$

For $C=1$, $n$ relaxes toward one; for $C=0$, it relaxes toward zero. The closed interval $[0,1]$ is invariant for initial values in that interval. This is a kinetic **proxy**, not a derivation of physical vortex volume, particle mass, or energy.

For $0<D<1$, define

$$
a=e^{-\Gamma_{\rm on}DT},
\qquad
b=e^{-\Gamma_{\rm off}(1-D)T}.
$$

Let $n_{\min}$ be occupancy at the start of a low-pressure window, and $n_{\max}$ its value at the end. In a periodic steady state,

$$
n_{\max}=1-(1-n_{\min})a,\qquad n_{\min}=bn_{\max}.
$$

Solving,

$$
\boxed{
n_{\max}=\frac{1-a}{1-ab},\qquad
n_{\min}=\frac{b(1-a)}{1-ab}.
}
\tag{12}
$$

The convergence of occupancy toward the periodic solution is geometric, with one-cycle factor $ab$ for positive durations and rates. The limiting cases $D=0$ and $D=1$ have the obvious pure-decay and pure-formation asymptotic states.

**A sharp physical obligation:** If Rahasya's literal picture requires nearly complete disappearance between Moments, then $\Gamma_{\rm off}(1-D)T\gg1$. Merely having a high-pressure interval is insufficient to show disappearance.

Another obligation is to specify where energy, momentum, charge, and topological information go during the changing occupancy. Equation (11) does not conserve them.

## 7. Optional recursive-history extension

As an **EFMW-inspired candidate extension**, define a memory state $m$ through

$$
\boxed{\tau\dot m+m=u,\quad \tau>0.}
\tag{13}
$$

For a specified history, $m$ is an exponentially weighted record of past $u$ values. Now postulate

$$
J_{\rm eff}=
\frac{1}{4\pi}
\left[\omega_0^2u+\lambda(u-m)-F\right],
$$

where $[\lambda]=\mathrm{s^{-2}}$ and $[F]=[u]\mathrm{s^{-2}}$. The wave equation becomes

$$
\boxed{
u_{tt}-c^2\nabla^2u+\omega_0^2u+
\lambda(u-m)=F,
\qquad
\tau\dot m+m=u.
}
\tag{14}
$$

This introduces a true, explicitly specified feedback state, rather than using “recursion” as a metaphor. Yet it is **not a theorem of EFMW's canonical memory models**; its provenance and comparison with existing EFMW definitions remain open.

For slowly varying $u$, $m\simeq u-\tau u_t$, so $\lambda(u-m)\simeq\lambda\tau u_t$. Thus positive $\lambda$ behaves approximately as damping in this limit. A persistent oscillation in the memory-extended model generally needs suitable forcing or another mechanism; Eq. (14) does not automatically provide perpetual self-sustained motion.

## 8. Stoney time is an optional hypothesis, not a derivation

Rahasya proposes a time scale comparable to the Stoney time. In SI units,

$$
t_S=\sqrt{\frac{G e^2}{4\pi\varepsilon_0 c^6}}
=\sqrt{\alpha_{\rm fs}}\,t_P
\approx 4.605\times10^{-45}\ {\rm s}.
\tag{15}
$$

A **test hypothesis**, rather than an established value, is

$$
\boxed{T=t_S,\qquad
f_0=t_S^{-1}\approx2.17\times10^{44}\ {\rm Hz},
\qquad
\omega_0=2\pi/t_S.}
\tag{16}
$$

The free-frequency model and Stoney-fixed model must be evaluated separately. Choosing $T=t_S$ because it appears physically suggestive is not evidence of a real Stoney clock. A universal phase-locked time background would also face stringent preferred-frame/covariance tests.

At this scale, direct temporal resolution is unavailable with current instrumentation; useful tests need *derived*, observable lower-energy signatures with quantitative amplitudes, not merely a stated frequency.

## 9. Why this is not yet a derivation of quantum theory or gravity

### 9.1 Missing vortex structure

A real scalar $u$ by itself has no continuous internal phase whose winding generates an ordinary quantized vortex. A candidate extension might introduce an independent complex order parameter $\Psi=R e^{i\theta}$ and a winding quantity

$$
\nu=\frac{1}{2\pi}\oint_\gamma\nabla\theta\cdot d\boldsymbol{\ell}\in\mathbb Z
$$

where this construction is well-defined. Coupled field equations, topology, stability, and particle properties would still need to be derived. Nothing here identifies vortices with electrons, photons, fermions, or the Standard Model spectrum.

### 9.2 Missing quantum measurement and Born rule

A model of a periodically permitted detector event is **not** a derivation of quantum probabilities. In standard two-path quantum mechanics, which-path detector overlap determines interference via

$$
P(x)=|\psi_1|^2+|\psi_2|^2+
2\operatorname{Re}\left[
\psi_1^*\psi_2\langle d_1|d_2\rangle
\right].
\tag{17}
$$

Experimental visibility and distinguishability exhibit a continuous complementarity relationship, often written $V^2+D^2\le1$ under the relevant definitions. A viable proposed replacement must **derive**, not insert, the amplitudes, distinguishability dependence, unitarity or an appropriately documented alternative, and the Born rule. In particular, two experimental conditions (“which-path information available” versus “not”) do not themselves demonstrate cosmic temporal alternation.

### 9.3 Missing gravity

Local contraction, cavitation collapse, and pressure gradients do not automatically imply Newton's $1/r^2$ force, gravitational redshift, Einsteinian lensing, universal free fall, or the Einstein field equations. A dynamical stress-energy tensor, constitutive equations, a covariant long-wavelength limit, and comparison with strong-field and gravitational-wave constraints are necessary.

### 9.4 Missing physical conservation

The invariant $\mathcal E_u$ of Eq. (6) is only for the isolated free scalar sector. Adding the occupancy proxy, pressure coupling, or driving may exchange or create modeled energy unless full equations and energy accounting are supplied. We cannot claim physical energy conservation for the combined system.

### 9.5 TUFT correspondence unproved

Rahasya's suggested relationship to J. N. Nielsen's proposed TUFT is a research comparison, not a mathematical embedding. No map from the Hopf-bundle variables of that proposal to $(u,p,C,n,m)$, and no equality of dynamical predictions, is demonstrated here.

### 9.6 Consciousness excluded

The source discussion extends the ontology to a supposed singular consciousness mediated by persistent shear topology. That is not established by the pressure-cycle mathematics and is excluded from RHC-001's results.

## 10. Minimal reproducibility checks

A reviewer can independently verify Eqs. (3)–(16) symbolically or numerically. A simple exact duty-cycle reference implementation is:

```python
import math

def low_pressure_fraction(eta: float) -> float:
    if eta <= -1:
        return 0.0
    if eta >= 1:
        return 1.0
    return 1.0 - math.acos(eta) / math.pi

def steady_occupancies(eta, period, gamma_on, gamma_off):
    if period <= 0 or gamma_on <= 0 or gamma_off <= 0:
        raise ValueError("period and rates must be positive")
    duty = low_pressure_fraction(eta)
    if duty == 0:
        return 0.0, 0.0
    if duty == 1:
        return 1.0, 1.0
    a = math.exp(-gamma_on * duty * period)
    b = math.exp(-gamma_off * (1 - duty) * period)
    nmax = (1 - a) / (1 - a * b)
    return b * nmax, nmax

assert math.isclose(low_pressure_fraction(-0.5), 1/3)
assert math.isclose(low_pressure_fraction(0.0), 0.5)
assert math.isclose(low_pressure_fraction(0.5), 2/3)
assert 0 <= steady_occupancies(-0.5, 1, 2, 4)[0] <= 1
```

These checks validate formulas under the specified assumptions, not particle behavior. At Stoney-scale periods, simulation should use nondimensional time $s=t/T$ to avoid extreme scale disparity.

## 11. Falsification and next experimental design (RHC-002)

**Primary comparison:** Does adding a pressure-cycle gate to an otherwise fixed two-path interferometric model produce a uniquely specified, measurable prediction without assuming quantum probabilities?

A suitable registered sequence is:

1. **Freeze baseline:** Ordinary quantum two-path density-matrix model including partial which-path distinguishability and environmental decoherence.
2. **Freeze candidate:** Fix Eqs. (1)–(11), state how detector event probabilities are generated, and prohibit manually inserting the target Born-rule distribution as a free lookup table.
3. **Energy/covariance checks:** State frame transformations, stress-energy balance, and which observable quantities couple to the pressure cycle.
4. **Ablations:** Compare no gate, fixed-duty gate, variable-duty gate, randomized phase, and any memory-extended gate at equal complexity and calibration budgets.
5. **Observables:** Predefine fringe visibility versus detector distinguishability, phase behavior, and any proposed periodic sidebands; specify realistic detector resolution and noise.
6. **Decision:** Report PASS only on predeclared mathematical or empirical criteria; FAIL on demonstrated contradictions; UNRESOLVED where derivation or observation is missing; N/A when genuinely inapplicable.

If the model exactly reproduces standard quantum predictions without novel observations, it is at most a candidate *interpretation*, not an experimentally established physical correction. Failure on partial distinguishability would directly challenge the simplest binary-gate account.

## 12. Claims register

| Claim | Scope | Status |
|---|---|---|
| Restoring-source assumption reduces Eq. (1) to Eq. (3) | Conditional algebra | **Derived** |
| Eq. (3) admits homogeneous periodic solutions | Linear PDE/ODE | **Derived** |
| Threshold gate has duty cycle Eq. (10) | Sinusoid + threshold assumptions | **Derived** |
| Finite-rate occupancy has extrema Eq. (12) | Piecewise linear kinetic ODE | **Derived** |
| Isolated free scalar has invariant Eq. (6) | Boundary assumptions | **Derived** |
| Memory extension produces physically stable, self-sustained pressure dynamics | Requires further analysis | **UNRESOLVED** |
| $E+cP$ is a covariant source for a physical scalar | Source transformation undefined | **UNRESOLVED** |
| Singular Substance exists | Physical ontology | **UNRESOLVED** |
| Cycle period equals the Stoney time | Physical hypothesis | **UNRESOLVED** |
| Cavitations represent Standard Model particles | No derived spectrum or topology | **UNRESOLVED** |
| Pressure cycle derives the Born rule or double-slit probabilities | Missing model | **UNRESOLVED** |
| Cavitation collapse yields GR/Newtonian gravity | Missing field-equation limit | **UNRESOLVED** |
| TUFT and RHC-001 are equivalent | No constructed correspondence | **UNRESOLVED** |
| Consciousness is a shear-topological invariant | Not investigated by this model | **N/A** |

## 13. Conclusion

A pressure oscillation, its cavitation-permission windows, and a finite-rate cavity occupancy law can be mathematically specified and audited. This turns the pressure-cycle component of Rahasya's hypothesis into a **conditional modeling target**, not a physical discovery. The decisive step is to derive a quantum-interference prediction, including partial path distinguishability, from the actual proposed dynamics and test it against a conventional equal-complexity baseline. Gravity and particle-physics claims remain separate, larger derivational burdens. The unproven constitutive closure must stay visible wherever the model is cited.

## Sources and provenance

- **Swami Rahasya**, [*Physics Paradigm Correction*](https://www.quora.com/profile/Swami-Rahasya/Physics-Paradigm-Correction). Source of the Singular Substance, pulsation, low/high-pressure Moment, and cavitation-collapse conjecture.
- **Swami Rahasya,** *Physics paradigm/ontology correction*, 24-page discussion document supplied to Wright for technical consideration, 27 October 2026; the source document and its AI-generated discussion are **not** independently adopted as verified scientific claims here.
- **J. N. Nielsen,** proposed *Topological Unified Field Theory* manuscript, [PhilArchive record](https://philarchive.org/rec/NIETTU). Listed only as a proposed comparison; no technical verification of TUFT is claimed in this work.
- **Matthew Chenoweth Wright / EFMW**, source-equation variant displayed in Eq. (1). The present note explicitly **does not** reconcile that equation with all historical EFMW coefficient and sign conventions.

---

**Publication and evidence note:** RHC-001 is a candidate theoretical note, not a peer-reviewed result, formal Lean proof, experimentally supported TOE, or confirmation of Rahasya's physical ontology. Authorship credit for the conceptual hypothesis is preserved; no endorsement by Rahasya is implied.


## Related research navigation (non-substantive links)

- [EFMW canonical review entry](https://github.com/enuminous/EFMW) · [Monolithic 102 source equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean audit](https://github.com/enuminous/Monolithic-102-Zoo-Lean4).
- [Standard Model reduction](https://github.com/enuminous/Standard-Model-Reduction) · [Higgs gauge laboratory](https://github.com/enuminous/Higgs-Gauge-Lab) · [Standard Model + EFMW physics lab](https://github.com/enuminous/EFMW-Physics-Lab).
- [Base888 quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry) · [QST-001: classical baseline and 888-state toy](https://github.com/enuminous/Quantum-Gravity/blob/main/QST-001.md) · [QST-002: quantum-geometry bridge](https://github.com/enuminous/QST/blob/main/QST-002.md).

These links provide navigation and potential comparisons; they are not proofs of equivalence or endorsements by Rahasya or other named researchers.
