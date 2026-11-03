# EFMW Physical Validation: A Falsifiable Research Roadmap

**Date:** 2026-11-03  
**Author:** Matthew Chenoweth Wright / Monolithic LLC  
**Document type:** prospective research protocol, not an empirical finding  
**Status:** PROPOSED — physical validation UNRESOLVED

## Executive objective

Identify at least one dimensionally specified, noncircular relation from *defined* EFMW (Einstein–Feynman–Maxwell–Wright / Entangled Field Memory Waveform) variables to an independently measurable physical observable; register a discriminating prediction before testing; compare it against strong established-theory models; and obtain independently reproducible external evidence.

**Success is not guaranteed.** A null result, equivalence to established theory, or failure of identifiability is a legitimate outcome.

## 1. Evidence boundary

Distinguish (a) definitions and conjectures, (b) mathematical derivations, (c) Lean-checked conditional theorems, (d) simulations, (e) physical predictions, (f) measurements, and (g) independent replications. None implies the next without additional evidence. Existing EFMW numerical experiments in monitoring/AI assurance do not establish a new physical law. No EFMW-specific independently replicated physical effect is asserted here.

## 2. Phase I — Source and dimensional inventory (weeks 1–4)

1. Pin exact commits, Lean version, Mathlib revision, datasets and dependencies for EFMW, the Monolithic 102, Phase-Vorticity-Lab, Geometry and relevant physics labs.
2. Extract candidate primitive variables into a ledger: symbol, exact source equation, mathematical domain, SI dimensions, operational measurement map, initial/boundary conditions, free parameters and assumptions.
3. Classify every relation as definition, derived theorem, modeling ansatz or empirical law. Identify any imported standard-physics identity.
4. Run a dimensional audit of every sum, derivative, action, coupling and proposed observable. Require invariance under a consistent change of units.
5. Trace dependency graphs from observable back to assumptions; flag any insertion of the observed target, data leakage or fitted outcome.

**Gate G1:** PASS only if one fully defined candidate relation has consistent dimensions and a reproducible source chain; FAIL for contradictory units or circular dependence; otherwise UNRESOLVED. Deliver: `variables.csv`, `equation-provenance.md`, `dimensional-audit.md`.

## 3. Phase II — Derive an identifiable prediction (weeks 5–8)

Priority candidate: phase/current/vorticity, because there are established observables and stringent comparators. For a normalized 3D nonrelativistic wavefunction, the conventional baseline is

`psi = rho exp(i theta)`, `j_QM = (hbar/m) rho^2 grad(theta)`.

Here `theta` is dimensionless, `rho^2` has dimensions m^-3, and `j_QM` has dimensions m^-2 s^-1. This is **standard quantum mechanics**, not an EFMW prediction. For electromagnetic or condensate systems, use the correct gauge-covariant current and normalization instead.

The research task is to **derive**, not invent, an EFMW-specific correction `Delta j_EFMW` from pinned EFMW dynamics such that `j_EFMW = j_baseline + Delta j_EFMW`, with units m^-2 s^-1 in this chosen setting. Specify its gauge behavior, continuity equation, domain of applicability and limiting behavior. If no correction follows, report equivalence or non-identifiability; do not attach an arbitrary free coefficient to manufacture novelty.

Candidate observable: a predeclared interference fringe shift or spatial flux distribution, with a forward model for instrument response. Alternative branches: gravitational-wave memory against GR, rotational sky statistics against LCDM plus anisotropic models, or circulation against fluid/quantum hydrodynamics. Advance **one** branch only after G1.

**Gate G2:** PASS requires an observable function `y=f_EFMW(x;theta)` with identifiable parameters, stated units, a no-target-data derivation and a numerical prediction distinguishable from baseline under feasible uncertainties. Otherwise FAIL or UNRESOLVED. Deliver: `candidate-law.md`, `identifiability.ipynb`, `predictions.json`.

## 4. Phase III — Strong baselines and preregistration (weeks 9–12)

Choose the strongest domain-appropriate established comparator: Schrödinger/Pauli/QED with instrument effects for phase experiments; GR waveform models for gravitational waves; LCDM and appropriate anisotropic cosmologies for sky tests. Include systematic-error models, realistic noise, nuisance parameters and at least one plausible non-EFMW alternative.

