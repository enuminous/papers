# EFMW-RP-001: Detecting Relaxation Without Identifying Its Origin

## A synthetic bubble-response benchmark and an exact Maxwell equivalence

**Matthew Chenoweth Wright**  
Monolithic LLC · 29 October 2026  
**Status:** AI-assisted computational research preprint; all observations synthetic; not peer reviewed.  
**Study:** EFMW-RP-001, protocol version 1.0.  
**Companion:** [Bubble Dynamics Test: source, data, and browser laboratory](https://github.com/enuminous/Bubble-Dynamics-Test/tree/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4).

## Abstract

A pressure-driven bubble provides a concrete setting in which to distinguish the detection of temporal relaxation from the identification of a proposed physical mechanism. We linearize the Rayleigh–Plesset equation about an existing spherical bubble and append a passive, single-exponential stress memory. An internally frozen computational protocol compares this model with a fitted constant-stiffness, constant-damping baseline using complex radius-to-pressure responses at 61 frequencies between 2 and 200 kHz. Five hundred null simulations calibrate a training-fit threshold; separate sets of 250 null and 250 injected-memory simulations evaluate a three-part detection rule. The rule detects relaxation in 223 of 250 injected trials, or 89.2%, and in none of the 250 null trials. It therefore fails its prespecified 90% positive-detection target, despite a median 61.4% reduction in held-out prediction error. Independent time integration agrees with the analytic transfer function to a maximum relative error of approximately 2.05 × 10⁻¹¹. The decisive interpretive result is algebraic: the appended memory is exactly a conventional Maxwell branch with a viscous background. Radius–pressure frequency response alone cannot distinguish those two descriptions, even with noiseless measurements. A lumped gas-relaxation surrogate provides a second exact algebraic ambiguity. The work establishes a reproducible synthetic benchmark and a structural limit on mechanism identification. It does not establish a physical EFMW or TUFT mechanism, cavitation-driven matter formation, or a universal Stoney-scale pulsation.

**Keywords:** bubble dynamics; Rayleigh–Plesset equation; viscoelastic relaxation; Maxwell model; structural identifiability; synthetic benchmark; negative results; EFMW.

## 1. Motivation and the question actually tested

The pressure-cycle proposal motivating this work associates an underlying pulsating medium with recurring low-pressure intervals, localized cavitation, and an accumulated history of vortex or shear structure. RHC-001 previously translated part of that proposal into a candidate scalar closure, pressure gate, and occupancy dynamics [1]. That note credits Swami Rahasya's originating pressure/cavitation conjecture and treats its proposed relation to J. N. Nielsen's TUFT as unresolved. This paper reports a narrower computational continuation. Neither Rahasya nor Nielsen is represented as having authored, reviewed, or endorsed the present model or results.

The suggested next test was to insert an oscillatory pressure into a bubble equation and examine amplitude and phase around $\omega\tau\sim1$. To make that instruction executable, a bubble state, constitutive law, relaxation time, drive, noise model, and decision rule must be specified. Here those choices are analyst-selected. They are not derived predictions of EFMW, TUFT, or the proposed substrate.

Three questions must remain separate:

1. **Synthetic detectability:** can this analysis detect the inserted relaxation against a fitted constant-coefficient baseline at the declared parameter and noise setting?
2. **Mechanism identifiability:** can the resulting observable distinguish the selected memory law from conventional constitutive physics?
3. **Physical validity:** does a corresponding effect occur in measurements, with an independently derived signature attributable to the proposed theory?

Only the first two questions are answered here. The third requires empirical data and additional theory. The study concerns small oscillations of an already existing bubble. It does not simulate nucleation, collapse, particle creation, a pressure-threshold gate, or two alternating physical regimes.

## 2. From the pressure proposal to a limited continuum model

### 2.1 Constitutive qualifications

The motivating identification $E=\rho c^2$ needs a geometric qualification. For a slender elastic rod in the appropriate long-wavelength extensional limit, the wave speed involves Young's modulus $E$. In a three-dimensional isotropic elastic medium, the longitudinal speed instead satisfies

$$
c_L^2=\frac{K+4G/3}{\rho},
$$

where $K$ and $G$ are the bulk and shear moduli [2]. An irrotational displacement field does not generally replace this longitudinal modulus with $E$. A specified wave speed also does not set the oscillatory stress amplitude: a strain amplitude or a driving-energy prescription is additionally required.

Using the tension-positive convention for Cauchy stress $\boldsymbol{\sigma}$, the mechanical mean pressure is $-\operatorname{tr}\boldsymbol{\sigma}/3$. Identifying that quantity with thermodynamic pressure requires a constitutive setting. Likewise, $p'=-\rho\partial_t\phi$ is a linear acoustic relation for a suitably defined velocity potential with $\mathbf v=\nabla\phi$ [3]. It does not by itself construct a vortex field, establish a topological coupling, or reconcile the units and source terms of a different EFMW scalar equation. Those mappings remain separate derivation obligations.

The present benchmark therefore does not assign the test medium the light speed, a fundamental Young's modulus, or a field-to-pressure map. It uses an effective incompressible bubble model and an externally prescribed pressure. This is a defined continuum comparison, not a completed constitutive description of the proposed Singular Substance.

### 2.2 Equilibrium and linearization

For a spherical bubble of radius $R(t)$ in an unbounded incompressible Newtonian medium, use the Rayleigh–Plesset balance [4]

$$
\rho\left(R\ddot R+\frac32\dot R^2\right)
=p_B(R)-p_\infty(t)-\frac{2\sigma_s}{R}
-\frac{4\eta_{\mathrm{eff}}\dot R}{R},
\tag{1}
$$

with surface tension $\sigma_s$, effective viscosity $\eta_{\mathrm{eff}}$, and the selected polytropic closure

$$
p_B(R)=p_v+p_{g0}\left(\frac{R_0}{R}\right)^{3\kappa},
\qquad p_\infty(t)=P_0+A\cos\omega t.
\tag{2}
$$

Equilibrium requires $p_{g0}=P_0-p_v+2\sigma_s/R_0$. Set $x=(R-R_0)/R_0$ and retain first-order terms. The inertial term becomes $\rho R_0^2\ddot x$, the gas pressure changes by $-3\kappa p_{g0}x$, and the surface-tension contribution changes by $+2\sigma_s x/R_0$. Thus

$$
m\ddot x+b\dot x+kx=-p_d(t),
\tag{3}
$$

$$
m=\rho R_0^2,\qquad b=4\eta_{\mathrm{eff}},\qquad
k=3\kappa p_{g0}-\frac{2\sigma_s}{R_0},\qquad
p_d(t)=A\cos\omega t.
\tag{4}
$$

Here $x$ is dimensionless; $m$, $b$, and $k$ have units Pa·s², Pa·s, and Pa. The coefficient $m$ is an inertia in the pressure-normalized equation, not a mass in kilograms. The constant effective viscosity and polytropic exponent are simplifying closures. Full gas heat transport, acoustic radiation, compressibility, mass transfer, and nonspherical motion are absent.

### 2.3 Selected memory extension and passivity

Append a stress-like state $q$, measured in Pa:

$$
m\ddot x+b\dot x+kx+q=-p_d(t),
\qquad
\tau\dot q+q=\Delta k\,\tau\dot x,
\qquad \Delta k=4G_m.
\tag{5}
$$

The parameters $G_m>0$ and $\tau>0$ specify the strength and relaxation time of the chosen memory. The exact history form is

$$
q(t)=q(0)e^{-t/\tau}
+\Delta k\int_0^t e^{-(t-s)/\tau}\dot x(s)\,ds.
\tag{6}
$$

Thus the state is a sufficient statistic for an exponentially fading history of radial strain rate. It does not encode an arbitrary cumulative vortex topology. A convolution-only representation removes the explicit state variable but retains the same memory through its history and initial condition.

**Proposition 1 — passivity of the selected linear system.** For positive $m,k,b,\Delta k,\tau$, define the pressure-normalized storage function

$$
\mathcal E=\frac12m\dot x^2+\frac12kx^2+\frac{q^2}{2\Delta k}.
\tag{7}
$$

Differentiation and substitution of Eq. (5) give

$$
\dot{\mathcal E}
=-b\dot x^2-\frac{q^2}{\Delta k\tau}-p_d\dot x.
\tag{8}
$$

The first two terms are nonpositive. The last is the prescribed pressure's power input in this normalization. This proves passive relaxation, rather than autonomous generation of a coherent drive. Multiplication by $4\pi R_0^3$ gives the associated leading-order radial energy and pressure-work normalization in joules. For $\Delta k=0$, remove $q$ and its storage term to recover the baseline. These are conditional mathematical statements about Eq. (5).

### 2.4 Transfer function and the relaxation crossover

With phasors proportional to $e^{i\omega t}$,

$$
H_1(\omega):=\frac{\hat x}{\hat p_d}
=-\left[k-m\omega^2+ib\omega
+\Delta k\frac{i\omega\tau}{1+i\omega\tau}\right]^{-1}.
\tag{9}
$$

The baseline $H_0$ sets $\Delta k=0$. Both have units Pa⁻¹. Radius amplitude is $R_0A|H|$ and its phase relative to the pressure is $\arg H$ under this convention. At low frequency, positive pressure compresses the bubble, explaining the phase near 180°.

Writing $z=\omega\tau$, the added dynamic stiffness is

$$
\Delta k\frac{iz}{1+iz}
=\Delta k\frac{z^2}{1+z^2}
+i\Delta k\frac{z}{1+z^2}.
\tag{10}
$$

At $z\ll1$ it acts approximately as an additional damping coefficient $\Delta k\tau$; at $z\gg1$ it approaches an elastic increment $\Delta k$. At $z=1$, its real and imaginary parts both equal $\Delta k/2$. This is a smooth frequency crossover. It is not a switch between low- and high-pressure halves of a cycle, and it does not generally place the total bubble response at a 45° phase. Inertia and the baseline coefficients also enter Eq. (9).

## 3. Structural identifiability and established counterparts

**Proposition 2 — exact conventional counterpart.** A linear Maxwell branch with modulus $G_m$ and relaxation time $\tau$ has complex shear modulus

$$
G^*(\omega)=G_m\frac{i\omega\tau}{1+i\omega\tau}.
\tag{11}
$$

For the small radial perturbation used here, its restoring-pressure contribution is $4G^*\hat x$. Substitution into the bubble balance gives $4G^*=\Delta k\,i\omega\tau/(1+i\omega\tau)$, precisely the last term in Eq. (9). The viscous background $b\dot x$ remains present. Equivalently, the Maxwell stress obeys the same state equation as $q$ in Eq. (5).

Consequently, the two descriptions produce identical steady-state radius–pressure responses at every frequency for matched parameters. Their linear time-domain responses also coincide for matched initial states. With the same measurement-noise model, their observable data distributions are identical. No test based solely on this observable can assign different physical origins to these identical laws. This is structural non-identifiability of the interpretation, not merely an insufficient sample size or a weak instrument.

Maxwell and Jeffreys constitutive models were already applied to bubble dynamics by Allen and Roy [5]. Warnez and Johnsen developed a broader framework including relaxation, compressibility, and thermal effects [6]. The present small-amplitude equation is not a replication of those full finite-amplitude calculations. Its overlap is **equivalent/reparameterized conventional linear viscoelasticity**; no novelty is claimed for the response law or the fitting method.

A second construction illustrates why even the location of an inferred relaxation requires care. Define a lumped, frequency-dependent gas exponent

$$
\kappa^*(\omega)=\kappa+
\frac{\Delta k}{3p_{g0}}\frac{i\omega\tau}{1+i\omega\tau}.
\tag{12}
$$

Then $3p_{g0}\kappa^*(\omega)-2\sigma_s/R_0$ reproduces the same complex stiffness. For the benchmark values, its limiting exponent rises from 1.2 to 1.330879. This is an algebraic surrogate, not an exact solution of gas heat diffusion or evidence for that thermal mechanism. Actual frequency-dependent gas stiffness and thermal damping require the relevant transport problem; they are established concerns in bubble acoustics [3].

## 4. Internally frozen computational protocol

### 4.1 Parameters and simulated observations

The executable protocol was written and fingerprinted before the original run. Its SHA256 record is an internal freeze, not an externally timestamped preregistration. The paper and the browser interface were prepared after the results. No signal strength, noise, frequency split, seed, or acceptance threshold was changed in response to the observed outcome.

| Quantity | Value |
|---|---:|
| Density $\rho$ | 998 kg·m⁻³ |
| Equilibrium radius $R_0$ | 50 µm |
| Ambient pressure $P_0$ | 101,325 Pa |
| Vapor pressure $p_v$ | 2,330 Pa |
| Surface tension $\sigma_s$ | 0.072 N·m⁻¹ |
| Polytropic exponent $\kappa$ | 1.2 |
| Effective viscosity $\eta_{\mathrm{eff}}$ | 0.010 Pa·s |
| Injected memory modulus $G_m$ | 10,000 Pa |
| Injected relaxation time $\tau$ | 8 µs |
| Pressure amplitude $A$ | 20 Pa |

These are illustrative effective-medium parameters, not measured properties of an identified specimen. They give $p_{g0}=101875$ Pa, $m=2.495\times10^{-6}$ Pa·s², $k=363870$ Pa, $b=0.04$ Pa·s, and $\Delta k=40000$ Pa. The undamped baseline natural frequency is $\sqrt{k/m}/(2\pi)=60.7796$ kHz. The relaxation corner is $1/(2\pi\tau)=19.8944$ kHz. The natural frequency is not identical to the damped response peak.

Each trial contains 61 geometrically spaced frequencies from 2 to 200 kHz. Even zero-based indices supply 31 training frequencies; odd indices supply 30 held-out frequencies. Independent zero-mean Gaussian errors with standard deviation $\sigma_H=5\times10^{-8}$ Pa⁻¹ are added separately to the real and imaginary parts of $H$. This gives 62 training and 60 held-out real-valued residual components.

The noise level is assumed known and constant in transfer-function units. The drive amplitude enters the small-amplitude and nonlinear checks; the noise model does not derive a pressure-dependent experimental signal-to-noise ratio. The results therefore do not determine instrument sensitivity or required laboratory drive strength.

### 4.2 Fitting and calibration

The baseline fits $k$ and $b$; the extended model fits $k,b,\Delta k,\tau$. Inertia is fixed to its synthetic generating value. With $k_0$ the nominal stiffness and $\omega_0=\sqrt{k_0/m}$, the bounds are

$$
0.5\le k/k_0\le2,\quad
10^{-5}\le b\omega_0/k_0\le1.5,\quad
0\le\Delta k/k_0\le1,\quad
10^{-7}\le\tau\le10^{-3}\ \mathrm{s}.
\tag{13}
$$

Bounded nonlinear least squares uses an analytic Jacobian. The memory fit starts at three relaxation times, 1, 10, and 100 µs, and retains the best converged result together with an exact nested-null fallback. The baseline starts at its nominal generating parameters. Neither model fits held-out observations.

Define $\chi^2$ as the sum of squared training residuals normalized by $\sigma_H$, including both quadratures. For a set of $N$ complex held-out responses, define

$$
\mathrm{WRMSE}
=\left[\frac{1}{2N}\sum_{j=1}^{N}
\frac{|\widehat H_j-H_j^{\mathrm{obs}}|^2}{\sigma_H^2}\right]^{1/2}.
\tag{14}
$$

Five hundred no-memory trials calibrate the 95th percentile of $\Delta\chi^2=\chi_0^2-\chi_1^2$, using the higher order statistic. The resulting cutoff is **4.605608162369428**. This simulation-based calibration avoids assuming the regular chi-square likelihood-ratio law: $\Delta k=0$ is a boundary and $\tau$ is unidentified there.

Independent pseudorandom streams generate calibration, null-test, and memory-test data, using seeds 2026102901, 2026102902, and 2026102903. The two evaluation cohorts contain 250 trials each. Independence here refers to simulated noise streams and the fitting split; all cohorts share the same assumed model, design, and noise law.

### 4.3 Frozen decision rule

A trial counts as a detection only when all three conditions hold:

1. Training $\Delta\chi^2>4.605608162369428$.
2. Held-out improvement $1-\mathrm{WRMSE}_1/\mathrm{WRMSE}_0\ge0.20$.
3. Memory-model held-out $\mathrm{WRMSE}_1\le1.5$.

The algorithm-level acceptance criterion is a null detection fraction no greater than 5% and an injected-memory detection fraction at least 90%. This criterion addresses synthetic performance at one setting. It is neither a test of physical truth nor a requirement inferred after examining the trials. The interleaved held-out design assesses interpolation within the same frequency band, not extrapolation or transfer to another material.

## 5. Results

### 5.1 Detection, prediction, and parameter recovery

| Outcome | Independent null | Injected memory |
|---|---:|---:|
| Trials | 250 | 250 |
| Detections | 0 | 223 |
| Detection fraction | 0.0% | 89.2% |
| 95% Wilson interval | 0–1.51% | 84.74–92.47% |
| Median held-out WRMSE, baseline | 1.000 | 3.081 |
| Median held-out WRMSE, memory | 1.027 | 1.178 |
| Median held-out error reduction | −0.76% | 61.45% |

The independent null cohort meets its acceptance condition. The injected cohort misses the frozen 90% target, so the overall algorithm check is **FAIL**. The 95% interval includes 90%; the procedural failure is not evidence that the underlying detection probability is definitively below 90%. Likewise, 0/250 null detections does not establish a zero false-positive probability.

All 250 injected trials pass the training improvement and 20% held-out gain conditions. The 27 rejected trials fail the held-out adequacy condition, with WRMSE above 1.5. Since these data were generated by the candidate itself, those failures do not independently demonstrate missing physics. They describe the behavior of the fixed fitting and decision procedure under noise and finite training data. The threshold was not relaxed after inspection.

Across all 250 injected trials, including rejected ones, the fitted relaxation time has median **8.036 µs**, with central 95% empirical quantiles **6.830–9.510 µs** around the injected 8 µs value. The fitted modulus has median **10.060 kPa**, with corresponding quantiles **9.165–10.916 kPa**. These are Monte Carlo recovery distributions, not uncertainty intervals for a measured physical medium. Fitted relaxation times under the null have no identified physical interpretation.

![Synthetic amplitude, phase, held-out error improvement, and relaxation-time recovery for EFMW-RP-001](https://raw.githubusercontent.com/enuminous/Bubble-Dynamics-Test/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/results/EFMW-RP-001-results.png)

**Figure 1.** Recorded output of the frozen study. Panels A and B show fits and held-out predictions for the first injected-memory trial, selected by replicate index rather than favorable performance. The baseline coefficients are fitted, not held at their generating values. Panels C and D use all 250 independent trials in each applicable condition. The 20% line in panel C is only one of the three detection conditions; crossing it is not sufficient for detection. Every plotted observation is simulated.

### 5.2 Numerical verification and optimization accounting

Independent time integration of the linear state equations uses DOP853, discards decaying transients, and projects the final 12 cycles onto sine and cosine. It checks both baseline and memory responses at 5 kHz, 20 kHz, the nominal natural frequency, and 150 kHz. A separate integration of nonlinear Newtonian Eq. (1) checks its first harmonic against the linear baseline at the same frequencies.

| Check | Recorded maximum or outcome | Frozen criterion |
|---|---:|---:|
| Linear ODE versus analytic transfer, relative complex error | $2.05\times10^{-11}$ | $<10^{-5}$ |
| Nonlinear Newtonian RP first harmonic versus linear baseline | $1.64\times10^{-5}$ | $<0.01$ |
| Fractional radius amplitude, maximum across both models on a dense grid | 0.00130954 (0.131%) | $<0.01$ |
| Maxwell versus selected memory, relative discrepancy | $5.28\times10^{-15}$ | $<10^{-12}$ |
| Lumped gas surrogate versus selected memory, relative discrepancy | $7.77\times10^{-15}$ | $<10^{-12}$ |

The numerical checks pass. The equality results rest on algebra; their floating-point residuals only check implementation. The nonlinear integration verifies the Newtonian baseline, not a finite-amplitude Maxwell model or a cavitation threshold. The grid amplitude check is a numerical sample, not a certified continuum maximum. The time-domain calculation is a separate numerical formulation within the same workflow, not replication by an independent laboratory or research group.

Of 3,000 memory optimizer starts, 47 did not converge: 32 in calibration, 15 in the independent null cohort, and none in the injected cohort. At most two of the three starts failed in any trial. Every trial retained at least one converged memory start, and no trial was excluded. The nested fallback prevents a worse training fit than the baseline; it does not prove global optimization. A post-run reporting audit also compared the analytic Jacobian with central finite differences, obtaining relative maximum discrepancy $5.21\times10^{-11}$. That supplementary check was not part of the pre-execution evidence.

## 6. Interactive laboratory and its evidential role

The companion [`index.html`](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/index.html) implements the analytic transfer function as a self-contained browser laboratory. Readers can vary radius, drive pressure, viscosity, memory strength, and relaxation time; inspect amplitude and phase; locate a response peak; overlay the exact Maxwell counterpart; and export spectra. A separate trial inspector displays the recorded outcomes and the three frozen criteria.

The interface distinguishes live exploration from the stored study. Its response curves compare models at shared current physical coefficients; the original detector instead refits baseline and memory coefficients on training data. Moving controls does not rerun the 1,000-trial protocol, revise its results, or establish power at a new setting. The animated bubble uses amplified displacement and slowed display time. It is a schematic of a harmonic response, not an observation of cavitation or an integration at the physical acoustic frequency.

The browser implementation was checked against 120 NumPy complex-response evaluations across parameter settings, with maximum relative discrepancy about $1.71\times10^{-15}$. Desktop and narrow-screen interaction checks were also performed. These are software verification results, separate from the frozen scientific acceptance criterion.

## 7. Interpretation, limitations, and proof obligations

### 7.1 What the result supports

The model demonstrates that one passive relaxation branch can produce a frequency-dependent amplitude and phase response that a fitted constant-coefficient baseline cannot fully absorb at the selected synthetic noise level. Its time constant can be recovered with finite dispersion under those same generating assumptions. Detection is therefore **supported but incomplete** under the frozen target: 223/250 successes are informative, while the acceptance check still fails.

The proposed specificity of this response is **rejected for this model and observable**. The same law is conventional Maxwell viscoelasticity. An EFMW interpretation attached to the identical transfer function adds no distinguishing prediction. This conclusion does not reject every possible EFMW or TUFT model; it rejects uniqueness of the particular observable law tested here.

### 7.2 What was not tested

The suggested fundamental period is of order the Stoney time,

$$
t_S=\sqrt{\frac{G_Ne^2}{4\pi\epsilon_0c^6}}
\approx4.6\times10^{-45}\ \mathrm{s}.
\tag{15}
$$

The benchmark drive periods are 5–500 µs. No coarse-graining derivation, frequency-conversion mechanism, energy budget, or coupling connects those periods to $t_S$. The numerical pressure input is an ordinary prescribed sinusoid; it is not an integration of a universal Stoney-scale pulsation. Applying a continuum bubble equation at the proposed fundamental frequency would itself require a validity argument.

Nor does the selected linear law contain a low-pressure threshold, an occupancy variable, topological vortex invariants, or a different evolution rule during the high-pressure half-cycle. Its smooth crossover near $\omega\tau=1$ therefore cannot validate the proposed two-regime ontology. The relation between a gas cavity in this model and any claim about elementary matter is unspecified.

Even an ordinary laboratory relaxation measurement would require a stronger conventional baseline than the one used here. Gas thermal response, acoustic radiation, compressibility, boundaries, surface rheology, and nonspherical motion can affect the observed response. Unknown inertia, frequency-dependent or correlated noise, and parameter drift would further change inference. The assumed precision and known coefficients are not independent calibrations. Only one generating parameter set and one noise law were studied.

### 7.3 Audit of claims and independence

The following operations implement the consistency and anti-circularity requirements of the EFMW Zoo analysis workflow. No named animal operation or formal proof certificate is invented for this study.

| Operation | Inputs and criterion | Output and evidence status |
|---|---|---|
| Dimensional and energy check | Eqs. (3)–(8); consistent pressure units and nonnegative dissipation | **Demonstrated:** passive linear closure under stated assumptions |
| Numerical cross-check | Independent time integration; frozen discrepancies and amplitude bounds | **Demonstrated computationally:** checks pass at tested points |
| Null calibration and prediction test | Fixed seeds, split, noise, bounds, and three-part rule | **Rejected acceptance:** 89.2% falls below the declared 90% target |
| Conventional equivalence check | Equality with a Maxwell branch for matched parameters | **Demonstrated:** exact equivalence; uniqueness rejected |
| Physical identification | Measured data and an independently derived distinguishing prediction | **Unresolved:** neither supplied |
| Pressure-cycle and topology bridge | Specified threshold dynamics, field map, and scale connection | **Hypothesis/postulate:** outside the executed model |

The principal anti-circularity constraint is that injecting a chosen response and recovering it cannot establish its existence in nature. The calibration and held-out split control aspects of the synthetic analysis; they do not remove dependence on the generating assumptions. Similarly, numerical agreement between equivalent descriptions cannot turn either interpretation into independent evidence for its own premises.

## 8. A falsifiable next step

A practical next stage has two distinct goals. First, assess conventional parameter inference in a physically characterized bubble system, with independently measured radius, pressure transfer, rheology, gas properties, temperature, surface tension, and noise covariance. The baseline should include the thermal and acoustic effects justified for that apparatus. A study seeking a practical detector could freeze a new protocol requiring at most 5% null detections and at least 90% positive-control detections over a declared parameter/noise domain. Those are proposed future criteria, not a reclassification of the present failed check.

Second, a theory-specific test requires a quantitative prediction that differs from every allowed conventional counterpart. The additional observable, parameter restrictions, or coupling must be derived and frozen before outcomes are inspected. A proposed success rule is a prespecified practical prediction gain on blinded held-out measurements, calibrated against the full conventional null and reproduced on an independent acquisition; failure is absence of that gain, failed adequacy, or reproduction by an allowed conventional model. Numerical thresholds and sample size must be set from independent calibration before data collection, not selected from favorable results.

For the exact Maxwell-equivalent law in this paper, collecting more of the same radius–pressure response cannot resolve the interpretation. A useful next derivation must first break that degeneracy. A sharper measurement of an identical prediction would only characterize the common response more precisely.

## 9. Conclusion

EFMW-RP-001 turns a proposed memory test into an explicit, reproducible synthetic benchmark. It obtains a substantial prediction improvement over a fitted constant-coefficient baseline, while failing its own 90% positive-detection acceptance condition. More decisively, the selected exponential memory has an exact conventional Maxwell counterpart. The numerical work verifies a chosen passive response and documents a limit of mechanism identification. Physical validation of the proposed pressure-cycle substrate, its topological interpretation, and its fundamental timescale remains unresolved.

## Data, software, and reproducibility

The source and results are pinned to `enuminous/Bubble-Dynamics-Test` commit **`1f47d523a3f1e6fa2e732eb493f54d8c4658cac4`**. That revision adds the browser laboratory to the preceding study snapshot; the original protocol and Python analysis are unchanged. The following links are immutable revision references:

- [Frozen protocol](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/protocol.json) and [executable analysis](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/run_test.py).
- [Machine-readable results](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/results/results.json) and [post-run audit](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/results/postrun_audit.json).
- [All 1,000 trial rows](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/results/trials.csv), [500 independent synthetic spectra](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/results/synthetic_spectra.csv), and [first-trial predictions](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/results/representative_predictions.csv).
- [ODE verification table](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/results/ode_verification.csv), [original report](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/results/report.html), and [reporting finalizer](https://github.com/enuminous/Bubble-Dynamics-Test/blob/1f47d523a3f1e6fa2e732eb493f54d8c4658cac4/finalize_report.py).

The run used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. To reproduce in a separate output directory:

```bash
git clone https://github.com/enuminous/Bubble-Dynamics-Test.git
cd Bubble-Dynamics-Test
git checkout 1f47d523a3f1e6fa2e732eb493f54d8c4658cac4
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python run_test.py --output replication
```

The archived `results/report.html` includes reporting-only clarifications from `finalize_report.py`. That script targets the default `results` directory, so it should not be assumed to amend a custom `replication` directory. It does not refit models or change thresholds. Numerical reruns should be compared within sensible floating-point tolerances rather than requiring identical execution time.

Protocol SHA256:

```text
83880cce64bca739711aff4277dfc59b9c387b1138592fa97c6dd7b8e134afa0
```

Analysis-source SHA256 (`run_test.py`):

```text
fc3c21480b66a15ed9b29d0014e4afbd7c8ab0091ac4e0fcb7655820d484a627
```

**AI assistance and provenance.** Codex assisted with formulation, coding, numerical execution, checks, interface development, and manuscript drafting. This paper reports the recorded computational workflow; it does not claim independent human replication or peer review. No laboratory measurements were collected, and no new empirical dataset is represented as part of the work.

## References

1. Wright, M. C. (2026). *RHC-001: An EFMW-Based Candidate Formalization of Rahasya's Pulsating-Substrate Pressure Cycle*. Candidate-model research note, 27 October 2026. [Pinned repository text](https://github.com/enuminous/papers/blob/303826f1276ca7207061badb7d16f1dbdb01c222/RHC-001-EFMW-Rahasya-Pressure-Cycle-Formalization.md). This is contextual provenance, not independent validation.
2. Fitzpatrick, R. (2016). *Fluid Mechanics*, Cartesian Tensors, Exercises, exercise 7. University of Texas at Austin. [Author's teaching text](https://farside.ph.utexas.edu/teaching/336L/Fluid/node253.html).
3. Prosperetti, A. (1977). Thermal effects and damping mechanisms in the forced radial oscillations of gas bubbles in liquids. *Journal of the Acoustical Society of America*, **61**, 17–27. [doi:10.1121/1.381252](https://doi.org/10.1121/1.381252). [Author-hosted full text](https://pages.jh.edu/aprospe1/publications/PapersPublished/GasBubbles/JASA_Thermal_77.pdf).
4. Brennen, C. E. (1995). *Cavitation and Bubble Dynamics*. Oxford University Press. [Chapter 2: spherical bubble dynamics](https://media.library.caltech.edu/CaltechBOOK:1995.001/chap2.htm); [Chapter 4: bubble oscillations](https://media.library.caltech.edu/CaltechBOOK:1995.001/chap4.htm).
5. Allen, J. S., and Roy, R. A. (2000). Dynamics of gas bubbles in viscoelastic fluids. I. Linear viscoelasticity. *Journal of the Acoustical Society of America*, **107**, 3167–3178. [doi:10.1121/1.429344](https://doi.org/10.1121/1.429344).
6. Warnez, M. T., and Johnsen, E. (2015). Numerical modeling of bubble dynamics in viscoelastic media with relaxation. *Physics of Fluids*, **27**, 063103. [doi:10.1063/1.4922598](https://doi.org/10.1063/1.4922598). [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4474959/).
