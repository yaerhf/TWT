#!/usr/bin/env python
"""RECORD-INVARIANTS gate (standing policy, coordinator-directed 2026-08-13).

THE POLICY: load-bearing prose about the tree's state — counts, file structure,
what-runs-what, pointer paths — must be either generated from the tree or PINNED
here as an executable invariant. The suite verifies the mathematics; this gate
verifies the sentences that describe what was executed. Motivating record: the
2026-08-13 keeper round found the engine split's code conserved exactly on three
independent axes while its prose drifted at 26 sites in one commit; earlier
instances of the same class: the phantom-cite discipline (canon §2), the dead
render-guard greps (I-23 round), the five-answer check-count divergence.

RUN: standalone (structural + census invariants; count-total checks are skipped
without arguments) or from bank.sh as gate [2/4]:
    python scripts/check_records.py --main 412 --companion 81
Exit 0 = all invariants hold; exit 1 = the records have drifted from the tree —
fix the documents (or, if a count legitimately moved, update the count-bearing
sites) before banking.

    python scripts/check_records.py --self-test
Runs the PLANTED-DEFECT DEMONSTRATIONS for the 2026-08-24 apparatus checks
(sections 11b(W), 11c, 11d, 11e, 11f) and the 2026-08-25 consolidation pins
(the retired DEBT hatch, the relative premise floor, the standalone-note prompt
pin §7d, the mirror knowledge/-tree divergence sweep §7b(ii)) against text held
in memory — the tree is never mutated — and exits nonzero if any check fails to
fire on its own defect or any control fires on clean text. R2, and the reason it
is a mode rather than a paragraph in a report: a check never SHOWN able to fail
is a phantom cite of the gate class, and a demonstration that lives only in prose
decays silently. RUN BY bank.sh AT GATE [2/4] since 2026-08-25 — before the pin,
the mode was invoked nowhere, which is the same failure it exists to prevent.

TOLERANCE: count-bearing sites may lag the tree by at most DRIFT_TOL between
consolidations (counts are refreshed by counting at consolidation, not at every
bank); beyond that the gate FAILS. Exact-quoted harness totals must be exact.

EXTENDING (the policy's teeth): when a review catches a NEW prose-drift class,
the fix INCLUDES adding its invariant here where mechanizable. A drift class
caught twice in prose is a process failure. Keep every entry keyed to a measured
failure, never speculative; keep this file small enough to read.
"""
import argparse
import ast
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRIFT_TOL = 2  # tightened 5 -> 2 at the 2026-08-21 apparatus audit (U-1): max observed lag over
               # 26 banks and every count-bearing site was 2; the old width let the canon sit
               # wrong for four consecutive banks while the exact-match region self-corrected.

FAILS = []


def _ck(name, cond):
    print(f"  [{'OK ' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)


def _read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.exists() else None


# ---------------------------------------------------------------------------
# APPARATUS PORTS 2026-09-17 (from research-ratchet, on the coordinator's word): pure text
# predicates, each with a planted FIRE case and a silent CONTROL in self_test().
DISPATCH_LOG_REL = "knowledge/ledgers/DISPATCH_LOG.tsv"
DESIGN_WORDS = ("APPROVED-AS-IS", "APPROVED-WITH-AMENDMENTS", "RETURNED")



def _roster_missing(fc_text, on_disk_names):
    """11 (2D demo, 2026-09-17): the standing-ledger roster in FORMATION_CORE must name every
    ledger file on disk — a roster is protective only while complete (TWT_EOM_MAP was
    missed for a whole sweep round). Pure: names vs text."""
    return [n for n in on_disk_names if n not in (fc_text or "")]


def _census_read(text):
    """9 (2D demo): the pinned register census '<n> ruling rows + <m> adjudication fences'
    as a (n, m) pair, or None when the pin is absent."""
    mm = re.search(r"(\d+) ruling rows \+ (\d+) adjudication\s+fences", text or "")
    return (int(mm.group(1)), int(mm.group(2))) if mm else None



# ENDORSEMENT COUNT (2026-09-22, the paper-sync keeper's item 17 — a drift class caught at the sync: the Core
# paper's §1.3 said nine after S5-LOCAL's stamp while seven other live sites still said eight). The truth is the
# number of items in the Core paper's §1.3 list; every live count site must carry the same number.
_NUMWORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
             "ten": 10, "eleven": 11, "twelve": 12}
ENDORSE_SITES = [
    ("knowledge/corpus/TWT_core_paper.md", r"(\w+) further commitments are endorsed as highly plausible", "Core §1.3"),
    ("knowledge/corpus/TWT_core_paper.md", r"one refusal, (\w+) preferred directions,", "Core price paragraph"),
    ("knowledge/corpus/TWT_core_paper.md", r"\*\*plus (\w+) preferred directions,", "Core comparison table"),
    ("knowledge/corpus/TWT_foundational_paper.md", r"(\w+) further commitments are endorsed as highly plausible", "dossier §A.6.3"),
    ("knowledge/corpus/TWT_foundational_paper.md", r"the (\w+) preferred directions \(endorsements, not", "dossier Part A summary"),
    ("knowledge/corpus/TWT_foundational_paper_companion.md", r"Eight as stamped, (\w+) as now standing", "companion ENDORSED bullet"),
    ("knowledge/ledgers/TWT_FAMILY_TREE.md", r"eight directions as stamped, (\w+) standing", "family tree PREFERRED DIRECTIONS"),
    ("knowledge/prompts/FORMATION_CORE.md", r"eight as stamped, (\w+) as now\s+standing", "formation core §0"),
]


def _num(w):
    w = (w or "").strip().lower()
    return int(w) if w.isdigit() else _NUMWORDS.get(w)


def _core_endorsement_items(core_text):
    """the number of ' · '-separated items in the Core paper's §1.3 blockquote list, or None."""
    m = re.search(r"is still a member of the family:\s*\n((?:>.*\n?)+)", core_text or "")
    if not m: return None
    body = " ".join(ln.lstrip("> ").strip() for ln in m.group(1).splitlines())
    return len([x for x in body.split(" · ") if x.strip()])


def _endorsement_count_defects(texts, truth):
    """texts: {rel: text}; returns the sites whose count word is missing or differs from truth. Pure."""
    bad = []
    for rel, pat, label in ENDORSE_SITES:
        m = re.search(pat, texts.get(rel) or "")
        got = _num(m.group(1)) if m else None
        if got != truth: bad.append(f"{label}: {m.group(1) if m else 'MISSING'} vs {truth}")
    return bad

def _census_ok(got, n_rul, n_adj, tol):
    return got is not None and abs(got[0] - n_rul) <= tol and abs(got[1] - n_adj) <= tol


def _dispatch_log_rows(log_text):
    """rows of the dispatch log as dicts (the ratchet header: utc role checker_model
    author_model claim_id verdict verdict_path); comment and header lines skipped."""
    rows = []
    for line in (log_text or "").splitlines():
        if not line.strip() or line.startswith("#") or line.startswith("utc\t"):
            continue
        f = line.split("\t")
        if len(f) < 7:
            continue
        rows.append(dict(utc=f[0], role=f[1], checker=f[2], author=f[3], claim=f[4],
                         verdict=f[5], path=f[6].strip()))
    return rows


def _dispatch_log_missing(log_text, verdict_paths, opened="2026-09-16"):
    """2A: every persisted verdict file dated on/after the log's opening date must
    have a row whose verdict_path points at it (a pointer, never a copy)."""
    logged = {r["path"].replace("\\", "/") for r in _dispatch_log_rows(log_text)}
    missing = []
    for rel in verdict_paths:
        m = re.search(r"(\d{4}-\d{2}-\d{2})", Path(rel).name)
        if not m or m.group(1) < opened:
            continue
        if rel.replace("\\", "/") not in logged:
            missing.append(rel)
    return missing


def _design_verdict_word_defect(text):
    """2F: a design-review verdict carries EXACTLY ONE of the three registered words
    (RUL-134 / C-37-bis), read from its TITLE line and its VERDICT lines — the earliest word on
    each such line is that line's word (so "APPROVED-WITH-AMENDMENTS ... not RETURNED" reads
    as one word); a defect iff no such line carries a word, or the lines disagree."""
    lines = (text or "").splitlines()
    # a VERDICT line is one that BEGINS with the word (after markdown bold / heading / quote marks); a prose line that merely
    # mentions "verdict" is not a candidate (2026-09-18: a design review's prose "why this is not APPROVED-AS-IS" fired the gate)
    cands = ([lines[0]] if lines else []) + [l for l in lines[1:] if l.lstrip(" *#>_").upper().startswith("VERDICT")]
    words = set()
    for l in cands:
        hits = [(l.find(w), w) for w in DESIGN_WORDS if w in l]
        if hits:
            words.add(min(hits)[1])
    return len(words) != 1


def _paths_ledger_defects(text):
    """2C: every FORK header carries a 'last re-ranked YYYY-MM-DD'; every LIVE row has a
    non-empty 'becomes first choice if' cell that is a condition, not a mood word."""
    defects = []
    fork = None
    for line in (text or "").splitlines():
        if line.startswith("## FORK"):
            fork = line
            if not re.search(r"last re-ranked \d{4}-\d{2}-\d{2}", line):
                defects.append("fork without a last-re-ranked date: " + line[:60])
            continue
        if line.startswith("|") and "| LIVE " in line + " ":
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 6:
                defects.append("LIVE row with too few cells: " + line[:60]); continue
            cond = cells[-1]
            if not cond or re.fullmatch(r"(less promising|later|someday|tbd|-|—)\.?", cond, re.I):
                defects.append("LIVE row without a promotion condition: " + cells[0][:40])
    # ---- the three predicates promoted 2026-09-20 (the closure keeper's K14; the class fired three times in prose):
    # (1) within a fork the non-empty ranks are a permutation of 1..n (no duplicates, no gaps);
    # (2) a row whose status cell contains LANDED carries rank '—' (a landed path is not ranked);
    # (3) every P<n>.<m> token in a fork header or in a promotion cell has a row in that fork.
    fork = None; forks = {}
    for line in (text or "").splitlines():
        if line.startswith("## FORK"):
            fork = line; forks[fork] = dict(header=line, ids=set(), ranks=[], rows=[]); continue
        if fork is None or not line.startswith("| P"): continue
        m = re.match(r"\| (P\d+\.\d+[a-z]?) \|", line)
        if not m: continue
        rid = m.group(1); forks[fork]["ids"].add(rid)
        mm = re.search(r" \| (—|\d+) \| ([ABC]) \| ", line)   # the rank | grade | status triple, located by its shape (the path cell may itself contain '|')
        if not mm: defects.append("row without a rank|grade|status triple: " + rid); continue
        rank = mm.group(1); status = line[mm.end():].split(" | ", 1)[0]
        if rank != "—": forks[fork]["ranks"].append((rid, int(rank)))
        if "LANDED" in status and rank != "—": defects.append("a LANDED row carries a rank: " + rid + " rank " + rank)
        promo = line.strip().strip("|").split("|")[-1]
        forks[fork]["rows"].append((rid, promo))
    for fk, d in forks.items():
        rs = sorted(r for _, r in d["ranks"])
        if rs and rs != list(range(1, len(rs) + 1)):
            defects.append("ranks are not a permutation of 1..n in " + fk[:40] + ": " + str([(i, r) for i, r in d["ranks"]]))
        fk_id = re.search(r"FORK (F\d+)", fk); fk_id = fk_id.group(1) if fk_id else ""
        toks = set(re.findall(r"\b(P" + re.escape(fk_id[1:]) + r"\.\d+[a-z]?)\b", d["header"])) if fk_id else set()
        for rid, promo in d["rows"]: toks |= set(re.findall(r"\b(P" + re.escape(fk_id[1:]) + r"\.\d+[a-z]?)\b", promo)) if fk_id else set()
        for tk in sorted(toks - d["ids"]): defects.append("a path token without a row in its fork: " + tk + " in " + fk[:30])
    return defects


# ---- PENDING HUMAN-APPLIED CANON DIFFS (instituted 2026-08-23, RUL-095 execution) ----
# CANON EDITS ARE HUMAN-ONLY. So a structural change to the tree (the engine's family split
# is the motivating case) necessarily leaves CLAUDE.md's count-bearing lines stale until the
# coordinator applies the pre-written diffs. The two bad answers are: fail the gate at every
# bank until he gets to it (which trains people to ignore the gate), or widen the tolerance
# (which hides the debt permanently). Instead: a canon site that disagrees with the tree is
# reported as [PEND] — NOT a failure — but ONLY while a diffs file exists that quotes the
# CURRENT TREE VALUE. Stale the diffs file, or delete it, and the canon sites fail again.
# The allowance cannot outlive the diff that justifies it, and it is loud at every bank.
CANON_DIFF_FILES = [
    "knowledge/audit/engine_split_2026-08-23/CANON_DIFFS_ENGINE_SPLIT_2026-08-23.md",
    # 2026-08-23, the Γ-referent + Layer-A joint banking pass: carries BOTH the §2 D/J
    # referent sentence (the review canon has held open since 2026-08-17, now closed) AND
    # the census/total lines that pass moves. Same allowance, same expiry: the numbers in
    # its §2 must quote the CURRENT tree values or the canon sites fail again.
    "knowledge/audit/gamma_referent_2026-08-23/CANON_DIFF_DJ_NOTE_2026-08-23.md",
]
PENDS = []


def _canon_diff_covers(values):
    """True iff some PROPOSED/UNAPPLIED canon-diff file quotes every tree value given."""
    for rel in CANON_DIFF_FILES:
        text = _read(rel)
        if not text or "UNAPPLIED" not in text:
            continue
        if all(re.search(r"(?<!\d)%d(?!\d)" % v, text) for v in values):
            return rel          # the COVERING file, so the [PEND] line names the right one
    return None


def _ck_canon(name, ok, values):
    """_ck for a HUMAN-ONLY canon site: [PEND] instead of [FAIL] when a live diff covers it."""
    if ok:
        print(f"  [OK ] {name}")
        return
    if _canon_diff_covers(values):
        print(f"  [PEND] {name} — PENDING HUMAN-APPLIED CANON DIFF "
              f"({_canon_diff_covers(values)}); canon is human-only, the diff is written "
              f"and unapplied")
        PENDS.append(name)
        return
    _ck(name, False)


# ======================================================================
# THE APPARATUS PASS (round-4 item 20 + the round's additions, 2026-08-24)
# Five checks, each shipping with a DEMONSTRATED failure mode. The predicates
# below are PURE FUNCTIONS OVER TEXT precisely so `--self-test` can plant a
# defect and watch the check fire without mutating the tree — the R2 rule:
# a check never shown able to fail is a phantom cite of the gate class.
# ======================================================================

# ---- §11b WIDENED: NAMED-PREMISE COVERAGE ----------------------------------
# THE CLASS, and why it is wider than the datum-restatement sweep it grows out
# of. §11b mechanized RUL-097: an entered FAMILY INPUT may not be restated more
# strongly than its register row. Round 4 measured the SAME defect one level up,
# four times in one round, from two independent cold readers: a premise the
# CORPUS carries (a companion row's premise cell) that the PAPER's use-site does
# not carry, so the paper states the result unconditioned and the reader has no
# way to see the condition. The four instances were Nielsen-Ninomiya, the
# lattice topological charge, one-medium universality, and Volovik. That is the
# conditioning-drift class, and it is the general form of the datum class.
#
# THE INVARIANT. Every entry below names a premise carried by a banked row. It
# must resolve to at least ONE paper-side use-site carrying that conditioning
# language, OR carry an explicit `PAPER-EXEMPT <reason>` stamp in its own row.
#
# THE EXTENSION RULE (documented here because a curated registry that nobody
# extends decays into a museum piece): add a row when a premise becomes
# LOAD-BEARING for a paper-side claim — i.e. when a companion row's premise cell
# names a condition that some paper sentence rides. Do NOT add a row for every
# premise cell in Section 13: most imports are cited in the companion only, and
# a registry that fires on all of them would be noise, which is how a gate gets
# ignored. The seed set is the round-4 measurement itself (LATT-π₃, I-22's
# premise (a), I-31's NN hypotheses, R-165's (P-an ∧ P-pg)) plus the premise the
# round added (I-6's elementary-field-RGE validity).
#
# NON-VACUITY, three ways, because a phrase-matching gate is exactly where a
# vacuous pass hides (canon §8a: a tight tolerance on a vacuous check is a tell):
#   (i)  every entry's ROW must be found — a stale ID fails, never skips;
#   (ii) every entry's premise token must appear IN that row — so the registry
#        stays bound to the corpus and cannot drift into describing nothing;
#   (iii) a floor on how many entries resolve by a REAL paper hit (not by an
#        exemption, not by a debt stamp) — if the phrase families go stale the
#        gate says so instead of going quietly green.
PREMISE_PAPERS = ("knowledge/corpus/TWT_core_paper.md",
                  "knowledge/corpus/TWT_foundational_paper.md")
PREMISE_REGISTRY = [
    # (id, row file, row locator, token that must appear IN the row,
    #  paper-side conditioning phrases — any one suffices)
    ("LATT-π₃ (lattice winding is smooth-sector-protected; the strong-twist "
     "local reading is not integer-faithful)",
     "knowledge/corpus/TWT_foundational_paper_companion.md", r"^\| R-143 \|",
     "LATT-π₃", ("smooth sector", "unwinding event")),
    ("I-22 premise (a) (ONE substrate field generates every radiative "
     "correction, so the induced dim-4 coefficient is species-universal)",
     "knowledge/corpus/TWT_foundational_paper_companion.md", r"^\| I-22 \|",
     "ONE substrate field", ("species-universal", "species universal")),
    ("I-31 hypotheses (Nielsen–Ninomiya quantifies over a FREE QUADRATIC "
     "lattice fermion action with a conserved chiral phase)",
     "knowledge/corpus/TWT_foundational_paper_companion.md", r"^\| I-31 \|",
     "quadratic in the fields",
     ("free quadratic fermion action", "quadratic fermion action")),
    ("R-165 (P-an ∧ P-pg) (analyticity of the dispersion kernel in k; the full "
     "point group — the dimension-eight inference rides both)",
     "knowledge/corpus/TWT_foundational_paper_companion.md", r"^\| R-165 \|",
     "(P-an", ("analyticity of the dispersion kernel", "P-an")),
    # Added 2026-08-25 by the R-165 operative-symmetry amendment, under the
    # extension rule above: (P-op) became load-bearing for paper-side claims in
    # the same pass that named it (§B.1.5, §B.6.3, §E.3.5(4), the §E premise
    # table, the VG-6 row). Its shape is the round-4 conditioning-drift class
    # exactly — a theorem proved at one group, quoted for a sector where a
    # smaller group is what the drive leaves intact.
    ("R-165 (P-op) (the symmetry OPERATIVE on the spatial anisotropy sector is "
     "the full point group [1152], not the driven subgroup Stab(e4) [48])",
     "knowledge/corpus/TWT_foundational_paper_companion.md", r"^\| R-165 \|",
     "(P-op)", ("P-op", "operative-symmetry premise",
                "symmetry **operative** on the sector")),
    ("I-6 compositeness premise (elementary-field RGEs valid for a gauge sector "
     "this candidate holds emergent/composite at Λ_L)",
     "knowledge/corpus/TWT_foundational_paper_companion.md", r"^\| I-6 \|",
     "elementary-field",
     ("elementary-field renormalization", "elementary-field RGE",
      "elementary-field running", "held emergent", "emergent / composite",
      "emergent/composite")),
]
# THE FLOOR IS RELATIVE, NOT A CONSTANT (pin, 2026-08-25 consolidation; removal
# audit §3.1). It was `PREMISE_MIN_COVERED = 3` against a 6-entry registry — three
# entries of slack, meaning three could be converted to PAPER-EXEMPT stamps and the
# non-vacuity clause would still go green. And the registry is DESIGNED to grow (the
# extension rule above invites it; one entry was added this window), so the slack
# grows with it: at twelve entries a constant floor of 3 leaves nine. That is the
# worst shape a floor can have — it rots exactly as the structure it guards succeeds.
# Now: at least 60% of the registry must resolve by a REAL paper hit, never fewer
# than 3. Integer ceiling arithmetic (no float rounding at the boundary):
# ceil(3n/5) == (3n + 4) // 5.
PREMISE_MIN_ABS = 3              # the old constant, kept as the small-registry floor
PREMISE_MIN_NUM, PREMISE_MIN_DEN = 3, 5      # 60%


