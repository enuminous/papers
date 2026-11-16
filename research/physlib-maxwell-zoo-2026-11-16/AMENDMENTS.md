# Preserved execution corrections

These are audit-harness/setup corrections, not modifications to Physlib or the Zoo's mathematical statements. Initial logs are retained.

1. Zoo `lake build zoo46 regression` does not build its separately registered extension roots. The first `Audit.lean` invocation therefore failed to find `Extensions.olean`. Running the documented default `lake build` resolved that setup omission; the subsequent axiom audit passed.
2. An explicitly scoped PATH included `python3` but not the environment's `python` alias. The first Zoo rejection-control launch failed with `python: command not found`; rerunning with `python3` passed. No target result was inferred from the failed launch.
3. Local `Audit.lean` initially used an incorrectly parenthesized quoted Lean name and an unconstrained counter type. It failed compilation. Correcting the name expression and declaring the counter `Nat` produced the complete passing four-root trace. The strict three-axiom policy was unchanged.
4. The first local zero-field witness needed `timeSlice` unfolded and `contDiff_const` used explicitly. Its elaboration failed and Lean reported `sorryAx` in the failed declaration. That attempt is not a proof. The corrected witness compiled with warnings treated as errors and its final axiom list contains only the three allowed foundational axioms.
5. The native-computation rejection control initially expected the Lean 4.19 spelling `Lean.ofReduceBool`. Lean 4.35 instead reports `AuditProbe.good._native.native_decide.ax_1_1`. The strict scanner rejected it on the first run, but the harness's diagnostic-string assertion failed. Version 2 changes only that assertion to expect `native_decide`, retaining the nonzero exit and `Unapproved axiom` requirements. Only this changed control is rerun; original input hashes, results and logs remain available. This is a toolchain-adaptation correction, not a new acceptance rule for Physlib.

The separate Zoo `verify.py` checksum failure is **not corrected or suppressed**: at the pinned revision, README.md differs from its recorded manifest hash. All 80 manifest entries were checked individually; only that entry differs.

6. CIRCUS first returned N/A while external review was pending. After the static manifest failure was identified, the final ledger adds that observed material release-integrity risk. The unchanged fixed CIRCUS procedure returns FAIL. The initial input/result are preserved; no gate threshold was changed. This FAIL concerns the audit tool release, not Physlib's theorem validity.
