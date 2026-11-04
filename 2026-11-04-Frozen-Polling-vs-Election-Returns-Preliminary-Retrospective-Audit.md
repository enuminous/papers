# A Frozen Election-Eve Polling Snapshot Against November 2026 Returns: A Preliminary Retrospective Audit

**Author:** Matthew Chenoweth Wright, Monolithic LLC / EFMW research program  
**Prepared:** November 4, 2026  
**Evidence classification:** Retrospective, preliminary, *secondary-source transcription*. **Not an EFMW election forecast. Not certified election results.**  
**Original pre-election record:** [November 2 polling snapshot](2026-11-02-US-Election-Eve-Polling-Snapshot-EFMW-Residual-Protocol.md); [frozen CSV](data/2026-11-02_election_eve_polling_snapshot.csv).

## Abstract

A pre-election archival record dated November 2, 2026 preserved 16 U.S. Senate and 15 gubernatorial two-candidate polling pairs, with candidate identities and one-decimal support percentages, but **no explicit EFMW-predicted winners, margins, probabilities, or U.S. House district forecasts**. This paper audits a preliminary November 4 conversational comparison of these 31 records with election-night vote-share differences. Recalculation from that comparison yields a 5.00-percentage-point mean absolute margin error (MAE), a +3.50-point mean signed difference in the candidate orientation preserved in the archival table, and 26/31 agreements in the sign of the archived polling versus the previously reported election-night margin. Two included contests (Alaska Senate and Kansas governor) were described as uncalled in the earlier comparison, so 26/31 **must not** be called a winner-forecast accuracy rate. The 24/29 figure for reportedly called contests is also only a consistency count from the provisional transcription, not an independently authenticated audit. The 31 election-night margin values are reproduced below for transparency but have not all been independently re-extracted and timestamped against provider archives; no definitive empirical performance claim is warranted. No improvement attributable to EFMW is tested.

## 1. Scientific question and provenance

This is a **polling-calibration exercise**: how did pre-election displayed polling *differences* compare with election-night reported *vote-share differences* for the same candidate pairs? It is not a test of an EFMW predictive model. The archived November 2 document itself explicitly stated that its 50-state table was a polling transcript, not a winner or margin forecast, and supplied no district-level House predictions.

There are two provenance tiers:

1. **Frozen before election day:** the 31 candidate polling pairs and absolute gaps in the linked November 2 CSV and document. They must never be overwritten to improve apparent agreement.
2. **Provisional post-election:** the reported November 4 margin values transcribed into the preceding ChatGPT comparison. They were attributed there to election-results pages; this article preserves them *as a reproducible secondary transcription*, not as an independently downloaded, timestamped AP or official-election dataset. Results may change as votes are counted. Some candidate identity or denominator mismatches could also invalidate a row until checked.

For current context, November 4 AP results coverage and the Guardian's AP-backed election tracker report that election-night returns remain incomplete in some races (https://apnews.com/article/b1d26390b7ed7968435089be6d3bf612 ; https://www.theguardian.com/us-news/ng-interactive/2026/nov/04/midterm-elections-full-results-senate-house-governor-races). An individual *race call* and a final *certified margin* are distinct.

## 2. Methods

For each candidate pair, retain the order used in the frozen polling record: first candidate A, second candidate B. Define the **signed frozen polling gap** as

\[
s_i = p_{i,A}-p_{i,B},
\]

and the **provisional election-night difference** as

\[
o_i = v_{i,A}-v_{i,B}.
\]

Both are measured in **percentage points**, with positive values favoring the *first listed candidate*. Define the descriptive residual \(e_i=o_i-s_i\), MAE \(n^{-1}\sum_i|e_i|\), and mean signed residual \(n^{-1}\sum_i e_i\). A sign agreement is \(\operatorname{sgn}(s_i)=\operatorname{sgn}(o_i)\); it is **not** equivalent to a correctly forecast or certified winner. This scoring convention does not handle ranked-choice tabulation changes or differing two-candidate vs. all-candidate denominators, which must be resolved in a future certified audit.

