# Nonzero local vorticity from two C1 scalar fields

**EFMW-C1-LOCAL-VORT-001 v1.0.0 — conditional mathematical result, 18 October 2026.**

Two canonical scalar fields in an allowed fixed-background specialization of the parent C1 action admit an exact solution whose **total Landau energy flow develops nonzero local vorticity from zero initial flow and vorticity**. Each constituent scalar's own flow remains irrotational. Symbolic identities and an independent numerical stress-tensor calculation verify the construction.

This establishes an existence result under specified inhomogeneous initial conditions. It does not derive rotation from an exactly homogeneous/isotropic universe, solve the Einstein equations, predict a cosmic rotation rate or explain a CMB alignment. All special C1 interaction coefficients are zero in this example: the mechanism belongs to ordinary multicomponent scalar-field dynamics and is not evidence of a uniquely EFMW force.

This is a derivation and executable appendix to the existing [CMB research companion](../../README.md), [R-001](../../../../EFMW-Zoo-R001-Primordial-Recursion-Boundary.md) and [Great Recursion](../../../../great-recursion-primordial-rotation.md), not a separate publication. The [C1Q prediction lock](../../prediction-lock/v1/LOCK.md) remains unchanged; its single-field/linear cosmological scope differs from this construction.

## 1. Frozen objects and assumptions

