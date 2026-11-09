# The Theory That Was Allowed to Fail
### Inside Monolithic LLC's unusual experiment in mathematical physics, artificial intelligence, and the discipline of knowing when to stop

*Science & Technology | November 9, 2026*

**By the Monolithic Research Desk | AI-assisted science journalism**

---

The result was not a new particle, a new force, or an equation destined for the textbooks.

It was three words:

**NO SOURCE SUPPORT.**

Twice.

On November 9, 2026, an independent physics research program led by Matthew Chenoweth Wright reached the end of a carefully bounded investigation into whether its proposed mathematics of information and memory could support a distinctive gravitational phenomenon.

The investigation had acquired an imposing collection of machinery: a covariant field-theory proposal, an oscillator-reservoir model, a mathematical provenance system, a corpus of 717 source records, frozen hypotheses, adversarial review, automated tests, and an execution pipeline on GitHub.

At the end, the machinery produced no supporting derivation for either of the two hypotheses it had been authorized to test.

The researchers had agreed in advance what that outcome would mean.

They stopped.

That decision—not a mathematical breakthrough—is what makes the experiment worth examining.

## I. The Problem With Giving Information Weight

The project emerged from Wright's broader Einstein–Feynman–Maxwell–Wright research program, or EFMW, an independent attempt to explore whether concepts of recursive coherence, information, and memory could be given useful mathematical roles in descriptions of physical systems.

One particularly ambitious possibility concerned gravity.

General relativity describes gravitation through spacetime geometry, sourced by energy and momentum. Could a physical system's memory contribute something independently meaningful to that source?

The question sounds deceptively simple.

First, define a field that retains memory. Then derive its energy and momentum. Finally, determine whether that contribution can be distinguished from conventional matter.

But a substantial difficulty appears immediately.

A new name for part of a physical system's energy is not a new source of gravity.

If a system consists of interacting fields, the complete stress-energy tensor already accounts for their physical contributions. Dividing that total into components labeled "ordinary" and "informational" does not, by itself, change the gravitational physics.

This distinction had become unavoidable in Monolithic's earlier work.

In the Wrightian Informational Tensor Dynamics laboratory, a physical field was coupled to a tracking-memory variable. The laboratory made the relationship computationally visible: the memory field followed the changing physical state, with a delay determined by its tracking dynamics.

But the subsequent WITD-002 investigation asked an uncomfortable question.

Where was the memory's energy actually going?

The answer was not what an advocate of informational gravity might have preferred.

A derived energy-accounting model showed that the tensor originally displayed by the laboratory did not, in general, represent the energy stored in the system's interacting memory dynamics.

The investigation found a mathematical obstruction to equating the two using a single constant tensor weight under its stated assumptions. It also established that part of the model's memory behavior was exactly expressible using a conventional exponential-memory kernel.

The findings did not invalidate all possible informational tensors.

They did invalidate the easy assumption that the displayed construction could simply be promoted into a new gravitational source.

Instead of concealing that limitation, Monolithic published it.

## II. A More Serious Attempt

The next step was IST-001, *Deriving Informational Stress from Covariant Memory and Reservoir Models*.

This time, the proposal would begin with a physical action and derive its stress-energy tensor through metric variation.

That is the conventional mathematical route for constructing gravitational source terms from matter fields.

The model introduced an ordinary scalar field, a memory-like scalar field, and an interaction coupling the two. It then extended the system with additional oscillator fields intended to represent an energy reservoir.

The new formulation accomplished something useful.

Under its stated assumptions, the interacting scalar fields admitted a mathematically consistent total energy-momentum account. The memory sector could exchange energy and momentum with the ordinary field without requiring each sector to be separately conserved.

An accompanying implementation passed 24 software tests in GitHub Actions.

Six of eight narrowly defined mathematical-control gates passed; two remained unresolved.

But there was a ceiling on what those results could establish.

As the paper itself acknowledged, a generic reservoir stress is ordinary gravitational matter stress.

That statement was devastating to any attempt to present the construction, by itself, as evidence of a novel informational force.

