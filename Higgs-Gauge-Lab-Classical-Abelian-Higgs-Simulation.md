# Higgs–Gauge Lab and the numerical simulation of a classical Abelian–Higgs field

**Matthew Chenoweth Wright**  
Monolithic LLC · 29 October 2026  
**Status:** AI-assisted computational methods preprint; not peer reviewed.  
**Application:** [Higgs–Gauge Lab](https://enuminous.github.io/Higgs-Gauge-Lab/)  
**Implementation reviewed:** [enuminous/Higgs-Gauge-Lab at 06056de](https://github.com/enuminous/Higgs-Gauge-Lab/tree/06056de25e0ad0f5306e6a5d272f983436e54126)  
**Reproduction package:** [Code, results, and instructions](https://github.com/enuminous/papers/tree/main/research/higgs-gauge-lab)

## Abstract

Higgs–Gauge Lab evolves a classical complex scalar field coupled to an Abelian gauge field on a periodic, two-dimensional spatial lattice. Its dynamics follow a gauge-covariant discretization of the Abelian–Higgs model with a quartic symmetry-breaking potential. The implementation uses a 64 × 64 grid, real-valued gauge potentials, exponential matter links, a quadratic magnetic plaquette energy, and velocity-Verlet time integration. A single HTML file provides field displays, three initial conditions, parameter controls, energy diagnostics, and a Gauss-law residual. Numerical checks execute the pinned implementation's force, integration, and diagnostic functions. At the default time step and with damping disabled, sampled relative energy deviations remain below 0.115% for the tested pulse, vortex-pair, and quench trajectories through time 45. The largest sampled Gauss-law RMS residual among those trajectories is approximately 1.4 × 10⁻¹⁵. Pulse refinement gives an observed temporal order of 2.006, and a small uniform radial oscillation agrees with the linearized Verlet frequency to a relative error of 4.3 × 10⁻⁸. These results support the implementation as a functioning classical lattice simulator within the tested regime. The model is an educational and computational analogue of Higgs-mechanism dynamics; it does not implement the Standard Model Higgs doublet, non-Abelian electroweak fields, quantum fluctuations, or dynamical fermions. Spatial convergence and empirical calibration remain separate requirements for quantitative physical use.

**Keywords:** Abelian–Higgs model; classical lattice fields; gauge covariance; symmetry breaking; numerical verification; browser simulation.

## 1 Motivation and contribution

A field animation becomes a numerical physics simulation when its displayed state evolves under specified equations, initial conditions, boundary conditions, and a reproducible update rule. Higgs–Gauge Lab meets that operational description: its images encode arrays of evolving fields, and the force calculation implements the interactions in a defined classical action. Whether the discretization is accurate, and whether the selected theory describes a particular physical system, are additional questions.

The Abelian–Higgs model is established physics. Coupling a symmetry-breaking scalar to a gauge field provides the setting for the Higgs mechanism [1]; related field equations also admit vortex solutions [2]. The contribution here is a compact implementation, an explicit account of its mathematical scope, and a reproducible set of implementation checks. No new Higgs mechanism, particle spectrum, or physical law is proposed.

The repository's interface uses the title “Standard Model: Higgs–Gauge Lab,” while its introduction and physics notes identify a classical 2+1-dimensional U(1) reduction [3]. The precise description used throughout this paper is **a classical Abelian–Higgs lattice simulator**. Here 2+1 means two spatial coordinates and one time coordinate.

## 2 Continuum model and linear mass scales

### 2.1 Fields and action

Let $\Phi$ be one complex scalar and $A_\mu$ a real Abelian gauge potential. With metric signature $(+,-,-)$, write

$$
\mathcal L=-\frac14F_{\mu\nu}F^{\mu\nu}
+(D_\mu\Phi)^*D^\mu\Phi
-\lambda\left(|\Phi|^2-\frac{v^2}{2}\right)^2,
\tag{1}
$$

$$
D_\mu=\partial_\mu-igA_\mu,
\qquad F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu.
\tag{2}
$$

The parameters satisfy $\lambda>0$ and $v>0$ in the interface. The potential is minimized at $|\Phi|=v/\sqrt2$. The symmetric configuration $\Phi=0$ has negative scalar curvature and is unstable to sufficiently long-wavelength perturbations. In temporal gauge, $A_0=0$, the scalar equation is

$$
\ddot\Phi=\sum_{i=x,y}D_iD_i\Phi
-2\lambda\left(|\Phi|^2-\frac{v^2}{2}\right)\Phi.
\tag{3}
$$

The code numerically evolves this structure and the corresponding spatial gauge dynamics. It does not merely interpolate between prescribed pictures. Its displayed values use dimensionless lattice units with spatial spacing fixed to one. There is no conversion to GeV, metres, or seconds. In particular, borrowing a numerical parameter value from four-dimensional electroweak physics would not by itself calibrate this 2+1-dimensional model.

### 2.2 Linearization about a uniform vacuum

Locally express the scalar as

$$
\Phi=\frac{v+h}{\sqrt2}\exp(i\theta/v).
\tag{4}
$$

To quadratic order, the radial fluctuation has a canonical kinetic term and potential $\lambda v^2h^2$, giving

$$
m_h^2=2\lambda v^2.
\tag{5}
$$

The scalar kinetic term contains

$$
\frac12(\partial_\mu h)^2
+\frac12(v+h)^2\left(\frac{\partial_\mu\theta}{v}-gA_\mu\right)^2.
\tag{6}
$$

For $g>0$, the gauge-invariant combination $A_\mu-\partial_\mu\theta/(gv)$ therefore has a quadratic mass coefficient

$$
m_A^2=g^2v^2.
\tag{7}
$$

These are small-fluctuation scales of the chosen classical model. The application displays $m_h=\sqrt{2\lambda}\,v$ and $m_A=gv$ directly from the parameters. Its additional display $m_f=yv/\sqrt2$ is an illustrative Yukawa formula: no fermion state or Yukawa backreaction is evolved. Section 6 independently measures a radial oscillation frequency from an evolved field; the gauge mass is not spectrally measured in this study.

“Symmetry breaking” here refers to the classical potential and expansion about a selected vacuum representative. The phase of a charged field is gauge-dependent; its colored display does not demonstrate an observable choice of absolute local phase.

## 3 Lattice equations and discrete energy

### 3.1 Spatial discretization

Sites $n=(n_x,n_y)$ form a periodic $N\times N$ square lattice with $N=64$. Denote a forward unit lattice displacement by $\hat i$, and set $a=\Delta x=1$. The stored scalar is $\Phi_n=q_n+iw_n$. The real link potentials $A_{i,n}$ define

$$
U_{i,n}=\exp(-igA_{i,n}),\qquad
\nabla_i^U\Phi_n=U_{i,n}\Phi_{n+\hat i}-\Phi_n.
\tag{8}
$$

The covariant lattice Laplacian is

$$
(\Delta_U\Phi)_n=
\sum_{i=x,y}\left[
U_{i,n}\Phi_{n+\hat i}
+U_{i,n-\hat i}^*\Phi_{n-\hat i}
-2\Phi_n\right].
\tag{9}
$$

The oriented magnetic difference around a plaquette is

$$
B_n=A_{y,n+\hat x}-A_{y,n}-A_{x,n+\hat y}+A_{x,n}.
\tag{10}
$$

Although the matter links are phases, the magnetic energy is $B_n^2/2$, not a Wilson cosine plaquette action. The gauge potentials are real, noncompact variables. This distinction identifies the discretization and prevents conflating the application with a compact lattice quantum gauge calculation. Periodic real potentials also imply $\sum_n B_n=0$ by telescoping, so this implementation does not explore a nonzero total magnetic-flux sector.

### 3.2 Hamiltonian and force calculation

Let $\Pi_n=\dot\Phi_n$ and $\mathcal E_{i,n}=\dot A_{i,n}$, using the code's canonical electric-field convention. The discrete energy reported by the application is the site average of

$$
H=\sum_n\left[
|\Pi_n|^2+\frac12\sum_i\mathcal E_{i,n}^2
+\sum_i|\nabla_i^U\Phi_n|^2+\frac12B_n^2
+\lambda\left(|\Phi_n|^2-\frac{v^2}{2}\right)^2
\right].
\tag{11}
$$

The scalar acceleration is

$$
\ddot\Phi_n=(\Delta_U\Phi)_n
-2\lambda\left(|\Phi_n|^2-\frac{v^2}{2}\right)\Phi_n.
\tag{12}
$$

Define the oriented matter-link current

$$
J_{i,n}=2g\,\operatorname{Im}
\left(\Phi_n^*U_{i,n}\Phi_{n+\hat i}\right).
\tag{13}
$$

The implemented gauge accelerations are

$$
\ddot A_{x,n}=B_{n-\hat y}-B_n+J_{x,n},
\qquad
\ddot A_{y,n}=B_n-B_{n-\hat x}+J_{y,n}.
\tag{14}
$$

The factors in these equations can be checked against Eq. (11). Because the real scalar coordinates have kinetic energy $\dot q_n^2+\dot w_n^2$, their accelerations are $-\tfrac12\partial H/\partial q_n$ and $-\tfrac12\partial H/\partial w_n$. The gauge kinetic terms instead carry a factor of one half, so their accelerations are $-\partial H/\partial A_{i,n}$. A directional finite-difference check of this relationship is included in the reproduction package.

### 3.3 Gauge covariance and Gauss law

For any periodic, time-independent site phase $\alpha_n$ and $g\ne0$, the transformation

$$
\Phi_n\mapsto e^{i\alpha_n}\Phi_n,
\quad \Pi_n\mapsto e^{i\alpha_n}\Pi_n,
\quad A_{i,n}\mapsto A_{i,n}
+\frac{\alpha_{n+\hat i}-\alpha_n}{g}
\tag{15}
$$

preserves the energy and magnetic flux while rotating the scalar force covariantly. This is the residual gauge freedom compatible with temporal gauge. The corresponding discrete Gauss residual is

$$
G_n=\sum_i(\mathcal E_{i,n}-\mathcal E_{i,n-\hat i})
-2g\,\operatorname{Im}(\Phi_n^*\Pi_n),
\qquad
G_{\rm RMS}=\sqrt{N^{-2}\sum_nG_n^2}.
\tag{16}
$$

The interface monitors $G_{\rm RMS}$ without projecting the state onto the constraint surface. Its presets initialize both scalar and gauge velocities to zero, so $G_n=0$ initially. With fixed parameters, the matter currents and the covariant scalar force have matching discrete divergences. This supports constraint preservation; the numerical tests quantify it for the reported trajectories.

## 4 Integration and user controls

The default step is $\Delta t=0.045$. For the collective field coordinates $Q$, velocities $P$, and acceleration $F(Q)$, one step is

$$
P_{n+1/2}=P_n+\frac{\Delta t}{2}F(Q_n),
\quad Q_{n+1}=Q_n+\Delta t\,P_{n+1/2},
\tag{17}
$$

$$
P_{n+1}=e^{-\gamma\Delta t}
\left[P_{n+1/2}+\frac{\Delta t}{2}F(Q_{n+1})\right].
\tag{18}
$$

When $\gamma=0$, these are velocity-Verlet updates for the discrete conservative model. The default interface value $\gamma=0.028$ adds phenomenological damping to all velocities. It removes energy intentionally and is not a term in Eq. (1). The end-of-step damping is a nonsymmetric splitting; the second-order result in Section 6 applies to the undamped integrator, not automatically to damped trajectories.

The interface's “steps per frame” control changes playback work, not $\Delta t$. Changing $\lambda$, $v$, or $g$ during a trajectory changes the model and invalidates a fixed-Hamiltonian energy comparison. In the reviewed source, slider handlers also leave the cached force unchanged until the next force evaluation, so the first half-kick after an edit uses the previous force. A change to $g$ can change the charge term in Eq. (16) without adjusting the electric field. Reproducible fixed-parameter runs should therefore set their controls before resetting the initial condition. The validation runs follow that procedure.

## 5 Initial conditions and interpretation of the displays

| Preset | Initialization | Interpretation |
|---|---|---|
| Quench | Independent small Gaussian real and imaginary scalar values with component standard deviation $0.035v/\sqrt2$; small Gaussian gauge potentials with standard deviation 0.018; zero velocities | Evolution from near the unstable symmetric configuration; random classical initial data, not quantum vacuum sampling |
| Vortex pair | Opposite phase windings near $(0.32N,0.5N)$ and $(0.68N,0.5N)$ with a product of radial $\tanh(r/3.5)$ core profiles; zero initial gauge potentials and velocities | A seeded, nonequilibrium configuration, not an exact periodic Nielsen–Olesen solution |
| Pulse | Real field $(v/\sqrt2)[1+0.5\exp(-r^2/70)]$ about the lattice center; all other arrays zero | A finite radial displacement that launches nonlinear scalar dynamics |

The amplitude display shows $|\Phi|/(v/\sqrt2)$; brightness denotes field magnitude, not a probability density or particle count. The phase display shows $\arg\Phi$ in the chosen gauge, and the value is undefined where the field vanishes. Magnetic flux and energy density provide gauge-invariant quantities for the transformations in Eq. (15). The energy view uses a changing display scale, so colors alone cannot establish absolute energy conservation.

Wavefronts and interference-like structures can arise from these classical equations. Their appearance is not sufficient to identify quantum diffraction or individual Higgs bosons. Likewise, identifying a stable vortex requires more than a phase image: an appropriate winding or flux diagnostic, relaxation study, and boundary analysis are needed. The application has no implemented vortex counter or topological certification procedure.

## 6 Numerical verification

### 6.1 Source identity and execution method

All results below refer to `index.html` at commit `06056de25e0ad0f5306e6a5d272f983436e54126`, Git blob `cf4482f77fe02086e884e6da905e472b77f3769c`. The file is 25,948 bytes, with SHA-256

```text
007d024176506541e62b9d3652014dc0c9512add78eb1664216f2b14b9b4a539
```

The companion script checks the source blob before execution. It runs the HTML's JavaScript under Node.js v24.22.1 on Linux x64, substitutes no-op DOM and canvas objects, suppresses animation scheduling, and exposes internal arrays for inspection. The functions `computeForces`, `step`, `sample`, and `reset` execute verbatim. The numerical modifications are a seeded replacement for `Math.random` and, only in refinement runs, replacement of the time-step constant. Thus the checks exercise the implementation's numerical core rather than a separately transcribed solver. They do not test browser rendering or mobile performance.

Unless specified otherwise, $N=64$, $a=1$, $\lambda=0.5$, $v=1.25$, $g=0.75$, $y=0.65$, and $\gamma=0$. The random generator is Mulberry32 with seed 20261029. The browser itself uses unseeded `Math.random`; its successive quench resets are therefore not expected to reproduce the reported trajectory.

### 6.2 Equilibrium and conservative trajectories

A uniform real vacuum with all other arrays zero remains stationary through 1,000 steps to an RMS state change of $1.84\times10^{-16}$ across the eight stored arrays. Its final energy per site is approximately $2.78\times10^{-31}$.

The following runs use $\Delta t=0.045$ and end at $T=45$ after 1,000 steps. Energy and Gauss residuals are sampled every ten steps, as well as initially. The reported maximum energy deviation is the maximum sampled $|H(t)-H(0)|/H(0)$, not a bound on every intermediate step.

| Initial condition | Initial energy per site | Final energy per site | Maximum sampled relative energy deviation | Maximum sampled Gauss RMS |
|---|---:|---:|---:|---:|
| Pulse | 0.0113284014 | 0.0113208975 | 0.11464% | 0 |
| Vortex pair | 0.0229680114 | 0.0229557798 | 0.07237% | $5.61\times10^{-16}$ |
| Seeded quench | 0.3119508960 | 0.3118878105 | 0.02371% | $1.39\times10^{-15}$ |

The pulse remains in a real-scalar sector with vanishing gauge fields, making its zero Gauss residual a limited check. The vortex and quench runs exercise nontrivial gauge dynamics and provide the stronger constraint tests. Their residuals remain near floating-point roundoff for the stated durations.

### 6.3 Temporal refinement

The deterministic pulse is evolved to the same final time at three step sizes. Define $d(Q,P)$ as the RMS difference over all entries of the eight field and velocity arrays. The observed temporal order is

$$
p=\log_2\frac{d(X_{\Delta t},X_{\Delta t/2})}
{d(X_{\Delta t/2},X_{\Delta t/4})}.
\tag{19}
$$

| Time step | Steps to $T=45$ | Final energy per site | Maximum sampled relative energy deviation |
|---|---:|---:|---:|
| 0.045 | 1,000 | 0.0113208975 | 0.11464% |
| 0.0225 | 2,000 | 0.0113265304 | 0.03386% |
| 0.01125 | 4,000 | 0.0113279339 | 0.00857% |

The successive state differences are $6.40849\times10^{-4}$ and $1.59547\times10^{-4}$, with ratio 4.01668 and $p=2.00600$. This is consistent with second-order temporal accuracy for this undamped trajectory at fixed spatial discretization. The maximum-deviation samples have different physical cadences across the three runs; the order estimate uses the common final state, not ratios of those sampled maxima. The result is not a spatial-continuum convergence test or a test across the full parameter slider range.

### 6.4 Gauge and Hamiltonian checks

A seeded quench is evolved for 100 undamped steps, then transformed with independently seeded periodic phases in $[-1,1)$. Comparing transformed and untransformed quantities gives

| Quantity | Maximum error or relative difference |
|---|---:|
| Covariantly rotated complex scalar force | $3.99\times10^{-16}$ absolute |
| Gauge force | $1.15\times10^{-15}$ absolute |
| Magnetic flux | $8.22\times10^{-16}$ absolute |
| Scalar charge density | $2.99\times10^{-17}$ absolute |
| Total energy | $1.78\times10^{-16}$ relative |

A separate directional derivative check perturbs all four coordinate arrays at a quench state after 50 steps. The central difference of energy per site is compared with the force contraction using scalar weights two and gauge weights one, as required by Eq. (11). The smallest relative discrepancy among perturbation sizes $10^{-4}$, $10^{-5}$, and $10^{-6}$ is $1.09\times10^{-8}$. This is a local consistency check on one state and direction, supplemented by the algebra above; it is not an exhaustive test of the Hamiltonian gradient.

### 6.5 Radial frequency and damping

For an additional analytic benchmark, set a uniform real field to $(v/\sqrt2)(1+10^{-4})$ with all other arrays zero. Evolve for $T=90$ at $\Delta t=0.045$ and estimate the period from linearly interpolated upward crossings of $\Phi-v/\sqrt2$. Eighteen crossings give

$$
\omega_{\rm measured}=1.2501647999,
\qquad m_h=1.25.
\tag{20}
$$

For a linear oscillator integrated by undamped Verlet, the discrete angular frequency follows from the recurrence:

$$
\omega_{\rm Verlet}=\frac{2}{\Delta t}
\arcsin\left(\frac{m_h\Delta t}{2}\right)
=1.2501648536.
\tag{21}
$$

The measured frequency differs from the continuum value by 0.01318% and from the discrete linear prediction by $4.30\times10^{-8}$ in relative terms. The latter comparison includes finite oscillation amplitude and crossing interpolation. It tests the radial potential normalization and integration, rather than measuring a physical Higgs mass.

Finally, repeating the seeded quench with the interface's default $\gamma=0.028$ decreases energy per site from 0.3119508960 to 0.1223424614 by $T=45$, a 60.78% reduction. The maximum sampled Gauss RMS is $7.74\times10^{-16}$. That energy loss is consistent with the deliberately dissipative update. Equal damping of all velocities multiplies both terms of Eq. (16) by the same factor at the damping substep, preserving an initially satisfied constraint up to rounding.

The ten implementation sanity criteria encoded in the script all pass. Their tolerances are reported in the companion README and are numerical review choices, not an independently preregistered protocol or criteria for experimental validity. Full precision outputs are retained in `results.json`.

## 7 Relationship to the Standard Model and EFMW

The Standard Model Higgs is a complex SU(2) doublet coupled to the electroweak SU(2) × U(1) gauge sector [4]. This application instead uses one complex scalar and one Abelian gauge field. The reduction preserves a useful example of scalar–gauge coupling and the classical mass-generating structure, while changing the field content and interactions.

| Feature | Implemented scope |
|---|---|
| Scalar kinetic term and quartic potential | Dynamically evolved for one complex scalar |
| Gauge dynamics | One classical noncompact Abelian gauge potential |
| Spatial structure | Two spatial dimensions with periodic boundaries |
| Standard Model Higgs doublet and weak gauge fields | Absent |
| QCD and gluon dynamics | Absent |
| Fermions and Yukawa backreaction | Absent; one formula readout only |
| Quantum fluctuations, loops, or path-integral sampling | Absent |
| Scattering cross sections and particle production | Not calculated |
| Experimental parameter calibration | Not provided |

Within Monolithic's broader research program, the lab supplies an established-theory baseline. The inspected evolution law contains no additional EFMW-specific force, recursive memory term, informational tensor, or quantum-gravity dynamics. Cross-links to other research repositories do not add such terms to the solver. Any future EFMW modification would require its own explicit action or evolution rule and a comparison against this baseline.

## 8 Limits and next validation steps

The numerical results establish bounded evidence about a fixed implementation. The most useful next validation is spatial refinement: introduce a variable lattice spacing, preserve physical box size and initial-condition widths, and compare gauge-invariant observables across resolutions. Merely increasing $N$ while retaining $a=1$ changes the box size and is not that test.

Further work should measure transverse and longitudinal gauge-mode frequencies against the discrete dispersion relation, test longer trajectories and the accessible parameter range, and quantify finite-volume effects. A genuine vortex benchmark should compare relaxed solutions, core profiles, winding, flux, and energy against a specified reference problem. The unsymmetrized damping step deserves a separate convergence study if dissipative trajectories are used quantitatively.

Two practical refinements would strengthen reproducibility: a user-selectable random seed and a force refresh after physical-parameter edits. Parameter changes that affect the constraint should also have a defined initialization or constraint-handling policy. None of these changes is silently included in the results above; the reported source remains the pinned version.

A faithful electroweak classical extension would require the Higgs doublet and SU(2) × U(1) gauge fields with consistent constraints. Quantizing that system, adding dynamical fermions, and including QCD are additional projects, rather than consequences of relabeling this interface.

## 9 Conclusion

Higgs–Gauge Lab implements the evolution of a defined classical Abelian–Higgs lattice system. Its numerical core passes the reported equilibrium, energy, gauge-covariance, constraint, force-consistency, temporal-refinement, and radial-frequency checks. The computed patterns therefore have a traceable mathematical basis in the implemented field equations. The supported claim is a functioning classical simulator within the tested settings; quantitative continuum prediction and physical Standard Model simulation require additional validation and field content.

## Reproducibility and authorship

The [companion directory](https://github.com/enuminous/papers/tree/main/research/higgs-gauge-lab) supplies the executable verification script, complete numerical outputs, source hashes, and exact commands. Results derive from synthetic initial conditions and no experimental dataset. The paper, derivations, and verification script were prepared with OpenAI assistance at Matthew Chenoweth Wright's direction. Executed software checks are reported explicitly; no independent replication, peer review, or external endorsement is implied.

## References

1. P. W. Higgs, “Broken Symmetries and the Masses of Gauge Bosons,” *Physical Review Letters* **13**, 508–509 (1964). [doi:10.1103/PhysRevLett.13.508](https://doi.org/10.1103/PhysRevLett.13.508).
2. H. B. Nielsen and P. Olesen, “Vortex-line models for dual strings,” *Nuclear Physics B* **61**, 45–61 (1973). [doi:10.1016/0550-3213(73)90350-7](https://doi.org/10.1016/0550-3213(73)90350-7).
3. enuminous, *Higgs–Gauge Lab*, implementation at commit `06056de25e0ad0f5306e6a5d272f983436e54126`: [index.html](https://github.com/enuminous/Higgs-Gauge-Lab/blob/06056de25e0ad0f5306e6a5d272f983436e54126/index.html), [PHYSICS.md](https://github.com/enuminous/Higgs-Gauge-Lab/blob/06056de25e0ad0f5306e6a5d272f983436e54126/PHYSICS.md), and [README.md](https://github.com/enuminous/Higgs-Gauge-Lab/blob/06056de25e0ad0f5306e6a5d272f983436e54126/README.md). Inspected 29 October 2026.
4. S. Floerchinger, *Quantum Field Theory 2*, lecture 16, sections on the Standard Model gauge group and field representations, Friedrich Schiller University Jena. [Author's lecture notes](https://www.tpi.uni-jena.de/~floerchinger/qft2/lecture16/). Accessed 29 October 2026.
