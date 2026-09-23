#!/usr/bin/env python3
"""Exact identities and source contracts for the reusable-lemma revision.

Not a proof assistant. Universal geometry is proved in numbered sources;
these checks protect identities, endpoint domains, and manuscript interfaces.
"""
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PAPER = ROOT / "arrange/paper_draft"
m, delta, beta, k, a, b, c, u, d = sp.symbols("m delta beta k a b c u d", real=True)
identities = []
def zero(name, expression):
    assert sp.factor(expression) == 0, name
    identities.append(name)

q = m * (1-m) / 2
lower = m/2-sp.Rational(2,5)*m*m
zero("deficit bound gives the F baseline", 2*(1-q)-1-(1-m+m*m))
zero("chord coefficient", (m-lower)/lower-(5+4*m)/(5-4*m))
zero("chord endpoint", m-(m-beta)*beta/beta-beta)
zero("one-caliper envelope", (1-k/2+k*k/2)**2-(1-k+k*k)-k*k*(1-k)**2/4)
# The original a >= 1/2 restriction is insufficient for the chord interval.
M = 1-m-lower
assert M.subs(m, sp.Rational(3,8)) == sp.Rational(79,160)
assert (M-m).subs(m, sp.Rational(3,8)) == sp.Rational(19,160)
assert sp.diff(M-m,m).subs(m,sp.Rational(3,8)) < 0
assert sp.diff(M-m,m).subs(m,0) < 0
assert lower.subs(m,sp.Rational(3,8)) == sp.Rational(21,160)
# Exact Q substitution retained instead of a long expanded display.
P=(a*a-1)*c*c+(2*a*b*b+b)*c+b**4-b*b
Q=sp.expand(16*P.subs({a:(u-d)/2,b:(u+d)/2,c:sp.Rational(3,2)-u}))
zero("Q derivative factor",sp.diff(Q,d)-2*(2*d+4*u-3)*(d*d+d*(4*u-3)+(u-1)*(2-u)))
zero("Q boundary factor",Q.subs(d,0)-(u-1)*(u**3-5*u*u-24*u+36))
# Generic radial minimum: deleting the two monotone-path dominated entries
# is justified by f <= A_i,B_i; identities are not used as a numerical proof.
radial=(PAPER/"06_finite_enclosure_full.tex").read_text()
assert "Gamma_i" not in radial
assert "C_i>1-d_i'" not in radial
assert "s_i=\\min\\{f(A_i,B_i),A_{i-1},B_{i+1}\\}" in radial
assert "0\\le s\\le d_i" in radial
geom=(PAPER/"fixed_witness/D_bc_finite_calipers.tex").read_text()
statement=geom[geom.index("\\begin{lemma}"):geom.index("\\end{lemma}")]
assert "c_{\\max}" not in statement and "z\\le" not in statement
assert "\\Longleftrightarrow" in statement
assert "not a" in statement and "minimizes" in statement
cap=(PAPER/"fixed_witness/D_bc_capacity_envelope.tex").read_text()
assert "H'(m)" not in cap and "H(m)" not in cap
legacy=(ROOT/"proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2615a_wide_range_slack_envelope.md").read_text()
assert "19/160" in legacy
assert "m=\\min(a,b)\\le1/4" in cap
assert "15/38" in cap and "-18325/1024" in cap
for rel in ("E_zero_gap_nine_point_optimization.tex", "inline_proofs/06_zero_gap.tex"):
    text=(PAPER/rel).read_text()
    assert "lem:bc-capacity-tools" in text
    assert "tab:finite-enclosure-subcases" not in text
print(f"PASS: {len(identities)} reusable-lemma identities; ordered chord domain and source contracts")
