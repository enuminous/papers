# MOC-001 — Unity Appendix

**Path:** `research/moc-001/UNITY_APPENDIX.md`  
**Companion paper:** [MOC-001 — Compiling Ontologies Toward a Testable Unity of Physics](../../MOC-001-Compiling-Ontologies-Toward-Testable-Unity-of-Physics-2026-11-08.md)  
**Date:** 8 November 2026  
**Status:** Proposed mathematical criteria; **no unity closure or physical verification achieved**.

## A. What "Unity" would have to mean

The term *Unity* refers here to mathematical and empirical unity across physical descriptions, not a claim that all historical or proposed ontologies are jointly true.

Let a candidate unified model be

\[
\mathcal U=(X_{\rm U},T_{\rm U},\Theta_{\rm U},C_{\rm U},\mathcal A_{\rm U}),
\]

with a specified state/model space, dynamics (or admissible histories), parameters, constraints, and observables. For each established reference sector \(i\), define a state space \(X_i\), its domain-appropriate evolution \(T_i^t\) where meaningful, and observables \(A_i:X_i\to Y_i\).

A genuine correspondence requires an explicitly constructed *partial restriction or limiting map*

\[
r_i:D_i\subseteq X_{\rm U}\longrightarrow X_i,
\]

not a declaration of resemblance. On a valid subdomain with compatible time/evolution notions, a quantified approximate commutation condition is

\[
d_i\!\left(r_i(T_{\rm U}^{t}u),\ T_i^{t}(r_i(u))\right)
\leq \varepsilon_i(t,u).
\tag{U1}
\]

This is a **proposed criterion**, not a proved identity. Define \(d_i\), the allowed domain, and tolerance \(\varepsilon_i\) before evaluating. Sectors without a common evolution parameter require a more general relation between admissible histories, not forced use of (U1).

If the unified theory predicts a sector's observable \(A_i^{\rm U}:X_{\rm U}\to Y_i\), the correspondence condition additionally requires

\[
d_{Y_i}\!\left(A_i^{\rm U}(u),\ A_i(r_i(u))\right)
\leq \delta_i(u)
\tag{U2}
\]

with predeclared uncertainty bounds and measurement conventions. Equations (U1) and (U2) alone are neither sufficient for physical completeness nor evidence of empirical success.

For a hypothetical new physical effect, define a forward observable model with a conventional comparator, for example

\[
\Delta y(x)=y_{\rm candidate}(x)-y_{\rm conventional}(x),
\tag{U3}
\]

and determine whether \(\Delta y\) is identifiable after nuisance, calibration, and strong alternative-model effects are accounted for. If \(\Delta y\equiv0\) over the available measurements—or the candidate is observationally degenerate—then the putative novelty is **not** established.

## B. The required compilation contract

| Layer | Requirement | What does not count |
|---|---|---|
| Source | Exact file/commit, hash, origin, license, original wording, environment | Mutable README citation as frozen theorem |
| Syntax | Versioned parser, explicit AST, preserved original formula | LaTeX string treated as executable semantics |
| Type/units | Dimension, index/tensor variance, density weight, domain and assumptions | Dimension match called a dynamical proof |
| Theory | Variational derivation or valid evolution laws; boundary and constraints | Naive addition of incompatible actions |
| Interface | Defined reduction/coupling map; quantified regimes | Same symbol used in unrelated models |
| Proof | Explicit hypotheses and exact independent kernel replay | Lean toolchain file without `lake build` receipt |
| Simulation | Convergence, seeds, errors, matched controls, exact outputs | Attractive animation as evidence |
| Observation | Calibrated data, source/detector coupling, nulls and alternatives | Post hoc effect or unconstrained fit |
| Independence | External audit and independent physical replication | Self-reported compiler success |

**PASS** is gate-specific and must name what was executed. **FAIL** records an actual discrepancy. **UNRESOLVED** is the default for absent mathematical maps, missing data, conflicting conventions, and unexecuted verification. No automatic promotion from UNRESOLVED to PASS is permitted.

## C. Initial cross-ontology bridge graph

The pilot carries four *declared but unimplemented* interface sockets:

1. `if_gr_sm` — general-relativistic spacetime and Standard Model matter. Classical coupling is available in restricted formulations, but the scaffold has not imported a shared full construction, and quantized-gravity completion is open.
2. `if_efmw_gr` — proposed informational effects and gravitational sources. The exact source stress tensor, gauge/covariance properties, and observational status of nonzero \(\kappa_I\) are not established.
3. `if_topology_field` — topological quantities and physical field observables. Required maps, regularity conditions, and stability under the intended dynamics are absent.
4. `if_observer_physics` — model states, measurement records, and observational probability rules. An observation model must be specified rather than assumed to follow from an ontology's name.

