# Quantum Math the Greek Way: Music of the Spheres

**Matthew Chenoweth Wright · Monolithic LLC**  
**October 30, 2026 · Research proposal and bounded geometric reconstruction · Version 0.1**

**Status:** A geometric reconstruction of a restricted interference rule, conditional on explicitly added physical postulates. This is not a derivation of quantum mechanics from ancient Greek philosophy, a claim that the Greeks possessed quantum theory, or a report of new experimental evidence.

## Abstract

Can a mathematical language built around unity, multitude, positive magnitude, proportion, and geometric construction express quantum behavior without numerical zero? We distinguish a restriction on notation from a restriction on mathematical operations and from a claim about what exists. Within a deliberately restricted, Greek-inspired object-language, oriented segment constructions can express reinforcement, opposition, and exact closure. Squares on resultant segments supply positive outcome weights; a closed construction is handled by an exclusion judgment rather than a magnitude called zero. We give a conditional two-output construction whose geometric proportions reproduce the balanced two-path interference pattern. Its physical interpretation requires new rules for coherent alternatives, outcome weights, and distinguishable records. These are declared postulates, not consequences of Euclid or Parmenides. The construction establishes a limited expressive possibility while identifying the remaining obligations: quantum measurement, composition of systems, dynamics, and empirical discrimination from classical wave models. The Music of the Spheres repository provides a historical and formal research setting; its existing Lean declarations do not yet formalize the construction proposed here.

## The question and the historical boundary

“Nonexistence is not a state” motivates the project. It does not by itself determine a physical theory.

Here, **Greek cognition** means a selected discipline of reasoning through constructions and relations among admitted magnitudes. It does not mean that all Greek thinkers shared one ontology. An Eleatic argument about being, Euclidean proportion, harmonic traditions, and later astronomical models cannot simply be assembled and attributed to a single historical school.

Euclid distinguishes a unit from the multitude composed of units in Book VII, Definitions 1–2 [1]. Book V offers a way to compare proportions through equimultiples without treating every ratio as a modern numerical object [2]. Those resources motivate our choice of language. They do not contain the quantum interpretation introduced below.

The title therefore names a contemporary research exercise: how much of a quantum calculation can be reconstructed under a Greek-inspired cognitive constraint? It does not announce the recovery of a lost ancient quantum theory.

The project has two layers:

- **Native construction layer:** points, nondegenerate segments, angles, circles, squares, positive magnitudes, proportions, and judgments about admissibility or closure.
- **External audit layer:** contemporary logic, software, historical criticism, and comparison with quantum predictions.

An external verifier may use ordinary modern mathematics. Its use does not establish that the native construction secretly had those historical foundations. Conversely, writing modern algebra in Greek vocabulary would not satisfy the intended constraint.

## Three meanings of “without zero”

The distinction is essential.

| Restriction | Meaning | Consequence |
|---|---|---|
| No numerical-zero expression | The native language has no numeral or magnitude designated as numerical zero | Interference can still be described through geometric closure |
| No vanishing or exclusion relation | Coincident endpoints, complete cancellation, and excluded outcomes are all forbidden | The construction below cannot reproduce exact dark outcomes |
| No nonexistent physical substance | A failed outcome is not a thing occupying a special state | Compatible with describing a real apparatus that excludes that outcome |

This paper adopts the first and third restrictions. It does not adopt the second.

We do not call a coincident pair of endpoints a positive segment. When a construction returns to its starting point, the result is a **closure judgment**, not a newly admitted magnitude.

This preserves an important distinction: eliminating a numeral does not eliminate the mathematical role usually expressed by that numeral. The closure relation retains the role of exact cancellation. We disclose that role rather than presenting renamed cancellation as a new physical discovery.

## An admitted construction language

Begin with a plane in which segments can be copied, joined, bisected, and compared, and squares can be constructed upon nondegenerate segments. Orientation is specified by an ordered pair of endpoints; it is not a signed numerical length.

For two contributions, carry out the following construction:

1. Draw a segment from A to B.
2. Starting at B, copy the second contribution with its assigned orientation, ending at C.
3. If C differs from A, take AC as the resultant segment.
4. If C coincides with A, record closure.

This head-to-tail rule is a contemporary definition using geometric operations. We do not attribute a general quantum-amplitude calculus to Euclid.

For nonclosed constructions, compare the squares on resultant segments. Squares supply areas of the same kind, so their relative sizes can be expressed as proportions. The physics has not yet entered: these are relations among constructed figures.

### Reinforcement

When equal contributions continue in the same direction, their resultant is twice either original length. The square on the resultant is four times the square on an original contribution.

### Opposition

When equal contributions face opposite ways, the second ends where the first began. The construction closes. Neither original contribution is declared nonexistent.

### Oblique meeting

