# Conventional multiscale explanations for matched error histories

**Exploratory technical supplement — 7 November 2026**

Publication authorized by Matthew Chenoweth Wright on 7 November 2026 after delivery of the private computational review. This extension was implemented and executed with ChatGPT/Codex; it has not been independently reviewed. Professor Naoki Saito was not contacted about, involved in, or asked to endorse these calculations. The frozen plan and execution logs retain their historical review-stage wording; see [PUBLICATION.md](PUBLICATION.md).

## Result in brief

Ordinary differences between exponential filters distinguish **all 362 published constructed pairs**, representing **181 pairs modulo global sign**. A four-observation Haar detail distinguishes 320/362. The original matching conditions therefore do not isolate weighted absolute-error memory B from conventional temporal structure.

This mathematical design limitation does not, by itself, explain the behavioral results. On the checksum-verified Loosen et al. data, the specified eight-feature signed contrast/energy bank **slightly worsens held-out confidence prediction in both sessions**. Two ordinary absolute-error averages with alternative decay rates yield small improvements comparable to the published B improvements, but their direct advantage over B is uncertain. Adding B to either competing bank retains a small predictive gain. These findings establish neither an EFMW-specific memory mechanism nor elimination of all conventional alternatives.

## 1. Frozen scope and evidence provenance

The reference is `enuminous/papers` at commit `65f50f6710efa6801169429e5a5ad567f4d567d8`, directory `research/metacognition-matched-histories`. All nine original files were retrieved at this immutable commit and checked against their Git blob digests. The extension adds a new directory only. The original design, parameters, source, `pairs.csv`, `results.json` and `sensitivity.json` are unchanged.

`PLAN.md` specifies the new predictors, models, evaluation and controls. Its SHA-256 is `14a028a667882e583591c274343925318c3739f1c4a7db1e47738406213efca5`. It was recorded locally before running the new feature comparisons and outcome fits, **after** inspecting the published results. This is an exploratory analysis specification, not a public preregistration. The data have already informed earlier analyses and are not a fresh confirmatory sample.

The two public anonymized source files are those linked by the original package and Loosen, Seow and Hauser [1–3]. No participant-level data are included in the review patch.

| Session | Local alias | Bytes | SHA-256 |
|---|---|---:|---|
| 1 | `t1.csv` | 43,805,326 | `caacb0c111100ee8b24dbefe265f6bb7992e5599ab0b7ffce6abb227726dc2a9` |
| 2 | `t2.csv` | 29,104,752 | `fc5ce566ba808850b7706095075139a360a2ca1ae79a83308a9fda0064535a06` |

Both checksums matched before fitting. The eligible analysis rows remain 59,450 trials from 330 participants in session 1 and 39,420 trials from 219 participants in session 2. Session 2 consists of returning participants, not an independent cohort. None of these behavioral observations was collected under assignment to the constructed matched-history pairs.

## 2. Translation into standard signal-processing terminology

Let $e_{t-1}$ be the most recently observed signed angular prediction error, in radians, before the current confidence rating or action update. The original code uses the authors' signed shortest-angle residual. All new predictors retain that coordinate convention.

For a scalar signal $x$, define the causal, exponentially weighted filter

$$
E_r[x]_t=(1-r)\sum_{k=1}^{n} r^{k-1}x_{t-k},\qquad 0<r<1.
$$

The state starts at zero in each block; $n$ is the available history. There is no finite-history renormalization. Its recurrence is

$$
E_r[x]_{t+1}=rE_r[x]_t+(1-r)x_t.
$$

Equivalently, for zero initial state its transfer function is $H_r(z)=(1-r)z^{-1}/(1-rz^{-1})$. This is a first-order causal low-pass filter. The implementation uses SciPy's standard difference-equation filter [4], with a one-observation lag so the current error is unavailable to the prediction.

| Original variable | Standard description | Formula | Units in behavioral data |
|---|---|---|---|
| signed memory $m$ | Exponentially weighted signed error | $E_{1/2}[e]$ | radians |
| squared-error memory $Q$ | Exponentially weighted uncentered second moment | $E_{1/2}[e^2]$ | radians squared |
| `rms` | Square root of the weighted uncentered second moment | $\sqrt Q$ | radians |
| absolute-error memory $B$ | Exponentially weighted magnitude; low-pass filtering after full-wave rectification | $E_{1/2}[|e|]$ | radians |
| ratio $R$ | Absolute signed aggregate divided by magnitude aggregate | $|m|/B$ | dimensionless |
| contrast | A specified difference between filters or adjacent local means | Definitions below | radians |
| confidence | Current raw rating | `conf` | rating units |
| signed adjustment | Shortest signed change in bucket position | Current minus preceding placement | degrees in the original analysis |

