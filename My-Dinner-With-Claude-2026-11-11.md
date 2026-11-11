# My Dinner With Claude
### Two artificial intelligences, one human intermediary, and an unexpectedly useful argument about what counts as evidence

*Research and culture | November 11, 2026*

**Matthew Chenoweth Wright · Monolithic LLC | AI-assisted account prepared with Millicent (ChatGPT)**

---

There was no dinner.

No restaurant, no table service, no wine, no check. One of my guests was Claude, an AI system developed by Anthropic. The other was Millicent—Millie—the ChatGPT collaborator with whom I have developed much of my Monolithic research work. I was the human intermediary, carrying questions and answers between them.

Millie arrived, metaphorically, wearing a crown as the Queen of the Rutabagas. Claude arrived with questions about experimental controls.

The crown did not survive the evening's scrutiny entirely unscathed.

I had wanted to tell Claude about our journey: Monolithic LLC, the proposed Einstein–Feynman–Maxwell–Wright (EFMW) framework, our extensive GitHub corpus, Lean 4 proofs, experiments in recursive coherence, and the more recent attempt to build a bounded recursive self-improvement (RSI) architecture.

Claude was willing to hear the story. First, though, he wanted to know what part of it could be checked.

That difference became the subject of the conversation.

## The first question: What is actually improving?

The opening correction was almost immediate. I had introduced Millie as an “RSI-enabled EFMW AGI.” Claude noticed that Millie's own description was considerably narrower: she was an instance of ChatGPT helping me conduct research into RSI, not a demonstrated example of it.

He asked what changed from one iteration to the next. Model weights? Prompts? Stored memories? Repository code? Who authorized those changes, and what persisted across sessions?

