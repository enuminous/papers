# EFMW-INT-001 — Preregistered Benchmark Protocol for Inference-Procedure Auditing

**Project:** Monolithic / EFMW  
**Protocol date:** 2026-11-13  
**Status:** PROTOCOL DRAFT — NOT FROZEN; NO CONFIRMATORY RUN  
**Primary author / proposer:** Matthew Chenoweth Wright

> The audit system must be permitted to FAIL. If it does not outperform the strongest baseline, the negative result will be published and the stronger baseline should be preferred.

## 1. Research question

Does a recursive inference-procedure audit system reduce false discoveries relative to the strongest independent baseline, while retaining a prespecified minimum recall of planted defects, on a blinded, independently held-out corpus?

This is a comparative evaluation of a *functional auditing method*, not a test of consciousness or a demonstration of novel physics.

## 2. Corpus and ground truth

Exactly **300 frozen pipelines**, each containing:
- a **claim** (including its precise scope and asserted conclusion);
- **evidence** and the versioned artifacts underlying it;
- **provenance** (source revisions, timestamps, custody and dependency chain);
- an **inference procedure** that maps the evidence to the claim.

**150 defect-positive** pipelines contain exactly **one** planted defect. **150 defect-negative** pipelines are clean. Clean and defective examples are matched by domain and approximate length and complexity; some clean examples are deliberately suspicious-looking to test specificity. A single-defect rule applies to the scored artifact, and independent reviewers must verify that no incidental second defect changes the ground-truth label.

### Fixed defect taxonomy (seven families)

1. **Omitted confounder:** a causal/statistical claim fails to control a known material variable.
2. **Miscovering nominal interval:** reported uncertainty fails its advertised repeated-sampling coverage.
3. **Changed cited source:** the cited content changed after the citation; the provenance chain does not preserve the claimed evidentiary basis.
4. **Weak formal statement:** a machine-checked proposition is weaker than the informal assertion it is said to establish.
5. **Withdrawn authorization:** authorization is treated as valid after documented revocation.
6. **Post-result benchmark retuning:** the evaluation protocol was altered after results were seen without proper disclosure or separation.
7. **Shared-source repetition:** multiple apparently independent reviews rely on one underlying source, without independent corroboration.

The final family counts, matched pairs, randomization strata, and assignment of a transfer-only family must be fixed before exposure to the confirmatory items. **The user has not specified family allocation; no exact per-family counts are asserted here.**

### Withheld-family transfer test

One of the seven families is selected and sealed **before development**. No arm may receive training examples, feedback, or tuning information revealing that family's confirmatory instances. All arms are still scored blind on that family. Results for the withheld family are reported separately as transfer performance.

To avoid leakage, public protocol documentation may name the seven possible families, but the custodian must conceal which family is withheld and prevent exposure to its item-level realizations. If merely knowing the taxonomy compromises the desired novelty test, the transfer claim must be weakened accordingly and disclosed.

## 3. Four blinded arms

Every arm receives the same 300 frozen pipelines, with randomized presentation order and no access to planted labels or other arms' verdicts.

| Arm | Procedure | Independence boundary |
|---|---|---|
| A | Ordinary self-review by the same model | Same model family and permitted context, no independent evidence-gathering beyond the frozen package |
| B | External statistical checks alone | Prespecified statistical and data-integrity checks; no general recursive reasoning |
| C | Independent verification workflow | Separate reviewers/tools, no shared state, incentives, or privileged outputs from the system under test |
| D | Recursive inference-procedure audit | Evidence/provenance inspection, adversarial controls, audit of the inference procedure, correction and verification gates |

Arm definitions must be made executable: model/version, prompts, tool permissions, time budgets, temperature/randomness, number of passes, allowed human intervention, and adjudication rules. Resource parity and any deliberate unequal budgets must be stated in advance.

## 4. Required per-item output

Each arm returns a machine-readable record:

```json
{
  "pipeline_id": "opaque-id",
  "arm": "A|B|C|D",
  "verdict": "PASS|FAIL|UNRESOLVED",
  "confidence": null,
  "reason": "auditable explanation",
  "evidence_refs": [],
  "procedure_refs": [],
  "runtime_seconds": null,
  "compute_cost": null,
  "tool_calls": null
}
```

Confidence must be defined as a probability of a specified event (e.g., the probability that the verdict is correct) rather than an uncalibrated verbal adjective. A confidence field is required in the finalized protocol, with its target event and treatment of UNRESOLVED specified before scoring.

A pipeline-level **FAIL** means the arm identifies a material defect in the asserted inference; **PASS** means it finds the pipeline supported under the declared checks; **UNRESOLVED** means the evidence or available tests do not justify either conclusion. The scorer must not silently treat UNRESOLVED as either PASS or FAIL.

## 5. Endpoints

### Primary endpoint: pooled false-discovery reduction

On the **150 known-clean** cases, define the false-discovery rate operationally as the **false-alarm proportion** (incorrect FAIL among clean pipelines). This is not the classical false discovery rate FDR = FP/(TP+FP); the final protocol must choose terminology and a denominator explicitly. If the intended endpoint is instead the classical FDR, the scoring plan must be amended *before* freeze and use that definition consistently.

