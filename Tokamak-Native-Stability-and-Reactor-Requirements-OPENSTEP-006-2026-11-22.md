# Tokamak native stability and reactor requirements: OPENSTEP-006

**Matthew Chenoweth Wright / Monolithic LLC · 22 November 2026**

Computational follow-up to the OPENSTEP-001–005 interim report. Evidence frozen at [Tokamak commit 7f2842f3086f](https://github.com/enuminous/Tokamak/commit/7f2842f3086fae73ad51c1b784830862c314658f).

**Finding: the computational assessment has advanced; a working reactor has not been established.** A native axisymmetric plasma–wall calculation reproduces a published DIII-D eigenvalue, survives a two-grid comparison, and obeys a resistivity scaling control. Its time-domain growth comparison fails the frozen agreement limit. Prescribed-current feedback suppresses one small displacement over a short interval, but the tested delays spoil that result. Independent thermal-reactivity integration recovers the historical STEP scenario's alpha power within 0.73%; a reduced energy model then exposes thermal instability. Exhaust, fuel and electricity calculations quantify requirements under stated assumptions.

The result is **PARTIAL**, with **23 PASS and 4 FAIL numerical/model-comparison checks**, plus **340 passing integrity checks**. Those counts have different meanings and must not be presented as reactor-validation statistics. There are also two retained pre-physics temporary-directory failures and the retained initial stale-axis diagnostic. Negative physical scenarios are tabulated, not counted as software failures.

This package extends [OPENSTEP-005](https://github.com/enuminous/Tokamak/blob/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-005/README.md) and the [001–005 interim report](https://github.com/enuminous/papers/blob/10c40a06860eb99681321f0b9b6419e4a093f0cc/Tokamak-Interim-Report-OPENSTEP-001-005-2026-11-21.md). All 241 historical manifest entries checked across OPENSTEP-003–005 remain unchanged. No earlier design-selection failure is reversed.

## Scope and source separation

Three distinct numerical objects are involved:

| Object | Source | What it supports |
|---|---|---|
| DIII-D reference device model | OpenFUSIONToolkit 26.9, commit `73d8eb09bce0a4f4c56b88f13fcf36f951c53e91`; EFIT `g192185.02440`, vessel polygons/resistivities and coils | Testing a native axisymmetric plasma/wall calculation and prescribed-current response |
| STEP free-boundary equilibrium and target outline | OpenSTEP commit `6f66ae09c60b361d600b178416ef3f22b8d0aa6a`; accepted OPENSTEP-003 fields and OPENSTEP-005 footprints | Conditional heat-load and cooling requirements for the existing coil-position cases |
| STEP EB-CC JETTO flat-top profiles | Same historical OpenSTEP source, archived in OPENSTEP-002 | Thermal fusion, reduced energy balance, source-equivalent fuel burn and power accounting |

These are not one integrated, calibrated reactor model. The public OpenSTEP wall data supply a limiter outline, not the passive-conductor thicknesses, resistivities, connectivity and controller transfer functions needed to calculate STEP's wall-stabilized dynamics. The source is the historical SPR45/SPP001/CML5 scenario, not a claim about the current STEP engineering design. The DIII-D source is a published numerical model; no new experimental measurements were acquired.

The [protocol](https://github.com/enuminous/Tokamak/blob/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/PROTOCOL.md) precedes the new physical runs. [Amendments](https://github.com/enuminous/Tokamak/blob/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/AMENDMENTS.md) identify implementation fixes and later diagnostics. The [source catalog](https://github.com/enuminous/Tokamak/blob/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/source/catalog.json) records upstream revisions and Git blob identities. Three transferred source files contain one extra trailing newline; removing that byte exactly reproduces their upstream blob hashes. Numerical content is unchanged.

## Native equilibrium, wall and growth calculations

The native OFT library was actually executed. The original mesh has 8,911 vertices, 17,660 triangles and 35,481 second-order degrees of freedom. Halving all mesh length scales produces 30,451 vertices and 60,578 triangles. We follow the published inverse reconstruction, forward reconstruction, and final edge-current ramp with `Ip_ratio=5.6`. That ramp changes the equilibrium; stability results belong to the ramped case. Numerical vertical-position constraints used to construct it are not feedback hardware.

| Comparison | Result | Frozen limit | Outcome |
|---|---:|---:|---|
| Published notebook growth | 945.98 /s | Reference | — |
| Replayed coarse growth | 945.977600 /s | Within 10% of reference | PASS |
| Finer mesh growth | 929.348247 /s | Coarse/fine difference ≤10% | PASS: 1.76% |
| Slowest passive-wall decay time | 11.558139 ms coarse; 11.559189 ms fine | Difference ≤10% | PASS: 0.0091% |
| Double all vessel resistivities | Growth 1891.955200 /s | Twice growth within 2% | PASS |
| Double all vessel resistivities | All four wall decay times halve | Within 0.1% | PASS |

The leading coarse mode has a 1.057107 ms e-folding time. Positive growth denotes instability. The other nine requested eigenvalues near the specified spectral search point are decaying; this is a partial axisymmetric spectrum, not a general 3D MHD stability assessment. Two-grid agreement is not a proof of continuum convergence.

The upstream notebook's stored current-derived statistics do not all match this library's current output. For example, its inverse-solve text prints 567,670 A, whereas the replay reports 493,324 A. The printed magnetic-axis location, volume and leading growth are reproduced. The [stored upstream text](https://github.com/enuminous/Tokamak/blob/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/source/reference-text-outputs.txt) and replay statistics remain available; we do not claim identity of every notebook output or diagnose the statistic difference as a physical effect.

## The time-domain comparison fails

We seed the leading mode at 0.0005 of the equilibrium flux span, evolve for two e-folding times and fit the first e-folding interval. The fit uses the absolute projection of the evolving flux difference onto the seeded eigenvector. This is a Euclidean field projection, not a separately derived biorthogonal modal amplitude.

| Linear model / time step | Eigenvalue (/s) | Fitted growth (/s) | Relative disagreement | Outcome at 10% |
|---|---:|---:|---:|---|
| Published fixed-bounds setting; 0.1/γ | 945.978 | 802.146 | 15.20% | FAIL |
| Published fixed-bounds setting; 0.05/γ | 945.978 | 784.789 | 17.04% | FAIL |
| Include-boundary-terms diagnostic; 0.05/γ | 807.703 | 618.296 | 23.45% | FAIL |
| Include-boundary-terms diagnostic; 0.025/γ | 807.703 | 608.485 | 24.66% | FAIL |

Within each model the two time-step fits agree inside the separate 5% criterion. Refining time therefore does not close the linear/time comparison. Including boundary terms moves the eigenvalue toward the original measured rate, but seeding that model's own eigenvector still fails. This explanation is incomplete, not resolved.

The negative-seed fixed-bounds run fits 781.013/s. An unseeded trajectory drifts by 19.604 μm over the same 2.114 ms interval, compared with 1.260 mm final displacement in the positive-seed open-loop case. These diagnose sign sensitivity and residual drift; they do not erase the primary failures. Linearization conventions, profile/global-target treatment, initialization and mode projection require a matched investigation before claiming time/eigenmode validation.

The first isolated run initially reported an almost zero axis displacement because setting flux did not update the cached critical-point bounds. Explicit bounds updates fix the diagnostic. Its original output and the earlier temporary-directory collision errors are retained in `results/` and `development/`.

## Prescribed-current feedback and delay

The controller applies opposite current corrections to F9A and F9B, using `u = -K ΔZ`, a ±500 A correction limit and a 1 MA/s slew limit. Current is prescribed directly. There is no claimed power-supply voltage model, physical sensor, circuit calibration or noise model. Each initial displacement is approximately 0.26335 mm; the test lasts 2.114 ms. Suppression requires final displacement no larger than initial and peak displacement no larger than twice initial.

| Gain (A/m) | Measurement delay | Final absolute displacement (mm) | Peak absolute displacement (mm) | Conditional suppression |
|---:|---:|---:|---:|---|
| −100,000 | 0 | 146.840 | 146.840 | No |
| −20,000 | 0 | 19.353 | 19.353 | No |
| 0 | 0 | 1.260 | 1.260 | No |
| +20,000 | 0 | 0.02904 | 0.26335 | Yes |
| +100,000 | 0 | 0.00212 | 0.26335 | Yes |
| +100,000 | 0.5 ms | 5.956 | 6.959 | No |
| +100,000 | 1.0 ms | 1.045 | 4.042 | No |

The +100,000 A/m gain was selected by its smallest final displacement and then subjected to the two frozen delay tests. That is an exploratory selection, not an independently optimized or robust controller. No time-step retries occurred. The adverse-gain large displacements leave the small-perturbation regime; they are nonlinear numerical stress cases.

![Native reference solution and feedback trajectories](https://raw.githubusercontent.com/enuminous/Tokamak/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/results/native-reference.png)

## Temperature-dependent fusion and reduced burn balance

Using the supplied D and T thermal-density profiles and ion temperatures, we integrate

\[
P_\alpha=E_\alpha\int n_D n_T\langle\sigma v\rangle_{DT}(T_i)\,dV.
\]

The Bosch–Hale coefficients and formula are checked against a pinned [UKAEA PROCESS implementation](https://github.com/ukaea/PROCESS/blob/2f2d82125fab1b0a22ec1bc5891a9f032bc86319/process/models/physics/fusion_reactions.py); see the original [Bosch–Hale paper](https://doi.org/10.1088/0029-5515/32/4/I07). This formula comparison tests implementation agreement, not independent nuclear physics. Trapezoid and Simpson volume integration differ by 0.00362%.

The unfitted result is **308.9996 MW alpha power** and **1,553.8266 MW thermal D–T fusion power**. The archived source reports 311.2489 MW deposited alpha power and 1,554.5129 MW total fusion power. Alpha disagreement is −0.7227%; production and deposition are not identical quantities, so that agreement is a comparison screen. The source's fusion-to-auxiliary-power ratio is 12.0505, not a plant electric gain.

For the reduced dynamic model, all temperatures scale by `x`, densities and profile shapes remain fixed, and `W=xW0`. Fusion follows reactivity rather than an imposed constant alpha source:

\[
\dot W=f_{aux}P_{aux,0}+P_{ohm,0}+f_{dep}P_\alpha(x)
 -P_{rad,0}x^a-\frac{xP_{transport,0}}{f_\tau}.
\]

The 4.01744 s reference transport time and radiation magnitude are calibrated to the source. They do not independently predict confinement or impurity radiation. The 72 declared cases have 58 sign-changing roots within `0.5≤x≤2.5`; only two roots are locally stable under their particular assumptions. This root count is not a probability. Tangential roots can be missed by the specified search.

The central case has an equilibrium at `x=1.0070316`, with **positive thermal growth 0.557887/s**. Starting 5% colder reaches the lower model boundary in 4.7223 s; 5% hotter reaches the upper boundary in 6.1168 s. Integration stops there and makes no prediction outside the declared range. Dense-trajectory and event-time comparisons against tighter integration pass. Stabilizing this model requires a heat-removal/heating response steeper than approximately 321 MW per unit `x` locally; that is a linearized requirement, not an implemented burn controller.

These calculations omit evolving density, helium ash, separate electron/ion energy equations, current sustainment, predictive turbulence, time-dependent radiation and alpha slowing down. Consequently they are more informative than fixed-alpha accounting, but still not a self-consistent burning-plasma simulation.

## Exhaust and component requirements

Starting from OPENSTEP-005's sharp-wall peak loads and its 50% assumed SOL radiation, the radiation fractions needed to reach an assumed 10 MW/m² screen are:

| p9 shift | Existing peak (MW/m²) | Required SOL radiation |
|---|---:|---:|
| Baseline | 13.6930 | 63.48% |
| −1 cm | 11.8367 | 57.76% |
| +1 cm | 21.9709 | 77.24% |
| +5 cm | 63.5180 | 92.13% |

This rescales fixed-geometry attached heat mapping. It does not simulate detachment or establish that the required radiation is achievable. Geometry and power sharing remain inherited assumptions; the 0.25–20 mm footprint window is not a proof of a global wall maximum.

The 108 constant-property slab/coolant cases use `Tsurface=450 K + q(L/k+1/h)`. **42 fall below the assumed 1800 K screen**. This is not a certified tungsten limit or component lifetime. Hydraulics, critical heat flux, joints, stress, fatigue, erosion, irradiation and transients remain unresolved. Earlier coil-force screens remain available in OPENSTEP-002; no new structural or quench qualification is claimed.

![Reduced burn and radiation requirements](https://raw.githubusercontent.com/enuminous/Tokamak/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/results/reactor-requirements.png)

## Fuel and net electricity

Treating the historical source power as D–T-equivalent gives **0.238546 kg tritium burned per full-power day**, or **87.1290 kg per full-power year**. At a 3% burn fraction, injected tritium throughput is about 7.95 kg/day. Routing all unburned fuel through a four-hour processing path implies approximately 1.29 kg in that path. This excludes reserves, retained fuel, blanket inventory and start-up supply, and changes if direct recycling bypasses that path.

For breeding ratio `B`, breeding recovery `r`, exhaust loss per pass `l`, and burn fraction `b`, the modeled surplus relative to burn is

\[
s=rB-1-l(1/b-1),\qquad B_{required}=\frac{1+l(1/b-1)}{r}.
\]

Only 50 of 135 assumed combinations have nonnegative balance. This is not a TBR prediction or self-sufficiency demonstration. Neutron transport, radioactive decay, retention, reserve inventory, maintenance and supply constraints are absent.

The 162 electric-balance cases span **−319.28 to +606.67 MWe while operating**, and **−317.35 to +541.00 MWe as annual averages**. There are 123 online-positive and 86 annual-positive cases. These counts measure a chosen parameter grid, not success likelihood.

As a labeled illustration, 40% heat conversion, 50% auxiliary wall-plug efficiency, full fusion-heat recovery, 150 MW fixed loads and 60% availability give 264.47 MWe online and 98.68 MWe annual average. Deposited auxiliary/ohmic heat is credited once and its electric supply charged once; fixed loads persist during downtime. This example assumes the source fusion power can be sustained, the stated heat recovered and those loads/efficiencies achieved. None is established by the arithmetic. No blanket multiplication is credited.

## Verification, replay and remaining work

| Check group | PASS | FAIL |
|---|---:|---:|
| Historical artifact integrity | 241 | 0 |
| Inputs, archived code and execution integrity | 99 | 0 |
| Primary native comparisons | 6 | 2 |
| Added native diagnostics | 1 | 2 |
| Reactor accounting and numerical comparisons | 16 | 0 |

Raw checks are in [verification.json](https://github.com/enuminous/Tokamak/blob/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/results/verification.json); all scenario rows and trajectories are in `results/`. The [readiness matrix](https://github.com/enuminous/Tokamak/blob/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/READINESS.md) lists the actual closure requirements. A valid native linear/time comparison is the next computational gate. STEP passive-vessel/circuit/controller data and independent comparison with a real displacement measurement are the next input gate. General MHD, predictive burn/transport, detachment, engineering qualification, neutronics and sustained net electricity remain open.

Use Python 3.12 and [requirements.txt](https://github.com/enuminous/Tokamak/blob/7f2842f3086fae73ad51c1b784830862c314658f/benchmarks/openstep-006/requirements.txt), with the OFT 26.9 native library available. The recorded run used Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, h5py 3.16.0 and matplotlib 3.10.8 on Linux x86-64. In an expendable checkout:

```bash
OPENBLAS_NUM_THREADS=1 python benchmarks/openstep-006/run.py
```

The replay runs the native cases sequentially to avoid oversubscribing the library, then recomputes reactor screens, verification and plots. It overwrites current named outputs in that checkout. Historical failed attempts remain archived rather than being silently regenerated as successes. A successful process exit means execution completed; `verification.json` deliberately retains the failed physics-comparison outcomes. The published manifest and commit preserve original bytes; floating-point, mesh and timing differences on another system must be evaluated against the stated criteria rather than expected to hash identically.

No hardware has been built or operated by this work, and no build-ready reactor design or completion date is supported by these results.
