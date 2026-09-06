#!/usr/bin/env python3
"""Exact algebraic regression tests for the new fixed-witness identities.

These tests do not certify the inherited local admissible-set formulas,
conditional CE1 return, or zero-gap polynomial certificate.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
import sympy as sp


def main() -> int:
    R, alpha, delta, eta = sp.symbols('R alpha delta eta', real=True)
    W = 1-R
    Q = (eta+alpha+delta)/(2*R)
    L1 = (2-4*alpha)*Q-(1-4*alpha)*alpha
    rhs = (1-2*alpha)*eta+(W-2*alpha)*(alpha+delta)+4*R*alpha**2
    checks: dict[str, bool] = {}
    checks['CE1 first-step bridge identity'] = sp.factor(R*(L1-delta)-rhs) == 0
    h = sp.sqrt(3)/2
    V0=sp.Matrix([1,0]); V1=sp.Matrix([sp.Rational(1,2),h])
    V2=sp.Matrix([-sp.Rational(1,2),h]); V4=sp.Matrix([-sp.Rational(1,2),-h])
    V5=sp.Matrix([sp.Rational(1,2),-h])
    t,d2,d4 = sp.symbols('t d2 d4', positive=True)
    G=(1-t)*V0+t*V1
    checks['origin in path-witness hull identity'] = all(sp.simplify(z)==0 for z in G+(1-t)/d2*(d2*V2)+(d4*V4)/d4)
    a, eps=sp.symbols('a eps', positive=True); s=a+eps
    Y=(1-a)*V0+a*V5
    checks['rescuer convex-combination identity'] = all(sp.simplify(z)==0 for z in eps/s*Y+a/s*(eps*V1)-eps/s*V0)
    P=sp.sqrt(3)/2-sp.Rational(3,4)
    A=sp.Rational(1,100); D=sp.Rational(3,20)
    checks['bare CE1 domain does not imply delta < 1/10'] = bool(A+D/2<P and A/2+D>=P and D>sp.Rational(1,10))
    # With W=1-R, the CE1 elimination uses 1-RW=E^2.
    checks['CE1 weighted elimination coefficient'] = sp.expand(1-R*W-(1-R+R**2))==0
    # The inequality at the end of the four-point proof uses only s<=1.
    ss,rr=sp.symbols('s rr', real=True)
    checks['rescuer support comparison identity'] = sp.expand((a/ss-(a+rr*(1-ss)))-(1-ss)*(a/ss-rr))==0
    result={'scope':'exact identities and one hypothesis-regression example only', 'checks':checks, 'passed':all(checks.values())}
    print(json.dumps(result, indent=2))
    return 0 if result['passed'] else 1

if __name__=='__main__':
    raise SystemExit(main())
