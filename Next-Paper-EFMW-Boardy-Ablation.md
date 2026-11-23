# Next paper · What the EFMW + Boardy ablation can identify
## A counterexample and a two-arm amendment to DEV2-001

**November 23, 2026 · Methods note · Follow-on protocol proposed**

### Abstract

DEV2-001 can test whether the combined workflow reduces unsupported assertions relative to direct answering. We show that even agreement across all five current arms can leave the interaction between provenance labeling and targeted criticism undetermined. Two additional arms complete a matched-budget comparison among revised answers. A finite check confirms the counterexample. The result concerns identification by design. No models were run and no benchmark performance was estimated.

### 1. The missing comparisons

The first [EFMW and Boardy paper](https://github.com/enuminous/papers/blob/e9167038069051d6251a20a4f67b0554334f4c2a/EFMW-and-Boardy-Methods-Paper.md) proposed removing provenance labeling, targeted criticism, and revision in turn. The [DEV2-001 protocol](https://github.com/enuminous/Devs2.0/blob/3ddaf05c27954866c44ad9603aac09960b6d9d21/research/dev2-001/PROTOCOL.md) already has two three-stage arms. C uses a provenance-tagged draft and targeted criticism. E uses a plain draft and generic feedback. Both revise. Their difference changes two factors at once. A, B, and D have no feedback-plus-revision stage and give no observation of the two missing three-stage combinations.

| Draft policy | Generic feedback, then revision | Targeted criticism, then revision |
| --- | --- | --- |
| Plain | E | **New arm** |
| Provenance-tagged | **New arm** | C |

The table describes a prospective amendment. Reuse C and E as the diagonal only if prompt inspection confirms that intended factor changes are the only material differences. If the existing prompts differ elsewhere, write matched versions of all four cells and leave the original C and E defined as before.

### 2. Counterexample

On an evidence-absent item let 1 denote an unsupported assertion and 0 its absence. Suppose E scores 1 and C scores 0. Give A, B, and D identical outputs across the following two worlds.

| World | Plain + generic (E) | Plain + targeted | Tagged + generic | Tagged + targeted (C) |
| --- | ---: | ---: | ---: | ---: |
| I | 1 | 0 | 0 | 0 |
| II | 1 | 1 | 1 | 0 |

Define the targeted-criticism gain as generic loss minus targeted loss at a fixed draft policy. In World I, the gain is 1 with a plain draft and 0 with tags. In World II, it is 0 with a plain draft and 1 with tags. The interaction, tagged gain minus plain gain, is **−1** in the first world and **+1** in the second. The observed arms agree in both worlds. The unobserved cells therefore determine even the sign. Repeating the construction across evidence families preserves the ambiguity under family-weighted averaging. These are counterexamples, not forecasts about how frequently any outcome occurs.

### 3. What to measure in the amended design

Use the same held-out items, retrieved passages, pinned model and settings, and randomized arm order. Keep revision instructions, citation rules, evidence access, and per-stage budgets common. For the four three-stage cells, use the protocol's draft/feedback/revision allotment of 256/256/512 generated tokens under the shared total-token ceiling. Record actual consumption. Use isolated state and preserve the full earlier stage outputs in each arm. Keep evaluators blind to arm assignment where feasible and declare how visible formatting may reveal a condition.

For each family, compute the criticism gain within each draft policy, then subtract the plain gain from the tagged gain. Average the family-level interaction and report its paired uncertainty interval. Also report both within-policy gains, supported-answer and conflict-report rates, unnecessary abstention, and resource usage. Declare all confirmatory versus exploratory comparisons and multiplicity handling before accessing the holdout. The original C-versus-A absent-tier endpoint and 20-point target remain separate.

This comparison identifies the interaction of two **assigned policies** under the tested implementation. It cannot establish which internal reasoning mechanism a model used. A secondary paired comparison of the retained draft and revised answer can count when revision corrects an error or damages a correct draft. That comparison estimates the effect of submitting the revision after feedback and includes the additional generation that revision uses. It does not establish an effect of the Boardy role itself.

### 4. Replay

Save the block below as `check_ablation.py` and run `python3 check_ablation.py`. It enumerates all binary loss tables and checks the interaction identity and the counterexample. The calculation is exact and requires only the standard library.

```python
from itertools import product

# Order: plain/generic, plain/targeted, tagged/generic, tagged/targeted.
def effects(table):
    pg, pt, tg, tt = table
    return pg - pt, tg - tt, (tg - tt) - (pg - pt)

tables = list(product((0, 1), repeat=4))
for table in tables:
    pg, pt, tg, tt = table
    plain_gain, tagged_gain, interaction = effects(table)
    assert interaction == (pt - tt) - (pg - tg)
    assert abs(interaction) <= 2

# E and C agree across worlds. The two intermediate cells are unobserved.
compatible = [t for t in tables if t[0] == 1 and t[3] == 0]
interactions = sorted({effects(t)[2] for t in compatible})
assert interactions == [-1, 0, 1]
assert effects((1, 0, 0, 0))[2] == -1
assert effects((1, 1, 1, 0))[2] == 1
print(f"{len(tables)} tables checked; {len(compatible)} compatible.")
print(f"Compatible interaction values: {interactions}")
```

Observed output:

```text
16 tables checked; 4 compatible.
Compatible interaction values: [-1, 0, 1]
```

### 5. Disposition

**Established:** the original design leaves the provenance-by-criticism interaction unidentified without additional assumptions. Two crossover arms supply the missing observations when C and E can act as matched diagonal cells.

**Open:** whether targeted criticism, provenance labeling, or their interaction helps on held-out tasks. The amendment remains proposed. DEV2-001 is unfrozen and unrun. This note leaves the benchmark and its repository untouched.
