# Formal Structure and Emergent Compatibility Conditions in the 165-Triplet FieldSpace Atlas

**Matthew Chenoweth Wright**  
Monolithic LLC / eNuminous  
October 1, 2026

## Abstract

A 165-triplet FieldSpace construction built from 11 sectors has now been subjected to formal verification. The resulting theorem set establishes the exact combinatorial structure of the atlas, verifies the source inventory, proves the parameter economy induced by reciprocity, characterizes when three-scalar non-derivative couplings arise from a common potential, proves overlap and ablation laws, and derives an additional scalar compatibility equation forced by gauge-current conservation.

The strongest dynamical result is the following. In flat space with any constant diagonal metric, suppose an antisymmetric gauge field satisfies

[
\partial_\mu F^{\mu\nu}
=
\kappa\phi\,\partial^\nu\phi + J^\nu,
]

with all remaining currents conserved, while the scalar field satisfies

[
\Box\phi + m^2\phi + s = 0.
]

If (\kappa\neq 0), every joint solution must also satisfy

[
(\partial\phi)^2 = m^2\phi^2 + \phi s.
]

This equation is not separately listed in the source system. It therefore functions as a derived compatibility condition on the joint solution space. The formal result does not by itself establish a new law of nature; it shows that the stated FieldSpace equations imply an additional restriction that any physical interpretation of the system must confront.

The remaining results show that the 165-triplet atlas is not merely a large collection of equations. It has a formally certified hypergraph structure, an exact reciprocity criterion for potential integrability, a quantified parameter reduction, and precise gluing laws between overlapping triplets. Together these results define a tractable mathematical skeleton for further analysis and empirical testing.

---

## 1. Introduction

FieldSpace organizes interactions among 11 sectors by taking every unordered 3-element subset of those sectors. The complete atlas therefore contains

[
\binom{11}{3}=165
]

triplets.

Each triplet carries a prescribed block of gravitational, gauge, Bianchi, and scalar statements. The formalization effort described here had two goals:

1. determine whether the source atlas has the exact combinatorial structure claimed for it; and
2. determine whether the equations impose hidden algebraic or differential constraints beyond those explicitly listed.

The resulting theorems answer both questions affirmatively, although in different senses.

The combinatorial claims are now exact theorems. The atlas size, sector incidence, pair incidence, class sizes, overlap spectrum, ablation behavior, source inventory, and overlap gluing laws have all been proved.

More significantly for dynamics, one conservation-closure theorem derives an additional scalar equation from the gauge equation, antisymmetry, current conservation, and the scalar equation. This exposes a nontrivial compatibility condition that was not entered as an independent source equation.

This paper records the current formal result set and clarifies what has—and has not—been established.

---

## 2. The FieldSpace Atlas

Let the theory contain 11 sectors. A FieldSpace triplet is an unordered choice of three distinct sectors.

The atlas is therefore naturally the complete 3-uniform hypergraph on 11 vertices.

This observation gives immediate counting expectations, but the formal development does not merely rely on those expectations. The relevant statements have been encoded and proved.

### 2.1 Atlas cardinality

The theorem

[
	exttt{FieldSpace.atlas\_card}
]

establishes that the atlas contains exactly

[
165
]

triplets.

### 2.2 Sector incidence

For any fixed sector, there are 10 remaining sectors from which the other two members of a triplet may be chosen. Thus the expected incidence is

[
\binom{10}{2}=45.
]

The theorem

[
	exttt{FieldSpace.sector\_incidence}
]

proves that every sector belongs to exactly 45 atlas triplets.

### 2.3 Pair incidence

For any fixed pair of distinct sectors, the third member of the triplet may be chosen from the 9 remaining sectors.

The theorem

[
	exttt{FieldSpace.pair\_incidence}
]

therefore establishes that every distinct sector pair occurs in exactly

[
9
]

triplets.

These three results constitute FS-T01 through FS-T03.

---

## 3. Six-Class Partition

The atlas may be partitioned according to the number of gravity and gauge sectors appearing in each triplet.

The theorem

[
	exttt{FieldSpace.six\_classes\_partition}
]

proves that the six classes have cardinalities

[
56,;56,;28,;16,;8,;1,
]

and that every atlas triplet belongs to exactly one class.

The total is

[
56+56+28+16+8+1=165.
]

This matters because the classification is therefore exhaustive and non-overlapping. Any later theorem proved class-by-class can be assembled into a theorem over the full atlas without concern that some triplets have been omitted or counted twice.

This result is designated FS-T04.

---

## 4. Source Inventory Verification

A large formal system can fail before physics begins if its source representation is incomplete, duplicated, or inconsistent with its own grammar.

The theorem

[
	exttt{FieldSpace.source\_inventory}
]

