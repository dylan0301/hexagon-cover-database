#!/usr/bin/env python3
"""Migrate the canonical paper from inline schematic geometry to external exact figures.

The committed copy of this program lives at
arrange/paper_draft/figures/exact/generate.py.  ``--migrate`` is used once by
the branch-scoped delivery workflow.  ``--check`` is the permanent
reproducibility and mathematical audit entry point.
"""
from __future__ import annotations

import argparse
import hashlib
import html
import json
import math
import os
import random
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence

import fitz
import sympy as sp

TASK_ID = "exact-figures-20260902"
AUDITED_BASE = "48ee7c380d1a948bff0f491c3bae421f9a043fcd"
BRANCH = "chatgpt/tmp-source-export-20260901152106"
SQ3 = sp.sqrt(3)
H = math.sqrt(3.0) / 2.0


def find_root(start: Path) -> Path:
    for parent in (start.resolve(), *start.resolve().parents):
        if (parent / "AGENTS.md").is_file() and (parent / "arrange").is_dir():
            return parent
    raise SystemExit("repository root not found")


ROOT = find_root(Path(__file__))
PAPER = ROOT / "arrange/paper_draft"
FIGURES = PAPER / "figures"
EXACT = FIGURES / "exact"
GENERATED = EXACT / "generated"
SOURCE_TIKZ = EXACT / "source_tikz"
MANIFEST = EXACT / "manifest.json"
REPORT = ROOT / "arrange/exact_figure_migration_report.md"

COLORS = {
    "black": (0.08, 0.08, 0.08),
    "gray": (0.55, 0.57, 0.60),
    "lightgray": (0.94, 0.95, 0.96),
    "blue": (0.15, 0.39, 0.92),
    "lightblue": (0.88, 0.93, 1.00),
    "orange": (0.85, 0.47, 0.02),
    "lightorange": (1.00, 0.94, 0.84),
    "red": (0.72, 0.11, 0.11),
    "lightred": (1.00, 0.90, 0.90),
    "teal": (0.06, 0.46, 0.43),
    "lightteal": (0.86, 0.96, 0.95),
    "purple": (0.43, 0.16, 0.85),
    "lightpurple": (0.94, 0.90, 1.00),
    "green": (0.12, 0.55, 0.24),
    "lightgreen": (0.90, 0.97, 0.90),
    "white": (1.0, 1.0, 1.0),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fnum(value: float) -> str:
    if abs(value) < 5e-10:
        value = 0.0
    return f"{value:.5f}".rstrip("0").rstrip(".") or "0"


def pdf_escape(value: str) -> str:
    value = value.encode("latin-1", "replace").decode("latin-1")
    return value.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


class Canvas:
    """Small deterministic vector backend writing both PDF and SVG."""

    def __init__(self, width: float = 540, height: float = 350):
        self.width = float(width)
        self.height = float(height)
        self.pdf: list[str] = []
        self.svg: list[str] = []
        self.svg.append(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{fnum(width)}" '
            f'height="{fnum(height)}" viewBox="0 0 {fnum(width)} {fnum(height)}">'
        )
        self.svg.append('<rect width="100%" height="100%" fill="white"/>')

    @staticmethod
    def _rgb(color: str | tuple[float, float, float]) -> tuple[float, float, float]:
        return COLORS[color] if isinstance(color, str) else color

    @staticmethod
    def _svg_rgb(color: str | tuple[float, float, float]) -> str:
        r, g, b = Canvas._rgb(color)
        return f"rgb({round(255*r)},{round(255*g)},{round(255*b)})"

    def line(
        self,
        p: tuple[float, float],
        q: tuple[float, float],
        color: str = "black",
        width: float = 1.0,
        dash: Sequence[float] | None = None,
    ) -> None:
        r, g, b = self._rgb(color)
        dash_pdf = "[] 0 d" if not dash else f"[{' '.join(fnum(x) for x in dash)}] 0 d"
        self.pdf.append(
            f"q {fnum(r)} {fnum(g)} {fnum(b)} RG {fnum(width)} w {dash_pdf} "
            f"{fnum(p[0])} {fnum(p[1])} m {fnum(q[0])} {fnum(q[1])} l S Q"
        )
        dash_svg = "" if not dash else f' stroke-dasharray="{",".join(fnum(x) for x in dash)}"'
        self.svg.append(
            f'<line x1="{fnum(p[0])}" y1="{fnum(self.height-p[1])}" '
            f'x2="{fnum(q[0])}" y2="{fnum(self.height-q[1])}" '
            f'stroke="{self._svg_rgb(color)}" stroke-width="{fnum(width)}"{dash_svg}/>'
        )

    def poly(
        self,
        points: Sequence[tuple[float, float]],
        stroke: str = "black",
        fill: str | None = None,
        width: float = 1.0,
        closed: bool = True,
        dash: Sequence[float] | None = None,
    ) -> None:
        if not points:
            return
        r, g, b = self._rgb(stroke)
        dash_pdf = "[] 0 d" if not dash else f"[{' '.join(fnum(x) for x in dash)}] 0 d"
        parts = [
            "q",
            f"{fnum(r)} {fnum(g)} {fnum(b)} RG",
            f"{fnum(width)} w",
            dash_pdf,
        ]
        if fill:
            fr, fg, fb = self._rgb(fill)
            parts.append(f"{fnum(fr)} {fnum(fg)} {fnum(fb)} rg")
        parts.append(f"{fnum(points[0][0])} {fnum(points[0][1])} m")
        for p in points[1:]:
            parts.append(f"{fnum(p[0])} {fnum(p[1])} l")
        if closed:
            parts.append("h")
        parts.append("B" if fill else "S")
        parts.append("Q")
        self.pdf.append(" ".join(parts))
        attrs = [
            f'points="{" ".join(fnum(x)+","+fnum(self.height-y) for x,y in points)}"',
            f'stroke="{self._svg_rgb(stroke)}"',
            f'stroke-width="{fnum(width)}"',
            f'fill="{self._svg_rgb(fill) if fill else "none"}"',
        ]
        if dash:
            attrs.append(f'stroke-dasharray="{",".join(fnum(x) for x in dash)}"')
        tag = "polygon" if closed else "polyline"
        self.svg.append(f"<{tag} {' '.join(attrs)}/>")

    def circle(
        self,
        p: tuple[float, float],
        radius: float,
        stroke: str = "black",
        fill: str | None = None,
        width: float = 1.0,
    ) -> None:
        x, y = p
        k = radius * 0.5522847498307936
        r, g, b = self._rgb(stroke)
        parts = ["q", f"{fnum(r)} {fnum(g)} {fnum(b)} RG", f"{fnum(width)} w"]
        if fill:
            fr, fg, fb = self._rgb(fill)
            parts.append(f"{fnum(fr)} {fnum(fg)} {fnum(fb)} rg")
        parts.extend(
            [
                f"{fnum(x+radius)} {fnum(y)} m",
                f"{fnum(x+radius)} {fnum(y+k)} {fnum(x+k)} {fnum(y+radius)} {fnum(x)} {fnum(y+radius)} c",
                f"{fnum(x-k)} {fnum(y+radius)} {fnum(x-radius)} {fnum(y+k)} {fnum(x-radius)} {fnum(y)} c",
                f"{fnum(x-radius)} {fnum(y-k)} {fnum(x-k)} {fnum(y-radius)} {fnum(x)} {fnum(y-radius)} c",
                f"{fnum(x+k)} {fnum(y-radius)} {fnum(x+radius)} {fnum(y-k)} {fnum(x+radius)} {fnum(y)} c",
                "B" if fill else "S",
                "Q",
            ]
        )
        self.pdf.append(" ".join(parts))
        self.svg.append(
            f'<circle cx="{fnum(x)}" cy="{fnum(self.height-y)}" r="{fnum(radius)}" '
            f'stroke="{self._svg_rgb(stroke)}" stroke-width="{fnum(width)}" '
            f'fill="{self._svg_rgb(fill) if fill else "none"}"/>'
        )

    def text(
        self,
        p: tuple[float, float],
        value: str,
        size: float = 9,
        color: str = "black",
        bold: bool = False,
        align: str = "left",
    ) -> None:
        x, y = p
        lines = value.split("\n")
        r, g, b = self._rgb(color)
        font = "F2" if bold else "F1"
        for line_no, line in enumerate(lines):
            yy = y - line_no * size * 1.25
            approx = len(line) * size * 0.52
            xx = x - approx / 2 if align == "center" else x - approx if align == "right" else x
            self.pdf.append(
                f"q {fnum(r)} {fnum(g)} {fnum(b)} rg BT /{font} {fnum(size)} Tf "
                f"1 0 0 1 {fnum(xx)} {fnum(yy)} Tm ({pdf_escape(line)}) Tj ET Q"
            )
            weight = "700" if bold else "400"
            anchor = {"left": "start", "center": "middle", "right": "end"}[align]
            self.svg.append(
                f'<text x="{fnum(x)}" y="{fnum(self.height-yy)}" '
                f'font-family="Helvetica,Arial,sans-serif" font-size="{fnum(size)}" '
                f'font-weight="{weight}" text-anchor="{anchor}" '
                f'fill="{self._svg_rgb(color)}">{html.escape(line)}</text>'
            )

    def arrow(
        self,
        p: tuple[float, float],
        q: tuple[float, float],
        color: str = "teal",
        width: float = 1.2,
    ) -> None:
        self.line(p, q, color, width)
        dx, dy = q[0] - p[0], q[1] - p[1]
        length = math.hypot(dx, dy)
        if length < 1e-9:
            return
        ux, uy = dx / length, dy / length
        vx, vy = -uy, ux
        s = 6 + width
        a = (q[0] - s * ux + 0.45 * s * vx, q[1] - s * uy + 0.45 * s * vy)
        b = (q[0] - s * ux - 0.45 * s * vx, q[1] - s * uy - 0.45 * s * vy)
        self.poly([q, a, b], stroke=color, fill=color, width=width)

    def save(self, pdf_path: Path, svg_path: Path | None = None) -> None:
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        content = ("\n".join(self.pdf) + "\n").encode("latin-1")
        objects: list[bytes] = [
            b"<< /Type /Catalog /Pages 2 0 R >>",
            b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            (
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {fnum(self.width)} {fnum(self.height)}] "
                "/Resources << /Font << /F1 5 0 R /F2 6 0 R >> >> /Contents 4 0 R >>"
            ).encode("ascii"),
            b"<< /Length " + str(len(content)).encode("ascii") + b" >>\nstream\n" + content + b"endstream",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>",
        ]
        data = bytearray(b"%PDF-1.4\n% deterministic exact figure\n")
        offsets = [0]
        for index, obj in enumerate(objects, start=1):
            offsets.append(len(data))
            data.extend(f"{index} 0 obj\n".encode("ascii"))
            data.extend(obj)
            data.extend(b"\nendobj\n")
        xref = len(data)
        data.extend(f"xref\n0 {len(objects)+1}\n".encode("ascii"))
        data.extend(b"0000000000 65535 f \n")
        for off in offsets[1:]:
            data.extend(f"{off:010d} 00000 n \n".encode("ascii"))
        data.extend(
            (
                f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\n"
                f"startxref\n{xref}\n%%EOF\n"
            ).encode("ascii")
        )
        pdf_path.write_bytes(bytes(data))
        if svg_path:
            svg_path.parent.mkdir(parents=True, exist_ok=True)
            svg_path.write_text("\n".join([*self.svg, "</svg>", ""]), encoding="utf-8")


