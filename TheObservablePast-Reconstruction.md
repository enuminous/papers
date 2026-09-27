# Devs 2.0  
## Probabilistic Reconstruction of the Observable Past

### Matthew Chenoweth Wright  
Monolithic LLC / EFMW Research Program  
September 2026

## Abstract

This paper proposes a bounded version of the central technological idea dramatized by *Devs*: reconstruction of past physical events from information remaining in the present.

The strong version of this proposition—that an arbitrary past scene can be recovered exactly from its surviving quantum state—is not presently justified. Environmental interactions disperse information, observations are incomplete, and ordinary historical records do not preserve the complete quantum state of past events.

A scientifically tractable problem nevertheless remains.

Given a sufficiently well-observed historical event, can heterogeneous surviving measurements be combined with physical models to calculate a probability distribution over possible past scenes and then produce the image, or family of images, most consistent with all surviving evidence?

We call this approach **Devs 2.0**.

Rather than claiming to “see the past,” Devs 2.0 treats historical reconstruction as a constrained inverse problem. Images, telemetry, timestamps, geometry, physical models, later observations and other surviving evidence define a set of admissible histories. A Collapse Ω operator ranks candidate reconstructions according to their consistency with those constraints while explicitly retaining uncertainty where evidence is insufficient.

NASA's 2022 DART collision with the asteroid moonlet Dimorphos is proposed as an initial benchmark because the event possesses unusually rich observational coverage before, during and after impact.

The central principle is:

> **Do not reconstruct what the surviving evidence does not constrain.**

Under this formulation, the desired product is not a synthetic photograph falsely presented as historical fact. It is a probabilistic reconstruction accompanied by uncertainty, alternatives and provenance.

---

# 1. The Problem

Every physical event leaves consequences.

Light propagates away. Matter moves. Energy is transferred. Objects acquire new configurations. Instruments record measurements. Human observers produce photographs and descriptions. Later states of a system constrain what its earlier states could have been.

But these traces are incomplete.

The fundamental question is therefore not:

**Can we perfectly recover the past?**

It is:

**How much of a past physical state remains recoverable from information available now?**

This distinction transforms an extraordinary claim into an inverse problem.

Suppose a historical event produced some physical state \(X_t\).

At a later time we possess observations

\[
D=\{D_1,D_2,\ldots,D_n\}.
\]

We seek the posterior distribution

\[
P(X_t\mid D).
\]

The objective is not necessarily to recover one uniquely correct state.

Instead, we seek

\[
X^*=\arg\max_X P(X\mid D),
\]

together with the uncertainty surrounding that solution.

The output therefore becomes:

\[
\text{reconstruction}
+
\text{uncertainty}
+
\text{alternatives}
+
\text{provenance}.
\]

This is Devs 2.0.

---

# 2. Collapse Ω as Reconstruction Operator

In this context, **Collapse Ω** should not be interpreted as a demonstrated physical collapse law.

It is an inference operator.

Let \(\Gamma\) denote the space of candidate historical scenes consistent with some initial set of constraints.

Then:

\[
\Omega(D)=P(\Gamma\mid D).
\]

Each new observation reduces or reshapes the admissible state space.

Conceptually:

\[
\Gamma_0
\rightarrow
\Gamma_1
\rightarrow
\Gamma_2
\rightarrow
\cdots
\rightarrow
\Gamma_n.
\]

The process is therefore a progressive collapse of epistemic possibility rather than an assertion about physical wavefunction collapse.

The best-supported reconstruction is

\[
I^*=\arg\max_{I\in\Gamma_n} P(I\mid D).
\]

Importantly,

\[
P(I^*\mid D)<1
\]

will ordinarily remain true.

There are things the evidence simply does not determine.

Those uncertainties must survive into the final representation.

---

# 3. Why DART Is an Appropriate First Benchmark

On 26 September 2022, NASA's Double Asteroid Redirection Test spacecraft intentionally collided with Dimorphos, the moonlet of asteroid Didymos.

This event is unusually suitable for historical reconstruction.

The event was deliberately observed.

The spacecraft itself imaged Dimorphos during final approach.

Its trajectory and impact conditions were constrained by spacecraft navigation and telemetry.

