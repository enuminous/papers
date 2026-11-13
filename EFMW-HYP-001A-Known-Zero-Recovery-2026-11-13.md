# EFMW-HYP-001A — Known-Zero Recovery Under Drift, Crosstalk, and Thermal Lag

**Matthew Chenoweth Wright / Monolithic LLC**  
**13 November 2026 · Synthetic computational experiment · Verdict: FAIL (naive), UNRESOLVED (adjusted)**

## Abstract
A proposed EFMW physical coupling, \(\kappa CM\), must not be inferred merely because its regression coefficient differs from zero. We evaluated whether a synthetic analysis pipeline recovers a *known zero* under correlated conventional disturbances. We generated 1,000 independent synthetic trials with \(\kappa=0\) and 1,000 with \(\kappa=0.35\), each containing 400 observations. The naive regression produced false exclusions of zero in **999/1,000 (99.9%)** null trials. A nuisance-adjusted heteroskedasticity/autocorrelation-consistent (HAC) regression reduced this to **99/1,000 (9.9%)**, still exceeding the nominal 5% rate. Thus neither pipeline passes a nominal 95% null-calibration gate as currently specified.

## Generative model
Define coherence \(C_t\) as a clipped oscillatory stochastic sequence, memory by \(M_t=M_{t-1}+(C_t-M_{t-1})/18\), and \(X_t=C_tM_t\). The synthetic response is

\[
Y_t=\kappa X_t+0.7D_t+0.45Q_t+0.65T_t+\epsilon_t.
\]

Here \(D_t\) is a random-walk drift plus linear trend; \(Q_t=0.65C_t+0.3C_{t-2}+\eta_t\) is crosstalk; \(T_t=T_{t-1}+(Q_t-T_{t-1})/26\) is thermal lag; and \(\epsilon_t=0.65\epsilon_{t-1}+\xi_t\) is autocorrelated noise. See the companion script for exact initial conditions, noise scales, and reproducible random-number stream. Units are arbitrary standardized force units, **not newtons**. These data are simulated, not measurements.

## Estimators
1. **Naive H2:** ordinary least squares \(Y_t\sim 1+X_t\) with conventional iid standard errors; intentionally omits confounders.
2. **Nuisance-adjusted H2:** \(Y_t\sim 1+X_t+D_t+Q_t+T_t+t\), with HAC covariance using 20 lags. This is optimistic about experimental observability of nuisance signals.

A two-sided nominal 95% confidence interval is counted as a detection if it excludes zero. Null false-positive rate is that count divided by 1,000. Truth coverage measures the fraction of intervals containing the generating coefficient. Interval width is upper minus lower bound.

## Results

| Generating κ | Estimator | Mean fitted κ | Zero excluded | True κ covered | Median 95% CI width |
|---|---|---:|---:|---:|---:|
| 0 | Naive iid | +0.5534 | **99.9%** | 0.1% | 0.3014 |
| 0 | Nuisance + HAC | −0.0046 | **9.9%** | 90.1% | 0.4342 |
| 0.35 | Naive iid | +0.8978 | 100.0% | 0.2% | 0.3004 |
| 0.35 | Nuisance + HAC | +0.3508 | 83.4% | 88.6% | 0.4296 |

Each row represents 1,000 simulations; there are 4,000 fitted result rows total. The adjusted model recovers the nonzero coefficient in mean but still undercovers. The injected condition's 83.4% zero-exclusion rate is detection power, not false-positive rate.

## Interpretation
The naive pipeline almost always confidently reports a nonexistent interaction. That is a **decisive failure of the naive estimator under this synthetic data-generating process**. It does **not** prove that all prior exploratory EFMW estimates are noise or that the underlying physical hypothesis is false. The adjusted pipeline is less biased but its 9.9% null false-positive rate is about twice the nominal 5% and its confidence intervals are not calibrated. Therefore it is not ready to serve as confirmatory evidence.

The synthetic design intentionally correlates coherence with nuisance channels. Results depend on that choice, sample size, nuisance magnitudes, memory and noise timescales, and the HAC lag choice. The same script uses one random stream sequentially for the null and injected experiments; reproducibility requires preserving its seed and ordering.

## Next validation gate
Freeze an estimator and calibration procedure *before* testing on fresh synthetic datasets. Demand near-nominal known-zero false-positive rates with uncertainty bands, calibrated interval coverage, and recovery/power for preregistered injected values. Stress-test omitted or imperfectly measured nuisance signals, varying noise timescales, collinearity, sample size, and multiple testing. Report failures and UNRESOLVED cases. A pipeline passing these tests warrants *consideration* of P1 hardware design; P2–P4 require separate physical and statistical validation.

## Reproducibility
- Random seed: `20261113`
- Observations per trial: `400`
- Trials: `1000 null + 1000 injected`
- Injected coefficient: `0.35`
- Estimation: Python, NumPy, SciPy, pandas, statsmodels
- Companion: `EFMW-HYP-001A/run.py`, `EFMW-HYP-001A/summary.csv`
- Full replicate-level data were generated locally as `replicates.csv`; the published summary and code permit regeneration.

**Scientific status: naive estimator FAIL; adjusted estimator UNRESOLVED; EFMW physical coupling unestablished.**
