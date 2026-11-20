# From the Tokamak Return Loop to the TriSphere Simulator

November 19, 2026 · Technical companion to *Energy Through the Hourglass*

A. Beth Jones developed the TriSphere framework. The diverted-tokamak lab isolates a physical analogue for its routing and return loop. The proposed full TriSphere simulator extends that kernel into a thirteen-layer interpretive model. The muon engine is a separate application of return-loop accounting. [Jones’s TriSphere equations](https://tri-sphere-text.abethjones.workers.dev/) · [Energy Through the Hourglass](Energy-Through-the-Hourglass-TriSphere-Tokamak-2026-11-19.md) · [Tokamak repository](https://github.com/enuminous/Tokamak)

| Component | Published implementation | Proposed extension |
| --- | --- | --- |
| Particle and energy inventory | Independent one-step budgets | Time-resolved return and inventory in transit |
| Radial motion | Harmonic potential with positive damping and explicit center kicks | Shelved effective potential, valve-controlled drive, and stability mapping |
| Layer structure | Hopf shell evaluator and documented analogy | Thirteen evolving layers with mirror-paired shelf occupancy |
| Filter | Illustrative routing fractions | Time-dependent Product/Compost split and byproduct destinations |
| Boundary | Divertor-style exhaust and an independent toy oscillator | A matched exhaust-versus-containment experiment |
| Muon engine | Catalyst loss, bootstrap demand, recovered energy, and conditional ideal thrust | No validated quark-stage mechanism or tested hardware |

## Proposed boundary comparison

Start both runs from the same inventories and use identical drive, damping, routing, integration step, and run length. Change only the outer-boundary rule. In the exhaust run, record what leaves. In the containing run, route energy removed from organized motion to an explicitly tracked internal reservoir. If that reservoir transfers energy back, debit the reservoir by the amount credited to motion.

For either run, the change in total tracked energy should equal supplied work minus cumulative exhaust and any other recorded boundary losses. Score energy closure, return time, energy and particles remaining in transit, shelf occupancy, and stability after a defined perturbation. A closed boundary alone gives no positive contribution to the energy balance. A stable cycle in the existing center-kick model establishes that behavior only for its specified drive and potential.

The boundary comparison and full layer model are proposed work. The published implementations are the narrower [Tokamak lab](https://enuminous.github.io/Tokamak/) and [muon engine simulator](https://enuminous.github.io/Tokamak/engine.html).
