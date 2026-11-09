#!/usr/bin/env python3
"""UNITY-001 Phase 3: bounded source-frozen correspondence and obstruction audit.

Scope:
- exact rational formal-polynomial *action-density* projection with explicit
  removed fields/couplings; this is not an off-shell full Standard Model map;
- exact rational 4D Maxwell contractions and metric-direction identities;
- source-only component-array absorption under unrestricted ordinary matter.

This program does not prove field/PDE solutions, gauge covariance, quantum
gravity, EFMW physical uniqueness or empirical predictions. No external deps.
"""
from __future__ import annotations
import argparse
import csv
import json
import random
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
P1 = HERE.parent / "phase-1"
P2 = HERE.parent / "phase-2"

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def provenance():
    lock = load_json(P1 / "sources.lock.json")
    conflicts = load_json(P2 / "conflicts.json")
    if lock["files_count"] != 209 or len(lock["repositories"]) != 4:
        raise ValueError("Phase 1 source-lock contract changed")
    if len(conflicts["items"]) != 8 or any(c["status"] != "UNRESOLVED" for c in conflicts["items"]):
        raise ValueError("Phase 2 conflict ledger changed or was silently promoted")
    with (P1 / "source-equations.csv").open(encoding="utf-8", newline="") as f:
        records = list(csv.DictReader(f))
    if len(records) != 717:
        raise ValueError("Phase 1 source ledger count changed")
    ids = {x["record_id"]: x for x in records}
    if len(ids) != len(records):
        raise ValueError("Duplicate Phase 1 source record")
    needs = {
        "E002-Geometry": ("285b95551ca11c487eb6c0c13f8dde86b702df71", "232d48f36da46dc8c0e51096a1b56c56a5c4706f", "def totalSource"),
        "E021-EFMW_Lagrangian": ("83f9d2ec03e055c6cd09aa6359189161ad1571f6", "916e04935f50cbbf07ddcd81e7c71a02954b1c96", "S_{C1}"),
        "E022-EFMW_Lagrangian": ("83f9d2ec03e055c6cd09aa6359189161ad1571f6", "916e04935f50cbbf07ddcd81e7c71a02954b1c96", "g_{ij}Q_iQ_j"),
        "E025-EFMW_Lagrangian": ("83f9d2ec03e055c6cd09aa6359189161ad1571f6", "916e04935f50cbbf07ddcd81e7c71a02954b1c96", "M_{\\rm Pl}^2"),
        "E027-Standard_Model_Reduction": ("aa569b13a594735774c7b643d44aebff4d5ad17c", "c88257811c598708ac68cc77cd6b402d036a0671", "mathcal L_{\\rm SM}"),
    }
    for ident, (commit, blob, substring) in needs.items():
        r = ids[ident]
        if r["original_commit"] != commit or r["original_blob_sha"] != blob or substring not in r["original_statement"]:
            raise ValueError("Original source record pin or formula anchor changed: " + ident)
    return {"ledger_rows": len(records), "phase2_conflicts": len(conflicts["items"]),
            "source_ids": sorted(needs), "source_pins_matched": len(needs),
            "source_sha_scope": "Git commit/blob and original statement anchor; not independent field-equation derivation"}

# Formal commutative polynomial ring over rationals in named independent symbols.
# Monomials are sorted tuples of variable names. Zero is the empty dict.
def num(x):
    q = Q(x)
    return {(): q} if q else {}

def var(name):
    if not isinstance(name, str) or not name or not name.replace("_","").isalnum():
        raise ValueError("Invalid polynomial symbol")
    return {(name,): Q(1)}

def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, Q(0)) + v
        if out[k] == 0:
            del out[k]
    return out

def neg(a):
    return {m:-v for m,v in a.items()}

def sub(a, b):
    return add(a, neg(b))

def mul(a, b):
    out = {}
    for m, x in a.items():
        for n, y in b.items():
            key = tuple(sorted(m+n))
            out[key] = out.get(key, Q(0)) + x*y
            if out[key] == 0:
                del out[key]
    return out

