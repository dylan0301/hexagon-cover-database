#!/usr/bin/env python3
"""Certify the three disk-plus-two-point counterexamples from 31034.

At the exact rational parameter

    (a, b) = (1/10, 187/200),

this verifier constructs the exact witnesses from 31033 and exhibits one
exact rational unit normal for each of the three two-point subsets.  It proves
that the corresponding support sum is strictly below the unit-triangle
threshold.  Thus none of the three fixed disk-plus-two-point subsets can
replace the full three-point witness uniformly.

All nonlinear quantities are enclosed with 90-significant-digit Decimal
interval arithmetic.  Every arithmetic endpoint is widened by one Decimal
ulp after directed rounding.  The selected C_L root is isolated by bisection
on an interval where its defining polynomial is strictly increasing.  The
script uses only the Python standard library and does not make a claim about
the full three-point witness at this parameter.

Run from the repository root:

    python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/3103X_computation/verify_two_point_subset_counterexamples.py
"""

from __future__ import annotations

from decimal import (
    Decimal,
    ROUND_CEILING,
    ROUND_FLOOR,
    getcontext,
    localcontext,
)


PRECISION = 90
WORK_PRECISION = 110
getcontext().prec = WORK_PRECISION


class Interval:
    """Closed Decimal interval with outward-rounded elementary operations."""

    __slots__ = ("lo", "hi")

    def __init__(self, lo: int | str | Decimal, hi: int | str | Decimal | None = None):
        self.lo = Decimal(lo)
        self.hi = Decimal(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def _down(value: Decimal) -> Decimal:
        with localcontext() as context:
            context.prec = PRECISION
            context.rounding = ROUND_FLOOR
            rounded = +value
            return rounded.next_minus(context)

    @staticmethod
    def _up(value: Decimal) -> Decimal:
        with localcontext() as context:
            context.prec = PRECISION
            context.rounding = ROUND_CEILING
            rounded = +value
            return rounded.next_plus(context)

    @staticmethod
    def _coerce(value: Interval | int | str | Decimal) -> Interval:
        return value if isinstance(value, Interval) else Interval(value)

    def __add__(self, other: Interval | int | str | Decimal) -> Interval:
        other = self._coerce(other)
        with localcontext() as context:
            context.prec = WORK_PRECISION
            lo = self.lo + other.lo
            hi = self.hi + other.hi
        return Interval(self._down(lo), self._up(hi))

    __radd__ = __add__

    def __neg__(self) -> Interval:
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: Interval | int | str | Decimal) -> Interval:
        return self + (-self._coerce(other))

    def __rsub__(self, other: Interval | int | str | Decimal) -> Interval:
        return self._coerce(other) - self

    def __mul__(self, other: Interval | int | str | Decimal) -> Interval:
        other = self._coerce(other)
        with localcontext() as context:
            context.prec = WORK_PRECISION
            products = (
                self.lo * other.lo,
                self.lo * other.hi,
                self.hi * other.lo,
                self.hi * other.hi,
            )
        return Interval(self._down(min(products)), self._up(max(products)))

    __rmul__ = __mul__

    def __truediv__(self, other: Interval | int | str | Decimal) -> Interval:
        other = self._coerce(other)
        assert not (other.lo <= 0 <= other.hi), "division interval contains zero"
        with localcontext() as context:
            context.prec = WORK_PRECISION
            quotients = (
                self.lo / other.lo,
                self.lo / other.hi,
                self.hi / other.lo,
                self.hi / other.hi,
            )
        return Interval(self._down(min(quotients)), self._up(max(quotients)))

    def __rtruediv__(self, other: Interval | int | str | Decimal) -> Interval:
        return self._coerce(other) / self

    def square(self) -> Interval:
        with localcontext() as context:
            context.prec = WORK_PRECISION
            endpoint_squares = (self.lo * self.lo, self.hi * self.hi)
        lo = Decimal(0) if self.lo <= 0 <= self.hi else min(endpoint_squares)
        return Interval(self._down(lo), self._up(max(endpoint_squares)))

    def sqrt(self) -> Interval:
        assert self.lo >= 0, "square-root interval has negative lower endpoint"
        with localcontext() as context:
            context.prec = WORK_PRECISION
            lo = self.lo.sqrt(context)
            hi = self.hi.sqrt(context)
        return Interval(self._down(lo), self._up(hi))

    def contains(self, value: int | str | Decimal) -> bool:
        value = Decimal(value)
        return self.lo <= value <= self.hi


def radial_polynomial(c: Interval, m: Interval) -> Interval:
    return c.square().square() - c.square() + m * c - m.square()


