#!/usr/bin/env python3
"""UNITY-001 Phase 4 — exact rational, bounded dynamical-consistency checks.

Not a full GR/EFMW theory, tensor-manifold Lean proof, quantum field theory,
nonlinear PDE solver, experiment, or claim of nonzero informational coupling.
Uses sparse polynomials and Fraction; standard library only.
"""
from __future__ import annotations
import argparse
import json
import random
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
P1 = HERE.parent / "phase-1"
P2 = HERE.parent / "phase-2"
P3 = HERE.parent / "phase-3"
D = 4
ZEROEXP = (0, 0, 0, 0)
SIGN = (-1, 1, 1, 1)

def q(x):
    return Fraction(x)

class Poly:
    """Exact polynomial in (t,x,y,z), with rational coefficients."""
    def __init__(self, terms=None):
        self.terms = {}
        for k, c in (terms or {}).items():
            k = tuple(k)
            if len(k) != D or any(type(e) is not int or e < 0 for e in k):
                raise ValueError("Invalid polynomial exponents")
            c = q(c)
            if c:
                self.terms[k] = self.terms.get(k, q(0)) + c
        self.terms = {k: v for k,v in self.terms.items() if v}

    @classmethod
    def const(cls, val):
        val = q(val)
        return cls({ZEROEXP: val}) if val else cls()

    @classmethod
    def variable(cls, n):
        if type(n) is not int or n not in range(D):
            raise ValueError("Unknown coordinate")
        exp = list(ZEROEXP); exp[n] = 1
        return cls({tuple(exp): q(1)})

    def __add__(self, other):
        other = cast(other)
        out = dict(self.terms)
        for k,v in other.terms.items():
            out[k] = out.get(k,q(0)) + v
        return Poly(out)

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Poly({k: -v for k,v in self.terms.items()})

    def __sub__(self, other):
        return self + -cast(other)

    def __rsub__(self, other):
        return cast(other) - self

    def __mul__(self, other):
        other = cast(other)
        out = {}
        for a,x in self.terms.items():
            for b,y in other.terms.items():
                k = tuple(i+j for i,j in zip(a,b))
                out[k] = out.get(k,q(0)) + x*y
        return Poly(out)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        denom = cast(other)
        if len(denom.terms) != 1 or ZEROEXP not in denom.terms:
            raise ValueError("Only division by a nonzero rational constant")
        return Poly({k: v/denom.terms[ZEROEXP] for k,v in self.terms.items()})

    def __pow__(self, n):
        if type(n) is not int or not 0 <= n <= 12:
            raise ValueError("Only bounded nonnegative integral powers")
        result = Poly.const(1)
        for _ in range(n):
            result = result * self
        return result

    def diff(self, axis):
        if type(axis) is not int or axis not in range(D):
            raise ValueError("Unknown derivative axis")
        out = {}
        for k,c in self.terms.items():
            if k[axis]:
                v = list(k)
                v[axis] -= 1
                out[tuple(v)] = c * k[axis]
        return Poly(out)

    def evaluate(self, values):
        if len(values) != D:
            raise ValueError("Need four coordinate values")
        return sum((c * prod(q(values[i])**k[i] for i in range(D))
                    for k,c in self.terms.items()), q(0))

    def __eq__(self, other):
        try:
            return self.terms == cast(other).terms
        except (TypeError,ValueError):
            return False

    def __bool__(self):
        return bool(self.terms)

    def __repr__(self):
        return f"Poly({self.terms!r})"

def cast(x):
    if isinstance(x, Poly):
        return x
    if type(x) in (int, Fraction):
        return Poly.const(x)
    raise TypeError("Invalid polynomial operand")

def prod(values):
    out = q(1)
    for x in values: out *= x
    return out

def vec(*xs):
    if len(xs) != D:
        raise ValueError("Four-dimensional vector expected")
    return tuple(cast(x) for x in xs)

