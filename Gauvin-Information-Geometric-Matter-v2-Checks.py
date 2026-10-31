#!/usr/bin/env python3
"""Bounded independent checks of Gauvin, Preprints 202609.2275 v2.

Source: https://doi.org/10.20944/preprints202609.2275.v2
Review date: 2026-10-31. Python 3 standard library only.
Exact rational spot checks are not general symbolic proofs. Floating checks
verify selected printed formulas, not their microscopic physical derivation.
The Gaussian tail is reproduced from REPORTED aggregate residual sums in
Supplement Table S2, not from independently fitted SPARC rows. No fit is run.
Version 3 exists and is outside this review's scope.
"""

from fractions import Fraction as F
import json
import math


def evaluate():
    checks = []
    for r in [F(7, 10), F(4, 5), F(9, 10), F(99, 100)]:
        s = 5*(1-r)*(1+6*r)/(6*r*(3*r-2))
        p = (3-2*r)*(1+11*r)/(6*r*(3*r-2))
        S, P = s+p, s*p
        contact_ok = r*(3-2*r)+3*r*(2*r-1)-4*r*r == 0
        dispersion_ok = 192*P-45*S*S+40*S+100 == 0
        assert contact_ok and dispersion_ok
        checks.append({'r': str(r), 'contact_link_exact': contact_ok,
                       'dispersion_identity_exact': dispersion_ok})
        # C0=M_phi=1: factor out the common positive normalization.
        f = (1+6*r)/(1+11*r)
        D = (1-r)*(1+11*r)
        A = r*(3-2*r)
        K0 = 12*r*r*(3*r-2)/(1+11*r)/8
        for n1, n2, R2 in [(F(1),F(2),F(0)), (F(3),F(4),F(5)),
                           (F(2,3),F(1,7),F(1,20))]:
            # R2=[Re(psi1* psi2)]^2; all choices obey R2 <= n1*n2.
            Sp = 4*R2-2*n1*n2
            h = (n1*n1+r*r*n2*n2+4*r*(2*r-1)*n1*n2
                 +r*(3-2*r)*Sp)/16
            completed = (K0*(n1+n2)**2/2
                         +D*(n2-f*(n1+n2))**2/16+A*R2/4)
            assert h == completed
    n, Q0, Q1 = 3389, 1960465.195407, 20805.852268
    t = Q0-Q1
    pG = n*math.erfc(math.sqrt(t/(2*n)))
    # Invert the two-sided normal tail without subtracting p from 1.
    lo, hi = 0.0, 40.0
    for _ in range(120):
        mid = (lo+hi)/2
        if math.erfc(mid/math.sqrt(2)) > pG:
            lo = mid
        else:
            hi = mid
    for eps in [.0001, .00238539763061, .01, .1, .5]:
        b = 1-eps
        x = b*math.sqrt(eps)
        slope = -(x*x+2*eps*b*x+eps*b*b)/(2*(x*x+2*b*x+eps*b*b))
        assert abs(slope+math.sqrt(eps)/2) < 1e-14
    for nf, m0, d in [(1,0,.2), (2,.3,.01), (3,1,.4)]:
        m = m0+8*math.pi*d/nf
        source = m*m-m0*m0
        pressure = nf*((m**3-m0**3)/(12*math.pi)-m0*source/(8*math.pi))
        legendre = source*d-pressure
        formula = 8*math.pi*m0/nf*d*d+64*math.pi**2/(3*nf*nf)*d**3
        assert abs(legendre-formula) < 1e-12*max(1, abs(formula))
    return {
        'exact_rational_checks': checks,
        'quartic_completion_spotchecks': 12,
        'Gaussian_Legendre_spotchecks': 3,
        'floor_slope_spotchecks': 5,
        'p_G': pG,
        'Z_G': (lo+hi)/2,
        'p_variance': n/t,
        'alternative_standardized_RMS': math.sqrt(Q1/n),
        'a_H_m_s2': 299792458*(67.4*1000/3.085677581491367e22)/(2*math.pi),
        'floor_RMS_improvement_percent': 100*(11.4126-11.4042)/11.4126,
    }


if __name__ == '__main__':
    print(json.dumps(evaluate(), indent=2))