Partition calibration data and held-out test data **before** examining outcomes. Freeze source revisions, fit parameters, prediction intervals, exclusion rules, primary statistic, sample-size/power rationale, null controls, alternative models and stopping rule. Forbid refitting on the holdout. Publish a timestamped preregistration and hashes. Report both absolute fit and incremental improvement over the strongest baseline, with uncertainty and complexity penalties.

**Gate G3:** PASS if the preregistration is complete, testable and frozen before holdout access; otherwise UNRESOLVED. Deliver: `preregistration.md`, `analysis-plan.md`, `environment.lock`.

## 5. Phase IV — External measurement and blind test (months 4–6)

Use an external, provenance-verifiable dataset or a genuinely independent laboratory. Record original acquisition links, licenses, calibration and selection functions, raw checksums, observation timestamps, preprocessing and access history. For public archival data already inspected, explicitly acknowledge that the test is retrospective rather than blind; prefer a newly released holdout or prospective acquisition.

Run baseline and EFMW predictions under identical information budgets. Publish effect size, confidence/credible intervals as appropriate, residual diagnostics, sensitivity to nuisance assumptions, negative controls and every failed or excluded run. Do not use statistical significance alone as proof of physical novelty.

**Gate G4:** PASS requires a prespecified discriminating prediction supported by external measurements and robust to reasonable systematics; FAIL if contradicted; UNRESOLVED if precision is insufficient. Deliver: `external-data-manifest.md`, `results.md`, reproducible code and machine-readable outputs.

## 6. Phase V — Independent replication (months 6–12+)

Invite an unaffiliated group to reconstruct the prediction from the frozen specification and evaluate a distinct dataset or apparatus. They must independently check dimensions, assumptions, calibration, baselines and the statistical analysis. Record disagreements and unsuccessful attempts without selective omission.

**Gate G5:** PASS only after documented independent replication of the EFMW-specific discriminating result. One favorable retrospective fit is insufficient. Deliver: external replication report, independent code/data identifiers and a discrepancy log.

## 7. Decision matrix

| Result | Scientific disposition |
|---|---|
| Undefined variables or inconsistent units | FAIL; repair formulation before physical claims |
| Circular target dependence | FAIL; redesign derivation and split |
| Exact recovery of known physics | Mathematical/implementation consistency only; no novel physical validation |
| No identifiable difference from comparator | Report non-identifiability or observational equivalence |
| Better simulation fit only | Computational finding, not external physical confirmation |
| External test inconclusive | UNRESOLVED; report precision limit |
| External result contradicts frozen prediction | FAIL for the tested hypothesis/domain |
| One external positive test | Preliminary empirical support, not established replication |
| Independent successful replication | Stronger evidence, subject to further systematic and theoretical review |

## 8. Mandatory reporting schema

Each candidate receives: `candidate_id`, pinned `source_commit`, `source_equations`, `variable_definitions`, `SI_dimensions`, `assumptions`, `derivation`, `measurement_map`, `baseline_models`, `free_parameters`, `calibration_data`, `heldout_data`, `prediction_freeze_timestamp`, `primary_metric`, `uncertainty_model`, `null_controls`, `outcome`, `independent_reviewer`, `status` (PASS/FAIL/UNRESOLVED), and `limitations`. Unknown fields must be marked **UNKNOWN**, not silently filled.

## 9. Immediate next actions

1. Audit the canonical EFMW equations and Phase-Vorticity-Lab for one source-pinned phase/current law.
2. Produce the SI-unit and dependency ledger, identifying exactly which quantities are assumed and which are derived.
3. Attempt one observable prediction with zero parameters fitted to its own validation set.
4. Have an external quantum/field-theory reviewer challenge the derivation before collecting or opening held-out outcomes.

## 10. Publication language

Until G5 is passed, describe EFMW as a **research program** and candidate relations as hypotheses or conditional results. Never label a Lean theorem an experimental confirmation, a numerical illustration an independent measurement, or a successful fit proof of a new law. Retain null results and provenance. This roadmap is a study plan, not a claim of physical validation.

## Reference resources

- NIST CODATA physical constants: https://physics.nist.gov/cuu/Constants/
- Gravitational Wave Open Science Center: https://gwosc.org/
- Canonical source repository: https://github.com/enuminous/EFMW
- Related laboratory: https://github.com/enuminous/Phase-Vorticity-Lab
