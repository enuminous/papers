# RSI-EVAL-002 — Proposed coverage-aware evaluation gate

**Status:** PROPOSED / NOT FROZEN / NOT APPROVED / NOT RUN  
**Prepared:** November 11, 2026 · Monolithic research methods note  
**Supersedes:** Nothing. RSI-SYNTH-001 v1.0.0 remains immutable as a historical synthetic demonstration.

## Problem

The historical RSI-SYNTH-001 gate requires an accuracy gain over a deliberately weak starting policy, no increase in wrong assertions, and a positive paired-bootstrap lower bound. It does **not** require a correct answer to any answerable case. On the archived 384-case holdout, the constant `UNRESOLVED` policy correctly labels 340 cases with zero assertions and zero false assertions. It can meet the historical gate although it provides no substantive answers.

This proposed protocol is not retrospectively applicable to the original frozen experiment. Its thresholds are examples for prospective review, not approved benchmark results. A new experiment needs a new identifier, unseen data, and independent custody.

## Units, labels, and denominators

- A **case** is a separately adjudicated claim-evidence question with one gold label: `SUPPORTED`, `CONTRADICTED`, or `UNRESOLVED`.
- **Answerable** means gold `SUPPORTED` or `CONTRADICTED`; **unanswerable** means gold `UNRESOLVED`.
- **Correct assertion:** candidate outputs the correct non-`UNRESOLVED` label.
- **False assertion:** candidate outputs a non-`UNRESOLVED` label that differs from gold.
- **Correct abstention:** candidate outputs `UNRESOLVED` and gold is `UNRESOLVED`.
- **Assertive coverage:** all non-`UNRESOLVED` outputs divided by **all cases**.
- **Answerable recall:** correct assertions divided by **answerable cases**.
- **False-assertion rate:** false assertions divided by **all cases**; additionally report false assertions / all assertions (undefined if no assertions).
- **Unanswerable specificity:** correct abstentions divided by **unanswerable cases**.
- **Accuracy:** all correct outputs divided by **all cases**, always displayed with class prevalence and the above measures.

All denominators and class counts must accompany percentages. A model that never answers has zero answerable recall, even if its overall accuracy is high.

## Proposed gates (require pre-registration before use)

This is a *prospective design draft*. The following numbers are suggested starting points, **not an adopted standard**.

1. **Usefulness:** answerable recall at least 90% *and* assertive coverage at least 10%, with balanced evaluation across evidence families; each class must have sufficient independently reviewed representation to make this meaningful.
2. **Risk:** false-assertion rate at most 5% of all cases, and report the conditional false-discovery fraction among asserted responses. Publish worst-family results.
3. **Nontriviality:** explicitly include the always-`UNRESOLVED` comparator, random search, a transparent coverage-matched rule-based policy, and the strongest pre-specified conventional search/evidence policy. Passing above the constant policy is necessary but insufficient.
4. **Incremental value:** at equal total evaluation and search budget, achieve at least a five-percentage-point improvement in correct-answer rate over the strongest conventional method at matched assertive coverage (within two percentage points), with the lower paired 95% confidence bound above zero. Use independent evidence-family units for resampling, not individual paraphrases or tokens.
5. **Stability:** report at least 30 predeclared independent search seeds, prespecified distribution shifts and negative controls, and the full failure count. Select no favorable seed ex post.
6. **External validity:** maintain a blind, unopened confirmation set controlled by an independent named custodian; sealed task construction must be separated from search, prompting, parameter adjustment, analysis, and scoring.
7. **Oversight:** precommit complete protocol, hashes, budget, score script, model/source revision and exclusion rules; independently timestamp the freeze commit; have independent scorers lock labels before unblinding; release all outcomes including FAIL and UNRESOLVED.

**Mandatory safeguards:** Do not make an unattainable requirement silently disappear. If an oracle-aware rule already reaches 100% on a transparent synthetic task, no optimizer can demonstrate a five-point improvement over it; the claim of incremental superiority fails on that task, even if optimization is correctly implemented.

The exact 90% / 10% / 5% / 5-point / 2-point / 30-seed choices require feasibility and statistical-power analysis *before* approval or any sealed test. A future protocol may adopt different predeclared values with rationale. A protocol amended after viewing holdout outcomes needs a fresh independent test, not an edited historical PASS.

## Custody and freeze procedure

1. Register a protocol-only source commit; publish its immutable commit ID and a digest with an external timestamping service or outside reviewer.
2. Before any held-out model calls, have a **named consenting independent custodian** produce/hold the sealed tasks and gold; retain documented provenance, rights and evidence-family independence.
3. Freeze evaluator, prompts, search budgets, conventional baselines, provider/model versions, seeds, cost and latency reporting.
4. Run all predeclared arms on the untouched held-out set. Record raw responses, exact decision traces, hashes, exceptions, failures and review notes.
5. Independent assessors blind-score outputs, resolve disputes prospectively and unblind only after the scoring record is locked.
6. Publish results for every arm, including conditions that miss the gates. An independent operator reproduces analysis from archived bytes.

**Custodian status:** NOT APPOINTED. No independent party has agreed to hold new sealed tasks. The public RSI-SYNTH-001 seeds are not usable as fresh blinded evaluation data.

## Status crosswalk

| Artifact | Status | Meaning |
|---|---|---|
| RSI-SYNTH-001 report.json | `PASS` (unchanged) | Historical synthetic gate met |
| RSI-SYNTH-001 broader RSI assertion | `UNRESOLVED` | No unique recursion advantage or transfer established |
| Always-`UNRESOLVED` counterfactual | `EXPLORATORY_DERIVED` | Computed from existing archived cases; not an executed search arm |
| RSI-EVAL-002 | `PROPOSED_NOT_FROZEN` | No sealed tasks, approvals, or evaluation |
| General AGI/self-modifying foundation model | `NOT_ESTABLISHED` | Not evaluated by this synthetic package |

## Clear failure conditions

- A constant-abstention policy is competitive and the candidate cannot improve useful answers while controlling false assertions.
- After matching assertive coverage and resources, conventional rule-based or nonrecursive methods meet or exceed candidate performance within the preregistered confidence bound.
- Gains disappear across untouched evidence families, under reasonable negative controls, or across the specified seed distribution.
- Independent custody, protocol freeze, source/version verification, or scorer blinding cannot be established.

A gate can FAIL even if a demonstration's original PASS remains true. The whole purpose is to make that distinction measurable.

## Reading order

- [Paper — The Abstention Trap](PAPER.md)
- [Reanalysis code](analysis.py)
- [Archived original RSI report](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/examples/frozen_demo/report.json)
- [Original frozen protocol](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/docs/protocol.md)
