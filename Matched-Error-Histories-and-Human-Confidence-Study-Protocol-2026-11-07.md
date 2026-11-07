# Matched error histories and human confidence

*Prospective controlled study protocol*

Version 1.0  |  7 November 2026  |  Proposed design for review

**Repository publication status:** Protocol draft, not preregistered and not a report of a completed study. [Original editable document](Matched-Error-Histories-and-Human-Confidence-Study-Protocol-2026-11-07.docx).

<!-- Original delivered DOCX SHA-256: c492b0d2cd22662b98476bbba8f0f2523eab3233bebd4e8d451aff6715fc0926 -->

This protocol tests whether changing the order of matched feedback errors changes confidence while leaving correction practically unchanged. The primary experiment uses assigned histories from a simulated instrument. Confidence is measured for an identical corrected probe, and correction is measured separately on free-response probes. This separates a causal history-order effect from the stronger claim that people compute a particular memory statistic.

The design is not ready for registration or recruitment until the pilot, model lock, stimulus manifest, power simulation, and ethics review described below are complete. All numerical design choices in this document are proposals, not estimates established by the existing human analysis. No prospective data have been collected for this protocol.

## 1 Research claim and evidence boundary

The source paper reports a small incremental predictive contribution from weighted absolute error in an exploratory reanalysis. The primary first-session loss-gain interval includes zero; retest is a returning subset, not a new independent cohort. Those results do not establish a causal effect, a useful effect size, or adjustment equivalence. The 362 exact history pairs establish a stimulus construction, not 362 human observations. [1–4]

The confirmatory target is a finite-bank average treatment effect: among eligible adults and the frozen stimulus bank, does the higher-absolute-memory history lower confidence by more than the prespecified meaningful amount, while mean direction-aligned free correction differs by less than a prespecified tolerance? A positive result would support sensitivity to history order beyond the named matched-moment comparator. It would not by itself identify a coherence calculation, conscious self-reflection, or a distinctive EFMW mechanism.

Evidence status at launch: the supplied moment identities are demonstrated algebraically and checked computationally. The proposed confidence decrease and correction equivalence are hypotheses. Generalization to personally generated mistakes and the psychological memory-decay parameter remain unresolved.

## 2 Exact quantities and stimulus audit

An error is the true result minus the instrument reading, measured in stimulus units. A positive correction is added to the reading. For each episode, signed memory m, absolute memory B, and squared memory Q start at zero. After each observed error, replace each memory by half its previous value plus half the new signed error, absolute error, or squared error, respectively. Coherence R is the absolute value of m divided by B when B is positive. Q has squared units; m and B have stimulus units; R is dimensionless.

Use the source bank at repository commit 1a407e130b4f6375435e3a518c1a367232970ce4. Within every pair, history A has larger B than history B. The two histories have the same length, error multiset, final two errors, nonzero m, and Q. Their B and R values differ. At fixed m, larger B necessarily means smaller R; this manipulation cannot distinguish those accounts. The conventional concentration measure |m|/√Q is also matched. [2–3]

A direct rational-arithmetic audit for this protocol verified all 362 rows. Fourteen rows have six observations and 348 have seven. Collapsing global sign mirrors leaves 181 pairs. Removing the positions that are identical in both histories and then collapsing sign mirrors produces five distinct ordered mismatch patterns. This last count is an explicitly defined dependence diagnostic, not a count of independent psychological stimulus types. The differences in B range from 1/64 to 7/64 stimulus units.

For illustration, appending the common zero to the original example gives A = (3, 0, −1, 2, 1, 0) and B = (−1, 2, 3, 0, 1, 0). Both have m = 31/64 and Q = 61/64. Their absolute memories are 39/64 and 33/64. Both end with (1, 0). The shorter five-observation example alone is not an adequate last-two-error control.

Before registration, regenerate the bank from the frozen generator, compare byte-normalized files and rational values, and record SHA-256 digests of the exact experimental assets. Preserve each original row ID, sign-canonical pair ID, construction-family tag, history length, sign orientation, and all model predictions. Do not choose pairs using confirmatory outcomes.

