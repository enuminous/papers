#!/usr/bin/env python3
"""EFMW-C1-OBS-001: conditional predictions, not measurements or a discovery."""
from pathlib import Path
import argparse, csv, hashlib, json, math, platform, sys
from datetime import datetime, timezone
import numpy as np
import scipy
from scipy.linalg import expm
from scipy.integrate import quad
import sympy as sp

ROOT=Path(__file__).resolve().parent
H_SI=6.62607015e-34
C_SI=299792458.
EV_J=1.602176634e-19
MU0_APPROX=4*math.pi*1e-7  # Stated approximation, not a claim of exact post-2019 SI.
HBARC_EV_M=H_SI*C_SI/(2*math.pi*EV_J)
TESLA_EV2=math.sqrt(HBARC_EV_M**3/(MU0_APPROX*EV_J))

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def verify_scope():
    record=json.loads((ROOT/'SCOPE_LOCK.json').read_text())
    for name,wanted in record['files'].items():
        assert sha(ROOT/name)==wanted,('Scope changed',name)
    blobs={'CANDIDATE.md':'916e04935f50cbbf07ddcd81e7c71a02954b1c96',
           'conventions.json':'a4d84fa9c70ea53f298675de74c88a505ea0af87',
           'DERIVATION.md':'dcd375e8c80a661f2e019bbcbb494e16150b3c65'}
    for name,wanted in blobs.items():
        data=(ROOT/'sources'/name).read_bytes()
        actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert actual==wanted,(name,actual,wanted)
    return record

def sinc(x):return float(np.sinc(x/math.pi))

def forward_probability(a,d):
    """Exact within the two-mode forward model: a=g B L/2; d=m^2 L/(4 omega)."""
    radius=math.hypot(a,d)
    return 0. if radius==0 else (a/radius)**2*math.sin(radius)**2

def weak_probability(a,d):return a*a*sinc(d)**2

def parameters(g_GeV_inverse,m_eV,B_T,L_m,wavelength_nm):
    if m_eV<0 or L_m<0 or wavelength_nm<=0:raise ValueError('Invalid domain')
    omega=H_SI*C_SI/(wavelength_nm*1e-9*EV_J)
    if m_eV>=omega:raise ValueError('Relativistic propagating formula cannot be used at/above threshold')
    g=g_GeV_inverse*1e-9
    B=B_T*TESLA_EV2
    L=L_m/HBARC_EV_M
    q=m_eV*m_eV/(2*omega)
    q_exact=m_eV*m_eV/(omega+math.sqrt(omega*omega-m_eV*m_eV))
    a=g*B*L/2
    d=q*L/2
    return {'omega_eV':omega,'g_eV_inverse':g,'B_eV2':B,'L_eV_inverse':L,
            'q_rel_eV':q,'q_kinematic_eV':q_exact,'mixing_a':a,'phase_d':d,
            'm_over_omega':m_eV/omega,'gB_over_omega':abs(g*B)/omega,
            'qL_error':abs(q_exact-q)*L}

def prediction(g_GeV_inverse,m_eV,B1_T,B2_T,L1_m,L2_m,wavelength_nm,
               power_W=1.,seconds=1.,efficiency=1.,theta=math.pi/2):
    if not 0<=efficiency<=1 or seconds<0 or power_W<0:raise ValueError('Invalid exposure')
    p1=parameters(g_GeV_inverse,m_eV,B1_T,L1_m,wavelength_nm)
    p2=parameters(g_GeV_inverse,m_eV,B2_T,L2_m,wavelength_nm)
    for p in (p1,p2):
        if p['m_over_omega']>.01 or p['gB_over_omega']>.01 or p['qL_error']>.01:
            raise ValueError('Outside declared relativistic/phase-accuracy domain')
    photon_number=power_W*seconds/(p1['omega_eV']*EV_J)
    prob1=weak_probability(p1['mixing_a'],p1['phase_d'])
    prob2=weak_probability(p2['mixing_a'],p2['phase_d'])
    regenerated=math.sin(theta)**2*prob1*prob2
    return {'single_conversion_1':prob1,'single_conversion_2':prob2,
            'regeneration_probability':regenerated,'incident_photons':photon_number,
            'expected_signal_counts':efficiency*photon_number*regenerated,
            'detector_efficiency':efficiency,'input_angle_rad':theta,
            'kinematics_1':p1,'kinematics_2':p2}