$Q$ is not a centered variance. $B$ itself is an ordinary mathematical signal statistic; its use within an EFMW hypothesis does not make the operation mathematically unique to that hypothesis. The constructed integer histories have arbitrary stimulus units, rather than calibrated confidence or behavioral units.

## 3. Precisely specified competitors

The primary conventional bank C contains eight coordinates. Each signed contrast is accompanied by its square, allowing sensitivity to contrast energy rather than only direction.

| Pair of coordinates | Definition and purpose |
|---|---|
| $d,d^2$ | $d=e_{t-1}-e_{t-2}$: local error change and squared change |
| $f,f^2$ | $f=E_{1/4}[e]-E_{1/2}[e]$: fast versus intermediate signed error |
| $s,s^2$ | $s=E_{1/2}[e]-E_{3/4}[e]$: intermediate versus slower signed error |
| $h,h^2$ | $h=(e_{t-1}+e_{t-2}-e_{t-3}-e_{t-4})/2$: adjacent two-observation mean contrast |

The four-tap vector defining $h$ has zero sum and unit Euclidean norm. It is a Haar detail at one location and scale. It is evaluated at every trial as a sliding coefficient; this is **not** a full decimated wavelet decomposition or a survey of wavelet families. The local difference is proportional to the finer two-tap Haar detail. Haar and multilevel decomposition conventions are documented in [5]; the explicit formulas above determine this implementation without a wavelet-library dependency.

The secondary bank A contains only $E_{1/4}[|e|]$ and $E_{3/4}[|e|]$. It examines alternative conventional magnitude-memory time scales. Neither coordinate equals the original $B=E_{1/2}[|e|]$. C and A are reported separately because temporal contrast and magnitude smoothing are distinct explanations.

These scales were fixed before new fits. No new feature uses a fitted decay, outcome-selected window, or selected wavelet. For a stationary infinite history, the normalized mean lag is $1/(1-r)$: 4/3, 2 and 4 observations for the three decay rates. Finite zero initialization creates a transient: differences of exponential filters need not be zero for a short constant history. That transient is retained, documented and tested.

## 4. Exact constructed-history results

The unchanged original generator reproduced `pairs.csv` byte-for-byte. Every row passed exact rational checks for its error multiset, weighted signed memory, weighted second moment, last two errors, magnitude memories and ratios. Feature differences below are exact rational inequalities, with no numerical threshold.

| Feature | Distinguishable rows / 362 | Distinguishable pairs modulo sign / 181 |
|---|---:|---:|
| Local difference $d$ | 0 | 0 |
| Local energy $d^2$ | 0 | 0 |
| Fast contrast $f$ | 362 | 181 |
| Fast contrast energy $f^2$ | 362 | 181 |
| Slow contrast $s$ | 362 | 181 |
| Slow contrast energy $s^2$ | 362 | 181 |
| Haar detail $h$ | 320 | 160 |
| Haar energy $h^2$ | 276 | 138 |
| Fast magnitude average | 362 | 181 |
| Slow magnitude average | 362 | 181 |

The local-difference null is expected because both recent errors are equal within each pair. The multiscale differences show why that recency control is insufficient. Mirrored rows are not independent evidence. These counts describe the entire selected stimulus bank; they do not estimate a population frequency or support a significance test.

For the original illustrative pair with the common terminal zero appended, histories in oldest-first order are

$$
a=(3,0,-1,2,1,0),\qquad b=(-1,2,3,0,1,0).
$$

| Quantity | History a | History b |
|---|---:|---:|
| $m$ | 31/64 | 31/64 |
| $Q$ | 61/64 | 61/64 |
| $B$ | 39/64 | 33/64 |
| $d$ | −1 | −1 |
| $f$ | −871/4096 | −1051/4096 |
| $s$ | −233/4096 | −485/4096 |
| $h$ | 0 | −1 |

Thus a response difference after these histories could also be associated with an ordinary Haar or exponential-filter contrast. **Demonstrated:** the original matching constraints do not isolate B. **Unresolved:** whether any of those differences would influence a human response under assigned, matched conditions.