The primary bank retains the final zero. A separately labeled diagnostic set will append an identical +1 or −1 observation to both members, balanced across signs. This halves their existing B difference, preserves equal m and Q, and makes the last two observations identical and nonzero-ending. Recheck nonzero signed memory and every matching assertion. These are newly constructed stimuli and do not replace the original bank or count as an independent replication.

## 3 Study structure and provisional settings

| Design element | Proposed specification |
| --- | --- |
| Population | Adults aged 18 or older, able to consent and understand the task language; desktop or laptop input. Recruitment source and jurisdiction must be set before ethics submission. |
| Preparation | 20 usability participants, then 60 separate calibration participants on the finalized task. No pilot participant enters the confirmatory sample. |
| Primary session | 72 episodes: 48 critical, 12 controls, and 12 diagnostic episodes. Pilot verifies duration and fatigue before this count is locked. |
| Critical episodes | 24 fixed-correction confidence probes and 24 free-correction probes. Each mode has 12 high-B and 12 low-B histories, with balanced memory sign. |
| Stimulus scale | One error unit is one displayed numerical unit. Probe tolerance is ±1 unit. Free correction range is −6 to +6 units, with 0.01-unit resolution. |
| Confidence | Explicit probability from 0 to 100 in one-point steps; no preselected answer or movable slider starting point. |
| Meaningful confidence decrease | 3 percentage points on the fixed-correction confidence scale. This is a proposed smallest effect of interest, not an estimate from the paper. |
| Correction equivalence margin | −0.10 to +0.10 stimulus units for the mean direction-aligned treatment contrast, equivalent to 10% of the probe half-width. |
| Confirmatory sample | Chosen by the simulation rule in Section 8 and locked before recruitment. No defensible final sample size follows from 362 constructed pairs. |

The investigator must defend the three-point confidence threshold and the 0.10-unit correction margin in practical task terms before seeing confirmatory data. The margin must exceed input quantization but remain smaller than a consequential correction. If the pilot requires a different scale or tolerance, update the margins and power calculation prospectively and version the protocol. Do not widen the margin or reduce the meaningful effect to accommodate observed results.

## 4 Task and randomization

### External instrument task

Tell participants that they are evaluating a simulated instrument using experimenter-constructed calibration examples. Do not describe the sequences as their own mistakes or as naturally sampled records. Explain the error sign and the probability question with neutral examples that are not target pairs. Do not reveal B, R, the expected direction, or the matched-pair construction.

Each episode introduces a new instrument and an explicit reset. Display its six or seven errors serially, oldest first, each for 1,000 ms with a 250 ms blank interval. Use the same layout, exposure time, instrument label format, reading anchor, and response controls for both variants. Do not leave a cumulative history chart visible in the primary memory condition. Training and neutral fillers explain resets but cannot guarantee a biological memory reset; record episode position and test carryover secondarily.

On fixed-correction probes, show the same new reading of zero and the same candidate correction for both variants: the pair’s common m in stimulus units. Ask: “What is the probability that the true result will be within 1 unit of this corrected reading?” The candidate correction and target event are identical within a pair. No participant correction precedes the primary confidence judgment.

On free-correction probes, show the new reading of zero and ask participants to choose its signed correction. Lock that response, then ask confidence that the true result is within 1 unit of their corrected reading. The correction is the co-primary endpoint; confidence here is secondary because the target interval now depends on a treatment-affected response. Never control for that response in the primary causal confidence test.

For each pair, generate the probe’s true residual from the same normal reference distribution in both variants, with mean equal to the common m and standard deviation 1 unit. Use a precomputed outcome pool and independently randomized draws, balanced between conditions. The fixed corrected probe therefore has the same objective coverage probability across history variants. Outcomes are for scoring and calibration, not inputs to the current judgment. Do not show critical-probe outcomes until the end of the session. This is a test of confidence sensitivity, not a demonstration that a lower rating is more accurate or normatively optimal.

The simulated probe rule and selection of histories are design choices rather than a natural data-generating model validated by the source paper. Freeze the participant instructions and disclose the constructed nature of the examples without teaching the hypothesis. Check credibility, comprehension, confidence range, and ceiling effects in the pilot. A Bayesian change-point model is a candidate account of perceived history structure, not automatically the true normative model of this constructed task.

### Allocation and concealment

