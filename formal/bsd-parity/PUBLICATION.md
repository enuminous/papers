# Publication provenance

This package accompanies [Exact Parity in a Three-Prime Elliptic-Curve Image](../../BSD-Three-Prime-Parity-and-Fixed-Invariants.md), Matthew Chenoweth Wright, 17 October 2026.

The 23 files of the previously verified `BSD-Improvements-2026-10-17.zip` were extracted unchanged. Its SHA-256 is:

```text
fa7fb44ba8ea3437c2896cbdb1ddf870b53464a6785d462392f69d66e68edde4
```

`SHA256SUMS` covers the 22 original files other than itself. It does not include this new publication note or repository-level publication files. The original verification logs record local verification, not the subsequent GitHub run.

The source illustration, `https://cknights.com/works/bsd/sphere_cube_bessel.html`, was retrieved again on 17 October 2026 and matched the earlier audited bytes:

```text
bytes: 363288
sha256: 6443bb640ca8a4a160ec3577ab2807ed677f7b30a17c3be1066375e05c399276
```

The upstream Ramtastic snapshot is `916ab476012852778edd9ca63aecf200a8e90ed1`. The actual mathematical target here is identified by coefficients `[1,-1,0,-79,289]` and the four named points, not by a database label.

The repository-level [BSD workflow](../../.github/workflows/bsd-parity.yml) verifies original file digests before any logs are regenerated, builds the package using its pinned toolchain, runs the exact arithmetic and theorem-axiom checks, and checks that dependency declarations stay unchanged. See the [run history](https://github.com/enuminous/papers/actions/workflows/bsd-parity.yml) for the actual GitHub outcome.

The general reduction map from E(Q), rational basis saturation, canonical-height identification, actual L-function comparison, central vanishing, and full BSD equality remain outside this package's established conclusions. The manuscript explains these boundaries.
