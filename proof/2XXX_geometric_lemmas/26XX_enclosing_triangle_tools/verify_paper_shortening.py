#!/usr/bin/env python3
"""Exact identities and source regressions for manuscript shortening.

These checks protect the refactor's contracts; they are not a formal proof of
all geometry. The numbered proofs and exact certificate remain authoritative.
"""
from pathlib import Path
import hashlib
import re
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PAPER = ROOT / "arrange/paper_draft"
m, M, c = sp.symbols("m M c", real=True)
F = (m*m-1)*c*c + (2*m*M*M+M)*c + M**4-M*M
assert sp.expand(4*F.subs({m:1-M,c:sp.Rational(1,2)})-M*M*(2*M-1)**2) == 0
assert sp.expand(sp.diff(4*F.subs(c,sp.Rational(1,2)),m)-(2*m+4*M*M)) == 0
print("self-midpoint corollary: 2 exact polynomial identities OK")

PRESERVED_SECTIONS = [('arrange/paper_draft/02_structure_and_common_geometry.tex',
  '\\begin{proposition}[Exact-trace normalization of raw $(3,0)$ roles]',
  '\\end{proof}',
  '4cce63413809de3d51da801aec67e890bccedc8db641831922e9c85943ea177f'),
 ('arrange/paper_draft/A_structural_shared_local_signed_center_optimization.tex',
  '\\begin{lemma}[Raw $(3,0)$ trace-normalization calculation]',
  '\\end{proof}',
  'b48ff7c49c63b9a23bfead2441e379a5124d27a675e4c2f5a88902229a9c2517'),
 ('arrange/paper_draft/D_nonzero_gap_finite_enclosure_optimization.tex',
  '\\begin{lemma}[Two-vertex replacement from scalar margins]',
  '\\end{proof}',
  '2265e938cbaab39caec4937a5cd4e3484b73246be7cc9515b7711318f653f10c')]
for raw, start, end, digest in PRESERVED_SECTIONS:
    text = (ROOT / raw).read_text()
    section = text[text.index(start):text.index(end,text.index(start))]
    # The readability revision defers reach symbols until their definition.
    # Reverse only this exact prose substitution before checking the original
    # fingerprint; the statement's content and the proof calculation stay fixed.
    if raw == "arrange/paper_draft/02_structure_and_common_geometry.tex":
        revised = ("all three actual maximal reaches, and whether the two boundary reaches\n"
                   "have sum greater than one, are unchanged.")
        original = ("all three actual maximal reaches and the inequality\n"
                    "$A_i+B_i>1$ are unchanged.")
        assert section.count(revised) == 1, "normalization wording changed unexpectedly"
        section = section.replace(revised, original)
    assert hashlib.sha256(section.encode()).hexdigest() == digest, raw
print("raw (3,0) calculations and both replacement charts: preserved; statement wording crosschecked")

d = (PAPER / "D_nonzero_gap_finite_enclosure_optimization.tex").read_text()
assert "D_bc_capacity_envelope" in d and "D_bc_finite_calipers" in d
assert "First CE1 return step" not in d
fixed=(PAPER / "fixed_witness/06_fixed_witness_body.tex").read_text()
assert not (PAPER / "fixed_witness/D_fixed_witness_extensions.tex").exists()
assert "lem:bc-five-point" in fixed and "thm:cert-caliper" in fixed
assert "prop:signed-center-normal-form" not in fixed
assert "prop:new-ce1-direct-certificate" not in fixed
print("BC/D terminal calipers replace the historical center-normal-form route: OK")

body = (PAPER / "fixed_witness/06_fixed_witness_body.tex").read_text()
assert "B_5\\ge B_0/2" in body
assert "rV_2,\\widehat tV_4" in body and "\\widehat t=\\min\\{t,A_3\\}" in body
radial = (PAPER / "06_finite_enclosure_full.tex").read_text()
assert "C_i>1-d_i'" not in radial
for label in ("lem:fixed-total-radial-forcing", "cor:clipped-radial-forcing",
              "eq:clipped-path-radius", "cor:new-uniform-common-pair-forcing"):
    assert "\\label{" + label + "}" in radial, label
for name in ("optional_B.tex", "06_fixed_zero_gap_coordinates.tex"):
    assert not (PAPER / "fixed_witness" / name).exists()
for label in ("cor:ce1-five-handoff-return", "lem:appendix-ktr-ce2",
              "lem:appendix-adjacent-vd-separation", "thm:new-complementary-gap",
              "lem:new-open-trace-endpoint"):
    assert "\\label{" + label + "}" not in d + body + (PAPER / "06_finite_enclosure_full.tex").read_text()
print("selected-gap witnesses and inactive-package removals: OK")