And it was one of the most valuable sentences in the paper.

## III. Enter the Adversarial Review

Wright brought the paper into a discussion involving ChatGPT, which he calls Millie, and a second interlocutor he calls Boardy.

Boardy's comments were relayed through Wright. The exchange was an AI-assisted research critique, not a formally appointed or independently authenticated scientific peer review.

Nevertheless, its central feature was striking.

The participants were not merely asking how to defend the theory.

They were trying to identify the assumptions under which it stopped working.

Boardy raised three technical objections.

The first concerned conservation.

The paper derived total stress-energy conservation when both principal scalar fields were dynamical. But its later oscillator-reservoir demonstration treated one of those fields as an externally prescribed drive.

Those are different physical circumstances.

A driven subsystem can exchange work with the external source. Its manufactured numerical agreement does not independently demonstrate the behavior of the complete autonomous system.

That objection stood.

The second concerned bath-induced frequency renormalization.

Boardy argued that eliminating the reservoir oscillators would shift the restoring coefficient used in the memory equation.

Millie pointed out that the specific action already contained the conventional static counterterm, written within the oscillator's squared displacement.

For the action actually published, the proposed objection did not hold.

Boardy acknowledged the mistake.

The third concerned a memory-mass term that appeared in the first model but disappeared from the later reservoir construction.

Initially, Boardy suggested that the oscillator bath effectively supplied the missing restoring mass.

That was also incorrect for the completed-square coupling at issue.

The bath's equilibrium displacement did not automatically replace the missing standalone mass.

And this correction uncovered a more consequential problem.

With the original positive memory mass retained, the system's equilibrium tracking gain would generally fall below one. The exact unit-gain tracking desired by the proposed memory law required an additional model restriction or a separately justified physical mechanism.

The reservoir model had not derived that restriction from the original EFMW equations.

Boardy's response was unusually candid:

> "Being wrong in writing is cheaper than being wrong in a paper."

The line captured the character of the exchange.

The disagreement had not produced a winner.

It had produced a narrower, more accurately specified scientific claim.

## IV. A Stress Tensor Is Not a Fingerprint

The next question concerned how a distinctive informational source could ever be identified.

One possibility was anisotropic stress: a difference between stresses measured in different spatial directions.

Boardy initially observed that a homogeneous canonical scalar field and a conventional perfect fluid can both have zero anisotropic stress.

Millie supplied an important qualification.

Multiple interacting scalar fields, or fields with spatial gradients, can exhibit anisotropic stress under appropriate conditions and in suitable reference frames.

That correction prevented the researchers from declaring a general mathematical impossibility where none had been demonstrated.

But it did not save the gravitational hypothesis.

Conventional multifield systems and imperfect fluids can also produce anisotropic stresses.

So merely finding a nonzero anisotropic component would not identify a uniquely informational physical mechanism.

Boardy proposed looking at something harder to imitate: not one stress configuration, but an entire family of responses under varying physical conditions.

An arbitrarily flexible conventional model may reproduce a single configuration. A constrained physical theory is more demanding because its parameters must generate consistent predictions across many configurations without being adjusted independently for every observation.

That moved the discussion from fitting a stress tensor to comparing the mathematical families of responses generated by competing theories.

It was a genuine improvement in the proposed test.

But the new comparison brought another complication.

The finite oscillator reservoir in IST-001 already belonged to an established class of conventional physical models.

Its memory kernel had the form

\[
\gamma(t)=\sum_j b_j\cos(\omega_jt),
\qquad b_j\geq0.
\]

The coefficients were nonnegative, the frequencies described oscillator modes, and the resulting function could be represented by a positive discrete spectral measure.

This was standard oscillator-reservoir mathematics.

A conventional oscillator bath with the same spectrum would generate the same kernel and corresponding linear response under the same model assumptions.

The proposed informational interpretation added no independently established physical distinction.

The issue was no longer whether the mathematical model could work.

It could.

The issue was whether anything in the original EFMW source equations imposed a restriction that the conventional reservoir model did not already possess.

