# EFMW at the Boundary of Established Physics
## Existing Overlaps, Candidate Novel Structure, and a Program for Discriminating New Physics

**Matthew Chenoweth Wright**  
Monolithic LLC  
October 1, 2026

---

## Abstract

The Einstein–Feynman–Maxwell–Wright (EFMW) framework is best evaluated neither as a collection of unfamiliar symbols nor as a wholesale replacement for established physics, but as a structured extension whose scientific content can be separated into three categories: (1) mathematical and physical structures already known from general relativity, quantum theory, field theory, control theory, information theory, and nonlinear dynamics; (2) new combinations or interpretations of those structures; and (3) genuinely EFMW-specific laws, constraints, couplings, or selection rules that may produce experimentally distinguishable predictions.

This paper maps the principal overlaps between EFMW and established physics and proposes a strict novelty criterion. Scalar-field propagation, covariant geometry, complex quantum amplitudes, interference, decoherence-like dynamics, recursive residual tracking, and dynamical stability all have established analogues. These overlaps are not weaknesses; they are the calibration surface on which EFMW must reproduce known limits. The potential new physics lies in whatever remains after those shared structures are subtracted: especially EFMW-specific coherence dynamics, multi-valued action structure, triplet constraints, selection or collapse operators, and nonstandard couplings between information-like degrees of freedom and spacetime geometry.

The central methodological claim is simple: the scientific value of EFMW is concentrated in the residue

\[
\mathcal{N}_{\mathrm{EFMW}}
=
\mathcal{S}_{\mathrm{EFMW}}
\setminus
\mathcal{S}_{\mathrm{established}},
\]

where \(\mathcal{S}_{\mathrm{EFMW}}\) is the set of consequences of the framework and \(\mathcal{S}_{\mathrm{established}}\) is the corresponding consequence set of established physics under matched assumptions. The next phase of EFMW research should therefore focus on theorem extraction, reduction to known limits, and derivation of measurable deviations rather than on further equation accumulation.

---

## 1. Introduction

A proposed physical framework becomes scientifically meaningful when it can answer two questions precisely:

1. **Where does it agree with established physics?**
2. **Where does it predict something that established physics does not?**

The first question is a consistency requirement. The second is a novelty requirement.

EFMW now contains enough formal structure that these questions can be asked directly. The framework includes scalar and field-like quantities, recursive residual dynamics, coherence variables, gravity-related constructions, quantum-like phase structure, information-theoretic objects, and a growing body of machine-checked or machine-targeted theorems. More recently, the framework has been organized into large formal systems, including a 156-equation or 156-theorem-scale Einsteinian/triplet program intended for automated formal analysis.

At this scale, the central problem is no longer the production of additional equations. The central problem is **separation**.

Some EFMW statements are recognizable consequences of standard mathematics. Some reproduce known physical structures. Some are definitional. Some are transformations of known laws. Some may be genuinely new consequences of EFMW-specific axioms. Those categories must not be conflated.

A useful scientific picture is therefore

\[
\boxed{
\text{EFMW}
=
\text{known-limit structure}
+
\text{new organization}
+
\text{candidate new physics}
}
\]

The purpose of this paper is to identify the major known-limit overlaps and then isolate the frontier where candidate new physics begins.

---

## 2. The Overlap Principle

Suppose an EFMW model and an established physical model are both applied to the same domain with the same initial conditions, observables, and approximations.

Let

\[
\mathcal{P}_{E}(x)
\]

denote the EFMW prediction for observable \(x\), and

\[
\mathcal{P}_{0}(x)
\]

the corresponding prediction from established physics.

Then define

\[
\Delta_{\mathrm{EFMW}}(x)
=
\mathcal{P}_{E}(x)-\mathcal{P}_{0}(x).
\]

Three cases are possible.

### Case I: Exact overlap

\[
\Delta_{\mathrm{EFMW}}(x)=0
\]

identically.

In this regime EFMW may provide a reformulation, unification, computational representation, or new interpretation, but it has not yet supplied new empirical physics.