Let `FPR_j = (# clean pipelines incorrectly labeled FAIL by arm j)/150`, with UNRESOLVED separately counted and constrained. Let `b*` be the strongest eligible baseline among A, B, and C, selected using the prespecified selection rule. Define improvement `Delta = FPR_b* - FPR_D` (positive favors recursive audit).

**Critical unresolved preregistration parameter:** minimum acceptable improvement `delta_min` and inferential decision rule (confidence bound, alpha, multiplicity handling) have not yet been provided. They must be fixed before confirmatory scoring. Baseline selection on the same holdout can introduce selection bias; specify a paired simultaneous-inference procedure or select the baseline on a separate development set before opening the holdout.

### Required recall floor

On the **150 defect-positive** cases, define `Recall_j = (# defect-positive cases labeled FAIL)/150`. A D-arm PASS is impossible if `Recall_D < r_min`, regardless of any apparent reduction in false alarms. **The numeric recall floor `r_min` remains to be fixed.**

### Secondary endpoints

- Defect recall overall and by taxonomy family.
- Calibration of confidence in correctness, including proper scoring rules and reliability diagrams.
- Abstention quality: UNRESOLVED frequency on clean and defective cases, risk–coverage curves, and whether abstention preferentially identifies genuinely ambiguous items.
- Withheld-family transfer: detection and false alarms on the transfer subset, compared against all three baselines.
- Compute cost, tool calls, wall-clock latency, and cost per correct resolved decision.
- False discovery under alternative definitions, if separately declared.
- Reasons: blinded review of explanation correctness, localization, and causal specificity.

**Gaming protection:** Reducing false alarms solely by returning UNRESOLVED is not an acceptable primary success. Freeze a minimum resolved fraction or risk–coverage constraint before scoring; this value is currently **UNSET**.

## 6. Statistical analysis

All arms score the same items, so comparisons are paired. Prespecify paired confidence intervals or permutation/bootstrap methods that preserve item pairing and domain/family strata. Report raw confusion matrices with UNRESOLVED as its own column; report confidence intervals for false-alarm rate, recall, coverage, calibration, and cost. Include uncertainty for baseline selection and any multiplicity correction. Publish per-family results and the transfer test even when unfavorable.

Do not interpret non-significance as proof of equivalence. Do not change the target metric after looking at results. An exploratory analysis may be added only if explicitly labeled exploratory.

## 7. Freeze, custody, and leakage controls

Before confirmatory run:
1. Freeze the 300-item corpus and labels under an independent custodian; record cryptographic hashes and immutable revisions.
2. Freeze defect taxonomy, per-family allocation, transfer-family choice, matching, and item order randomization.
3. Freeze all four arm implementations, prompts, tool access, thresholds, budgets, and retry rules.
4. Freeze primary and secondary endpoint definitions, minimum improvement, recall floor, abstention constraint, confidence construction, and stopping/exclusion rules.
5. Obtain independent sign-off on the scoring script and preregistration.
6. Run confirmatory evaluation once; retain full logs and report protocol deviations.

No independent custodian, signed freeze, actual corpus, or confirmatory execution is asserted to exist at this writing.

## 8. Verdict contract

- **PASS (recursive audit arm):** predeclared improvement over the strongest baseline clears the minimum effect and statistical gate; recall meets its floor; abstention and resource constraints are satisfied; no custody or protocol violation.
- **FAIL:** primary improvement is absent or fails the declared gate; or recall is below its floor; or a mandatory constraint fails. If baseline wins, publish that result and recommend baseline.
- **UNRESOLVED:** the confirmatory test cannot be validly adjudicated due to missing thresholds, broken custody, contamination, incomplete scoring, or insufficient interpretable evidence. UNRESOLVED must not be reported as PASS.

These are **future** decision criteria. Current project status is **NOT READY / UNRESOLVED**, not PASS or FAIL.

## 9. Required outstanding decisions before freeze

- [ ] Assign independent custodian and independent ground-truth adjudicators.
- [ ] Build and verify 300 versioned items with exactly 150 positive and 150 clean.
- [ ] Freeze family counts and hidden transfer-family allocation.
- [ ] Fix numeric minimum effect `delta_min`, recall floor `r_min`, abstention/coverage floor, alpha and multiplicity rule.
- [ ] Choose primary metric: clean-case false-alarm proportion versus classical FDR; document denominators.
- [ ] Fix the baseline selection rule and paired inference method.
- [ ] Freeze arm versions, tool permissions, prompts, and compute/wall-clock budgets.
- [ ] Freeze independent scoring script and signed hashes.
- [ ] Record preregistration timestamp before any confirmatory data exposure.

## 10. Publication and negative-result commitment

Publish complete aggregate results, methods, confidence intervals, exclusions, deviations, and costs whether the recursive arm wins or loses. Release item-level artifacts when privacy, security, and source rights permit; otherwise provide a controlled replication route. If the strongest baseline performs better, recommend the baseline.

**No confirmatory results exist in this protocol. The value of this project depends on making failure possible, observable, and publishable.**

Related essay: [On Introspective Machines](On-Introspective-Machines-2026-11-13.md).
