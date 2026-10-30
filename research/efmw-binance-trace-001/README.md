# EFMW-BINANCE-TRACE-001: report and reproducible evidence

30 October 2026 · Version 0.1.0

[Read the paper](../../EFMW-Binance-Traceback-Bounded-Public-Evidence-Audit-2026-10-30.md) · [Original HTML report](EFMW-Binance-Traceback-2026-10-30.html) · [Download the evidence archive](EFMW-Binance-Traceback-2026-10-30-evidence.zip)

This package supports the bounded public-evidence audit of the reported 29 October Binance theft. It reconciles one XRP destination account and corroborates one Ethereum receipt. The full incident-wide trace remains **UNRESOLVED**, and the CIRCUS acceptance gate for a complete trace returns **FAIL**. Personal control, knowing receipt, and independent North Korean attribution are not established by this package.

## Files

| File | Purpose |
|---|---|
| [EFMW-Binance-Traceback-2026-10-30.html](EFMW-Binance-Traceback-2026-10-30.html) | Original self-contained report, preserved byte for byte. Open locally in a browser after download. |
| [EFMW-Binance-Traceback-2026-10-30-evidence.zip](EFMW-Binance-Traceback-2026-10-30-evidence.zip) | Original 76-file evidence archive: public RPC records, requests and hashes, source-address feed, event graph, fixed Zoo inputs and outputs, method source pins, licenses, and offline audit script. |
| [SHA256SUMS](SHA256SUMS) | SHA-256 checksums of the two original deliverables. The archive also contains its own manifest. |

## Reproduce the captured checks

Use Python 3 and run these commands from this directory. The audit consumes only the extracted public evidence and requires no private credentials or network requests.

```sh
sha256sum -c SHA256SUMS
python -m zipfile -e EFMW-Binance-Traceback-2026-10-30-evidence.zip audit-evidence
cd audit-evidence
sha256sum -c SHA256SUMS
python audit.py
```

The captured evidence produces twelve passing checks, `full_trace_status: UNRESOLVED`, and `complete_trace_acceptance_gate: FAIL`. The archive was extracted and these checks reproduced offline before publication. Running the script can rewrite the derived audit-result files in the extraction directory; verify the original archive hashes before running it.

## Scope and provenance

- XRP cutoff: ledger `108007272`, hash `252A6A26AA793013D3642DAD10A28D54D98843BA4C8A5422F535E65EAFFD430C`, timestamp `2026-10-30T19:02:31Z`.
- Ethereum root: `0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3`, block `26300770`.
- Method reference: [Monolithic-Zoo-Lean4 at 8b22841ffcf44e41451e7696335bf6a6ae8f222e](https://github.com/enuminous/Monolithic-Zoo-Lean4/tree/8b22841ffcf44e41451e7696335bf6a6ae8f222e). Exact upstream snapshots, provenance and licenses are inside `method/` in the archive.
- Sources: the archive's `source-manifest.json` records website URLs, retrieval metadata and hashes. Full third-party news articles and website HTML are not redistributed.

The checks establish consistency within captured provider records, not independent full-node validation, cryptographic inclusion-proof verification, a complete eleven-chain graph, or a mapping from addresses to beneficial owners. Labels and incidental incoming payments do not establish an individual's identity, knowledge or intent. Live feeds and later account activity can change.

The original HTML and ZIP are unchanged. The paper's Markdown edition clarifies “small incoming transfers” because solicitation was not established; no new ledger retrieval or attribution result is added at publication.