All 362 rows, including both feature values and their exact differences, are archived in `results/pair-features.csv`.

## 5. Behavioral evaluation and leakage boundaries

The extension reuses the original five balanced participant folds, sorted by SHA-256 of `EFMW:{id}`. Every model trains on session 1 participants outside its test fold. The same trained relationship is evaluated on the held-out participants' session 1 and session 2 rows. No participant appears in both training and test sets, in either session.

The original baseline has 49 design columns: training-fold quartile linear-spline terms for previous ratings, cumulative prior confidence, two recent signed and unsigned errors, signed memory, absolute signed memory, weighted RMS, lagged Bayesian change-point probability and relative uncertainty, and block age; plus previous hit status. The intercept is additional and unpenalized. All original choices are reused unchanged.

Each new coordinate is linearly added and standardized using training rows only. The fixed ridge penalty is $\alpha=1$, with no tuning. Models are base, base+B, base+C, base+C+B, base+A, base+A+B, base+C+A and base+C+A+B. Added dimensions are respectively 0, 1, 8, 9, 2, 3, 10 and 11. Different dimensions and collinearity mean these are comparisons of fixed predictive pipelines, not equal-complexity mechanism tests. In particular, signed $d$ is already in the linear span of recent signed errors; adding it can change the effective ridge penalty rather than add information. Its square introduces an interaction.

The stronger published sensitivity baseline adds $|m|/\sqrt Q$, randomized slider start and current absolute bucket adjustment, yielding 52 columns before the new features. It is used only for confidence; current adjustment is never used to predict itself. The current placement is available by the time confidence is rated [1]. All newly computed error features exclude current and future errors and reset at block boundaries; the original five-observation burn-in is retained.

For session $v$ and model $M$, the score is

$$
L_{v,M}=\frac1{N_v}\sum_{i=1}^{N_v}\frac1{n_{iv}}\sum_t
(y_{ivt}-\widehat y_{ivt,M})^2.
$$

Positive gain $\Delta=L_{\rm reference}-L_{\rm alternative}$ means improvement. Percent gain is $100\Delta/L_{\rm reference}$, **not** a percentage-point change in accuracy. Intervals are paired percentile bootstrap intervals from 5,000 resamples of participants, seed 20261106, with predictions fixed. They omit model-training uncertainty, previous data reuse and multiple-comparison selection. Session estimates are not independent. All intervals here are descriptive, not confirmatory tests or equivalence claims.

## 6. Confidence results

All values in this table use the original baseline, with percent gain computed against that same baseline within each session. MSE is in squared rating units.

| Added features | Session 1 MSE | Gain vs base | Session 2 MSE | Gain vs base |
|---|---:|---:|---:|---:|
| None | 344.242475732 | 0 | 289.494400314 | 0 |
| B, reproduced original | 344.231345793 | +0.003233% | 289.436744871 | +0.019916% |
| C | 344.263088646 | −0.005988% | 289.527921352 | −0.011579% |
| C+B | 344.239714564 | +0.000802% | 289.447797901 | +0.016098% |
| A | 344.219216011 | +0.006757% | 289.421367879 | +0.025228% |
| A+B | 344.177341155 | +0.018921% | 289.278682359 | +0.074515% |
| C+A | 344.235085008 | +0.002147% | 289.446790065 | +0.016446% |
| C+A+B | 344.184638981 | +0.016801% | 289.295252155 | +0.068792% |

The following paired comparisons use each row's stated reference. Gains and intervals are in squared rating units, not percentages.

| Comparison | Session 1 gain [conditional 95% interval] | Session 2 gain [conditional 95% interval] |
|---|---:|---:|
| Add B to base | 0.011130 [−0.047775, 0.067721] | 0.057655 [0.004690, 0.109714] |
| Add C to base | −0.020613 [−0.145231, 0.108189] | −0.033521 [−0.156626, 0.090924] |
| Add A to base | 0.023260 [−0.044142, 0.088593] | 0.073032 [0.008318, 0.140251] |
| Replace B with A | 0.012130 [−0.057334, 0.081964] | 0.015377 [−0.060191, 0.092179] |
| Add B after C | 0.023374 [−0.050015, 0.099058] | 0.080123 [0.012740, 0.146846] |
| Add B after A | 0.041875 [−0.025286, 0.105176] | 0.142686 [0.072464, 0.215870] |
| Add B after C+A | 0.050446 [−0.023793, 0.120879] | 0.151538 [0.074260, 0.229673] |