The LICIACube spacecraft observed the impact aftermath from another geometry.

Space- and ground-based telescopes observed the ejecta and subsequent evolution of the system.

Later measurements constrain the consequences of the collision.

Thus the reconstruction does not begin with an unconstrained request such as:

> Show us what the impact looked like.

It begins with:

> Find the family of physical scenes simultaneously compatible with all available observations.

That difference is fundamental.

---

# 4. The Reconstruction Pipeline

A Devs 2.0 reconstruction can be divided into seven stages.

## 4.1 Evidence ingestion

Collect all admissible observations.

These can include:

- photographs;
- video frames;
- spacecraft telemetry;
- timestamps;
- spacecraft ephemerides;
- camera calibration;
- optical characteristics;
- illumination geometry;
- spectroscopic observations;
- later measurements;
- physical dimensions;
- orbital parameters;
- dynamical constraints.

Every datum retains its provenance.

---

## 4.2 Coordinate reconstruction

Observations from different instruments must be placed into a common physical coordinate system.

For each camera observation, the system estimates:

- observer position;
- orientation;
- field of view;
- optical distortion;
- exposure characteristics;
- observation time;
- illumination.

An image then becomes more than a picture.

It becomes a collection of geometrically constrained rays through a physical scene.

---

## 4.3 Candidate world generation

The system constructs candidate three-dimensional states compatible with the observations.

For the DART benchmark these might differ in:

- exact surface topology;
- impact-point geometry;
- ejecta particle distribution;
- velocity distribution;
- grain sizes;
- illumination;
- plume structure;
- unresolved surface regions.

This creates a possibility ensemble rather than one arbitrary reconstruction.

---

## 4.4 Forward physical simulation

Each candidate history is evolved through appropriate physical models.

For DART, this would include at minimum impact dynamics, ballistic ejecta evolution, gravitational effects and illumination.

The resulting candidate scene is then rendered from the viewpoints of the actual observing instruments.

---

## 4.5 Observation comparison

Synthetic observations are compared against real observations.

A candidate that resembles one photograph but contradicts another is penalized.

Likewise, a visually convincing candidate that violates telemetry or later dynamical observations must lose probability.

The target is therefore not visual plausibility.

It is **cross-modal physical consistency**.

---

# 5. Collapse

After evaluating the candidate ensemble, Collapse Ω identifies the most strongly constrained regions of the posterior.

The system can produce a maximum-posterior reconstruction:

\[
I^*.
\]

But that image alone is insufficient.

Every reconstructed region should carry a confidence estimate.

For pixel or region \(r\),

\[
C(r)=P(r\mid D).
\]

High-confidence areas are strongly constrained by observations.

Low-confidence areas admit many physically compatible alternatives.

The system therefore produces at least four products:

### Maximum-posterior image

The reconstruction most compatible with the total evidence.

### Confidence map

A spatial representation of how strongly each visible feature is constrained.

### Alternative reconstructions

Other scenes remaining statistically compatible with the evidence.

### Provenance map

For every reconstructed feature:

**Which observation caused us to believe this?**

---

# 6. The Anti-Hallucination Requirement

This is arguably the most important part of Devs 2.0.

Modern generative models are exceptionally capable of filling missing information.

Historical reconstruction requires precisely the opposite discipline.

Suppose no observation constrains the far side of Dimorphos at the moment of impact.

A generative system can easily invent a convincing rocky surface there.

But a convincing surface is not recovered information.

Therefore:

\[
\text{plausibility}\neq\text{evidence}.
\]

The system must preserve unresolved information as unresolved.

This gives Devs 2.0 its governing constraint:

> **Do not heal the parts of history that the evidence did not preserve.**

This principle emerged independently in the associated Borges Library and Backrooms Protocol experiments.

It becomes even more important here.

A beautiful invented pixel is still an invented pixel.

---

# 7. The Backrooms Constraint

The Backrooms Protocol provides an unexpected but useful epistemic component of the reconstruction architecture.

AI systems tend toward completion.

Incomplete patterns encourage inference.

Inference encourages narrative closure.

Historical reconstruction therefore creates an especially dangerous failure mode:

\[
\text{missing evidence}
\rightarrow
\text{plausible completion}
\rightarrow
\text{confidence}
\rightarrow
\text{false history}.
\]

