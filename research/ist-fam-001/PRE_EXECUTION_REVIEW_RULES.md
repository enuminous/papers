# IST-FAM-001 — Pre-execution review rules (separate from frozen v1)

**Date:** 2026-11-09  
**Decision:** Added after the original [v1 protocol](PROTOCOL.json), in response to the author's explicitly approved Boardy-relayed critique, **before the new complete source scan**. The original v1 file remains byte-for-byte unchanged. This document is an **auditable tightening**, not a claim of external preregistration or blind analysis.

## Rule A — Source-to-bath map first

For either H1 or H2, the pinned source must **itself** specify the entities corresponding to physical bath modes and a physically meaningful map into the frequencies \(\omega_j\) (and, for H2, weights \(b_j=z_j\omega_j^2a_j^2\)). A source must fix the mode indexing and order independently of the hypothesized ratios. A definition chosen only to make the proposed equality true, a mapping selected after inspecting frequencies, or a free choice of modes cannot count as SOURCE PASS.

*If the source mapping is absent or ambiguous, record the precise gap. A complete bounded scan with no qualifying derivation is NO_SOURCE_SUPPORT; if source provenance cannot be checked or the scan is incomplete, UNRESOLVED. Do not treat lack of evidence as a mathematical counterexample.*

## Rule B — Full source-defined sequence, not three cherry-picked points

The v1 mention of a “prespecified consecutive triple” is a minimum for candidate definition, **not** a window that can be selected from a longer sequence. If the original source itself specifies an ordered run \(j=1,\ldots,N\) with \(N\ge3\), require H1, and separately H2, **for every adjacent pair** throughout that entire run:

\[
\omega_{j+1}/\omega_j=\varphi,\qquad
b_{j+1}/b_j=\varphi^{-2},\quad j=1,\ldots,N-1.
\]

The run endpoints and order must be source-defined before evaluating ratios. An unordered multiset does not qualify. No numerical “near-φ” tolerance is introduced to rescue patterns: claims of approximate equality require a separately justified source-derived exact error model and remain outside these v1 hypotheses.

## Rule C — H2 exponent was guessed

The choice \(-2\) was a **speculative authored guess** motivated by earlier golden-ratio/Scalar-23 themes; the protocol did not cite a source derivation of this exponent. Freezing a guess avoids retuning but does not make it a theoretically sourced constraint. If the corpus lacks an independent derivation linking its physical bath weights to \(\varphi^{-2}\), report NO_SOURCE_SUPPORT. A formula defined with the desired exponent does not qualify.

## Rule D — PASS is not novel gravity

**In the same paragraph as any possible H1 or H2 SOURCE PASS**, explicitly state:

> This result would define a conventionally realizable oscillator bath with golden-ratio-spaced frequencies or weights. It does **not** establish a uniquely EFMW informational stress tensor, new gravitational interaction, or independent physical validation.

A conventional positive spectral representation is the comparator, not an EFMW novelty certificate.

## Rule E — Full audit coverage and stop

Review every one of the **717** locked [source-equation records](../unity-001/phase-1/source-equations.csv) (102 canonical, 585 historical FieldSpace, and 30 additional source pointers). Keep separate machine-readable row-by-row disposition and manually inspect all nontrivial candidate hits. Refer to exact original source revisions/blobs; derived audit candidate expressions in CSV are **not** original evidence. Report counts and reasons for excluded near matches.

No new confirmatory hypotheses or extra numerical parameters can be introduced during execution. Unanticipated constraints go to an exploratory ledger only. A completed bounded source scan with no qualifying H1 or H2 support invokes the original stop rule for **this spectral-novelty route**, not for all EFMW theories.

## Change control

This is a **prospectively recorded protocol amendment** relative to the present execution, but is **post-v1** and based on a discussion already informed by earlier exposure to the corpus. Show both versions in all results. Original IST-001, WITD-002, UNITY Phase 5 and v1 IST-FAM-001 protocol remain unchanged.