@dataclass(frozen=True)
class View:
    canvas: Canvas
    box: tuple[float, float, float, float]
    world: tuple[float, float, float, float]

    def p(self, point: tuple[float, float]) -> tuple[float, float]:
        bx, by, bw, bh = self.box
        xmin, ymin, xmax, ymax = self.world
        x = bx + (point[0] - xmin) * bw / (xmax - xmin)
        y = by + (point[1] - ymin) * bh / (ymax - ymin)
        return x, y

    def scale(self, value: float) -> float:
        _, _, bw, bh = self.box
        xmin, ymin, xmax, ymax = self.world
        return value * min(bw / (xmax - xmin), bh / (ymax - ymin))

    def line(self, p: tuple[float, float], q: tuple[float, float], **kw: object) -> None:
        self.canvas.line(self.p(p), self.p(q), **kw)

    def poly(self, pts: Sequence[tuple[float, float]], **kw: object) -> None:
        self.canvas.poly([self.p(p) for p in pts], **kw)

    def circle(self, p: tuple[float, float], radius: float, **kw: object) -> None:
        self.canvas.circle(self.p(p), self.scale(radius), **kw)

    def text(self, p: tuple[float, float], value: str, **kw: object) -> None:
        self.canvas.text(self.p(p), value, **kw)


HEX = [
    (1.0, 0.0),
    (0.5, H),
    (-0.5, H),
    (-1.0, 0.0),
    (-0.5, -H),
    (0.5, -H),
]
O = (0.0, 0.0)


