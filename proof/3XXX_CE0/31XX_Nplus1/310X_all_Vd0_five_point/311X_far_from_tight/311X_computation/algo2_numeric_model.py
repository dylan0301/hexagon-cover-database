"""High-precision numerical model for the 311X algorithm-2 construction.

This script is an empirical helper. It reproduces the two-variable model,
the transition polynomial, the selected line-branch points, and the lower-bound
quantities used in the 311X notes. It is not by itself a proof certificate.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Tuple

import mpmath as mp

mp.mp.dps = 80


@dataclass(frozen=True)
class BranchData:
    p: mp.mpf
    q: mp.mpf
    a: mp.mpf
    b: mp.mpf
    rho: mp.mpf
    D: mp.mpf
    h: mp.mpf
    alpha: mp.mpf
    beta: mp.mpf
    gamma: mp.mpf
    delta: mp.mpf
    lam_star: mp.mpf


def Q(x: mp.mpf, y: mp.mpf) -> mp.mpf:
    return x * x + y * y - x * y


def branch_data(p: mp.mpf, q: mp.mpf) -> BranchData:
    a = mp.mpf(1) - p
    b = mp.mpf(1) - q
    rho = a * a + a * b + b * b
    D = mp.sqrt(4 * rho - 3)
    h = mp.sqrt(3) / 2
    alpha = h * (a + 2 * b - a * D) / (2 * rho)
    beta = h * (a - b + (a + b) * D) / (2 * rho)
    gamma = h * (-a + b + (a + b) * D) / (2 * rho)
    delta = h * (2 * a + b - b * D) / (2 * rho)
    lam_star = 8 * h * rho / (3 * (D + 3))
    return BranchData(p, q, a, b, rho, D, h, alpha, beta, gamma, delta, lam_star)


def line_circle_root(
    Y: Tuple[mp.mpf, mp.mpf],
    Z: Tuple[mp.mpf, mp.mpf],
    C: Tuple[mp.mpf, mp.mpf],
    lo: mp.mpf,
    hi: mp.mpf,
) -> mp.mpf:
    y0, y1 = Y
    z0, z1 = Z
    c0, c1 = C
    A = Q(z0, z1)
    X0 = y0 - c0
    X1 = y1 - c1
    B = 2 * (X0 * z0 + X1 * z1) - (X0 * z1 + X1 * z0)
    C0 = Q(X0, X1) - 1
    disc = B * B - 4 * A * C0
    if disc < 0:
        raise ValueError(f"negative discriminant {disc}")
    roots = [(-B - mp.sqrt(disc)) / (2 * A), (-B + mp.sqrt(disc)) / (2 * A)]
    good = [r for r in roots if lo - mp.mpf("1e-40") <= r <= hi + mp.mpf("1e-40")]
    if len(good) != 1:
        raise ValueError(f"expected one root in segment, got {roots}, interval {lo}, {hi}")
    return good[0]


def p3_p5_local(p: mp.mpf, q: mp.mpf) -> Tuple[mp.mpf, mp.mpf, mp.mpf, mp.mpf]:
    bd = branch_data(p, q)
    lo, hi = bd.lam_star, 1 / bd.h
    lam3 = line_circle_root(
        (bd.a, mp.mpf(0)),
        (-bd.beta, bd.alpha),
        (bd.b, 1 + bd.b),
        lo,
        hi,
    )
    u = bd.a - lam3 * bd.beta
    v = lam3 * bd.alpha
    lam5 = line_circle_root(
        (mp.mpf(0), bd.b),
        (bd.delta, -bd.gamma),
        (1 + bd.a, bd.a),
        lo,
        hi,
    )
    s = lam5 * bd.delta
    t = bd.b - lam5 * bd.gamma
    return u, v, s, t


def transition_T(p: mp.mpf, q: mp.mpf) -> mp.mpf:
    S = p + q
    return S ** 4 - S ** 2 + p * q


def c_star(p: mp.mpf, q: mp.mpf) -> mp.mpf:
    S = p + q
    T = transition_T(p, q)
    if T >= 0:
        return 2 * q / (1 + mp.sqrt(4 * S * S - 3))

    lo, hi = S, mp.mpf(1)

    def f(c: mp.mpf) -> mp.mpf:
        return c ** 4 - c ** 2 + p * c - p ** 2

    flo, fhi = f(lo), f(hi)
    if flo > 0 or fhi < 0:
        raise ValueError(f"bad quartic bracket: f(S)={flo}, f(1)={fhi}")
    for _ in range(240):
        mid = (lo + hi) / 2
        if f(mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def q_minus(p: mp.mpf) -> mp.mpf:
    return (3 - p - mp.sqrt(1 + 6 * p - 3 * p * p)) / 2


def q_transition(p: mp.mpf) -> mp.mpf:
    lo = q_minus(p)
    hi = 1 - p
    for _ in range(240):
        mid = (lo + hi) / 2
        if transition_T(p, mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def lower_bounds(p: mp.mpf, q: mp.mpf) -> dict[str, mp.mpf]:
    u, v, s, t = p3_p5_local(p, q)
    r = 1 - c_star(p, q)
    A23 = r * r + r * s - r * t - r * u - r * v + 2 * r + s * u - s * v + t * v - t - u + 1
    L23 = r * r + r * u - 2 * r * v + r + u * u - u * v - u + v * v - v + 1
    B23 = A23 / mp.sqrt(L23)
    A401 = r * r - r * s - r * t - r * u + r * v + 2 * r + s * u - s * v + t * v - t - u + 1
    A402 = -2 * r * t - r * u + r * v + 2 * r + s * u - s * v + t * v - t - u + 1
    L40 = r * r - 2 * r * s + r * t + r + s * s - s * t - s + t * t - t + 1
    B401 = A401 / mp.sqrt(L40)
    B402 = A402 / mp.sqrt(L40)
    B40max = max(B401, B402)
    B01 = 1 + 2 * r - t
    B12 = 1 - u + mp.mpf("1.5") * r + mp.mpf("0.5") * (s - t)
    return {
        "u": u,
        "v": v,
        "s": s,
        "t": t,
        "r": r,
        "B01": B01,
        "B12": B12,
        "B23": B23,
        "B401": B401,
        "B402": B402,
        "B40max": B40max,
        "G23": A23 * A23 - L23,
        "G401": A401 * A401 - L40,
        "G402": A402 * A402 - L40,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--p", default="0.1")
    parser.add_argument("--q", default=None)
    args = parser.parse_args()
    p = mp.mpf(args.p)
    q = q_transition(p) if args.q is None else mp.mpf(args.q)
    vals = lower_bounds(p, q)
    print(f"p = {mp.nstr(p, 30)}")
    print(f"q = {mp.nstr(q, 30)}")
    print(f"T = {mp.nstr(transition_T(p, q), 30)}")
    for key in ["u", "v", "s", "t", "r", "B01", "B12", "B23", "B401", "B402", "B40max", "G23", "G401", "G402"]:
        print(f"{key} = {mp.nstr(vals[key], 30)}")


if __name__ == "__main__":
    main()
