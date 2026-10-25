# EFMW-BIO-001 — frozen exploratory biological-memory screen

Date: 2026-10-25. Authoring/analysis: ChatGPT for Matthew Chenoweth Wright.
This protocol is frozen before loading individual protein outcomes, fitting models,
or calculating predictive performance. Dataset headers, row counts, grouping metadata,
the source paper's published results, and the existing EFMW code were inspected.
This is a timestamped local analysis plan, NOT an externally registered preregistration.

## Target and provenance

Question: does adding the existing EFMW-style recursive memory update to elementary
ERK summary features improve prediction of endpoint nuclear Fra-1 measurements
on held-out experimental replicates, relative to conventional models?

Source: Ram et al., Nature Communications 16, 4721 (2025), DOI
10.1038/s41467-025-58348-7. Figshare DOI 10.6084/m9.figshare.27047617.v1,
CC BY 4.0, SourceData.zip, SupplementaryData1 (MCF10A).
Use all rows in the supplied matched df_erk, df_ETGs, and df_tx tables.
They contain 71,459 matched rows, 190 time samples, eight nuclear targets, and
three independent experimental replicate identifiers (1, 2, 3).
Row correspondence is asserted by the authors' README; no independent cell ID is supplied.

Primary outcome: log10(FRA1_nuc). The other seven nuclear proteins are secondary,
reported without selecting a favorable target. cJun_nuc is a biological negative
control as described in the source paper, not necessarily an uncorrelated variable.
These are measured endpoint stains, not generated targets. This is endpoint
prediction from the complete preceding ERK trace, not forecasting future disease.

## Mandatory limitation known before evaluation

The authors corrected stain batch effects using matched-treatment medians across
all three replicates, aligning replicates 1 and 2 to replicate 3 in log space.
Consequently these published labels are not independent of held-out batches at
the upstream preprocessing stage. We cannot claim a completely untouched external
test or clinical validation. Our own preprocessing, feature scaling, model fitting,
and hyperparameter selection must use training data only. No synthetic replacement
of unavailable data is permitted. No claims about the original paper's model ranking
are implied: our split and weighting differ, and its CNN is not reproduced here.

## Quality and units

Retain traces with at least 80% finite samples (152 of 190). Interpolate missing
samples linearly within each individual observed trace; carry nearest observed
value at either end. This uses only that cell's preceding observed window and no
other cell or outcome. Exclude a cell for a target if that target is missing,
non-finite, or nonpositive. No target outlier filtering or winsorization.
No clipping of finite ERK values. Targets are log10 of author-normalized staining
intensity. ERK inputs are the authors' calibrated, normalized activity readouts.
Both are assay quantities, not physical EFMW field variables.

## Frozen candidate and conventional overlap

Existing code source: enuminous/EFMW-EXP-001/monitors.py, blob
aef763fa47d15a7438f9f917700d59209c13724a.
Its memory is m[t]=0.97*m[t-1]+0.03*r[t], score=abs(m[t]), m[0]=0.
The original r[t]=y[t]-(0.82*y[t-1]+u[t]) is specific to a synthetic controlled
plant. That plant model is not asserted for a cell. This explicit biological
adaptation sets the input r[t]=observed ERK activity x[t], for t=1,...,T-1.
It retains the zero initial state, 0.97 coefficient, and absolute terminal score.
This is an EFMW-inspired feature transfer, not an unchanged validation of EXP-001,
and not a derivation of EFMW's physical field equation.

The candidate's five predictors: whole-trace mean, population standard deviation,
mean of first 10 samples, mean of last 10 samples, and abs(m[T-1]).
The four-predictor summary model is its no-recursion ablation.
The recurrence is exactly a conventional exponential filter. A second independent
implementation uses the closed form abs(0.03*sum(0.97**(T-1-t)*x[t], t=1..T-1)).
It must match features and predictions within floating-point tolerance.
No unique algorithmic novelty can be established by this candidate.