def prod(*args):
    value=num(1)
    for arg in args:
        value=mul(value,arg)
    return value

def drop_zero(p, names):
    removed = set(names)
    return {m:c for m,c in p.items() if all(x not in removed for x in m)}

def value(p, assignments):
    out=Q(0)
    for m,c in p.items():
        term=c
        for name in m:
            if name not in assignments:
                raise ValueError("Unassigned symbol: "+name)
            term*=Q(assignments[name])
        out+=term
    return out

def as_terms(p):
    return [{"monomial":list(m),"numerator":c.numerator,"denominator":c.denominator}
            for m,c in sorted(p.items())]

def action_correspondence():
    R,Lambda,MP2,X,Y,K,gEM,gES,gMS,hEMS,lam,v=map(
        var, ("R","Lambda","MP2","X","Y","K","gEM","gES","gMS","hEMS","lam","v"))
    gravity=sub(prod(num(Q(1,2)),MP2,R),prod(MP2,Lambda))
    c1_core=sub(sub(sub(gravity,prod(num(Q(1,4)),X)),prod(num(Q(1,4)),Y)),prod(num(Q(1,2)),K))
    # At scalar=0 the C1 potential still permits g_EM R X, g_ES R Y,
    # g_MS X Y and h_EMS R X Y (the E/M/S triples).
    u0=add(add(prod(gEM,R,X),prod(gES,R,Y)),
           add(prod(gMS,X,Y),prod(hEMS,R,X,Y)))
    c1_scalar_zero=sub(c1_core,u0)
    # Project B=0 so Y=0, and all eight scalar kinetic terms are zero.
    restricted=drop_zero(c1_scalar_zero,("Y","K"))
    em_reference=sub(gravity,prod(num(Q(1,4)),X))
    if sub(restricted, em_reference) != neg(prod(gEM,R,X)):
        raise AssertionError("C1 restricted polynomial differs from expected RX remainder")
    em_zero=drop_zero(restricted,("gEM",))
    if em_zero != em_reference:
        raise AssertionError("C1 Einstein-Maxwell projection failed")
    # Fixed-background SM SU3=SU2=H=fermions=0 retains Higgs V(0).
    V0=prod(num(Q(1,4)),lam,v,v,v,v)
    sm_hypercharge=sub(neg(prod(num(Q(1,4)),X)),V0)
    if add(sm_hypercharge,V0) != neg(prod(num(Q(1,4)),X)):
        raise AssertionError("SM gauge projection fails even after vacuum offset")
    nonzero_rx=value(sub(restricted,em_reference),{"gEM":Q(1,7),"R":Q(3),"X":Q(4)})
    if nonzero_rx != Q(-12,7):
        raise AssertionError("Required nonminimal counterexample not found")
    sm_offset=value(sub(sm_hypercharge,neg(prod(num(Q(1,4)),X))),
                    {"lam":2,"v":2})
    if sm_offset != Q(-8):
        raise AssertionError("SM Higgs vacuum offset counterexample missing")
    # In a proposed (-+++) gravity+SM coupling, constant V0 shifts Lambda:
    # MP2/2 R - MP2 Lambda - X/4 - V0 = MP2/2 R - MP2 (Lambda+V0/MP2) -X/4
    # no implicit positive/signature translation of the fixed-background GR action.
    return {
        "status":"PASS_RESTRICTED_ACTION_DENSITY_IDENTITY",
        "C1_projection":"C1 phi=0, B=0, all pair/triple couplings including gEM=0 -> EH + one Maxwell U(1)",
        "identity":"L_C1|phi=B=couplings=0 = (MP2/2)R - MP2 Lambda - X/4",
        "nonminimal_remainder":"For phi=B=0 but gEM free, L_C1 - L_EM = -gEM*R*X",
        "nonminimal_counterexample":str(nonzero_rx),
        "sm_fixed_background_projection":"SM|SU3=SU2=H=fermions=0 = -X/4 - lam*v^4/4",
        "sm_vacuum_counterexample":str(sm_offset),
        "sm_same_gauge_term_after_signature_flip":True,
        "limitations":[
            "Action projection is a selected, coupling-restricted classical sector; it is not a full Standard Model or unified field equation proof.",
            "SM Higgs H=0 is a stationary but generally unstable configuration, not the observed electroweak vacuum.",
            "When coupling the SM to gravity, its constant Higgs V(0) cannot be ignored; it contributes to effective cosmological constant.",
            "No C1-to-original EFMW stress, memory or physical observable map established.",
            "Original C1 has no full Standard Model matter action; the SM comparison is only the Abelian gauge kinetic expression."
        ],
        "polynomial_c1_restricted_terms":as_terms(restricted),
        "polynomial_einstein_maxwell_terms":as_terms(em_reference)
    }