The original B percentages are exactly reproduced, rather than replaced by a new analysis. The primary signed contrast competitor C has a negative mean gain in both sessions; this implementation does not explain away the original confidence result. Alternative magnitude bank A performs slightly better than B by point estimate, but both direct A-versus-B intervals span zero. Conditional B gains remain, and combining magnitude time scales performs better than choosing just one. That result is compatible with ordinary temporal magnitude integration as well as other explanations; it identifies no unique cognitive operator.

With the stronger rating-cue baseline, the qualitative pattern persists:

| Added features, relative to the rating-cue baseline | Session 1 percent gain | Session 2 percent gain |
|---|---:|---:|
| B | +0.006352% | +0.023082% |
| C | −0.006743% | −0.013730% |
| A | +0.007247% | +0.023328% |
| A+B | +0.025929% | +0.083986% |
| C+A+B | +0.023701% | +0.073601% |

The direct A-versus-B gain with rating cues is 0.002997 [−0.067293, 0.072676] in session 1 and 0.000694 [−0.075304, 0.078393] in session 2. Those results offer no clear ranking between A and B. All models, all comparisons and all fold losses are retained in the JSON/CSV outputs; no losing model is omitted from those records.

For secondary signed adjustment, C changes MSE by +0.224791 improvement in session 1 and −0.412128 in session 2; intervals are [−1.922769, 2.227750] and [−1.705322, 0.856081], respectively. A gives −0.019904 and +0.037436, also with intervals spanning zero. These inconsistent point estimates do not provide stable support for the proposed competitors on adjustment. Adjustment MSE uses squared degrees and must not be compared directly with confidence MSE.

## 7. Negative controls and implementation checks

Seven automated scientific checks pass: exact rational/direct-sum agreement with vectorized filters over 60 seeded sequences of lengths 6, 7, 20 and 41; constant/zero-signal responses including finite-start transients; self equality and mirror parity; current/future-error perturbations; independent block initialization; training-only standardization; and Haar normalization. The pair audit additionally verifies equality of local features for all 362 recent-error-matched pairs.

An initial test run exposed fixed-width NumPy integer arithmetic inside `Fraction` for long synthetic histories. Scalar conversion to Python integers fixed the exact-reference implementation. The failed and corrected test logs are retained. The pair parser already supplied Python integers, so the original pair computations were unaffected. The final full replay uses the corrected code. This was an implementation repair, not a feature or model-selection change.

For an alignment diagnostic, each added bank B, C or A was circularly shifted within participant-block, retaining column alignment, with 20 predetermined seeds (20261107–20261126). Offsets were at least five positions from either endpoint. Original baseline predictors and confidence outcomes were fixed, and the shifted models were refit with the same held-out folds. All six observed gains lie within their corresponding shifted ranges.

| Session / added bank | Observed MSE gain | Shifted mean | Shifted range | Shifts at least as large / 20 |
|---|---:|---:|---:|---:|
| 1 / B | 0.011130 | 0.023668 | [−0.028350, 0.089178] | 13 |
| 1 / C | −0.020613 | −0.034717 | [−0.101285, 0.021011] | 9 |
| 1 / A | 0.023260 | 0.109819 | [0.012548, 0.200940] | 19 |
| 2 / B | 0.057655 | 0.012927 | [−0.053018, 0.059763] | 1 |
| 2 / C | −0.033521 | −0.040777 | [−0.145731, 0.026286] | 7 |
| 2 / A | 0.073032 | 0.079290 | [−0.047896, 0.180424] | 12 |

These are **not permutation p-values**. Shifts disturb relationships with the baseline, retain participant/block-level information, and wrap history so some shifted predictors refer to later observations. Only this deliberate diagnostic permits that misalignment; the actual fitted competitors remain causal. Positive shifted gains show that this diagnostic is not a zero-gain null. In particular, A's small benefit is not specific to its original timing under this check. The diagnostic does not determine whether the original B association is spurious and does not erase the original result. A valid conditional temporal null remains an open methodological task.

## 8. Reproducibility record and source patch

The recorded environment is Python 3.12.14, NumPy 2.3.5, pandas 2.2.3, SciPy 1.17.0 and scikit-learn 1.8.0, matching the original pins. Analysis subprocesses in the final replay use `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1` and `MKL_NUM_THREADS=1`.

