# When Errors Agree

*Directional coherence in EFMW residual memory*

**Matthew Chenoweth Wright · Monolithic LLC**  
**6 November 2026 · Mathematical research note**

## Abstract

An instrument can read too high on every observation. Its errors then agree perfectly in direction while every reading is wrong. The EFMW signed-memory identity makes that distinction measurable. For a shared set of memory weights, the magnitude of the signed residual average divided by the average residual magnitude is the fraction of weighted error that survives cancellation. We derive its exact relation to positive and negative error, give examples in which the same signed memory conceals different histories, and show why the two published EXP-003 monitor scores cannot simply be divided to obtain this fraction. Garret Sutherland’s external audit supplies the empirical boundary. He reproduced the frozen mean-drift result, then obtained the reverse ranking on an exploratory variance fault. The fraction developed here describes directional agreement. Its usefulness for issuing warnings or modeling human judgment remains an empirical question.

## 1. Coherence of what?

Think of a balance sheet. A net error of three units could come from three units of overestimation alone, or from ten units of overestimation offset by seven units of underestimation. Someone correcting a systematic bias might make the same adjustment in either case. Someone deciding whether to trust the instrument has a reason to care which history produced the three.

The EFMW monitor poses that question over time. It gives greater weight to recent residuals and retains their signs until it computes the size of the net error. The discovery within EFMW was to identify exactly what that implementation remembers. The earlier paper proves the equivalence to a signed exponentially weighted moving average and checks the formula against the published implementation. Here we ask what a coherence measure derived from that identity can legitimately tell us. [Signed-memory paper](https://github.com/enuminous/papers/blob/063e7bf3ee85eb672e71e75badf11526380da5ce/The-Signed-Memory-Identity-and-Human-Self-Correction-2026-11-06.md)

## 2. The fraction of error that survives cancellation

Let $r_j$ be observation minus prediction. For fixed decay $0<\lambda<1$ and zero initial state, use the same weights $w_{tj}=(1-\lambda)\lambda^{t-j}$ for every quantity below. Let $P_t$ be the weighted sum of positive residual parts and $N_t$ the weighted sum of negative residual magnitudes. Both are nonnegative. The signed state $m_t$ and total weighted magnitude $B_t$ satisfy

$$
m_t=P_t-N_t,\qquad B_t=P_t+N_t,\qquad B_t-|m_t|=2\min(P_t,N_t).
$$

The last equality follows by subtracting the absolute difference from the sum. For example, if the two contributions are seven and three units, $B_t=10$, $|m_t|=4$, and six units cancel. Each unit on the smaller side offsets one on the larger side.

For $B_t>0$, define the dimensionless directional coherence

$$
R_t=\frac{|m_t|}{B_t}
    =1-\frac{2\min(P_t,N_t)}{P_t+N_t}.
$$

The bounds $0\le R_t\le1$ follow immediately. At one, every nonzero weighted contribution has the same sign. At zero, positive and negative contributions balance exactly. If $B_t=0$, there is no weighted error to compare and the fraction is undefined. Reporting a zero in that case would give absence of error the same label as complete cancellation. Changing units multiplies both numerator and denominator by the same positive factor and leaves $R_t$ unchanged. The value of $B_t$ therefore belongs alongside $R_t$ whenever error size matters.

The construction has an established interpretation in directional statistics. Represent a positive error by direction $0$ and a negative one by direction $\pi$. Give each observation weight $w_{tj}|r_j|$. The weighted mean resultant length on those two opposite directions is exactly $R_t$. In the EFMW monitor this familiar statistic measures the share of weighted error magnitude that survives cancellation. [Berens, *CircStat* (2009)](https://www.jstatsoft.org/article/view/v031i10) · [Weighted resultant implementation](https://github.com/circstat/circstat-matlab/blob/master/circ_r.m)

## 3. What the instrument can forget

At decay $\lambda=1/2$, the most recent of three residuals has weight $1/2$, the previous one $1/4$, and the oldest $1/8$. These are exact illustrative inputs.

| Residuals, oldest first | Signed state $m_t$ | Total magnitude $B_t$ | Coherence $R_t$ |
|---|---:|---:|---:|
| $0,0,0$ | $0$ | $0$ | Undefined |
| $0,0,+1$ | $1/2$ | $1/2$ | $1$ |
| $+2,-1,+1$ | $1/2$ | $1$ | $1/2$ |
| $+2,-1,0$ | $0$ | $1/2$ | $0$ |

The middle rows have the same last observation and the same signed memory. One history contains twice the weighted error magnitude of the other. In the first and last rows, the signed warning score is zero in both histories, yet only one instrument has made errors. Keeping the signed state and total magnitude lets an observer recover the two contributions separately.

$$
P_t=\frac{B_t+m_t}{2},\qquad N_t=\frac{B_t-m_t}{2}.
$$

Even those two numbers cannot recover the order of every observation. Nor does high $R_t$ require repeated mistakes. After one positive residual followed only by zeros, $R_t$ stays at one at every finite later step while $B_t$ decays toward zero. A completely directional trace can carry almost no remaining error. A confidence rating, a measure of accuracy, or a warning threshold would each need its own justification.

## 4. A denominator the frozen comparison does not supply

The EXP-003 candidate uses decay 0.97 on signed residuals, while the baseline uses decay 0.90 on residual magnitudes. To describe the candidate’s directional coherence one must construct $B_t$ at **0.97** on the same residuals and with the same initialization. The published baseline measures a different memory window. [Frozen monitor code](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/monitors.py)

A single unit error followed by $k$ zeros gives an exact counterexample. The quotient of the published candidate score and the published baseline score would be

$$
\frac{0.03(0.97)^k}{0.10(0.90)^k}
=0.3\left(\frac{0.97}{0.90}\right)^k.
$$

After 17 zeros this is approximately 1.072, already above the largest possible fraction. For the same trace the matched-decay fraction is exactly one, as every nonzero residual has the same sign. The difference comes entirely from the two memory lengths. No EXP-003 alert was based on $R_t$.

## 5. Where the distinction mattered in EXP-003

Sutherland’s public audit puts the boundary alongside the reproduced finding. He varied residual sign treatment and memory length separately. On his own exploratory variance fault, he retained the thresholds calibrated for each monitor and used the same actionable-warning criterion. The following counts are from his archived report. [Sutherland’s original audit, data and logs](https://github.com/enuminous/EFMW-EXP-001/tree/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret)

| Synthetic fault | Signed memory, decay 0.97 | Absolute-error baseline, decay 0.90 |
|---|---:|---:|
| Frozen mean-drift benchmark | 77/80 actionable warnings | 65/80 actionable warnings |
| Sutherland’s exploratory variance fault | 41/80 actionable warnings | 77/80 actionable warnings |

Sutherland reproduced the frozen **+41.5-timestep** median paired warning-lead gain on the original benchmark. That endpoint scores runs without an actionable warning using the protocol’s missed-warning convention. The table keeps the detection counts visible separately. In the exploratory extension the ranking reversed. The patch replaced the additive drift bias and sinusoid with growing zero-mean process noise while retaining the original change in the autoregressive coefficient. The original result stands for the published fault and monitor settings. [Sutherland’s two comparisons](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/attachments/README.txt) · [Frozen endpoint](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/protocol.md)

The mathematics explains why positive and negative errors can cancel in the candidate even as their magnitudes grow. The experiment reports what happened to warnings in the two settings. It measured the published detectors, and it leaves open whether using $R_t$ would improve detection. In particular, a large $R_t$ after a single small error would be a poor reason on its own to raise an alarm.

## 6. A question for human coherence studies

The middle rows of the example suggest a behavioral comparison. Show an observer two histories with the same latest error and the same signed memory but different total error magnitudes. On an identical next probe, ask how far to correct the instrument. Then, separately, ask how reliable the corrected reading will be. The first judgment concerns the direction of the bias. The second concerns variation around that bias.

The prediction is that bias corrections will agree within a prespecified tolerance while reliability ratings will be lower for the history with greater total error. A precise reversal, or an interval that excludes a preregistered meaningful reduction in reliability ratings, would count against that prediction. An ordinary bias estimator paired with a noise estimate is a competing explanation. At fixed $m_t$, changing $B_t$ also changes $R_t$, so this comparison alone cannot tell which quantity the participant used. A discriminating study would vary both quantities across additional histories, specify the competing response rules in advance, and compare predictions on held-out participants and histories. An instructed assessment of an instrument would also need a separate transfer test before drawing conclusions about how people monitor their own mistakes.

## Conclusion

The remarkable feature of this example is how precisely the word *coherence* can be used. The residuals agree in direction to a measurable extent. Their total magnitude tells us how much error was available to agree or cancel. Sutherland’s two fault settings show why both questions are worth asking. An observer trying to correct bias and an observer trying to detect growing disturbance can read the same history accurately and have good reason to act differently.

*Evidence scope. The examples are algebraic. The benchmark figures are attributed to the published record. This note adds no experimental run, threshold calibration, or human observations.*
