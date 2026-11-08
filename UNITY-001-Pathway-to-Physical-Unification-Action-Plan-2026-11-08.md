# UNITY-001 — Pathway to Physical Unification: An Evidence-Gated Action Plan

**Research program:** Matthew Chenoweth Wright / Monolithic LLC  
**Preparation:** AI-assisted technical planning  
**Date:** 8 November 2026  
**Document type:** prospective research action plan, not an empirical finding  
**Status:** **PROPOSED — UNITY NOT ACHIEVED; NO PHYSICAL CLOSURE CLAIMED**

**Related records:** [MOC-001 methodology](MOC-001-Compiling-Ontologies-Toward-Testable-Unity-of-Physics-2026-11-08.md) · [Unity Appendix](research/moc-001/UNITY_APPENDIX.md) · [Observe Unity](https://enuminous.github.io/Observatory/) · [Observatory source ledger](https://github.com/enuminous/Observatory)

> **Operating rule:** Unity is not achieved by collecting equations. The goal is to establish source-faithful mathematical relationships, recover independently successful physical descriptions in their tested regimes, and risk falsifiable predictions. A documented obstruction or negative result counts as progress, not defeat.

## Executive decision

Adopt a **seven-phase, evidence-gated** program. Begin with **UNITY-001: Source-Frozen Gravitational Correspondence**, a deliberately bounded campaign to inspect one GR–matter–EFMW candidate interface before attempting a global 22-sector synthesis.

Two finish lines must remain separate:

1. **Research infrastructure completion:** a compiler and ontology registry that faithfully import defined mathematical sources, provide typed expressions, explicit interfaces, replayable checks, provenance, export and failure-aware evidence ledgers.
2. **Physical-theory completion:** a coherent mathematical model with well-defined correspondence to established physics and a distinguishable, experimentally supported new prediction; comprehensive claims would additionally need a satisfactory quantum/gravitational interface and broad empirical coverage.

The first is a software and formal-research goal. The second is an open scientific problem with **no guaranteed timetable or success**.

## 1. Starting evidence — exact denominators

The MOC-001 / Observe Unity snapshot registers **22 ontology sectors, 22 equation record slots, 17 quantities, four unresolved interfaces, nine open obligations and 12 source links**. It is a static representation of an earlier local compiler run, **not** a complete import of the source physics.

| Metric | Status | Correct interpretation |
|---|---:|---|
| Structural PASS findings | **5 / 40** | Four restricted dimension checks plus one registry check |
| Equation records with dimensional PASS | **4 / 22** | Two established reference equations and two illustrative expressions; not a validated field-equation derivation |
| EFMW-specific physical PASS | **0** | No established new EFMW-specific effect or theory |
| Structural FAIL findings | **0 / 40** | No contradiction detected in the limited checks actually run |
| UNRESOLVED findings | **35 / 40** | Eighteen equation checks, four interfaces, nine obligations, four source-pinning findings |
| MOC-001 local Python tests | **16 / 16 PASS** | Software checks, not physical confirmation |
| New Lean 4 kernel replay for the unified model | **Not run** | No new formal certification |
| External physics test / independent replication | **Not performed** | Physical Unity remains unresolved |

**Critical reporting rule:** Do not say “five of 22 equations passed.” The fifth PASS is the registry check. The two illustrative dimensional passes are not laws of established physics, and no EFMW-specific physical equation is independently validated.

## 2. Target mathematical specification

An organizational shorthand such as

\[
S_{\mathrm{organizational}}=S_{\mathrm{GR}}+S_{\mathrm{SM}}+S_{\mathrm{interaction}}+S_{\mathrm{candidate}}
\]

is **not** a completed action or unified theory. A valid sum requires compatible integration domains, measures, fields, transformation laws, boundary terms, quantum prescriptions and controls against double counting. Memory models may require nonlocal formulations or auxiliary degrees of freedom; not all laws should be forced into one local Lagrangian.

Suppose a putative unified system \(\mathcal U\) admits partial reduction maps \(r_i:D_i\subseteq X_\mathcal U\to X_i\) into established reference sectors. Under appropriate shared notions of evolution, the *target* correspondence criterion is

\[
d_i\bigl(r_i(T_{\mathcal U}^{t}u),\,T_i^t(r_i(u))\bigr)\leq \varepsilon_i(t,u)\quad(U1).
\]

For operationally defined observables,

\[
d_{Y_i}\bigl(A_i^{\mathcal U}(u),\,A_i(r_i(u))\bigr)\leq \delta_i(u)\quad(U2).
\]

These are **proposed tests, not theorems already established**. When sectors have incompatible notions of time, the correct correspondence may instead be between admissible histories or observable distributions. The criteria require declared domains, metrics, tolerances, conventions, and conditions.

A proposed novelty requires a predeclared physical comparison,

\[
\Delta y(x)=y_{\mathrm{candidate}}(x)-y_{\mathrm{conventional}}(x)\quad(U3).
\]

The comparator must be serious and domain-appropriate. For the gravitational informational hypothesis this includes the null \(\kappa_I=0\), conventional GR and plausible non-EFMW alternatives. Exact observational equivalence or inadequate discrimination is a legitimate negative/inconclusive result, not physical validation.

The [canonical Unity Appendix](research/moc-001/UNITY_APPENDIX.md) is the governing reference for U1–U3.

## 3. Phase-by-phase execution program

### Phase 1 — Freeze the foundations: `ob_pin_sources` — PRIORITY ONE

**Objective:** reproducibly identify the precise original mathematical inputs before translating or joining them.

**First sources:** [Geometry](https://github.com/enuminous/Geometry), [Information-Tensor](https://github.com/enuminous/Information-Tensor), [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian), and [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction). Earlier README inspection is **not** an immutable freeze, and other proposed upstream repositories remain queued.

**Work:** record exact commit SHAs, original file hashes, paths and line/equation IDs, ownership/license, symbol conventions, units, Lean and Mathlib pins where relevant, build commands, actual replay output and open assumptions. Store original statements **unaltered**; separately record any proposed correction or alternative interpretation.

**Deliverables:** `sources.lock.json`, `source-equations.csv`, `conventions.md`, `provenance-ledger.md` and `replay-receipts/`.

**PASS P1:** every *claimed imported* expression resolves to immutable original bytes, exact extraction coordinates and a reproducibility procedure. **FAIL:** mismatch, alteration without disclosed versioning or invented provenance. **UNRESOLVED:** absent files, commit pins, environment or receipts. Pinning is necessary but not itself a mathematical proof.

### Phase 2 — Compile the mathematics

**Objective:** create typed mathematical representations without pretending distinct ontologies agree.

**Work:** define state spaces, field and tensor types, SI dimensions, index variance, density weights, regularity, operator domains, parameters, boundary/initial conditions and constraint assumptions. Convert supported original formulas into a versioned abstract-syntax tree (AST), preserving source notation next to normalized notation. Retain unparsed expressions as **unimported**, detect dependency cycles, and maintain conflict branches for differing source signs or currents.

**Deliverables:** `ontology-registry.json`, `equations/`, `type-check-report.json`, `constraint-graph.json` and `conflicts.md`.

**PASS P2:** all expressions labeled “compiled” are typed and source-linked, with executed static checks reported precisely. **FAIL:** false equivalence or silent equation repair. **UNRESOLVED:** unsupported parsing or missing mathematical premises. A parser PASS is not a dynamics PASS.

### Phase 3 — Establish a real correspondence map

**Objective:** replace an attractive graph edge with a defined reduction, embedding or coupling.

**Work:** begin with a bounded classical GR–matter consistency reference and one proposed EFMW–gravity interface. Specify its variables, maps, domains, limiting approximations and null behavior. Check actual source equations against independently varied candidate actions. Supply counterexamples and explicitly separate known minimal matter coupling from unresolved quantum gravity.

**Deliverables:** `CORRESPONDENCE_ATLAS.md`, `interfaces/*.json`, derivations and adversarial counterexamples.

**PASS P3:** at least one genuine mathematically defined cross-sector relation is demonstrated within precisely stated assumptions. **FAIL:** reproducible obstruction or incorrect source correspondence. **UNRESOLVED:** the interface is still verbal or a decorative link.

### Phase 4 — Verify dynamics, symmetries and formal obligations

**Objective:** establish bounded mathematical consistency and expose incompatibilities.

**Work:** test covariance, gauge identities, correct stress-energy and Bianchi relationships, conservation laws, constraint propagation, causal/hyperbolic properties where required, stability and quantum consistency where claimed. Address the reported scalar-sign mismatch, unmatched gauge currents and gravitational stress identification in [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian), and the energy-accounting boundary described in [WITD-002](WITD-002-Where-Does-the-Memorys-Energy-Go-2026-11-05.md). Rebuild exact Lean 4 statements against pinned dependencies and publish axiom and kernel-replay receipts. Run numerical convergence and negative controls separately.

**Deliverables:** `formal/`, `lean-replay.md`, `numerics/`, `invariants.json`, `dynamic-audit.md`, `counterexamples/`.

**PASS P4:** named theorems or numerical statements survive the corresponding executed check under published assumptions. **FAIL:** reproduced contradiction. **UNRESOLVED:** partial or missing replay, unproved physical premises. A green CI build cannot independently establish the physical correctness of its axioms.

### Phase 5 — Derive one discriminating prediction

**Objective:** turn mathematical proposals into a physically risky claim.

**First candidate:** does the proposed gravitational coupling \(\kappa_I\) imply an operationally measurable effect distinguishable from \(\kappa_I=0\), ordinary GR and conventional alternatives?

**Work:** derive any correction from frozen equations *without* choosing a convenient new coefficient after seeing the outcome. Define source and detector couplings, measurement units, calibrations, uncertainty, nuisance parameters, feasibility and a realistically strong reference model. Freeze the primary statistic, effect size, sensitivity/power rationale, holdout definition, exclusions and stopping rules before test data access. If no distinctive effect follows, document equivalence or non-identifiability.

**Deliverables:** `PREDICTION_001.md`, `prediction-spec.json`, `null-models/`, `preregistration.md` and sensitivity report.

**PASS P5:** a quantitatively specified, identifiable, prospectively testable prediction with locked comparisons. **FAIL:** invalid derivation or manufactured novelty. **UNRESOLVED:** unspecified observable or insufficient feasibility. Passing P5 is *readiness to test*, not empirical success.

### Phase 6 — Confront independent observations

**Objective:** determine whether the frozen candidate survives measurement.

**Work:** obtain external data with acquisition provenance, calibration, uncertainties, selection effects and raw checksums; do not mislabel previously inspected data as blind. Compare candidate and conventional baselines with identical information budgets. Publish raw outputs, confidence or credible intervals, nuisance sensitivity, alternate models, all negative controls and documented failures. Evaluate established physics only in the tested domains.

**Deliverables:** `external-data-manifest.md`, `results/`, `external-comparison.md` and reproducible analysis code.

**PASS P6:** the *predeclared* distinguishing physical prediction survives an appropriate external test with credible uncertainty control. **FAIL:** the prediction is contradicted within its declared domain. **UNRESOLVED:** instrumentation, precision or systematic limitations prevent a decision. A synthetic demonstration is not a physical experiment.

### Phase 7 — Replication, critique and expansion

**Objective:** test whether conclusions survive independent mathematical and physical scrutiny.

**Work:** provide unaffiliated groups frozen inputs, theorem statements, tests, independent execution instructions and data/protocols. Invite contrary derivations and independently collected or unseen data. Preserve critiques, disagreements and unsuccessful attempts. Extend sector by sector only where actual maps exist. If claiming *total* physical unity, explicitly address the quantum gravity interface and the full range of claimed physical observations.

**Deliverables:** `replications/`, independent receipts, `UNITY-STATUS.md` and an open discrepancy ledger.

**PASS P7:** independently reproduced evidence supports the *specified* physical claim. P7 on one narrow interface does **not** close a total theory. **UNRESOLVED:** otherwise.

## 4. First flagship campaign: UNITY-001 — Source-Frozen Gravitational Correspondence

The smallest meaningful campaign contains six sequential tasks.

| Order | Task | Required evidence | Outcome boundary |
|---|---|---|---|
| 01 | Pin source revisions and original bytes | Exact SHAs, paths, hashes, environments | No claim based only on mutable URLs |
| 02 | Import source-faithful equations | Original GR/matter/EFMW statements, sign and index conventions | No normalized substitution passed off as original |
| 03 | Compare metric variation, source split and stress/conservation premises | A real derivation or counterexample | PASS / FAIL / UNRESOLVED by mathematical claim |
| 04 | Evaluate zero-coupling and limiting cases | Explicit \(\kappa_I=0\) reference; ordinary-matter alternatives | Baseline recovery, obstruction or ambiguity |
| 05 | Find or rule out an identifiable observation | Quantitative response, instrument model, uncertainty and null | Viable prediction or documented non-identifiability |
| 06 | Freeze and publish a complete audit | Proof/counterexample logs, command receipts, claims and limitations | A bounded campaign report, not a universal closure certificate |

**Stop conditions:** reject or pause any derivation dependent on unpinned source text; preserve source-sign/covariance contradictions as FAIL when actually demonstrated; close the novelty claim in its tested domain if a standard model reproduces it; never retune after a holdout is opened. Every unexecuted gate stays UNRESOLVED.

The first commit to a dedicated implementation corpus should therefore contain a source-lock manifest and an original-equation extraction ledger. Only after those files and their receipts exist should [Observe Unity](https://enuminous.github.io/Observatory/) be updated with new PASS findings.

## 5. Reporting contract and change control

Every item in the cumulative evidence ledger needs a stable ID, provenance, exact assumptions, method and result. Suggested schema:

~~~yaml
finding_id: UNITY-001-...
claim_class: reference | derived | candidate | simulation | prediction | measurement
source_commit: UNRESOLVED
source_file_hash: UNRESOLVED
equation_or_theorem_id: ...
assumptions_and_conventions: ...
verification_method: static | Lean-kernel | numerical | measured-data | replication
replay_command_or_protocol: ...
expected: ...
observed: ...
status: PASS | FAIL | UNRESOLVED
scope_limitations: ...
independent_review: ...
~~~

**PASS** means only that a *named executed gate* succeeded in its stated domain. **FAIL** means the predeclared proposition or check was contradicted. **UNRESOLVED** means inputs, proof, measurement or execution are missing or inconclusive. Never inflate structural results into physical results.

Every corrected equation, changed parameter, modified null model, reinterpreted observable, new proof assumption or updated benchmark must have an explicit version and downstream invalidation record. The old source and failures remain reviewable. A theoretical explanation equivalent to a conventional model is not independent discovery of an EFMW-specific physical mechanism.

## 6. Dependencies and resource-efficient execution

~~~text
ob_pin_sources                     [FIRST; UNRESOLVED]
  └─ faithful source-equation import + conventions
       └─ typed compilation and recorded incompatibilities
            └─ one explicit correspondence map + counterexamples
                 └─ invariant and dynamic verification
                      └─ frozen discriminating prediction + nulls
                           └─ external experiment
                                └─ independent replication
                                     └─ sector-by-sector synthesis
~~~

Safe parallel work can improve the parser, prepare reference implementations and negative controls, write reviewer instructions, and build evidence exporters. But no downstream claim is promoted to PASS before its prerequisite is actually verified.

## 7. Milestone decisions, not promised dates

| Gate | Advancing evidence | Invalid shortcut |
|---|---|---|
| M1 source integrity | Pinned files, original equations, checksums, extraction coordinates | README link alone |
| M2 typed import | Parsed, versioned equations with stated units, tensor types, premises | Free-text LaTeX called verified |
| M3 cross-ontology map | Domain-specific map, theorem or counterexample | Diagram arrow |
| M4 mathematical dynamics | Actual exact proof replay and independent numerical checks | CI badge as physical evidence |
| M5 discriminating prediction | Frozen source-to-observable derivation, null controls and feasibility | Post hoc correction |
| M6 observed result | Independent data, error model and preregistered assessment | Synthetic example as measurement |
| M7 replication | Unaffiliated reproduction plus scope-correct inference | Internal rerun as independent replication |

After each milestone ask: *Which precise hypothesis was tested? What would falsify it? Which source or certificate is missing? Is the predicted effect distinguishable from conventional explanations?* If an answer is missing, keep that claim UNRESOLVED.

## 8. Definitions of research closure

**MOC-001 software completion** can be reached when the promised source management, type checking, interfaces, evidence exports and test/replay tooling work under a clear versioned specification. Its outstanding physical questions may remain unresolved.

**UNITY-001 campaign closure** can yield (a) a well-supported, bounded mathematical connection and testable candidate prediction; (b) a demonstrated contradiction or conventional equivalence closing that novelty route; or (c) an explicit incompleteness assessment explaining why the question remains UNRESOLVED. Closing a campaign does not close physics.

**Physical Unity** would require a much stronger, independently scrutinized theory recovering established physics, resolving the physical compatibility problems within its claimed scope and repeatedly surviving external experiments. We do not currently possess such a completion certificate.

### Immediate operational instruction

**Perform `ob_pin_sources` first.** Freeze the four initial repositories' commits and source hashes, identify the actual original mathematical statements and proof environments, and record failures without silent repair. Then test one real GR–EFMW correspondence. This is a tightening of the scientific standard, not a retreat.

---

## Sources and related work

1. [MOC-001 working paper](MOC-001-Compiling-Ontologies-Toward-Testable-Unity-of-Physics-2026-11-08.md).
2. [MOC-001 Unity Appendix: mathematical correspondence and empirical closure](research/moc-001/UNITY_APPENDIX.md).
3. [MOC-001 research companion: local prototype and evidence limits](research/moc-001/README.md).
4. [Observe Unity public site](https://enuminous.github.io/Observatory/) · [source and finding ledger](https://github.com/enuminous/Observatory).
5. [TOE-001 conditional two-scalar action and correspondence study](TOE-001-Unified-Action-and-Correspondence-Test.md).
6. [EFMW physical-validation research roadmap](EFMW-Physical-Validation-Research-Roadmap-2026-11-03.md).
7. [WITD-002 energy accounting](WITD-002-Where-Does-the-Memorys-Energy-Go-2026-11-05.md).

*This is a prospective research action plan. Publication here does not certify completion of the source-pinning phase, any candidate physical law, Lean kernel replay, an independently replicated experiment, or a theory of everything.*
