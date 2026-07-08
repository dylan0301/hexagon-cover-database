r"""Generate exact certificates for the bulk zone
   {1/32 <= s <= 1/2,  s <= t <= min(tmax(s), 1-s)}   (WLOG half).

Boxes [s1,s2]x[t1,t2] from a recursive subdivision of the root box.
Per kept box: fixed supersets  K^ = K(s1, 1-t2) at V_1..V_5 and
K^_0 = K(t1, 1-s2) at V_0 (monotonicity), constant rational witnesses in
the fixed hole, constant fitting arcs, constant validity certificates
(disk or selection arcs).  All exact checks are Q(sqrt3)-number signs.

Writes hole_certificates_bulk.py.
"""
import itertools
import numpy as np
import sympy as sp
from fractions import Fraction

import hole_cert_lib as L
import verify_ab_set as V
from hole_lab import Hole, HCONST

s, t = L.s, L.t
R3, H = L.R3, L.H
NAMES = 'AOBx'
S0 = sp.Rational(1, 32)
SMAXB = sp.Rational(1, 2)


def tmax_of(sv):
    q = 1 - sv
    return (-q + np.sqrt(4 - 3 * q * q)) / 2


WEDGE = sp.Rational(5, 4)          # C-ext covers {s<=1/16, t <= (5/4)s}
S16 = sp.Rational(1, 16)


def box_disjoint(box):
    """certified-disjoint from the region (exact rational conditions)"""
    s1, s2, t1, t2 = box
    if t2 <= s1:                       # below diagonal t >= s
        return ('below-diagonal', t2, s1)
    if s2 <= S16 and t2 <= WEDGE * s1:  # covered by corner leaf C-ext
        return ('wedge', t2, WEDGE * s1)
    if t1 >= 1 - s1:                   # above the WLOG line t <= 1-s
        return ('above-half', t1, 1 - s1)
    # above the R0 constraint: R0^2(s,t) >= 1 for all box points iff at
    # (s2, t1) [R0^2 decreasing in s, increasing in t]
    R2c = sp.expand(t1 ** 2 + t1 * (1 - s2) + (1 - s2) ** 2)
    if R2c >= 1:
        return ('above-R0', sp.nsimplify(R2c))
    return None


def t2_eff(box):
    """rational upper bound for t over the feasible part of the box:
    t <= min(t2, tmax(s2), 1 - s1); tmax(s2) is bounded above by any
    rational r with R0^2(s2, r) >= 1 (exactly checkable)."""
    s1, s2, t1, t2 = box
    cap = min(t2, 1 - s1)
    tm = tmax_of(float(s2))
    if float(cap) <= tm:
        return sp.nsimplify(cap), None
    r = sp.Rational(Fraction(tm).limit_denominator(4096))
    while sp.Rational(sp.expand(r ** 2 + r * (1 - s2) + (1 - s2) ** 2)) < 1:
        r += sp.Rational(1, 4096)
    return min(cap, r), r


def fixed_sets(box):
    """superset parameters per vertex for the box (exact rationals),
    with t clipped to the feasible part of the box.  For boxes inside
    s <= 1/16 the wedge t <= (5/4)s is covered by leaf C-ext, so the
    remaining region has t >= (5/4)s >= (5/4)s1: t1 may be raised."""
    s1, s2, t1, t2 = box
    t2e, twitness = t2_eff(box)
    t1e = max(t1, WEDGE * s1) if s2 <= S16 else t1
    a = [t1e, s1, s1, s1, s1, s1]
    b = [1 - s2] + [1 - t2e] * 5
    return a, b, t2e, t1e


def hole_of_box(box, ntheta=360, m=3000):
    a, b, _, _ = fixed_sets(box)
    return Hole(np.array([float(v) for v in a]),
                bvec=np.array([float(v) for v in b]))


def in_hex_exact(pt):
    import hole_cert_gen as G
    for k in range(6):
        n = L.u_deg((30 + 60 * k) % 360)
        if G.exact_sign_q3(sp.expand(H - (pt[0] * n[0] + pt[1] * n[1]))) < 0:
            return False
    return True


def rational_point(x, denom=96):
    return (sp.Rational(Fraction(float(x[0])).limit_denominator(denom)),
            sp.Rational(Fraction(float(x[1])).limit_denominator(denom)))


def eval_q3(e):
    return float(sp.nsimplify(e))


