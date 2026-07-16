#!/usr/bin/env python3
"""Outward-rounded certificate for the two mixed witness overlaps.

This verifier concerns the inner junction-tangent witnesses obtained by taking
one tangent (equivalently, one Newton) step on each of the two line--circle
quadratics at the frontier junction.  Each tangent zero lies strictly between
the junction and the corresponding first circle root.  In contrast to the
first-root witnesses, its coordinates are rational in ``a``, ``b``, and
``D = sqrt(4 rho - 3)``.

The reflection ``(a,b) -> (b,a)`` lets us assume ``z = a-b >= 0``.  Put

    p = 1-b, q = 1-a, s = p+q = 1-U, m = q, z = p-q.

The selected radial envelope is covered by two rational charts.

L chart:

    x = 2c-sqrt(4c^2-3) = 1+t,
    c = (x^2+3)/(4x),
    m = (x^2+3)(x-1)(x+3)/(16x^2),
    s = c-v.

Here 0 <= t <= sqrt(3)-1 < 3/4.  The original-domain bound
``U < 2/sqrt(3)-1 < 0.155`` implies ``0 <= v < 0.155``, so the
verified rectangle ``0 <= v <= 4/25`` is an enclosing rectangle.

T chart:

    x = 2s-sqrt(4s^2-3) = 1+t,
    s = (x^2+3)/(4x), r = (3-x^2)/(2x),
    c = s-v, z = sr-v(1+r).

The condition ``c > 2/3`` gives the enclosing bound ``0 <= v < 1/3``.
Boxes outside the actual domain are discarded only when an outward interval
proves that they contain no valid parameter.

Represent a global vector as ``(X,hY)``, where ``h^2=3/4``.  Let ``A`` be
the lower tangent witness and ``C`` the upper tangent witness.  If
``C' = R^{-1}C``, define

    X0 = A dot A,
    u  = A dot C',
    Delta0 = det(A,C')/h,
    e2 = (3/4)(1-c)^2,
    L0 = (1-c)u-(2c-1)X0,
    P0 = (X0-e2)Delta0^2-L0^2.

For ``Y=A,C``, put

    PY = (|Y|^2-e2)Delta0^2-((1-c)u-(2c-1)|Y|^2)^2.

The signs

    |A|^2-e2 >= 0, |C|^2-e2 >= 0,
    Delta0 <= 0, PA >= 0, PC >= 0

prove both mixed disk--point overlaps.  Indeed
``Delta = det(C,RA) = -h Delta0 >= 0`` and, after removing the common
factor ``h^2``, ``PY >= 0`` is exactly, for ``Y=A,C``,

    (|Y|^2-eta^2) Delta^2
      >= (h(2c-1)|Y|^2-eta(C dot RA))^2.

Reflection extends these two inequalities from ``z>=0`` to the other half of
the parameter domain.  It is important that both ``PA`` and ``PC`` are tested
on the same half-domain; reflection alone would not supply the second one.

All basic interval operations are rounded outward by one binary64 ulp.
Square-root endpoints are additionally checked against the exact rational
values of the participating binary64 numbers.  A first-order centered form
with interval automatic derivatives removes the dependency blow-up of the
raw rational formulas.  The final JSON object is the certificate summary.
"""

from __future__ import annotations

import json
import math
import sys
from dataclasses import dataclass


NEG_INF = -math.inf
POS_INF = math.inf


def down(value: float) -> float:
    if math.isnan(value):
        raise ArithmeticError("NaN in lower interval endpoint")
    if value == NEG_INF:
        return value
    return math.nextafter(value, NEG_INF)


def up(value: float) -> float:
    if math.isnan(value):
        raise ArithmeticError("NaN in upper interval endpoint")
    if value == POS_INF:
        return value
    return math.nextafter(value, POS_INF)