Sample 48 distinct sign-canonical pairs per participant from the 181-pair bank, without showing the alternate version or its mirror to that participant. Randomize probe mode, high/low-B variant, and global sign under the exact balance constraints above. Use a pre-generated balanced allocation schedule so that every pair is tested in both variants and modes across participants. The target estimate weights all 181 canonical pairs equally and both signs equally; retain assignment probabilities for any weighting required by a nonuniform schedule.

Interleave controls and diagnostics using a frozen schedule, with breaks after every 24 episodes. Balance episode positions across conditions, avoid long same-condition runs using one documented constrained-randomization algorithm, and retain its seed. Analyze under the actual constrained assignment scheme. Keep participant-facing labels and analyst condition codes neutral until exclusions, data checks, and analysis scripts are locked.

The primary instrument task uses stable incentive instructions. Pay a fixed fair base rate and, if approved, a bounded bonus from a pre-announced proper probability scoring rule on a randomly chosen eligible probe. Freeze the scoring rule and maximum bonus in consent. Do not pay for guessing the hypothesis, rating lower confidence, or matching a model. Practice should explain the scoring rule without creating an anchor for target confidence.

## 5 Controls and diagnostic questions

The 12 control episodes contain six obvious directional-bias checks and six reliability checks, balanced in sign and probe mode. Direction checks use consistently positive versus negative errors and should reverse free correction. Reliability checks hold the candidate correction fixed but vary the displayed dispersion strongly. Fix their exact sequences and expected contrasts before the calibration pilot; choose ranges that avoid arithmetic and motor ceiling effects. Controls verify that the task can elicit correction and confidence responses, not that participants agree with the target hypothesis.

The 12 diagnostic episodes comprise six balanced common-nonzero-tail probes and six model-disagreement probes selected entirely by frozen stimulus properties and pilot-fitted predictions. The latter may use additional histories varying m and B separately, with common-m or common-R subsets where feasible. Record which controls cease to be matched. These episodes support mechanism comparison only and do not alter the primary original-bank estimate.

No control result can exclude a participant after randomization merely because their confidence–error slope is inverted, flat, or opposite to the hypothesis. At the study level, report positive-control contrasts and their intervals. If the controls show no usable response range or fail their frozen directional checks, describe a target null as task-limited. Do not erase such a null or redefine the endpoint after inspection.

Collect an end-of-task comprehension and strategy questionnaire after all target outcomes. Ask about recalled recent errors, perceived changes, use of order, and whether examples felt like instrument or personal errors. Treat these reports as secondary descriptive measures; they do not establish a latent computation or conscious introspective access.

## 6 Competing models and the lock before confirmation

Freeze code, inputs, transformations, priors, parameter bounds, fitting loss, complexity penalties, and predictions for every stimulus before opening the confirmatory data. Use calibration-pilot outcomes for parameter estimation only. Deposit the final parameter file and digest with the registration. Numerical model parameters are not currently known; this protocol freezes the estimation rule rather than pretending they have already been measured.

| Model | Definition and role |
| --- | --- |
| Matched moments | Half-decay m, absolute m, square root of Q, concentration \|m\|/√Q, history length, and the last two signed, absolute, and squared errors. Prespecified linear terms and pilot-defined quartile hinges. For a fixed identical probe, every input is identical within a pair, so this comparator predicts an exact tie. |
| Alternative decay moments | The same moment model evaluated at retention weights 0.10, 0.25, 0.50, 0.75, and 0.90. Select one weight using grouped pilot validation only, and retain the full grid as a sensitivity set. Its within-pair moments generally cease to match away from 0.50. |
| Older lag model | Signed, absolute, and squared errors at each of the seven lags; explicit presence indicators for shorter histories. Use standardized features and ridge shrinkage selected in pilot validation. This is a flexible recency benchmark, not an independent rival to all absolute-memory computations. |
| Change point model | Bayesian run-length mixture for a latent residual mean with normal observation noise. Constant hazard on a frozen grid; normal reset prior; update all run lengths exactly for these short histories. Predict the next residual distribution, its mean, and mass within the actual fixed probe interval. |
| Absolute memory extension | Matched-moment model plus one linear half-decay B term. No sign constraint during fitting; a positive fitted slope is a legitimate contrary result. |
| Coherence extension | Matched-moment model plus one linear R term, fitted separately from B. No within-pair claim can distinguish B from R; the independent variation in diagnostic families is required. |