def pts_of_ab(a, b):
    A = sp.Matrix([-a / 2, R3 * a / 2])
    O = sp.Matrix([0, 0])
    B = sp.Matrix([b, 0])
    return {'A': A, 'O': O, 'B': B}


def to_local_const(j, gpt):
    return L.to_local(j, sp.Matrix([gpt[0], gpt[1]]))


def sel_vec(a, b, xloc, sigma):
    pts = pts_of_ab(a, b)
    pts['x'] = xloc
    return L.selection_vector([pts[c] for c in sigma])


def exact_ge(a_expr, b_expr):
    """exact a >= b in Q(sqrt3)"""
    import hole_cert_gen as G
    return G.exact_sign_q3(sp.expand(a_expr - b_expr)) >= 0


def dir_of_angle_rational(deg, denom=64):
    base = 30 * round(deg / 30)
    off = deg - base
    bvec = L.u_deg(base % 360)
    if abs(off) < 1e-9:
        return bvec
    import hole_cert_gen as G
    xi = sp.Rational(Fraction(np.tan(np.radians(abs(off) / 2)))
                     .limit_denominator(denom))
    return G.rot_tanhalf(bvec, xi, 1 if off > 0 else -1)


def box_gens(box):
    s1, s2, t1, t2 = box
    R02 = sp.expand(t ** 2 + t * (1 - s) + (1 - s) ** 2)
    return {'s': s - s1, 'g': t - s, 'R0slack': sp.expand(1 - R02),
            'shi': s2 - s, 'tlo': t - t1, 'thi': t2 - t}


def box_samples(box, n=4):
    s1, s2, t1, t2 = [float(v) for v in box]
    out = []
    for sv in np.linspace(s1, s2, n):
        q = 1 - sv
        tmaxs = (-q + np.sqrt(4 - 3 * q * q)) / 2
        lo = max(t1, sv)
        hi = min(t2, tmaxs)
        if hi <= lo:
            continue
        for tv in np.linspace(lo + 1e-9, hi, n):
            out.append((sv, tv))
    return out


def validity_param_K0(xglob, box, tag):
    """parametric selection certificate that the constant point xglob is
    outside K(t, 1-s) at V_0 for every feasible (s,t) in the box (needed
    for diagonal-adjacent boxes where the frozen superset degenerates)."""
    import gen_corner as GC
    gens = box_gens(box)
    pre = box_samples(box)
    if not pre:
        return None
    xloc = L.to_local(0, sp.Matrix([xglob[0], xglob[1]]))
    xloc = sp.Matrix([sp.expand(xloc[0]), sp.expand(xloc[1])])
    cut_pool = [L.u_deg(d) for d in (0, 30, 60, 90, 120)]
    u90, u180v = L.u_deg(90), sp.Matrix([-1, 0])
    u30, u120v = L.u_deg(30), L.u_deg(120)
    for mu in (t - s, t, s):
        for c in (sp.Rational(1, 2), 1, 2):
            cut_pool.append(sp.Matrix(u90 - c * mu * u180v))
            cut_pool.append(sp.Matrix(u90 + c * mu * u180v))
            cut_pool.append(sp.Matrix(u30 - c * mu * u120v))
    m0 = sp.Matrix([sp.sqrt(3) * t, t + 2 * (1 - s)])
    mp = sp.Matrix([-m0[1], m0[0]])
    R0sl = gens['R0slack']
    cut_pool.append(m0)
    for c in (sp.Rational(1, 2), 1, 2, 4):
        cut_pool.append(sp.Matrix(m0 + c * R0sl * mp))
        cut_pool.append(sp.Matrix(m0 - c * R0sl * mp))
    try:
        arcs = GC.validity_selection(tag, xloc, 0, gens, pre, cut_pool)
    except RuntimeError:
        return None
    return {'kind': 'sel-param',
            'gens': {k: sp.srepr(sp.expand(v)) for k, v in gens.items()},
            'arcs': arcs}


