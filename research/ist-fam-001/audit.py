#!/usr/bin/env python3
"""IST-FAM-001 bounded source audit. Read-only; no hypothesis tuning.
Original v1 locked first; stricter pre-execution rules committed separately.
Counts are about source SUPPORT, not mathematical impossibility or physical novelty.
"""
import argparse
import csv
import hashlib
import io
import json
import re
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LEDGER = ROOT / "research/unity-001/phase-1/source-equations.csv"
PROTOCOL = HERE / "PROTOCOL.json"
REVIEW_RULES = HERE / "PRE_EXECUTION_REVIEW_RULES.md"
EXPECTED_BLOBS = {
    "research/unity-001/phase-1/source-equations.csv": "aff2302bcbad8759f6302f8b218cf029dfc3de2a",
    "research/ist-fam-001/PROTOCOL.json": "f98961739080aa0828baf65c8ce5811044cc3904",
}
GROUP_COUNTS = {"historical_fieldspace_source": 585, "canonical": 102, "selected_source_pointers": 30}

# Hand-adjudicated near-miss source anchors from an explicit inspection of their
# ORIGINAL statements (not the separately authored audit_candidate_expression).
# The full 717-row screen still examines every original_statement.
REVIEWED_NEAR_MISSES = {
    "ME-006": "A proposed informational tensor, but no oscillator-bath modes or spectral map.",
    "ME-007": "Gravitational source split; not a source-to-bath mode construction.",
    "ME-009": "Schematic action naming recursive coupling; no physical bath-mode order.",
    "ME-011": "State/memory coupling penalty, not an oscillator-bath spectral relation.",
    "ME-023": "First-order self-model tracking; supplies no bath frequencies or weights.",
    "ME-024": "Coherence dynamics with stochastic forcing, not a derived bath spectrum.",
    "ME-041": "Defines the golden-ratio constant; does not specify physical modes.",
    "ME-042": "Scalar-23 phi power; no bath-frequency mapping.",
    "ME-043": "Phi-46 square of phi-23, described as a harmonic scale; not a physical bath-mode ladder.",
    "ME-044": "Phi-13 veto coefficient; no physically assigned oscillator weights.",
    "ME-045": "Phase/synchronization interval T=DeltaPhi/f; f is not an ordered bath spectrum.",
    "ME-046": "Phi-tiled coherence operation; spatial scaling is not a bath-frequency constraint.",
    "ME-050": "Entropic harmony expression; no spectral measure or mode index.",
    "ME-071": "Weighted memory superposition amplitudes; not the bath weights b_j=z_j omega_j^2 a_j^2.",
    "ME-072": "Recursive memory update; no oscillator spectral parameters.",
    "ME-075": "Single omega_rec phase-rate symbol; no physically specified bath-mode j sequence.",
    "ME-076": "Integral of omega_rec; no bath frequency ladder or weight relation.",
    "ME-081": "A phenomenological fluid stress; no bath spectrum or unique EFMW discriminator.",
    "ME-082": "Thixotropic relaxation law, not an oscillator-bath spectral constraint.",
    "ME-085": "Scalar-23 recursion scaling; no bath frequency or weight map.",
    "E013-Information_Tensor": "Tracking relation m_dot=alpha(q-m) only, without bath microphysics.",
    "E016-Information_Tensor": "Defined displayed memory stress R_ab=beta T_ab[m]; no physical mode map.",
    "E017-Information_Tensor": "Defined displayed informational tensor; no bath parameters.",
    "E019-Information_Tensor": "WITD PDE with memory and forcing; no source-defined spectral modes.",
    "E020-Information_Tensor": "Conditional energy ledger; no bath frequency/weight structure.",
    "E021-EFMW_Lagrangian": "C1 candidate action; no oscillator-bath mode indexing.",
    "E022-EFMW_Lagrangian": "C1 potential couplings; no source-justified spectral frequency and weight ladder.",
}

EXPLICIT_MODE = re.compile(
    r"(?:\boscillat(?:or|ion)?s?\b|\bbath\b|\breservoir\b|\bspectr(?:um|al)\b|"
    r"\beigen(?:mode|frequency|frequencies)\b|\bnormal[\s-]+modes?\b|"
    r"\bfrequency[\s-]+modes?\b|\bbath[\s-]+modes?\b)",
    re.IGNORECASE,
)
FREQUENCY_SYMBOL = re.compile(r"(?:\bomega\b|ω|\\omega|\bfrequenc(?:y|ies)\b|\bfreq\b)", re.IGNORECASE)
WEIGHT_SYMBOL = re.compile(r"(?:\bb_j\b|\\b_\{?j\}?|\bspectral[\s-]+weight\b)", re.IGNORECASE)

