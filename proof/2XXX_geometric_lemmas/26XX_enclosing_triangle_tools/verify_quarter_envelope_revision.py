#!/usr/bin/env python3
"""Exact checks for the September 23 quarter-envelope proof revision.

Run with Python 3.10+ and SymPy:
    python verify_quarter_envelope_revision.py

Identities and stated rational interval bounds are checked exactly.
The grid and transition tests are diagnostics, not proofs of universality.
Numbered source 2615 and the implementation report supply the geometric input and exhaustive domain
reduction. This is not a replacement for repository CI or zero-gap replay.
"""
from __future__ import annotations

from fractions import Fraction as Q
import sympy as S

m, c, d, u, z, y, r, t, a, x = S.symbols("m c d u z y r t a x", real=True)
checks: list[str] = []

def eq(name: str, lhs: S.Expr, rhs: S.Expr = S.Integer(0)) -> None:
    if S.cancel(lhs-rhs) != 0:
        raise AssertionError(name + ': ' + str(S.factor(lhs-rhs)))
    checks.append(name)

def positive(name: str, value: S.Expr) -> None:
    if value.is_positive is not True:
        raise AssertionError(name + ': ' + str(value))
    checks.append(name)

F = lambda cc, mm: cc**4-cc**2+mm*cc-mm**2
q = lambda w: w*(1-w)/2
beta = lambda w: 2*w/(4+3*w)
kappa = lambda w: 1+S.Rational(3,2)*w
g = lambda w: w+beta(w)
P = lambda yy, rr, tt: 2*(rr+tt)-(1-yy+rr)*(4*u-yy+rr)
Qcx = lambda cc, xx: xx**2+(cc-2)*xx+cc

# Shared quadratic deficit; the residual is exactly the defining quartic.
eq('quartic rearrangement', (1-c)*c**2*(1+c)-m*(c-m), -F(c,m))
eq('shared q factor', 2*(c-m)-(1-m)*c**2*(1+c),
   (1-c)*((1-m)*c*(c+2)-2*m))
positive('q bracket lower bound', S.Rational(1,2)*S.Rational(3,4)*S.Rational(11,4)-1)

# Stronger baseline on the smaller range m <= 1/4.
B = 81*m**4+405*m**3+656*m**2+272*m-128
eq('new beta quartic substitution', F(1-beta(m),m), -m**2*B/(4+3*m)**4)
assert all(coef > 0 for coef in S.Poly(S.diff(B,m),m).all_coeffs())
checks.append('baseline residual polynomial is strictly increasing')
eq('baseline residual endpoint', B.subs(m,S.Rational(1,4)), -S.Rational(3163,256))
positive('test root stays above sqrt(3)/2', (1-beta(S.Rational(1,4)))**2-S.Rational(3,4))
eq('beta dominates q', beta(m)-q(m), m**2*(3*m+1)/(2*(3*m+4)))
eq('beta dominates former b on common domain', beta(m)-(m/2-S.Rational(2,5)*m**2),
   m**2*(12*m+1)/(10*(3*m+4)))
eq('new envelope branches meet', m-kappa(m)*beta(m), beta(m))
eq('ordered chord interval endpoint', (1-2*m-beta(m)).subs(m,S.Rational(1,4)), S.Rational(15,38))

# Direct polynomial proof of the affine-slope envelope. No root derivatives.
M = 1-m-d
H = ((1-d)**2-1)*c**2+M*c-M**2
Cbar = 1-m+kappa(m)*d
N = ((3*m+2)**2*d**3-10*m*(3*m+2)*d**2
     +(28*m*m-22*m-20)*d+14*m*(1-m))
eq('selected quadratic residual', H.subs(c,Cbar), d*N/4)
eq('envelope cubic derivative', S.diff(N,d),
   3*(3*m+2)**2*d*d-20*m*(3*m+2)*d+28*m*m-22*m-20)
