# A Field That Remembers: Inside the Wrightian Tensor Laboratory

*An EFMW browser laboratory turns recursive coherence and golden-ratio scaling into experiments whose behavior, assumptions and failures can be inspected.*

**Research feature · November 4, 2026**  
**Prepared for Matthew C. Wright / Monolithic, with AI assistance**

Two patches of color face one another across a dark grid. Press Run, and the field starts to change. Arrows trace a calculated flow of energy. A second field follows behind, tracking what the first is doing. Alongside the animation, a matrix updates its account of energy and stress.

The scene belongs to the **Wrightian Informational Tensor Dynamics Laboratory**, a new computational instrument in Matthew C. Wright’s EFMW research program. Published in the `enuminous/Information-Tensor` repository, it brings selected equations, explicit modeling assumptions, a semantic workbench and reproducibility tools into one browser interface. Its first experiments expose a consequential tension: a literal-gain recursive map grows enormously, while a bounded alternative can erase almost all of its spatial variation.[^1]

That tension gives the laboratory its story. A mechanism can remain finite and still become uninformative. A picture can remain vivid while the numbers underneath it shrink. A numerical check can pass while the proposed physical interpretation remains unresolved. Here, those differences are available for a reader to examine.

The release contains 51 files, including the interactive application, shared browser and command-line engines, sample results, documentation and automated checks. It can be downloaded and opened locally without an API key or an external language model. The published code makes the behavior accessible to inspection at the level of an individual grid cell, an equation or a replayable experiment.[^1]

At the center of the simulation is a scalar field, called **q** in the software. A scalar assigns one number to each location. The laboratory evolves that field across a two-dimensional periodic grid: the edges wrap around, so a pattern reaching one boundary encounters the opposite side. Its dynamics include wave propagation, a potential, damping and configurable forcing.

A second field, **m**, supplies the tracking memory. It follows q at a chosen rate. When the field changes, the memory can lag behind; when conditions settle, the two can draw closer. Their difference becomes a measurable model gap. A separate coherence variable, **Phi**, responds to field–memory discrepancies and helps control recursive feedback. The structure gives operational meaning to the idea of a system responding partly through an internal representation of its own state.[^2]

The word “memory” has a precise computational meaning here: a state variable with a specified update rule. Likewise, coherence is an evolving mathematical quantity, not a percentage or a certified measure of intelligence. It can exceed one. A low model gap can indicate close tracking, but a field that has become nearly constant can also be easy to track. The interpretation depends on what the system is being asked to accomplish.

The animated display adds another complication. Its colors automatically rescale. In a signed field view, blue represents negative values, dark tones sit near zero, and cyan through gold marks positive values. The image can retain strong contrast even when its absolute amplitude is small. Reading the colorbar and the numerical diagnostics is part of reading the experiment.

The tensor panel provides a more structured account. The laboratory calculates a four-by-four informational tensor from the field’s motion, spatial gradients and potential, then adds an explicitly chosen contribution from the tracking memory. The first component, I₀₀, has the role of an energy density within that model. Other components describe energy flux and stresses. A pointer over the grid changes the panel from a spatial average to the selected cell’s values.[^2]

The four coordinates are time and three spatial directions, although the simulated fields vary across only two of those spatial directions. The background geometry is fixed and flat. No evolving spacetime curvature is being calculated. The tensor is a derived quantity evaluated from the fields, with its physical interpretation conditional on the model’s assumptions.

This is where the laboratory also makes an unresolved part of the EFMW source material concrete. The canonical Wright informational tensor includes a residual term, R_ab. To run an experiment, that term needs a definition. This release chooses a multiple of the tracking memory’s scalar stress tensor. It documents that choice as a new laboratory closure—a supplied rule that completes this particular model—rather than attributing a fully specified residual dynamics to the original catalogue.[^3]

Because the memory follows a relaxation law, its stress need not be conserved by itself. The interface therefore distinguishes the scalar field’s energy balance from the behavior of the total informational tensor. One diagnostic compares the field’s actual finite-step energy change with the calculated work done by forcing and damping. Another estimates a local energy-divergence quantity. The two answer different questions, and neither establishes general curved-spacetime conservation.

