# The Signed-Memory Identity and Human Self-Correction

**Matthew Chenoweth Wright · Monolithic LLC**  
**6 November 2026 · Mathematical research note and proposed behavioral study**

## Abstract

What does an early-warning monitor remember about a run of mistakes? The monitor studied in the Einstein–Feynman–Maxwell–Wright (EFMW) program retains their direction as well as their size. Its signed state is exactly an exponentially weighted moving average of the residuals, and its warning score is the magnitude of that state. This identity, documented in the November 2 EFMW monograph, is a mathematical discovery about the implemented monitor. It also gives an exact measure of cancellation. The difference between averaging error magnitudes and taking the magnitude after averaging equals twice the smaller of the accumulated positive and negative contributions. That quantity measures precisely how much cancellation the second procedure permits. A direct evaluation of the weighted sum reproduced the monitor’s scores on 40 frozen synthetic traces to a maximum absolute discrepancy of $8.33\times10^{-17}$, with agreement on every first alert. We propose separate tests of whether people retain the direction of prior errors and whether checking the basis of an earlier confidence judgment helps them repair a wrong answer. Both human predictions await data.

## 1. What was discovered

Suppose an instrument reads one unit too high four times. Now suppose it alternates between one unit low and one unit high. In both cases the error is one unit on every observation. Should an observer adjust the instrument by the same amount? For someone trying to remove a persistent bias, the *direction* of the errors matters. For someone monitoring the *size* of the disturbances, either history deserves attention.

The original EFMW benchmark posed a related question about a changing synthetic control system. The candidate beat its published baseline by a median paired warning lead of 16.5 timesteps on 40 held-out seeds. But the comparison changed two things at once. The baseline applied the absolute value to each residual and used decay 0.90. The candidate kept the residual’s sign, used decay 0.97, and took the absolute value at the end. The warning-lead result belongs to that comparison. The identity tells us exactly which computation produced the candidate’s score. [Frozen benchmark reconciliation](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/CONFIRMATORY_RECONCILIATION.md) · [Monitor source](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/monitors.py)

The same research program also recorded a failed specificity test. With the original thresholds, the candidate raised a sustained false alarm in 66 of 80 stable runs. After a separate whole-run recalibration, it raised 2 alerts in 80 held-out null runs and gave actionable warnings in 77 of 80 degradation runs. These are observations about a simulator and its alert policy. The identity holds at both operating points. [Specificity screen](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-002/README.md) · [Recalibrated screen](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/README.md)

