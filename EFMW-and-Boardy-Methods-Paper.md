# EFMW and Boardy
## An evidence-bounded workflow for advisory decisions

**Matthew Chenoweth Wright · Monolithic LLC**  
**Draft methods paper · November 23, 2026**

### Abstract

Advisory conversations often move from partial evidence to recommendations before anyone has made clear which facts are established, which remain disputed, and who may act on the result. We propose combining a Boardy-style advisory dialogue with an EFMW workflow in Devs 2.0. The advisor elicits the decision. A provenance-tagged draft ties material assertions to pinned evidence. An adversarial critic searches the same record for unsupported inferences and conflicts. A revision stage can change the recommendation in response. The existing Boardy+ simulator illustrates these stages with scripted cases. DEV2-001 specifies a paired benchmark for testing the combined workflow against direct answering. We distinguish that benchmark from a proposed mechanism ablation and describe a separate governance test for independent challenge and reversal. The confirmatory benchmark has yet to run.

### 1. From a conversation to a decision record

A useful advisor helps a person decide what to do with the information they have. Consider an advisor weighing an introduction between two people whose interests overlap. The proposal might be promising, the scope of permission might be unclear, and one participant might have supplied a private reason for declining. The system needs to preserve the distinction between a plausible opportunity, a documented permission, and the later outcome of a decision. It can recommend a follow-up while leaving authorization unresolved.

In this design, **Boardy** supplies the advisory setting and conversational role. **EFMW** supplies the workflow for grounding, challenging, and revising assertions. **Devs 2.0** supplies the simulator and the research environment. Boardy+ is the repository’s scripted interface. Boardy++ is the conversational role explored in the interactive session. Neither constitutes access to Boardy’s production systems or evidence of a live integration.

We use coherence in a bounded operational sense. The recommendation should remain consistent with the recorded evidence, the unresolved questions, and the authority available at the time. Evidence may remain genuinely conflicting. A coherent decision record preserves that conflict and shows what action, if any, the parties have authorized while it is reviewed. This paper makes no mathematical identification between that operational use and an EFMW physical quantity.

### 2. The proposed workflow

1. **Frame the decision.** Record the advisory question, the proposed action, the affected parties, and the decision owner. Identify which assertions would materially change the recommendation.
2. **Draft with provenance.** Tie each material assertion to a specific source and revision where possible. Label evidence status. Keep participant testimony identifiable as testimony. For closed-corpus evaluation, distinguish a fact absent from the record from a fact established to be false.
3. **Challenge the draft.** Give the critic the same evidence and the draft. Ask it to flag unsupported assertions, circular support, unresolved conflicts, and claims that exceed their cited source. Record precisely which passage or missing premise motivated each objection.
4. **Revise once.** Preserve the draft and critic output. Record materially changed assertions and the grounds for each change. A good revision can retain a correct answer, narrow an overclaim, or report an unresolved question. The critic can also be wrong.
5. **Review consequential decisions.** Record authorizing scope, any restrictions on evidence disclosure, the independent challenge route, and who can reverse the decision. The parties confer that authority. A generated critique is an input to review. The actual decision and any reversal have their own evidence and audit trail.

For audit use, the Monolithic Zoo supplies a compatible discipline: pin the target and environment, define each operation’s applicability and criterion, and record PASS, FAIL, UNRESOLVED, or NOT_APPLICABLE against each scoped obligation. The DEV2-001 critic is a specified prompt intervention. A Zoo audit can examine its artifacts, but the critic does not execute the full Zoo roster.

### 3. Worked example · Humanitarian access

Consider a fictional agreement allowing a convoy to cross a checkpoint during a specified window. One source records an order to clear the route. The aid coordinator reports that the convoy turned back. A direct draft might say the route was open because an order was issued. The critic identifies the missing premise: evidence of the order does not establish that it was implemented. A revised answer preserves both accounts and leaves passability unresolved.

A separate decision record identifies what the parties had already agreed may continue during a dispute and who can review the passability finding. A mutually accepted custodian could protect sensitive evidence while sharing the minimum information needed to challenge a finding. If a later record overturns the initial decision, the workflow should preserve the superseded finding and show whether the correction reached everyone who relied on it.

The example yields a testable question for a tabletop exercise: can participants correctly identify the commitment, the disputed fact, and the action still authorized? Introduce evidence that changes a finding and check whether participants acting from the record adopt the correction. This would evaluate a specific coordination task. Effects on real negotiations or humanitarian outcomes would require separate evidence.

### 4. What the current benchmark measures