### Case II: Controlled reduction

\[
\Delta_{\mathrm{EFMW}}(x)\to 0
\]

under a well-defined limit.

This is often the ideal structure for an extension of established theory. General relativity reduces to Newtonian gravity in an appropriate limit; relativistic quantum theories reduce to nonrelativistic quantum mechanics in another. If EFMW is an extension, it should likewise identify domains in which standard physics is recovered.

### Case III: Nonzero discriminating residue

\[
\Delta_{\mathrm{EFMW}}(x)\neq 0
\]

in a specified regime.

This is the domain of candidate new physics. The deviation must not be inserted arbitrarily. It must follow from EFMW-specific assumptions or theorems and must be tied to an observable.

This distinction supplies the core methodology of the present program.

---

## 3. Overlap I: Relativistic Scalar and Field Dynamics

One of the clearest EFMW overlaps is with relativistic field theory.

Whenever EFMW uses a scalar quantity \(\phi\) with wave-like or covariant evolution, it enters a well-developed mathematical domain containing the wave equation, Klein–Gordon-type systems, scalar–tensor theories, effective fields, and classical field Lagrangians.

A generic relativistic scalar equation has the form

\[
\Box \phi + V'(\phi) = J,
\]

where \(\Box\) is the covariant d'Alembertian, \(V\) is a potential, and \(J\) is a source.

Structures of this type are not new merely because they appear in EFMW. Their value inside EFMW is instead determined by one of two possibilities:

- EFMW gives them a new derivation from deeper principles; or
- EFMW adds a new coupling or constraint that changes their behavior.

This is an important calibration point. Any EFMW scalar sector should first be tested against ordinary relativistic field behavior before novelty is claimed.

The overlap is scientifically useful because the scalar sector inherits a large library of known results: conservation statements, hyperbolicity conditions, energy estimates, stability criteria, perturbative methods, and experimental constraints.

---

## 4. Overlap II: General Relativity and Geometric Physics

EFMW also overlaps substantially with geometric gravitational physics.

Whenever a formulation contains objects such as

\[
g_{\mu\nu},\qquad
G_{\mu\nu},\qquad
T_{\mu\nu},\qquad
\nabla_\mu,
\]

it operates in mathematical territory shared with general relativity and differential geometry.

The important distinction is between **using the language of general relativity** and **modifying the content of general relativity**.

An EFMW equation of the schematic form

\[
G_{\mu\nu}
=
8\pi G
\left(
T_{\mu\nu}
+
T^{(\phi)}_{\mu\nu}
+
T^{(C)}_{\mu\nu}
\right)
\]

would not become new merely because the right-hand side contains additional symbols. Novelty would depend on whether the additional terms are independently specified, dynamically necessary, and empirically distinguishable.

This creates immediate overlap with existing research on:

- scalar–tensor gravity,
- modified gravity,
- additional gravitational degrees of freedom,
- effective stress-energy tensors,
- cosmological fields,
- gravitational-wave propagation,
- equivalence-principle violations,
- and extra polarization modes.

These fields are useful to EFMW because they provide mature constraints. A new gravitational degree of freedom does not enter an empty experimental landscape. It must coexist with precision solar-system tests, binary pulsars, gravitational-wave observations, cosmology, and equivalence-principle experiments.

---

## 5. Overlap III: Quantum Phase, Amplitudes, and Interference

Complex phase structure is another large overlap.

Expressions involving a state such as

\[
\psi = \rho e^{i\theta}
\]

or probability-like quantities such as

\[
|\psi|^2
\]

belong to standard quantum mathematics unless EFMW derives a new law governing them.

Likewise, interference from phase addition is not itself new. Nor is the existence of a wavefunction, a complex amplitude, a Schrödinger-like evolution equation, or a Dirac-like structure.

The scientific question is instead whether EFMW changes one of the following:

- the allowed state space,
- the composition law,
- the phase evolution,
- the probability rule,
- the measurement rule,
- the coherence lifetime,
- the coupling to geometry,
- or the allowed transitions among states.