For reproducibility, use ridge penalties {0.01, 0.1, 1, 10, 100}; standardize features on pilot training folds only; use squared error for both confidence and correction forecasts. Form five deterministic participant-grouped folds and a separate leave-construction-pattern-out validation. Choose tuning settings by mean participant-weighted validation loss; break ties within 0.1% of loss in favor of the more strongly regularized or simpler model. Refit the selected setting on the complete calibration pilot and freeze it. Keep all related variants and mirrors together in stimulus-family validation. If the five-pattern split cannot identify a stable model, state that limitation and restrict interpretation rather than relabeling variants as independent.

For the change-point model, use a normal reset prior centered at zero; reset standard deviations {1, 2, 4} units; known candidate observation standard deviations {0.5, 1, 2}; and hazards {0, 0.01, 0.05, 0.10, 0.20, 0.50}. Update the full Gaussian posterior for each possible run length, with a new-segment branch at every observation. Select parameters using the same grouped pilot rule. At the probe, include the possibility of a new segment before predicting. Confidence is the model predictive probability of the stated interval; calibrate this probability with an intercept and a nonnegative slope on its logit using the pilot only. Apply a fixed 0.005 to 0.995 probability bound only for numerical stability. Archive a tested implementation, including initialization and whether the change occurs before an observation.

The unrestricted absolute-lag features can represent B exactly because B is a weighted sum of those features. Adding B to that full lag model is therefore not an identifiable test of extra information. The comparison concerns a restricted, compact weighting rule versus more flexible recency rules and their out-of-sample performance. If both predict the result, report them as observationally compatible. Similarly, a half-decay memory match does not establish that humans actually retain half the preceding state.

Estimate any individual decay parameter from a separate calibration task or independent correction/recall trials, not from the confidence contrast being explained. Such individual-decay analyses are secondary unless their task, reliability requirements, and model are fully registered before confirmation. No post hoc decay search can replace a failed primary half-decay test.

## 7 Outcomes and statistical analysis

### Two co-primary estimands

Confidence contrast ΔC: the average fixed-probe confidence rating after the higher-B history minus that after the lower-B history, in percentage points, standardized to equal pair and sign weights. The predicted direction is negative.

Correction contrast ΔD: on free probes, first multiply the chosen signed correction by the sign of that pair’s common m; then compare the higher-B and lower-B conditions in stimulus units. Sign alignment prevents positive and mirrored negative effects from canceling by construction. The equivalence claim concerns this mean, not equality of individual responses or entire distributions.

Fit each outcome with prespecified pair-by-sign fixed intercepts, participant random intercepts and treatment slopes, and treatment-by-sign terms, including probe mode only in analyses that pool modes. Estimate the marginal contrast by equal weighting of frozen pair/sign cells. Include episode block; history length is absorbed by pair effects. Keep only pre-assignment/design covariates in the primary causal analysis. Do not adjust for current correction, response time, elicited confidence, or perceived change-point judgments as though they were pretreatment controls.

Use maximum likelihood with the prespecified random-effects structure. If the fit is singular or fails, first remove random-effect correlations, then the participant treatment slope, in that order. Never change fixed treatment terms to achieve significance. Use a participant-cluster bootstrap with 5,000 resamples, refitting the full analysis on every resample, for percentile confidence intervals. If this procedure fails, report the failure and the locked simpler model result; do not substitute an unregistered method without labeling it exploratory. Simulations must verify interval coverage under the exact design before this plan is registered.

The primary uncertainty target generalizes across people while treating the 181 canonical pairs as a fixed stimulus population. A separate crossed participant-and-stimulus sensitivity analysis and leave-pattern-out results address stimulus generalization. They cannot turn five related construction patterns into a broad random sample of human experiences. Report both the finite-bank limit and any instability across patterns.

### Decision rules