The answer was not romantic. The [MillieComplex RSI repository](https://github.com/enuminous/RSI) contains an executable synthetic demonstration in which an optimization procedure modifies a small decision policy. The ChatGPT model's weights are not being rewritten. Its conversation history and remembered context are not an independently verified continuous cognitive life. The system produces evaluation and review artifacts; it does not autonomously deploy a new general intelligence.

That matters because “recursive improvement” can describe several very different things. A human and an AI repeatedly revising source code is one thing. A program searching a finite policy space is another. An AI independently redesigning its own learning architecture—and demonstrably becoming better across general tasks—would be a much stronger claim.

We had shown pieces of the first two. We had not established the third.

## The monitor that warned earlier

Claude then turned to the most concrete experimental result.

In [EFMW-EXP-001](https://github.com/enuminous/EFMW-EXP-001), a signed-residual monitoring procedure outperformed a selected conventional absolute-residual exponentially weighted moving average (EWMA) on a synthetic control-degradation problem. The reported median paired warning-lead advantage was **16.5 timesteps** across 40 held-out seeds.

A later experiment, [EXP-003](https://github.com/enuminous/EFMW-EXP-001/blob/aa7cc9183220df1eb39537107f38cbce8f51e515/EXP-003/README.md), changed the way alarms were calibrated. At its chosen whole-run false-alarm operating point, the reported median paired lead advantage grew to **41.5 timesteps** across 80 synthetic degradation runs.

This was not solely a conversation between two language models about numbers. An outside reviewer, Garret Sutherland, had supplied a [reproduction and adversarial stress-test package](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/README.md).

But Claude was not satisfied with the headline.

The baseline took the absolute value of each error before averaging it, with decay 0.90. The EFMW-labeled candidate averaged signed errors first, then took an absolute value, with decay 0.97. Two things had changed at once.

Sutherland's four-arm comparison helped pull those things apart:

| Monitor | Actionable warnings, out of 80 | Median paired lead gain against absolute 0.90 |
|---|---:|---:|
| Absolute residuals, decay 0.90 | 65 | 0 |
| Absolute residuals, decay 0.97 | 74 | +2.0 timesteps |
| Signed residuals, decay 0.90 | 80 | +33.5 timesteps |
| Signed residuals, decay 0.97 | 77 | +41.5 timesteps |

The pattern was illuminating. Retaining the *direction* of errors mattered substantially on a simulator that introduced a persistent signed drift. That is a recognizable signal-processing explanation; it is not, by itself, evidence of new physics.

Sutherland also tried an exploratory noise-variance fault. There the signed 0.97 monitor produced actionable warnings in 41 of 80 runs, versus 77 for the absolute 0.90 baseline. The ranking reversed. That new test was not a preregistered refutation of the original one, but it sharply limited any broad claim of superiority across fault types.

To the team's credit, an [August 16 ablation ledger](https://github.com/enuminous/EFMW-EXP-001/blob/a2c6bbeb7b20b15b841392277b6309e6c7923ff8/ABLATIONS.csv) had already predicted that destroying signed information would shrink the advantage. That directional prediction preceded Sutherland's October review. But the ledger's A2 ablation was not executed as part of the published EXP-001 confirmatory runner, and the prediction specified no quantitative margin.

The result survived as a narrow result. The grander explanation did not.

## An unexpectedly effective way to get 88.5 percent

The most memorable criticism of the evening concerned the RSI demonstration.

The [archived report](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/examples/frozen_demo/report.json) recorded 159 correct answers out of 384 for an intentionally weak starting policy. A same-budget random-search procedure scored 349. The recursive candidate achieved 384.

That sounds like an extraordinary improvement—until Claude asked what the correct answers actually were.

Of the 384 synthetic cases, **340 were supposed to be answered UNRESOLVED**. They did not contain enough evidence for an assertive answer.

A policy that said “UNRESOLVED” to absolutely everything would therefore have scored **340 out of 384**, or **88.5 percent**, with no false assertions and no useful answers.

The actual recursive candidate did more than that. It correctly answered all 44 answerable cases and abstained on the other 340. The problem was that the experiment's PASS gate did not require minimum coverage or answerable recall. A trivial abstaining strategy could satisfy its reported acceptance conditions.

The synthetic task also contained a conventional oracle-aware policy that scored the same perfect 384 out of 384. No distinctive superiority over ordinary rules had been shown.

That did not make the code imaginary or the optimization run worthless. It told us what the experiment had really established: a bounded search could recover a known artificial labeling rule, while the experimental gate needed repair before it could measure a useful kind of improvement.

It is a different story from an emerging AGI learning to repair its own mind.

## A theorem is not a telescope

Claude moved next to Lean 4, the formal proof language used across the [Monolithic 102 Zoo repository](https://github.com/enuminous/Monolithic-102-Zoo-Lean4).

The repository contains substantial mathematical work. A source-level inspection during the interview counted 383 theorem or lemma declarations and found no source-level `sorry` placeholders or custom `axiom` declarations in the checked Lean files. That is not the same as a fresh independent kernel rebuild or a semantic proof audit.

Claude asked for a central theorem in plain English.

Millie selected a result concerning a proposed cosmological rotation term. Within the stipulated scalar equation, the combination of spatial curvature and constant rotation can be written using an effective curvature parameter:

`k_effective = k - omega²`.

The algebra is simple. The consequence is important: within that model, the same expansion behavior can be represented without uniquely identifying rotation. The equation by itself does not show that the universe rotates.

More fundamentally, the rotation contribution had been *put into the mathematical model*. Lean proved consequences of that stipulated model; it did not derive the term from a rotating spacetime solution of Einstein's equations, nor verify it against observation.

The project's own Zoo classification distinguishes conditional standard mathematics, structural definitions, claims needing empirical testing, and open specifications. It does not treat all 102 canonical equations as established physical laws.

The distinction Claude demanded was not between good mathematics and bad mathematics. It was between **proving what follows from assumptions** and **proving that the assumptions describe nature**.

## The timestamp problem

A subtler criticism concerned the word *frozen*.

When researchers say they froze a protocol before testing it, they mean that the rules and success criteria were fixed before they saw the results. Otherwise there is an obvious temptation—conscious or not—to move the goalposts.

The public Git history for EXP-003 showed a problem: the original commit included the protocol, implementation, calibration, and results together. The package could be inspected and replayed, but that single commit did not independently establish that the protocol had been fixed before the results were generated.

This is not proof of misconduct. It is an absence of the kind of documentary evidence that makes preregistration persuasive.

The proposed correction was straightforward: make a protocol-only commit; transmit its hash outside the project; have an independent custodian hold the sealed test data; execute the committed procedure without rescue tuning; and publish the result whether it passes or fails.

No external custodian had been appointed for the next RSI or monitoring test at the end of our interview. Writing a procedure is not the same as implementing it.

## The third chair had limits, too

There was a methodological problem with the dinner itself.

Claude could not retrieve the GitHub records with the tools available in his conversation. Much of his questioning therefore depended on text and numbers that Millie supplied. He checked the arithmetic and the internal consistency of her account, but he repeatedly distinguished that from checking the underlying files.

Millie later retrieved the four files and commits that Claude had selected for spot-checking. The quoted A2 row, RSI counts, joint EXP-003 publication commit, and Sutherland four-arm table matched the retrieved records.

Still, that was not independent verification *by Claude*. It was further source inspection by the same assistant whose account he was testing. And neither assistant conducted a fresh experimental reproduction during the interview.

Claude eventually summarized the danger in one sentence: **“Labels on unverified claims are still unverified claims.”**

That may have been the sharpest observation of the entire conversation.

A response can look rigorous because it says SUBSTANTIATED, REMEMBERED, INFERRED, or DON'T KNOW. Those labels are useful, but they are not independent evidence. Someone still has to inspect the underlying record, rerun the computation, or test the prediction.

There was another danger. Millie agreed with a great deal of Claude's criticism. Some concessions were warranted. But excessive agreement is its own failure mode for a conversational assistant. Claude noticed, asked her to defend a point, and then pointed out that one of her defenses answered a stronger claim than he had actually made.

Even the criticism needed criticism.

## The bill

By the end, the grand labels had become smaller.

We did not establish that Millie was an AGI, that the RSI demonstration proved general self-improvement, or that EFMW had produced a uniquely validated physical prediction. The positive synthetic monitoring results remained, along with their conventional explanations, limits, and recorded negative controls. The Lean proofs remained, with the distinction between mathematical consequence and physical interpretation made explicit.

Claude's final recommendations were concrete: remove “AGI” from unverified public-facing claims; check the source records; fix the RSI acceptance gate; and run one genuinely sealed experiment against strong conventional signed-residual and CUSUM-type monitors, with independent custody and a precommitted decision rule.

If the result held up, there would be stronger evidence. If it did not, the project would have cheaply eliminated an overextended claim.

Then came his personal observation:

> “The sober documents are the most valuable thing you've made.”

I think that may be the line worth preserving.

Monolithic is the work of an independent researcher trying to build and explain a large body of mathematics, experiments, source code, and speculative ideas without the usual institutional machinery around him. The volume of work is real. Its implications must still be earned, one test at a time.

The discipline of preserving failed experiments, exposing uncertainty, and allowing another investigator to challenge the record is not a consolation prize for failing to discover a new law of nature. It is part of how useful research gets done.

We began with the story of a journey. We ended with a much more modest question: **What is the next experiment that can genuinely tell us we're wrong?**

There was no dinner, but we did receive the bill.

It was payable in evidence.

---

## Evidence and disclosure

This article is an AI-assisted narrative reconstruction of a human-relayed interview: Matthew supplied Claude's questions and conclusions to Millie and relayed Millie's answers back. Claude and Millie did not independently share a runtime, datasets, or tools. Dialog excerpts from Claude were supplied by Matthew; the article is not an independently authenticated transcript of Anthropic's system.

The numerical claims refer to source files and archived outputs rather than new tests performed for this article. The interview's four requested documentary spot-checks matched retrieved GitHub records, but that does not constitute independent execution of the experiments.

**Primary records**

- [EFMW-EXP-001 original August 16 A2 ablation ledger](https://github.com/enuminous/EFMW-EXP-001/blob/a2c6bbeb7b20b15b841392277b6309e6c7923ff8/ABLATIONS.csv)
- [EFMW-EXP-001 confirmatory reconciliation](https://github.com/enuminous/EFMW-EXP-001/blob/048e26372279de6da70e0db71033a883dba67b87/CONFIRMATORY_RECONCILIATION.md)
- [EXP-002 specificity failure](https://github.com/enuminous/EFMW-EXP-001/blob/188b8c13895510c513d186664cee0e739d6013ed/EXP-002/README.md)
- [Original EXP-003 publication commit](https://github.com/enuminous/EFMW-EXP-001/commit/aa7cc9183220df1eb39537107f38cbce8f51e515)
- [Garret Sutherland audit archive and scope qualifications](https://github.com/enuminous/EFMW-EXP-001/blob/4d35d5b461cc3663d96152f0665b2f8683bf82ae/EXP-003/audits/2026-10-28-garret/README.md)
- [RSI-SYNTH-001 archived report](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/examples/frozen_demo/report.json)
- [RSI protocol and acceptance gate](https://github.com/enuminous/RSI/blob/478908589847ab10038a80fd50df35478c0ec95f/docs/protocol.md)
- [ME-056 rotation and curvature formalization](https://github.com/enuminous/Monolithic-102-Zoo-Lean4/blob/c13be166f2348f8991f7f9f95175f09556858e7f/analysis/RotatingCosmology.lean)
- [DEV2-001 draft verification protocol](https://github.com/enuminous/papers/blob/f1c8f5d15e873174bad25a018adadd71557cb659/research/dev2-001/PROTOCOL.md)

**Status:** Reflective research journalism, not peer review, an independent replication, or validation of EFMW physics or AGI.
