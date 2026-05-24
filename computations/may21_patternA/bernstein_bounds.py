"""Prototype Bernstein bounds for low-dimensional polynomial boxes.

This module is a helper for the May 21/22 Pattern A certificate prototype.
It currently implements exact univariate power-to-Bernstein conversion.
A full production certificate should add cached multivariate de Casteljau
subdivision.
"""

from __future__ import annotations

from math import comb
from typing import Iterable

import sympy as sp


def power_to_bernstein_1d(power_coeffs: Iterable[sp.Expr], a: sp.Expr, b: sp.Expr) -> list[sp.Expr]:
    """Convert a univariate power-basis polynomial to Bernstein coefficients.

    `power_coeffs[k]` is the coefficient of x**k.  The output is the list of
    Bernstein coefficients on the interval [a,b].
    """
    coeffs = list(power_coeffs)
    n = len(coeffs) - 1
    t = sp.symbols("t")
    x = a + (b - a) * t
    poly_t = sp.expand(sum(coeffs[k] * x**k for k in range(n + 1)))
    power_t = [sp.expand(poly_t).coeff(t, k) for k in range(n + 1)]

    # Power-to-Bernstein triangular relation:
    # p(t)=sum_i b_i C(n,i)t^i(1-t)^{n-i}.
    bern: list[sp.Expr] = []
    for k in range(n + 1):
        val = power_t[k]
        for i in range(k):
            val -= bern[i] * comb(n, i) * comb(n - i, k - i) * (-1) ** (k - i)
        val /= comb(n, k)
        bern.append(sp.simplify(val))
    return bern


def bernstein_bounds_1d(poly_expr: sp.Expr, var: sp.Symbol, a: sp.Expr, b: sp.Expr) -> tuple[sp.Expr, sp.Expr]:
    poly = sp.Poly(poly_expr, var)
    coeffs = [poly.coeff_monomial(var**k) for k in range(poly.degree() + 1)]
    bern = power_to_bernstein_1d(coeffs, sp.Rational(a), sp.Rational(b))
    return min(bern), max(bern)


def sign_certify_1d(poly_expr: sp.Expr, var: sp.Symbol, a: sp.Expr, b: sp.Expr) -> str:
    lo, hi = bernstein_bounds_1d(poly_expr, var, a, b)
    if lo > 0:
        return "positive"
    if hi < 0:
        return "negative"
    return "unknown"


def demo() -> None:
    x = sp.symbols("x")
    p = (x - sp.Rational(1, 3)) ** 2 + sp.Rational(1, 10)
    print("demo sign on [0,1]:", sign_certify_1d(p, x, 0, 1))


if __name__ == "__main__":
    demo()