upper = 3*S.Rational(11,4)**2*S.Rational(1,8)**2+S.Rational(7,4)-20
eq('cubic derivative upper bound value', upper, -S.Rational(18325,1024))
positive('cubic derivative is strictly negative', -upper)
eq('envelope cubic endpoint', N.subs(d,beta(m)), -2*m*B/(4+3*m)**3)

# Global radius monotonicity and all easy-region algebra.
eq('P radius derivative', S.diff(P(y,r,t),r),1-4*u+2*y-2*r)
eq('P second radius derivative', S.diff(P(y,r,t),t),2)
eq('high-y first endpoint',P(1-a,q(a),q(u)).subs(u,(1-a)/2),(1-a)**3*(1+a)/4)
eq('high-y second endpoint',P(1-a,q(a),q(a)).subs(u,(1-a)/2),a*(1-a)*(a*a-a+2)/4)
polys = [14-43*u+14*u*u-u**3, 1-17*u*u+10*u**3-u**4, -u**3+2*u*u+9*u-2]
eq('high-y endpoint a=u',P(1-a,q(u),q(u)).subs(a,u),u*polys[0]/4)
eq('high-y endpoint a=1/2',P(1-a,q(u),q(u)).subs(a,S.Rational(1,2)),polys[1]/4)
eq('high-y endpoint a=1-2u',P(1-a,q(u),q(u)).subs(a,1-2*u),u*polys[2]/4)
for i,pt in enumerate([S.Rational(1,3),S.Rational(1,4),S.Rational(1,4)]):
    positive(f'high-y polynomial {i+1} endpoint sign',polys[i].subs(u,pt))
# Derivative signs as used in the report, without relying on numerical roots.
positive('high-y first polynomial decreasing bound', 43-S.Rational(28,3))
positive('high-y second polynomial decreasing bound', 34-S.Rational(30,4))
positive('high-y third polynomial increasing bound', 9-S.Rational(1,3))
eq('z>=2u endpoint',P(z,q(z),q(u)).subs(u,z/2),z**3*(2-z)/4)
eq('low-y q replacement',P(2*u,q(z),q(u)),q(z)*(1-q(z))-u+3*u*u)
eq('complete square in u',-u+3*u*u,3*(u-S.Rational(1,6))**2-S.Rational(1,12))
eq('new cutoff margin',q(S.Rational(1,4))*(1-q(S.Rational(1,4)))-S.Rational(1,12),S.Rational(5,3072))

# Complete hard-region reduction, with elementary rather than implicit switches.
Ry=z-kappa(z)*(y-z)
eq('affine y concavity',S.diff(P(y,Ry,t),y,2),-2*(1+kappa(z))**2)
eq('constant y slope',S.diff(P(y,beta(z),t),y),1+4*u+2*beta(z)-2*y)
eq('switch upper endpoint',g(S.Rational(1,4)),S.Rational(27,76))
eq('beta derivative',S.diff(beta(z),z),8/(4+3*z)**2)
eq('beta concavity',S.diff(beta(z),z,2),-48/(4+3*z)**3)
R=z-kappa(z)*(2*u-z)
eq('quadratic comparison radius',R,2*z+S.Rational(3,2)*z*z-2*u-3*u*z)
eq('quadratic radius slope',S.diff(R,z),2+3*z-3*u)
eq('quadratic radius curvature',S.diff(R,z,2),3)
eq('composition curvature',S.diff(R*(1-R),z,2),3*(1-2*R)-2*(2+3*z-3*u)**2)
Tu=u-kappa(u)*(z-u)
SwitchP=lambda tt:2*beta(z)+2*tt-(1-z)*(4*u-z)
eq('affine switch slope',S.diff(SwitchP(Tu),u),6*u+z)
eq('baseline switch slope',S.diff(SwitchP(beta(u)),u),16/(4+3*u)**2-4*(1-z))

