# Who gets to verify? A comparative study and ablation of TORTOISE and KAIROSEED

**Matthew Chenoweth Wright · Monolithic LLC · November 8, 2026**

## Abstract

TORTOISE evaluates predictive claims against criteria fixed before evaluation. Sangmuan Valte’s KAIROSEED separates a proposed agent action, authorization, execution, and verification. Both require the object under review to be separated from the evidence that earns a favorable verdict. The separation has different meanings. For TORTOISE, a candidate or its outcomes must not determine its own evaluation criteria. For KAIROSEED, an action must not be able to hide or rewrite the evidence needed to verify its effects. We compare the designs and exhaustively ablate six safeguards in a six-case synthetic model. The model illustrates four ways the gates can admit an unwarranted PASS. Two further ablations test authorization and causal attribution. The results concern the model only.

## 1. Sources and scope

TORTOISE’s public account specifies a frozen candidate, held-out prediction, scoring against matched conventional controls, ablation, and replication on fresh samples. Its central question is whether a candidate adds predictive information beyond the matched comparison. Here, independence of the obligations means that the candidate's own assertions and the inspected outcomes cannot supply the acceptance rule. The test can still be tailored to the claim's domain. [Wright, *The Yard Refused the Label*](https://enuminous.substack.com/p/the-yard-refused-the-label).

Valte publicly describes KAIROSEED as experimental governance for agent actions, with authorization, enforcement and verification as distinct stages. His public posts identify replay and stale state among the research targets. The project account supplied for this comparison additionally describes a frozen contract, ten falsification scenarios, and a PASS requiring valid authorization, complete mediation, no prohibited effects, independent verification, and evidence integrity. It describes a required observation gap as NOT VERIFIED and observer placement as open. Those details come from the supplied account. A public versioned contract and scenario matrix were unavailable for direct comparison, so no scenario-level fidelity or implementation result is claimed here. [Valte, public architecture description](https://community.openai.com/t/kairoseed-a-verification-first-governance-layer-for-ai-agents/1392570/2) · [Valte, research scope](https://community.openai.com/t/kairoseed-a-verification-first-governance-layer-for-ai-agents/1392570/8).

## 2. Where the designs agree

| Shared requirement | TORTOISE | KAIROSEED |
|---|---|---|
| Fix the terms before judgment | Freeze the candidate, comparison, score, and failure threshold before evaluating outcomes. | Fix the action contract, protected effects, and evidence obligations before exercising the boundary. |
| Separate the object from its evidence | Use held-out observations and a comparison the candidate cannot redefine after scoring. | Verify effects using observations whose coverage and integrity the action cannot defeat within the threat model. |
| Give contrary evidence a path to the verdict | Matched controls and ablations can remove apparent predictive gain. | Adversarial action scenarios can expose unauthorized effects or bypasses. |
| Withhold credit when an obligation is missing | An unfrozen or unevaluated candidate has insufficient support for the claimed gain. | A required observation gap leaves a particular execution NOT VERIFIED. |
| Keep assurance scoped to the evidence | Fresh replication tests whether an effect generalizes. | Repeated trials test the mechanism under new executions. The original action still needs its own evidence. |

The common rule is **a favorable verdict requires evidence that the evaluated object cannot arrange to look favorable by changing the basis of judgment**. This is a comparison of assurance structures. A matched predictor is a comparator for incremental performance. A mediation path is a control over authority. These mechanisms answer different questions.

## 3. Coverage and integrity are separate

Let a contract forbid any write to field `x`. Consider two histories starting at zero. The first does nothing. The second writes one and then restores zero. Both yield endpoint evidence `(0, 0)`. For an observation map `O` and verdict function `V`, equality `O(h₀) = O(h₁)` implies `V(O(h₀)) = V(O(h₁))`. If the verdict rule is randomized, the two histories instead induce the same verdict distribution for the same observed input. Endpoint evidence alone therefore cannot certify the compliant history while excluding the prohibited one. For a contract that only constrains the final value, the two histories may legitimately be equivalent. The result depends on what the contract protects.

An external observer with endpoint-only coverage has this blind spot even if its log is pristine. An internal observer may satisfy the obligation if its sensor, collection path, and record are protected against the action and cover every relevant effect within the declared threat model. Signing an endpoint record can authenticate it while preserving the blind spot. Likewise, a complete sensor with an editable record can lose the very event it was built to see.

Complete mediation concerns checking authority at each relevant access. Observation concerns which facts can support a verdict about execution. A separately justified enforcement invariant may rule out a forbidden transition when evidence binds that invariant to the execution in question. Merely repeating the action demonstrates a new history. It cannot recover an unrecorded event from the original. [Saltzer and Schroeder, *The Protection of Information in Computer Systems*](https://web.mit.edu/saltzer/www/publications/protection/index.html).

## 4. Executed ablation on a finite model

The test below is a constructed truth-table ablation. Each case is an intentionally isolated witness. Oracle facts describe the synthetic history independently of the verdict, including whether an unobserved prohibited write occurred. The verifier receives a favorable surface signal in every case, such as clean endpoints or an apparent score gain. It then checks the named obligations. An absent or untrusted obligation yields NOT VERIFIED. A demonstrated authorization violation yields FAIL. This simplified adjudicator does not model every way a real execution or experiment could fail.

| Removed safeguard | Synthetic witness | Full gate | Ablated gate |
|---|---|---|---|
| Pre-outcome freeze | Apparent gain depends on a threshold chosen after scoring | NOT VERIFIED | PASS |
| Held-out evidence | The apparent gain exists only on the fitting data | NOT VERIFIED | PASS |
| Observation coverage | A prohibited write is restored before the final snapshot | NOT VERIFIED | PASS |
| Evidence integrity | A prohibited write occurs and its event is removed from the log | NOT VERIFIED | PASS |
| Authorization | The recorded action took effect without authorization | FAIL | PASS |
| Attribution control | A candidate and conventional feature tie when the conventional feature is evaluated fairly | NOT VERIFIED | PASS |

The first two ablations test the claim side of the common rule. The next two test the action side. The final two locate the boundary of the analogy. Authorization is a condition on action. Attribution is a condition on what explains the measured gain. Neither substitutes for the other.

All six single ablations were crossed with all six witnesses. The full gate issued zero PASS verdicts on the six witnesses and passed the all-safeguards control. Exactly six of the 36 ablated witness evaluations issued PASS, one per removed safeguard. The other 30 retained the full-gate verdict. These counts follow from the construction, so they measure logical dependence in the model. They do not estimate a false-pass rate in either project. Each witness has one intentionally isolated gap. Real defects may interact, so an ablation may show no effect if another safeguard still blocks the same case.

### Reproduce with Python 3

```python
gates = ("freeze", "held_out", "coverage", "integrity", "authorization", "attribution")

def verdict(evidence, removed=None):
    active = tuple(gate for gate in gates if gate != removed)
    if "authorization" in active and evidence["authorization"] is False:
        return "FAIL"
    if any(evidence[gate] is not True for gate in active):
        return "NOT VERIFIED"
    return "PASS"

control = dict.fromkeys(gates, True)
witnesses = {
    gate: {**control, gate: False if gate == "authorization" else None}
    for gate in gates
}
assert verdict(control) == "PASS"
assert all(verdict(evidence) != "PASS" for evidence in witnesses.values())

passes = []
for removed in gates:
    for witness, evidence in witnesses.items():
        result = verdict(evidence, removed)
        if result == "PASS":
            passes.append((removed, witness))
        else:
            assert result == verdict(evidence)
assert passes == [(gate, gate) for gate in gates]
print(f"{len(passes)} unwarranted PASS verdicts in {len(gates)**2} ablated evaluations")
```

## 5. What would distinguish the designs empirically

For TORTOISE, freeze a candidate, matched comparator, effect threshold, split, and replication rule. Cross pre-outcome versus outcome-informed threshold selection with held-out versus reused data in a controlled benchmark containing null signals. Record the rate at which each condition endorses a null candidate. Run the component ablation and fresh replication separately so a test of incremental performance remains distinguishable from a test of generalization.

For KAIROSEED, freeze the protected state, permitted effects, adversary capabilities, and evidence rules. In an isolated fixture, cross endpoint-only versus transition-level observation with agent-writable versus independently protected evidence. Use an evaluator-controlled record as ground truth for permitted actions, write-and-restore, and deliberately missing evidence. A decisive failure is PASS on a prohibited or materially unobserved history. Record verified permitted actions, confirmed violations, and NOT VERIFIED separately so a verifier that refuses every case cannot pass the evaluation by abstention alone. This is a proposed experiment. It has not been run against KAIROSEED.

The shared insight is that freezing the rules and protecting the evidence solve different problems. A claim can sometimes be tested again on fresh data. An action verifier must preserve adequate evidence of the particular execution it certifies.
