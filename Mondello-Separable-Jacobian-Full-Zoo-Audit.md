# Monolithic Zoo dissection: Romy Mondello · arXiv:2608.02634v1

The mathematical counterexample survives this audit. Exact polynomial checks pass; the written proof has a coherent, noncircular dependency chain. Fresh local Lean certification remains unresolved.

**Prepared for Matthew Chenoweth Wright, Monolithic LLC, with AI-assisted analysis.**

Audit date: October 26, 2026. This is a complete roster applicability review plus substantive mathematical, source, and provenance analysis. It is not a claim that 46 empirical pipelines executed on a PDF. No percentage “truth score” is assigned.

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

## 7. Full Zoo roster: scope before scoring

Frozen reference: Monolithic-Zoo-Lean4 commit 509480eb63d9fa2ca89f17506793a1f9412d2439. Its registry contains 46 main animals and documents five extension decision procedures separately. This is the recoverable operational roster, not an assumed 52-name list. The current coverage warns that these are selected kernels, including 17 rank-aggregation modules with feature extraction outside the formalization.

For each row below, the scope is the actual published operation. Its input contract and success criterion govern applicability; no metaphorical reassignment is made. This paper asserts an exact algebraic theorem, not the predictive, temporal, queueing, repair, or cooperation property measured by these kernels. Therefore main-roster outputs are N/A for this target. They are not passes, and no denominator is silently reduced into a flattering score. Missing evidence for the *formal-replay claim* is separately UNRESOLVED, never disguised as N/A.

| Animal | Published kernel / required domain | Output / criterion for this paper |
| --- | --- | --- |
| 1. TORTOISE | ordered split; temporal separation contract; Brier gain | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 2. OWL | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 3. OCTOPUS | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 4. GECKO | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 5. HIVE | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 6. EAGLE | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 7. CRAB | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 8. SHEPHERD | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 9. PULSE | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 10. CAT | ablation penalty and sign classifier; exact-integer sign reference | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 11. FOX | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 12. SPIDER | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 13. RAVEN | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 14. DOLPHIN | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 15. ANT | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 16. MOTH | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 17. SHARK | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 18. PENGUIN | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 19. BAT | verdict kernel with source placebo precedence; fitting excluded | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 20. HEDGEHOG | generalization verdict and environment separation obligation; training excluded | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 21. CROCODILE | difference-in-differences kernel and conditional identification contract | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 22. DRAGON | rank aggregation of precomputed component columns; feature extraction and model training not ported | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 23. TURTLE | summary verdict and veto precedence; group normalization supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 24. MAGPIE | groundedness and history-dependent alarm; entropy/storage excluded | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 25. WOLF | local channel contribution, weight, EMA and alarm contract; graph aggregation supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 26. ELEPHANT | active-event filter and fuel-bounded lineage abstraction; full memory API excluded | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 27. CHAMELEON | unexplained/noise-adjusted excess; supplied centroid distances | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 28. JELLYFISH | dynamic edge weight, flow, next health and harm; graph aggregation supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 29. BEAVER | acceptance contract including bounds and rollback flags; external repair not certified | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 30. MANTIS | calibrated z-score aggregation and state decision; baseline fitting supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 31. BISON | single-component queue transition; exact natural-number capacity bound | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 32. WEASEL | bounded finding filter; target search/enumeration remains external | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 33. SALMON | unresolved-mass kernel and fuel-bounded trace abstraction; weighted tracing excluded | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 34. ORCA | handoff checks and aggregate coordination formula; pairwise metrics supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 35. MOLE | observability gap and coverage-gated hidden-failure flag; indicators supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 36. LYNX | novelty, yield and emergence contract; reference distances supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 37. HORSE | trust/workload/joint-effectiveness kernels and handoff contract | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 38. TERMITE | agent update and synchronous mapping; graph weighted inputs supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 39. PHOENIX | recovery completeness and hold-window predicate; fidelity inputs supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 40. COBRA | persistent/proxy divergence and risk kernels; deltas supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 41. WHALE | cumulative deviation, history gap and stability formula; slope supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 42. FALCON | latency/missed/reaction-margin kernel; streaming threshold monitor excluded | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 43. RHINO | retention, amplification and graceful-failure kernels; invariants supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 44. BONOBO | gain, exploitation and cooperation score; dispersion supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 45. AXOLOTL | recovery, efficiency and resilience; transformation/invariants supplied | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |
| 46. BUTTERFLY | layer update, amplification and bounded trajectory; graph comparison excluded | N/A — no claim or typed dataset in this operation’s domain; not executed. No scientific pass inferred. |

### Extensions

| Operation | Inputs, transformation, criterion | Result |
| --- | --- | --- |
| CIRCUS | Declared provenance/dependencies/risks/checks → ordered report gate. Material unresolved risks veto certification; a complete frozen independent check set is required for PASS. | Executed pinned decide() twice. Fresh-verification certification: FAIL because local replay is explicitly unresolved. Restricted no-cycle report: N/A because source independence is not established. Neither output rejects the mathematical theorem. |
| MONSTER | Preregistered matched baseline, metric tolerance, registered perturbations and failure boundaries → performance-envelope gate. | N/A; this is no empirical performance claim. Algebraic coefficient controls above are not relabeled a preregistered MONSTER experiment. |
| WOODPECKER | Validated candidate/comparator metrics and exact thresholds → ordered threshold decision. | N/A; no comparator-performance claim. |
| NIGHTINGALE | Numerical data, prediction functions, quantiles and recursive stopping conditions → partition/growth decisions. | N/A; no fitted-response tree claim. |
| CHIMERA | Classical/quantum/key/recovery/feedback record declarations → ordered record tags. | N/A; no physical observation or recovery mechanism is asserted. |

CIRCUS source pin: enuminous/Circus 647c91dc06b4ea48871c06608298b46f00f68f99, src/circus.py, retrieved via the Zoo’s extension-sources.json. Inputs were conservative reviewer declarations, not measurements. The gate checks those declarations’ logic; it cannot establish their truth. No Zoo-wide percentage or alternative limiter classification is manufactured.

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