def gitblob(content):
    return hashlib.sha1(b"blob " + str(len(content)).encode("ascii") + b"\x00" + content).hexdigest()

def read_locked():
    for path, sha in EXPECTED_BLOBS.items():
        p = ROOT / path
        if gitblob(p.read_bytes()) != sha:
            raise RuntimeError("LOCK_DRIFT: " + path)
    if not REVIEW_RULES.is_file():
        raise RuntimeError("Missing post-v1, pre-execution review rules")
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    if protocol["status"] != "FROZEN_HYPOTHESES_NOT_EXECUTED":
        raise RuntimeError("Frozen protocol status was silently modified")
    if [x["id"] for x in protocol["candidate_constraints"]] != ["IST-FAM-H1", "IST-FAM-H2"]:
        raise RuntimeError("Wrong or additional confirmatory hypotheses")
    text = LEDGER.read_text(encoding="utf-8-sig")
    rows = list(csv.DictReader(io.StringIO(text)))
    if len(rows) != 717 or len({r["record_id"] for r in rows}) != 717:
        raise RuntimeError("Ledger incomplete or duplicate record IDs")
    groups = Counter(group(r) for r in rows)
    if dict(groups) != GROUP_COUNTS:
        raise RuntimeError("Frozen corpus grouping changed: " + repr(groups))
    return protocol, rows

def group(r):
    if r["claim_class"] == "historical_fieldspace_source":
        return "historical_fieldspace_source"
    if r["record_id"].startswith("ME-"):
        return "canonical"
    return "selected_source_pointers"

def classify_row(r):
    original = r["original_statement"]
    flags = []
    if EXPLICIT_MODE.search(original):
        flags.append("DIRECT_OSCILLATOR_OR_SPECTRAL_VOCABULARY")
    if FREQUENCY_SYMBOL.search(original):
        flags.append("FREQUENCY_SYMBOL")
    if WEIGHT_SYMBOL.search(original):
        flags.append("POTENTIAL_WEIGHT_SYMBOL")
    if r["record_id"] in REVIEWED_NEAR_MISSES:
        flags.append("MANUALLY_REVIEWED_NEAR_MISS")
    note = REVIEWED_NEAR_MISSES.get(r["record_id"], "")
    return {
        "record_id": r["record_id"],
        "group": group(r),
        "original_repo": r["original_repo"],
        "original_commit": r["original_commit"],
        "original_path": r["original_path"],
        "original_blob_sha": r["original_blob_sha"],
        "source_line": r["source_line"],
        "flags": flags,
        "row_disposition": "NO_QUALIFYING_SOURCE_DERIVATION",
        "review_note": note,
    }

def analyze():
    protocol, rows = read_locked()
    screened = [classify_row(r) for r in rows]
    countflags = Counter(flag for rec in screened for flag in rec["flags"])
    explicit = [r for r in screened if "DIRECT_OSCILLATOR_OR_SPECTRAL_VOCABULARY" in r["flags"]]
    near = [r for r in screened if r["review_note"]]
    if explicit:
        # Do not automatically infer absence; the source text needs a manual
        # derivation and physical-index audit for every direct candidate.
        raise RuntimeError("Manual review required for direct bath/spectral candidates: " + repr([r["record_id"] for r in explicit]))
    return {
        "schema": "ist-fam-001-executed-bounded-source-audit-v1",
        "date": "2026-11-09",
        "status": "COMPLETE_BOUNDED_SOURCE_SCREEN_NO_SOURCE_SUPPORT",
        "source_lock": {
            "ledger_git_blob": EXPECTED_BLOBS["research/unity-001/phase-1/source-equations.csv"],
            "protocol_git_blob": EXPECTED_BLOBS["research/ist-fam-001/PROTOCOL.json"],
            "pre_execution_amendment": "research/ist-fam-001/PRE_EXECUTION_REVIEW_RULES.md",
            "source_count": len(rows),
            "group_counts": GROUP_COUNTS,
            "unique_source_ids": len({r["record_id"] for r in rows}),
            "source_fields_screened": ["record_id","original_statement","original_repo","original_commit","original_path","source_line"],
            "excluded_evidence_fields": ["audit_candidate_expression","normalized_status"],
        },
        "screening": {
            "records_examined": len(screened),
            "direct_oscillator_or_spectral_vocabulary": len(explicit),
            "frequency_symbol_rows": countflags["FREQUENCY_SYMBOL"],
            "potential_weight_symbol_rows": countflags["POTENTIAL_WEIGHT_SYMBOL"],
            "explicit_physically_ordered_bath_mode_maps": 0,
            "manual_near_misses": len(near),
            "manually_adjudicated_ids": list(REVIEWED_NEAR_MISSES),
            "positive_source_derived_frequency_ladders": 0,
            "positive_source_derived_weight_ladders": 0
        },
        "H1": {
            "id": "IST-FAM-H1",
            "source_support": "NO_SOURCE_SUPPORT",
            "reason": "No physically indexed oscillator-bath mode sequence or source-derived omega_j map was found in the 717 frozen original statements; golden ratio constructs and omega_rec do not specify such a sequence.",
            "full_source_defined_sequence_test": "NOT_APPLICABLE_MISSING_MAP",
            "physical_novelty": "NOT_ESTABLISHED",
        },
        "H2": {
            "id": "IST-FAM-H2",
            "source_support": "NO_SOURCE_SUPPORT",
            "reason": "No source-defined b_j=z_j omega_j^2 a_j^2 physical weights or full ordered mode run; phi^-2 exponent was a guessed frozen choice, not source-derived.",
            "full_source_defined_sequence_test": "NOT_APPLICABLE_MISSING_MAP",
            "physical_novelty": "NOT_ESTABLISHED",
        },
        "bounded_stop_rule": "INVOKED_NOT_ESTABLISHED_IN_FROZEN_CORPUS",
        "beyond_scope": "No general impossibility theorem; no independently calibrated physical discriminator; no claim of external peer review or experimental replication; no new physical FAIL against all EFMW theories.",
        "near_misses": [{"id": r["record_id"],"note":r["review_note"],"original_repo":r["original_repo"],"original_path":r["original_path"],"source_line":r["source_line"]} for r in near],
        "row_screen": screened
    }

