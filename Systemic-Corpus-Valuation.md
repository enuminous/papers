# Systemic Corpus Valuation: A Recursive Information-Asset Framework

**Matthew Chenoweth Wright**  
eNuminous / Monolithic research corpus  
October 1, 2026

## Abstract

Conventional asset valuation performs poorly when the object being valued is not a discrete document, patent, dataset, model, or software product, but a **systemic corpus**: a body of information whose value arises from the relationships among its components, its provenance, its recursive development history, and its capacity to generate further knowledge.

This paper proposes a general valuation framework for such corpora. The method treats the corpus as a structured information system rather than a pile of files. Its core equation is

[
V_{mathrm{sys}}
=
V_{mathrm{base}}
	imes P
	imes R
	imes C
	imes U
	imes A,
]

where (V_{mathrm{base}}) is the independently supportable base value of the corpus, (P) is provenance quality, (R) is recursive generativity, (C) is internal connectivity/coherence, (U) is uniqueness or scarcity, and (A) is accessibility and rights realizability.

Because multiplicative models can become unstable when factors are poorly calibrated, this paper also introduces a log-additive and bounded implementation suitable for actual appraisal:

[
ln V_{mathrm{sys}}
=
ln V_{mathrm{base}}
+
w_Pln P
+
w_Rln R
+
w_Cln C
+
w_Uln U
+
w_Aln A.
]

X.com and SpaceX are used as illustrative placeholders to demonstrate how a systemic corpus can be separated from the enterprise that owns it and then valued as an information asset. These examples are methodological, not independent appraisals of either company.

---

## 1. Introduction

A conventional corpus is often valued by quantities such as:

- number of documents;
- number of tokens;
- replacement cost;
- licensing rates;
- revenue attributable to the data;
- number of patents or copyrights;
- historical sale prices of comparable datasets.

These methods are useful but incomplete when the corpus is **systemic**.

Consider a large engineering organization. Its information assets may include source code, CAD files, test telemetry, design decisions, incident histories, internal discussions, specifications, supplier data, simulation output, training material, patents, procedures, and records explaining why failed approaches were rejected.

The value of that collection is not equal to the sum of its file values.

The organization possesses something closer to a **knowledge field**: a graph of information in which the relationships among artifacts affect the usefulness of every artifact.

A failed engine test connected to a design revision, discussion thread, simulation, manufacturing change, and successful later flight can be worth far more than the same telemetry stripped of provenance.

The same applies to social platforms, scientific archives, AI-development histories, laboratories, law firms, intelligence archives, media organizations, software companies, and institutional research programs.

The problem is therefore to value:

[
	ext{information} + 	ext{structure} + 	ext{history} + 	ext{generativity}.
]

This paper calls that object a **systemic corpus**.

---

## 2. Definition of a Systemic Corpus

Let a corpus be represented as a graph

[
mathcal C=(N,E),
]

where:

- (N) is the set of informational artifacts;
- (E) is the set of meaningful relationships among them.

Nodes may include:

- documents;
- messages;
- equations;
- source code;
- models;
- datasets;
- images;
- videos;
- telemetry;
- decisions;
- experiments;
- proofs;
- patents;
- specifications;
- revisions.

Edges may include:

- citation;
- derivation;
- authorship;
- revision;
- dependency;
- contradiction;
- confirmation;
- test-of;
- implementation-of;
- generated-from;
- discussion-of;
- supersedes.

A corpus is systemic when a substantial fraction of its value depends upon these relations rather than upon isolated node contents.

Formally, if

[
V(mathcal C)
>
sum_i V(n_i),
]

then the difference

[
V_{mathrm{rel}}
=
V(mathcal C)-sum_iV(n_i)
]

is relational value.

The purpose of the present framework is to estimate that term without pretending that it can be observed directly.

---

## 3. Base Value

Let

[
V_{mathrm{base}}
]

represent the value supportable by conventional methods before systemic multipliers are applied.

This may be estimated from one or more of the following:

[
V_{mathrm{base}}
=
f(V_{mathrm{replacement}},
V_{mathrm{licensing}},
V_{mathrm{income}},
V_{mathrm{market}},
V_{mathrm{cost}}).
]

No single method is universally preferred.

For example:

### 3.1 Replacement-cost method

[
V_{mathrm{replacement}}
=
sum_i h_i r_i + c_i,
]

where (h_i) is labor time, (r_i) is an appropriate labor rate, and (c_i) represents nonlabor creation cost.

