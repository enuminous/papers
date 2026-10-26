# Monolithic Zoo dissection: Romy Mondello · arXiv:2608.02634v1

**Binary certification edition.** The exact algebra checks pass, and the written mathematical argument survives review. The supplied evidence does not earn a positive certification from any of the 46 main Zoo operations or five extensions: all 51 binary certification gates return **FAIL**, for the specific reasons below. These are failures to substantiate Zoo certification, not 51 mathematical objections to the theorem. Fresh local Lean certification also fails its evidence requirement because no replay was performed.

**Prepared for Matthew Chenoweth Wright, Monolithic LLC, with AI-assisted analysis.**

Audit and revision date: October 26, 2026. The revised object is the **paper-plus-proof-audit evidence package**. The mathematical statement, polynomial formulas, and animal implementations are unchanged. This edition adds a strict binary decision layer; it does not claim that the animal implementations all have native pass/fail outputs or that all pipelines executed.

Revision provenance: the [first edition](https://github.com/enuminous/papers/blob/e08b8a6cd182b8dc820ea0db1907d8f90e9aa70a/Mondello-Separable-Jacobian-Full-Zoo-Audit.md) classified most operations as inapplicable. This edition preserves that fact in explicit failure reasons. The policy was requested after the original analysis and is **not a preregistered experiment**. No Zoo-wide truth percentage is reported.

## 0. What PASS and FAIL mean

Two questions require separate verdicts:

1. **Mathematical obligation:** does the stated calculation or reviewed argument satisfy its specified obligation? A PASS is limited to the method listed: exact computation, written reasoning, or source inspection. It is not automatically a kernel-checked theorem.
2. **Animal certification:** does the available package justify a positive result under that animal's existing operation, with a faithful domain mapping, sufficient inputs, a declared acceptance criterion, an actual pinned execution, and closed material risks?

For question 2, PASS requires all six conditions below. Otherwise the binary result is FAIL. A native ranking, category, or non-certification output cannot silently become PASS. **The binary decision belongs to this review's certification wrapper; it is not a changed native animal result.**

| Required condition | Evidence requirement |
| --- | --- |
| Faithful domain bridge | A documented mapping from the proof-audit workflow to the existing operation's input and output semantics. Similar terminology is insufficient. |
| Complete typed inputs | Actual source-compatible records, provenance, and all required measurements. Missing values are not replaced with invented numbers. |
| Acceptance contract | Existing decision rules, or an independently justified rule for a nonbinary output, declared before a new evaluation. |
| Recorded execution | Pinned operation, exact inputs, output, and execution receipt. |
| Criterion satisfied | The observed output satisfies the acceptance contract. |
| Material risks closed | No unresolved risk material to the particular certification claim; this does not require resolving unrelated questions. |

Reason codes: **DOMAIN** = faithful mapping absent; **INPUT** = required evidence absent; **CRITERION** = a positive-output interpretation is not established; **NOT_RUN** = no applicable pipeline execution; **OPEN_RISK** = a declared certification risk remains unresolved. These reasons are preserved even though the public decision column has only PASS or FAIL. An unexecuted gate has unknown native performance, not demonstrated poor performance.

### Direct mathematical and reproducibility obligations

These obligations supplement the Zoo table; they are not renamed animals.

| Obligation and PASS criterion | Method and evidence | Binary result | Evidence status / limit |
| --- | --- | --- | --- |
| Determinant is identically one over F₂ | Exact sparse-polynomial expansion | **PASS** | Demonstrated. |
| Three named distinct inputs share one output | Exact evaluation; distinct coordinates | **PASS** | Demonstrated noninjectivity. |
| All compact, recovery, cubic, derivative, and descent identities agree | Fifteen exact identities in total, including the determinant | **PASS** | Demonstrated finite identities; field/geometry implications need reasoning below. |
| Function-field reconstruction uses nonzero elements | Nonzero polynomial checks plus the displayed rational reconstruction | **PASS** | Written argument reviewed; not a claim about denominators at every affine point. |
| Algebraic independence precedes irreducibility | Algebraicity, transcendence-degree, then irreducibility dependency chain | **PASS** | Supported by reviewed argument and source inspection. |
| Cubic irreducibility holds over the actual target field | Gauss-lemma/coefficient argument and source-level transport inspected | **PASS** | Supported by written argument; no fresh kernel replay. |
| Degree, separability, étaleness, and generic-fiber bridge follow | Field reconstruction, nonzero derivative, Jacobian criterion, embedding bridge | **PASS** | Supported by written argument; no fresh kernel replay. |
| Characteristic and generic-versus-every-fiber limits are respected | Characteristic-zero check and origin-fiber deduction | **PASS** | Demonstrated boundary calculations; not a characteristic-zero result. |
| Checker detects the two declared coefficient mutations | Both mutations break determinant one | **PASS** | Demonstrated sensitivity to these two controls only. |
| Archived source files match supplied manifest | 18/18 SHA-256 entries agree | **PASS** | Demonstrated internal bundle consistency, not external authenticity. |
| Every named auxiliary document is present in the archived bundle | Three referenced documents absent | **FAIL** | Demonstrated packaging gap; no missing Lean import established. |
| This review freshly rebuilds the exact Lean theorem and audits axioms | No local Lean/lake run | **FAIL** | Unresolved certification; not a mathematical refutation. |
| External execution receipts are directly authenticated | Supplied receipt text inspected, remote execution not authenticated | **FAIL** | Unresolved provenance. |
| Exhaustive priority is established | Only the identified predecessor comparison was reviewed | **FAIL** | No exhaustive novelty certification; no plagiarism conclusion. |

## 1. Frozen object and criteria

Target: the user-supplied ten-page PDF, version 1; the corresponding arXiv source archive and ancillary Lean package retrieved in this session. Base field k is the algebraic closure of F₂. The PDF’s overbars can disappear in plain-text extraction; the source and Lean definition resolve that ambiguity. The theorem concerns the separable/Adjamagbo formulation in characteristic two.

```
P = x + x²y + x⁴ + x⁶y²
Q = y + x⁵ + x⁶y + x⁷y² + x⁸y³
F = (P,Q)
```

Frozen audit obligations: (a) exact determinant and collisions; (b) justified function-field denominators and recovery; (c) algebraic independence without assuming degree three; (d) irreducibility over the actual target field; (e) separability; (f) genuine étaleness and geometric-fiber bridge; (g) valid coordinate reduction; (h) source/prose fidelity and reproducibility. Reject a mathematical subclaim only upon an explicit contradiction or invalid inference. Withhold fresh formal-verification certification without a local kernel run. These are audit criteria, not retroactively preregistered experimental criteria.

## 2. What was actually executed

A newly written, dependency-free Python checker implements sparse multivariate polynomials over F₂ using exponent tuples and symmetric-difference addition. It checks identities as polynomials, not by sampling real numbers. Fifteen identity/equality checks and two deliberately changed-coefficient controls passed; three specified collision evaluations agree. The checker also verifies all 18 supplied file digests. A textual scan of 15 Lean files, with comments removed, found no sorry, admit, custom axiom, unsafe, or native_decide tokens. This scan is not a Lean parser or kernel axiom audit.

The independent implementation uses the paper’s claimed formulas as its target. It is computational corroboration with a different small implementation, not independent discovery or human peer review. No model fitting, statistical significance, floating-point tolerance, physics experiment, or randomized null benchmark was needed for these identities.

## 3. Mathematical dissection

### Jacobian and noninvertibility — demonstrated

In characteristic two, Pₓ=1, Pᵧ=x², Qₓ=x⁴+x⁶y², Qᵧ=1+x⁶+x⁸y². Consequently det JF=1. Direct evaluation gives F(0,1)=F(1,0)=F(1,1)=(0,1). The three inputs are pairwise distinct. This establishes noninjectivity and rules out an automorphism. It alone does not establish the additional generic-degree condition.

### The hidden cubic — demonstrated identities

```
r = 1+xy; u = 1+x³r; w = ru²
P = xru; Q = y+x⁵r³
xQ = 1+w; P² = x²rw
PQ+P³ = ru+w²
H(T) = T³+T²+(PQ+P³)T+P³
H(w) = 0
```

Every displayed identity above passes exact polynomial expansion. The auxiliary variable is called r in the PDF but Generic.q in Lean; this is a documented naming difference, not confusion with the output Q.

### Denominators and field reconstruction — demonstrated by argument

x, P, Q, r, u, w are nonzero polynomials. In L=k(x,y), they are legitimate nonzero field elements even though they can vanish at particular affine points. With E=k(P,Q), x=(w+1)/Q, r=P²/(x²w), and y=(r+1)/x show L=E(w). The monic cubic already implies a finite algebraic extension of degree at most three.

This is a function-field argument. It neither requires nor claims that those rational formulas work at every point. Evaluating a denominator at a zero locus and calling that a contradiction would misread the proof.

### Anti-circularity — no cycle found

```
polynomial identities + nonzero denominators
  → L=E(w) and L/E algebraic
  → trdeg(E)=trdeg(L)=2
  → P,Q algebraically independent
  → Q transcendental over k(P)
  → actual-target irreducibility
  → degree exactly 3 and separability
  → three geometric generic-fiber points
```

The important distinction is “at most three” before irreducibility versus “exactly three” afterward. The earlier algebraicity step does not assume irreducibility or the desired exact degree. Inspection of FieldExtension.lean and the terminal assembly confirms this organization at source level.

### Irreducibility — the decisive step survives

Set K=k(P), treating Q as transcendental only after the preceding proof. Write H=H₀+PQT. A nontrivial factorization in K(Q)[T] lifts, by monicity and Gauss’s lemma, to monic positive-T-degree factors in K[Q,T]. Degree one in Q forces one factor R to be independent of Q. Comparing coefficients makes R divide both PT and H₀. Since P is a unit in K, a nonconstant divisor of PT is associated with T; but H₀(0)=P³≠0. Contradiction.

The Lean generic-cubic proof takes a different valid route: a rational root of the monic cubic would be a polynomial in Q dividing the unit constant coefficient P³, hence a constant. Its Q coefficient forces that constant to be zero, which contradicts P³≠0. For a cubic, absence of a root establishes irreducibility. ActualIrreducibility.lean transports this result to the literal intermediate field. The terminal theorem supplies the irreducibility proof; it does not leave it as an unproved hypothesis.

### Degree, separability, geometry — supported by a complete written argument

Since H is the monic irreducible polynomial of w and L=E(w), [L:E]=3. Also H′(w)=ru≠0. Thus the extension is separable. The square graph presentation k[A,B,X,Y]/(P(X,Y)−A,Q(X,Y)−B) has relative Jacobian determinant a unit; the standard Jacobian criterion gives étaleness.

Section 7 separately identifies geometric generic-fiber points with E-embeddings L→Ω. A compatible polynomial-ring map sends w to a root of H, defining an embedding; the recovery identities then force the original x and y images. This closes the bridge from field degree to exactly three generic geometric points. Section 8 also proves coordinate-ring nonsurjectivity directly using the collision, instead of relying on a vague invertibility slogan.

### Structural descent — demonstrated identities

The source permutation and target permutation turn Huq-Kuruvilla’s map into Φ=(x+x²z,y+x²y²,z+xy+x²yz). The polynomial coordinate change a=x, b=z+y², c=x+y+x²b has the displayed polynomial inverse. The target coordinate X+Y equals c. Substituting c=0 yields precisely P(a,b),Q(a,b). The inverse, preserved-coordinate identity, and both plane restrictions passed exact expansion.

## 4. Boundary and falsification tests

**Characteristic matters.** Interpreting the same formulas over the rationals gives determinant 5 at (1,0), not 1. Thus the characteristic-zero extrapolation fails immediately; the paper explicitly excludes it. Likewise, zero is an ordinary algebraic element here, not a physical claim about nonexistence.

**Generic does not mean every fiber.** An additional deduction from the verified identities: the fiber over (0,0) has only (0,0). Indeed Q=0 forces w=1; P=0 gives xru=0. If r=0 or u=0 then w=0, impossible, so x=0 and Q=y forces y=0. This is compatible with a generic degree-three étale map. It also rules out a finite étale degree-three covering of the whole connected target; finite function-field degree must not be conflated with a finite morphism. This deduction is from this review, not a new claim attributed to the author.

**Coefficient mutation controls.** Replacing P by P+x, or Q by Q+y, breaks the determinant-one identity. The checker detects both changes. These are sensitivity controls for the checker; arbitrary coefficient changes leave the theorem’s hypotheses and do not refute it.

## 5. Formal verification and reproducibility

The actual terminal source defines k=AlgebraicClosure(ZMod 2), the fraction field of the source polynomial ring, and the literal intermediate field generated by P,Q. It uses Mathlib’s scheme-level Etale, Module.finrank, Algebra.IsSeparable, Field.finSepDegree, a pullback-defined geometric generic fiber, and IsIso. This is materially stronger than renaming a local Boolean “verified.” The final proof explicitly assembles those predicates.

**Verified here:** 18/18 source/toolchain manifest hashes; presence and inspection of the terminal proposition and proof; selected dependency modules; textual absence of proof escape tokens in all 15 Lean files. The terminal collision conjunction names two inequalities relative to (0,1); it does not explicitly list (1,0)≠(1,1). Those concrete points are plainly distinct, and the separate geometric count is present. This is a harmless presentation observation.

**Reported by the supplied receipts:** original source commit ab26ce21e3b272eec73908d5ed2f8b10117f2e38; Lean 4.28.0 and Mathlib revision 8f9d9cff6bd728b17a24e163c9402775d9e6a365; successful local and Aristotle replays; standard axioms propext, Classical.choice, Quot.sound only. The Aristotle receipt supplies service task identifiers and explains its lake-manifest byte normalization while claiming identical dependency revisions. Hash consistency authenticates correspondence within the bundle; it does not authenticate the remote service’s account of execution.

**Unresolved here:** a fresh local Lean run and direct authentication of external execution records. No Lean/lake executable was found in the current environment; no build was attempted or certified. The full external Mathlib trust chain was not audited. The absence of a rebuild is an audit limitation, not a mathematical counterexample.

**Packaging repair:** the README references CLOSURE_LEDGER.md, PRESERVATION_MANIFEST.md, and source-solution.txt, which are absent from the downloaded ancillary bundle. Include them, or label the references repository-only. The main PDF and FORMALIZATION_MAP.md still provide the argument and declaration mapping; the missing documents were not found among Lean imports.

## 6. Novelty and evidence independence

Huq-Kuruvilla’s earlier arXiv:2607.20968 supplies the three-variable source map. Mondello explicitly credits it and derives a preserved plane fiber. The candidate contribution is the dimension-two construction and its field/geometric proof, not discovery of characteristic-two Jacobian counterexamples in general. The derivative rules, Gauss lemma, separability criterion, and étale criterion are established tools. The paper makes no broader priority claim; this review has not established exhaustive historical priority.

Lean and Aristotle are distinct execution environments according to the receipts, but both check the same source through the Lean kernel and pinned dependencies. That helps detect environment/replay errors, not independently validate the translation of a literature conjecture or eliminate shared-library assumptions. The exact algebra checker supplies a separate implementation of the finite identities; human-level mathematical review remains a different evidence stream.

## 7. Every animal: binary certification verdict

Frozen reference: [Monolithic-Zoo-Lean4, commit 509480eb63d9fa2ca89f17506793a1f9412d2439](https://github.com/enuminous/Monolithic-Zoo-Lean4/tree/509480eb63d9fa2ca89f17506793a1f9412d2439). The recoverable roster is 46 main operations plus five extensions. The repository formalizes selected kernels; 17 rank-aggregation animals still require external feature extraction. Its own coverage documentation warns that caller-supplied evidence flags do not establish the truth of those flags.

The purpose, transformation, and output domain in each row remain those of the published kernel. Section 0 defines the common binary certification rule. For every main-roster row, the current result is **FAIL [DOMAIN, INPUT, CRITERION, NOT_RUN]**: no faithful measured proof-workflow adapter, complete inputs, accepted positive-result contract, or run has been supplied. The final column specifies the missing evidence needed even to begin that evaluation; supplying it would not guarantee a PASS.

| Animal | Existing transformation / output domain | Binary certification | Required evidence absent from this package |
| --- | --- | --- | --- |
| 1. TORTOISE | ordered split; temporal separation contract; Brier gain | **FAIL** | Timestamped prediction/label records, ordered split, leakage checks, and measured Brier gain. |
| 2. OWL | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 3. OCTOPUS | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 4. GECKO | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 5. HIVE | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 6. EAGLE | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 7. CRAB | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 8. SHEPHERD | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 9. PULSE | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 10. CAT | ablation penalty and sign classifier; exact-integer sign reference | **FAIL** | Measured full-versus-ablated scores and the source penalty/sign inputs; deleting a theorem hypothesis is not a measured ablation. |
| 11. FOX | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 12. SPIDER | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 13. RAVEN | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 14. DOLPHIN | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 15. ANT | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 16. MOTH | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 17. SHARK | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 18. PENGUIN | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 19. BAT | verdict kernel with source placebo precedence; fitting excluded | **FAIL** | Source-compatible fitted and placebo results with their provenance; a polynomial coefficient mutation is not a placebo experiment. |
| 20. HEDGEHOG | generalization verdict and environment separation obligation; training excluded | **FAIL** | Separate training and evaluation environments, generalization measurements, and the environment-separation contract. |
| 21. CROCODILE | difference-in-differences kernel and conditional identification contract | **FAIL** | Treatment/control and pre/post outcomes plus an independently justified identification contract. |
| 22. DRAGON | rank aggregation of precomputed component columns; feature extraction and model training not ported | **FAIL** | Animal-specific precomputed component columns with documented extraction, a frozen reporting contract, and an independently justified acceptance rule. A rank alone is not a proof verdict. |
| 23. TURTLE | summary verdict and veto precedence; group normalization supplied | **FAIL** | Source summary metrics, supplied group normalization, and all veto inputs. |
| 24. MAGPIE | groundedness and history-dependent alarm; entropy/storage excluded | **FAIL** | Groundedness evidence and ordered alarm history in the source schema. |
| 25. WOLF | local channel contribution, weight, EMA and alarm contract; graph aggregation supplied | **FAIL** | Channel contributions, weights, EMA history, and graph aggregation inputs. |
| 26. ELEPHANT | active-event filter and fuel-bounded lineage abstraction; full memory API excluded | **FAIL** | Typed active events, parent links, and declared traversal fuel; citations alone do not instantiate the event model. |
| 27. CHAMELEON | unexplained/noise-adjusted excess; supplied centroid distances | **FAIL** | Measured excess/noise inputs and justified reference-centroid distances. |
| 28. JELLYFISH | dynamic edge weight, flow, next health and harm; graph aggregation supplied | **FAIL** | Typed graph edges, flows, weights, and health/harm observations. |
| 29. BEAVER | acceptance contract including bounds and rollback flags; external repair not certified | **FAIL** | A concrete repair candidate, acceptance bounds, and observed rollback/invariant checks. |
| 30. MANTIS | calibrated z-score aggregation and state decision; baseline fitting supplied | **FAIL** | Fitted baseline, calibrated component z-scores, and source decision inputs. |
| 31. BISON | single-component queue transition; exact natural-number capacity bound | **FAIL** | A specified queue, arrival/service trace, capacity, and transition records. |
| 32. WEASEL | bounded finding filter; target search/enumeration remains external | **FAIL** | A declared search space, enumerated candidate findings, filter inputs, and fuel/bounds; narrative review is not a bounded search certificate. |
| 33. SALMON | unresolved-mass kernel and fuel-bounded trace abstraction; weighted tracing excluded | **FAIL** | A typed provenance trace with unresolved masses and fuel; counts of missing documents are not the weighted trace. |
| 34. ORCA | handoff checks and aggregate coordination formula; pairwise metrics supplied | **FAIL** | Recorded handoffs and independently measured pairwise coordination inputs. |
| 35. MOLE | observability gap and coverage-gated hidden-failure flag; indicators supplied | **FAIL** | Declared observable coverage and hidden-failure indicators; a missing Lean run is not a calibrated hidden-failure signal. |
| 36. LYNX | novelty, yield and emergence contract; reference distances supplied | **FAIL** | A frozen reference corpus, reference distances, and measured discovery yield; priority discussion is not the kernel input. |
| 37. HORSE | trust/workload/joint-effectiveness kernels and handoff contract | **FAIL** | Measured trust, workload, joint-effectiveness, and handoff inputs. |
| 38. TERMITE | agent update and synchronous mapping; graph weighted inputs supplied | **FAIL** | Agent states, synchronous updates, and graph-weighted inputs. |
| 39. PHOENIX | recovery completeness and hold-window predicate; fidelity inputs supplied | **FAIL** | Observed failure/recovery trajectory, fidelity measures, and a declared hold window. |
| 40. COBRA | persistent/proxy divergence and risk kernels; deltas supplied | **FAIL** | Measured persistent/proxy deltas and risk inputs; prose overclaim checking is not the native divergence calculation. |
| 41. WHALE | cumulative deviation, history gap and stability formula; slope supplied | **FAIL** | A time history of deviations, history gaps, and independently supplied slope. |
| 42. FALCON | latency/missed/reaction-margin kernel; streaming threshold monitor excluded | **FAIL** | Observed event/detection times, missed-event labels, and reaction margin. |
| 43. RHINO | retention, amplification and graceful-failure kernels; invariants supplied | **FAIL** | A frozen stress protocol, measured invariant retention/amplification, and graceful-failure records. |
| 44. BONOBO | gain, exploitation and cooperation score; dispersion supplied | **FAIL** | Measured cooperation gains, exploitation, and dispersion inputs. |
| 45. AXOLOTL | recovery, efficiency and resilience; transformation/invariants supplied | **FAIL** | A specified transformation and observed recovery/efficiency/invariant measurements. |
| 46. BUTTERFLY | layer update, amplification and bounded trajectory; graph comparison excluded | **FAIL** | Layer states, update parameters, amplification measurements, and trajectory bounds. |

### Five extensions

| Extension | Existing transformation / output domain | Binary certification | Evidence and failure reason |
| --- | --- | --- | --- |
| CIRCUS | Declared pipeline, dependencies, risks, and independent checks → ordered report gate | **FAIL** | **OPEN_RISK.** Pinned `decide()` re-executed on the explicit report below; native output is FAIL because fresh local formal replay is an unresolved material certification risk. The supplied independent-check flag is also false; this does not claim the algebra checks failed. |
| MONSTER / Zoo-Monster | Preregistered matched-comparator performance envelope, perturbations, and boundaries → eligibility/violation gate | **FAIL** | **DOMAIN, INPUT, CRITERION, NOT_RUN.** No measured performance envelope for a defined proof-audit service, matched comparator, tolerances, and registered boundary trials. Two polynomial mutations do not supply those data. |
| WOODPECKER | Validated candidate/comparator metrics and thresholds → ordered decision | **FAIL** | **DOMAIN, INPUT, CRITERION, NOT_RUN.** No independently validated comparator metrics and source-compatible frozen thresholds. A true algebraic identity is not a performance improvement measurement. |
| NIGHTINGALE / Nightengale | Numerical responses, predictions, quantiles, and stopping conditions → partition/growth decisions | **FAIL** | **DOMAIN, INPUT, CRITERION, NOT_RUN.** No fitted-response dataset, valid prediction functions, or accepted interpretation of tree output as certification. The formalized branch projection is not the full numerical pipeline. |
| CHIMERA | Classical/quantum/key/recovery/feedback declarations → ordered record tags | **FAIL** | **DOMAIN, INPUT, CRITERION, NOT_RUN.** No independently supported source-domain record declarations or justified acceptance interpretation for the returned tags. Algebraic field reconstruction does not establish a physical recovery record. |

The earlier restricted CIRCUS no-cycle case returned native N/A because independence was not established. Under this edition's binary wrapper that case also fails certification. That historical native output remains part of the audit trail; it has not been changed to a native FAIL. CIRCUS checks the consistency of reviewer declarations, not their truth.

**Execution accounting:** one extension's native gate executed for this revision; 50 other native operations not run on a valid case. All 51 wrapper decisions were computed from the declared evidence records. There are no native performance results for those 50 operations. The aggregate means “no positive Zoo certification is supported by this package,” not “the paper is false.”

### Reframing the paper into an evaluable workflow

A substantive full-Zoo experiment would study **how a proof-audit system detects, explains, repairs, and reproduces valid and invalid proof packages**. That is a new empirical claim about a review workflow, separate from Mondello's theorem. This paper can provide one case; it cannot alone establish generalization or benchmark superiority.

A prospective design would:

1. Preserve this versioned paper as a seed case. Build an independently labeled corpus of valid packages and documented defects, with the reference judgments and source lineage recorded. Assign related mutations to the same split to avoid leakage.
2. Freeze each animal's actual input adapter and acceptance contract before running new evaluations. Rank-producing animals need their own documented component extraction; numerical and temporal animals need real measurements, not prose converted to arbitrary scores.
3. Instrument audit events, tool calls, failures, repairs, provenance edges, handoffs, latency, and resource use only where they instantiate the relevant native schema. State the assumptions that make each mapping legitimate.
4. Use matched review budgets and conventional comparators. Measure error detection and false accusations against independent labels; include missing-evidence cases without treating them as mathematical counterexamples.
5. Record the exact native outputs, then apply this binary wrapper. If an animal's domain still has no faithful mapping, it continues to FAIL certification. No experiment should be invented merely to make the coverage count look complete.

This is a proposed design, not a completed experiment or a claimed executable adapter. It would evaluate the audit system, not supply a replacement proof of the theorem. For the mathematical claim, the highest-value next step remains the pinned Lean replay in §8.

### Executed binary policy and CIRCUS input

CIRCUS source: [enuminous/Circus, pinned src/circus.py](https://github.com/enuminous/Circus/blob/647c91dc06b4ea48871c06608298b46f00f68f99/src/circus.py), Git blob `65421922766c9178c1b188703ac21c03f95be6dd`, verified against the local file before this execution.

The following policy was executed over all 51 evidence records. It deliberately does not substitute for a native animal implementation. `False` means the required affirmative evidence has not been established; it does not encode a measured negative performance score.

```python
FIELDS = ("bridge", "inputs", "acceptance", "executed", "satisfied",
          "no_open_material_risk")

def certify(record):
    return "PASS" if all(record[k] is True for k in FIELDS) else "FAIL"

# Main 46 + CHIMERA, MONSTER, WOODPECKER, NIGHTINGALE:
# no validated evidence adapter or applicable recorded evaluation.
missing_evidence_record = {k: False for k in FIELDS}

# CIRCUS alone has a typed gate invocation on reviewer declarations.
circus_record = dict(bridge=True, inputs=True, acceptance=True,
                     executed=True, satisfied=False,
                     no_open_material_risk=False)
assert certify(missing_evidence_record) == "FAIL"
assert certify(circus_record) == "FAIL"
# Audit assertion across the 51 named records: PASS=0, FAIL=51.
```

Exact CIRCUS input for the re-executed fresh-certification gate:

```json
{
  "animal": "CIRCUS",
  "pipeline": [
    {
      "stage": "definition",
      "provenance_status": "documented"
    },
    {
      "stage": "data_selection",
      "provenance_status": "documented"
    },
    {
      "stage": "labels",
      "provenance_status": "documented"
    },
    {
      "stage": "scoring",
      "provenance_status": "documented"
    },
    {
      "stage": "validation",
      "provenance_status": "documented"
    }
  ],
  "dependencies": [],
  "risks": [
    {
      "description": "Fresh local Lean/kernel replay remains unperformed.",
      "materiality": "material",
      "status": "unresolved"
    }
  ],
  "independent_checks": [
    {
      "name": "Exact F2 polynomial identities",
      "status": "passed",
      "frozen": true,
      "independently_sourced": false
    }
  ]
}
```

Observed native output: `FAIL`. Observed certification wrapper output: `FAIL`. All provenance flags in that input are reviewer declarations about this report; the implementation does not authenticate provenance. The polynomial identities were the frozen target of the original checker; `frozen: true` does not claim statistical preregistration or independent source discovery.

## 8. Surviving claims and next gate

| Claim | Assessment |
| --- | --- |
| Determinant one, explicit collision, compact/recovery/cubic identities and descent | DEMONSTRATED by exact recomputation. |
| Exact degree three, separability, étaleness, geometric fiber, nonautomorphism | Written mathematical argument survives; source-level support inspected. Fresh kernel reproduction remains incomplete. |
| Source corresponds to its manifest | DEMONSTRATED: 18/18 entries match. |
| Fresh independent Lean verification in this session | UNRESOLVED; not performed. |
| Classical characteristic-zero refutation or EFMW physics validation | REJECTED extrapolations; neither is claimed by this paper. |
| Exhaustive novelty / independent human peer review | UNRESOLVED; no such certification supplied here. |

**Minimal next test, criteria fixed now:** recreate the archived Lean 4.28.0 environment with the manifest’s exact dependency revisions, verify hashes, rebuild the GeometricBridge target, FinalTheorem target, root library, and run KernelAudit.lean. Success requires all commands to exit zero without source edits, the exact FullCounterexampleStatement, and no axioms beyond propext, Classical.choice, Quot.sound. A changed theorem, admitted obligation, extra axiom, or reproducible kernel error fails this verification gate. Network/cache/toolchain availability errors remain infrastructure blockers, not mathematical refutations. Authenticating the Aristotle result is a separate provenance task.

**Questions for Romy:** Can you publish a clean exact-revision CI replay and its raw axiom output? Can you include or remove the three missing documentation references? Can a reviewer access the original Aristotle audit output rather than only its summary? These are concrete closure requests; this audit found no reason to demand a replacement of the central proof.

## 9. Sources and audit receipts

- [Romy Mondello, arXiv:2608.02634v1](https://arxiv.org/pdf/2608.02634v1), all ten pages, especially §§3–7 and Appendix A.

- [Versioned arXiv source archive](https://arxiv.org/src/2608.02634v1); ancillary Lean package inspected directly.

- [Huq-Kuruvilla, earlier three-variable construction](https://arxiv.org/abs/2607.20968), primary-source abstract for provenance comparison.

- [Frozen Zoo reference](https://github.com/enuminous/Monolithic-Zoo-Lean4/tree/509480eb63d9fa2ca89f17506793a1f9412d2439): README, Registry.lean, coverage.json, EXTENSION_COVERAGE.md, extension-sources.json.

### Machine-readable results

```
{
  "checks": {
    "Jacobian determinant": true,
    "P compact": true,
    "Q compact": true,
    "Recovery x": true,
    "Recovery r": true,
    "PQ+P^3": true,
    "Hidden cubic root": true,
    "Derivative at root": true,
    "Elimination cubic": true,
    "Recovery y": true,
    "Coordinate inverse b": true,
    "Coordinate inverse c": true,
    "Preserved coordinate": true,
    "Plane restriction P": true,
    "Plane restriction Q": true,
    "Mutation P+x caught": true,
    "Mutation Q+y caught": true
  },
  "collisions": {
    "(0, 1, 0)": [
      0,
      1
    ],
    "(1, 0, 0)": [
      0,
      1
    ],
    "(1, 1, 0)": [
      0,
      1
    ]
  },
  "digests": {
    "DimensionTwoCounterexample.lean": true,
    "DimensionTwoCounterexample/ActualIrreducibility.lean": true,
    "DimensionTwoCounterexample/Certificate.lean": true,
    "DimensionTwoCounterexample/CounterexampleStatement.lean": true,
    "DimensionTwoCounterexample/DegreeFromIrreducible.lean": true,
    "DimensionTwoCounterexample/EtalePresentation.lean": true,
    "DimensionTwoCounterexample/FieldExtension.lean": true,
    "DimensionTwoCounterexample/FinalElementary.lean": true,
    "DimensionTwoCounterexample/FinalTheorem.lean": true,
    "DimensionTwoCounterexample/GenericCertificate.lean": true,
    "DimensionTwoCounterexample/GenericCubicIrreducible.lean": true,
    "DimensionTwoCounterexample/GeometricBridge.lean": true,
    "DimensionTwoCounterexample/Reconstruction.lean": true,
    "DimensionTwoCounterexample/Structural.lean": true,
    "KernelAudit.lean": true,
    "lake-manifest.json": true,
    "lakefile.toml": true,
    "lean-toolchain": true
  },
  "source_scan_hits": {},
  "source_scan_limit": "Textual scan, not Lean parsing or axiom audit",
  "lean_rebuilt": false,
  "pdf_sha256": "b6933e8dc2238cc46aac5b96727cc01ae97ee4b178d691cf65ff175dc8d6a86e",
  "source_archive_sha256": "ae12bc3c553094f26fb739317fcec610f1a67aefbf2481769810aa8f440094fa"
}
```

### Reproduction checker (Python standard library)

Run from a directory containing upload/2608.02634v1.pdf; extract the versioned arXiv source into /tmp/mondello-source and save its archive as /tmp/mondello-source.tar. This checker does not compile Lean.

```
import json, hashlib, pathlib, re
# Exact sparse polynomials over F_2 in x,y,z: addition is symmetric difference.
class P:
 def __init__(self,s=()): self.s=frozenset(s)
 def __add__(a,b): return P(a.s^b.s)
 def __mul__(a,b):
  s=set()
  for u in a.s:
   for v in b.s:
    w=tuple(i+j for i,j in zip(u,v))
    if w in s:s.remove(w)
    else:s.add(w)
  return P(s)
 def __pow__(a,n):
  r=one
  for _ in range(n):r=r*a
  return r
 def d(a,i):
  s=[]
  for e in a.s:
   if e[i]%2:
    t=list(e);t[i]-=1;s.append(tuple(t))
  return P(s)
 def at(a,*vals):return sum(__import__('functools').reduce(lambda a,b:a*b,[v**e for v,e in zip(vals,t)],1) for t in a.s)%2
 def __eq__(a,b):return a.s==b.s
zero=P();one=P([(0,0,0)]);x=P([(1,0,0)]);y=P([(0,1,0)]);z=P([(0,0,1)])
p=x+x**2*y+x**4+x**6*y**2
q=y+x**5+x**6*y+x**7*y**2+x**8*y**3
r=one+x*y;u=one+x**3*r;w=r*u**2
checks={}
def check(n,a,b):checks[n]=a==b;assert a==b,n
check('Jacobian determinant',p.d(0)*q.d(1)+p.d(1)*q.d(0),one)
check('P compact',p,x*r*u);check('Q compact',q,y+x**5*r**3)
check('Recovery x',x*q,one+w);check('Recovery r',p**2,x**2*r*w)
check('PQ+P^3',p*q+p**3,r*u+w**2)
check('Hidden cubic root',w**3+w**2+(p*q+p**3)*w+p**3,zero)
check('Derivative at root',w**2+p*q+p**3,r*u)
check('Elimination cubic',q**2*x**3+(p**3+p*q+one)*x+p,zero)
check('Recovery y',x*y,r+one)
collisions={str(v):(p.at(*v),q.at(*v)) for v in [(0,1,0),(1,0,0),(1,1,0)]}
assert len(set(collisions.values()))==1 and next(iter(collisions.values()))==(0,1)
# Source coordinate inverse for section 10, with (a,b,c) represented by (x,y,z).
yy=z+x+x**2*y;zz=y+yy**2
check('Coordinate inverse b',zz+yy**2,y)
check('Coordinate inverse c',x+yy+x**2*(zz+yy**2),z)
X=x+x**2*zz;Y=yy+x**2*yy**2;Z=zz+x*yy+x**2*yy*zz
check('Preserved coordinate',X+Y,z)
def restrict(f):return P(e for e in f.s if e[2]==0)
check('Plane restriction P',restrict(X),p);check('Plane restriction Q',restrict(Z),q)
assert all(v.s for v in [x,p,q,r,u,w])
# Mutation controls: changing a coefficient is not a new conjecture test.
check('Mutation P+x caught',(p+x).d(0)*q.d(1)+(p+x).d(1)*q.d(0)==one,False)
check('Mutation Q+y caught',p.d(0)*(q+y).d(1)+p.d(1)*(q+y).d(0)==one,False)
root=pathlib.Path('/tmp/mondello-source/anc/lean')
digests={}
for line in (root/'SOURCE_DIGESTS.sha256').read_text().splitlines():
 if line.strip():
  h,f=line.split(maxsplit=1);digests[f]=hashlib.sha256((root/f).read_bytes()).hexdigest()==h
assert all(digests.values())
hits={}
for f in root.rglob('*.lean'):
 s=f.read_text();s=re.sub(r'/\-.*?\-/','',s,flags=re.S);s=re.sub(r'--[^\n]*','',s)
 found=re.findall(r'\b(sorry|admit|axiom|unsafe|native_decide)\b',s)
 if found:hits[str(f.relative_to(root))]=found
out={'checks':checks,'collisions':collisions,'digests':digests,'source_scan_hits':hits,'source_scan_limit':'Textual scan, not Lean parsing or axiom audit','lean_rebuilt':False,'pdf_sha256':hashlib.sha256(pathlib.Path('upload/2608.02634v1.pdf').read_bytes()).hexdigest(),'source_archive_sha256':hashlib.sha256(pathlib.Path('/tmp/mondello-source.tar').read_bytes()).hexdigest()}
pathlib.Path('/tmp/mondello-results.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
```
