"""EFMW Humanoid Platform v0.1 — intentionally OFFLINE-ONLY reference.

Implements a standard memory/innovation monitor motivated by EFMW and a strict,
human-reviewed assembly graph. It is NOT a control system for real hardware.
There are deliberately no motor drivers, ROS topics, network calls or
motor command outputs. Actual hardware cannot be enabled by these methods.

Pure standard-library Python, 3.10+. Public review is required before reuse.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from typing import Dict, Iterable, Mapping, Optional, Tuple
import hashlib
import json
import math

FEATURE_KEYS = (
    "tracking_error",
    "sensor_innovation",
    "contact_disagreement",
    "thermal_margin_risk",
)

PHYSICAL_MODES = frozenset({
    "BENCH_LOW_ENERGY", "FIXED_BASE_RESTRICTED", "HARNESS_RESTRICTED"
})


class EvidenceError(ValueError):
    """A required model, observation, approval or evidence contract was broken."""


def _sha256(data: object) -> str:
    message = json.dumps(data, sort_keys=True, ensure_ascii=False,
                         separators=(",", ":"), allow_nan=False)
    return hashlib.sha256(message.encode("utf-8")).hexdigest()


def _finite(value: object, description: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise EvidenceError(f"{description} must be numeric")
    z = float(value)
    if not math.isfinite(z):
        raise EvidenceError(f"{description} must be finite")
    return z


@dataclass(frozen=True)
class MonitorConfig:
    alpha: float = 0.15  # memory EWMA retention update
    beta: float = 0.12   # coherence smoothing rate
    k: float = 2.0      # innovation penalty scale
    anomaly_penalty: float = 0.05
    anomaly_threshold: float = 0.40
    max_age_s: float = 0.12

    def __post_init__(self) -> None:
        for name in ("alpha", "beta", "k", "anomaly_penalty",
                     "anomaly_threshold", "max_age_s"):
            z = _finite(getattr(self, name), name)
            if name in ("alpha", "beta") and not (0.0 < z <= 1.0):
                raise EvidenceError(f"{name} must be in (0,1]")
            if name in ("anomaly_penalty", "k", "max_age_s") and z < 0.0:
                raise EvidenceError(f"{name} must be nonnegative")
            if name == "anomaly_threshold" and not (0.0 <= z <= 1.0):
                raise EvidenceError(f"{name} must be in [0,1]")
        if self.max_age_s <= 0:
            raise EvidenceError("max_age_s must be positive")


@dataclass(frozen=True)
class Observation:
    timestamp_s: float
    features: Mapping[str, float]
    independently_reported_anomaly: bool = False


@dataclass(frozen=True)
class MonitorResult:
    status: str
    timestamp_s: float
    coherence: float
    innovation: float
    history_hash: str
    recommended_hold: bool
    feature_flags: Tuple[str, ...]
    note: str = "Telemetry only. No permission to operate physical motors."


class OfflineCoherenceMonitor:
    """Standard EWMA + bounded coherence *proposal*; NOT canonical ME-024.

    Config and timestamp are frozen by caller; no actuator authority exists.
    """

    def __init__(self, config: MonitorConfig = MonitorConfig()):
        self.config = config
        self.memory: Optional[Dict[str, float]] = None
        self.coherence = 0.5
        self.previous_time: Optional[float] = None

    def update(self, obs: Observation, *, now_s: float) -> MonitorResult:
        t = _finite(obs.timestamp_s, "timestamp_s")
        now = _finite(now_s, "now_s")
        if self.previous_time is not None and t <= self.previous_time:
            raise EvidenceError("observation clock is not strictly increasing")
        if t > now or now - t > self.config.max_age_s:
            raise EvidenceError("measurement stale or from the future")
        if not isinstance(obs.independently_reported_anomaly, bool):
            raise EvidenceError("independently_reported_anomaly must be boolean")
        if not isinstance(obs.features, Mapping) or set(obs.features) != set(FEATURE_KEYS):
            raise EvidenceError("feature schema mismatch")
        features = {key: _finite(obs.features[key], key) for key in FEATURE_KEYS}
        for name, x in features.items():
            if not 0.0 <= x <= 1.0:
                raise EvidenceError(f"{name} feature outside normalized [0,1] range")
        if self.memory is None:
            # First observation is an initialization, not a confident stable baseline.
            self.memory = dict(features)
            innovation = 0.0
            self.coherence = 0.5
        else:
            innovation = math.sqrt(sum(
                (features[key] - self.memory[key]) ** 2 for key in FEATURE_KEYS
            ) / len(FEATURE_KEYS))
            # Novelty is scored against the PRIOR memory: avoids self-erasure.
            target = math.exp(-self.config.k * innovation)
            p = self.config.anomaly_penalty if obs.independently_reported_anomaly else 0.0
            self.coherence = min(1.0, max(0.0,
                (1.0 - self.config.beta) * self.coherence
                + self.config.beta * target - p))
            self.memory = {
                key: (1.0 - self.config.alpha) * self.memory[key]
                     + self.config.alpha * features[key]
                for key in FEATURE_KEYS
            }
        self.previous_time = t
        flags = tuple(key for key in FEATURE_KEYS if features[key] > 0.8)
        return MonitorResult(
            status="OBSERVED_SIMULATION_ONLY", timestamp_s=t,
            coherence=round(self.coherence, 10), innovation=round(innovation, 10),
            history_hash=_sha256(self.memory),
            recommended_hold=(self.coherence < self.config.anomaly_threshold
                              or bool(flags) or obs.independently_reported_anomaly),
            feature_flags=flags,
        )


@dataclass(frozen=True)
class SafetySnapshot:
    mode: str
    human_authorized: bool
    sensors_fresh: bool
    model_version_matches: bool
    emergency_stop_latched: bool
    safety_permit: bool
    hardware_motion_requested: bool


@dataclass(frozen=True)
class GateDecision:
    outcome: str
    reasons: Tuple[str, ...]
    is_physical_motion_authorized: bool = False


def assess_candidate(snapshot: SafetySnapshot, *, efmw_score: float) -> GateDecision:
    """Offline task-candidate prefilter. ALWAYS refuses physical authorization.

    This function is not connected to certified sensors or real actuator output.
    It reports 'SIMULATED_CANDIDATE_OK' at most, never a motor token.
    """
    score = _finite(efmw_score, "efmw_score")
    if not 0.0 <= score <= 1.0:
        raise EvidenceError("efmw_score must be in [0,1]")
    reasons = []
    if snapshot.mode not in {"POWER_ISOLATED", "MAINTENANCE_LOCKOUT", "SIMULATION",
                             "DIAGNOSTIC", *PHYSICAL_MODES, "SAFE_STOP", "E_STOP_LATCHED"}:
        reasons.append("UNKNOWN_MODE")
    if snapshot.emergency_stop_latched:
        reasons.append("EMERGENCY_STOP_LATCHED")
    if not snapshot.human_authorized:
        reasons.append("MISSING_HUMAN_APPROVAL")
    if not snapshot.sensors_fresh:
        reasons.append("STALE_SENSORS")
    if not snapshot.model_version_matches:
        reasons.append("CONFIGURATION_MISMATCH")
    if not snapshot.safety_permit:
        reasons.append("INDEPENDENT_SAFETY_DENY")
    if snapshot.hardware_motion_requested or snapshot.mode in PHYSICAL_MODES:
        reasons.append("HARDWARE_NOT_SUPPORTED_BY_REFERENCE")
    if snapshot.mode != "SIMULATION":
        reasons.append("SIMULATION_MODE_ONLY")
    # EFMW score cannot authorize operation. Lower confidence is advisory only.
    if score < 0.40:
        reasons.append("EFMW_RECOMMENDS_HOLD_ADVISORY")
    decision = "SIMULATED_CANDIDATE_OK" if not reasons else "DENIED"
    return GateDecision(outcome=decision, reasons=tuple(reasons),
                        is_physical_motion_authorized=False)


class OfflineAssemblyLedger:
    """Human-reviewed simulation-stage advancement, physically incapable of acting.

    A0/A1/A2 only; all A3+ transitions denied regardless of apparent evidence.
    Approval tokens here are mock attestations, NOT cryptographic signatures.
    """
    SIMULATION_STAGE_IDS = frozenset({"A0", "A1", "A2"})

    def __init__(self, assembly_config: Mapping):
        stages = assembly_config.get("stages")
        if not isinstance(stages, list) or not stages:
            raise EvidenceError("assembly graph missing stages")
        self.stages = {s["id"]: dict(s) for s in stages}
        if len(self.stages) != len(stages):
            raise EvidenceError("duplicate stage IDs")
        self._check_graph()
        self.accepted: set[str] = set()
        self.events: list[Dict] = []
        self.event_hash = "0" * 64

    def _check_graph(self) -> None:
        visiting: set[str] = set()
        visited: set[str] = set()
        def walk(stage_id: str) -> None:
            if stage_id in visiting:
                raise EvidenceError("assembly graph cycle")
            if stage_id in visited:
                return
            visiting.add(stage_id)
            for p in self.stages[stage_id].get("depends_on", []):
                if p not in self.stages:
                    raise EvidenceError(f"missing assembly prerequisite {p}")
                walk(p)
            visiting.remove(stage_id)
            visited.add(stage_id)
        for sid in self.stages:
            walk(sid)

    def suggest_next(self, priorities: Optional[Mapping[str, float]] = None) -> list[str]:
        """Return eligible NEXT PROPOSALS ranked by optional bounded task utility."""
        priorities = priorities or {}
        for stage_id, val in priorities.items():
            if stage_id not in self.stages or not 0.0 <= _finite(val,stage_id) <= 1.0:
                raise EvidenceError("invalid priority entry")
        candidates = [sid for sid,s in self.stages.items()
                      if sid not in self.accepted
                      and not s.get("physical", False)
                      and all(p in self.accepted for p in s.get("depends_on", []))]
        return sorted(candidates, key=lambda sid:(-priorities.get(sid,0.0),sid))

    def promote_simulation_stage(self, stage_id: str, *, evidence: Mapping[str,str],
                                 human_review: str, frozen_revision: str) -> str:
        if stage_id not in self.stages:
            return self._event(stage_id,"FAIL","UNKNOWN_STAGE")
        stage = self.stages[stage_id]
        if stage.get("physical", False) or stage_id not in self.SIMULATION_STAGE_IDS:
            return self._event(stage_id,"FAIL","PHYSICAL_STAGES_NEVER_ALLOWED")
        if stage_id in self.accepted:
            return self._event(stage_id,"FAIL","ALREADY_ACCEPTED")
        if any(p not in self.accepted for p in stage.get("depends_on", [])):
            return self._event(stage_id,"UNRESOLVED","PREREQUISITES_NOT_PASSED")
        if (not isinstance(evidence, Mapping)
            or any(not isinstance(evidence.get(k),str) or not evidence[k].strip()
                   for k in stage.get("required_evidence",[]))):
            return self._event(stage_id,"UNRESOLVED","MISSING_REQUIRED_EVIDENCE")
        if not isinstance(human_review,str) or not human_review.strip():
            return self._event(stage_id,"UNRESOLVED","MISSING_HUMAN_REVIEW")
        if not isinstance(frozen_revision,str) or not frozen_revision.strip():
            return self._event(stage_id,"UNRESOLVED","MISSING_FROZEN_REVISION")
        self.accepted.add(stage_id)
        return self._event(stage_id,"PASS","SIMULATION_DOCUMENTARY_GATE_ONLY",
                           {'evidence_digest':_sha256(dict(evidence)),
                            'review_token':human_review,
                            'frozen_revision':frozen_revision})

    def _event(self, stage_id: str, outcome: str, reason: str,
               metadata: Optional[Mapping] = None) -> str:
        event={"seq":len(self.events)+1,"stage_id":stage_id,"outcome":outcome,
               "reason":reason,"metadata":dict(metadata or {}),
               "previous_event_hash":self.event_hash}
        self.event_hash=_sha256(event)
        event["event_hash"]=self.event_hash
        self.events.append(event)
        return outcome

    def replay(self) -> bool:
        digest="0"*64
        for i,e in enumerate(self.events):
            if e.get('seq')!=i+1 or e.get('previous_event_hash')!=digest:
                return False
            clone={k:v for k,v in e.items() if k!='event_hash'}
            digest=_sha256(clone)
            if e.get('event_hash')!=digest:
                return False
        return digest == self.event_hash


def load_assembly_graph(file_path: str) -> OfflineAssemblyLedger:
    with open(file_path, "r", encoding="utf-8") as f:
        return OfflineAssemblyLedger(json.load(f))
