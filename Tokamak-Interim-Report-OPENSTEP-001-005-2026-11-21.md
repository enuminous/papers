# From Tokamak Analogy to Reproducible Equilibrium and Exhaust Screens

## Interim report on OPENSTEP-001–005

**Matthew Chenoweth Wright · Monolithic LLC · 21 November 2026**  
**Status:** interim computational research report; physical design qualification unresolved.  
**Evidence cutoff:** Tokamak commit [`dcdfb6956dac7143066f0c308474fda2bb83f48e`](https://github.com/enuminous/Tokamak/commit/dcdfb6956dac7143066f0c308474fda2bb83f48e). The final OPENSTEP-005 records are timestamped 22 November in UTC, corresponding to 21 November in Pacific time.

### Abstract

This report documents the transition from an illustrative tokamak return-loop model to a reproducible sequence of equilibrium, engineering-screen and numerical-validation calculations. OPENSTEP-001 reproduced a published UKAEA OpenSTEP design equilibrium using its explicit coil geometry and native profile functions. Subsequent experiments separated a coil displacement at fixed pressure/current derivatives from displacements at fixed pressure profile and total plasma current. The latter scan accepted eight of fourteen grid/geometry cases; no candidate satisfied its frozen improvement rule. OPENSTEP-004 reproduced the accepted equilibria and compared distinct field-line integrators, but recorded 220 failed assertions involving stricter flux, refinement, symmetry and sampling checks. OPENSTEP-005 introduced implicit flux-contour tracing with separate connection-length quadrature, resolved one-sided heat limits at a wall corner, and examined assumed circular fillets. Its frozen record contains 2,064 passing assertions and no failures. The baseline sharp-wall heat maximum over the specified launch window increases from the previously sampled 12.3507 to 13.6930 MW/m². These are conditional calculations on shared equilibrium fields, not measurements. Synthetic wall-current and feedback controls pass, while actual-device conducting-wall modes, feedback performance, transport and engineering qualification remain unresolved.

### 1. Scope and the question being tested

The earlier [*Energy Through the Hourglass*](Energy-Through-the-Hourglass-TriSphere-Tokamak-2026-11-19.md) used a diverted tokamak as a physical analogue for a circulation, exhaust and return motif in A. Beth Jones’s TriSphere framework. It distinguished returned particle inventory from returned energy. Those illustrative balances and radial models remain separate from the calculations reviewed here.

The present sequence asks narrower questions. Can a conventional free-boundary equilibrium calculation reproduce a specified public design case? What changes when selected coils move under clearly stated operating constraints? Which apparent improvements survive numerical refinement? Can a heat-footprint feature be distinguished from an integration or wall-discretization artifact?

The implemented magnetic model is the conventional axisymmetric Grad–Shafranov equation. No additional EFMW force term or physical law derived from TriSphere layer counts is introduced. The contribution is a reproducible computational investigation, with explicit controls, retained failures and limits on interpretation. Neither the analogy nor the number of passing assertions establishes a new magnetic law, improved confinement or a feasible reactor. The protocols record declared thresholds, while numerical development and restarts are exploratory and disclosed; independent preregistration is not claimed. [S1–S5]

### 2. Source data, equations and numerical conventions

The external reference is Brown et al., *OpenSTEP: public data release of the STEP Prototype Powerplant scenario SPP-001*, DOI [10.14468/07jt-s540](https://doi.org/10.14468/07jt-s540), at source revision `6f66ae09c60b361d600b178416ef3f22b8d0aa6a`. This is a published design simulation, not an experimental plasma discharge. The equilibrium source includes fourteen coil packs, seven circuit currents and 2,196 numerical filaments. Pack currents are equivalent one-turn currents; they do not specify a completed superconducting winding design. [M1]

With internal poloidal flux per radian denoted by $\psi$, the equilibrium calculation uses

$$
\Delta^*\psi=-\mu_0 R J_\phi,
\qquad
\Delta^*=\partial_R^2-\frac{1}{R}\partial_R+\partial_Z^2,
$$

$$
J_\phi=R p'(s)+\frac{FF'(s)}{\mu_0R},
\qquad
s=\frac{\psi-\psi_{\mathrm{axis}}}{\psi_{\mathrm{boundary}}-\psi_{\mathrm{axis}}}.
$$

The source terms are restricted to the connected plasma core. The total flux combines the plasma solution with the field of the specified coil filaments. The numerical implementation uses FreeGS 0.8.2, a fourth-order operator, a cell-area treatment of the separatrix source, refined critical points and a Newton–Krylov solve. Accepted equilibria must meet the recorded full-domain normalized residual threshold of $10^{-5}$. The plasma boundary contribution is calculated using the von Hagenow routine; the reference flux serves as a starting field rather than a fixed final answer. [M1, F1]

The source convention check matters. The OpenSTEP README and the actual NetCDF metadata identify different IMAS/COCOS versions. The native MAT data, NetCDF identities and current-density checks determine the sign and $2\pi$ conversion used in the reproduction. Internal coordinates are metres, pressure is pascals, current is amperes and $F=RB_\phi$ is in tesla metres. The boundary value is $F=11.52$ T m, with pressure set to zero at the edge. [M1]

Up-down symmetry is imposed in the equilibrium solve. Consequently, a symmetric equilibrium or a successful mirror-trace check does not test the stability of antisymmetric vertical perturbations. Numerical convergence, equilibrium reproduction and dynamic stability are separate questions throughout this report.

### 3. Evidence accumulated across the five stages

| Stage | Main calculation | Recorded result | Interpretation |
|---|---|---|---|
| OPENSTEP-001 | Reproduce the public equilibrium; translate both p9 packs 10 cm toward the midplane at fixed circuit currents and derivative-profile functions | Reproduction criteria PASS; 129 × 257 and 257 × 513 scored fields converge; 65 × 129 attempts remain unresolved | A numerical benchmark and a conditional equilibrium response |
| OPENSTEP-002 | Refine the original comparison to 513 × 1025; add a fixed-pressure/current comparison and reduced physics/engineering screens | 66 verification assertions PASS, 0 FAIL; important physical screens remain adverse or unresolved | Implementation checks pass without establishing design feasibility |
| OPENSTEP-003 | Scan seven p9 positions on two grids at fixed full pressure profile and total plasma current | 8 of 14 grid/geometry cases accepted, 6 unresolved; 120 verification assertions PASS, 0 FAIL; no qualifying candidate | The optional 513 × 1025 candidate refinement is not triggered |
| OPENSTEP-004 | Uncached equilibrium replay, direct coil-force comparison, alternate field-line integration and denser heat sampling | Initial ledger: 792 PASS, 220 FAIL; separate third-tolerance diagnosis: 32 PASS, 1 FAIL | Earlier numerical agreement was insufficient for the stricter checks |
| OPENSTEP-005 | Implicit flux contours, separate length quadrature, wall-corner limits, assumed rounding and synthetic feedback controls | 2,064 assertions PASS, 0 FAIL in the frozen publication | The specified numerical questions are better resolved; device qualification remains unresolved |

The counts include integrity checks, repeated per-trace conditions and synthetic controls. They are neither independent experiments nor probabilities of physical success. They should not be summed into a cumulative validation score. The failures in OPENSTEP-004 remain part of the historical record; OPENSTEP-005 adds a new calculation rather than retroactively relabelling them. [S1–S5, L4, L5]

### 4. Operating constraints change the answer

In the original fixed-derivative comparison, moving both p9 coil packs 10 cm toward the midplane increases the fine-grid plasma current from 22.77441 to 23.01689 MA and the on-axis pressure from 1.33527 to 1.38385 MPa. The magnetic axis moves outward by about 1.600 cm. These changes are outputs of the imposed profile convention, not evidence of improved energy confinement or newly generated power. [S1]

OPENSTEP-002 refines that comparison to 513 × 1025. The reproduced baseline core-flux error against the reference falls to approximately 0.0878% of the axis-to-boundary flux span. Under a different constraint—holding the full pressure profile and total plasma current fixed—the 257-grid axis shift for the 10 cm move is instead approximately **−8.935 cm**. Its coarse baseline was unresolved at that stage, so that number was not a refinement-verified design improvement. The opposite direction of the axis response illustrates why the operating constraint must accompany every geometry claim. [S2]

OPENSTEP-003 recovers the constrained coarse baseline and scans displacements of 0, ±1, ±2.5 and ±5 cm. Positive displacement means movement toward the midplane. The target current is approximately 22.77441055 MA and the target on-axis pressure is 1.33526685 MPa; the full $p(s)$ function is held fixed, not merely its axis value. Coil currents and boundary $F$ also remain fixed. Shape, safety factor, pressure integral and the mapped thermal-energy target may still change. [S3]

Its improvement rule requires a resolved reduction in representative heat, a lower sampled maximum, valid traces, and no resolved deterioration in clearance or required confinement multiplier. Resolution is screened using the sum of the observed candidate and baseline grid changes; this is a numerical heuristic, not a confidence interval or rigorous error bound. No candidate passes the combined rule. In particular, the +5 cm fine-grid field lacks an accepted coarse counterpart. Unsuccessful solves do not prove that the associated physical equilibrium is impossible.

The earlier extended screens also remain relevant. They include 72 prescribed-source energy trajectories, 240 heat samples, 36 thermal-diffusion cases and 80 conditional electric-budget combinations. Fusion/source powers, loss closures and engineering assumptions are supplied inputs. These screens identify sensitivities and failure conditions; they do not establish burn, cooling capability or positive net electricity. [S2]

### 5. What the numerical validation did—and did not—resolve

#### 5.1 Equilibrium and rigid-force replay

OPENSTEP-004 reruns all eight accepted fields through the uncached equilibrium operator. The largest normalized defect is approximately $4.34\times10^{-8}$, below the unchanged $10^{-5}$ limit. Direct coil-field evaluation and the previous interpolated-vacuum calculation agree in the rigid vertical-force slope to within about 0.01142%. [S4]

The slopes remain positive, approximately 20.45–20.89 MN/m across the accepted cases. This is a destabilizing response in the specified rigid-current, fixed-coil, no-wall model. It supplies neither a wall-coupled eigenmode nor a physical growth rate. Conducting structures, current redistribution, shape response and feedback are absent from that calculation.

#### 5.2 Integration agreement exposed a stricter problem

The original fixed-step RK4 tracer follows poloidal arc length and uses chord/wall intersections. OPENSTEP-004 adds adaptive DOP853 integration in toroidal angle with continuous wall events. Across forty original-offset comparisons, their maximum differences are approximately 3.587 µm in strike position, 0.199 mm in connection length and 0.00015% in representative heat. Both routes share the equilibrium arrays, interpolation and wall geometry. [S4]

The stronger checks still fail: 189 flux assertions, 29 adaptive-tightening assertions, one mirror assertion and one nested-sampling assertion. In the separate eight-field, 1 mm third-tolerance diagnosis, flux checks pass but one connection-length comparison remains outside its 0.1 mm tolerance: the fine baseline changes by about 0.2383 mm. Retaining those failures identifies a useful next calculation; agreement at a looser tolerance is not a reason to erase them. [S4, L4]

#### 5.3 Implicit contours and separate length quadrature

OPENSTEP-005 follows the level set $\psi(R,Z)=\psi_{\mathrm{launch}}$ using alternating implicit R/Z charts. It solves locally for the dependent coordinate and splits steps at interpolation-grid crossings. Connection length is then integrated separately along the contour. If $u$ is the independent chart coordinate and $v$ the dependent coordinate,

$$
\frac{dv}{du}=-\frac{\partial_u\psi}{\partial_v\psi},
\qquad
dL=\sqrt{1+\left(\frac{dv}{du}\right)^2}
\sqrt{1+\frac{F^2}{|\nabla\psi|^2}}\,|du|.
$$

The second factor accounts for the toroidal contribution to field-line length. The tested settings pair maximum coordinate steps of 20/10 mm with 8/16 Gauss–Legendre nodes. Analytic straight and curved contours, both directions, and a deliberately inconsistent field/flux pair provide implementation controls. [S5, C5]

The primary physical-field record contains 88 traces: five offsets on each of eight fields at two settings, plus eight reverse 1 mm traces. Maximum normalized flux error is approximately $2.0\times10^{-13}$. Across the forty refinement pairs, the largest connection-length difference is $2.25\times10^{-11}$ m. Across the eight comparisons with the saved third-tolerance DOP853 route, the largest length difference is $1.61\times10^{-5}$ m, or about **16.1 µm**, within the frozen 0.1 mm criterion. [S5]

Those very small refinement differences concern calculation on one fixed interpolant; they are not physical accuracy estimates. Projection enforces the flux condition, so small flux error alone would be weak evidence. The analytic length controls, separate quadrature refinement, mirrored traces and alternate-integrator comparison supply additional numerical checks. Neither route independently validates the common equilibrium or physics model.

A performance change is also recorded rather than hidden. Caching the spline derivatives matched the uncached evaluation at 692,744 grid/seeded points and reproduced eight tight 1 mm comparison traces exactly. The initial rounding sweep was interrupted after five complete scenarios and restarted using the checked cache. Its partial checkpoint, source and log are retained. No physical parameter or acceptance threshold changed. [D5]

### 6. The divertor-corner result

The heat projection keeps the earlier imposed assumptions: upstream exponential width $\lambda_q=6$ mm, SOL radiation fraction $f_{\mathrm{SOL}}=0.5$, one-target share $f_t=0.25$, and transported source power approximately 143.049 MW. That power is taken from the separately identified JETTO flat-top source; it is not recalculated self-consistently for each modified equilibrium. [S2, S5]

For upstream offset $x$ and launch radius $R_u$, the conditional target load is

$$
q_t(x)=\frac{f_t(1-f_{\mathrm{SOL}})P_{\mathrm{transport}}}
{2\pi R_u\lambda_q}
e^{-x/\lambda_q}
\frac{|\mathbf B_t\cdot\mathbf n|}{B_{p,u}}.
$$

Thus the local target normal is consequential. At 1 mm offset, the fine baseline and ±1 cm cases hit main-wall face 12, whereas the +5 cm field hits adjacent face 13. The latter incidence produces a much larger normal field and a smaller area expansion. The resulting high heat projection is reproduced by alternate tracing; it is not removed by changing the integrator. [S4]

OPENSTEP-005 maps the target branches over a **0.25–20 mm upstream offset window**, locates the sharp transition from the flux at the vertex, and evaluates one-sided limits. It also replaces the lower corner and its upper mirror with exact circular fillets of assumed radius 1, 5 and 10 mm. The equilibrium fields are held fixed. The results are:

| p9 displacement | Previous 37-point sharp sample maximum | Corner-resolved sharp-wall maximum | 1 mm fillet | 5 mm fillet | 10 mm fillet |
|---|---:|---:|---:|---:|---:|
| 0 cm | 12.3507 | 13.6930 | 12.3690 | 11.8204 | 11.8204 |
| −1 cm | 11.8367 | 11.8367 | 11.8367 | 11.8367 | 11.8367 |
| +1 cm | 21.5351 | 21.9709 | 19.8338 | 15.2811 | 13.2477 |
| +5 cm | 63.5180 | 63.5180 | 63.5180 | 63.5180 | 58.8269 |

**All entries are conditional MW/m² within the specified window.** The previous column is a historical sampled result; the current columns use the contour/target-map investigation. The baseline transition occurs at approximately 9.380951 mm upstream offset, at the lower polygon vertex $(R,Z)=(5.855,-8.52316)$ m. Its two face limits are about 2.6555 and 13.6930 MW/m². The mathematical corner has no unique normal, so reporting a single value at the vertex without its side would be misleading. [S5, H5]

![Conditional heat footprints across the four accepted fine-grid fields and assumed target radii](https://raw.githubusercontent.com/enuminous/Tokamak/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/results/footprint-rounding.png)

*Figure 1. OPENSTEP-005 calculation on fixed equilibrium fields. Curves show the supplied sharp wall and three assumed radii. The dashed line marks the inherited 10 MW/m² screening value; it is not a qualified material limit. Adapted computational geometry derives from the cited OpenSTEP release.*

The sixteen scenarios contain 9,766 direct flux-map samples and 146 additional first-hit/near-peak trace records. Nested sampling and bounded searches satisfy the declared 1% peak-consistency criterion. Full traces check connectivity at three interior locations per target branch and near each scenario’s maximum. The search covers the observed lower faces and fillet; it is not an interval proof excluding every possible topological transition. [H5]

Three limits remain decisive. First, the −1 cm and +5 cm maxima lie at the 0.25 mm window boundary; the test does not bound the load closer to the separatrix. Second, the fillet radii are invented sensitivity cases, not measured CAD. Third, tracing more accurately on a saved spline does not add equilibrium resolution. These results therefore do not reverse OPENSTEP-003’s design-selection verdict. The lower −1 cm maximum under this new metric is not sufficient to promote a geometry under the earlier rule.

### 7. Conducting wall and feedback: a tested implementation, an unrun device calculation

OPENSTEP-005 implements a synthetic four-state electromechanical model:

$$
\dot z=v,\qquad
m\dot v=kz-dv+g_wI_w+g_cI_c,
$$

$$
L_w\dot I_w=-R_wI_w-g_wv,\qquad
L_c\dot I_c=u-R_cI_c-g_cv,
\qquad u=-K_pz-K_dv.
$$

Here $z$ and $v$ are displacement and velocity; $I_w$ and $I_c$ are wall and control-coil currents. The fixture parameters $m$, $k$ and $d$ specify inertia, displacement stiffness and damping; $L$, $R$ and $g$ specify inductance, resistance and reciprocal coupling. The reciprocal coupling terms permit an explicit energy-balance check. For the passive restoring control with $k<0$, the positive energy

$$
E=\tfrac12mv^2-\tfrac12kz^2+\tfrac12L_wI_w^2+\tfrac12L_cI_c^2
$$

satisfies

$$
\dot E=-dv^2-R_wI_w^2-R_cI_c^2+uI_c.
$$

Its 28 checks cover no-wall and ideal-wall analytic limits, the resistive-wall characteristic polynomial, passive energy balance, time integration against a matrix exponential, stabilizing and reversed feedback signs, voltage saturation and rejection of missing or malformed inputs. A separate synthetic gain grid contains 546 cases, 287 with strictly decaying linear modes. The grid count is a property of the chosen synthetic model and gains, not the probability of stabilizing a tokamak. [W5]

The mass, coupling, inductance, resistance and controller values are implementation fixtures. They are not inferred STEP parameters. Sensor noise, sampled control, latency, current limits, evolving equilibrium and distributed plasma/conductor dynamics are not represented by this fixture. The scalar rigid-force slope from the earlier screen cannot substitute for these missing data.

The actual-device input record therefore remains incomplete. A first-wall outline is not a conducting volume or shell model. Required inputs include conductor geometry/thickness, material resistivity and temperature, electrical continuity and contacts, dynamic active-coil circuits, a validated plasma response, sensor/actuator characteristics and a controller with explicit timing and limits. The completeness validator deliberately rejects the current record. Passing a metadata schema would still not establish calibration or independent review. [I5]

TokaMaker native initialization was demonstrated earlier, and its official vertical-stability example provides a possible route for a subsequent model. **No TokaMaker wall eigenmode or actual-device feedback result is reported in OPENSTEP-001–005.** [S2, T1]

### 8. Present claims and remaining limits

| Claim | Interim finding | Basis or missing evidence |
|---|---|---|
| The specified public equilibrium can be reproduced numerically | PASS within the recorded benchmark tolerances | Source identities, accepted solves and residual/reproduction checks |
| The new contour method passes the declared frozen-field checks | PASS for the tested cases | Analytic controls, refinement, alternate integration and retained raw data |
| Wall-corner geometry materially changes the imposed heat footprint | Supported within this model | One-sided limits and sixteen conditional geometry scenarios |
| A coil displacement is a demonstrated design improvement | UNRESOLVED; no candidate met the frozen rule | Incomplete matched-grid acceptance and unresolved model/engineering uncertainties |
| The synthetic wall/feedback implementation meets its declared checks | PASS for its specified equations and fixtures | Analytic limits, energy balance, sign/saturation controls |
| The proposed device has validated wall-coupled or 3-D MHD stability | NOT RUN / UNRESOLVED | No calibrated device wall/plasma/circuit/controller calculation |
| Confinement, burn, detached exhaust, materials or net electricity are qualified | UNRESOLVED | Prescribed-source/reduced screens do not provide the required predictive or engineering models |
| TriSphere or EFMW has gained experimental physical confirmation from this sequence | Not established | No device measurements or theory-specific discriminating experiment |

The demonstrated advance is a more explicit and reproducible computational basis for evaluating selected geometry changes. Agreement between numerical routes using shared inputs is useful implementation evidence. It is not independent experimental confirmation or independent external review.

### 9. Next bounded work

1. **Establish the device model needed for wall modes.** Obtain referenced conducting geometry, material properties, connections, circuits and a plasma response. Reproduce the equilibrium in the chosen wall-coupled solver before evaluating modes. Check mesh dependence, passive limits and growth/decay against time evolution before adding sampled, delayed and limited feedback.
2. **Replace assumed target geometry and heat inputs.** Obtain a defensible target radius and manufacturing geometry, quantify upstream-width/power uncertainty, and define how the near-separatrix region will be resolved. Extend the footprint study under a declared domain and metric; retain one-sided treatment wherever sharp geometry remains.
3. **Resolve the design-comparison gaps and obtain an external replay.** Address the six unaccepted grid/geometry cases and require matched operating constraints and accepted grid pairs. Any revised selection metric should be stated before a new comparison. The earlier optional 513 × 1025 test remains untriggered under its original rule. An external reviewer can start with one pinned contour/heat comparison and its negative controls.

These are proposed next steps. This report does not claim that the missing inputs, external review or further physical-model runs have been obtained.

### 10. Reproducibility and publication record

The canonical code, field arrays, raw outputs, protocols, development attempts and hash manifests remain in **enuminous/Tokamak**. This paper summarizes them at one immutable revision instead of maintaining a competing copy of the numerical results. A compact [evidence index](assets/tokamak-interim-2026-11-21/evidence-index.json) records the source paths and SHA-256 hashes used for this report.

The recorded environment is Python 3.12.14, FreeGS 0.8.2, NumPy 2.3.5, SciPy 1.17.0, Matplotlib 3.10.8 and Shapely 2.2.0; the full dependency list is pinned in the repository. To replay OPENSTEP-005 from the published inputs:

```sh
git clone https://github.com/enuminous/Tokamak.git
cd Tokamak
git checkout dcdfb6956dac7143066f0c308474fda2bb83f48e
python -m venv .venv
. .venv/bin/activate
python -m pip install -r benchmarks/openstep-005/requirements.txt
OPENBLAS_NUM_THREADS=1 python benchmarks/openstep-005/run.py
```

The runner returns nonzero on a failed assertion. Inspect the per-stage JSON and raw values as well as the process status. The 2,064 count belongs to the frozen publication: its controls and primary traces started before all later drivers existed, and the provenance inventory records the Python files present at each stage start. A fresh sequential replay can contain additional provenance checks. Comparison should therefore use named assertions, source identities and numerical outcomes, not an exact aggregate count alone. The separate stage READMEs provide instructions for regenerating earlier equilibria and historical diagnostics. [S1–S5, D5]

This is an AI-assisted interim report of computational work, not an independently peer-reviewed validation. A. Beth Jones is credited for the originating TriSphere framework. Brown et al., UKAEA and the STEP Team are credited for the external design data. The OpenSTEP source and adapted data/figures retain their CC BY 4.0 attribution; FreeGS remains an LGPL-3.0-or-later dependency. No UKAEA endorsement is implied.

### References and exact evidence locations

All Tokamak links below use the report’s immutable evidence revision.

- **[S1]** [OPENSTEP-001: published-equilibrium reproduction](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-001/README.md).
- **[S2]** [OPENSTEP-002: extended simulation screens](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-002/README.md).
- **[S3]** [OPENSTEP-003: fixed-pressure/current scan](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-003/README.md).
- **[S4]** [OPENSTEP-004: stricter numerical validation and retained failures](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-004/README.md).
- **[S5]** [OPENSTEP-005: contours, corners and synthetic feedback](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/README.md).
- **[M1]** [Equations, units and source-convention checks](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-001/METHODS.md); Brown, T., Casson, F., Hudoba, A., Marsden, S., Tholerus, E., Wilson, T., and the STEP Team (2025), *OpenSTEP*, [DOI 10.14468/07jt-s540](https://doi.org/10.14468/07jt-s540), [pinned source](https://github.com/ukaea/OpenSTEP/tree/6f66ae09c60b361d600b178416ef3f22b8d0aa6a).
- **[L4]** [OPENSTEP-004 verification ledger](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-004/results/verification.json) and [separate refinement assessment](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-004/results/refinement-assessment.json).
- **[L5]** [OPENSTEP-005 verification ledger](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/results/verification.json) and [machine-readable summary](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/results/summary.json).
- **[C5]** [Implicit contour implementation](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/contour.py) and [declared protocol](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/PROTOCOL.md).
- **[H5]** [Footprint results and branch checks](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/results/footprints.json) and [raw heat-map samples](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/results/footprints.csv).
- **[W5]** [Synthetic wall/feedback results and parameters](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/results/wall-feedback.json).
- **[I5]** [Actual-device input contract](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/INPUT-CONTRACT.md) and [incomplete input record](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/device-inputs.json).
- **[D5]** [Development and interruption record](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/DEVELOPMENT.md), [derivative-cache comparison](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/results/derivative-cache.json) and [artifact manifest](https://github.com/enuminous/Tokamak/blob/dcdfb6956dac7143066f0c308474fda2bb83f48e/benchmarks/openstep-005/artifact-manifest.json).
- **[F1]** [FreeGS 0.8.2: creating equilibria](https://freegs.readthedocs.io/en/stable/creating_equilibria.html).
- **[T1]** [Open FUSION Toolkit 26.9: TokaMaker vertical-stability example](https://openfusiontoolkit.github.io/OpenFUSIONToolkit/docs/v26.9/doc_tMaker_DIIID_ex2.html).