def field(A):
    if len(A) != D:
        raise ValueError("Four potential components required")
    a = tuple(cast(x) for x in A)
    return tuple(tuple(a[j].diff(i)-a[i].diff(j) for j in range(D)) for i in range(D))

def gauge_shift(A, chi):
    chi = cast(chi)
    if len(A) != D:
        raise ValueError("Four potential components required")
    return tuple(cast(A[i]) + chi.diff(i) for i in range(D))

def bianchi(F):
    return [F[mu][nu].diff(lam)+F[nu][lam].diff(mu)+F[lam][mu].diff(nu)
            for lam in range(D) for mu in range(D) for nu in range(D)]

def raised(F):
    return tuple(tuple(SIGN[mu]*SIGN[nu]*F[mu][nu] for nu in range(D))
                 for mu in range(D))

def maxwell_current(F):
    up = raised(F)
    return tuple(sum((up[mu][nu].diff(mu) for mu in range(D)), Poly()) for nu in range(D))

def field_square(F):
    up = raised(F)
    return sum((F[mu][nu]*up[mu][nu] for mu in range(D) for nu in range(D)), Poly())

def stress(F):
    sq=field_square(F)
    return tuple(tuple(sum((SIGN[rho]*F[mu][rho]*F[nu][rho] for rho in range(D)),Poly())
                        -(SIGN[mu]*sq/4 if mu==nu else Poly())
                        for nu in range(D)) for mu in range(D))

def stress_divergence(T):
    return tuple(sum((SIGN[mu]*T[mu][nu].diff(mu) for mu in range(D)),Poly())
                 for nu in range(D))

def lorentz_force(F,J):
    return tuple(sum((F[nu][lam]*J[lam] for lam in range(D)),Poly())
                 for nu in range(D))

def sample_poly(rng, count=5):
    out=Poly()
    for _ in range(count):
        exps=[0,0,0,0]
        for _ in range(rng.randrange(1,4)):
            exps[rng.randrange(D)]+=1
        out+=Poly({tuple(exps):q(rng.randrange(-3,4))})
    return out

def maxwell_checks(samples=12):
    rng=random.Random(20261109)
    gauge=bianchi_total=stress_total=0
    nonvacuum=0
    for _ in range(samples):
        A=tuple(sample_poly(rng,5) for _ in range(D))
        chi=sample_poly(rng,7)
        F=field(A)
        if field(gauge_shift(A,chi)) != F:
            raise AssertionError("Gauge shift changed F")
        gauge+=1
        if any(bianchi(F)):
            raise AssertionError("Abelian Bianchi closure failed")
        bianchi_total+=64
        J=maxwell_current(F)
        if any(J): nonvacuum+=1
        if stress_divergence(stress(F)) != lorentz_force(F,J):
            raise AssertionError("Maxwell stress-current off-shell identity failed")
        stress_total+=4

    t,x,_,_=tuple(Poly.variable(i) for i in range(D))
    plane=vec(0,0,(t-x)**3,0)
    F=field(plane)
    if any(maxwell_current(F)):
        raise AssertionError("Manufactured plane-wave vacuum current nonzero")
    if any(stress_divergence(stress(F))):
        raise AssertionError("Manufactured plane-wave stress not conserved")
    # Deliberately off-shell A_x=t²: J^x=-2, so stress is not conserved.
    nonvac=vec(0,t**2,0,0)
    FN=field(nonvac)
    JN=maxwell_current(FN)
    div=stress_divergence(stress(FN))
    if not any(JN) or not any(div):
        raise AssertionError("Nonvacuum negative control became vacuous")
    if div != lorentz_force(FN,JN):
        raise AssertionError("Sourceful stress-current relation incorrect")
    if nonvacuum==0:
        raise AssertionError("Random trials did not include nonvacuum fields")
    return {
        "status":"PASS_BOUNDED_POLYNOMIAL_MAXWELL_IDENTITIES",
        "random_potential_samples":samples,
        "gauge_shift_checks":gauge,
        "Bianchi_component_checks":bianchi_total,
        "off_shell_stress_divergence_checks":stress_total,
        "sourceful_random_examples":nonvacuum,
        "vacuum_plane_wave_J_zero":True,
        "vacuum_plane_wave_divT_zero":True,
        "nonvacuum_J_nonzero":True,
        "nonvacuum_divT_nonzero":True,
        "conditions":"Flat Minkowski (-+++) and polynomial 4-potentials; F=dA, no boundary or topology problem."
    }

