# Conditional experimental contract

EFMW-C1-OBS-001 • Proposed version 0.1 • No experiment has been booked, registered or run.

This contract tests the selected scalar–photon interaction. An excess would support that common interaction model only after conventional backgrounds and alternatives are addressed. The identical generic scalar model remains an indistinguishable comparator.

## Estimand and prediction

The parameters are the scalar mass m and the magnitude of its photon coupling |g|. In the weak regime, counts depend on g⁴, so this experiment cannot determine the sign of g.

For exposure i:

\[
\mu_i=b_i(\nu)+\eta_i N_{\mathrm{in},i}g^4K_i(m),
\]

\[
K_i(m)=\frac{(B_{1i}L_{1i}B_{2i}L_{2i})^2}{16}
\sin^2\theta_i
\,\operatorname{sinc}^2\frac{m^2L_{1i}}{4\omega_i}
\,\operatorname{sinc}^2\frac{m^2L_{2i}}{4\omega_i}.
\]

Use measured field-profile integrals instead of BL where the uniform-field approximation is insufficient. All field and length factors in this expression use natural units.

For a photon-counting detector, a possible sampling model is \(n_i\sim{\rm Poisson}(\mu_i)\), with independently characterized dead time and efficiency. An analog CCD requires its calibrated analog likelihood; its output must not be treated as integer photon counts.

The nuisance model b_i(ν) must be constrained by control data. Allowing an arbitrary independent background for every condition would destroy identification.

## Conditions fixed before an outcome is unblinded

| Change from the signal condition | Predicted leading scalar response | What it tests |
| --- | --- | --- |
| Both regions active; input perpendicular | Full predicted signal | Primary condition |
| Input parallel, fields otherwise held fixed | Zero conversion signal | Polarization selection |
| Production field suppressed | Zero regeneration signal | Need for conversion before barrier |
| Regeneration field suppressed | Zero regeneration signal | Need for conversion after barrier |
| Both field magnitudes halved | 1/16 signal at fixed phase mismatch | Field dependence |
| Input at 45 degrees | Half signal | Polarization dependence |
| Input shuttered | Zero laser-derived signal | Detector and electronics background |
| Changed wavelength or effective length | Locked sinc response | Held-out mass/phase prediction |

These are predicted signal relations, not assertions that physical backgrounds remain unchanged. Polarization can change ordinary transmission or leakage; magnetic changes can affect optics, alignment and electronics. The control model must measure or bound those changes.

A scalar signal is insensitive to the sign of either field at the intensity level in this single-path setup. A sign reversal should not be advertised as an odd-in-field count signature.

## Apparatus assumptions to qualify

1. Establish which C1 gauge field corresponds to ordinary electromagnetic calibration.
2. Measure laser power, spectrum, polarization, field maps, path length, vacuum index, optical alignment, efficiency and acquisition losses.
3. Model or bound the static scalar background and verify the positive gauge-kinetic and weak-background conditions.
4. Verify the propagation approximation, including accumulated phase error, for the full predeclared mass domain.
5. Bound direct light transmission, scattered light, stray electromagnetic pickup, dark events and changes in these backgrounds across conditions.
6. Justify scalar transmission through the barrier and the absence of relevant extra interactions or screening.
7. Validate recovery with calibrated optical injections through a separately controlled calibration path. Such injections check instrumentation; they do not demonstrate scalar conversion.
8. Specify independent custody of condition labels and preserve all invalid/failed exposures with reasons.

The present package establishes none of these for a currently available physical apparatus. It supplies the mathematical quantities the qualification must measure.

## Parameter treatment and holdout

C1 does not specify g or m. A null experiment therefore yields parameter constraints, not a refutation of every member of the family.

For a search, declare the mass grid or continuous search procedure before unblinding. Use a stated family-level false-alarm rule for discovery, accounting for searching across masses and channels. Do not substitute a pointwise 95% exclusion curve for a global discovery test.

If separate discovery/calibration data estimate g and m, freeze them before examining a second wavelength, length or field schedule. Test those held-out predictions with the propagated parameter uncertainty. The same data cannot both select a favorable mass and serve as its independent confirmation.

All examples in the calculation use chosen parameters; there is no parameter fit to real data.

## One exact idealized sensitivity calculation

For zero observed events with exactly known zero background, the one-sided 95% Poisson upper bound on the signal mean solves

\[
e^{-\mu_{95}}=0.05,\qquad \mu_{95}=-\log(0.05).
\]

At a fixed mass with known exposure factor \(A=\eta N_{\rm in}K(m)>0\),

\[
|g|_{95}=\left(\frac{-\log0.05}{A}\right)^{1/4}.
\]

This does not apply unchanged when background, calibration, efficiency or mass selection is uncertain. At a coherence zero, A vanishes and the configuration supplies no leading bound.

The corresponding calculation in results/example.json is an idealized numerical illustration. It is not an analysis of OSQAR data and not a feasible-exposure guarantee.

## Decisions

**Support for the selected interaction:** an excess survives the predeclared background and uncertainty model, matches the polarization and field dependence, predicts held-out conditions, and is independently replicated. It would still be shared evidence for the generic scalar–photon model.

**Exclusion of a specified parameter region:** sensitivity is adequate and the predeclared analysis excludes that region while preserving the complete result record.

**Unresolved:** background transfer, signal attenuation, alignment, model validity, statistical power or apparatus characterization is inadequate.

**No unique EFMW attribution:** even perfect data for this branch cannot distinguish two exactly identical Lagrangians. A further theory-derived quantitative relation is needed to make such attribution testable.

