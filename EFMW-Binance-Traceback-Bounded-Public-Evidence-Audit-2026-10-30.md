# EFMW Binance Traceback: A Bounded Public-Evidence Audit

**Matthew Chenoweth Wright** · Monolithic LLC / eNuminous

30 October 2026 · Public-evidence technical report · Version 0.1.0  
**Audit:** EFMW-BINANCE-TRACE-001  
**XRP evidence cutoff:** 30 October 2026, 19:02:31 UTC / 12:02:31 p.m. PDT; ledger 108007272  
**Overall status:** **FULL TRACE UNRESOLVED; COMPLETE-TRACE ACCEPTANCE GATE FAIL**

[Original HTML report](research/efmw-binance-trace-001/EFMW-Binance-Traceback-2026-10-30.html) · [Evidence package and reproduction](research/efmw-binance-trace-001/README.md)

## Abstract

This retrospective audit examines a bounded portion of the reported 29 October 2026 Binance theft using public XRP Ledger and Ethereum records. Five explorer-labelled Binance payments deliver 233,461,943.1 XRP to one account. Including five additional payments totalling 50 drops, exact integer accounting and transaction-metadata replay reconcile its closing balance of 233,461,943.100050 XRP; no account-authored transaction appears through the fixed cutoff. One Ethereum transaction is corroborated at the public-provider record level, with 63 token-transfer events, including a USDT event corresponding to 1,615,409,498.973240 USDT. Its displayed internal native-ETH transfer was not independently replayed. Twelve checks pass on the captured evidence. The canonical CIRCUS gate rejects acceptance of an incident-wide complete-trace assertion because the complete theft-root set, subsequent branches, cross-chain matches and custody records are missing. North Korean attribution remains source-supported rather than independently established in this audit; no personal control by Kim Jong Un or knowing receipt by a named intermediary is demonstrated. The contribution is a reproducible, explicitly bounded evidence audit using established forensic methods, with no demonstrated EFMW tracing advantage.

**Keywords:** blockchain forensics; Binance; XRP Ledger; Ethereum; evidence provenance; exact accounting; attribution; Monolithic Zoo.

## 1. Frozen target and interpretation

The request is interpreted as tracing the reported October 29 Binance theft back to its source transactions and forward toward holdings, freezes, custody endpoints and any independently supported attribution. Full success requires a complete root set, exact per-asset accounting, matched cross-chain transitions, a declared cutoff and no unresolved branch. Personal identity and knowledge require separate evidence. Missing material is recorded as UNRESOLVED.

This is a retrospective public-evidence audit. It is not a preregistered test of predictive performance, a Lean proof of the incident, or a demonstrated new capability of EFMW physics. A fixed protocol was recorded before the new retrieval round; the news event and initial claims were already known.

## 2. Published context and its limits