| Finding | Prespecified interpretation |
| --- | --- |
| Meaningful predicted dissociation | The upper endpoint of the two-sided 95% interval for ΔC is below −3 points, and the entire two-sided 90% interval for ΔD lies strictly inside (−0.10, +0.10) units. Both requirements must pass. |
| Directional effect only | The 95% interval for ΔC lies below zero but does not establish a decrease greater than 3 points, or correction equivalence is not established. Do not call the full prediction confirmed. |
| Meaningful decrease ruled out | The lower endpoint of the 95% interval for ΔC is above −3. This counts against the specified effect size, even if a smaller negative effect remains possible. |
| Practical confidence null | The entire 90% interval for ΔC lies within (−3, +3). This supports equivalence on the chosen confidence scale; it is not inferred from a nonsignificant test. |
| Reversal | The 95% interval for ΔC lies entirely above zero. A lower endpoint above +3 establishes a practically meaningful reversal under the chosen threshold. |
| Correction failure | A correction interval establishes a difference outside the equivalence bounds, or sign-stratum diagnostics show opposing material effects hidden by the average. The proposed confidence–correction dissociation is unsupported. |
| Unresolved | Intervals are too wide, attrition is materially differential, the task lacks useful positive-control sensitivity, or measurement/model checks fail. Report what remains unidentified. |

The joint success criterion is an intersection–union claim: both conditions are required, so separate success declarations are not chosen from multiple outcomes. Report all component estimates and intervals regardless of the headline. Use Holm adjustment for any family of formal secondary model-comparison claims. Report all diagnostic, free-probe confidence, sign-stratum, accuracy, and strategy results as secondary, with an explicit distinction between registered and exploratory analyses.

For correction, also report treatment contrasts separately for positive and negative memory orientations, absolute correction, response-bound frequency, variance, and selected quantiles. Mean equivalence alone does not establish equivalent correction distributions. If heterogeneity is large, limit the conclusion to the registered mean or report the dissociation as inadequate for the broader claim.

Score frozen model predictions on the confirmatory sample without retraining: participant-weighted mean squared error and pair-level prediction contrasts. Report calibration, errors by family, and actual versus predicted effect direction. For confirmatory comparative claims, use participant-cluster loss-difference intervals conditional on the frozen pilot-trained models and disclose that limitation. A separate outer bootstrap that refits the pilot models assesses training uncertainty. A causal history-order effect is not uniquely attributed to B or R if the frozen recency or change-point models explain it comparably well.

## 8 Sample size and stopping rule

Do not convert the source paper’s tiny prediction-loss gains or its conditional fitted slopes into a causal effect size. The stimulus-bank count, the number of source trials, and overlapping training folds also cannot supply the prospective sample size. Use pilot estimates only for nuisance quantities such as variance, within-person dependence, ceiling mass, dropout, and model reliability. The minimum meaningful effect remains chosen in advance.

Power the joint decision by simulation of the exact allocation, pair reuse, participant treatment slopes, response bounds, missingness, and analysis procedure. Use at least 10,000 replicates per candidate sample size, fixed documented seeds, and a grid of nuisance values spanning the pilot interval rather than a single optimistic estimate. Simulate a planning alternative of ΔC = −5 points and ΔD = 0 units. A true decrease exactly at the −3-point boundary cannot yield high probability of establishing an effect beyond that boundary.

Select the smallest sample size on a grid in increments of 20 that achieves at least 90% joint success under the planning alternative and the prespecified conservative nuisance scenarios. Also verify false joint-support rates at the confidence boundary and correction-equivalence boundaries. Report power at −1, −3, −5, and −7 confidence points and at correction differences 0, 0.05, 0.10, and 0.20 units. Use a separately chosen maximum recruitment budget; if no feasible sample meets the criterion, redesign or state the achievable precision before confirmation starts.

The following independent-participant approximations illustrate scale only. They assume normally distributed participant-level high-minus-low contrasts, ignore stimulus and allocation complications, and target 95% power for each component so that joint power is at least 90% by a union bound. They are not a completed power analysis.

| Endpoint | Assumed contrast SD | Approximate analyzable N |
| --- | --- | --- |
| Confidence, true −5, threshold −3 | 8 / 12 / 16 points | 208 / 468 / 832 |
| Correction, true 0, margin ±0.10 | 0.25 / 0.40 / 0.60 units | 82 / 208 / 468 |