def symbolic_checks():
    t,z=sp.symbols('t z',real=True)
    g,m,c,X,s0=sp.symbols('g m c X s0',real=True)
    A=sp.Function('A')(t,z);s=sp.Function('s')(t,z);B=sp.Function('B')(z)
    lag=(sp.diff(A,t)**2-sp.diff(A,z)**2+sp.diff(s,t)**2-sp.diff(s,z)**2
         -m*m*s*s)/2+g*B*s*sp.diff(A,z)
    def el(field):
        return sp.simplify(sp.diff(sp.diff(lag,sp.diff(field,t)),t)+
                           sp.diff(sp.diff(lag,sp.diff(field,z)),z)-sp.diff(lag,field))
    el_A=el(A);el_s=el(s)
    expected_A=sp.diff(A,t,2)-sp.diff(A,z,2)+g*sp.diff(B*s,z)
    expected_s=sp.diff(s,t,2)-sp.diff(s,z,2)+m*m*s-g*B*sp.diff(A,z)
    assert sp.simplify(el_A-expected_A)==0
    assert sp.simplify(el_s-expected_s)==0
    scalar_source=sp.diff(m*m*s0*s0/2+c*X*s0,s0)
    assert sp.simplify(scalar_source.subs(c,g/4)-(m*m*s0+g*X/4))==0
    L_C1=-X/4-c*X*s0
    L_known=-(1+g*s0)*X/4
    assert sp.simplify(L_C1.subs(c,g/4)-L_known)==0
    gauge_factor=-4*sp.diff(L_C1,X)
    assert sp.simplify(gauge_factor.subs(c,g/4)-(1+g*s0))==0
    w,k,B0,aa,ss=sp.symbols('w k B0 aa ss',real=True)
    phase=sp.exp(sp.I*(k*z-w*t))
    sub={A:aa*phase,s:ss*phase,B:B0}
    plane_A=sp.simplify(-el_A.subs(sub).doit()/phase)
    plane_s=sp.simplify(-el_s.subs(sub).doit()/phase)
    matrix=sp.Matrix([[sp.diff(plane_A,aa),sp.diff(plane_A,ss)],
                      [sp.diff(plane_s,aa),sp.diff(plane_s,ss)]])
    target_det=(w*w-k*k)*(w*w-k*k-m*m)-g*g*B0*B0*k*k
    assert sp.simplify(matrix.det()-target_det)==0
    a,q=sp.symbols('a q',real=True)
    H=sp.Matrix([[0,sp.I*a],[-sp.I*a,q]])
    R=sp.diag(1,sp.I)
    Hr=sp.simplify(R*H*R.inv())
    assert Hr==sp.Matrix([[0,a],[a,q]]) and Hr==Hr.conjugate().T
    sigma_bg=-g*B0**2/(2*m**2)
    assert sp.simplify(m*m*sigma_bg+g*B0**2/2)==0
    # Full field energy is positive only on the stated positive-kinetic branch.
    assert sp.simplify((1+g*s0).subs(s0,-2/g))==-1
    dimension_terms={'F_squared':4,'scalar_kinetic':4,'mass_term':2+2,
                     'scalar_photon':-1+1+4}
    assert set(dimension_terms.values())=={4}
    return {'source_copies_verified':True,'C1_to_known_scalar_interaction_identity':True,
        'g_equals_4_c_MW':True,'scalar_source':str(scalar_source.subs(c,g/4)),
        'gauge_kinetic_factor':str(gauge_factor.subs(c,g/4)),
        'EL_A_nonuniform_B':str(el_A),'EL_scalar':str(el_s),
        'wave_matrix':str(matrix),'wave_determinant':str(sp.factor(matrix.det())),
        'forward_H_after_rephasing':str(Hr),'magnetic_scalar_background':str(sigma_bg),
        'mass_dimensions':dimension_terms,
        'negative_kinetic_counterexample':'sigma=-2/g gives 1+g sigma=-1; no global stability claim',
        'proof_kind':'symbolic identities plus written derivation; not Lean-checked'}