Between those cases, the resultant depends on the angle. Euclid's Book II, Propositions 12–13 relates squares on triangle sides through rectangles associated with projections [3,4]. These provide historical geometric resources for treating oblique constructions without signed coordinates or a numerical cosine.

This is already enough to describe reinforcement and cancellation geometrically. It does not distinguish quantum phenomena from classical waves.

## A conditional balanced two-output construction

A single square weight does not yet define a probability distribution. We therefore specify two outputs and their common comparison magnitude.

Take two equal positive segments meeting at a common initial point. Let their outer endpoints be B and C. Complete their parallelogram, with opposite vertex D.

Associate one output with the diagonal AD and the other with BC. When one diagonal closes, assign that output an exclusion judgment; do not construct a square on a degenerate segment.

For a nondegenerate parallelogram, its two diagonal squares together equal four squares on either original equal side. This follows by applying the right-triangle square relation to the halves of the diagonals of the resulting rhombus. The collinear boundary cases are handled separately by reinforcement and closure, without pretending they are nondegenerate rhombi.

**Common comparison magnitude:** four squares on an original side.

**Proposed output weight:** the proportion of a diagonal's square to that common magnitude. A closed output is excluded; the other accounts for the whole.

The construction gives the following exact cases:

| Relative orientation of the equal contributions | First output | Second output |
|---|---|---|
| Same direction | Whole comparison magnitude | Excluded by closure |
| Right angle | Half the comparison magnitude | Half the comparison magnitude |
| Opposite directions | Excluded by closure | Whole comparison magnitude |

For intermediate orientations, the proportions vary continuously if a continuous family of rotations is admitted. That continuity is an additional mathematical setting; a finite straightedge-and-compass construction repertoire alone does not supply every possible rotation.

A common rotation of the entire figure preserves the output proportions. Exchanging the labels of the two contributions also preserves them. Thus the response depends on their relative arrangement, rather than an arbitrary orientation of the drawing.

These statements are geometric consequences of the construction. Identifying them with detection frequencies is a separate step.

## Where the quantum assumptions enter

The following are **new physical postulates**, not historical conclusions.

**Coherent-alternative postulate.** When two experimental paths are not distinguished by an effective path record, assign them contributions that compose by the specified segment construction. Path settings determine their relative orientations.

**Square-weight postulate.** In repeated trials of an ideal balanced two-output apparatus, relative detection frequencies follow the square-area proportions defined above. Each trial supplies a single outcome.

**Distinguishable-record postulate.** When the apparatus carries effectively distinguishable path records and those records are ignored, combine the separate path outcome weights rather than coherently joining their contributions. For the symmetric apparatus, this gives equal output proportions independent of the relative path setting.

The last postulate is not a claim that a human must look. It concerns the physical distinguishability of records. A complete account would have to construct the joint system, its record degrees of freedom, and the rule for disregarding them. That account is absent here.

Standard quantum theory combines coherent alternative amplitudes before taking their squared magnitude; it treats distinguished alternatives differently [5,6]. Our geometric postulates reproduce a limited version of that structure. They do not derive it from the prohibition on non-being.

Nor does the geometry fix which experimental change produces which rotation. Path-length, wavelength, apparatus phase shifts, and their calibration require physical laws or measured inputs.

## What has been obtained—and what has not

The positive result is specific:

> Equal oriented contributions, geometric composition, closure judgments, and proportions of squares can express a balanced two-path interference rule without introducing a numerical-zero object into the native language.

The result is conditional on the declared language and construction rules. It is a paper derivation, not a newly machine-checked theorem.

The physical conclusion is narrower:

> If the added correspondence and frequency postulates are accepted, the construction matches the ideal balanced two-output interference proportions.

Classical coherent fields can exhibit the same intensity pattern. Consequently, matching that pattern alone would not establish a quantum theory. A quantum account must also justify its single-event statistics and address tests beyond classical interference.

Several essential obligations remain:

| Obligation | Present status |
|---|---|
| Geometric reinforcement, opposition, and balanced area comparison | Derived here at the level of an ordinary geometric argument |
| Rule connecting square proportions to frequencies | Postulated |
| Physical assignment of relative orientations | Unspecified beyond calibrated input |
| Discrete energy exchange | Not derived |
| Dynamics, including a rule governing change with time | Not supplied |
| Spin and transformations of spin states | Not supplied; planar arrows alone are insufficient [7] |
| Joint systems, entanglement, and Bell-test correlations | Not supplied |
| Measurement and record composition | Restricted operational postulate only |
| Empirical distinction from existing quantum theory | No different prediction established |

Harmonic modes do not close these gaps. Classical resonators also have distinct allowed modes. A mode catalogue does not derive quantized energy exchange.

The present overlap with established theory is therefore best classified as a **geometric representation of restricted known interference mathematics**, with a deliberately constrained object-language. Neither this paper nor its terminology establishes priority for a novel formulation of quantum mechanics.

