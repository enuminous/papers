# Derivations and counterexamples

## Conventions and scope

Use the C1 convention \((-+++ )\), \(c=\hbar=1\), a flat fixed metric and canonical real scalars. Let \(X=F_{\mu\nu}F^{\mu\nu}=2(B^2-E^2)\). We identify the M-sector gauge field with laboratory electromagnetism as an explicit operational assumption, not an implication of a sector label. The second gauge field has zero background. Unless stated otherwise, these are classical results near the scalar origin, with a positive definite scalar mass-squared Hessian and positive gauge kinetic factor in the field domain used.

The original ME-002 branch is treated separately with its own stated operator convention. Its alpha parameter is not identified with the electromagnetic fine-structure constant.

## 1. Why C1 does not require a mass–coupling function

The one-scalar, one-gauge C1 projection is

\[
\mathcal L=-\frac14(1+g\sigma)X
-\frac12\partial_\mu\sigma\partial^\mu\sigma
-\frac12m^2\sigma^2,
\qquad g=4g_{MW}
\]

when the W scalar is selected. C1 declares its coupling slots independent. Its mass and its gauge–scalar pair coefficient are separate inputs.

Choose an arbitrary positive energy unit \(M_*\), and restrict the field domain to \(|\sigma|\le M_*\). Consider

| Model | \(m/M_*\) | \(gM_*\) | Minimum \(1+g\sigma\) on that domain |
| --- | ---: | ---: | ---: |
| A | 1 | 1/100 | 99/100 |
| B | 1 | 1/50 | 49/50 |
| C | 2 | 1/100 | 99/100 |

All have positive scalar mass and positive gauge kinetic factor in the same domain, with weak fields chosen around the vacuum. A and B have the same mass and different nonzero couplings. A and C have the same coupling and different masses. These are exact parameter countermodels, not measurements or phenomenological fits.

Consequently, no mandatory single-valued relation \(g=f(m)\) follows from this C1 subfamily and these local consistency conditions. More generally, the allowed parameters contain an open set; a nonzero polynomial equality between \(m\) and \(g\) cannot hold throughout it. Such a polynomial would vanish on an interval in one variable for each value of the other, forcing all its coefficients to vanish.

This does not prove that a more restricted future theory cannot relate the parameters. It proves that the restriction is additional to the frozen inputs.

## 2. Low-energy matching with all scalar mass mixing included

Let \(\varphi\) collect the active canonical scalar fields. At \(\varphi=0\), \(R=0\), \(Y=0\), write the relevant C1 potential as

\[
U=\frac12\varphi^T A\varphi+Xb^T\varphi
+O(\varphi^3,X\varphi^2).
\]

Here \(A=A^T>0\) is the complete scalar mass-squared Hessian, including scalar-pair coefficients. The components of \(b\) are the C1 M–scalar coefficients. Because the catalogue uses distinct sector indices, it contains no independent \(X^2\) term in this branch. This absence is a restriction of the frozen ansatz, not a universal property of effective field theory.

At leading order in field strength and in derivatives divided by scalar masses,

\[
A\varphi+bX+O(X\varphi,\varphi^2)=0,
\qquad
\varphi=-A^{-1}bX+O(X^2,\partial^2X/m_{\min}^2).
\]

Substituting into \(-U\) gives

\[
\mathcal L_{\rm eff}=-\frac14X+
\underbrace{\frac12b^TA^{-1}b}_{a_X}X^2
+\text{higher-field and derivative operators}.
\]

The stationary quadratic term is positive in the effective Lagrangian. Directly differentiating the one-field Lagrangian independently gives \(\sigma=-gX/(4m^2)\), hence \(a_X=g^2/(32m^2)\), checking both sign and normalization.

Take \(A=O\,\mathrm{diag}(m_i^2)O^T\) with real orthogonal \(O\). Canonical mass eigenfields have photon couplings \(g_i=4(O^Tb)_i\). Therefore

\[
\boxed{a_X=\sum_i\frac{g_i^2}{32m_i^2}\ge0.}
\]

Every omitted positive-mass mode adds a nonnegative term. Thus an independently resolved subset \(S\) implies

\[
\boxed{a_X\ge\sum_{i\in S}\frac{g_i^2}{32m_i^2}.}
\]

This result survives the allowed scalar mixing and leading C1 cubic interactions in the stated vacuum. It is a statement about the leading local coefficient. It is not an exact finite-frequency, finite-field bound after all higher-order corrections.

The formula is undefined for a massless mode being integrated out. Negative Hessian eigenvalues violate the assumed stable local scalar vacuum. Integrating out an unstable mode to create a negative term is not an admissible counterexample to this conditional statement.

An independent additional operator \(a_0X^2\) changes the total coefficient to \(a_0+\sum_i g_i^2/(32m_i^2)\). A quantum completion also requires its own matching and renormalization analysis. The frozen C1 record is a proposed classical effective action, so this audit does not claim that its tree-level truncation is an exact quantum prediction.

## 3. Connecting the coefficient to optical propagation

Use

\[
\mathcal L_{\rm em}=\frac12(E^2-B^2)+4a_X(B^2-E^2)^2.
\]

Let the constant background field be \(\mathbf B_0=B_0\hat x\), with zero electric background and a small probe propagating along \(z\). Differentiating the Lagrangian gives

\[
\mathbf D=\frac{\partial\mathcal L}{\partial\mathbf E},
\qquad \mathbf H=-\frac{\partial\mathcal L}{\partial\mathbf B}.
\]

The linearized electric and magnetic response matrices are

\[
\epsilon=(1-16a_XB_0^2)I,
\]

\[
\mu^{-1}=\mathrm{diag}(1-48a_XB_0^2,
1-16a_XB_0^2,1-16a_XB_0^2).
\]