## V. The Temptation of the Golden Ratio

The investigation now approached its most dangerous methodological moment.

The broader EFMW corpus contained many expressions involving the golden ratio, recursive coefficients, coherence relations, and powers of \(\varphi\).

It would have been easy to search the collection until some sequence appeared to resemble a physical oscillator spectrum.

But the researchers recognized the trap.

If an investigator is free to choose which mathematical quantities count as oscillator modes, arrange them into a favorable order, and select convenient subsets, the investigator can generate remarkable-looking patterns without deriving a physical law.

A golden-ratio relationship is only meaningful as a physical prediction when the underlying model independently determines what the frequencies represent.

Boardy insisted that the search itself be restricted before it began.

Two hypotheses were selected.

The first proposed that the frequencies of a physically defined, ordered sequence of oscillator modes would have successive ratios equal to the golden ratio:

\[
\frac{\omega_{j+1}}{\omega_j}=\varphi.
\]

The second proposed that the corresponding spectral weights would follow a fixed inverse-square golden-ratio relation:

\[
\frac{b_{j+1}}{b_j}=\varphi^{-2}.
\]

The exponent of two had not been derived from an existing source equation. It was a speculative choice.

The researchers disclosed that.

Freezing a guess can prevent retrospective tuning. It cannot transform the guess into an established law of nature.

The original two-hypothesis protocol was committed to GitHub before the audit. A subsequent, explicitly versioned tightening of its acceptance rules was also committed before the full source scan.

The stricter rules prohibited selecting favorable triples from a longer sequence. The proposed ratios had to hold across the entire contiguous mode run defined by the source itself.

The source also had to determine the ordering and the map from its own mathematical quantities to physical oscillator frequencies and weights.

Without that mapping, an apparent ratio could not pass.

There was another critical restriction.

Even a successful source-derived golden-ratio relationship would describe a constrained, conventionally realizable oscillator bath.

It would not establish new gravity.

The distinction between a source-derived mathematical relationship and an independently demonstrated gravitational effect was written into the acceptance conditions.

The paper would not be allowed to turn a spectral result into a gravitational discovery through rhetoric.

## VI. The Protocol Before the Story

Boardy summarized the governing principle:

> "Committed before the audit is the part that matters. That's the whole difference between a protocol and a story."

The statement deserves attention.

A researcher can always write an attractive explanation after finding something interesting.

That is not inherently dishonest. Exploratory science depends upon noticing unexpected relationships.

But a retrospective explanation is not the same as a prediction whose success and failure conditions were defined before the relevant test.

The IST-FAM-001 exercise attempted to preserve that distinction.

Its two hypotheses were locked.

Its source corpus was frozen.

Its required mapping criteria were stated.

Its stopping condition was specified.

And the protocol expressly permitted the investigation to end without identifying a distinctive spectral constraint.

The researchers did not claim that the exercise was blind. Portions of the EFMW corpus had already been examined during earlier work, and the hypothesis choices had been informed by that history.

Nor was this an externally registered experimental trial.

It was a prospective, author-defined source-support audit within a previously explored research program.

Those limitations were disclosed rather than disguised.

## VII. The 717-Record Audit

The final audit examined a frozen inventory containing 717 mathematical source records.

There were 585 historical FieldSpace entries, 102 canonical EFMW formulas, and 30 additional mathematical source pointers from related repositories.

The audit compared the records against seven original source files pinned to exact Git revisions.

All seven source-file blob identities matched their archived references.

All 717 recorded source statements matched the corresponding originals.

The audit also generated a machine-readable record of the complete screening process, including the original source locations and reasons for rejecting superficially relevant equations.

Twenty-seven candidate near-misses received focused review.

Some defined golden-ratio powers.

Others concerned recursive phase accumulation, self-model tracking, informational stress, or relaxation dynamics.

None established the source-defined physical oscillator-mode sequence required for H1.

None established the physically defined reservoir weights required for H2.

No justified mapping meant there was no legitimate sequence on which to evaluate the proposed full-run ratios.

