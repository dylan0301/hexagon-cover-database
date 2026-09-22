#!/usr/bin/env python3
"""Exact algebra audit for the accompanying proof of inequality (19).

Requirements: Python 3.10+ and SymPy.
This verifies the polynomial identities and rational sign certificates used
in the analytic proof. It does not replace that proof's concavity reduction
or claim to be a general quantified-inequality solver. No floating point is
used in any check.
"""
from __future__ import annotations
from math import comb
import sympy as S

u, y, z, r, t, a, m, v, c, D = S.symbols('u y z r t a m v c D', real=True)
R = S.Rational
identities = 0
sign_leaves = 0

def equal(lhs, rhs):
    global identities
    assert S.cancel(lhs-rhs) == 0, S.factor(lhs-rhs)
    identities += 1

def bernstein_positive(poly, var, lo, hi, depth=0):
    """A rational Bernstein certificate, with rational subdivision if needed."""
    global sign_leaves
    w = S.Symbol('_w')
    pp = S.Poly(S.expand(poly.subs(var, lo+(hi-lo)*w)), w)
    n = pp.degree()
    if pp.is_zero:
        raise AssertionError('Strict positivity requested for the zero polynomial')
    bc = [sum(pp.nth(j)*R(comb(k,j), comb(n,j)) for j in range(k+1)) for k in range(n+1)]
    if all(q > 0 for q in bc):
        sign_leaves += 1
        return
    if depth >= 12:
        raise AssertionError((poly, lo, hi, bc))
    mid = (lo+hi)/2
    bernstein_positive(poly,var,lo,mid,depth+1)
    bernstein_positive(poly,var,mid,hi,depth+1)

q = lambda s:s*(1-s)/2
b = lambda s:s/2-R(2,5)*s*s
F = lambda C,M:C**4-C**2+M*C-M*M
P = lambda Y,RR,TT:2*(RR+TT)-(1-Y+RR)*(4*u-Y+RR)

# The two lower envelopes for the capacity deficit.
polyq = 64*v**6+64*v**5+496*v**4+480*v**3+1276*v**2+644*v+33
polyb = 262144*v**6+720896*v**5+3174400*v**4+5826560*v**3+11428800*v**2+9721776*v+3049
equal(F(1-q(m),m),m*m*polyq.subs(v,R(1,2)-m)/1024)
equal(F(1-b(m),m),m*m*polyb.subs(v,R(3,8)-m)/10240000)
assert all(coef > 0 for coef in S.Poly(polyq,v).all_coeffs())
assert all(coef > 0 for coef in S.Poly(polyb,v).all_coeffs())
assert (1-b(R(3,8)))**2 > R(3,4)
assert R(3,8)+b(R(3,8)) == R(81,160) > R(1,2)

# Implicit second derivative of c=C_L(m), modulo its defining quartic.
den=4*c**3-2*c+m
cp=(2*m-c)/den
cpp=(2-2*cp-(12*c*c-2)*cp*cp)/den
num=S.cancel(cpp*den**3)
target=2*(8*c*c*m*(c-m)+c*c-c*m+m*m)
assert S.rem(S.Poly(S.expand(num-target),c),S.Poly(F(c,m),c)).is_zero
identities += 1

# Reciprocal H(s) derivatives used for piecewise concavity.
s=S.Symbol('s',positive=True)
f=2/(1+S.sqrt(4*s*s-3))
expr=S.simplify((2*S.diff(f,s)+s*S.diff(f,s,2)/2).subs(S.sqrt(4*s*s-3),D))
num=S.simplify(expr*D**3*(1+D)**3/s)
equal(S.expand(num).subs(s*s,(D*D+3)/4),4*(-2*D**3-4*D**2+9*D+3))
# -2D^3-4D^2+9D+3 >= 3D+3 for 0<=D<=1.
equal((-2*D**3-4*D**2+9*D+3)-(3*D+3),2*D*(1-D)*(D+3))

# Upper quadratic envelope in the L cell.
B=S.Symbol('B',real=True)
ss=a+B
lhs=a*a-a*c+c*c-c*c*ss*ss
rhs=(c-ss)*(c*c*(c+ss)-(a-B))
equal(lhs-rhs, -(c**4-c*c+B*c-B*B))

