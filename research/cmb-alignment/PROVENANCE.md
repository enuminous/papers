# Provenance and recovery ledger

Search date: 18 October 2026. Machine-readable metadata are in [provenance.json](provenance.json); file-level SHA-256 digests are in [SHA256SUMS](SHA256SUMS).

## Historical claim: narrative recovered, computation unresolved

The matching source is [*Foundations of a Dynamic Cosmos*](https://github.com/enuminous/medium/blob/61f5f441628563a313ed64a295f69c7baeb71c72/2025-01-23_Foundations-of-a-Dynamic-Cosmos--Resolving-Anomalies-with-Rotational-Potentials--Linear-Potentials--79279ea03332.html), by Matthew Chenoweth Wright and Millie Complex AI. The article is dated January 23, 2025. Its HTML export is dated August 19, and its GitHub upload commit is dated August 21, 2025. These establish a preserved account, not a verifiable simulation execution date.

Section 3.1.1 describes 100,000 proto black holes, Gaussian spin assignments, directional anisotropic momenta, and Monte Carlo work. The discussion connects the account with the Axis of Evil and iterative refinement. Thus an initial bounded code search that failed to locate a package must not be generalized to “no historical record exists.”

The inspected HTML did not supply an executable repository, seed archive, raw output arrays or a reconstructible sky-map pipeline. Twenty external images include equations/figures/results. Their pixels were inaccessible in this session, so a complete inventory of numbers in those images is **not** claimed. Accessible hyperlinks point to Medium pages rather than a simulation archive.

| Required historical artifact | Recovery |
|---|---|
| Narrative identifying 100,000 objects | Recovered |
| Original executable and environment | Not recovered |
| Seed or full RNG state | Not recovered |
| Complete distributions, parameter values and units | Partial narrative only |
| Physical evolution and PBH-to-CMB transfer | Not recovered as executable specification |
| Raw outputs and preserved simulated sky maps | Not recovered |
| Alignment estimator and selection history | Not recovered |
| Isotropic controls processed identically | Not recovered |

Assigned directional momenta would already encode anisotropy. Even a recovered alignment from such inputs would need an isotropic-input ablation before it could support spontaneous generation. “Gaussian spins” alone is insufficient: the means, covariance, directions, normalization and correlations determine the symmetry of the sampling law.

## Search coverage and limits

Repository/code searches used terms including Axis of Evil, primordial, black hole, CMB, 100000, 100_000, 100,000, rotation and recursion. Recursive default-branch inventories were read for papers, medium, Medium2, Medium3, Multiverse-Simulator, EFMW, EFMW-FULL, efmw-research-cache, docs and EFMW-Axioms. The exact returned references and entry counts are preserved in the JSON ledger.

Candidate paths were selected and read; this was not a full content scan of every blob. Relevant checks included:

- Multiverse-Simulator's README and simulation script describe a finite quantum world graph, not the claimed PBH/CMB computation.
- EFMW-FULL's simulator concerns synthetic control degradation, not primordial black holes.
- An indexed 100000 hit in Emergentology was a decimal output value; the Oroboros hit was a number-formatting threshold. Neither identified the claimed package.
- Additional January, March, June and July 2025 articles/comments repeat rotational or CMB motivations but did not identify the missing executable products in the inspected text.

Repository enumeration returned 100 entries and an empty continuation despite additional known repositories. Known repositories were therefore inspected directly. Indexed code searches also missed known narrative content. Both limitations preclude an exhaustive absence claim. Full historical branches, deleted files, gists, unconnected disks and inaccessible conversations were not searched. Personal-context retrieval did not recover an attributable original execution record.

Research-file searches recovered the October 18 records below. Their creation metadata and original content distinguish them from the 2025 narrative. No historical sky-map file was identified among the retrieved records.

## Separate October 18, 2026 artifacts

| Record | Creation time, UTC | Role |
|---|---|---|
| recursion_run2.py and results | 14:59 | Toy hierarchical spin/mass accounting, assigned rebound inheritance |
| Universe_003_Audit.md | 15:02 | Statistical audit of the toy population |
| recursion_run3.py and results | 15:02 | 128 isotropic seeds and 32 deliberately biased controls |
| Universe_004_Audit.md | 15:06 | Separate 64-body experiment, no recovered CMB transfer |
| Universe_005_Audit.md | 15:10 | Separate 64-body experiment, no recovered CMB transfer |

Relevant 002/003 source and result snapshots are preserved in [recovered/](recovered/). They were read from the research records, not inferred from the historical narrative. Library creation times document the recovered record versions; they are not independent attestations of when their computations first ran.

The snapshots preserve connector-retrieved text. Text transport may normalize trailing newlines; file digests identify the committed snapshots, not independently downloaded original attachment bytes. The primary protocol and initially staged numerical files are preserved byte-for-byte from their frozen Git commits.

The 003 source uses NumPy default_rng, seed 20261018+i for 128 null populations and 20261018+100000+i for 32 biased controls. Each population begins with 100,000 objects. Masses follow lognormal(0,0.35); directions are normalized independent standard Gaussian vectors; dimensionless spin factors are uniform on [0.05,0.85]. The biased control adds 0.2 to the z component before normalization. Pairwise mass-loss fractions are uniform on [0.005,0.025] and vector-spin-loss fractions on [0.03,0.15].

These are explicit toy distributions, not recovered observationally constrained PBH populations. The four-remnant stopping rule and the 002 inheritance factor 0.65 are imposed. Source comments call one statistic preregistered, but no independent earlier registration record was recovered for that claim; it is treated here as a declared statistic in an exploratory source.

The 003 source has a stale comment saying “two” controls; its executable range and results contain 32. The archived file is unmodified. The rerun driver omits only its final absolute-path write and print, executes all numerical statements, and compares the complete generated dictionary with the saved JSON. The local rerun matched exactly. It does not rerun or certify Universe 002, 004 or 005.

## New work performed here

The frozen null protocol, harmonic estimator, public WMAP measurement and scoring code are newly implemented. They must not be attributed to the missing historical simulation. The WMAP FITS checksum identifies an observed NASA data product, not an EFMW-generated output.

The primary protocol commit and the later observational protocol commit preserve the order of work. [execution.json](execution.json) records local execution and verification. [README.md](README.md) explains the inferential limits, model obligations and reproducibility commands.
