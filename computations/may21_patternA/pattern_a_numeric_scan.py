"""Numerical scan for the May 21/22 Pattern A reduced inequalities.

This is a reproducibility helper for `documentation/620_may21_patternA/`.
It is not a proof.  It uses numerical Newton solving and finite differences.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import mpmath as mp

mp.mp.dps = 50


@dataclass(frozen=True)
class BranchPoint:
    u: mp.mpf
    v: mp.mpf


def metric2(u: mp.mpf, v: mp.mpf) -> mp.mpf:
    return u*u + v*v - u*v


def phi(A: mp.mpf, B: mp.mpf) -> mp.mpf:
    x = 1 - A + B
    return x**4 - x**2 + B*(1-A)


def sigma(A: mp.mpf) -> mp.mpf:
    lo = mp.mpf("0")
    hi = A
    for _ in range(90):
        mid = (lo + hi) / 2
        if phi(A, mid) <= 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def q_min(r: mp.mpf) -> mp.mpf:
    return (r + 2 - mp.sqrt(4 - 3*r*r)) / 2


def rho2(A: mp.mpf, B: mp.mpf) -> mp.mpf:
    g = mp.sqrt(4*(1-A+B)**2 - 3)
    return 1 - 2*(1-A)/(1+g)


def local_values(u: mp.mpf, v: mp.mpf, q: mp.mpf, r: mp.mpf):
    alpha = r
    beta = 1 - q
    DA2 = (u-alpha)**2 + v**2 - (u-alpha)*v
    PA = alpha*(alpha-u+v) + beta*v
    QA = alpha*(alpha-u)
    SA = alpha*(alpha+beta-u) + beta*(v-u)
    DB2 = u**2 + (v-beta)**2 - u*(v-beta)
    PB = beta*(beta-v+u) + alpha*u
    QB = beta*(beta-v)
    SB = beta*(alpha+beta-v) + alpha*(u-v)
    return DA2, PA, QA, SA, DB2, PB, QB, SB


def equations_A(u: mp.mpf, v: mp.mpf, q: mp.mpf, r: mp.mpf):
    beta = 1 - q
    DA2, PA, *_ = local_values(u, v, q, r)
    FA = PA**2 - DA2
    C2 = (u-beta)**2 + (v-beta-1)**2 - (u-beta)*(v-beta-1) - 1
    return FA, C2


def equations_B(u: mp.mpf, v: mp.mpf, q: mp.mpf, r: mp.mpf):
    alpha = r
    *_, DB2, PB, _, _ = local_values(u, v, q, r)
    FB = PB**2 - DB2
    C5 = (u-alpha-1)**2 + (v-alpha)**2 - (u-alpha-1)*(v-alpha) - 1
    return FB, C5


def solve_branch_A(q: mp.mpf, r: mp.mpf) -> BranchPoint:
    s = q/r
    guesses = [((2*s-1)*r, 1-(4*s-1)*r), (r, 1-2*r), (mp.mpf("0.05"), mp.mpf("0.8"))]
    out: list[BranchPoint] = []
    for gu, gv in guesses:
        try:
            u, v = mp.findroot(lambda uu, vv: equations_A(uu, vv, q, r), (gu, gv), tol=mp.mpf("1e-35"))
            DA2, PA, QA, SA, *_ = local_values(u, v, q, r)
            if PA >= -1e-24 and QA >= -1e-24 and SA >= -1e-24 and DA2 <= 1 + 1e-24:
                out.append(BranchPoint(u, v))
        except Exception:
            pass
    if not out:
        raise RuntimeError(f"no A branch at q={q}, r={r}")
    return min(out, key=lambda z: metric2(z.u, z.v))


def solve_branch_B(q: mp.mpf, r: mp.mpf) -> BranchPoint:
    s = q/r
    guesses = [(2*s*r, (4*s-1)*r), (2*r, r), (mp.mpf("0.05"), mp.mpf("0.05"))]
    out: list[BranchPoint] = []
    for gu, gv in guesses:
        try:
            u, v = mp.findroot(lambda uu, vv: equations_B(uu, vv, q, r), (gu, gv), tol=mp.mpf("1e-35"))
            *_, DB2, PB, QB, SB = local_values(u, v, q, r)
            if PB >= -1e-24 and QB >= -1e-24 and SB >= -1e-24 and DB2 <= 1 + 1e-24:
                out.append(BranchPoint(u, v))
        except Exception:
            pass
    if not out:
        raise RuntimeError(f"no B branch at q={q}, r={r}")
    return min(out, key=lambda z: metric2(z.u, z.v))


def tau(q: mp.mpf, r: mp.mpf) -> mp.mpf:
    A = solve_branch_A(q, r)
    B = solve_branch_B(q, r)
    du = A.u - B.u
    dv = A.v - B.v
    D = mp.sqrt(du*du - du*dv + dv*dv)
    N0 = dv*(1-B.u) - du*(1-B.v)
    return (D - N0) / (dv - du)


def F_I(s: mp.mpf, r: mp.mpf) -> mp.mpf:
    q = s*r
    return rho2(r, q) + q - tau(q, r)


def F_II(s: mp.mpf, r: mp.mpf) -> mp.mpf:
    q = s*r
    sig = sigma(r)
    return r - sig + rho2(sig, q) - tau(q, r)


def fd_s(f, s: mp.mpf, r: mp.mpf) -> mp.mpf:
    h = mp.mpf("1e-6")
    return (f(s+h, r) - f(s-h, r)) / (2*h)


def fd_r(f, s: mp.mpf, r: mp.mpf) -> mp.mpf:
    h = mp.mpf("1e-6")
    return (f(s, r+h) - f(s, r-h)) / (2*h)


def scan(grid: int) -> None:
    r_star = (mp.sqrt(37) - 3) / 8
    mins = {name: (mp.inf, None) for name in ["FI", "FIs", "FIr", "FII", "FIIs", "FIIr"]}
    for i in range(grid):
        r = mp.mpf("0.005") + (r_star - mp.mpf("0.005"))*i/max(1, grid-1)
        smin = q_min(r)/r
        ssig = sigma(r)/r
        smax = min(mp.mpf("1"), mp.mpf("0.25")/r)
        for j in range(grid):
            if ssig < smax:
                s = ssig + (smax-ssig)*j/max(1, grid-1)
                try:
                    values = [("FI", F_I(s, r)), ("FIs", fd_s(F_I, s, r)), ("FIr", fd_r(F_I, s, r))]
                    for key, val in values:
                        if val < mins[key][0]:
                            mins[key] = (val, (s, r))
                except Exception:
                    pass
            upper_ii = min(ssig, smax)
            if smin < upper_ii:
                s = smin + (upper_ii-smin)*j/max(1, grid-1)
                try:
                    values = [("FII", F_II(s, r)), ("FIIs", fd_s(F_II, s, r)), ("FIIr", fd_r(F_II, s, r))]
                    for key, val in values:
                        if val < mins[key][0]:
                            mins[key] = (val, (s, r))
                except Exception:
                    pass
    for key, (val, loc) in mins.items():
        print(f"{key}: {mp.nstr(val, 12)} at {loc}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", type=int, default=12)
    args = parser.parse_args()
    scan(args.grid)
