# EFMW-INT-001 Pilot 60 — Results and Decision

**Date:** 2026-11-13  
**Release:** `pilot-60-v1`  
**Status:** Corpus construction **PASS**; comparative audit performance **UNRESOLVED / NOT RUN**

## Question answered

This release answers whether a small, fully synthetic pilot corpus can be packaged with the intended pipeline fields, balanced labels, matched pairs, fixed defect families, and reproducible integrity checks. It does **not** answer whether recursive auditing outperforms any baseline.

## Construction outcome

| Check | Outcome |
|---|---|
| Unique pipeline records | 60 — PASS |
| Defect-positive / clean balance | 30 / 30 — PASS |
| Complete defect/clean matched pairs | 30 — PASS |
| Fixed defect families represented | 7 — PASS |
| Family allocation | 5, 5, 4, 4, 4, 4, 4 positives — PASS |
| Generator and validator hashes | Verified — PASS |
| Four-arm evaluation | NOT RUN |
| Comparative performance conclusion | UNRESOLVED |

The construction checks were run with `python3 validate.py` against the released files. These checks establish corpus structure and file integrity only.

## Why no arm verdict is reported

The four-arm protocol requires executable, frozen versions of ordinary model self-review, external statistical checks, independent verification, and recursive audit, plus fixed budgets and a scoring rule. This pilot environment had no independent custodian or independent ground-truth adjudicators, and the four arm implementations were not frozen or executed. The same authoring workflow generated the synthetic cases and labels. Calling any resulting self-score blind, independent, or confirmatory would be inaccurate.

The only valid benchmark-level verdict is therefore **UNRESOLVED**. This is not a failure of the recursive system; its comparative performance was not measured. It is also not a success. No false-alarm, recall, calibration, abstention, transfer, or cost estimate is claimed.

## Interpretation

The corpus-construction pilot passes its limited engineering objective. The audit-performance question remains open. Because `labels.csv` is released with the corpus, these 60 records are permanently unsuitable as a sealed holdout. Any confirmatory evaluation must use a new corpus, independent custody and adjudication, and the still-open thresholds and statistical decisions in the parent protocol.

No physical claim about EFMW is evaluated by this pilot.
