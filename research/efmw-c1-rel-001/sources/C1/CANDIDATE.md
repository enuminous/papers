# EFMW-LAGRANGIAN-C1 — frozen candidate

Version 1.0.0. Frozen for Matthew Chenoweth Wright, October 13, 2026 (Pacific).

This is a proposed classical effective action family. It is a versioned construction from the preceding chat derivation, not a claim that the historical catalogue has been proved correct or that these fields exist in nature. The scalar interaction checks cover formal coefficient identities for every allowed coefficient value; physical stability does not follow from them.

## Fixed conventions

Use signature $(-,+,+,+)$, $c=\hbar=1$, $M_{\rm Pl}^2=(8\pi G)^{-1}$, and
$\Box_g=g^{\mu\nu}\nabla_\mu\nabla_\nu$. The curvature convention and every normalization are in [conventions.json](conventions.json). Variations have compact support. Geometry remains a background in triplets without the dynamical-gravity sector E.

Fields: $g_{\mu\nu}$, two Abelian potentials $A_\mu,B_\mu$, and eight neutral real canonical fields $\varphi_a$, with $a\in\{F,W,T,I,R,H,P,A\}$. Write $F=dA$, $H=dB$, $X=F_{\mu\nu}F^{\mu\nu}$, $Y=H_{\mu\nu}H^{\mu\nu}$. The catalogue denotes $H$ by $S$. Sector labels E and P do not identify the root equation's energy and rotational source.

## Bulk action

$$S_{C1}=\int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}(R-2\Lambda)-\frac14X-\frac14Y-\frac12\sum_a\nabla_\mu\varphi_a\nabla^\mu\varphi_a-\mathcal U\right].$$

The finite catalogue audit is source-free: $\mathcal L_{matter}=0$. A specified gauge- and diffeomorphism-invariant matter action may be added as a separately versioned extension. Arbitrary source currents are not silently introduced.

Let $Q_E=R$, $Q_M=X$, $Q_S=Y$, and $Q_a=\varphi_a$, in the order E,M,S,F,W,T,I,R,H,P,A. Then

$$\mathcal U=\frac12\sum_a(m_a^2+\xi_aR)\varphi_a^2+\sum_{i<j}g_{ij}Q_iQ_j+\sum_{i<j<k}h_{ijk}Q_iQ_jQ_k.$$

The $g$ and $h$ coefficients are independent spacetime constants indexed by unordered sectors. They carry the required dimensions; they are not fitted values. This ansatz is not the most general invariant action. It has 55 pair slots and 165 triple slots, plus masses, nonminimal couplings, gravity and the cosmological term. The 165 triple slots are not 165 established forces.

## Actual variations

$$\Box_g\varphi_a-\mathcal U_{,a}=0.$$

$$\nabla_\mu[(1+4\mathcal U_X)F^{\mu\nu}]=0,\qquad \nabla_\mu[(1+4\mathcal U_Y)H^{\mu\nu}]=0.$$

$$\nabla_{[\lambda}F_{\mu\nu]}=0,\qquad\nabla_{[\lambda}H_{\mu\nu]}=0.$$

The latter are identities, not extra Euler–Lagrange equations. The metric equation is

$$M_{\rm Pl}^2(G_{\mu\nu}+\Lambda g_{\mu\nu})=T^{(0)}_{\mu\nu}+T^{(U)}_{\mu\nu},$$

$$\begin{aligned}T^{(U)}_{\mu\nu}={}&-g_{\mu\nu}\mathcal U+2\mathcal U_RR_{\mu\nu}+2(g_{\mu\nu}\Box_g-\nabla_\mu\nabla_\nu)\mathcal U_R\\&+4\mathcal U_XF_{\mu\rho}F_\nu{}^\rho+4\mathcal U_YH_{\mu\rho}H_\nu{}^\rho.\end{aligned}$$

Here $T^{(0)}$ is the sum of canonical scalar kinetic stresses and the two Maxwell stresses. The displayed $T^{(U)}$ assumes exactly the dependence $\mathcal U(\varphi,R,X,Y)$ and no hidden metric dependence in unspecified external source functions.

## Projection and comparison

Restrict the action before variation. Set couplings naming absent sectors to zero. Delete inactive scalar and gauge fields. Vary the metric only when E is active. Retain the background-curvature terms $\xi_aR\varphi_a^2/2$ in every scalar block.

For each source scalar equation $\Box\varphi_a+C_a=0$, compare its positive source polynomial $C_a$ with the independently differentiated $\partial\mathcal U/\partial\varphi_a$. Equality of these magnitudes does **not** establish equality of the source equation: the action requires the minus sign. The change is a declared correction, not multiplication of the entire source equation by minus one.

## Root scalar branch

For the separate physical root relation, with $c$ explicit,

$$\nabla^2\phi-c^{-2}\partial_t^2\phi=\beta J,\quad\beta=4\pi/c^2,\quad J=E+cP,$$

the density is

$$\mathcal L_{root}=\frac{Z}{2c^2}\dot\phi^2-\frac Z2|\nabla\phi|^2-Z\beta J\phi,\quad Z>0.$$

Treat $J$ as independent of $\phi$ during this variation. Its physical source model is not supplied by C1. A canonical embedding uses $\varphi=\sqrt Z\phi$ and a linear potential $\sqrt Z\beta J\varphi$; that external-source addition is outside the source-free frozen master. Overall normalization is not selected by the root equation. Physical E/P definitions, including rotational P, remain open.

## Freeze rule

[FREEZE.json](FREEZE.json) hashes this specification, the conventions, the independent action generator, parser, and exact arithmetic implementation. Any change to a locked file requires a new candidate version and a new audit. Historical source blobs remain byte-for-byte unchanged.
