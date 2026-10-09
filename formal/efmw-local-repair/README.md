# EFMW local-repair core

This is a deliberately narrow formalization of the observer → discrepancy →
local repair loop. It separates local information flow from the global
convergence condition, so locality is not accidentally treated as a
convergence proof.

## Frozen model

- A state assigns a real value to each node.
- A neighborhood is a directed adjacency relation.
- A residual at node `i` is local when it is unchanged by replacing a state
  with another state that agrees at `i` and every adjacent node.
- A synchronous repair is `xᵢ ↦ xᵢ − η rᵢ(x)`, with `η ≠ 0`.
- A global contraction factor `q < 1` is an independent hypothesis on the
  state update. Graph connectivity alone does not establish it.

## Results encoded

1. A local residual yields a local one-step repair rule.
2. For nonzero gain, the repair update is fixed exactly when every residual is
   zero.
3. A strict contraction has at most one fixed point.
4. Given an existing fixed point, iteration error is bounded by
   `q^n · dist(x, x*)`.
5. If geometric decay of `q^n` is supplied, the iterates converge in metric
   distance to that fixed point.
6. Pairwise synchronous swap has a period-two orbit; identity repair has
   multiple equilibria. These falsify convergence/uniqueness claims without
   the corresponding assumptions.

## Deliberate limits / open proof obligations

- This core does **not** prove that a fixed point exists. An existence result
  needs a complete state space and a Banach fixed-point theorem, or a
  system-specific invariant/compactness argument.
- `GeometricDecay q` is explicit so the convergence proof does not hide a
  library lemma. It should be discharged from the standard real geometric
  sequence theorem for `0 ≤ q < 1` in the pinned Mathlib version.
- No EFMW empirical constants, measurements, causal claims, or novelty claims
  are assumed or encoded here.
- The pair-swap counterexample records an exact 2-cycle; the project does not
  elevate that example into a general instability theorem.

## Build

With Lean 4.19.0 and network access to the pinned Mathlib tag:

```sh
lake update
lake build
```

The authoring environment for this artifact had no `lean`/`lake` executable,
so kernel compilation remains pending. There are no `sorry` or axioms in the
source; that is not a substitute for a successful build.
