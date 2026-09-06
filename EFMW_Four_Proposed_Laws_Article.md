# Four Proposed Laws, One Demand: Let Nature Decide
*Inside Matthew Chenoweth Wright’s EFMW project, mathematical auditing is bringing four ambitious ideas into sharper focus.*

A wave crosses a laboratory. A galaxy moves through curved spacetime. The universe expands. A machine continually revises its estimate of what is happening around it.

These seem like separate stories. Within the EFMW Physics Project, developed by Matthew Chenoweth Wright of Monolithic LLC, they become four places to investigate a larger question: can a connected mathematical framework say something useful about both physical fields and systems that track changing conditions?

The project’s supplied Aristotle audit catalogs 156 theorem declarations across 12 Lean modules. Within that inventory, four candidate-law families appear, labeled L1 through L4. They concern scalar-wave propagation, a proposed extension to gravity, a correction to cosmic expansion, and the dynamics of coherence.

Their scientific interest lies in what they require us to calculate, distinguish, and measure. The audit also makes their unequal status clear: some results follow directly from definitions, some connect previously separate equations, and some describe possible experimental consequences of physical assumptions.

The descriptive names used here explain those four families; the audit does not supply official long-form law names or every underlying equation.

**L1: A proposed rule for scalar-wave propagation**

Imagine watching a procession of wave crests pass a detector. Their spacing and rate of arrival tell you how quickly the pattern travels.

EFMW’s first candidate concerns that relationship for a proposed scalar field—a quantity assigned a value at each location, rather than a direction. The audit identifies a result establishing when a plane wave solves the written field equation, followed by a result for its phase speed. A parameter called alpha enters the model’s speed relation.

That creates an experimental question. If alpha takes a specified value, how far should the predicted speed depart from the reference value? How precise must a measurement be to distinguish them?

The audit lists deductions that turn speed measurements into parameter bounds, and others that address whether sufficient measurement precision could separate competing predictions. This is the route from an equation on a page to an experiment someone can design.

There is an essential distinction: phase speed describes the movement of a wave’s crests. A claim about information travelling faster than light requires further analysis of signal propagation and causality. A phase-speed result alone does not settle it.