def validity_const(xglob, j, a, b, hole, floor=5e-4):
    """constant validity certificate of xglob vs K(a,b) at vertex j:
    disk if possible else selection arcs (constant).  Returns dict or None
    (None = the witness is inside / too close)."""
    import hole_cert_gen as G
    xloc = to_local_const(j, xglob)
    # quick numeric membership
    XY = np.array([[float(xloc[0]), float(xloc[1])]])
    ang = np.degrees(np.arctan2(XY[0, 1], XY[0, 0]))
    r = np.hypot(*XY[0])
    if (not (-1e-9 <= ang <= 120 + 1e-9)) and r > 1e-12:
        # outside the cone: certify via a cone half-plane (linear, exact)
        # cone = {Y >= 0} ∩ {sqrt3 X + Y <= ... } in local coords:
        # outside iff Y < 0 or sqrt3*X < -Y i.e. the point violates one.
        if float(xloc[1]) < 0:
            return {'kind': 'cone', 'side': 'B',
                    'value': sp.srepr(sp.expand(-xloc[1]))}
        val = sp.expand(-(R3 * xloc[0] + xloc[1]))
        if float(val) > 0:
            return {'kind': 'cone', 'side': 'A', 'value': sp.srepr(val)}
    fv = hole.Fmin_local(j, XY, nphi=1024)[0] - HCONST
    if fv <= floor:
        return None
    # disk exclusions
    for cname, P in pts_of_ab(a, b).items():
        qv = sp.expand((xloc[0] - P[0]) ** 2 + (xloc[1] - P[1]) ** 2 - 1)
        if eval_q3(qv) > 1e-6 and exact_ge(qv, 0):
            return {'kind': 'disk', 'center': cname,
                    'value': sp.srepr(qv)}
    # selection arcs (constant)
    sigmas = [''.join(p) for p in itertools.product(NAMES, repeat=3)]
    vecs = {sg: sel_vec(a, b, xloc, sg) for sg in sigmas}
    fns = {sg: (float(v[0]), float(v[1])) for sg, v in vecs.items()}
    nphi = 720
    phis = np.linspace(0, 2 * np.pi / 3, nphi)
    Hc = float(H)
    vals = {sg: fns[sg][0] * np.cos(phis) + fns[sg][1] * np.sin(phis) - Hc
            for sg in sigmas}
    best = np.max(np.stack(list(vals.values())), 0)
    if best.min() <= 1e-6:
        return None
    # greedy arcs
    arcs = []
    i, start = 0, 0
    cur = max(sigmas, key=lambda sg: vals[sg][0])
    while i < nphi - 1:
        j2 = i
        while j2 < nphi - 1 and vals[cur][j2 + 1] > 0.35 * best[j2 + 1]:
            j2 += 1
        if j2 == nphi - 1:
            arcs.append((start, nphi - 1, cur))
            break
        nxt = max(sigmas, key=lambda sg: vals[sg][min(j2 + 3, nphi - 1)])
        ok = np.where((vals[cur][: j2 + 1] > 0.3 * best[: j2 + 1])
                      & (vals[nxt][: j2 + 1] > 0.3 * best[: j2 + 1]))[0]
        ok = ok[ok >= start + 1]
        cut = int(ok[-1]) if len(ok) else j2
        arcs.append((start, cut, cur))
        start, i, cur = cut, cut, nxt
    out = []
    prev = L.u_deg(0)
    for k, (i0, i1, sg) in enumerate(arcs):
        d2 = (L.u_deg(120) if k == len(arcs) - 1
              else dir_of_angle_rational(np.degrees(phis[i1])))
        w = vecs[sg]
        # exact endpoint checks
        for dd in (prev, d2):
            lin = sp.expand(w[0] * dd[0] + w[1] * dd[1])
            quad = sp.expand(lin ** 2 - H ** 2 * (dd[0] ** 2 + dd[1] ** 2))
            if not (exact_ge(lin, 0) and exact_ge(quad, 0)):
                return None
        cross = sp.expand(prev[0] * d2[1] - prev[1] * d2[0])
        if not exact_ge(cross, 0) or eval_q3(cross) <= 0:
            return None
        out.append({'sigma': sg,
                    'd1': (sp.srepr(prev[0]), sp.srepr(prev[1])),
                    'd2': (sp.srepr(d2[0]), sp.srepr(d2[1]))})
        prev = d2
    return {'kind': 'sel', 'arcs': out}


