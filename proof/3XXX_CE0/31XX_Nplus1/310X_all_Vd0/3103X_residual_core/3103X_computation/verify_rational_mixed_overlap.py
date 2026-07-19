#!/usr/bin/env python3
"""Exact rational certificate for the two mixed tangent-witness overlaps.

No floating-point or interval arithmetic is used. SymPy's exact rational
function field derives the four residual numerators. Each numerator reduces,
using D^2=z^2+6U+3U^2, to a positive factor times A(U,z)+D B(U,z). Exact
integer Bernstein coefficients certify A,B >= 0 on each radial cell.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, gcd
from typing import Dict, Tuple

import sympy as sp
from sympy.polys.fields import field

QQ = sp.QQ
ROOT_U = Fraction(4, 25)
MAX_DEPTH = 24


def derive_core_polynomials():
    F, U, z, D = field("U,z,D", QQ)
    R = F.ring
    s = 1 - U
    m = (s - z) / 2
    p = (s + z) / 2
    a = 1 - m
    b = 1 - p
    rho = a * a + a * b + b * b

    alpha = (b + 2 * a - b * D) / (2 * rho)
    beta = (b - a + (a + b) * D) / (2 * rho)
    gamma = (a - b + (a + b) * D) / (2 * rho)
    delta = (2 * b + a - a * D) / (2 * rho)
    junction = 8 * rho / (3 * (D + 3))

    amp_minus = alpha + b * beta
    amp_plus = delta + a * gamma
    g_minus = (
        QQ(9, 16) * junction**2
        - QQ(9, 4) * amp_minus * junction
        + 3 * b**2
        - 3 * b
        + 2
    )
    g_plus = (
        QQ(9, 16) * junction**2
        - QQ(9, 4) * amp_plus * junction
        + 3 * a**2
        - 3 * a
        + 2
    )
    derivative_minus = QQ(3, 2) * junction - 3 * amp_minus
    derivative_plus = QQ(3, 2) * junction - 3 * amp_plus
    tangent_minus = junction - QQ(4, 3) * g_minus / derivative_minus
    tangent_plus = junction - QQ(4, 3) * g_plus / derivative_plus

    local_A_u = b - QQ(3, 4) * beta * tangent_minus
    local_A_v = QQ(3, 4) * alpha * tangent_minus
    local_C_u = QQ(3, 4) * delta * tangent_plus
    local_C_v = a - QQ(3, 4) * gamma * tangent_plus

    # A global vector is represented by (x,h*y), h^2=3/4.
    A_x = local_A_u - QQ(1, 2) * local_A_v - QQ(1, 2)
    A_y = local_A_v - 1
    C_x = local_C_u - QQ(1, 2) * local_C_v - QQ(1, 2)
    C_y = local_C_v - 1
    # C' = R^{-1}C.
    Cp_x = -QQ(1, 2) * C_x + QQ(3, 4) * C_y
    Cp_y = -C_x - QQ(1, 2) * C_y

    determinant = A_x * Cp_y - A_y * Cp_x

    def dot(x1, y1, x2, y2):
        return x1 * x2 + QQ(3, 4) * y1 * y2

    chi = s**4 - s**2 + m * (s - m)
    kappa = 4 * s**3 - 2 * s + m
    c_L = s - chi / kappa
    c_T = s - chi / (1 - m)

    def mixed_residuals(c):
        e = 1 - c
        t = 2 * c - 1
        vA_x = t * A_x - e * Cp_x
        vA_y = t * A_y - e * Cp_y
        vC_x = t * Cp_x - e * A_x
        vC_y = t * Cp_y - e * A_y
        q_A = determinant**2 - dot(vA_x, vA_y, vA_x, vA_y)
        q_C = determinant**2 - dot(vC_x, vC_y, vC_x, vC_y)
        return q_A, q_C

    L_A, L_C = mixed_residuals(c_L)
    T_A, T_C = mixed_residuals(c_T)
    residuals = {"L_A": L_A, "L_C": L_C, "T_A": T_A, "T_C": T_C}

    K = z * z + 6 * U + 3 * U * U
    K_poly = K.numer
    D_poly = R.gens[2]

    def reduce_D(poly):
        out = R.zero
        for (i_u, i_z, i_D), coefficient in poly.terms():
            quotient, remainder = divmod(i_D, 2)
            out += (
                R.term_new((i_u, i_z, 0), coefficient)
                * K_poly**quotient
                * D_poly**remainder
            )
        return out

    def split_D(poly):
        A = R.zero
        B = R.zero
        for (i_u, i_z, i_D), coefficient in poly.terms():
            assert i_D <= 1
            term = R.term_new((i_u, i_z, 0), coefficient)
            if i_D:
                B += term
            else:
                A += term
        return A, B

    expected_gcd = (K_poly + 3) ** 2 / 9
    cores = {}
    denominator_factorizations = {}
    for name, residual in residuals.items():
        reduced_numerator = reduce_D(residual.numer)
        A, B = split_D(reduced_numerator)
        common = A.gcd(B)
        assert common == expected_gcd
        A = A.exquo(common)
        B = B.exquo(common)
        content_A, primitive_A = A.primitive()
        content_B, primitive_B = B.primitive()
        assert content_A == 288
        assert content_B == 576
        # reduced numerator = 288*expected_gcd*(primitive_A+2D*primitive_B)
        cores[name] = (primitive_A, 2 * primitive_B)

        factorization = sp.factor_list(residual.denom.as_expr())
        assert factorization[0] > 0
        assert all(exponent % 2 == 0 for _, exponent in factorization[1])
        denominator_factorizations[name] = [
            (str(factor), exponent) for factor, exponent in factorization[1]
        ]

    return cores, denominator_factorizations


PowerPolynomial = Dict[Tuple[int, int], int]
BernsteinGrid = Tuple[Tuple[int, ...], ...]


def ring_to_power(poly) -> PowerPolynomial:
    output: PowerPolynomial = {}
    for (i_u, i_z, i_D), coefficient in poly.terms():
        assert i_D == 0 and coefficient.denominator == 1
        output[(int(i_u), int(i_z))] = int(coefficient.numerator)
    return output


def root_bernstein(power: PowerPolynomial) -> BernsteinGrid:
    degree_u = max((i for i, _ in power), default=0)
    degree_z = max((j for _, j in power), default=0)
    affine = [
        [Fraction(0) for _ in range(degree_z + 1)]
        for _ in range(degree_u + 1)
    ]
    for (i, j), coefficient in power.items():
        affine[i][j] += Fraction(coefficient) * ROOT_U**i

    bernstein = [
        [Fraction(0) for _ in range(degree_z + 1)]
        for _ in range(degree_u + 1)
    ]
    for k in range(degree_u + 1):
        for ell in range(degree_z + 1):
            value = Fraction(0)
            for i in range(k + 1):
                factor_u = Fraction(comb(k, i), comb(degree_u, i))
                for j in range(ell + 1):
                    value += (
                        affine[i][j]
                        * factor_u
                        * Fraction(comb(ell, j), comb(degree_z, j))
                    )
            bernstein[k][ell] = value

    denominator = 1
    for row in bernstein:
        for value in row:
            denominator = (
                denominator
                * value.denominator
                // gcd(denominator, value.denominator)
            )
    return tuple(
        tuple(int(value * denominator) for value in row)
        for row in bernstein
    )


def split_u(grid: BernsteinGrid) -> Tuple[BernsteinGrid, BernsteinGrid]:
    degree_u = len(grid) - 1
    degree_z = len(grid[0]) - 1
    left = [[0] * (degree_z + 1) for _ in range(degree_u + 1)]
    right = [[0] * (degree_z + 1) for _ in range(degree_u + 1)]
    for j in range(degree_z + 1):
        values = [grid[i][j] for i in range(degree_u + 1)]
        for i in range(degree_u + 1):
            left[i][j] = (1 << (degree_u - i)) * sum(
                comb(i, k) * values[k] for k in range(i + 1)
            )
            right[i][j] = (1 << i) * sum(
                comb(degree_u - i, k) * values[i + k]
                for k in range(degree_u - i + 1)
            )
    return (
        tuple(tuple(row) for row in left),
        tuple(tuple(row) for row in right),
    )


def split_z(grid: BernsteinGrid) -> Tuple[BernsteinGrid, BernsteinGrid]:
    degree_u = len(grid) - 1
    degree_z = len(grid[0]) - 1
    left = [[0] * (degree_z + 1) for _ in range(degree_u + 1)]
    right = [[0] * (degree_z + 1) for _ in range(degree_u + 1)]
    for i in range(degree_u + 1):
        values = list(grid[i])
        for j in range(degree_z + 1):
            left[i][j] = (1 << (degree_z - j)) * sum(
                comb(j, k) * values[k] for k in range(j + 1)
            )
            right[i][j] = (1 << j) * sum(
                comb(degree_z - j, k) * values[j + k]
                for k in range(degree_z - j + 1)
            )
    return (
        tuple(tuple(row) for row in left),
        tuple(tuple(row) for row in right),
    )


def bounds(grid: BernsteinGrid) -> Tuple[int, int]:
    return min(min(row) for row in grid), max(max(row) for row in grid)


DOMAIN_K = {(0, 0): 1, (0, 2): -1, (1, 0): -6, (2, 0): -3}
# This is 4*chi.
DOMAIN_CHI = {
    (0, 0): 1,
    (1, 0): -10,
    (2, 0): 21,
    (3, 0): -16,
    (4, 0): 4,
    (0, 2): -1,
}


def certify_branch(branch: str, cores):
    labels = ("L_A", "L_C") if branch == "L" else ("T_A", "T_C")
    target_grids = []
    for label in labels:
        A, B = cores[label]
        target_grids.extend(
            (root_bernstein(ring_to_power(A)), root_bernstein(ring_to_power(B)))
        )
    root = tuple(
        target_grids
        + [root_bernstein(DOMAIN_K), root_bernstein(DOMAIN_CHI)]
    )

    # Each box is encoded in normalized coordinates x=25U/4 and z.
    stack = [(root, 0, 0, 0, 0, 0)]
    stats = Counter()
    transcript = []
    maximum_used_depth = 0
    unresolved = []

    while stack:
        grids, depth_u, depth_z, depth, index_u, index_z = stack.pop()
        stats["processed"] += 1
        maximum_used_depth = max(maximum_used_depth, depth)
        K_bounds = bounds(grids[4])
        chi_bounds = bounds(grids[5])

        if K_bounds[1] <= 0:
            stats["pruned_K"] += 1
            transcript.append(("K", depth_u, depth_z, index_u, index_z))
            continue
        if branch == "L" and chi_bounds[0] > 0:
            stats["pruned_branch"] += 1
            transcript.append(("B", depth_u, depth_z, index_u, index_z))
            continue
        if branch == "T" and chi_bounds[1] < 0:
            stats["pruned_branch"] += 1
            transcript.append(("B", depth_u, depth_z, index_u, index_z))
            continue
        if all(bounds(grid)[0] >= 0 for grid in grids[:4]):
            stats["certified"] += 1
            transcript.append(("C", depth_u, depth_z, index_u, index_z))
            continue
        if depth >= MAX_DEPTH:
            unresolved.append((depth_u, depth_z, index_u, index_z))
            continue

        axis = "u" if depth_u <= depth_z else "z"
        pairs = [split_u(grid) if axis == "u" else split_z(grid) for grid in grids]
        lower = tuple(pair[0] for pair in pairs)
        upper = tuple(pair[1] for pair in pairs)
        if axis == "u":
            stack.append((upper, depth_u + 1, depth_z, depth + 1, 2 * index_u + 1, index_z))
            stack.append((lower, depth_u + 1, depth_z, depth + 1, 2 * index_u, index_z))
        else:
            stack.append((upper, depth_u, depth_z + 1, depth + 1, index_u, 2 * index_z + 1))
            stack.append((lower, depth_u, depth_z + 1, depth + 1, index_u, 2 * index_z))
        stats["split"] += 1

    assert not unresolved
    digest = sha256(
        json.dumps(transcript, separators=(",", ":")).encode("ascii")
    ).hexdigest()
    return {
        "branch": branch,
        "processed_boxes": stats["processed"],
        "split_boxes": stats["split"],
        "certified_boxes": stats["certified"],
        "pruned_by_radial_domain": stats["pruned_K"],
        "pruned_by_radial_cell": stats["pruned_branch"],
        "maximum_depth_used": maximum_used_depth,
        "unresolved_boxes": 0,
        "transcript_sha256": digest,
    }


def main() -> None:
    cores, denominator_factorizations = derive_core_polynomials()
    summaries = [certify_branch("L", cores), certify_branch("T", cores)]
    output = {
        "certificate": "3103X_exact_rational_mixed_overlaps",
        "arithmetic": "exact_rational_function_and_integer_Bernstein",
        "root_rectangle": {"U": [0, "4/25"], "z": [0, 1]},
        "core_term_counts": {
            name: [len(A.terms()), len(B.terms())]
            for name, (A, B) in sorted(cores.items())
        },
        "denominator_factor_counts": {
            name: len(factors)
            for name, factors in sorted(denominator_factorizations.items())
        },
        "branches": summaries,
        "result": "PASS",
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