checks the source file against the declared atlas grammar.

It proves that:

- the block headings are exactly the 165 atlas triplets;
- every block contains exactly the statements prescribed by the grammar;
- the complete source contains
  - 45 Einstein statements,
  - 90 gauge statements,
  - 90 Bianchi statements,
  - 360 scalar statements;
- the total source inventory is therefore

[
45+90+90+360=585
]

statements.

This is FS-T05.

The importance of this result is methodological. Subsequent conclusions can be stated about a source whose structural completeness has itself been checked formally.

---

## 5. Ablation Law

Suppose a set (X) of sectors is removed.

The theorem

[
	exttt{FieldSpace.ablate\_card}
]

proves that the surviving atlas is exactly the collection of 3-subsets of the complement of (X). Hence the number of surviving triplets is

[
\binom{11-|X|}{3}.
]

In particular:

- deleting one sector leaves

[
\binom{10}{3}=120
]

triplets;

- deleting two leaves

[
\binom{9}{3}=84;
]

- deleting three leaves

[
\binom{8}{3}=56.
]

This is FS-T06.

The result gives a precise ablation rule for any experiment that removes one or more sectors from the formal system.

---

## 6. Overlap Spectrum of the Atlas

Two distinct triplets in a 3-uniform atlas may share two sectors, one sector, or none.

The theorem

[
	exttt{FieldSpace.overlap\_spectrum}
]

proves the complete distribution over all unordered pairs of distinct atlas triplets.

There are

[
\binom{165}{2}=13530
]

such pairs.

Among them:

- 1980 pairs share exactly two sectors;
- 6930 pairs share exactly one sector;
- 4620 pairs are disjoint.

Thus

[
1980+6930+4620=13530.
]

The theorem also proves that no pair of distinct triplets shares more than two sectors, as expected for distinct 3-element subsets.

This is FS-T07.

The overlap spectrum provides the exact combinatorial background for any later analysis of consistency propagation, shared couplings, gluing, or local-to-global reconstruction.

---

## 7. Gluing Across Shared Pairs

The theorem

[
	exttt{FieldSpace.shared\_pair\_overlap\_iff}
]

analyzes two triplets sharing a common pair of sectors.

Two structural facts follow.

First, the three-way interaction term vanishes on the relevant null slices where the third field is set to zero.

Second, two triplets sharing a pair glue on those third-field-zero slices if and only if the surviving base terms and pair coefficients agree.

This gives a sharp local compatibility criterion between neighboring atlas blocks.

The result encompasses FS-T08 and FS-T09.

Its significance is that consistency between overlapping triplets is not vague. On the reduced slice, compatibility is characterized by explicit equality of the surviving data.

---

## 8. Scalar Potential Integrability

Consider a three-scalar triplet with directional pair couplings and a three-way coupling.

The theorem

[
	exttt{FieldSpace.ScalarTripletCouplings.exists\_potential\_iff\_reciprocal}
]

proves that the non-derivative pieces of the three scalar equations are the partial derivatives of a single scalar potential if and only if the couplings obey the reciprocity conditions

[
\lambda_{xy}=\lambda_{yx},
]

[
\lambda_{xz}=\lambda_{zx},
]

[
\lambda_{yz}=\lambda_{zy},
]

and

[
\lambda_{xyz}
=
\lambda_{yxz}
=
\lambda_{zxy}.
]

This is FS-C02.

The theorem upgrades reciprocity from an aesthetic or simplifying assumption to an exact integrability criterion.

Within the stated three-scalar model, reciprocal coupling is precisely what permits the non-derivative scalar forces to be represented as the gradient of one common potential.

Conversely, asymmetric directional couplings represent a genuinely non-potential scalar system unless additional structure is introduced.

---

## 9. Parameter Economy from Reciprocity

The theorem

[
	exttt{FieldSpace.scalar\_parameter\_economy}
]

counts the scalar coupling symbols before and after the reciprocity identifications.

In the scalar-only triplets, the directional notation contains:

- 56 directional pair symbols;
- 168 directional three-way symbols;

for a total of

[
224
]

symbols.

Under reciprocity these collapse to:

- 28 unordered pair parameters;
- 56 unordered triplet parameters;

for a total of

[
84
]

independent parameters.

The reduction is therefore

[
224-84=140
]

parameters.

As a percentage,

[
\frac{140}{224}=0.625,
]

so reciprocity removes

[
62.5\%
]

of the directional scalar coupling degrees of freedom.

This is FS-C04.

The result is useful in both model selection and implementation. A reciprocal, potential-derived scalar sector is not only structurally constrained; it is substantially more economical.

---

## 10. Conservation Closure and the Extra Scalar Equation

The most consequential present theorem is

