#!/usr/bin/env python3
"""Exact checks supporting the B/C unification report.

These checks verify identities and an explicit counterexample to dropping the
boundary-transfer hypothesis. They do not replace the inherited CE1/CE2 proofs.
Requires SymPy. All sign checks below use rational outward intervals, not floats.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from math import isqrt
import sympy as sp

checked: list[str] = []

def identity(name: str, expression: sp.Expr) -> None:
    assert sp.simplify(expression) == 0, name
    checked.append(name)

@dataclass(frozen=True)
class I:
    lo: F
    hi: F
    def __post_init__(self) -> None:
        assert self.lo <= self.hi
    @staticmethod
    def point(v: F | int) -> 'I':
        return I(F(v), F(v))
    def __add__(self, other: 'I | F | int') -> 'I':
        o = other if isinstance(other, I) else I.point(other)
        return I(self.lo + o.lo, self.hi + o.hi)
    __radd__ = __add__
    def __neg__(self) -> 'I':
        return I(-self.hi, -self.lo)
    def __sub__(self, other: 'I | F | int') -> 'I':
        o = other if isinstance(other, I) else I.point(other)
        return self + (-o)
    def __rsub__(self, other: 'I | F | int') -> 'I':
        return -self + other
    def __mul__(self, other: 'I | F | int') -> 'I':
        o = other if isinstance(other, I) else I.point(other)
        p = [a*b for a in (self.lo, self.hi) for b in (o.lo, o.hi)]
        return I(min(p), max(p))
    __rmul__ = __mul__
    def __truediv__(self, other: 'I | F | int') -> 'I':
        o = other if isinstance(other, I) else I.point(other)
        assert o.lo > 0 or o.hi < 0
        return self * I(1/o.hi, 1/o.lo)

def root(n: int) -> I:
    scale = 10**12
    k = isqrt(n*scale**2)
    assert k*k <= n*scale**2 < (k+1)*(k+1)
    return I(F(k, scale), F(k+1, scale))

def positive(name: str, expression: I | F | int) -> None:
    e = expression if isinstance(expression, I) else I.point(expression)
    assert e.lo > 0, (name, e)
    checked.append(name)

b, t, R, al, de, eta, Ai, Bi, An, Bn = sp.symbols(
    'b t R al de eta Ai Bi An Bn', real=True)
identity('diameter identity at the half-tail threshold',
         b*b+b*(1-b/2)+(1-b/2)**2 - (1+3*b*b/4))
identity('completed-square diameter identity',
         b*b+b*t+t*t - ((t+b/2)**2+3*b*b/4))
identity('A path-deficit identity',
         An-Ai-((1-Ai-Bi)+(Bi+An-1)))
identity('B path-deficit identity',
         Bi-Bn-((1-An-Bn)+(Bi+An-1)))
Q = (eta+al+de)/(2*R)
L1 = (2-4*al)*Q-(1-4*al)*al
identity('CE1 first-step L1 minus delta identity',
         R*(L1-de)-((1-2*al)*eta+(1-R-2*al)*(al+de)+4*R*al**2))

# Explicit six-triangle counterexample: the opposite boundary gap is not covered.
a = (root(157)-9)/20
A = [a, I.point(F(9,100)), I.point(F(1,10)), I.point(F(199,200)),
     I.point(F(997,1000)), I.point(F(999,1000))]
B = [I.point(F(9,10)), I.point(F(909,1000)), I.point(F(1,100)),
     I.point(F(1,250)), I.point(F(1,500)), I.point(F(1,2000))]
C = [a*F(9,10)/(a+F(9,10)), B[1], (root(10101)-F(11,10))/101,
     A[3], A[4], A[5]]
R0, W0 = F(1,10), F(9,10)
al0 = de0 = F(1,50)
E = root(91)/10
et = 1-E
P = E*et
k = et+al0+de0
positive('candidate right trace positive', P-al0-W0*de0)
positive('candidate companion trace positive', P-R0*al0-de0)
positive('candidate contains M0 openly', E-al0-de0-F(1,2))
positive('right gap first endpoint is above candidate entry', B[0]-k/R0)
positive('right gap second endpoint is below candidate exit',
         W0+de0-(1-A[1]))
positive('right actual gap has positive length', 1-A[1]-B[0])
positive('left actual gap has positive length', 1-A[0]-B[5])
positive('left actual gap starts beyond candidate left trace', A[0]-(R0+al0))
positive('the omitted transfer inequality fails', B[0]/2-B[5])
positive('T0 is supercritical', A[0]+B[0]-1)
for i in range(1,6):
    positive(f'T{i} is strictly nonsupercritical', 1-A[i]-B[i])
for i in range(1,5):
    positive(f'middle edge {i} has strict overlap', B[i]+A[i+1]-1)
for i in range(6):
    positive(f'T{i} own radial reach positive', C[i])
    positive(f'T{i} own radial reach below one', 1-C[i])
exits = [E-al0-de0, I.point(de0/R0), I.point(de0),
         I.point(min(al0/R0,de0/W0)), I.point(al0), I.point(al0/W0)]
for i in range(6):
    positive(f'all of radial arm {i} is covered openly', exits[i]-(1-C[i]))

# Unit-side construction checks in the local metric x^2+y^2-xy.
a_s, b_s = (sp.sqrt(157)-9)/20, sp.Rational(9,10)
def norm2(v: sp.Matrix) -> sp.Expr:
    x,y=v
    return x*x+y*y-x*y
vertices = [sp.Matrix([a_s,0]), sp.Matrix([0,b_s]), sp.Matrix([-b_s,-a_s])]
for i in range(3):
    identity(f'T0 side {i} has squared length one',
             norm2(vertices[i]-vertices[(i+1)%3])-1)
p,eps=sp.symbols('p eps')
minus = [sp.Matrix([-eps,1-p]),sp.Matrix([1-eps,1-p]),sp.Matrix([-eps,-p])]
plus = [sp.Matrix([p,-eps]),sp.Matrix([p,1-eps]),sp.Matrix([p-1,-eps])]
for name,vs in [('minus',minus),('plus',plus)]:
    for i in range(3):
        identity(f'{name} template side {i} has squared length one',
                 norm2(vs[i]-vs[(i+1)%3])-1)
Ginv=sp.Matrix([[sp.Rational(4,3),sp.Rational(2,3)],
                [sp.Rational(2,3),sp.Rational(4,3)]])
ns=[sp.Matrix([1,-101]),sp.Matrix([-101,100]),sp.Matrix([100,1])]
for i in range(3):
    identity(f'T2 normal {i} has required dual length',
             (ns[i].T*Ginv*ns[i])[0]-sp.Rational(4,3)*10101)
    identity(f'T2 adjacent normals {i} meet at 120 degrees',
             (ns[i].T*Ginv*ns[(i+1)%3])[0]+sp.Rational(2,3)*10101)
identity('T2 normals sum to zero (first component)', sum(v[0] for v in ns))
identity('T2 normals sum to zero (second component)', sum(v[1] for v in ns))
# Its three constants sum to sqrt(10101), giving unit equilateral side.
identity('T2 constants have the required unit-side sum',
         sp.Rational(1,10)+1+(sp.sqrt(10101)-sp.Rational(11,10))-sp.sqrt(10101))
for name in checked:
    print('PASS', name)
print(f'ALL {len(checked)} EXACT CHECKS PASSED')

# The numbered D sources and the geometric D theorem/proof are immutable.
# Historical prose around them is not a mathematical preservation contract.
from pathlib import Path
import hashlib
ROOT = Path(__file__).resolve().parents[3]
PRESERVED_SECTIONS = [('proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md',
  '## 6. Family D:',
  '## 7.',
  'dad6e3e829e8730f1973f20c5950cd2874078e0fbdeb39aa3239ed367d5d9946'),
 ('proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2610_finite_enclosure_terminal_interfaces.md',
  '## 5. D:',
  '## 6. F:',
  'e6b126f12ae4a5965d2f2b2824ab1303d6257631ea623d25576d827103af9236'),
 ('arrange/paper_draft/fixed_witness/D_fixed_witness_extensions.tex',
  '\\begin{lemma}[Fixed four-point supported-rescuer proof]',
  '\\end{proof}',
  '1374d2f084fba4548299c1d7d1f886a67cd1884828b1f700dadf726eb34a0c99'),
 ('arrange/paper_draft/fixed_witness/06_fixed_witness_body.tex',
  '\\begin{theorem}[Four-point rescuer geometry]',
  '\\end{proof}',
  'ef28d870cb5155b81d74187b7f0a11113b12d0810d218fc117a57b7d0a6bafde')]
for path, start, end, digest in PRESERVED_SECTIONS:
    text = (ROOT / path).read_text(encoding="utf-8")
    section = text[text.index(start):text.index(end, text.index(start))]
    assert hashlib.sha256(section.encode()).hexdigest() == digest, path
PRESERVED_FILES = [('proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md',
  '4e2ad6e6f6e63427695193cff07ccd228e7dc0b5ec80086f5fb8b52dc2d16821'),
 ('proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md',
  'c1dfec8125ff4e0dc94fccb90f60b2a79d4f5c07d61853762b74dacc17913696'),
 ('proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md',
  '09f5668ce99ba850a03c41f41487e20bbdcdd340b72f663d843d248c8d9acf47')]
for path, digest in PRESERVED_FILES:
    assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, path
core = (ROOT / "proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md").read_text()
assert "B_5\\ge B_0/2" in core
assert "B_i+A_{i+1}>1\\quad(1\\le i\\le4)" in core
assert "## 4. Optional family B:" in core
print("BC source hypotheses, numbered D sources, and D geometry: OK")
