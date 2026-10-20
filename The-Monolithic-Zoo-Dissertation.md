# The Monolithic Zoo: An Adversarial, Provenance-Aware Architecture for Formal and Empirical Scientific Claim Evaluation

### A dissertation-style technical monograph on recursive criticism, theorem verification, computational reproducibility, and scientific epistemology

**Matthew Chenoweth Wright**  
**Monolithic LLC — October 20, 2026**

Summary for Technical and Commercial Readers

What the Monolithic Zoo is. A claim-evaluation architecture, not a theory of nature. A scientific or mathematical claim arrives in whatever form it lives in: prose, equation, Lean theorem, simulation, report. The Zoo returns a structured record separating what is syntactically well formed, what is formally derivable from stated assumptions, what the implementation actually corresponds to, what the evidence supports, and what remains an open obligation. Its analytic procedures, the animals, each target a distinct failure mode: circularity, scope inflation, missing provenance, unstated dimensions, correlation read as causation, post hoc selection. The animal names are organizational. They are not themselves a claim of novelty.

What it has caught in practice. Three examples, all drawn from the author's own corpus, which is the harder test than auditing someone else.

Necessity versus permission. For the source-free scalar wave equation, the constant field is a solution. The equation therefore does not entail a nonzero rotational state. The Zoo's counterexample defeats a universal necessity claim without denying that rotational solutions exist in a larger theory, or that physical systems rotate.

An identifiability degeneracy. The Post-156 audit examines the effective relation between rotation and expansion. In a model whose curvature contribution carries the same inverse-square scale factor, the combination can be absorbed into an effective curvature parameter. Expansion-only evidence cannot separate the two. The correct output is a demand for an independent directional or rotational observable, not a detection claim.

Denominator discipline. The portfolio's 181 registry entries are not 181 theorems freshly checked in that repository. The 102 equations classify as 15 conditional standard survivors, 28 structural survivors, 12 requiring empirical test, and 47 open specifications. The 774,180 potential evaluation slots are combinations in an index, not completed tests. An additional 46-module Lean 4 package pins Lean 4.19.0 without Mathlib and reports a 90-comparison reference runner, while disclosing that 17 rank-aggregation modules operate on supplied feature columns rather than formalizing upstream feature extraction. An audit system that refuses to inflate its own numbers is the product.

What is not established. There is no independent demonstration that the Zoo detects consequential scientific defects better than a matched conventional review. That question is open, and this document says so in its own text.

The experiment that would settle it. A preregistered corpus of labelled claims: sound theorems and proofs, false statements with counterexamples, sound proofs of misleading specifications, reports with leakage or incorrect denominators, and improperly attributed material. Items are developed and labelled by independent experts, with holdouts inaccessible during operator design. Comparators are matched on time, computation, search access, and prior context: a single structured model reviewer, an ensemble at the same budget, static verification and unit-test tooling, and expert human review where practical. The primary outcome is recall of consequential defects at a fixed false-positive rate, with blinded adjudication and uncertainty intervals. Ablations remove provenance checking, counterexample search, and the proof kernel one at a time, with negative controls including bogus citations, circular proofs, duplicated conclusions, and prompt-injection contamination. Results are published whether or not they flatter the system.

What a bounded engagement looks like. Two shapes. A single-artifact audit freezes one flagship theorem and its stated product connection at a pinned commit, reproduces the Lean build and axiom dependencies, attacks the construction's assumptions, traces one product claim back to the theorem, and documents the findings in a separate repository. A comparative study runs the benchmark above on a specified class of claims and reports results against the organization's current review process. Scope, data handling, deliverables, and acceptance criteria are agreed in writing before work begins.

**Document status:** Scholarly technical dissertation-style manuscript, not a university-submitted or degree-awarded dissertation. The evidence survey covers identified repository documents inspected on October 20, 2026. It is not a new independent execution of every Lean build, regression suite, or scientific experiment.

## Abstract

Scientific claims increasingly emerge from coupled systems of symbolic mathematics, simulation, computational agents, experimental datasets, and natural-language argument. These systems can propagate an invalid premise far beyond its initial appearance: software can execute correctly against an inadequate specification, a theorem prover can certify a proposition whose physical referent has not been justified, and an apparently decisive simulation can reflect an unacknowledged assumption or inappropriate comparator. This dissertation examines the **Monolithic Zoo**, an adversarial scientific-evaluation architecture developed within the Einstein–Feynman–Maxwell–Wright (EFMW) research program, as a case study in separating mathematical well-formedness, deductive derivability, computational correspondence, empirical support, and claim provenance.