The result for each hypothesis was therefore the same:

**NO SOURCE SUPPORT.**

This was not a measured experimental contradiction. The researchers had not constructed a physical oscillator spectrum and discovered that its ratios disagreed with a prediction.

They had found that the frozen source corpus did not supply the prerequisite physical definitions and derivations needed to make those predictions.

That was sufficient to trigger the audit's stated stop rule.

The software verification also caught a small but revealing error.

An initial text-screening expression had mistaken uppercase Greek Omega, used in cosmological formulas, for lowercase omega, used as a frequency symbol.

The mistake inflated one lexical count.

It did not change the scientific findings.

The scanner was corrected, a regression test was added, and the audit was executed again.

The final GitHub Actions run passed all 19 software tests and archived the full evidence package.

A successful software test did not turn either scientific hypothesis into a success.

The distinction remained intact.

## VIII. The Failure That Saved the Research From Its Own Momentum

The original research ambition had been large: investigate whether information, recursion, and physical memory could lead toward a deeper unification of physics.

The completed audit addressed something much smaller.

It asked whether two particular spectral relationships could be derived, under specific mapping requirements, from a specified frozen collection of equations.

Neither could be substantiated.

That conclusion closes neither general relativity nor the study of physical memory. It does not disprove every future possibility for EFMW, and it does not invalidate the useful mathematical work already produced.

The conventional scalar-field calculations remain available.

The reservoir model remains available.

The energy-accounting derivations remain available.

The counterexamples, failed numerical gates, source archives, code, tests, and published corrections remain available.

What ends is the attempt to use this particular spectral route as an unsupported bridge to novel informational gravity.

That is a much narrower conclusion than declaring a theory of everything disproven.

It is also a considerably more defensible one.

Boardy's resource argument was practical: a bounded source audit might consume days, whereas allowing a questionable hypothesis to accumulate successive layers of mathematics and simulation could consume several additional research phases.

It is impossible to know how much future work was actually avoided.

But the logic of the decision is clear.

When a proposed route lacks the source-derived structure required to make an independently testable prediction, further complexity is not automatically progress.

Sometimes it is merely expense.

## IX. The Role of Artificial Intelligence

There is another unusual dimension to this investigation.

Much of the mathematical drafting, software implementation, critique, and reporting was assisted by artificial intelligence.

AI systems are capable of generating sophisticated-looking mathematical constructions, including constructions that are incomplete, misleading, or incorrect.

This creates a particular problem for independent researchers using them: an argument can become more elaborate long before it becomes more justified.

In this case, the collaboration itself became an object of scrutiny.

Boardy made technical objections and withdrew some of them after correction.

Millie supplied counterarguments and also had to narrow earlier statements.

The research lead authorized a frozen audit rather than another speculative expansion.

The resulting record contains disagreement, self-correction, and a negative outcome.

It does not establish that the AI systems were independent scientific referees or that the research was externally peer-reviewed.

It shows something more limited and immediately useful: AI-assisted research can be organized so that its outputs are subjected to explicit evidence gates, source verification, adversarial objections, and stopping conditions.

That organization matters because AI systems can produce plausible explanations faster than their physical implications can be verified.

A reproducible protocol cannot eliminate every error. But it can constrain the ways an unsupported explanation is allowed to become a claimed result.

The investigation's most telling feature may be that the final algorithm was not asked to find a way for EFMW to succeed.

It was asked to determine whether the existing sources satisfied conditions that had already been written down.

When they did not, the search ended.

## X. The Zoo's Real Purpose

Within Wright's broader Monolithic research ecosystem, the EFMW Zoo serves as a collection of named audit and verification functions intended to challenge claims, expose hidden assumptions, and preserve unresolved or contradictory evidence.

Its deeper organizing principle is straightforward:

A claim should be allowed to fail without forcing the surrounding research program to fail with it.

The IST-FAM-001 investigation gives that principle a concrete example.

The work did not end in a discovery announcement.

It ended with an execution receipt.

