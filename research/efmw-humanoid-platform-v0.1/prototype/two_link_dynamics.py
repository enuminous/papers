"""Offline 2-link planar arm, standard textbook rigid-body dynamics.

Used solely to exercise a candidate research workflow and classical feedback
baseline. NOT a 32-DoF humanoid twin, hardware controller or validated plant.
All constants below are invented for a benign synthetic simulation.
"""
from __future__ import annotations
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class LinkParameters:
    length_m: float = 0.40
    mass_kg: float = 1.0


@dataclass(frozen=True)
class PlanarPlant:
    link1: LinkParameters = LinkParameters()
    link2: LinkParameters = LinkParameters()
    g_m_s2: float = 9.81
    viscous_friction_nms_rad: float = 0.06
    torque_limit_nm: float = 8.0

    def _masses(self, q):
        q1, q2 = q
        m1, m2 = self.link1.mass_kg, self.link2.mass_kg
        L1, L2 = self.link1.length_m, self.link2.length_m
        lc1, lc2 = L1 / 2, L2 / 2
        I1, I2 = m1 * L1**2 / 12, m2 * L2**2 / 12
        coupling = m2 * L1 * lc2 * math.cos(q2)
        m11 = I1 + I2 + m1 * lc1**2 + m2 * (L1**2 + lc2**2) + 2 * coupling
        m12 = I2 + m2 * lc2**2 + coupling
        m22 = I2 + m2 * lc2**2
        return m11, m12, m22

    def _gravity(self, q):
        q1, q2=q
        m1, m2=self.link1.mass_kg, self.link2.mass_kg
        L1, L2=self.link1.length_m, self.link2.length_m
        g1=((m1 * L1/2 + m2 * L1) * self.g_m_s2 * math.cos(q1)
            +m2 * L2/2 * self.g_m_s2 * math.cos(q1+q2))
        g2=m2 * L2/2 * self.g_m_s2 * math.cos(q1+q2)
        return g1,g2

    def gravity_torque(self,q):return self._gravity(q)

    def mass_matrix(self,q):
        m11,m12,m22=self._masses(q)
        return ((m11,m12),(m12,m22))

    def acceleration(self, q, dq, torque, friction_multiplier=1.0):
        m11,m12,m22=self._masses(q)
        det=m11*m22-m12*m12
        if det<=0:raise ValueError('Nonpositive arm mass-matrix determinant')
        q1,q2=q
        dq1,dq2=dq
        h=self.link2.mass_kg*self.link1.length_m*(self.link2.length_m/2)*math.sin(q2)
        coriolis=(-h*(2*dq1*dq2+dq2*dq2),h*dq1*dq1)
        grav=self._gravity(q)
        rhs=[]
        for i in range(2):
            tau=min(self.torque_limit_nm,max(-self.torque_limit_nm,float(torque[i])))
            rhs.append(tau-coriolis[i]-grav[i]-self.viscous_friction_nms_rad*friction_multiplier*dq[i])
        return ((m22*rhs[0]-m12*rhs[1])/det,(-m12*rhs[0]+m11*rhs[1])/det)


@dataclass(frozen=True)
class ArmState:
    q: tuple[float,float] = (0.0,0.0)
    dq: tuple[float,float] = (0.0,0.0)


def classical_joint_pd(plant:PlanarPlant,state:ArmState,goal=(0.1,-0.1),kp=8.0,kd=2.5):
    gravity=plant.gravity_torque(state.q)
    return tuple(min(plant.torque_limit_nm,max(-plant.torque_limit_nm,
                 kp*(goal[i]-state.q[i])-kd*state.dq[i]+gravity[i])) for i in range(2))


def step(plant:PlanarPlant,state:ArmState,torque,dt_s=0.002,friction_multiplier=1.0):
    if not 0<dt_s<=0.01:raise ValueError('Explicit integration step must be positive and small')
    ddq=plant.acceleration(state.q,state.dq,torque,friction_multiplier)
    # Fixed-step semi-implicit Euler, a low-order illustrative integrator.
    ndq=tuple(state.dq[i]+dt_s*ddq[i] for i in range(2))
    nq=tuple(state.q[i]+dt_s*ndq[i] for i in range(2))
    if not all(math.isfinite(x) for x in (*nq,*ndq)):
        raise ValueError('Nonfinite simulated state')
    return ArmState(nq,ndq)


def simulated_episode(duration_s=2.0,goal=(0.1,-0.1),inject_friction_at_s=1.0):
    """Return strictly synthetic tracking traces, no robot command channel."""
    plant=PlanarPlant()
    dt=0.002
    count=round(duration_s/dt)
    state=ArmState()
    out=[]
    for i in range(count):
        t=i*dt
        tau=classical_joint_pd(plant,state,goal)
        state=step(plant,state,tau,dt_s=dt,
                   friction_multiplier=3.0 if t>=inject_friction_at_s else 1.0)
        if i%50==0:
            err=math.sqrt(sum((state.q[j]-goal[j])**2 for j in range(2)))
            out.append({'t_s':round(t+dt,6),'q_rad':[round(x,7) for x in state.q],
                        'velocity_rad_s':[round(x,7) for x in state.dq],
                        'tracking_error_rad':round(err,7),
                        'tau_nm':[round(x,7) for x in tau],
                        'friction_multiplier':3.0 if t>=inject_friction_at_s else 1.0})
    return out
