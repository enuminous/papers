# Replaying Signed Evidence and Read-Only Tests for ALEX PR 38

Matthew Chenoweth Wright · Monolithic LLC · November 19, 2026  
Technical research note · Simulation-space audit of a published sample

## Abstract

We replayed the ALEX verifier's published PR 38 evidence package and independently tested the source revision named by that package. The parent verifier revision failed two of nine archived checksum checks. The repaired revision passed all nine and preserved the historical verifier and four specification files byte for byte. Python and TypeScript agreed on the sampled signature, hash-chain, and timestamp checks in an isolated read-only replay. Separately retrieved Git objects agreed with both reported file digests, and the target's test suite passed 58 of 58 tests from a read-only checkout. These results establish reproducibility for one fixture and one target revision. The TypeScript verifier reported claim level L1, with live observer inclusion unresolved.

## 1. Three claims that need separate evidence

A signed execution record can be checked for internal consistency using published inputs. The record can also be compared against independently retrieved source. The source can then be executed again under a new environment. Each test answers a different question. A reproducible record can describe work whose functional correctness remains open. A successful test run today says what happened under the replay conditions, while the original producer's confinement and side effects require evidence from the original run.

The audit used the Monolithic Zoo to screen evidence and determine which checks applied. It reviewed 53 roster entries, including the 46 historical animals and seven extensions. Twelve checks passed, eight remained unresolved, and 33 lacked the required input domain. These are rubric dispositions rather than 53 executed experiments. The Zoo registry passed its static integrity check. The Lean kernels were outside the execution scope. [Full operation ledger and replay commands](https://github.com/enuminous/alex-mrtb-verify-bundle/blob/79ac75b9cd9cd214f61f64f117368bd6838195af/audits/2026-11-19-monolithic-zoo/README.md)

## 2. Materials and procedure

| Item | Revision or environment |
|---|---|
| ALEX fork | `a9578b33c61d8c5623f4dd176274f0b2b0350513` |
| Parent control | `c8f4fd24b25d3dbbf1fbc6e0bbd4e81cbbd8a272` |
| Historical snapshot source | `b3d11484041ae6579baec694a75de404d682c2cc` |
| Evidence fixture | `independence/demo-pr-38.json`, schema `evidence-package@2.2`, signed L1, bundled evidence and approval PEMs |
| PR 38 base | `6144503d1eca83a8cb1ad3e0c5d0b8929af4e256` |
| PR 38 result | `b46e336852ffa3070d76f07590d59acef372f282` |
| Runtime | Linux, Python 3.13.5, OpenSSL 3.5.7, Node 24.22.3, Git 2.52.0 |

We ran the archive's manifest check against the parent and fixed revisions and compared each frozen source/spec file with the corresponding historical Git object. For execution, Bubblewrap exposed the repository read-only and provided writable temporary space. A syscall filter denied socket creation and io_uring setup while leaving local process IPC available. Direct probes confirmed that a repository write returned EROFS and socket creation returned EPERM. TypeScript dependencies and compilation were staged before the read-only replay. We fetched the two target commits separately, compared the source bytes and full diff, and ran the target's own `node --test` suite under the same read-only constraints. [Published fixture](https://github.com/enuminous/alex-mrtb-verify-bundle/tree/a9578b33c61d8c5623f4dd176274f0b2b0350513/independence) · [Target pull request](https://github.com/Alex-Proof/alex-controlled-agent-demo/pull/38)

## 3. Results

| Claim | Observation | Disposition |
|---|---|---|
| Archive checks its historical inputs | Parent 7/9, repair 9/9. The five source/spec copies match the historical revision. | Supported |
| Frozen verifier can replay offline | Two frozen Python invocations returned VERIFIED, exit 0. | Supported |
| Current implementations agree on sampled core checks | Both validated signature, hash chain, timestamp imprint, and timestamp trust chain. TypeScript reported L1. | Supported for PR 38 |
| Signed source record agrees with independently fetched Git objects | Both added files and their SHA-256 digests matched. The full diff matched after trimming trailing whitespace from the whole output. | Supported within that normalization |
| Target tests run with a read-only checkout | 58 passed, zero failed or skipped. The target has a test command and no separate build script. | Supported for the recorded result |
| Historical negative claims have independent runtime witnesses | The replay surfaced three policy-derived negatives and zero observed or attested negative claims. Live observer inclusion was unavailable. | Unresolved |

Two failed attempts help specify the environment. The default TypeScript invocation tried its GitHub diff cross-check and exited 5 in the initial sandbox. The documented `ALEX_VERIFY_SKIP_GITHUB_DIFF=1` path succeeded. The separate Git object comparison covers the diff in this study. In the first Python run, the minimal mount omitted the system OpenSSL configuration. Overall verification still passed while the timestamp trust-chain subcheck failed. Mounting `/etc/ssl` read-only restored that subcheck, and a standalone OpenSSL replay confirmed the diagnosis. These observations favor recording individual check outcomes alongside the exit status.

## 4. Interpretation and limits

The archive repair isolates preservation from ordinary development. Its predecessor pointed at mutable root files, which produced apparent manifest corruption when those files evolved. The repaired kit points at fixed copies. Historical byte comparison shows that the repair restored the intended inputs.

The fixture and PEMs came from the publisher. The signature result is therefore conditional on the supplied keys. Separate retrieval of the target Git objects corroborates the change record, and the fresh 58-test run corroborates the sampled target behavior. The study did not independently authenticate key custody, contact the live observer, reproduce the producer's runtime, measure coverage, or exercise other verifier artifact families. It also did not compile the verifier itself with a read-only checkout. The sample has an L1 approval and no WebAuthn assertion. The verifier's documented trust model describes why those distinctions matter. [ALEX trust boundary](https://github.com/enuminous/alex-mrtb-verify-bundle/blob/a9578b33c61d8c5623f4dd176274f0b2b0350513/TRUST-BOUNDARY.md)

A follow-on test can add a new evidence source without changing the fixture. Freeze the exact bundle digest, obtain the evidence and approval keys over an independently authenticated channel, and verify an observer inclusion proof using a separately authenticated observer key. A matching proof would corroborate publication of this exact record. Authenticated disagreement or an invalid supplied proof would fail the test. Unavailable inputs would keep it unresolved.
