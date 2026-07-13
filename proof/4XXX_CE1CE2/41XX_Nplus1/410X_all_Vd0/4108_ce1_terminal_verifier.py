#!/usr/bin/env python3
"""Exact verifier for the CE1 two-T+ terminal certificate.

Requires SymPy. Every comparison below is over QQ; no floating point is used.
The printed SHA-256 digests canonicalize a Bernstein tensor by listing its
coefficients in increasing first index, then increasing second index, one
SymPy rational per line, including a final newline.
"""

from hashlib import sha256

import sympy as S


k, alpha, R, A, D, eta = S.symbols("k alpha R A D eta")
x, y = S.symbols("x y")


def bernstein_tensor(poly, variables, box):
    """Return the full-degree tensor on a rational rectangle."""
    u, v = variables
    ulo, uhi, vlo, vhi = map(S.Rational, box)
    p = S.Poly(S.expand(poly), u, v, domain=S.QQ)
    n, m = p.degree_list()
    q = S.Poly(
        S.expand(
            p.as_expr().subs(
                {u: ulo + (uhi - ulo) * x, v: vlo + (vhi - vlo) * y}
            )
        ),
        x,
        y,
        domain=S.QQ,
    )
    ans = []
    for i in range(n + 1):
        for j in range(m + 1):
            ans.append(
                sum(
                    (
                        q.coeff_monomial(x**r * y**s)
                        * S.Rational(S.binomial(i, r), S.binomial(n, r))
                        * S.Rational(S.binomial(j, s), S.binomial(m, s))
                        for r in range(i + 1)
                        for s in range(j + 1)
                    ),
                    S.Rational(0),
                )
            )
    return (n, m), ans


def digest(coefficients):
    """Return the digest of the canonical rational-coefficient listing."""
    payload = "".join(f"{c}\n" for c in coefficients)
    return sha256(payload.encode("ascii")).hexdigest()


# Rationalization E=(1-k+k^2)/(1-k^2), k=R/(1+E).
Rk = k * (2 - k) / (1 - k**2)
Ek = (1 - k + k**2) / (1 - k**2)
etak = k * (1 - 2 * k) / (1 - k**2)
Kk = S.factor(etak * Ek)
Ak = S.factor(alpha * Kk)

# CE1 backward-growth lower bounds.
H = (eta + A + D) / (2 * R)
m = A / R
p1 = (2 - 4 * A) * H - (1 - 4 * A) * A
p2 = (2 - 5 * m) * p1 - (1 - 5 * m) * m
Psi = S.expand(p2 - 2 * D - 3 * D**2)
Psi_k = S.cancel(Psi.subs({R: Rk, eta: etak, A: Ak}))

D0 = S.factor(Kk - Rk * Ak)
Dh = S.factor(Ak * (4 * Rk - 1) + 10 * Rk * Ak**2 - etak)


def positive_endpoint_numerator(endpoint):
    """Extract the endpoint numerator after its known positive factor."""
    value = S.factor(S.cancel(Psi_k.subs(D, endpoint)))
    num, den = S.fraction(value)
    # In both cases value=(1-2k)*Q/positive_denominator.
    q_poly = S.Poly(
        S.expand(S.cancel(num / (1 - 2 * k))), k, alpha, domain=S.QQ
    )
    return value, q_poly, S.factor(den)


v0, Q0, den0 = positive_endpoint_numerator(D0)
vh, Qh, denh = positive_endpoint_numerator(Dh)
assert S.factor(den0 - (k - 2) ** 2 * (k - 1) ** 6 * (k + 1) ** 6) == 0
assert S.factor(denh - (k - 2) ** 2 * (k - 1) ** 10 * (k + 1) ** 10) == 0
assert S.factor(v0 - (1 - 2 * k) * Q0.as_expr() / den0) == 0
assert S.factor(vh - (1 - 2 * k) * Qh.as_expr() / denh) == 0

