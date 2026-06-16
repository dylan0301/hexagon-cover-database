"""Symbolic identity checks for the strict branch line-realization proof.

The file 3105 contains the human-readable proof. This script verifies the
main algebraic identities used there with SymPy. It is a proof-helper, not a
replacement for the sign arguments in the Markdown file.
"""

from __future__ import annotations

import sympy as sp


def assert_zero(expr: sp.Expr, name: str) -> None:
    simplified = sp.simplify(sp.factor(sp.together(expr)))
    if simplified != 0:
        raise AssertionError(f"{name} did not simplify to zero: {simplified}")
    print(f"ok: {name}")


def reduce_relation(expr: sp.Expr, D: sp.Symbol, D2_expr: sp.Expr) -> sp.Expr:
    """Reduce a rational expression modulo D^2 = D2_expr."""
    num, den = sp.fraction(sp.together(expr))
    poly = sp.Poly(sp.expand(num), D)
    rel = sp.Poly(D * D - D2_expr, D)
    rem = poly.rem(rel).as_expr()
    return sp.simplify(sp.factor(sp.together(rem / den)))


def assert_zero_rel(expr: sp.Expr, name: str, D: sp.Symbol, D2_expr: sp.Expr) -> None:
    reduced = reduce_relation(expr, D, D2_expr)
    if reduced != 0:
        raise AssertionError(f"{name} did not reduce to zero: {reduced}")
    print(f"ok: {name}")


def main() -> None:
    a, b, D = sp.symbols("a b D")
    h = sp.sqrt(3) / 2
    rho = a * a + a * b + b * b
    D2 = 4 * rho - 3

    alpha = h * (a + 2 * b - a * D) / (2 * rho)
    beta = h * (a - b + (a + b) * D) / (2 * rho)
    gamma = h * (-a + b + (a + b) * D) / (2 * rho)
    delta = h * (2 * a + b - b * D) / (2 * rho)

    assert_zero(
        (a + b) ** 2 * D2 - (a - b) ** 2 - 4 * (a + b - 1) * (a + b + 1) * rho,
        "beta/gamma positivity square identity",
    )
    assert_zero(beta + delta - h * a * (D + 3) / (2 * rho), "beta plus delta")
    assert_zero(alpha + gamma - h * b * (D + 3) / (2 * rho), "alpha plus gamma")

    lam = 8 * h * rho / (3 * (D + 3))
    assert_zero_rel(lam - 2 * h * (D * D + 3) / (3 * (D + 3)), "lambda star formula in D", D, D2)
    assert_zero_rel(lam * (beta + delta) - a, "junction u-coordinate", D, D2)
    assert_zero_rel(lam * (alpha + gamma) - b, "junction v-coordinate", D, D2)

    assert_zero(
        a * a * D2 - (a + 2 * b - 2 * rho) ** 2 - 4 * (1 - b) * (a + b - 1) * rho,
        "alpha endpoint bound identity",
    )
    assert_zero(
        b * b * D2 - (2 * a + b - 2 * rho) ** 2 - 4 * (1 - a) * (a + b - 1) * rho,
        "delta endpoint bound identity",
    )
    assert_zero(
        (2 * a * rho - a + b) ** 2 - (a + b) ** 2 * D2 - 4 * (a - 1) * (a + 1) * rho * (rho - 1),
        "lower u endpoint identity",
    )

    print("all symbolic identity checks passed")


if __name__ == "__main__":
    main()