def fitting_const(wits, hole_pts, floor=2e-3):
    """constant fitting arcs from the witness dict {name: exact (x,y)}"""
    import hole_cert_gen as G
    names = list(wits.keys())
    P = {k: (float(v[0]), float(v[1])) for k, v in wits.items()}
    nphi = 720
    phis = np.linspace(0, 2 * np.pi / 3, nphi)
    Hc = float(H)
    # triples: assign per normal the best witness at each phi
    def triple_val(tr, ph):
        tot = 0.0
        for k in range(3):
            th = ph + 2 * np.pi * k / 3
            x, y = P[tr[k]]
            tot += x * np.cos(th) + y * np.sin(th)
        return tot
    # best triple per phi (greedy from per-normal argmax)
    best_tr = []
    for ph in phis:
        tr = []
        for k in range(3):
            th = ph + 2 * np.pi * k / 3
            tr.append(max(names, key=lambda nm: P[nm][0] * np.cos(th)
                          + P[nm][1] * np.sin(th)))
        best_tr.append(tuple(tr))
    vals = np.array([triple_val(tr, ph) - Hc
                     for tr, ph in zip(best_tr, phis)])
    if vals.min() <= floor:
        return None
    # arcs of constant triple
    arcs = []
    start = 0
    for i in range(1, nphi):
        if best_tr[i] != best_tr[start]:
            arcs.append((start, i, best_tr[start]))
            start = i
    arcs.append((start, nphi - 1, best_tr[start]))
    # merge micro-arcs into neighbors when neighbor triple still >= floor
    merged = []
    for (i0, i1, tr) in arcs:
        if merged and (i1 - i0) < 6:
            ptr = merged[-1][2]
            if all(triple_val(ptr, phis[i]) - Hc > 0.5 * floor
                   for i in range(i0, i1 + 1)):
                merged[-1] = (merged[-1][0], i1, ptr)
                continue
        merged.append((i0, i1, tr))
    arcs = merged
    out = []
    prev = L.u_deg(0)
    for k, (i0, i1, tr) in enumerate(arcs):
        d2 = (L.u_deg(120) if k == len(arcs) - 1
              else dir_of_angle_rational(np.degrees(phis[i1])))
        w = L.selection_vector([sp.Matrix(wits[tr[0]]),
                                sp.Matrix(wits[tr[1]]),
                                sp.Matrix(wits[tr[2]])])
        for dd in (prev, d2):
            lin = sp.expand(w[0] * dd[0] + w[1] * dd[1])
            quad = sp.expand(lin ** 2 - H ** 2 * (dd[0] ** 2 + dd[1] ** 2))
            if not (exact_ge(lin, 0) and exact_ge(quad, 0)):
                return None
        cross = sp.expand(prev[0] * d2[1] - prev[1] * d2[0])
        if eval_q3(cross) <= 0:
            return None
        out.append({'triple': tr,
                    'd1': (sp.srepr(prev[0]), sp.srepr(prev[1])),
                    'd2': (sp.srepr(d2[0]), sp.srepr(d2[1]))})
        prev = d2
    return out