def scalar_current_counterexample():
    t=Poly.variable(0)
    phi=t
    j=tuple(SIGN[nu]*phi*phi.diff(nu) for nu in range(D))
    div=sum((j[nu].diff(nu) for nu in range(D)),Poly())
    if div != -1:
        raise AssertionError("Neutral scalar current failed explicit nonconservation witness")
    # Any F=dA automatically obeys ∂ν∂μ F^μν=0. A source such as
    # j^ν=φ∂^νφ with div j=-1 is therefore incompatible without constraints.
    return {"status":"FAIL_UNCONSTRAINED_NEUTRAL_SCALAR_GAUGE_SOURCE",
            "phi":"t","current":"j^nu=phi*partial^nu phi","divergence":"-1",
            "necessary_condition":"div j=0 for a Maxwell-like antisymmetric field equation",
            "scope":"Counterexample to unconditional current admissibility; not a no-go theorem for all coupled or constrained matter extensions."}

def witd_manufactured_balance(variable_h=False):
    t,x,_,_=tuple(Poly.variable(i) for i in range(D))
    alpha=q(2); gamma=q(1)/3; coupling=q(3)/4
    mass2=q(2); quartic=q(1)/2
    m=1+t+t*x+t**2/2
    qfield=m+m.diff(0)/alpha
    p=qfield.diff(0)
    g=1+t+t**2
    h=1+x+(t if variable_h else 0)
    r=qfield-m
    V=mass2*qfield**2/2+quartic*qfield**4/4
    Vprime=mass2*qfield+quartic*qfield**3
    # Manufactured source deliberately makes all chosen polynomials
    # satisfy the q,p,m PDE at the selected values. Not a source-free test.
    forcing=p.diff(0)-qfield.diff(1).diff(1)+Vprime+gamma*p+g*r+coupling*(qfield-h)
    e=p**2/2+qfield.diff(1)**2/2+V+g*r**2/2+coupling*(qfield-h)**2/2
    flux=-(p*qfield.diff(1))
    lhs=e.diff(0)+flux.diff(1)
    rhs=-gamma*p**2-g*alpha*r**2+g.diff(0)*r**2/2+p*forcing
    map_work=-coupling*(qfield-h)*h.diff(0)
    residual=lhs-rhs
    if residual!=map_work:
        raise AssertionError("WITD local energy accounting mismatch")
    if variable_h:
        if not residual:
            raise AssertionError("Time-varying map has no energy transfer")
    else:
        if residual:
            raise AssertionError("Frozen-map energy balance not exact")
        omitted_modulation=lhs-(rhs-g.diff(0)*r**2/2)
        if not omitted_modulation:
            raise AssertionError("Modulation-work negative control not detected")
    if m.diff(0)!=alpha*r or qfield.diff(0)!=p:
        raise AssertionError("Manufactured field does not satisfy state/memory constraints")
    return {
        "status":"PASS_CONDITIONAL_MANUFACTURED_ENERGY_BALANCE",
        "h_time_dependent":variable_h,
        "exact_polynomial_residual_zero_with_required_work":(residual-map_work)==0,
        "energy_defect_if_h_work_omitted":bool(residual),
        "source_is_manufactured":True,
        "notes":"1+1-dimensional subcase of normalized WITD smooth balance; no physical instrument, finite-step integrator convergence or full tensor stress."
    }