The table below preserves the *numbers previously reported in conversation*, with an independently recalculated residual. No polling estimates or election-night margins were edited to fit the result. Because the latter are secondary transcription data, quantitative results are conditional on their eventual validation.

## 3. Senate: all 16 archived polling pairs

| State | Frozen signed polling difference (pp) | Provisional reported vote difference (pp) | Residual \(e_i\) (pp) |
|---|---:|---:|---:|
| AK | +1.80 | +0.30 | -1.50 |
| FL | -6.10 | -2.88 | +3.22 |
| GA | +8.40 | +18.00 | +9.60 |
| IA | -0.20 | +4.11 | +4.31 |
| KS | +3.60 | +4.87 | +1.27 |
| ME | +3.60 | +7.70 | +4.10 |
| MI | +3.90 | +7.04 | +3.14 |
| MN | +5.40 | +10.16 | +4.76 |
| MT | -8.30 | -10.02 | -1.72 |
| NE | -1.30 | -6.58 | -5.28 |
| NH | +8.00 | +14.27 | +6.27 |
| NC | +10.30 | +19.63 | +9.33 |
| OH | +2.70 | +4.86 | +2.16 |
| SC | -1.80 | +4.48 | +6.28 |
| SD | -10.20 | -21.00 | -10.80 |
| TX | +2.70 | +12.07 | +9.37 |

**Senate descriptive calculations:** 16 rows; 14 sign agreements; MAE **5.1944 pp**; mean signed residual **+2.7819 pp**. **AK was described as uncalled**, so the 14/16 sign statistic includes a provisional leader, not a confirmed result. In the preliminary table, IA and SC were the two sign disagreements.

## 4. Governor: all 15 archived polling pairs

| State | Frozen signed polling difference (pp) | Provisional reported vote difference (pp) | Residual \(e_i\) (pp) |
|---|---:|---:|---:|
| AZ | +7.90 | +12.93 | +5.03 |
| CA | +22.60 | +27.96 | +5.36 |
| FL | -4.60 | -1.31 | +3.29 |
| GA | -0.20 | +8.62 | +8.82 |
| IA | +6.70 | +10.98 | +4.28 |
| KS | -0.80 | +0.52 | +1.32 |
| ME | +10.30 | +18.42 | +8.12 |
| MI | +8.50 | +10.80 | +2.30 |
| MN | +10.80 | +12.84 | +2.04 |
| NE | -4.50 | -8.43 | -3.93 |
| NH | -6.50 | -3.85 | +2.65 |
| NY | +11.80 | +20.37 | +8.57 |
| OH | +4.50 | +7.93 | +3.43 |
| TX | -2.10 | +7.10 | +9.20 |
| WI | +4.70 | +8.16 | +3.46 |

**Governor descriptive calculations:** 15 rows; 12 sign agreements; MAE **4.7867 pp**; mean signed residual **+4.2627 pp**. **KS was described as uncalled**; the table's provisional positive margin should not be treated as a final outcome. GA, KS, and TX were the three sign disagreements against provisional vote leads.

## 5. Combined descriptive result and uncertainty

Across the 31 rows, the absolute residuals sum to **154.91 percentage points**, yielding **MAE = 154.91/31 = 4.9971 pp**, conventionally displayed as **5.00 pp**. Mean signed residual = **+3.4984 pp**. The provisional sign agreement is **26/31**, or **83.87%**; counting only the 29 races the earlier conversation described as called yields **24/29 = 82.76%**. The latter figure is based on the earlier call designations and requires independent reconciliation.

**Important:** these figures are not confidence-calibrated, do not include error bars, and cannot support claims of exceptional forecasting skill. Polling leader agreement is a weak metric, particularly across races with widely differing competitiveness. The 31-row set was selected by availability in the November 2 transcript; absent and N/A states are not zero-error observations. Sample selection and correlated statewide errors limit generalization.