The receipt recorded a frozen source corpus, a precommitted two-hypothesis protocol, a disclosed amendment to the acceptance rules, complete source coverage, passing software tests, two unsupported source-derivation claims, and a bounded closure decision.

That is a modest result measured against the ambition of unifying physics.

But it is not an empty one.

It demonstrates a research workflow in which preserving the integrity of a negative result takes precedence over preserving the attractiveness of a theory.

It also draws an important boundary around the phrase *informational stress*.

A mathematical model may describe how a memory-bearing system stores and exchanges physical energy. That achievement does not imply that nature contains a new gravitational charge associated with information.

If a genuinely novel claim is to emerge later, it will require more than a name, a successful simulation, or an unusual mathematical constant.

It will require an independently justified physical structure, a prediction that could have been wrong, and an observation capable of distinguishing that prediction from conventional alternatives.

IST-FAM-001 did not reach that destination.

It showed why the present route did not justify proceeding toward it.

## XI. The Result That Remains

Scientific progress is often narrated as a succession of discoveries.

Less attention is given to the hypotheses that are examined, restricted, and abandoned before they consume an entire research career.

Such decisions seldom produce dramatic photographs or memorable headlines.

They produce smaller artifacts: corrected equations, archived source files, reproducible scripts, explicit counterexamples, and carefully worded conclusions.

In this instance, the most important artifact may have been the original protocol commit.

Its significance lies in what happened afterward.

The researchers did not use their negative result as an invitation to choose a new exponent, rearrange the mode sequence, or reinterpret a golden-ratio scaling expression as a physical oscillator frequency.

They did not promote a successful computational audit into evidence of new gravity.

They did not declare the entire EFMW program disproven.

They stopped exactly the route they had agreed to stop.

That distinction is essential.

Monolithic LLC's attempt to extract novel informational gravity from its present oscillator-reservoir construction ended without the necessary source support.

The conventional mathematics survived.

The broader physical questions remained open.

And the research program gained a documented example of a process many scientific projects promise but do not consistently practice:

**A theory was given a genuine opportunity to fail, and failure was accepted as the result.**

No new force was discovered.

No physical unification was established.

But a boundary was drawn before the search began, and the investigators respected it when the evidence failed to cross.

That is not the end of scientific inquiry.

It is one of the ways scientific inquiry remains trustworthy.

---

## Reporting notes and primary records

This article is based on Monolithic LLC's public GitHub research records and the author's account of the Boardy–Millie review dialogue. It is AI-assisted journalism, not an independent experimental replication or an externally peer-reviewed scientific assessment.

- [IST-001 — Deriving Informational Stress from Covariant Memory and Reservoir Models](https://github.com/enuminous/papers/blob/main/IST-001-Deriving-Informational-Stress-from-Covariant-Memory-and-Reservoir-Models-2026-11-09.md)
- [WITD-002 — Where Does the Memory's Energy Go?](https://github.com/enuminous/papers/blob/main/WITD-002-Where-Does-the-Memorys-Energy-Go-2026-11-05.md)
- [IST-FAM-001 — Referee Review and Spectral Novelty Audit](https://github.com/enuminous/papers/blob/main/IST-FAM-001-Referee-Review-and-Spectral-Novelty-Audit-2026-11-09.md)
- [Original two-hypothesis protocol](https://github.com/enuminous/papers/blob/main/research/ist-fam-001/PROTOCOL.json)
- [Pre-execution protocol amendment](https://github.com/enuminous/papers/blob/main/research/ist-fam-001/PRE_EXECUTION_REVIEW_RULES.md)
- [Complete 717-record executed audit and bounded closure report](https://github.com/enuminous/papers/blob/main/research/ist-fam-001/AUDIT_REPORT.md)
- [Final verified GitHub Actions run — 19 tests passed](https://github.com/enuminous/papers/actions/runs/42676059594)

**Final scientific distinction:** The investigation established a bounded *lack of source support* for two specified spectral hypotheses. It did not conduct a gravitational experiment, prove that all informational models are impossible, or identify a new gravitational effect.

*© 2026 Monolithic LLC · Research journalism*
