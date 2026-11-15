# A test that can fail

This is a proposed measurement contract, not a registered experiment, a claim of apparatus access, or a claim that an existing dataset meets its requirements. No data were collected for this audit.

## Target and comparison class

Test whether independently inferred scalar masses and photon couplings agree with a separately measured leading low-energy photon-response coefficient. Freeze one of these hypotheses before collecting the held-out data:

| Model | Prediction |
| --- | --- |
| One positive-mass, photon-coupled canonical scalar; no independent four-photon contact term | \(a_X=g^2/(32m^2)\) |
| C1 flat-vacuum classical branch with positive-mass canonical modes, and no independent \(X^2\) term | \(a_X\ge\sum_{i\in S}g_i^2/(32m_i^2)\) for independently resolved subset \(S\) |
| Generic scalar effective theory with the same assumptions | The same equality or inequality |
| An enlarged theory containing independent four-photon operators | No such unrestricted relation for the total measured coefficient |

Agreement cannot distinguish the first two models from their matching generic-scalar counterparts. The equality and inequality are alternatives with different rejection conditions; do not change from equality to inequality after seeing an adverse result and describe the original test as a success.

## Two independently constrained measurements

1. **Mass and coupling channel.** Use an on-shell or otherwise appropriate propagating-scalar observable to constrain masses and couplings. If photon regeneration is chosen, use the full suitable propagation model, calibrated geometry, efficiency and backgrounds. A single coherent-limit rate generally constrains a coupling combination and does not identify a mass. Resolving the phase dependence or obtaining independent mass information is required. Multiple unresolved modes must not be reported as a resolved single mode.
2. **Low-energy response channel.** Infer the leading coefficient of the scalar optical contribution from independent data. For transverse-field birefringence, define the zero-field slope \(s_B=\lim_{B^2\to0}\Delta n_{\rm scalar}/B^2\), so that \(a_X=s_B/16\) under the stated assumptions. Vary field strength and probe conditions to bound higher-order and dispersive contamination. Demonstrate that the relevant frequencies and momentum transfers are below all integrated-out masses.

The second measurement must not be numerically generated from the first channel's fitted parameters. Distinct instruments or an independent custodian would improve independence, but shared calibration and systematic uncertainties still need explicit accounting.

## Background and validity requirements

Before interpreting a result, record:

- The operational mapping from the C1 M-sector field to calibrated electromagnetism.
- The ordinary quantum-electrodynamic contribution, material response, detector offsets, polarization calibration and magnetic calibration, with uncertainties and correlations.
- The field and energy ranges, a quantitative bound on neglected derivative and nonlinear terms, and evidence that the apparatus stays in the declared positive-response domain.
- The assumed mode content, any matter or hidden-sector extension, and whether independent local photon operators are excluded by the tested hypothesis rather than by data selection.
- A locked likelihood or inference procedure, treatment of nuisance parameters, and a sensitivity calculation using that apparatus's actual noise. Neither an achievable signal size nor a sample size has been established in this audit.

For one nonzero, resolved mode, the dimensionless diagnostic is

\[
R=\frac{32m^2a_X}{g^2}=\frac{2m^2s_B}{g^2}.
\]

The one-mode prediction is \(R=1\); the positive multimode prediction based on that resolved mode is \(R\ge1\). If the coupling is consistent with zero, do not use this ratio. Use the undivided equality or inequality with the full joint uncertainty instead.

## Proposed decision rule

Build a joint 95% confidence region for the relevant masses, couplings and \(a_X\), with nuisance and systematic uncertainty included. Its coverage must be checked for the chosen inference procedure before the final data are unblinded. The 95% level is an explicit future design choice, not an EFMW prediction.

- **Reject the selected conditional model** if that region has no intersection with its equality or inequality surface, after the predeclared validity checks pass.
- **Compatible but not confirmed** if it intersects the prediction and the experiment has the predeclared resolving power. Report the region's width rather than interpreting mere overlap as strong evidence.
- **Unresolved** if parameters are not identified, sensitivity is insufficient, background separation fails, or the approximation and apparatus requirements cannot be demonstrated.

For a confidence region with valid joint 95% coverage, rejection by nonintersection has false-rejection probability at most 5% when the tested model and validity assumptions hold. This coverage statement does not establish that a proposed apparatus or analysis actually achieves that coverage.

No result of this test by itself is a proof of the entire EFMW program. A failure rejects the declared model under its tested conditions. A future physical theory may introduce additional terms, but it must receive a new specification and new predictions rather than retroactively changing the failed target.