[Elliptic’s primary analysis](https://www.elliptic.co/insights/binance-largest-hack-in-history/) reports $6.43 billion stolen across 11 chains and $2.84 billion frozen at its stated cutoff. Its loss and freeze estimates use different valuation times. They should not be subtracted to produce an exact current spendable balance.

Elliptic attributes the theft to North Korea-linked actors, citing methods and a small overlap with funds from the Bitget exploit. It also warns that shared laundering infrastructure can serve different clients and says official attribution had not been confirmed at its article cutoff. This audit has not independently reproduced that attribution.

The earlier “about $3 billion frozen” figure remains a company-reported estimate repeated by the [BBC](https://www.bbc.co.uk/news/articles/cwe8lp7zy07zo). A freeze, a tracing label, a seizure, a return to Binance and customer reimbursement are different events. A reimbursement promise is not a proof of recovery.

## 3. XRP: exact bounded reconciliation

Destination: [rK21t6nGLy4MNDqhvy3pGwcLFy25qgfzMx](https://xrpscan.com/account/rK21t6nGLy4MNDqhvy3pGwcLFy25qgfzMx). Labels below come from XRPSCAN; amounts and transaction membership were cross-checked with a public XRP Ledger RPC provider. Two providers agreeing on ledger data does not independently prove the legal owner behind a label.

| Explorer source label | Time, Pacific | Delivered XRP | Transaction |
| --- | --- | --- | --- |
| Binance 6 | Oct 29 01:05:00 PM PDT | 185,017,485.5 | [78E31E7BB06ADA…](https://xrpscan.com/tx/78E31E7BB06ADABE2322FDD0553533873C1D90664AEDE0C12DE06208F50BFA6A) |
| Binance 9 | Oct 29 01:07:00 PM PDT | 14,693,052.5 | [6DDF398B6950B3…](https://xrpscan.com/tx/6DDF398B6950B34057A7B817E761A1E2A1C59ECAFD594536C54AA6963C5B7E67) |
| Binance 18 | Oct 29 01:08:20 PM PDT | 13,140,680.4 | [9FE8F79876B30E…](https://xrpscan.com/tx/9FE8F79876B30E24843031CBE89EA75496FE75BD2F0B9779D91D55BEE52C6AAA) |
| Binance 15 | Oct 29 01:08:50 PM PDT | 11,955,157.6 | [27C7D0D5EDAD05…](https://xrpscan.com/tx/27C7D0D5EDAD05B5F8C7616DF6CB64C872DD22DED8697B380824A8C5B8D385F5) |
| Binance 10 | Oct 29 01:09:20 PM PDT | 8,655,567.1 | [0571C4D9703DEC…](https://xrpscan.com/tx/0571C4D9703DECA7D03B8D63E9EEB2AB0E8E6D949150A7355519AEEE9A595DB0) |

All five payments arrived between 1:05 and 1:09:20 p.m. Pacific on October 29. The complete returned account history contains 11 records: five large source-labelled payments, five inbound payments of 10 drops each, and one CheckCreate. The latter is not counted as an XRP transfer.

```text
233,461,943.100000 XRP + 0.000050 XRP − 0 outgoing XRP = 233,461,943.100050 XRP
```

The balance reconciles both by summing delivered amounts and by replaying the account balance changes in transaction metadata. No account-authored transaction appears through ledger `108007272`. The history request has no remaining pagination marker. Each returned transaction is present in its corresponding validated ledger response.

Cutoff ledger hash: `252A6A26AA793013D3642DAD10A28D54D98843BA4C8A5422F535E65EAFFD430C`. Ledger time: `2026-10-30T19:02:31Z`.

**Held does not mean frozen.** The [XRP Ledger documentation](https://xrpl.org/docs/concepts/tokens/fungible-tokens/freezes) states that native XRP has no issuer-freeze mechanism; custodians can restrict funds under their control. This account’s lack of outgoing activity does not establish that its keys are accessible, that the balance is permanently unusable, or that a particular person controls it.

The five tiny incoming transfers are a concrete contamination risk for identity analysis. Neither those payments nor the incoming check establishes that the senders are collaborators. Their identities and motives are not asserted here.

## 4. Ethereum: a corroborated root transaction

[Transaction 0x53bd38b816c23e74…](https://etherscan.io/tx/0x53bd38b816c23e74134786c29a8c18d792777998a3b9326047b583100e88e2f3) is in Ethereum mainnet block `26300770`. The public RPC returned a successful receipt; its transaction and block hashes match the containing block. Etherscan corroborates the event display.

| Role | Observed address |
| --- | --- |
| Transaction caller | `0x7c8601d4645b93cea45f71e118a729332e6b5ca0` |
| Execution context, labelled Binance 14 | `0x28c6c06298d514db089934071355e5743bf21d60` |
| Recipient of the 63 victim-origin Transfer events | `0x5227f603c1ee34ce3c06efe6477003bdfccb2f8c` |

The receipt has 64 logs, including 63 distinct Transfer events from Binance 14 to the same recipient. One is the USDT contract’s event for `1615409498973240` atomic units. The [verified token metadata](https://etherscan.io/token/0xdac17f958d2ee523a2206206994597c13d831ec7) reports six decimals, yielding **1,615,409,498.973240 USDT**.

The top-level transaction has zero native ETH value. Etherscan separately displays an internal transfer of **167,464.247856558836135296 ETH**. Internal execution traces were unavailable from the queried RPC, so that native amount remains explorer-supported rather than independently replayed here. The receipt logs do not by themselves prove every token’s economic value or implement a complete token-state replay.

These records establish a bounded source-to-recipient path. They do not enumerate every later transfer, establish the recipient’s personal identity, or prove a later cash-out.

## 5. Address leads and coverage

The [public Elliptic feed](https://data-cdn.elliptic.co/blocklists/binance-hack-blocklist.csv) captured at 19:01:14 UTC contains 1,075 headerless, single-column rows. Preserving the first row matters: treating it as a header would silently drop a lead. EVM case normalization gives 1,071 address strings; this is not a count of distinct chain-qualified accounts, and not a count of people. The feed supplies no chain IDs, transaction hashes, per-row ownership evidence or edge roles.

| Syntactic form only | Raw rows |
| --- | --- |
| EVM-shaped hexadecimal | 346 |
| Tron-shaped | 695 |
| Bitcoin bech32-shaped | 30 |
| XRP classic-shaped | 1 |
| Unclassified in this audit | 3 |

Syntax alone does not assign an EVM address to Ethereum rather than another EVM chain. A publisher’s attribution entry is retained as a lead, not promoted to proof of criminal control. The inspected XRP and Ethereum records are a deliberately bounded corroboration; no percentage of the entire theft independently traced is asserted because the full root/value denominator is absent.

## 6. Fixed Zoo operations and actual execution

The method reference is [Monolithic-Zoo-Lean4 at 8b22841ffcf4](https://github.com/enuminous/Monolithic-Zoo-Lean4/tree/8b22841ffcf44e41451e7696335bf6a6ae8f222e). Exact upstream Python snapshots and Git blob identities were checked before execution. No operation was renamed into a blockchain detector.

| Operation | Purpose | Inputs → transformation | Criterion | Actual result |
| --- | --- | --- | --- | --- |
| ELEPHANT | Retain event order, source pointers, current records and correction lineage. | Four supplied audit records → current/history/lineage functions. | Earlier parse record must become superseded; both versions and provenance must remain available. | PASS on bookkeeping. It does not validate the truth of supplied evidence. |
| CIRCUS | Gate a proposed complete-trace assertion against provenance, dependencies, open material risks and checks. | Frozen scope plus documented coverage gaps → unmodified decide(report). | The original gate rejects materially unresolved risks; it cannot treat incomplete validation as a complete trace. | FAIL for acceptance of the complete-trace claim. Underlying missing links remain UNRESOLVED. |
| MONSTER | Check eligibility for a preregistered robustness comparison. | No matched baseline, frozen performance tolerance or registered conditions → original eligibility gate. | All required eligibility fields must be supplied before a robustness verdict. | N/A. No robustness experiment was run. |
| Other Zoo animals | Preserve their actual domains and required inputs. | No suitable frozen feature arrays, predictive experiment or causal ablation supplied. | No substitute operation may be invented to obtain a verdict. | NOT RUN. This is not a claim that all Zoo software executed. |

ELEPHANT is pinned to `a30bd9ae77d7df31f35b533e5310eb7e06aa3d40`; CIRCUS to `647c91dc06b4ea48871c06608298b46f00f68f99`; MONSTER to `95f475ccffa30afe1853659dfd9431734b2788e0`. The package contains exact inputs and outputs. No Lean compilation or theorem-proving run was performed for this audit.

## 7. Anti-circularity, independence and rejected inferences

- Elliptic’s list selected candidate addresses. Finding the same list or its quotations in other news reports is not independent confirmation of its labels.
- RPC records corroborate payments, logs and balances. They do not establish the ownership or knowledge of a human behind an address.
- Receipt logs are evidence of emitted events. Contract semantics, actual balance changes and economic value are separate obligations.
- A shared destination may be a service used by multiple clients. It does not by itself establish a common attacker.
- Small incoming transfers and incoming nonpayment objects are retained as events but excluded from unsupported collaborator claims.
- Freeze amounts are state observations. They are not added as new transfer volume, and later hops are not counted again as newly stolen principal.
- Missing data are not converted into a “clean” verdict or an assertion that tracing is impossible.

A historical example supports the existence of facilitators, not their involvement here: the [U.S. Treasury’s March 2, 2020 sanctions notice](https://home.treasury.gov/news/press-releases/sm924) describes two intermediaries accused of handling roughly $100 million linked to North Korean exchange thefts. That official account is not evidence that those people handled this incident.

## 8. Proof obligations and claim dispositions

| Obligation | Status | Evidence or gap |
| --- | --- | --- |
| Complete initial theft-root set across all affected chains | UNRESOLVED | Public attribution feed lacks chain IDs, edge roles and initial transaction identifiers. |
| Exact XRP unit accounting and complete inspected-account history | PASS in the fixed window | One drop is 10⁻⁶ XRP; received amounts and account-state transitions match exactly. |
| Ethereum root transaction and token-event inclusion | PASS at provider-record level | Successful receipt and containing block obtained independently of the news articles. |
| Ethereum internal execution replay and present freeze-state proof | UNRESOLVED | Internal-trace methods were unavailable/forbidden; no historical state proof was obtained. |
| Cross-chain bridge and swap links | UNRESOLVED | Require matched protocol events, identifiers and asset/fee accounting; matching amounts or times alone are insufficient. |
| Proof of withdrawal to a specific exchange customer or bank beneficiary | UNRESOLVED | Public addresses stop at custody boundaries; customer and bank records are outside this audit. |
| Proof of an intermediary’s knowledge and intent | UNRESOLVED | Requires independent evidence beyond transfer proximity, name tags, country, or a shared service address. |
| Reproducible evidence handling | PASS in this package | Source byte hashes, fixed ledger cutoffs, raw public RPC records, exact method pins and offline checks are included. |

### Claim-by-claim results

| Claim | Disposition | Reason |
| --- | --- | --- |
| Five source-labelled XRP inflows and the closing balance reconcile. | PASS · demonstrated within the captured provider evidence | Raw integer amounts, full returned history, ledger membership and account-state changes agree. |
| No XRP payment left the inspected account through the cutoff. | PASS · bounded observation | No account-authored transaction appears in the 11-record history. This says nothing about later activity or control of its keys. |
| The Ethereum root receipt contains 63 victim-origin Transfer events. | PASS · receipt-level observation | Transaction, successful receipt, block hash and block membership agree. This is not a full token-state replay. |
| The displayed 167,464.247856558836135296 ETH internal transfer was independently replayed. | UNRESOLVED | Etherscan displays it. The public RPC did not supply a usable internal trace. |
| The entire theft has been traced to final beneficial owners. | UNRESOLVED; complete-trace acceptance FAIL | A complete root set, all subsequent branches, cross-chain matches and private custody records are missing. |
| A named intermediary knowingly accepted this theft’s proceeds. | UNRESOLVED | No such person-specific evidence was obtained. A transaction alone does not establish knowledge or consent. |
| The funds were personally controlled or spent by Kim Jong Un. | UNRESOLVED | No direct personal-control or expenditure evidence was obtained. |
| EFMW outperforms conventional tracing methods on this case. | UNRESOLVED; benchmark N/A | No blinded, preregistered comparison against an established tracing baseline was run. |

## 9. Known-method and novelty check

The tracing work uses established public-ledger queries, exact integer accounting, event decoding, source hashing, attribution lists and provenance checks. Those components overlap directly with conventional blockchain forensics. EFMW here supplies a disciplined audit structure and explicit gates. No new de-anonymization result, physical law, superior detection rate or complete illicit-network reconstruction has been demonstrated.

## 10. Minimal next test, frozen in advance

**Target:** reconstruct one independently supplied cross-chain laundering segment from its initial transaction to its destination, without using the destination label to choose the answer.

**Required input:** a chain-qualified root transaction; both chains’ fixed cutoffs; protocol contract identities and event schemas; the public bridge/swap event data; and a withheld, independently established destination. Use integer quantities, explicit fees and any asset-conversion records.

**PASS:** the destination is recovered from the events, all included value reconciles under the declared conversion model, and an independent replay obtains the same branch. **FAIL:** the asserted link conflicts with the protocol events or assigns unrelated funds. **UNRESOLVED:** missing records, unresolved commingling or multiple indistinguishable destinations. Identity and intent remain separate even if the transaction link passes.

## 11. Reproduction and evidence boundary

The accompanying ZIP contains public RPC responses, their request records and SHA-256 hashes; the address-feed snapshot; the normalized event graph; fixed Zoo source pins and licenses; and the audit script. Run `python audit.py` from the extracted directory to reproduce the 12 recorded checks offline. These checks establish internal consistency of the captured evidence, not independent consensus validation.

Website URLs and hashes identify the pages reviewed. Full third-party articles and website HTML are not redistributed. Live pages and address feeds can change. The package preserves the public ledger data required for the bounded calculations.

**Current stopping boundary:** no full-node validation or independent cryptographic inclusion-proof verification; no complete 11-chain graph; no custody-customer mapping; no personal control or knowing-receipt evidence. The full traceback therefore remains UNRESOLVED.

## Reproduction commands and publication record

The [evidence directory](research/efmw-binance-trace-001/README.md) contains the original report, the unchanged 76-file evidence archive, and SHA-256 checksums. From a checkout of this repository:

```sh
cd research/efmw-binance-trace-001
sha256sum -c SHA256SUMS
python -m zipfile -e EFMW-Binance-Traceback-2026-10-30-evidence.zip audit-evidence
cd audit-evidence
sha256sum -c SHA256SUMS
python audit.py
```

The captured package was extracted, its recorded hashes checked, and its audit reproduced offline before publication. Its twelve passing checks concern the captured records and audit behavior. The expected overall outputs remain `full_trace_status: UNRESOLVED` and `complete_trace_acceptance_gate: FAIL`; a passing check that CIRCUS rejects the completeness assertion does not make that assertion pass. The commands above do not retrieve later transactions or update any observation cutoff.

The Markdown edition preserves the original report's eleven analytical sections and evidence limits. The wording “small incoming transfers” avoids inferring whether those payments were solicited. The archived HTML and evidence files are preserved unchanged, and no new ledger retrieval or attribution finding is claimed by this publication step.
