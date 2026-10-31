#!/usr/bin/env python3
"""Independent arithmetic checks of Nielsen, Preprints 202604.0315, v5.

Reviewed source: https://www.preprints.org/manuscript/202604.0315/v5
Version posted 2026-07-17; review performed 2026-10-31.
Run: python3 Hopf-v5-Numerical-Review.py
Standard library only. No fitting, experimental mass inputs, or optimization.

These checks evaluate the PRINTED formulas and numbers, not an unpublished
implementation. Discrepancies may indicate transcription errors or omitted
corrections. They are not evidence about the author's intent. This is not an
independent derivation of the proposed physics.

Formula inputs: eqs. 66-69, 78, 82, 85-90 and Theorem 48. Boson n=1,2,3
follows the stated unknot/Hopf-link/trefoil assignments for W/Z/H.
Zeta(3) below is given to double-precision accuracy. The printed VEV and D(n)
values limit physical precision; extra output digits only aid reproducibility.

Comparison constant: CODATA 2022, https://physics.nist.gov/cuu/pdf/all.pdf
Inverse alpha = 137.035999177 with standard uncertainty 0.000000021.
The ratios to uncertainty assume the geometric formula is exact and identifies
the same low-energy alpha. They are NOT a global statistical model comparison.
"""

import json
import math


def evaluate():
    pi = math.pi
    zeta3 = 1.2020569031595942854
    v = 246220.0  # MeV, as printed
    vol_s2 = 4*pi
    vol_s4 = 8*pi**2/3
    vol_s9 = pi**5/12
    alpha = 2*vol_s2/(vol_s4**2*pi)*(vol_s9/160)**0.25
    kappa = math.exp(zeta3/(24*pi**2))/(4*pi**2)
    helicity = 6*math.sqrt(2)*math.exp(zeta3/(24*pi**2))
    scale = math.sqrt(2*pi)*v*kappa**6
    sigma3 = zeta3/(4*pi**2)
    D = [1.203011392, 4.806545406, 10.818228646]
    lepton_torsions = [1, 1, math.sqrt(3)]
    leptons = [scale*(n+1)*math.exp(helicity*n-D[n-1]+n*alpha/6
               +sigma3*math.log(lepton_torsions[n-1])) for n in (1,2,3)]
    r = 8.0
    rf = r+math.sqrt(3)*alpha/(2*pi)
    boson_scale = v*math.sqrt(2/r)*math.sin(pi/r)*math.exp(-2*alpha)
    T = [math.sqrt(3)/2*math.exp(-alpha*math.sqrt(2)/pi+math.sqrt(3)*alpha/(2*pi)),
         math.sin(4*pi/rf)/(4*math.sin(pi/rf)),
         2/3*math.exp(-3*alpha*math.sqrt(2)/pi+9*math.sqrt(3)*alpha/(2*pi))]
    bosons = [boson_scale*(n+1)*math.exp(n*alpha/6)*T[n-1] for n in (1,2,3)]
    # From the printed series: zeta_B(s)=zeta_R(s-2)-zeta_R(s).
    actual_logdet = sigma3-math.log(2*pi)/2
    return {
        'inverse_alpha_from_volume_formula': 1/alpha,
        'difference_over_paper_quoted_uncertainty': (1/alpha-137.0359991)/2e-7,
        'difference_over_CODATA2022_standard_uncertainty': (1/alpha-137.035999177)/2.1e-8,
        'kappa_eq67': kappa,
        'a_eq69': helicity,
        'Lambda_Hopf_MeV': scale,
        'lepton_masses_MeV_e_mu_tau': leptons,
        'printed_lepton_table_MeV': [0.510999, 105.658, 1776.86],
        'boson_masses_MeV_W_Z_H': bosons,
        'printed_boson_table_MeV': [80369.5, 91187.8, 125225],
        'minus_zeta_B_prime_0_from_printed_series': actual_logdet,
        'minus_zeta_B_prime_0_claimed_in_section_4_14': sigma3,
        'missing_constant_half_log_2pi': math.log(2*pi)/2,
    }


if __name__ == '__main__':
    print(json.dumps(evaluate(), indent=2))