The [protocol](protocol.json), including the proposed formula, numerical gates, ablations and orientation seed, was committed in [a135f5b](https://github.com/enuminous/papers/commit/a135f5b88d6421a6edcfd08c6b91bf9d26431604) before execution. Its SHA-256 is `ecbd2498dfb0d6ee6e45b6410b6d6bb27e3712ce46a9fe151a79b0823411db18`. This is a computational prediction freeze, not external empirical preregistration.

The source [C1 candidate](source/C1-CANDIDATE.md) and [conventions](source/C1-conventions.json) were recovered from the frozen C1Q archive; byte hashes and archive provenance are in the protocol. C1 permits prescribed background geometry when its dynamical metric sector E is inactive. Activate its real scalar fields F and W, here called \(\phi,\chi\); set their masses, nonminimal couplings, all pair/triple interactions and gauge fields to zero. This is a declared specialization of C1, **not a modification of C1Q v1**.

Use signature \((-+++ )\), \(c=\hbar=1\), fixed Minkowski metric, and action

$$S=-\frac12\int d^4x\left(\partial_\mu\phi\,\partial^\mu\phi+\partial_\mu\chi\,\partial^\mu\chi\right).$$

The equations are \(\Box\phi=\Box\chi=0\). A nonzero stress tensor on this fixed background is permitted by the chosen test-field problem. It would **not** satisfy the full finite-\(G\) Einstein equations with a Minkowski metric; no such claim is made.

Let \(\tau=t/L,\xi=x/L,\eta=y/L,\zeta=z/L\), for arbitrary positive length \(L\), and let \(\Phi_* >0\) have mass dimension one. The following are exact wave-equation solutions:

$$\phi=\Phi_*\tau f(\xi),\qquad \chi=\Phi_*\tau g(\eta),\qquad
f=p+\alpha\xi,\quad g=q+\beta\eta.$$

Their second time derivatives and spatial Laplacians vanish separately. Freeze

$$p=q=1,\quad\alpha=1,\quad\beta=2,\qquad
0\le\tau\le0.1,\quad |\xi|,|\eta|\le0.2.$$

Both gradients are timelike on this patch because \(f^2-\alpha^2\tau^2>0\) and \(g^2-\beta^2\tau^2>0\). The smallest margin is 0.32. The solution is independent of \(\zeta\). These polynomial fields are not globally bounded or finite energy; the claim is local.

At \(\tau=0\), both fields and their spatial gradients vanish. Their time derivatives are \(\Phi_*f/L\) and \(\Phi_*g/L\), respectively. Thus there is **no initial momentum density, velocity or vorticity**, but there are already prescribed spatial gradients of the initial scalar momenta and energy density. Their directions, unequal magnitudes and scale are inputs. This distinction prevents the construction from being called spontaneous rotation of exactly isotropic initial data.

## 2. Specify the congruence before calculating rotation

For one scalar with timelike gradient, the future-directed normalized velocity has covector \(u_\mu=-N\partial_\mu\phi\), \(N>0\), on this patch. Therefore

$$u\wedge du=(-N\,d\phi)\wedge(-dN\wedge d\phi)=0.$$

Frobenius implies zero projected vorticity, independently of a scalar potential. Normalizing a gradient does not defeat this identity. Where the scalar gradient vanishes or ceases to be timelike, this fluid identification is undefined; that is not a vorticity detection. The same argument applies separately to \(\chi\). This standard single-scalar limitation is discussed by [Faraoni et al. (2023)](https://link.springer.com/article/10.1140/epjc/s10052-023-11186-7).

For the **sum** of the scalar stresses, specify instead the unique future-directed unit timelike Landau eigenvector:

$$T^{\mu\nu}u_\nu=-\rho_Lu^\mu,\qquad u_\mu u^\mu=-1,\quad u^0>0.$$

It is the local frame with zero total energy flux. It is generally not proportional to either scalar gradient or to the gradient of their sum. Its vorticity is an invariant of this specified congruence, not an assertion that every constituent, baryon observer or cosmic fluid has that vorticity.

With all stress components below normalized by \(\Phi_*^2/L^2\), define

$$A=f^2+g^2,\quad B=\alpha^2+\beta^2,\quad
\rho_0=\frac12(A+\tau^2B),\quad P_0=\frac12(A-\tau^2B).$$

Direct variation gives

$$T^{00}=\rho_0,\qquad
(T^{01},T^{02},T^{03})=-\tau(\alpha f,\beta g,0),$$

$$T^{ij}=P_0\delta^{ij}+\tau^2\operatorname{diag}(\alpha^2,\beta^2,0).$$

\(P_0\) is the isotropic part in these coordinates, not an assumption that the combined stress is a perfect fluid. Each scalar stress and their sum obey \(\partial_\mu T^{\mu\nu}=0\).

Write \(u^\mu=\gamma(1,v_x,v_y,0)\), \(r=\rho_L+P_0\), and

$$d_1=r+\alpha^2\tau^2,\qquad d_2=r+\beta^2\tau^2.$$

The eigenvector equations reduce to

$$v_x=-\frac{\tau\alpha f}{d_1},\qquad v_y=-\frac{\tau\beta g}{d_2},$$

$$F(r)\equiv r-A+\tau^2\left(\frac{\alpha^2f^2}{d_1}+\frac{\beta^2g^2}{d_2}\right)=0.$$

Choose the branch \(r\to A\) as \(\tau\to0\), with \(s=1-v_x^2-v_y^2>0\), and \(\gamma^2=1/s\). On the frozen patch, \(A\ge1\), \(F(A/2)<0\), \(F(A)>0\) for \(\tau>0\), and \(F_r=s\ge0.84\) throughout this bracket. Hence there is a unique physical root there. At \(\tau=0\), \(r=A\). A zero root arising on another algebraic branch at nonzero time is not the timelike solution and is not used.

## 3. Exact nonzero result

Fix right-handed spatial coordinates and \(\epsilon^{0123}=+1\). Define dimensionless vorticity by

$$\widehat\omega^\mu\equiv L\omega^\mu
=\frac12\epsilon^{\mu\nu\rho\sigma}u_\nu\partial_{y^\rho}u_\sigma,
\qquad y^\mu=(\tau,\xi,\eta,\zeta).$$

For the planar flow,

$$\widehat\omega^z=\frac{\gamma^2}{2}
\left[\partial_\xi v_y-\partial_\eta v_x
+v_x\partial_\tau v_y-v_y\partial_\tau v_x\right].$$

The time-derivative term matters: retaining only half the three-dimensional curl would give the wrong answer here. Implicit differentiation of \(F(r)=0\) yields

$$r_{,\xi}=\frac{2\alpha f r}{d_1s},\qquad
r_{,\eta}=\frac{2\beta g r}{d_2s},\qquad
r_{,\tau}=-\frac{2r(1-s)}{\tau s},$$

with the continuous zero limit for the last expression at \(\tau=0\). Substitution gives the identical expressions

$$\partial_\xi v_y-\partial_\eta v_x
=v_x\partial_\tau v_y-v_y\partial_\tau v_x
=\frac{2\tau^3\alpha\beta fgr(\alpha^2-\beta^2)}{s\,d_1^2d_2^2}.$$

Consequently,

$$\boxed{\widehat\omega^z=
\frac{2\tau^3\alpha\beta fgr(\alpha^2-\beta^2)}{s^2d_1^2d_2^2}},\qquad
\widehat\omega^0=\widehat\omega^x=\widehat\omega^y=0.$$

This is generically nonzero for nonzero time, nonzero orthogonal gradients and unequal squared gradient magnitudes. Its invariant squared norm is \(\omega_\mu\omega^\mu=(\widehat\omega^z/L)^2>0\). Changing the orientation convention reverses the signed component, not this conclusion.

For the frozen parameters at the spatial origin,

$$\boxed{\widehat\omega^z=-\frac32\tau^3+O(\tau^5)}.$$

In physical units the angular rate is \((c/L)\widehat\omega^z\), with \(\tau=ct/L\). Neither \(L\), \(\Phi_*\), nor these initial profiles are selected by the action; the result is not a numerical cosmological rate. \(\Phi_*\) cancels from the normalized energy-frame velocity for nonzero amplitude, but would matter for gravitational backreaction.

The leading velocity is \(-\tau\nabla\log A/2\), which is curl-free. Relative scalar flows and the combined anisotropic stress develop at later times; the complete energy-frame velocity no longer has a scalar-gradient integrating factor. This is the operative distinction from the single-field no-go. The summed stress cannot be replaced without justification by one barotropic perfect fluid. In its Landau decomposition, stress conservation gives

$$ (\rho_L+P_L)a_\mu+D_\mu P_L
+h_{\mu\nu}\nabla_\alpha\pi^{\alpha\nu}=0,$$

where \(h_{\mu\nu}=g_{\mu\nu}+u_\mu u_\nu\), \(D_\mu=h_\mu{}^\nu\nabla_\nu\), and \(\pi^{\mu\nu}\) is the combined anisotropic stress. Dropping this term would change the system. Standard entropy-gradient sourcing of vorticity at second order in cosmology is already established by [Christopherson, Malik and Matravers (2009)](https://arxiv.org/abs/0904.0940); their perfect-fluid perturbation formula is not silently applied to this exact imperfect composite stress.

## 4. Executed verification

[verify.py](verify.py) performs two distinct computations: a symbolic reduction and a numerical reconstruction of the full \(4\times4\) stress eigensystem. The latter builds stress directly from field derivatives, normalizes its timelike eigenvector, uses fourth-order centered differences of its covector, and contracts the full four-dimensional Levi-Civita tensor. It does not use the proposed vorticity formula to generate its measured result. A separate scalar root solve evaluates the analytic prediction.

All frozen gates passed on the first execution. No formula, seed, tolerance or initial profile was changed after inspecting the result. [results.json](results.json) retains every grid point, all three derivative resolutions, component ablations, symmetry residuals and the random-stream fingerprint.

| Check | Executed result |
|---|---:|
| Exact Klein–Gordon and stress-divergence residuals | Identically zero |
| Individual scalar Frobenius three-forms | Identically zero |
| Implicit-root derivatives, curl and time-cross identities | Exact symbolic equality |
| Spacetime grid | 125 points |
| Maximum eigenvector/root velocity disagreement | \(3.33\times10^{-16}\) |
| Maximum vorticity error, step 0.002 | \(5.48\times10^{-11}\) |
| Maximum vorticity error, step 0.001 | \(3.43\times10^{-12}\) |
| Maximum vorticity error, step 0.0005 | \(2.11\times10^{-13}\) |
| Initial total flow and vorticity | Exactly zero numerically |
| Homogeneous initial momenta | Exactly zero vorticity numerically |
| Remove either field, equal gradient magnitudes, each scalar's own flow | Maximum residual \(3.37\times10^{-14}\) |
| Proper rotation, axial reflection, time-reversal controls | Maximum residual \(2.14\times10^{-13}\) |

At \((\tau,\xi,\eta)=(0.1,0,0)\), the predicted \(\widehat\omega^z=-0.00151855915116196\); the independent eigenvector/difference calculation gives \(-0.00151855915126039\). At \(\tau=0.0025\), the numerical ratio \(\widehat\omega^z/\tau^3=-1.50001185208\), approaching the frozen coefficient \(-1.5\).

The derivative-error reduction is approximately a factor of 16 for each halved step, consistent with fourth-order convergence. Centered derivative stencils evaluate the same exact polynomial solution slightly outside the displayed test grid; the scalar gradients remain timelike there. These are mathematical/numerical checks, not observational significance estimates or a formal proof-assistant audit.

## 5. Nonzero vorticity without an absolute preferred axis

Freeze 10,000 independent Haar-distributed proper rotations using NumPy PCG64 seed **2026101820**, normal draws of shape \((10000,4)\) in C order, normalized unit quaternions \((w,x,y,z)\), and the active rotation matrix implemented in the code. Each realization rotates the **initial field gradients**, reconstructs the stress, solves for the energy frame and recomputes vorticity. Merely rotating a precomputed output was not used as the numerical measurement.

Rotational covariance predicts exactly

$$\mathbb E[\boldsymbol\omega]=0,\qquad
\mathbb E[\omega_i\omega_j]=\frac{|\boldsymbol\omega|^2}{3}\delta_{ij}.$$

The measured component means divided by the fixed magnitude are \((0.00218033,0.01001589,0.00438482)\), compared with the single-component null standard error \(1/\sqrt{3N}=0.00577350\). The normalized second-moment diagonal is \((0.33552189,0.33311962,0.33135849)\); the normalized RMS magnitude is \(0.9999999999975\). The frozen broad calibration gates pass. The analytic ensemble mean is zero; a finite sample mean is not expected to vanish exactly.

This is an isotropic **orientation ensemble of one specified local configuration**. It is not a statistically homogeneous cosmological initial-field ensemble, an instrument/foreground sky null, or evidence that a cosmic axis exists. Nonzero realization vorticity and nonzero RMS coexist with no ensemble preferred direction. The local z axis here has no declared relation to Galactic coordinates or the observed CMB axes. Reflection changes an axial vector with \(\det(R)R\), while time reversal reverses the vorticity; both were tested.

## 6. What is resolved, and what remains necessary

| Question | Disposition |
|---|---|
| Can a specified C1-compatible multiscalar energy frame acquire nonzero local vorticity from zero initial flow? | **Yes**, conditional exact construction verified above |
| Does the normalized flow of either individual scalar rotate? | **No**, exact Frobenius identity |
| Is a new nonzero rotational amplitude inserted as an initial velocity? | **No**; initial energy flow and vorticity vanish |
| Is directional spatial structure supplied in initial data? | **Yes**, explicitly; this is not exact initial isotropy |
| Are uniquely EFMW interactions necessary in this example? | **No**, they are all zero |
| Is a finite-energy global or self-gravitating rotating universe constructed? | **No** |
| Does this derive net global angular momentum? | **No**; no convergent global angular-momentum integral is claimed |
| Is the C1Q v1 zero/linear prediction contradicted? | **No**, different fields, background and nonlinear scope |
| Does it predict PBH-induced CMB alignment, absolute axis, handedness or angular rate? | **No**, these predictions remain unspecified |

For deterministic, smooth, uniquely evolved, rotationally covariant equations, exactly symmetric initial data retain that symmetry. Introducing inhomogeneous realizations can allow local vorticity; their probability law and any instability or symmetry-breaking mechanism must be supplied. This statement does not assume away quantum fluctuations or singular evolution, which are outside the specified problem.

The next physical derivation must choose a cosmological multicomponent congruence, solve the Einstein constraints and subsequent evolution with the scalar sources, and determine an initial statistical ensemble and parameter scale independently of the measured CMB alignment. It must establish any large-scale coherence, vorticity spectrum, amplitude and polarization/handedness prediction, then propagate the perturbations to temperature and polarization maps. A comparison must include nonrotating anisotropic alternatives and the previously declared selection/systematics controls. These are prerequisites for a new cosmological prediction lock, not inferred consequences of this local example.

The parent historical 100,000-object simulation provenance remains unresolved beyond its recovered narrative. No original simulation, PBH dynamics or sky-transfer calculation is recreated here. The existing WMAP significance values are unchanged. The unused C1Q prediction-lock seed is not consumed by this experiment.

**Novelty and Zoo status:** The contribution is a traceable worked construction and a frozen, independently checked calculation inside the existing action family. No new fundamental force, first-in-literature theorem, full-Zoo certification or canonical Tortoise/Brier pass is claimed. Freeze → Predict → Score → Ablate → Replicate applies to this mathematical experiment only; an independent clean CI run is an engineering replication, not an independent physical observation.

## 7. Reproduce

From this directory, with Python 3.12:

```sh
python3.12 -m venv /tmp/efmw-local-vorticity-venv
/tmp/efmw-local-vorticity-venv/bin/pip install -r requirements.txt
sha256sum --check FREEZE.sha256
/tmp/efmw-local-vorticity-venv/bin/python verify.py --check --out /tmp/efmw-local-vorticity-rerun.json
```

The checked-in results are not overwritten by `--check`. All numerical dependencies are pinned. The [dedicated workflow](../../../../.github/workflows/nonzero-vorticity.yml) reruns the symbolic identities, full numerical reconstruction and frozen orientation ensemble. It also validates the original prediction lock without executing that lock's reserved realization set.
