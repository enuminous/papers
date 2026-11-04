import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dataclasses import dataclass

# ==================== Configuration ====================
@dataclass
class Config:
    n_agents: int = 400
    world_size: float = 100.0
    energy_sources: int = 8
    steps: int = 600
    dt: float = 0.1
    sensory_radius: float = 12.0
    mutation_rate: float = 0.05
    mutation_scale: float = 0.1
    base_energy_cost: float = 0.02
    coherence_cost_scale: float = 0.015
    reproduce_threshold: float = 1.8
    max_energy: float = 3.0
    device: str = "cuda" if torch.cuda.is_available() else "cpu"

cfg = Config()
device = torch.device(cfg.device)

# ==================== Neural Policy ====================
class PolicyNet(nn.Module):
    def __init__(self, obs_dim=8, hidden=16, act_dim=4):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(obs_dim, hidden),
            nn.Tanh(),
            nn.Linear(hidden, hidden),
            nn.Tanh(),
            nn.Linear(hidden, act_dim),
            nn.Tanh(),
        )
    def forward(self, x):
        return self.net(x)

# ==================== Agent Population (vectorized) ====================
class Population:
    def __init__(self, cfg):
        self.cfg = cfg
        self.n = cfg.n_agents
        # Positions, velocities, energy
        self.pos = torch.rand(self.n, 2, device=device) * cfg.world_size
        self.vel = torch.randn(self.n, 2, device=device) * 0.5
        self.energy = torch.ones(self.n, device=device) * 1.0
        self.alive = torch.ones(self.n, dtype=torch.bool, device=device)
        # Neural nets (one shared architecture, individual weights stored flat)
        self.policy = PolicyNet().to(device)
        self.param_shapes = [p.shape for p in self.policy.parameters()]
        self.param_sizes = [p.numel() for p in self.policy.parameters()]
        total_params = sum(self.param_sizes)
        self.genomes = torch.randn(self.n, total_params, device=device) * 0.1
        # EFMW-style recursive residual memory + coherence
        self.memory = torch.zeros(self.n, device=device)          # residual memory m_t
        self.coherence = torch.ones(self.n, device=device) * 0.5  # |m| or derived score
        self.lambda_mem = 0.97                                    # memory decay

    def get_observation(self):
        # Local energy sources + nearest neighbors (simplified)
        # For demo: random local field + self state
        local_energy = torch.zeros(self.n, 1, device=device)
        for src in self.energy_sources:
            dist = torch.norm(self.pos - src, dim=1, keepdim=True)
            local_energy += torch.exp(-dist / 15.0)
        self_energy = self.energy.unsqueeze(1)
        coherence = self.coherence.unsqueeze(1)
        # Dummy neighbor signal (average coherence of nearby agents)
        neighbor_coh = self._neighbor_average(self.coherence).unsqueeze(1)
        obs = torch.cat([
            self.pos / self.cfg.world_size,
            self.vel / 5.0,
            local_energy,
            self_energy,
            coherence,
            neighbor_coh,
        ], dim=1)
        return obs[:, :8]  # truncate/pad to obs_dim

    def _neighbor_average(self, values, radius=12.0):
        # Cheap approximation: global mean weighted by proximity (full pairwise is slow)
        # For larger n, replace with spatial hash or radius graph
        dist = torch.cdist(self.pos, self.pos)
        mask = (dist < radius) & (dist > 0)
        weights = torch.exp(-dist / 5.0) * mask.float()
        weights = weights / (weights.sum(dim=1, keepdim=True) + 1e-6)
        return (weights @ values.unsqueeze(1)).squeeze(1)

    def step(self):
        if not self.alive.any():
            return
        obs = self.get_observation()
        # Apply individual genomes to policy (simplified: average for demo speed)
        # Real version would batch per-agent forward; this is a compromise
        actions = self.policy(obs)
        # EFMW recursive residual update
        residual = actions[:, 0] - self.memory          # simple residual
        self.memory = self.lambda_mem * self.memory + (1 - self.lambda_mem) * residual
        self.coherence = torch.abs(self.memory).clamp(0, 1)
        # Physics + energy
        accel = actions[:, 1:3] * 2.0
        self.vel = self.vel * 0.9 + accel * self.cfg.dt
        self.vel = torch.clamp(self.vel, -3, 3)
        self.pos = (self.pos + self.vel * self.cfg.dt) % self.cfg.world_size
        # Energy cost modulated by coherence (higher coherence = slightly cheaper)
        cost = self.cfg.base_energy_cost + self.cfg.coherence_cost_scale * (1 - self.coherence)
        self.energy -= cost * self.cfg.dt
        # Harvest from sources
        for src in self.energy_sources:
            dist = torch.norm(self.pos - src, dim=1)
            harvest = torch.exp(-dist / 8.0) * 0.08
            self.energy += harvest * self.cfg.dt
        self.energy = torch.clamp(self.energy, 0, self.cfg.max_energy)
        # Death
        self.alive = self.energy > 0.05
        # Reproduction
        can_repro = self.alive & (self.energy > self.cfg.reproduce_threshold)
        if can_repro.any() and self.alive.sum() < self.n * 0.95:
            parents = torch.where(can_repro)[0]
            if len(parents) > 0:
                parent = parents[torch.randint(0, len(parents), (1,))]
                child_idx = torch.where(~self.alive)[0]
                if len(child_idx) > 0:
                    child = child_idx[0]
                    self.genomes[child] = self.genomes[parent] + \
                        torch.randn_like(self.genomes[parent]) * self.cfg.mutation_scale
                    self.pos[child] = self.pos[parent] + torch.randn(2, device=device) * 2
                    self.energy[child] = self.energy[parent] * 0.5
                    self.energy[parent] *= 0.5
                    self.memory[child] = self.memory[parent] * 0.8
                    self.coherence[child] = self.coherence[parent] * 0.9
                    self.alive[child] = True

    def init_energy_sources(self):
        self.energy_sources = torch.rand(self.cfg.energy_sources, 2, device=device) * self.cfg.world_size