def numerical_checks(scope):
    grid=scope['numerical_grid'];records=[]
    max_expm=max_unitarity=max_integral=max_weak_error=0.
    for a in grid['mixing_angle_parameter']:
        for d in grid['phase_mismatch']:
            H=np.array([[0,a],[a,2*d]],dtype=complex)
            U=expm(-1j*H)
            p=float(abs(U[1,0])**2)
            formula=forward_probability(a,d)
            error=abs(p-formula);unit=float(np.max(np.abs(U.conj().T@U-np.eye(2))))
            max_expm=max(max_expm,error);max_unitarity=max(max_unitarity,unit)
            integral=a*complex(quad(lambda x:math.cos(2*d*x),0,1,epsabs=1e-12)[0],
                               quad(lambda x:math.sin(2*d*x),0,1,epsabs=1e-12)[0])
            weak=weak_probability(a,d)
            ie=abs(abs(integral)**2-weak);max_integral=max(max_integral,ie)
            assert 0<=formula<=1
            assert error<2e-13 and unit<2e-13 and ie<2e-13
            if a<=1e-6:
                we=abs(formula-weak);max_weak_error=max(max_weak_error,we)
                assert we<1e-22
            records.append({'a':a,'d':d,'matrix_exponential_probability':p,
                'closed_probability':formula,'weak_probability':weak,'absolute_error':error,
                'unitarity_error':unit,'amplitude_integral_error':ie})
    # Independently check magnetic conversion via SI energy density and direct SI coherent formula.
    nat_energy=TESLA_EV2**2/2
    si_energy=(1/(2*MU0_APPROX))*(HBARC_EV_M**3/EV_J)
    assert math.isclose(nat_energy,si_energy,rel_tol=1e-14)
    ex=scope['example']
    pars=parameters(ex['g_GeV_inverse'],ex['mass_eV'],ex['B_T'],ex['L_m'],ex['wavelength_nm'])
    direct_si=(ex['g_GeV_inverse']*1e-9)**2*ex['B_T']**2*ex['L_m']**2*HBARC_EV_M/(4*MU0_APPROX*EV_J)
    assert math.isclose(direct_si,pars['mixing_a']**2,rel_tol=1e-14)
    def n(g=ex['g_GeV_inverse'],B1=ex['B_T'],B2=ex['B_T'],theta=math.pi/2):
        return prediction(g,ex['mass_eV'],B1,B2,ex['L_m'],ex['L_m'],
            ex['wavelength_nm'],power_W=ex['power_W'],seconds=3600,theta=theta)['expected_signal_counts']
    baseline=n()
    ratios={'coupling_doubled':n(g=2*ex['g_GeV_inverse'])/baseline,
            'both_fields_halved':n(B1=ex['B_T']/2,B2=ex['B_T']/2)/baseline,
            'production_field_halved':n(B1=ex['B_T']/2)/baseline,
            'polarization_45_degrees':n(theta=math.pi/4)/baseline,
            'coupling_sign_reversed':n(g=-ex['g_GeV_inverse'])/baseline}
    for key,wanted in {'coupling_doubled':16,'both_fields_halved':1/16,
                      'production_field_halved':.25,'polarization_45_degrees':.5,
                      'coupling_sign_reversed':1}.items():
        assert math.isclose(ratios[key],wanted,rel_tol=1e-12)
    assert n(g=0)==0 and n(B1=0)==0 and n(B2=0)==0 and n(theta=0)==0
    assert forward_probability(.1,0)==math.sin(.1)**2
    return records,{'grid_cases':len(records),'max_expm_absolute_error':max_expm,
        'max_unitarity_error':max_unitarity,'max_amplitude_integral_error':max_integral,
        'weak_limit_max_absolute_error_for_a_at_most_1e_minus_6':max_weak_error,
        'SI_energy_conversion_verified':True,'direct_SI_amplitude_verified':True,
        'scaling_ratios':ratios,'null_limits_verified':True}