The most dramatic behavior comes from the third state, **h**, which carries the Scalar-23 recurrence. The canonical coefficient is the golden ratio raised to the twenty-third power, approximately 64,079. The phi-13 coefficient is approximately 521. In this source convention, 23 is an exponent; it does not identify a supplied set of 23 physical coordinate axes.[^3]

The implemented recurrence applies phi-weighted averaging, phase synchronization, threshold-based pruning, a spatial prefix-memory operation and sinusoidal feedback. The interface offers a single recursion or a cycle of 23. Those controls advance h without advancing the physical-model time of the field. When scalar coupling is enabled, the bounded map also participates in subsequent field steps through an explicit feedback term.[^2]

Two modes expose the consequences of the scaling choices. **Literal mode** retains the large phi-13 and phi-23 gains. **Bounded mode** replaces those gains with normalized forms and applies a saturating function. That modification changes the mathematical model; it is not merely a more accurate way to calculate the same recurrence. The laboratory’s spatial operations are also a documented two-dimensional adaptation of an earlier computational implementation, not a claim to reproduce every detail of its original array behavior.[^2][^3]

In the recorded 24-by-24-grid example, 23 literal recursions produce a root-mean-square amplitude of approximately **4.26 × 10⁶³**. The bounded version finishes near **0.972**, but with spatial variation reduced almost to floating-point roundoff. One trajectory exhibits extreme growth; the other approaches a nearly uniform state.[^4]

Those results belong to the specified implementation and starting conditions. They do not settle the behavior of every possible Scalar-23 construction. They do, however, defeat a simple reading of this demonstration as automatically stable, information-preserving dynamics. Saturation has solved the finite-amplitude problem in the bounded example while leaving a different question: what useful distinctions survive?

