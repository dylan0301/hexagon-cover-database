"""Exact sub-case thresholds: tangency conditions at the master corners.

P1 = A + (1,0) = (1 - a/2, sqrt3 a/2)   [on cA1, LA, EP(A|O)]
P2 = B + (1-b) u60 = ((1+b)/2, sqrt3(1-b)/2)  [on LA, EP(B|A), EP(B|O)]
P3 = B + u120 = (b - 1/2, sqrt3/2)      [on LB, cB1, EP(B|O)]
P2' = A + (1-a) u60                      [on LB, EP(A|B), EP(A|O)]
"""
import sympy as sp

a, b, X, Y = sp.symbols('a b X Y', real=True, nonnegative=True)
s3 = sp.sqrt(3)

# quartics from exact.py (times 3)
epAO = (3*X**4 + 6*X**3*a + 6*X**2*Y**2 - 2*s3*X**2*Y*a + 3*X**2*a**2
        - 3*X**2 + 6*X*Y**2*a - 2*s3*X*Y*a**2 - 3*X*a + 3*Y**4
        - 2*s3*Y**3*a + Y**2*a**2 - 3*Y**2 + 3*s3*Y*a - 3*a**2)
epBO = (3*X**4 - 6*X**3*b + 6*X**2*Y**2 + 2*s3*X**2*Y*b + 3*X**2*b**2
        - 3*X**2 - 6*X*Y**2*b - 2*s3*X*Y*b**2 + 6*X*b + 3*Y**4
        + 2*s3*Y**3*b + Y**2*b**2 - 3*Y**2 - 3*b**2)
epBA = (3*X**4 + 6*X**3*a - 6*X**3*b + 6*X**2*Y**2 - 2*s3*X**2*Y*a
        + 2*s3*X**2*Y*b + 3*X**2*a**2 - 12*X**2*a*b + 3*X**2*b**2 - 3*X**2
        + 6*X*Y**2*a - 6*X*Y**2*b - 2*s3*X*Y*a**2 + 4*s3*X*Y*a*b
        - 2*s3*X*Y*b**2 - 6*X*a**2*b + 6*X*a*b**2 + 6*X*b + 3*Y**4
        - 2*s3*Y**3*a + 2*s3*Y**3*b + Y**2*a**2 - 8*Y**2*a*b + Y**2*b**2
        - 3*Y**2 + 2*s3*Y*a**2*b - 2*s3*Y*a*b**2 + 3*a**2*b**2 - 3*b**2)
epAB = (3*X**4 + 6*X**3*a - 6*X**3*b + 6*X**2*Y**2 - 2*s3*X**2*Y*a
        + 2*s3*X**2*Y*b + 3*X**2*a**2 - 12*X**2*a*b + 3*X**2*b**2 - 3*X**2
        + 6*X*Y**2*a - 6*X*Y**2*b - 2*s3*X*Y*a**2 + 4*s3*X*Y*a*b
        - 2*s3*X*Y*b**2 - 6*X*a**2*b + 6*X*a*b**2 - 3*X*a + 3*Y**4
        - 2*s3*Y**3*a + 2*s3*Y**3*b + Y**2*a**2 - 8*Y**2*a*b + Y**2*b**2
        - 3*Y**2 + 2*s3*Y*a**2*b - 2*s3*Y*a*b**2 + 3*s3*Y*a + 3*a**2*b**2
        - 3*a**2)

P1 = (1 - a/2, s3*a/2)
P2 = ((1 + b)/2, s3*(1 - b)/2)
P3 = (b - sp.Rational(1, 2), s3/2)
P2p = ((1 - a)/2 - a/2 + sp.Rational(0), None)  # A + (1-a)u60 computed below
P2p = (-a/2 + (1 - a)/2, s3*a/2 + s3*(1 - a)/2)

uLA = (s3/2, sp.Rational(1, 2))   # normal of LA (<x,u>=h)
uLB = (0, 1)

def on_curve(F, P):
    return sp.simplify(F.subs({X: P[0], Y: P[1]}))

def tangency(F, P, un):
    """gradient of F at P parallel to normal un <=> grad . un_perp = 0"""
    gx = sp.diff(F, X).subs({X: P[0], Y: P[1]})
    gy = sp.diff(F, Y).subs({X: P[0], Y: P[1]})
    # un_perp = (-un_y, un_x)
    return sp.simplify(-un[1]*gx + un[0]*gy)

print('--- P1 on epAO:', on_curve(epAO, P1))
print('--- P2 on epBA:', on_curve(epBA, P2))
print('--- P2 on epBO:', on_curve(epBO, P2))
print('--- P3 on epBO:', on_curve(epBO, P3))
print('--- P2p on epAB:', on_curve(epAB, P2p))
print('--- P2p on epAO:', on_curve(epAO, P2p))
print()
print('E1  (epAO tangent to LA at P1):', sp.factor(tangency(epAO, P1, uLA)))
print('E2  (epBA tangent to LA at P2):', sp.factor(tangency(epBA, P2, uLA)))
print('E2b (epBO tangent to LA at P2):', sp.factor(tangency(epBO, P2, uLA)))
print('E1b (epBO tangent to LB at P3):', sp.factor(tangency(epBO, P3, uLB)))
print('E2p (epAB tangent to LB at P2p):', sp.factor(tangency(epAB, P2p, uLB)))
print('E2q (epAO tangent to LB at P2p):', sp.factor(tangency(epAO, P2p, uLB)))
