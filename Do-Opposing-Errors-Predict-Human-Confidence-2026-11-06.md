# Do Opposing Errors Predict Human Confidence?

**Matthew Chenoweth Wright · Monolithic LLC**  
**6 November 2026 · Exploratory secondary analysis of human behavioral data**

## Abstract

Two people can have the same net prediction error while one has experienced more errors in opposing directions. Does that difference help explain how much they trust their next prediction? We tested this question in public human data from Loosen, Seow and Hauser. Participants positioned a bucket, rated their confidence, and then saw where a particle landed. We predicted confidence using only information available before feedback on the current trial. Adding exponentially weighted absolute error to a model that already knew recent errors, signed and squared error memory, prior confidence and normative uncertainty reduced held-out mean squared prediction error by **0.0032%** in the first session and **0.0199%** in the retest. The first-session uncertainty interval included zero. All five training folds gave the predicted negative slope, but the incremental predictive value was small. A separate exact construction produced 362 pairs of error histories for which a model based only on matched first and second moments must predict a tie. The observed study tested prediction across people. The proposed intervention on error order remains untested.

## 1. The question and the comparator

The EFMW signed-memory investigation identified an exact equivalence between its implemented update and a matched exponential moving average of signed errors. For an error history, let $m$ be its signed average, $B$ its average absolute magnitude, and $Q$ its average squared magnitude, all with identical weights. Where $B>0$, the directional coherence $R=|m|/B$ is the fraction of weighted magnitude that survives cancellation. The algebra identifies what the filter remembers. Whether a person uses that information to judge their own answer requires behavioral evidence. [Signed-memory identity](The-Signed-Memory-Identity-and-Human-Self-Correction-2026-11-06.md) · [Directional coherence and the proposed human comparison](When-Errors-Agree-Directional-Coherence-in-EFMW-Residual-Memory-2026-11-06.md)

