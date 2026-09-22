#!/usr/bin/env python3
"""Exact identities and rational support-selection regression tests for 2616.

The written proof supplies the universal domains and exhaustive hull argument.
Finite rational test cases are regression checks, not a substitute for that proof.
"""
from __future__ import annotations
import sympy as S
from fractions import Fraction
from random import Random

x,y,r,t,v,s=S.symbols('x y r t v s', real=True)
h=S.sqrt(3)/2
R=S.Matrix([[-S.Rational(1,2),-h],[h,-S.Rational(1,2)]])
identities=[]
def identity(label, expr):
    assert S.factor(expr)==0, (label,S.factor(expr))
    identities.append(label)
identity('BC MGx lower caliper',(1-x+2*x*x)**2-(1-2*x+4*x*x)-x*x*(2*x-1)**2)
identity('BC QM lower caliper',(1+t+2*t*t)**2-(1+2*t+4*t*t)-t*t*(1+2*t)**2)
g=v+S.Rational(1,2)+1/(2*(1+v))
identity('BC radial edge',g*g-(1+v+v*v)-v*v/(4*(1+v)**2))
identity('BC square root envelope',(1-x/2+x*x/2)**2-(1-x+x*x)-x*x*(1-x)**2/4)
V1=S.Matrix([S.Rational(1,2),h]); V4=-V1
Gy=S.Matrix([1-y/2,h*y]); M=S.Matrix([S.Rational(1,2),0])
identity('BC clipping diameter',(Gy-(1-y)*V4).dot(Gy-(1-y)*V4)-1-(1-y)*(2-y))
identity('D diameter',(S.Matrix([1,0])-s*V1).dot(S.Matrix([1,0])-s*V1)-(1-s+s*s))
points=[M,S.Matrix([1-x/2,h*x]),Gy,S.Matrix([-r/2,h*r]),S.Matrix([-t/2,-h*t])]
k=y-r
normals=[S.Matrix([2*h*x,x-1]),S.Matrix([h,S.Rational(1,2)]),S.Matrix([-h*k,1-k/2]),S.Matrix([-h*(r+t),(t-r)/2]),S.Matrix([2*h*t,-1-t])]
den=[1-2*x+4*x*x,S.Integer(1),1-k+k*k,r*r+r*t+t*t,1+2*t+4*t*t]
for i,n in enumerate(normals):identity(f'BC normal squared {i}',n.dot(n)-den[i])
# All supports divided by h are rational polynomials at rational data.
projections=[[[S.simplify(p.dot(R**j*n)/h) for p in points] for j in range(3)] for n in normals]
nums=[1-x+2*x*y+S.Max(r*(1-2*x),2*t*x),1+r+t,r+t+S.Max(S.Rational(1,2),1-x*(1-k)),r*t+t+r*y+S.Max(r/2,r-(r+t)*x,t*t),1+t+2*t*y+S.Max(r,2*t*t)]
rng=Random(2616); count=0
for _ in range(48):
    yy=S.Rational(rng.randint(2,98),100)
    xx=yy*S.Rational(rng.randint(1,10),10)
    rr=min(yy,1-yy)*S.Rational(rng.randint(1,10),10)
    tt=xx*S.Rational(rng.randint(1,10),20)
    val={x:xx,y:yy,r:rr,t:tt}
    for i,dirs in enumerate(projections):
        actual=sum(max(q.subs(val) for q in row) for row in dirs)
        assert S.simplify(actual-nums[i].subs(val))==0,(i,val,actual)
    count+=1
# D: exact identities for the asserted active triples and all four norms.
O=S.zeros(2,1); Q=S.Matrix([1-v/2,-h*v]); A=S.Matrix([1-s*v/2,-h*s*v]); P=s*(1-v)*V1
Dpts=[O,Q,A,P]
Dns=[S.Matrix([-h*v,v/2-1]),v*(1-s)*S.Matrix([h,-S.Rational(1,2)]),S.Matrix([h*s,1-s/2]),s*(1-v)*S.Matrix([-h,S.Rational(1,2)])]
triples=[(0,2,3),(2,3,0),(2,0,1),(0,1,2)]
expected_num=[S.Integer(1),v*(1-s)*(1+s*(1-v)),S.Integer(1),s*(1-v)*(1+v*(1-s))]
for i,n in enumerate(Dns):
    w=sum(Dpts[ind].dot(R**j*n)/h for j,ind in enumerate(triples[i]))
    identity(f'D support sum {i}',w-expected_num[i])
for ss in [S.Rational(1,9),S.Rational(1,2),S.Rational(8,9)]:
 for vv in [S.Rational(1,9),S.Rational(1,2),S.Rational(8,9)]:
  for i,n in enumerate(Dns):
   for j,ind in enumerate(triples[i]):
    dots=[S.simplify(p.dot(R**j*n)/h).subs({s:ss,v:vv}) for p in Dpts]
    assert dots[ind]==max(dots)
print(f'PASS: {len(identities)} exact caliper identities; {count} rational BC support cases; 9 rational D support cases.')
print('Analytic domain coverage and hull completeness are supplied by 2616, not by sampling.')