In the registry, a null or absent `map_definition` means **UNRESOLVED**. A compiler should never substitute narrative similarity for a mathematical map.

## D. Action formulation is a hypothesis, not the closure certificate

One may propose

\[
S_{\rm U}=S_{\rm GR}+S_{\rm SM}+S_{\rm interaction}+S_{\rm candidate},
\tag{U4}
\]

only after establishing consistent integration measures, field representations, domain, conventions, boundary terms, and double-counting controls. Some history-dependent kernels may require a nonlocal action, auxiliary fields, open-system dynamics, or a non-variational evolution law. An arbitrarily chosen sum does not prove covariance, gauge invariance, unitarity, stability, or renormalizability.

Where a valid action is supplied, the resulting Euler–Lagrange equations and constraint algebra must be independently derived and compared with the *original* sector equations, preserving any sign/current mismatch. A substitution of a conventional two-scalar model is not an identification of a historical EFMW tensor.

## E. Minimal concrete falsification gates

| Gate | Concrete question | Current disposition |
|---|---|---|
| U0 structure | Are graph identities, dependencies and elementary units internally checked? | **Bounded PASS**: Python pilot only |
| U1 provenance | Are full authoritative source equations frozen to immutable input hashes? | UNRESOLVED |
| U2 reduction | Do exact maps reproduce established tested theories in stated limits? | UNRESOLVED |
| U3 invariances | Are covariance, gauge identities, constraints, and conservation compatible? | UNRESOLVED |
| U4 EFMW origin | Do proposed information/memory terms follow noncircularly from frozen source equations? | UNRESOLVED |
| U5 physical discrimination | Is a measurable nonzero candidate effect distinguishable from \(\kappa_I=0\) and conventional alternatives? | UNRESOLVED |
| U6 mathematical replay | Are exact theorems, builds and numerical checks independently reproduced? | UNRESOLVED |
| U7 external evaluation | Does a frozen prediction survive external held-out data with uncertainty? | UNRESOLVED |
| U8 replication | Does a separate group replicate or falsify the proposed effect? | UNRESOLVED |

"Total unity" would require far more than these necessary gates, notably correct treatment of quantum spacetime and the full empirical domains. The table is a minimum progress criterion, not an exhaustive definition of a Theory of Everything.

## F. Failure-aware source relationships

The following source boundaries must survive any future integration:

- [Geometry](https://github.com/enuminous/Geometry): conditional source-split/Bianchi work is not experimental identification of \(\kappa_I\neq0\).
- [Information-Tensor](https://github.com/enuminous/Information-Tensor) and [WITD-002](../../WITD-002-Where-Does-the-Memorys-Energy-Go-2026-11-05.md): simulated memory and tensor diagnostics do not automatically yield conserved physical stress-energy.
- [EFMW-Lagrangian](https://github.com/enuminous/EFMW-Lagrangian): reported scalar-sign, gauge-current, and gravitational identification problems must remain visible rather than "fixed" silently by compilation.
- [Standard-Model-Reduction](https://github.com/enuminous/Standard-Model-Reduction): an established classical rewrite is not a derivation of the proposed 39-strata hypothesis.
- [TOE-001](../../TOE-001-Unified-Action-and-Correspondence-Test.md): a conventional two-scalar action provides conditional mathematical identities, not an EFMW-specific discovery or a quantum-gravity completion.

No statement in this appendix asserts that the four source repositories have been fully ingested into MOC-001. Their README documentation was inspected; exact frozen source and independent proof replay are still required.

## G. Reproduction reference and next work

The companion MOC-001 local prototype (not uploaded to `enuminous/papers` with this publication) reported 16/16 passing Python unit tests, and five structural PASS, zero FAIL, and 35 UNRESOLVED gate findings when compiled on 8 November 2026. Its locally archived ZIP SHA-256 is `77509faffce09dcbe23d31c4cb956d5e335fbd6c113edfed9cae7e22cbadeb7e`. The digest identifies a particular local artifact, but a digest without the artifact and an independent rerun is **not** a reproduction receipt.

A useful next experiment is to freeze exactly one existing-source expression and build one real interface map with a null comparator. For gravitational informational coupling, predeclare \(\kappa_I=0\) and at least one strong conventional alternative; choose a measurable observable and uncertainty model; carry the analysis through to a negative or positive result without tuning the holdout.

**Unity closure certificate: NOT ISSUED.** The paper and appendix document testable requirements for a future closure attempt; they do not certify it.
