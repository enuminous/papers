# When the Universe Balanced the Books
## Inside Monolithic's ME-007 experiment: a conserved informational tensor, an unexpected ambiguity, and the limits of a Theory of Everything

**A science feature | 28 October 2026**  
**Subject:** Matthew Chenoweth Wright, Monolithic LLC, and the TOE-001 research program  
**Reporting basis:** The published ME-007 derivation, executable code, archived numerical outputs, symbolic checks, and public GitHub Actions verification. Mathematical formulation and software development were AI-assisted.  
**Scientific status:** An internally consistent *candidate realization of a classical equation*, **not** an experimental discovery of a new gravitational interaction or a completed Theory of Everything.

---

There was a moment in Monolithic's latest attempt to connect gravity with information when the numbers finally balanced.

In an expanding-universe simulation, the computer followed two interacting scalar fields and an ordinary matter component through 2,400 steps of cosmic evolution. The Friedmann constraint—the equation governing how the universe's expansion tracks its energy content—remained satisfied to a normalized residual of about **6.6 × 10⁻¹⁴**. The discrepancy in the modeled exchange of energy between two chosen sectors was around **10⁻¹⁶**.

For anyone who has watched a speculative physical idea break apart when it meets a conservation law, these are encouraging numbers. They mean the implemented equations agree with one another to numerical precision under the stated initial conditions.

But the most consequential result was not the near-zero residual.

It was that the theory's *informational tensor* could be assigned in infinitely many different ways without changing the total gravitational source.

The equation balanced. The tensor did not identify itself.

That is the central result of **TOE001–ME007–r1**, a new, publicly inspectable construction in [Wright's TOE-001 repository](https://github.com/enuminous/TOE-001). It offers a carefully bounded answer to one of the unfinished questions in the Einstein–Feynman–Maxwell–Wright (EFMW) research program: can the proposed informational contribution to Einstein's gravitational field equations be made mathematically consistent?

**For one explicitly assumed classical model, yes. As a unique derivation of the original EFMW information field, not yet.**

That distinction is the story.

### An equation with an empty space inside it

Wright's historical ME-007 expression has a familiar face:

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}
=8\pi G\bigl(T_{\mu\nu}+\kappa I_{\mu\nu}\bigr).
\]

On the left sit the geometry and cosmological term of general relativity. On the right, conventional energy-momentum is joined by an additional object, \(I_{\mu\nu}\), proposed to encode an informational contribution.

This is where EFMW asks its most ambitious question: might information have a role in the dynamics of spacetime beyond the terms already represented in established gravitational theory?