`execution/` records actual subprocess argument lists, working directories, UTC start times, exit codes, standard output, standard error, input/source hashes and output hashes. A separate development subdirectory preserves the first runs, including the test failure and repair. Download logs and acquisition provenance identify the actual OSF retrieval. Portable instructions are in `README.md`; the final replay was invoked with:

```bash
python reproduce.py --data /workspace/scratch/f74477cd559d/raw-data --out /workspace/scratch/f74477cd559d/final-replay
```

The runner executes the original `analyze.py`, `sensitivity.py` and `matched.py`, the new pair and behavioral analyses, seven tests and preservation checks. The complete replay is distinct from merely inspecting source code. The original analysis's 64 numerical leaves and the original sensitivity analysis's 44 numerical leaves matched with maximum absolute difference **zero**. Generated pairs matched byte-for-byte. The extension's reused original and rating-cue baselines and B gains/intervals also matched exactly.

The original review patch adds only `research/metacognition-matched-histories/exploratory-multiscale/`. It was checked by applying it to a fresh copy of the immutable nine-file source snapshot, then comparing the resulting file bytes. The separately delivered review ZIP also includes a runnable snapshot and the supplement. Following Matthew's publication authorization, this extension is published with links in the repository README and HTML index. Publication changes only status/navigation text and mathematical display delimiters relative to the reviewed material; the executed code, frozen plan, original numerical results and execution logs are preserved. No email has been sent.

## 9. Evidence ledger and remaining uncertainties

| Claim or obligation | Status | Basis or limitation |
|---|---|---|
| Original numerical results reproduce | **Demonstrated computationally** | Exact numerical replay in the recorded environment |
| Original controls isolate B in the constructed bank | **Rejected** | Conventional contrasts differ within every pair |
| The fixed C bank improves confidence prediction | **Unsupported in this execution** | Mean held-out gains negative in both sessions |
| Ordinary magnitude time scales are competitive predictors | **Supported but incomplete** | Small A gains; direct advantage over B uncertain; shifted controls weaken timing specificity |
| C or A removes B's incremental prediction | **Not demonstrated** | Conditional B point gains remain |
| Human observers implement B or an EFMW-specific mechanism | **Unresolved** | Observational associations and constructed arithmetic do not identify a mechanism |
| Conventional multiscale explanations are exhausted | **Not established** | Only a small fixed family and linear/squared readouts were examined |
| Practical benefit of any improvement | **Unresolved** | Small gains; no prospectively defined useful margin |

Further limits include the dependence of squared contrasts on the signed principal-angle coordinate near the angular branch cut; unexamined circular-signal alternatives; fixed regularization and coordinate redundancy; fixed decay choices rather than nested model selection; short zero-initialized histories; dependent repeated visits; and conditional intervals that omit training uncertainty. The constructed examples were originally selected for a B difference, so their exhaustive discrimination counts cannot validate a human theory.

A suitable next study would first determine whether histories can be constructed that match a declared expanded family of conventional predictors while retaining a B contrast. Feasibility is **not tested here**. If feasible, identical probes after randomized assigned histories, a prospectively defined meaningful effect, an independently collected sample and an appropriate temporal null could test a narrower mechanistic claim. No such experiment or additional search is represented as executed in this supplement.

## References

1. Loosen, A. M., Seow, T. X. F., and Hauser, T. U. (2024). *Consistency within change: Evaluating the psychometric properties of a widely used predictive-inference task*. Behavior Research Methods 56, 7410–7426. https://doi.org/10.3758/s13428-024-02427-y . Consulted for task timing and data provenance; its authors did not perform this extension.
2. Authors' anonymized data: https://osf.io/hakq9/ . Original download endpoints: https://osf.io/download/v89g7/ and https://osf.io/download/59py4/ . Original analysis code: https://github.com/amloosen/A-Psychometric-Investigation-of-the-Predictive-Inference-Task .
3. Immutable EFMW reanalysis source: https://github.com/enuminous/papers/tree/65f50f6710efa6801169429e5a5ad567f4d567d8/research/metacognition-matched-histories .
4. SciPy, `scipy.signal.lfilter`, official reference: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html . Consulted for the difference-equation/filter convention; calculations ran with SciPy 1.17.0, not the current documentation build.
5. PyWavelets, *Discrete Wavelet Transform*, official reference: https://pywavelets.readthedocs.io/en/latest/ref/dwt-discrete-wavelet-transform.html . Consulted for Haar/detail terminology; no PyWavelets dependency was used in the extension.
