# 2026 U.S. Election-Eve Polling Snapshot: Frozen November 2 State Records and an EFMW-Inspired Residual-Audit Protocol

**Version:** 1.0; prepared 2 November 2026, ahead of the 3 November election  
**Publication:** Monolithic LLC / enuminous/papers; AI-assisted data transcription and methods documentation  
**Evidence class:** **ARCHIVED POLLING SNAPSHOT — NOT AN ELECTION FORECAST OR AN EFMW-PREDICTED RESULT**  
**Freeze input:** The 50-state polling table presented earlier in the same ChatGPT conversation, preserved here without retroactive correction; [machine-readable CSV](data/2026-11-02_election_eve_polling_snapshot.csv).

## Abstract

This document freezes a reported, election-eve 50-state table of candidate polling percentages and absolute percentage-point differences for selected U.S. Senate and gubernatorial contests. It captures what the earlier conversational table actually contained: **16 Senate candidate pairs and 15 governor candidate pairs with numeric averages**, plus states labeled as missing an aggregate or not applicable. Candidate vote-share outcomes, win probabilities, and prospective winning margins were **not** computed. Although the originating request asked for predictions of all House, Senate, and governor elections, no candidate-by-candidate House data were supplied and no EFMW electoral forecast model was estimated or validated. Publishing an unverified model prediction ex post would undermine the research record. The provided comparisons are frozen for future auditing, without asserting that the live aggregator remains identical or that the recorded candidate names are authoritative ballots.

## 1. Scope, provenance, and status