def isolate_c_l(m: Interval) -> Interval:
    """Isolate the unique C_L root used by 2004 at the certificate point."""

    lo = Decimal("0.86")
    hi = Decimal(1)
    assert radial_polynomial(Interval(lo), m).hi < 0
    assert radial_polynomial(Interval(hi), m).lo > 0

    derivative = 4 * Interval(lo, hi) * Interval(lo, hi).square() - 2 * Interval(lo, hi) + m
    assert derivative.lo > 0

    for _ in range(270):
        with localcontext() as context:
            context.prec = WORK_PRECISION
            midpoint = (lo + hi) / Decimal(2)
        value = radial_polynomial(Interval(midpoint), m)
        if value.hi < 0:
            lo = midpoint
        elif value.lo > 0:
            hi = midpoint
        else:
            raise ArithmeticError("root bisection lost the polynomial sign")

    root = Interval(lo, hi)
    assert root.hi - root.lo < Decimal("1e-79")
    return root


def local_to_global(u: Interval, v: Interval, h: Interval) -> tuple[Interval, Interval]:
    return -Interval(1) / 2 + u - v / 2, h * (v - 1)


def rotate_120(vector: tuple[Interval, Interval], h: Interval) -> tuple[Interval, Interval]:
    x, y = vector
    return -x / 2 - h * y, h * x - y / 2


def dot(left: tuple[Interval, Interval], right: tuple[Interval, Interval]) -> Interval:
    return left[0] * right[0] + left[1] * right[1]


def rational_unit_normal(numerator: int) -> tuple[Interval, Interval]:
    """Return n(t)=((1-t^2)/(1+t^2),2t/(1+t^2)), t=numerator/10^9."""

    t = Interval(Decimal(numerator) / Decimal(10**9))
    denominator = 1 + t.square()
    normal = ((1 - t.square()) / denominator, 2 * t / denominator)
    assert (normal[0].square() + normal[1].square()).contains(1)
    return normal


def support_upper_bound(
    normal_numerator: int,
    subset: tuple[int, int],
    eta: Interval,
    points: tuple[tuple[Interval, Interval], ...],
    h: Interval,
) -> Interval:
    normal = rational_unit_normal(normal_numerator)
    total = Interval(0)

    for _ in range(3):
        upper_support = max(
            eta.hi,
            *(dot(points[index], normal).hi for index in subset),
        )
        total += Interval(upper_support)
        normal = rotate_120(normal, h)

    return total / h


def main() -> None:
    a = Interval("0.1")
    b = Interval("0.935")
    h = Interval(3).sqrt() / 2
    rho = a.square() + a * b + b.square()

    assert h.lo > Decimal("0.86")
    assert a.lo > 0 and b.lo > 0 and a.hi < 1 and b.hi < 1
    assert (a + b).lo > 1 and rho.hi < 1

    p = 1 - b
    q = 1 - a
    radial_sum = p + q
    selector = radial_sum.square().square() - radial_sum.square() + p * q
    assert selector.hi < 0

    c_star = isolate_c_l(p)
    eta = h * (1 - c_star)
    discriminant = (4 * rho - 3).sqrt()

    alpha = h * (b + 2 * a - b * discriminant) / (2 * rho)
    beta = h * (b - a + (a + b) * discriminant) / (2 * rho)
    gamma = h * (-b + a + (a + b) * discriminant) / (2 * rho)
    delta = h * (2 * b + a - a * discriminant) / (2 * rho)

    radicand_minus = 9 * (alpha + b * beta).square() - 9 * b.square() + 9 * b - 6
    radicand_plus = 9 * (delta + a * gamma).square() - 9 * a.square() + 9 * a - 6
    assert radicand_minus.lo > 0 and radicand_plus.lo > 0

    lambda_minus = 2 * (alpha + b * beta) - (Interval(2) / 3) * radicand_minus.sqrt()
    mu_plus = 2 * (delta + a * gamma) - (Interval(2) / 3) * radicand_plus.sqrt()

    q_minus = local_to_global(b - beta * lambda_minus, alpha * lambda_minus, h)
    q_zero = local_to_global(
        (2 * b + a - a * discriminant) / (discriminant + 3),
        (b + 2 * a - b * discriminant) / (discriminant + 3),
        h,
    )
    q_plus = local_to_global(delta * mu_plus, a - gamma * mu_plus, h)
    points = (q_minus, q_zero, q_plus)

    certificates = (
        ("{Q-, Q0}", (0, 1), 304277494),
        ("{Q0, Q+}", (1, 2), 151499905),
        ("{Q-, Q+}", (0, 2), 221307616),
    )

    print("parameter: a=1/10, b=187/200")
    print(f"C_L root enclosure width: {c_star.hi - c_star.lo:.3E}")
    for label, subset, normal_numerator in certificates:
        bound = support_upper_bound(normal_numerator, subset, eta, points, h)
        assert bound.hi < 1
        print(
            f"{label}: Lambda <= {bound.hi:.18f} "
            f"at t={normal_numerator}/10^9"
        )

    print("certified: every disk-plus-two-point subset has Lambda < 1")


if __name__ == "__main__":
    main()