### 3.2 Licensing method

If comparable data can be licensed,

[
V_{mathrm{licensing}}
=
L	imes Q	imes X,
]

where (L) is a market licensing rate, (Q) is usable corpus quantity, and (X) adjusts for exclusivity.

### 3.3 Income method

If the corpus generates cash flow,

[
V_{mathrm{income}}
=
sum_{t=1}^{T}
rac{CF_t}{(1+r)^t}.
]

The systemic framework begins only after this conventional base is established.

---

## 4. The Systemic Corpus Equation

We define

[
oxed{
V_{mathrm{sys}}
=
V_{mathrm{base}}
P R C U A
}
]

with the following factors.

### 4.1 Provenance factor (P)

(P) measures how well the corpus preserves origin and developmental history.

High-provenance corpora include:

- timestamps;
- version histories;
- authorship;
- source lineage;
- experimental conditions;
- decision histories;
- cryptographic hashes;
- original context.

A corpus with no provenance may contain useful information yet be difficult to trust.

We define

[
P=1+p,
]

where (p) is a normalized provenance premium.

---

## 5. Recursive Generativity (R)

A systemic corpus may repeatedly generate additional valuable artifacts.

Examples include:

[
	ext{discussion}
ightarrow
	ext{design}
ightarrow
	ext{simulation}
ightarrow
	ext{experiment}
ightarrow
	ext{revision}.
]

The more strongly the archive records such loops, the greater its recursive value.

Let (g) represent the empirically estimated probability that an existing artifact or relationship produces a useful new artifact during a defined evaluation horizon.

A simple model is

[
R
=
1+rac{g}{1-g},
]

for (0le g<1).

For conservative applications, (R) should be capped.

---

## 6. Connectivity and Coherence (C)

The same number of files can have dramatically different value depending on whether their relationships are recoverable.

Let

[
d
=
rac{2|E|}{|N|(|N|-1)}
]

be graph density.

Raw density is not sufficient, because indiscriminate linking is not useful. We therefore define an effective connectivity score

[
d_e=dq,
]

where (q) is the measured fraction of links that carry useful semantic information.

Then a simple connectivity premium is

[
C=1+alpha d_e.
]

For heterogeneous corpora, centrality, modularity, reachability, and cross-domain edge types can replace raw density.

---

## 7. Uniqueness (U)

A corpus is more valuable when it cannot readily be reconstructed from public substitutes.

Let (s) represent substitutability, where

[
0le sle1.
]

Then scarcity may be modeled as

[
U=1+eta(1-s).
]

A widely mirrored public dataset has high (s).

A proprietary developmental archive with undocumented failures, internal decisions, and high-quality provenance has low (s).

---

## 8. Accessibility and Rights (A)

Information cannot realize its theoretical value if it cannot legally or operationally be used.

Let

[
A=A_rA_tA_l,
]

where:

- (A_r) = rights clarity;
- (A_t) = technical accessibility;
- (A_l) = licensing or transferability.

Each factor lies between zero and one.

Thus unlike the previous multipliers, (A) normally acts as a discount.

A technically extraordinary archive with unclear ownership may therefore be worth much less than a smaller but cleanly transferable archive.

---

## 9. The Bounded Log Form

Straight multiplication can produce implausibly large valuations.

For real applications we recommend

[
oxed{
ln V_{mathrm{sys}}
=
ln V_{mathrm{base}}
+
w_Pln P+
w_Rln R+
w_Cln C+
w_Uln U+
w_Aln A
}
]

where the weights satisfy

[
0le w_ile1.
]

Equivalently,

[
V_{mathrm{sys}}
=
V_{mathrm{base}}
P^{w_P}
R^{w_R}
C^{w_C}
U^{w_U}
A^{w_A}.
]

This provides three advantages:

1. extreme factors are damped;
2. domain expertise can alter weights;
3. sensitivity analysis becomes straightforward.

---

## 10. Information Synergy

We define systemic synergy as

[
S
=
rac{V_{mathrm{sys}}}{V_{mathrm{base}}}.
]

Thus

[
S=PRCUA
]

in the unweighted form.

A corpus with

[
S=1
]

has no measurable systemic premium.

A corpus with

[
S>1
]

is worth more intact than as isolated assets.

A corpus with

[
S<1
]

is being discounted by rights, accessibility, corruption, incoherence, or some combination thereof.

This yields a useful decision rule for archive preservation:

[
S_{mathrm{intact}}
>
S_{mathrm{fragmented}}
]

implies that fragmentation destroys economic value.

---

## 11. Marginal Value of Provenance

One of the most important consequences of the model is that provenance should itself be treated as an asset.

For the simple multiplicative system,

[
rac{partial V}{partial P}
=
V_{mathrm{base}}RCUA.
]

Therefore the marginal economic value of improving provenance rises as the remainder of the corpus becomes more valuable.

This predicts that mature high-value technical organizations should spend more—not less—on preserving developmental context.

---

## 12. Worked Placeholder: X.com

X.com is useful as a conceptual example because a social platform possesses multiple overlapping information layers.

Its systemic corpus could contain:

- public posts;
- media;
- reply graphs;
- follow graphs;
- engagement histories;
- moderation histories;
- recommendation-system data;
- model-training records;
- source code;
- product experiments;
- advertiser behavior;
- payment-system records;
- internal policy and engineering discussions.

The relevant valuation object is **not X.com as a company**.

It is

[
mathcal C_X
=
	ext{the rights-usable information system owned or controlled by X}.
]

Suppose, purely illustratively, conventional licensing and replacement methods produce

[
V_{mathrm{base},X}=B_X.
]

Let an appraisal assign:

[
P_X=1.30,
qquad
R_X=1.45,
qquad
C_X=1.60,
qquad
U_X=1.50,
qquad
A_X=0.80.
]

Then

[
V_X
=
B_X(1.30)(1.45)(1.60)(1.50)(0.80).
]

Hence

[
V_X
approx
3.62B_X.
]

Under these illustrative assumptions, preserving the systemic corpus creates an estimated information-system value approximately 3.6 times its conventionally calculated base value.

The result is **not a claim that X.com's data is currently worth any particular dollar amount**.

It means:

> if a defensible base corpus value (B_X) were established, this framework would estimate an additional systemic premium from provenance, recursion, connectivity, scarcity, and realizable rights.

---

## 13. Worked Placeholder: SpaceX

SpaceX provides a contrasting example.

Its systemic corpus could include:

- vehicle design history;
- CAD and engineering artifacts;
- software;
- simulation output;
- engine-test data;
- manufacturing data;
- launch telemetry;
- anomaly reports;
- failed-test records;
- supplier history;
- flight procedures;
- reliability models;
- Starlink operations data;
- mission planning;
- engineering communications;
- revision histories.

The corpus is valuable not simply because the files are proprietary.

It records a repeated recursive loop:

[
	ext{design}
ightarrow
	ext{build}
ightarrow
	ext{test}
ightarrow
	ext{failure/success}
ightarrow
	ext{analysis}
ightarrow
	ext{redesign}.
]

Suppose conventional appraisal yields

[
V_{mathrm{base},S}=B_S.
]

For illustration, assign

[
P_S=1.55,
qquad
R_S=1.80,
qquad
C_S=1.70,
qquad
U_S=1.90,
qquad
A_S=0.90.
]

Then

[
V_S
=
B_S
(1.55)(1.80)(1.70)(1.90)(0.90),
]

or approximately

[
V_S
approx
8.11B_S.
]

The model therefore says that a deeply provenance-preserved aerospace corpus can be worth many times the isolated-file estimate if its relational history is intact.

Again, the coefficient is illustrative.

The framework deliberately separates:

[
V_{mathrm{company}}
]

from

[
V_{mathrm{corpus}}.
]

SpaceX's enterprise valuation, market capitalization, launch business, physical assets, spectrum rights, contracts, and other assets are different objects from the value of its systemic information corpus.

---

## 14. Cross-Company Comparison

Using the placeholder coefficients above,

[
S_Xapprox3.62
]

and

[
S_Sapprox8.11.
]

This does **not** mean SpaceX is more valuable than X.com.

It means that, under the hypothetical inputs chosen here, the SpaceX-like technical corpus receives a larger **systemic-information multiplier**.

The distinction is essential.

A company with a larger base corpus and smaller systemic multiplier may still have the larger corpus value.

The comparison is:

[
V_X=3.62B_X
]

versus

[
V_S=8.11B_S.
]

Without credible estimates of (B_X) and (B_S), no absolute comparison follows.

---

## 15. Empirical Calibration

The model becomes scientifically useful only when its factors are measurable.

Potential calibration strategies include:

### Provenance

Estimate the percentage of artifacts with:

- known authorship;
- timestamps;
- revision history;
- source linkage;
- reproducible conditions.