# ==================== Simulation Loop ====================
def run_simulation(cfg):
    pop = Population(cfg)
    pop.init_energy_sources()
    history = []
    for t in range(cfg.steps):
        pop.step()
        if t % 10 == 0:
            alive = pop.alive.sum().item()
            mean_e = pop.energy[pop.alive].mean().item() if alive > 0 else 0
            mean_c = pop.coherence[pop.alive].mean().item() if alive > 0 else 0
            history.append((t, alive, mean_e, mean_c))
            print(f"Step {t:4d} | Alive: {alive:4d} | Mean E: {mean_e:.3f} | Mean Coh: {mean_c:.3f}")
    return pop, history

# ==================== Visualization ====================
def animate(pop, history):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    sc = ax1.scatter([], [], s=20, c=[], cmap="plasma", alpha=0.7)
    ax1.set_xlim(0, cfg.world_size)
    ax1.set_ylim(0, cfg.world_size)
    ax1.set_title("Agents (color = coherence)")
    ax2.set_title("Population & Coherence")
    line_pop, = ax2.plot([], [], label="Alive")
    line_coh, = ax2.plot([], [], label="Mean Coherence")
    ax2.legend()
    ax2.set_xlim(0, cfg.steps)
    ax2.set_ylim(0, cfg.n_agents)

    def update(frame):
        # Re-run a short segment for animation (or store positions)
        # For simplicity this is a static snapshot version
        return sc, line_pop, line_coh

    # Static final plot instead of full animation for reliability
    alive_mask = pop.alive.cpu().numpy()
    pos = pop.pos.cpu().numpy()
    coh = pop.coherence.cpu().numpy()
    ax1.scatter(pos[alive_mask, 0], pos[alive_mask, 1],
                c=coh[alive_mask], s=20, cmap="plasma", alpha=0.8)
    # Energy sources
    src = pop.energy_sources.cpu().numpy()
    ax1.scatter(src[:, 0], src[:, 1], c="lime", s=100, marker="*", label="Energy")
    ax1.legend()
    steps, alive_h, _, coh_h = zip(*history)
    ax2.plot(steps, alive_h, label="Alive")
    ax2.plot(steps, [c * cfg.n_agents for c in coh_h], label="Coh * N")
    ax2.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print(f"Running on {device}")
    pop, history = run_simulation(cfg)
    animate(pop, history)
    print("Done.")
