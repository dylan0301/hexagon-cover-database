#!/usr/bin/env python3
"""Global analytic proof of the eight mixed-overlap core inequalities.

The input file records the exact integer polynomials A_{B,X}(U,z) and
B_{B,X}(U,z) obtained after eliminating D^2=z^2+6U+3U^2 from the four mixed
residuals.  This verifier proves their nonnegativity with three fixed analytic
charts and one global tensor-product Bernstein expansion per target.

There is no interval arithmetic, branch-and-bound, pruning, or subdivision.
All calculations use integers, rational numbers, and exact Q(sqrt(3)) signs.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import base64
import json
import zlib
from math import comb
from typing import Dict, Tuple

from mixed_overlap_core_polynomials import CORE_DATA_B85, CORE_POLYNOMIAL_SHA256

# ---------------------------------------------------------------------------
# Sparse integer bivariate polynomial arithmetic
# ---------------------------------------------------------------------------

IntPoly = Dict[Tuple[int, int], int]


def clean(poly: IntPoly) -> IntPoly:
    return {key: value for key, value in poly.items() if value}


def add(left: IntPoly, right: IntPoly, scale: int = 1) -> IntPoly:
    output = dict(left)
    for key, value in right.items():
        output[key] = output.get(key, 0) + scale * value
    return clean(output)


def multiply(left: IntPoly, right: IntPoly) -> IntPoly:
    output: IntPoly = {}
    for (i, j), a in left.items():
        for (k, ell), b in right.items():
            key = (i + k, j + ell)
            output[key] = output.get(key, 0) + a * b
    return clean(output)


def shift(poly: IntPoly, first: int, second: int, scale: int = 1) -> IntPoly:
    return {
        (i + first, j + second): scale * value
        for (i, j), value in poly.items()
    }


def powers(poly: IntPoly, maximum: int) -> list[IntPoly]:
    output = [{(0, 0): 1}]
    for _ in range(maximum):
        output.append(multiply(output[-1], poly))
    return output


def split_even_odd(poly: IntPoly) -> tuple[IntPoly, IntPoly]:
    even: IntPoly = {}
    odd: IntPoly = {}
    for (i, j), coefficient in poly.items():
        if j % 2 == 0:
            even[(i, j // 2)] = even.get((i, j // 2), 0) + coefficient
        else:
            odd[(i, (j - 1) // 2)] = odd.get((i, (j - 1) // 2), 0) + coefficient
    return clean(even), clean(odd)


def square_difference(even: IntPoly, odd: IntPoly) -> IntPoly:
    # E(U,w)^2 - w O(U,w)^2.
    return add(multiply(even, even), shift(multiply(odd, odd), 0, 1), -1)


# ---------------------------------------------------------------------------
# The fixed analytic charts
# ---------------------------------------------------------------------------

G_POLY = {(0, 0): 1, (1, 0): -6, (2, 0): -3}
H_POLY = {(0, 0): 1, (1, 0): -10, (2, 0): 21, (3, 0): -16, (4, 0): 4}
G_MINUS_H = add(G_POLY, H_POLY, -1)

# T chart:
# U=(x-1)(3-x)/(4x), z=y(9-x^4)/(8x^2), 1<=x<=sqrt(3), 0<=y<=1.
P_U = {(0, 0): -3, (1, 0): 4, (2, 0): -1}
P_Z = {(0, 0): 9, (4, 0): -1}


def transform_T(poly: IntPoly) -> tuple[IntPoly, int, int]:
    denominator_x = max(i + 2 * j for i, j in poly)
    denominator_two = max(2 * i + 3 * j for i, j in poly)
    U_powers = powers(P_U, max(i for i, _ in poly))
    Z_powers = powers(P_Z, max(j for _, j in poly))

    output: IntPoly = {}
    for (i, j), coefficient in poly.items():
        base = multiply(U_powers[i], Z_powers[j])
        x_shift = denominator_x - (i + 2 * j)
        scale = coefficient * 2 ** (denominator_two - (2 * i + 3 * j))
        output = add(output, shift(base, x_shift, j, scale))
    return output, denominator_x, denominator_two


def substitute_w_y_g(poly: IntPoly, g: IntPoly) -> IntPoly:
    g_powers = powers(g, max(j for _, j in poly))
    output: IntPoly = {}
    for (i, j), coefficient in poly.items():
        output = add(output, shift(g_powers[j], i, j, coefficient))
    return output


def substitute_w_h_plus_y_d(poly: IntPoly, h: IntPoly, d: IntPoly) -> IntPoly:
    maximum = max(j for _, j in poly)
    h_powers = powers(h, maximum)
    d_powers = powers(d, maximum)
    output: IntPoly = {}
    for (i, j), coefficient in poly.items():
        for k in range(j + 1):
            base = multiply(h_powers[j - k], d_powers[k])
            output = add(output, shift(base, i, k, coefficient * comb(j, k)))
    return output


# ---------------------------------------------------------------------------
# Exact arithmetic in Q(sqrt(3)) and global Bernstein conversion
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class Quad:
    rational: Fraction = Fraction(0)
    radical: Fraction = Fraction(0)

    def __add__(self, other: "Quad") -> "Quad":
        return Quad(self.rational + other.rational, self.radical + other.radical)

    def __sub__(self, other: "Quad") -> "Quad":
        return Quad(self.rational - other.rational, self.radical - other.radical)

    def __mul__(self, other: "Quad") -> "Quad":
        return Quad(
            self.rational * other.rational + 3 * self.radical * other.radical,
            self.rational * other.radical + self.radical * other.rational,
        )

    def scale(self, scalar: Fraction | int) -> "Quad":
        scalar = Fraction(scalar)
        return Quad(self.rational * scalar, self.radical * scalar)

    def sign(self) -> int:
        a = self.rational
        b = self.radical
        if b == 0:
            return (a > 0) - (a < 0)
        if b > 0:
            if a >= 0:
                return 1
            return 1 if 3 * b * b > a * a else -1
        if a <= 0:
            return -1
        return 1 if a * a > 3 * b * b else -1

    def token(self) -> tuple[int, int, int, int]:
        return (
            self.rational.numerator,
            self.rational.denominator,
            self.radical.numerator,
            self.radical.denominator,
        )


ZERO = Quad()
ONE = Quad(Fraction(1))
SQRT3 = Quad(Fraction(0), Fraction(1))
U_H = Quad(Fraction(1), Fraction(-1, 2))
U_MAX = Quad(Fraction(-1), Fraction(2, 3))


def quad_power(value: Quad, exponent: int) -> Quad:
    output = ONE
    base = value
    while exponent:
        if exponent & 1:
            output = output * base
        base = base * base
        exponent //= 2
    return output


QuadPoly = Dict[Tuple[int, int], Quad]
BernsteinGrid = Tuple[Tuple[Quad, ...], ...]


def affine_first(poly: IntPoly, lower: Quad, upper: Quad) -> QuadPoly:
    maximum = max(i for i, _ in poly)
    width = upper - lower
    lower_powers = [quad_power(lower, i) for i in range(maximum + 1)]
    width_powers = [quad_power(width, i) for i in range(maximum + 1)]

    output: QuadPoly = {}
    for (i, j), coefficient in poly.items():
        for k in range(i + 1):
            value = (lower_powers[i - k] * width_powers[k]).scale(
                coefficient * comb(i, k)
            )
            key = (k, j)
            output[key] = output.get(key, ZERO) + value
    return {key: value for key, value in output.items() if value != ZERO}


def degrees(poly: Dict[Tuple[int, int], object]) -> tuple[int, int]:
    return max(i for i, _ in poly), max(j for _, j in poly)


def global_bernstein(poly: QuadPoly) -> BernsteinGrid:
    degree_first, degree_second = degrees(poly)
    power = [
        [ZERO for _ in range(degree_second + 1)]
        for _ in range(degree_first + 1)
    ]
    for (i, j), value in poly.items():
        power[i][j] = value

    first = [
        [ZERO for _ in range(degree_second + 1)]
        for _ in range(degree_first + 1)
    ]
    for i in range(degree_first + 1):
        for k in range(i + 1):
            factor = Fraction(comb(i, k), comb(degree_first, k))
            for j in range(degree_second + 1):
                if power[k][j] != ZERO:
                    first[i][j] = first[i][j] + power[k][j].scale(factor)

    output = [
        [ZERO for _ in range(degree_second + 1)]
        for _ in range(degree_first + 1)
    ]
    for j in range(degree_second + 1):
        for ell in range(j + 1):
            factor = Fraction(comb(j, ell), comb(degree_second, ell))
            for i in range(degree_first + 1):
                if first[i][ell] != ZERO:
                    output[i][j] = output[i][j] + first[i][ell].scale(factor)

    return tuple(tuple(row) for row in output)


def certify_global(poly: IntPoly, lower: Quad, upper: Quad) -> dict[str, object]:
    transformed = affine_first(poly, lower, upper)
    grid = global_bernstein(transformed)
    flattened = [value for row in grid for value in row]
    signs = [value.sign() for value in flattened]
    assert min(signs) >= 0

    transcript = json.dumps(
        [value.token() for value in flattened], separators=(",", ":")
    ).encode("ascii")
    degree_first, degree_second = degrees(transformed)
    return {
        "degree": [degree_first, degree_second],
        "coefficient_count": len(flattened),
        "zero_coefficients": sum(sign == 0 for sign in signs),
        "positive_coefficients": sum(sign > 0 for sign in signs),
        "coefficient_sha256": sha256(transcript).hexdigest(),
    }


def load_integer_cores() -> dict[str, IntPoly]:
    compressed = base64.b85decode("".join(CORE_DATA_B85.split()))
    raw_bytes = zlib.decompress(compressed)
    raw = json.loads(raw_bytes.decode("utf-8"))
    canonical = json.dumps(raw, separators=(",", ":"), sort_keys=True).encode("ascii")
    assert sha256(canonical).hexdigest() == CORE_POLYNOMIAL_SHA256
    return {
        name: {(int(i), int(j)): int(c) for i, j, c in terms}
        for name, terms in raw.items()
    }


def main() -> None:
    integer_cores = load_integer_cores()
    assert set(integer_cores) == {
        "L_A_A", "L_A_B", "L_C_A", "L_C_B",
        "T_A_A", "T_A_B", "T_C_A", "T_C_B",
    }

    T_summary = {}
    for label in ("T_A_A", "T_A_B", "T_C_A", "T_C_B"):
        transformed, denominator_x, denominator_two = transform_T(integer_cores[label])
        result = certify_global(transformed, ONE, SQRT3)
        result["positive_clearing_factor"] = {
            "power_of_x": denominator_x,
            "power_of_two": denominator_two,
        }
        T_summary[label] = result

    L_summary = {}
    for label in ("L_A_A", "L_A_B", "L_C_A", "L_C_B"):
        even, odd = split_even_odd(integer_cores[label])
        square = square_difference(even, odd)
        lower_E = substitute_w_y_g(even, G_POLY)
        lower_square = substitute_w_y_g(square, G_POLY)
        upper_E = substitute_w_h_plus_y_d(even, H_POLY, G_MINUS_H)
        upper_square = substitute_w_h_plus_y_d(square, H_POLY, G_MINUS_H)
        L_summary[label] = {
            "U_H_to_U_MAX_E": certify_global(lower_E, U_H, U_MAX),
            "U_H_to_U_MAX_E2_minus_wO2": certify_global(lower_square, U_H, U_MAX),
            "zero_to_U_H_E": certify_global(upper_E, ZERO, U_H),
            "zero_to_U_H_E2_minus_wO2": certify_global(upper_square, ZERO, U_H),
        }

    core_transcript = json.dumps(
        {
            name: [[i, j, c] for (i, j), c in sorted(poly.items())]
            for name, poly in sorted(integer_cores.items())
        },
        separators=(",", ":"), sort_keys=True,
    ).encode("ascii")
    output = {
        "certificate": "3105X_global_analytic_core_positivity",
        "arithmetic": "exact_Qsqrt3_global_tensor_Bernstein",
        "adaptive_subdivision": False,
        "branch_and_bound": False,
        "core_polynomial_sha256": sha256(core_transcript).hexdigest(),
        "charts": {"T": T_summary, "L": L_summary},
        "result": "PASS",
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