The November 3, 2026 general election includes **435 U.S. House races, 35 U.S. Senate races, and 36 gubernatorial races**, according to [Ballotpedia's 2026 election overview](https://ballotpedia.org/Election_results%2C_2026). This release is **not** a complete race-by-race snapshot of those elections. The source table covered all 50 states but provided numeric pairs only where previously displayed; it did not include any of the 435 House district rows.

The prior assistant response identified **[People's Poll Senate](https://peoplespoll.com/senate)**, **[People's Poll Governors](https://peoplespoll.com/governors)**, and its **[methods page](https://peoplespoll.com/methods)** as the basis. This freeze reproduces the numbers **as displayed in that prior response**, not a raw archive of every underlying poll. The aggregator's live pages are continuously updated and were already observed to differ in certain entries at the time of this publication (for example the previously reported Arizona governor percentages 50.0/42.1 versus the subsequently displayed 49.8/42.4). Such discrepancies must be treated as source-version differences or transcription issues until independently audited; they must not be silently revised after the freeze.

The actual aggregator states plainly that it **does not publish forecasts, winning probabilities, or betting odds**. The earlier conversational response also explicitly labeled its numbers as *polling averages rather than predicted winning margins*. This document therefore makes no invented claim to a pre-election winner list.

## 2. Frozen state records (percent support and reported absolute gap)

Column interpretation: candidate strings show the percentages **as originally reported**, not newly verified ballot entries. The difference score is the **absolute difference in percentage points** between the two shown percentages. This is **not** a forecasted election margin. D = Democratic; R = Republican; I = Independent. The em dash means that the earlier table supplied no qualifying average. `N/A` reproduces a previously reported no-race marker; the current ballot status for each state has not been independently re-adjudicated here.

| State | Senate recorded candidate support (%) | Abs. gap (pp) | Governor recorded candidate support (%) | Abs. gap (pp) |
|---|---|---:|---|---:|
| AL | — | — | — | — |
| AK | Peltola D 47.6 / Sullivan R 45.8 | 1.8 | — | — |
| AZ | N/A | — | Hobbs D 50.0 / Biggs R 42.1 | 7.9 |
| AR | — | — | — | — |
| CA | N/A | — | Becerra D 58.6 / Hilton R 36.0 | 22.6 |
| CO | — | — | — | — |
| CT | N/A | — | — | — |
| DE | — | — | N/A | — |
| FL | Nixon D 43.8 / Moody R 49.9 | 6.1 | Jolly D 44.4 / Donalds R 49.0 | 4.6 |
| GA | Ossoff D 52.5 / Collins R 44.1 | 8.4 | Bottoms D 48.3 / Jackson R 48.5 | 0.2 |
| HI | N/A | — | — | — |
| ID | — | — | — | — |
| IL | — | — | — | — |
| IN | N/A | — | N/A | — |
| IA | Turek D 46.6 / Hinson R 46.8 | 0.2 | Sand D 51.3 / Lahn R 44.6 | 6.7 |
| KS | Hamilton D 49.1 / Marshall R 45.5 | 3.6 | Holscher D 47.9 / Masterson R 48.7 | 0.8 |
| KY | — | — | N/A | — |
| LA | — | — | N/A | — |
| ME | Jackson D 50.0 / Collins R 46.4 | 3.6 | Pingree D 50.5 / Charles R 40.2 | 10.3 |
| MD | N/A | — | — | — |
| MA | — | — | — | — |
| MI | El-Sayed D 49.0 / Rogers R 45.1 | 3.9 | Benson D 51.4 / James R 42.9 | 8.5 |
| MN | Flanagan D 48.9 / Tafoya R 43.5 | 5.4 | Klobuchar D 51.8 / Demuth R 41.0 | 10.8 |
| MS | — | — | N/A | — |
| MO | N/A | — | N/A | — |
| MT | Bodnar I 33.1 / Alme R 41.4 | 8.3 | N/A | — |
| NE | Osborn I 46.8 / Ricketts R 48.1 | 1.3 | Walz D 42.3 / Pillen R 46.8 | 4.5 |
| NV | N/A | — | — | — |
| NH | Pappas D 51.2 / Sununu R 43.2 | 8.0 | Warmington D 43.8 / Ayotte R 50.3 | 6.5 |
| NJ | — | — | N/A | — |
| NM | — | — | — | — |
| NY | N/A | — | Hochul D 53.1 / Blakeman R 41.3 | 11.8 |
| NC | Cooper D 52.8 / Whatley R 42.5 | 10.3 | N/A | — |
| ND | N/A | — | N/A | — |
| OH | Brown D 48.1 / Husted R 45.4 | 2.7 | Acton D 49.3 / Ramaswamy R 44.8 | 4.5 |
| OK | — | — | — | — |
| OR | — | — | — | — |
| PA | N/A | — | — | — |
| RI | — | — | — | — |
| SC | Andrews D 45.9 / Graham R 47.7 | 1.8 | — | — |
| SD | Bengs I 41.4 / Rounds R 51.6 | 10.2 | — | — |
| TN | — | — | — | — |
| TX | Talarico D 48.9 / Paxton R 46.2 | 2.7 | Hinojosa D 47.1 / Abbott R 49.2 | 2.1 |
| UT | N/A | — | N/A | — |
| VT | N/A | — | — | — |
| VA | — | — | N/A | — |
| WA | N/A | — | N/A | — |
| WV | — | — | N/A | — |
| WI | N/A | — | Crowley D 49.3 / Tiffany R 44.6 | 4.7 |
| WY | — | — | — | — |

**Coverage check:** 50 states; **16** recorded Senate numeric pairs; **15** recorded governor numeric pairs; **0** House district candidate pairs. Blank and `N/A` cells were not estimated, inferred, or converted to zero margins. Neither the archived pair nor the gap constitutes a result call or a projected winner.

## 3. Reconstructed quantitative score and no-model boundary

For a displayed two-candidate polling pair with support estimates `p1` and `p2`, the sole numerical *gap score* is

```text
absolute_gap_pp = |p1 - p2|
```

All 31 numeric gaps were checked against their displayed percentages to the table's one-decimal precision; no arithmetic mismatches were detected. A signed difference would require a declared orientation and may be calculated only as a description of the displayed polling pair, not as a prospective election-outcome margin.

**Not performed:** no independent election forecast, district model, trained EFMW electoral predictor, probability distribution, historical fit, vote-turnout model, scenario weighting, simulation-based candidate projection, or residual-driven winner inference. The term *EFMW-inspired* refers only to the proposed discipline of freezing data and testing prediction residuals. It must not be confused with a verified physical connection between EFMW and political behavior.

Accordingly no Brier score, probability-based log loss, race-by-race winner-accuracy rate, electoral winner projection, error bar on the population vote, or forecasted seat total exists in this snapshot.

## 4. Underlying polling aggregation method, distinguished from the freeze

The external aggregator describes a **42-day** rolling window for Senate and gubernatorial polling averages, with a poll's weight **halving every 14 days**, larger respondent samples weighted more strongly up to a cap of **2,000**, and publication gates involving recent surveys from sufficiently diverse pollsters. Pollster repetition is capped and qualifying standards differ somewhat for House districts. See [People's Poll methodology](https://peoplespoll.com/methods) and [FAQ](https://peoplespoll.com/faq). These are the aggregator's own procedures. They were **not reimplemented or independently audited** in producing this frozen conversational snapshot.

The source says its published poll records are based principally on poll compilations credited to The New York Times under CC BY 4.0. The data and this archive should not be misrepresented as exclusive original EFMW measurements, as independently acquired polls, or as verified official election counts.

## 5. Prospective holdout audit after certified election results

For any future retrospective analysis:

1. Keep this archived document, CSV, and Git commit immutable. Never overwrite original candidate identities, percentages, or missing markers to match election outcomes.
2. Obtain official certified two-candidate or all-candidate vote shares with explicit jurisdiction, office, date, special/regular election distinction, and source citation.
3. Independently resolve recorded candidate names against actual ballot identities. Flag mismatches and non-comparable contests as **UNRESOLVED**; do not quietly relabel or substitute candidates.
4. For matched pairs, construct a signed *polling difference* `s_i` with a fixed orientation and an official *observed difference* `o_i` on the same vote-share denominator. Calculate `e_i = o_i - s_i`. Report `MAE = mean(|e_i|)` only over the disclosed set of matched contests and with exclusions reported.
5. Separately assess omitted contests, third-party candidates, likely-voter definitions, selection effects, polling design effects, and regional covariance. Do not claim an inference about all House races from the zero-house-row dataset.
6. Compare any newly developed EFMW-inspired estimator **prospectively**, with published frozen code, dated predictions, baselines, controls, and genuine holdout outcomes. Such a future study must not backfit to the November 3 results and then claim it was made November 2.

A statistical comparison between **polling margins** and later actual margins is a *polling-calibration audit*, not retrospectively an election forecast. An out-of-sample prospective forecast requires explicit model inputs and a timestamped output made **before** outcomes are observed.

## 6. Interpretation and limitations

**PASS:** The conversational polling percentages and displayed absolute gaps are recoverable and were transcribed into a machine-readable record. All 31 numeric gap calculations match the stated formula.

**UNRESOLVED:** Original poll-by-poll input reconstruction, candidate roster completeness, source versioning for individual cells, statewide population sampling error, per-race uncertainty intervals, actual outcome residuals, and external replication.

**NOT ESTABLISHED:** EFMW electoral forecasting skill, an EFMW-derived winner for any contest, election-outcome margin predictions, or evidence that a cognitive EFMW analogy outperforms ordinary polling analysis.

**Bottom line:** This release *locks an auditable election-eve polling observation*, not a list of model-predicted winners. Its scientific value lies in preserving a pre-election record whose provenance, missingness, and mathematical limits remain visible after the votes are counted.

## Sources

- People's Poll: [Senate polls](https://peoplespoll.com/senate), [governor polls](https://peoplespoll.com/governors), [House polls](https://peoplespoll.com/house), [methods](https://peoplespoll.com/methods), and [FAQ](https://peoplespoll.com/faq).
- [Ballotpedia 2026 election overview](https://ballotpedia.org/Election_results%2C_2026) for scheduled national contest counts and eventual election reporting.
- Source of **the fixed numeric cells**: November 2, 2026 in-conversation table preceding this publication. A replayable raw polling-input archive for those exact cells was **not** supplied. Live pages should not be assumed to reproduce the frozen historical table.

*Monolithic LLC / EFMW research documentation. No candidate endorsement, outcome prediction, independent physical validation, or election result is asserted.*