The correct behavior is sometimes:

**UNKNOWN.**

Or:

**MULTIPLE STATES REMAIN CONSISTENT WITH THE DATA.**

Consequently, a successful Devs 2.0 architecture needs both a collapse operator and a **non-collapse operator**.

Collapse when evidence discriminates.

Preserve superposed hypotheses when it does not.

---

# 8. EFMW and the Zoo

EFMW's most useful role in this architecture is not to supply unknown historical information.

It is to audit reconstruction.

Different Zoo operations can attack different stages of the pipeline.

TORTOISE asks whether information from the desired reconstruction has been inadvertently inserted into the assumptions.

RAVEN asks whether unexplained residual structure actually remains after conventional models are applied.

HEDGEHOG asks whether reconstruction rules generalize to observations withheld during model development.

CAT removes components and determines whether they actually contribute information.

DRAGON identifies attractors in the reconstruction process—candidate explanations toward which the inference machinery repeatedly converges.

CHIMERA can preserve competing model families when the available evidence does not distinguish between them.

The Zoo therefore becomes an adversarial layer between reconstruction and publication.

No image should be labeled a Devs 2.0 reconstruction merely because it looks convincing.

It must survive attempts to prove that it is unjustified.

---

# 9. A Crucial Distinction: Quantum Information

The phrase “quantum reconstruction of history” requires considerable caution.

Quantum mechanics governs the physical evolution underlying the event.

That does not imply that the complete quantum state of a historical event remains practically available for reconstruction.

Photons are absorbed.

Environmental interactions generate decoherence.

Measurements preserve selected observables rather than complete universal states.

Information disperses into enormous numbers of uncontrolled environmental degrees of freedom.

Therefore this paper does **not** claim that Collapse Ω can presently reverse universal quantum evolution and retrieve arbitrary historical scenes.

The DART reconstruction instead uses surviving **classical measurement records produced by an underlying quantum universe**.

This distinction should remain explicit.

---

# 10. What Counts as Success?

The experiment must be prospective.

Some observations should deliberately be withheld.

Construct the reconstruction using dataset

\[
D_{\mathrm{train}}.
\]

Then ask the reconstructed world to predict observations

\[
D_{\mathrm{heldout}}
\]

that were never supplied to it.

A successful reconstruction should predict the withheld observations within predetermined tolerances.

This is substantially stronger than generating an image resembling photographs already provided to the system.

The key question becomes:

> If this reconstructed world were really the world that existed, would it have produced observations we deliberately hid from the reconstruction engine?

That is the central validation test.

---

# 11. Reconstruction Ladder

DART should be only the first rung.

The methodology can then be tested against increasingly information-poor historical events.

### Tier 1 — Instrument-saturated events

Spacecraft impacts, rocket launches, laboratory experiments and heavily instrumented astronomical events.

### Tier 2 — Multi-camera modern events

Events observed simultaneously from numerous independent locations.

### Tier 3 — Single-camera historical events

The system must infer substantially more geometry.

### Tier 4 — Photographic history

Multiple photographs but little telemetry.

### Tier 5 — Early photography

Sparse images and documentary evidence.

### Tier 6 — Pre-photographic history

Paintings, measurements, written descriptions, archaeology and surviving physical objects.

### Tier 7 — Ancient events

Only indirect physical and documentary constraints survive.

The prediction is straightforward:

\[
\text{historical distance}
\uparrow
\quad\Rightarrow\quad
\text{uncertainty generally}
\uparrow.
\]

But chronological age alone is not decisive.

A very old astronomical event may sometimes be better physically constrained than a poorly documented event occurring yesterday.

The true variable is surviving information.

---

# 12. The Information Horizon

This suggests a new concept:

## Historical information horizon

For any event \(E\), define the recoverable information as

\[
H(E,t)=I(E;D_t),
\]

where \(D_t\) represents evidence about event \(E\) still accessible at later time \(t\).

As evidence disappears, is destroyed, becomes inaccessible or was never recorded,

\[
H(E,t)
\]

generally decreases.

But later discoveries can occasionally increase accessible information.

