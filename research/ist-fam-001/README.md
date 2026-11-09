# IST-FAM-001 — Complete Source Audit and Bounded Route Closure

**Current status (November 9, 2026): EXECUTED — NO SOURCE SUPPORT for H1 and H2; bounded spectral-novelty stop rule invoked.**

The original two-hypothesis contract was frozen *before* execution at [commit 3661841](https://github.com/enuminous/papers/commit/3661841f69bb9dbd01338ee21f494d8d0b8ca7ce). [Boardy's tighter source-map/full-run requirements](PRE_EXECUTION_REVIEW_RULES.md) were committed separately **before the source scan** at [063565d](https://github.com/enuminous/papers/commit/063565de702d0cd1ac7c7eb090cb55ffe65f98d5). The original protocol and its original status fields are unchanged for audit integrity.

## Read the executed results

1. **[Full executed audit and bounded closure report](AUDIT_REPORT.md)** — read this first; both source-support hypotheses lack a justified mapping, with no physical claim.
2. [Verified machine-readable execution receipt](EXECUTION.json) — final run, artifact digest, source coverage, corrected lexical scan and decision.
3. [GitHub CI run 42676059594](https://github.com/enuminous/papers/actions/runs/42676059594) — 19 passing software tests, complete 717-record scan, exact seven-file upstream provenance checks.
4. [Original generated 717-row screening ledger and source verification artifact](https://github.com/enuminous/papers/actions/runs/42676059594/artifacts/13700690578) — \`ROW_SCREEN.csv\`, \`RESULTS.json\`, and \`SOURCE_FIDELITY.json\`. This artifact expires per GitHub retention rules and can be regenerated from the script.
5. [Runnable auditor](audit.py) · [tests](test_audit.py) · [workflow](../../.github/workflows/ist-fam-001.yml).
6. [Frozen original two-hypothesis protocol](PROTOCOL.json) · [pre-execution tightening](PRE_EXECUTION_REVIEW_RULES.md) · [historical referee discussion](../../IST-FAM-001-Referee-Review-and-Spectral-Novelty-Audit-2026-11-09.md) · [original pre-execution review ledger](REVIEW_LEDGER.json).

## Exact bounded outcome

| Item | Result |
|---|---|
| Frozen source statements screened | **717/717** (585 FieldSpace, 102 canonical, 30 additional pointers) |
| Original pinned Git source files | **7/7** matched by Git object identity |
| Original source text | **717/717** exact equality/line-fragment matches |
| Automated replay checks | **19/19 PASS** |
| Closely related source entries manually reviewed | **27** |
| Qualifying physically ordered oscillator-bath source maps | **0** |
| H1: source-derived full-run frequency ratios | **NO SOURCE SUPPORT** |
| H2: source-derived full-run weight ratios | **NO SOURCE SUPPORT** |
| New EFMW-specific gravitational evidence | **NONE** |

**Interpretation:** This is a clean bounded failure *to substantiate the source-support hypotheses*, not a theorem excluding all EFMW models or a failed physical experiment. A hypothetical golden-ratio-spectrum SOURCE PASS would describe an ordinary oscillator bath with constrained parameters; it would not independently support novel gravity.

The initial scanner mistakenly matched upper-case cosmological Ω as lower-case frequency ω (nine flags instead of two). The [corrected final CI run](https://github.com/enuminous/papers/actions/runs/42676059594) includes a regression test; the scientific outcomes were not changed.

## Decision and replay

**The original stop rule is now invoked for this particular spectral-novelty route.** Retain IST-001's conventional memory and reservoir mathematics, but do not use H1/H2 to motivate further costly gravitational-development phases without an independently sourced and discriminating physical prediction. The existing [UNITY-001 Phase 5 NOT READY](../unity-001/phase-5/PHASE5_REPORT.md) decision remains unchanged.

From the repository root at the audited [CI source revision](https://github.com/enuminous/papers/commit/49e5b61bce594c889f1b4ba5cffdaa116414631c):

~~~bash
python3 -m unittest discover -s research/ist-fam-001 -p 'test_*.py' -v
python3 research/ist-fam-001/audit.py --verify-upstream --out research/ist-fam-001/build
~~~

The first command tests software and ledger controls; the second retrieves the original seven files at immutable commits and generates row-level findings and source-fidelity receipts. Internet access is necessary for upstream replay. Original candidate expressions are preserved in the frozen source inventory but never treated as independent source proof. This review remains AI-assisted and is **not** independently certified peer review.