DEV2-001 holds the retrieved passages and model settings fixed across five configurations. The draft uses the same available ceilings of 8,192 total tokens and 1,024 generated tokens per item. Actual consumption can differ across arms and must be reported.

| Arm | Workflow |
| --- | --- |
| A | Direct answer |
| B | Answer with eight provenance statuses |
| C | Provenance-tagged draft → adversarial criticism → revision |
| D | Conventional cite-or-abstain answer |
| E | Plain draft → generic feedback → revision |

The approved target mix is **120 answerable, 240 absent, and 120 contradictory**. The primary contrast is C versus A on the absent tier. Define the effect as the family-weighted false-assertion rate in A minus that in C. The approved minimum observed improvement is **20 percentage points**. The draft also specifies uncertainty, utility, and resource gates. The answerable and conflict checks guard against achieving a low false-assertion rate by refusing useful answers. Incomplete or malformed responses are tracked separately from valid abstentions.

The protocol plans paired analysis by evidence family and blind human ratings with adjudication. Evidence-family splits prevent paraphrases of the same claim from entering both development and evaluation. Holdout custody and runtime pins protect the interpretation of the comparison. A result favoring C over A would support the combined workflow on the recorded testbed. Comparisons against D and E matter for judging whether standard grounding or self-refinement can explain the gain. The contrast does not estimate a gain attributable to the Boardy role.

### 5. A mechanism ablation for a follow-on study

The simulator lets readers see what happens when stages are disabled. Because its transcripts are scripted, the differences demonstrate the design. A measured mechanism ablation would require a separate prospective amendment.

| Question | Proposed paired comparison | Attribution limit |
| --- | --- | --- |
| Does provenance labeling help? | Compare the full pipeline against a version using a plain draft with the same downstream instructions. Hold evidence access and citation requirements fixed. | A vs. B in the existing design probes labeling at the draft stage. The proposed pair probes its contribution inside the full workflow. |
| Does targeted criticism help? | Keep the provenance draft and revision stages. Compare targeted criticism with a predeclared generic-feedback control and report a critic-omission comparison separately. | Omitting a call also changes available information and compute. The generic-feedback comparison better isolates the content of the critique. |
| Does revision help after a critique? | Compare the retained draft and revised final answer from the same draft-and-critique pair. Blind raters to stage. | This estimates the effect of using revision after the critique. It includes the additional generation used to revise. |
| Does the advisory setting interact with the workflow? | Cross a fixed Boardy-style role and a neutral assistant role with the full workflow and a prespecified comparator. Match evidence and evaluate both error and advisory usefulness. | The effect applies to the tested role instructions. A production integration would require access and its own protocol. |

Define task families, budgets, hypotheses, and scoring rules before generation. Retain unnecessary abstentions, missed contradictions, and revisions that damage a correct draft. If the workflow cannot outperform a strong grounded baseline at comparable utility and cost, report that outcome. An advisory benefit on one task family also leaves transfer to other settings open.

### 6. Evidence status and contribution

At the inspected Devs 2.0 revision, the software replay passed 39 unit tests and produced 60 fixture responses across 12 development questions, with zero model calls and zero human ratings. The freeze check found zero of the 480 required held-out questions and reported missing runtime and custody pins. Those observations establish software behavior and the state of the benchmark package at that revision. The empirical performance claim remains unresolved.

The contribution of this design is a record that shows how a recommendation was produced and gives people a way to contest it. It lets a reviewer inspect whether evidence actually supports the recommendation, whether criticism changed the answer, and whether the person who challenged the decision had authority to reverse it. These are distinct obligations. Testing them separately makes it possible to learn where the combination helps and where it fails.

### Project references

- [Devs 2.0 research desktop and white paper](https://github.com/enuminous/Devs2.0/tree/3ddaf05c27954866c44ad9603aac09960b6d9d21)
- [Boardy+ simulator scope and fixtures](https://github.com/enuminous/Devs2.0/tree/3ddaf05c27954866c44ad9603aac09960b6d9d21/boardy-plus)
- [DEV2-001 draft protocol](https://github.com/enuminous/Devs2.0/blob/3ddaf05c27954866c44ad9603aac09960b6d9d21/research/dev2-001/PROTOCOL.md)
- [DEV2-001 scoring manual](https://github.com/enuminous/Devs2.0/blob/3ddaf05c27954866c44ad9603aac09960b6d9d21/research/dev2-001/SCORING.md)
- [Monolithic Zoo Audit](https://chatgpt.com/skills?skill_id=6b048cd641a88191835f66f0fc63d293)
