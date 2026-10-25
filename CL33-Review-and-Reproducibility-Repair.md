# CL33 Under Review: Operator-Only Language Modeling and a Documented Reproducibility Repair

**Matthew Chenoweth Wright**  
Monolithic LLC  
25 October 2026 · Version 1.0  
**Article type:** Technical review and release-maintenance case study  
**Status:** Public research note; not journal peer review or an independent model-performance replication

## Abstract

This paper examines Garret Sutherland’s CL33 operator-only language-model project and a specific review–repair exchange on 25 October 2026. Wright’s first-pass inspection identified inconsistent release checksums, incorrect checkpoint paths, an incomplete public decoding-evaluation procedure, and a need to distinguish operator dependence from recurrent-memory dependence. Sutherland published a corrective release explicitly attributing the maintenance work to that review. We independently compare the two pinned releases using byte hashing, source inspection, checkpoint metadata, and evaluation-fixture inspection. The original manifest yields eight passing checks, two hash mismatches, and three missing paths. The revised manifest yields thirteen passing downloaded-file checks; its three checkpoint entries agree with published storage metadata, although checkpoint bytes were not downloaded. All six inspected model-definition files are unchanged, while evaluation scripts and documentation are revised and a held-out fixture is added. These observations establish a concrete improvement in the inspectability of the release. They do not reproduce CL33’s reported performance or demonstrate an EFMW integration benefit. The case illustrates how a bounded external review can produce a rapid, attributable correction while preserving the distinction between a computational record, a causal mechanism, and a correct answer.

**Keywords:** operator language models; geometric algebra; reproducibility; ablation; external review; provenance; Monolithic

## 1. What Sutherland is building

Sutherland’s *One Object: Memory, Navigation, and Reportability in an Operator-Only Language Model* investigates an architecture that exposes an operator representation between a learned emitter and its output machinery. A transformer processes tokens and emits geometric operators; the model then constructs state evolution and readout features from those operators. The research question is whether a compulsory intermediate representation can support useful inspection, reconstruction, and intervention. The public release contains prose and chat model checkpoints and a decoding probe. Its experimental motivation deserves evaluation on those terms, separately from the quality of an individual dashboard answer. [1, 2]

The released algebra implementation uses six-dimensional matrix actions associated with signature (3,3). Its fifteen generator coefficients define a matrix exponential. In the notation used here,

$$
\eta=\operatorname{diag}(-1,-1,-1,+1,+1,+1),\qquad
\Omega_t^T\eta+\eta\Omega_t=0,
$$

$$
R_t=\exp(\Omega_t),\qquad s_t=R_t s_{t-1}.
$$

Since the generators preserve the indefinite metric, exact arithmetic gives

$$
R_t^T\eta R_t=\eta,\qquad R_t^{-1}=\eta R_t^T\eta.
$$

This is standard matrix-group structure, not a new physical law. The code supplies a particular learned use of it. Algebraic invertibility also does not imply exact bitwise reversal of arbitrary floating-point computations: numerical accuracy requires its own measurement. [3]

Three questions must remain separate:

1. **Record:** What information can be recovered from emitted operators?
2. **Mechanism:** Which state or feature actually changes the output under a controlled intervention?
3. **Answer quality:** Is the generated response relevant, coherent, and factually correct?

A model may preserve a computational record of a mistaken response. Recovering a token from that record measures recoverability, not the truth of the token’s surrounding assertion. Conversely, an unconvincing conversational example does not, by itself, refute an architectural bottleneck. This separation is the central interpretive discipline of the review.

## 2. Scope, provenance, and chronology

The first inspection targeted the public Hugging Face release, not every result in Sutherland’s research program. The two source objects are:

| Role | Immutable Hugging Face revision |
|---|---|
| Release inspected in the first pass | `0f7d63c4551a15a9bb5b2f35c8d4fe6b111dc2bf` |
| Corrective release | `b081c1c8888a857d5dfdd1ec4f1d94b497834473` |

The original review was sent at **13:51:22 PDT on 25 October 2026**, according to Wright’s sent-message record. The public corrective commit is timestamped **15:33:09 PDT** the same day. The interval is **1 hour, 41 minutes, 47 seconds**. That measures the interval between the recorded review transmission and commit publication; it does not establish how much work time the repair required. The public commit message and revised model card explicitly attribute the maintenance pass to M. Wright’s review. [2, 4]

The review was assisted by AI-based source inspection. It did not execute CL33’s model code or deserialize checkpoints. For this paper, a new verifier re-fetches both immutable revisions, checks small-file bytes, parses the reproduction scripts, inspects the added numerical fixture, and records its observations in a machine-readable companion. It does not import upstream model code, load model or probe weights, or run inference. [5]