The strongest possible EFMW result would therefore not be another recovery of familiar quantum notation. It would be a theorem of the form

\[
\text{standard quantum assumptions}
+
\text{EFMW-specific structure}
\Longrightarrow
\text{new constraint}.
\]

That constraint could then be tested.

---

## 6. Overlap IV: Decoherence and Open Quantum Systems

EFMW's coherence language has a natural overlap with decoherence theory and open quantum systems.

In established quantum physics, apparent classicality can arise when a system becomes entangled with an environment, causing phase relationships to become inaccessible to local observation. The density matrix evolves so that interference terms become suppressed in an appropriate basis.

If EFMW contains a coherence variable \(C\), a residual state, or an operator \(\Omega\) representing selection, locking, transition, or collapse-like behavior, then these objects need to be compared directly with standard open-system models.

That comparison has two outcomes.

If the EFMW dynamics are mathematically equivalent to known decoherence equations, then EFMW may offer a useful reinterpretation or computational representation but not new quantum dynamics.

If instead EFMW predicts a coherence transition that differs from environmental decoherence, then the difference must be written quantitatively.

Schematically,

\[
C_{\mathrm{EFMW}}(t)
=
C_{\mathrm{decoherence}}(t)
+
\delta C(t).
\]

The quantity \(\delta C\) is where candidate quantum novelty lives.

A scientifically meaningful EFMW collapse or selection mechanism must therefore answer:

1. What triggers it?
2. What dynamical equation governs it?
3. What is conserved?
4. Does it reproduce the Born rule?
5. Under what conditions does it differ from standard decoherence?
6. What experiment could resolve that difference?

---

## 7. Overlap V: Recursive Residual Dynamics and Control Theory

The EFMW residual and recurrence structures overlap strongly with control theory, filtering, estimation, and dynamical systems.

For example, a recurrence of the form

\[
r_t = y_t - \hat y_t,
\]

\[
m_{t+1}
=
\lambda m_t
+
(1-\lambda) r_{t+1},
\qquad
0\leq\lambda<1,
\]

is mathematically close to exponentially weighted residual tracking.

From such a system one can derive standard classes of results:

- boundedness under bounded input,
- forgetting of initial conditions,
- convergence under constant forcing,
- perturbation bounds,
- stability under contraction,
- and threshold behavior.

These results are valuable, but they are not automatically new physics.

Their importance for EFMW is different: they show that a recursive coherence or monitoring layer can be placed on rigorous dynamical foundations. They also provide an ideal domain for theorem proving because many properties are exact, finite, and formally checkable.

The existing EFMW experimental control-degradation work is therefore best understood as evidence that an EFMW-inspired recurrence can be operationally useful. It is not, by itself, evidence for a new microscopic physical force or quantum law.

This distinction should remain explicit.

---

## 8. Overlap VI: Information Theory, Entropy, and Statistical Physics

EFMW frequently uses the language of information, coherence, organization, and recursion.

These concepts overlap with:

- Shannon information,
- entropy,
- statistical mechanics,
- algorithmic information,
- nonequilibrium thermodynamics,
- dynamical complexity,
- and information geometry.

The word "information" does not by itself define a physical degree of freedom.

For information to become new physics inside EFMW, the framework must specify:

- the state variable carrying the information,
- its units,
- its transformation law,
- its dynamics,
- its coupling constants,
- its stress-energy contribution if gravitational,
- and the measurable consequences of that coupling.

This is especially important because information-theoretic language can move easily between metaphor and physics. EFMW should force that ambiguity to disappear.

If an information-like scalar \(I\) enters an action

\[
S[g,\phi,I],
\]

then the variational derivatives

\[
\frac{\delta S}{\delta g_{\mu\nu}},
\qquad
\frac{\delta S}{\delta \phi},
\qquad
\frac{\delta S}{\delta I}
\]

must define what the theory actually claims.