def witd_tensor_obstruction():
    # μ²>0, g>0, α>0, a=1, c=0, p=0, homogeneous.
    # q=m=a -> e=V(a), I00=V(a)+β μ²a²/2, forcing β=0.
    # q=0,m=a, β=0 -> I00=0, e=g a²/2>0.
    mu2=q(2); g=q(3); a=q(1)
    beta_forced=q(0)
    first_difference_at_beta_one=mu2*a*a/2
    second_difference_at_beta_zero=g*a*a/2
    assert first_difference_at_beta_one and second_difference_at_beta_zero
    return {"status":"FAIL_GLOBAL_CONSTANT_BETA_STORAGE_IDENTIFICATION",
            "first_witness_q_equals_m":"β must be zero if μ²>0",
            "second_witness_q_zero_m_one":"e-I00="+str(second_difference_at_beta_zero)+" at β=0",
            "note":"This was already identified by WITD-002. Independent small algebraic counterexample, not a general classification of possible covariant stresses."}

def c1_scalar_stability():
    # C1 permits scalar cubic h_abc φaφbφc with positive masses and h_abc=1.
    def U(s): return q(3)*q(s)*q(s)/2+q(s)**3
    witness={str(n):str(U(-n)) for n in (2,4,8,16)}
    if not all(U(-n)<0 for n in (2,4,8,16)):
        raise AssertionError("Missing negative potential samples")
    if not all(U(-2*n)<U(-n) for n in (2,4,8)):
        raise AssertionError("Cubic unboundedness witnesses not descending")
    return {"status":"FAIL_GLOBAL_C1_POTENTIAL_BOUNDEDNESS",
            "restriction":"Three canonical scalars equal s, unit positive squared masses, h_abc=1, other couplings zero.",
            "potential":"U(s)=3s²/2+s³",
            "negative_ray_witnesses":witness,
            "analytic_reason":"Negative cubic s³ dominates positive quadratic 3s²/2 as s→-∞; permitted parameter family is not globally bounded below.",
            "scope":"A genuine allowed C1 subfamily counterexample; not instability of every restricted EFT parameter choice."}

def source_guard():
    lock=json.loads((P1/"sources.lock.json").read_text(encoding="utf8"))
    phase2=json.loads((P2/"conflicts.json").read_text(encoding="utf8"))
    phase3=json.loads((P3/"interfaces.json").read_text(encoding="utf8"))
    if lock.get("files_count")!=209 or len(lock.get("repositories",[]))!=4:
        raise AssertionError("Phase 1 provenance drift")
    if len(phase2.get("items",[]))!=8 or any(x["status"]!="UNRESOLVED" for x in phase2["items"]):
        raise AssertionError("Phase 2 unresolved conflicts were modified")
    if not any(x["id"]=="P3-REF-001" for x in phase3["interfaces"]):
        raise AssertionError("Phase 3 reference projection missing")
    refs={
        "C1_candidate":{"commit":"83f9d2ec03e055c6cd09aa6359189161ad1571f6",
                        "blob":"916e04935f50cbbf07ddcd81e7c71a02954b1c96",
                        "path":"candidate/CANDIDATE.md"},
        "WITD002":{"commit":"b02b04897743d34cdb846e9fac2518cd8faa4399",
                   "blob":"d427b2f50bd8e577f6c206e076aa4121a612c6d9",
                   "path":"research/witd-002/DERIVATION.md"}
    }
    for name, ref in refs.items():
        repo="EFMW-Lagrangian" if name=="C1_candidate" else "Information-Tensor"
        entry=next((r for r in lock["repositories"] if r["repo"]==repo),None)
        if entry is None or entry["commit"]!=ref["commit"]:
            raise AssertionError("Source repo commit mismatch "+name)
        f=next((x for x in entry["files"] if x["path"]==ref["path"]),None)
        if f is None or f["git_blob_sha"]!=ref["blob"]:
            raise AssertionError("Pinned source blob mismatch "+name)
    return {"status":"PASS_LOCKED_SOURCE_METADATA","sources":refs,
            "phase2_held_conflicts":8,"phase3_bridge_reviewed":"P3-REF-001"}