The Zoo organizes specialized analytic procedures—termed *animals*—into a structured audit intended to identify different failure modes rather than provide generic model agreement. Its documented implementations include a 46-animal Lean 4 package with pinned upstream kernel snapshots, numerical correspondence fixtures, axiom auditing, and selected source-report models; a separate 102-equation catalog and audit; and a Post-156 portfolio-level theorem and evidence review. The research program has produced both surviving conditional mathematical results and explicit negative or non-identifiability findings. In particular, the 102-equation audit classifies 15 entries as conditional standard survivors, 28 as structural survivors, 12 as requiring empirical testing, and 47 as open specifications. The Post-156 audit warns against treating registry counts as distinct kernel-verified theorems or promoting candidate mathematical relations directly into new physical laws.

We formalize a claim-centered evidence architecture, identify soundness and coverage obligations for its stages, propose a controlled assessment protocol against conventional review workflows, and analyze methodological hazards including circularity, proof-scope inflation, correlated agent errors, dataset leakage, and interpretive overreach. The central thesis is *methodological rather than cosmological*: a scientific reasoning system becomes more reliable to the extent that it can document not just why a claim appears supported, but which assumptions, counterexamples, untested mappings, and independent observations could defeat it. Whether the Zoo measurably outperforms existing scientific-audit methods remains an empirical question.

**Keywords:** formal verification; scientific reasoning; adversarial audit; Lean 4; provenance; reproducibility; falsifiability; epistemic uncertainty; computational science; multi-agent systems; EFMW.

---

## 1. Introduction

Scientific reasoning requires distinctions that fluent explanatory systems can obscure. A proposition may be intelligible but false; internally consistent but empirically unsupported; verified against a computer representation but unrelated to its purported physical referent; or statistically significant only under post hoc selection. When scientific artifacts move between prose, mathematics, executable programs, experimental instruments, and automated agents, each translation becomes a possible site of error.

The Monolithic Zoo addresses this general problem by distributing critical operations across named, specialized audit procedures. The animal metaphor is an organizational device, not itself a claim of biological, cognitive, or mathematical novelty. Its scientific contribution, if sustained by evidence, lies in explicit task decomposition, traceability to immutable source artifacts, counterexample generation, conditional proof obligations, and a refusal to equate software or theorem success with physical confirmation.

The motivating EFMW portfolio is unusually demanding because it spans proposed physical relations, equation catalogs, formalized specializations, finite computations, and broader speculative interpretations. Such breadth makes the Zoo useful as a methodological testbed; it does not establish the EFMW framework as a validated theory of nature.

### 1.1 Research questions

This dissertation asks:

1. Can a heterogeneous scientific claim be represented as a machine-auditable object while preserving the difference between its prose, formal meaning, computational implementation, and physical interpretation?
2. Which substantive obligations can finite algorithms, theorem provers, and numerical fixtures actually discharge?
3. How can multi-operator adversarial evaluation reduce unsupported promotion and the propagation of hidden assumptions?
4. How should the Zoo’s own coverage, failures, and source dependencies be audited?
5. What independent experiments would establish whether the system improves research quality relative to standard alternative workflows?

### 1.2 Thesis

The proposed thesis is that **scientific reliability can be improved by maintaining an explicit, versioned chain from claim through assumptions, formalization, implementation, evidence, criticism, and revision**, provided that audit operators have defined semantics, negative controls, appropriate independence, and independently evaluated performance. The evidence currently demonstrates implementations of portions of this architecture; it does not yet establish a general quantified improvement in scientific discovery.

## 2. Theoretical foundations and related methods

### 2.1 Falsification and scientific fallibility

Popperian falsifiability emphasizes that claims gain empirical content through observations that could show them false. The Zoo operationalizes a related engineering discipline: every promoted claim should state the conditions under which it would be downgraded. This principle is necessary but insufficient; a formally falsifiable claim can still be practically untestable or poorly measured.

### 2.2 Formal proof and specification adequacy

Lean 4 and comparable proof assistants can check whether a term inhabits a declared type and whether a theorem follows from axioms and definitions admitted by the kernel. They cannot, without additional bridges, establish that a symbol denotes the intended physical observable or that a simulation matches nature. The formal-methods distinction between **verification** (“does the implementation satisfy its specification?”) and **validation** (“is this the appropriate specification of the real problem?”) is central.