# Three rational transition signs. B is bounded without a sixth-degree display.
uA=g(z)/2
A=2*(uA-kappa(uA)*(z-uA))-z*(1-z-2*beta(z))
eq('transition A positive expression',A,z*z*(9*z*z+36*z+44)/(4*(3*z+4)**2))
zB=g(u)
RB=S.factor(zB-kappa(zB)*(2*u-zB))
rlow=u*(1-2*u)
eq('transition B radius comparison',RB-rlow,u*u*(9*u*u+6*u+4)/(2*(3*u+4)**2))
eq('transition B cubic sign',rlow*(1-rlow)+2*beta(u)-2*u*(1-2*u),
   u*u*(1+19*u-4*u*u-12*u**3)/(3*u+4))
positive('transition B cubic lower bound',1-4*S.Rational(1,4)**2-12*S.Rational(1,4)**3)
Cexpr=2*(beta(zB)+beta(u))-(1-zB)*(4*u-zB)
Cnum=81*u**4+441*u**3+768*u*u+460*u+48
eq('transition C positive expression',Cexpr,3*u*u*Cnum/((3*u+2)*(3*u+4)**2*(3*u+8)))
assert all(coef>0 for coef in S.Poly(Cnum,u).all_coeffs())
checks.append('transition C positive coefficients')

# Both D local ratio replacements, retaining their geometric assumptions.
theta=S.symbols('theta',real=True)
eq('T3 quadratic reduction',Qcx(x+theta,x),2*x*x+(theta-1)*x+theta)
lower_theta=(1-2*x)/(4*(1-x))
eq('T3 factored bound',Qcx(x+lower_theta,x), (1-2*x)*(4*x*x-3*x+1)/(4*(1-x)))
eq('T3 last quadratic positive',4*x*x-3*x+1,4*(x-S.Rational(3,8))**2+S.Rational(7,16))
eq('Vd1 factored bound',Qcx((3+2*x)/8,x),(1-2*x)*(3-5*x)/8)
positive('sqrt3 upper bound is strict',S.Rational(7,4)**2-3)

# Strict own-ray bound and F's unchanged witnesses.
eq('strict quartic residual',F(1-m,m),-m*((1-m)**3+m*m))
eq('strict triangular residual',H.subs(c,1-m),-d*((1-m)*(1-2*m)+m*(2-m)*d))

# A rejected superficially simpler comparison. Diagnostic value, not an input.
def env_simple(aa: Q, bb: Q) -> Q:
    mm=min(aa,bb);delta=1-aa-bb
    return max(mm/(2+2*mm),mm-(1+2*mm)*delta)
xx=Q(1,8);zz=Q(47,512)
rr=env_simple(1-xx,zz);tt=env_simple(1-zz,xx/2)
failed=2*(rr+tt)-(1-xx+rr)*(xx+rr)
assert failed == -Q(9468353,17179869184)
checks.append('rejected weaker linear-slope envelope exact counterexample')


def envelope(aa: Q, bb: Q) -> Q:
    mm=min(aa,bb);delta=1-aa-bb
    if not (mm>=0 and delta>=0):
        raise ValueError('outside nonsupercritical domain')
    if mm<=Q(1,4):
        return max(2*mm/(4+3*mm),mm-(1+Q(3,2)*mm)*delta)
    return mm*(1-mm)/2

def test_point(xx: Q, yy: Q, zz: Q) -> Q:
    if not (0<xx<=yy<1 and xx/2<=zz<=yy):
        raise ValueError('outside BC domain')
    rr=envelope(1-yy,zz);tt=envelope(1-zz,xx/2)
    pp=2*(rr+tt)-(1-yy+rr)*(2*xx-yy+rr)
    if not pp>0:
        raise AssertionError((xx,yy,zz,rr,tt,pp))
    return pp

def grid(n: int=36) -> tuple[int,Q]:
    count=0;minimum=None
    for X in range(1,n):
        for Y in range(X,n):
            for Z in range(X,2*Y+1):
                value=test_point(Q(X,n),Q(Y,n),Q(Z,2*n))
                minimum=value if minimum is None else min(minimum,value)
                count+=1
    if minimum is None: raise AssertionError('empty grid')
    return count,minimum

