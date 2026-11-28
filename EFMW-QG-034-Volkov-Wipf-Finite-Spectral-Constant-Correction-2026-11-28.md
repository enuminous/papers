# Re-evaluation of the finite spectral constant in the $S^2\times S^2$ gravitational instanton determinant

**Matthew Chenoweth Wright**  
Independent researcher, Monolithic LLC  
28 November 2026

**QG-034 technical note — public correction candidate, not peer reviewed.**

*Publication note:* This Markdown edition reproduces the technical note sent to Mikhail S. Volkov and Andreas Wipf on 28 November 2026, with the distribution status and reproducibility paragraph updated for public publication. Author confirmation has not been established. The numerical results, derivations and scope are unchanged.

## Abstract

We re-evaluate the analytically continued double spectral sum used in Volkov and Wipf, *Nucl. Phys. B* **582** (2000), 313–362. Their Appendix A reports $\Upsilon=Z'(2,-10\mid 0)=-18.3118$. Direct differentiation of the preceding Abel–Plana representation gives an additional polynomial in the printed single-integral numerator. A rectangular Euler–Maclaurin continuation of the defining sum, independent of that integral representation, supports $\Upsilon\simeq-18.20808121537573$. In the authors' determinant convention, substitution increases the finite positive-mode determinant factor by approximately $10.93\%$. The ultraviolet scaling and physical negative mode are unchanged. We invite the original authors to check the calculation; no correction to the complete nucleation rate or claim of new gravitational physics is established.

## 1. The quantity being compared

Following Eq. (A.1) of Ref. [1], define

$$
Z(k,\nu\mid s)=\sum_{n,m=k}^{\infty}
(2n+1)(2m+1)\big[(2n+1)^2+(2m+1)^2+\nu\big]^{-s}.
\tag{1}
$$

For $k=2,\nu=-10$ the minimum denominator is 40; the sum is absolutely convergent for $\operatorname{Re}s>2$ and the desired finite constant is its continued derivative at zero. Equation (5.26) of Ref. [1] specifies the positive-mode combination

$$
\zeta(s)=-9\,2^{-s}+4^sZ(2,-10\mid s),\quad
\zeta'(0)=\frac{1567}{45}\log 2+\Upsilon,
\tag{2}
$$

using $Z(2,-10\mid0)=581/45$. This fixes the normalization and does not include the negative, zero, or scalar exceptional factors. The reported components on p. 360 give $1.9445-19.9469-0.1294=-18.1318$, whereas Eq. (A.50) reports $-18.3118$. The discrepancy of $0.1800$ cannot be explained by the order-$10^{-12}$ cut term or rounding.

## 2. Differentiating the one-axis integral

Put $A=2k+1$, $B=2A^2+\nu$, $x=A+2it$, and $D=B-4t^2+4iAt$. The analytically integrated edge in the original Abel–Plana construction is

$$
\frac12\int_A^\infty y(x^2+y^2+\nu)^{-s}\,dy
=\frac{(x^2+A^2+\nu)^{1-s}}{4(s-1)}.
\tag{3}
$$

The derivative at zero of the right side is $D(\log D-1)/4$. Combining it with the half-endpoint term yields the single-edge numerator (with the convention of Eq. (A.43))

$$
\mathcal G_{\mathrm{new}}(t)=\operatorname{Im}\left[A x\log D-\tfrac12 xD(\log D-1)\right].
\tag{4}
$$

Expanding this expression with the principal logarithm gives the printed Eq. (A.45) plus

$$
\boxed{\mathcal G_{\mathrm{new}}-\mathcal G_{\mathrm{printed}}
=\tfrac12\operatorname{Im}(xD)=(4A^2+\nu)t-4t^3.}
\tag{5}
$$

Using the first and third Bose-factor moments, $\int_0^\infty t/(e^{2\pi t}-1)\,dt=1/24$ and $\int_0^\infty t^3/(e^{2\pi t}-1)\,dt=1/240$, the change to the two-edge term is

$$
2\int_0^\infty\frac{\mathcal G_{\mathrm{new}}-\mathcal G_{\mathrm{printed}}}{e^{2\pi t}-1}\,dt
=\frac{4A^2+\nu}{12}-\frac1{30}=\frac{112}{15}
\tag{6}
$$

for $k=2,\nu=-10$. This identity is not a numerical fit. The real corner, edges and area give

$$
\mathcal H=-\frac{A^2}{4}\log B+\frac{AB}{4}(\log B-1)+\frac{B^2}{32}(3/2-\log B),
\tag{7}
$$

consistent with Eq. (A.44). The mixed-edge term is computed as the difference $W_0(t,u)-W_0(t,-u)$, with $W_0(t,u)=2\operatorname{Re}[x(t)x(u)\log(x(t)^2+x(u)^2+\nu)]$.

The branch point beneath Eq. (A.49) also appears to omit a factor $1/2$ multiplying the radical relative to Eq. (A.41). The upper-half-plane conjugate root obeying the defining polynomial is

$$
z(u)=-\tfrac12+\tfrac12\sqrt{4u^2-A^2-\nu+4iAu},\quad u_*=\sqrt{B/8}.
\tag{8}
$$

It gives $z(u_*)=2+i\sqrt5$ in the target case, consistent with the published suppression factor. The cut contribution is numerically tiny. This second typographical issue does not account for the finite discrepancy.

## 3. Numerical re-evaluation and independent check

