# Exploratory multiscale extension: analysis specification

Date: 2026-11-07. Private review draft; publication requires Matthew's approval.
Base repository commit: `65f50f6710efa6801169429e5a5ad567f4d567d8`.
This specification is recorded before running new feature comparisons or outcome fits. The published B results and original source have already been inspected. This is not a preregistration, an untouched confirmatory sample, or an independent replication.

## Frozen feature set

At prediction time t, e[t-1] is the most recent signed angular prediction error (radians). For any scalar signal x, define E_r[x]_t=(1-r) sum_{k=1}^{n} r^(k-1) x[t-k], zero initialized separately in each block, without finite-window renormalization. n is the available history length. The original m=E_.5[e], Q=E_.5[e^2], B=E_.5[|e|], R=|m|/B. Q is an uncentered second moment, not a variance. A contrast means an explicitly specified difference of filtered signals or adjacent window means.

The primary conventional bank C has eight scalar features:

1. d=e[t-1]-e[t-2], and d^2 (local difference and its energy).
2. f=E_.25[e]-E_.5[e], and f^2 (fast versus intermediate exponential contrast).
3. s=E_.5[e]-E_.75[e], and s^2 (intermediate versus slower exponential contrast).
4. h=(e[t-1]+e[t-2]-e[t-3]-e[t-4])/2, and h^2 (a unit-norm, four-tap Haar detail and its energy).

The secondary magnitude bank A has two features: E_.25[|e|] and E_.75[|e|]. It asks whether a different ordinary magnitude-memory time scale competes with B. B itself is exactly a rectified signal passed through a first-order low-pass filter, not a uniquely EFMW mathematical operator. A is kept distinct from signed contrast/energy bank C.

The squared features are explicit nonlinear interactions; no spline knots or scales are selected for the new features. For pair analysis, histories are oldest first and evaluated immediately after their final element. All histories have at least four elements. For real data, all predictors are strictly prior to the current error and reset at block boundaries; retain the original five-observation burn-in.

## Exact constructed-history analysis

Run the published generator unchanged and compare generated pairs byte-for-byte. Use Fraction arithmetic to verify every published pair's multiset, m, Q and last two errors. Count pair differences for each feature, each bank and their union. Report mirrored rows separately from unique pairs modulo global sign, and provide all row-level values/differences. These are exhaustive descriptive counts for a selected stimulus bank, not independent human observations or evidence of human mechanism.

## Behavioral evaluation

Require both original OSF SHA-256 digests before fitting. Replay analyze.py and sensitivity.py unchanged into a separate output directory, compare every numerical leaf with the original outputs, and never overwrite published files.

Reuse the original five SHA-256-derived participant folds and original training-only spline/scaling basis; train on session 1 only and exclude the entire tested participant. Session 2 is a repeated visit of held-out participants, not a separate cohort. Use fixed Ridge(alpha=1), training-only standardization for additional features and the exact original eligible rows. No tuning, feature selection or outcome-based changes to scales. Report both confidence (focus) and signed adjustment (secondary).

Evaluate base, base+B, base+C, base+C+B, base+A, base+A+B, base+C+A and base+C+A+B. Report participant-weighted MSE and paired gains; primary new comparisons are C versus base and B conditional on C. Secondary A/full-bank contrasts address time-scale dependence. Retain every specified model, including losses. Also repeat confidence with the published stronger sensitivity baseline (|m|/sqrt(Q), slider start and current absolute adjustment) to assess behavioral cues.

Use 5,000 participant bootstrap samples, seed 20261106, for descriptive conditional 95% intervals, holding fitted predictions fixed. These omit training uncertainty, multiplicity and previous use of these data. Do not treat an interval crossing zero as proof of equivalence or an interval excluding zero as confirmatory significance. Report paired model comparisons directly rather than comparing separate intervals.

## Controls and interpretation

- Exact self-pair equality, global sign parity, constant-signal behavior and local-difference equality for matched last-two observations.
- Independent Fraction/direct-sum reference versus vectorized causal filters; future-error perturbations cannot change earlier predictions; histories reset for each block.
- Twenty deterministic within-block circular shifts (seeds 20261107 through 20261126) of each added bank B, C or A, with the original base and confidence target fixed. Train and held-out blocks are shifted separately by offsets at least five from either endpoint. Use the same permutation for columns within each bank. Compare observed gain with the full descriptive range of shifted gains in both sessions. These shifts are a pipeline/alignment diagnostic, not a valid conditional permutation test or a p-value: they disturb covariate dependence and wrap boundaries.
- Verify all original files still match their retrieved blob digests, and patch adds only the extension directory.

An ordinary feature distinguishing constructed pairs rejects isolation of B by the original matching controls; it does not establish what people use. Improved held-out prediction supports that specific predictive competitor only. A remaining B gain does not identify an EFMW-specific mechanism. A loss of B gain does not disprove all absolute-error memory. No finite feature bank exhausts conventional explanations, and all results remain exploratory.
