# The TWT research apparatus

**The operating system this programme runs on — the rules, the roles with their deliberately
different information diets, the manuals, the gates and their generators — published beside the
engine it governs, so a reader can audit not only the results but the process that admitted
them.**

## What is here

- **`prompts/RULES_CORE.md`** — the core rules every agent holds (tiers, the honesty spine, the
  commitment budget, verification discipline), each with its motivating incident.
- **`prompts/RULES_BY_ROLE.md`** — role packs and activity blocks.
- **The roles, each defined by its information DIET** — the adversarial reviewer (saturated with
  the derivation), the meta-observer (deliberately starved of it), the coherence keeper
  (saturated with the whole result set), the re-derivation agent (handed only a claim's bare
  statement), the philosopher, the archivist, the removal auditor, the coordinator, and the
  rest — `prompts/*.md`.
- **`prompts/FORMATION_CORE.md`** — the versioned worker-formation prefix.
- **`prompts/manuals/`** — activity manuals (banking, and the probes index conventions).
- **`scripts/`** — the gates and their generators as they actually run: `bank.sh` (the banking
  gate: both test harnesses + the record-invariants check + the RAG ingest + the commit),
  `check_records.py` (the record-invariants gate with its self-test of demonstrated failure
  modes), `gen_negatives_index.py`, `gen_twt_worker_agent.py`, `honesty_telemetry.py`, the
  PDF render/verify pipeline.

The master copies live in the working programme's repository and are synced here at each
release; this directory is the citable public home the papers point to.

## Provenance

This apparatus was previously published as a standalone repository
(`github.com/yaerhf/research-ratchet`), which has since been dissociated into an independent
project. The exact state the TWT papers cited through 2026-08-27 is permanently preserved at
that repository's tag **`twt-apparatus-20260827`**; from 2026-08-27 the apparatus's public home
is this directory, and the working programme's own copies are authoritative for TWT.

An honest caveat the design itself insists on: a ratchet can be emptied. The measured incidents
the rules rest on are recorded in the rule files themselves — each rule carries the failure
that motivated it.