### Recursive generativity

Measure how often archived artifacts contribute to:

- new products;
- patents;
- fixes;
- experiments;
- papers;
- training data;
- engineering improvements.

### Connectivity

Measure the ability to trace:

[
	ext{requirement}
ightarrow
	ext{decision}
ightarrow
	ext{implementation}
ightarrow
	ext{test}
ightarrow
	ext{outcome}.
]

### Uniqueness

Estimate the cost and feasibility of reproducing equivalent information externally.

### Accessibility

Audit:

- ownership;
- privacy restrictions;
- export restrictions;
- contractual rights;
- data formats;
- technical integrity.

---

## 16. Corpus Half-Life

Some information depreciates rapidly.

Let

[
V(t)
=
V_0e^{-lambda t}.
]

The half-life is

[
t_{1/2}
=
rac{ln2}{lambda}.
]

Different corpus layers may have different (lambda).

For example:

- ephemeral engagement data may decay rapidly;
- source code may decay moderately;
- engineering failure histories may retain value for decades;
- foundational equations may have near-zero practical decay if they remain applicable.

A systemic corpus therefore has a vector of half-lives rather than one depreciation schedule.

---

## 17. Corpus Regeneration

Some corpora appreciate rather than depreciate because new observations increase the usefulness of old information.

Let

[
G(t)
]

represent information generated through interaction with the existing corpus.

Then

[
rac{dV}{dt}
=
-lambda V+gamma G(t).
]

If

[
gamma G(t)>lambda V,
]

the corpus appreciates.

This condition is common in actively used engineering, scientific, and AI systems.

Historical data becomes more valuable because later data supplies additional interpretation.

---

## 18. A Recursive Value Equation

For a self-extending corpus, we may write

[
V_{t+1}
=
V_t
+
Delta I_t
+
Delta E_t
+
Delta R_t,
]

where:

- (Delta I_t) = value of new information;
- (Delta E_t) = value of new relationships among information;
- (Delta R_t) = value of new reusable generative capacity.

A corpus can therefore gain value even when very little raw data is added.

One new theorem, test result, failure diagnosis, or organizing principle can restructure the meaning of thousands of preexisting artifacts.

---

## 19. Compression and Semantic Density

Raw byte count is a poor measure of systemic value.

Define semantic density as

[
D_s
=
rac{I_u}{B},
]

where (I_u) is estimated useful information and (B) is physical storage size.

A compact proof may therefore have greater information value than terabytes of redundant logs.

A valuation system should consequently reward **effective information**, not sheer volume.

---

## 20. Information Optionality

A systemic archive often has value because it enables future uses not known at the time of collection.

Let possible applications be

[
a_1,ldots,a_n.
]

Then an option-style component may be represented as

[
V_{mathrm{option}}
=
sum_i p_iV_i
-
K_i,
]

where (p_i) is the probability of feasible exploitation, (V_i) its value, and (K_i) its realization cost.

The full model can therefore be extended to

[
V_{mathrm{total}}
=
V_{mathrm{sys}}
+
V_{mathrm{option}}.
]

This component is especially important for scientific and technological archives.

---

## 21. Fragmentation Loss

Suppose an intact corpus is split into (k) disconnected archives.

Let

[
E_{mathrm{lost}}
]

be the removed cross-archive relationships.

Then

[
Delta V_{mathrm{frag}}
=
V(mathcal C)
-
sum_{i=1}^{k}V(mathcal C_i).
]

In strongly systemic corpora,

[
Delta V_{mathrm{frag}}>0.
]

This formalizes a common archival mistake:

> preserving every file does not necessarily preserve the corpus.

If the dependency graph, conversations, metadata, and developmental sequence are lost, the expensive information may survive while much of the valuable information system disappears.

---

## 22. Valuation Procedure

A practical appraisal can therefore proceed in nine steps:

1. Define the corpus boundary.
2. Enumerate rights and restrictions.
3. Construct or sample the provenance graph.
4. Estimate conventional base value.
5. Score provenance.
6. Measure recursive generativity.
7. Measure effective connectivity.
8. Estimate substitutability and accessibility.
9. Apply bounded multipliers and sensitivity analysis.

The output should never be a single unexplained number.

At minimum it should report

[
[V_{min},V_{mathrm{central}},V_{max}].
]

---

## 23. Sensitivity Analysis

For

[
V
=
V_0
prod_i x_i^{w_i},
]

