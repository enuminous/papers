# Evidence, authority and traceability protocol

**Status:** proposed mechanism; no physical hardware approved.

1. Every requirement (R) references a subsystem, acceptance test, evidence link, reviewer and exact configuration digest.
2. Every hazard (H) has an owner, control/mitigation, independent review, closure test, and blocking status. Hazard status defaults to `UNRESOLVED`.
3. Every assembly step (A) references a dependency DAG, evidence IDs, approved version lock and explicit human review. Physical stages additionally require independently closed critical hazards and a real engineering signoff.
4. Every test (V) includes code hash, model hash, seed/scene, raw log, reproducible method, adverse cases, result and reviewer. Distinguish executed from proposed.
5. Every experimental research hypothesis (E) has a frozen primary metric, predeclared effect size, strongest conventional comparators, untouched holdout, ablations and null controls.
6. The evidence status `PASS` belongs to an **exact test**, not to a whole robot or to EFMW physics. An internal software test does not qualify as independent replication.
7. Accepted modifications create a new build revision; rejected proposals stay in an append-only audit ledger. Cryptographic hashes detect byte changes, not the identity or authority of a human signatory.
8. Neither an AI model nor a research-supplied `coherence_score` can change safety thresholds or release hardware.

## Authorization matrix

| Actor | Propose design | Approve software experiment | Approve motor energization | Override E-stop | Modify safety firmware |
|---|---|---|---|---|---|
| EFMW/AI assembly planner | YES, proposal only | NO | NO | NEVER | NEVER |
| Research operator | YES | with delegated review | NO, independently insufficient | NEVER | NO |
| Qualified hardware integrator | YES | YES | only with safety review and procedure | NEVER | controlled maintenance only |
| Independent safety assessor | Review/veto | Veto | required approval/veto | NEVER | review, no AI direct writes |
| Physical E-stop system | n/a | n/a | can inhibit | latches until deliberate reset | protected system |

## Stop / default rule

Any missing signature, missing immutable artifact, unsigned mode selection, contradictory telemetry, power fault, critical unclosed hazard or external safety system fault causes `UNRESOLVED` or `FAIL`, and therefore **no permission to advance**.