For confidence, the approximation squares the sum of the 97.5th and 95th standard-normal quantiles, multiplies by contrast variance, and divides by the squared two-point gap between the planning alternative and threshold. For correction, it uses the sum of the 95th and 97.5th quantiles, the contrast variance, and the squared 0.10-unit margin. The same quantile sum occurs for different reasons. Round upward. Final simulation takes precedence.

Once N is locked, recruit to that number of eligible analyzable participants, replacing only prespecified technical or eligibility exclusions and recording every replacement. Fix a maximum number of attempts and a calendar stop date before launch. No outcome-based interim looks, early success stopping, or extension after a near miss. Report attrition and total recruited. Any ethically required safety stop remains possible and must be documented.

## 9 Eligibility exclusions and missing data

Before randomization, require informed consent, adulthood, successful device checks, and correct answers to error-sign, correction, and probability questions after at most two instruction attempts. Freeze the exact items and passing rule. Record failures separately from post-randomization exclusions. Do not gather unnecessary diagnoses, financial information, or other sensitive attributes.

Exclude post-randomization records only for verified duplicate participation, ineligible age or consent, a confirmed rendering/assignment failure, or insufficient recorded task exposure under the rule locked after usability testing. A proposed exposure rule is fewer than 80% of critical episodes with both a complete displayed history and a recorded primary response. The final technical timing threshold must be supported by device testing, not chosen from effect size. Preserve a broad available-case sensitivity analysis including partial completers.

Never exclude people for unusual confidence, negative confidence–accuracy relations, low estimated B/R slopes, fast responses without a verified technical criterion, disagreement with the hypothesis, or failed outcome-dependent pattern checks. Do not remove stimulus families because their effects differ from the average.

Report missingness by assigned condition, mode, episode position, and completion status. The primary mixed model uses observed responses under its missing-at-random assumption; it is not a guarantee against informative dropout. Predefine inverse-probability weighting using pretreatment and prior technical predictors, and a sensitivity analysis shifting missing confidence by up to ±10 points across conditions. If plausible missingness changes the decision, classify the result as unresolved. Do not silently impute errors, confidence, or participant correction.

## 10 Participant generated extension

The primary study establishes only monitoring of assigned external feedback. A self-error claim requires a separate registered experiment in which participants make their own prediction or action before veridical feedback. Merely calling an assigned instrument record “your errors” is inadequate and potentially deceptive.

A candidate second-stage option is a participant-generated error pool. Participants first complete a discrete prediction or motor-estimation task with veridical outcomes; record each response and its actual signed error. Before any target confidence outcome, a deterministic matching procedure searches permutations of an eligible set of those errors for equal half-decay m and Q and equal recent errors but unequal B. Randomize the replay order of the participant’s own error records, then test a held-out probe. State clearly that the replay order is experimenter-assigned rather than the original chronology.

That design tests memory for one’s own previously generated mistakes under randomized review order. It does not establish that an experimentally assigned sequence was the natural online sequence of the participant’s mistakes. A live online design may manipulate task difficulty or targets prospectively, but exact realized error matching cannot be promised; use truthful feedback and register the intended-treatment analysis and any approximate matching tolerances before outcomes.

Pilot the yield of usable within-person exact matches. Eligibility based on the error pool must be assessed before target-condition assignment, with all rejected pools counted. Do not change feedback, fabricate errors, or keep only people whose target confidence follows the prediction. A yoked external-record comparison can examine ownership while matching visual exposure, but task knowledge and agency still differ. Power and register this extension separately; a null external-instrument result cannot be silently replaced by a positive selected self-error subgroup.

## 11 Ethics data and reporting

Obtain the appropriate institutional or independent ethics review before any pilot or recruitment. The responsible investigator, institution, recruitment platform, jurisdiction, compensation, total duration, risk assessment, withdrawal process, and retention period are unresolved administrative inputs. This protocol is not ethics approval. Use adults, nonclinical tasks, minimal-risk content, accessible instructions, breaks, and a clear right to stop without penalty to earned base compensation.

Prefer a truthful constructed-instrument task. If any later design requires deception about feedback or ownership, obtain explicit ethics approval for that specific procedure, justify necessity, arrange debriefing, and honor the approved withdrawal provisions. Do not infer clinical traits or make claims about an individual’s self-awareness from task responses.