[
	exttt{FieldSpace.scalar\_current\_extra\_equation}.
]

Work in flat space with any constant diagonal metric.

Assume an antisymmetric gauge field strength:

[
F^{\mu\nu}=-F^{\nu\mu}.
]

Suppose the gauge equation is

[
\partial_\mu F^{\mu\nu}
=
\kappa\phi\partial^\nu\phi + J^\nu,
]

where the remaining current satisfies

[
\partial_\nu J^\nu=0.
]

Also suppose the scalar equation is

[
\Box\phi+m^2\phi+s=0.
]

Taking the divergence of the gauge equation gives

[
\partial_\nu\partial_\mu F^{\mu\nu}
=
\kappa\,\partial_\nu
\left(
\phi\partial^\nu\phi
\right)
+
\partial_\nu J^\nu.
]

Because (F^{\mu\nu}) is antisymmetric while the commuting second derivatives are symmetric in their indices,

[
\partial_\nu\partial_\mu F^{\mu\nu}=0.
]

Current conservation removes the final term, leaving

[
0=
\kappa
\left[
(\partial\phi)^2+\phi\Box\phi
\right].
]

For

[
\kappa\neq 0,
]

this implies

[
(\partial\phi)^2+\phi\Box\phi=0.
]

Substituting

[
\Box\phi=-m^2\phi-s
]

from the scalar equation yields

[
(\partial\phi)^2
=
m^2\phi^2+\phi s.
]

Thus every joint solution of the stated gauge and scalar equations must also satisfy

[
oxed{
(\partial\phi)^2
=
m^2\phi^2+\phi s
}
]

whenever (\kappa\neq0).

This result is FS-C03.

---

## 11. Interpretation of the Extra Equation

The formal conclusion should be stated carefully.

The theorem does **not** establish that

[
(\partial\phi)^2=m^2\phi^2+\phi s
]

is an experimentally verified law of nature.

It establishes something narrower and mathematically stronger:

> within the stated FieldSpace gauge-scalar system, under the theorem's assumptions, the equation is a necessary condition for any joint solution.

That has several possible interpretations.

### 11.1 Hidden closure law

The relation may be an intended but previously unstated closure condition. In that case, the formalization has exposed a law implicit in the source equations.

### 11.2 Overdetermination

The relation may be unintended. Then the joint system is more restrictive than its source presentation suggests, and generic initial data may fail to admit solutions.

### 11.3 Source or current modification

A physically intended theory may require a modified source term, non-conserved exchange current, altered scalar equation, or different coupling structure so that the divergence identity closes differently.

### 11.4 Prediction target

If the relation survives model refinement and applies to a physically identified scalar sector, it becomes a candidate empirical discriminator. The next step would be to derive observable consequences in a specified regime and compare them against an established model.

These possibilities must be distinguished by further mathematics and experiment.

---

## 12. Structural Results Versus Physical Results

The current theorem set naturally divides into two categories.

### 12.1 Structural theorems

The following results certify the organization of the FieldSpace formal system:

- atlas cardinality;
- sector incidence;
- pair incidence;
- six-class partition;
- source inventory;
- ablation cardinality;
- overlap spectrum;
- shared-pair gluing;
- reciprocity-based parameter counting.

These are exact mathematical facts about the encoded system.

### 12.2 Dynamical compatibility theorem

The conservation-closure result differs in character.

It begins with differential field equations and proves an additional differential-algebraic constraint on their common solution space.

That makes it more than a cataloguing theorem.

It is still a theorem about the model, not yet about nature, but it identifies a concrete place where the model can succeed, fail, or distinguish itself.

---

## 13. What Has Been Established

The present formal results establish the following.

1. The atlas is exactly the complete collection of 165 three-sector combinations over 11 sectors.

2. Every sector occurs in 45 triplets.

3. Every pair of sectors occurs in 9 triplets.

4. The six declared gravity/gauge classes form an exact partition with sizes

   [
   56,56,28,16,8,1.
   ]

5. The source file contains exactly the 165 prescribed blocks and 585 prescribed statements.

6. Sector deletion obeys the exact law

   [
   \binom{11-|X|}{3}.
   ]

7. The overlap spectrum of all 13,530 unordered triplet pairs is exactly

   [
   1980/6930/4620
   ]

   for overlap sizes (2/1/0).

8. Shared-pair triplets have a precise reduced-slice gluing criterion.

9. A three-scalar triplet possesses a common non-derivative potential exactly when its couplings satisfy reciprocity.

10. Reciprocity reduces the scalar directional parameter count from 224 to 84.

11. Under the assumptions of FS-C03, gauge-current conservation forces the additional relation

   [
   (\partial\phi)^2=m^2\phi^2+\phi s.
   ]