The distinction matters for attribution. S. W. Roberts described geometric moving averages for process monitoring in 1959. The EFMW discovery identifies the particular quantity its own monitor computes and establishes what follows for every possible input. Section 3.2 of the November 2 monograph already gives the proof. This note develops its cancellation consequence, checks the published implementation, and proposes a transfer to human cognition. [Roberts, 1959](https://doi.org/10.1080/00401706.1959.10489860) · [EFMW monograph, §§3.1–3.4](https://github.com/enuminous/papers/blob/3533d87bf3c47f6116c75a4c55aca9b92e8646a6/EFMW-Dissertation-Recursive-Coherence-Evidence-Bounded-Verification-2026-11-02.md)

## 2. The identity and the amount that cancels

Let $r_t$ be observed minus predicted value at step $t$. Use the same sequence of real residuals, the same zero initialization, and fixed decay $0\leq\lambda<1$. Residuals, memory, and both scores have the units of the observation. The decay is dimensionless. The signed state $m_t$, its score $C_t$, and the matched unsigned score $B_t$ are

$$
m_t=\lambda m_{t-1}+(1-\lambda)r_t,\qquad C_t=|m_t|,
\qquad B_t=\lambda B_{t-1}+(1-\lambda)|r_t|,\qquad m_0=B_0=0.
$$

**Signed-memory identity.** Write $w_{tj}=(1-\lambda)\lambda^{t-j}$, with the lag-zero weight $1-\lambda$. Then

$$
m_t=\sum_{j=1}^{t}w_{tj}r_j.
$$

At $t=1$ both expressions give $(1-\lambda)r_1$. At the next step, multiplying the previous sum by $\lambda$ supplies each old residual with one additional factor of decay. Adding the new term completes the induction. The identity is exact for every finite real sequence. Identical scores also give identical mathematical alerts when both detectors use the same threshold, start time, and alert rule.

**Cancellation identity.** Let $P_t$ be the weighted sum of positive parts $\max(r_j,0)$ and $N_t$ the weighted sum of negative parts $\max(-r_j,0)$, both with weights $w_{tj}$. Then $m_t=P_t-N_t$ and $B_t=P_t+N_t$. Consequently,

$$
B_t-C_t=P_t+N_t-|P_t-N_t|=2\min(P_t,N_t).
$$

Thus the two scores agree precisely when one side has zero effective weight. Each unit of weighted negative error paired with a unit of weighted positive error removes two units from the unsigned total. The gap measures cancellation in observation units. It compares scores at a common decay. Detectors with separately calibrated thresholds can still alert in either order.

### Four observations and an exact counterexample

Use $\lambda=1/2$ so the arithmetic is visible. Both histories end with the same positive error, and every error has magnitude one.

| Residuals, oldest first | Signed state after each observation | Final signed score $C_4$ | Final unsigned score $B_4$ |
|---|---|---:|---:|
| $+1,+1,+1,+1$ | $1/2,\ 3/4,\ 7/8,\ 15/16$ | $15/16$ | $15/16$ |
| $-1,+1,-1,+1$ | $-1/2,\ 1/4,\ -3/8,\ 5/16$ | $5/16$ | $15/16$ |

There is also a two-observation counterexample to the claim that a nonzero disturbance must leave a positive terminal signed score. Take $r_1=a$ and $r_2=-\lambda a$, where $a\ne0$ and $0<\lambda<1$. Then $m_2=0$ exactly, while $B_2=2\lambda(1-\lambda)|a|>0$. At that instant the signed score coincides with the score for two zero residuals. The earlier score and the unsigned score still distinguish the histories. This is the price of using a single terminal number to summarize directional bias.

## 3. Checking the frozen implementation

The benchmark computes $r_t=y_t-(0.82y_{t-1}+u_t)$. Its code initializes array element zero to zero and first consumes residual index one. Using that convention, we regenerated seeds 1001–1040 from the pinned simulator and computed each signed score a second way, by convolution with the geometric weights. The check reused the published alert rule of three consecutive scores strictly above the candidate’s frozen threshold, starting the search at each run’s degradation onset. [Pinned simulator](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/simulator.py) · [Frozen runner](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/run_confirmatory.py)

| Replay quantity | Result |
|---|---:|
| Synthetic traces × samples per trace | 40 × 500 |
| Scores compared, including each initial zero | 20,000 |
| Maximum absolute score discrepancy | $8.33\times10^{-17}$ |
| First-alert disagreements | 0 of 40 |

The induction establishes the mathematical identity. The replay checks indexing, numerical agreement and the consequence for the published alert rule. Floating-point recurrences and weighted sums can round differently because they group operations differently. The Appendix gives the calculation.

## 4. What human studies contribute

A separate EFMW case study describes recursive metacognition as examining one’s thought at multiple nested levels. That description motivates a behavioral distinction: reconsidering an answer and reconsidering *how one judged that answer* are different instructions. There are two senses of recursion here. A filter carries a past value into its next update. A person can turn a judgment about an answer into the object of another judgment. The filter identity gives a way to model the first operation, while the case report motivates testing the second. Observing one does not establish the other. [Wright, August 2025, §2](https://github.com/enuminous/medium/blob/20c70372ef186009222b29189031b4f7390346ed/2025-08-17_Neuropsychological-Development-Across-Eight-Months-of-Recursive-Cognitive-Engagement--A-Case-Study--46dc9558579e.html)

| Source and publication status | Human observation | Bearing on the proposed tests |
|---|---|---|
| Juzhi Zhang, *Frontiers in Psychology*. Peer-reviewed, accepted November 4, 2026. | Across three university-student experiments ($N=264,360,386$, respectively), fluent explanations increased predicted test performance. In Study 2 the authors detected increased overestimation, with no significant group difference in objective performance or absolute calibration error. In Study 3 an unaided retrieval attempt reduced average overestimation. | A learner can adjust confidence without repairing an error. An active retrieval control and a separate accuracy measure are essential. The accepted abstract reports immediate testing. [Primary article](https://doi.org/10.3389/fpsyg.2026.2003031) |
| Noelle Clark and colleagues, bioRxiv preprint, November 2, 2026. | In think-aloud interviews, 39 senior life-science students asked themselves questions while solving biology problems. The researchers observed that progress depended on students answering those questions correctly. | Recognizing a gap and repairing it can come apart. An observational interview cannot determine the causal effect of a self-check, and unspoken monitoring falls outside its record. [Primary preprint](https://doi.org/10.64898/2026.10.30.762163) |
| M. Gawlowska, bioRxiv preprint, November 2, 2026. | Participants learned under both 100%- and 75%-reliable feedback. Learning was better with fully reliable feedback. In that condition, two components of midfrontal theta activity changed in opposite directions as learning progressed. | Feedback reliability belongs under experimental control. The neural measures track aspects of learning. Whether participants consciously detected and corrected an error requires a behavioral measure. The accessible abstract does not give sample size. [Primary preprint](https://doi.org/10.64898/2026.10.30.762838) |

These studies make ordinary retrieval, cue use, and feedback learning concrete competing explanations. None compared the signed and unsigned histories defined in §2.

## 5. Two proposed tests with distinct failure conditions

### A. Does the direction of past errors change a human correction?

Give participants an instrument-calibration task. On each history trial, show an instrument reading and a verified reference. The residual is the reading minus the reference, in the displayed units. At the probe, ask participants to revise a new instrument reading before revealing its reference. The response is their signed adjustment to the reading. Using instrument errors makes it possible to assign histories experimentally and avoids treating a person's reported confidence as a measured prediction error.

Randomize matched histories within participants. Persistent and alternating blocks have the same residual magnitudes at each position, the same length, the same final residual, and the same probe. Mirror all signs across trials and counterbalance block order. Start each block with a new instrument and a common, disclosed calibration history of zero bias. Include irregular histories that separate a geometric average from an ordinary mean and a last-error rule. Use enough observations for the chosen decay to produce a measurable contrast.

**Prediction.** Code an adjustment that compensates for the last error as positive. The signed-memory proposal predicts a larger compensating adjustment after persistent errors than after alternating errors. A rule using only absolute error history and the most recent sign predicts equal mean adjustments on these matched probes. An unweighted signed average, a learner estimating instrument bias, and the EFMW state can all predict the contrast. Compare their trial-level predictions on held-out participants and histories. The worked example uses $1/2$ for exposition. Score the benchmark’s fixed $0.97$ and, separately, any decay estimated from training data. An ordinary signed average with the identical exponential weights is an exact tie by construction.

**Decision rule.** Before enrollment, fix a smallest meaningful mean difference in instrument units, a sample size based on that difference, a participant-level interval method, and a holdout rule. Support for the directional prediction requires the interval to clear the positive margin. An interval inside a prespecified negligible-effect band, or a precise effect in the opposite direction, counts against the proposed transfer. An interval spanning meaningful benefit and negligible effect leaves the question unresolved. Success concerns adjustment to external feedback. A claim about monitoring one’s *own* errors requires a separate transfer experiment using genuine participant-generated errors.

### B. Does checking the basis of confidence repair additional mistakes?

Give everybody the same learning materials and questions. Each participant supplies an initial answer, rates confidence, and attempts unaided retrieval. Record an answer immediately after retrieval, before the final prompt. Randomly assign the prompt only after that answer is recorded. One group spends the allotted time checking the evidence for its answer again. The other spends the same time checking what made it confident in the first place and whether that cue deserves weight. Both see the same information and can revise once. Score responses against an independently fixed key.

**Prediction.** Among answers wrong immediately before the prompt, the confidence-check group will repair more errors. Among answers right before the prompt, it will introduce no practically important excess of harmful revisions. The competing account predicts that retrieval and additional time to review the evidence explain the benefit.

Report both denominators, both transition rates and participant-level uncertainty. A lower average confidence score is a secondary result. Before recruitment, set a minimum worthwhile gain in repairs and a maximum acceptable increase in harmful revisions, and power the study for both. An interval excluding the minimum repair gain counts against the proposed added benefit. An increase in harmful revisions beyond the prespecified tolerance defeats the joint prediction even if more wrong answers are fixed. This is a prospective design. Preregistration, recruitment and outcome data are outstanding.

## 6. Conclusion

The discovery is that the EFMW monitor remembers an imbalance between weighted positive and negative residuals. The cancellation identity gives the exact amount lost when the two directions offset each other. The frozen replay checks that this interpretation reaches the code that actually issued the warnings. At the human level, the open questions are whether people use error direction to decide how far to revise a judgment and whether examining the basis of confidence helps them repair an error that another look at the evidence would leave in place. Those are distinct claims, and either can fail on its own.

## Appendix. Reproduce the synthetic check

The following calculation uses Python 3.12.14 and NumPy 2.3.5. Run it from a checkout of the [benchmark at revision 4d35d5b](https://github.com/enuminous/EFMW-EXP-001/tree/4d35d5b461cc3663d96152f0665b2f8683bf82ae). It reads the frozen seed list and uses the published simulator and candidate score. The comparison computes the score directly from the weights.

```python
from pathlib import Path
import numpy as np
from monitors import EFMW_THRESHOLD, efmw_score, first_sustained_after
from simulator import simulate

seeds = Path("CONFIRMATORY_SEEDS_FROZEN.txt").read_text().split()
worst = 0.0
mismatches = 0
scores = 0
for seed in seeds:
    rows = simulate(int(seed))
    y = np.array([row[2] for row in rows])
    u = np.array([row[3] for row in rows])
    r = y[1:] - (0.82 * y[:-1] + u[1:])
    weights = 0.03 * 0.97 ** np.arange(len(r))
    closed = np.r_[0.0, np.abs(np.convolve(r, weights)[:len(r)])]
    recorded = efmw_score(y, u)
    worst = max(worst, float(np.max(np.abs(closed - recorded))))
    onset = rows[0][5]
    mismatches += (first_sustained_after(closed, EFMW_THRESHOLD, onset)
                   != first_sustained_after(recorded, EFMW_THRESHOLD, onset))
    scores += len(recorded)
print(len(seeds), scores, format(worst, ".3g"), mismatches)
```

Expected output in the stated environment is `40 20000 8.33e-17 0`. The third field can vary slightly across numerical environments.
