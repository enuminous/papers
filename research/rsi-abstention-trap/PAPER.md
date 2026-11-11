# The Abstention Trap
## How an AI Can Pass a Recursive Self-Improvement Benchmark Without Demonstrating Useful Intelligence

**Matthew Chenoweth Wright · Monolithic LLC**  
**AI-assisted research analysis · November 11, 2026**

**Status:** Retrospective source inspection and derived control calculation. This is **not** a new confirmatory run, independent replication, validation of EFMW physics, or evidence of AGI. The historical `RSI-SYNTH-001` records remain unchanged.

---

## Abstract

Evidence-bounded AI systems should avoid unsupported assertions. Yet an evaluation that rewards abstention without requiring useful answers may mistake refusal for improvement. We re-examine the public 384-case synthetic holdout of `RSI-SYNTH-001`, a bounded policy-search prototype in [enuminous/RSI](https://github.com/enuminous/RSI). Its archived report records 159 correct labels for a deliberately weak initial policy, 349 for same-proposal-budget random search, and 384 for the recursive candidate. A conventional oracle-aware rule also scores 384.

Inspection of the public cases and policies shows that **340 of 384 cases (88.54%) have the gold label `UNRESOLVED`**. An always-`UNRESOLVED` control therefore gets 340 right, makes zero false assertions, produces zero useful answers, and would satisfy the historical acceptance gate when compared with the weak initial policy. Importantly, the recursive candidate does *more* than this trivial control: it correctly asserts all 44 answerable cases and abstains on all 340 unanswerable ones. The flaw is in what the gate requires, not in this candidate's recorded synthetic answers.

We present the exact class counts, a reproducible source-pinned analysis program, and a proposed successor protocol requiring answerable recall, false-assertion control, coverage-aware comparison against strong ordinary rules, multiple search seeds, and outside custody of sealed evaluation data. No general recursive self-improvement or EFMW-specific cognitive mechanism is established.

**Keywords:** selective prediction, abstention, evidence-bounded reasoning, recursive self-improvement, hallucination evaluation, coverage, benchmark design, negative controls.

## 1. The question behind the headline

An AI that refuses to guess can be safer than an AI that invents certainty. But if a benchmark rewards correct abstention as heavily as correct substantive answers, the easiest route to a good score may be never to answer.

That problem became explicit in a human-relayed adversarial interview between Matthew Chenoweth Wright, a ChatGPT collaborator called Millie, and Claude, an Anthropic AI system. Claude questioned an apparent improvement from 159 correct labels to 384 and asked how many cases could be solved by always saying `UNRESOLVED`. The dialogue motivated this audit; the dialogue itself is not independent experimental evidence. See [*My Dinner With Claude*](../../My-Dinner-With-Claude-2026-11-11.md).

The practical research question is narrow:

> Does the published synthetic PASS gate distinguish a policy that recognizes both supported answers and justified uncertainty from one that indiscriminately abstains?

For this archived experiment, the answer is **no**.

## 2. Dataset and original procedure

The [frozen demonstration protocol](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/docs/protocol.md) defines a synthetic label oracle. Each case has support and contradiction counts, a provenance-verification flag, and a bridge-verification flag. The correct label is `SUPPORTED` or `CONTRADICTED` only when relevant evidence is unopposed and both verifications are present. Otherwise the answer is `UNRESOLVED`.

The search space comprises 108 parameter combinations, varying evidence thresholds, verification requirements, and conflict handling. A one-gene hill climber gets 64 development proposals; a random-policy search gets 64 proposals. The development and holdout each contain 384 generated cases with different public seeds. The original candidate's policy does not update ChatGPT model weights, conduct autonomous open-ended research, or modify the evaluation rules.

The original gate declares PASS when all of the following hold:

1. Holdout accuracy improves by at least **0.05** over a deliberately weak initial policy.
2. Wrong assertive decisions, measured over all cases, do **not increase**.
3. The lower bound of a predeclared paired bootstrap interval for accuracy gain is **greater than zero**.

It does *not* require any minimum number of correct non-abstaining answers. An explicit ordinary oracle-aware rule policy serves as a ceiling comparator, and the original repository already acknowledges its synthetic and nonblind limitations.

## 3. Source-pinned reanalysis

We inspected the public [holdout cases and policy files](https://github.com/enuminous/RSI/tree/478908589847ab10038a80fd50df35478c0ec95f/examples/frozen_demo) at commit `478908589847ab10038a80fd50df35478c0ec95f` and reconstructed their decisions. The following is a retrospective calculation, not a newly registered experiment.

| Policy | Correct / 384 | False assertions / 384 | Assertive outputs / 384 | Correct answerable / 44 |
|---|---:|---:|---:|---:|
| Initial policy | 159 | 205 | 229 | 24 |
| Conservative conventional rule | 330 | 34 | 58 | 24 |
| Always `UNRESOLVED` (derived counterfactual) | **340** | **0** | **0** | **0** |
| Random search (64 proposals) | 349 | 35 | 79 | 44 |
| Recursive proposer (64 proposals) | **384** | **0** | **44** | **44** |
| Conventional oracle-aware rule | **384** | **0** | **44** | **44** |

The gold distribution is **15 SUPPORTED, 29 CONTRADICTED, 340 UNRESOLVED**. Thus:

- Always abstaining gives **340/384 = 88.54%** overall accuracy but **0%** answerable recall.
- The random-search policy yields **349/384 = 90.89%** accuracy. It identifies all 44 answerable cases, but additionally makes 35 wrong assertions.
- The recursive candidate yields **384/384 = 100%** accuracy and 44 correct assertions.
- The conventional oracle-aware rule also yields 384/384.

The original initial policy correctly answers 24 of 44 answerable cases, makes 205 wrong assertions, and correctly abstains on 135 of the 340 unanswerable cases. Replacing every prediction with `UNRESOLVED` gains 205 cases where it eliminates a bad assertion, loses 24 cases where it discards a correct answer, and ties on 155 cases:

```text
constant-abstain correct = 340
initial correct          = 159
net gain                 = (205 - 24) / 384
                         = 181 / 384 = 47.1354 percentage points
```

The historical gate requires only a five-percentage-point accuracy gain. The constant abstainer provides a much larger gain and reduces wrong assertions to zero. Its paired bootstrap accuracy-gain interval also has a positive lower bound under the archived comparison method. The associated [`analysis.py`](analysis.py) performs the source-based calculation with the original bootstrap convention. This demonstrates a **gate design vulnerability**; it does not imply that the published hill-climber itself selected or could necessarily represent an always-abstain policy.

### The result worth preserving

The recursive candidate is *not* simply refusing to answer. It solved all 44 answerable cases without adding unsupported claims. This is a genuine property of the archived **synthetic** run.

But the known ordinary oracle-aware rule achieves the same outcome. Consequently, the result shows successful recovery of an artificial decision rule, not a demonstrated distinctive benefit of recursion over conventional methods.

## 4. An evaluation must measure usefulness and restraint separately

Let `N` be all cases, `A` the number of answerable cases, `TP` the number of correctly asserted supported/contradicted labels, `FA` the number of wrong assertions, and `CA` the number of correct abstentions.

Define:

```text
overall accuracy          = (TP + CA) / N
assertive coverage        = (TP + FA) / N
answerable recall         = TP / A
false-assertion rate      = FA / N
wrong-share of assertions = FA / (TP + FA), when TP + FA > 0
```

A constant abstainer has `TP = 0`, `FA = 0`, `CA = N - A`. Its accuracy is `(N - A)/N`. The more unanswerable cases a test contains, the more impressive that accuracy can look—without any improvement in answering ability.

For evidence-bounded systems, refusing unsupported questions is an essential competency. But refusing answerable questions is a loss of usefulness. Both must be evaluated.

A calibrated system should not be punished for accurate abstention; it should be required to distinguish when abstention is warranted. Raw accuracy alone is not enough. Neither is an all-case false-assertion rate alone, because a policy that never asserts necessarily scores zero on that measure.

## 5. A proposed replacement gate: RSI-EVAL-002

We provide a prospective [coverage-aware gate proposal](PROPOSED-GATE.md). It has **not** been approved, frozen or run.

A serious successor test should contain:

1. **An explicit usefulness requirement.** Predeclare minimum answerable recall and meaningful assertive coverage, plus separate performance on unanswerable cases.
2. **An explicit safety requirement.** Limit false assertions, and publish their rate among actual assertions as well as among all cases.
3. **Strong controls.** Always abstain, coverage-matched transparent rules, matched-budget random search, conventional nonrecursive optimization, and the strongest plausible ordinary evidence-checking method.
4. **Multiple independent trials.** Report search-seed distributions, unseen evidence families, negative controls and resource costs; do not promote a favorable single seed.
5. **Outside custody.** Have a named consenting independent custodian maintain sealed tasks and labels beyond the optimizing team's access. Freeze the protocol-only commit and transmit its digest externally *before* evaluation.

The proposal sketches thresholds including 90% answerable recall, 10% assertive coverage, a 5% all-case false-assertion limit, and a minimum five-percentage-point advantage over a strong conventional baseline at matched coverage. **These numbers are proposals, not adopted acceptance criteria; they require power, prevalence and cost analysis before freezing.**

On this particular toy task, the conventional oracle-aware rule already reaches 100%, so no candidate can show a positive margin over it. That is a legitimate ceiling. A new claim of incremental recursive advantage must be tested on different, independently curated tasks rather than excluding the inconvenient comparator.

## 6. Preserve the historical PASS and correct the interpretation

The original `RSI-SYNTH-001` `report.json` records `PASS`, and it should remain unaltered. It met the rules defined for that historical synthetic demonstration. Retroactively changing the archived verdict would conflate an original benchmark decision with a later, stricter question.

The scientifically appropriate claims ledger distinguishes:

| Claim | Status |
|---|---|
| RSI-SYNTH-001 met its original three-part synthetic gate | HISTORICAL PASS |
| A constant-abstain strategy would score 340/384 and satisfy that gate | RETROSPECTIVE DERIVATION |
| The optimized policy correctly asserts all 44 answerable labels | RECONSTRUCTED SYNTHETIC RESULT |
| The recursive policy outperforms a strong rule-based oracle | NOT SHOWN (it ties) |
| Recursion delivers general improvement across independent tasks | UNRESOLVED |
| A model autonomously improves its underlying weights or is AGI | NOT ESTABLISHED |
| RSI-EVAL-002 confirms useful recursive advantage | NOT RUN |

The existence of a weakness in a gate is not proof of bad faith. It is a reason to update the next protocol, preserve the old evidence and attempt a genuine independent test.

## 7. Limitations and prospective research

This audit uses a small, transparent artificial oracle, not independently labeled real-world questions. It does not estimate transfer to commercial audits, scientific discovery, human metacognition or physics. The always-abstain result is calculated from archived cases rather than produced by a separately executed historical search arm. The comparison of one recursive run with one random-search run does not establish population-level superiority over random search.

Nor do the proposed gates by themselves establish scientific validity; a good metric can still be exploited if the dataset, labels, custody or comparison class is inadequate. Future experiments must account for source-family dependence, asymmetric costs of wrong claims, prevalence changes, and limitations of blinded scoring.

The next honest experiment would use **independently curated and sealed evidence-grounded tasks**, test ordinary rule-based and nonrecursive alternatives at matched costs, and state prospectively what would count as a failure. Until that is complete, the broader RSI claim remains unresolved.

## Conclusion

The difference between good uncertainty and useless refusal is not philosophical decoration. It is measurable.

RSI-SYNTH-001 contains an optimized policy that identifies supported conclusions and abstains appropriately on its synthetic examples. But the experiment's own PASS rule could also be satisfied by a strategy that never answers. The historical success criterion was therefore insufficient to establish useful recursive improvement.

**A system should know when not to answer; a system that never answers has not thereby demonstrated intelligence.**

The next benchmark must reward the harder achievement: offering answers when the evidence supports them, withholding claims when it does not, and outperforming the best conventional way to do both.

---

## Reproducibility and provenance

**Source revision:** `enuminous/RSI@478908589847ab10038a80fd50df35478c0ec95f`  
**Original data:** [`examples/frozen_demo/holdout_cases.json`](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/examples/frozen_demo/holdout_cases.json) and [`report.json`](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/examples/frozen_demo/report.json)  
**Policies:** `baseline_policy.json`, `candidate_policy.json`, `null_policy.json`, `control_policies.json` in the same source directory  
**Logic:** [`rsi/core.py`](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/rsi/core.py) and [`rsi/experiment.py`](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/rsi/experiment.py)  
**Reanalysis code:** [`analysis.py`](analysis.py)  
**Proposed protocol:** [`PROPOSED-GATE.md`](PROPOSED-GATE.md)

Run from a local checkout containing this analysis file and a separately cloned version-pinned RSI repository:

```bash
git clone https://github.com/enuminous/RSI.git
cd RSI
git checkout 478908589847ab10038a80fd50df35478c0ec95f
cd ..
python research/rsi-abstention-trap/analysis.py --self-test
python research/rsi-abstention-trap/analysis.py --snapshot-dir RSI/examples/frozen_demo
```

The commands assume the `papers` and `RSI` checkouts share a parent directory; run the final two commands from the `papers` root and provide the correct sibling path (typically `../RSI/examples/frozen_demo`) if they do not. No files from the original RSI repository are modified by this script. A source-level reanalysis of the values was performed while preparing this paper; the posted Python script is supplied for independent replay, not represented as externally reviewed execution.

**Attribution and scope:** Matthew Chenoweth Wright / Monolithic LLC, with AI assistance; the human-relayed critique by Claude motivated the abstention-control question. This is a retrospective methodological analysis and protocol proposal, not confirmation of an EFMW physical law, cognitive mechanism or AGI.
