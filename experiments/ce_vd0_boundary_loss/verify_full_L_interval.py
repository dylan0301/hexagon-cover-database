"""
Verifier for the (Full,L) far-region interval certificate.
It certifies emptiness of the bad set for R in [1/2,50/51], eta in [0,1-sqrt(3)/2].

Bad set conditions:
  Delta(R,eta) <= 0   (Low-branch separator condition for B1=L)
  H(R,eta) >= 0       (Full condition plus s <= ell(eta), maximized at s=ell)
A box is safe if inf(Delta)>0 or sup(H)<0.

This script uses mpmath.iv interval arithmetic. For repository-grade certification,
run with an outward-rounded interval backend and compare terminal boxes.
"""
from mpmath import iv, mp
import sys

mp.dps = 50
ETA_MAX = float(1 - mp.sqrt(3) / 2)


def bounds(x):
    return float(x.a), float(x.b)


def eval_box(Rlo, Rhi, elo, ehi):
    R = iv.mpf([Rlo, Rhi])
    eta = iv.mpf([elo, ehi])
    c = 1 - eta
    # disc=4(1-eta)^2-3 is decreasing on [0, ETA_MAX], so use exact endpoint range.
    disc_lo = max(0.0, float(4 * (1 - ehi) ** 2 - 3))
    disc_hi = float(4 * (1 - elo) ** 2 - 3)
    sqrt_disc = iv.sqrt(iv.mpf([disc_lo, disc_hi]))
    ell = c * (1 - sqrt_disc) / 2
    u = (1 - eta) * R
    Delta = (u + ell) ** 4 - (u + ell) ** 2 + u * ell
    delta = R / (iv.sqrt(1 - R + R * R) + 1)
    H = u - delta - R * (1 - u) / (1 - R) + ell * (2 * R - 1) / (1 - R)
    dlo, dhi = bounds(Delta)
    hlo, hhi = bounds(H)
    return dlo, dhi, hlo, hhi


def generate(max_depth=35, min_width=1e-9):
    stack = [(0.5, 50 / 51, 0.0, ETA_MAX, 0)]
    cert = []
    unresolved = []
    while stack:
        Rlo, Rhi, elo, ehi, d = stack.pop()
        dlo, dhi, hlo, hhi = eval_box(Rlo, Rhi, elo, ehi)
        if dlo > 0:
            cert.append([Rlo, Rhi, elo, ehi, "Delta_positive", dlo, dhi, hlo, hhi])
        elif hhi < 0:
            cert.append([Rlo, Rhi, elo, ehi, "H_negative", dlo, dhi, hlo, hhi])
        elif d >= max_depth or max(Rhi - Rlo, ehi - elo) < min_width:
            unresolved.append([Rlo, Rhi, elo, ehi, d, dlo, dhi, hlo, hhi])
        else:
            if (Rhi - Rlo) >= (ehi - elo):
                mid = (Rlo + Rhi) / 2
                stack.append((Rlo, mid, elo, ehi, d + 1))
                stack.append((mid, Rhi, elo, ehi, d + 1))
            else:
                mid = (elo + ehi) / 2
                stack.append((Rlo, Rhi, elo, mid, d + 1))
                stack.append((Rlo, Rhi, mid, ehi, d + 1))
    return cert, unresolved


if __name__ == "__main__":
    cert, unresolved = generate()
    print("certified_boxes", len(cert))
    print("unresolved_boxes", len(unresolved))
    if unresolved:
        print("first_unresolved", unresolved[0])
        sys.exit(1)