def verify_originals(records):
    """Fetch seven exact pinned original source files and verify Git blobs and rows.
    Network operation is optional for offline replay; CI runs it expressly."""
    groups = {}
    for r in records:
        key = (r["original_repo"],r["original_commit"],r["original_path"],r["original_blob_sha"])
        groups.setdefault(key,[]).append(r)
    checks = []
    for (repo,commit,path,sha), items in sorted(groups.items()):
        url="https://raw.githubusercontent.com/" + repo + "/" + commit + "/" + urllib.parse.quote(path,safe="/")
        req=urllib.request.Request(url,headers={"User-Agent":"monolithic-ist-fam-audit/1.0"})
        with urllib.request.urlopen(req,timeout=35) as resp:
            data=resp.read()
        if gitblob(data)!=sha:
            raise RuntimeError("Upstream Git blob mismatch: "+url)
        text=data.decode("utf-8-sig")
        if path.endswith("/equations.json"):
            byid={x["id"]:x["formula"] for x in json.loads(text)["equations"]}
            bad=[x["record_id"] for x in items if byid.get(x["record_id"])!=x["original_statement"]]
        else:
            lines=text.splitlines()
            bad=[]
            for x in items:
                n=int(x["source_line"])
                if n<1 or n>len(lines):
                    bad.append(x["record_id"]); continue
                actual=" ".join(lines[n-1].strip().split())
                excerpt=" ".join(x["original_statement"].strip().split())
                if actual!=excerpt and excerpt not in actual:
                    bad.append(x["record_id"])
        if bad:
            raise RuntimeError("Original source text mismatches: "+str(bad[:10]))
        checks.append({"repository":repo,"commit":commit,"path":path,"blob":sha,"records_checked":len(items),"mismatches":0})
    return {"status":"PASS_EXACT_IMMUTABLE_SOURCE_MATCH","source_files":len(checks),"records_checked":sum(x["records_checked"] for x in checks),"files":checks}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",type=Path,default=HERE/"build")
    ap.add_argument("--verify-upstream",action="store_true")
    args=ap.parse_args()
    result=analyze()
    rows=result.pop("row_screen")
    args.out.mkdir(parents=True,exist_ok=True)
    with (args.out/"ROW_SCREEN.csv").open("w",newline="",encoding="utf-8") as f:
        headers=["record_id","group","original_repo","original_commit","original_path","original_blob_sha","source_line","flags","row_disposition","review_note"]
        writer=csv.DictWriter(f,fieldnames=headers)
        writer.writeheader()
        for r in rows:writer.writerow({**r,"flags":";".join(r["flags"])})
    if args.verify_upstream:
        _, originals=read_locked()
        fidelity=verify_originals(originals)
        (args.out/"SOURCE_FIDELITY.json").write_text(json.dumps(fidelity,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
        result["source_fidelity"]=fidelity["status"]
    else:
        result["source_fidelity"]="NOT_RECHECKED_IN_THIS_RUN; use --verify-upstream"
    (args.out/"RESULTS.json").write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":result["status"],"records":result["screening"]["records_examined"],"h1":result["H1"]["source_support"],"h2":result["H2"]["source_support"],"stop_rule":result["bounded_stop_rule"],"fidelity":result["source_fidelity"]},indent=2))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