---

## 14. What Has Not Been Established

These proofs do not by themselves establish:

- that the complete FieldSpace model is a correct description of nature;
- that every sector has a known physical realization;
- that every parameter has a measured value;
- that the extra scalar equation has been observed experimentally;
- that the full system possesses globally well-posed solutions;
- that the quantum theory is defined or renormalizable;
- that the gauge-scalar source structure is phenomenologically viable;
- that reciprocity must hold in nature rather than merely characterizing the potential-derived subclass;
- that the 165-triplet construction is unique.

These remain separate questions.

Formal verification narrows them. It does not replace them.

---

## 15. Immediate Research Program

The results point to a focused next stage.

### 15.1 Classify solutions of FS-C03

Solve or classify

[
(\partial\phi)^2=m^2\phi^2+\phi s
]

together with

[
\Box\phi+m^2\phi+s=0
]

for simple source choices.

Particularly useful cases include:

- (s=0);
- constant (s);
- static one-dimensional solutions;
- homogeneous time-dependent solutions;
- weak-field perturbations.

### 15.2 Determine whether FS-C03 is redundant or restrictive

For each regime, determine whether the extra equation follows automatically from a known first integral or whether it removes otherwise valid scalar solutions.

### 15.3 Derive observable quantities

If a physically identified scalar sector survives the consistency analysis, derive measurable consequences rather than treating the compatibility equation itself as sufficient evidence.

### 15.4 Extend reciprocity to larger overlaps

The three-scalar potential theorem suggests a broader question: what global reciprocity conditions are required for all overlapping scalar triplets to arise from one atlas-wide potential?

### 15.5 Prove global gluing theorems

The shared-pair theorem gives a local result. A natural next target is a local-to-global theorem specifying when all 165 triplets can be glued into a single consistent field model.

### 15.6 Couple formal results to numerical experiments

Formal theorems should determine what the numerical harness is required to preserve. Numerical experiments can then search the admissible solution space rather than unknowingly integrating inconsistent initial conditions.

---

## 16. Conclusion

The 165-triplet FieldSpace atlas has crossed an important mathematical threshold.

Its basic architecture is now formally certified rather than informally counted. The source inventory is exact. The overlap and ablation laws are known. Scalar reciprocity has been characterized by an if-and-only-if potential theorem. The reduction in independent scalar parameters has been quantified exactly.

Most importantly, conservation closure has produced a nontrivial additional equation:

[
(\partial\phi)^2=m^2\phi^2+\phi s.
]

This equation should not yet be advertised as a discovered law of physics. It should be treated as something more immediately useful: a precise theorem about what the current FieldSpace equations require.

That is exactly the role formalization should play.

It converts a large symbolic framework into explicit proof obligations, exposes hidden dependencies, distinguishes free assumptions from forced consequences, and produces sharply stated targets for the next round of mathematical and experimental work.

---

## Appendix A. Current Formal Result Index

| Formal theorem | Result |
|---|---|
| `FieldSpace.atlas_card` | 165 triplets |
| `FieldSpace.sector_incidence` | each sector occurs in 45 triplets |
| `FieldSpace.pair_incidence` | each distinct pair occurs in 9 triplets |
| `FieldSpace.six_classes_partition` | six classes of sizes 56/56/28/16/8/1 partition the atlas |
| `FieldSpace.source_inventory` | 165 source blocks; 585 total statements |
| `FieldSpace.ablate_card` | deleting (X) leaves (inom{11-|X|}{3}) triplets |
| `FieldSpace.overlap_spectrum` | 1980/6930/4620 pairs share 2/1/0 sectors |
| `FieldSpace.shared_pair_overlap_iff` | exact shared-pair reduced-slice gluing criterion |
| `FieldSpace.ScalarTripletCouplings.exists_potential_iff_reciprocal` | potential exists iff scalar couplings are reciprocal |
| `FieldSpace.scalar_parameter_economy` | 224 directional scalar symbols reduce to 84 reciprocal parameters |
| `FieldSpace.scalar_current_extra_equation` | conservation closure forces ((\partial\phi)^2=m^2\phi^2+\phi s) for (kappa\neq0) |

---

## Appendix B. Evidence Status

The claims in this paper are intentionally divided by evidence type.

**Formally proved:** the theorem statements listed in Appendix A, subject to the definitions and assumptions encoded in the formal development.

**Mathematical interpretation:** conclusions such as overdetermination, integrability, parameter economy, and compatibility are interpretations of those proved statements.

**Not yet established empirically:** any claim that the FieldSpace equations, the reciprocal subclass, or the extra scalar compatibility equation describe observed physical reality.

This distinction should be preserved in subsequent publication, simulation, and experimental work.