def run(out_name):
    scope_lock=verify_scope();scope=json.loads((ROOT/'scope.json').read_text())
    out=ROOT/out_name;out.mkdir(exist_ok=False)
    started=datetime.now(timezone.utc).isoformat()
    symbolic=symbolic_checks()
    rows,checks=numerical_checks(scope)
    (out/'symbolic_checks.json').write_text(json.dumps(symbolic,indent=2)+'\n')
    (out/'numerical_checks.json').write_text(json.dumps(checks,indent=2)+'\n')
    with (out/'verification_grid.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
    ex=scope['example']
    pred=prediction(ex['g_GeV_inverse'],ex['mass_eV'],ex['B_T'],ex['B_T'],
        ex['L_m'],ex['L_m'],ex['wavelength_nm'],power_W=ex['power_W'],
        seconds=ex['run_hours']*3600,efficiency=ex['efficiency'])
    par=pred['kinematics_1']
    pred.update(status='Conditional calculation with a chosen coupling, not observed data',
        input=ex,tesla_in_eV_squared=TESLA_EV2,hbarc_eV_m=HBARC_EV_M,
        homogeneous_background_g_sigma=-par['g_eV_inverse']**2*par['B_eV2']**2/(2*ex['mass_eV']**2),
        first_coherence_zero_mass_eV=math.sqrt(4*math.pi*par['omega_eV']/par['L_eV_inverse']),
        ideal_hours_for_mean_three_counts=3/pred['expected_signal_counts'],
        ideal_95_upper_g_if_zero_counts_one_hour=ex['g_GeV_inverse']*
             (-math.log(.05)/pred['expected_signal_counts'])**.25,
        caveat='Ideal efficiency and zero-background count example; not OSQAR detector performance or its likelihood.')
    (out/'example.json').write_text(json.dumps(pred,indent=2)+'\n')
    scan=[]
    for mass in np.geomspace(scope['scan']['mass_min_eV'],scope['scan']['mass_max_eV'],scope['scan']['points']):
        p=prediction(scope['scan']['g_GeV_inverse'],float(mass),ex['B_T'],ex['B_T'],
            ex['L_m'],ex['L_m'],ex['wavelength_nm'],power_W=ex['power_W'],seconds=3600)
        scan.append({'mass_eV':float(mass),'single_conversion_probability':p['single_conversion_1'],
            'regeneration_probability':p['regeneration_probability'],
            'ideal_signal_counts_per_hour':p['expected_signal_counts'],
            'qL_relativistic_error':p['kinematics_1']['qL_error'],
            'm_over_omega':p['kinematics_1']['m_over_omega']})
    with (out/'mass_scan.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=scan[0]);writer.writeheader();writer.writerows(scan)
    # Re-express the published single-scalar bound, without reanalyzing experimental data.
    translation={'source':'Ballou et al., Phys. Rev. D 92, 092002 (2015), Eq. 2 and conclusion',
        'source_url':'https://doi.org/10.1103/PhysRevD.92.092002',
        'published_scalar_g_GeV_inverse':3.2e-8,'mass_domain_eV_upper':2e-4,
        'confidence_label':'95% as reported by authors; Bayesian posterior construction',
        'C1_c_MW_GeV_inverse':3.2e-8/4,
        'assumptions':'One scalar, matching mass and coupling convention, ordinary EM identification, no screening or additional interactions, weak-background normalization',
        'not_claimed':['new data analysis','current strongest limit','global exclusion of EFMW','discovery']}
    (out/'existing_bound_translation.json').write_text(json.dumps(translation,indent=2)+'\n')
    verify_scope()
    provenance={'started_utc':started,'finished_utc':datetime.now(timezone.utc).isoformat(),
        'scope_lock_sha256':sha(ROOT/'SCOPE_LOCK.json'),'calculation_sha256':sha(ROOT/'calculate.py'),
        'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,
        'physical_measurements':False,'independent_replication':False,
        'results_sha256':{p.name:sha(p) for p in sorted(out.iterdir()) if p.is_file()}}
    (out/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    print(json.dumps({'checks':checks,'example':pred,'published_bound_translation':translation},indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='results')
    args=ap.parse_args();run(args.out)

