#!/usr/bin/env python3
"""Derive and verify the eight canonical mixed-overlap core polynomials.

No floating-point or interval arithmetic is used. SymPy's exact rational
function field constructs the four residuals directly from the witness
formulas. Reducing by D^2=z^2+6U+3U^2 splits each residual numerator into
its A(U,z) and D B(U,z) cores, which are compared term-for-term with the
package-local canonical transcript.
"""
from __future__ import annotations

import base64
from hashlib import sha256
import json
import zlib

import sympy as sp
from sympy.polys.fields import field

from mixed_overlap_core_polynomials import CORE_DATA_B85, CORE_POLYNOMIAL_SHA256

QQ = sp.QQ
EXPECTED_CORE_SHA256 = (
    "dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485"
)
EXPECTED_NAMES = {
    "L_A_A",
    "L_A_B",
    "L_C_A",
    "L_C_B",
    "T_A_A",
    "T_A_B",
    "T_C_A",
    "T_C_B",
}


def derive_core_polynomials():
    """Construct the four residuals and return their eight primitive cores."""
    F, U, z, D = field("U,z,D", QQ)
    ring = F.ring
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

    # A global vector is represented by (x,h*y), where h^2=3/4.
    A_x = local_A_u - QQ(1, 2) * local_A_v - QQ(1, 2)
    A_y = local_A_v - 1
    C_x = local_C_u - QQ(1, 2) * local_C_v - QQ(1, 2)
    C_y = local_C_v - 1
    # C' is the inverse 120-degree rotation of C.
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
    D_poly = ring.gens[2]

    def reduce_D(poly):
        output = ring.zero
        for (i_u, i_z, i_D), coefficient in poly.terms():
            quotient, remainder = divmod(i_D, 2)
            output += (
                ring.term_new((i_u, i_z, 0), coefficient)
                * K_poly**quotient
                * D_poly**remainder
            )
        return output

    def split_D(poly):
        core_A = ring.zero
        core_B = ring.zero
        for (i_u, i_z, i_D), coefficient in poly.terms():
            assert i_D <= 1
            term = ring.term_new((i_u, i_z, 0), coefficient)
            if i_D:
                core_B += term
            else:
                core_A += term
        return core_A, core_B

    expected_gcd = (K_poly + 3) ** 2 / 9
    cores = {}
    denominator_factorizations = {}
    for name, residual in residuals.items():
        reduced_numerator = reduce_D(residual.numer)
        core_A, core_B = split_D(reduced_numerator)
        common = core_A.gcd(core_B)
        assert common == expected_gcd
        core_A = core_A.exquo(common)
        core_B = core_B.exquo(common)
        content_A, primitive_A = core_A.primitive()
        content_B, primitive_B = core_B.primitive()
        assert content_A == 288
        assert content_B == 576
        # numerator = 288*expected_gcd*(primitive_A+D*(2*primitive_B)).
        cores[name] = (primitive_A, 2 * primitive_B)

        positive_content, factors = sp.factor_list(residual.denom.as_expr())
        assert positive_content > 0
        assert all(exponent % 2 == 0 for _, exponent in factors)
        denominator_factorizations[name] = {
            "positive_content": str(positive_content),
            "even_power_factors": [
                [str(factor), exponent] for factor, exponent in factors
            ],
        }

    return cores, denominator_factorizations


def canonicalize_terms(raw):
    """Normalize names and sparse terms before hashing or comparison."""
    assert set(raw) == EXPECTED_NAMES
    canonical = {}
    for name in sorted(raw):
        seen = set()
        terms = []
        for term in raw[name]:
            assert len(term) == 3
            assert all(isinstance(value, int) for value in term)
            i_u, i_z, coefficient = term
            assert i_u >= 0 and i_z >= 0 and coefficient != 0
            assert (i_u, i_z) not in seen
            seen.add((i_u, i_z))
            terms.append([i_u, i_z, coefficient])
        canonical[name] = sorted(terms)
    return canonical


def load_canonical_cores():
    compressed = base64.b85decode("".join(CORE_DATA_B85.split()))
    raw = json.loads(zlib.decompress(compressed).decode("utf-8"))
    canonical = canonicalize_terms(raw)
    transcript = json.dumps(
        canonical, separators=(",", ":"), sort_keys=True
    ).encode("ascii")
    digest = sha256(transcript).hexdigest()
    assert CORE_POLYNOMIAL_SHA256 == EXPECTED_CORE_SHA256
    assert digest == EXPECTED_CORE_SHA256
    return canonical, digest


def ring_to_terms(poly):
    terms = []
    for (i_u, i_z, i_D), coefficient in poly.terms():
        assert i_D == 0
        assert coefficient.denominator == 1
        terms.append([int(i_u), int(i_z), int(coefficient.numerator)])
    return sorted(terms)


def main() -> None:
    stored_cores, digest = load_canonical_cores()
    derived_pairs, denominator_factorizations = derive_core_polynomials()
    derived_cores = {}
    for name, (core_A, core_B) in derived_pairs.items():
        derived_cores[f"{name}_A"] = ring_to_terms(core_A)
        derived_cores[f"{name}_B"] = ring_to_terms(core_B)
    derived_cores = canonicalize_terms(derived_cores)
    assert derived_cores == stored_cores

    output = {
        "certificate": "3105X_mixed_overlap_core_derivation",
        "arithmetic": "exact_rational_function_field",
        "core_polynomial_sha256": digest,
        "core_term_counts": {
            name: len(terms) for name, terms in derived_cores.items()
        },
        "denominator_factorizations": denominator_factorizations,
        "result": "PASS",
    }
    print(json.dumps(output, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
