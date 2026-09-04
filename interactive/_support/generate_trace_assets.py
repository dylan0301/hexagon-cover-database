#!/usr/bin/env python3
"""Generate the standalone trace-exact AB-envelope explorer.

The browser samples unions of valid source triangles satisfying the prescribed
exact boundary reach.  Those samples visualize subsets of the exact
source-conditioned envelopes; they are not proof certificates.  This generator
writes only the self-contained explorer and its deterministic preset data.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Callable, Literal
import json
import math

ROOT = Path(__file__).resolve().parents[2]
INTERACTIVE_DIR = ROOT / "interactive"
INTERACTIVE_DIR.mkdir(parents=True, exist_ok=True)

SQ3 = math.sqrt(3.0)
H = SQ3 / 2.0
Point = tuple[float, float]
V: list[Point] = [
    (math.cos(i * math.pi / 3), math.sin(i * math.pi / 3)) for i in range(6)
]


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1])


def subtract(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1])


def scale(s: float, a: Point) -> Point:
    return (s * a[0], s * a[1])


def dot(a: Point, b: Point) -> float:
    return a[0] * b[0] + a[1] * b[1]


def edge_point(i: int, t: float) -> Point:
    return add(V[i], scale(t, subtract(V[(i + 1) % 6], V[i])))


def rotate(x: Point, theta: float) -> Point:
    c, s = math.cos(theta), math.sin(theta)
    return (c * x[0] - s * x[1], s * x[0] + c * x[1])


def line_intersection(n1: Point, c1: float, n2: Point, c2: float) -> Point:
    determinant = n1[0] * n2[1] - n1[1] * n2[0]
    if abs(determinant) <= 1e-15:
        raise ValueError("parallel support lines")
    return (
        (c1 * n2[1] - n1[1] * c2) / determinant,
        (n1[0] * c2 - c1 * n2[0]) / determinant,
    )


def bisect_root(function: Callable[[float], float], lower: float, upper: float) -> float:
    """Return the bracketed root using deterministic binary subdivision."""

    lower_value = function(lower)
    upper_value = function(upper)
    if abs(lower_value) <= 1e-15:
        return lower
    if abs(upper_value) <= 1e-15:
        return upper
    if lower_value * upper_value > 0:
        raise ValueError("root is not bracketed")
    for _ in range(100):
        middle = (lower + upper) / 2.0
        middle_value = function(middle)
        if lower_value * middle_value <= 0:
            upper = middle
        else:
            lower = middle
            lower_value = middle_value
    return (lower + upper) / 2.0


def c_l_root(m: float) -> float:
    if m <= 1e-13:
        return 1.0
    return bisect_root(lambda c: c**4 - c*c + m*c - m*m, H, 1.0)


def c_max(a: float, b: float) -> float:
    d2 = a*a + a*b + b*b
    if d2 > 1.0 + 1e-9:
        return 1.0
    s = a + b
    if s <= 1e-13:
        return 1.0
    m, M = min(a, b), max(a, b)
    q = s**4 - s*s + a*b
    if s <= 1.0 + 1e-10:
        if q <= 1e-10:
            return c_l_root(m)
        return 2.0*M/(1.0 + math.sqrt(max(0.0, 4.0*s*s - 3.0)))
    return (M*(2.0*m*M+1.0)-M*math.sqrt(max(0.0,4.0*d2-3.0)))/(2.0*(1.0-m*m))


def p_root(a: float) -> float:
    return bisect_root(lambda p: p**3-(a+2)*p*p+2*(a+1)*p-1, a, 1.0)


def c_plus(a: float, b: float) -> float | None:
    if a + b > 1.0 + 1e-9:
        return None
    if a > 0.5 + 1e-10:
        return 1.0-b
    p = p_root(max(0.0,min(0.5,a)))
    sigma = 1.0-p
    tau = 1.0-a-(p-a)*(1.0-p)
    if b <= sigma + 1e-10:
        return 1.0-b
    if b <= tau + 1e-10:
        return p
    return a+0.5-math.sqrt(max(0.0,(a+b)**2-0.75))


def role_mask(code: str) -> tuple[bool,bool]:
    if code == "Vd2": return True, True
    if code in {"T3L","Vd1L"}: return True, False
    if code in {"T3R","Vd1R"}: return False, True
    return False, False


def radial_witnesses(pairs: list[tuple[float,float]], roles: list[str]) -> list[float]:
    radii=[]
    masks=[role_mask(x) for x in roles]
    for i,(a,b) in enumerate(pairs):
        candidates=[c_max(a,b)]
        left=(i-1)%6
        if masks[left][1]:
            val=c_plus(*pairs[left])
            if val is not None: candidates.append(val)
        right=(i+1)%6
        if masks[right][0]:
            ar,br=pairs[right]
            val=c_plus(br,ar)
            if val is not None: candidates.append(val)
        radii.append(max(0.0,1.0-max(candidates)))
    return radii


def cross(origin: Point, a: Point, b: Point) -> float:
    return (a[0] - origin[0]) * (b[1] - origin[1]) - (
        a[1] - origin[1]
    ) * (b[0] - origin[0])


def convex_hull(points: list[Point]) -> list[Point]:
    unique: list[Point] = []
    for point in sorted(points):
        if not any(math.dist(point, other) < 1e-10 for other in unique):
            unique.append(point)
    if len(unique) <= 1:
        return unique

    lower: list[Point] = []
    for point in unique:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper: list[Point] = []
    for point in reversed(unique):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)
    return lower[:-1] + upper[:-1]


def min_enclosing_equilateral(points: list[Point]) -> tuple[float, list[Point]]:
    hull = convex_hull(points)
    if len(hull) < 2:
        raise ValueError("at least two distinct witness points are required")

    best_side = float("inf")
    best_triangle: list[Point] = []
    for index, point in enumerate(hull):
        edge = subtract(hull[(index + 1) % len(hull)], point)
        length = math.hypot(*edge)
        normal = (edge[1] / length, -edge[0] / length)
        normals = [
            normal,
            rotate(normal, 2.0 * math.pi / 3.0),
            rotate(normal, 4.0 * math.pi / 3.0),
        ]
        supports = [max(dot(candidate, normal) for candidate in points) for normal in normals]
        side = 2.0 / SQ3 * sum(supports)
        triangle = [
            line_intersection(normals[0], supports[0], normals[1], supports[1]),
            line_intersection(normals[1], supports[1], normals[2], supports[2]),
            line_intersection(normals[2], supports[2], normals[0], supports[0]),
        ]
        if side < best_side:
            best_side = side
            best_triangle = triangle
    return best_side, best_triangle


@dataclass
class Gap:
    edge: int
    left: float
    right: float

@dataclass
class Envelope:
    role: int
    a: float
    b: float
    mode: Literal["ordinary","out","in","both"]
    label: str

@dataclass
class Preset:
    key: str
    title: str
    case_id: str
    case: str
    roles: list[str]
    actual_reaches: list[tuple[float,float]]
    predicate: dict[str, object]
    envelopes: list[Envelope] = field(default_factory=list)
    extras: list[tuple[str,float,float]] = field(default_factory=list)
    note: str = ""


OVERLAP = 0.01


def one_gap(
    key: str,
    title: str,
    case_id: str,
    case: str,
    ell: float,
    r: float,
    x: list[float],
    roles: list[str],
    predicate: dict[str, object],
    note: str = "",
) -> Preset:
    x1,x2,x3,x4,x5=x
    # The extra OVERLAP is essential: equality would leave a singleton gap
    # because the original V triangles are open.
    pairs=[
        (1-x5,ell),
        (1-r,x1+OVERLAP),
        (1-x1,x2+OVERLAP),
        (1-x2,x3+OVERLAP),
        (1-x3,x4+OVERLAP),
        (1-x4,x5+OVERLAP),
    ]
    env=[Envelope(0,1-x5,ell,"out","left exact trace"),
         Envelope(1,1-r,x1+OVERLAP,"in","right exact trace")]
    return Preset(
        key, title, case_id, case, roles, pairs, predicate, env, note=note
    )


def two_gap(
    key: str,
    title: str,
    case_id: str,
    case: str,
    ellR: float,
    rR: float,
    ellL: float,
    rL: float,
    x: list[float],
    roles: list[str],
    predicate: dict[str, object],
    note: str = "",
) -> Preset:
    x1,x2,x3,x4=x
    pairs=[
        (1-rL,ellR),
        (1-rR,x1+OVERLAP),
        (1-x1,x2+OVERLAP),
        (1-x2,x3+OVERLAP),
        (1-x3,x4+OVERLAP),
        (1-x4,ellL),
    ]
    env=[Envelope(0,1-rL,ellR,"both","two-sided exact trace"),
         Envelope(1,1-rR,x1+OVERLAP,"in","right exact trace"),
         Envelope(5,1-x4,ellL,"out","left exact trace")]
    return Preset(
        key, title, case_id, case, roles, pairs, predicate, env, note=note
    )


PRESETS: list[Preset]=[
    Preset("zero_gap_n1_vd0","Zero-gap nine-point data", "F",
           r"$N_{\rm gap}=0,\ N_+=1,\ \sigma=4,\ (d,t)=(0,0)$",
           ["Vd0"]*6,
           [(0.54,0.445),(0.57,0.415),(0.60,0.385),(0.63,0.365),(0.64,0.50),(0.51,0.475)],
           {"N_gap":0,"gap_edges":[],"N_plus":1,
            "supercritical_indices":[4],"d":0,"t":0},
           envelopes=[Envelope(4,0.64,0.50,"ordinary","strict-supercritical AB union")],
           extras=[("Q_-",-0.10,0.11),("Q_0",0.0,0.16),("Q_+",0.10,0.11)],
           note="Ordinary strict-supercritical AB union; no boundary gap is present."),
    one_gap("one_gap_n0_vd0","Row A: all Vd0", "A",
            r"$N_{\rm gap}=1,\ N_+=0,\ (d,t)=(0,0)$",
            .35,.65,[.60,.55,.50,.45,.40],["Vd0"]*6,
            {"N_gap":1,"gap_edges":[0],"N_plus":0,"d":0,"t":0}),
    two_gap("two_gap_vd0","Row B: all Vd0", "B",
            r"$N_{\rm gap}=2,\ N_+=0,\ (d,t)=(0,0)$",
            .42,.58,.30,.50,[.55,.50,.45,.40],["Vd0"]*6,
            {"N_gap":2,"gap_edges":[0,5],"N_plus":0,"d":0,"t":0}),
    one_gap("one_t3_n0","Row A: one T3-like role", "A",
            r"$N_{\rm gap}=1,\ N_+=0,\ (d,t)=(0,1)$",
            .35,.65,[.60,.55,.50,.45,.40],["T3R","Vd0","Vd0","Vd0","Vd0","Vd0"],
            {"N_gap":1,"gap_edges":[0],"N_plus":0,"d":0,"t":1,
             "t3_indices":[0]},
            "The dashed arm marks the permitted T3-like adjacent support."),
    one_gap("two_t3_n0","Row A: two T3-like roles", "A",
            r"$N_{\rm gap}=1,\ N_+=0,\ (d,t)=(0,2)$",
            .34,.66,[.61,.56,.50,.44,.39],["T3R","Vd0","Vd0","T3L","Vd0","Vd0"],
            {"N_gap":1,"gap_edges":[0],"N_plus":0,"d":0,"t":2,
             "t3_indices":[0,3]}),
    two_gap("two_gap_t3_n0","Row B: two T3-like roles", "B",
            r"$N_{\rm gap}=2,\ N_+=0,\ (d,t)=(0,2)$",
            .42,.58,.30,.50,[.55,.50,.45,.40],["T3R","Vd0","Vd0","T3L","Vd0","Vd0"],
            {"N_gap":2,"gap_edges":[0,5],"N_plus":0,"d":0,"t":2,
             "t3_indices":[0,3]}),
    one_gap("one_gap_n1_vd0_ce1","Row C data for the CE1 terminal", "C",
            r"$N_{\rm gap}=1,\ N_+=1,\ \sigma=0,\ (d,t)=(0,0)$",
            .50,.75,[.70,.62,.55,.48,.40],["Vd0"]*6,
            {"N_gap":1,"gap_edges":[0],"N_plus":1,
             "supercritical_indices":[0],"d":0,"t":0},
            "The left incident role is the unique supercritical role."),
    one_gap("one_gap_n1_vd0_ce2","Row C data for the CE2 terminal", "C",
            r"$N_{\rm gap}=1,\ N_+=1,\ \sigma=0,\ (d,t)=(0,0)$",
            .45,.70,[.65,.58,.52,.46,.38],["Vd0"]*6,
            {"N_gap":1,"gap_edges":[0],"N_plus":1,
             "supercritical_indices":[0],"d":0,"t":0}),
    two_gap("two_gap_n1_vd0","Row B: one supercritical Vd0 role", "B",
            r"$N_{\rm gap}=2,\ N_+=1,\ \sigma=0,\ (d,t)=(0,0)$",
            .45,.60,.25,.40,[.55,.50,.45,.35],["Vd0"]*6,
            {"N_gap":2,"gap_edges":[0,5],"N_plus":1,
             "supercritical_indices":[0],"d":0,"t":0}),
    one_gap("one_gap_n1_t3","Row D_T: one-gap data", "D_T",
            r"$N_{\rm gap}=1,\ N_+=1,\ \sigma=1,\ (d,t)=(0,1)$",
            .35,.75,[.80,.65,.55,.45,.35],["T3R","Vd0","Vd0","Vd0","Vd0","Vd0"],
            {"N_gap":1,"gap_edges":[0],"N_plus":1,
             "supercritical_indices":[1],"d":0,"t":1,"t3_indices":[0]},
            "T1 is supercritical; T0 supplies the supported-trace witness."),
    two_gap("two_gap_n1_t3","Row D_T: two-gap data", "D_T",
            r"$N_{\rm gap}=2,\ N_+=1,\ \sigma=1,\ (d,t)=(0,1)$",
            .40,.75,.30,.55,[.80,.65,.55,.45],["T3R","Vd0","Vd0","Vd0","Vd0","Vd0"],
            {"N_gap":2,"gap_edges":[0,5],"N_plus":1,
             "supercritical_indices":[1],"d":0,"t":1,"t3_indices":[0]}),
    two_gap("adjacent_vd","Row E_a: adjacent Vd1 placement", "E_a",
            r"$N_{\rm gap}=2,\ N_+=1,\ \sigma=0,\ \tau=1,\ (d,t)=(1,0)$",
            .45,.60,.25,.40,[.55,.50,.45,.35],["Vd0","Vd1R","Vd0","Vd0","Vd0","Vd0"],
            {"N_gap":2,"gap_edges":[0,5],"N_plus":1,
             "supercritical_indices":[0],"d":1,"t":0,"vd_indices":[1]}),
    two_gap("nonadjacent_vd","Row E_n: nonadjacent Vd2 placement", "E_n",
            r"$N_{\rm gap}=2,\ N_+=1,\ \sigma=0,\ \tau=3,\ (d,t)=(1,0)$",
            .45,.60,.25,.40,[.55,.50,.45,.35],["Vd0","Vd0","Vd0","Vd2","Vd0","Vd0"],
            {"N_gap":2,"gap_edges":[0,5],"N_plus":1,
             "supercritical_indices":[0],"d":1,"t":0,"vd_indices":[3]}),
    Preset("vd1_rescuer","Row D_V: Vd1 supported-tail data", "D_V",
           r"$N_{\rm gap}=2,\ N_+=1,\ \sigma=1,\ \tau=0,\ (d,t)=(1,0),\ A_0+B_0<1/2$",
           ["Vd1R","Vd0","Vd0","Vd0","Vd0","Vd0"],
           [(0.20,0.20),(0.60,0.51),(0.50,0.46),(0.55,0.41),(0.60,0.36),(0.65,0.20)],
           {"N_gap":2,"gap_edges":[0,5],"N_plus":1,
            "supercritical_indices":[1],"d":1,"t":0,"vd_indices":[0],
            "A0_plus_B0_lt_half":True},
           envelopes=[Envelope(0,0.20,0.20,"both","two-sided exact trace"),
                      Envelope(1,0.60,0.51,"in","right exact trace"),
                      Envelope(5,0.65,0.20,"out","left exact trace")]),
    one_gap("replacement_output","One-gap all-Vd0 replacement output (R to A)", "R_to_A",
            r"$N'_{\rm gap}=1,\ \left|\{i\in\mathbb Z/6\mathbb Z:A(T'_i)+B(T'_i)>1\}\right|=0$",
            .33,.67,[.61,.55,.49,.43,.37],["Vd0"]*6,
            {"N_gap":1,"gap_edges":[0],"N_plus":0,"d":0,"t":0},
            "This is a primed one-gap output of row R, routed to row A; it is not the row-R input."),
]


def actual_gaps(preset: Preset) -> list[Gap]:
    """Return all gaps of the original open V triangles, including singletons."""

    gaps: list[Gap] = []
    for edge, (_, B_i) in enumerate(preset.actual_reaches):
        A_next = preset.actual_reaches[(edge + 1) % 6][0]
        right = 1.0 - A_next
        if B_i <= right:
            gaps.append(Gap(edge, B_i, right))
    return gaps


def derived_predicate(preset: Preset) -> dict[str, object]:
    supercritical = [
        index
        for index, (A_i, B_i) in enumerate(preset.actual_reaches)
        if A_i + B_i > 1.0
    ]
    vd_indices = [
        index
        for index, role in enumerate(preset.roles)
        if role.startswith("Vd1") or role == "Vd2"
    ]
    t3_indices = [
        index for index, role in enumerate(preset.roles) if role.startswith("T3")
    ]
    gaps = actual_gaps(preset)
    return {
        "N_gap": len(gaps),
        "gap_edges": [gap.edge for gap in gaps],
        "singleton_gap_edges": [
            gap.edge for gap in gaps if gap.left == gap.right
        ],
        "N_plus": len(supercritical),
        "supercritical_indices": supercritical,
        "d": len(vd_indices),
        "t": len(t3_indices),
        "vd_indices": vd_indices,
        "t3_indices": t3_indices,
        "A0_plus_B0_lt_half": sum(preset.actual_reaches[0]) < 0.5,
    }


def validate_presets() -> None:
    keys: set[str] = set()
    for preset in PRESETS:
        if preset.key in keys:
            raise ValueError(f"duplicate preset key: {preset.key}")
        keys.add(preset.key)
        if len(preset.roles) != 6 or len(preset.actual_reaches) != 6:
            raise ValueError(f"{preset.key}: expected six roles and reach pairs")
        for index, (A_i, B_i) in enumerate(preset.actual_reaches):
            if not (0.0 <= A_i <= 1.0 and 0.0 <= B_i <= 1.0):
                raise ValueError(f"{preset.key}: reach {index} is outside [0,1]")
            if A_i*A_i + A_i*B_i + B_i*B_i > 1.0 + 1e-12:
                raise ValueError(f"{preset.key}: anchors for role {index} exceed diameter one")
            if preset.roles[index].startswith("T3") and A_i + B_i > 1.0:
                raise ValueError(f"{preset.key}: T3-like role {index} is supercritical")
        derived = derived_predicate(preset)
        for name, expected in preset.predicate.items():
            if derived.get(name) != expected:
                raise ValueError(
                    f"{preset.key}: predicate {name}={expected!r}, "
                    f"derived {derived.get(name)!r}"
                )


def evaluate_preset(preset: Preset) -> dict[str, object]:
    gaps = actual_gaps(preset)
    radii = radial_witnesses(preset.actual_reaches, preset.roles)
    witnesses: list[Point] = [(0.0, 0.0), scale(0.5, V[0])]
    witnesses.extend(
        edge_point(gap.edge, parameter)
        for gap in gaps
        for parameter in (gap.left, gap.right)
    )
    witnesses.extend(scale(radius, V[index]) for index, radius in enumerate(radii))
    witnesses.extend((x, y) for _, x, y in preset.extras)
    side, triangle = min_enclosing_equilateral(witnesses)
    return {
        "side": side,
        "radii": radii,
        "triangle": [list(point) for point in triangle],
    }


def make_html(results: dict[str,dict]):
    data=[]
    for p in PRESETS:
        d=asdict(p)
        d["gaps"]=[asdict(gap) for gap in actual_gaps(p)]
        d["derived"]=derived_predicate(p)
        d["result"]=results[p.key]
        data.append(d)
    jsdata=json.dumps(data,separators=(",",":"))
    html_template=r'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Trace-exact AB-envelope explorer</title>
<style>
body{margin:0;background:#f4f6f5;color:#172127;font-family:Inter,Segoe UI,system-ui,sans-serif}
header{max-width:1450px;margin:auto;padding:20px 22px 10px} h1{margin:0;font-size:clamp(25px,4vw,42px)}
header p{max-width:1050px;color:#66727b} main{max-width:1450px;margin:auto;padding:0 16px 30px;display:grid;grid-template-columns:minmax(640px,1fr) 390px;gap:14px}
.card{background:#fff;border:1px solid #ccd5d2;border-radius:12px;box-shadow:0 8px 24px rgba(20,35,40,.07)}
.visual{padding:10px;position:sticky;top:6px} canvas{width:100%;height:auto;display:block;background:#fbfcfb;border-radius:8px}
.side{display:grid;gap:12px} section{padding:13px} h2{font-size:17px;margin:0 0 8px} select,button,input{font:inherit}
select{width:100%;padding:7px;border:1px solid #ccd5d2;border-radius:7px} .tog{display:flex;gap:8px;margin:7px 0;font-size:12px;color:#5f6d75}
.note{border-left:4px solid #28717b;background:#eaf0ee;padding:9px;font-size:12px;color:#5f6d75}
table{width:100%;border-collapse:collapse;font-size:11px} td,th{border-bottom:1px solid #d7dfdc;padding:5px;text-align:left}
.legend{display:flex;flex-wrap:wrap;gap:9px;font-size:11px;color:#65717a;margin-top:7px} .sw{display:inline-block;width:13px;height:4px;margin-right:4px}
@media(max-width:1050px){main{grid-template-columns:1fr}.visual{position:static}}
</style></head><body>
<header><h1>Trace-exact AB-envelope explorer</h1>
<p>The colored regions are sampled unions of unit source triangles whose actual maximal boundary trace has the prescribed endpoint.  They are subsets of the pale ordinary AB-unions.  The orange intervals are genuine V-gaps: on each displayed edge, the incident exact traces stop at the two gap endpoints.  The mathematical proof uses the exact source-conditioned union, not a planar clipping and not the raster sample.</p></header>
<main><div class="card visual"><canvas id="cv" width="980" height="820"></canvas>
<div class="legend"><span><i class="sw" style="background:#cbd3d0"></i>ordinary AB-union sample</span><span><i class="sw" style="background:#8bb9c0"></i>trace-exact AB envelope</span><span><i class="sw" style="background:#b2701d"></i>actual V-gap</span><span><i class="sw" style="background:#7254a0"></i>forced finite witnesses</span><span><i class="sw" style="background:#a23f35"></i>minimum enclosing triangle</span></div></div>
<div class="side"><section class="card"><h2>Normalized subcase</h2><select id="preset"></select><p id="case"></p></section>
<section class="card"><h2>Layers</h2><label class="tog"><input id="ordinary" type="checkbox" checked>show ordinary AB-union samples</label><label class="tog"><input id="exact" type="checkbox" checked>show trace-exact envelopes</label><label class="tog"><input id="witness" type="checkbox" checked>show finite witnesses and minimum triangle</label><div class="note">The endpoint condition is imposed on the source triangles: B(S)=ell on the left and A(S)=1-r on the right.  A half-plane clipping of the ordinary union would not be proof-safe.</div></section>
<section class="card"><h2>Preset data</h2><table id="tbl"></table></section>
<section class="card"><h2>Interpretation</h2><p id="note"></p><p>This standalone explorer renders each preset directly from the embedded registry.  Its sampled regions explain the geometry but are not proof objects.</p></section></div></main>
<script>
const PRESETS=__PRESETS__;
const cv=document.getElementById('cv'),ctx=cv.getContext('2d'); const W=cv.width,Hc=cv.height,S=330,ox=490,oy=405;
const rt3=Math.sqrt(3), hh=rt3/2; const V=Array.from({length:6},(_,i)=>[Math.cos(i*Math.PI/3),Math.sin(i*Math.PI/3)]);
function P(x){return[ox+S*x[0],oy-S*x[1]]} function add(a,b){return[a[0]+b[0],a[1]+b[1]]} function sub(a,b){return[a[0]-b[0],a[1]-b[1]]} function mul(s,a){return[s*a[0],s*a[1]]} function dot(a,b){return a[0]*b[0]+a[1]*b[1]}
function edge(i,t){return add(V[i],mul(t,sub(V[(i+1)%6],V[i])))} function line(a,b){let A=P(a),B=P(b);ctx.beginPath();ctx.moveTo(...A);ctx.lineTo(...B);ctx.stroke()}
function inter(n1,c1,n2,c2){let d=n1[0]*n2[1]-n1[1]*n2[0];return[(c1*n2[1]-n1[1]*c2)/d,(n1[0]*c2-c1*n2[0])/d]}
function triVerts(ns,cs){let q=[inter(ns[0],cs[0],ns[1],cs[1]),inter(ns[1],cs[1],ns[2],cs[2]),inter(ns[2],cs[2],ns[0],cs[0])];let c=q.reduce((z,p)=>add(z,p),[0,0]).map(x=>x/3);q.sort((a,b)=>Math.atan2(a[1]-c[1],a[0]-c[0])-Math.atan2(b[1]-c[1],b[0]-c[0]));return q}
function reach(ns,cs,O,d){let z=[];for(let j=0;j<3;j++){let den=dot(ns[j],d);if(den>1e-9)z.push((cs[j]-dot(ns[j],O))/den)}return Math.min(...z)}
function drawFamily(e,mode,alpha){let O=V[e.role],ein=sub(V[(e.role+5)%6],O),eout=sub(V[(e.role+1)%6],O),A=add(O,mul(e.a,ein)),B=add(O,mul(e.b,eout));let N=150,steps=5;
ctx.save();ctx.beginPath();V.forEach((v,i)=>{let q=P(v);if(i==0)ctx.moveTo(...q);else ctx.lineTo(...q)});ctx.closePath();ctx.clip();ctx.globalAlpha=alpha;
for(let z=0;z<N;z++){let th=(2*Math.PI/3)*z/N,ns=[0,1,2].map(j=>[Math.cos(th+2*Math.PI*j/3),Math.sin(th+2*Math.PI*j/3)]),pts=[O,A,B],q=ns.map(n=>Math.max(...pts.map(p=>dot(p,n)))),sl=hh-q.reduce((a,b)=>a+b,0);if(sl<-1e-8)continue;sl=Math.max(0,sl);let ain=[],aout=[];for(let j=0;j<3;j++){if(dot(ns[j],ein)>1e-8&&Math.abs(q[j]-dot(A,ns[j]))<5e-7)ain.push(j);if(dot(ns[j],eout)>1e-8&&Math.abs(q[j]-dot(B,ns[j]))<5e-7)aout.push(j)}let offs=[];
if(mode==='ordinary'){for(let i=0;i<=steps;i++)for(let j=0;j<=steps-i;j++){let w=steps-i-j,den=steps+1.05,ex=[(i+.35)*sl/den,(j+.35)*sl/den,(w+.35)*sl/den];offs.push(q.map((x,k)=>x+ex[k]))}}
else if(mode==='out'||mode==='in'){let aa=mode==='out'?aout:ain;for(const j of aa){let o=[0,1,2].filter(k=>k!==j);for(let k=1;k<steps;k++){let ex=[0,0,0];ex[o[0]]=sl*k/steps;ex[o[1]]=sl*(steps-k)/steps;offs.push(q.map((x,m)=>x+ex[m]))}}}
else{for(const j of ain)for(const k of aout){let free=[0,1,2].filter(m=>m!==j&&m!==k);if(free.length===1){let ex=[0,0,0];ex[free[0]]=sl;offs.push(q.map((x,m)=>x+ex[m]))}}}
for(const cs of offs){if(Math.min(...cs.map((c,j)=>c-dot(ns[j],O)))<2e-6)continue;let ri=reach(ns,cs,O,ein),ro=reach(ns,cs,O,eout);if((mode==='in'||mode==='both')&&Math.abs(ri-e.a)>3e-4)continue;if((mode==='out'||mode==='both')&&Math.abs(ro-e.b)>3e-4)continue;let tv=triVerts(ns,cs);ctx.beginPath();tv.forEach((v,i)=>{let q=P(v);if(i===0)ctx.moveTo(...q);else ctx.lineTo(...q)});ctx.closePath();ctx.fill()}}
ctx.restore()}
function draw(){let p=PRESETS[+document.getElementById('preset').value];ctx.clearRect(0,0,W,Hc);ctx.fillStyle='#fbfcfb';ctx.fillRect(0,0,W,Hc);ctx.lineWidth=2;ctx.strokeStyle='#263238';let q=V.map(P);ctx.beginPath();q.forEach((z,i)=>i?ctx.lineTo(...z):ctx.moveTo(...z));ctx.closePath();ctx.stroke();ctx.lineWidth=.7;ctx.globalAlpha=.35;for(const v of V)line([0,0],v);ctx.globalAlpha=1;
if(document.getElementById('ordinary').checked){ctx.fillStyle='#bfc8c5';p.envelopes.forEach(e=>drawFamily(e,'ordinary',.08))}if(document.getElementById('exact').checked){ctx.fillStyle='#5b98a2';p.envelopes.filter(e=>e.mode!=='ordinary').forEach(e=>drawFamily(e,e.mode,.20))}
ctx.strokeStyle='#263238';ctx.lineWidth=4;ctx.globalAlpha=.55;for(const g of p.gaps){line(V[g.edge],edge(g.edge,g.left));line(edge(g.edge,g.right),V[(g.edge+1)%6])}ctx.globalAlpha=1;ctx.strokeStyle='#b2701d';ctx.lineWidth=7;for(const g of p.gaps)line(edge(g.edge,g.left),edge(g.edge,g.right));
for(let i=0;i<6;i++){let m=p.roles[i],L=m==='Vd2'||m.endsWith('L'),R=m==='Vd2'||m.endsWith('R');ctx.strokeStyle='#2d737a';ctx.setLineDash([7,5]);ctx.lineWidth=1.7;if(L)line(V[i],mul(.52,V[(i+5)%6]));if(R)line(V[i],mul(.52,V[(i+1)%6]));ctx.setLineDash([])}
if(document.getElementById('witness').checked){let pts=[[0,0],[.5,0]];for(const g of p.gaps)pts.push(edge(g.edge,g.left),edge(g.edge,g.right));p.result.radii.forEach((d,i)=>pts.push(mul(d,V[i])));p.extras.forEach(x=>pts.push([x[1],x[2]]));ctx.fillStyle='#7254a0';p.result.radii.forEach((d,i)=>{let z=P(mul(d,V[i]));ctx.beginPath();ctx.arc(...z,5,0,2*Math.PI);ctx.fill();ctx.fillText('D'+i,z[0]+6,z[1]-5)});let t=p.result.triangle;ctx.strokeStyle='#a23f35';ctx.lineWidth=2.2;ctx.setLineDash([9,6]);ctx.beginPath();t.forEach((v,i)=>{let z=P(v);if(i)ctx.lineTo(...z);else ctx.moveTo(...z)});ctx.closePath();ctx.stroke();ctx.setLineDash([])}ctx.fillStyle='#172127';ctx.font='12px system-ui';V.forEach((v,i)=>{let z=P(v);ctx.fillText('V'+i,z[0]+5,z[1]-5)})}
const sel=document.getElementById('preset');PRESETS.forEach((p,i)=>{let o=document.createElement('option');o.value=i;o.textContent=(i+1)+'. '+p.title;sel.appendChild(o)});function update(){let p=PRESETS[+sel.value];document.getElementById('case').innerHTML=p.case;document.getElementById('note').textContent=p.note||'The source envelopes enforce the actual gap endpoints; ordinary capacities remain safe upper bounds.';let rows='<tr><th>role</th><th>type</th><th>(A_i,B_i)</th></tr>';p.actual_reaches.forEach((x,i)=>rows+=`<tr><td>T${i}</td><td>${p.roles[i]}</td><td>(${x[0].toFixed(3)}, ${x[1].toFixed(3)})</td></tr>`);rows+=`<tr><td colspan="2">case id</td><td>${p.case_id}</td></tr><tr><td colspan="2">displayed min. side</td><td>${p.result.side.toFixed(6)}</td></tr>`;document.getElementById('tbl').innerHTML=rows;draw()}sel.onchange=update;['ordinary','exact','witness'].forEach(x=>document.getElementById(x).onchange=draw);update();
</script></body></html>'''
    html=html_template.replace('__PRESETS__',jsdata)
    (INTERACTIVE_DIR/'trace_exact_ab_envelope_explorer.html').write_text(html,encoding='utf-8')
    (INTERACTIVE_DIR/'trace_exact_ab_presets.json').write_text(json.dumps(data,indent=2),encoding='utf-8')


def main():
    validate_presets()
    results={}
    for idx,p in enumerate(PRESETS,1):
        result=evaluate_preset(p)
        results[p.key]=result
        print(f'{idx:02d} {p.key}: side={result["side"]:.6f}')
    make_html(results)

if __name__=='__main__':
    main()
