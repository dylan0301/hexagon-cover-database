r"""Generate exact certificates for the corner zone C (s <= 1/32).

Writes hole_certificates_corner.py.  Run:  python3 gen_corner.py
"""
import numpy as np
import sympy as sp
import itertools
from fractions import Fraction

import hole_cert_lib as L
import hole_cert_gen as G

s, t = L.s, L.t
R3, H = L.R3, L.H
NAMES = 'AOBx'
FAILED = []


# ----------------------------------------------------------------
# helpers
# ----------------------------------------------------------------
def leaf_samples(leaf, ns=4, nl=6):
    out = []
    if leaf == 'C-ext':
        svals = np.linspace(float(G.S0), 1 / 16, ns)
    else:
        svals = np.linspace(0.0015, float(G.S0), ns)
    for sv in svals:
        q = 1 - sv
        tmax = (-q + np.sqrt(4 - 3 * q * q)) / 2
        ts = 8 * sv / 5
        if leaf == 'C-low':
            lo, hi = sv, min(ts, tmax)
        elif leaf == 'C-high':
            lo, hi = min(ts, tmax), tmax
        else:
            lo, hi = sv, min(1.25 * sv, tmax)
        for tv in np.linspace(lo + 1e-9, hi, nl):
            out.append((float(sv), float(tv)))
    return out


def rational_dir(deg_target, denom=64):
    """rational-tan-half direction near deg_target (exact in Q(sqrt3) when
    a multiple of 30; else rot_tanhalf from the nearest multiple of 30)"""
    base = 30 * round(deg_target / 30)
    off = deg_target - base
    b = L.u_deg(base % 360)
    if abs(off) < 1e-12:
        return b
    xi = sp.Rational(round(np.tan(np.radians(abs(off) / 2)) * denom), denom)
    return G.rot_tanhalf(b, xi, 1 if off > 0 else -1)


def numeric_vec(v):
    f = sp.lambdify((s, t), v, 'numpy')
    return lambda sv, tv: np.array(f(sv, tv), float).reshape(2)


def pts_of_set(j):
    a, b = L.ab_of(j)
    A = sp.Matrix([-a / 2, R3 * a / 2])
    O = sp.Matrix([0, 0])
    B = sp.Matrix([b, 0])
    return {'A': A, 'O': O, 'B': B}


def sel_vector(j, sigma, xloc):
    pts = pts_of_set(j)
    pts['x'] = xloc
    return L.selection_vector([pts[c] for c in sigma])


def clear_den(expr):
    """expr -> (numer, denom) exact, denom to be certified positive"""
    e = sp.cancel(sp.together(sp.expand(expr)))
    n, d = sp.fraction(e)
    # normalize sign so denominator has positive leading numeric part
    return sp.expand(n), sp.expand(d)


CERT_CACHE = {}


def strictness_term(cert, gens):
    """index data of a certificate term that is > 0 on {s>0, g>0}:
    constant term or a term supported on {s, g, dg?} only — dg = 2s-t may
    vanish at t = 2s inside the open region, so only {s, g} count.
    Returns the (coeff, alpha) or None."""
    gnames = list(gens.keys())
    ok_idx = {gnames.index('s')}
    if 'g' in gnames:
        ok_idx.add(gnames.index('g'))
    for c, a in cert:
        if all((v == 0 or i in ok_idx) for i, v in enumerate(a)):
            return (c, a)
    return None