def _premise_floor(n_entries):
    """How many entries must resolve by a real paper hit. Pure — self-tested."""
    return max(PREMISE_MIN_ABS,
               (PREMISE_MIN_NUM * n_entries + PREMISE_MIN_DEN - 1) // PREMISE_MIN_DEN)
# A premise whose paper-side clause is OWED but not yet written is reported
# [DEBT], not [FAIL] — the same shape as the canon-diff allowance above and for
# the same reason: the repair is a paper edit that this pass is fenced out of,
# and failing every bank on it trains people to ignore the gate. The allowance
# is not free: it holds ONLY while a governing record carries a line naming both
# the marker and the premise id, with a reason. Delete the record, or the line,
# and the premise fails again.
PREMISE_DEBT_FILES = [
    "knowledge/audit/external_review_r4_2026-08-24/"
    "APPARATUS_PASS_REPORT_2026-08-24.md",
]
PREMISE_DEBT_MARK = "PAPER-PREMISE-DEBT"


def _premise_status(row_text, phrases, papers_text, debt_text, pid):
    """(status, detail) for one registry entry. Pure — the self-test plants text.

    COVERED  a paper use-site carries the conditioning language
    EXEMPT   the row carries `PAPER-EXEMPT <reason>` (reason >= 20 chars)
    DEBT     a governing record books the owed paper clause (non-fatal, loud)
    UNCOVERED  none of the above -> the check FAILS
    """
    m = re.search(r"PAPER-EXEMPT\s+(.{0,400})", row_text or "")
    if m:
        reason = m.group(1).split("|")[0].strip()
        return (("EXEMPT", reason) if len(reason) >= 20
                else ("UNCOVERED", "PAPER-EXEMPT stamp carries no readable reason"))
    hit = next((p for p in phrases if p.lower() in papers_text.lower()), None)
    if hit:
        return ("COVERED", hit)
    key = pid.split("(")[0].strip()
    for ln in (debt_text or "").splitlines():
        if PREMISE_DEBT_MARK in ln and key.split()[0] in ln and len(ln) >= 60:
            return ("DEBT", ln.strip()[:150])
    return ("UNCOVERED", f"no paper-side site carries any of {list(phrases)}")


# ---- F8: THE ROUND-DECISION ENACTMENT GATE ---------------------------------
# MEASURED FAILURE (round-4 merge, PART C): the round-3 record's
# "branch-independent (enacted regardless)" list had UNENACTED items — the GST
# naming and the "file NN as a named open problem" item — found only because a
# later round happened to re-derive them. The list was not gated by anything
# executable; items were enacted by hand and two were missed.
#
# THE INVARIANT. Every numbered item on a round's APPLY LIST must carry an
# enactment stamp: either the item's own marker says APPLIED/ENACTED, or some
# OTHER record in the same round directory stamps that item number (an apply
# report's per-item table row supplies the locator), or the round records it
# DEFERRED with a readable reason.
#
# SCOPE: rounds >= r4 only. r3's record predates the convention and cannot be
# retro-stamped without rewriting history; grandfathering it is the same inverse
# control the withdrawn-ground sweep uses (history keeps the state it was written
# in). The skip is PRINTED, never silent.
ROUND_GATE_MIN = 4
ROUND_DIR_PAT = re.compile(r"external_review_r(\d+)_")


def _apply_list_items(gov_text):
    """[(item number, marker text)] from a governing record's APPLY LIST."""
    sec = re.search(r"^#+ [^\n]*APPLY LIST[^\n]*$(.*?)(?=^#+ )",
                    gov_text, re.M | re.S)
    if not sec:
        return []
    return [(int(n), mk) for n, mk in
            re.findall(r"^(\d+)\.\s*\*\*\[([^\]]+)\]", sec.group(1), re.M)]


def _item_enacted(num, marker, others):
    """(ok, kind) — is this apply-list item stamped somewhere in the round?"""
    if re.search(r"APPLIED|ENACTED", marker):
        return True, f"marker: [{marker}]"
    for name, text in others:
        m = re.search(r"^\|\s*\*\*%d(\*\*|\()" % num, text, re.M)
        if m:
            row = text[m.start():text.find("\n", m.start())]
            loc = [c.strip() for c in row.split("|")][2:3]
            return True, f"{name} row -> {(loc or ['?'])[0][:60]}"
        d = re.search(r"ITEM\s+%d\b[^\n]{0,40}DEFERRED" % num, text, re.I)
        if not d:
            d = re.search(r"item\s+%d\b[^\n]{0,20}\*\*deferred\*\*" % num, text, re.I)
        if d:
            tail = text[d.start():d.start() + 400]
            if len(tail.strip()) >= 60:
                return True, f"{name}: DEFERRED with reason"
            return False, f"{name}: DEFERRED with no readable reason"
    return False, "no ENACTED/APPLIED stamp and no DEFERRED reason anywhere in the round"


# ---- O8.2: THE ENGINE-LITERAL PARENTHETICAL CHECK --------------------------
# MEASURED FAILURE (round 4, O8): `charge_normalization_anchor_free()` returns
# the counterfactual residue `2c` WITH the scope note "substrate-specific to
# Y_lep/Y_Q = −3". The Core paper quoted `2c ≠ 0` with no normalization named,
# so a reader computing the same object in conventional hypercharge got `−2c/3`
# and read a factor-3 disagreement where there was none. Both computations were
# right; the paper had dropped the engine's own parenthetical.
#
# THE INVARIANT, registry-driven like census_sites: for each curated site, every
# occurrence of the engine literal in that document must have the primitive's
# scope parenthetical — or an explicitly stated normalization — within N lines.
#
# WHY A CURATED REGISTRY AND NOT A BLANKET RULE, said so the design can be
# judged: a blanket sweep for "3/8" was tried first and returns nine hits in the
# dossier that are not Weinberg-angle quotes at all (`(3/16)^{3/8}`,
# `ρ_vac = (3/8πG_N)…`, a catalog line). A gate that cries wolf nine times gets
# switched off. The literals below are chosen to be normalization-DEPENDENT
# engine outputs, which is exactly the class the defect lives in.
#
# ONE TUNING DECISION, recorded because it is the difference between a live
# check and a vacuous one. The first draft accepted the mere WORD "normaliz" in
# the window. The self-test then refused to fire on the reverted §3.1 sentence —
# because the NEXT paragraph happens to say "the free normalization", so the
# word was in view while the normalization itself was not stated. The tokens are
# therefore the normalization NAMED (`Y_lep / Y_Q = −3` / `Y_Q = 1/3`), which is
# what the invariant is actually about. The self-test found this, not review.
LITERAL_SITES = [
    ("Core §3.1 residue counterfactual",
     "knowledge/corpus/TWT_core_paper.md", "2c ≠ 0",
     ("Y_lep / Y_Q = −3", "Y_Q = 1/3"), 3),
    ("Core §3.1 conventional-normalization companion value",
     "knowledge/corpus/TWT_core_paper.md", "2c/3",
     ("Y_lep / Y_Q = −3", "Y_Q = 1/3"), 3),
    ("dossier §C.2.7 residue counterfactual",
     "knowledge/corpus/TWT_foundational_paper.md", "2c ≠ 0",
     ("Y_lep / Y_Q = −3", "Y_Q = 1/3"), 3),
    ("dossier §C.4.5 Weinberg headline",
     "knowledge/corpus/TWT_foundational_paper.md", "= 3/8 = 0.375",
     ("GUT normalization", "unification", "crossing", "at the scale"), 8),
    ("Core §5.3 Weinberg quote",
     "knowledge/corpus/TWT_core_paper.md", "sin²θ_W = 3/8",
     ("at the scale", "crossing", "unification"), 3),
]
# §2.1's repair is a PRESENCE statement rather than a per-occurrence window (the
# section states the normalization once and then uses it throughout), so it is
# checked as such: the section that makes the neutrality bracket vanish must
# name the normalization it is written in.
LITERAL_PRESENCE = [
    ("Core §2.1 states the residue normalization once, for the whole section",
     "knowledge/corpus/TWT_core_paper.md", "3 × 1/3 = 1", "Y_lep / Y_Q = −3"),
    # RUL-133 (coordinator 2026-09-15): the two energy faces carry their own words, COST
    # (outside-frame elastic cost) and RATE (inside-frame rotor rate), so that "energy"
    # cannot drift between them again. Pinned at the three sites that define the rule.
    ("canon §5 carries the COST ≠ RATE energy-face rule with its ruling id",
     "CLAUDE.md", "COST ≠ ROTOR RATE", "RUL-133"),
    ("the formation core §1 names both energy faces by their words (RUL-133)",
     "knowledge/prompts/FORMATION_CORE.md", "COST ≠ ROTOR RATE", "RUL-133"),
    ("the ruling register carries the RUL-133 row naming COST and RATE",
     "knowledge/ledgers/TWT_RULING_REGISTER.md", "| RUL-133 |", "COST ≠ ROTOR RATE"),
]


def _literal_violations(text, literal, tokens, window):
    """Line numbers where `literal` appears with no scope token in view."""
    lines = text.splitlines()
    out = []
    for i, ln in enumerate(lines):
        if literal not in ln:
            continue
        win = "\n".join(lines[max(0, i - window):i + window + 1]).lower()
        if not any(t.lower() in win for t in tokens):
            out.append(i + 1)
    return out


# ---- RUL-103: SHIPPED-CITE RESOLUTION (WARN-only for now) ------------------
# MEASURED FAILURE (round 4, warm phase, TWO reviewers independently): 66
# citations to 36 distinct `knowledge/audit/` paths in the shipped corpus, zero
# resolving in the public repo. The Opus reviewer's sentence: the results ship,
# the process doesn't — against a paper claiming the apparatus is published so a
# reader can audit the process. RUL-103 ruled PUBLISH-ON-CITE: a `knowledge/`
# path cited as the basis of a status in a public-facing artifact qualifies for
# the mirror, quarantine markers preserved.
#
# THE INVARIANT: every `knowledge/` path cited in a SHIPPED artifact resolves in
# the mirror clone, or carries a not-shipped/internal marker near its citing
# line.
#
# WARN-ONLY, DELIBERATELY, with a promotion note. The unresolved set is a QUEUE
# the human curates (publish-on-cite makes citation the trigger, but which
# records go out is a publication decision, not a mechanical one). A gate that
# goes red on a curated queue is a gate that gets bypassed. PROMOTE IT TO FATAL
# once the queue is drained to a stable exempt-marked residue — the promotion is
# a one-word change (`_ck` instead of the print) and should be made the first
# time the residual list is empty at a release.
SHIPPED_ARTIFACTS = [
    # the render_pdf.sh mirror copy list (prose artifacts; the engine files are
    # covered by the mirror-scope pins in section 4) ...
    "knowledge/corpus/TWT_core_paper.md",
    "knowledge/corpus/TWT_foundational_paper.md",
    "knowledge/corpus/TWT_foundational_paper_companion.md",
    "knowledge/corpus/D4_lattice_quartic_isotropy.md",
    "knowledge/ledgers/TWT_NEGATIVES_LEDGER.md",
    "knowledge/ledgers/TWT_FAMILY_TREE.md",
    "knowledge/ledgers/TWT_COMPARATIVE_LEDGER.md",
    "knowledge/reviewer_package/COVER_NOTE.md",
    # ... plus the generated negatives INDEX, which is the reader's entry point
    # into the ledger and cites freely.
    "knowledge/ledgers/TWT_NEGATIVES_INDEX.md",
]
SHIPPED_CITE_PAT = re.compile(r"knowledge/[A-Za-z0-9_./\-]+")
SHIPPED_EXEMPT = ("not shipped", "internal record", "internal-only",
                  "not in the public mirror", "unpublished")


def _shipped_cite_misses(text, resolves, window=2):
    """[(path, line no)] for cited knowledge/ paths that neither resolve nor
    carry a not-shipped marker in view. `resolves` is a callable path -> bool."""
    lines = text.splitlines()
    out = []
    for i, ln in enumerate(lines):
        for raw in SHIPPED_CITE_PAT.findall(ln):
            path = raw.rstrip(".,;:)`'\"")
            if resolves(path):
                continue
            win = "\n".join(lines[max(0, i - window):i + window + 1]).lower()
            if any(m in win for m in SHIPPED_EXEMPT):
                continue
            out.append((path, i + 1))
    return out


# ---- §7d: THE STANDALONE-NOTE COLD-REVIEW PROMPT ---------------------------
# The note-level sibling of §7c, pinned for the same reason and by the same
# shape. MEASURED GAP (removal audit 2026-08-25, §3.6 / structure L2): the
# standalone-send prompt — which produced two of that window's four highest-yield
# reactions — lived ONLY in a dated round directory, with the identical fence as
# the paper prompt ("the prompt is pinned verbatim and minimal: any coaching
# invalidates the measurement") and NO pin at all. `grep` for SEND_INSTRUCTIONS
# across knowledge/prompts/ and scripts/ returned zero hits, so the bootstrap
# path never reached it and a future send could drift with nothing to notice.
#
# THE INVARIANT: the durable routine and the archived send package must quote the
# SAME prompt, byte for byte, and a package must not have used two different
# prompts across its sends (that would make its own two samples incomparable).
STANDALONE_PROMPT_SITES = [
    ("durable routine", "knowledge/prompts/standalone_review_send.md"),
    ("2026-08-25 send package",
     "knowledge/audit/standalone_reviews_2026-08-25/SEND_INSTRUCTIONS.md"),
]
STANDALONE_PROMPT_PAT = re.compile(r"Prompt, verbatim[^\n]*\n\s*>\s*([^\n]+)")


def _verbatim_prompts(text):
    """Every prompt quoted under a `Prompt, verbatim` marker. Pure — self-tested."""
    return [m.group(1).strip() for m in STANDALONE_PROMPT_PAT.finditer(text or "")]


# ---- MIRROR knowledge/ TREE DIVERGENCE (WARN) ------------------------------
# ★ MEASURED INCIDENT, 2026-08-25 (removal audit §1 — the one prevention
# structure found already failing, inside four days of installing it). RUL-103
# published the `knowledge/` tree on the promise that "quarantine/fence markers
# in these files are load-bearing, not decoration" and would be preserved. The
# public copy of `knowledge/reviews/r4_commission_2026-08-24/05_SORKIN_route_memo.md`
# was shipping WITHOUT the 44-line dated quarantine annotation that the working
# copy carries — the memo is the Sorkin arc's cited Authority, so a reader
# following the public pointer took its unverified figures as operative. The
# mechanism: `render_pdf.sh`'s mirror copy list is thirteen FLAT named files and
# `knowledge/` is not among them; the tree was pushed by hand once and NOTHING
# re-copies or re-diffs it, while `git add -A` commits whatever is there. The
# divergence was repaired at mirror commit `0a5a6fb`; this check is what makes
# the next one visible instead of silent.
#
# WARN, NOT FAIL, and the reason is structural rather than lenient: a divergence
# IMMEDIATELY AFTER a ruled working-tree edit is the expected state — the working
# tree is where records are repaired, and republishing is a publication decision
# under RUL-103, which is the human's. So the WARN names the RESYNC DUTY and
# lists the files; it does not block a bank on a duty that belongs to a release.
# (Same reasoning as §7b's between-release-trains suspension, and the same reason
# §11f is WARN-only. If the mirror sync is ever automated at release, this is the
# check to promote to FATAL there — in render_pdf.sh's path, not bank.sh's.)
#
# Files that exist ONLY in the mirror are exempt BY LIST, not by rule: the mirror's
# own `knowledge/README.md` is its MANIFEST and reader fence (structure L4), written
# for the public tree and deliberately absent from the working tree.
MIRROR_KNOWLEDGE_EXEMPT = ["knowledge/README.md"]


def _mirror_divergences(pairs, exempt=()):
    """[(rel, why)] for mirror knowledge/ files that do not match the working tree.

    `pairs` is (rel, mirror_bytes, working_bytes_or_None) — passed in rather than
    read here so the self-test can plant a divergence in memory. Pure.
    """
    out = []
    for rel, mbytes, wbytes in pairs:
        if rel in exempt:
            continue
        if wbytes is None:
            out.append((rel, "in the mirror, absent from the working tree "
                             "and not on the exempt list"))
        elif mbytes != wbytes:
            out.append((rel, "bytes differ from the working-tree twin"))
    return out


def _rul128_offenders(py_files, has_validation_artifact):
    """RUL-128 / RUL-122 cl. 7c predicate over ONE post-fix g8 round: py_files = {name: text}. Fires on any import or call of the
    DEFECTIVE geometric names (min_image3, seed_hedgehog_gen, far_mask_gen, q_expected_gen without the _exact suffix) and on a
    round that touches a geometric instrument (any *_exact name or an INSTRUMENT_VALIDATION reference) without shipping an
    INSTRUMENT_VALIDATION* artifact. Pure; self-tested with a planted round."""
    bad = []
    touches_geometry = False
    for name, text in py_files.items():
        # a DELIBERATE call of a defective name (a failure demonstration, the clause-7c comparison) is allowed when the
        # line carries the marker RUL-128-DELIBERATE; every other occurrence fires
        unmarked = "\n".join(ln for ln in text.splitlines() if "RUL-128-DELIBERATE" not in ln)
        if re.search(r"\b(min_image3|seed_hedgehog_gen|far_mask_gen|q_expected_gen)\b(?!_exact)", unmarked):
            bad.append("%s: imports/calls a DEFECTIVE geometric name (unmarked)" % name)
        if re.search(r"\b(min_image3_exact|far_mask_gen_exact|seed_hedgehog_gen_exact|half_diagonal3)\b", text):
            touches_geometry = True
    if touches_geometry and not has_validation_artifact:
        bad.append("round touches a geometric instrument and ships no INSTRUMENT_VALIDATION* artifact")
    return bad


def _min_image_geometry_probe():
    """RUL-128: run both min-image functions on the two CFW cells and return the maxima against the half-diagonals.
    Imports n2d_lib from its audit directory; returns ok=False (and the gate FAILS) if the library cannot be imported."""
    import sys as _sys
    out = {"ok": False, "exact_max": (0.0, 0.0), "defective_max": (0.0, 0.0), "bound": (0.0, 0.0), "n_wrong": (0, 0)}
    try:
        _p = os.path.join(str(ROOT), "knowledge", "audit", "g8_n2d_bandhost_2026-08-30")
        if _p not in _sys.path: _sys.path.insert(0, _p)
        import n2d_lib as _NL
        from n1_lib import Cell as _Cell
        em, dm, bd, nw = [], [], [], []
        for M in (_NL.CFW16, _NL.CFW16W):
            import warnings as _w
            c = _Cell(M); _, r_e = _NL.min_image3_exact(c); b = _NL.half_diagonal3(c)
            with _w.catch_warnings():
                _w.simplefilter("ignore"); _, r_d = _NL.min_image3(c)          # the DEFECTIVE one, called on purpose
            em.append(float(r_e.max())); dm.append(float(r_d.max())); bd.append(float(b)); nw.append(int((r_d > r_e + 1e-9).sum()))
        out.update(ok=True, exact_max=tuple(em), defective_max=tuple(dm), bound=tuple(bd), n_wrong=tuple(nw))
    except Exception as e:
        out["error"] = repr(e)[:200]
    return out


def self_test():
    """DEMONSTRATED FAILURE MODES for the five checks of the 2026-08-24
    apparatus pass (R2: a check never SHOWN able to fail is a phantom cite of
    the gate class). Each trial plants a defect in a COPY OF THE TEXT and
    asserts the predicate fires — the tree is never mutated, so this is
    repeatable, runs in a second, and is part of the shipped apparatus rather
    than a paragraph in a report claiming a test once happened.

    Every trial pairs a FIRE case with a NOT-FIRE control, because a predicate
    that fires on everything is as useless as one that fires on nothing.

        python scripts/check_records.py --self-test
    """
    print("=" * 70)
    print("  APPARATUS SELF-TEST — planted defects must FIRE, controls must NOT")
    print("=" * 70)
    trials = []

    def trial(name, fired, expect=True):
        ok = bool(fired) == expect
        print(f"  [{'OK ' if ok else 'FAIL'}] {name} "
              f"({'fired' if fired else 'did not fire'}; expected "
              f"{'fire' if expect else 'no fire'})")
        trials.append(ok)

    # --- 0. RUL-128 / RUL-122 cl. 7c: the geometric-instrument predicate (2026-09-06) ----
    trial("RUL-128: a planted round importing the DEFECTIVE min_image3 fires",
          bool(_rul128_offenders({"run.py": "from n2d_lib import min_image3, Cell"}, True)))
    trial("RUL-128: a planted round using min_image3_exact WITHOUT an INSTRUMENT_VALIDATION artifact fires",
          bool(_rul128_offenders({"run.py": "from n2d_lib import min_image3_exact"}, False)))
    trial("RUL-128 control: a DELIBERATE defective call marked RUL-128-DELIBERATE on its line does NOT fire",
          bool(_rul128_offenders({"recon.py": "_, r_def = NL.min_image3(c)   # RUL-128-DELIBERATE: the clause-7c comparison\nfrom n2d_lib import min_image3_exact"}, True)), expect=False)
    trial("RUL-128: the same defective call WITHOUT the marker fires",
          bool(_rul128_offenders({"recon.py": "_, r_def = NL.min_image3(c)\nfrom n2d_lib import min_image3_exact"}, True)))
    trial("RUL-128 control: exact names + the validation artifact do NOT fire",
          bool(_rul128_offenders({"run.py": "from n2d_lib import min_image3_exact, far_mask_gen_exact"}, True)), expect=False)
    trial("RUL-128 control: a round with no geometry at all does NOT fire",
          bool(_rul128_offenders({"run.py": "import numpy as np"}, False)), expect=False)

    # --- 1. named-premise coverage -------------------------------------
    papers = "the family states the result with no condition anywhere."
    st, _ = _premise_status("| I-X | premise: THE PLANTED PREMISE |",
                            ("a conditioning phrase no paper carries",),
                            papers, "", "I-X planted")
    trial("premise coverage: a planted premise with no paper use-site",
          st == "UNCOVERED")
    st, _ = _premise_status("| I-X | premise: THE PLANTED PREMISE |",
                            ("with no condition",), papers, "", "I-X planted")
    trial("premise coverage: CONTROL — the same premise once a paper "
          "sentence carries it", st == "UNCOVERED", expect=False)
    st, _ = _premise_status(
        "| I-X | premise: P | PAPER-EXEMPT companion-only import, never quoted "
        "in either paper body |",
        ("absent",), papers, "", "I-X planted")
    trial("premise coverage: CONTROL — a PAPER-EXEMPT stamp with a reason",
          st == "UNCOVERED", expect=False)
    st, _ = _premise_status("| I-X | premise: P | PAPER-EXEMPT ok |",
                            ("absent",), papers, "", "I-X planted")
    trial("premise coverage: a PAPER-EXEMPT stamp with no readable reason",
          st == "UNCOVERED")

    # --- 2. round-decision enactment gate ------------------------------
    gov = ("## A.3 APPLY LIST — items\n\n"
           "1. **[APPLIED prior pass]** something done.\n"
           "2. **[PROPOSED §8a]** something proposed.\n\n"
           "## A.4 next section\n")
    items = _apply_list_items(gov)
    trial("round gate: the APPLY LIST parses (2 items)", len(items) == 2)
    ok, _ = _item_enacted(2, "PROPOSED §8a", [("apply_report.md", "nothing here")])
    trial("round gate: a proposed item with no enactment stamp anywhere",
          not ok)
    ok, _ = _item_enacted(2, "PROPOSED §8a",
                          [("apply_report.md",
                            "| **2** | `paper.md:120` | what was applied |")])
    trial("round gate: CONTROL — the same item once an apply report stamps it "
          "with a locator", not ok, expect=False)
    ok, _ = _item_enacted(2, "PROPOSED §8a",
                          [("apply_report.md",
                            "## E — ITEM 2, DEFERRED (as instructed)\n"
                            "It is deferred to a separate pass for these "
                            "stated reasons, at length.")])
    trial("round gate: CONTROL — a deferral carrying a readable reason",
          not ok, expect=False)

    # --- 3. engine-literal parenthetical -------------------------------
    # The FIRE case is the ACTUAL pre-repair text of Core §3.1, reverted in a
    # scratch copy: the sentence as it read before the round-4 O8.2 repair.
    fixed = _read("knowledge/corpus/TWT_core_paper.md") or ""
    # RE-KEYED 2026-08-26 (the round-6 restructure rewrote §3.1's counterfactual
    # sentence, so the old anchor "So the identity is broken" no longer exists and
    # the demonstration silently stopped firing — caught by --self-test at the bank
    # gate, which is what the self-test is for). The plant is unchanged in KIND:
    # strip the normalization parenthetical that follows the literal, leaving it bare.
    pre = re.sub(r"(the residue is `2c ≠ 0`) in this paper's normalization.*?written first\.",
                 r"\1.", fixed, flags=re.S)
    _lt = ("Y_lep / Y_Q = −3", "Y_Q = 1/3")
    trial("engine literal: the pre-repair Core §3.1 sentence (reverted in a "
          "scratch copy) leaves `2c ≠ 0` bare",
          pre != fixed and bool(_literal_violations(pre, "2c ≠ 0", _lt, 3)))
    trial("engine literal: CONTROL — the repaired text on the current tree",
          bool(_literal_violations(fixed, "2c ≠ 0", _lt, 3)), expect=False)

    # --- 4. R-159 findability ------------------------------------------
    comp = _read("knowledge/corpus/TWT_foundational_paper_companion.md") or ""
    m = re.search(r"^\| R-159 \|", comp, re.M)
    row = comp[m.start():comp.find("\n", m.start())] if m else ""
    trial("R-159 findability: the row with its anomaly terms stripped",
          any(t not in row.lower().replace("two-branch", "")
              for t in ("anomaly", "two-branch")))
    trial("R-159 findability: CONTROL — the repaired row on the current tree",
          any(t not in row.lower() for t in ("anomaly", "two-branch")),
          expect=False)

    # --- 5. shipped-cite resolution ------------------------------------
    planted = ("The basis for this status is\n"
               "`knowledge/audit/never_published_2026-01-01/RECORD.md`, which "
               "settles it.\n")
    trial("shipped cite: a cited knowledge/ path that resolves nowhere and "
          "carries no marker",
          bool(_shipped_cite_misses(planted, lambda p: False)))
    marked = planted.replace("which settles it.",
                             "which settles it (internal record, not shipped).")
    trial("shipped cite: CONTROL — the same cite once marked not shipped",
          bool(_shipped_cite_misses(marked, lambda p: False)), expect=False)
    trial("shipped cite: CONTROL — the same cite once the path resolves",
          bool(_shipped_cite_misses(planted, lambda p: True)), expect=False)

    # ================= the 2026-08-25 consolidation pins =================
    # Same R2 rule, same shape: each pin is DEMONSTRATED here or it is a claim.

    # --- 6. the DEBT hatch's retirement (removal audit §3.5) ------------
    # The retirement was executed by splitting PREMISE_DEBT_MARK and the premise
    # id across two lines of the governing record. Plant the reflow that re-joins
    # them and watch the status fall back to DEBT — which the new _ck now FAILS on
    # instead of printing.
    _rejoined = ("Booked " + PREMISE_DEBT_MARK + " for I-X planted: the paper "
                 "clause is owed and this line re-joins the marker with the id.")
    st, _ = _premise_status("| I-X | premise: THE PLANTED PREMISE |",
                            ("a conditioning phrase no paper carries",),
                            papers, _rejoined, "I-X planted")
    trial("DEBT hatch: a reflow re-joining the marker and a premise id on ONE "
          "line re-opens the retired allowance (n_debt would go nonzero)",
          st == "DEBT")
    st, _ = _premise_status("| I-X | premise: THE PLANTED PREMISE |",
                            ("a conditioning phrase no paper carries",),
                            papers,
                            "Booked " + PREMISE_DEBT_MARK + " for the premise "
                            "named on the next line, which is how it was retired:"
                            "\nI-X planted — the clause has since been PAID.",
                            "I-X planted")
    trial("DEBT hatch: CONTROL — the retirement as executed (marker and id on "
          "different lines) leaves the allowance closed", st == "DEBT",
          expect=False)

    # --- 7. the relative premise floor (removal audit §3.1) -------------
    # The defect the pin removes is SLACK THAT GROWS WITH THE REGISTRY: under the
    # old constant floor of 3, a 12-entry registry could have nine entries
    # converted to exemption stamps and still go green.
    trial("premise floor: a registry that grows while real coverage stays flat "
          "trips the relative floor (12 entries, 3 real hits)",
          3 < _premise_floor(12))
    trial("premise floor: CONTROL — the old CONSTANT floor never trips on the "
          "same registry (this is the slack the pin removes)",
          3 < PREMISE_MIN_ABS, expect=False)
    trial("premise floor: CONTROL — a fully covered registry passes at any size",
          not (12 >= _premise_floor(12)), expect=False)
    trial("premise floor: CONTROL — the small-registry absolute floor still "
          "binds (3 entries -> floor 3, not 2)", _premise_floor(3) != 3,
          expect=False)

    # --- 8. the standalone-note prompt pin (removal audit §3.6) ---------
    _pkg = ("- **Prompt, verbatim, nothing added:**\n"
            "  > Please review this note carefully.\n")
    _coached = ("- **Prompt, verbatim, nothing added:**\n"
                "  > Please review this note carefully, focusing on whether the "
                "lattice argument holds.\n")
    trial("standalone prompt: a coached prompt in the durable routine drifts "
          "from the send package's string",
          _verbatim_prompts(_coached) != _verbatim_prompts(_pkg))
    trial("standalone prompt: CONTROL — the two files quoting the same string",
          _verbatim_prompts(_pkg) != _verbatim_prompts(_pkg), expect=False)
    trial("standalone prompt: a file with no `Prompt, verbatim` block at all "
          "(the string silently gone)",
          not _verbatim_prompts("Send the note to a cold reviewer.\n"))

    # --- 9. the mirror knowledge/ divergence sweep (removal audit §1) ---
    # The planted case IS the measured incident: a published record whose
    # quarantine annotation is missing from the public copy.
    _quar = b"# route memo\n\n> QUARANTINE: numbers below did not survive.\n\nbody\n"
    _stripped = b"# route memo\n\nbody\n"
    _rel = "knowledge/reviews/r4_commission_2026-08-24/05_SORKIN_route_memo.md"
    trial("mirror tree: a published record shipping WITHOUT its quarantine "
          "annotation (the 2026-08-25 incident, replayed in memory)",
          bool(_mirror_divergences([(_rel, _stripped, _quar)],
                                   MIRROR_KNOWLEDGE_EXEMPT)))
    trial("mirror tree: CONTROL — the same record once re-synced byte-identical",
          bool(_mirror_divergences([(_rel, _quar, _quar)],
                                   MIRROR_KNOWLEDGE_EXEMPT)), expect=False)
    trial("mirror tree: CONTROL — the mirror-only README is exempt BY LIST",
          bool(_mirror_divergences([("knowledge/README.md", b"public fence", None)],
                                   MIRROR_KNOWLEDGE_EXEMPT)), expect=False)
    trial("mirror tree: an unlisted mirror-only file (a published record with no "
          "working-tree source)",
          bool(_mirror_divergences([("knowledge/audit/ghost.md", b"x", None)],
                                   MIRROR_KNOWLEDGE_EXEMPT)))

    # --- 13. APPARATUS PORTS 2026-09-17 -----------------------------------------------
    _lg = "# utc\trole\tchecker_model\tauthor_model\tclaim_id\tverdict\tverdict_path\n" \
          "2026-09-17T18:03\treviewer\topus\tfable\tC4D1\tHOLDS\tknowledge/audit/x/X_VERDICT_REVIEWER_2026-09-17.md\n"
    trial("2A dispatch log: a verdict file with no pointer row fires",
          bool(_dispatch_log_missing(_lg, ["knowledge/audit/x/Y_VERDICT_META_2026-09-17.md"])))
    trial("2A control: the logged verdict file does NOT fire",
          bool(_dispatch_log_missing(_lg, ["knowledge/audit/x/X_VERDICT_REVIEWER_2026-09-17.md"])), expect=False)
    trial("2A control: a verdict dated before the log opened does NOT fire",
          bool(_dispatch_log_missing(_lg, ["knowledge/audit/x/OLD_VERDICT_KEEPER_2026-09-10.md"])), expect=False)
    trial("2F design verdict: prose with none of the three words fires",
          _design_verdict_word_defect("The design looks sound; proceed with care."))
    trial("2F design verdict: two VERDICT lines with different words fires",
          _design_verdict_word_defect("# a design" + chr(10) + "VERDICT: RETURNED" + chr(10) + "..." + chr(10) + "VERDICT (revised): APPROVED-AS-IS"))
    trial("2F control: one VERDICT line naming a second word in negation does NOT fire",
          _design_verdict_word_defect("# a design" + chr(10) + "**VERDICT: APPROVED-WITH-AMENDMENTS. Not RETURNED: the structure is right.**"), expect=False)
    trial("2F control: a PROSE line mentioning the verdict and a second word in negation does NOT fire (2026-09-18)",
          _design_verdict_word_defect("# a design: **APPROVED-WITH-AMENDMENTS**" + chr(10) + "VERDICT: APPROVED-WITH-AMENDMENTS" + chr(10) + "the adverse verdict beside this claim is why this is not APPROVED-AS-IS."), expect=False)
    trial("2F control: exactly one word on the VERDICT line does NOT fire",
          _design_verdict_word_defect("# a design" + chr(10) + "VERDICT: APPROVED-WITH-AMENDMENTS (A1, A2)"), expect=False)
    _pl_bad = "## FORK F9 — a fork (last re-ranked 2026-09-17)" + chr(10) + "| P9.1 | a path | 1 | B | LIVE | not taken because X | less promising |" + chr(10)
    _pl_ok = "## FORK F9 — a fork (last re-ranked 2026-09-17)" + chr(10) + "| P9.1 | a path | 1 | B | LIVE | not taken because X | the t = 60 read prints THIRD-ASYMPTOTE |" + chr(10)
    _pl_nodate = "## FORK F9 — a fork" + chr(10) + _pl_ok.split(chr(10), 1)[1]
    trial("2C paths ledger: a LIVE row whose promotion cell is a mood word fires", bool(_paths_ledger_defects(_pl_bad)))
    trial("2C paths ledger: a fork header without a last-re-ranked date fires", bool(_paths_ledger_defects(_pl_nodate)))
    trial("2C control: a dated fork with a conditioned LIVE row does NOT fire", bool(_paths_ledger_defects(_pl_ok)), expect=False)
    # the three promoted predicates (2026-09-20), each with a planted demonstration
    _pl_dup = "## FORK F9 — a fork (last re-ranked 2026-09-20)" + chr(10) + "| P9.1 | a path | 1 | B | LIVE | not taken because X | the read prints Y |" + chr(10) + "| P9.2 | a path | 1 | B | LIVE | not taken because X | the read prints Z |" + chr(10)
    _pl_gap = "## FORK F9 — a fork (last re-ranked 2026-09-20)" + chr(10) + "| P9.1 | a path | 1 | B | LIVE | not taken because X | the read prints Y |" + chr(10) + "| P9.2 | a path | 3 | B | LIVE | not taken because X | the read prints Z |" + chr(10)
    _pl_landed = "## FORK F9 — a fork (last re-ranked 2026-09-20)" + chr(10) + "| P9.1 | a path | 1 | B | **LANDED 2026-09-20** the words | not taken because X | the read prints Y |" + chr(10)
    _pl_tok = "## FORK F9 — a fork (last re-ranked 2026-09-20: P9.7 is first)" + chr(10) + "| P9.1 | a path | 1 | B | LIVE | not taken because X | it becomes first if P9.3 lands |" + chr(10)
    _pl_ok3 = "## FORK F9 — a fork (last re-ranked 2026-09-20: P9.1 is first)" + chr(10) + "| P9.1 | a path with a | in it | 1 | B | LIVE | not taken because X | it becomes first if P9.2 lands |" + chr(10) + "| P9.2 | a path | — | A | **LANDED 2026-09-20** the words | tried | landed |" + chr(10) + "| P9.3 | a path | 2 | C | LIVE | not taken | the read prints Q |" + chr(10)
    trial("2C paths ledger: duplicate ranks in a fork fire", any("permutation" in d for d in _paths_ledger_defects(_pl_dup)))
    trial("2C paths ledger: a gap in the ranks fires", any("permutation" in d for d in _paths_ledger_defects(_pl_gap)))
    trial("2C paths ledger: a LANDED row with a rank fires", any("LANDED row carries a rank" in d for d in _paths_ledger_defects(_pl_landed)))
    trial("2C paths ledger: a path token without a row fires", any("without a row" in d for d in _paths_ledger_defects(_pl_tok)))
    trial("2C control: a fork with a permutation of ranks, an unranked LANDED row and only rowed tokens does NOT fire", bool(_paths_ledger_defects(_pl_ok3)), expect=False)

    # --- 2D (2026-09-17), first batch: record checks never seen to fire ----------------
    trial("11 roster: a ledger on disk that FORMATION_CORE does not name fires",
          bool(_roster_missing("... `TWT_A.md` · `TWT_B.md` ...", ["TWT_A.md", "TWT_C.md"])))
    trial("11 roster control: every on-disk ledger named does NOT fire",
          bool(_roster_missing("... `TWT_A.md` · `TWT_B.md` ...", ["TWT_A.md", "TWT_B.md"])), expect=False)
    trial("9 census: a pinned count drifted beyond the tolerance fires",
          not _census_ok(_census_read("the register: 131 ruling rows + 4 adjudication fences"), 135, 4, 2))
    trial("9 census: a missing pin fires",
          _census_read("the register has many rows") is None)
    trial("9 census control: a pin within the tolerance does NOT fire",
          not _census_ok(_census_read("134 ruling rows + 4 adjudication fences"), 135, 4, 2), expect=False)

    # --- the endorsement-count invariant (2026-09-22, the paper-sync keeper's item 17) ----------
    _core_ok = "a member of the family:" + chr(10) + "> a · b · c" + chr(10) + chr(10) + "Three further commitments are endorsed as highly plausible"
    trial("endorsement count: the Core list's item count is read from its blockquote", _core_endorsement_items("is still a member of the family:" + chr(10) + "> a · b ·" + chr(10) + "> c" + chr(10)) == 3)
    _txt = {rel: "" for rel, _, _ in ENDORSE_SITES}
    _good = {"knowledge/corpus/TWT_core_paper.md": "Nine further commitments are endorsed as highly plausible; one refusal, nine preferred directions, and **plus 9 preferred directions,",
             "knowledge/corpus/TWT_foundational_paper.md": "Nine further commitments are endorsed as highly plausible; the nine preferred directions (endorsements, not",
             "knowledge/corpus/TWT_foundational_paper_companion.md": "Eight as stamped, nine as now standing",
             "knowledge/ledgers/TWT_FAMILY_TREE.md": "eight directions as stamped, nine standing",
             "knowledge/prompts/FORMATION_CORE.md": "eight as stamped, NINE as now" + chr(10) + "standing"}
    trial("endorsement count control: every site at nine against a nine-item list does NOT fire", bool(_endorsement_count_defects(_good, 9)), expect=False)
    _bad = dict(_good); _bad["knowledge/ledgers/TWT_FAMILY_TREE.md"] = "eight directions as stamped, eight standing"
    trial("endorsement count: ONE site left at eight fires", bool(_endorsement_count_defects(_bad, 9)))
    _miss = dict(_good); _miss["knowledge/corpus/TWT_foundational_paper.md"] = "the list was rewritten"
    trial("endorsement count: a site whose count sentence vanished fires", bool(_endorsement_count_defects(_miss, 9)))

    print("-" * 70)
    if all(trials):
        print(f"  SELF-TEST: {len(trials)}/{len(trials)} demonstrations behaved "
              f"as specified (every check SEEN to fire; every control silent).")
        sys.exit(0)
    print(f"  SELF-TEST: {trials.count(False)} of {len(trials)} demonstrations "
          f"did NOT behave as specified — a check that cannot be shown to fire "
          f"verifies nothing.")
    sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--main", type=int, default=None,
                    help="main-harness printed total (from bank.sh)")
    ap.add_argument("--companion", type=int, default=None,
                    help="companion-harness printed total (from bank.sh)")
    ap.add_argument("--release", action="store_true",
                    help="RELEASE mode: additionally require every calibration-ledger "
                         "RELEASE-BLOCKERS row to be FIXED or WAIVED. Called by "
                         "scripts/render_pdf.sh; NOT by bank.sh (this gate is a release "
                         "gate, not a per-bank gate — see section 12).")
    ap.add_argument("--self-test", action="store_true",
                    help="run the planted-defect demonstrations for the "
                         "2026-08-24 apparatus checks and exit (R2: a check "
                         "never shown able to fail verifies nothing)")
    args = ap.parse_args()
    if args.self_test:
        self_test()

    print("=" * 70)
    print("  RECORD-INVARIANTS gate (prose vs tree; policy 2026-08-13)")
    print("=" * 70)

    # ---- 1. STRUCTURE: the files the records name must exist -------------
    print("structure:")
    for rel in [
        "knowledge/corpus/twt.py", "knowledge/corpus/twt_companion.py",
        "knowledge/corpus/twt_test.py", "knowledge/corpus/twt_companion_test.py",
        # THE FAMILY SPLIT (RUL-093/RUL-095, 2026-08-23): the MAIN engine is now the
        # facade twt.py over two halves. Both halves are pinned here — a mirror or a
        # clone missing one of them has an engine that imports nothing.
        "knowledge/corpus/twt_core.py", "knowledge/corpus/twt_candidate_v3.py",
        "knowledge/audit/engine_split_2026-08-23/CLASSIFICATION_SHEET_2026-08-23.md",
        "CLAUDE.md", "knowledge/audit/SESSION_HANDOFF_2026-07-27.md",
        "knowledge/ledgers/TWT_worklist.md",
        "knowledge/ledgers/TWT_NEGATIVES_LEDGER.md",
        "knowledge/prompts/FORMATION_CORE.md",
        "knowledge/candidates/probes_2026-08-02/ADJUDICATION3_2026-08-12.md",
        "knowledge/audit/engine_split_classification_2026-08-12.md",
        # methodology registers (proposals 1+3 implemented 2026-08-13):
        "knowledge/ledgers/TWT_RULING_REGISTER.md",
        "knowledge/ledgers/TWT_CHECKER_CALIBRATION.md",
        # standing ledgers instituted during the 2026-08 arc (archivist pass 2026-08-18,
        # brief item E-4): these carry live pointers from the canon, the role files and
        # FORMATION_CORE, and had no existence invariant.
        "knowledge/ledgers/TWT_COMPARATIVE_LEDGER.md",
        "knowledge/ledgers/TWT_EDIT_REACTION_LEDGER.md",
        "knowledge/ledgers/TWT_FAMILY_TREE.md",
        # THE THREE-ARTIFACT PACKAGE (relocation leg 2026-08-21). The Core paper is the
        # front-facing entry document; the foundational paper KEEPS its filename and its
        # Part A-E numbering as the instance dossier, so every companion §-cite, engine
        # docstring cite, register site list and revert clause keeps resolving. Both are
        # pinned because the package's readability now depends on both existing.
        "knowledge/corpus/TWT_core_paper.md",
        "knowledge/corpus/TWT_foundational_paper.md",
        "knowledge/corpus/TWT_foundational_paper_companion.md",
    ]:
        _ck(f"exists: {rel}", (ROOT / rel).exists())

    # ---- 2. SPLIT INVARIANTS: two of them, on two axes --------------------
    # (a) 2026-08-13: the MAIN engine never imports the COMPANION. WIDENED 2026-08-23 —
    #     "the MAIN engine" is now three files (facade + two family halves), and a guard
    #     that watched only the facade would pass vacuously.
    # (b) 2026-08-23 (RUL-093/RUL-095): CORE never consumes CANDIDATE. The executable
    #     AST form of this guard lives in twt_test.py (check_twt_algebra) where it can be
    #     run against mutations; here it is checked at the import/grep level so a bank
    #     with a broken engine cannot slip past on a skipped harness.
    print("split invariants:")
    main_files = ("knowledge/corpus/twt.py", "knowledge/corpus/twt_core.py",
                  "knowledge/corpus/twt_candidate_v3.py")
    _ck("the MAIN engine (twt.py + twt_core.py + twt_candidate_v3.py) contains no "
        "'import twt_companion' statement",
        not any(ln.strip().startswith(("import twt_companion", "from twt_companion"))
                for f in main_files for ln in (_read(f) or "").splitlines()))
    core_src = _read("knowledge/corpus/twt_core.py") or ""
    cand_src = _read("knowledge/corpus/twt_candidate_v3.py") or ""

    def _module_names(text):
        out = set()
        for n in ast.parse(text).body:
            if isinstance(n, (ast.FunctionDef, ast.ClassDef)):
                out.add(n.name)
            elif isinstance(n, ast.Assign):
                for t in n.targets:
                    for x in (t.elts if isinstance(t, ast.Tuple) else [t]):
                        if isinstance(x, ast.Name):
                            out.add(x.id)
        return out

    core_names, cand_names = _module_names(core_src), _module_names(cand_src)
    dir_viol = sorted({x.id for x in ast.walk(ast.parse(core_src))
                       if isinstance(x, ast.Name) and x.id in cand_names
                       and x.id not in core_names})
    _ck(f"CORE never consumes CANDIDATE: twt_core.py references no name defined in "
        f"twt_candidate_v3.py (violations: {dir_viol or 'none'})", not dir_viol)
    _ck("twt_core.py contains no 'import twt_candidate_v3' statement",
        not any(ln.strip().startswith(("import twt_candidate_v3", "from twt_candidate_v3"))
                for ln in core_src.splitlines()))
    _ck("twt.py is a FACADE: it defines no primitive of its own and imports both halves",
        not [n for n in ast.parse(_read("knowledge/corpus/twt.py") or "").body
             if isinstance(n, (ast.FunctionDef, ast.ClassDef))]
        and "from twt_core import *" in (_read("knowledge/corpus/twt.py") or "")
        and "from twt_candidate_v3 import *" in (_read("knowledge/corpus/twt.py") or ""))

    # ---- 3. GATE LIVENESS: bank.sh greps match what the harnesses print --
    print("gate liveness (a guard that greps nothing verifies nothing):")
    bank = _read("scripts/bank.sh") or ""
    tmain = _read("knowledge/corpus/twt_test.py") or ""
    tcomp = _read("knowledge/corpus/twt_companion_test.py") or ""
    _ck("bank.sh gates on the MAIN pass-line pattern",
        "ALL [0-9]+ CHECKS PASSED across" in bank)
    _ck("bank.sh gates on the COMPANION pass-line pattern",
        "ALL [0-9]+ COMPANION CHECKS PASSED across" in bank)
    _ck("twt_test.py prints a matching pass line",
        "CHECKS PASSED across" in tmain)
    _ck("twt_companion_test.py prints a matching pass line",
        "COMPANION CHECKS PASSED across" in tcomp)

    # ---- 4. MIRROR SCOPE (RATIFIED, coordinator 2026-08-13): both engines
    # NEW DRIFT CLASS, caught 2026-08-23 by mutating the tree instead of trusting the pin
    # (RUL-095 execution, "seen to fire"): this check used to grep the WHOLE FILE for the
    # filename, so the moment a COMMENT in render_pdf.sh mentioned a file, the pin passed
    # whether or not the `cp` actually copied it — the M6 mutation deleted the twt_core.py
    # copy line and the gate stayed green. A guard that a comment can satisfy verifies
    # nothing. The scope is now the cp COMMAND ITSELF, with comment lines stripped.
    print("mirror scope (ratified: both engines ship):")
    render_raw = _read("scripts/render_pdf.sh") or ""
    _m = re.search(r"\n\s*cp\s(.*?)\"\$MIRROR/\"", render_raw, re.S)
    _ck("render_pdf.sh mirror sync block parses (the `cp ... \"$MIRROR/\"` command)", bool(_m))
    render = "\n".join(ln for ln in (_m.group(1) if _m else "").splitlines()
                       if not ln.strip().startswith("#"))
    for f in ("twt.py", "twt_companion.py", "twt_test.py",
              "twt_companion_test.py",
              # family split 2026-08-23: the facade alone is an empty engine.
              "twt_core.py", "twt_candidate_v3.py",
              # human ruling 2026-08-21: the paper's family-tree pointer must
              # resolve for an external reader, so the tree ships with the mirror.
              "TWT_FAMILY_TREE.md",
              # relocation leg 2026-08-21. TWT_core_paper.md is the front-facing
              # artifact — a mirror without it hands a stranger the dossier as the
              # entry point, which is the reading round 2 reported as an obstacle.
              # TWT_COMPARATIVE_LEDGER.md is the evidence behind the Core paper's §3
              # separator grading; it was promised in the paper and absent from the
              # mirror for two rounds running (N2 U-1), which is exactly the class of
              # omission a pin exists to make impossible to repeat.
              "TWT_core_paper.md", "TWT_COMPARATIVE_LEDGER.md"):
        _ck(f"render_pdf.sh mirror copy list includes {f}", f in render)

    # ---- 5. TOOLING COHERENCE: rag 'code' shorthand covers both engines --
    print("tooling:")
    ragq = _read("rag/query.py") or ""
    _ck("rag/query.py 'code' source shorthand covers the companion engine",
        "twt_companion" in ragq)

    # ---- 6. CENSUS: doc-quoted def counts vs the tree (AST truth) --------
    print("census (AST truth vs count-bearing sites; tol ±%d):" % DRIFT_TOL)

    def _counts(rel):
        tree = ast.parse(_read(rel))
        fns = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
        pub = [n for n in fns if not n.startswith("_")]
        return len(pub)

    # THE MAIN CENSUS AFTER THE FAMILY SPLIT (2026-08-23). "The MAIN engine's public
    # surface" is unchanged as a THING — it is what `import twt` exposes — but it is now
    # spread over two files behind a facade, and the facade itself defines nothing. So the
    # main census is the SUM of the two halves. Counting twt.py alone would report 0 and
    # every count-bearing site would look catastrophically stale; counting the facade's
    # namespace would double-count the star re-exports. Count the halves.
    pub_core = _counts("knowledge/corpus/twt_core.py")
    pub_cand = _counts("knowledge/corpus/twt_candidate_v3.py")
    pub_main = pub_core + pub_cand
    pub_comp = _counts("knowledge/corpus/twt_companion.py")
    _ck(f"the facade defines no public primitive of its own "
        f"(twt.py: {_counts('knowledge/corpus/twt.py')})",
        _counts("knowledge/corpus/twt.py") == 0)

    def _defcount(rel):
        tree = ast.parse(_read(rel))
        return sum(1 for n in tree.body
                   if isinstance(n, (ast.FunctionDef, ast.ClassDef)))

    core_defs = _defcount("knowledge/corpus/twt_core.py")
    cand_defs = _defcount("knowledge/corpus/twt_candidate_v3.py")

    # COMPANION SECTION CENSUS. The companion carries the family cut as an in-file
    # section split (ruled Option C), so its two halves have no module boundary to be
    # counted by — the banner is the boundary and the count is taken across it. Without
    # this pin the section split is prose, and prose drifts (policy 2026-08-13).
    comp_src = _read("knowledge/corpus/twt_companion.py") or ""
    marker = "SECTION CANDIDATE"
    _ck("twt_companion.py carries both family-split section banners",
        "SECTION CORE" in comp_src and marker in comp_src)
    _cut = comp_src.index(marker) if marker in comp_src else len(comp_src)
    _sec_names = lambda t: re.findall(r"^def ([A-Za-z_]\w*)", t, re.M)
    comp_core_defs = len(_sec_names(comp_src[:_cut]))
    comp_cand_defs = len(_sec_names(comp_src[_cut:]))
    comp_core_pub = sum(1 for n in _sec_names(comp_src[:_cut]) if not n.startswith("_"))
    comp_cand_pub = sum(1 for n in _sec_names(comp_src[_cut:]) if not n.startswith("_"))
    _ck(f"companion section census sums to the file census "
        f"({comp_core_defs} + {comp_cand_defs} = {comp_core_defs + comp_cand_defs} defs; "
        f"{comp_core_pub} + {comp_cand_pub} = {comp_core_pub + comp_cand_pub} public vs "
        f"{pub_comp})", comp_core_pub + comp_cand_pub == pub_comp)
    print(f"  [ - ] family split: MAIN {pub_main} public = {pub_core} CORE + {pub_cand} "
          f"CANDIDATE; COMPANION {pub_comp} public (section-split in place)")

    # SITE REGISTRY — count-bearing prose. Adding a count to a document means
    # adding a row here (or generating the sentence from the tree instead).
    census_sites = [
        ("CLAUDE.md", r"MAIN engine\*\* \(~(\d+) public primitives",
         pub_main, "canon §6 main census"),
        ("CLAUDE.md", r"COMPANION\s+engine\*\* \(~(\d+) public primitives",
         pub_comp, "canon §6 companion census"),
        ("CLAUDE.md", r"MAIN/CORE: the FAMILY-level primitives \(~(\d+) public",
         pub_core, "canon Pointers CORE census"),
        ("CLAUDE.md", r"MAIN/CANDIDATE: the V3-instance primitives \(~(\d+) public",
         pub_cand, "canon Pointers CANDIDATE census"),
        ("knowledge/reviewer_package/COVER_NOTE.md",
         r"engine: (\d+) public primitives \((\d+) main \+ (\d+) companion\)",
         (pub_main + pub_comp, pub_main, pub_comp), "COVER_NOTE census"),
        # FAMILY-SPLIT CENSUS SITES (new 2026-08-23). The split creates a second thing
        # prose can be wrong about — not "how many primitives" but "how many on each
        # side" — and that is exactly the count a reader uses to judge what the family
        # earns without the candidate. Both pins were SEEN TO FIRE before going green.
        ("knowledge/reviewer_package/COVER_NOTE.md",
         r"split family/instance (\d+) CORE \+ (\d+) CANDIDATE",
         (pub_core, pub_cand), "COVER_NOTE family-split census"),
        ("knowledge/corpus/TWT_foundational_paper_companion.md",
         r"split (\d+) CORE \((\d+) public [^)]*\) \+ (\d+) CANDIDATE \((\d+) public",
         (core_defs, pub_core, cand_defs, pub_cand),
         "Section 3 family-split census"),
        ("knowledge/corpus/TWT_foundational_paper_companion.md",
         r"(\d+) defs in SECTION CORE \((\d+) public\) and (\d+) in SECTION CANDIDATE "
         r"\((\d+) public\)",
         (comp_core_defs, comp_core_pub, comp_cand_defs, comp_cand_pub),
         "Section 3 companion section-split census"),
    ]
    for rel, pat, truth, label in census_sites:
        text = _read(rel)
        m = re.search(pat, text) if text else None
        if not m:
            _ck(f"{label}: pattern found in {rel}", False)
            continue
        got = tuple(int(g) for g in m.groups())
        want = truth if isinstance(truth, tuple) else (truth,)
        ok = len(got) == len(want) and all(
            abs(g - w) <= DRIFT_TOL for g, w in zip(got, want))
        label_txt = f"{label}: {got} vs tree {want} (tol ±{DRIFT_TOL})"
        (_ck_canon(label_txt, ok, want) if rel == "CLAUDE.md"
         else _ck(label_txt, ok))

    # ---- 7. TOTALS: doc-quoted check counts vs the live harness totals ---
    if args.main is None or args.companion is None:
        print("totals: SKIPPED (no --main/--companion; bank.sh supplies them)")
    else:
        print("totals (live harness prints vs count-bearing sites):")
        m_, c_, t_ = args.main, args.companion, args.main + args.companion
        total_sites = [
            ("CLAUDE.md",
             r"ALL CHECKS PASSED\" \((\d+) as of", (m_,), "canon §6 main total"),
            ("CLAUDE.md",
             r"ALL COMPANION CHECKS PASSED\" \((\d+) as of", (c_,), "canon §6 companion total (R-198 orphan 2: was ungated)"),
            ("knowledge/reviewer_package/COVER_NOTE.md",
             r"(\d+) checks \((\d+) main \+ (\d+) companion\)",
             (t_, m_, c_), "COVER_NOTE totals"),
            ("knowledge/ledgers/TWT_worklist.md",
             r"\*\*(\d+) MAIN \+ (\d+) COMPANION = (\d+) as of",
             (m_, c_, t_), "worklist header totals"),
            ("knowledge/audit/SESSION_HANDOFF_2026-07-27.md",
             r"\*\*(\d+) MAIN \+ (\d+) COMPANION = (\d+), both green\*\*",
             (m_, c_, t_), "handoff table totals"),
            ("knowledge/prompts/FORMATION_CORE.md",
             r"two suites \((\d+) \+ (\d+) = (\d+)",
             (m_, c_, t_), "FORMATION_CORE map totals"),
        ]
        for rel, pat, want, label in total_sites:
            text = _read(rel)
            m = re.search(pat, text) if text else None
            if not m:
                _ck(f"{label}: pattern found in {rel}", False)
                continue
            got = tuple(int(g) for g in m.groups())
            ok = len(got) == len(want) and all(
                abs(g - w) <= DRIFT_TOL for g, w in zip(got, want))
            label_txt = f"{label}: {got} vs live {want} (tol ±{DRIFT_TOL})"
            (_ck_canon(label_txt, ok, want) if rel == "CLAUDE.md"
             else _ck(label_txt, ok))

    # ---- 7b. VERBATIM REVIEWER-FACING PASS LINES ------------------------
    # NEW DRIFT CLASS (external-review loop, iteration 1, 2026-08-13). Distinct
    # from section 7: these sites do not *describe* a total, they QUOTE the
    # harness output and instruct a cold reviewer to compare it against what
    # their own terminal prints. DRIFT_TOL therefore does NOT apply — a lagging
    # quote here is not a stale count, it is a costly signal that fails in the
    # reviewer's hands at the exact moment it is meant to land. Measured
    # failure: COVER_NOTE §0 said "ALL 81 COMPANION CHECKS PASSED" against a
    # tree printing 87, and the public mirror README said 464 against 414 —
    # both on the release path, both invisible to every prior gate (the render
    # script's mirror-README guard only WARNS, and it greps the main pattern
    # only). The mirror is what a reviewer actually clones, so it is checked
    # here too; it lives outside ROOT and is skipped when absent.
    if args.main is None or args.companion is None:
        print("verbatim pass lines: SKIPPED (no --main/--companion)")
    else:
        print("verbatim pass lines (exact — quoted for a reviewer to compare):")
        quote_sites = [
            (ROOT / "knowledge/reviewer_package/COVER_NOTE.md",
             "COVER_NOTE §0"),
            (Path(os.environ.get("TWT_MIRROR_DIR",
                                 Path.home() / "Claude/Projects/twt-engine"))
             / "README.md", "mirror README"),
        ]
        for path, label in quote_sites:
            if not path.exists():
                print(f"  [SKIP] {label}: not present at {path}")
                continue
            text = path.read_text(encoding="utf-8")
            # REFERENT FIX (keeper closing-round collision 1, 2026-08-24): the
            # mirror README's true referent is the MIRROR'S OWN shipped engine,
            # not the working tree's live print. Between release trains the two
            # legitimately diverge (measured: the README was synced to a live 491
            # and published while the mirror's engine printed 490 — a
            # wrong-referent sync, publicly wrong either way it is read). When
            # the mirror's harness files differ from the working tree's, the
            # exact-match demand is suspended with a loud note; when they are
            # byte-identical, exact match binds as before.
            mirror_diverges = False
            if label == "mirror README":
                for _hf in ("twt_test.py", "twt_companion_test.py"):
                    _lp = ROOT / "knowledge/corpus" / _hf
                    _mp = path.parent / _hf
                    if _lp.exists() and _mp.exists() and \
                            _lp.read_bytes() != _mp.read_bytes():
                        mirror_diverges = True
                if mirror_diverges:
                    print(f"  [ - ] {label}: mirror harness differs from the "
                          f"working tree (between release trains) — the README "
                          f"must match the MIRROR's own print, exact-vs-live "
                          f"suspended; the next release sync re-binds it")
            for pat, want, kind in [
                (r"ALL (\d+) CHECKS PASSED across (\d+) modules",
                 args.main, "main"),
                (r"ALL (\d+) COMPANION CHECKS PASSED across (\d+) modules",
                 args.companion, "companion"),
            ]:
                m = re.search(pat, text)
                if not m:
                    _ck(f"{label}: quotes the {kind} pass line", False)
                    continue
                if mirror_diverges:
                    continue
                _ck(f"{label}: {kind} pass line quotes {m.group(1)}, "
                    f"harness prints {want} (must be EXACT)",
                    int(m.group(1)) == want)

    # ---- 7b(ii). THE MIRROR'S knowledge/ TREE vs THE WORKING TREE ----------
    # See the _mirror_divergences header for the measured 2026-08-25 incident
    # (a shipped record whose quarantine annotation was not in the public copy),
    # the mechanism (nothing re-copies knowledge/ at release), and why this WARNs
    # rather than fails.
    _mk = Path(os.environ.get("TWT_MIRROR_DIR",
                              Path.home() / "Claude/Projects/twt-engine"))
    _mkk = _mk / "knowledge"
    if not _mkk.exists():
        print(f"  [SKIP] mirror knowledge/ tree not present at {_mkk} "
              f"(set TWT_MIRROR_DIR) — divergence sweep needs the published tree")
    else:
        _pairs = []
        for _p in sorted(_mkk.rglob("*")):
            if not _p.is_file():
                continue
            _rel = _p.relative_to(_mk).as_posix()
            _w = ROOT / _rel
            _pairs.append((_rel, _p.read_bytes(),
                           _w.read_bytes() if _w.is_file() else None))
        _div = _mirror_divergences(_pairs, MIRROR_KNOWLEDGE_EXEMPT)
        print(f"mirror knowledge/ tree ({len(_pairs)} published files) vs the "
              f"working tree:")
        if _div:
            print(f"  [WARN] {len(_div)} published file(s) DIVERGE from the "
                  f"working tree. RESYNC DUTY: the public copy is what a reader "
                  f"following a cited pointer gets, and quarantine/fence markers "
                  f"in these files are load-bearing — re-copy them at the next "
                  f"sync (RUL-103; republishing is the human's call, so this "
                  f"WARNs). Expected transiently right after a ruled working-tree "
                  f"edit; a divergence that survives a release is the 2026-08-25 "
                  f"incident class:")
            for _rel, _why in _div:
                print(f"    - {_rel}  ({_why})")
        else:
            print(f"  [OK ] every published knowledge/ file is byte-identical to "
                  f"its working-tree twin (exempt-by-list, mirror-only: "
                  f"{', '.join(MIRROR_KNOWLEDGE_EXEMPT)})")

    # ---- 7c. THE COLD-REVIEW PROMPT: routine text == what the sampler sends
    # PREVENTIVE, not reactive (the only entry here that is). The external-review
    # loop's own fence is "the reviewer prompt stays verbatim and minimal: any
    # coaching in the prompt invalidates the measurement" — so the prompt is the
    # single highest-stakes string in the loop, it lives in two files that must
    # agree, and a drift between them voids every sample SILENTLY: the routine
    # would document one instrument while the sampler shipped another, and the
    # logged request body would look perfectly well-formed. Six lines to pin.
    routine = _read("knowledge/prompts/external_review_loop.md")
    sampler = _read("knowledge/audit/external_review_2026-08-13/send_cold_review.py")
    if routine and sampler:
        print("cold-review prompt (routine text == sampler payload):")
        m = re.search(r'PROMPT = "([^"]+)"', sampler)
        _ck("sampler defines a PROMPT string", bool(m))
        if m:
            _ck(f"routine quotes the sampler's prompt verbatim: {m.group(1)!r}",
                m.group(1) in routine)

    # ---- 7d. THE STANDALONE-NOTE PROMPT: durable routine == what was sent ---
    # See the STANDALONE_PROMPT_SITES header for the class and the measured gap.
    print("standalone-note cold-review prompt (durable routine == send package, "
          "byte for byte):")
    _sp = {}
    for _label, _rel in STANDALONE_PROMPT_SITES:
        _txt = _read(_rel)
        _ck(f"{_label}: {_rel} exists", _txt is not None)
        _got = _verbatim_prompts(_txt)
        _ck(f"{_label}: quotes at least one `Prompt, verbatim` block "
            f"({len(_got)} found in {_rel})", bool(_got))
        _ck(f"{_label}: every quoted prompt in the file is the SAME string "
            f"(a package that sent two different prompts made its own samples "
            f"incomparable) — {sorted(set(_got))!r}", len(set(_got)) <= 1)
        _sp[_label] = _got[0] if _got else None
    _a, _b = (_sp.get(STANDALONE_PROMPT_SITES[0][0]),
              _sp.get(STANDALONE_PROMPT_SITES[1][0]))
    _ck(f"the durable routine ({STANDALONE_PROMPT_SITES[0][1]}) and the send "
        f"package ({STANDALONE_PROMPT_SITES[1][1]}) quote the IDENTICAL prompt "
        f"— routine {_a!r} vs package {_b!r} (any coaching drift between them "
        f"voids every sample silently)", _a is not None and _a == _b)

    # ---- 8. POINTER RESOLUTION: paths the canon/records rely on ----------
    print("pointers:")
    for src, rel in [
        ("canon bootstrap step 2", "knowledge/audit/SESSION_HANDOFF_2026-07-27.md"),
        ("FORMATION_CORE §5 record", "knowledge/candidates/probes_2026-08-02/ADJUDICATION_2026-08-03.md"),
        ("FORMATION_CORE §5 record", "knowledge/candidates/probes_2026-08-02/ADJUDICATION2_2026-08-03.md"),
        ("FORMATION_CORE §5 record", "knowledge/candidates/probes_2026-08-02/ADJUDICATION3_2026-08-12.md"),
        # (probe-dir INDEX rows replaced 2026-08-21 by the GENERATED form below — the
        # archivist observed the hard-coded family was itself the enumeration-drift class:
        # a new probes_* dir silently escaped the invariant until someone added a row.)
        ("canon Pointers (ruling register)", "knowledge/ledgers/TWT_RULING_REGISTER.md"),
        ("canon Pointers (checker calibration)", "knowledge/ledgers/TWT_CHECKER_CALIBRATION.md"),
        # archivist pass 2026-08-18 (brief E-4): the arc's other standing ledgers are
        # pointed at from live prose but were never pointer-checked.
        ("canon §2 (RUL-048 commitment budget)", "knowledge/ledgers/TWT_FAMILY_TREE.md"),
        ("coordinator role file", "knowledge/ledgers/TWT_EDIT_REACTION_LEDGER.md"),
        ("philosopher role file", "knowledge/ledgers/TWT_COMPARATIVE_LEDGER.md"),
    ]:
        _ck(f"{src} -> {rel}", (ROOT / rel).exists())
    # GENERATED probe-dir INDEX invariant (2026-08-21): every probes_*/ directory carries
    # an INDEX.md — the archivist role's power (7), now enumerated from the tree itself.
    probe_dirs = sorted(p for p in (ROOT / "knowledge/candidates").glob("probes_*") if p.is_dir())
    missing_idx = [p.name for p in probe_dirs if not (p / "INDEX.md").exists()]
    _ck(f"every probes_* dir carries an INDEX.md ({len(probe_dirs)} dirs; missing: "
        f"{missing_idx or 'none'})", not missing_idx)
    # the citing prose must actually NAME the path it is credited with (pointer liveness,
    # same failure shape as the canon Pointers block below: a pointer nobody writes down
    # is not a pointer):
    for citer, path in [
        ("CLAUDE.md", "knowledge/ledgers/TWT_FAMILY_TREE.md"),
        ("knowledge/prompts/coordinator_agent.md",
         "knowledge/ledgers/TWT_EDIT_REACTION_LEDGER.md"),
        ("knowledge/prompts/philosopher_ledger_agent.md",
         "knowledge/ledgers/TWT_COMPARATIVE_LEDGER.md"),
    ]:
        src_text = _read(citer) or ""
        _ck(f"{citer} names {path}", path in src_text)
    # the canon POINTERS BLOCK must actually NAME the two registers (pointer liveness,
    # scoped to the fenced block per keeper S-1 — a whole-file grep goes vacuous the
    # moment other canon sections also mention the registers):
    canon = _read("CLAUDE.md") or ""
    mp = re.search(r"## Pointers\s*```(.*?)```", canon, re.S)
    pointers_block = mp.group(1) if mp else ""
    _ck("CLAUDE.md Pointers fenced block found", bool(pointers_block))
    for reg in ("TWT_RULING_REGISTER.md", "TWT_CHECKER_CALIBRATION.md"):
        _ck(f"CLAUDE.md Pointers block names {reg}", reg in pointers_block)

    # ---- 8b. RUL-120 CLAUSE 2 (2026-09-01): EVERY NUMERIC LITERAL IN A ROUND
    # RECORD'S "REGISTERED CONDITION" COLUMN MUST APPEAR IN THAT ROUND'S FROZEN
    # PREREGISTRATION.
    # The measured case that forced this: N3b's prereg froze control (c) at
    # 1e-6; every script coded 1e-5; and the L1's own control table printed
    # 1e-5 in the *registered condition* column, inside a section asserting
    # "thresholds as frozen, none moved". A moved bar described as unmoved is
    # invisible to every other gate here — but it is exactly mechanisable, and
    # this is the cheap half of RUL-120.
    print("RUL-120 cl.2 — registered-condition literals vs the frozen prereg:")
    import glob as _glob
    _lit = re.compile(r"\d+(?:\.\d+)?[eE][-+]?\d+")
    _rounds = 0
    _bad = []
    for _pre in _glob.glob("knowledge/audit/*/PREREGISTRATION_FROZEN.md"):
        _dir = os.path.dirname(_pre)
        _pretext = _read(_pre) or ""
        for _l1 in _glob.glob(os.path.join(_dir, "*L1*.md")):
            _txt = _read(_l1) or ""
            _in_tbl = False
            _col = None
            for _line in _txt.splitlines():
                if "|" not in _line:
                    _in_tbl = False
                    continue
                _cells = [c.strip() for c in _line.strip().strip("|").split("|")]
                _low = [c.lower() for c in _cells]
                if any("registered condition" in c for c in _low):
                    _in_tbl = True
                    _col = next(i for i, c in enumerate(_low)
                                if "registered condition" in c)
                    _rounds += 1
                    continue
                if _in_tbl and _col is not None and len(_cells) > _col:
                    for _m in _lit.findall(_cells[_col]):
                        if _m not in _pretext:
                            _bad.append("%s: %r not in the frozen prereg"
                                        % (os.path.basename(_l1), _m))
    _ck("every 'registered condition' literal appears in its frozen prereg "
        "(%d tables scanned; offenders: %s)"
        % (_rounds, "; ".join(_bad[:4]) or "none"), not _bad)

    # ---- 8c. RUL-122 CLAUSE 2 (2026-09-01): EVERY REGISTERED CONTROL SHIPS A
    # DEMONSTRATED FAILURE MODE, OR THE ROUND RECORDS IT VOID.
    # Six vacuous checks in six rounds. N3d's own frozen prereg carried the
    # prose clause "any control whose response is fixed by an identity is not a
    # control" and the round then built its Q1 discriminator in violation of
    # it. The prose half of this guard has now demonstrably failed once at the
    # only moment it mattered; this is the executable half. Enforcement is
    # opt-in by registration so that stopped rounds predating the ruling are
    # not retro-broken -- future rounds append to the set.
    print("RUL-122 cl.2 - demonstrated failure modes for registered controls:")
    _RUL122_ROUNDS = ["knowledge/audit/g8_n3d_bank_2026-09-01",
                      "knowledge/audit/g8_n3e_generic_2026-09-01",
                      "knowledge/audit/g8_n3f_shortwave_2026-09-02"]
    _fm_bad = []
    for _rd_ in _RUL122_ROUNDS:
        _logs = [f for f in (os.listdir(_rd_) if os.path.isdir(_rd_) else [])
                 if f.endswith(".log")]
        _all = "".join((_read(os.path.join(_rd_, f)) or "") for f in _logs)
        # RUL-122 cl.2 (generalised at R-197): the round must carry, in a committed log,
        # EITHER an exhibited failure mode ("CAN FAIL: True" / "FAILURE MODE EXHIBITED")
        # for its controls OR a VOID accounting for a control that has none.
        if not _logs:
            _fm_bad.append("%s: no committed *.log at all" % _rd_)
            continue
        _fm = ("CAN FAIL: True" in _all) or ("FAILURE MODE EXHIBITED" in _all)
        _void = "VOID" in _all
        if not (_fm or _void):
            _fm_bad.append("%s: no exhibited failure mode and no VOID accounting "
                           "in any committed log" % _rd_)
    _ck("every RUL-122 round ships a demonstrated failure mode or a VOID "
        "record (%d round(s); offenders: %s)"
        % (len(_RUL122_ROUNDS), "; ".join(_fm_bad) or "none"), not _fm_bad)

    # ---- 8d. RUL-122 CLAUSE 3 (2026-09-02, post-R-197): THE FOUR-FIELD CONTROL
    # TEMPLATE. N3f banked its headline through a control whose two arms were vacuous
    # by construction (accept-arm coefficients exactly zero; reject arm fixed by
    # dimension counting) and read back a dt rule that was a constant of the dial.
    # Clause 3 makes every registered control name four fields. The checker is
    # self-tested on a planted complete and a planted incomplete block, so an empty
    # enforcement set cannot make this gate vacuous; enforcement is by glob on N4+
    # rounds that carry a frozen prereg (a scoping directory is not yet a round).
    print("RUL-122 cl.3 - four-field control template (self-tested; enforced on frozen g8_n4_* preregs):")
    _T_FIELDS = ("ACCEPT ARM", "REJECT ARM", "VACUITY CONSTRUCTION", "IN-RUN FAILURE MODE")
    def _rul122_template(text):
        blk = text.find("CONTROLS (RUL-122 template)")
        if blk < 0:
            return False, ["no 'CONTROLS (RUL-122 template)' block"]
        body = text[blk:]
        miss = [f for f in _T_FIELDS if f not in body]
        return not miss, miss
    _good = "## CONTROLS (RUL-122 template)\n- C1 x\n  ACCEPT ARM: a\n  REJECT ARM: b\n  VACUITY CONSTRUCTION: c\n  IN-RUN FAILURE MODE: d"
    _bad = "## CONTROLS (RUL-122 template)\n- C1 x\n  ACCEPT ARM: a\n  REJECT ARM: b"
    _ck("cl.3 checker accepts the planted complete block", _rul122_template(_good)[0])
    _ck("cl.3 checker rejects the planted incomplete block (missing %s)" % _rul122_template(_bad)[1],
        not _rul122_template(_bad)[0])
    _ck("cl.3 template file exists (knowledge/audit/PREREG_CONTROL_TEMPLATE.md)",
        (ROOT / "knowledge/audit/PREREG_CONTROL_TEMPLATE.md").exists())
    _t_bad = []
    for _d in sorted(_glob.glob(os.path.join(str(ROOT), "knowledge", "audit", "g8_n4_*"))):
        _pre = [f for f in os.listdir(_d) if f.startswith("PREREGISTRATION")]
        if not _pre:
            continue
        # RUL-122 clause 4 (R-198): PER FILE - every PREREGISTRATION* file (freeze or amendment)
        # must itself carry the block; an amendment that re-cuts a control cannot inherit the
        # freeze's fields by concatenation.
        for f in _pre:
            _ok, _miss = _rul122_template(_read(os.path.join("knowledge/audit", os.path.basename(_d), f)) or "")
            if not _ok:
                _t_bad.append("%s/%s: %s" % (os.path.basename(_d), f, _miss))
    _ck("every frozen N4+ prereg carries the four-field template (offenders: %s)" % (_t_bad or "none"),
        not _t_bad)

    # ---- 8e. RUL-122 CLAUSE 5 (2026-09-03, R-199): an amendment that DEFERS / DELETES / DROPS a dial
    # named in a frozen control's arms must restate that control inside its own CONTROLS block.
    # (Track 2's Amendment 1 deferred m5 = 3, the arm C4's reject arm ran on, unnoticed.)
    print("RUL-122 cl.5 - deferred dials named in frozen control arms are restated (self-tested):")
    def _arm_tokens(frozen_text):
        blk = frozen_text.find("CONTROLS (RUL-122 template)")
        if blk < 0:
            return {}
        out = {}; cur = None
        for line in frozen_text[blk:].splitlines():
            s = line.strip()
            m = re.match(r"- (C\d+)\b", s)
            if m:
                cur = m.group(1); continue
            if cur and ("ACCEPT ARM" in s or "REJECT ARM" in s):
                for tok in re.findall(r"(?:m\u2085|m5|\u03c1|rho|\u03b3_d|gd|c|\u03a9\u2080|Om0)\s*=\s*[0-9.]+", s):
                    out.setdefault(re.sub(r"\s+", "", tok), set()).add(cur)
        return out
    def _cl5_check(frozen_text, amend_text):
        bad = []
        if not re.search(r"DEFER|DELET|DROP", amend_text, re.I):
            return bad
        blk = amend_text.find("CONTROLS (RUL-122 template)"); ablk = amend_text[blk:] if blk >= 0 else ""
        for tok, ctrls in _arm_tokens(frozen_text).items():
            # the dial must match as a NUMBER, not as a prefix ("rho=1" is not "rho=1e6" - the false positive
            # this gate fired on Track 1a's Amendments 2/3, whose control arms were explicitly UNCHANGED)
            if re.search(re.escape(re.sub(r"\s+", "", tok)) + r"(?![0-9.eE])", re.sub(r"\s+", "", amend_text)):
                for cname in ctrls:
                    if not re.search(r"- %s\b" % cname, ablk):
                        bad.append("%s (dial %s) not restated" % (cname, tok))
        return bad
    _fz = "## CONTROLS (RUL-122 template)\n- C4 x\n  ACCEPT ARM: a\n  REJECT ARM: the m5 = 3 arm must scale\n  VACUITY CONSTRUCTION: c\n  IN-RUN FAILURE MODE: d"
    _am_bad = "the m5 = 3 arm is DEFERRED\n## CONTROLS (RUL-122 template)\nfields as frozen"
    _am_good = "the m5 = 3 arm is DEFERRED\n## CONTROLS (RUL-122 template)\n- C4 x\n  REJECT ARM: re-cut to the m5 = 1 arm"
    _ck("cl.5 checker flags the planted amendment that defers a control's dial without restating it (%s)" % _cl5_check(_fz, _am_bad), bool(_cl5_check(_fz, _am_bad)))
    _ck("cl.5 checker accepts the planted amendment that restates the control", not _cl5_check(_fz, _am_good))
    _c5_bad = []
    for _d in sorted(_glob.glob(os.path.join(str(ROOT), "knowledge", "audit", "g8_n4_*"))):
        _fzp = os.path.join(_d, "PREREGISTRATION_FROZEN.md")
        if not os.path.exists(_fzp):
            continue
        _fzt = _read(os.path.join("knowledge/audit", os.path.basename(_d), "PREREGISTRATION_FROZEN.md")) or ""
        for f in sorted(os.listdir(_d)):
            if f.startswith("PREREGISTRATION_AMENDMENT"):
                _b = _cl5_check(_fzt, _read(os.path.join("knowledge/audit", os.path.basename(_d), f)) or "")
                # Track 2's Amendment 1 is the EXHIBITED failure of this class: recorded VOID at R-199, not re-cut
                if _b and not (os.path.basename(_d) == "g8_n4_track2_2026-09-03" and f == "PREREGISTRATION_AMENDMENT_1.md"):
                    _c5_bad.append("%s/%s: %s" % (os.path.basename(_d), f, _b))
    _ck("no N4+ amendment defers a dial named in a frozen control's arms without restating it (the Track 2 Amendment 1 exhibit excepted; offenders: %s)" % (_c5_bad or "none"), not _c5_bad)

    # ---- 8f. RUL-122 CLAUSE 6 (2026-09-04, R-200): every numeric bar in an ACCEPT/REJECT ARM line of a
    # frozen prereg names its source and regime as "(bar: ...)", and the IN-RUN field is never "none"/"n/a".
    # Enforced on rounds whose directory date is AFTER 2026-09-04 (five bars mis-set in the Branch B freeze).
    print("RUL-122 cl.6 - numeric bars in control arms carry a (bar: ...) grounding; IN-RUN never 'none' (self-tested):")
    def _cl6_check(frozen_text):
        bad = []; blk = frozen_text.find("CONTROLS (RUL-122 template)")
        if blk < 0:
            return bad
        cur = None
        for line in frozen_text[blk:].splitlines():
            s = line.strip(); m = re.match(r"- (C\d+)\b", s)
            if m:
                cur = m.group(1); continue
            if cur and (s.startswith("ACCEPT ARM") or s.startswith("REJECT ARM")):
                if re.search(r"[<>\u2264\u2265]\s*[0-9]|\bwithin\b|\bat least\b|\bat most\b", s) and "(bar:" not in s:
                    bad.append("%s: %s has a numeric bar with no (bar: ...) grounding" % (cur, s.split(":")[0]))
            if cur and s.startswith("IN-RUN FAILURE MODE") and re.match(r"IN-RUN FAILURE MODE:\s*(none|n/a|-)\b", s, re.I):
                bad.append("%s: IN-RUN FAILURE MODE reads none" % cur)
        return bad
    _fz6_bad = "## CONTROLS (RUL-122 template)\n- C1 x\n  ACCEPT ARM: drift <= 1e-9 over 1 tu\n  REJECT ARM: rises > 0\n  VACUITY CONSTRUCTION: c\n  IN-RUN FAILURE MODE: none"
    _fz6_good = "## CONTROLS (RUL-122 template)\n- C1 x\n  ACCEPT ARM: drift <= 1e-9 over 1 tu (bar: R-199 C1 at dt 2e-4, same cell, same cadence)\n  REJECT ARM: rises > 0 (bar: any rise; the force placement exhibits 10 per 0.1 tu at c = 12)\n  VACUITY CONSTRUCTION: c\n  IN-RUN FAILURE MODE: a rise flags INVALID"
    _ck("cl.6 checker flags the planted ungrounded bar and the 'none' IN-RUN field (%s)" % _cl6_check(_fz6_bad), len(_cl6_check(_fz6_bad)) == 2)
    _ck("cl.6 checker accepts the planted grounded block", not _cl6_check(_fz6_good))
    _c6_bad = []
    for _d in sorted(_glob.glob(os.path.join(str(ROOT), "knowledge", "audit", "g8_n4_*"))):
        _dm = re.search(r"_(\d{4}-\d{2}-\d{2})$", os.path.basename(_d))
        if not _dm or _dm.group(1) < "2026-09-04" or os.path.basename(_d) == "g8_n4_track2b_2026-09-04":
            continue                                                       # rounds frozen before the clause are exempt (Branch B, frozen the same day before the clause, by name)
        for f in sorted(os.listdir(_d)):
            if f.startswith("PREREGISTRATION_FROZEN"):
                _b = _cl6_check(_read(os.path.join("knowledge/audit", os.path.basename(_d), f)) or "")
                if _b:
                    _c6_bad.append("%s/%s: %s" % (os.path.basename(_d), f, _b))
    _ck("every prereg frozen after 2026-09-04 grounds its numeric bars and names an in-run failure (offenders: %s)" % (_c6_bad or "none"), not _c6_bad)

    # ---- 8g. RUL-122 CLAUSE 7 (2026-09-06, R-201): (i) a prereg frozen from 2026-09-07 on carries an INVARIANCE record
    # (every criterion observable tested under the flow's banked symmetry group); (ii) "R_half ... rad" is refused in the
    # corpus and ledgers (R_half is a radius in lattice units; the class recurred at R-198, R-199 and the Track 1b freeze).
    print("RUL-122 cl.7 - invariance record on new freezes; R_half is not an angle:")
    _c7_bad = []
    for _d in sorted(_glob.glob(os.path.join(str(ROOT), "knowledge", "audit", "g8_n4_*"))):
        _dm = re.search(r"_(\d{4}-\d{2}-\d{2})$", os.path.basename(_d))
        if not _dm or _dm.group(1) < "2026-09-06":
            continue
        for f in sorted(os.listdir(_d)):
            if f.startswith("PREREGISTRATION_FROZEN"):
                _ft = _read(os.path.join("knowledge/audit", os.path.basename(_d), f)) or ""
                if "CONTROLS (RUL-122 template)" in _ft and "INVARIANCE" not in _ft:
                    _c7_bad.append("%s/%s: no INVARIANCE record" % (os.path.basename(_d), f))
                if "CONTROLS (RUL-122 template)" in _ft:
                    _blk = _ft[_ft.find("CONTROLS (RUL-122 template)"):]
                    _nc = len(re.findall(r"^- C\d+\b", _blk, re.M)); _nr = len(re.findall(r"^\s*REFERENT:", _blk, re.M))
                    if _nr < _nc:
                        _c7_bad.append("%s/%s: %d controls but %d REFERENT lines (RUL-127)" % (os.path.basename(_d), f, _nc, _nr))
    _ck("every prereg frozen from 2026-09-06 on carries an INVARIANCE record and a REFERENT line per control (RUL-122 cl. 7 / RUL-127; offenders: %s)" % (_c7_bad or "none"), not _c7_bad)
    _rh_bad = []
    for _rel in ("knowledge/corpus/TWT_foundational_paper.md", "knowledge/corpus/TWT_core_paper.md", "knowledge/corpus/TWT_foundational_paper_companion.md") + tuple("knowledge/ledgers/" + x for x in os.listdir(os.path.join(str(ROOT), "knowledge", "ledgers")) if x.endswith(".md")):
        _tx = _read(_rel) or ""
        for _m in re.finditer(r"R_half.{0,40}?\brad\b", _tx):
            if "unit corrected" not in _tx[_m.start():_m.end() + 80] and "not rad" not in _tx[_m.start():_m.end() + 80]:
                _rh_bad.append("%s: %r" % (_rel, _tx[_m.start():_m.end()]))
    _ck("no corpus/ledger sentence calls R_half an angle ('rad' within 40 chars; offenders: %s)" % (_rh_bad[:3] or "none"), not _rh_bad)

    # ---- 8h. RUL-128 (2026-09-06, R-202): GEOMETRIC INSTRUMENTS SHIP A PLANTED-GEOMETRY CHECK. (i) the recorded
    # defect is re-measured at every bank: n2d_lib.min_image3 (DEFECTIVE, kept for reproducibility) must still exceed the
    # half-diagonal on CFW16W while min_image3_exact must not - the demonstration that the check can fail is the defect
    # itself; (ii) no g8 round directory dated 2026-09-07 or later may import the defective name.
    print("RUL-128 - planted-geometry check on the min-image instrument; new rounds use the exact function:")
    _g = _min_image_geometry_probe()
    _ck("min_image3_exact stays within the half-diagonal on CFW16 and CFW16W (max %.2f / %.2f vs bounds %.2f / %.2f)"
        % (_g["exact_max"][0], _g["exact_max"][1], _g["bound"][0], _g["bound"][1]),
        _g["ok"] and _g["exact_max"][0] <= _g["bound"][0] + 1e-9 and _g["exact_max"][1] <= _g["bound"][1] + 1e-9)
    _ck("the DEFECTIVE min_image3 still fires the check on both cells (max %.2f / %.2f > the bounds; %d / %d sites too large) - the recorded defect is re-measured, not remembered"
        % (_g["defective_max"][0], _g["defective_max"][1], _g["n_wrong"][0], _g["n_wrong"][1]),
        _g["ok"] and _g["defective_max"][0] > _g["bound"][0] and _g["defective_max"][1] > _g["bound"][1])
    _c8_bad = []
    for _d in sorted(_glob.glob(os.path.join(str(ROOT), "knowledge", "audit", "g8_*"))):
        _dm = re.search(r"_(\d{4}-\d{2}-\d{2})$", os.path.basename(_d))
        if not _dm or _dm.group(1) < "2026-09-06" or os.path.basename(_d) in ("g8_n4_track1b2_2026-09-06",):
            continue                      # rounds frozen BEFORE the fix (round 2 imports the defective names legitimately; frozen)
        _files = {f: (_read(os.path.join("knowledge/audit", os.path.basename(_d), f)) or "") for f in sorted(os.listdir(_d)) if f.endswith(".py")}
        _has_val = any(f.startswith("INSTRUMENT_VALIDATION") for f in os.listdir(_d))
        _c8_bad += ["%s/%s" % (os.path.basename(_d), b) for b in _rul128_offenders(_files, _has_val)]
    _ck("no g8 round frozen after the fix (2026-09-06 on, round 2 excepted) imports a DEFECTIVE geometric name, and every such round touching a geometric instrument ships INSTRUMENT_VALIDATION* (RUL-128 / RUL-122 cl. 7c; offenders: %s)" % (_c8_bad or "none"), not _c8_bad)

    # ---- 8i. DOCKET #0b (coordinator-directed 2026-09-06, executed 2026-09-07): THE CORE PAPER CARRIES CONDITIONS, NOT
    # CONFESSIONS. Measured motivation: about nine in ten external critiques open with "by the paper's own admission" quoting
    # a caveat without the condition that came with it. The pass rewrote every self-critique-register sentence of
    # TWT_core_paper.md as a condition attached, in the same sentence, to the claim it qualifies (companion G.17 lists them
    # verbatim). This clause keeps it from drifting back: a short pattern list of the register, and "remains open" is refused
        # unless the same sentence carries its conditioning ("given" / "rides" / "conditional on"). Self-tested on a planted pair.
    # WHEN THIS FIRES: a refused sentence is RE-CAST as a condition on the claim it qualifies, never deleted; companion G.17
    # records any sentence removed rather than re-cast (the keeper's latent item L1, 2026-09-07 - the cheapest way to satisfy
    # a red gate is to delete the condition, and that is the one move the docket forbids).
    print("DOCKET #0b - the Core paper carries conditions, not confessions (self-tested):")
    _CONF_PATTERNS = ("we have not", "is a weakness", "we do not claim", "the honest", "honestly", "by our own admission",
                      "by the paper's own admission", "not a hedge", "we would rather", "this paper does not claim",
                      "said at its truest", "worth naming")
    _COND_WORDS = ("given", "rides", "riding", "conditional on")
    def _confessions(text):
        txt = re.sub(r"`[^`]*`", " CODE ", text or ""); txt = re.sub(r"\*+", "", txt)
        out = []
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])|\n\s*\n|\n(?=[-|#>])", txt):
            low = " ".join(s.split()).lower()
            if not low:
                continue
            if any(p in low for p in _CONF_PATTERNS) or ("remains open" in low and not any(c in low for c in _COND_WORDS)):
                out.append(low[:90])
        return out
    _ck("#0b checker fires on the planted confession ('we have not derived the count of three; it remains open')",
        bool(_confessions("We have not derived the count of three; it remains open.")))
    _ck("#0b checker accepts the same fact as a condition ('the count of three rides the identification ... remains open given it')",
        not _confessions("The count of three rides the generation-is-a-quaternion-unit identification, and its dynamical selection remains open given that identification."))
    _c0b = _confessions(_read("knowledge/corpus/TWT_core_paper.md") or "")
    _ck("no sentence of TWT_core_paper.md is in the self-critique register (DOCKET #0b gate; offenders: %s)" % (_c0b[:3] or "none"), not _c0b)


    # ---- 8j. GS-3 (2026-09-09, the keeper's item 11 - a drift class caught at THREE banked sites): the canted vacuum's
    # Gamma-gapped modes are NOT gapped modes - "two Goldstone modes and four gapped" / "(2 gapless + 4 gapped)" is a
    # twisted-frame Gamma count read as a mode count; the lab frame has six exact Goldstones (R-189 [9]). Any such sentence
    # must carry the frame qualifier (Gamma / Gamma / twisted) or the six-count in the same sentence. Self-tested. ----------
    print("GS-3 drift class - 'Gamma-gapless vs Goldstone' (self-tested):")
    _GG_PAT = re.compile(r"\b(two|2)\s+(goldstone\s+modes?|gapless)\b[^.\n|]{0,80}\b(four|4)\s+gapped\b", re.I)
    def _gamma_goldstone_slips(text):
        out = []
        for m in _GG_PAT.finditer(text or ""):
            s = text[max(0, m.start() - 160): m.end() + 160]
            if not re.search(r"Γ|Gamma|twisted|six|SIX|6 exact|six exact", s):
                out.append(m.group(0)[:70])
        return out
    _ck("GS-3 checker fires on the planted 'the canted vacuum's two Goldstone modes and four gapped ones soften it'",
        bool(_gamma_goldstone_slips("The value is an idealization; the canted vacuum's two Goldstone modes and four gapped ones soften it.")))
    _ck("GS-3 checker accepts the qualified form ('2 Gamma-gapless + 4 Gamma-gapped in the twisted frame - six Goldstones')",
        not _gamma_goldstone_slips("The count is 2 Gamma-gapless + 4 Gamma-gapped in the twisted frame - six Goldstones in the lab frame."))
    _gg = []
    for _f in ("knowledge/corpus/TWT_foundational_paper.md", "knowledge/corpus/TWT_core_paper.md", "knowledge/corpus/TWT_foundational_paper_companion.md", "knowledge/corpus/twt_candidate_v3.py", "knowledge/corpus/twt_core.py"):
        _gg += ["%s: %s" % (_f.split("/")[-1], x) for x in _gamma_goldstone_slips(_read(_f) or "")]
    _ck("no banked sentence reads the canted vacuum's Gamma count as a Goldstone count without the frame qualifier (offenders: %s)" % (_gg[:3] or "none"), not _gg)

        # ---- 8k. GS-6 (2026-09-09, coordinator-directed - THE STATIC-FACE TRAP): the canted vacuum's anisotropy sentences
    # (the stiffness split / ratio / birefringence / sidereal residual read off the static Hessian) must carry the FACE word
    # ('static face' / 'driven face' / 'static reading' / 'STATIC-FACE') within the sentence's neighbourhood, because on the
    # driven face the carrier detunes the hybridization behind them (GS-6a). Anchored on twelve banked sites (four at GS-6a, eight more from the face sweep). Self-tested. ----
    print("GS-6 drift class - 'static face vs driven face' (self-tested):")
    _FACE_SITES = [("knowledge/corpus/TWT_foundational_paper.md", r"What the canting changes[^\n]{0,400}?the shape of the six soft branches"),
                   ("knowledge/corpus/TWT_foundational_paper.md", r"up to 68 % in the squared speed along a lattice axis"),
                   ("knowledge/corpus/TWT_foundational_paper.md", r"the canted spiral's space-fixed residual"),
                   ("knowledge/corpus/TWT_foundational_paper_companion.md", r"GS-4 RIDER \(2026-09-09, keeper item 14"),
                   ("knowledge/corpus/TWT_foundational_paper.md", r"spread from about 4 to about 12\.3"),
                   ("knowledge/corpus/TWT_foundational_paper.md", r"The quadratic order, stated honestly"),
                   ("knowledge/corpus/TWT_foundational_paper.md", r"stiffness splitting is polarization-dependent"),
                   ("knowledge/corpus/TWT_foundational_paper_companion.md", r"\| R-174 \| \*\*THE SIX-BAND MAGNON STIFFNESS SPECTRUM"),
                   ("knowledge/corpus/TWT_foundational_paper_companion.md", r"K_long = √38·J ≠ K_⊥` on the canted vacuum"),
                   ("knowledge/corpus/TWT_foundational_paper_companion.md", r"reproduces textbook spiral linear spin-wave theory"),
                   ("knowledge/ledgers/TWT_NEGATIVES_LEDGER.md", r"## N70 — "),
                   ("knowledge/corpus/twt_candidate_v3.py", r"def induced_G_from_linear_face_band")]
    def _face_slips(text, pat):
        out = []
        for m in re.finditer(pat, text or ""):
            s = text[max(0, m.start() - 250): m.end() + 350]
            if not re.search(r"static face|driven face|static reading|STATIC-FACE|STATIC face", s, re.I): out.append(m.group(0)[:60])
        return out
    _ck("GS-6 checker fires on the planted 'the split is up to 68 % in the squared speed along a lattice axis, an exposure'",
        bool(_face_slips("The canting sets the split: up to 68 % in the squared speed along a lattice axis, an exposure of the framework.", r"up to 68 % in the squared speed along a lattice axis")))
    _ck("GS-6 checker accepts the labelled form ('... along a lattice axis, on the static face of the linear problem')",
        not _face_slips("up to 68 % in the squared speed along a lattice axis, on the static face of the linear problem", r"up to 68 % in the squared speed along a lattice axis"))
    _fs = []
    for _f, _pat in _FACE_SITES:
        _txt = _read(_f) or ""
        if not re.search(_pat, _txt): _fs.append("%s: anchor missing (%s)" % (_f.split("/")[-1], _pat[:40]))
        _fs += ["%s: %s" % (_f.split("/")[-1], x) for x in _face_slips(_txt, _pat)]
    _ck("every banked canted-vacuum anisotropy site carries its face word (offenders: %s)" % (_fs[:3] or "none"), not _fs)

    # ---- 9. REGISTER CENSUS (keeper S-2, under the RUL-024 policy): row counts in the
    # ruling register vs the count-bearing prose sites ------------------------------
    print("register census:")
    reg_text = _read("knowledge/ledgers/TWT_RULING_REGISTER.md") or ""
    n_rul = len(re.findall(r"^\| RUL-\d", reg_text, re.M))   # \d excludes the header's RUL-ID
    n_adj = len(re.findall(r"^\| ADJ-F", reg_text, re.M))
    _ck(f"ruling register parses: {n_rul} RUL rows, {n_adj} ADJ-F rows",
        n_rul > 0 and n_adj > 0)
    for rel, label in [
        ("knowledge/ledgers/TWT_worklist.md", "worklist register counts"),
        ("knowledge/audit/SESSION_HANDOFF_2026-07-27.md", "handoff register counts"),
    ]:
        text = _read(rel) or ""
        got = _census_read(text)
        if got is None:
            _ck(f"{label}: pattern found in {rel}", False)
            continue
        ok = _census_ok(got, n_rul, n_adj, DRIFT_TOL)
        _ck(f"{label}: {got} vs tree ({n_rul}, {n_adj}) (tol ±{DRIFT_TOL})", ok)

    # ---- 10. RECORD-ID UNIQUENESS ---------------------------------------
    # NEW DRIFT CLASS (archivist pass 2026-08-18, promoted under RUL-024 / canon §2's
    # extension duty). The class was caught TWICE in prose, which the policy calls a
    # process failure, and both misses were invisible to every prior gate:
    #   (i)  Import-Registry ID `I-23` named TWO different rows — Collins et al. 2004
    #        (companion §13.1) and the mass→weight chain (§13.2) — while a dozen sites
    #        cited "I-23" by number, so every one of those citations was ambiguous. The
    #        registry's entire excision discipline (13.4: Used-at = blast radius, revert
    #        clause) is keyed to the ID, so a duplicated ID is not cosmetic: it makes the
    #        blast radius uncomputable. Fixed by renumbering Collins to I-28.
    #   (ii) companion Section 3 View A carried TWO byte-identical `B_minus_L_anomaly`
    #        rows, so the table's own row count disagreed with its primitive count.
    # An ID that names two rows names neither. Checked on every ID-bearing record.
    print("record-id uniqueness (an ID that names two rows names neither):")
    comp = _read("knowledge/corpus/TWT_foundational_paper_companion.md") or ""

    def _dups(seq):
        seen, dup = set(), []
        for x in seq:
            if x in seen and x not in dup:
                dup.append(x)
            seen.add(x)
        return dup

    imp_ids = re.findall(r"^\| (I-\d+) \|", comp, re.M)
    d = _dups(imp_ids)
    _ck(f"companion Section 13 import-registry IDs unique ({len(imp_ids)} rows; "
        f"duplicates: {d or 'none'})", not d and bool(imp_ids))

    i0 = comp.find("\n## View A ")
    i1 = comp.find("\n### View A.")
    if i0 == -1 or i1 == -1 or i1 <= i0:
        _ck("companion View A section located", False)
        va_rows = []
    else:
        va_rows = [ln.split("|")[1].strip() for ln in comp[i0:i1].splitlines()
                   if ln.startswith("| ") and not ln.startswith("|---")
                   and not ln.startswith("| Primitive")]
        d = _dups(va_rows)
        _ck(f"companion View A primitive rows unique ({len(va_rows)} rows; "
            f"duplicates: {d or 'none'})", not d and bool(va_rows))

    # NB the `[a-z]?` suffix form is real — RUL-014b exists; a regex without it silently
    # skips that row, which is the vacuous-guard class §3 exists to prevent.
    reg_ids = re.findall(r"^\| (RUL-\d+[a-z]?) \|", reg_text, re.M)
    d = _dups(reg_ids)
    _ck(f"ruling-register RUL IDs unique ({len(reg_ids)} rows; "
        f"duplicates: {d or 'none'})", not d and bool(reg_ids))

    # The family tree's branch-node IDs: unique AND contiguous from V3-1. The tree's node
    # COUNT is a quantity other records quote (and it legitimately runs ahead of a dated
    # stamping tally — V3-11 was added after the RUL-047 stamping, which is why the tally
    # is NOT compared against it here); what is mechanizable, and what protects the count
    # from becoming meaningless, is that the IDs themselves form a clean run.
    tree_text = _read("knowledge/ledgers/TWT_FAMILY_TREE.md") or ""
    v3 = [int(n) for n in re.findall(r"^\| V3-(\d+) \|", tree_text, re.M)]
    _ck(f"family-tree V3 node IDs unique and contiguous V3-1..V3-{len(v3)} "
        f"(found {sorted(v3)})",
        bool(v3) and sorted(v3) == list(range(1, len(v3) + 1)))

    # ---- 10b. COMPANION SECTION-3 COUNT-BEARING PROSE --------------------
    # Promotion candidate handed over by the Phase-0 leg (its report §C, M-7 item (i)):
    # View A's own row count had drifted by 7 before anyone counted, and NOTHING pinned
    # it. These three sentences describe the tree and are now generated-checkable.
    print("companion Section 3 self-description (tol ±%d):" % DRIFT_TOL)
    for pat, truth, label in [
        (r"The table below lists the\s*\n?(\d+) load-bearing-primitive rows",
         len(va_rows), "View A row count"),
        # the Δ list is backtick-delimited entries; count only the list lines (those that
        # BEGIN with a backtick), never the surrounding prose, which also uses backticks.
        (r"The following (\d+) entries \(counted",
         sum(len(re.findall(r"`([A-Za-z_][A-Za-z0-9_*]*)`", ln))
             for ln in comp[comp.find("\n### View A."):
                            comp.find("\n## View B")].splitlines()
             if ln.startswith("`") and (ln.endswith(",") or ln.endswith("`"))),
         "View A.Δ entry count"),
        (r"MAIN: \d+ module-level defs = (\d+) public", pub_main,
         "Section 3 MAIN public census"),
        (r"COMPANION: \d+ defs = (\d+) public", pub_comp,
         "Section 3 COMPANION public census"),
    ]:
        m = re.search(pat, comp)
        if not m:
            _ck(f"{label}: pattern found in the companion", False)
            continue
        got = int(m.group(1))
        _ck(f"{label}: {got} vs tree {truth} (tol ±{DRIFT_TOL})",
            abs(got - truth) <= DRIFT_TOL)

    # ---- 10c. THE ℤ×ℤ CITE INVARIANT (mis-cite class, SECOND catch) ------
    # NEW DRIFT CLASS, promoted per the record-invariants policy (canon §2: "a drift
    # class caught twice in prose is a process failure"), on the coherence keeper's
    # recommendation (axiom arc 2026-08-23, disposition D3a).
    #
    # THE CLASS is the MIS-cite, and it is worth separating from the phantom cite: the
    # supporting primitive EXISTS and is suite-checked, so the claim is engine-backed and
    # merely mis-pointed — which is exactly why no gate saw it. `pi3_S3_integer_completion`
    # computes ONE ℤ (the lepton-sector π₃(S³) and the baryon integer-completion facts) and
    # contains no chiral factorization; the ℤ×ℤ is computed by
    # `pi3_orientation_class_two_windings`. Catch 1: R-002's cite set, repaired by the
    # 2026-08-18 state-space pass. Catch 2: R-052 — whose headline IS the ℤ×ℤ claim — was
    # one row past that sweep and kept the wrong cite for five days.
    #
    # FORM. The keeper proposed the prohibitive form ("no such row may cite
    # `pi3_S3_integer_completion`"). Negative-tested here before adoption: that form FIRES
    # on R-002, which is a CORRECT row — it cites both primitives with each one's scope
    # spelled out, which is the shape the repair should encourage, not forbid. So the
    # invariant is implemented in the REQUIRING direction — a row claiming the ℤ×ℤ must
    # cite the primitive that computes the ℤ×ℤ — which catches the identical defect
    # (R-052 pre-repair FIRES) and cannot punish a correctly-scoped double cite.
    print("ℤ×ℤ cite invariant (a ℤ×ℤ headline must cite the primitive that computes it):")
    ZZ = ("ℤ × ℤ", "ℤ×ℤ", "two conserved topological windings")
    COMPUTES_ZZ = "pi3_orientation_class_two_windings"
    zz_rows, zz_bad = [], []
    for ln in comp.splitlines():
        m = re.match(r"^\| (R-\d+) \|", ln)
        if not m:
            continue
        cols = [c.strip() for c in ln.split("|")]
        if len(cols) < 5:
            continue
        rid, headline, engine = m.group(1), cols[2], cols[4]
        if not any(t in headline for t in ZZ):
            continue
        zz_rows.append(rid)
        if COMPUTES_ZZ not in engine:
            zz_bad.append(f"{rid} (engine col: {engine[:60]!r})")
    _ck(f"every Result-Index row claiming the ℤ×ℤ cites {COMPUTES_ZZ} "
        f"(rows found: {zz_rows or 'none'}; offenders: {zz_bad or 'none'})",
        bool(zz_rows) and not zz_bad)
    # the per-section cite list is a SECOND surface for the same defect — the 2026-08-18
    # sweep repaired the row and the list together, and the 2026-08-23 catch was present
    # in both. Check it for exactly the rows the invariant already identified.
    cite_bad = []
    for rid in zz_rows:
        for ln in comp.splitlines():
            if ln.startswith(f"- {rid}:") and COMPUTES_ZZ not in ln:
                cite_bad.append(f"{rid}: {ln.strip()[:70]!r}")
    _ck(f"the per-section cite list agrees for those rows "
        f"(offenders: {cite_bad or 'none'})", not cite_bad)

    # ---- 11. THE STANDING-LEDGER ROSTER ----------------------------------
    # FORMATION_CORE §5 enumerates the standing ledgers "so nothing is missed by a
    # too-narrow search (a measured failure, three times)" — TWT_EOM_MAP.md was missed
    # for a whole sweep round. That roster is only protective while it is COMPLETE, and
    # nothing checked it. Bidirectional: every ledger on disk must be named, and every
    # name must resolve.
    print("standing-ledger roster (FORMATION_CORE §5 list vs knowledge/ledgers/):")
    fc = _read("knowledge/prompts/FORMATION_CORE.md") or ""
    on_disk = sorted(p.name for p in (ROOT / "knowledge/ledgers").glob("*.md"))
    missing = _roster_missing(fc, on_disk)
    _ck(f"every ledger in knowledge/ledgers/ is named in FORMATION_CORE "
        f"({len(on_disk)} files; unnamed: {missing or 'none'})", not missing)

    # ---- cached-worker prefix sync (RUL-079(vi)) -------------------------
    # Soft invariant: .claude/ is gitignored, so absence on a fresh clone is
    # legitimate; but IF the generated twt-worker agent exists, its embedded
    # FORMATION_CORE version must match the source header (a stale embedded
    # prefix silently forms every worker on an old contract).
    tw = ROOT / ".claude/agents/twt-worker.md"
    fc_head = (_read("knowledge/prompts/FORMATION_CORE.md") or "").splitlines()[0][:40]
    if tw.exists():
        print("cached-worker prefix sync (soft — skipped when the gitignored file is absent):")
        _ck(f"twt-worker embeds current FORMATION_CORE header ({fc_head!r}...)",
            fc_head in tw.read_text(encoding="utf-8"))

    # ---- rules-files ruling sync (R1 of the 2026-08-21 restriction analysis) --
    # RUL-068 enacted the general break clause and withdrew the per-rule [PROPOSED]
    # permission mechanism; RUL-066/072 adopted-then-merged the enforcer. The rules
    # files told agents the OPPOSITE for a day — the drift class caught twice
    # (engine split's 26 sites; F-A of the restriction analysis), hence this check.
    print("rules-files ruling sync (RUL-066/067/068 executed; no stale [PROPOSED] stamps):")
    for rel in ("knowledge/prompts/RULES_CORE.md", "knowledge/prompts/RULES_BY_ROLE.md"):
        txt = _read(rel) or ""
        stale = txt.count("*[PROPOSED]*")
        _ck(f"{rel}: no *[PROPOSED]* permission stamps survive (found {stale})", stale == 0)
    core_txt = _read("knowledge/prompts/RULES_CORE.md") or ""
    _ck("RULES_CORE.md states the RUL-068 general break clause",
        "GENERAL BREAK CLAUSE (RUL-068" in core_txt)

    # ---- 12. WITHDRAWN-GROUND SWEEP (RUL-082 / RV-7; reviewer recommendation) -
    # The canon's own named recurring failure is "a local relabel leaves a TRAIL of
    # stale labels across the corpus", and the C-32 promotion produced a live instance:
    # the withdrawn causal ground "weak = SD is neutrino-forced / the neutrino picks SD"
    # survived at four governing sites AFTER the paper, companion and family tree were
    # swept, and one of them was guarded by a passing suite check. Per the
    # record-invariants policy (a drift class caught twice in prose is a process
    # failure), the class is promoted to a check here.
    #
    # DESIGN, stated so the check can be judged:
    #  * scope = the LIVE governing files only. Dated audit records, archives, candidate
    #    probes and the canon-declared legacy standalones are HISTORY and must keep the
    #    state they were written in; firing on them would be the defect, not the catch.
    #  * a hit is EXEMPT when it sits in an explicitly-marked supersession context — the
    #    same line, the 40 preceding lines, or the 3 following lines carry one of the
    #    marker tokens. That is how the corpus legitimately QUOTES the withdrawn phrase
    #    (the engine's retained-history banner; the companion's R-079 note; the
    #    comparative ledger's audited row with its annotation directly beneath).
    #  * CLAUDE.md is reported but NON-FATAL. The lead may not edit the canon, so a hard
    #    failure there would block every bank on an edit only the coordinator can make.
    #    The exact diffs are written out for them; the WARN is the standing reminder and
    #    disappears when they are applied.
    #
    # WHAT IT DOES NOT GUARANTEE, stated so nobody over-trusts it: the marker window is a
    # HEURISTIC. A stale assertion that happens to sit within 40 lines of an unrelated
    # "no longer" or "RV-7" is exempted and will not be caught — that is a false NEGATIVE
    # the check accepts in exchange for never firing on the corpus's legitimate quotations
    # of the withdrawn phrase. Negative-tested 2026-08-21, three trials: a fresh unmarked
    # assertion in the harness FIRES; deleting the engine's supersession banner (the exact
    # pre-repair state) FIRES; an unmarked assertion planted in a dated audit record does
    # NOT fire (the inverse control — history must keep the state it was written in). The
    # second trial had to be rebuilt: hand-stripping marker tokens left "RV-6/RV-7" behind
    # and the check passed, which is itself the demonstration that the window is generous.
    print("withdrawn-ground sweep (RUL-082/RV-7: 'weak = SD is neutrino-forced' is retired):")
    WITHDRAWN = ("neutrino-forced", "neutrino picks sd", "neutrino-linked")
    MARKERS = ("superseded", "withdrawn", "rv-7", "is false", "historical assessment",
               "retained verbatim", "no longer")
    LIVE = ["knowledge/prompts/FORMATION_CORE.md", "knowledge/prompts/RULES_CORE.md",
            "knowledge/prompts/RULES_BY_ROLE.md", "knowledge/corpus/twt.py",
            "knowledge/corpus/twt_companion.py", "knowledge/corpus/twt_test.py",
            "knowledge/corpus/twt_companion_test.py",
            # the three-artifact package (relocation leg 2026-08-21): the sweep must cover
            # the front-facing Core paper as well as the dossier it cites.
            "knowledge/corpus/TWT_core_paper.md",
            "knowledge/corpus/TWT_foundational_paper.md",
            "knowledge/corpus/TWT_foundational_paper_companion.md"]
    LIVE += sorted("knowledge/ledgers/" + q.name
                   for q in (ROOT / "knowledge/ledgers").glob("*.md"))
    # L3 (keeper, 2026-08-21): _unmarked_hits used to return [] for a MISSING file with no
    # failure, so the day a LIVE file was renamed or replaced the sweep silently stopped
    # covering it while the gate stayed green — the vacuous-check tell this file exists to
    # prevent. A named LIVE file that is not on disk is now a FAILURE, not a skip.
    absent = [rel for rel in LIVE if not (ROOT / rel).exists()]
    _ck(f"every file the withdrawn-ground sweep names exists — a missing one would be "
        f"swept vacuously (absent: {absent or 'none'})", not absent)

    def _unmarked_hits(rel):
        txt = _read(rel)
        if txt is None:
            return []
        lines = txt.splitlines()
        low = [ln.lower() for ln in lines]
        out = []
        for i, ln in enumerate(low):
            if not any(w in ln for w in WITHDRAWN):
                continue
            window = low[max(0, i - 40):i + 4]
            if any(m in w for w in window for m in MARKERS):
                continue
            out.append(f"{rel}:{i + 1}")
        return out

    bad = [h for rel in LIVE for h in _unmarked_hits(rel)]
    _ck("no LIVE governing file asserts the withdrawn ground unmarked "
        f"(hits: {bad or 'none'})", not bad)
    canon_hits = _unmarked_hits("CLAUDE.md")
    if canon_hits:
        print(f"  [WARN] CLAUDE.md still asserts the withdrawn ground at {canon_hits} \u2014 "
              f"NON-FATAL by design (canon edits are the coordinator's). Diffs: "
              f"knowledge/audit/consolidation_2026-08-21/CANON_DIFFS_WEAK_SD_2026-08-21.md")
    else:
        print("  [OK ] CLAUDE.md carries no unmarked withdrawn-ground assertion")

    # ---- 11b. THE ENTERED-DATUM RESTATEMENT SWEEP (RUL-097's ground, mechanized) ------
    # NEW DRIFT CLASS, caught TWICE in prose, which canon §2 calls a process failure and
    # which it therefore requires be promoted to a check where mechanizable:
    #   (1) 2026-08-23, keeper K1: the Core paper and four other sites asserted the
    #       RH-singlet datum as a universal ("there are none"), out-stating its own FAMILY
    #       INPUTS register row, which carries a would-change-if. Five sites repaired.
    #   (2) 2026-08-24, Core-revision review: the K1 sweep grepped ONE phrase family
    #       ("right-handed charged current") and declared "no sixth LIVE site". The datum is
    #       also restated in an ISOSPIN-worded family it never touched, and two live sites
    #       survived in it (dossier §C.4.2's closing datum sentence, and CORE_PROVENANCE's
    #       own `entered` string, which this pass found only by running the check).
    # THE INVARIANT, in RUL-097's own words: an entered FAMILY INPUT may not be restated
    # more strongly than its own register row. Mechanized as: any line in a GOVERNING file
    # restating the datum must have a scope or reversal marker in view. It is deliberately
    # PHRASE-FAMILY-PLURAL — the whole point of the second catch is that one family is not
    # the datum. Dated audit records and archived drafts are NOT swept: history keeps the
    # state it was written in (the same inverse control the withdrawn-ground sweep uses).
    # NEGATIVE-TESTED IN-PROCESS 2026-08-24, three trials, all seen to fire/not-fire as
    # named: (a) restoring the pre-repair dossier sentence ("The second is the datum:
    # right-handed fermions carry no weak isospin.") FIRES; (b) restoring CORE_PROVENANCE's
    # pre-repair `entered` string FIRES; (c) the same unmarked sentence planted in a dated
    # record under knowledge/audit/ does NOT fire (history is exempt by design).
    print("entered-datum restatement sweep (RUL-097: a FAMILY INPUT may not be restated "
          "more strongly than its register row):")
    DATUM_PHRASES = ("right-handed charged current", "rh charged current",
                     "no weak isospin", "weak-isospin singlet", "weak isospin singlet")
    # A restatement is COMPLIANT if a scope word (the observation is energy-indexed) or a
    # reversal word (the would-change-if travels with it) is in view, or if the sentence is
    # explicitly a counterfactual about the refuted diagonal host ("at full strength").
    DATUM_MARKERS = ("accessible energy", "accessible energies", "observed", "observation",
                     "reversible", "reverses", "would-change-if", "would change if",
                     "at full strength", "register row")
    DATUM_LIVE = ["knowledge/corpus/TWT_core_paper.md",
                  "knowledge/corpus/TWT_foundational_paper.md",
                  "knowledge/corpus/TWT_foundational_paper_companion.md",
                  "knowledge/corpus/twt_core.py",
                  "knowledge/corpus/twt_candidate_v3.py",
                  "knowledge/corpus/twt_companion.py",
                  "knowledge/corpus/twt_test.py",
                  "knowledge/corpus/twt_companion_test.py",
                  "knowledge/ledgers/TWT_FAMILY_TREE.md"]
    d_absent = [rel for rel in DATUM_LIVE if not (ROOT / rel).exists()]
    _ck(f"every file the entered-datum sweep names exists — a missing one would be swept "
        f"vacuously (absent: {d_absent or 'none'})", not d_absent)

    def _datum_unmarked(rel, text=None):
        txt = _read(rel) if text is None else text
        if txt is None:
            return []
        low = [ln.lower() for ln in txt.splitlines()]
        out = []
        for i, ln in enumerate(low):
            if not any(p in ln for p in DATUM_PHRASES):
                continue
            window = low[max(0, i - 6):i + 7]
            if any(m in w for w in window for m in DATUM_MARKERS):
                continue
            out.append(f"{rel}:{i + 1}")
        return out

    d_bad = [h for rel in DATUM_LIVE for h in _datum_unmarked(rel)]
    _ck("no governing file restates the RH-singlet datum unscoped — every restatement "
        f"carries its energy scope or its reversal clause (hits: {d_bad or 'none'})",
        not d_bad)
    # The sweep must be able to FAIL — a phrase list that matches nothing is the
    # tight-tolerance-on-a-vacuous-check tell (canon §8a). Assert it is live.
    d_seen = sum(1 for rel in DATUM_LIVE
                 for ln in ((_read(rel) or "").lower().splitlines())
                 if any(p in ln for p in DATUM_PHRASES))
    _ck(f"the sweep is NOT vacuous — it matched {d_seen} live restatement lines "
        f"(a zero here means the phrase families went stale, not that the corpus is clean)",
        d_seen >= 8)
    d_canon = _datum_unmarked("CLAUDE.md")
    if d_canon:
        print(f"  [WARN] CLAUDE.md restates the datum unscoped at {d_canon} — NON-FATAL "
              f"by design (canon edits are the coordinator's); the register row is "
              f"knowledge/ledgers/TWT_FAMILY_TREE.md FAMILY INPUTS")
    else:
        print("  [OK ] CLAUDE.md carries no unscoped restatement of the datum")

    # ---- 11b(W). NAMED-PREMISE COVERAGE (the §11b widening, item 20) --------
    # See the PREMISE_REGISTRY header for the class, the invariant, the
    # extension rule, and the three non-vacuity clauses.
    print("named-premise coverage (§11b widened: a premise the corpus carries "
          "must be carried at a paper use-site, or be stamped PAPER-EXEMPT):")
    papers_text = "\n".join(_read(p) or "" for p in PREMISE_PAPERS)
    debt_text = "\n".join(_read(p) or "" for p in PREMISE_DEBT_FILES)
    for rel in PREMISE_PAPERS:
        _ck(f"premise sweep names an existing paper: {rel}", (ROOT / rel).exists())
    n_covered, n_debt = 0, 0
    for pid, rel, row_pat, token, phrases in PREMISE_REGISTRY:
        short = pid.split("(")[0].strip()
        text = _read(rel) or ""
        m = re.search(row_pat, text, re.M)
        if not m:
            _ck(f"{short}: its row {row_pat!r} is findable in {rel}", False)
            continue
        row = text[m.start():text.find("\n", m.start())]
        # (ii) registry <-> corpus binding: the premise token must be IN the row.
        if token not in row:
            _ck(f"{short}: the row still carries the premise token {token!r} "
                f"(a registry entry describing nothing is a vacuous pin)", False)
            continue
        status, detail = _premise_status(row, phrases, papers_text, debt_text, pid)
        if status == "COVERED":
            n_covered += 1
            print(f"  [OK ] {short}: paper use-site carries it ({detail!r})")
        elif status == "EXEMPT":
            print(f"  [OK ] {short}: PAPER-EXEMPT — {detail[:110]}")
        elif status == "DEBT":
            n_debt += 1
            print(f"  [DEBT] {short}: no paper-side use-site yet; the clause is "
                  f"OWED and booked — {detail}")
        else:
            _ck(f"{short}: resolves to a paper use-site, or is stamped "
                f"PAPER-EXEMPT ({detail})", False)
    # (iii) the floor — if the phrase families go stale this says so. RELATIVE
    # (60%, min 3), so it tightens as the registry grows instead of accumulating
    # slack; see the _premise_floor header.
    _floor = _premise_floor(len(PREMISE_REGISTRY))
    _ck(f"the premise sweep is NOT vacuous — {n_covered} of "
        f"{len(PREMISE_REGISTRY)} entries resolved by a REAL paper hit "
        f"(floor {_floor} = max({PREMISE_MIN_ABS}, 60% of "
        f"{len(PREMISE_REGISTRY)}); exemptions and debt stamps do not count)",
        n_covered >= _floor)
    # (iv) THE DEBT HATCH STAYS RETIRED (pin, 2026-08-25 consolidation; removal
    # audit §3.5). The hatch booked I-6 as non-fatal-but-loud while the paper
    # repair was owed; it was PAID 2026-08-24 and retired by the hatch's own
    # designed path — moving PREMISE_DEBT_MARK and the premise id onto DIFFERENT
    # LINES of the governing record, so the same-line predicate can no longer
    # match. That retirement is held by nothing but line layout in an archived
    # file: any reflow of that blockquote, or a tool normalising line lengths,
    # silently re-opens the allowance. It used to re-open into a `print` inside a
    # 132-line gate — a non-fatal line nobody would read. It is now a _ck: the
    # allowance is not an exemption and must not be converted into one, so
    # re-opening it FAILS the gate and takes a deliberate edit here to permit.
    # Fail-safe direction is already right: deleting the record makes DEBT
    # impossible, so the risk guarded is re-opening, never silent closure.
    if n_debt:
        print(f"  [ - ] {n_debt} premise(s) carrying an OWED paper clause — "
              f"records: {', '.join(PREMISE_DEBT_FILES)}")
    _ck(f"the PAPER-PREMISE-DEBT hatch stays RETIRED (n_debt == 0; it was paid "
        f"2026-08-24 and the allowance 'is not an exemption and must not be "
        f"converted into one' — a reflow that re-joins the marker and a premise "
        f"id on one line re-opens it, and that must FAIL, not print)",
        n_debt == 0)

    # ---- 11c. ROUND-DECISION ENACTMENT GATE (F8) ---------------------------
    print("round-decision enactment gate (F8: every apply-list item is ENACTED "
          "with a locator, or DEFERRED with a reason):")
    rounds = sorted(p for p in (ROOT / "knowledge/audit").glob("external_review_r*")
                    if p.is_dir())
    _ck(f"at least one external-review round directory is present "
        f"({len(rounds)} found)", bool(rounds))
    for rd in rounds:
        mm = ROUND_DIR_PAT.search(rd.name)
        n = int(mm.group(1)) if mm else 0
        if n < ROUND_GATE_MIN:
            print(f"  [SKIP] {rd.name}: round {n} predates the stamping "
                  f"convention (gate scoped to r{ROUND_GATE_MIN}+; history keeps "
                  f"the state it was written in)")
            continue
        gov = next((p for p in sorted(rd.glob("*.md"))
                    if p.name.startswith("MERGE")), None) or \
              next((p for p in sorted(rd.glob("*.md"))
                    if p.name.startswith("ADJUDICATION")), None)
        # PRE-SEND ROUNDS (added 2026-08-25, the r5 opening): a round directory whose
        # INDEX declares the package assembled but NOT YET SENT has no decisions to
        # stamp, so the governing-record demand does not bind YET. The skip requires
        # the declaration to be present in the INDEX — the moment a review returns
        # (and the declaration is removed/superseded), the gate binds in full. This is
        # the same shape as the r<ROUND_GATE_MIN grandfather skip: scoped, declared,
        # and it cannot hide a closed round (a returned review with no adjudication
        # still fails, because the INDEX's pre-send declaration must be gone by then
        # per the round's own log discipline).
        _idx = rd / "INDEX.md"
        if not gov and _idx.exists() and \
                "Nothing has been sent" in _idx.read_text(encoding="utf-8"):
            print(f"  [SKIP] {rd.name}: PRE-SEND (INDEX declares the package "
                  f"assembled, nothing sent) — the governing-record gate binds "
                  f"from the first returned review")
            continue
        _ck(f"{rd.name}: a governing record (MERGE*/ADJUDICATION*) is present",
            bool(gov))
        if not gov:
            continue
        items = _apply_list_items(gov.read_text(encoding="utf-8"))
        _ck(f"{rd.name}: {gov.name} carries a parseable APPLY LIST "
            f"({len(items)} numbered items)", bool(items))
        others = [(p.name, p.read_text(encoding="utf-8"))
                  for p in sorted(rd.glob("*.md")) if p != gov]
        bad = []
        for num, marker in items:
            ok, kind = _item_enacted(num, marker, others)
            if not ok:
                bad.append(f"item {num} [{marker}] — {kind}")
        _ck(f"{rd.name}: every apply-list item carries an enactment stamp "
            f"(unstamped: {bad or 'none'})", not bad)

    # ---- 11d. ENGINE-LITERAL PARENTHETICAL (O8.2) --------------------------
    print("engine-literal parentheticals (O8.2: a quoted engine literal carries "
          "its scope note or a stated normalization):")
    lit_seen = 0
    for label, rel, literal, tokens, window in LITERAL_SITES:
        text = _read(rel)
        if text is None:
            _ck(f"{label}: {rel} exists", False)
            continue
        occ = sum(1 for ln in text.splitlines() if literal in ln)
        lit_seen += occ
        if occ == 0:
            _ck(f"{label}: the literal {literal!r} is still quoted in {rel} "
                f"(zero occurrences means the site moved, not that it is clean)",
                False)
            continue
        viol = _literal_violations(text, literal, tokens, window)
        _ck(f"{label}: all {occ} occurrence(s) of {literal!r} carry a scope "
            f"token within ±{window} lines (bare: {viol or 'none'})", not viol)
    for label, rel, anchor, required in LITERAL_PRESENCE:
        text = _read(rel) or ""
        _ck(f"{label}: {anchor!r} present and {required!r} stated in the same "
            f"document", anchor in text and required in text)
    _ck(f"the literal registry is NOT vacuous — it matched {lit_seen} quoted "
        f"literals", lit_seen >= 5)

    # ---- 11e. R-159 FINDABILITY -------------------------------------------
    # OI-1's finding, worth more than the item it came from: a commission
    # worker, the merge adjudicator and the OI-1 author all failed to find a
    # banked result IN THE SAME FILE as the code they were reading, because the
    # whole continuous hypercharge anomaly system lives inside a large primitive
    # named `charge_normalization_anchor_free` — a name that does not say
    # "anomaly". A banked result whose name does not carry its strongest content
    # is findable only by whoever already knows it exists. The repair is
    # prose-level (put the searchable terms in the row and the map entry); this
    # check is what keeps the repair from being swept away.
    print("R-159 findability (a banked result must be findable by what it "
          "contains, not only by what it is named):")
    comp_txt = _read("knowledge/corpus/TWT_foundational_paper_companion.md") or ""
    for locator, label in [(r"^\| R-159 \|", "companion Result-Index row R-159"),
                           (r"^\| charge_normalization_anchor_free \|",
                            "engine↔paper-map entry")]:
        m = re.search(locator, comp_txt, re.M)
        if not m:
            _ck(f"{label}: located", False)
            continue
        row = comp_txt[m.start():comp_txt.find("\n", m.start())]
        missing = [t for t in ("anomaly", "two-branch") if t not in row.lower()]
        _ck(f"{label} carries the searchable terms 'anomaly' and 'two-branch' "
            f"(missing: {missing or 'none'})", not missing)

    # ---- 11f. SHIPPED-CITE RESOLUTION (RUL-103) — WARN-only ----------------
    print("shipped-cite resolution (RUL-103 publish-on-cite; WARN-only — the "
          "unresolved set is a curated queue, see the promotion note):")
    mirror = Path(os.environ.get("TWT_MIRROR_DIR",
                                 Path.home() / "Claude/Projects/twt-engine"))
    for rel in SHIPPED_ARTIFACTS:
        _ck(f"shipped-cite sweep names an existing artifact: {rel}",
            (ROOT / rel).exists())
    if not mirror.exists():
        print(f"  [SKIP] mirror clone not present at {mirror} (set TWT_MIRROR_DIR); "
              f"the sweep needs the mirror tree to resolve against")
    else:
        def _resolves(path):
            # RUL-107(3) (human, 2026-08-25): EXACT-PATH semantics — a cite resolves
            # only if the cited path itself exists in the mirror. The bare-basename
            # fallback (and with it the directory-satisfies-file reading H-1/K5
            # flagged) is RETIRED: it let a cite count as published the moment its
            # parent directory existed, which certified less than the check's name
            # claimed. The queue reads bigger and honestly under this semantics.
            return (mirror / path).exists()

        queue, sites = {}, 0
        for rel in SHIPPED_ARTIFACTS:
            for path, ln in _shipped_cite_misses(_read(rel) or "", _resolves):
                queue.setdefault(path, []).append(f"{rel}:{ln}")
                sites += 1
        if queue:
            print(f"  [WARN] {len(queue)} cited knowledge/ path(s) at {sites} site(s) "
                  f"resolve in NEITHER the mirror nor a not-shipped marker — this is "
                  f"the next sync's QUEUE, not a failure (RUL-103: citation is the "
                  f"curation trigger; which records ship stays the human's call):")
            for path in sorted(queue):
                print(f"    - {path}  <- {len(queue[path])} site(s), "
                      f"e.g. {queue[path][0]}")
        else:
            print("  [OK ] every cited knowledge/ path resolves in the mirror or "
                  "carries a not-shipped marker — PROMOTE THIS CHECK TO FATAL "
                  "(swap the print for _ck); the queue is drained")

    # ---- 12. RELEASE BLOCKERS (release mode only) ------------------------
    # NEW DRIFT CLASS, and it is not prose drift — it is DOCKET drift. External-review
    # round 2 independently reproduced two defects our own blind probe P2 had already
    # found and filed: a vacuous suite check and a stale provenance comment, both in the
    # charge sector, both still shipping in the release the reviewer read. The record
    # was correct and the release ignored it. Nothing in the apparatus connected the
    # FOUND-LATER table to the release path, so a known, located, engine-sited defect
    # could be handed to a cold reviewer with no gate objecting.
    #
    # WHY HERE AND NOT IN render_pdf.sh. The enforcement POINT is the release —
    # render_pdf.sh, which builds the reviewer-facing PDFs and then syncs and pushes the
    # public mirror — so that is where the call goes. But the LOGIC belongs here: this
    # file is already the record-invariants gate, it is Python (so the negative test is
    # cheap and repeatable), and render_pdf.sh's own header records two of its grep-based
    # guards going silently dead. A guard that greps nothing verifies nothing. bank.sh
    # calls without --release, so ordinary banking is untouched: this fires at releases.
    #
    # THE CONTRACT. knowledge/ledgers/TWT_CHECKER_CALIBRATION.md carries a
    # "## RELEASE-BLOCKERS" section whose table has columns
    #     | id | status | site | defect | discharge |
    # status in {FIXED, WAIVED, OPEN}. A release refuses on any OPEN row, naming it.
    #
    # WHAT THE WAIVER CLAUSE ACTUALLY ENFORCES, said honestly (§8a reviewer, COMPUTED —
    # it mutated a row to WAIVED with the 38-character discharge "waived for now, busy
    # with other things" and the gate went green). The predicate is a LENGTH test. It
    # enforces that a waiver is WRITTEN DOWN in a governing ledger and long enough to
    # read — recordedness and auditability, not merit. Merit is a human judgment and no
    # regex reaches it. That is the correct scope for a mechanical gate, and it still
    # converts a silent skip into an on-record sentence someone can be asked about; but
    # do not gloss it as "prevents a reasonless waiver," which is one notch more than it
    # delivers. Release mode PRINTS every WAIVED row for the same reason — otherwise a
    # waived row ships silently forever.
    #
    # Every named site must still resolve to a file in the tree. And the row COUNT must
    # match the number of FOUND-LATER rows that name an engine site, so a new miss filed
    # in that table cannot silently escape the release path.
    #
    # COVERAGE SCOPE, stated because it was nowhere (keeper orphan): NON-ENGINE-SITED
    # misses are outside this gate BY DESIGN — the coverage clause counts only rows
    # naming twt.py/twt_test.py/twt_companion*. A recorded defect in the paper or the
    # ledgers (e.g. the 7 % Λ-factor trap) is real and docketed, and this gate will not
    # see it. Widening the gate to prose would need a different predicate than "the site
    # resolves"; until then, the worklist is that class's only tracker.
    print("release blockers (calibration ledger vs the release path):")
    cal = _read("knowledge/ledgers/TWT_CHECKER_CALIBRATION.md") or ""
    blk = re.search(r"^##\s*RELEASE-BLOCKERS(.*?)(?=^##\s|\Z)", cal, re.S | re.M)
    _ck("calibration ledger carries a RELEASE-BLOCKERS section", bool(blk))
    if blk:
        # NOTE: cells may contain markdown-escaped pipes (\|) — e.g. an absolute-value
        # bar inside a defect description. A naive [^|]* stops at the backslash and the
        # row silently vanishes from the table. That is not hypothetical: the first
        # draft of this check parsed 4 of 5 rows and only the coverage clause caught it,
        # which is the same "a regex that silently skipped a row" defect the 2026-08-18
        # negative-testing round found. CELL matches escaped pipes explicitly.
        CELL = r"(?:[^|\\]|\\.)*?"
        rows = re.findall(
            rf"^\|\s*([A-Za-z0-9\-]+)\s*\|\s*([A-Z]+)\s*\|\s*({CELL})\s*\|"
            rf"\s*({CELL})\s*\|\s*({CELL})\s*\|\s*$",
            blk.group(1), re.M)
        rows = [r for r in rows if r[0] not in ("id", "---")]
        _ck(f"RELEASE-BLOCKERS table parses ({len(rows)} rows)", bool(rows))
        bad_status = [r[0] for r in rows if r[1] not in ("FIXED", "WAIVED", "OPEN")]
        _ck(f"every row carries a known status FIXED/WAIVED/OPEN (bad: {bad_status or 'none'})",
            not bad_status)
        nude_waivers = [r[0] for r in rows if r[1] == "WAIVED" and len(r[4]) < 20]
        _ck(f"every WAIVED row is WRITTEN DOWN and long enough to read — recordedness "
            f"and auditability, NOT reasonedness; merit stays a human call (unwritten: "
            f"{nude_waivers or 'none'})", not nude_waivers)
        # referential integrity: the named site must resolve to a file that exists.
        dead = []
        for r in rows:
            fname = re.split(r"[:\s]", r[2].strip().strip("`"))[0]
            if fname and not list(ROOT.rglob(fname)):
                dead.append(f"{r[0]}->{fname}")
        _ck(f"every blocker's named site resolves in the tree (dead: {dead or 'none'})",
            not dead)
        # coverage: FOUND-LATER rows naming an engine site must all be represented.
        fl = re.search(r"^##\s*FOUND-LATER(.*?)(?=^##\s|\Z)", cal, re.S | re.M)
        fl_engine = 0
        if fl:
            for ln in fl.group(1).splitlines():
                if ln.startswith("|") and ln.count("|") >= 6 and "date found" not in ln \
                        and not set(ln) <= set("|- "):
                    if "twt.py" in ln or "twt_test.py" in ln or "twt_companion" in ln:
                        fl_engine += 1
        _ck(f"RELEASE-BLOCKERS covers every engine-sited FOUND-LATER row "
            f"({len(rows)} blockers vs {fl_engine} engine-sited misses)",
            len(rows) == fl_engine)
        open_rows = [f"{r[0]} ({r[2]}): {r[3][:70]}" for r in rows if r[1] == "OPEN"]
        if args.release:
            # A waived row would otherwise ship silently forever. One line each, every
            # release, so the waiver is re-read by whoever is doing the shipping.
            waived = [r for r in rows if r[1] == "WAIVED"]
            if waived:
                print(f"  [WAIVED] {len(waived)} blocker(s) shipping under a recorded waiver "
                      f"— re-read them before sending:")
                for r in waived:
                    print(f"    - {r[0]} ({r[2]}): {r[4][:160]}")
            else:
                print("  [OK ] no WAIVED blockers shipping")
            _ck(f"RELEASE MODE: no OPEN blocker ships (open: {open_rows or 'none'})",
                not open_rows)
        elif open_rows:
            print(f"  [WARN] {len(open_rows)} OPEN blocker(s) — non-fatal at bank, FATAL at "
                  f"release (scripts/check_records.py --release): {open_rows}")
        else:
            print("  [OK ] no OPEN blockers (release path clear)")

    # ---- 13. APPARATUS PORTS 2026-09-17 (2A the dispatch log; 2C the paths ledger; 2F the
    # design-verdict vocabulary) — each predicate has a planted demo in self_test() ------
    print("apparatus ports (2A/2C/2F):")
    _log = _read(DISPATCH_LOG_REL) or ""
    _PORT_GLOBS = ["knowledge/candidates/probes_*", "knowledge/audit/*"]
    _VNAME = re.compile(r"VERDICT|ADJUDICATION|CONTRA_REVIEW", re.I)
    _pdirs = [_d for _g in _PORT_GLOBS for _d in sorted(ROOT.glob(_g)) if _d.is_dir()]
    _vpaths = []
    for _d in _pdirs:
        for _f in sorted(_d.iterdir()):
            if _f.is_file() and _f.suffix == ".md" and _VNAME.search(_f.name):
                _vpaths.append(_f.relative_to(ROOT).as_posix())
    _miss = _dispatch_log_missing(_log, _vpaths)
    _ck(f"2A dispatch log: every verdict file since the log opened has a pointer row "
        f"({len(_vpaths)} verdict files, {len(_dispatch_log_rows(_log))} rows; missing {_miss[:3]})",
        not _miss and bool(_log))
    _bad = []
    for _d in _pdirs:
        for _f in sorted(_d.glob("*DESIGN_VERDICT*.md")):
            if _design_verdict_word_defect(_f.read_text(encoding="utf-8", errors="replace")):
                _bad.append(_f.name)
    _ck(f"2F design verdicts carry exactly one of {DESIGN_WORDS} (offenders {_bad[:3]})", not _bad)
    _pl = _read("knowledge/ledgers/TWT_PATHS_LEDGER.md")
    _pd = _paths_ledger_defects(_pl) if _pl else ["paths ledger missing"]
    _ck(f"2C paths ledger: fork headers dated, LIVE rows carry a promotion condition ({_pd[:2]})", not _pd)

    _et = {rel: _read(rel) for rel, _, _ in ENDORSE_SITES}
    _truth = _core_endorsement_items(_et.get("knowledge/corpus/TWT_core_paper.md"))
    _ed = _endorsement_count_defects(_et, _truth) if _truth else ["the Core paper's §1.3 list not found"]
    _ck(f"endorsement count: every live site carries the Core §1.3 list's {_truth} items ({_ed[:3]})", not _ed)

    # ---- verdict ---------------------------------------------------------
    print("-" * 70)
    if FAILS:
        print(f"  RECORD-INVARIANTS: {len(FAILS)} FAILURE(S) — the records have "
              f"drifted from the tree. Fix the documents before banking.")
        for f in FAILS:
            print(f"    - {f}")
        sys.exit(1)
    if PENDS:
        print(f"  RECORD-INVARIANTS: ALL HOLD, with {len(PENDS)} canon site(s) awaiting a "
              f"HUMAN-APPLIED diff (canon edits are human-only; the diffs are written):")
        for p in PENDS:
            print(f"    - {p}")
        print(f"    diffs: {', '.join(CANON_DIFF_FILES)}")
        sys.exit(0)
    print("  RECORD-INVARIANTS: ALL HOLD (prose matches tree).")
    sys.exit(0)


if __name__ == "__main__":
    main()