## Frozen model roster

1. Training mean only (intercept).
2. Snapshot: last 10 sample mean.
3. Time average: whole-trace mean.
4. Summary ablation: four summary predictors above.
5. EFMW-inspired: summary plus fixed 0.97 absolute memory score.
6. Matched conventional EWMA: summary plus identical closed-form feature.
7. Multiscale conventional EMA: summary plus terminal signed EMA states for
   a in [0.5, 0.8, 0.9, 0.97, 0.99, 0.995]. Zero initial state, same t range.
8. Temporal bins: mean of each of 19 consecutive blocks of 10 samples.
9. Production-decay filter bank: summary plus nine two-stage terminal states,
   m[t]=a*m[t-1]+(1-a)*x[t], p[t]=b*p[t-1]+(1-b)*m[t],
   with (a,b) in [0.8,0.97,0.995] squared. This is a discrete linear
   transcription/translation surrogate, not the full nonlinear published ODE.

All non-intercept models use the same standardized ridge regression procedure,
with an unpenalized intercept and alpha in [0.1,1,10,100,1000]. No nonlinear
expansion, neural-network training, or tuning of the fixed EFMW coefficient.
The standard comparator feature counts differ and are reported; all receive
identical raw modalities, data splits, target, and ridge tuning budget.
No treatment identity, replicate ID, well ID, or other protein is a predictor.

## Splits, fitting, and metrics

Outer leave-one-replicate-out evaluation: hold out replicate 1, 2, then 3.
Inner tuning: of the two remaining replicates, train on one and validate on the
other in each direction. Choose each model's ridge alpha by the mean inner
replicate score; ties go to the first (smaller) alpha. In each outer split,
also choose the strongest conventional comparator using inner scores only
from models 2,3,4,7,8,9, then refit that selected model on both training replicates.
The equivalent EWMA is checked separately and not used for adaptive selection.

Training weights make each replicate equally weighted and each well within a
replicate equally weighted. Cell weights sum to the number of training cells.
Feature centering/scaling uses these training weights. No test fitting.
Primary score: for each held-out replicate, average squared log10 errors within
each well, then average wells. Aggregate the three replicate scores equally.
Secondary scores: similarly weighted MAE and out-of-sample R2 relative to the
held-out replicate's weighted mean (evaluation denominator only).
Report cell counts, well counts, fold scores, and chosen hyperparameters.

## Success and failure criteria

Practical performance screen passes only if the candidate reduces the primary
macro MSE by at least 5% versus the training-selected conventional comparator,
has lower MSE in all three held-out replicates, and improves over the summary
ablation in all three replicates. Otherwise the proposed performance advantage
fails this screen. The 5% threshold is a prespecified methodological screen,
not a clinical threshold. Any pass is provisional due to upstream normalization.

Statistical evidence is separate: use an exact paired sign-flip test on the three
replicate-level MSE differences, and report its limited resolution. Three replicates
cannot support a two-sided p<0.05 sign-flip result. Do not treat 71,459 correlated
cells as 71,459 independent experimental replications. Bootstrap intervals, if
shown, resample whole replicates and are descriptive given n=3.

Novelty screen: conventional EWMA equivalence rejects any claim of a unique
EFMW-specific memory algorithm for this recurrence regardless of predictive scores.
Remove-recursion performance is an ablation, not proof of a biological mechanism.
All secondary target results remain exploratory with no confirmatory claims.

## Audit and deliverables

Preserve source URLs, source archive/member checksums, this protocol and its SHA256,
code, software versions, complete retained numeric data, fold predictions, and
all results including failures. Use fixed seed 20261025 for optional resampling.
No post-result model revision is authorized under this protocol. Correct coding
errors transparently, preserving the original protocol and a deviation log.
No named Zoo animal operation is claimed without loading its canonical definition.
This screen applies the Zoo skill's evidence, independence, and novelty rules.