def process_box(box, depth=0, maxdepth=13):
    """returns list of certified box dicts (possibly after subdivision)"""
    s1, s2, t1, t2 = box
    dis = box_disjoint(box)
    tag = f'[{float(s1):.4f},{float(s2):.4f}]x[{float(t1):.4f},{float(t2):.4f}]'
    if dis:
        return [{'box': [sp.srepr(v) for v in box], 'kind': 'disjoint',
                 'why': dis[0]}]
    def subdivide():
        if depth >= maxdepth:
            raise RuntimeError(f'max depth at {tag}')
        if (s2 - s1) >= (t2 - t1):
            sm = (s1 + s2) / 2
            k1 = process_box((s1, sm, t1, t2), depth + 1, maxdepth)
            k2 = process_box((sm, s2, t1, t2), depth + 1, maxdepth)
        else:
            tm = (t1 + t2) / 2
            k1 = process_box((s1, s2, t1, tm), depth + 1, maxdepth)
            k2 = process_box((s1, s2, tm, t2), depth + 1, maxdepth)
        return k1 + k2
    s1, s2, t1, t2 = box
    diag_adjacent = bool(t1 < s2)
    if diag_adjacent:
        # frozen sliver superset degenerates; search on the centre config
        sc = float(s1 + s2) / 2
        qq = 1 - sc
        tmaxs = (-qq + np.sqrt(4 - 3 * qq * qq)) / 2
        tc = min(max(float(t1 + t2) / 2, sc * (1 + 1e-6)), tmaxs)
        if tc <= sc:
            return [{'box': [sp.srepr(v) for v in box], 'kind': 'disjoint',
                     'why': 'below-diagonal', 'note': 'feasible part empty'}]
        from hole_lab import Hole as _H
        a_c, b_c, t2e_c = ([tc] + [sc] * 5, [1 - sc] + [1 - tc] * 5, None)
        hole = _H(np.array([tc] + [sc] * 5),
                  bvec=np.array([1 - sc] + [1 - tc] * 5))
    else:
        hole = hole_of_box(box)
    try:
        pts, tags, _ = hole.hole_boundary_points(ntheta=220, m=1800)
    except Exception:
        return subdivide()
    if len(pts) < 10:
        return subdivide()
    # drop ghost points (near-coincident boundaries of adjacent sets):
    # require a genuine clearance from every other set
    clr = np.full(len(pts), np.inf)
    for j in range(6):
        XY = hole.to_local(j, pts)
        ang = np.degrees(np.arctan2(XY[:, 1], XY[:, 0]))
        r = np.hypot(XY[:, 0], XY[:, 1])
        inc = ((ang >= -1e-9) & (ang <= 120 + 1e-9)) | (r < 1e-12)
        if inc.any():
            fv = hole.Fmin_local(j, XY[inc], nphi=1024) - HCONST
            cj = np.full(len(pts), np.inf)
            cj[inc] = fv
            # points on their own set's boundary have fv ~ 0 for that set;
            # clearance = second-smallest is approximated by ignoring
            # values within 5e-5 of zero (own boundary)
            cj[np.abs(cj) < 5e-5] = np.inf
            clr = np.minimum(clr, cj)
    real = clr > 2e-4
    if real.sum() < 10:
        return subdivide()
    deep_pt = pts[int(np.argmax(np.where(np.isfinite(clr), clr, -1.0)))]
    pts = pts[real]
    f, phimin, _ = hole.min_F_S(pts=pts)
    margin = f - HCONST
    if margin < 0.004:
        return subdivide()
    # witnesses: support argmaxes at 12 directions, pulled inward
    a, b, t2e, t1e = fixed_sets(box)
    ctr = deep_pt if np.isfinite(deep_pt).all() else pts.mean(0)
    wits = {}
    pull = min(margin / 4, 0.02)
    denom = 64
    while 1.0 / denom > max(margin / 8, 1e-4) and denom < 65536:
        denom *= 4
    seen, wuniq, val = set(), {}, {}
    for k in range(12):
        ang = k * np.pi / 6
        n = np.array([np.cos(ang), np.sin(ang)])
        j = int(np.argmax(pts @ n))
        d = ctr - pts[j]
        nd = np.hypot(*d)
        if nd <= 1e-12:
            continue
        for mult in (1, 2, 4, 8):
            v = rational_point(pts[j] + (d / nd) * pull * mult, denom=denom)
            if v in seen or not in_hex_exact(v):
                continue
            ok = {}
            for jj in range(6):
                if jj == 0 and diag_adjacent:
                    c = validity_param_K0(v, box, f'K0param')
                else:
                    c = validity_const(v, jj, a[jj], b[jj], hole)
                if c is None:
                    ok = None
                    break
                ok[jj] = c
            if ok is not None:
                wuniq[f'P{k}'] = v
                val[f'P{k}'] = ok
                seen.add(v)
                break
    if len(wuniq) < 2:
        return subdivide()
    fit = fitting_const(wuniq, pts)
    if fit is None:
        return subdivide()
    used = sorted({nm for arc in fit for nm in arc['triple']})
    return [{'box': [sp.srepr(v) for v in box], 'kind': 'certified',
             't2e': sp.srepr(t2e), 't1e': sp.srepr(t1e),
             'sets': [(sp.srepr(a[j]), sp.srepr(b[j])) for j in range(6)],
             'witnesses': {k: (sp.srepr(wuniq[k][0]), sp.srepr(wuniq[k][1]))
                           for k in used},
             'validity': {k: val[k] for k in used},
             'fitting': fit}]


def main():
    roots = [(S0, S16, S0, sp.Rational(2, 3)),
             (S16, SMAXB, S16, sp.Rational(2, 3))]
    boxes = []
    for root in roots:
        boxes += process_box(root)
        print(f'root {root}: cumulative {len(boxes)} boxes', flush=True)
    ncert = sum(1 for b in boxes if b['kind'] == 'certified')
    print(f'{len(boxes)} boxes ({ncert} certified, '
          f'{len(boxes) - ncert} disjoint)')
    with open('hole_certificates_bulk.py', 'w') as f:
        f.write('# generated by gen_bulk.py — exact certificate data\n')
        f.write('DATA = ' + repr({'roots': [[sp.srepr(v) for v in r]
                                            for r in roots],
                                  'boxes': boxes}) + '\n')
    print('written hole_certificates_bulk.py')


if __name__ == '__main__':
    main()