## Relation to Music of the Spheres and EFMW

The companion [Music of the Spheres repository](https://github.com/enuminous/Music-of-the-Spheres/tree/62604e05716457147d17caddd5ea463e47739f1c) contains a bilingual world-view modeller and a starter Lean formalization.

At that pinned revision:

- `GreekFoundations.lean` defines unity, multitudes, a magnitude-expression grammar, and an abstract proportion language.
- `GreekHarmonics.lean` checks selected positive-length ratio equalities in an explicitly modern external arithmetic.
- `GreekCosmos.lean` defines evidence and verdict records and proves limited qualification-propagation facts.
- `MusicOfTheSpheres.lean` imports those modules.

Those declarations do not contain the plane geometry, parallelogram construction, square-area outcome rule, or measurement postulates proposed here. A passing build of the existing project must not be cited as verification of this paper's quantum construction.

EFMW's role here is to organize definitions, dependencies, provenance, objections, and unresolved claims. No EFMW physical equation is used to derive the interference rule. The candidate therefore does not demonstrate an EFMW-specific quantum prediction.

## A bounded next study

Before implementation, freeze a two-output specification with equal contributions and the three exact configurations in the table above. Require the geometric diagonal-square relation for nondegenerate configurations and separate proofs for the closed boundary cases.

Success at the **mathematical level** means:

- both open-output weights are ratios of positive areas;
- the two open-output areas exhaust the comparison magnitude;
- closed cases are handled explicitly without admitting a positive degenerate segment;
- common rotation does not alter the predicted proportions;
- the right-angle case divides the comparison magnitude equally.

Failure includes an undefined normalization, a missing boundary case, or an output rule that depends on the arbitrary orientation of the whole drawing.

At the **comparison level**, an external modern calculation may check agreement with the standard balanced-interferometer formula. That calculation must be labeled an audit, not smuggled into the native derivation.

At the **physical level**, measured outcome frequencies would test the correspondence postulates. Agreement with an already established interference pattern would validate the restricted reconstruction against that target; it would not distinguish the proposal from standard quantum mechanics or, by itself, from a classical-wave intensity model.

A subsequent research stage must address a discriminating quantum target, such as joint-system correlations or single-photon statistics with the relevant classical comparator. It cannot declare success simply because circles and harmonies appear in a diagram.

## Conclusion

Numerical zero is not required as a native object for the restricted geometric construction presented here. Exact opposition can be expressed as closure, and nonclosed outcomes can be compared through positive square areas.

That is an expressive result, not an escape from cancellation or an independent derivation of quantum physics. Greek-inspired construction supplies the geometry. The proposed rules connecting that geometry to paths, records, and detection frequencies supply the physical content.

Music of the Spheres can make this boundary productive: build the permitted constructions, state every added rule, and ask which observed relations follow. A quantum theory would have to emerge from that full chain of explicit mathematics and empirical obligations, rather than from vocabulary alone.

## References

1. Euclid, *Elements*, Book VII, Definitions 1–2. Primary text in translation, with David E. Joyce's editorial guide. [Clark University edition](https://mathcs.clarku.edu/~DJoyce/java/elements/bookVII/defVII1.html).
2. Euclid, *Elements*, Book V, Definitions 5–6. [Text and editorial guide](https://mathcs.clarku.edu/~DJoyce/java/elements/bookV/defV5.html).
3. Euclid, *Elements*, Book II, Proposition 12. [Text and construction](https://mathcs.clarku.edu/~DJoyce/java/elements/bookII/propII12.html).
4. Euclid, *Elements*, Book II, Proposition 13. [Text and construction](https://mathcs.clarku.edu/~DJoyce/java/elements/bookII/propII13.html).
5. Feynman, Leighton, and Sands, *The Feynman Lectures on Physics*, Volume III, Chapter 1, “Quantum Behavior.” [Caltech edition](https://www.feynmanlectures.caltech.edu/III_01.html).
6. Feynman, Leighton, and Sands, Volume III, Chapter 3, “Probability Amplitudes.” [Caltech edition](https://www.feynmanlectures.caltech.edu/III_03.html).
7. Feynman, Leighton, and Sands, Volume III, Chapter 6, “Spin One-Half.” [Caltech edition](https://www.feynmanlectures.caltech.edu/III_06.html).
8. Wright, Matthew Chenoweth. *Music of the Spheres*, source revision `62604e05716457147d17caddd5ea463e47739f1c`. [Repository](https://github.com/enuminous/Music-of-the-Spheres/tree/62604e05716457147d17caddd5ea463e47739f1c).

**Authorship and preparation:** Prepared for Matthew Chenoweth Wright with AI assistance. The proposal continues the Greek-mathematics research discussion with Vincenzo Barney; acknowledgment does not imply his endorsement or coauthorship. No new experiment, simulation, or Lean proof of this proposed construction was performed for this paper.