def fraction_matrix(matrix):
    if not isinstance(matrix,(tuple,list)) or len(matrix)!=4:
        raise ValueError("Expected 4-by-4 matrix")
    out=tuple(tuple(Q(v) for v in row) for row in matrix)
    if any(len(row)!=4 for row in out):
        raise ValueError("Expected 4-by-4 matrix")
    return out

def valid_field(F):
    F=fraction_matrix(F)
    if any(F[i][j]!=-F[j][i] for i in range(4) for j in range(4)):
        raise ValueError("Field strength is not antisymmetric")
    return F

def valid_contravariant_metric(g):
    g=fraction_matrix(g)
    if any(g[i][j]!=g[j][i] for i in range(4) for j in range(4)):
        raise ValueError("Inverse metric is not symmetric")
    return g

def raised(F, g):
    F=valid_field(F);g=valid_contravariant_metric(g)
    return tuple(tuple(sum((g[i][a]*g[j][b]*F[a][b]
                            for a in range(4) for b in range(4)), Q(0))
                        for j in range(4)) for i in range(4))

def f_squared(F, g):
    F=valid_field(F);upper=raised(F,g)
    return sum((F[i][j]*upper[i][j] for i in range(4) for j in range(4)),Q(0))

def k_tensor(F,g):
    F=valid_field(F);g=valid_contravariant_metric(g)
    return tuple(tuple(sum((F[i][a]*g[a][b]*F[j][b]
                             for a in range(4) for b in range(4)),Q(0))
                       for j in range(4)) for i in range(4))

def perturb(g, a,b,h):
    q=[list(row) for row in valid_contravariant_metric(g)]
    q[a][b]+=h
    if a!=b: q[b][a]+=h
    return tuple(tuple(row) for row in q)

def directional_derivative_x(F,g,a,b):
    h=Q(1,3)
    return (f_squared(F,perturb(g,a,b,h))-
            f_squared(F,perturb(g,a,b,-h)))/(2*h)