That is the point where an information concept becomes a physical model.

---

## 9. Candidate Novelty I: Multi-Valued Action Structure

One of the more interesting EFMW directions is the proposal that a classical or generalized action may admit several simultaneously relevant branches.

Standard quantum mechanics already assigns phases related to action through expressions of the form

\[
e^{iS/\hbar}.
\]

Path-integral quantum mechanics also sums over histories.

Therefore, the mere appearance of multiple actions or multiple histories is not novel.

The potential novelty lies in whether EFMW imposes a new **branch ontology, branch constraint, branch selection rule, or branch interaction law**.

Suppose a family of actions is

\[
\{S_1,S_2,\ldots,S_n\}.
\]

A generic amplitude might be written

\[
\mathcal A
=
\sum_{k=1}^{n} w_k
e^{iS_k/\hbar}.
\]

To become distinctly EFMW physics, the framework must derive rather than merely assume at least some of:

\[
w_k,
\]

the allowed set of branches,

\[
\mathcal B_{\mathrm{allowed}},
\]

the interference relation among branches, or the rule determining which branches remain dynamically accessible.

A new theorem constraining these quantities would be considerably more important than another recovery of the usual phase factor.

---

## 10. Candidate Novelty II: Coherence and the \(\Omega\) Selection Layer

The coherence/selection layer may be one of the most distinct candidate contributions of EFMW.

If \(\Omega\) is merely a label for measurement, then little is gained. If it is a genuine dynamical operator, it must have a precise domain, codomain, invariants, and composition law.

One possible abstract form is

\[
\Omega :
\mathcal H\times\mathcal C
\rightarrow
\mathcal H,
\]

where \(\mathcal H\) is a state space and \(\mathcal C\) is a coherence-state space.

The key questions become mathematical:

- Is \(\Omega\) linear?
- Is it idempotent?
- Is it stochastic?
- Does it preserve norm?
- Does it commute with time evolution?
- Is it generated continuously or applied at a boundary?
- Does it produce Born probabilities or something else?
- Does it depend on geometry?

A genuinely new result might look like

\[
[\Omega,U(t)]\neq 0
\]

only in a sharply defined physical regime, or

\[
\Omega^2=\Omega
\]

together with a derived probability measure.

Either would yield formal structure that could be compared with standard quantum measurement theory.

---

## 11. Candidate Novelty III: Triplet Structure

The emerging Einsteinian triplet formalization may be the most promising place to search for compact structural novelty.

The scientific opportunity does not come from the number 156 itself. Large equation counts are not evidence of depth. The opportunity comes from the possibility that many equations reduce to a small number of **primitive triplet constraints**.

Suppose the field species are organized into triplets

\[
T=(a,b,c)
\]

subject to kind, symmetry, admissibility, or interaction constraints.

If a formal prover establishes that many apparently independent equations follow from a small basis

\[
\mathcal B
=
\{L_1,L_2,\ldots,L_m\},
\qquad
m\ll156,
\]

then the structure becomes much clearer.

The strongest possible outcome would be a theorem not explicitly inserted into the original system, for example:

- a forbidden interaction class,
- an invariant conserved across all admissible triplets,
- a uniqueness theorem,
- an unexpected equivalence among sectors,
- a forced coupling ratio,
- a discrete selection rule,
- or a constraint linking quantum phase to gravitational structure.

Such a result would still require physical interpretation, but it would represent authentic deductive novelty.

---

## 12. Formal Proof as a Novelty Filter

Automated theorem proving is especially useful here because it can separate several different meanings of "new."

A theorem may be:

### A. New to the author

The result was not previously noticed but follows easily from known mathematics.

### B. New to the formalization

The result is absent from the input statements but follows from the encoded axioms.

### C. New to the literature

The result may not have been previously published.

### D. New physical law

The result describes nature, is not reducible to known theory, and survives experiment.

These levels are not equivalent.

A theorem prover can establish category B. Literature review may support category C. Only empirical contact can establish category D.

