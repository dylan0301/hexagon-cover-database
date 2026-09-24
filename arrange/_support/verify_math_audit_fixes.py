#!/usr/bin/env python3
"""Exact regressions for the three 2026-09-24 mathematical review corrections.

These symbolic identities, rational examples, and source contracts protect the
specific repairs. They are not a formal verification of the entire covering proof.
Run with Python and SymPy, without -O.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = Path(__file__).with_name("math_audit_fixes.json")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> None:
    t, x, y, alpha, beta = sp.symbols("t x y alpha beta", real=True)
    D = 1 - t + t**2
    U = alpha + y - t*x
    V = beta + x - (1-t)*y
    jacobian = sp.Matrix([U, V]).jacobian([x, y]).det()
    require(sp.expand(jacobian + D) == 0, "Type-I Jacobian must be -D")
    require(sp.expand((1-t)*U + V - (1-t)*alpha - beta - D*x) == 0,
            "First reference-simplex wedge inequality")
    require(sp.expand(U + t*V - alpha - t*beta - D*y) == 0,
            "Second reference-simplex wedge inequality")
    # The affine slack coefficients are nonnegative on the whole [0,1] interval.
    coefficients = [1-t, sp.Integer(1), sp.Integer(1), t]
    require(all(c.subs(t, 0) >= 0 and c.subs(t, 1) >= 0 for c in coefficients),
            "Monotonicity includes both endpoint orientations")
    require(sp.expand(D - ((t-sp.Rational(1, 2))**2+sp.Rational(3, 4))) == 0,
            "Positive, translation-independent Jacobian")
    print("PASS reference-simplex inclusion and invariant area scaling")

    # Exact counterexample to physical set inclusion (not to area monotonicity).
    half, tenth = sp.Rational(1, 2), sp.Rational(1, 10)
    z = sp.sqrt(3)/2
    old = {t: half, alpha: sp.Rational(1, 5), beta: sp.Rational(1, 5)}
    new = {t: half, alpha: sp.Rational(1, 20), beta: sp.Rational(1, 5)}
    for parameters in [old, new]:
        for px, py in [(0, 0), (tenth, 0), (0, tenth)]:
            uu = U.subs(parameters).subs({x: px, y: py})
            vv = V.subs(parameters).subs({x: px, y: py})
            require(uu >= 0 and vv >= 0 and z-uu-vv >= 0,
                    "Counterexample triangles must contain the required anchors")
    point = {x: sp.Rational(3, 10), y: 0}
    old_u, old_v = [expr.subs(old).subs(point) for expr in [U, V]]
    require(old_u == sp.Rational(1, 20) and old_v == half and z-old_u-old_v > 0,
            "Counterexample point must lie inside the original triangle")
    require(U.subs(new).subs(point) == -sp.Rational(1, 10),
            "The same physical point must leave the translated triangle")
    print("PASS exact counterexample to physical nesting")

    # For the unit disk and P={O}, each of three supports is 1, while O's
    # projection is 0 in every unit direction. No supporting side contains O.
    radius, point_support = sp.Integer(1), sp.Integer(0)
    require(point_support < radius, "Disk-only point is not a contact point")
    require(sp.simplify(3*radius/(sp.sqrt(3)/2)-2*sp.sqrt(3)) == 0,
            "Disk-only enclosing side")
    print("PASS disk-only exception fixture")

    record = json.loads(MANIFEST.read_text())
    require(len(record["reviewed_files"]) == 7, "Exactly seven reviewed source files")
    for name, hashes in record["reviewed_files"].items():
        require(hashes["before_sha256"] != hashes["after_sha256"], name)
        require(hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == hashes["after_sha256"],
                f"Unreviewed source bytes: {name}")
    area_paths = ["C_area_loss_optimization.tex", "inline_proofs/04_area_loss.tex"]
    for name in area_paths:
        text = (ROOT/"arrange/paper_draft"/name).read_text()
        require("not necessarily the physical intersection" in text, name)
        require("Jacobian magnitude $D$ is independent" in text, name)
    for name in ["06_finite_enclosure_full.tex", "inline_proofs/02_common_geometry.tex"]:
        require("Outside the disk-only alternative" in
                (ROOT/"arrange/paper_draft"/name).read_text(), name)
    bc = (ROOT/"proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md").read_text()
    assembly = bc.split("### Theorem 7.0.", 1)[1].split("### Theorem 7.1.", 1)[0]
    require("same five-point set $K_{BC}$" in assembly and "All five points" in assembly,
            "BC assembly must name the current five-point witness")
    require("six-point" not in assembly and "six points" not in assembly,
            "Obsolete BC assembly count")
    print("PASS both editions, three numbered sources, and exact reviewed hashes")
    print("Mathematical audit regressions: PASS (not a formal proof certification)")


if __name__ == "__main__":
    main()
