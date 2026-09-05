#!/usr/bin/env python3
"""Exact algebraic checks for the four-contact wrapper, not sampling.

This supplements, and never replaces, the two authenticated zero-gap
certificate verifiers. It changes no archived polynomial data.
"""
from __future__ import annotations
import sympy as s

x, y, u, v, e, e0 = s.symbols("x y u v e e0", real=True)
h = s.sqrt(3)/2
A, C = s.Matrix([x,y]), s.Matrix([u,v])
J = s.Matrix([[0,-1],[1,0]])
R = s.Matrix([[-s.Rational(1,2),-h],[h,-s.Rational(1,2)]])
Y = R.T*C
cross = lambda a,b: s.det(s.Matrix.hstack(a,b))
Delta, nu = cross(C,R*A), C.dot(R*A)
NA, NC = A.dot(A), C.dot(C)
checks = {}
checks["oriented determinant crosswalk"] = cross(A,Y)+Delta
checks["Gram identity"] = NA*NC-nu**2-Delta**2
for name,N,X,Z in [("A",NA,A,Y),("C",NC,Y,A)]:
    eta = h*e
    P = (N-eta**2)*Delta**2-((h-2*eta)*N-eta*nu)**2
    Q = (Delta/h)**2-((1-2*e)*X-e*Z).dot((1-2*e)*X-e*Z)
    checks[f"{name} residual factor"] = P-h**2*N*Q
r = s.symbols("r", real=True)
eta = h*e
tA = (eta*A-r*J*A)/NA
tC = (eta*C+r*J*C)/NC
checks["A tangent projection"] = NA*C.dot(R*tA)-eta*nu-r*Delta
checks["C tangent projection"] = NC*A.dot(R.T*tC)-eta*nu-r*Delta
lam = (e-e0)/(s.Rational(1,3)-e0)
for name,X,Z in [("A",A,Y),("C",Y,A)]:
    diff = (1-2*e)*X-e*Z-((1-lam)*((1-2*e0)*X-e0*Z)+lam*(X-Z)/3)
    for i in range(2): checks[f"{name} affine transfer coordinate {i}"] = diff[i]
for name,expr in checks.items():
    if s.cancel(s.expand(expr)) != 0:
        raise AssertionError(name)
print(f"four-contact identities: OK ({len(checks)} exact identities)")