### 2.3 Reproducibility, provenance, and methodological transparency

Computational reproducibility requires more than a file with plausible output. It requires fixed source versions, environments, input hashes, deterministic seeds where applicable, expected tolerances, execution logs, and enough description for third parties to repeat the analysis. Provenance should capture who or what introduced each assumption, when a theorem statement changed, whether external code was copied, and which software license conditions apply.

### 2.4 Diverse criticism and correlated failure

Specialized reviewers can uncover distinct failure modes, but multiple reviewers built on the same language model, assumptions, dataset, or templates may share errors. Agreement among correlated agents cannot be counted as independent confirmation. The Zoo's diversity therefore requires measurement at the *failure-detection level*, not merely distinct names or prompts.

## 3. Claim-centered scientific architecture

A candidate claim is represented as an auditable record

\[
C=(I,S,A,D,O,M,E,P,V),
\]

where:

- \(I\): stable claim identifier;
- \(S\): exact source expression, including text or code;
- \(A\): explicit assumptions;
- \(D\): mathematical domain, dimensions, types, and operators;
- \(O\): proof or test obligations;
- \(M\): machine-readable model or implementation;
- \(E\): evidence, including negative evidence and null controls;
- \(P\): provenance, dependencies, versions, contributors, and licensing;
- \(V\): current status and rationale.

The record should retain *separate* judgments for syntactic validity, typing, logical consequence, implementation correspondence, empirical support, and claimed novelty. A convenient candidate status lattice distinguishes **proposed**, **formalized**, **conditionally proved**, **numerically tested**, **empirically supported**, **independently replicated**, **contradicted**, and **superseded**. These labels describe an ideal classification system; not every currently published Zoo record implements this exact tuple or all of these statuses.

The audit may be represented as a directed dependency graph \(G=(N,E_G)\). A result depends on source definitions, lemmas, assumptions, executable transformations, and measured data. Criticism propagates along dependency edges when a source assumption is withdrawn. However, a failed upstream premise should not automatically invalidate independent downstream claims supported by alternate derivations.

### 3.1 An elementary inference rule

Suppose a proof kernel verifies

\[
A_1,\dots,A_n\vdash T.
\]

The valid promotion is “\(T\) follows from encoded assumptions \(A_1,\dots,A_n\).” It is **not** “\(T\) holds for the observed universe.” The second claim additionally requires a justified mapping \(f\) from model variables to physical observables, evidence that the assumptions apply, and empirical tests. A claim promotion policy must refuse any unrecorded jump across these layers.

### 3.2 Audit operation

Let \(Z_j(C)\) be the result of animal \(j\) on claim \(C\), returning a structured record with verdict, tested preconditions, detected defects, evidence references, and unresolved obligations. A candidate aggregation is

\[
Z(C)=\mathcal A\big(Z_1(C),\ldots,Z_n(C)\big).
\]

The aggregator \(\mathcal A\) must not implement naïve majority voting. A single valid counterexample can refute a universal assertion regardless of how many other agents endorse it. A passing Lean proof can establish a formal obligation regardless of rhetorical skepticism, but cannot settle a separate empirical obligation. Aggregation must be *obligation-sensitive*.

## 4. Documented implementation: the 46-animal Zoo

The repository [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) reports a shared package containing the 46 original animal modules, each represented by selected operational kernels and contracts. It pins Lean 4.19.0 without Mathlib, provides source snapshots, and includes registration, regression, axiom-audit, and verification machinery. The published README reports a selected reference runner with **90 comparisons** and a linked successful workflow run, while explicitly noting that **17 rank-aggregation modules** operate on supplied feature columns rather than formalizing upstream feature extraction and training.

This distinction is fundamental. A proved rank aggregator can still receive inappropriate inputs; a verified report can still summarize an inadequate experiment. The package’s selected-kernel scope must not be described as full verification of every associated upstream pipeline.

Extension reporting includes five selected decision procedures, structured report models for CHIMERA and CIRCUS/MONSTER, 1,432 reported source-executed certificates, and additional exact-threshold arithmetic certificates. These counts are repository-reported coverage statements requiring their associated versioned files and CI logs for independent repetition; they are not 1,432 independent confirmations of EFMW physics.

### 4.1 Specialized failure modes

The source architecture names animals including TORTOISE, CHIMERA, WOODPECKER, CIRCUS, and MONSTER. In the currently documented research workflow, CIRCUS is associated with circularity and provenance checks, MONSTER with perturbation or robustness stress, and WOODPECKER with arithmetic and threshold checks. Other animals require their own source-specific contracts. The names alone do not authorize attributing a particular algorithm or scientific result to a module.

