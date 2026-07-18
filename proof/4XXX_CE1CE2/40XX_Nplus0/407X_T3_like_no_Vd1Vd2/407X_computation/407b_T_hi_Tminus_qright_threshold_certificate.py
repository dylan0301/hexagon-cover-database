"""
Optional finite interval cross-check for the 407X left-high/right-Tminus
q-right reduction, now proved analytically in 407c, Lemma 4.1.

It proves the implication

    realized left T_+^hi domain, S0 < 93/200  ==>  B5 < 5657/10000,

where
    S0 = 1 - sqrt(beta^2-beta+1)/(r+beta)
         + (1-r)/(1+sqrt(r^2-r+1)),
    B5 = beta*sqrt(beta^2-beta+1)/(r+beta).

The verification is by rational interval arithmetic with one-sided square-root
bounds obtained from integer arithmetic. No floating point comparisons are used
for certification.
"""
from __future__ import annotations
from collections import deque, defaultdict
from fractions import Fraction
from math import isqrt

B0 = Fraction(5657, 10000)
T = Fraction(93, 200)
HALF = Fraction(1, 2)
ONE = Fraction(1, 1)
Q = 10**18


def sqrt_upper(x: Fraction) -> Fraction:
    """Return a rational >= sqrt(x), for x >= 0."""
    if x < 0:
        raise ValueError("sqrt_upper called on negative")
    n, d = x.numerator, x.denominator
    a = isqrt(n * Q * Q // d)
    while Fraction(a, Q) * Fraction(a, Q) < x:
        a += 1
    return Fraction(a, Q)


def ratio_f(r: Fraction) -> Fraction:
    return (ONE - r*r) / (ONE + 2*r)


def certify(box):
    """Return (True, reason) if this rational box is certified."""
    rl, rh, bl, bh = box

    if bh < HALF or bh < rl or bh < ratio_f(rh):
        return True, "domain_beta"

    cell_max = rh - (ONE - bh) * (rl + bl) * (rl + bl)
    if cell_max < 0:
        return True, "domain_cell"

    m_bh_up = sqrt_upper(bh*bh - bh + ONE)
    b_upper = bh * m_bh_up / (rl + bl)
    if b_upper < B0:
        return True, "B5_upper"

    rho_rh_up = sqrt_upper(rh*rh - rh + ONE)
    c_upper = m_bh_up / (rl + bl)
    delta_lower = (ONE - rh) / (ONE + rho_rh_up)
    S0_lower = ONE - c_upper + delta_lower
    if S0_lower >= T:
        return True, "S0_lower"

    return False, ""


def main():
    q = deque([(Fraction(0), Fraction(1), HALF, ONE)])
    qd = deque([0])
    counts = defaultdict(int)
    max_depth = 0
    terminal = 0
    unresolved = []

    while q:
        box = q.popleft()
        depth = qd.popleft()
        max_depth = max(max_depth, depth)
        ok, reason = certify(box)
        if ok:
            counts[reason] += 1
            terminal += 1
            continue

        rl, rh, bl, bh = box
        if max(rh - rl, bh - bl) <= Fraction(1, 2**30):
            unresolved.append(box)
            continue

        if rh - rl >= bh - bl:
            mid = (rl + rh) / 2
            q.append((rl, mid, bl, bh)); qd.append(depth + 1)
            q.append((mid, rh, bl, bh)); qd.append(depth + 1)
        else:
            mid = (bl + bh) / 2
            q.append((rl, rh, bl, mid)); qd.append(depth + 1)
            q.append((rl, rh, mid, bh)); qd.append(depth + 1)

    print("terminal boxes:", terminal)
    print("max depth:", max_depth)
    print("counts:", dict(sorted(counts.items())))
    print("unresolved boxes:", len(unresolved))
    if unresolved:
        for box in unresolved[:10]:
            print(box)
        raise SystemExit(1)

    rhs = Fraction(7) - 6*B0
    assert rhs > 0 and rhs*rhs > 13
    print("B0 < (7-sqrt(13))/6 verified")


if __name__ == "__main__":
    main()