The audit also identifies familiar mathematical ancestry: the equation belongs to a known class of anisotropic or Lorentz-violating kinetic models. Modified propagation relations already have an extensive research literature. EFMW would need to establish why its particular parameter and physical interpretation are necessary, and what distinctive observation follows. [Background: research on modified dispersion relations](https://arxiv.org/abs/1110.2720).

For L1, the prospect is concrete: a physical hypothesis whose consequences might become measurable. Its next challenge is to specify the field, its interaction with a detector, and the conditions under which the speed prediction applies.

**L2: A proposed connection between a scalar field and gravity**

Gravity presents a different challenge. General relativity ties spacetime geometry to the energy, momentum, and stresses of matter. Altering that relationship means altering a tightly connected mathematical structure.

The second EFMW candidate introduces what the project calls the Wright tensor. In the audit’s shorthand, it decomposes as:

I = Tφ + Ric.

Here Tφ denotes the scalar-field stress contribution, while Ric denotes Ricci curvature. The audit identifies an algebraic equivalence involving the modified gravitational equation and a check that switching off a coupling recovers the unmodified equation.

Think of modifying a bridge design. Showing that the old design returns when the new component is removed is a useful check. The bridge with the new component still needs its own structural analysis.

For gravity, that analysis includes covariance, compatible units, the number of independent dynamical quantities, and conservation requirements associated with the Bianchi identity. These are part of what makes a gravitational theory physically coherent. [Background: Sean Carroll’s general relativity lectures](https://preposterousuniverse.com/grnotes/).

The audit explicitly leaves these tasks open. Its algebraic result does not yet derive the extension from an action—a mathematical principle from which equations of motion can be obtained.

L2 therefore supplies a proposed structural connection. To mature into a physical law, it needs a consistent theory around that connection and a prediction that differs observably from existing gravity models.

**L3: An extra term in the expansion of the universe**

The third proposal takes the discussion to the largest scale.

The audit describes an addition to the Friedmann expansion equation proportional to:

Ω_U² / a²,

where a is the cosmic scale factor and Ω_U is the model parameter associated with the proposed rotation interpretation.

For fixed values of the other quantities, the square makes this contribution nonnegative. The ledger records consequences of that modification and deductions connecting expansion measurements to bounds on the parameter.

But this proposal comes with a particularly instructive ambiguity.

In the equation’s stated convention, if Ω_U is constant, the extra term can be absorbed into a redefined spatial-curvature parameter:

k_eff = k − Ω_U².

Two differently described models can then produce the same background expansion equation. One description speaks of an added contribution; another speaks of different curvature.

It is like hearing the same musical note from behind a curtain. The pitch alone may not tell you which instrument produced it.

This matters because fitting an expansion history would not, by itself, establish cosmic rotation. The audit specifically identifies this degeneracy. The role of curvature in the standard expansion equation is covered in conventional cosmology treatments. [Background: David Tong’s cosmology lectures](https://davidtong.org/teaching/cosmology/).

A discriminating test would need an additional observable that the full EFMW model actually predicts and that cannot be reproduced by changing curvature alone. Direction-dependent effects might be a subject to investigate, but the audit does not establish such predictions.

L3’s immediate contribution is consequently both a proposed correction and a clear warning about what that correction cannot uniquely identify.

**L4: How a system approaches coherence**

The fourth family moves from cosmology to systems that evolve and maintain internal estimates.

Picture a robot trying to track a moving target. Its internal estimate and the target’s actual position initially disagree. If the tracking dynamics make that mismatch approach zero, a coherence score constructed from the mismatch can approach its maximum.

The audit identifies cross-sector deductions of this kind: tracking implies asymptotic coherence, a specified self-model tends toward full coherence, and perfect coherence produces no warning under the encoded criterion.

It also identifies a connection between two EFMW equations, ME-024 and ME-025, through a quartic double-well gradient flow.

The intuitive picture is a ball descending into one of two valleys. The landscape determines the direction of movement and the available resting places. Such double-well and gradient-flow structures have established uses in phase-transition models and computational methods. [Background: Allen–Cahn gradient-flow research](https://arxiv.org/abs/2010.14556).

EFMW’s possible contribution here is the precise connection among its chosen dynamics, score, and warning rules. The audit classifies several of those connections as potentially original within the corpus.

That could be useful engineering. An explicitly defined monitor is easier to inspect: what does it measure, when does it warn, and which failure modes fall outside its field of view?

Yet agreement between an internal estimate and its target variable does not automatically establish the truth of every claim a system makes. Likewise, a theorem that a warning vanishes at perfect coherence does not show that every dangerous condition will be detected.

L4’s practical test is whether those mathematical relationships support useful, reliable monitoring on systems and data beyond the definitions themselves.

**What the four proposals have in common**

The most revealing feature of this work is the audit’s refusal to treat every theorem as the same kind of achievement.

A theorem can establish that a deduction follows from assumptions. Testing whether those assumptions describe the world is another task. Lean provides machinery for checking formal proofs and tracking their logical foundations; it does not supply experimental observations. [Background: Lean’s account of axioms and computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/).

The supplied ledger is an audit of theorem declarations. This article does not independently certify their compilation or proof dependencies.

Within that boundary, a recognizable research program emerges. L1 asks for a propagation experiment. L2 asks for a complete, consistent gravitational formulation. L3 asks for a way to distinguish an extra cosmic contribution from curvature. L4 asks whether formally related scores and dynamics make better monitors.

For Wright and Monolithic, these are four routes from mathematical ambition toward scientific accountability.

The decisive moment for any of them will arrive when someone can state, before looking at the result, what should happen—and what outcome would make the proposal fail.

*Primary source: “Aristotle EFMW Lean — 156-Theorem Total Novelty / Relativity / Axiom Audit,” supplied by the project. L1: entries 100–106, 109, 127–128; L2: 130–132; L3: 46–48, 107–108; L4: 10, 136–138. Descriptive labels and analogies are editorial explanations.*

