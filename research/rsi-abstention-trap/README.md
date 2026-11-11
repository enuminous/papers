# The Abstention Trap — research package

**Published November 11, 2026 · Matthew Chenoweth Wright / Monolithic LLC**  
**Status:** Retrospective RSI-SYNTH-001 benchmark audit and prospective evaluation proposal; not independent replication or new confirmatory results.

The package re-examines a finite-policy synthetic recursive-improvement demonstration and derives a crucial negative-control result: a constant `UNRESOLVED` response scores 340/384 on the public holdout without supplying any answers. The original candidate correctly supplied all 44 answerable labels and abstained on the 340 remainder, but its PASS criteria did not require that behavior, and a conventional oracle-aware rule achieved the same 384/384 ceiling.

## Files

- [PAPER.md](PAPER.md) — 2,100-word research note, original counts, methodological analysis, and limitations
- [analysis.py](analysis.py) — Python standard-library offline source inspection and always-abstain counterfactual
- [PROPOSED-GATE.md](PROPOSED-GATE.md) — successor RSI-EVAL-002 design proposal; **not approved, frozen or run**

## Source and replay

Pin the original RSI repository at commit `478908589847ab10038a80fd50df35478c0ec95f`. The archive is not privately held or independently blinded. The following assumes the two checkouts sit side-by-side:

```sh
git clone https://github.com/enuminous/papers.git
git clone https://github.com/enuminous/RSI.git
cd RSI
git checkout 478908589847ab10038a80fd50df35478c0ec95f
cd ../papers
python research/rsi-abstention-trap/analysis.py --self-test
python research/rsi-abstention-trap/analysis.py --snapshot-dir ../RSI/examples/frozen_demo
```

The program verifies the snapshot counts and calculates a deterministic paired-case-bootstrap interval for always-abstain versus the historical initial baseline. It does not change the source package, run an independent confirmatory experiment, or claim an RSI-specific mechanism.

## Decision boundaries

- Original historical result: **PASS under original synthetic gate**, preserved unchanged.
- The abstention-control finding: **DERIVED retrospectively from the public data**.
- Unique recursive benefit over strong ordinary methods: **UNRESOLVED**.
- Autonomous recursive modification of AI model weights or AGI: **NOT ESTABLISHED**.
- RSI-EVAL-002: **PROPOSED / NO EXTERNAL CUSTODIAN / NO SEALED RUN**.

The analysis and the new gate remain separate from the frozen original `RSI-SYNTH-001` artifacts.