An effective specialist should specify:
1. Its input grammar and applicability domain;
2. A precise defect it can detect or bound;
3. An expected output structure and witness;
4. Soundness limits, failure modes, and positive/negative fixtures;
5. Independence assumptions relative to other operators.

### 4.2 The status of the formal proof evidence

The repository describes an axiom allowlist and controls against inappropriate admitted axioms or \`sorryAx\`. The existence of these checks is valuable; the current dissertation did **not** run them independently. Any public statement of a passing build must be tied to a particular commit, toolchain, workflow run, and theorem scope. Historical successful CI runs do not automatically establish that all future branch heads pass.

## 5. Equation-level application: the canonical 102

The separate [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) package freezes the ME-001–ME-102 catalog and assigns per-equation Zoo dispositions. Its README reports:

| Classification | Count | Interpretation |
|---|---:|---|
| Conditional standard survivor | 15 | Recognizable mathematical content under conditions |
| Structural survivor | 28 | Coherent definition or mathematical predicate |
| Empirical test required | 12 | External data must adjudicate |
| Open specification | 47 | Domain, units, operators, assumptions, or derivations incomplete |
| **Total** | **102** | Complete identifier accounting |

This classification resists a common error: treating the number of equations in a catalog as the number of new physical laws.

The repository reports 53 discrete or structural typed models and, in its newer analytic coverage description, 21 explicit analytic models plus 28 partial specializations or counterexample results among the other 49 entries. These coverage categories do not mean that all original source obligations are completely formalized. The repository also describes specific work on phase currents, Cartesian vorticity, scalar-action variations, linearized gravity, and rotation/cosmology, while preserving open nonlinear geometric, quantum-gravitational, and empirical bridges.

### 5.1 Example: necessary rotation versus permitted rotation

For a source-free scalar wave equation,

\[
\nabla^2\phi-c^{-2}\partial_t^2\phi=0,
\]

the constant \(\phi=C\) is a solution. Therefore the equation alone does not logically entail a nonzero rotational state. This counterexample is a useful demonstration of **scope-specific falsification**: it defeats a universal necessity claim without denying that rotational solutions exist in larger theories or that physical systems rotate.

### 5.2 Example: rotation–curvature identifiability

The Post-156 audit examines an effective relation

\[
\Delta H^2=\frac{\Omega_U^2}{a^2}.
\]

In a model whose curvature contribution has the same \(a^{-2}\) scaling, the combination can be absorbed into an effective curvature parameter. This creates an identifiability problem for expansion-only evidence. A competent Zoo finding should document the degeneracy and request an independent directional or rotational observable, rather than interpreting a fitted parameter as a cosmic-rotation detection.

## 6. Portfolio-level audit and non-inflation rules

The [EFMW_Post156_Zoo_Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit) distinguishes a 156-entry historical baseline from later promoted theorem-family entries and five separately kernel-checked results T177–T181. Its README explicitly cautions that the total **181 registry entries are not 181 theorems all freshly checked in that repository**. It also documents a distinction between earlier repository-backed claims and actual scope of current builds. Its interpretation of candidate physical laws remains conditional.

The portfolio-level “research engine” connects catalogs of 102 equations, 165 triplets and 46 animals into \(102\times165\times46=774{,}180\) **potential evaluation slots**. These are combinations in an index, not 774,180 completed scientific tests, proofs, or discoveries. A reported synthetic demonstration lists 48 attempts, 47 computed outputs, two unmet criteria, and one rejected input, with no newly accepted scientific mapping.

This is a useful illustration of why audit systems require denominator discipline: the number of possible tests, the number actually applicable, the number executed, the number passing a defined criterion, and the number independently replicated must be separately recorded.

## 7. Experimental validation design

The central untested claim of this dissertation is that structured, provenance-aware adversarial evaluation improves science relative to existing practice. We propose an evaluation that can fail.

### 7.1 Benchmarked tasks

Construct a preregistered, diverse corpus containing:
- sound theorem statements and proofs;
- false statements with counterexamples;
- sound formal proofs of misleading or incomplete specifications;
- synthetic research reports with leakage, incorrect denominators, or post hoc hypotheses;
- empirically valid but underexplained findings;
- intentionally ambiguous or unsupported physical extrapolations;
- duplicated, superseded, or improperly attributed source material.

Benchmark items should be developed and labeled by independent experts, with hidden holdouts inaccessible during operator design.

### 7.2 Comparator conditions

Evaluate the Zoo against (A) a single structured language-model reviewer, (B) an ensemble of generic reviewers with the same compute budget, (C) standard static verification and unit-test tools, and (D) expert human review where practical. A strong comparison should match time, computation, search access, prior context, and opportunities to request clarification.

### 7.3 Outcome measures

Primary outcome: recall of consequential defects at fixed false-positive rate, with uncertainty intervals and blinded adjudication. Secondary measures: precision, time to valid counterexample, percentage of claims with complete provenance, calibration of verdict confidence, reproducibility of citations, costs, and robustness against paraphrase or adversarial reformulation. Where a proof assistant is used, separate kernel-checked obligations from informal reviewer judgments.

A possible design uses paired task-level measurements \(d_i = \ell_{\mathrm{baseline},i}-\ell_{\mathrm{Zoo},i}\) under a preregistered loss function \(\ell\). The estimated difference and interval must be calculated over independent tasks or appropriately clustered families, not over correlated outputs counted as independent discoveries.

### 7.4 Ablations and negative controls

Remove provenance checks, counterexample search, independent specialized modules, or the proof kernel one at a time. The system should demonstrate that its complexity contributes measurable value rather than merely increasing verbosity. Include bogus citations, circular proofs, duplicated conclusions, and prompt-injection contamination to test claim laundering.

### 7.5 Reproducibility and preregistration

Freeze the benchmark, metric definitions, search/tuning budget, model versions, prompts, seeds, and code; make source archives available subject to licensing. Permit third-party reproduction. Publish negative and null results without retroactively relabeling success criteria.

## 8. Limitations and risk analysis

**Specification drift.** Formalizing a convenient weakened proposition while presenting the original stronger claim as proved is a principal danger. Both statements must appear side by side.

**Shared errors.** Different animal names do not guarantee independent evidence. Measure correlated misses, especially when models or sources overlap.

**Computational correspondence.** A Lean theorem about rational arithmetic may not correspond exactly to floating-point runtime behavior. Prove an explicit refinement theorem or characterize error bounds.

**Domain transfer.** A structurally valid equation may lack dimensions, boundary conditions, physical coupling, or an identifiable measurement process.

**False reassurance from passing CI.** Infrastructure failures and proof failures differ; a green build proves neither untested source completeness nor empirical fit.

**Sociotechnical hazards.** Claim evaluation may be used as an authority signal in investment, medicine, education, or other consequential settings. An automated verdict should preserve contestability, audit logs, and human-governed decisions.

**Licensing and attribution.** The Zoo references upstream contributions and code. Open visibility and accessibility do not alone establish reuse rights, assignment, or commercial licensing authority.

**Generalization.** A performance advantage on the EFMW portfolio would not demonstrate superior review for every discipline or class of claims.

## 9. Scientific and educational applications

The Zoo is best regarded as an *instrument for structured skepticism*. In research, it can surface hidden assumptions and convert broad claims into tractable proof or empirical obligations. In teaching, it can make the distinction between statement, inference, evidence, and refutation visible. In scientific software, it can encourage explicit correspondence among implementation, specification, and observational purpose.

A student or nonspecialist could submit a proposition and receive a traceable explanation of which questions are mathematical, which are empirical, and which are presently undecidable using supplied evidence. Such accessibility is a promising application but requires usability, calibration, privacy, and learning-outcome testing. A helpful interface should not imply that every Zoo verdict has the epistemic standing of a peer-reviewed finding.

## 10. Roadmap

The next research phase should prioritize the following sequence:

**Stage 1 — Evidence freezing:** Fix representative repository commits, dependency snapshots, upstream licenses, and reproducibility instructions. Generate machine-readable coverage summaries for each animal and claim.

**Stage 2 — Formal soundness scope:** Define and audit the result schemas, source correspondence, explicit axiom policies, and counterexample witnesses for the highest-risk modules.

**Stage 3 — Blinded benchmark:** Run matched-budget experiments against strong conventional alternatives, reporting defect-detection metrics and calibration rather than only aggregate “pass” percentages.

**Stage 4 — Independent evaluation:** Have third parties reproduce the reported runs and adjudicate disputed defect labels.

**Stage 5 — Domain expansion:** Test hypotheses in mathematics, computational engineering, education, and experimental science, maintaining separate validity criteria.

**Stage 6 — Governance:** Publish contributor attribution and licensing records, versioned corrections, retractions, and mechanisms for appeal or manual override.

## 11. Discussion

The Zoo's strongest intellectual position is not that EFMW has discovered universal laws. Rather, it is that a scientific program can build machinery capable of resisting premature declarations of discovery. The 102-equation classification, conditional theorem counts, constant-field counterexample, and curvature–rotation degeneracy show how negative and bounded results can clarify a research program.

A recursive critic must also remain corrigible. Auditing one's own conclusions creates a further risk of infinite review loops, circular confidence, or inflated claims based on the volume of self-generated analysis. An effective termination rule can stop when every material obligation has either a specified witness or a documented unresolved status; infinite self-criticism is not a substitute for independent observation.

The ambition of the architecture is therefore *not omniscience*. It is disciplined uncertainty management: discover what survives scrutiny, explain why, record what does not, and expose the next observation that could change the answer.

## 12. Conclusion

The Monolithic Zoo constitutes a substantive research-software architecture for adversarial claim analysis, selected formal verification, source-aware regression testing, and epistemic classification. Inspected repository documentation demonstrates its operational development beyond conceptual description, including a 46-module Lean package, equation-level auditing, coverage records, finite certificates, and portfolio-level evidence reporting.

What has not yet been established is a general empirical advantage in detecting scientific mistakes or accelerating reliable discoveries over matched alternative systems. That question is not an embarrassment to the project; it is the defining next experiment.

The guiding principle is simple:

> **An audit system is valuable not because it certifies the researcher's conviction, but because it makes the researcher's convictions answerable to evidence.**

A mature Zoo should be capable of ruling against EFMW, against its author, against established conventions when warranted, and against its own prior judgments. The ultimate authority must remain explicit mathematical proof within its scope and reproducible observation within the physical domain—not the name of the framework, the number of modules, or the persuasiveness of an artificial critic.

---

## References and inspected project resources

1. Wright, M. C. [*Monolithic Zoo — 46 animals in Lean 4*](https://github.com/enuminous/Monolithic-Zoo-Lean4), README and linked coverage/verification records, inspected October 20, 2026.
2. Wright, M. C. [*Monolithic 102 — Zoo Audit + Lean 4*](https://github.com/enuminous/Monolithic-102-Zoo-Lean4), README and linked coverage records, inspected October 20, 2026.
3. Wright, M. C. [*EFMW Post-156 Theorem & Zoo Audit*](https://github.com/enuminous/EFMW_Post156_Zoo_Audit), README and linked audit artifacts, inspected October 20, 2026.
4. Wright, M. C. [*Devs 2.0: EFMW—Distributed Intelligence, Prediction, and Human Agency*](Devs2.0-EFMW.md), September 2026.
5. Wright, M. C. [*EFMW Zoo R-001: Primordial Recursion Boundary*](EFMW-Zoo-R001-Primordial-Recursion-Boundary.md), October 2026.
6. Wright, M. C. [*EFMW–MWI-001: Four-World Record-Entanglement Test*](EFMW-MWI-001-Four-World-Record-Entanglement-Test.md), October 2026.
7. Popper, K. R. *The Logic of Scientific Discovery*. Hutchinson, 1959 (English ed.).
8. Lakatos, I. “Falsification and the Methodology of Scientific Research Programmes.” In *Criticism and the Growth of Knowledge*, 1970.
9. National Academies of Sciences, Engineering, and Medicine. *Reproducibility and Replicability in Science*. National Academies Press, 2019. https://doi.org/10.17226/25303
10. de Moura, L., Kong, S., Avigad, J., van Doorn, F., and von Raumer, J. “The Lean Theorem Prover (System Description).” CADE-25, 2015. https://doi.org/10.1007/978-3-319-21401-6_26
11. Nosek, B. A. et al. “Promoting an Open Research Culture.” *Science* 348, 1422–1425 (2015). https://doi.org/10.1126/science.aab2374

## Statement of evidence and contribution

This manuscript synthesizes repository-reported architecture, classifications, and verification claims with a proposed comparative research methodology. It does not claim that all indexed theorems have been checked in this session, that the complete system has undergone an independent security or scientific audit, or that EFMW's speculative physical propositions have been experimentally validated. The claim tuple, aggregation formulation, benchmark design, and roadmap are analytical proposals in this dissertation, not retrospective descriptions of fully implemented components.

**Publication category:** Independent technical research monograph / dissertation-style exposition. No institutional degree, doctoral committee approval, external peer review, or new empirical trial is represented.
