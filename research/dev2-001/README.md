# DEV2-001: Provenance and Adversarial Criticism Benchmark

**DRAFT, NOT FROZEN · 22 October 2026 · No experimental result**

This executable draft develops the existing [Boardy proposal](../../DEVS2-Protocol.md),
testing the bounded architecture claim in [Devs 2.0, section 16](../../Devs2.0-EFMW.md).
It does **not** validate EFMW physics, demonstrate a new law, or establish novelty.

## Start here

- [Protocol](PROTOCOL.md): target, arms, budgets, scoring, failure and release rules.
- [Design decision brief](DESIGN.md): category distributions, pass thresholds and statistical consequences.
- [Scoring manual](SCORING.md): two independent human raters, blinding and adjudication.
- [Reproducibility guide](REPRODUCIBILITY.md): exact commands, adapter contract and freeze procedure.
- [Run report template](RUN.md): a report to complete only after a real run.
- [Source and reuse audit](SOURCE_AUDIT.md): existing work, scoped search and evidence boundaries.

`CORPUS.json` pins ten document versions by full Git commit and SHA-256. The
current-document anchor is `c4e9d7cf4a2dbf6646aaf45f39d75593fa674331`.
Historical versions are separate manifest entries. The corpus excludes this
benchmark's protocol, questions, answers and future results.

`QUESTIONS.schema.json` defines the private question/gold ledger. There are twelve
**unreviewed development examples** in `development/QUESTIONS.json`.
The held-out `QUESTIONS.json` is intentionally empty. No development example may
later be relabeled as held-out. There are no independently verified Tier C
questions yet. Historical amendments alone do not establish contradictions.

## What runs now

From the repository root, using Python 3.12:

```bash
python -m unittest discover -s research/dev2-001/tests -v
python research/dev2-001/prepare.py --out /tmp/dev2-plan.json
python research/dev2-001/planning.py
python research/dev2-001/prepare.py --questions research/dev2-001/QUESTIONS.json --check-freeze --out /tmp/dev2-evaluation-plan.json
```

The last command **must refuse** the present draft. The first three commands use
no paid APIs. Tests use fabricated outcomes solely to check software behavior;
planning calculations are assumptions, not measured performance.

The live runner is provider-neutral: supply a pinned model/tokenizer and an
audited adapter satisfying the documented JSON contract. No provider adapter,
model access, spending authorization or completed model run is implied here.
The adapter contract and orchestration are executable, but an actual provider
integration still needs development testing before freeze.

## Recommended design awaiting Matthew's decision

**480 evaluation questions: 120 answerable, 240 absent, 120 contradictory**;
60 separately authored development questions; at least one independent evidence
family per evaluation question under this proposed design. Do not pad the corpus
with paraphrases to meet the sample size. If 120 genuine conflict families cannot
be found, revise the corpus or the proposed design **before** freeze.

Proposed primary pass: C reduces absent-tier false assertions versus A by at
least **20 percentage points**, paired 95% bootstrap interval above zero,
mean total tokens at most **1.5×**, and answerability/conflict guardrails met.
All numbers, including the additional guardrails, remain proposals.

Approval of the mix and margin alone does not freeze the experiment. A complete
reviewed holdout, pinned model/adapter, price schedule, retrieval coverage review,
human scoring roles and dated approval record must also be committed first.
The analyzer never automatically issues `SUPPORTED`; independent reproduction
and a reviewed release record are required.