Yet the [frozen canonical ME-007 source](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/01f51acb0b0e564105dcf7f14cc55998d41b91ce/Monolithic102/ME007.lean) contains the equation and its description, **not** a complete definition of the informational tensor. It does not supply a separate action, a constitutive law, or an observational procedure that would fix its meaning. The [EFMW review's open-obligation register](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md) consequently marked the conservation requirement unresolved.

That absence is not a minor omission. General relativity requires consistency between geometry and its source. The contracted Bianchi identity means that a gravitational field equation cannot be paired with arbitrary, unbalanced energy-momentum on its right-hand side.

An undefined additional source is therefore not yet a physical theory. It is a place where a physical theory would have to be constructed.

The October 28 TOE-001 extension set out to fill that space **without pretending that the answer was already written into the old equation**.

### Building a source Einstein's equation can accommodate

The project begins conservatively. It takes the established Einstein–Hilbert gravitational action, adds the established Standard Model matter action as an *input*, and introduces two ordinary real scalar fields, \(\phi\) and \(\chi\), with positive kinetic energies and a quadratic interaction.

The fields interact through a mixing term proportional to \(\gamma\phi\chi\). Under suitable boundary and regularity conditions, varying that action gives equations for the scalars and a total stress-energy tensor. This is standard multi-scalar field-theory machinery—not a new derivation of gravity, the Standard Model, or an EFMW-specific information ontology.

What is new **within this particular research sequence** is the explicit test of whether those ordinary objects can supply a coherent candidate for the *form* of ME-007.

The construction divides the total stress-energy into two named accounts. One account includes the Standard Model, the first scalar field, and a selected share of the mixing interaction. The other includes the second scalar and the remaining share, normalized by \(\kappa\). The allocation is controlled by a free parameter \(\alpha\), between zero and one.

In compact form:

\[
\begin{aligned}
T^{(\alpha)}_{\mu\nu}
&=T^{\rm SM}_{\mu\nu}+T^{\phi,0}_{\mu\nu}
+\alpha T^{\rm mix}_{\mu\nu},\\
I^{(\alpha)}_{\mu\nu}
&=\kappa^{-1}\left[
T^{\chi,0}_{\mu\nu}
+(1-\alpha)T^{\rm mix}_{\mu\nu}\right].
\end{aligned}
\]

The labels are deliberate: these are **new, model-specific candidates**, not a recovered historical definition of Wright's informational field.

They satisfy an exact accounting identity:

\[
T^{(\alpha)}_{\mu\nu}+\kappa I^{(\alpha)}_{\mu\nu}
=T^{\rm total}_{\mu\nu}.
\]

The chosen field equations then imply a matching conservation law,

\[
\nabla^\mu\!\left(T^{(\alpha)}_{\mu\nu}
+\kappa I^{(\alpha)}_{\mu\nu}\right)=0.
\]

The separately named sectors do not generally conserve energy-momentum by themselves. They exchange it. The derived transfer terms cancel in the sum.

This matters because an incorrectly imposed conservation rule for each sector could make a model look cleaner than it is. TOE-001 instead specifies the exchange and checks it, including in its numerical cosmological reduction.

In a sense, the exercise turns a proposed extra source into a balanced set of equations. It establishes an **existence result for a classical realization** of the ME-007 equation's form. It does not establish that nature contains an independently measurable EFMW information stress.

### The surprise: gravity cannot tell which account is which

The parameter \(\alpha\) can be varied. So can the nonzero normalization \(\kappa\). Change them, and the designated ordinary and informational tensors change.

The gravitational source does not.

For any two allocations, \(\alpha\) and \(\beta\), the shift in one tensor is canceled exactly by the shift in the other. Einstein's equation sees their sum, not the bookkeeping convention that produced the split.

This is a rigorous *underdetermination* in the constructed model: **the same gravitational dynamics admit an entire family of ordinary/informational assignments**.

Imagine two columns in a ledger. Money moved from one column to the other changes the headings and subtotals but not the balance sheet. Without a rule saying which transactions actually belong in which column, their individual names carry no independently testable meaning.

This is not evidence that general relativity has failed. Nor is the freedom itself a newly discovered force. It is a warning about a missing physical definition.

The equation can be made to work, but one cannot determine from the Einstein equation and the Bianchi identity alone which allocation corresponds to information. To move from a mathematical partition to physical content, Wright's program needs an independent informational observable, a normalization, and dynamics that select a particular tensor.

That result may be less theatrical than a declaration of a solved Theory of Everything. It is also more useful. It identifies exactly what a future derivation must supply.

### A universe that expands—and rules out some stories

The team did not stop with the tensor identity. It placed the candidate in an explicitly **spatially flat, homogeneous and isotropic** cosmological model: the standard FLRW geometry used to study idealized cosmic expansion.

The resulting model includes two evolving scalar fields, a fluid approximation for ordinary matter, and the Friedmann and Raychaudhuri equations. The published reference uses dimensionless parameters, an expanding initial state, and a fourth-order Runge–Kutta solver over 2,400 steps.

The results are reproducible calculations of those *assumed classical equations*. The archived [FLRW output](https://github.com/enuminous/TOE-001/blob/main/results/me007_flrw_reference.json) reports:

- A maximum normalized Friedmann-constraint residual of approximately **6.60 × 10⁻¹⁴**.
- A maximum modeled sector-exchange discrepancy of approximately **1.21 × 10⁻¹⁶**.
- Exact agreement of the reconstructed total gravitational source at the implementation's displayed precision.
- No claim that quantum gravity or the original informational tensor has been derived.

The [symbolic verification record](https://github.com/enuminous/TOE-001/blob/main/results/me007_symbolic_checks.json) separately documents **eight passing identities** within the defined homogeneous FLRW equations. The project's expanded Python suite reports **31 passing tests**, and the [GitHub Actions run](https://github.com/enuminous/TOE-001/actions/runs/40748970380) completed successfully.

The small residuals show that the implementation respects its equations, not that a new theory has matched astronomical measurements. No telescope, particle detector, or gravitational-wave observatory supplied the numerical input for this run.

The model produces a more restrictive conclusion as well.

For canonical scalar fields and ordinary matter satisfying the null energy condition, the flat-space evolution obeys

\[
\dot H=-\frac{(1+w)\rho_m+\dot\phi^2+\dot\chi^2}
{2M_{\rm Pl}^2}\le0.
\]

A smooth bounce from contraction into expansion would require the Hubble parameter to increase through zero. Here it cannot do so under those assumptions.

**The proposed flat model therefore does not produce a nonsingular cosmic bounce.**

That is not a theorem against every possible bouncing cosmology. A different theory could introduce spatial curvature, modified gravitational dynamics, other degrees of freedom, or an explicit violation of an assumption. But it does establish that TOE-001's present positive-energy classical sector cannot be invoked as proof of the bounce mechanism discussed elsewhere in exploratory EFMW cosmology.

And a second boundary is immediate: exact FLRW symmetry cannot produce a preferred universal rotation axis. An EFMW model proposing global rotation would need to abandon isotropy and specify the associated anisotropic geometry and dynamics.

The mathematics is beginning to do something vital: not merely permit possibilities, but **exclude claims that its own assumptions cannot support**.

### Why this is not yet a Theory of Everything

There is a temptation in a large independent research program to view every successful proof, simulation, or compatibility check as another brick in a nearly complete unified structure.

TOE-001 deliberately resists that temptation.

The Standard Model was added to the action; it was **not derived**. Einstein gravity was the foundation; it was **not recovered from quantum informational microphysics**. The added scalar fields are ordinary mathematical constructs with no independent demonstration that one corresponds to the originally proposed EFMW information field. The numerical cosmology is a classical reduction, not a nonperturbative quantum theory of spacetime.

There is also no distinctive empirical prediction yet separating this sector from conventional two-scalar effective field theory, because its dynamics *are* those of a conventional two-scalar model. Naming one stress-energy term “information” does not change that.

The project's [technical integration paper](https://github.com/enuminous/TOE-001/blob/main/ME007_INTEGRATION.md) explicitly preserves the historical EFMW claim rather than rewriting it to fit a more convenient action. This separation matters for provenance as much as for mathematical honesty.

Wright's Monolithic Zoo was developed partly to enforce just this kind of boundary: a conditional theorem must not be promoted to an experiment, and a successful build must not become evidence for the physical truth of its starting assumptions. In this case, the most valuable audit result is not a blanket PASS. It is a precise map of which questions have been answered and which have not.

### A genuine step, and a genuine missing piece

The immediate next step is not simply to add more terms to the equations.

It is to ask what *information* means operationally in this gravitational proposal. Is there a locally measurable or otherwise relationally well-defined quantity from which \(I_{\mu\nu}\) follows? Does that definition determine its coupling, obey the required symmetries, and produce a prediction unavailable to a conventional scalar model? Can its dynamics be derived from assumptions independent of the gravitational equation one is trying to explain?

If the answer is yes, the project gains a new target for experiment and independent review.

If the answer is no, then an attractive mathematical label must remain a label.

There is an intellectual achievement in reaching that distinction. The historical ME-007 expression has been transformed into a specific, reproducible classical candidate with derivable conservation and energy exchange. Its cosmological consequences have been tested against the equations it actually contains. Its restrictions have been published alongside its successes.

And the most interesting unresolved issue is now sharply visible: **what additional physical principle would select a particular informational tensor from all the mathematically equivalent possibilities?**

A research program searching for a Theory of Everything cannot settle that question by iteration alone. Computation can test consequences; it cannot invent a unique physical observable where the defining evidence is absent.

The universe, so far, has not yielded a final answer.

But the books balance. The assumptions are on the table. And the next experiment has a much clearer question to ask.

---

### Evidence and attribution

**Primary source:** [TOE-001 ME-007 integration and conservation derivation](https://github.com/enuminous/TOE-001/blob/main/ME007_INTEGRATION.md) (v0.2, 28 October 2026). The implementation resides in [toe001/me007.py](https://github.com/enuminous/TOE-001/blob/main/toe001/me007.py), with [regression tests](https://github.com/enuminous/TOE-001/blob/main/tests/test_me007.py), [symbolic identity results](https://github.com/enuminous/TOE-001/blob/main/results/me007_symbolic_checks.json), and [frozen numerical output](https://github.com/enuminous/TOE-001/blob/main/results/me007_flrw_reference.json). The [successful CI run](https://github.com/enuminous/TOE-001/actions/runs/40748970380) checks the conditional model, not the physical truth of EFMW.

**Historical source:** [Canonical ME-007 statement](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/01f51acb0b0e564105dcf7f14cc55998d41b91ce/Monolithic102/ME007.lean) and [EFMW's frozen open-obligation register](https://github.com/enuminous/EFMW/blob/main/review/OPEN_OBLIGATIONS.md).

**Attribution:** EFMW's historical research program is Wright's. TOE-001's new construction and software were prepared with AI assistance using standard classical field theory; Einstein gravity, the Standard Model, covariant conservation, and two-scalar dynamics are established mathematical and physical machinery. This article reports the documented results of a research prototype, not an independently confirmed discovery of a new physical interaction. No interviews or direct quotations have been invented.