def cert_ineq(tag, expr, gens, pre_samples, floor=0.0, need_strict=False):
    """certify expr >= 0 on the region given by gens; returns dict with
    numerator/denominator Handelman certificates. Numeric precheck on
    pre_samples.  need_strict: additionally guarantee expr > 0 on the open
    region {s>0, g>0} by exhibiting a strictness term (re-certifying
    q - eps*s^k*g^m when necessary)."""
    n, d = clear_den(expr)
    fn = sp.lambdify((s, t), n / d, 'numpy')
    worst = min(float(fn(sv, tv)) for sv, tv in pre_samples)
    if worst < -1e-12:
        raise RuntimeError(f'{tag}: numeric precheck FAILED ({worst:.2e})')
    dn = sp.lambdify((s, t), d, 'numpy')
    if min(float(dn(sv, tv)) for sv, tv in pre_samples) <= 0:
        n, d = -n, -d
        if min(float(sp.lambdify((s, t), d, 'numpy')(sv, tv))
               for sv, tv in pre_samples) <= 0:
            raise RuntimeError(f'{tag}: denominator sign not constant')
    out = {}
    for part, key in ((n, 'num'), (d, 'den')):
        strict_here = need_strict and key == 'num'
        pkey = (sp.srepr(sp.expand(part)), strict_here,
                tuple(sorted(sp.srepr(sp.expand(v))
                             for v in gens.values())))
        if pkey in CERT_CACHE:
            out[key] = CERT_CACHE[pkey]
            continue
        item = None
        cert, dm, aux = G.certify_nonneg_auto(part, gens,
                                              samples=pre_samples)
        if cert is not None and (not strict_here
                                 or strictness_term(cert, gens)):
            item = {'poly': sp.srepr(sp.expand(part)),
                    'cert': [(sp.srepr(c), a) for c, a in cert],
                    'degmax': dm}
            if aux:
                item['aux_sq'] = [sp.srepr(l) for l in aux]
        elif strict_here:
            # shave eps * gs^k gg^m (gs, gg = the leaf's own s/g gens)
            gnames = list(gens.keys())
            i_s, i_g = gnames.index('s'), gnames.index('g')
            gs_, gg_ = sp.expand(gens['s']), sp.expand(gens['g'])
            for (k, m) in [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (2, 1),
                           (1, 2), (3, 0), (2, 2), (3, 1), (4, 0), (3, 2),
                           (4, 1), (4, 2), (5, 1), (6, 0)]:
                mono = gs_ ** k * gg_ ** m
                fm = sp.lambdify((s, t), mono, 'numpy')
                ratio = min(float(fn(sv, tv)) / max(float(fm(sv, tv)), 1e-30)
                            for sv, tv in pre_samples)
                if ratio <= 0:
                    continue
                eps = sp.Rational(Fraction(ratio / 4)
                                  .limit_denominator(10 ** 4))
                if eps <= 0:
                    continue
                cert2, dm2, aux2 = G.certify_nonneg_auto(
                    sp.expand(part - eps * mono), gens,
                    samples=pre_samples)
                if cert2 is not None:
                    alpha = [0] * len(gnames)
                    alpha[i_s], alpha[i_g] = k, m
                    # pad the strictness term's alpha to the aux width
                    wid = max((len(a) for c_, a in cert2), default=len(alpha))
                    alpha = tuple(alpha + [0] * (wid - len(alpha)))
                    cert2 = list(cert2) + [(eps, alpha)]
                    item = {'poly': sp.srepr(sp.expand(part)),
                            'cert': [(sp.srepr(c), a) for c, a in cert2],
                            'degmax': dm2}
                    if aux2:
                        item['aux_sq'] = [sp.srepr(l) for l in aux2]
                    break
        if item is None:
            raise RuntimeError(f'{tag}/{key}: no Handelman certificate '
                               f'(deg<=5{"+strict" if strict_here else ""});'
                               f' poly = {sp.expand(part)}')
        if strict_here:
            # final check of the strictness term on the merged certificate
            cc = [(sp.sympify(cs), a) for cs, a in item['cert']]
            if strictness_term(cc, gens) is None:
                raise RuntimeError(f'{tag}/{key}: strictness term missing')
        CERT_CACHE[pkey] = item
        out[key] = item
    return out


def endpoint_certs(tag, w, d, gens, pre, h0=H):
    """certificates for <w, d/|d|> > h0:  lin = <w,d> >= 0 and
    quad = <w,d>^2 - h0^2 |d|^2 > 0 (strict via strictness term)"""
    lin = w[0] * d[0] + w[1] * d[1]
    quad = lin ** 2 - h0 ** 2 * (d[0] ** 2 + d[1] ** 2)
    return {'lin': cert_ineq(tag + '/lin', lin, gens, pre),
            'quad': cert_ineq(tag + '/quad', quad, gens, pre,
                              need_strict=True)}


def hexagon_certs(tag, w, gens, pre):
    """certificates that w is in the hexagon: h - <w, u(30+60k)> >= 0"""
    out = []
    for k in range(6):
        n = L.u_deg((30 + 60 * k) % 360)
        e = H - (w[0] * n[0] + w[1] * n[1])
        out.append(cert_ineq(f'{tag}/hex{k}', e, gens, pre))
    return out


def arc_cert(tag, d1, d2, gens, pre):
    """certificate that the arc from d1 to d2 (ccw) is < 180 deg and
    positively oriented: cross(d1,d2) > 0"""
    cr = d1[0] * d2[1] - d1[1] * d2[0]
    return cert_ineq(tag + '/cross', cr, gens, pre)


# ----------------------------------------------------------------
# validity: automated selection-arc search
# ----------------------------------------------------------------
def try_arcs(tag, arcs_spec, gens, pre):
    """attempt exact certification of a full arc list; returns certified
    list or None"""
    certified = []
    for k, arc in enumerate(arcs_spec):
        atag = f'{tag}/arc{k}({arc["sigma"]})'
        try:
            ac = arc_cert(atag, arc['d1'], arc['d2'], gens, pre)
            e1 = endpoint_certs(atag + '/d1', arc['w'], arc['d1'], gens, pre)
            e2 = endpoint_certs(atag + '/d2', arc['w'], arc['d2'], gens, pre)
        except RuntimeError as e:
            print(f'    [cert-fail] {str(e)[:180]}', flush=True)
            return ('FAIL', k)
        certified.append({'sigma': arc['sigma'],
                          'd1': (sp.srepr(arc['d1'][0]),
                                 sp.srepr(arc['d1'][1])),
                          'd2': (sp.srepr(arc['d2'][0]),
                                 sp.srepr(arc['d2'][1])),
                          'cross': ac, 'end1': e1, 'end2': e2})
    return certified


