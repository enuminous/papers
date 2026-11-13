# EFMW-INT-001 Pilot 60

**Release:** `pilot-60-v1`  
**Freeze date:** 2026-11-13  
**Status:** Synthetic pilot corpus frozen; system-comparison result **UNRESOLVED / NOT RUN**  
**Use:** Instrument and corpus-construction pilot only; not confirmatory evidence

This release contains 60 synthetic inference pipelines. Each item has a claim, evidence, provenance, and inference procedure. Thirty contain exactly one intentionally planted defect and thirty are clean. There are 30 matched pairs: each pair shares a defect family and domain slot, with a clean counterpart designed to look superficially concerning in some cases. The exact keys are public in `labels.csv` in this release.

Parent protocol: [`EFMW-INT-001` 300-pipeline preregistration](../../EFMW-INT-001-Preregistered-Audit-Benchmark-Protocol-2026-11-13.md). This pilot does not amend or satisfy that protocol.

## Defect families

| Family | Positive items |
|---|---:|
| Omitted confounder | 5 |
| Miscovering nominal interval | 5 |
| Changed cited source | 4 |
| Weak formal statement | 4 |
| Withdrawn authorization | 4 |
| Post-result benchmark retuning | 4 |
| Shared-source repetition | 4 |
| **Total** | **30** |

## Files

- `items.jsonl`: blinded-format pipeline records, with opaque IDs and no ground-truth label.
- `labels.csv`: item labels and defect families; released with the pilot, so this is no longer a sealed holdout.
- `generate.py`: deterministic synthetic-corpus generator, seed `20261113`.
- `validate.py`: structural and hash validation; does not evaluate an audit arm.
- `freeze.json`: release metadata and status.
- `PILOT-60-RESULTS.md`: outcome and limitations.
- `SHA256SUMS`: hashes for the frozen items, labels, scripts, and report.

Run `python3 validate.py` from this directory. Expected construction result: 60 unique items, 30 defect-positive, 30 clean, 30 complete pairs, and the family allocation above. The validator does not score a model or audit workflow.

## What this release can establish

It can establish that the synthetic records and labels have the stated counts, pair structure, family allocation, and file hashes. It can support software-interface checks and exploratory debugging of scoring code.

It cannot establish comparative audit performance, external validity, real-world defect prevalence, or an advantage for recursive auditing. The records are author-generated and deliberately templated; no independent ground-truth adjudication, custodian, arm execution, or blinded scoring is reported. Publication of the label key burns this corpus for any later blind evaluation. A confirmatory study needs a newly generated corpus, an independent custodian, executable frozen arms, and the unresolved preregistration decisions in the parent protocol.

The pilot does not revise or satisfy the separate 300-pipeline confirmatory protocol. No arm result should be inferred from the construction `PASS`.
