import math
import unittest
from prototype.two_link_dynamics import (PlanarPlant,ArmState,
                                           classical_joint_pd,step,simulated_episode)

class ClassicalRobotTests(unittest.TestCase):
    def test_mass_matrix_positive_definite(self):
        p=PlanarPlant()
        for q1 in [-math.pi,0,math.pi]:
            for q2 in [-math.pi,-1,0,1,math.pi]:
                m=p.mass_matrix((q1,q2))
                self.assertGreater(m[0][0],0)
                self.assertGreater(m[0][0]*m[1][1]-m[0][1]*m[1][0],0)
    def test_gravity_compensation_static_equilibrium(self):
        p=PlanarPlant()
        q=(0.3,-0.4)
        a=p.acceleration(q,(0,0),p.gravity_torque(q))
        self.assertAlmostEqual(a[0],0,places=9)
        self.assertAlmostEqual(a[1],0,places=9)
    def test_effort_never_exceeds_declared_torque_limit(self):
        p=PlanarPlant()
        for q in [(0,0),(1,-2),(-1.5,0.3)]:
            tau=classical_joint_pd(p,ArmState(q,(0,0)),goal=(3,-3))
            self.assertTrue(all(abs(x)<=p.torque_limit_nm for x in tau))
    def test_simulation_determinism(self):
        self.assertEqual(simulated_episode(),simulated_episode())
    def test_trace_length_and_time_monotonic(self):
        t=simulated_episode()
        self.assertEqual(len(t),20)
        self.assertTrue(all(t[i]['t_s']<t[i+1]['t_s'] for i in range(len(t)-1)))
    def test_toy_integration_sensible_small_step(self):
        p=PlanarPlant()
        x=step(p,ArmState(),p.gravity_torque((0.0,0.0)),dt_s=0.002)
        self.assertEqual(x,ArmState())
        with self.assertRaises(ValueError):step(p,ArmState(),(0,0),dt_s=1.0)

if __name__=='__main__':unittest.main()