def transition_diagnostics() -> int:
    count=0
    for w in [Q(1,4),Q(1,8),Q(1,12),Q(1,16)]+[Q(1,10**j) for j in range(1,13)]:
        be=lambda v:2*v/(4+3*v)
        gg=lambda v:v+be(v)
        # A: choose rational z; u=g(z)/2.
        zz=w;uu=gg(zz)/2
        test_point(2*uu,2*uu,zz);count+=1
        # B and C: choose rational u with g(u)<=1/4.
        uu=w;zz=gg(uu)
        if zz<=Q(1,4):
            test_point(2*uu,2*uu,zz);count+=1
            test_point(2*uu,gg(zz),zz);count+=1
            # Probe both sides of the switch without floating-point arithmetic.
            e=uu*uu/100
            test_point(2*uu,2*uu,zz-e);count+=1
            test_point(2*uu,2*uu,zz+e);count+=1
    return count

if __name__=='__main__':
    print('SymPy',S.__version__)
    for name in checks: print('PASS',name)
    print(f'PASS {len(checks)} exact identity/sign checks')
    count,minimum=grid()
    print(f'PASS rational-grid diagnostic: {count} triples; minimum P={minimum}')
    print(f'PASS exact transition/boundary diagnostics: {transition_diagnostics()} triples')
    print('Grid and transition diagnostics are not proofs. See the analytic report.')
    print('This audit does not substitute for repository CI, PDF builds, or exact zero-gap replay.')


# Source contracts are separate from the algebra: no finite sample certifies
# the underlying universal geometry or the completeness of the domain split.
from pathlib import Path
import hashlib
import json
ROOT = Path(__file__).resolve().parents[3]
PAPER = ROOT / "arrange/paper_draft"
record = json.loads((ROOT / "arrange/_support/quarter_envelope_preservation.json").read_text())
for path, expected in record["unchanged_files"].items():
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == expected, path
for path, hashes in record["reviewed_supplier_hash_changes"].items():
    assert hashes["before"] != hashes["after"], path
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest() == hashes["after"], path
cap = (PAPER/"fixed_witness/D_bc_capacity_envelope.tex").read_text()
assert "m=\\min(a,b)\\le1/4" in cap
for term in ("2m}{4+3m}", "1+\\frac32m"):
    assert term in cap, term
assert "\\frac5{3072}" in cap
assert "selected smaller root" in cap
assert "-18325/1024" in cap and "15/38" in cap
assert "implicit differentiation" not in cap and "\\ell''" not in cap
for path in (PAPER/"D_nonzero_gap_finite_enclosure_optimization.tex",
             PAPER/"inline_proofs/05_nonzero_gap.tex"):
    text = path.read_text()
    for label in ("lem:appendix-t3-supported-tail", "lem:appendix-vd1-supported-tail"):
        pos=text.index("\\label{"+label+"}")
        proof=text[pos:text.index("\\end{proof}",pos)]
        assert "C_1\\ge c" in proof and "\\varepsilon V_1\\in U_C" in proof
        assert "26-15\\sqrt3" not in proof and "1/5\\le\\theta" not in proof
    assert "(1-2x)(3-5x)" in text and "(1-2x)(4x^2-3x+1)" in text
for path in (PAPER/"E_zero_gap_nine_point_optimization.tex",PAPER/"inline_proofs/06_zero_gap.tex"):
    text=path.read_text(); pos=text.index("\\label{lem:symmetric-core-witness}")
    proof=text[pos:text.index("\\end{proof}",pos)]
    assert "lem:strict-own-ray-positive-slack" in proof
    assert "lem:bc-capacity-tools" in proof and "A_*" not in proof
print(f"PASS source contracts: {len(record['unchanged_files'])} preserved files, two reviewed supplier hashes, both editions")
