# Monolithic Zoo audit of the Alpöge RH reconstruction

**24 November 2026 · Jimmie Adriazola’s reconstruction · revision `aa9c86bf2a7d29b08575641fecea19a2a603e87c`**

**Verdict.** The reconstruction is a reviewable, conditional manuscript. Its own final deduction requires a uniform chain-record hypothesis that the manuscript explicitly leaves unproved. The separate Alpöge Lean archive has independent kernel verification. This audit authenticated that archive, checked every published ownership coordinate against its source, and found a repeatable error in the reconstruction’s literature-evidence export. [Pinned reconstruction](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/tree/aa9c86bf2a7d29b08575641fecea19a2a603e87c) · [Lean FRO and Mathlib joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) · [Andrew Sutherland’s verification record](https://math.mit.edu/~drew/grh/)

| Question | Finding | Decisive evidence |
| --- | --- | --- |
| Is the published RH formalization authenticated and independently checked? | **PASS, external kernel verification** | The source archive and per-file manifest hashes match locally. Independent checkers accept the exported proof and match the headline theorem statements. |
| Did this audit repeat the full RH kernel build? | **UNRESOLVED locally** | Available disk at intake was 4.5 GiB. The independently checked export alone occupies 61,570,595,788 bytes. We inspected the archive and the third-party log. |
| Can the manuscripts be built? | **PASS** | Clean builds produced 287 pages for the working manuscript and 67 for the older route notes. Both final TeX logs clear the reference checks. |
| Does the supplied ownership ledger reconcile? | **PASS for the table and its source locations** | All 868,718 declaration/location pairs exist at the cited source lines. Exact status, kind and all 1,469 owner-group counts reproduce. |
| Is the literature boundary export faithful? | **FAIL** | Seven source-reproduced rows assign data to the wrong columns or truncate a field at an escaped bar. Three additional rows differ from their source records at this revision. |
| Can the distributed graph workflow regenerate its underlying graph as documented from a clean checkout? | **FAIL at the published replay entry point** | The live-closure command exits 1 while opening an unavailable absolute-path index. The edge set and its mathematical adequacy remain independently unresolved. |
| Does the 287-page manuscript itself close the conventional proof? | **FAIL as a completion claim** | §18.3 explicitly leaves the uniform K1–K8 assembly open. §18.7 lists further internal and literature hypotheses. This agrees with the author’s current qualification. |
| Does the alternative small-prime proof in §17.4.3 establish its full K1 bound? | **UNRESOLVED, with several supported steps** | Published comparison and exponent results match the cited uses. The uniform cell-to-flag bound and the full bridge to the consuming statement remain open in this audit. |

## 1. What the formal verification covers

The reconstruction repository contains 222 tracked files and no Lean source. The formal object comes from a separate release. We downloaded all fourteen parts from Alpöge, reassembled them, hashed every regular file and traversed the package-local imports from `Main`. The archive is 239,275,554 bytes with SHA-256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`. Its sorted per-file hash list also reproduces the manifest’s independent digest. [Reconstruction source manifest](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/docs/SOURCE_MANIFEST.md) · [Public archive locations and receipts](https://github.com/leanprover-community/riemann-hypothesis/blob/main/verification/NOTES.md)

| Local source check | Result |
| --- | ---: |
| Regular files | 175,190 |
| Lean source files / files reachable by project imports from Main | 175,187 / 175,187 |
| Lean source bytes / newline count | 1,030,531,854 / 17,374,215 |
| Dependency revisions matched against the reconstruction manifest | 9 / 9 |
| Files containing any of the exact source tokens `addDecl`, `kcopy`, `kexactB` | 55 |
| Occurrences of `sorry`, `admit`, `axiom`, `unsafe`, `native_decide` or the other six listed trust markers | 0 |

The manifest reports **56** files for the metaprogramming union. Both whole-word and substring scans yield **55** at its exact archive digest. Only one file contains `addDecl`. The package locks Lean 4.33.1 and Mathlib `0df444a360eaa60ab8c11dca51a86af692955474`. All five public theorem headers are present. The independent MIT log resolves `RiemannHypothesis` to Mathlib and lists only `propext`, `Classical.choice` and `Quot.sound` for each headline theorem. The RH result, the critical-strip statements for Dirichlet characters, and the right-half-plane nonvanishing statement have separately checked types. This audit did not execute that kernel build. [MIT kernel and axiom records](https://math.mit.edu/~drew/grh/) · [Original announcement](https://alpo.ge/remark.pdf)

## 2. What the ownership labels establish

We streamed the compressed ownership table and read the original archive a second time to look up every location. All **868,718** pairs of declaration name and source location are distinct. There are **864,353** distinct declaration-name strings. Every cited line exists and contains the last component of the recorded name. A tool joining on names alone would merge distinct rows. This check does not resolve the names as Lean constants.

| Producer label | Exact-edge rows | Additional dot-only rows |
| --- | ---: | ---: |
| CLOSED | 4,506 | 620 |
| CLOSED VIA PRIOR PACKAGE | 631,740 | 78,641 |
| EXTERNAL | 130,542 | 22,664 |
| DEAD-FALSE EDGE | 0 | 5 |
| **Total** | **766,788** | **101,930** |

The exact rows include 595,612 theorems and 26,797 lemmas. Removing one row, duplicating one row, or changing a status while keeping the total fixed each broke the independent reconciliation. All 449 rows in the published-statement table have matching ownership coordinates. Only 181 have a nonempty value in `proved_in_archive_by`. A blank can reflect the exporter’s search and is insufficient evidence for an unproved theorem.

The producer reports 4,415,583 exact-live edges and 1,696 nodes in nontrivial strongly connected components. Its resolver tokenizes source and infers names, including additional dot edges. Its final classifier assigns 93,682 exact rows to a shared remainder. An empty residual table is a reproducible property of **that assignment**. A kernel dependency export and a declaration-by-declaration proof of human coverage would answer different questions. Recounting the producer’s files cannot independently validate the decisions that populated them. [Graph methods and scripts](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/tree/aa9c86bf2a7d29b08575641fecea19a2a603e87c/audit/final_certification/scripts) · [Producer’s evidence tiers](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/audit/final_certification/Global_Live_DAG_Summary.md)

The unmodified `gc_live.py` exits 1 on `/home/claude/idx/g2_meta.pkl`. The documented indexing route also reads a private-declaration list from that workspace; later stages use staged reports at other absolute paths. We did not independently recover the published edge set. The historical reconciliation contains 26 rows, five of which refer explicitly to a report unavailable in the producer’s workspace. Some reports were subsequently included. In particular the checkout now contains a separate R-2 dossier and its corrected ledger entry. Evaluating its mathematical argument remains a separate obligation. [R-2 corrected ledger](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/audit/pre_synthesis/R2_p2_Integral_HodgeTate/R2_Corrected_Ledger_Entry.md)

## 3. A reproducible error in the literature evidence

The boundary exporter splits Markdown rows at every vertical bar. The source authors escaped vertical bars used for absolute value. In row **F4-A3**, the input is an elliptic-function identity involving the squared norm of α, with Masser in the source column. The exported requirement stops inside that norm, the source column contains a fragment of α, and the bibliographic reference moves into the fidelity column. A reader consulting the TSV cannot recover the citation from its designated field. [Source row, line 23](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/audit/pre_synthesis/Final_External_Fidelity/Authoritative_External_Theorem_Ledger.md#L23) · [Exported row, line 5](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/audit/final_certification/Global_External_Boundary.tsv#L5) · [Exporter, line 7](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/audit/final_certification/scripts/gc_boundary.py#L7)

Of the 163 distributed rows, 156 come from two Markdown documents and seven are supplied directly by the exporter. The published splitting rule reproduces **153 of those 156** exactly from this checkout. Changing only the treatment of escaped bars changes seven of those 153 rows, on TSV lines **5, 7, 25, 47, 51, 118 and 126**. The other three imported rows already differ before that diagnostic change. They concern FHT-odd, FHT-2 and R-2. In the underlying R-2 material a later dossier claims internal closure with one comparison still qualified. The older TSV records an open or unverified boundary. These three records require version-aware reconciliation. The evidence bundle gives the source line, original value and recovered field for each confirmed parser failure.

The immediate repair is small and testable. Preserve escaped pipes, validate each input row against its source schema, and assert the exact mathematical requirement, source, fidelity and verdict for F4-A3 and V14. A repeat export should recover all seven documented rows and explicitly version the three differing records. This correction addresses literature provenance; it has no bearing on acceptance of the exported formal proof.

## 4. The small-prime shortcut in §17.4.3

The author asks whether an absolute exponent works for every allowed field, twist and prime. Write $i=2e$, $u=id$, $Y=\log(2D)$ and $A=H^2(G_{L,S},\mathbb Z_p(e+1))$. The claim is $\log |A|\leq\exp(u^{150}Y)$ for a totally imaginary field of degree $d$ and absolute discriminant $D$, with all places above $p$ removed and the stated roots of unity present. The register of assumptions matters at $p=2$. [Pinned argument and hypotheses](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/sec17_twisted.tex#L392)

| Step | What survived scrutiny |
| --- | --- |
| Cohomology to even K-theory | Weibel’s Theorem 73 has the totally imaginary even-degree formula with coefficients on the ring with $p$ inverted. Schmidt’s Proposition 2.3 and its proof address restricted ramification when all primes over $p$ are included in $S$. The manuscript explicitly uses finite coefficients before taking inverse limits. |
| Number of generators | Reduction modulo $p$, the Kummer sequence and the absence of real places give the stated class-group and Brauer contributions. A rank estimate alone would leave the exponent undetermined. |
| Geometry and stability | The geometric source gives the stated bound on the set of possible minimal vectors for a free lattice of rank $N\ge5$, and records stability for $N\ge2i+1$. Its published small-torsion exclusion applies to its final K-group bound. The reconstruction instead imports the geometric estimate and proposes its own integral argument. |
| Transfer at bad primes | For the subgroup of index $I$, inclusion after transfer multiplies a class by $I$. If $T$ kills subgroup torsion, $IT$ therefore kills the original torsion. No inversion of $I$ is needed. In exact cyclic controls at $p=2,3,5,7$, omitting $I$ fails on the generator in every case. |
| Hurewicz kernel | Mathew’s Theorem 6.3 applies to a connected infinite loop space with parameter $m=1$. Substitution in both prime cases gives exponents below the manuscript’s $i+4$. |
| Remaining bridge | A uniform bound on flag orbits for the chosen integral quotient must follow from the short code for nested faces. The resulting integral cellular complex must have the stated boundary-column bound. The application must then carry the resulting estimate, with its precise quantifiers, into the cohomological input used downstream. No complete independent verification of this composite step is recorded here. |

Primary checks: [Weibel, Theorem 73](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/weibel-ints.pdf) · [Schmidt, Proposition 2.3](https://www.mathi.uni-heidelberg.de/~schmidt/papers/kpi1.pdf) · [Bayer-Fluckiger, Emery and Houriet, §§3.1 and 5.1](https://ftp.gwdg.de/pub/misc/EMIS/journals/DMJDMV/vol-merkurjev/bayer_emery_houriet.pdf) · [Mathew, Theorem 6.3](https://msp.org/agt/2016/16-2/agt-v16-n2-p12-s.pdf)

**Check on the constant.** Conditional on the geometric and homological inputs, the final exponent has ample slack. For $u\ge4$ and $Y\ge\log 2>1/2$, the bound on $M$ gives $\log(1+M)\le (1+12u^5+20u^9+9u^6)Y\le u^{13}Y$, using $dN\le u^2$. With $s+1\le u^4$, this gives $\log B\le u^5+u^{21}Y\le u^{23}Y$. The quantity multiplying the generator bound is at most $B(2u^2+1+2u)\le Bu^3$. Taking logarithms once more reduces the last absorption to $7\log u+\log Y\le(u^{24}-u^{23})Y$, valid on the stated domain. This checks the arithmetic following the flag estimate. It leaves the estimate itself visible for review.

**Test that would change the verdict.** State and prove a lemma for the actual normalized well-rounded retract assigning every quotient flag a code, with at most $I(1+M)^{(s+1)^2}$ flags in each degree. Specify how a code recovers every face and how barycentric subdivision deals with stabilizers. Verify the integral boundary estimate even when quotient faces coincide. Then identify the exact fully qualified Lean obligation or downstream prose proposition and match every parameter. A valid uniform proof and matching application would close this part of the audit; a pair of inequivalent flags with the same claimed determining data would refute that coding step. The literature establishes the ingredients above. Priority for the combined shortcut has not been established.

## 5. Where the conventional proof stops

The strongest obstruction is in §18.3, where the authors require one admissible chain datum at each scale. The estimates feeding conditions K1–K8 use different presentations of constants and exponents. The manuscript explicitly records that it has yet to derive the simultaneous uniform bounds, even conditional on the hypotheses of the earlier sections. This assembly label K1 is local to the chain records; it should not be conflated with §17.4.3’s cohomological K1. Completing the small-prime argument alone cannot settle the final deduction. [Assembly, lines 272–274](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/sec18_assembly.tex#L272)

Section 18.7 identifies concrete further obligations. They include the comparisons between levels and test systems in the Hecke estimates, the seesaw pairing and period identifications, integral and local bounds in the height calculation, propagation of automorphy and rigidity in the rank-four cases, and matching the Petersson norm and measures used in the final formulas. The PDF link to that inventory lands on page 281 as advertised. A completed proof would have to discharge the applicable obligations with one consistent set of normalizations. [Final hypotheses](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/manuscript/sec18_assembly.tex#L445)

The next mathematical review with the broadest effect is a constants table for §18.3. For each of K1–K8, record its required inequality, prior result, common datum, dependence on (x,E,m) and the proposed absolute exponents. A dependence escaping those exponents is a concrete failure. A table still referring to an unproved input should retain that hypothesis explicitly.

## 6. Document and Zoo replay

The manifest has seven document hash receipts. Four match current bytes when moved paths are resolved. The working TeX and PDF hashes identify an older commit, `6f4e8cb70bc6998bdf6e9d6193eda5427fa49017`. The older route-notes PDF receipt also identifies historical bytes. The current archived PDF physically contains 67 pages and its last printed number is 67; the README describes 66. Document builds succeeded with a local TeX Live 2026 installation. The machine’s initial system TeX lacked a prebuilt format; that failure is preserved in the evidence alongside the successful runs. Rebuilt and shipped PDF text-extraction digests differ, with visible examples of changed mathematical-glyph encoding. At 96 dpi in grayscale, 276 of 287 working-manuscript pages and 55 of 67 archived pages also render pixel-identically. The other pages differ under this renderer. A byte-identical PDF claim would require a pinned typesetting environment. [Manifest and receipts](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/docs/SOURCE_MANIFEST.md)

All **12 native Zoo replay commands** passed at `b12200364f7d1424c4d9cdfbe20fff4d52de379d` with Lean 4.19.0. The native suite checked 46 registered animals, 90 fixture entries and 186 source hashes. The standalone PEGASUS suite also passed 26 reference tests. Across the 46 core operations and seven additional tracked names, this audit recorded **3 PASS, 1 FAIL, 13 UNRESOLVED and 36 NOT_APPLICABLE**. Four native decision kernels had actual target inputs. The remaining 49 received applicability reviews. The full roster gives each operation’s source, contract, rationale and result. [Zoo at the audited pin](https://github.com/enuminous/Monolithic-Zoo-Lean4/tree/b12200364f7d1424c4d9cdfbe20fff4d52de379d) · [PEGASUS at the audited pin](https://github.com/enuminous/Pegasus/tree/41d57615f16c43ea8858e35cd1250d44c3c7df97)

| Target operation | Result | Input and interpretation |
| --- | --- | --- |
| TURTLE | PASS | The open chain-record hypothesis triggers the expected veto on manuscript completion. |
| WEASEL | PASS | Four of the seven independently reproduced table defects affect at most two exported fields. A zero-field budget retains none. |
| SALMON | PASS | A bounded traversal from the actual RH declaration through its immediate proof term yields two unexpanded frontier nodes at depth two, as expected. |
| CIRCUS | FAIL | The material graph-replay check fails on missing input. The risk gate returns failure. Its missing-only and clean controls produce their expected outcomes. |

The package includes all claim dispositions, per-operation rows, original failure logs, source hashes and replay instructions. The audit was retrospective. Source inspection preceded the frozen protocol. Comparisons on the same archive or the same tables share their underlying evidence. No result from the Zoo fixtures is counted as mathematical certification of §17 or §18.
