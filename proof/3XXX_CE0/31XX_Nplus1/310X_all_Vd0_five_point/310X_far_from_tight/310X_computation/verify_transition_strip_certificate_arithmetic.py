"""Check the arithmetic layer of the 3109 transition-strip certificate outline.

This script verifies that the recorded endpoint lower bounds, branch widths,
and curvature bounds imply positive denominator-free lower bounds on the
transition strip by the interpolation lemma. It does not verify the endpoint
or curvature interval enclosures themselves.
"""

from __future__ import annotations

from decimal import Decimal, getcontext

getcontext().prec = 80


def D(x: str) -> Decimal:
    return Decimal(x)


def interpolation_margin(endpoint_lb: Decimal, curvature_bound: Decimal, width: Decimal, pieces: int) -> Decimal:
    h = width / Decimal(pieces)
    return endpoint_lb - curvature_bound * h * h / Decimal(8)


def main() -> None:
    width_q = D("0.03174845")
    width_m = D("0.07010087")
    M = D("1000")

    checks = [
        ("G23 quartic", D("0.0431230626"), M, width_q, 4),
        ("G40 quartic", D("0.0103524421"), M, width_q, 4),
        ("G23 mixed", D("0.0403426738"), M, width_m, 12),
        ("G40 mixed", D("0.0077528147"), M, width_m, 12),
    ]

    ok = True
    for name, endpoint, curvature, width, pieces in checks:
        margin = interpolation_margin(endpoint, curvature, width, pieces)
        print(f"{name}: endpoint={endpoint}, pieces={pieces}, margin={margin}")
        if margin <= 0:
            ok = False

    F_eta = D("1.0031590223")
    print(f"dangerous edge base margin F_eta - 1 = {F_eta - D('1')}")
    if F_eta <= 1:
        ok = False

    if not ok:
        raise SystemExit("certificate arithmetic failed")
    print("certificate arithmetic checks passed")


if __name__ == "__main__":
    main()