# Easy region y>=1/2.
Qa=q(a);Qu=q(u)
equal(P(1-a,Qa,Qu).subs(u,(1-a)/2),(1-a)**3*(1+a)/4)
equal(P(1-a,Qa,Qa).subs(u,(1-a)/2),a*(1-a)*(a*a-a+2)/4)
equal(P(1-a,Qu,Qu).subs(a,u),u*(14-43*u+14*u*u-u**3)/4)
equal(P(1-a,Qu,Qu).subs(a,R(1,2)),(1-17*u*u+10*u**3-u**4)/4)
equal(P(1-a,Qu,Qu).subs(a,1-2*u),u*(-u**3+2*u*u+9*u-2)/4)
bernstein_positive(14-43*u+14*u*u-u**3,u,R(0),R(1,3))
bernstein_positive(1-17*u*u+10*u**3-u**4,u,R(0),R(1,4))
bernstein_positive(-u**3+2*u*u+9*u-2,u,R(1,4),R(1,3))
# Easy region z>=2u, y<=1/2.
equal(P(z,q(z),q(u)).subs(u,z/2),z**3*(2-z)/4)

# P on the boundary y=2u.
equal(P(2*u,r,t),r*(1-r)+2*t-2*u*(1-2*u))

# Transition A: y=2u=z+ell(z).
uA=(z+r)/2
tau=z*(1-z-2*r)/2
GA=S.expand(uA*(1-uA)-z*(1-z-2*r))
equal(GA,(-r*r+6*r*z+2*r+3*z*z-2*z)/4)
HA=-16*z**3-200*z*z+495*z-100
equal(GA.subs(r,b(z)),z*HA/400)
bernstein_positive(HA,z,R(1,4),R(3,8))
A=1-z;ss=1-(z-r)/2;C=1-tau
FTA=(ss*ss-1)*C*C+A*C-A*A
PA=256*z**8-640*z**7-3120*z**6+10320*z**5-6500*z**4+3700*z**3+19225*z*z-83500*z+26500
equal(FTA.subs(r,b(z)),z*z*PA/40000)
bernstein_positive(PA,z,R(0),R(1,4))
assert 26500-R(83500,4)-R(6500,4**4)-R(3120,4**6)-R(640,4**7)>0

# Transition B: z=u+ell(u), y=2u.
v0=b(u);z0=u+v0
Rsmall=u-R(9,5)*u*u
A=1-2*u;ss=A+z0;C=1-Rsmall
PB=1296*u**6+1800*u**5-6215*u**4+650*u**3+1075*u*u-16750*u+3125
equal((ss*ss-1)*C*C+A*C-A*A,u*u*PB/2500)
bernstein_positive(PB,u,R(0),R(1,6))
assert 3125-R(16750,6)-R(6215,6**4)>0
equal(Rsmall*(1-Rsmall)+2*v0-2*u*(1-2*u),u*u*(10+90*u-81*u*u)/25)
bernstein_positive(10+90*u-81*u*u,u,R(0),R(1,6))
Q=1024*u**7-15360*u**6+92800*u**5-288000*u**4+498500*u**3-532500*u*u-384375*u+62500
Rlarge=b(z0)
equal(Rlarge*(1-Rlarge)+2*v0-2*u*(1-2*u),-u*Q/250000)
bernstein_positive(-Q,u,R(1,6),R(1,4))
assert Q.subs(u,R(1,6)) == -R(31179862,2187)
assert R(7168,4**6)+R(464000,4**4)+R(1495500,4**2)-384375 == -289092

# Transition C: both capacities at their L/T boundaries.
equal(2*(b(z0)+v0)-(1-z0)*(4*u-z0),u*u*(175+280*u-144*u*u)/500)
bernstein_positive(175+280*u-144*u*u,u,R(0),R(1,4))

# (19) implies (16).
k=S.Symbol('k',real=True)
equal((1-k/2+k*k/2)**2-(1-k+k*k),k*k*(1-k)**2/4)

print(f'PASS: {identities} exact identities and {sign_leaves} rational Bernstein sign-certificate leaves.')
print('The associated analytic proof supplies domain coverage and the concavity/monotonicity reductions.')
