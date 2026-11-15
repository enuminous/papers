# Dependency Map

## Established identities

\[
\alpha=\frac{e^2}{4\pi\epsilon_0\hbar c}
\]

\[
c^{-2}=\mu_0\epsilon_0
\]

\[
\ell_P^2=\frac{\hbar G}{c^3},\qquad
t_P^2=\frac{\hbar G}{c^5},\qquad
m_P^2=\frac{\hbar c}{G}.
\]

## Classification

| Quantity | Role |
|---|---|
| \(c\) | exact SI constant / invariant speed |
| \(e\) | exact SI constant |
| \(h,\hbar\) | exact SI constants |
| \(G\) | measured gravitational coupling |
| \(\epsilon_0,\mu_0\) | EM constants tied to the modern SI and measured \(\alpha\) |
| \(\alpha\) | dimensionless measured coupling; preferred generative target |

## Non-circularity criterion

A derivation of \(\alpha\) is nontrivial only if \(\alpha\) is not used directly or indirectly as an input.

Bad:
- setting a free parameter equal to \(\alpha\);
- renaming \(\alpha\) and substituting it back;
- fitting a coefficient after seeing the target.

Potentially meaningful:
- deriving \(\alpha\) from independently fixed integer, topological, symmetry, or invariant data;
- deriving a new relation among multiple dimensionless observables that can be tested independently.


## Numerical provenance

The repository's numerical verifier uses the NIST **2022 CODATA recommended values**, the latest CODATA adjustment currently available at the time of this audit (October 2026). In particular it uses \(\epsilon_0=8.8541878188\times10^{-12}\,\mathrm{F\,m^{-1}}\) and compares against \(\alpha^{-1}=137.035999177\). Source: NIST Fundamental Physical Constants, https://physics.nist.gov/constants.
