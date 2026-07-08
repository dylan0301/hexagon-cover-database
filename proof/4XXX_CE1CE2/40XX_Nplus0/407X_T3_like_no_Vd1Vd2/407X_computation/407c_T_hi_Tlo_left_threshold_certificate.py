"""
Finite rational interval certificate for the 407X branch (T_+^hi,T_+^lo).

It proves the implication

    realized left T_+^hi domain, p possible for a right lower sheet,
    S0 < L(p) = sqrt(p^2-p+1)-p  ==>  B5 < 1-p.

Variables:
    r in [0,1], beta in [1/2,1], p in [0,1/2].

Realized left T_+^hi necessary conditions:
    beta >= r,
    beta >= (1-r^2)/(1+2r),
    r >= (1-beta)(r+beta)^2.

Right lower-sheet necessary condition:
    3p^2+p-1 >= 0.

The verification is by rational interval arithmetic with one-sided square-root
bounds obtained from integer arithmetic. No floating point comparisons are used
for certification.
"""
from __future__ import annotations
from collections import deque, defaultdict
from fractions import Fraction
from math import isqrt

ONE = Fraction(1, 1)
HALF = Fraction(1, 2)
Q = 10**18


def sqrt_upper(x: Fraction) -> Fraction:
    """Return a rational number >= sqrt(x), for x >= 0."""
    if x < 0:
        raise ValueError(x)
    n, d = x.numerator, x.denominator
    a = isqrt(n * Q * Q // d)
    while Fraction(a, Q) * Fraction(a, Q) < x:
        a += 1
    return Fraction(a, Q)


def ratio_f(r: Fraction) -> Fraction:
    return (ONE - r * r) / (ONE + 2 * r)


def left_domain_exclusion(rl, rh, bl, bh):
    if bh < HALF or bh < rl or bh < ratio_f(rh):
        return True, "domain_beta"
    cell_max = rh - (ONE - bh) * (rl + bl) * (rl + bl)
    if cell_max < 0:
        return True, "domain_cell"
    return False, ""


def b5_upper(rl, rh, bl, bh):
    m_up = sqrt_upper(bh * bh - bh + ONE)
    return bh * m_up / (rl + bl)


def S0_lower(rl, rh, bl, bh):
    m_up = sqrt_upper(bh * bh - bh + ONE)
    c_up = m_up / (rl + bl)
    rho_up = sqrt_upper(rh * rh - rh + ONE)
    delta_low = (ONE - rh) / (ONE + rho_up)
    return ONE - c_up + delta_low


def L_upper(pl):
    return sqrt_upper(pl * pl - pl + ONE) - pl


def certify(box):
    rl, rh, bl, bh, pl, ph = box

    ok, reason = left_domain_exclusion(rl, rh, bl, bh)
    if ok:
        return True, reason

    if 3 * ph * ph + ph - ONE < 0:
        return True, "domain_p"

    if b5_upper(rl, rh, bl, bh) < ONE - ph:
        return True, "B5_upper"

    if S0_lower(rl, rh, bl, bh) >= L_upper(pl):
        return True, "S0_lower"

    return False, ""


def main():
    q = deque([(Fraction(0), ONE, HALF, ONE, Fraction(0), HALF)])
    qd = deque([0])
    counts = defaultdict(int)
    unresolved = []
    terminal = 0
    max_depth = 0

    while q:
        box = q.popleft()
        depth = qd.popleft()
        max_depth = max(max_depth, depth)
        ok, reason = certify(box)
        if ok:
            counts[reason] += 1
            terminal += 1
            continue

        rl, rh, bl, bh, pl, ph = box
        widths = [rh - rl, bh - bl, ph - pl]
        if max(widths) <= Fraction(1, 2**28):
            unresolved.append(box)
            continue

        i = widths.index(max(widths))
        if i == 0:
            mid = (rl + rh) / 2
            q.append((rl, mid, bl, bh, pl, ph)); qd.append(depth + 1)
            q.append((mid, rh, bl, bh, pl, ph)); qd.append(depth + 1)
        elif i == 1:
            mid = (bl + bh) / 2
            q.append((rl, rh, bl, mid, pl, ph)); qd.append(depth + 1)
            q.append((rl, rh, mid, bh, pl, ph)); qd.append(depth + 1)
        else:
            mid = (pl + ph) / 2
            q.append((rl, rh, bl, bh, pl, mid)); qd.append(depth + 1)
            q.append((rl, rh, bl, bh, mid, ph)); qd.append(depth + 1)

    print("terminal boxes:", terminal)
    print("max depth:", max_depth)
    print("counts:", dict(sorted(counts.items())))
    print("unresolved boxes:", len(unresolved))
    if unresolved:
        for box in unresolved[:10]:
            print(box)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