This article summarizes Wright’s own review and the public corrective record. Private correspondence is not reproduced. Sutherland is the researcher whose work is examined, not a coauthor of this article; publication does not imply his endorsement.

The relevant scope is a release-level technical review. We do not retrospectively assign a Zoo-wide score or claim that every named Zoo operation was executed.

## 3. What the first pass found

The first review made four practical observations and one scientific distinction.

**Release integrity.** A checksum list should match the bytes and paths a reader can obtain. In the inspected revision, two listed small files did not match their advertised hashes, while three checkpoint entries named a directory absent from the published tree. Eight other listed small-file checks passed. This was evidence of an inconsistent release manifest, not evidence of model falsification or misconduct.

**Evaluation access.** The original reverse-readout script could load a saved evaluation card and decode a user-supplied text. Printing a saved result is different from recomputing it on its evaluation data. The public bundle lacked the held-out fixture and scoring path needed to replay that part of the claim.

**Checkpoint loading.** Static inspection found three `torch.load` calls across the two reproduction scripts, each explicitly setting `weights_only=False`. This made the loading choice a concrete maintenance issue. A restriction on deserialization is useful, but does not amount to a comprehensive security audit.

**Version and claim boundaries.** Readers needed an explicit mapping from the bundle’s historical preprint version to the claims in the later paper. Possession of model weights alone does not make every experiment in a paper reproducible: evaluation harnesses, data splits, controls, and configurations also matter.

**Causal attribution.** The state-operator features participate both in recurrent state evolution and in direct readout features. Disabling both routes in one intervention cannot isolate the recurrent route’s contribution.

The companion verifier reproduces the byte-level findings today. The historical review’s scope and the present checks are therefore independently distinguishable: the former records what was communicated; the latter records what was computed for this publication. [3–6]

## 4. The repair and what we verified

The release comparison identifies five changed existing files—`README.md`, `REPRODUCE.md`, `SHA256SUMS`, and the two reproduction scripts—and one added fixture, `eval_slice_invert_heldout.npz`. No existing file is removed. [5]

| Review item | Observable change | Verification in this paper |
|---|---|---|
| Two incorrect small-file hashes | Manifest entries now match the published bytes | Both repaired entries pass |
| Three incorrect checkpoint paths | Entries now use the published root-level paths | Paths exist; manifest hashes match storage metadata |
| Incomplete manifest coverage | Documentation, license, and the new fixture are covered | Thirteen downloaded manifest-listed files pass |
| Unrestricted checkpoint loading | All three calls now explicitly set `weights_only=True` | Confirmed through Python syntax-tree inspection |
| Missing public held-out scoring path | New fixture and `--heldout` mode | Fixture structure and evaluation source inspected |
| Ambiguous claim coverage | Expanded version and claim mapping | Documentation change inspected |
| Concern that the model itself might have changed | Model definitions and checkpoint references remain stable | Six source files byte-identical; three checkpoint storage identifiers unchanged |

The three checkpoint objects total roughly two gigabytes. Their underlying bytes were neither downloaded nor hashed in this review. Equal published content identifiers are evidence of unchanged referenced objects, not a replacement for verifying downloaded bytes.

The updated manifest lists sixteen release files: thirteen checked locally and three checkpoints assessed only through metadata. It does not hash itself or repository transport metadata. This is the precise scope of our integrity result.

The added fixture was opened using NumPy with `allow_pickle=False`. It contains an `ids` array of shape **108 × 1024**, a source-ID array of length 108, and six source labels. Each source contributes eighteen rows, giving **110,592 token positions**. This confirms the file’s structure and source balance; it does not independently establish the claimed separation from the probe’s training data. That would require access to the relevant training manifests or an equivalent overlap audit. [5]

The revised script contains actual batched scoring logic: it emits operator features, runs the probe, compares predictions with token IDs, and computes aggregate and per-source statistics. We inspected that procedure without executing the model. Its console output compares recomputed values with the stored card; the script does not convert a disagreement into a failing exit status. A future automated regression job should add an explicit numerical acceptance gate. [6]

The repair is therefore substantive and bounded. It improves a reader’s ability to check the work while leaving the learned models in place.

## 5. Why operator dependence does not identify memory dependence

The distinction can be expressed with a schematic model:

$$
O_t=E(x_{\leq t}),\qquad
S_t=F(O_{\leq t}),\qquad
Y_t=G(O_{\leq t},S_t).
$$