def compare_square_to_float(root: float, value: float) -> int:
    """Compare root**2 and value exactly as binary rationals."""

    root_num, root_den = root.as_integer_ratio()
    value_num, value_den = value.as_integer_ratio()
    left = root_num * root_num * value_den
    right = value_num * root_den * root_den
    return (left > right) - (left < right)


def sqrt_down(value: float) -> float:
    if value <= 0.0:
        return 0.0
    root = math.sqrt(value)
    while compare_square_to_float(root, value) > 0:
        root = math.nextafter(root, NEG_INF)
    while True:
        candidate = math.nextafter(root, POS_INF)
        if compare_square_to_float(candidate, value) <= 0:
            root = candidate
        else:
            return root


def sqrt_up(value: float) -> float:
    if value <= 0.0:
        return 0.0
    root = math.sqrt(value)
    while compare_square_to_float(root, value) < 0:
        root = math.nextafter(root, POS_INF)
    while True:
        candidate = math.nextafter(root, NEG_INF)
        if compare_square_to_float(candidate, value) >= 0:
            root = candidate
        else:
            return root


@dataclass(frozen=True, slots=True)
class Interval:
    lo: float
    hi: float

    def __post_init__(self) -> None:
        if math.isnan(self.lo) or math.isnan(self.hi) or self.lo > self.hi:
            raise ArithmeticError(f"invalid interval [{self.lo}, {self.hi}]")

    @staticmethod
    def point(value: float) -> "Interval":
        return Interval(value, value)

    @staticmethod
    def integer(value: int) -> "Interval":
        return Interval.point(float(value))

    @staticmethod
    def rational(numerator: int, denominator: int) -> "Interval":
        value = numerator / denominator
        return Interval(down(value), up(value))

    def add(self, other: "Interval") -> "Interval":
        return Interval(down(self.lo + other.lo), up(self.hi + other.hi))

    def sub(self, other: "Interval") -> "Interval":
        return Interval(down(self.lo - other.hi), up(self.hi - other.lo))

    def neg(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def mul(self, other: "Interval") -> "Interval":
        if (self.lo == 0.0 and self.hi == 0.0) or (
            other.lo == 0.0 and other.hi == 0.0
        ):
            return Interval(0.0, 0.0)
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        if any(math.isnan(product) for product in products):
            # This can occur only in a coarse, as-yet-unseparated box through
            # the extended-real product 0*infinity.  The whole interval is a
            # conservative enclosure; subdivision separates every retained
            # parameter box from this case.
            return Interval(NEG_INF, POS_INF)
        return Interval(down(min(products)), up(max(products)))

    def div(self, other: "Interval") -> "Interval":
        if other.lo <= 0.0 <= other.hi:
            return Interval(NEG_INF, POS_INF)
        quotients = (
            self.lo / other.lo,
            self.lo / other.hi,
            self.hi / other.lo,
            self.hi / other.hi,
        )
        return Interval(down(min(quotients)), up(max(quotients)))

    def square(self) -> "Interval":
        if self.lo >= 0.0:
            return Interval(max(0.0, down(self.lo * self.lo)), up(self.hi * self.hi))
        if self.hi <= 0.0:
            return Interval(max(0.0, down(self.hi * self.hi)), up(self.lo * self.lo))
        return Interval(0.0, up(max(self.lo * self.lo, self.hi * self.hi)))

    def sqrt_nonnegative_hull(self) -> "Interval":
        return Interval(sqrt_down(max(0.0, self.lo)), sqrt_up(max(0.0, self.hi)))


ZERO = Interval.integer(0)
ONE = Interval.integer(1)
TWO = Interval.integer(2)
THREE = Interval.integer(3)
FOUR = Interval.integer(4)
HALF = Interval.rational(1, 2)
THREE_QUARTERS = Interval.rational(3, 4)


@dataclass(frozen=True, slots=True)
class Dual2:
    value: Interval
    dt: Interval = ZERO
    dv: Interval = ZERO

    @staticmethod
    def constant(value: int | Interval) -> "Dual2":
        if isinstance(value, int):
            value = Interval.integer(value)
        return Dual2(value)

    def add(self, other: "Dual2") -> "Dual2":
        return Dual2(
            self.value.add(other.value),
            self.dt.add(other.dt),
            self.dv.add(other.dv),
        )

    def sub(self, other: "Dual2") -> "Dual2":
        return Dual2(
            self.value.sub(other.value),
            self.dt.sub(other.dt),
            self.dv.sub(other.dv),
        )

    def neg(self) -> "Dual2":
        return Dual2(self.value.neg(), self.dt.neg(), self.dv.neg())

    def mul(self, other: "Dual2") -> "Dual2":
        return Dual2(
            self.value.mul(other.value),
            self.dt.mul(other.value).add(self.value.mul(other.dt)),
            self.dv.mul(other.value).add(self.value.mul(other.dv)),
        )

    def div(self, other: "Dual2") -> "Dual2":
        denominator = other.value.square()
        return Dual2(
            self.value.div(other.value),
            self.dt.mul(other.value).sub(self.value.mul(other.dt)).div(denominator),
            self.dv.mul(other.value).sub(self.value.mul(other.dv)).div(denominator),
        )

    def square(self) -> "Dual2":
        twice = Interval.integer(2).mul(self.value)
        return Dual2(
            self.value.square(),
            twice.mul(self.dt),
            twice.mul(self.dv),
        )

    def sqrt_nonnegative_hull(self) -> "Dual2":
        root = self.value.sqrt_nonnegative_hull()
        denominator = Interval.integer(2).mul(root)
        return Dual2(root, self.dt.div(denominator), self.dv.div(denominator))


def const_rational(numerator: int, denominator: int = 1) -> Dual2:
    return Dual2.constant(Interval.rational(numerator, denominator))


def scale(numerator: int, denominator: int, value: Dual2) -> Dual2:
    return const_rational(numerator, denominator).mul(value)


@dataclass(frozen=True, slots=True)
class CoreValues:
    x: Dual2
    c: Dual2
    m: Dual2
    z: Dual2
    U: Dual2
    D2: Dual2
    derivative_minus: Dual2
    derivative_plus: Dual2
    radial_excess_a: Dual2
    radial_excess_c: Dual2
    delta0: Dual2
    square_certificate_a: Dual2
    square_certificate_c: Dual2


def tangent_core(t: Dual2, v: Dual2, branch: str) -> CoreValues:
    one = Dual2.constant(1)
    two = Dual2.constant(2)
    three = Dual2.constant(3)
    x = one.add(t)
    x2 = x.square()

    if branch == "L":
        c = x2.add(three).div(scale(4, 1, x))
        m = (
            x2.add(three)
            .mul(x.sub(one))
            .mul(x.add(three))
            .div(scale(16, 1, x2))
        )
        s = c.sub(v)
        z = s.sub(scale(2, 1, m))
    elif branch == "T":
        s = x2.add(three).div(scale(4, 1, x))
        radial_root = three.sub(x2).div(scale(2, 1, x))
        c = s.sub(v)
        z = s.mul(radial_root).sub(v.mul(one.add(radial_root)))
        m = s.sub(z).div(two)
    else:
        raise ValueError(f"unknown radial branch: {branch}")

    U = one.sub(s)
    D2 = z.square().add(scale(6, 1, U)).add(scale(3, 1, U.square()))
    D = D2.sqrt_nonnegative_hull()
    p = s.add(z).div(two)
    a = one.sub(m)
    b = one.sub(p)
    rho = D2.add(three).div(scale(4, 1, one))
    coefficient_denominator = scale(2, 1, rho)

    alpha0 = b.add(scale(2, 1, a)).sub(b.mul(D)).div(coefficient_denominator)
    beta0 = b.sub(a).add(a.add(b).mul(D)).div(coefficient_denominator)
    gamma0 = a.sub(b).add(a.add(b).mul(D)).div(coefficient_denominator)
    delta0_line = scale(2, 1, b).add(a).sub(a.mul(D)).div(coefficient_denominator)

    junction_parameter = scale(8, 1, rho).div(scale(3, 1, D.add(three)))
    amplitude_minus = alpha0.add(b.mul(beta0))
    amplitude_plus = delta0_line.add(a.mul(gamma0))

    def junction_circle_value(parameter: Dual2, amplitude: Dual2, endpoint: Dual2) -> Dual2:
        return (
            scale(9, 16, parameter.square())
            .sub(scale(9, 4, amplitude.mul(parameter)))
            .add(scale(3, 1, endpoint.square()))
            .sub(scale(3, 1, endpoint))
            .add(two)
        )

    circle_minus = junction_circle_value(junction_parameter, amplitude_minus, b)
    circle_plus = junction_circle_value(junction_parameter, amplitude_plus, a)
    derivative_minus = scale(3, 2, junction_parameter).sub(scale(3, 1, amplitude_minus))
    derivative_plus = scale(3, 2, junction_parameter).sub(scale(3, 1, amplitude_plus))

    tangent_minus = junction_parameter.sub(
        scale(4, 3, circle_minus.div(derivative_minus))
    )
    tangent_plus = junction_parameter.sub(
        scale(4, 3, circle_plus.div(derivative_plus))
    )

    local_minus_u = b.sub(scale(3, 4, beta0.mul(tangent_minus)))
    local_minus_v = scale(3, 4, alpha0.mul(tangent_minus))
    local_plus_u = scale(3, 4, delta0_line.mul(tangent_plus))
    local_plus_v = a.sub(scale(3, 4, gamma0.mul(tangent_plus)))

    def global_pair(local_u: Dual2, local_v: Dual2) -> tuple[Dual2, Dual2]:
        # The actual Cartesian vector is (first, h*second).
        return local_u.sub(scale(1, 2, local_v)).sub(const_rational(1, 2)), local_v.sub(one)

    point_minus = global_pair(local_minus_u, local_minus_v)
    point_plus = global_pair(local_plus_u, local_plus_v)

    # R^{-1}(x,h*y) = (-x/2+3y/4, h*(-x-y/2)).
    rotated_plus = (
        scale(-1, 2, point_plus[0]).add(scale(3, 4, point_plus[1])),
        point_plus[0].neg().sub(scale(1, 2, point_plus[1])),
    )

    def pair_dot(left: tuple[Dual2, Dual2], right: tuple[Dual2, Dual2]) -> Dual2:
        return left[0].mul(right[0]).add(scale(3, 4, left[1].mul(right[1])))

    norm2_a = pair_dot(point_minus, point_minus)
    norm2_c = pair_dot(point_plus, point_plus)
    mixed_dot = pair_dot(point_minus, rotated_plus)
    determinant0 = point_minus[0].mul(rotated_plus[1]).sub(
        point_minus[1].mul(rotated_plus[0])
    )
    eta2 = scale(3, 4, one.sub(c).square())
    radial_excess_a = norm2_a.sub(eta2)
    radial_excess_c = norm2_c.sub(eta2)
    linear_term_a = one.sub(c).mul(mixed_dot).sub(
        scale(2, 1, c).sub(one).mul(norm2_a)
    )
    linear_term_c = one.sub(c).mul(mixed_dot).sub(
        scale(2, 1, c).sub(one).mul(norm2_c)
    )
    determinant_squared = determinant0.square()
    square_certificate_a = radial_excess_a.mul(determinant_squared).sub(
        linear_term_a.square()
    )
    square_certificate_c = radial_excess_c.mul(determinant_squared).sub(
        linear_term_c.square()
    )

    return CoreValues(
        x=x,
        c=c,
        m=m,
        z=z,
        U=U,
        D2=D2,
        derivative_minus=derivative_minus,
        derivative_plus=derivative_plus,
        radial_excess_a=radial_excess_a,
        radial_excess_c=radial_excess_c,
        delta0=determinant0,
        square_certificate_a=square_certificate_a,
        square_certificate_c=square_certificate_c,
    )


def centered_bound(midpoint: Dual2, full_box: Dual2, radius_t: float, radius_v: float) -> Interval:
    displacement_t = Interval(-radius_t, radius_t)
    displacement_v = Interval(-radius_v, radius_v)
    return midpoint.value.add(full_box.dt.mul(displacement_t)).add(
        full_box.dv.mul(displacement_v)
    )


@dataclass(frozen=True, slots=True)
class BoxResult:
    status: str
    lower_certificate: float | None = None
    reason: str | None = None


def verify_box(
    t_lo: float,
    t_hi: float,
    v_lo: float,
    v_hi: float,
    branch: str,
) -> BoxResult:
    midpoint_t = (t_lo + t_hi) / 2.0
    midpoint_v = (v_lo + v_hi) / 2.0
    radius_t = up(max(midpoint_t - t_lo, t_hi - midpoint_t))
    radius_v = up(max(midpoint_v - v_lo, v_hi - midpoint_v))

    full = tangent_core(
        Dual2(Interval(t_lo, t_hi), ONE, ZERO),
        Dual2(Interval(v_lo, v_hi), ZERO, ONE),
        branch,
    )
    midpoint = tangent_core(
        Dual2(Interval.point(midpoint_t), ONE, ZERO),
        Dual2(Interval.point(midpoint_v), ZERO, ONE),
        branch,
    )

    # These are necessary conditions for a point in the charted strict domain.
    x_squared = full.x.value.square()
    if (
        x_squared.lo > 3.0
        or full.z.value.hi < 0.0
        or full.m.value.hi < 0.0
        or full.U.value.hi < 0.0
        or full.D2.value.hi < 0.0
        or full.D2.value.lo > 1.0
        or (branch == "T" and full.c.value.hi <= Interval.rational(2, 3).lo)
    ):
        return BoxResult("pruned")

    # The centered mean-value form differentiates D=sqrt(D2) on the full box,
    # so a certified box must stay strictly inside D2>0.  Boxes meeting the
    # singular face are subdivided; boxes wholly in D2<0 were pruned above.
    if full.D2.value.lo <= 0.0:
        return BoxResult("split", reason="square-root differentiability")

    # Convexity at the junction requires both line--circle derivatives to be negative.
    if full.derivative_minus.value.hi >= 0.0 or full.derivative_plus.value.hi >= 0.0:
        return BoxResult("split", reason="Newton denominator sign")

    radial_excess_a = centered_bound(
        midpoint.radial_excess_a, full.radial_excess_a, radius_t, radius_v
    )
    radial_excess_c = centered_bound(
        midpoint.radial_excess_c, full.radial_excess_c, radius_t, radius_v
    )
    delta0 = centered_bound(midpoint.delta0, full.delta0, radius_t, radius_v)
    certificate_a = centered_bound(
        midpoint.square_certificate_a,
        full.square_certificate_a,
        radius_t,
        radius_v,
    )
    certificate_c = centered_bound(
        midpoint.square_certificate_c,
        full.square_certificate_c,
        radius_t,
        radius_v,
    )

    if (
        radial_excess_a.lo >= 0.0
        and radial_excess_c.lo >= 0.0
        and delta0.hi <= 0.0
        and certificate_a.lo >= 0.0
        and certificate_c.lo >= 0.0
    ):
        return BoxResult(
            "certified",
            lower_certificate=min(certificate_a.lo, certificate_c.lo),
        )

    if radial_excess_a.lo < 0.0 or radial_excess_c.lo < 0.0:
        reason = "disk tangent radicand"
    elif delta0.hi > 0.0:
        reason = "oriented determinant"
    else:
        reason = "squared overlap"
    return BoxResult("split", reason=reason)


@dataclass(slots=True)
class ChartSummary:
    branch: str
    processed: int = 0
    certified: int = 0
    pruned: int = 0
    unresolved: int = 0
    minimum_lower_bound: float = POS_INF

    def as_json(self) -> dict[str, int | float | str]:
        return {
            "branch": self.branch,
            "processed_boxes": self.processed,
            "certified_boxes": self.certified,
            "pruned_boxes": self.pruned,
            "unresolved_boxes": self.unresolved,
            "minimum_certified_mixed_P_lower_bound": self.minimum_lower_bound,
        }


def verify_chart(
    branch: str,
    v_max: float,
    initial_t_count: int,
    initial_v_count: int,
    maximum_depth: int,
) -> ChartSummary:
    stack: list[tuple[float, float, float, float, int]] = []
    t_max = 3.0 / 4.0
    for t_index in range(initial_t_count):
        t_lo = t_max * t_index / initial_t_count
        t_hi = t_max * (t_index + 1) / initial_t_count
        for v_index in range(initial_v_count):
            v_lo = v_max * v_index / initial_v_count
            v_hi = v_max * (v_index + 1) / initial_v_count
            stack.append((t_lo, t_hi, v_lo, v_hi, 0))

    summary = ChartSummary(branch)
    while stack:
        t_lo, t_hi, v_lo, v_hi, depth = stack.pop()
        result = verify_box(t_lo, t_hi, v_lo, v_hi, branch)
        if result.status == "pruned":
            summary.pruned += 1
            continue

        summary.processed += 1
        if result.status == "certified":
            summary.certified += 1
            assert result.lower_certificate is not None
            summary.minimum_lower_bound = min(
                summary.minimum_lower_bound, result.lower_certificate
            )
            continue

        if depth >= maximum_depth:
            summary.unresolved += 1
            continue

        relative_t_width = (t_hi - t_lo) / t_max
        relative_v_width = (v_hi - v_lo) / v_max
        if relative_t_width > relative_v_width:
            midpoint = (t_lo + t_hi) / 2.0
            stack.append((t_lo, midpoint, v_lo, v_hi, depth + 1))
            stack.append((midpoint, t_hi, v_lo, v_hi, depth + 1))
        else:
            midpoint = (v_lo + v_hi) / 2.0
            stack.append((t_lo, t_hi, v_lo, midpoint, depth + 1))
            stack.append((t_lo, t_hi, midpoint, v_hi, depth + 1))

    return summary


def rational_upper(numerator: int, denominator: int) -> float:
    value = numerator / denominator
    value_num, value_den = value.as_integer_ratio()
    if value_num * denominator < numerator * value_den:
        return math.nextafter(value, POS_INF)
    return value


def main() -> None:
    if sys.float_info.radix != 2 or sys.float_info.mant_dig != 53:
        raise SystemExit("this verifier requires IEEE-754 binary64 Python floats")

    maximum_depth = 16
    summaries = [
        verify_chart(
            branch="L",
            v_max=rational_upper(4, 25),
            initial_t_count=8,
            initial_v_count=4,
            maximum_depth=maximum_depth,
        ),
        verify_chart(
            branch="T",
            v_max=rational_upper(1, 3),
            initial_t_count=8,
            initial_v_count=8,
            maximum_depth=maximum_depth,
        ),
    ]

    unresolved = sum(summary.unresolved for summary in summaries)
    certificate = {
        "certificate": "3103X_junction_tangent_mixed_overlaps",
        "result": "PASS" if unresolved == 0 else "INCOMPLETE",
        "rounding": "binary64_nextafter_outward_with_exact_sqrt_endpoint_checks",
        "centered_form": "first_order_interval_automatic_differentiation",
        "maximum_adaptive_depth": maximum_depth,
        "reflection_half_domain": "z=a-b>=0",
        "charts": [summary.as_json() for summary in summaries],
        "total_unresolved_boxes": unresolved,
    }
    print(json.dumps(certificate, sort_keys=True, separators=(",", ":")))

    if unresolved:
        raise SystemExit("mixed-overlap certificate has unresolved boxes")


if __name__ == "__main__":
    main()