def maxwell_audit(trials=24):
    rng=random.Random(20261109)
    g=tuple(tuple(Q((-1,1,2,3)[i]) if i==j else Q(0)
                  for j in range(4)) for i in range(4))
    gsign=tuple(tuple(-v for v in row) for row in g)
    tested=0
    samples=[]
    for z in range(trials):
        F=[[Q(0)]*4 for _ in range(4)]
        for a in range(4):
            for b in range(a+1,4):
                v=Q(rng.randint(-5,5),rng.randint(1,5))
                F[a][b],F[b][a]=v,-v
        F=valid_field(F)
        X=f_squared(F,g)
        if f_squared(F,gsign)!=X:
            raise AssertionError("Maxwell X failed metric signature sign-flip invariant")
        # For symmetric inverse-metric variations: ∂X/∂g^{aa}=2K_aa;
        # off-diagonal perturbation changes both g^{ab} and g^{ba}: derivative=4K_ab.
        K=k_tensor(F,g)
        for a in range(4):
            for b in range(a,4):
                actual=directional_derivative_x(F,g,a,b)
                expected=(Q(2) if a==b else Q(4))*K[a][b]
                if actual!=expected:
                    raise AssertionError(f"metric kinetic derivative mismatch {a,b}: {actual} != {expected}")
                tested+=1
        # Polarization of Maxwell L=-X/4: dL[F;dF]=-1/2 * F^ab dF_ab.
        H=[[Q(0)]*4 for _ in range(4)]
        for a in range(4):
            for b in range(a+1,4):
                u=Q(rng.randint(-3,3))
                H[a][b],H[b][a]=u,-u
        def combine(t):
            return tuple(tuple(F[a][b]+t*H[a][b] for b in range(4)) for a in range(4))
        h=Q(1,5)
        observed=(-(f_squared(combine(h),g))/4
                  +f_squared(combine(-h),g)/4)/(2*h)
        Fu=raised(F,g)
        predicted=-Q(1,2)*sum((Fu[a][b]*H[a][b] for a in range(4) for b in range(4)),Q(0))
        if observed!=predicted:
            raise AssertionError("Maxwell field variation polarization mismatch")
        if z<3:
            samples.append({"trial":z,"F2":str(X),"polarization":str(observed)})
    return {"status":"PASS_EXACT_RATIONAL_EXAMPLES_AND_ANALYTIC_POLARIZATION",
            "trials":trials,"metric_direction_checks":tested,
            "field_variation_checks":trials,"metric_signature_flip_checks":trials,
            "background_inverse_metric":"diag(-1,1,2,3); opposite +--- = -g",
            "method":"Fraction arithmetic on antisymmetric 4x4 field matrices; analytic formulas separately derived in report",
            "examples":samples,
            "limitations":["Exact finite examples are not a theorem of arbitrary metrics; algebraic proof is written separately.",
                           "Metric kinetic variation is not by itself full Hilbert stress tensor variation or Einstein-Maxwell PDE existence.",
                           "Signature flip was applied to the Maxwell kinetic term only, not to the full Einstein-Hilbert action."]}

def total_source(T,I,kappa):
    T=fraction_matrix(T);I=fraction_matrix(I);kappa=Q(kappa)
    return tuple(tuple(T[a][b]+kappa*I[a][b] for b in range(4)) for a in range(4))

def source_identifiability(trials=24):
    rng=random.Random(404)
    identical=0; distinct_sources=0; independent_channel=0;examples=[]
    for it in range(trials):
        T=tuple(tuple(Q(rng.randint(-4,4)) for b in range(4)) for a in range(4))
        I=tuple(tuple(Q(rng.randint(-4,4)) for b in range(4)) for a in range(4))
        J=tuple(tuple(Q(rng.randint(-4,4)) for b in range(4)) for a in range(4))
        kappa=Q(3,5)
        Tprime=total_source(T,J,kappa)
        Iprime=tuple(tuple(I[a][b]-J[a][b] for b in range(4)) for a in range(4))
        s=total_source(T,I,kappa)
        if s!=total_source(Tprime,Iprime,kappa):
            raise AssertionError("affine split source identity failed")
        # kappa=0 representation when ordinary T is unrestricted
        if s!=total_source(s,[[0]*4 for _ in range(4)],0):
            raise AssertionError("source absorption failed")
        identical+=1
        # A total-source observer sees only s. Independently measuring T adds
        # different information and can discriminate, so no physical no-go follows.
        if any(I[a][b] for a in range(4) for b in range(4)):
            if total_source(T,I,kappa)!=total_source(T,I,0):
                distinct_sources+=1
            if (T,s)!=(s,s):
                independent_channel+=1
        if it<2:
            examples.append({"trial":it,"total_00":str(s[0][0]),
                             "ordinary_00":str(T[0][0]),"info_00":str(I[0][0]),
                             "reallocated_ordinary_00":str(Tprime[0][0])})
    if distinct_sources!=trials or independent_channel!=trials:
        raise AssertionError("Independent ordinary-sector counter-control did not discriminate")
    return {"status":"PASS_CONDITIONAL_COMPONENT_LEVEL_NONIDENTIFIABILITY",
            "affine_split_exact_trials":identical,"absorption_exact_trials":identical,
            "independently_fixed_ordinary_source_detection_trials":independent_channel,
            "examples":examples,
            "theorem":"For unrestricted T and any J, S(T+κJ,I-J,κ)=S(T,I,κ). Any observable f(S) is identical for the same S.",
            "negative_control":"If independent matter information fixes T and I is nonzero, the κ=0 and κ≠0 totals need not match.",
            "source":"Geometry.lean source_absorption, affine_split_invariance, source_only_observable_blind (pinned upstream)",
            "limitations":["4x4 component arrays, not covariant tensors or Einstein-matter solutions",
                           "No theorem that κ is unidentifiable if matter dynamics or independent measurements restrict ordinary T",
                           "No physical data, likelihood or observational sensitivity modeled"]}