def validity_selection(tag, xloc, j, gens, pre, cut_pool, nphi=1441,
                       min_floor=1e-12):
    """find arcs + selections certifying  F^{(j)}_{A,O,B,x} > h  for all
    phi; returns list of arcs [{'d1','d2','sigma','w'}] (exact) after
    exact certification of all endpoints."""
    sigmas = [''.join(p) for p in itertools.product(NAMES, repeat=3)]
    vecs = {sg: sel_vector(j, sg, xloc) for sg in sigmas}
    fns = {sg: numeric_vec(v) for sg, v in vecs.items()}
    phis = np.linspace(0, 2 * np.pi / 3, nphi)
    U = np.stack([np.cos(phis), np.sin(phis)], 0)
    Hc = float(H)
    # per-sample scale reference and normalized value arrays
    Hc = float(H)
    bestmin = {}
    Vraw = {}
    for sg in sigmas:
        Vraw[sg] = np.stack([fns[sg](sv, tv) @ U - Hc for sv, tv in pre])
    stack = np.stack([Vraw[sg] for sg in sigmas])       # (nsig, nsmp, nphi)
    best_per_sample = stack.max(0)                       # (nsmp, nphi)
    for idx in range(len(pre)):
        m = best_per_sample[idx].min()
        if m <= min_floor:
            raise RuntimeError(f'{tag}: witness not certifiable at sample '
                               f'{pre[idx]} (best {m:.2e})')
        bestmin[idx] = max(m, 1e-12)
    scale = np.array([bestmin[i] for i in range(len(pre))])[:, None]
    Vn = {sg: Vraw[sg] / scale for sg in sigmas}
    rmin = {sg: Vn[sg].min(0) for sg in sigmas}

    # template attempt: constant cuts at 30 and 90 degrees
    i30 = int(round((nphi - 1) / 4)); i90 = int(round(3 * (nphi - 1) / 4))
    tpl = []
    okt = True
    for (i0, i1, imid) in ((0, i30, i30 // 2), (i30, i90, (i30 + i90) // 2),
                           (i90, nphi - 1, (i90 + nphi - 1) // 2)):
        sg = max(sigmas, key=lambda g_: rmin[g_][imid])
        if min(rmin[sg][i0], rmin[sg][i1], rmin[sg][imid]) <= 1e-9:
            okt = False
            break
        tpl.append(sg)
    if okt:
        dirs = [L.u_deg(0), L.u_deg(30), L.u_deg(90), L.u_deg(120)]
        spec = [{'sigma': tpl[k], 'd1': dirs[k], 'd2': dirs[k + 1],
                 'w': vecs[tpl[k]]} for k in range(3)]
        got = try_arcs(tag, spec, gens, pre)
        if got is not None and not (isinstance(got, tuple)
                                    and got[0] == 'FAIL'):
            return got

    # pool of exact cut directions (constants preferred)
    pool_num = []
    for dv in cut_pool:
        is_par = bool(sp.Matrix(dv).free_symbols)
        pool_num.append((is_par, numeric_vec(dv), dv))
    pool_num.sort(key=lambda p: p[0])

    def val_at(sg, dvfn, idx):
        sv, tv = pre[idx]
        w = fns[sg](sv, tv)
        e = dvfn(sv, tv)
        e = e / np.hypot(*e)
        return (w @ e - Hc) / bestmin[idx]

    def min_margin_at(sg, dvfn):
        return min(val_at(sg, dvfn, idx) for idx in range(len(pre)))

    def cut_ok(sg1, sg2, dvfn):
        return (min_margin_at(sg1, dvfn) > 0.12
                and min_margin_at(sg2, dvfn) > 0.12)

    def cand_dirs(target):
        sv, tv = pre[len(pre) // 2]
        return sorted(pool_num, key=lambda p: (p[0], abs(
            (np.arctan2(*p[1](sv, tv)[::-1]) - target + np.pi)
            % (2 * np.pi) - np.pi)))

    # graph search: nodes = pool directions (plus u(0), u(120)) sorted by
    # angle; edge (d, d\') usable iff some selection has per-sample margin
    # > 0.12 at BOTH endpoints (the arc lemma needs nothing else).
    node_dirs = [L.u_deg(0)] + [dv for _, _, dv in pool_num] + [L.u_deg(120)]
    svm, tvm = pre[len(pre) // 2]
    ang = []
    for dv in node_dirs:
        f = numeric_vec(dv)
        e = f(svm, tvm)
        ang.append(np.arctan2(e[1], e[0]) % (2 * np.pi))
    order = sorted(range(len(node_dirs)),
                   key=lambda i: (ang[i], i not in (0, len(node_dirs) - 1)))
    # keep only nodes with angles in [0, 120deg]
    keep = [i for i in order if ang[i] <= 2 * np.pi / 3 + 1e-9]
    if 0 not in keep:
        keep = [0] + keep
    if len(node_dirs) - 1 not in keep:
        keep.append(len(node_dirs) - 1)
    nodes = [node_dirs[i] for i in keep]
    angs = [ang[i] for i in keep]
    nfn = [numeric_vec(dv) for dv in nodes]
    # margins matrix M[sigma][node]
    M = {}
    for sg in sigmas:
        row = []
        for f in nfn:
            worst = 1e9
            for idx, (sv, tv) in enumerate(pre):
                e = f(sv, tv)
                e = e / np.hypot(*e)
                w = fns[sg](sv, tv)
                worst = min(worst, (w @ e - Hc) / bestmin[idx])
                if worst <= 0.12:
                    break
            row.append(worst)
        M[sg] = row
    nN = len(nodes)
    # polynomial degree of each node direction (penalize heavy cuts)
    ndeg = []
    for dv in nodes:
        e = sp.expand(dv[0].subs(R3, 2) + dv[1].subs(R3, 2))
        ndeg.append(sp.total_degree(e, s, t) if e.free_symbols else 0)
    src_i = next(i for i, dv in enumerate(nodes)
                 if dv == L.u_deg(0) or (abs(angs[i]) < 1e-12))
    dst_i = max(range(nN), key=lambda i: angs[i])
    import heapq
    banned = set()
    for _attempt in range(5):
        INF = 10 ** 9
        dist = [INF] * nN
        prev = [None] * nN
        dist[src_i] = 0
        hq = [(0, src_i)]
        while hq:
            dcur, i = heapq.heappop(hq)
            if dcur > dist[i]:
                continue
            if i == dst_i:
                break
            for j2 in range(nN):
                if j2 in banned:
                    continue
                if (angs[j2] <= angs[i] + 1e-12
                        or angs[j2] - angs[i] > np.pi):
                    continue
                bests = max(sigmas, key=lambda sg: min(M[sg][i],
                                                       M[sg][j2]))
                if min(M[bests][i], M[bests][j2]) <= 0.12:
                    continue
                w2 = dcur + 100 + ndeg[j2]
                if w2 < dist[j2]:
                    dist[j2] = w2
                    prev[j2] = (i, bests)
                    heapq.heappush(hq, (w2, j2))
        if dist[dst_i] >= INF:
            raise RuntimeError(f'{tag}: INFEASIBLE-ROBUST (no arc path)')
        path = []
        i = dst_i
        while prev[i] is not None:
            pi, sg = prev[i]
            path.append((pi, i, sg))
            i = pi
        path.reverse()
        spec = [{'sigma': sg, 'd1': nodes[i1], 'd2': nodes[i2],
                 'w': vecs[sg]} for (i1, i2, sg) in path]
        got = try_arcs(tag, spec, gens, pre)
        if got is not None and not (isinstance(got, tuple)
                                    and got[0] == 'FAIL'):
            return got
        if isinstance(got, tuple):
            kf = got[1]
            i1, i2, _ = path[kf]
            for cand in (i1, i2):
                if cand not in (src_i, dst_i):
                    banned.add(cand)
            if not banned:
                break
        else:
            break
    raise RuntimeError(f'{tag}: arc certification failed')


def _samples_for_interval(pre, slo, shi):
    out = [(sv, tv) for (sv, tv) in pre if slo <= sv <= shi]
    for spf in (float(slo), float(shi)):
        if spf <= 0:
            continue
        qq = 1 - spf
        tmaxs = (-qq + np.sqrt(4 - 3 * qq * qq)) / 2
        out += [(spf, spf + (tmaxs - spf) * lam)
                for lam in (1e-6, 0.3, 0.6, 0.9)]
    return out


def validity_selection_split(tag, xloc, j, gens, pre, cut_pool,
                             s_range=None, depth=0):
    """selection certificate; on robust infeasibility (the needed
    selection swaps within the region), bisect the s-interval (depth<=3)
    and certify each piece with the interval constraints added."""
    if s_range is None:
        import math
        svals = [sv for sv, tv in pre]
        hi = sp.Rational(math.ceil(max(svals) * 256), 256)
        s_range = (sp.Integer(0), hi)
    slo, shi = s_range
    gcur = dict(gens)
    if slo > 0:
        gcur[f'sge{slo}'] = s - slo
    gcur[f'sle{shi}'] = shi - s
    pcur = _samples_for_interval(pre, float(slo), float(shi))
    try:
        arcs = validity_selection(tag + f'[{float(slo):.4f},'
                                  f'{float(shi):.4f}]', xloc, j, gcur,
                                  pcur, cut_pool)
        return {'kind': 'sel', 'slo': sp.srepr(slo), 'shi': sp.srepr(shi),
                'arcs': arcs}
    except RuntimeError as e:
        if 'INFEASIBLE-ROBUST' not in str(e) or depth >= 3:
            raise
    mid = (slo + shi) / 2
    lo = validity_selection_split(tag, xloc, j, gens, pre, cut_pool,
                                  (slo, mid), depth + 1)
    hi2 = validity_selection_split(tag, xloc, j, gens, pre, cut_pool,
                                   (mid, shi), depth + 1)
    return {'kind': 'sel-tree', 'mid': sp.srepr(mid), 'lo': lo, 'hi': hi2}


def combo_mul(c1, c2):
    """product of two positive combinations [(coeff, alpha)] -> one"""
    out = {}
    for a, al1 in c1:
        for b, al2 in c2:
            al = tuple(x + y for x, y in zip(al1, al2))
            out[al] = out.get(al, sp.Integer(0)) + a * b
    return [(sp.expand(c), al) for al, c in out.items() if c != 0]


def combo_scale(c1, lam):
    return [(sp.expand(lam * a), al) for a, al in c1]


def combo_add(*cs):
    out = {}
    for c1 in cs:
        for a, al in c1:
            out[al] = out.get(al, sp.Integer(0)) + a
    return [(sp.expand(c), al) for al, c in out.items() if c != 0]


def structured_disk_cert(tag, base, dcomb, mvec, j, center, gens, pre):
    """certificate for |(base + delta*mvec) - P|^2 - 1 >= 0 where
    delta = positive combination `dcomb` of the generators, by expanding
      q = q1 + 2 delta q2 + delta^2 |m|^2,   q1 = |base-P|^2 - 1,
      q2 = <base-P, mvec>,
    and certifying  q1 - c1 >= 0,  C + q2 >= 0,  D - delta >= 0,
    |m|^2 >= 0  (as a plain combination), with  c1 - 2 C D > 0."""
    P = pts_of_set(j)[center]
    v1 = sp.Matrix([base[0] - P[0], base[1] - P[1]])
    q1 = sp.expand(v1[0] ** 2 + v1[1] ** 2 - 1)
    q2 = sp.expand(v1[0] * mvec[0] + v1[1] * mvec[1])
    m2 = sp.expand(mvec[0] ** 2 + mvec[1] ** 2)
    f1 = sp.lambdify((s, t), q1, 'numpy')
    f2 = sp.lambdify((s, t), q2, 'numpy')
    gl = list(gens.values())
    dpoly = sp.expand(sum(c * sp.prod([gl[i] ** a for i, a in enumerate(al)])
                          for c, al in dcomb))
    fd = sp.lambdify((s, t), dpoly, 'numpy')
    from fractions import Fraction
    c1 = sp.Rational(Fraction(min(float(f1(a_, b_)) for a_, b_ in pre)
                              * 0.75).limit_denominator(64))
    C = sp.Rational(Fraction(max(0.0, -min(float(f2(a_, b_))
                                           for a_, b_ in pre)) * 1.5
                             + 0.1).limit_denominator(16))
    D = sp.Rational(Fraction(max(float(fd(a_, b_)) for a_, b_ in pre)
                             * 1.5 + 1e-4).limit_denominator(1024))
    if c1 <= 0 or c1 - 2 * C * D <= 0:
        raise RuntimeError(f'{tag}: structured-disk constants fail '
                           f'(c1={c1}, C={C}, D={D})')
    certs = {}
    for nm, expr in (('q1c', q1 - c1), ('Cq2', C + q2), ('Dd', D - dpoly),
                     ('m2', m2)):
        cert, dm, aux = G.certify_nonneg_auto(sp.expand(expr), gens,
                                              samples=pre)
        if cert is None or aux:
            raise RuntimeError(f'{tag}: structured piece {nm} failed')
        certs[nm] = cert
    width = max(len(al) for c, al in certs['q1c'])
    def pad(cc):
        return [(c, tuple(list(al) + [0] * (width - len(al))))
                for c, al in cc]
    one = [(sp.Integer(1), tuple([0] * width))]
    dc = pad(dcomb)
    # q - (c1 - 2 C D) = (q1 - c1) + 2 delta (C + q2) + delta^2 m^2
    #                    + 2 C (D - delta)
    total = combo_add(
        pad(certs['q1c']),
        combo_scale(combo_mul(dc, pad(certs['Cq2'])), 2),
        combo_mul(combo_mul(dc, dc), pad(certs['m2'])),
        combo_scale(pad(certs['Dd']), 2 * C),
        combo_scale(one, c1 - 2 * C * D))
    # exact identity check against q
    q = sp.expand((base[0] + dpoly * mvec[0] - P[0]) ** 2
                  + (base[1] + dpoly * mvec[1] - P[1]) ** 2 - 1)
    rec = sp.expand(sum(c * sp.prod([gl[i] ** a for i, a in enumerate(al)])
                        for c, al in total))
    if sp.expand(q - rec) != 0:
        raise RuntimeError(f'{tag}: structured-disk identity fails')
    item = {'poly': sp.srepr(q),
            'cert': [(sp.srepr(c), al) for c, al in total], 'degmax': -1}
    return {'center': center,
            'cert': {'num': item,
                     'den': {'poly': sp.srepr(sp.Integer(1)),
                             'cert': [(sp.srepr(sp.Integer(1)),
                                       tuple([0] * width))],
                             'degmax': 0}}}


def validity_disk(tag, xloc, j, center, gens, pre, structured=None):
    if structured is not None:
        return structured_disk_cert(tag, structured['base'],
                                    structured['dcomb'],
                                    structured['mvec'], j, center, gens,
                                    pre)
    pts = pts_of_set(j)
    P = pts[center]
    q = (xloc[0] - P[0]) ** 2 + (xloc[1] - P[1]) ** 2 - 1
    return {'center': center, 'cert': cert_ineq(tag + '/disk', q, gens, pre)}


# ----------------------------------------------------------------
# main
# ----------------------------------------------------------------
def main():
    data = {'S0': sp.srepr(G.S0), 'leaves': {}, 'witnesses': {},
            'fitting': {}, 'validity': {}}
    # shared region (zone C without the split) for witness-validity
    shared_gens = {k: v for k, v in G.leaf_gens('C-low').items()
                   if k != 'split'}
    pre_shared = leaf_samples('C-low') + leaf_samples('C-high')

    cut_pool = [L.u_deg(d) for d in (0, 30, 60, 90, 120)]
    for dd in (15, 45, 75, 105):
        cut_pool.append(rational_dir(dd))
    # parametric candidates around 30deg (the T2-critical zone):
    # linear tilts  u(30) - c*mu*u(120)  ~  u(30 - c*mu)   (unnormalized)
    u30, u120v = L.u_deg(30), L.u_deg(120)
    for mu in (s, t - s, t):
        for c in (sp.Rational(1, 2), 1, 2, 4):
            cut_pool.append(sp.Matrix(u30 - c * mu * u120v))
    # and around 90deg (window-tracking tilts need mixed s,t forms)
    u90, u180v = L.u_deg(90), sp.Matrix([-1, 0])
    for mu in (s, t, 2 * s - t / 2, s + t, 4 * s - 2 * t + t / 8):
        for c in (sp.Rational(1, 2), sp.Rational(3, 4), 1,
                  sp.Rational(7, 4), 2, 3):
            cut_pool.append(sp.Matrix(u90 - c * mu * u180v))
            cut_pool.append(sp.Matrix(u90 + c * mu * u180v))
    for mu in (2 * s - t / 2, s + t):
        for c in (1, 2):
            cut_pool.append(sp.Matrix(u30 - c * mu * u120v))
    # exact chord-normal cuts (track the feasibility window of each set):
    # local normals m = (sqrt3 a, a+2b) for the sliver (a,b)=(t,1-s) and
    # the petal (a,b)=(s,1-t); tilts scaled by the window width R0slack
    R02 = L.R0_sq()
    R0sl = sp.expand(1 - R02)
    Rp2 = sp.expand(s ** 2 + s * (1 - t) + (1 - t) ** 2)
    Rpsl = sp.expand(1 - Rp2)
    for (a_, b_, wid) in ((t, 1 - s, R0sl), (s, 1 - t, Rpsl)):
        m = sp.Matrix([sp.sqrt(3) * a_, a_ + 2 * b_])
        mperp = sp.Matrix([-m[1], m[0]])
        cut_pool.append(m)
        for c in (sp.Rational(1, 4), sp.Rational(1, 2), 1, 2, 4):
            cut_pool.append(sp.Matrix(m + c * wid * mperp))
            cut_pool.append(sp.Matrix(m - c * wid * mperp))

    # -------- witness-validity (leaf-dependent for Wst, shared otherwise)
    plan_shared = [
        ('W0', [(1, 'sel'), (0, 'sel')]
         + [(j, 'same-as-petal1') for j in (2, 3, 4, 5)]),
        ('WV0b', [(0, 'sel'), (1, 'sel'), (5, 'disk'), (2, 'disk'),
                  (3, 'disk'), (4, 'disk')]),
        ('WV5', [(5, 'sel'), (0, 'sel'), (4, 'sel'), (1, 'disk'),
                 (2, 'disk'), (3, 'disk')]),
    ]
    plan_leaf = [
        ('Wdip', [(0, 'sel'), (5, 'sel'), (1, 'disk'), (2, 'disk'),
                  (3, 'disk'), (4, 'disk')]),
        ('Wst1', [(1, 'sel'), (2, 'sel'), (3, 'sel'), (0, 'sel'),
                  (5, 'disk'), (4, 'disk')]),
        ('Wst3', [(3, 'same-as:Wst1:1'), (4, 'same-as:Wst1:2'),
                  (5, 'same-as:Wst1:3'), (2, 'sel'), (0, 'sel'),
                  (1, 'disk')]),
    ]

    Wlow = G.witnesses('C-low')
    Whigh = G.witnesses('C-high')
    Wext = G.witnesses('C-ext')
    for leaf, W in (('C-low', Wlow), ('C-high', Whigh), ('C-ext', Wext)):
        data['witnesses'][leaf] = {k: (sp.srepr(v[0]), sp.srepr(v[1]))
                                   for k, v in W.items()}

    Wext = G.witnesses('C-ext')
    print('== witness validity (shared) ==', flush=True)
    vshared = {}
    for wname, tasks in plan_shared:
        wit = Wlow[wname]          # shared formulas identical in both leaves
        assert sp.expand(wit[0] - Whigh[wname][0]) == 0
        vshared[wname] = {}
        for j, kind in tasks:
            tag = f'{wname}-vs-K{j}'
            if kind == 'same-as-petal1':
                vshared[wname][j] = {'kind': 'congruent-petal', 'ref': 1}
                continue
            xl = L.to_local(j, wit)
            xl = sp.Matrix([sp.cancel(sp.together(xl[0])),
                            sp.cancel(sp.together(xl[1]))])
            if kind == 'disk':
                done = False
                for c in ('O', 'A', 'B'):
                    try:
                        d = validity_disk(tag, xl, j, c, shared_gens,
                                          pre_shared)
                        vshared[wname][j] = {'kind': 'disk', **d}
                        done = True
                        break
                    except RuntimeError:
                        continue
                if not done:
                    raise RuntimeError(f'{tag}: no disk certificate')
            else:
                try:
                    vshared[wname][j] = validity_selection_split(
                        tag, xl, j, shared_gens, pre_shared, cut_pool)
                except RuntimeError as e:
                    print(f'  {tag}: *** FAILED: {str(e)[:150]}', flush=True)
                    FAILED.append(tag)
                    continue
            print(f'  {tag}: {vshared[wname][j]["kind"]} ok', flush=True)
    print('== hexagon membership (shared) ==', flush=True)
    hexs = {}
    for wname, _ in plan_shared:
        hexs[wname] = hexagon_certs(f'{wname}-hex', Wlow[wname],
                                    shared_gens, pre_shared)
        print(f'  {wname}: in-H ok', flush=True)
    data['validity']['shared'] = vshared
    data['hex_shared'] = hexs

    # shared-witness validity must also hold on the C-ext region
    ext_gens = G.leaf_gens('C-ext')
    pre_ext = leaf_samples('C-ext')
    vext_shared = {}
    for wname, tasks in plan_shared:
        wit = Wext[wname]
        vext_shared[wname] = {}
        for j, kind in tasks:
            tag = f'{wname}-vs-K{j}[ext]'
            if kind == 'same-as-petal1':
                vext_shared[wname][j] = {'kind': 'congruent-petal', 'ref': 1}
                continue
            xl = L.to_local(j, wit)
            xl = sp.Matrix([sp.cancel(sp.together(xl[0])),
                            sp.cancel(sp.together(xl[1]))])
            if kind == 'disk':
                done = False
                for c in ('O', 'A', 'B'):
                    try:
                        d = validity_disk(tag, xl, j, c, ext_gens, pre_ext)
                        vext_shared[wname][j] = {'kind': 'disk', **d}
                        done = True
                        break
                    except RuntimeError:
                        continue
                if not done:
                    raise RuntimeError(f'{tag}: no disk certificate')
            else:
                try:
                    vext_shared[wname][j] = validity_selection_split(
                        tag, xl, j, ext_gens, pre_ext, cut_pool)
                except RuntimeError as e:
                    print(f'  {tag}: *** FAILED: {str(e)[:150]}', flush=True)
                    FAILED.append(tag)
                    continue
            print(f'  {tag}: {vext_shared[wname][j]["kind"]} ok', flush=True)
    data['validity']['ext-shared'] = vext_shared
    data['hex_ext_shared'] = {
        wname: hexagon_certs(f'{wname}-hex[ext]', Wext[wname], ext_gens,
                             pre_ext) for wname, _ in plan_shared}

    for leaf in ('C-low', 'C-high', 'C-ext'):
        gens = G.leaf_gens(leaf)
        pre = leaf_samples(leaf)
        W = {'C-low': Wlow, 'C-high': Whigh, 'C-ext': Wext}[leaf]
        print(f'== witness validity ({leaf}) ==', flush=True)
        vleaf = {}
        for wname, tasks in plan_leaf:
            vleaf[wname] = {}
            for j, kind in tasks:
                tag = f'{wname}-vs-K{j}[{leaf}]'
                if isinstance(kind, str) and kind.startswith('same-as:'):
                    _, ref, jr = kind.split(':')
                    vleaf[wname][j] = {'kind': 'congruent-rot',
                                       'ref': ref, 'ref_j': int(jr)}
                    continue
                xl = L.to_local(j, W[wname])
                xl = sp.Matrix([sp.cancel(sp.together(xl[0])),
                                sp.cancel(sp.together(xl[1]))])
                if kind == 'disk':
                    structured = None
                    if wname == 'Wdip':
                        A0g, O0g, B0g = L.AOB_global(0)
                        midg = (A0g + B0g) / 2
                        mloc0 = sp.Matrix([R3 * t, t + 2 * (1 - s)])
                        mg = sp.Matrix([
                            mloc0[0] * L.EX[0][0] + mloc0[1] * L.EY[0][0],
                            mloc0[0] * L.EX[0][1] + mloc0[1] * L.EY[0][1]])
                        basej = L.to_local(j, midg)
                        mj = sp.Matrix([mg[0] * L.EX[j][0]
                                        + mg[1] * L.EX[j][1],
                                        mg[0] * L.EY[j][0]
                                        + mg[1] * L.EY[j][1]])
                        gn = list(gens.keys())
                        wd_ = len(gn)
                        aR = [0] * wd_
                        aR[gn.index('R0slack')] = 1
                        aS = [0] * wd_
                        aS[gn.index('s')] = 2
                        structured = {
                            'base': sp.Matrix([sp.expand(basej[0]),
                                               sp.expand(basej[1])]),
                            'mvec': sp.Matrix([sp.expand(mj[0]),
                                               sp.expand(mj[1])]),
                            'dcomb': [(sp.Rational(4, 15), tuple(aR)),
                                      (sp.Rational(1, 16), tuple(aS))]}
                    done = False
                    for c in ('O', 'A', 'B'):
                        try:
                            d = validity_disk(tag, xl, j, c, gens, pre,
                                              structured=structured)
                            vleaf[wname][j] = {'kind': 'disk', **d}
                            done = True
                            break
                        except RuntimeError:
                            continue
                    if not done:
                        raise RuntimeError(f'{tag}: no disk certificate')
                else:
                    try:
                        vleaf[wname][j] = validity_selection_split(
                            tag, xl, j, gens, pre, cut_pool)
                    except RuntimeError as e:
                        print(f'  {tag}: *** FAILED: {str(e)[:150]}',
                              flush=True)
                        FAILED.append(tag)
                        continue
                print(f'  {tag}: {vleaf[wname][j]["kind"]} ok', flush=True)
        data['validity'][leaf] = vleaf
        data.setdefault('hex_leaf', {})[leaf] = {
            wname: hexagon_certs(f'{wname}-hex[{leaf}]', W[wname], gens, pre)
            for wname, _ in plan_leaf}
        print(f'  Wst in-H [{leaf}] ok', flush=True)

        # -------- fitting arcs
        print(f'== fitting ({leaf}) ==', flush=True)
        cuts = G.cut_dirs(leaf)
        fit = []
        for nm, d1k, d2k, triple in G.FITTING_ARCS:
            d1, d2 = cuts[d1k], cuts[d2k]
            w = L.selection_vector([W[triple[0]], W[triple[1]],
                                    W[triple[2]]])
            tag = f'fit-{nm}[{leaf}]'
            try:
                ac = arc_cert(tag, d1, d2, gens, pre)
                e1 = endpoint_certs(tag + '/d1', w, d1, gens, pre)
                e2 = endpoint_certs(tag + '/d2', w, d2, gens, pre)
            except RuntimeError as e:
                print(f'  {tag}: *** FAILED: {str(e)[:150]}', flush=True)
                FAILED.append(tag)
                continue
            fit.append({'name': nm, 'triple': triple,
                        'd1': (sp.srepr(d1[0]), sp.srepr(d1[1])),
                        'd2': (sp.srepr(d2[0]), sp.srepr(d2[1])),
                        'cross': ac, 'end1': e1, 'end2': e2})
            print(f'  {tag}: ok', flush=True)
        data['fitting'][leaf] = fit
        data['leaves'][leaf] = {k: sp.srepr(sp.expand(v))
                                for k, v in gens.items()}
    data['shared_gens'] = {k: sp.srepr(sp.expand(v))
                           for k, v in shared_gens.items()}

    with open('hole_certificates_corner.py', 'w') as f:
        f.write('# generated by gen_corner.py — exact certificate data\n')
        f.write('DATA = ' + repr(data) + '\n')
    print('written hole_certificates_corner.py')
    if FAILED:
        print(f'*** {len(FAILED)} INCOMPLETE ITEMS: {FAILED}')
        raise SystemExit(2)


if __name__ == '__main__':
    main()