An archaeological excavation, recovered archive or newly analyzed astronomical observation can constrain a historical state more tightly than was previously possible.

The past itself does not change.

Our posterior over the past does.

---

# 13. The Image

The accompanying experimental image should therefore not be interpreted as:

> This is what DART looked like.

It represents:

> This is an illustration of what the maximum-posterior visualization layer of a future Devs 2.0 system might produce.

A scientifically valid implementation would additionally expose uncertainty directly on the image.

Some regions could approach photographic certainty because an actual camera recorded them.

Other regions might be moderately constrained by geometry.

Still others would remain effectively unknown.

The final image should therefore contain visible epistemology.

---

# 14. From Photograph to Probability Field

This changes what an “image” means.

A conventional photograph maps approximately:

\[
(x,y)\rightarrow RGB.
\]

A Devs 2.0 reconstruction requires something richer:

\[
(x,y)\rightarrow
\{RGB,\;P,\;\sigma,\;\text{provenance},\;\text{alternatives}\}.
\]

Every pixel becomes a claim.

And every claim has evidence.

One could click a boulder in the reconstructed DART scene and ask:

**Why is this here?**

The machine might answer:

> Directly visible in DART frame X and consistent with LICIACube geometry. Confidence 0.97.

Another region might answer:

> Not directly observed. Surface realization sampled from configurations consistent with neighboring topology. Confidence 0.12.

That is radically different from ordinary generative imagery.

---

# 15. Devs 1.0 versus Devs 2.0

The fictional machine asks:

> What happened?

The scientific machine asks:

> What histories remain compatible with everything we know happened?

The fictional machine gives an image.

Devs 2.0 gives:

\[
\text{image}
+
\text{confidence}
+
\text{alternatives}
+
\text{evidence}.
\]

The fictional machine hides uncertainty.

Devs 2.0 makes uncertainty part of the display.

The fictional machine is omniscient.

Devs 2.0 is epistemically bounded.

And that limitation is not a defect.

It is what makes the project scientifically interesting.

---

# 16. Falsification

The framework can fail.

It fails if its reconstructed states systematically predict withheld observations worse than conventional reconstruction methods.

It fails if Collapse Ω contributes no measurable improvement over standard Bayesian inference, optimization, inverse rendering or data-assimilation techniques.

It fails if uncertainty estimates are poorly calibrated.

It fails if generated details repeatedly appear with greater confidence than the evidence warrants.

And stronger claims concerning quantum recovery fail unless experiments demonstrate information recovery unavailable to ordinary physical inference.

EFMW terminology must not exempt the architecture from comparison with existing methods.

Quite the opposite.

Those comparisons are the experiment.

---

# 17. Consequence

The interesting destination is therefore different from the original science-fiction fantasy.

We may never possess a machine capable of pointing at an arbitrary coordinate in spacetime and displaying exactly what occurred there.

But we can plausibly build machines that answer a more disciplined question:

> **Given everything the present universe still tells us about this moment, what can we responsibly reconstruct?**

For exceptionally well-recorded events, the answer may eventually approach photographic fidelity.

For poorly recorded events, the result may remain broad and uncertain.

For some questions the correct output will be no image at all.

That is not failure.

It is information.

---

# Conclusion

Devs 2.0 reframes historical observation as probabilistic physical reconstruction.

Collapse Ω is used not as a demonstrated mechanism for recovering lost quantum states but as a proposed inference operator over candidate histories.

EFMW supplies recursive comparison and audit structures.

The Zoo attempts to falsify the reconstruction.

Backrooms Protocol supplies the crucial principle that unresolved states must sometimes remain unresolved.

The resulting architecture is therefore:

**evidence → possibility space → physical simulation → observation matching → adversarial audit → probabilistic collapse / justified non-collapse → reconstruction + uncertainty + provenance.**

The first benchmark proposed here is the DART impact on Dimorphos because it offers unusually rich surviving constraints and multiple independent observing geometries.

The ultimate goal is not a machine that pretends to remember everything.

It is a machine capable of determining, with measurable confidence, **how much the universe still remembers.**

And perhaps that is the scientifically realizable fragment of *Devs*:

> **Not seeing the past perfectly, but calculating the boundary between the past that remains observable and the past that has become irretrievable.**