def run():
    sources=source_guard()
    maxwell=maxwell_checks()
    current=scalar_current_counterexample()
    witd=witd_manufactured_balance(False)
    mapwork=witd_manufactured_balance(True)
    tensor=witd_tensor_obstruction()
    stability=c1_scalar_stability()
    findings=[
        {"id":"P4-MAX-GAUGE","status":"PASS","scope":"F=dA invariant under A→A+dχ, 12 finite exact polynomial examples"},
        {"id":"P4-MAX-BIANCHI","status":"PASS","scope":"Abelian dF=0 via exact commuting derivatives in 12 polynomial examples"},
        {"id":"P4-MAX-STRESS","status":"PASS","scope":"Flat Maxwell ∂^μT_{μν}=F_{νλ}J^λ; if J=0, ∂T=0; examples and explicit sourceful negative control"},
        {"id":"P4-WITD-ENERGY","status":"PASS","scope":"Conditional 1+1 smooth manufactured WITD energy balance incl modulation and map work"},
        {"id":"P4-C1-UNBOUNDED","status":"FAIL","scope":"False universal global stability of all C1 potential choices; explicit allowed cubic ray to -∞"},
        {"id":"P4-C1-NEUTRAL-CURRENT","status":"FAIL","scope":"False universal conservation of arbitrary neutral-scalar current φ∂^νφ; explicit divergence -1"},
        {"id":"P4-WITD-STORAGE-TENSOR","status":"FAIL","scope":"False assertion one constant β makes displayed I00 equal WITD smooth storage for all states under μ²,g>0"},
        {"id":"P4-FULL-C1-METRIC","status":"UNRESOLVED","scope":"Coupled curved-space Einstein, gauge, scalar variations and constitutive principal symbol not independently derived"},
        {"id":"P4-HISTORICAL-EFMW-STRESS","status":"UNRESOLVED","scope":"Original EFMW 102 and 585 source equations not matched to a conserved full informational stress or physical source"},
        {"id":"P4-FULL-WITD-TENSOR","status":"UNRESOLVED","scope":"No covariant total stress, reservoir momentum, or physical calibration derived from WITD storage ledger"},
        {"id":"P4-QUANTUM-CAUSAL","status":"UNRESOLVED","scope":"Full quantum unitarity, microcausality, hyperbolicity and EFT cutoff of nonminimal RX interactions untested"},
        {"id":"P4-PHYSICAL-EVIDENCE","status":"UNRESOLVED","scope":"No external experiment or EFMW-specific signal, independent physical replication, or total Unity"}
    ]
    return {
        "schema":"unity-001-phase4-exact-bounded-dynamics-v1",
        "date":"2026-11-09","source_guard":sources,
        "maxwell":maxwell,"neutral_scalar_current":current,
        "witd_energy":witd,"witd_dynamic_h":mapwork,
        "witd_storage_tensor_obstruction":tensor,"C1_cubic_stability":stability,
        "findings":findings,"counts":dict(Counter(f["status"] for f in findings)),
        "efmw_specific_physical_pass":0,"phase4_disposition":"BOUNDED_DYNAMICAL_IDENTITY_PASS_GLOBAL_C1_AND_WITD_IDENTIFICATIONS_FAIL_FULL_PHYSICS_UNRESOLVED",
        "notes":["All PASS results are algebraic or exact rational manufactured-polynomial checks in declared submodels.",
                 "All FAIL results falsify named stronger or universal claims, not every variant of EFMW.",
                 "Source-only κ ambiguity from Phase 3 and eight Phase 2 scientific conflicts remain unresolved.",
                 "No full curved GR tensor-geometry or quantum kernel proof, prospective data, or independent physics verification."]}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out",default=str(HERE/"build"/"phase4.json"))
    args=p.parse_args()
    result=run()
    output=Path(args.out)
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"result":result["phase4_disposition"],
                      "counts":result["counts"],
                      "maxwell_stress_checks":result["maxwell"]["off_shell_stress_divergence_checks"],
                      "efmw_specific_physical_pass":result["efmw_specific_physical_pass"],
                      "manifest":str(output)},indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