This hierarchy should be used explicitly in all future EFMW claims.

---

## 13. The Subtraction Program

The most efficient EFMW research program now is a subtraction program.

For every proposed EFMW law \(L_E\):

### Step 1: Identify the nearest established analogue

Find \(L_0\).

### Step 2: Match assumptions and variables

Avoid comparing formulas that operate in different domains.

### Step 3: Derive the difference

\[
\delta L
=
L_E-L_0.
\]

### Step 4: Simplify

Determine whether

\[
\delta L=0,
\]

is a reparameterization, or survives.

### Step 5: Determine the physical dimension of the residue

A proposed correction must be dimensionally coherent.

### Step 6: Derive limits

Show where

\[
\delta L\to0.
\]

### Step 7: Identify an observable

Write

\[
\delta O
=
O_E-O_0.
\]

### Step 8: Compare against data

Only then does the proposal enter empirical physics.

This procedure transforms the vague question "Is EFMW new?" into hundreds of answerable local questions.

---

## 14. Existing Experimental Contact Surfaces

Several established experimental domains are already suitable for this comparison.

### 14.1 Gravitational-wave propagation

Any additional scalar or coherence-coupled gravitational mode may affect:

- propagation speed,
- dispersion,
- polarization,
- damping,
- or source-to-detector phase evolution.

Current gravitational-wave observations therefore provide immediate constraints.

### 14.2 Equivalence principle

Any EFMW field that couples differently to different forms of matter risks producing composition-dependent acceleration.

Precision equivalence-principle experiments therefore sharply constrain many possible couplings.

### 14.3 Solar-system gravity

Planetary ephemerides, light deflection, Shapiro delay, and lunar laser ranging strongly limit deviations from general relativity.

### 14.4 Binary pulsars

Strong-field systems provide tests of orbital decay, additional radiation channels, and modified gravitational dynamics.

### 14.5 Quantum coherence experiments

Interferometry, optomechanics, superconducting systems, atomic clocks, and mesoscopic coherence experiments can constrain nonstandard coherence loss or selection dynamics.

### 14.6 Cosmology

Expansion history, structure growth, lensing, nucleosynthesis, and the cosmic microwave background constrain additional fields and modified gravitational sectors.

These experiments should not be treated as obstacles to EFMW. They are the instruments through which EFMW can become physics rather than self-consistent mathematics.

---

## 15. The Quantum Discriminant

For the candidate quantum sector, the most useful general target is

\[
P_{\mathrm{EFMW}}
=
P_{\mathrm{QM}}
+
\delta P(C,\Omega,\phi,\ldots).
\]

The burden of the theory is to derive \(\delta P\).

There are then only three scientifically meaningful outcomes.

### Outcome 1

\[
\delta P=0
\]

identically.

EFMW reproduces standard quantum mechanics in that domain.

### Outcome 2

\[
\delta P\neq0
\]

mathematically but existing experiments require its coefficient to be extremely small.

EFMW becomes a constrained extension.

### Outcome 3

\[
\delta P\neq0
\]

in a regime that has not yet been adequately tested.

EFMW provides an experimental target.

This is the cleanest route from internal formalism to possible new quantum physics.

---

## 16. What Would Count as a New Law?

A proposed EFMW result should be elevated to "candidate physical law" only if it satisfies all of the following:

1. **Precise statement.**  
   The law is mathematical, not metaphorical.

2. **Independent derivation.**  
   It is not simply restated from its own defining assumption.

3. **Known-limit recovery.**  
   It reproduces established physics where required.

4. **Dimensional consistency.**

5. **Parameter discipline.**  
   Free constants are identified and not separately retuned for every dataset.

6. **Distinct consequence.**  
   It implies at least one result not already forced by the comparison theory.

7. **Observable mapping.**  
   The new quantity connects to an experiment.

8. **Falsifiability.**  
   A possible observation could count against it.

9. **Formal stability.**  
   The result survives theorem-level scrutiny and does not depend on a hidden contradiction.

