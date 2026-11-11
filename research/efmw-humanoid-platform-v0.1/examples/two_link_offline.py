"""Deterministic standard robotics 2-joint example; not a humanoid."""
import pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[1]))
from prototype.two_link_dynamics import simulated_episode
from prototype.efmw_supervisor import OfflineCoherenceMonitor,Observation

trace=simulated_episode()
monitor=OfflineCoherenceMonitor()
print('Offline 2DoF simulated standard arm dynamics; no hardware; not EFMW advantage')
for i,p in enumerate(trace):
    # Synthetic feature engineering for demonstration ONLY; not predictive study.
    normalized_error=min(1.0,10.0*p['tracking_error_rad'])
    f={
      'tracking_error':normalized_error,
      'sensor_innovation':min(1.0,abs(p['velocity_rad_s'][0])/2),
      'contact_disagreement':0.0, # unsupported in arm model
      'thermal_margin_risk':0.0 # no thermal model
    }
    r=monitor.update(Observation(p['t_s'],f),now_s=p['t_s'])
    if i in (0,3,5,10,15,20,25,30,35,39):
        print(f"t={p['t_s']:4.2f}s error={p['tracking_error_rad']:5.4f}rad phi={r.coherence:.3f} [telemetry-only]")
print('Trace rows:',len(trace),'Final angle:',trace[-1]['q_rad'])
print('No control-performance or anomaly-detection claim is made from this example.')