(deg0, B0) = bernstein_tensor(
    Q0.as_expr(), (k, alpha), (0, S.Rational(1, 2), 0, 1)
)
(degh, Bh) = bernstein_tensor(
    Qh.as_expr(), (k, alpha), (S.Rational(1, 5), S.Rational(1, 2), 0, 1)
)
assert deg0 == (13, 3) and len(B0) == 56
assert sum(1 for c in B0 if c > 0) == 55
assert sum(1 for c in B0 if c == 0) == 1
assert B0[0 * 4 + 3] == 0
assert min(c for c in B0 if c > 0) == S.Rational(2187, 8192)
assert degh == (21, 4) and len(Bh) == 110 and all(c > 0 for c in Bh)
assert min(Bh) == S.Rational(818360091, 28940800000)

# If k<=1/5, Dh<=0. The denominator of Dh is negative and its numerator
# has a nonnegative Bernstein tensor, with only the k=0 row equal to zero.
Dh_num, Dh_den = S.fraction(Dh)
(deg_guard, B_guard) = bernstein_tensor(
    Dh_num, (k, alpha), (0, S.Rational(1, 5), 0, 1)
)
assert deg_guard == (10, 2) and len(B_guard) == 33
assert sum(1 for c in B_guard if c > 0) == 30
assert sum(1 for c in B_guard if c == 0) == 3
assert all(c >= 0 for c in B_guard)
assert S.factor(Dh_den - (k - 1) ** 5 * (k + 1) ** 5) == 0

# D<1/10 certificate.
w = S.factor(1 - Rk)
A0 = S.factor(Kk - w / 10)
Dh_A0 = S.factor(
    (A * (4 * Rk - 1) + 10 * Rk * A**2 - etak).subs(A, A0)
)
g = (
    319 * k**8
    - 1028 * k**7
    + 2002 * k**6
    - 2220 * k**5
    + 1665 * k**4
    - 796 * k**3
    + 128 * k**2
    + 44 * k
    - 14
)
assert S.factor(
    S.Rational(1, 10)
    - Dh_A0
    + k * (k - 2) * g / (10 * (k - 1) ** 5 * (k + 1) ** 5)
) == 0


def bernstein_univariate(poly, lo, hi):
    """Return full-degree Bernstein coefficients on a rational interval."""
    p = S.Poly(S.expand(poly), k, domain=S.QQ)
    n = p.degree()
    q = S.Poly(
        S.expand(p.as_expr().subs(k, lo + (hi - lo) * x)), x, domain=S.QQ
    )
    return [
        sum(
            (
                q.coeff_monomial(x**j)
                * S.Rational(S.binomial(i, j), S.binomial(n, j))
                for j in range(i + 1)
            ),
            S.Rational(0),
        )
        for i in range(n + 1)
    ]


Bg0 = bernstein_univariate(-g, S.Rational(0), S.Rational(3, 8))
Bg1 = bernstein_univariate(-g, S.Rational(3, 8), S.Rational(1, 2))
assert all(c > 0 for c in Bg0 + Bg1)

# Last comparison e(d)<=2d+3d^2 on 0<d<1/10.
d = S.symbols("d")
q2 = 1 - 8 * d + 4 * d**2
M3 = 2 * d + 3 * d**2
assert S.factor((1 - d) ** 2 * q2 - ((1 - d) - 2 * M3) ** 2) == (
    -4 * d**2 * (8 * d**2 + 19 * d - 2)
)

print("D0", deg0, len(B0), min(c for c in B0 if c > 0), digest(B0))
print("Dh", degh, len(Bh), min(Bh), digest(Bh))
print(
    "guard",
    deg_guard,
    len(B_guard),
    sum(1 for c in B_guard if c > 0),
    sum(1 for c in B_guard if c == 0),
)
print("-g [0,3/8]", Bg0)
print("-g [3/8,1/2]", Bg1)