Separate consent and payment identifiers from pseudonymous trial data. Limit collection to task responses, assignment, device/timing checks, and necessary eligibility variables. Restrict access, encrypt storage, document the linkage-key custodian and deletion date, and use an approved data-processing agreement with any recruitment or hosting service. Do not publish direct identifiers, free-text strategy responses without review, or exact metadata that could enable re-identification.

The trial-level schema must include pseudonymous participant ID, session and episode IDs, pair and family IDs, original or diagnostic bank version, assigned variant and sign, probe mode, full presented error sequence, common m and Q, B and R, candidate correction, chosen correction when applicable, confidence, probe tolerance, outcome, assignment probability, stimulus and response timestamps, technical flags, and exclusion reason. Keep model predictions and derived variables in a separately versioned analysis table. Retain immutable raw records and a reproducible transformation log.

Register the final protocol, frozen hypotheses, participant instructions, bank and family manifest, allocation seeds, model code and parameters, simulation output, exclusions, and decision rules before the first confirmatory participant. Registration, recruitment, external submission, and publication require the investigator’s separate action or authorization; preparation of this protocol does not perform them.

Release de-identified data only to the extent consent and ethics approval allow. Publish code, synthetic examples, aggregate results, and a deviation log regardless of outcome. Report a complete participant flow, all co-primary estimates, interval endpoints, failed controls, competing model results, missingness sensitivity, and stimulus-family limitations. Keep the source observational finding separate from the new prospective result.

## 12 Checklist required before registration

- Approve the task meaning and scope: external instrument first, identical fixed-probe confidence and separate free correction, with self-generated errors reserved for a separate study.

- Approve or revise the proposed three-point confidence threshold and 0.10-unit correction margin before viewing confirmatory outcomes.

- Run the exact bank audit, define the construction-family manifest, verify new nonzero-tail and disagreement stimuli, and lock the equal-pair estimand.

- Complete approved usability and calibration pilots; check comprehension, display accuracy, positive controls, confidence range, fatigue, and personal-data minimization.

- Freeze every competing-model specification, fitted parameter, decay-selection rule, input feature, and stimulus prediction; document models that cannot be distinguished.

- Complete the coverage and joint-power simulation, set analyzable N, maximum recruitment attempts, calendar stop date, and fixed missing-data and exclusion thresholds.

- Lock analysis code on simulated null, predicted, reversal, differential-missingness, and mirror-cancellation cases; verify that the rules return the intended decisions.

- Obtain ethics approval, finalize consent and compensation, register the dated protocol, and only then begin confirmatory recruitment.

## Sources and provenance

The source repository was inspected at commit 1a407e130b4f6375435e3a518c1a367232970ce4. Stable source URLs below distinguish the current protocol proposals from the existing exploratory findings and exact construction.

[1] Wright, M. C. 2026. Do Opposing Errors Predict Human Confidence. Exploratory secondary analysis, 6 November 2026.

https://github.com/enuminous/papers/blob/1a407e130b4f6375435e3a518c1a367232970ce4/Do-Opposing-Errors-Predict-Human-Confidence-2026-11-06.md

[2] Exact stimulus bank. Git blob 8a080549d6ef6cdce5813dc49ddda134bd6ffa49.

https://github.com/enuminous/papers/blob/1a407e130b4f6375435e3a518c1a367232970ce4/research/metacognition-matched-histories/pairs.csv

[3] Exact generator. Git blob 1bd63150af5592e2474e48324750e9f58ca193cd.

https://github.com/enuminous/papers/blob/1a407e130b4f6375435e3a518c1a367232970ce4/research/metacognition-matched-histories/matched.py

[4] Original exploratory analysis decisions. Git blob 1f99b9412e7ce720583f692db526afaf41d45484.

https://github.com/enuminous/papers/blob/1a407e130b4f6375435e3a518c1a367232970ce4/research/metacognition-matched-histories/design.md

[5] Source reproduction instructions and data provenance.

https://github.com/enuminous/papers/blob/1a407e130b4f6375435e3a518c1a367232970ce4/research/metacognition-matched-histories/README.md

[6] Loosen, Seow and Hauser source study, cited by the reanalysis. The prospective effect and power assumptions above are not drawn from this study.

https://doi.org/10.3758/s13428-024-02427-y