No House comparison is possible: **0 archived House candidate predictions**. No Brier score or log loss is possible: **0 archived predictive probabilities**. No comparison to a conventional election forecast is performed here.

## 6. Illustrative large discrepancies

The following residuals are **conditional on the secondary transcription** and require source confirmation: South Dakota Senate (−10.80 pp), Georgia Senate (+9.60 pp), Texas Senate (+9.37 pp), North Carolina Senate (+9.33 pp), Texas governor (+9.20 pp), and Georgia governor (+8.82 pp). These illustrate why a favorable directional-agreement count should never substitute for continuous-margin evaluation.

A candidate-roster matching check must precede final scoring. Even when a name matches, preliminary percentages can depend on vote denominator, counting stage, third-party ballot votes, and, in some jurisdictions, subsequent tabulation rounds.

## 7. EFMW-specific interpretation and strict nonclaims

The *EFMW-inspired* component of the archived protocol is the discipline of a frozen pre-outcome record and subsequent residual analysis. There was **no published, independently executable EFMW election estimator**, no predeclared EFMW-specific vote-share prediction, and no randomized or out-of-sample benchmark against standard electoral analysis. The numerical figures reported here therefore **cannot validate EFMW, demonstrate superior forecasting, or establish a physical connection between EFMW and voting behavior**.

**PASS (documented):** the original 31 pre-election polling pairs exist in a dated public archive; the preliminary post-election comparison is transcribed in full here; its simple residual arithmetic is reproducible.

**UNRESOLVED:** independent source-level confirmation of all 31 provisional vote margins and candidate matchings; counting/certification status; exact results timestamps and denominators; uncertainty and comparable poll-source provenance; extrapolation to omitted contests.

**NOT ESTABLISHED:** EFMW election forecasting accuracy, causal or physical validation, predictive superiority, full House comparison, any certified final MAE, or prospective winner accuracy.

## 8. Reproduction and future certified audit

Reproduce the arithmetic by transcribing the preceding table into records with three fields (state, signed_poll_gap, provisional_vote_gap), calculating \(e=o-s\), and averaging \(|e|\) and \(e\). Code or analyst should independently check each published residual against the displayed numbers before reporting it.

To complete the empirical audit: (1) preserve the November 2 archive and this provisional paper unchanged; (2) obtain official certified results for the exact jurisdiction, office, date and ballot candidates; (3) fix the all-candidate vote-share denominator and handle ranked-choice stages correctly; (4) document any candidate mismatch or exclusion before aggregation; (5) release a row-level CSV with source URL, vote count, snapshot timestamp, reporting stage and eventual certification; (6) recompute MAE and directional agreement with explicit sample-size and uncertainty disclosures; and (7) prospectively register a genuinely new EFMW estimator and conventional baselines before evaluating it on future elections.

## References

1. [Frozen November 2 polling snapshot and protocol](2026-11-02-US-Election-Eve-Polling-Snapshot-EFMW-Residual-Protocol.md).
2. [Machine-readable frozen November 2 polling transcript](data/2026-11-02_election_eve_polling_snapshot.csv).
3. [Associated Press: November 4 election reporting](https://apnews.com/article/b1d26390b7ed7968435089be6d3bf612).
4. [Guardian election tracker, AP-backed reported results](https://www.theguardian.com/us-news/ng-interactive/2026/nov/04/midterm-elections-full-results-senate-house-governor-races).
5. [People's Poll methods](https://peoplespoll.com/methods) — stated aggregator methodology, **not** independently reconstructed source polling inputs.
6. [KQED California AP/county results](https://www.kqed.org/elections/results/california) — illustrative source for the continuing preliminary-count distinction.

**Editorial disclosure:** This is an AI-assisted retrospective descriptive note prepared within the research program whose archival record it examines. Its post-election margins are secondary, provisional transcriptions awaiting independent row-level provenance. Do not describe the 26/31 figure as an EFMW prediction success rate or as certified election outcomes.
