#!/usr/bin/env python3
"""Retained wider-range algebra (2615a); the active quarter-range proof
is audited by verify_quarter_envelope_revision.py.

Exact algebra audit for the rational envelope and simplified BC checks.

Requires SymPy. Run: python verify.py
This audits identities and rational sign bounds. The accompanying PROOF.md
supplies the analytic envelope argument and explains which domain reduction
is reused from the preceding inequality-(19) proof.
"""
import sympy as S
m,c,u,z,r,v,w,D,s=S.symbols('m c u z r v w D s',real=True)
b=lambda x:x/2-S.Rational(2,5)*x**2
K=lambda x:(5+4*x)/(5-4*x)
checks=[]
def eq(name,a,bv=0):
    assert S.cancel(S.together(a-bv))==0,name
    checks.append(name)
F=c**4-c**2+m*c-m**2
H=256*m**6-1280*m**5+4960*m**4-11600*m**3+20625*m**2-21000*m+5500
eq('quartic baseline substitution',F.subs(c,1-b(m)),m**2*H/10000)
eq('baseline coefficient',K(m),(m-b(m))/b(m))
assert H.subs(m,S.Rational(3,8))==S.Rational(3049,1024)
assert 1536*S.Rational(3,8)**5+19840*S.Rational(3,8)**3+41250*S.Rational(3,8)-21000== -S.Rational(286311,64)
assert (1-b(S.Rational(3,8)))**2>S.Rational(3,4)
checks+=['positive baseline polynomial by decreasing H','tested c above sqrt(3)/2']
# Convexity of M*j(s), with M>=s/2.
jprime=-8*s/(D*(1+D)**2)
jsecond=24/(D**3*(1+D)**2)+64*s**2/(D**2*(1+D)**3)
eq('convexity numerator',(2*jprime+s*jsecond/2).subs(s**2,(D**2+3)/4),
   4*s*(-2*D**3-4*D**2+9*D+3)/(D**3*(1+D)**3))
eq('convexity numerator positive',-2*D**3-4*D**2+9*D+3,
   3*D+3+2*D*(1-D)*(D+3))
# A: u=(z+r)/2, t>=u-K(u)*(z-u).
line=u-K(u)*(z-u)
eq('A monotonicity derivative',S.diff(line,u),10*(5-4*z)/(5-4*u)**2)
Aexpr=(2*line-z*(1-z-2*r)).subs(u,(z+r)/2)
AA=75-230*z+100*z**2-16*z**3
eq('A reduced rational residual',Aexpr.subs(r,b(z)),z**2*AA/(5*(25-15*z+4*z**2)))
assert AA.subs(z,S.Rational(3,8))==S.Rational(63,32)
assert -230+200*S.Rational(3,8)<0
checks+=['A cubic positive on [0,3/8]']
# B: z=u+v, r>=z-K(z)*(2u-z).
R=(z-K(z)*(2*u-z)).subs(z,u+v)
eq('B monotonicity derivative',S.diff(R,v),10*(5-8*u)/(5-4*u-4*v)**2)
R0=u*(25-80*u+16*u**2)/((5-2*u)*(5-4*u))
eq('B positive radius',R.subs(v,b(u)),R0)
Bexpr=R*(1-R)+2*v-2*u*(1-2*u)
BB=625+4500*u-18400*u**2+5440*u**3-256*u**4
eq('B reduced rational residual',Bexpr.subs(v,b(u)),u**2*BB/(5*(5-2*u)**2*(5-4*u)**2))
# On 0<=u<=1/4: u^2<=u/4 and 256u^4<=1; hence BB>=624-100u>=599.
assert 624-100*S.Rational(1,4)==599
assert 25-80*S.Rational(1,4)>0
checks+=['B quartic lower bound 599','B radius numerator positive']
# C: r>=b(z), z=u+v, v>=b(u).
Cexpr=(2*(b(z)+v)-(1-z)*(4*u-z)).subs(z,u+v)
eq('C monotonicity derivative',S.diff(Cexpr,v),4+4*u-S.Rational(18,5)*(u+v))
eq('C reduced polynomial',Cexpr.subs(v,b(u)),u**2*(175+280*u-144*u**2)/500)
assert 175-144*S.Rational(1,4)**2>0
checks+=['C residual positive']
# Demonstrate the old quarter bound is insufficient by substitution.
qres=(r*(1-r)+2*v-2*u+4*u**2).subs({r:u/3,v:u/4})
eq('quarter-bound failure',qres,-S.Rational(7,6)*u+S.Rational(35,9)*u**2)
print(f'PASS: {len(checks)} exact identities and rational sign checks.')
for i,name in enumerate(checks,1): print(f'{i:02d}. {name}')
print('No numerical sampling is used. Read 2615_slack_sensitive_radial_envelope.md for analytic hypotheses and scope.')