There is relevant precedent. Sanders, Hangya and Kepecs used the normalized difference between left and right clicks as a measure of evidence discriminability in a human confidence task. Loosen and colleagues found that participants who made a larger adjustment on a trial tended to report lower confidence. Our question concerns the ordering of earlier feedback errors and how much predictive information remains after a conventional model already knows their mean and dispersion. [Sanders et al.](https://doi.org/10.1016/j.neuron.2016.03.025) · [Loosen et al.](https://doi.org/10.3758/s13428-024-02427-y)

## 2. Data and prediction rule

We used the two public trial tables in the authors’ final analytic sample. At each trial participants placed a bucket on a circle, reported confidence from 1 to 100 that it would catch the particle, and then received feedback. Every participant contributed 200 trials per session attended. Session 1 included 330 people. Session 2 included 219 returning participants. We checked both files against the SHA-256 digests supplied by OSF. [Public data](https://osf.io/hakq9/) · [Original analysis code](https://github.com/amloosen/A-Psychometric-Investigation-of-the-Predictive-Inference-Task)

We retained the source’s signed angular error in radians, particle location minus bucket position around the shorter arc. For confidence at trial $t$, the most recent error used was $r_{t-1}$. At block start, all three memories were zero. Each new observed error updated them by taking half of the previous value and half of the new input ($r$, $|r|$ or $r^2$). The half-decay matches the proposed stimulus construction. The synthetic benchmark uses a different memory length. We did not select the decay from performance on these participants. We required five preceding observations in the recorded block. Five first-session participants had two recorded blocks of 100 trials rather than four of 50. Using the supplied blocks retained **59,450** scored trials in session 1 and **39,420** at retest.

**Primary contrast.** We predicted current confidence from the preceding confidence rating and its block-to-date mean, the last two signed and absolute errors, $m$, $|m|$, $\sqrt Q$, previous hit status, previous trial’s supplied Bayesian change-point probability and relative uncertainty, and position within the block. Continuous controls entered as linear terms with piecewise-linear adjustments at training quartiles. We added one linear $B$ term to this baseline. Secondary contrasts added $R$ instead and evaluated the same features against signed movement from the preceding bucket placement in degrees. The current trial’s particle outcome and confidence rating never entered its own predictors. [Analysis decisions recorded before fitting](research/metacognition-matched-histories/design.md)

Five deterministic folds split **people**, keeping their sessions together. For each fold, ridge regression with a fixed penalty of one was fitted on first-session data from the other four folds. The same fitted weights scored that fold’s session 1 and retest records. We calculated mean squared loss for each person before averaging across people. Positive gain means lower held-out loss. Intervals are paired 95% participant-bootstrap percentile intervals (5,000 resamples) conditional on the fitted predictions. They describe variation across test participants and omit uncertainty from refitting the models. The design was exploratory and locally specified, without public preregistration.

## 3. Human findings

| Outcome and added predictor | Session 1 gain in mean squared error [95% interval] | Session 2 gain [95% interval] |
|---|---:|---:|
| **Confidence · $B$ (primary)** | **0.011 [−0.048, 0.068]** | **0.058 [0.005, 0.110]** |
| Confidence · $R$ | 0.107 [0.008, 0.207] | 0.104 [−0.024, 0.234] |
| Signed adjustment · $B$ | −0.022 [−0.332, 0.260] | 0.014 [−0.200, 0.230] |
| Signed adjustment · $R$ | −0.007 [−0.022, 0.008] | 0.003 [−0.010, 0.019] |

Confidence gains are in squared rating points. Signed adjustment gains are in squared degrees. Baseline confidence losses were 344.24 and 289.49. Baseline adjustment losses were 628.67 and 418.34. The five first-session training coefficients for $B$ ranged from −5.01 to −2.89 confidence points per radian, conditional on the other features. Thus the direction agreed with the prediction in every overlapping training fit, while adding the term barely improved prediction on new people. The corresponding test-loss reduction was about three thousandths of one percent in session 1 and two hundredths of one percent at retest. [Full results and fold coefficients](research/metacognition-matched-histories/results.json)

**Sensitivity to the competing account.** After the primary analysis, we added the conventional concentration measure $|m|/\sqrt Q$ to the baseline. We then added two cues available when a person reports confidence: the magnitude of the movement they have just made and the randomized initial position of the confidence slider. With all three controls, the additional $B$ term reduced test loss by 0.0064% in session 1 and 0.0231% at retest. Both corresponding intervals for absolute loss gain included zero. The additional $R$ term reduced loss by 0.0182% and 0.0374%, respectively, with only the retest interval excluding zero. These were descriptive sensitivity comparisons with no multiple-comparison correction. [All sensitivity results](research/metacognition-matched-histories/sensitivity.json)

**What the observations settle.** At the tested decay, adding weighted absolute error to this fairly strong baseline contributed little to out-of-person confidence prediction. Retest is a transfer across time in a subset of the original sample. The weak gains and uniformly negative fitted slopes justify recording the direction while retaining the inconclusive first-session primary result. No practically meaningful threshold was specified before fitting. The wide adjustment intervals do not establish equivalent corrections. The study did not assign matched histories, measure participants’ private memory decay, or test whether they consciously reconsidered the basis for their confidence.

## 4. A sharper controlled test

Here is the original five-observation pair calculated exactly at decay $1/2$. The weights from oldest to newest are $(1,2,4,8,16)/32$, with zero initial memory. Both histories contain the same errors and end with $+1$.

| History, oldest first | Signed $m$ | Squared $Q$ | Absolute $B$ | Coherence $R$ |
|---|---:|---:|---:|---:|
| A: $+3,0,-1,+2,+1$ | $31/32$ | $61/32$ | $39/32$ | $31/39$ |
| B: $-1,+2,+3,0,+1$ | $31/32$ | $61/32$ | $33/32$ | $31/33$ |

A rule that uses only those first and second moments gives the same prediction for A and B. A rule that lowers confidence with greater absolute error at fixed $m,Q$ predicts lower confidence after A. The penultimate error also differs in this short example. We therefore searched permutations of five or six errors in the integer alphabet −3 through +3, matched the multiset, final error, and integer weighted first and second moments, and appended the same zero to both histories. We included mirrored signs. Each resulting pair has identical **two most recent observations**, different $B$, and equal nonzero signed memory. Exact integer and rational checks verify every row. The bank contains **362 constructed pairs**, including mirrors and related variants. They are stimuli rather than independent observations. [Stimulus bank](research/metacognition-matched-histories/pairs.csv) · [Exact generator](research/metacognition-matched-histories/matched.py)

A prospective task can randomize variants across people, mirror signs and counterbalance probes. After each history, ask separately for the signed adjustment to the reading and the probability that the corrected prediction will fall within a fixed tolerance. Use the same probe and reference distribution within a matched pair. Specify a meaningful decrease in confidence, an equivalence margin for adjustment, and sample size before collection. The predicted joint outcome is lower confidence after the larger-$B$ history with equivalent correction. A precise reversal, or an interval excluding the specified confidence decrease, counts against it. At a fixed $m$, $B$ and $R$ move together. Other probe families varying $m$ separately, and tests of older lag-specific and change-point cues, are needed to distinguish a coherence computation from those alternatives. An assigned instrument history tests monitoring of external feedback. A claim about monitoring one’s own mistakes requires a participant-generated error condition.

## Conclusion

The empirical answer is modest. The signed-memory calculation generates a testable distinction, and the direction of the fitted confidence association was consistent. In these records, the extra error-history term added little to predictions from the specified comparison model. The mathematically stronger result is that matched histories exist even after holding recent errors and the first two weighted moments fixed. Those histories make a human experiment possible in which a specified rival predicts an actual tie.

[Reproduction instructions, code, stimuli and aggregate outputs](research/metacognition-matched-histories/README.md)
