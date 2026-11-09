#!/usr/bin/env python3
"""UNITY-001 Phase 5 — prospective identifiability screening, NOT a physics experiment.

Reads a previously committed source-pinned PROTOCOL.json. Uses pure Python
Fraction arithmetic and explicit Gaussian elimination for profile Fisher
information. Gaussian sigma is hypothetical. No EFMW rho_I was derived.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path
from collections import Counter

HERE=Path(__file__).resolve().parent
P1=HERE.parent/"phase-1"
P2=HERE.parent/"phase-2"
P3=HERE.parent/"phase-3"
P4=HERE.parent/"phase-4"

def get_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def parse_fraction(value):
    if isinstance(value,bool):
        raise ValueError("Booleans are not rational constants")
    return F(str(value))

def dot(a,b):
    if len(a)!=len(b):
        raise ValueError("Vector length mismatch")
    return sum((x*y for x,y in zip(a,b)),F(0))

def solve(A,b):
    """Exact full-pivot-row Gaussian solve; refuse singular nuisance Gram."""
    n=len(A)
    if n==0 or len(b)!=n or any(len(row)!=n for row in A):
        raise ValueError("Square solve only")
    mat=[[F(x) for x in row]+[F(b[i])] for i,row in enumerate(A)]
    for j in range(n):
        k=next((i for i in range(j,n) if mat[i][j]),None)
        if k is None: raise ValueError("SINGULAR_NUISANCE_BASIS")
        mat[j],mat[k]=mat[k],mat[j]
        scale=mat[j][j]
        mat[j]=[v/scale for v in mat[j]]
        for i in range(n):
            if i==j: continue
            factor=mat[i][j]
            if factor:
                mat[i]=[a-factor*z for a,z in zip(mat[i],mat[j])]
    return [row[-1] for row in mat]

def project(columns, y):
    if not columns or not y or any(len(col)!=len(y) for col in columns):
        raise ValueError("Mismatched nuisance dimensions")
    gram=[[dot(x,z) for z in columns] for x in columns]
    coeff=solve(gram,[dot(x,y) for x in columns])
    return [sum((coeff[k]*columns[k][i] for k in range(len(columns))),F(0)) for i in range(len(y))]

def residual(columns, y):
    p=project(columns,y)
    return [a-b for a,b in zip(y,p)]

def profile(columns,signal,sigma,y=None):
    if sigma<=0:raise ValueError("sigma must be positive")
    q=residual(columns,signal)
    info=dot(q,q)/(sigma*sigma)
    if info==0:
        return {"status":"UNIDENTIFIABLE","profile_fisher":"0",
                "sigma_kappa":None,"nominal_5sigma_threshold":None,
                "fit_kappa":None, "rms_signal_remaining":"0"}
    out={"status":"IDENTIFIABLE_CONDITIONAL_ON_NUISANCE_FAMILY",
         "profile_fisher":str(info),
         "sigma_kappa":(float(1/info)**0.5),
         "nominal_5sigma_threshold":5*(float(1/info)**0.5),
         "rms_signal_remaining":float(dot(q,q)/len(q))**0.5}
    if y is not None:
        yr=residual(columns,y)
        out["fit_kappa"]=str(dot(q,yr)/dot(q,q))
        out["fit_kappa_float"]=float(dot(q,yr)/dot(q,q))
    return out

def frozen_source_guard(p):
    lk=get_json(P1/"sources.lock.json")
    if lk["files_count"]!=209 or len(lk["repositories"])!=4:
        raise ValueError("Phase 1 source freeze not intact")
    by_repo={"enuminous/"+r["repo"]:r for r in lk["repositories"]}
    for key in ("geometry","c1","witd"):
        src=p["provenance"][key]
        ref=by_repo[src["repo"]]
        if ref["commit"]!=src["commit"]:
            raise ValueError("Source commit drift "+key)
        file=next((f for f in ref["files"] if f["path"]==src["path"]),None)
        if file is None or file["git_blob_sha"]!=src["blob"]:
            raise ValueError("Source file drift "+key)
    conflicts=get_json(P2/"conflicts.json")
    if len(conflicts["items"])!=8 or any(c["status"]!="UNRESOLVED" for c in conflicts["items"]):
        raise ValueError("Previously unresolved physics conflicts unexpectedly changed")
    phase3=get_json(P3/"interfaces.json")
    if not any(i["id"]=="P3-NEG-001" and i["status"]=="PASS" for i in phase3["interfaces"]):
        raise ValueError("Required source-absorption negative control missing")
    if not any(i["id"]=="P3-GR-EFMW" and i["status"]=="UNRESOLVED" for i in phase3["interfaces"]):
        raise ValueError("Physical bridge promoted without evidence")
    return {"source_repos_checked":3,"preserved_phase2_conflicts":8,"prior_source_only_no_go":"CONDITIONAL_COMPONENT_ONLY",
            "phase4_missing_curved_stress":"UNRESOLVED"}

def enclosed_mass(r,R):
    if r<=0 or R<=0:
        raise ValueError("Positive radii required")
    return (r/R)**3 if r<=R else F(1)

def templates(p):
    t=p["toy_design"]
    radii=[parse_fraction(x) for x in t["radii"]]
    R=parse_fraction(t["source_sphere_radius"])
    mass=parse_fraction(t["source_total_mass"])
    scale=parse_fraction(t["signal_rescaling"])
    if len(radii)!=8 or radii!=sorted(radii) or len(set(radii))!=8:
        raise ValueError("Frozen eight distinct ordered radii required")
    s=[scale*mass*enclosed_mass(r,R)/r**2 for r in radii]
    # Dimensionless toy only. Conventional baseline columns are 1,1/r,1/r².
    n0=[[F(1) for r in radii],[1/r for r in radii],[1/r**2 for r in radii]]
    z=[r/F(8) for r in radii]
    eps=parse_fraction(t["nuisance_epsilon"])
    n1=n0+[s[:]]
    n2=n0+[[s[i]+eps*z[i] for i in range(len(s))]]
    return radii,s,n0,n1,n2

def simulate(p,s,n0):
    t=p["toy_design"]
    sigma=parse_fraction(t["noise_sigma"])
    kappa=parse_fraction(t["fiducial_kappa"])
    beta=[parse_fraction(x) for x in t["nuisance_truth"]]
    noise=[sigma*parse_fraction(v) for v in t["deterministic_pseudo_noise_multipliers"]]
    if len(beta)!=len(n0) or len(noise)!=len(s):
        raise ValueError("Toy design mismatch")
    null=[sum((beta[k]*n0[k][i] for k in range(len(beta))),F(0))+noise[i]
          for i in range(len(s))]
    alt=[null[i]+kappa*s[i] for i in range(len(s))]
    return null,alt,kappa,sigma

def classify(p, narrow, strong, near, nullfit, altfit):
    if narrow["status"]!="IDENTIFIABLE_CONDITIONAL_ON_NUISANCE_FAMILY":
        raise AssertionError("Narrow toy signal was lost")
    if strong["status"]!="UNIDENTIFIABLE":
        raise AssertionError("Conventional co-located mass did not fully confound signal")
    if near["status"]!="IDENTIFIABLE_CONDITIONAL_ON_NUISANCE_FAMILY":
        raise AssertionError("Near-confounding scenario unexpectedly singular")
    if not near["sigma_kappa"]>100*narrow["sigma_kappa"]:
        raise AssertionError("Near-confounding sensitivity not sufficiently degraded")
    if F(altfit["fit_kappa"])-F(nullfit["fit_kappa"])!=parse_fraction(p["toy_design"]["fiducial_kappa"]):
        raise AssertionError("Deterministic pseudo-injection not recovered algebraically")
    if abs(nullfit["fit_kappa_float"])>=narrow["nominal_5sigma_threshold"]:
        raise AssertionError("Synthetic null control unexpectedly above nominal threshold")
    if abs(altfit["fit_kappa_float"])<=narrow["nominal_5sigma_threshold"]:
        raise AssertionError("Injected toy response failed preregistered threshold")
    return [
      {"id":"P5-FWD-001","status":"PASS","claim":"Spherical toy Poisson source-to-acceleration response follows the explicit conditional weak-field assumption; no EFMW rho_I derived"},
      {"id":"P5-NARROW-001","status":"PASS","claim":"Under the restricted toy baseline, exact-rational profile Fisher is positive"},
      {"id":"P5-NEAR-001","status":"PASS","claim":"Near-collinear conventional alternative inflates nominal sensitivity by >100x"},
      {"id":"P5-SYNTHETIC-001","status":"PASS","claim":"Deterministic synthetic null/injection regression returns exact injected κ shift; no stochastic data or empirical 5σ claim"},
      {"id":"P5-ROBUST-001","status":"FAIL","claim":"False universal claim that gravity-only residual uniquely identifies EFMW κ under an allowed co-located conventional matter profile; exact Fisher=0"},
      {"id":"P5-EFMW-SOURCE","status":"UNRESOLVED","claim":"Frozen EFMW sources do not supply conserved independently calibrated rho_I and a unique forward physical source map"},
      {"id":"P5-STRESS-CAUSAL","status":"UNRESOLVED","claim":"No covariant stress conservation, energy reservoir, stability, hyperbolicity and physical admissibility for I supplied"},
      {"id":"P5-MATTER-PRIOR","status":"UNRESOLVED","claim":"No independent baryonic/ordinary-source constraints exclude the exact conventional co-located alternative"},
      {"id":"P5-OBSERVABLE","status":"UNRESOLVED","claim":"No instrument response, units, dataset, error covariance, feasibility, genuine power or sample-size decision"},
      {"id":"P5-DATA-CUSTODY","status":"UNRESOLVED","claim":"No approved external dataset, custody and held-out protocol"},
      {"id":"P5-CONFIRMATORY","status":"UNRESOLVED","claim":"Independent reviewers, frozen real endpoint, approvals and prospective registration absent"}
    ]

def run():
    p=get_json(HERE/"PROTOCOL.json")
    if p["schema"]!="unity-001-phase5-frozen-design-v1" or p["status"]!="FROZEN_EXPLORATORY_SIMULATION_SPEC_NOT_A_PHYSICAL_PREREGISTRATION":
        raise ValueError("Wrong or promoted protocol")
    src=frozen_source_guard(p)
    radii,s,n0,n1,n2=templates(p)
    y0,y1,kappa,sigma=simulate(p,s,n0)
    narrow=profile(n0,s,sigma)
    strong=profile(n1,s,sigma)
    near=profile(n2,s,sigma)
    nullfit=profile(n0,s,sigma,y0)
    altfit=profile(n0,s,sigma,y1)
    findings=classify(p,narrow,strong,near,nullfit,altfit)
    tally=dict(Counter(f["status"] for f in findings))
    readiness=p["readiness_gates"]
    if any(status!="UNRESOLVED" for status in readiness.values()):
        raise ValueError("Physical readiness cannot be promoted without an executed measurement and approval")
    return {
       "schema":"unity-001-phase5-identifiability-results-v1",
       "date":"2026-11-09",
       "protocol_sha256":hashlib.sha256((HERE/"PROTOCOL.json").read_bytes()).hexdigest(),
       "source_integrity":src,
       "toy_radii":[str(x) for x in radii],
       "toy_signal":[str(x) for x in s],
       "toy_units":"dimensionless hypothetical; not EFMW source, not external data",
       "nominal_sigma":str(sigma),
       "injected_kappa":str(kappa),
       "baseline":narrow,
       "strong_conventional_colocated":strong,
       "near_conventional":near,
       "synthetic_null":nullfit,
       "synthetic_injection":altfit,
       "sensitivity_degradation":near["sigma_kappa"]/narrow["sigma_kappa"],
       "findings":findings,
       "counts":tally,
       "physical_readiness":readiness,
       "readiness_verdict":"NOT_READY_FOR_CONFIRMATORY_PHYSICAL_PREDICTION",
       "efmw_specific_physical_pass":0,
       "phase5_status":"BOUNDED_IDENTIFIABILITY_SCREEN_PASS_PHYSICAL_PREDICTION_UNRESOLVED",
       "boundaries":["Strong allowed conventional alternative reproduces toy source exactly; nominal baseline success does not survive alternative-model expansion.",
                     "No validated EFMW-derived rho_I, fitted physical dimension, observed y, or independent review.",
                     "Nominal 5-sigma calculations describe a hypothetical Gaussian measurement model; no empirical discovery significance.",
                     "Historical MOC-001, Phase 2, Phase 3 and Phase 4 scores remain unchanged."]
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default=str(HERE/"build"/"results.json"))
    args=ap.parse_args()
    results=run()
    dest=Path(args.out)
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(results,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({k:results[k] for k in ("counts","readiness_verdict","phase5_status","efmw_specific_physical_pass","sensitivity_degradation")},indent=2))
    print("Manifest:",str(dest))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
