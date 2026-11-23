# What Would Change Our Minds?

*Inside Monolithic’s collection of equations, proof software, and computer experiments*

**Matthew Chenoweth Wright · Monolithic LLC**  
November 22, 2026

In one of our tokamak simulations, a coil moved one centimetre. The hottest patch on the modeled target cooled. Move the coil one centimetre the other way, and the patch got hotter. That made for a pleasingly simple story until we asked what would happen if the target had a rounded corner. Some of the predicted peaks changed substantially. Suddenly the shape of a corner mattered to the story we could tell about moving a magnet. [Tokamak heat-footprint study](https://github.com/enuminous/Tokamak/tree/main/benchmarks/openstep-005)

Monolithic grew around questions like that. We have a collection of equations about feedback and physical systems, software that checks mathematical claims, computational experiments, browser labs, and records that let other people inspect the work. One project asks whether a formula can describe a rotating spacetime. Another asks whether an AI system can produce a claim it has enough evidence to make. Each has its own standards of evidence, but both benefit from the same habit. Say what you expect to see, run a check that could prove you wrong, and leave enough of a record that someone else can tell what happened.

## An equation collection you can argue with

EFMW is the name of our umbrella research program. One of its recurring questions is what happens when a system uses information about its own state to change what it does next. Think of a tracker that sees a persistent error to the left. A running average tells it the error is getting larger. A calculation that retains the sign can also tell it which way to correct. That distinction sounds small until you build two trackers, give them the same data, and ask which one detects trouble first.

The Monolithic 102 is a numbered corpus of equations and proposed relationships that gives us something specific to inspect and revise. Some work in the corpus asks whether equations follow from stated assumptions. Other work asks whether a model could describe a physical system at all. An experiment on a tracking algorithm can tell us something about the algorithm on those inputs. A proposed physical mechanism needs its own test, including a way to distinguish it from ordinary effects. Our research archive makes room for both kinds of question. [Monolithic 102](https://github.com/enuminous/Monolithic_102_EFMW) · [EFMW research directory](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md)

## A zoo for checking claims

Lean is a programming language and proof assistant. Give it a precise statement and a proof, and its kernel checks each step against the rules of the system. The satisfaction of seeing a proof pass comes with a good follow-up question. What did we actually ask Lean to prove? If we assumed the condition we cared about, or proved a weaker statement than the one in the paper, a successful build can coexist with a serious gap.

Our Monolithic Zoo organizes verification methods under animal names. One Lean package covers selected computational routines and contracts for the original 46 entries. For example, some modules check how rankings are combined once features are supplied. The work leaves feature extraction and model training outside those modules. Another project, the EFMW Lagrangian Audit, checks a particular candidate mathematical construction against a defined comparison set. The scope written beside each result matters every bit as much as the result itself. [Monolithic Zoo in Lean](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [EFMW Lagrangian Audit](https://github.com/enuminous/EFMW-Lagrangian)

We’re developing a technical audit service around that practice. A focused review could take a named theorem, a particular version of its code, and a question the author or buyer needs answered. Can the proof be replayed? Which assumptions does it depend on? Does the public claim match the statement that was checked? Sometimes the answer is unresolved because a dependency, dataset, or formal link is missing. That tells the next reader where to look. The service is an offering in development, and its scope depends on the artifact under review.

## The physics labs are allowed to say no

The Rotation project began with a deceptively simple observation. Physicists use the word *rotation* for everything from a spinning body to the winding of a wave’s phase. The same word can make separate phenomena sound like evidence for one another. The Rotation atlas collects examples and counterexamples so we can ask what is actually turning, how we would measure it, and whether the proposed measurement can distinguish it from another effect. Its question about rotation of the universe as a whole remains open in our work. [Rotation evidence atlas](https://github.com/enuminous/Rotation)

The Tokamak project connects magnetic geometry with exhaust and plasma control. In its DIII-D benchmark, two calculations initially disagreed about how fast a simulated disturbance grew. The difference shrank to **0.75%** when we matched how the solvers treated the plasma profiles in the fixed-profile comparison. The disturbance still grew. That small success helps us understand the calculation. It leaves the controller and the performance of a power plant as separate problems. [OPENSTEP-007](https://github.com/enuminous/Tokamak/tree/main/benchmarks/openstep-007) · [How Do You Hold a Star-Shaped Fire?](https://github.com/enuminous/papers/blob/main/How-Do-You-Hold-a-Star-Shaped-Fire-2026-11-22.md)

Some of these projects also have browser labs. The Archimedes Engine, for instance, lets a reader follow a simulated agent as it moves, senses, and updates a model of its surroundings. You can rewind to an earlier state and try a different choice. The experiments use a deliberately limited environment, so the reader can inspect the rules that produce the behavior on screen. [Archimedes Engine](https://enuminous.github.io/Archimedes-3D/)

## Who gets to correct the record?

That question becomes harder when the system doing the work is also the system explaining what it did. The Autonomy project models a simple case. An agent makes a decision within a declared authority. Someone independent challenges it. Can that reviewer obtain the evidence, reverse the decision, and see the reversal take effect? A file can preserve the agent’s original account perfectly and still leave all three questions unanswered. We have an executable reference model and a browser demonstration. A live independent reversal is a different test. [Autonomy and the reversal test](https://github.com/enuminous/Autonomy)

That brings us back to the coil and the corner. The most useful thing we can hand someone is often small enough to name: this equation, this test, this version of the code, this change that made the result move. Our papers gather those records into stories people can follow. The repositories give readers a way to check the stories and, where the evidence calls for it, change them. [Monolithic papers and research archive](https://github.com/enuminous/papers)