![Recorded numerical results: literal and bounded recursion, conservative-wave energy drift, a text-driven field, and matched model comparisons.](https://raw.githubusercontent.com/enuminous/Information-Tensor/694b3f132e0cd451295a5dbba346859e9e070dd1/results/overview.png)

*The shipped numerical overview. These are conditional simulation results. The model gap in the lower-right panel has not been defined as a measure of task success.*

The semantic workbench offers a way to pose related questions about inputs. A user can enter a research statement and inspect the recognized concepts, their co-occurrence graph and the definitions returned by local search. A registered dependency graph explains relations such as the tensor’s dependence on its residual closure and that closure’s dependence on memory.[^5]

The engine also checks a restricted language of mathematical expressions. Combining the scalar q directly with the rank-two residual R produces a type failure. A properly formed tensor expression can pass checks of rank and formal dimensions. That is a useful barrier against certain mistakes, while equality, derivation and physical truth remain separate obligations.

A claim-auditing interface applies the same discipline to evidence records. Circular dependencies and self-citation can fail. Missing evidence remains unresolved. An empirical claim does not become verified merely because someone supplies a source string or labels it independent. The system checks declared structure and provenance requirements; it does not independently authenticate the linked evidence.

Text can also become an experimental source. The engine maps token weights into 23 numerical bins, reports collisions, and uses those coefficients to construct a reproducible pattern of Fourier forcing across the grid. Changing the text can therefore change the field’s input. The mapping is an authored lexical encoder: it does not establish that the evolving field understands the sentence. The glossary and encoder dimensions are laboratory design choices, separate from the canonical meaning of the Scalar-23 exponent.[^5]

That explicit connection is still useful. It makes text-driven behavior testable. Different inputs can collide in the same representation. Different forcing patterns can converge toward the same state. Null input, shuffled text and alternative encodings can become controls. The research question becomes what distinctions the machinery actually preserves under a defined task.

The release already includes matched comparisons. Its recorded batch runs five arms across three random seeds: the full model, scalar coupling disabled, recursive feedback disabled, a Klein–Gordon baseline, and the same family of recursive operations with a base of 1.5 instead of the golden ratio. The runs use a 24-by-24 noise-initialized grid and 400 field steps, with settings recorded for each arm.[^6]

The results give no basis for declaring a special predictive advantage for the golden ratio. For seed 23, the final field–memory gap is about 0.084227 in the full model and 0.084175 with base 1.5. Across the small reported set, those two arms have very similar gaps. More fundamentally, a smaller gap has not been established as a successful answer to an independent problem. The comparison documents behavior; an application would need an externally defined target.

The software’s numerical checks answer narrower questions with firmer conclusions. All **35 automated tests passed**, covering cases such as a known wave solution, energy behavior, reproducible seeded trajectories, checkpoint continuation and invalid semantic inputs. A separate Python implementation checks the tensor formula. That second implementation is part of the same project’s verification work, not an independent scientific replication.[^7]

In the shipped conservative-wave run, the relative energy change after 400 steps is approximately **−8.93 × 10⁻¹¹**. The unforced field tests also check the expected time-step refinement behavior. These results support the numerical implementation in those restricted cases. They do not establish fourth-order accuracy for the entire coupled recurrence with its discrete updates or optional noise.[^4][^7]

The published commit subsequently passed its GitHub reproducibility workflow. The successful run is attached to the exact source revision, so readers can distinguish the original recorded local checks from the later hosted execution. No Lean proof of this new laboratory is claimed.[^8]

The repository also preserves all 102 canonical equation records, including entries that the simulator does not implement. This provides a route from the source corpus to the subset being explored, without treating an equation atlas as a declaration that every equation has been solved. Documentation identifies the unresolved physical calibration, the missing independent interpretation of the residual, and the additional work needed to test information retention.[^3][^9]

For Wright’s EFMW research program, the advance is a more inspectable experimental object. A proposed relation can now be tied to a particular update rule. That rule can produce an uncomfortable result. The result can remain in the public record beside the successful software checks.

A compelling next result would preserve meaningful distinctions without runaway growth, withstand controls that remove or replace the proposed mechanism, and succeed on a task whose criterion was fixed before the answers were seen. A physical result would additionally require calibrated observables and independent measurements.

The field on the screen keeps moving. What gives the laboratory scientific value as a research tool is the ability to stop it, account for what happened, and change the assumptions in a way another person can reproduce.

---

## Reporting and sources

This feature was prepared with AI assistance for Matthew C. Wright / Monolithic. It is project-based science journalism, not an independently commissioned investigation or a peer-reviewed validation. It draws on the public source, recorded outputs and observed interface behavior of **Information-Tensor v1.0.0 at commit `694b3f132e0cd451295a5dbba346859e9e070dd1`**. Numerical statements refer to the documented sample configurations; no interviews, external endorsements or new physical measurements are implied.

[^1]: [Published laboratory and README](https://github.com/enuminous/Information-Tensor/tree/694b3f132e0cd451295a5dbba346859e9e070dd1). The browser application is supplied as `index.html`; the README explains local launch and GitHub Pages requirements. This article links the verified repository without assuming a live Pages deployment.
[^2]: [Complete implemented model, conventions and numerical methods](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/docs/THEORY.md); [numerical engine](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/engine/core.js).
[^3]: [Source provenance and canonical-to-implementation mapping](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/docs/PROVENANCE.md); [preserved 102-equation catalogue](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/sources/canonical-equations.json).
[^4]: [Recorded validation and interpretation](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/docs/VALIDATION.md); [literal Scalar-23 output](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/results/scalar-literal.json); [bounded Scalar-23 output](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/results/scalar-bounded.json); [conservative-wave output](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/results/conservative.json).
[^5]: [Semantic-engine specification](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/docs/SEMANTICS.md); [semantic engine](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/engine/semantic.js).
[^6]: [Experiment protocol and controls](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/docs/EXPERIMENTS.md); [all 15 comparison runs](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/results/comparison.json).
[^7]: [Automated tests](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/tests/engine.test.cjs); [recorded test output](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/results/test-output.txt); [Python tensor reference](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/scripts/reference.py).
[^8]: [Successful GitHub reproducibility run 41925720669](https://github.com/enuminous/Information-Tensor/actions/runs/41925720669), verified for source commit `694b3f132e0cd451295a5dbba346859e9e070dd1`.
[^9]: [Open scientific and engineering obligations](https://github.com/enuminous/Information-Tensor/blob/694b3f132e0cd451295a5dbba346859e9e070dd1/docs/OPEN_OBLIGATIONS.md).
