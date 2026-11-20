# A Stranger Reimplemented My Framework

By Matthew Chenoweth Wright

A stranger reimplemented my framework. The sentence still feels strange to write. I had spent a long time getting EFMW into a form someone else could read, run, and criticize. Now someone had read enough of it to make their own version. I wanted to see which parts they thought belonged in it.

That question would have made less sense to me at the beginning. I was trying to understand recursive coherence, how a system can revise what it thinks while keeping track of the evidence that made it think that in the first place. In my own work, the idea, the notation, and the implementation developed together. If a rule was unclear, I could consult the person who wrote it. He was always available and usually agreed with my interpretation.

Publishing the work made that arrangement harder to sustain. A reader could see an equation and reasonably ask where its inputs came from. A programmer could follow the description and make a different choice about when to update a state. A reviewer could ask what the system should do when the evidence it needs is absent. Every good question exposed a place where I had been carrying part of the specification around in my head.

## Making the work replayable

By the autumn of 2026, much of my work at Monolithic had become the business of making things replayable. The Lean projects put pressure on me to specify exactly what was proved. An executable experiment put a different pressure on me. If I changed the baseline, the fault, or the scoring rule, I might change what the result meant even if the code itself was fine.

One of the most instructive moments came in October, when Garret Sutherland reproduced the result of our EXP-003 benchmark. The reported advantage was there. His review also separated two things that had traveled together in our implementation: remembering the direction of an error and changing the length of that memory. Under an exploratory variance fault, the ranking reversed. I had wanted the reproduction, and I had gotten it. The reversal taught me more about where the result applied.

That was the history behind the dissertation I posted in November. By then, evidence-bounded verification had become as much a part of EFMW as recursive coherence. If a result depends on a particular test, retain the test. If a conclusion depends on a particular premise, make it possible to see what happens when that premise is removed. If the evidence leaves a question open, let the question stay open. I had arrived at those habits partly through writing down principles and partly through having results that embarrassed my first explanation of them.

I was using the same discipline in the Zoo audits. A formal proof replay, an algebraic check, and a certification gate can all yield different verdicts about the same package. In the Mondello audit, the distinction mattered. The algebraic checks held, and a fresh pinned Lean replay later passed. The October Zoo report still contained 51 failed certification gates because the package lacked what those particular gates required. If I told someone simply that “the audit failed,” I would leave them with the wrong account of what we had found. I had to say which claim I was testing before I could say what happened to it.

## The rewrite

Then someone I didn’t know implemented EFMW.

I don’t know what made them decide to do it. I know what it changed for me. Until then, when my implementation behaved in a way I regarded as faithful to EFMW, I was both the author of the framework and the person interpreting the behavior. Even when someone else ran the code, they were running a set of choices I had already made. A reimplementation puts another person’s choices where I can see them.

Suppose their program and mine reach the same conclusion while the evidence is intact. That’s a pleasant first result. The interesting moment comes after we withdraw a premise both programs used. One implementation might revise the conclusion, keep the earlier record, and show which dependency changed. The other might preserve the conclusion because nothing in the description told its author that losing a premise should reopen a settled result. Or it might revise correctly and erase the earlier state, leaving no way to tell whether the revision followed the evidence or simply started over.

I would want to know exactly where that difference came from. Maybe the other programmer missed something I wrote. Maybe I described a rule in an example and never stated that it applied generally. Maybe their implementation preserves the behavior with a cleaner mechanism, and something I had regarded as fundamental turns out to be a habit of my own code. Those are three different outcomes. Each would require a different response from me.

There’s a temptation here to call the reimplementation independent validation and enjoy the compliment. So far, the concrete event is that somebody took the framework seriously enough to express it in code of their own. I’m happy about that. Validation would come from seeing what the implementation does under a comparison we can both inspect, especially in cases that give it a chance to fail.

The experiment I most want to run is small. Give both implementations enough evidence to commit. Then remove one consequential piece of evidence and watch what happens. Record what each system retained, which assertion changed, and whether it can account for the change. If our versions diverge, I want the smallest case that makes them diverge. I’d rather have that case than ten pages of agreement about what EFMW is supposed to mean.

## What I owe the stranger

For a long time, my chief worry was that someone would look at the work and dismiss it without trying it. I had spent less time imagining the person who would try it in earnest and come back with something I didn’t recognize.

I hope I give that person room to show me what they built. My first impulse will be to explain what I meant. I want to wait long enough to hear what they understood, and to look at the passages and examples that led them there. If I have to supply a missing rule in conversation, I should put it in the public specification. If they found a better way to implement a rule, I should be able to point to the result and give them credit. And if their version and mine disagree about something fundamental, I want us to be able to say what it is in terms that a third person can test.

I used to think the milestone would be getting the framework written down. Then I thought it would be getting the code to run. Both mattered. But they left me free to fill in whatever I had failed to explain. This stranger has given me a chance to find out how much of the work can travel without me.

I’m eager to see the first place it surprises us both.