Here, \(E\) is a contextual emitter, \(O\) its operator record, \(S\) a transported state, and \(G\) the readout. These equations are an explanatory abstraction, not a replacement specification of CL33.

An intervention that destroys operator features can affect both inputs to \(G\). A large change in loss then establishes sensitivity to that joint intervention. It does not determine how much sensitivity came from the state route.

A counterexample makes the logic exact. Suppose \(S_t=F(O_{\leq t})\) is computed but the output is \(Y_t=G_0(O_{\leq t})\), independent of \(S_t\). Destroying \(O\) can still ruin predictions completely. The output collapse therefore cannot establish that \(S\) carried indispensable memory. This is a general causal-identification point, requiring no assumption about EFMW.

In the shipped bottleneck script, the tested operation specifically zeros `Bs`, the state-operator coefficients, before assembly; the query and key operator tensors are retained. Thus even the phrase “operators off” is shorthand for a particular intervention. The exact code and the readout connections matter more than the label. [7]

The direct source also prevents a mistaken attribution of novelty to this review. The **original inspected** `model_v2.py` already contained a September 10 note explaining that the grade-tower readout provides a direct operator route, that scan pinning has a modest effect, and that shuffling the state has approximately none. It already attributed corroborating evaluation to N. Watson. Those source bytes did not change in October’s repair. Wright’s review emphasized the distinction and its relevance to the public bundle; it did not originate the earlier negative result. [3, 5]

That historical boundary matters. A fair account credits Sutherland and the earlier evaluator for the reported investigation, and credits the present exchange for the documented release corrections.

## 6. Reported performance and remaining proof obligations

The following numbers are **publisher-reported**, not measurements made for this article. On the supplied bottleneck fixture, the revised card reports native perplexity 68.6 and ablated perplexity 18,552.6, approximately a 270-fold ratio. It reports 0.8436 top-1 reconstruction accuracy on the six public sources; the approximately 0.860 aggregate includes forty-five undistributed chat rows. Scan pinning is reported at 1.19–1.22 times native perplexity, with time-shuffling and removal of the relevant attention contribution approximately 1.00. [2]

These quantities answer different questions. Perplexity measures predictive loss on a specified evaluation. Token reconstruction measures a probe’s recovery of token identity. Neither directly measures the truth of generated claims.

| Claim or obligation | Evidence status in this review | What would strengthen it |
|---|---|---|
| The identified release faults were repaired | **Demonstrated**, within the checked byte and source scope | Full checkpoint-byte verification would extend the integrity result |
| Public held-out evaluation is now supplied | **Demonstrated** for fixture and scoring-code availability | Execute scoring and retain complete logs |
| Numerical CL33 performance is reproduced by this review | **Unresolved / not performed** | Run pinned checkpoints, fixtures, software, and explicit tolerances |
| Public fixture is disjoint from probe training | **Supported but incomplete** through the publisher’s account | Training-split provenance and overlap checks |
| Recurrent state is indispensable in these LM checkpoints | **Not supported by the cited controls** | A controlled positive result preserving competing information routes |
| Internal record guarantees factual answers | **Rejected as an inference** | Separate task-grounded correctness evaluation |
| Adding EFMW improves CL33 | **Hypothesis**, not an outcome of this review | A specified integration and matched comparison on actual checkpoints |

A large ablation ratio supports dependence on the tested features. The stronger assertion that every behaviorally relevant influence is transparently explained also needs architectural scrutiny and task-specific causal tests. The upstream transformer still computes the operators; an accessible intermediate record does not automatically explain every computation that produced it.

## 7. Dashboard feedback and the EFMW simulation

After the maintenance response, Wright reported that some dashboard outputs were confusing and shared an exploratory CL33–EFMW simulation concept. That exchange motivates further investigation; it supplies no additional measured result in this article.

No recoverable simulation implementation, run record, or checkpoint-linked evaluation accompanies this publication. We therefore report no simulated performance gain and make no claim that EFMW corrected the released model. A conceptual demonstration may help specify an intervention, but cannot establish its effect on CL33’s learned parameters.

The dashboard concern suggests a practical interface distinction: separately label generated text, recovered token traces, numerical operator checks, and externally checked facts. Each display should state what its indicator measures. A reversible transformation is meaningful engineering information, but visitors should not have to infer whether it also certifies an answer.

A prospective integration study should freeze the actual checkpoint, intervention code, questions, resource budgets, and scoring rules before testing. It should compare unchanged CL33, the proposed EFMW intervention, and a conventional intervention with comparable computation and information access. A generic error checker cannot be credited as a distinct EFMW contribution without specifying the additional mechanism.

