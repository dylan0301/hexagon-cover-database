"""Check endpoint Taylor coefficient bounds for the May 21/22 Pattern A package.

This script is a reproducibility helper for
`../../962X_may21_four_point_failure/9625_endpoint_taylor_remainder.md`.
It is not a proof by itself.
"""

from __future__ import annotations

import sympy as sp

s = sp.symbols("s", real=True)

A = [
    (2*s - 1)/2,
    -(24*s**2 - 88*s + 35)/8,
    -(200*s**3 + 536*s**2 - 872*s + 331)/16,
    (29824*s**4 + 608*s**3 - 61776*s**2 + 55312*s - 14755)/128,
    -(1338880*s**5 - 2162688*s**4 + 755280*s**3 + 736976*s**2 - 682192*s + 161185)/256,
]

B = [
    sp.Rational(1, 6),
    -(648*s**2 - 1512*s + 361)/216,
    -(48600*s**3 + 14904*s**2 - 36504*s + 13793)/3888,
    (65225088*s**4 - 57643488*s**3 + 3941136*s**2 + 10555056*s - 2777345)/279936,
    -(26353175040*s**5 - 50065993728*s**4 + 38811528432*s**3 - 14526968976*s**2 + 2402830224*s - 99661885)/5038848,
]


def critical_values(poly: sp.Expr, lo: sp.Rational, hi: sp.Rational) -> list[sp.Expr]:
    values: list[sp.Expr] = [lo, hi]
    for root in sp.nroots(sp.diff(poly, s), n=30, maxsteps=200):
        if abs(sp.im(root)) < 1e-25:
            x = sp.N(sp.re(root), 40)
            if sp.N(lo) <= x <= sp.N(hi):
                values.append(x)
    return values


def min_on(poly: sp.Expr, lo: sp.Rational, hi: sp.Rational) -> sp.Expr:
    return min(sp.N(poly.subs(s, x), 40) for x in critical_values(poly, lo, hi))


def max_abs_on(poly: sp.Expr, lo: sp.Rational, hi: sp.Rational) -> sp.Expr:
    return max(abs(sp.N(poly.subs(s, x), 40)) for x in critical_values(poly, lo, hi))


def main() -> None:
    print("Region I: s in [2/3, 1]")
    lo_i, hi_i = sp.Rational(2, 3), sp.Rational(1, 1)
    print("min A1", min_on(A[0], lo_i, hi_i))
    print("min A2", min_on(A[1], lo_i, hi_i))
    print("max |A3|", max_abs_on(A[2], lo_i, hi_i))
    print("min A4", min_on(A[3], lo_i, hi_i))
    print("max |A5|", max_abs_on(A[4], lo_i, hi_i))

    print("Region II: s in [1/2, 167/250]")
    lo_ii, hi_ii = sp.Rational(1, 2), sp.Rational(167, 250)
    print("min B1", min_on(B[0], lo_ii, hi_ii))
    print("min B2", min_on(B[1], lo_ii, hi_ii))
    print("max |B3|", max_abs_on(B[2], lo_ii, hi_ii))
    print("min B4", min_on(B[3], lo_ii, hi_ii))
    print("max |B5|", max_abs_on(B[4], lo_ii, hi_ii))


if __name__ == "__main__":
    main()