For the local truncated Lagrangian, Maxwell's plane-wave equations then give

\[
n_\perp^2=\frac{1-16a_XB_0^2}{1-48a_XB_0^2},
\qquad n_\parallel^2=1.
\]

The first label describes probe electric field perpendicular to \(\mathbf B_0\). Expanding consistently for \(|a_XB_0^2|\ll1\),

\[
\boxed{n_\perp-n_\parallel=16a_XB_0^2+O((a_XB_0^2)^2)}.
\]

For general C1, the omitted higher-field and derivative operators give additional corrections. The rational expression above is not an exact resummation of those omitted operators. Positive electric and magnetic response in this simple truncated background is ensured by taking fields sufficiently small, in particular \(48a_XB_0^2<1\) when \(a_X\ge0\).

For a one-mode model,

\[
\Delta n_{\rm scalar}=\frac{g^2B_0^2}{2m^2}+\cdots.
\]

This is the scalar contribution, not the total apparatus signal. Standard quantum-electrodynamic terms, matter, other sectors and instrumental effects must be treated separately. Local matching requires the relevant frequencies and momentum transfers much smaller than every scalar mass integrated out. An on-shell regeneration experiment requires higher energy and must use the propagating-scalar calculation from OBS-001 instead.

Dimensions check: \([\sigma]=1\), \([g]=-1\), \([m]=1\), \([X]=4\), \([a_X]=-4\), and \([B]=2\) in energy units. Both \(a_XX^2\) and the original density have dimension four; \(a_XB^2\) and \(\Delta n\) are dimensionless.

## 4. Why a two-channel rank-one relation is not a general prediction

The C1 action permits a direct pair term \(dXY\) in its potential, independently of scalar exchange. Select one scalar with

\[
U=\frac12m^2\sigma^2+\sigma(bX+cY)+dXY.
\]

Eliminating the scalar gives the quartic response

\[
\mathcal L^{(4)}=\frac{(bX+cY)^2}{2m^2}-dXY
=\frac12q_{XX}X^2+q_{XY}XY+\frac12q_{YY}Y^2,
\]

where

\[
q_{XX}=b^2/m^2,\quad q_{YY}=c^2/m^2,\quad
q_{XY}=bc/m^2-d.
\]

The determinant is

\[
q_{XX}q_{YY}-q_{XY}^2=2dbc/m^2-d^2.
\]

It vanishes for the one-mode, no-contact branch, but C1 does not require that branch. In units of a chosen energy scale, \(m=1\), \(b=c=1/100\), \(d=3/10000\) give determinant \(-3/10^8\), rather than zero. The dimensions of \(b,c\) are inverse energy and that of \(d\) inverse energy to the fourth power. Sufficiently small fields preserve the locally positive Maxwell kinetic terms; no global ultraviolet-consistency claim is made for this example.

Even with \(d=0\), two scalar modes separately coupled to the two gauge sectors give a positive diagonal response matrix and a nonzero determinant. The isolated one-scalar exchange contribution has rank one; the complete C1 response need not. A choice to set all other modes and contacts to zero must be labeled as a model restriction.

## 5. Positivity cannot fix the desired nonzero coupling

For a single scalar, the gauge kinetic factor is \(K(\sigma)=1+g\sigma\). If \(g\ne0\), evaluating at \(\sigma=-2/g\) gives \(K=-1\). Hence

\[
K(\sigma)>0\text{ for every }\sigma\in\mathbb R
\quad\Longleftrightarrow\quad g=0.
\]

On a declared compact field domain \(|\sigma|\le\Phi\), its minimum is \(1-|g|\Phi\), so strict positivity is equivalent to \(|g|\Phi<1\). This permits a continuum of couplings. A nonlinear positive kinetic function, a different field domain, or additional dynamics could change the conclusion, but would require a separately specified model. Neither the global nor local condition supplies a nonzero mass–coupling equality.

## 6. Root normalization and the separate alpha branch

The C1 root branch supplies the family

\[
\mathcal L_{\rm root}=\frac{Z}{2c^2}\dot\phi^2-
\frac Z2|\nabla\phi|^2-Z\beta J\phi,
\quad Z>0,\quad\beta=4\pi/c^2.
\]

For a source independent of \(\phi\), variation and division by \(Z\) give the same PDE for every positive \(Z\). Canonical normalization \(\sigma=\sqrt Z\phi\) changes the source term to \(-\sqrt Z\beta J\sigma\). Thus the PDE alone does not select a canonical coupling or an absolute field-energy normalization. Operational definitions of \(J=E+cP\), the source, and the measurement coupling remain necessary. This is an identifiability gap, not proof that differently normalized complete physical models must be observably different after all other couplings are transformed consistently.

Separately, canonical ME-002 combined with ME-004 and zero source, treating alpha as a real spacetime constant, gives

\[
\frac{1-\alpha^2}{c^2}\phi_{tt}-\nabla^2\phi=0.
\]

For a plane wave,

\[
\omega^2=\frac{c^2 k^2}{1-\alpha^2}.
\]

For real \(|\alpha|<1\), the wave speed is \(v=c/\sqrt{1-\alpha^2}\), strictly above \(c\) when \(\alpha\ne0\). At \(|\alpha|=1\), the time-derivative term vanishes. For \(|\alpha|>1\), real nonzero spatial Fourier modes have imaginary frequency, so this is not the same hyperbolic wave evolution. These are equation-level statements; no sensor or measurement is inferred from them.

The reviewed canonical text does not identify this alpha with the electromagnetic fine-structure constant, and C1's separate root branch has no alpha term. Combining them silently would change the model. Requiring a wave speed no greater than \(c\), as an additional condition, would force \(\alpha=0\) on the real hyperbolic branch. It would not produce a nonzero distinctive parameter prediction.