This is a proposed design, not a preregistered experiment. A future protocol should define success as an improvement on a prespecified primary task measure against the strongest matched comparator, with uncertainty and cost reported. It must allow a null result. A withheld test set, independent scoring, and full run logs would make that comparison reviewable.

## 8. What this case establishes

This case establishes an attributable maintenance outcome: a reviewer identified concrete obstacles to verification; the researcher published changes addressing them; a subsequent static check confirmed the relevant byte, path, and source-level repairs.

There are two different forms of progress. Scientific progress may change what is known about a model’s behavior. Release-maintenance progress changes how readily another person can inspect and test that knowledge. The October 25 patch demonstrably accomplished the second. No retraining or improvement in conversational capability is needed for that contribution to matter.

The case is also narrower than a validation of an entire audit business or theoretical framework. A single successful review does not establish that a branded method outperforms conventional review. It does show a concrete kind of useful work: locating a reproducibility failure precisely enough that its author can repair it and a later reader can verify the repair.

Sutherland’s contribution is the architecture, research program, released artifacts, and corrective implementation. Wright’s contribution here is the bounded external critique and this documented follow-up. The useful result is their traceable connection.

## Reproducibility companion

The repository includes:

- [Verifier and instructions](https://github.com/enuminous/papers/blob/main/research/cl33-review-2026-10-25/README.md).
- [Static verifier](https://github.com/enuminous/papers/blob/main/research/cl33-review-2026-10-25/verify_release.py).
- [Machine-readable observations](https://github.com/enuminous/papers/blob/main/research/cl33-review-2026-10-25/verification.json).
- [Public revision chronology](https://github.com/enuminous/papers/blob/main/research/cl33-review-2026-10-25/provenance.json).

These files preserve the distinction between downloaded-byte checks, storage metadata, source interpretation, publisher-reported performance, and unperformed experiments.

## References

1. Garret Sutherland. *One Object: Memory, Navigation, and Reportability in an Operator-Only Language Model*. Preprint, version 1.3 as identified by the release documentation. [Project paper](https://t3atlas.dev/cl33/paper/); [DOI: 10.5281/zenodo.22684392](https://doi.org/10.5281/zenodo.22684392). Accessed 25 October 2026.
2. MirrorEthic. [Revised model card at the corrective revision](https://huggingface.co/mirrorethic/cl33-oplm/blob/b081c1c8888a857d5dfdd1ec4f1d94b497834473/README.md). Publisher-reported performance is attributed to this source.
3. MirrorEthic. [Original inspected model source](https://huggingface.co/mirrorethic/cl33-oplm/blob/0f7d63c4551a15a9bb5b2f35c8d4fe6b111dc2bf/model_v2.py) and [matrix-generator implementation](https://huggingface.co/mirrorethic/cl33-oplm/blob/0f7d63c4551a15a9bb5b2f35c8d4fe6b111dc2bf/so33.py). The earlier negative-result note predates Wright’s review.
4. MirrorEthic. [Corrective commit b081c1c](https://huggingface.co/mirrorethic/cl33-oplm/commit/b081c1c8888a857d5dfdd1ec4f1d94b497834473); [public commit-history API](https://huggingface.co/api/models/mirrorethic/cl33-oplm/commits/main). Retrieved chronology is preserved in the companion.
5. Wright, M. C. [Verification record](https://github.com/enuminous/papers/blob/main/research/cl33-review-2026-10-25/verification.json), generated for this article, 25 October 2026. Methods: [verify_release.py](https://github.com/enuminous/papers/blob/main/research/cl33-review-2026-10-25/verify_release.py).
6. MirrorEthic. Reverse-readout script: [before repair](https://huggingface.co/mirrorethic/cl33-oplm/blob/0f7d63c4551a15a9bb5b2f35c8d4fe6b111dc2bf/repro_reverse_readout.py), [after repair](https://huggingface.co/mirrorethic/cl33-oplm/blob/b081c1c8888a857d5dfdd1ec4f1d94b497834473/repro_reverse_readout.py).
7. MirrorEthic. [Bottleneck reproduction script](https://huggingface.co/mirrorethic/cl33-oplm/blob/b081c1c8888a857d5dfdd1ec4f1d94b497834473/repro_bottleneck.py).

## Disclosure

Wright leads Monolithic LLC and develops the EFMW/Zoo research program, giving him a professional interest in useful external review. AI assistance supported source comparison, verifier construction, and manuscript preparation. This article reports static release verification and reasoned analysis, not new trained-model experiments, full security certification, a completed Zoo-wide audit, or validation of EFMW physics. All original CL33 authorship and implementation credit remains with Sutherland and the relevant contributors.