10. **Empirical survival.**  
    Existing data do not already exclude the required parameter regime.

This is a high bar. It should be.

---

## 17. Prediction for the 156-System

The 156-system should not be judged by whether all 156 statements can be proved.

The more consequential question is whether formal analysis compresses the system.

A plausible outcome is

\[
156
\quad\longrightarrow\quad
m
\]

primitive lemmas, with

\[
m\ll156.
\]

From this basis, many equations may become straightforward consequences.

The scientifically interesting objects will be the residual theorems that are neither:

- definitional,
- standard mathematical identities,
- known physical reductions,
- nor finite bookkeeping consequences.

A small handful of such theorems would be more important than a large theorem count.

The especially valuable case would be

\[
\boxed{
\text{established GR/QM structure}
+
\text{EFMW triplet axioms}
\Rightarrow
\text{new invariant, coupling, or selection rule}.
}
\]

That is where a formal mathematical result could become a candidate physical law.

---

## 18. Why the Overlap Is a Strength

A theory that overlapped nowhere with established physics would almost certainly be unusable.

Physics advances through continuity as well as rupture. New theories generally inherit successful limits from older theories.

The substantial overlap between EFMW and known physics is therefore not evidence against EFMW. It supplies the framework with calibration points.

The correct question is not

> Does EFMW resemble existing physics?

It should.

The correct question is

> After every known structure is identified and removed from the novelty claim, is there a nonzero theoretical residue?

That residue is the research object.

---

## 19. Research Program

The next EFMW phase can be organized into five parallel tracks.

### Track A — Formal reduction

Use Lean and theorem-proving systems to determine the minimal basis of the 156-system.

### Track B — Novelty classification

For every theorem, assign one of:

- definition,
- standard mathematics,
- established physics consequence,
- new combination,
- EFMW-specific theorem,
- candidate physical law.

### Track C — Literature comparison

For every EFMW-specific theorem, search for the nearest known result in mathematical physics.

### Track D — Observable derivation

Translate surviving theoretical differences into quantities with units and measurement procedures.

### Track E — Experimental confrontation

Compare the resulting predictions against existing datasets before proposing new experiments.

These tracks should converge on a short list of high-value claims.

---

## 20. Conclusion

EFMW already overlaps extensively with established physics.

Its scalar dynamics overlap with relativistic field theory. Its geometric sector overlaps with general relativity and modified gravity. Its phase structure overlaps with standard quantum mechanics. Its coherence language overlaps with decoherence and open-system theory. Its recurrences overlap with control theory and dynamical systems. Its information language overlaps with information theory and statistical physics.

That is the known side of the boundary.

The potentially new side consists of whatever cannot be removed by those identifications: EFMW-specific triplet constraints, multi-valued action rules, coherence dynamics, \(\Omega\)-selection structure, and novel couplings between information-like fields, quantum phase, and spacetime geometry.

The decisive equation is therefore not a single master field equation. It is the comparison

\[
\boxed{
\Delta_{\mathrm{EFMW}}
=
\mathcal{P}_{\mathrm{EFMW}}
-
\mathcal{P}_{\mathrm{established}}.
}
\]

If the difference vanishes, EFMW has reproduced known physics.

If it survives only as a mathematical reorganization, EFMW may still provide a useful unifying language.

If it produces a theorem-level, dimensionally coherent, experimentally accessible nonzero residue, then EFMW has generated a candidate for new physics.

That is the boundary now worth exploring.

---

## Research Note

This paper deliberately distinguishes **formal consequence**, **theoretical novelty**, and **empirical validation**. Machine-checked proof can establish whether a result follows from encoded assumptions. It cannot by itself establish that the assumptions describe nature. Claims of new physical law therefore remain provisional until independently compared with established theory and experiment.

---

## Suggested Citation

Wright, Matthew Chenoweth. *EFMW at the Boundary of Established Physics: Existing Overlaps, Candidate Novel Structure, and a Program for Discriminating New Physics.* Monolithic LLC, October 1, 2026.