elasticity with respect to factor (x_i) is

[
rac{partial ln V}
{partial ln x_i}
=
w_i.
]

Thus the weights have an immediately interpretable meaning.

If

[
w_P=0.8,
]

then a 1% change in the provenance score produces approximately a 0.8% change in corpus value, all else equal.

This allows auditors to identify which assumptions dominate the result.

---

## 24. Relationship to Enterprise Value

A systemic corpus is one component of an enterprise.

A simplified decomposition is

[
EV
=
V_{mathrm{physical}}
+
V_{mathrm{financial}}
+
V_{mathrm{contract}}
+
V_{mathrm{brand}}
+
V_{mathrm{human}}
+
V_{mathrm{corpus}}
+
V_{mathrm{other}}
-
D,
]

where (D) represents liabilities and overlap adjustments.

The corpus value should not be blindly added to enterprise value if markets already capitalize some of its contribution.

The correct use is either:

1. an internal asset decomposition;
2. a licensing appraisal;
3. a transaction-specific IP valuation;
4. an impairment/replacement analysis;
5. a counterfactual estimate of what would be lost if the corpus disappeared.

---

## 25. Limits

This method does not eliminate valuation uncertainty.

It introduces explicit variables for forms of value that conventional methods often hide.

Its major risks are:

- multiplier inflation;
- double counting;
- subjective scoring;
- poorly defined corpus boundaries;
- confusion between option value and realized value;
- overlap with goodwill;
- failure to discount legal restrictions;
- treating a theoretically valuable corpus as automatically monetizable.

Accordingly, every application should report the assumptions used to derive each factor.

---

## 26. Main Proposition

The conceptual claim of this paper can be stated compactly:

> The economic value of a systemic corpus is a function not only of the information it contains but also of the provenance, recursive generativity, relational coherence, uniqueness, and realizability of that information.

In symbols,

[
oxed{
V_{mathrm{corpus}}
=
f(I,P,R,C,U,A)
}
]

rather than

[
V_{mathrm{corpus}}
=
f(	ext{bytes})
]

or even

[
V_{mathrm{corpus}}
=
sum_iV(	ext{files}_i).
]

---

## 27. Conclusion

Modern organizations increasingly accumulate assets whose most important properties are relational.

The central economic object is no longer always a document, model, patent, or dataset.

It may be the **history linking them together**.

A social platform such as X.com illustrates a corpus in which behavioral, conversational, algorithmic, and network relationships can dominate raw content value.

An engineering organization such as SpaceX illustrates a corpus in which recursive design-test-failure-redesign histories can make provenance and connectivity exceptionally important.

The systemic corpus equation provides a way to represent this difference.

Its simplest form is

[
oxed{
V_{mathrm{sys}}
=
V_{mathrm{base}}PRCUA
}
]

and its recommended bounded form is

[
oxed{
V_{mathrm{sys}}
=
V_{mathrm{base}}
P^{w_P}
R^{w_R}
C^{w_C}
U^{w_U}
A^{w_A}.
}
]

The framework is intended not as a substitute for conventional appraisal but as an extension of it.

Where conventional valuation asks:

> What are these files worth?

systemic corpus valuation asks:

> What information-generating system would disappear if the corpus, its history, and its relationships ceased to exist?

That is often the more important question.

---

## Appendix A. Worked Multipliers

### X.com placeholder

[
P=1.30,quad
R=1.45,quad
C=1.60,quad
U=1.50,quad
A=0.80.
]

Therefore

[
S_X
=
PRCUA
approx3.62.
]

Hence

[
V_Xapprox3.62B_X.
]

### SpaceX placeholder

[
P=1.55,quad
R=1.80,quad
C=1.70,quad
U=1.90,quad
A=0.90.
]

Therefore

[
S_S
=
PRCUA
approx8.11.
]

Hence

[
V_Sapprox8.11B_S.
]

These are illustrative coefficients only.

---

## Appendix B. Evidence Discipline

The company names in this paper are placeholders for two different kinds of information systems.

No internal X.com or SpaceX data was used.

No claim is made that the illustrative corpus multipliers represent the actual internal information assets of either company.

Public enterprise valuations are not used as substitutes for corpus valuation. This distinction matters particularly for SpaceX, whose corporate structure and public-market valuation changed materially during 2026; the information corpus remains only one asset class within the enterprise.

The method should be empirically calibrated against real transaction, licensing, replacement-cost, and income data before being used for financial reporting or transaction pricing.
