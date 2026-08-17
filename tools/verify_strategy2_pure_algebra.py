#!/usr/bin/env python3
"""Exact symbolic checks for the pure Strategy 2 interface.

This is not a numerical optimizer and does not replace the written inequality
proofs.  It verifies the algebraic substitutions, radical equations, dual
records, and polynomial identities used to detach those proofs from geometry.
"""

from __future__ import annotations

import sympy as sp

CHECKS: list[str] = []


def zero(name: str, expression: sp.Expr) -> None:
    value = sp.factor(sp.together(expression))
    if value != 0:
        raise AssertionError(f"{name}: expected zero, found {value}")
    CHECKS.append(name)


def equal_mod_metric(name: str, expression: sp.Expr, e: sp.Symbol, metric: sp.Expr) -> None:
    numerator = sp.together(expression).as_numer_denom()[0]
    remainder = sp.Poly(numerator, e).rem(sp.Poly(metric, e)).as_expr()
    zero(name, remainder)


r, a, d, e = sp.symbols("r a d e")
w = 1 - r
metric = e**2 - (1 - r * w)
eta = 1 - e
p = e * (1 - e)
k = eta + a + d
delta_r = p - a - w * d
delta_l = p - r * a - d

# S2-E1 substitution.
s = k / r
u = r - d
omega = w + d - k / r
zero("E1 residual identity", sp.factor(omega - delta_r / r).subs(e**2, 1 - r * w))
gamma = u - r / (1 + e) - r * omega / w
equal_mod_metric("E1 center-line gamma", gamma - a / w, e, metric)
zero("E1 right demand", u / r - (1 - d / r))
equal_mod_metric("E1 left demand", 1 - gamma - (1 - a / w), e, metric)

# S2-E2 strict kernel identities.
alpha = (w - a) / w
p_end = w - a
beta = (r - d) / r
q_end = r - d
equal_mod_metric(
    "E2 left strict kernel",
    beta + p_end - 1 - w / (1 + e) - delta_l / r,
    e,
    metric,
)
equal_mod_metric(
    "E2 right strict kernel",
    alpha + q_end - 1 - r / (1 + e) - delta_r / w,
    e,
    metric,
)
zero("E2 left endpoint graph", p_end - w * alpha)
zero("E2 right endpoint graph", q_end - r * beta)

# Primitive capped-map identities.
c, x = sp.symbols("c x")
d_plus = (2 * x * c**2 + c) ** 2 - 4 * (1 - c**2) * (1 - x**2) * c**2
zero(
    "Qplus discriminant factorization",
    d_plus - c**2 * (4 * x**2 + 4 * c * x + 4 * c**2 - 3),
)
zero(
    "Qplus lower-bound endpoint",
    (4 * x**2 + 4 * c * x + 4 * c**2 - 3).subs(x, 1 - c) - (2 * c - 1) ** 2,
)
zero(
    "Qminus cap square gap",
    c**2 - (x**2 - c * x + c**2) - x * (c - x),
)

# T3 radical parameterization.
tau, z, b = sp.symbols("tau z b")
t3_metric = z**2 - (1 - tau + tau**2)
d_t = 1 / z
r_t = tau / z
alpha_t = b
p_t = z - b
q_t = 1 - p_t
q = 1 - z + b
c_star = q / tau
u_star = 1 + b - tau
equal_mod_metric(
    "T3 Type-II metric", r_t**2 - d_t * r_t + d_t**2 - 1, z, t3_metric
)
zero("T3 side sum", alpha_t + p_t - 1 / d_t)
zero("T3 q graph", q_t - q)
zero("T3 radial near endpoint", d_t * q_t / r_t - c_star)
zero("T3 radial far endpoint", q_t + (1 - r_t) / d_t - u_star)
equal_mod_metric("T3 order square gap", z**2 - tau**2 - (1 - tau), z, t3_metric)

# T3-like adjacent-support rational cell.
theta, y = sp.symbols("theta y")
rho = (1 - 2 * theta) / (1 - theta**2)
a_t = y * rho
c_t = y + theta
u_t = 1 - rho + a_t
zero("T3 adjacent support residual", 1 - u_t - (1 - y) * rho)
zero("T3 adjacent support ratio", a_t / (a_t + 1 - u_t) - y)
phi = y * (2 - y) / (1 + y)
q_theta = 2 * y**2 + (theta - 1) * y + theta
zero("T3 adjacent support envelope polynomial", c_t - phi - q_theta / (1 + y))

# Vd1 adjacent-support graph.
t, aa, bb, cc, delta = sp.symbols("t aa bb cc delta")
bb_graph = 1 - cc * (t + 1) / t
u_v = (delta - aa - t * bb - 1) / t
epsilon = 1 - sp.factor(u_v.subs(bb, bb_graph))
epsilon0 = (2 * t + 1 - cc * (t + 1) - delta) / t
g_fun = delta - 1 - sp.Rational(3, 2) * t + cc * (t + 1)
zero("Vd1 adjacent support epsilon decomposition", epsilon - epsilon0 - aa / t)
zero("Vd1 adjacent support endpoint half", epsilon0 + g_fun / t - sp.Rational(1, 2))
zero("corner radical strict gap", (t + 1) ** 2 - (t**2 + t + 1) - t)
zero("corner derivative strict gap", 4 * (t**2 + t + 1) - (2 * t + 1) ** 2 - 3)

# Adjacent and nonadjacent Vd algebra.
zero(
    "adjacent quarter identity",
    (2 - 3 * r) ** 2 - (1 - r + r**2) - (3 - 8 * r) * (1 - r),
)
q0 = sp.symbols("q0")
p_boundary = 1 - q0 / 2
zero(
    "endpoint-distance contradiction boundary",
    p_boundary**2 + p_boundary * q0 + q0**2 - 1 - sp.Rational(3, 4) * q0**2,
)
xx = sp.symbols("xx")
beta_x = (-xx + sp.sqrt(4 - 3 * xx**2)) / 2
zero("nonadjacent beta root", beta_x**2 + xx * beta_x + xx**2 - 1)

print(f"verify_strategy2_pure_algebra: PASS ({len(CHECKS)} exact identities)")
for check in CHECKS:
    print(f"- {check}")