def run():
    pv=provenance()
    action=action_correspondence()
    maxwell=maxwell_audit()
    degeneracy=source_identifiability()
    findings=[
        {"id":"P3-REF-001","status":"PASS","scope":"C1 to Einstein-Maxwell algebraic action density after explicit field/coupling truncation; not full field dynamics"},
        {"id":"P3-REF-002","status":"PASS","scope":"Classical U(1) gauge kinetic expression matches after opposite signature translation; Higgs vacuum offset kept"},
        {"id":"P3-CEX-001","status":"FAIL","scope":"Stronger claim C1 automatically becomes Einstein-Maxwell after zeroing extra fields: fails when g_EM R X remains"},
        {"id":"P3-CEX-002","status":"FAIL","scope":"Stronger claim SM hypercharge-only projection exactly equals -X/4: fails because H=0 leaves V(0)"},
        {"id":"P3-NEG-001","status":"PASS","scope":"Conditional source-only component ambiguity (existing Geometry theorem plus independent exact test)"},
        {"id":"P3-GR-EFMW","status":"UNRESOLVED","scope":"No demonstrated map identifying original EFMW informational stress with a covariantly conserved gravitational source or a measured κ"},
        {"id":"P3-FULL-SM","status":"UNRESOLVED","scope":"No complete chiral SM matter/yukawa/quantum/gravity correspondence"},
        {"id":"P3-FULL-DYNAMICS","status":"UNRESOLVED","scope":"No independent coupled Einstein-Maxwell PDE solution, field-theory equivalence theorem or Lean replay"}
    ]
    tally=dict(Counter(x["status"] for x in findings))
    return {"schema":"unity-001-phase3-execution-v1","date":"2026-11-09",
            "title":"Bounded classical Einstein-Maxwell / Abelian gauge action projection and source-split obstruction",
            "source_provenance":pv,"action_projection":action,
            "maxwell_metric_and_variation_checks":maxwell,
            "source_identifiability":degeneracy,
            "findings":findings,"finding_counts":tally,
            "efmw_specific_physical_pass":0,
            "full_unity_status":"UNRESOLVED",
            "phase3_disposition":"BOUNDED_CLASSICAL_CORRESPONDENCE_PASS; NOVEL_EFMW_GRAVITATIONAL_BRIDGE_UNRESOLVED",
            "scientific_boundary":"PASS and FAIL apply only to named algebraic claims. No new physical interaction, measured anomaly, full SM correspondence or quantum gravity completion."}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default=str(HERE/"build"/"phase3.json"))
    ap.add_argument("--print",action="store_true")
    args=ap.parse_args()
    r=run()
    dest=Path(args.out)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(r,indent=2,ensure_ascii=False,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"disposition":r["phase3_disposition"],"findings":r["finding_counts"],
                     "maxwell_direction_checks":r["maxwell_metric_and_variation_checks"]["metric_direction_checks"],
                     "source_split_trials":r["source_identifiability"]["affine_split_exact_trials"],
                     "physical_pass":r["efmw_specific_physical_pass"],"output":str(dest)},indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
