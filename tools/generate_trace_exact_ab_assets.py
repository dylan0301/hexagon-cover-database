#!/usr/bin/env python3
"""Generate proof-explanatory trace-exact AB-envelope assets.

The sampled polygons are unions of valid source triangles satisfying the
prescribed exact boundary reach.  They are visual subsets of the exact
source-conditioned envelopes, not proof certificates.  The numbered proof
sources use the exact set-theoretic definition and the ordinary AB capacity
bounds.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Iterable, Literal
import json
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
from scipy.optimize import brentq
from scipy.spatial import ConvexHull
from shapely.geometry import Polygon, MultiPolygon, GeometryCollection
from shapely.ops import unary_union

ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "arrange/paper_draft/figures/trace_exact_ab"
INTERACTIVE_DIR = ROOT / "interactive"
FIG_DIR.mkdir(parents=True, exist_ok=True)
INTERACTIVE_DIR.mkdir(parents=True, exist_ok=True)

SQ3 = math.sqrt(3.0)
H = SQ3 / 2.0
V = np.array([[math.cos(i * math.pi / 3), math.sin(i * math.pi / 3)] for i in range(6)])
HEX = Polygon(V)


def edge_point(i: int, t: float) -> np.ndarray:
    return V[i] + t * (V[(i + 1) % 6] - V[i])


def rotate(x: np.ndarray, theta: float) -> np.ndarray:
    c, s = math.cos(theta), math.sin(theta)
    return np.array([c * x[0] - s * x[1], s * x[0] + c * x[1]])


def line_intersection(n1: np.ndarray, c1: float, n2: np.ndarray, c2: float) -> np.ndarray:
    A = np.vstack([n1, n2])
    return np.linalg.solve(A, np.array([c1, c2]))


def triangle_vertices(normals: np.ndarray, offsets: np.ndarray) -> np.ndarray:
    pts = np.array([
        line_intersection(normals[0], offsets[0], normals[1], offsets[1]),
        line_intersection(normals[1], offsets[1], normals[2], offsets[2]),
        line_intersection(normals[2], offsets[2], normals[0], offsets[0]),
    ])
    center = pts.mean(axis=0)
    order = np.argsort(np.arctan2(pts[:, 1] - center[1], pts[:, 0] - center[0]))
    return pts[order]


def _positive_compositions(total: float, parts: int, steps: int) -> Iterable[np.ndarray]:
    if parts == 1:
        yield np.array([total])
        return
    eps = min(1e-5, total / max(1000, parts * 100))
    if total <= parts * eps:
        yield np.full(parts, total / parts)
        return
    if parts == 2:
        for u in np.linspace(eps, total - eps, steps):
            yield np.array([u, total - u])
        return
    # Simple barycentric grid for three parts.
    for i in range(steps + 1):
        for j in range(steps + 1 - i):
            w = steps - i - j
            arr = np.array([i, j, w], dtype=float)
            arr = (arr + 0.35) / (arr.sum() + 1.05) * total
            yield arr


def sample_source_triangles(
    role: int,
    a: float,
    b: float,
    mode: Literal["ordinary", "out", "in", "both"],
    theta_steps: int = 240,
    slack_steps: int = 7,
) -> list[Polygon]:
    """Sample valid unit source triangles for one local AB family.

    `a` is the backward anchor reach, `b` the forward anchor reach.
    In `out`, B(S)=b exactly; in `in`, A(S)=a exactly; in `both`, both
    reaches are exact.  All returned polygons are clipped to H.
    """
    O = V[role]
    e_in = V[(role - 1) % 6] - O
    e_out = V[(role + 1) % 6] - O
    A = O + a * e_in
    B = O + b * e_out
    points = np.vstack([O, A, B])
    polygons: list[Polygon] = []
    tol = 4e-8

    for theta in np.linspace(0.0, 2.0 * math.pi / 3.0, theta_steps, endpoint=False):
        normals = np.array([
            [math.cos(theta + 2.0 * math.pi * j / 3.0),
             math.sin(theta + 2.0 * math.pi * j / 3.0)]
            for j in range(3)
        ])
        projections = points @ normals.T
        q = projections.max(axis=0)
        slack = H - float(q.sum())
        if slack < -2e-8:
            continue
        slack = max(0.0, slack)
        din = normals @ e_in
        dout = normals @ e_out
        active_in = [j for j in range(3)
                     if din[j] > 1e-8 and abs(q[j] - float(A @ normals[j])) < tol]
        active_out = [j for j in range(3)
                      if dout[j] > 1e-8 and abs(q[j] - float(B @ normals[j])) < tol]

        offsets_list: list[np.ndarray] = []
        if mode == "ordinary":
            for extra in _positive_compositions(slack, 3, max(3, slack_steps // 2)):
                offsets_list.append(q + extra)
        elif mode in {"out", "in"}:
            active = active_out if mode == "out" else active_in
            for j in active:
                other = [k for k in range(3) if k != j]
                for extra_other in _positive_compositions(slack, 2, slack_steps):
                    extra = np.zeros(3)
                    extra[other] = extra_other
                    offsets_list.append(q + extra)
        else:  # both exact
            for j in active_in:
                for k in active_out:
                    fixed = {j, k}
                    free = [m for m in range(3) if m not in fixed]
                    if not free:
                        if slack <= 2e-7:
                            offsets_list.append(q.copy())
                        continue
                    if len(free) == 1:
                        extra = np.zeros(3)
                        extra[free[0]] = slack
                        offsets_list.append(q + extra)
                    else:
                        for extra_free in _positive_compositions(slack, len(free), slack_steps):
                            extra = np.zeros(3)
                            extra[free] = extra_free
                            offsets_list.append(q + extra)

        for offsets in offsets_list:
            if np.min(offsets - normals @ O) <= 2e-7:
                continue  # distinguished vertex must be interior
            # Exact trace checks, robust against orientation degeneracies.
            def reach(direction: np.ndarray) -> float:
                vals = []
                for n, c in zip(normals, offsets):
                    den = float(n @ direction)
                    if den > 1e-9:
                        vals.append((c - float(n @ O)) / den)
                return min(vals) if vals else float("inf")

            rin = reach(e_in)
            rout = reach(e_out)
            if mode in {"in", "both"} and abs(rin - a) > 2e-5:
                continue
            if mode in {"out", "both"} and abs(rout - b) > 2e-5:
                continue
            verts = triangle_vertices(normals, offsets)
            poly = Polygon(verts)
            if not poly.is_valid:
                poly = poly.buffer(0)
            clipped = poly.intersection(HEX)
            if not clipped.is_empty and clipped.area > 1e-9:
                if isinstance(clipped, Polygon):
                    polygons.append(clipped)
                elif isinstance(clipped, (MultiPolygon, GeometryCollection)):
                    polygons.extend([g for g in clipped.geoms if isinstance(g, Polygon) and g.area > 1e-9])
    return polygons


def union_geometry(polys: list[Polygon]):
    if not polys:
        return GeometryCollection()
    return unary_union(polys).buffer(0)


def c_l_root(m: float) -> float:
    if m <= 1e-13:
        return 1.0
    return brentq(lambda c: c**4 - c*c + m*c - m*m, H, 1.0)


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
    return brentq(lambda p: p**3-(a+2)*p*p+2*(a+1)*p-1, a, 1.0)


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


def min_enclosing_equilateral(points: list[np.ndarray]) -> tuple[float,np.ndarray]:
    pts=np.asarray(points,float)
    # remove duplicates
    uniq=[]
    for p in pts:
        if not any(np.linalg.norm(p-q)<1e-10 for q in uniq): uniq.append(p)
    pts=np.asarray(uniq)
    hull=ConvexHull(pts)
    hp=pts[hull.vertices]
    best=(float('inf'),np.empty((0,2)))
    for i in range(len(hp)):
        e=hp[(i+1)%len(hp)]-hp[i]
        n=np.array([e[1],-e[0]])/np.linalg.norm(e)
        normals=np.array([n,rotate(n,2*math.pi/3),rotate(n,4*math.pi/3)])
        supports=np.max(pts@normals.T,axis=0)
        side=2.0/SQ3*float(supports.sum())
        tri=np.array([
            line_intersection(normals[0],supports[0],normals[1],supports[1]),
            line_intersection(normals[1],supports[1],normals[2],supports[2]),
            line_intersection(normals[2],supports[2],normals[0],supports[0]),
        ])
        if side<best[0]: best=(side,tri)
    return best


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
    case: str
    roles: list[str]
    pairs: list[tuple[float,float]]
    gaps: list[Gap] = field(default_factory=list)
    envelopes: list[Envelope] = field(default_factory=list)
    extras: list[tuple[str,float,float]] = field(default_factory=list)
    note: str = ""


def one_gap(key,title,case,ell,r,x,roles,note="") -> Preset:
    x1,x2,x3,x4,x5=x
    pairs=[(1-x5,ell),(1-r,x1),(1-x1,x2),(1-x2,x3),(1-x3,x4),(1-x4,x5)]
    env=[Envelope(0,1-x5,ell,"out","left exact trace"),
         Envelope(1,1-r,x1,"in","right exact trace")]
    return Preset(key,title,case,roles,pairs,[Gap(0,ell,r)],env,note=note)


def two_gap(key,title,case,ellR,rR,ellL,rL,x,roles,note="") -> Preset:
    x1,x2,x3,x4=x
    pairs=[(1-rL,ellR),(1-rR,x1),(1-x1,x2),(1-x2,x3),(1-x3,x4),(1-x4,ellL)]
    env=[Envelope(0,1-rL,ellR,"both","two-sided exact trace"),
         Envelope(1,1-rR,x1,"in","right exact trace"),
         Envelope(5,1-x4,ellL,"out","left exact trace")]
    return Preset(key,title,case,roles,pairs,[Gap(0,ellR,rR),Gap(5,ellL,rL)],env,note=note)


PRESETS: list[Preset]=[
    Preset("zero_gap_n1_vd0","Zero-gap nine-point branch",
           r"$N_{\rm gap}=0,\ N_+=1,\ (d,t)=(0,0)$",
           ["Vd0"]*6,
           [(0.60,0.50),(0.40,0.55),(0.45,0.50),(0.50,0.45),(0.55,0.40),(0.50,0.45)],
           envelopes=[Envelope(0,0.60,0.50,"ordinary","strict-supercritical AB union")],
           extras=[("Q_-",-0.10,0.11),("Q_0",0.0,0.16),("Q_+",0.10,0.11)],
           note="Ordinary strict-supercritical AB union; no boundary gap is present."),
    one_gap("one_gap_n0_vd0","One gap, all Vd0, no supercritical role",
            r"$N_{\rm gap}=1,\ N_+=0,\ (d,t)=(0,0)$",
            .35,.65,[.60,.55,.50,.45,.40],["Vd0"]*6),
    two_gap("two_gap_vd0","Two-gap CE2 all-Vd0 branch",
            r"$N_{\rm gap}=2,\ N_+\in\{0,1\},\ (d,t)=(0,0)$",
            .42,.58,.30,.50,[.55,.50,.45,.40],["Vd0"]*6),
    one_gap("one_t3_n0","One gap with one T3-like role",
            r"$N_{\rm gap}=1,\ N_+=0,\ (d,t)=(0,1)$",
            .35,.65,[.60,.55,.50,.45,.40],["T3R","Vd0","Vd0","Vd0","Vd0","Vd0"],
            "The dashed arm marks the permitted T3-like adjacent support."),
    one_gap("two_t3_n0","One gap with two T3-like roles",
            r"$N_{\rm gap}=1,\ N_+=0,\ (d,t)=(0,2)$",
            .34,.66,[.61,.56,.50,.44,.39],["T3R","Vd0","Vd0","T3L","Vd0","Vd0"]),
    two_gap("two_gap_t3_n0","Two-gap CE2 T3-like branch",
            r"$N_{\rm gap}=2,\ N_+=0,\ (d,t)=(0,1)\text{ or }(0,2)$",
            .42,.58,.30,.50,[.55,.50,.45,.40],["T3R","Vd0","Vd0","T3L","Vd0","Vd0"]),
    one_gap("one_gap_n1_vd0_ce1","One-gap all-Vd0 CE1 branch",
            r"$N_{\rm gap}=1,\ N_+=1,\ (d,t)=(0,0),\ \mathrm{CE1}$",
            .50,.75,[.70,.62,.55,.48,.40],["Vd0"]*6,
            "The left incident role is the unique supercritical role."),
    one_gap("one_gap_n1_vd0_ce2","One-gap all-Vd0 CE2 branch",
            r"$N_{\rm gap}=1,\ N_+=1,\ (d,t)=(0,0),\ \mathrm{CE2}$",
            .45,.70,[.65,.58,.52,.46,.38],["Vd0"]*6),
    two_gap("two_gap_n1_vd0","Two-gap CE2 with one supercritical role",
            r"$N_{\rm gap}=2,\ N_+=1,\ (d,t)=(0,0)$",
            .45,.60,.25,.40,[.55,.50,.45,.35],["Vd0"]*6),
    one_gap("one_gap_n1_t3","One-gap adjacent T3-like rescuer",
            r"$N_{\rm gap}=1,\ N_+=1,\ (d,t)=(0,1)$",
            .35,.75,[.80,.65,.55,.45,.35],["T3R","Vd0","Vd0","Vd0","Vd0","Vd0"],
            "T1 is supercritical; T0 supplies the supported-trace witness."),
    two_gap("two_gap_n1_t3","Two-gap CE2 T3-like branch",
            r"$N_{\rm gap}=2,\ N_+=1,\ (d,t)=(0,1)$",
            .40,.75,.30,.55,[.80,.65,.55,.45],["T3R","Vd0","Vd0","Vd0","Vd0","Vd0"]),
    two_gap("adjacent_vd","Adjacent Vd1/Vd2 radial-separation branch",
            r"$N_+=1,\ (d,t)=(1,0)$, adjacent placement",
            .45,.60,.25,.40,[.55,.50,.45,.35],["Vd0","Vd1R","Vd0","Vd0","Vd0","Vd0"]),
    two_gap("nonadjacent_vd","Nonadjacent Vd1/Vd2 radial-separation branch",
            r"$N_+=1,\ (d,t)=(1,0)$, nonadjacent placement",
            .45,.60,.25,.40,[.55,.50,.45,.35],["Vd0","Vd0","Vd0","Vd2","Vd0","Vd0"]),
    one_gap("vd1_rescuer","Vd1 neighboring-midpoint rescuer",
            r"$N_+=1,\ (d,t)=(1,0)$, $T_0$ Vd1 rescuer",
            .35,.75,[.80,.65,.55,.45,.35],["Vd1R","Vd0","Vd0","Vd0","Vd0","Vd0"]),
    one_gap("replacement_output","Two-chart replacement output",
            r"$N_+=1,\ (d,t)=(1,0)$, pair away from $T_0$",
            .33,.67,[.61,.55,.49,.43,.37],["Vd0"]*6,
            "The displayed all-Vd0 state is the positive-gap output after replacement."),
]


def iter_polygons(geom):
    if geom.is_empty: return
    if isinstance(geom, Polygon):
        yield geom
    elif isinstance(geom, (MultiPolygon, GeometryCollection)):
        for g in geom.geoms:
            if isinstance(g, Polygon): yield g


def draw_geom(ax, geom, alpha: float, hatch: str | None=None, zorder: int=1):
    first=True
    for poly in iter_polygons(geom):
        x,y=poly.exterior.xy
        patch=MplPolygon(np.column_stack([x,y]), closed=True, alpha=alpha,
                         hatch=hatch, linewidth=0.7, zorder=zorder,
                         label="sampled envelope" if first else None)
        ax.add_patch(patch); first=False


def support_arrows(ax, roles):
    for i,code in enumerate(roles):
        left,right=role_mask(code)
        if left:
            p=.52*V[(i-1)%6]
            ax.plot([V[i,0],p[0]],[V[i,1],p[1]],linestyle='--',linewidth=1.1)
        if right:
            p=.52*V[(i+1)%6]
            ax.plot([V[i,0],p[0]],[V[i,1],p[1]],linestyle='--',linewidth=1.1)


def render_preset(preset: Preset, out: Path) -> dict:
    fig,ax=plt.subplots(figsize=(8.4,7.0))
    boundary=np.vstack([V,V[0]])
    ax.plot(boundary[:,0],boundary[:,1],linewidth=1.8,label='hexagon')
    for i in range(6):
        ax.plot([0,V[i,0]],[0,V[i,1]],linewidth=.55,alpha=.45)
        ax.text(V[i,0]+.025,V[i,1]+.025,f'$V_{i}$',fontsize=8)

    # Draw ordinary and trace-exact envelopes for each declared local family.
    cache={}
    for idx,e in enumerate(preset.envelopes):
        key=(e.role,round(e.a,6),round(e.b,6),'ordinary')
        if key not in cache:
            cache[key]=union_geometry(sample_source_triangles(e.role,e.a,e.b,'ordinary',150,5))
        draw_geom(ax,cache[key],.075,hatch='..',zorder=.5)
        if e.mode!='ordinary':
            key2=(e.role,round(e.a,6),round(e.b,6),e.mode)
            if key2 not in cache:
                cache[key2]=union_geometry(sample_source_triangles(e.role,e.a,e.b,e.mode,240,7))
            draw_geom(ax,cache[key2],.22,hatch='//',zorder=1)

    # Actual boundary traces and gaps.
    for g in preset.gaps:
        left=edge_point(g.edge,g.left); right=edge_point(g.edge,g.right)
        ax.plot([V[g.edge,0],left[0]],[V[g.edge,1],left[1]],linewidth=3.0,alpha=.60)
        ax.plot([right[0],V[(g.edge+1)%6,0]],[right[1],V[(g.edge+1)%6,1]],linewidth=3.0,alpha=.60)
        ax.plot([left[0],right[0]],[left[1],right[1]],linewidth=5.0,label='actual V-gap')
        ax.scatter([left[0],right[0]],[left[1],right[1]],s=28,zorder=7)

    support_arrows(ax,preset.roles)
    radii=radial_witnesses(preset.pairs,preset.roles)
    witness=[np.array([0.,0.]),.5*V[0]]
    labels=['O','M0']
    for g in preset.gaps:
        witness.extend([edge_point(g.edge,g.left),edge_point(g.edge,g.right)])
        labels.extend(['G-','G+'])
    for i,d in enumerate(radii):
        p=d*V[i]; witness.append(p); labels.append(f'D{i}')
        ax.scatter([p[0]],[p[1]],s=34,zorder=8)
        ax.text(p[0]+.018,p[1]+.018,f'$D_{i}$',fontsize=7)
    for label,x,y in preset.extras:
        p=np.array([x,y]); witness.append(p); labels.append(label)
        ax.scatter([x],[y],s=32,zorder=8)
        ax.text(x+.018,y+.018,f'${label}$',fontsize=7)
    side,tri=min_enclosing_equilateral(witness)
    tri_closed=np.vstack([tri,tri[0]])
    ax.plot(tri_closed[:,0],tri_closed[:,1],linestyle='--',linewidth=1.8,
            label=f'min. enclosing side {side:.3f}')
    ax.scatter([0,.5],[0,0],s=26,zorder=8)
    ax.text(.015,-.045,'$O$',fontsize=8); ax.text(.51,.02,'$M_0$',fontsize=8)

    ax.set_aspect('equal',adjustable='box')
    ax.set_xlim(-1.15,1.15); ax.set_ylim(-1.05,1.08)
    ax.set_title(preset.title+'\n'+preset.case,fontsize=10)
    ax.axis('off')
    handles,labels_legend=ax.get_legend_handles_labels()
    unique=[]; seen=set()
    for h,l in zip(handles,labels_legend):
        if l and l not in seen: seen.add(l); unique.append((h,l))
    if unique:
        ax.legend([x[0] for x in unique],[x[1] for x in unique],loc='lower center',
                  bbox_to_anchor=(.5,-.02),ncol=3,fontsize=6.5,frameon=False)
    fig.tight_layout(pad=.4)
    fig.savefig(out,dpi=190,bbox_inches='tight')
    plt.close(fig)
    return {'side':side,'radii':radii}


def make_atlas_tex():
    lines=[r"\subsection{Trace-exact AB-envelope atlas}",
           r"\label{subsec:trace-exact-ab-atlas}","",
           r"Figures~\ref{fig:trace-exact-ab-atlas-1}--\ref{fig:trace-exact-ab-atlas-8}",
           r"show the normalized subcases in Table~\ref{tab:finite-enclosure-subcases}.",
           r"Each shaded trace-exact envelope is a dense union of valid source triangles;",
           r"the exact proof object is the source-conditioned union in",
           r"Subsection~\ref{subsec:trace-exact-ab-envelopes}.  The dashed equilateral",
           r"triangle is the numerical minimum for the displayed finite witness set and is",
           r"included only to explain the terminal geometry.",""]
    for k in range(0,len(PRESETS),2):
        pair=PRESETS[k:k+2]
        num=k//2+1
        lines += [r"\begin{figure}[p]",r"\centering"]
        for j,p in enumerate(pair):
            width='.485\\linewidth'
            lines += [rf"\begin{{minipage}}[t]{{{width}}}",r"\centering",
                      rf"\includegraphics[width=\linewidth]{{figures/trace_exact_ab/{p.key}.png}}",
                      rf"\textbf{{({chr(97+j)})}} {p.title}.",r"\end{minipage}"]
            if j==0 and len(pair)>1: lines.append(r"\hfill")
        caption='; '.join(p.title for p in pair)
        lines += [rf"\caption{{Trace-exact AB-envelope snapshots: {caption}.}}",
                  rf"\label{{fig:trace-exact-ab-atlas-{num}}}",r"\end{figure}",""]
    (ROOT/'arrange/paper_draft/06i_trace_exact_ab_atlas.tex').write_text('\n'.join(lines)+'\n')


def make_html(results: dict[str,dict]):
    data=[]
    for p in PRESETS:
        d=asdict(p)
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
<section class="card"><h2>Interpretation</h2><p id="note"></p><p>The PNG figures in the paper are produced from the same preset registry and source-family sampler.</p></section></div></main>
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
const sel=document.getElementById('preset');PRESETS.forEach((p,i)=>{let o=document.createElement('option');o.value=i;o.textContent=(i+1)+'. '+p.title;sel.appendChild(o)});function update(){let p=PRESETS[+sel.value];document.getElementById('case').innerHTML=p.case;document.getElementById('note').textContent=p.note||'The source envelopes enforce the actual gap endpoints; ordinary capacities remain safe upper bounds.';let rows='<tr><th>role</th><th>type</th><th>(a,b)</th></tr>';p.pairs.forEach((x,i)=>rows+=`<tr><td>T${i}</td><td>${p.roles[i]}</td><td>(${x[0].toFixed(3)}, ${x[1].toFixed(3)})</td></tr>`);rows+=`<tr><td colspan="2">displayed min. side</td><td>${p.result.side.toFixed(6)}</td></tr>`;document.getElementById('tbl').innerHTML=rows;draw()}sel.onchange=update;['ordinary','exact','witness'].forEach(x=>document.getElementById(x).onchange=draw);update();
</script></body></html>'''
    html=html_template.replace('__PRESETS__',jsdata)
    (INTERACTIVE_DIR/'trace_exact_ab_envelope_explorer.html').write_text(html,encoding='utf-8')
    (INTERACTIVE_DIR/'trace_exact_ab_presets.json').write_text(json.dumps(data,indent=2),encoding='utf-8')


def main():
    results={}
    for idx,p in enumerate(PRESETS,1):
        out=FIG_DIR/f'{p.key}.png'
        result=render_preset(p,out)
        result['triangle']=min_enclosing_equilateral(
            [np.array([0.,0.]),.5*V[0]]+
            [edge_point(g.edge,t) for g in p.gaps for t in (g.left,g.right)]+
            [result['radii'][i]*V[i] for i in range(6)]+
            [np.array([x,y]) for _,x,y in p.extras]
        )[1].tolist()
        results[p.key]=result
        print(f'{idx:02d} {p.key}: side={result["side"]:.6f}')
    make_atlas_tex()
    make_html(results)

if __name__=='__main__':
    main()