| Contribution | Reported in Ref. [1] | Reconstructed |
|---|---:|---:|
| Real terms $\mathcal H$ | 1.9445 | 1.944503411788 |
| Single integral (corrected) | −19.9469 | −20.024413409137 |
| Double integral | −0.1294 | −0.128171218031 |
| Cut | order $10^{-12}$ | $4.598656\times10^{-12}$ |
| Total | −18.3118 | **−18.208081215376** |

The literal printed single integral, before restoration of the polynomial, evaluates to $-27.491080075803$. Thus correcting the displayed arithmetic alone or adding $112/15$ to the reported intermediate number would not give the reconstructed result. We cannot determine what the original implementation evaluated.

As a check independent of the Abel–Plana contour, split the original lattice sum at $L=2N+1$ into a finite square, two strips, and an infinite corner. For the odd-integer lattice the Euler–Maclaurin tail operator truncated at order $p$ is

$$
E_p[f]=\frac12\int_L^\infty f(x)\,dx+\frac12 f(L)
-\sum_{r=1}^p\frac{2^{2r-1}B_{2r}}{(2r)!}f^{(2r-1)}(L).
\tag{9}
$$

Apply this in both coordinates to the spectral summand before continuing to $s=0$. The finite derivative is $-xy\log(x^2+y^2+\nu)$; the continued one-axis and two-axis integrated derivatives are $xD_L(\log D_L-1)/4$, $D_L=x^2+L^2+\nu$, and $D_C^2(3/2-\log D_C)/32$, $D_C=2L^2+\nu$. Boundary derivatives are computed through algebraic Taylor recurrences. With 60-digit working precision, the convergence is:

| $N$ | $p$ | $Z'(2,-10\mid0)$ (rounded) |
|---:|---:|---:|
| 8 | 4 | −18.208081215740860529 |
| 8 | 10 | −18.208081215375730959 |
| 16 | 10 | −18.208081215375730953 |
| 32 | 10 | −18.208081215375730953 |
| 64 | 10 | −18.208081215375730953 |

The polynomial analogue reproduces $Z(0)=581/45$. The highest-resolution estimate differs from a separately formulated prior heat-Mellin calculation (QG-033) by about $2.31\times10^{-34}$ and from the corrected double-precision Abel–Plana calculation by $1.70\times10^{-13}$. Four other $(k,\nu)$ settings cross-check the two QG-034 methods within $10^{-9}$. These agreements are empirical numerical convergence checks, not certified remainder bounds or external replication. We recommend reporting only the conservative rounded correction $-18.2080812154$ pending review.

## 4. Conditional effect on the instanton prefactor

Under exactly Eq. (5.27)'s normalization, at $\mu_0=1$ the positive-mode ratio is $2^{1567/45}e^\Upsilon\simeq375.7199074463$. Relative to the value computed with the printed $\Upsilon$,

$$
\frac{D_{\mathrm{new}}}{D_{\mathrm{printed}}}
=\exp(\Upsilon_{\mathrm{new}}+18.3118)\simeq1.1092884621.
\tag{10}
$$

Substituting directly into the symbolic first line of Eq. (5.28) gives the finite coefficient $27\,2^{1567/45}e^{\Upsilon}/(256\pi^4)\simeq0.4068070913$, instead of the rounded $0.3667$. This does not alter the $\mu_0^{-98/45}$ scale exponent or the physical negative mode. All other finite normalization factors, the conformal contour and the $S^4$ sector are held fixed and are not validated by this audit.

## 5. Reproducibility and request for review

The plain-text reproducibility supplement sent to the original authors contains the exact QG-034 numerical source listings, pinned dependency versions, and expected results. The full evidence archive preserves the pre-execution protocol, initial failed numerical attempt, repair, outputs and SHA-256 manifest. The original failure occurred when an additional control sampled a logarithmic singularity on the integration diagonal; domain splitting repaired quadrature without changing the target or checks. Twelve checks passed in the archived run; its numerical output and logs were byte-identical on same-environment replay. The archive's 19 manifest entries were reverified for this note. No new independent run or author confirmation is claimed here.

The evidence archive and supplement are not deposited by this Markdown publication. They may be requested from the author. The following SHA-256 identifiers specify the preserved files:

| File | SHA-256 |
|---|---|
| QG-034.zip | 89ad989298f50ad3025b0ab6343b37f14e8398c92ba1a4e5fc8ce54f3357cd0d |
| QG-034_Correction_Note.pdf | f3cf484c415cead954a2e355a9662c55a1f81a3ebd0eb0e25b9c6a4119dc1ee7 |
| QG-034_Reproducibility_Supplement.txt | 03a0f687cbd28facc079e04349ff2ea840abbdfa91f69e8ebcd9b07d565ca232 |

We would appreciate clarification of whether the printed polynomial omission and finite constant are known typographical or numerical errors, or whether a convention or analytic contribution has been missed. We thank the authors for their detailed original spectral analysis, which makes this reconstruction possible. This note was prepared with AI assistance; it is a candidate correction, not a peer-reviewed erratum.

## References

[1] M. S. Volkov and A. Wipf, *Black hole pair creation in de Sitter space: a complete one-loop analysis*, Nuclear Physics B **582** (2000) 313–362. [doi:10.1016/S0550-3213(00)00287-X](https://doi.org/10.1016/S0550-3213(00)00287-X); [arXiv:hep-th/0003081](https://arxiv.org/abs/hep-th/0003081). Journal version, pp. 345 and 358–360, Eqs. (5.25)–(5.28), (A.40)–(A.50).