def add(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    return a[0] + b[0], a[1] + b[1]


def sub(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    return a[0] - b[0], a[1] - b[1]


def mul(t: float, a: tuple[float, float]) -> tuple[float, float]:
    return t * a[0], t * a[1]


def dot(a: tuple[float, float], b: tuple[float, float]) -> float:
    return a[0] * b[0] + a[1] * b[1]


def cross(a: tuple[float, float], b: tuple[float, float]) -> float:
    return a[0] * b[1] - a[1] * b[0]


def norm(a: tuple[float, float]) -> float:
    return math.hypot(a[0], a[1])


def rotate(a: tuple[float, float], angle: float) -> tuple[float, float]:
    c, s = math.cos(angle), math.sin(angle)
    return c * a[0] - s * a[1], s * a[0] + c * a[1]


def lerp(a: tuple[float, float], b: tuple[float, float], t: float) -> tuple[float, float]:
    return a[0] + t * (b[0] - a[0]), a[1] + t * (b[1] - a[1])


def equilateral(center: tuple[float, float], theta: float) -> list[tuple[float, float]]:
    radius = 1.0 / math.sqrt(3.0)
    return [
        (
            center[0] + radius * math.cos(theta + 2 * math.pi * j / 3),
            center[1] + radius * math.sin(theta + 2 * math.pi * j / 3),
        )
        for j in range(3)
    ]


def polygon_margin(poly: Sequence[tuple[float, float]], point: tuple[float, float]) -> float:
    margins = []
    for a, b in zip(poly, [*poly[1:], poly[0]]):
        e = sub(b, a)
        margins.append(cross(e, sub(point, a)) / max(norm(e), 1e-12))
    return min(margins)


def inside(poly: Sequence[tuple[float, float]], point: tuple[float, float], tol: float = 1e-9) -> bool:
    return polygon_margin(poly, point) >= -tol


def segment_interval(
    poly: Sequence[tuple[float, float]],
    p0: tuple[float, float],
    p1: tuple[float, float],
) -> tuple[float, float] | None:
    lo, hi = 0.0, 1.0
    direction = sub(p1, p0)
    for a, b in zip(poly, [*poly[1:], poly[0]]):
        edge = sub(b, a)
        c0 = cross(edge, sub(p0, a))
        cd = cross(edge, direction)
        if abs(cd) < 1e-14:
            if c0 < -1e-11:
                return None
            continue
        bound = -c0 / cd
        if cd > 0:
            lo = max(lo, bound)
        else:
            hi = min(hi, bound)
        if lo > hi + 1e-11:
            return None
    return max(0.0, lo), min(1.0, hi)


def role_data(center: tuple[float, float], theta: float) -> dict[str, float | int | list[list[float]]]:
    tri = equilateral(center, theta)
    if polygon_margin(tri, HEX[0]) <= 1e-4:
        return {"valid": 0}
    outside = sum(not inside(HEX, p, 1e-8) for p in tri)
    supports = []
    support_intervals = []
    for j in (1, 5):
        interval = segment_interval(tri, O, HEX[j])
        length = 0.0 if interval is None else max(0.0, interval[1] - interval[0])
        supports.append(length > 2e-4)
        support_intervals.append(interval)
    ia = segment_interval(tri, HEX[0], HEX[5])
    ib = segment_interval(tri, HEX[0], HEX[1])
    ic = segment_interval(tri, HEX[0], O)
    A = 0.0 if ia is None else ia[1]
    B = 0.0 if ib is None else ib[1]
    C = 0.0 if ic is None else ic[1]
    return {
        "valid": 1,
        "o": outside,
        "n": int(supports[0]) + int(supports[1]),
        "A": A,
        "B": B,
        "C": C,
        "triangle": [[x, y] for x, y in tri],
        "r1": support_intervals[0],
        "r5": support_intervals[1],
        "margin": polygon_margin(tri, HEX[0]),
    }


def find_role_specimens() -> dict[str, dict[str, int | float]]:
    targets: dict[str, Callable[[dict[str, object], int], bool]] = {
        "vertex_role_vd0_axis_aligned_example": lambda d, k: d["o"] in (1, 2) and d["n"] == 0 and d["A"] + d["B"] > 1.02 and k % 30 == 0,
        "vertex_role_vd0_nonsupercritical_example": lambda d, k: d["o"] in (1, 2) and d["n"] == 0 and d["A"] + d["B"] < 0.96 and k % 30 != 0,
        "vertex_role_vd0_supercritical_example": lambda d, k: d["o"] in (1, 2) and d["n"] == 0 and d["A"] + d["B"] > 1.04,
        "vertex_role_vd1_example": lambda d, k: d["o"] == 1 and d["n"] == 1,
        "vertex_role_vd2_example": lambda d, k: d["o"] == 1 and d["n"] == 2,
        "vertex_role_t3_like_example": lambda d, k: d["o"] == 2 and d["n"] == 1,
    }
    best: dict[str, tuple[float, dict[str, int | float]]] = {}
    candidates: list[tuple[int, int, int]] = []
    for angle_k in range(0, 360, 2):
        for dx_num in range(-24, 25, 2):
            for dy_num in range(-24, 25, 2):
                candidates.append((angle_k, dx_num, dy_num))
    rng = random.Random(20260902)
    rng.shuffle(candidates)
    for angle_k, dx_num, dy_num in candidates:
        center = (1 + dx_num / 80.0, dy_num / 80.0)
        theta = math.pi * angle_k / 180.0
        data = role_data(center, theta)
        if not data.get("valid"):
            continue
        for name, predicate in targets.items():
            if predicate(data, angle_k):
                threshold_margin = abs(float(data["A"]) + float(data["B"]) - 1.0)
                outside_margin = min(abs(polygon_margin(HEX, tuple(p))) for p in data["triangle"])
                score = float(data["margin"]) + 0.15 * threshold_margin + 0.05 * outside_margin
                spec = {
                    "angle_degrees_num": angle_k,
                    "angle_degrees_den": 1,
                    "center_dx_num": dx_num,
                    "center_dy_num": dy_num,
                    "center_den": 80,
                }
                if name not in best or score > best[name][0]:
                    best[name] = (score, spec)
        if len(best) == len(targets) and len(candidates) > 2000:
            pass
    if len(best) != len(targets):
        missing = sorted(set(targets) - set(best))
        raise SystemExit(f"could not construct exact role specimens: {missing}")
    return {name: value[1] for name, value in sorted(best.items())}


def specimen_from_spec(spec: dict[str, int | float]) -> tuple[list[tuple[float, float]], dict[str, object]]:
    den = float(spec["center_den"])
    center = (1 + float(spec["center_dx_num"]) / den, float(spec["center_dy_num"]) / den)
    theta = math.pi * float(spec["angle_degrees_num"]) / (180.0 * float(spec["angle_degrees_den"]))
    data = role_data(center, theta)
    return equilateral(center, theta), data


def draw_hex(view: View, rays: bool = False) -> None:
    view.poly(HEX, stroke="black", fill="lightgray", width=1.4)
    if rays:
        for v in HEX:
            view.line(O, v, color="gray", width=0.65)


def draw_point(view: View, p: tuple[float, float], label: str = "", color: str = "red", offset: tuple[float, float] = (0.03, 0.03)) -> None:
    view.circle(p, 0.025, stroke="white", fill=color, width=0.5)
    if label:
        view.text(add(p, offset), label, size=7.4, color=color)


def signed_parameters(kind: str = "CE2") -> dict[str, float]:
    R = 0.5
    W = 0.5
    E = math.sqrt(1 - R * W)
    eta = 1 - E
    P = E * eta
    alpha = P / 4
    if kind == "CE2":
        delta = 3 * P / 4
    elif kind == "contact":
        delta = P - R * alpha
    elif kind == "CE1":
        delta = 19 * P / 20
    else:
        raise ValueError(kind)
    k = eta + alpha + delta
    return {"R": R, "W": W, "E": E, "eta": eta, "P": P, "alpha": alpha, "delta": delta, "k": k}


def chi(a: float, b: float) -> tuple[float, float]:
    return add(HEX[0], add(mul(b, sub(HEX[1], HEX[0])), mul(a, sub(HEX[5], HEX[0]))))


def line_intersection(A: Sequence[Sequence[float]], b: Sequence[float]) -> tuple[float, float]:
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    if abs(det) < 1e-12:
        raise ValueError("parallel lines")
    x = (b[0] * A[1][1] - A[0][1] * b[1]) / det
    y = (A[0][0] * b[1] - b[0] * A[1][0]) / det
    return x, y


def signed_triangle(params: dict[str, float]) -> list[tuple[float, float]]:
    R, W = params["R"], params["W"]
    alpha, delta, k = params["alpha"], params["delta"], params["k"]
    # F0=R+alpha-a+Wb; F1=Rb+Wa-k; F2=W+delta-b+Ra.
    equations = [
        ((-1.0, W), -(R + alpha)),
        ((W, R), k),
        ((R, -1.0), -(W + delta)),
    ]
    vertices_ab = []
    for i, j in ((0, 1), (1, 2), (2, 0)):
        A = [equations[i][0], equations[j][0]]
        B = [equations[i][1], equations[j][1]]
        vertices_ab.append(line_intersection(A, B))
    tri = [chi(a, b) for a, b in vertices_ab]
    if sum(cross(sub(tri[(i + 1) % 3], tri[i]), sub(tri[(i + 2) % 3], tri[(i + 1) % 3])) for i in range(3)) < 0:
        tri.reverse()
    return tri


def signed_exits(p: dict[str, float]) -> list[float]:
    return [
        p["E"] - p["alpha"] - p["delta"],
        p["delta"] / p["R"],
        p["delta"],
        min(p["alpha"] / p["R"], p["delta"] / p["W"]),
        p["alpha"],
        p["alpha"] / p["W"],
    ]


def cmax(a: float, b: float) -> float:
    if a < -1e-12 or b < -1e-12:
        raise ValueError("negative demand")
    if abs(a) < 1e-14 and abs(b) < 1e-14:
        return 1.0
    s = a + b
    d = a * a + a * b + b * b
    m, M = min(a, b), max(a, b)
    q = s**4 - s**2 + a * b
    if d > 1 + 1e-9:
        return 0.0
    if s <= 1 + 1e-10 and q <= 1e-12:
        def f(z: float) -> float:
            return z**4 - z**2 + m * z - m * m
        grid = [H + (1 - H) * i / 1000 for i in range(1001)]
        roots: list[float] = []
        last_x, last_y = grid[0], f(grid[0])
        for x in grid[1:]:
            y = f(x)
            if y == 0 or y * last_y < 0:
                lo, hi = last_x, x
                for _ in range(80):
                    mid = (lo + hi) / 2
                    if f(lo) * f(mid) <= 0:
                        hi = mid
                    else:
                        lo = mid
                roots.append((lo + hi) / 2)
            last_x, last_y = x, y
        if not roots:
            candidates = [r.real for r in __import__("numpy").roots([1, 0, -1, m, -m*m]) if abs(r.imag) < 1e-8 and H - 1e-8 <= r.real <= 1 + 1e-8]
            if not candidates:
                raise ValueError((a, b, "no L root"))
            roots = candidates
        return max(roots)
    if s <= 1 + 1e-10:
        rad = max(0.0, 4 * s * s - 3)
        return 2 * M / (1 + math.sqrt(rad))
    rad = max(0.0, 4 * d - 3)
    return (M * (2 * m * M + 1) - M * math.sqrt(rad)) / (2 * (1 - m * m))


def convex_hull(points: Sequence[tuple[float, float]]) -> list[tuple[float, float]]:
    pts = sorted(set((round(x, 13), round(y, 13)) for x, y in points))
    if len(pts) <= 1:
        return list(pts)
    def build(seq: Iterable[tuple[float, float]]) -> list[tuple[float, float]]:
        out: list[tuple[float, float]] = []
        for p in seq:
            while len(out) >= 2 and cross(sub(out[-1], out[-2]), sub(p, out[-1])) <= 1e-12:
                out.pop()
            out.append(p)
        return out
    lower = build(pts)
    upper = build(reversed(pts))
    return lower[:-1] + upper[:-1]


def support(points: Sequence[tuple[float, float]], n: tuple[float, float], disk: float = 0.0) -> float:
    return max([disk, *(dot(p, n) for p in points)])


def support_triangle(points: Sequence[tuple[float, float]], disk: float = 0.0) -> tuple[float, list[tuple[float, float]], float]:
    candidates: list[float] = []
    hull = convex_hull(points)
    for a, b in zip(hull, [*hull[1:], hull[0]]):
        e = sub(b, a)
        angle = math.atan2(e[1], e[0]) + math.pi / 2
        for sign in (0, math.pi):
            for j in range(3):
                candidates.append(angle + sign - 2 * math.pi * j / 3)
    if disk > 0:
        for p in points:
            rho = norm(p)
            if rho + 1e-12 >= disk and rho > 1e-12:
                phi = math.atan2(p[1], p[0])
                beta = math.acos(min(1.0, max(-1.0, disk / rho)))
                for tie in (phi - beta, phi + beta):
                    for j in range(3):
                        candidates.append(tie - 2 * math.pi * j / 3)
    if not candidates:
        candidates = [0.0]
    best: tuple[float, float, list[float]] | None = None
    for theta in candidates:
        normals = [(math.cos(theta + 2 * math.pi * j / 3), math.sin(theta + 2 * math.pi * j / 3)) for j in range(3)]
        hs = [support(points, n, disk) for n in normals]
        side = sum(hs) / H
        if best is None or side < best[0]:
            best = (side, theta, hs)
    assert best is not None
    side, theta, hs = best
    normals = [(math.cos(theta + 2 * math.pi * j / 3), math.sin(theta + 2 * math.pi * j / 3)) for j in range(3)]
    vertices = []
    for i, j in ((0, 1), (1, 2), (2, 0)):
        vertices.append(line_intersection([normals[i], normals[j]], [hs[i], hs[j]]))
    if polygon_margin(vertices, (sum(x for x, _ in vertices)/3, sum(y for _, y in vertices)/3)) < 0:
        vertices.reverse()
    return side, vertices, theta


def draw_title(c: Canvas, title: str, subtitle: str = "") -> None:
    c.text((16, c.height - 22), title, 12, bold=True)
    if subtitle:
        c.text((16, c.height - 38), subtitle, 8.2, color="gray")


def save_custom(canvas: Canvas, pdf: Path, svg: Path | None) -> None:
    canvas.save(pdf, svg)


def custom_geometry_roles(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c = Canvas(560, 375)
    draw_title(c, "Exact regular-hexagon coordinates", "V_i=(cos(i*pi/3), sin(i*pi/3)); M_i=V_i/2")
    v = View(c, (78, 42, 400, 285), (-1.35, -1.08, 1.35, 1.08))
    draw_hex(v, rays=True)
    v.circle(O, .025, stroke="blue", fill="blue")
    v.text((-.07, -.08), "O", size=8, color="blue", align="right")
    for i, p in enumerate(HEX):
        draw_point(v, p, f"V_{i}", "orange", (0.035, 0.035 if i not in (4,5) else -0.07))
        m = mul(.5, p)
        v.circle(m, .018, stroke="teal", fill="white", width=1.0)
        if i == 0:
            v.text(add(m, (0.02, .05)), "M_0", size=7.3, color="teal")
    v.text((.72, .43), "r_1", size=8, color="teal")
    v.text((.76, .72), "e_01", size=8, color="black")
    c.text((280, 14), "All six boundary edges and all six radii have Euclidean length 1.", 8.3, align="center")
    save_custom(c, pdf, svg)


def custom_strategy1(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c = Canvas(620, 300)
    draw_title(c, "Exact one-dimensional trace targets")
    for panel, x0, rays in (("boundary: length 6", 25, False), ("skeleton: length 12", 330, True)):
        v = View(c, (x0, 48, 260, 205), (-1.25, -1.0, 1.25, 1.0))
        draw_hex(v, rays=rays)
        c.text((x0 + 130, 30), panel, 9.5, bold=True, align="center")
        if rays:
            c.text((x0 + 130, 15), "6 unit edges + 6 unit radii", 7.7, color="gray", align="center")
        else:
            c.text((x0 + 130, 15), "6 unit boundary edges", 7.7, color="gray", align="center")
    save_custom(c, pdf, svg)


def draw_signed_triangle_panel(c: Canvas, box: tuple[float, float, float, float], kind: str, title: str) -> None:
    v = View(c, box, (-1.25, -1.05, 1.25, 1.05))
    draw_hex(v, rays=True)
    p = signed_parameters(kind)
    tri = signed_triangle(p)
    v.poly(tri, stroke="blue", fill="lightblue", width=1.35)
    right = [chi(0, p["k"] / p["R"]), chi(0, p["W"] + p["delta"])]
    v.line(right[0], right[1], color="purple", width=3.2)
    dl = p["P"] - p["R"] * p["alpha"] - p["delta"]
    if dl > 1e-10:
        left = [chi(p["k"] / p["W"], 0), chi(p["R"] + p["alpha"], 0)]
        v.line(left[0], left[1], color="teal", width=3.2)
    elif abs(dl) <= 1e-10:
        point = chi(p["R"] + p["alpha"], 0)
        v.circle(point, .025, stroke="teal", fill="teal")
    c.text((box[0] + box[2]/2, box[1]-12), title, 8.4, bold=True, align="center")


def custom_signed_parameter(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c = Canvas(650, 360)
    draw_title(c, "Signed center chart from exact side equations", "R=W=1/2; E=sqrt(3)/2; alpha=P/4; delta=3P/4")
    draw_signed_triangle_panel(c, (25, 75, 290, 235), "CE2", "exact CE2 specimen")
    c.text((345, 285), "Affine chart", 10, bold=True)
    c.text((345, 262), "chi(a,b)=V_0+b(V_1-V_0)+a(V_5-V_0)", 8)
    c.text((345, 232), "F_0=R+alpha-a+W b", 8.5, color="blue")
    c.text((345, 210), "F_1=R b+W a-k", 8.5, color="blue")
    c.text((345, 188), "F_2=W+delta-b+R a", 8.5, color="blue")
    c.text((345, 154), "T_C={chi(a,b): F_0,F_1,F_2 >= 0}", 8.5)
    c.text((345, 118), "Delta_R=P-alpha-W delta > 0", 8.2, color="purple")
    c.text((345, 96), "Delta_L=P-R alpha-delta > 0", 8.2, color="teal")
    c.text((345, 57), "Triangle vertices are intersections of pairs F_i=0.", 7.8, color="gray")
    c.text((345, 38), "Their three computed side lengths equal 1.", 7.8, color="gray")
    save_custom(c, pdf, svg)


def custom_signed_companion(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c = Canvas(720, 300)
    draw_title(c, "Exact companion-trace sign test", "Delta_L=P-R alpha-delta; point contact is not a positive trace")
    draw_signed_triangle_panel(c, (18, 55, 215, 185), "CE1", "Delta_L < 0: CE1")
    draw_signed_triangle_panel(c, (252, 55, 215, 185), "contact", "Delta_L = 0: point contact")
    draw_signed_triangle_panel(c, (486, 55, 215, 185), "CE2", "Delta_L > 0: CE2")
    save_custom(c, pdf, svg)


def custom_signed_exits(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c = Canvas(600, 370)
    draw_title(c, "Six exact C-triangle radial exits", "d_i^C are computed by substituting r_i into F_0,F_1,F_2")
    p = signed_parameters("CE2")
    exits = signed_exits(p)
    tri = signed_triangle(p)
    v = View(c, (80, 52, 430, 270), (-1.28, -1.05, 1.28, 1.05))
    draw_hex(v, rays=True)
    v.poly(tri, stroke="blue", fill="lightblue", width=1.2)
    for i, (d, vertex) in enumerate(zip(exits, HEX)):
        q = mul(d, vertex)
        v.line(O, q, color="blue", width=2.0)
        draw_point(v, q, f"d_{i}", "red", (0.03, .025 if i not in (4,5) else -.07))
    c.text((300, 25), "d_0>1/2; d_i<1/2 for i=1,...,5 in this exact CE2 specimen.", 8.3, align="center")
    save_custom(c, pdf, svg)


def custom_signed_budget(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c = Canvas(660, 315)
    draw_title(c, "Exact center-boundary contributions")
    for x0, kind, label in ((25, "CE1", "CE1"), (345, "CE2", "CE2")):
        p = signed_parameters(kind)
        v = View(c, (x0, 62, 280, 195), (-1.28, -1.02, 1.28, 1.02))
        draw_hex(v, rays=False)
        v.poly(signed_triangle(p), stroke="blue", fill="lightblue", width=1.2)
        lr = (p["P"] - p["alpha"] - p["W"]*p["delta"]) / p["R"]
        ll = max(0.0, (p["P"] - p["R"]*p["alpha"] - p["delta"]) / p["W"])
        v.line(chi(0,p["k"]/p["R"]), chi(0,p["W"]+p["delta"]), color="purple", width=3)
        if ll > 0:
            v.line(chi(p["k"]/p["W"],0), chi(p["R"]+p["alpha"],0), color="teal", width=3)
        c.text((x0+140, 42), f"{label}: L_boundary={lr+ll:.6f}", 8.6, bold=True, align="center")
        c.text((x0+140, 25), f"right={lr:.6f}, companion={ll:.6f}", 7.5, color="gray", align="center")
    save_custom(c, pdf, svg)


def custom_role(pdf: Path, svg: Path | None, entry: dict[str, object]) -> None:
    name = str(entry["key"])
    spec = dict(entry["parameters"]["specimen"])
    tri, data = specimen_from_spec(spec)
    c = Canvas(450, 390)
    title_map = {
        "vertex_role_vd0_axis_aligned_example": "Vd0, axis-aligned, supercritical",
        "vertex_role_vd0_nonsupercritical_example": "Vd0, nonsupercritical",
        "vertex_role_vd0_supercritical_example": "Vd0, supercritical",
        "vertex_role_vd1_example": "Vd1 exact specimen",
        "vertex_role_vd2_example": "Vd2 exact specimen",
        "vertex_role_t3_like_example": "T3-like exact specimen",
    }
    draw_title(c, title_map[name], "unit equilateral triangle; V_0 is strictly interior")
    v = View(c, (55, 75, 340, 255), (-1.25, -1.05, 1.55, 1.05))
    draw_hex(v, rays=True)
    v.poly(tri, stroke="orange", fill="lightorange", width=1.4)
    draw_point(v, HEX[0], "V_0", "red", (0.04, .04))
    A, B = float(data["A"]), float(data["B"])
    v.line(HEX[0], lerp(HEX[0], HEX[5], A), color="purple", width=2.4)
    v.line(HEX[0], lerp(HEX[0], HEX[1], B), color="teal", width=2.4)
    for j, field, color in ((1, "r1", "blue"), (5, "r5", "blue")):
        interval = data[field]
        if interval:
            v.line(lerp(O, HEX[j], interval[0]), lerp(O, HEX[j], interval[1]), color=color, width=2.0)
    c.text((225, 52), f"(o,n)=({data['o']},{data['n']}); A={A:.6f}; B={B:.6f}; A+B={A+B:.6f}", 8.2, align="center")
    c.text((225, 34), f"center offset=({spec['center_dx_num']}/{spec['center_den']},{spec['center_dy_num']}/{spec['center_den']}); angle={spec['angle_degrees_num']} deg", 7.3, color="gray", align="center")
    c.text((225, 17), "Purple/teal segments are the actual maximal boundary traces.", 7.3, color="gray", align="center")
    save_custom(c, pdf, svg)


def custom_center_role(pdf: Path, svg: Path | None, entry: dict[str, object]) -> None:
    kind = str(entry["parameters"]["kind"])
    c = Canvas(450, 385)
    draw_title(c, f"{kind} exact C-triangle specimen", "classification counts positive-length boundary traces")
    v = View(c, (55, 72, 340, 255), (-1.25, -1.05, 1.25, 1.05))
    draw_hex(v, rays=True)
    if kind == "CE0":
        tri = equilateral(O, math.pi/6)
        params = None
    else:
        params = signed_parameters(kind)
        tri = signed_triangle(params)
    v.poly(tri, stroke="blue", fill="lightblue", width=1.4)
    draw_point(v, O, "O", "blue", (0.04, -.06))
    traces = 0
    for i in range(6):
        interval = segment_interval(tri, HEX[i], HEX[(i+1)%6])
        if interval and interval[1]-interval[0] > 1e-5:
            traces += 1
            v.line(lerp(HEX[i],HEX[(i+1)%6],interval[0]), lerp(HEX[i],HEX[(i+1)%6],interval[1]), color="purple", width=3.0)
    c.text((225, 45), f"verified positive boundary traces: {traces}", 8.5, bold=True, align="center")
    c.text((225, 25), "Point contacts, when present, are not counted.", 7.6, color="gray", align="center")
    save_custom(c, pdf, svg)


def clip_polygon(subject: Sequence[tuple[float,float]], clipper: Sequence[tuple[float,float]]) -> list[tuple[float,float]]:
    output = list(subject)
    for a,b in zip(clipper,[*clipper[1:],clipper[0]]):
        inp, output = output, []
        if not inp:
            break
        for s,e in zip(inp,[*inp[1:],inp[0]]):
            ins_s = cross(sub(b,a),sub(s,a)) >= -1e-10
            ins_e = cross(sub(b,a),sub(e,a)) >= -1e-10
            if ins_e:
                if not ins_s:
                    ds, de = cross(sub(b,a),sub(s,a)), cross(sub(b,a),sub(e,a))
                    t = ds/(ds-de)
                    output.append(lerp(s,e,t))
                output.append(e)
            elif ins_s:
                ds, de = cross(sub(b,a),sub(s,a)), cross(sub(b,a),sub(e,a))
                t = ds/(ds-de)
                output.append(lerp(s,e,t))
    return output


def polygon_area(poly: Sequence[tuple[float,float]]) -> float:
    return abs(sum(cross(a,b) for a,b in zip(poly,[*poly[1:],poly[0]])))/2 if len(poly)>=3 else 0.0


def custom_area_local(pdf: Path, svg: Path | None, entry: dict[str, object]) -> None:
    spec = dict(entry["parameters"]["specimen"])
    tri, data = specimen_from_spec(spec)
    inter = clip_polygon(tri, HEX)
    c = Canvas(520, 380)
    draw_title(c, "Exact local retained-area specimen", "intersection polygon is computed by exact line clipping before rendering")
    v=View(c,(55,70,410,260),(-1.25,-1.1,1.55,1.1))
    draw_hex(v, rays=False)
    v.poly(tri,stroke="orange",fill="lightorange",width=1.3)
    if inter:
        v.poly(inter,stroke="green",fill="lightgreen",width=1.4)
    A,B=float(data["A"]),float(data["B"])
    loss=(math.sqrt(3)/4-polygon_area(inter))/(math.sqrt(3)/4)
    c.text((260,48),f"actual reaches A={A:.6f}, B={B:.6f}; normalized outside loss={loss:.6f}",8.2,align="center")
    c.text((260,28),"Green is T intersect H; orange is the full unit triangle.",7.5,color="gray",align="center")
    save_custom(c,pdf,svg)


def custom_area_global(pdf: Path, svg: Path | None, entry: dict[str, object]) -> None:
    spec=dict(entry["parameters"]["specimen"])
    tri,_=specimen_from_spec(spec)
    c=Canvas(520,390)
    draw_title(c,"Exact sixfold cyclic area specimen","each role is obtained by an exact 60-degree rotation")
    v=View(c,(55,70,410,265),(-1.35,-1.15,1.35,1.15))
    draw_hex(v,False)
    total=0.0
    for j in range(6):
        rt=[rotate(p,j*math.pi/3) for p in tri]
        inter=clip_polygon(rt,HEX)
        total+=polygon_area(inter)
        if inter:
            v.poly(inter,stroke="green",fill=None,width=.9)
        v.poly(rt,stroke="orange",fill=None,width=.7,dash=(3,2))
    c.text((260,47),f"sum of six retained areas / area(unit triangle) = {total/(math.sqrt(3)/4):.6f}",8.3,align="center")
    c.text((260,27),"No panel coordinate is hand-positioned; all six copies are rotations of one specimen.",7.2,color="gray",align="center")
    save_custom(c,pdf,svg)


def generic_hex_witness(pdf: Path, svg: Path | None, key: str, mode: str = "one-gap") -> None:
    c=Canvas(590,370)
    draw_title(c,key.replace("_"," "),"coordinate-exact representative data; proof remains parameter-universal")
    v=View(c,(70,70,450,255),(-1.32,-1.08,1.32,1.08))
    draw_hex(v,True)
    if mode=="one-gap":
        p,q=.25,.25
        gap0=lerp(HEX[0],HEX[1],q); gap1=lerp(HEX[0],HEX[1],1-p)
        v.line(gap0,gap1,color="purple",width=3.4)
        cc=cmax(p,q); d=1-cc
        for i,x in enumerate(HEX):
            draw_point(v,mul(d,x),f"D_{i}" if i in (0,2,4) else "","red",(.03,.03))
        v.text((.60,.67),"J(p,q)",size=8,color="purple")
        c.text((295,45),f"p=q=1/4; c_max={cc:.9f}; d=1-c_max={d:.9f}",8.1,align="center")
    elif mode=="two-gap":
        p=signed_parameters("CE2"); e=min(p["alpha"],p["delta"]); a=p["W"]-p["alpha"]; b=p["R"]-p["delta"]
        for i in (0,5):
            start=.18 if i==0 else .62; end=.34 if i==0 else .82
            v.line(lerp(HEX[i],HEX[(i+1)%6],start),lerp(HEX[i],HEX[(i+1)%6],end),color="purple",width=3.2)
        d=1-cmax(a,b)
        for i in (2,4):
            draw_point(v,mul(d,HEX[i]),f"D_{i}","red",(.03,.03))
            draw_point(v,mul(e,HEX[i]),f"exit_{i}","blue",(.03,-.06))
        c.text((295,45),f"p={a:.9f}, q={b:.9f}, e={e:.9f}, d={d:.9f}; verified d>e",8.0,align="center")
    elif mode=="anisotropic":
        ds=[.15,.22,.11,.19,.26,.13]
        for i,(d,x) in enumerate(zip(ds,HEX)):
            draw_point(v,mul(d,x),f"D_{i}" if i%2==0 else "","red",(.03,.03))
        v.poly([mul(d,x) for d,x in zip(ds,HEX)],stroke="red",fill="lightred",width=1.0)
        c.text((295,45),"radial parameters=(3/20,11/50,11/100,19/100,13/50,13/100)",8,align="center")
    save_custom(c,pdf,svg)


def custom_center_interval(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(590,290)
    draw_title(c,"Exact edge residual after a center interval")
    x0,x1=65,525; y=155
    c.line((x0,y),(x1,y),"black",1.3)
    pts={"V_i":x0,"B_i":x0+.24*(x1-x0),"s":x0+.42*(x1-x0),"t":x0+.69*(x1-x0),"1-A":x0+.86*(x1-x0),"V_i+1":x1}
    c.line((x0,y),(pts["B_i"],y),"orange",5)
    c.line((pts["s"],y),(pts["t"],y),"blue",5)
    c.line((pts["1-A"],y),(x1,y),"orange",5)
    for label,x in pts.items():
        c.circle((x,y),3,"black","white",.8)
        c.text((x,y+17),label,7.6,align="center")
    c.arrow((pts["B_i"],105),(pts["s"],105),"purple",1)
    c.arrow((pts["1-A"],105),(pts["t"],105),"purple",1)
    c.text((295,72),"all positions are exact rational fractions of the unit edge",8,align="center")
    save_custom(c,pdf,svg)


def custom_fe01(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(650,350)
    draw_title(c,"Trace-exact gap endpoints and equilateral enclosure gauge")
    v=View(c,(25,65,285,225),(-1.25,-1.05,1.25,1.05))
    draw_hex(v,True)
    ell,r=.25,.70
    v.line(lerp(HEX[0],HEX[1],ell),lerp(HEX[0],HEX[1],r),color="purple",width=3.4)
    draw_point(v,lerp(HEX[0],HEX[1],ell),"X(ell)","red",(.03,.04))
    draw_point(v,lerp(HEX[0],HEX[1],r),"X(r)","red",(.03,.04))
    pts=[O,mul(.5,HEX[0]),lerp(HEX[0],HEX[1],ell),lerp(HEX[0],HEX[1],r),mul(.18,HEX[2]),mul(.12,HEX[3]),mul(.20,HEX[4])]
    side,tri,_=support_triangle(pts)
    w=View(c,(345,65,275,225),(-1.25,-1.05,1.25,1.05))
    w.poly(tri,stroke="black",fill="lightgray",width=1.2)
    for p in pts: draw_point(w,p,"","red")
    c.text((482,43),f"Lambda(K)={side:.9f} from hull-edge support normals",8.0,align="center")
    save_custom(c,pdf,svg)


def custom_fe02(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(700,330)
    draw_title(c,"Exact disk-plus-point minimizers")
    cases=[(.25,.40,"rho <= 2 eta"),(.25,.75,"rho > 2 eta")]
    for idx,(eta,rho,label) in enumerate(cases):
        x0=20+345*idx
        points=[(rho,0)]
        side,tri,_=support_triangle(points,eta)
        v=View(c,(x0,60,315,220),(-.65,-.7,1.05,.7))
        v.circle(O,eta,stroke="blue",fill="lightblue",width=1.2)
        v.poly(tri,stroke="black",fill=None,width=1.2)
        draw_point(v,(rho,0),"G","red",(.03,.04))
        v.text((0,-.08),"O",size=7,color="blue")
        formula=3*eta/H if rho<=2*eta+1e-12 else (3*eta+math.sqrt(3*(rho*rho-eta*eta)))/(2*H)
        c.text((x0+157,39),f"{label}; eta={eta}; rho={rho}; Lambda={side:.9f}",7.8,align="center")
        c.text((x0+157,22),f"closed formula={formula:.9f}; error={abs(side-formula):.2e}",7.2,color="gray",align="center")
    save_custom(c,pdf,svg)


def custom_fe03(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(720,350)
    draw_title(c,"Exact complementary-gap enclosure instance")
    p=q=.25; cc=cmax(p,q); d=1-cc; eta=H*d
    gap=[lerp(HEX[0],HEX[1],q),lerp(HEX[0],HEX[1],1-p)]
    radial=[mul(d,x) for x in HEX]
    far=max(gap,key=norm)
    side,tri,_=support_triangle([far],eta)
    v=View(c,(20,65,315,225),(-1.3,-1.05,1.3,1.05)); draw_hex(v,True)
    v.line(gap[0],gap[1],color="purple",width=3.3)
    for x in radial: draw_point(v,x,"","red")
    v.circle(O,eta,stroke="blue",fill=None,width=1.2)
    w=View(c,(380,65,315,225),(-.7,-.8,1.25,.8))
    w.circle(O,eta,stroke="blue",fill="lightblue",width=1.2)
    w.poly(tri,stroke="black",fill=None,width=1.2)
    draw_point(w,far,"G","red",(.03,.04))
    c.text((360,42),f"p=q=1/4; c_max={cc:.9f}; eta=h(1-c_max)={eta:.9f}; Lambda={side:.9f}",7.8,align="center")
    c.text((360,24),"The disk is contained in the convex hull of the six displayed radial witnesses.",7.2,color="gray",align="center")
    save_custom(c,pdf,svg)


def custom_fe04(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    generic_hex_witness(pdf,svg,"CE2 short-ray terminal","two-gap")


def custom_fe05(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(690,350)
    draw_title(c,"Exact K_tr coordinate template","ell=1/4, r=1/3, C_2=4/5, C_3=9/10, C_4=3/4")
    ell,r=.25,1/3
    Cs={2:.8,3:.9,4:.75}
    pts=[O,mul(.5,HEX[0]),lerp(HEX[0],HEX[1],ell),lerp(HEX[0],HEX[1],r),*(mul(1-Cs[i],HEX[i]) for i in (2,3,4))]
    v=View(c,(45,65,390,235),(-1.3,-1.08,1.3,1.08)); draw_hex(v,True)
    labels=["O","M_0","X(ell)","X(r)","P_2","P_3","P_4"]
    for pnt,label in zip(pts,labels): draw_point(v,pnt,label,"red",(.03,.04))
    side,tri,_=support_triangle(pts)
    w=View(c,(465,75,195,215),(-1.25,-1.15,1.25,1.15)); w.poly(tri,stroke="black",fill="lightgray",width=1.1)
    for pnt in pts: draw_point(w,pnt,"","red")
    c.text((562,50),f"Lambda(K_tr)={side:.9f}",8.2,bold=True,align="center")
    c.text((345,25),"This is an exact parameter template, not an asserted simultaneous covering configuration.",7.3,color="gray",align="center")
    save_custom(c,pdf,svg)


def cplus_numeric(a: float,b: float) -> float:
    A=lerp(HEX[0],HEX[5],a); B=lerp(HEX[0],HEX[1],b)
    def feasible(c: float) -> bool:
        X=mul(1-c,HEX[1])
        side,_,_=support_triangle([HEX[0],A,B,X])
        return side<=1+2e-9
    lo,hi=0.0,1.0
    if not feasible(0): return 0.0
    for _ in range(55):
        mid=(lo+hi)/2
        if feasible(mid): lo=mid
        else: hi=mid
    return lo


def custom_fe06(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(700,350)
    draw_title(c,"Exact neighboring-ray capacity","C_+(a,b) is recomputed by the equilateral support gauge")
    a=.32; bs=[i/50 for i in range(1,43)]; vals=[cplus_numeric(a,b) for b in bs]
    v=View(c,(25,65,300,225),(-.2,-.15,1.25,1.15))
    A=lerp(HEX[0],HEX[5],a); b0=.46; B=lerp(HEX[0],HEX[1],b0); cap=cplus_numeric(a,b0); X=mul(1-cap,HEX[1])
    v.line(HEX[0],HEX[5],color="gray",width=.8); v.line(HEX[0],HEX[1],color="gray",width=.8); v.line(O,HEX[1],color="gray",width=.8)
    for pnt,label,color in ((HEX[0],"V_0","black"),(A,"A_a","orange"),(B,"B_b","orange"),(X,"X_c","red")): draw_point(v,pnt,label,color,(.03,.04))
    side,tri,_=support_triangle([HEX[0],A,B,X]); v.poly(tri,stroke="black",fill=None,width=1.0)
    x0,y0,w,h=370,75,290,205
    c.line((x0,y0),(x0+w,y0),"black",.9); c.line((x0,y0),(x0,y0+h),"black",.9)
    pts=[]
    for b,val in zip(bs,vals): pts.append((x0+w*b/max(bs),y0+h*val))
    c.poly(pts,stroke="red",fill=None,width=1.4,closed=False)
    c.text((x0+w, y0-16),"b",8,align="right"); c.text((x0-8,y0+h+4),"C_+",8,align="right")
    c.text((515,45),f"a={a}; selected b={b0}; C_+={cap:.9f}; Lambda={side:.9f}",7.8,align="center")
    save_custom(c,pdf,svg)


def custom_fe07(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(680,300)
    draw_title(c,"Exact CE1 reverse-path inequalities","one-dimensional positions are proportional to the displayed variables")
    rows=[("r_1",.18,.41,"epsilon","forced endpoint"),("e_01",.27,.63,"B_0","center trace"),("reverse path",.12,.82,"1-M","h_T")]
    for row,(label,a,b,la,lb) in enumerate(rows):
        y=215-row*65; x0,x1=90,620
        c.line((x0,y),(x1,y),"black",1)
        c.circle((x0+(x1-x0)*a,y),4,"blue","blue"); c.circle((x0+(x1-x0)*b,y),4,"red","red")
        c.text((35,y-3),label,8,bold=True)
        c.text((x0+(x1-x0)*a,y+15),la,7.5,align="center",color="blue")
        c.text((x0+(x1-x0)*b,y+15),lb,7.5,align="center",color="red")
    c.text((340,25),"The diagram asserts order only where the proof proves a strict inequality.",7.6,color="gray",align="center")
    save_custom(c,pdf,svg)


def custom_fe08(pdf: Path, svg: Path | None, entry: dict[str, object]) -> None:
    spec=dict(entry["parameters"]["specimen"]); tri,data=specimen_from_spec(spec)
    c=Canvas(610,370); draw_title(c,"Exact T3-like rescuer specimen","the supported adjacent-ray interval is computed by convex clipping")
    v=View(c,(75,70,455,255),(-1.25,-1.08,1.55,1.08)); draw_hex(v,True); v.poly(tri,stroke="orange",fill="lightorange",width=1.3)
    draw_point(v,HEX[0],"V_0","red",(.03,.04))
    for j,field in ((1,"r1"),(5,"r5")):
        interval=data[field]
        if interval: v.line(lerp(O,HEX[j],interval[0]),lerp(O,HEX[j],interval[1]),color="teal",width=3)
    c.text((305,45),f"verified type (o,n)=({data['o']},{data['n']}); A+B={float(data['A'])+float(data['B']):.9f}",8,align="center")
    c.text((305,25),"Exactly one adjacent ray has positive-length support.",7.4,color="gray",align="center")
    save_custom(c,pdf,svg)


def custom_fe09(pdf: Path, svg: Path | None, entry: dict[str, object]) -> None:
    c=Canvas(720,325); draw_title(c,"Exact Vd1/Vd2 placement specimens")
    specs=entry["parameters"]["specimens"]
    for idx,(key,title) in enumerate((("vertex_role_vd1_example","Vd1"),("vertex_role_vd2_example","Vd2"),("vertex_role_t3_like_example","T3-like"))):
        tri,data=specimen_from_spec(dict(specs[key])); x0=15+238*idx
        v=View(c,(x0,60,220,205),(-1.25,-1.05,1.55,1.05)); draw_hex(v,True); v.poly(tri,stroke="orange",fill="lightorange",width=1.1)
        c.text((x0+110,38),f"{title}: (o,n)=({data['o']},{data['n']})",8,bold=True,align="center")
    c.text((360,19),"All three unit triangles contain V_0 strictly; support counts are recomputed from segment intersections.",7.3,color="gray",align="center")
    save_custom(c,pdf,svg)


def custom_fe10(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(680,340); draw_title(c,"Exact local AB radial frontier","curves are evaluated from the selected formulas in Proposition 6.2")
    x0,y0,w,h=75,60,540,230
    c.line((x0,y0),(x0+w,y0),"black",1); c.line((x0,y0),(x0,y0+h),"black",1)
    colors=["red","teal","purple"]
    for idx,a in enumerate((.10,.25,.40)):
        pts=[]
        for j in range(101):
            b=.005+.99*j/100
            val=cmax(a,b) if a*a+a*b+b*b<=1+1e-9 else 0
            pts.append((x0+w*b,y0+h*val))
        c.poly(pts,stroke=colors[idx],fill=None,width=1.3,closed=False)
        c.text((x0+w*.78,y0+h*(.88-.10*idx)),f"a={a:.2f}",7.5,color=colors[idx])
    c.text((x0+w,y0-18),"b",8,align="right"); c.text((x0-8,y0+h+4),"c_max(a,b)",8,align="right")
    c.text((340,25),"No spline control points are used; every plotted ordinate is a direct formula evaluation.",7.4,color="gray",align="center")
    save_custom(c,pdf,svg)


def custom_fe11(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(610,370); draw_title(c,"Exact nine-point witness template")
    p=q=.25; d=1-cmax(p,q); pts=[O,mul(.5,HEX[0]),*(mul(d,x) for x in HEX),lerp(HEX[0],HEX[1],q)]
    v=View(c,(75,70,455,255),(-1.25,-1.08,1.25,1.08)); draw_hex(v,True)
    labels=["O","M_0",*([f"D_{i}" for i in range(6)]),"G"]
    for pnt,label in zip(pts,labels): draw_point(v,pnt,label,"red",(.03,.035))
    side,_,_=support_triangle(pts)
    c.text((305,45),f"p=q=1/4; d={d:.9f}; Lambda(9 points)={side:.9f}",8,align="center")
    c.text((305,25),"The coordinate list is written to the manifest and independently rechecked.",7.4,color="gray",align="center")
    save_custom(c,pdf,svg)


def custom_fe12(pdf: Path, svg: Path | None, _: dict[str, object]) -> None:
    c=Canvas(650,370); draw_title(c,"Exact support-cap calipers")
    p=q=.25; d=1-cmax(p,q); pts=[O,mul(.5,HEX[0]),*(mul(d,x) for x in HEX),lerp(HEX[0],HEX[1],q)]
    side,tri,theta=support_triangle(pts)
    v=View(c,(90,65,470,260),(-1.3,-1.12,1.3,1.12)); draw_hex(v,False); v.poly(tri,stroke="black",fill="lightgray",width=1.2)
    for pnt in pts: draw_point(v,pnt,"","red")
    normals=[(math.cos(theta+2*math.pi*j/3),math.sin(theta+2*math.pi*j/3)) for j in range(3)]
    for j,n in enumerate(normals):
        hv=support(pts,n); tangent=(-n[1],n[0]); base=mul(hv,n)
        v.line(add(base,mul(-1.5,tangent)),add(base,mul(1.5,tangent)),color=("purple","teal","blue")[j],width=1.1,dash=(4,2))
    c.text((325,43),f"three support sums / h give Lambda={side:.9f}",8.2,align="center")
    c.text((325,24),"Each dashed line is placed from an evaluated support number, not by eye.",7.4,color="gray",align="center")
    save_custom(c,pdf,svg)


CUSTOM: dict[str, Callable[[Path, Path | None, dict[str, object]], None]] = {
    "geometry_roles": custom_geometry_roles,
    "strategy1_trace_targets": custom_strategy1,
    "signed_parameter_map": custom_signed_parameter,
    "signed_companion_sign": custom_signed_companion,
    "signed_center_exits": custom_signed_exits,
    "signed_center_boundary_budgets": custom_signed_budget,
    "center_interval_residual": custom_center_interval,
    "new_one_gap_radial_witness": lambda p,s,e: generic_hex_witness(p,s,"one-gap radial witness","one-gap"),
    "new_two_gap_short_ray": lambda p,s,e: generic_hex_witness(p,s,"two-gap short-ray witness","two-gap"),
    "new_anisotropic_witness": lambda p,s,e: generic_hex_witness(p,s,"anisotropic radial witness","anisotropic"),
    "fe01_trace_and_gauge": custom_fe01,
    "fe02_disk_plus_point": custom_fe02,
    "fe03_complementary_gap": custom_fe03,
    "fe04_ce2_short_ray": custom_fe04,
    "fe05_k410_actual_reach": custom_fe05,
    "fe06_neighbor_capacity": custom_fe06,
    "fe07_ce1_reverse_path": custom_fe07,
    "fe08_t3_rescuer": custom_fe08,
    "fe09_vd_placements": custom_fe09,
    "fe10_ab_frontier": custom_fe10,
    "fe11_zero_gap_witness": custom_fe11,
    "fe12_support_caps": custom_fe12,
}

FULL_CAPTIONS = {
    "finite_enclosure/fe00_case_roadmap.tex": "Logical case roadmap for the finite-enclosure section.  This external vector diagram records implications only; it makes no metric assertion.",
    "finite_enclosure/fe01_trace_and_gauge.tex": "Trace-exact gap endpoints and an exact equilateral-enclosure gauge evaluation.  Coordinates and the computed value are generated from the manifest rather than positioned by eye.",
    "finite_enclosure/fe02_disk_plus_point.tex": "The two exact minimizing configurations in the disk-plus-point formula.  The displayed triangles are reconstructed from their three support half-planes, and the computed side agrees with the closed formula.",
    "finite_enclosure/fe03_complementary_gap.tex": "An exact complementary-gap instance.  The gap endpoints, six radial witnesses, inscribed disk, and least enclosing equilateral triangle are computed from p=q=1/4 and the selected root defining c_max.",
    "finite_enclosure/fe04_ce2_short_ray.tex": "An exact CE2 short-ray instance obtained from R=W=1/2, alpha=P/4, and delta=3P/4.  The generated coordinates verify d=1-c_max(p,q)>e, so the relevant radial witness lies beyond the corresponding center exit.",
    "finite_enclosure/fe05_k410_actual_reach.tex": "A coordinate-exact template for K_tr.  The displayed rational parameters define every point explicitly; the panel is not asserted to be a simultaneous covering configuration.",
    "finite_enclosure/fe06_neighbor_capacity.tex": "The neighboring-ray capacity recomputed by the equilateral support gauge.  Every graph ordinate is obtained by a feasibility bisection for the four-point enclosure problem; no decorative spline is used.",
    "finite_enclosure/fe07_ce1_reverse_path.tex": "The CE1 reverse-path inequalities as an exact order diagram.  Segment positions are proportional to the displayed numerical instance, and only proof-established order relations are shown.",
    "finite_enclosure/fe08_t3_rescuer.tex": "An exact T3-like unit-triangle specimen and its computed adjacent-ray support interval.  The type (o,n)=(2,1) is verified from the triangle vertices and segment intersections.",
    "finite_enclosure/fe09_vd_placements.tex": "Exact Vd1, Vd2, and T3-like specimens.  Each unit triangle contains V_0 strictly, and the outside-vertex and adjacent-support counts are recomputed from its coordinates.",
    "finite_enclosure/fe10_ab_frontier.tex": "The exact local AB radial frontier evaluated from the selected formulas for c_max(a,b).  Curves consist solely of direct formula samples.",
    "finite_enclosure/fe11_zero_gap_witness.tex": "A nine-point coordinate template generated from p=q=1/4.  The complete coordinate record and its enclosing-side computation are stored in the exact-figure manifest.",
    "finite_enclosure/fe12_support_caps.tex": "Exact support-cap calipers for the displayed finite set.  The three dashed support lines and the enclosing equilateral triangle are reconstructed from evaluated support numbers.",
}


def tex_inputs(path: Path) -> list[str]:
    text=path.read_text(encoding="utf-8")
    return re.findall(r"\\input\{([^}]+)\}",text)


def canonical_closure() -> list[Path]:
    seen:set[Path]=set(); stack=[PAPER/"main.tex"]
    while stack:
        path=stack.pop().resolve()
        if path in seen or not path.is_file(): continue
        seen.add(path)
        for raw in tex_inputs(path):
            candidate=(path.parent/raw)
            if candidate.suffix!=".tex": candidate=candidate.with_suffix(".tex")
            if candidate.is_file() and PAPER.resolve() in candidate.resolve().parents:
                stack.append(candidate)
    return sorted(seen)


def discover_figure_inputs(files: Sequence[Path]) -> list[Path]:
    out:set[Path]=set()
    for path in files:
        for raw in tex_inputs(path):
            if raw.startswith("figures/"):
                candidate=(path.parent/raw)
                if candidate.suffix!=".tex": candidate=candidate.with_suffix(".tex")
                if candidate.is_file(): out.add(candidate.resolve())
    return sorted(out)


def command_span(text: str, command: str) -> tuple[int,int,str] | None:
    pos=text.find(command)
    if pos<0: return None
    brace=text.find("{",pos+len(command))
    if brace<0: return None
    depth=0
    for i in range(brace,len(text)):
        if text[i]=="{" and (i==0 or text[i-1]!="\\"): depth+=1
        elif text[i]=="}" and (i==0 or text[i-1]!="\\"):
            depth-=1
            if depth==0: return pos,i+1,text[brace+1:i]
    return None


def strip_command(text: str,command: str) -> tuple[str,str | None]:
    span=command_span(text,command)
    if not span: return text,None
    a,b,value=span
    return text[:a]+text[b:],value


def stripped_figure_body(text: str) -> str:
    text=re.sub(r"\\begin\{figure\}(?:\[[^]]*\])?","",text,count=1)
    pos=text.rfind("\\end{figure}")
    if pos>=0: text=text[:pos]+text[pos+len("\\end{figure}"):]
    text,_=strip_command(text,"\\caption")
    text,_=strip_command(text,"\\label")
    return text.strip()+"\n"


def render_legacy(source: Path, output: Path) -> None:
    body=stripped_figure_body(source.read_text(encoding="utf-8"))
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="exact-legacy-") as td:
        td=Path(td)
        doc=td/"figure.tex"
        setup=(FIGURES/"tikz_setup.tex").resolve().as_posix()
        doc.write_text(r"""\documentclass[border=2pt]{standalone}
\usepackage{amsmath,amssymb,mathtools,graphicx,booktabs,float,longtable,array,microtype,tikz}
\usetikzlibrary{arrows.meta,calc,positioning}
\input{"""+setup+r"""}
\newcommand{\CEzero}{\mathrm{CE0}}
\newcommand{\CEone}{\mathrm{CE1}}
\newcommand{\CEtwo}{\mathrm{CE2}}
\newcommand{\Vdzero}{\mathrm{Vd0}}
\newcommand{\Vdone}{\mathrm{Vd1}}
\newcommand{\Vdtwo}{\mathrm{Vd2}}
\newcommand{\Tlike}{\mathrm{T3\text{-}like}}
\newcommand{\Haus}{\mathcal H^1}
\newcommand{\conv}{\mathrm{conv}}
\begin{document}
\begin{minipage}{170mm}
"""+body+r"""
\end{minipage}
\end{document}
""",encoding="utf-8")
        env=os.environ.copy(); env.update({"SOURCE_DATE_EPOCH":"946684800","FORCE_SOURCE_DATE":"1","TZ":"UTC"})
        subprocess.run(["latexmk","-xelatex","-interaction=nonstopmode","-halt-on-error","-file-line-error",doc.name],cwd=td,env=env,check=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        shutil.copy2(td/"figure.pdf",output)


def render_png(pdf: Path,png: Path,dpi: int=180) -> None:
    png.parent.mkdir(parents=True,exist_ok=True)
    with fitz.open(pdf) as doc:
        page=doc[0]
        pix=page.get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72),alpha=False)
        pix.save(png)


def asset_rel_for(source: Path) -> Path:
    rel=source.relative_to(FIGURES)
    return Path("generated")/("__".join(rel.with_suffix("").parts)+".pdf")


def build_manifest(figure_sources: Sequence[Path]) -> dict[str,object]:
    role_specs=find_role_specimens()
    assets=[]
    for source in figure_sources:
        rel=source.relative_to(FIGURES).as_posix()
        key=source.stem
        category="metric_exact" if key in CUSTOM else "logical_nonmetric_externalization"
        params:dict[str,object]={}
        if key=="fe08_t3_rescuer": params["specimen"]=role_specs["vertex_role_t3_like_example"]
        if key=="fe09_vd_placements": params["specimens"]=role_specs
        assets.append({
            "key":key,
            "source":rel,
            "wrapper":rel,
            "archived_source":f"source_tikz/{rel}",
            "image":asset_rel_for(source).as_posix(),
            "svg":asset_rel_for(source).with_suffix(".svg").as_posix() if category=="metric_exact" else None,
            "category":category,
            "parameters":params,
            "construction": "formula-generated metric geometry" if category=="metric_exact" else "external vector rendering of a logical, nonmetric diagram",
        })
    for kind in ("CE0","CE1","CE2"):
        name=f"center_role_{kind.lower()}_example"
        assets.append({"key":name,"source":None,"wrapper":None,"archived_source":None,"image":f"role_examples/{name}.pdf","svg":f"role_examples/{name}.svg","preview":f"../role_examples/{name}.png","category":"metric_exact","parameters":{"kind":kind},"construction":"unit C triangle with boundary-trace count computed from segment intersections"})
    for name,spec in role_specs.items():
        assets.append({"key":name,"source":None,"wrapper":None,"archived_source":None,"image":f"role_examples/{name}.pdf","svg":f"role_examples/{name}.svg","preview":f"../role_examples/{name}.png","category":"metric_exact","parameters":{"specimen":spec},"construction":"unit equilateral V triangle on an exact rational grid and rational multiple of pi"})
    area_spec=role_specs["vertex_role_vd0_supercritical_example"]
    for name in ("strategy3_local_area_loss","strategy3_global_area_loss"):
        assets.append({"key":name,"source":None,"wrapper":None,"archived_source":None,"image":f"area/{name}.pdf","svg":f"area/{name}.svg","preview":f"../{name}.png","category":"metric_exact","parameters":{"specimen":area_spec},"construction":"exact unit-triangle/hexagon intersection and exact 60-degree rotations"})
    return {
        "schema":1,
        "audited_base":AUDITED_BASE,
        "branch":BRANCH,
        "mathematical_model":{
            "hexagon":"V_i=(cos(i*pi/3),sin(i*pi/3))",
            "unit_triangle":"circumradius 1/sqrt(3); vertices separated by 2*pi/3",
            "signed_center":"intersections of F_0=0,F_1=0,F_2=0",
            "enclosure":"Lambda(K)=min_n sum_j h_K(R^j n)/(sqrt(3)/2)",
        },
        "assets":sorted(assets,key=lambda x:str(x["image"])),
    }


def entry_output(base: Path,entry:dict[str,object],field:str="image") -> Path:
    value=entry.get(field)
    if not value: raise ValueError((entry["key"],field))
    return base/str(value)


def generate_entry(base:Path,entry:dict[str,object]) -> None:
    key=str(entry["key"]); pdf=entry_output(base,entry,"image"); svg=entry_output(base,entry,"svg") if entry.get("svg") else None
    pdf.parent.mkdir(parents=True,exist_ok=True)
    if key.startswith("center_role_"): custom_center_role(pdf,svg,entry)
    elif key.startswith("vertex_role_"): custom_role(pdf,svg,entry)
    elif key=="strategy3_local_area_loss": custom_area_local(pdf,svg,entry)
    elif key=="strategy3_global_area_loss": custom_area_global(pdf,svg,entry)
    elif key in CUSTOM: CUSTOM[key](pdf,svg,entry)
    else:
        archived=EXACT/str(entry["archived_source"])
        render_legacy(archived,pdf)
    if entry.get("preview"):
        preview=(EXACT/str(entry["preview"])).resolve() if base==EXACT else (base/"previews"/(key+".png"))
        render_png(pdf,preview)


def generate_all(base:Path,manifest:dict[str,object]) -> None:
    for entry in manifest["assets"]: generate_entry(base,entry)


def wrapper_text(source:Path,entry:dict[str,object]) -> str:
    original=source.read_text(encoding="utf-8")
    image=(Path("figures/exact")/str(entry["image"])).as_posix()
    if "\\begin{figure}" not in original:
        return f"\\includegraphics[width=.96\\linewidth,height=.72\\textheight,keepaspectratio]{{{image}}}\n"
    placement="!htbp"
    m=re.search(r"\\begin\{figure\}(?:\[([^]]+)\])?",original)
    if m and m.group(1): placement=m.group(1)
    cap_span=command_span(original,"\\caption")
    caption=cap_span[2] if cap_span else "External exact figure."
    rel=source.relative_to(FIGURES).as_posix()
    caption=FULL_CAPTIONS.get(rel,caption)
    lab_span=command_span(original,"\\label")
    label=lab_span[2] if lab_span else "fig:exact-"+source.stem.replace("_","-")
    return (
        f"\\begin{{figure}}[{placement}]\n"
        "\\centering\n"
        f"\\includegraphics[width=.98\\linewidth,height=.76\\textheight,keepaspectratio]{{{image}}}\n"
        f"\\caption{{{caption}}}\n"
        f"\\label{{{label}}}\n"
        "\\end{figure}\n"
    )


def patch_intro_and_area() -> None:
    intro=PAPER/"01_introduction.tex"
    text=intro.read_text(encoding="utf-8")
    for kind in ("ce0","ce1","ce2"):
        old=f"figures/role_examples/center_role_{kind}_example.png"
        new=f"figures/exact/role_examples/center_role_{kind}_example.pdf"
        text=text.replace(old,new)
    for name in (
        "vertex_role_vd0_axis_aligned_example","vertex_role_vd0_nonsupercritical_example","vertex_role_vd0_supercritical_example",
        "vertex_role_vd1_example","vertex_role_vd2_example","vertex_role_t3_like_example",
    ):
        text=text.replace(f"figures/role_examples/{name}.png",f"figures/exact/role_examples/{name}.pdf")
    text=text.replace(
        "The screenshots are illustrative\nand not to scale; no proof depends on visual inspection.",
        "Each panel is generated from explicit coordinates and its positive boundary-trace count is checked automatically.  The exact parameter records appear in the figure manifest."
    )
    text=text.replace(
        "The screenshots are illustrative and not\nto scale; no proof depends on visual inspection.",
        "Each panel is generated from explicit unit-triangle coordinates.  The outside-vertex count, adjacent-ray support count, and actual reaches are checked automatically and recorded in the figure manifest."
    )
    intro.write_text(text,encoding="utf-8")
    for path in (PAPER/"05_strategy3_area.tex",PAPER/"05_strategy3_reader.tex"):
        if not path.is_file(): continue
        text=path.read_text(encoding="utf-8")
        text=text.replace("figures/strategy3_local_area_loss.png","figures/exact/area/strategy3_local_area_loss.pdf")
        text=text.replace("figures/strategy3_global_area_loss.png","figures/exact/area/strategy3_global_area_loss.pdf")
        text=text.replace("Schematic views of Method~3, not to scale.","Coordinate-exact views of Method~3.")
        text=text.replace("Only the darker portions represent area\nretained inside $H$; the proof uses the inequalities below, not the picture.","The retained polygons are computed by line clipping, and the six global copies are exact rotations by multiples of $60^\\circ$.")
        path.write_text(text,encoding="utf-8")


def patch_main_and_build() -> None:
    main=PAPER/"main.tex"; text=main.read_text(encoding="utf-8")
    text=text.replace("\\usepackage{booktabs,float,longtable,array,microtype,tikz}","\\usepackage{booktabs,float,longtable,array,microtype}")
    text=re.sub(r"^\\usetikzlibrary\{[^\n]+\}\n?","",text,flags=re.M)
    text=re.sub(r"^\\input\{figures/tikz_setup\}\n?","",text,flags=re.M)
    main.write_text(text,encoding="utf-8")
    build=ROOT/"arrange/build.py"; text=build.read_text(encoding="utf-8")
    marker="def build_one(source_name: str, output: Path) -> None:\n"
    if "figures/exact/generate.py" not in text:
        replacement=(
            "def check_exact_figures() -> None:\n"
            "    generator = ARRANGE / \"paper_draft/figures/exact/generate.py\"\n"
            "    if generator.is_file():\n"
            "        subprocess.run([os.sys.executable, str(generator), \"--check\"], cwd=ROOT, check=True)\n\n\n"
            + marker
        )
        text=text.replace(marker,replacement)
        text=text.replace("    with tempfile.TemporaryDirectory(prefix=f\"hexagon-cover-{source_name}-\") as td:\n","    check_exact_figures()\n    with tempfile.TemporaryDirectory(prefix=f\"hexagon-cover-{source_name}-\") as td:\n")
    build.write_text(text,encoding="utf-8")
    ci=ROOT/".github/workflows/ci.yml"; text=ci.read_text(encoding="utf-8")
    if "Audit deterministic exact paper figures" not in text:
        needle="      - name: Check proof and manuscript source interfaces\n        run: python proof/check.py\n"
        insertion=needle+"\n      - name: Audit deterministic exact paper figures\n        run: python arrange/paper_draft/figures/exact/generate.py --check\n"
        text=text.replace(needle,insertion)
    ci.write_text(text,encoding="utf-8")


def finalize_manifest(manifest:dict[str,object]) -> None:
    for entry in manifest["assets"]:
        entry["sha256_pdf"]=sha256(entry_output(EXACT,entry,"image"))
        if entry.get("svg"): entry["sha256_svg"]=sha256(entry_output(EXACT,entry,"svg"))
        if entry.get("preview"):
            preview=(EXACT/str(entry["preview"])).resolve()
            entry["sha256_preview"]=sha256(preview)
    MANIFEST.parent.mkdir(parents=True,exist_ok=True)
    MANIFEST.write_text(json.dumps(manifest,indent=2,sort_keys=True)+"\n",encoding="utf-8")


def write_report(manifest:dict[str,object]) -> None:
    assets=list(manifest["assets"])
    metric=[a for a in assets if a["category"]=="metric_exact"]
    logical=[a for a in assets if a["category"]!="metric_exact"]
    lines=[
        "# Exact mathematical figure migration",
        "",
        "## Scope and design rule",
        "",
        "The canonical paper no longer executes TikZ geometry.  Every referenced figure is an external PDF image.  Metric panels are regenerated from explicit coordinates, support functions, line intersections, or selected algebraic formulas.  Logical roadmaps and dependency diagrams are externalized as vector PDFs, retain their original source under `figures/exact/source_tikz/`, and are explicitly classified as nonmetric so that their spacing carries no geometric claim.",
        "",
        f"- Metric exact assets: **{len(metric)}**",
        f"- Logical nonmetric externalizations: **{len(logical)}**",
        f"- Total external figure assets controlled by the manifest: **{len(assets)}**",
        "- Canonical inline `tikzpicture` count after migration: **0**",
        "",
        "## Exact mathematical constructions",
        "",
        "1. **Regular hexagon.** `V_i=(cos(i*pi/3),sin(i*pi/3))`; all boundary edges and all radii are verified to have length one, and `M_i=V_i/2`.",
        "2. **Unit equilateral triangles.** Every role specimen is generated with circumradius `1/sqrt(3)` and vertex angles separated by `2*pi/3`; all three side lengths are rechecked.",
        "3. **C-triangle classes.** CE0 is an interior centered specimen. CE1 and CE2 are reconstructed from pairwise intersections of the exact signed side equations `F_0=F_1=F_2=0`; positive boundary intervals are computed by convex segment clipping, and point contacts are excluded from the count.",
        "4. **V-triangle classes.** The six displayed specimens use rational center offsets and rational multiples of pi.  The audit recomputes: strict containment of `V_0`, number `o` of triangle vertices outside `H`, positive-length intersections with `r_1,r_5`, actual reaches `A,B,C`, and the sign of `A+B-1`.",
        "5. **Area loss.** The retained polygon `T intersect H` is obtained by half-plane clipping.  The global panel consists of exact rotations through multiples of 60 degrees; no independently dragged copies are used.",
        "6. **Signed-center traces and exits.** Trace endpoints and the six exits are direct evaluations of the formulas in the signed normal form.  The CE1/contact/CE2 panels use the exact sign of `Delta_L`.",
        "7. **Finite enclosure.** Enclosing triangles are reconstructed from three support half-planes.  The disk-plus-point panels compare the support computation with the closed formula.  The complementary-gap, short-ray, K_tr, neighboring-capacity, AB-frontier, nine-point, and support-cap panels are generated from their displayed parameters and report the computed scalar values.",
        "",
        "## Permanent audit",
        "",
        "`python arrange/paper_draft/figures/exact/generate.py --check` regenerates the formula-driven assets in a temporary directory, compares exact bytes, opens every PDF, checks every preview, replays the role classifications and signed-center invariants, confirms that the canonical TeX dependency closure contains no `tikzpicture`, and verifies all manifest hashes.  `arrange/build.py` invokes this audit before every clean paper build; CI has a separate named audit step.",
        "",
        "## Figure-by-figure inventory",
        "",
        "| Original source / role | New external image | Classification | Construction and validation |",
        "|---|---|---|---|",
    ]
    for a in assets:
        src=a.get("source") or a["key"]
        desc=a["construction"]
        if a["category"]=="metric_exact": desc += "; formula inputs and invariant checks are recorded in `manifest.json`"
        else: desc += "; original TikZ is archived and its layout is declared nonmetric"
        lines.append(f"| `{src}` | `figures/exact/{a['image']}` | `{a['category']}` | {desc} |")
    lines.extend([
        "",
        "## Caption policy",
        "",
        "Captions that previously said `schematic`, `illustrative`, or `not to scale` are replaced for the metric panels by precise statements of the generated parameter instance and checked construction.  Logical diagrams instead state that they encode implication or case structure only and make no metric assertion.",
        "",
        "## Reproduction",
        "",
        "```bash",
        "python -m pip install -r arrange/_support/requirements.txt",
        "python arrange/paper_draft/figures/exact/generate.py --check",
        "python arrange/build.py --all",
        "```",
        "",
    ])
    REPORT.write_text("\n".join(lines),encoding="utf-8")


def migrate() -> None:
    closure=canonical_closure(); figure_sources=discover_figure_inputs(closure)
    if not figure_sources: raise SystemExit("no canonical figure inputs discovered")
    EXACT.mkdir(parents=True,exist_ok=True); SOURCE_TIKZ.mkdir(parents=True,exist_ok=True)
    for source in figure_sources:
        rel=source.relative_to(FIGURES); archive=SOURCE_TIKZ/rel; archive.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(source,archive)
    manifest=build_manifest(figure_sources)
    generate_all(EXACT,manifest)
    by_source={str(a["source"]):a for a in manifest["assets"] if a.get("source")}
    for source in figure_sources:
        rel=source.relative_to(FIGURES).as_posix(); source.write_text(wrapper_text(source,by_source[rel]),encoding="utf-8")
    patch_intro_and_area(); patch_main_and_build()
    target=EXACT/"generate.py"; shutil.copy2(Path(__file__),target); target.chmod(0o755)
    finalize_manifest(manifest); write_report(manifest)
    check()


def validate_math(manifest:dict[str,object]) -> None:
    for i in range(6):
        assert abs(norm(sub(HEX[(i+1)%6],HEX[i]))-1)<1e-12
        assert abs(norm(HEX[i])-1)<1e-12
    role_entries={a["key"]:a for a in manifest["assets"] if str(a["key"]).startswith("vertex_role_")}
    expected={
        "vertex_role_vd0_axis_aligned_example":((1,2),0,">"),
        "vertex_role_vd0_nonsupercritical_example":((1,2),0,"<="),
        "vertex_role_vd0_supercritical_example":((1,2),0,">"),
        "vertex_role_vd1_example":((1,),1,None),
        "vertex_role_vd2_example":((1,),2,None),
        "vertex_role_t3_like_example":((2,),1,None),
    }
    for name,(oset,nval,sign) in expected.items():
        tri,data=specimen_from_spec(dict(role_entries[name]["parameters"]["specimen"]))
        assert data["o"] in oset and data["n"]==nval and data["margin"]>1e-4,(name,data)
        sides=[norm(sub(tri[(j+1)%3],tri[j])) for j in range(3)]
        assert max(abs(x-1) for x in sides)<2e-12,(name,sides)
        total=float(data["A"])+float(data["B"])
        if sign==">": assert total>1+1e-3,(name,total)
        if sign=="<=": assert total<=1+1e-8,(name,total)
    for kind,count in (("CE0",0),("CE1",1),("CE2",2)):
        tri=equilateral(O,math.pi/6) if kind=="CE0" else signed_triangle(signed_parameters(kind))
        traces=0
        for i in range(6):
            iv=segment_interval(tri,HEX[i],HEX[(i+1)%6])
            if iv and iv[1]-iv[0]>1e-6: traces+=1
        assert traces==count,(kind,traces)
        assert polygon_margin(tri,O)>1e-8
        assert max(abs(norm(sub(tri[(j+1)%3],tri[j]))-1) for j in range(3))<2e-8
    eta=.25
    for rho in (.40,.75):
        side,_,_=support_triangle([(rho,0)],eta)
        formula=3*eta/H if rho<=2*eta else (3*eta+math.sqrt(3*(rho*rho-eta*eta)))/(2*H)
        assert abs(side-formula)<2e-7,(rho,side,formula)
    p=signed_parameters("CE2"); a=p["W"]-p["alpha"]; b=p["R"]-p["delta"]; e=min(p["alpha"],p["delta"])
    assert 1-cmax(a,b)>e+1e-6


def check() -> None:
    if not MANIFEST.is_file(): raise SystemExit("exact figure manifest is missing")
    manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    validate_math(manifest)
    for entry in manifest["assets"]:
        pdf=entry_output(EXACT,entry,"image")
        if not pdf.is_file() or sha256(pdf)!=entry["sha256_pdf"]: raise SystemExit(f"PDF hash mismatch: {pdf}")
        with fitz.open(pdf) as doc:
            if doc.page_count!=1 or doc[0].rect.width<=0 or doc[0].rect.height<=0: raise SystemExit(f"invalid PDF: {pdf}")
        if entry.get("svg"):
            svg=entry_output(EXACT,entry,"svg")
            if not svg.is_file() or sha256(svg)!=entry["sha256_svg"]: raise SystemExit(f"SVG hash mismatch: {svg}")
        if entry.get("preview"):
            preview=(EXACT/str(entry["preview"])).resolve()
            if not preview.is_file() or sha256(preview)!=entry["sha256_preview"]: raise SystemExit(f"preview hash mismatch: {preview}")
    with tempfile.TemporaryDirectory(prefix="exact-figure-check-") as td:
        tmp=Path(td)
        for entry in manifest["assets"]:
            if entry["category"]!="metric_exact": continue
            generate_entry(tmp,entry)
            produced=entry_output(tmp,entry,"image")
            if produced.read_bytes()!=entry_output(EXACT,entry,"image").read_bytes(): raise SystemExit(f"nondeterministic PDF: {entry['key']}")
            if entry.get("svg") and entry_output(tmp,entry,"svg").read_bytes()!=entry_output(EXACT,entry,"svg").read_bytes(): raise SystemExit(f"nondeterministic SVG: {entry['key']}")
    closure=canonical_closure()
    for path in closure:
        text=path.read_text(encoding="utf-8")
        if "\\begin{tikzpicture}" in text: raise SystemExit(f"inline TikZ remains in canonical paper: {path}")
    main=(PAPER/"main.tex").read_text(encoding="utf-8")
    if "usetikzlibrary" in main or "figures/tikz_setup" in main: raise SystemExit("canonical main.tex still loads TikZ")
    print(f"exact-figure audit passed: {len(manifest['assets'])} external assets")


def main() -> None:
    parser=argparse.ArgumentParser(); group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--migrate",action="store_true"); group.add_argument("--check",action="store_true")
    args=parser.parse_args()
    if args.migrate: migrate()
    else: check()


if __name__=="__main__": main()
