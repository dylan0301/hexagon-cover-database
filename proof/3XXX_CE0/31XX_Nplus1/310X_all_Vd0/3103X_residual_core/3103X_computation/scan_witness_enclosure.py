#!/usr/bin/env python3
"""Empirical falsification scan for the 3103X witness enclosure target.

Run from the repository root:

    python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/3103X_computation/scan_witness_enclosure.py

The script uses only the exact formulas proved in 2004, 20091, 31012,
31032, and 31033.  It evaluates the finite support-tie list proved in 31034;
it is numerical evidence, not an interval certificate.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np


H = math.sqrt(3.0) / 2.0
ROT120 = np.array([[-0.5, -H], [H, -0.5]])
V4 = np.array([-0.5, -H])


@dataclass
class Witness:
    a: float
    b: float
    c_star: float
    disk_radius: float
    points: tuple[np.ndarray, np.ndarray, np.ndarray]


def c_max(p: float, q: float) -> float:
    """The selected subcritical radial envelope from 2004."""
    m = min(p, q)
    M = max(p, q)
    s = p + q
    selector = s**4 - s**2 + p * q
    if selector <= 0.0:
        roots = np.roots([1.0, 0.0, -1.0, m, -(m * m)])
        selected = [
            z.real
            for z in roots
            if abs(z.imag) <= 2.0e-9 and H - 2.0e-9 <= z.real <= 1.0 + 2.0e-9
        ]
        if len(selected) != 1:
            raise ArithmeticError(f"radial L-root selection failed: {roots}")
        return selected[0]
    return 2.0 * M / (1.0 + math.sqrt(max(0.0, 4.0 * s * s - 3.0)))


def local_to_global(u: float, v: float) -> np.ndarray:
    return np.array([-0.5 + u - 0.5 * v, H * (v - 1.0)])


def witness(a: float, b: float) -> Witness:
    rho = a * a + a * b + b * b
    if not (0.0 < a < 1.0 and 0.0 < b < 1.0 and a + b > 1.0 and rho < 1.0):
        raise ValueError("point is outside the strict 3103X domain")

    D = math.sqrt(4.0 * rho - 3.0)
    alpha = H * (b + 2.0 * a - b * D) / (2.0 * rho)
    beta = H * (b - a + (a + b) * D) / (2.0 * rho)
    gamma = H * (-b + a + (a + b) * D) / (2.0 * rho)
    delta = H * (2.0 * b + a - a * D) / (2.0 * rho)

    rad_minus = 9.0 * (alpha + b * beta) ** 2 - 9.0 * b * b + 9.0 * b - 6.0
    rad_plus = 9.0 * (delta + a * gamma) ** 2 - 9.0 * a * a + 9.0 * a - 6.0
    if rad_minus < -2.0e-10 or rad_plus < -2.0e-10:
        raise ArithmeticError("negative selected-root radicand")

    lam = 2.0 * (alpha + b * beta) - (2.0 / 3.0) * math.sqrt(max(0.0, rad_minus))
    mu = 2.0 * (delta + a * gamma) - (2.0 / 3.0) * math.sqrt(max(0.0, rad_plus))

    q_minus = local_to_global(b - beta * lam, alpha * lam)
    q_zero = local_to_global(
        (2.0 * b + a - a * D) / (D + 3.0),
        (b + 2.0 * a - b * D) / (D + 3.0),
    )
    q_plus = local_to_global(delta * mu, a - gamma * mu)

    p = 1.0 - b
    q = 1.0 - a
    c_star = c_max(p, q)
    disk_radius = H * (1.0 - c_star)
    return Witness(a, b, c_star, disk_radius, (q_minus, q_zero, q_plus))


def support_sum(normal: np.ndarray, disk_radius: float, points: tuple[np.ndarray, ...]):
    total = 0.0
    labels = []
    n = normal.copy()
    for _ in range(3):
        values = [disk_radius] + [float(point @ n) for point in points]
        total += max(values)
        labels.append(int(np.argmax(values)))
        n = ROT120 @ n
    return total / H, tuple(labels)


def finite_events(disk_radius: float, points: tuple[np.ndarray, ...]):
    """Yield the complete support-tie normal list from 31034."""
    yield "arbitrary", np.array([1.0, 0.0])

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            difference = points[j] - points[i]
            length = float(np.linalg.norm(difference))
            if length == 0.0:
                continue
            perpendicular = np.array([-difference[1], difference[0]]) / length
            yield f"point-{i}-point-{j}-plus", perpendicular
            yield f"point-{i}-point-{j}-minus", -perpendicular

    for i, point in enumerate(points):
        norm2 = float(point @ point)
        if norm2 + 2.0e-15 < disk_radius * disk_radius:
            continue
        root = math.sqrt(max(0.0, norm2 - disk_radius * disk_radius))
        perpendicular = np.array([-point[1], point[0]])
        for sign in (-1.0, 1.0):
            normal = (disk_radius * point + sign * root * perpendicular) / norm2
            normal /= np.linalg.norm(normal)
            yield f"disk-point-{i}-{'plus' if sign > 0 else 'minus'}", normal


def lambda_finite(w: Witness, subset=(0, 1, 2)):
    points = tuple(w.points[i] for i in subset)
    best = (math.inf, None, None, None)
    for event, normal in finite_events(w.disk_radius, points):
        value, labels = support_sum(normal, w.disk_radius, points)
        if value < best[0]:
            theta = math.atan2(normal[1], normal[0]) % (2.0 * math.pi / 3.0)
            best = (value, theta, labels, event)
    return best


def lambda_dense(w: Witness, angle_count: int = 8192):
    best = math.inf
    for index in range(angle_count):
        theta = (2.0 * math.pi / 3.0) * index / angle_count
        normal = np.array([math.cos(theta), math.sin(theta)])
        value, _ = support_sum(normal, w.disk_radius, w.points)
        best = min(best, value)
    return best


def domain_sample(u_index: int, u_count: int, z_index: int, z_count: int):
    """Boundary-focused interior parameterization by U=a+b-1 and z=a-b."""
    u_fraction = (u_index + 0.5) / u_count
    u_max = 2.0 / math.sqrt(3.0) - 1.0
    U = u_max * 0.5 * (1.0 - math.cos(math.pi * u_fraction))

    z_linear = -1.0 + 2.0 * (z_index + 0.5) / z_count
    tau = math.sin(0.5 * math.pi * z_linear)
    z_max = math.sqrt(max(0.0, 1.0 - 6.0 * U - 3.0 * U * U))
    z = tau * z_max

    a = 0.5 * (1.0 + U + z)
    b = 0.5 * (1.0 + U - z)
    return a, b


def run_scan(u_count: int, z_count: int):
    global_best = (math.inf, None)
    interior_best = (math.inf, None)
    patterns: dict[tuple[int, int, int], int] = {}
    failures = 0

    for i in range(u_count):
        for j in range(z_count):
            a, b = domain_sample(i, u_count, j, z_count)
            w = witness(a, b)
            result = lambda_finite(w)
            value, theta, labels, event = result
            patterns[labels] = patterns.get(labels, 0) + 1
            record = (a, b, w.c_star, w.disk_radius, theta, labels, event)
            if value < global_best[0]:
                global_best = (value, record)
            if min(a, b) >= 0.05 and value < interior_best[0]:
                interior_best = (value, record)
            if value < 1.0 - 5.0e-10:
                failures += 1

    print(f"samples: {u_count * z_count}")
    print(f"values below 1-5e-10: {failures}")
    print("global minimum sample:", global_best)
    print("minimum with min(a,b)>=0.05:", interior_best)
    print("active-label counts (0=disk, 1=Q-, 2=Q0, 3=Q+):")
    for labels, count in sorted(patterns.items(), key=lambda item: (-item[1], item[0])):
        print(f"  {labels}: {count}")

    test = witness(0.1, 0.935)
    print("subset test at (a,b)=(0.1,0.935):")
    for subset in ((0, 1, 2), (0, 1), (1, 2), (0, 2)):
        print(f"  {subset}: {lambda_finite(test, subset)[0]:.15f}")


def run_crosscheck(sample_count: int):
    rng = np.random.default_rng(31034)
    largest_dense_gap = 0.0
    smallest_dense_gap = math.inf
    for _ in range(sample_count):
        U_fraction = rng.random()
        U_max = 2.0 / math.sqrt(3.0) - 1.0
        U = U_max * U_fraction
        z_max = math.sqrt(1.0 - 6.0 * U - 3.0 * U * U)
        z = (2.0 * rng.random() - 1.0) * z_max
        a = 0.5 * (1.0 + U + z)
        b = 0.5 * (1.0 + U - z)
        w = witness(a, b)
        finite_value = lambda_finite(w)[0]
        dense_value = lambda_dense(w)
        gap = dense_value - finite_value
        largest_dense_gap = max(largest_dense_gap, gap)
        smallest_dense_gap = min(smallest_dense_gap, gap)
    print(f"dense-angle crosscheck samples: {sample_count}")
    print(f"dense minus finite-event range: [{smallest_dense_gap:.3e}, {largest_dense_gap:.3e}]")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--u-count", type=int, default=160)
    parser.add_argument("--z-count", type=int, default=241)
    parser.add_argument("--crosscheck", type=int, default=100)
    args = parser.parse_args()
    run_scan(args.u_count, args.z_count)
    if args.crosscheck > 0:
        run_crosscheck(args.crosscheck)


if __name__ == "__main__":
    main()
