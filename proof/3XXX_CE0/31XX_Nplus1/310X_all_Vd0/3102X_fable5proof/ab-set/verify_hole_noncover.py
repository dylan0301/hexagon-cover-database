r"""Standalone exact verifier for the hole-set non-coverability proof.

Re-checks, from scratch and exactly over Q(sqrt3):
  * region/tree coverage (corner leaves + bulk box tiling + disjointness),
  * every witness: in the hexagon and outside all six sets
    (disk / cone / selection-arc certificates, Lemmas 3.1-3.3 of
    hole_set_noncover.md),
  * every fitting arc: chaining over the phi-period, arc < 180 deg,
    endpoint inequalities > h with strictness terms,
  * every Handelman-style positivity certificate: literal expansion and
    exact coefficient signs.

The certificate files are treated as UNTRUSTED: all polynomials are
re-derived from the stored witness/cut/selection definitions; only the
certificate coefficients are taken from the data (and then verified).

Usage:  python3 verify_hole_noncover.py [--numeric]
"""
import sys
import itertools
import sympy as sp

import hole_cert_lib as L

s, t = L.s, L.t
R3, H = L.R3, L.H
NAMES = 'AOBx'

FAIL = []


def check(cond, msg):
    if not cond:
        FAIL.append(msg)
        print('  FAIL:', msg)
    return cond


def q3_parts(e):
    e = sp.expand(e)
    rat = e.subs(R3, 0)
    return rat, sp.expand((e - rat) / R3)


def exact_sign_q3num(c):
    """sign of an exact number p + q sqrt3"""
    c = sp.expand(c)
    p, q = q3_parts(c)
    p, q = sp.Rational(p), sp.Rational(q)
    if p == 0 and q == 0:
        return 0
    if p >= 0 and q >= 0:
        return 1
    if p <= 0 and q <= 0:
        return -1
    if p > 0:
        return 1 if p ** 2 > 3 * q ** 2 else (-1 if p ** 2 < 3 * q ** 2
                                              else 0)
    return -1 if p ** 2 > 3 * q ** 2 else (1 if p ** 2 < 3 * q ** 2 else 0)


def parse(v):
    return sp.sympify(v)


def parse_vec(v):
    return sp.Matrix([parse(v[0]), parse(v[1])])


# ----------------------------------------------------------------
# certificate checking
# ----------------------------------------------------------------
def check_handelman(item, gens_list, tag, need_strict=False,
                    strict_ok_idx=None):
    """item = {'poly': srepr, 'cert': [(coeff-srepr, alpha), ...],
    optional 'aux_sq': [linear-root sreprs]}.  Verifies
    poly == sum c_a g^a (over region generators extended by the
    aux squares, each globally nonnegative) with all c_a >= 0 (exact).
    If need_strict: some term with c_a > 0 and alpha supported on
    strict_ok_idx (or the constant term)."""
    poly = parse(item['poly'])
    glist = list(gens_list)
    if 'aux_sq' in item:
        for lr in item['aux_sq']:
            l = parse(lr)
            glist.append(sp.expand(l ** 2))   # a perfect square: >= 0
    tot = sp.Integer(0)
    strict_found = False
    for cs, alpha in item['cert']:
        c = parse(cs)
        if not check(exact_sign_q3num(c) >= 0,
                     f'{tag}: negative certificate coefficient'):
            return None
        term = c
        for i, a in enumerate(alpha):
            if a:
                if not check(i < len(glist), f'{tag}: alpha out of range'):
                    return None
                term = term * glist[i] ** a
        tot = tot + term
        if exact_sign_q3num(c) > 0 and all(
                (a == 0 or (strict_ok_idx and i in strict_ok_idx))
                for i, a in enumerate(alpha)):
            strict_found = True
    if not check(sp.expand(poly - tot) == 0,
                 f'{tag}: certificate identity fails'):
        return None
    if need_strict:
        check(strict_found, f'{tag}: no strictness term')
    return poly


def check_ineq(cert, expr, gens_list, tag, need_strict=False,
               strict_ok_idx=None):
    """cert = {'num': item, 'den': item}: verifies that expr >= 0 (with
    strictness on the open region if requested) using the stored
    numerator/denominator certificates.  The polynomials are re-derived
    from expr and matched against the stored ones by cross-multiplication."""
    e = sp.cancel(sp.together(sp.expand(expr)))
    n_re, d_re = sp.fraction(e)
    n_st = parse(cert['num']['poly'])
    d_st = parse(cert['den']['poly'])
    # stored pair must represent the same rational function
    if not check(sp.expand(n_re * d_st - n_st * d_re) == 0,
                 f'{tag}: stored num/den do not match the re-derived '
                 f'expression'):
        return False
    ok = True
    ok &= check_handelman(cert['num'], gens_list, tag + '/num',
                          need_strict=need_strict,
                          strict_ok_idx=strict_ok_idx) is not None
    # denominator must be strictly positive on the open region {s>0, g>0};
    # generators are ordered with 's' at index 0 and 'g' at index 1 in
    # every leaf (checked in verify_corner), so {0,1}-supported terms and
    # constants witness strictness.
    ok &= check_handelman(cert['den'], gens_list, tag + '/den',
                          need_strict=True,
                          strict_ok_idx={0, 1}) is not None
    return ok


def sel_points(a, b, xloc):
    return {'A': sp.Matrix([-a / 2, R3 * a / 2]), 'O': sp.Matrix([0, 0]),
            'B': sp.Matrix([b, 0]), 'x': xloc}


def sel_w(a, b, xloc, sigma):
    pts = sel_points(a, b, xloc)
    return L.selection_vector([pts[c] for c in sigma])


def check_sel_arcs(arcs, gens2, tag, a, b, xloc, strict_idx):
    check_arcchain(arcs, tag, lambda A, kk: parse_vec(A[kk]))
    for kk, arc in enumerate(arcs):
        w_sel = sel_w(a, b, xloc, arc['sigma'])
        d1 = parse_vec(arc['d1'])
        d2 = parse_vec(arc['d2'])
        cr = d1[0] * d2[1] - d1[1] * d2[0]
        check_ineq(arc['cross'], cr, gens2, f'{tag}/arc{kk}/cross')
        for dd, ek in ((d1, 'end1'), (d2, 'end2')):
            lin = w_sel[0] * dd[0] + w_sel[1] * dd[1]
            quad = lin ** 2 - H ** 2 * (dd[0] ** 2 + dd[1] ** 2)
            check_ineq(arc[ek]['lin'], lin, gens2,
                       f'{tag}/arc{kk}/{ek}/lin')
            check_ineq(arc[ek]['quad'], quad, gens2,
                       f'{tag}/arc{kk}/{ek}/quad', need_strict=True,
                       strict_ok_idx=strict_idx)


def check_sel_node(item, base_gens, tag, a, b, xloc, strict_idx):
    """recursive checker for sel / sel-tree; returns the covered
    s-interval (slo, shi) or None on failure"""
    if item['kind'] == 'sel-tree':
        mid = parse(item['mid'])
        lo = check_sel_node(item['lo'], base_gens, tag + '/lo', a, b,
                            xloc, strict_idx)
        hi = check_sel_node(item['hi'], base_gens, tag + '/hi', a, b,
                            xloc, strict_idx)
        if lo is None or hi is None:
            return None
        check(lo[1] >= mid and hi[0] <= mid,
              f'{tag}: tree pieces do not meet at the split')
        return (lo[0], hi[1])
    slo, shi = parse(item['slo']), parse(item['shi'])
    gens2 = list(base_gens) + [shi - s]
    if slo > 0:
        gens2.append(s - slo)
    check_sel_arcs(item['arcs'], gens2, tag, a, b, xloc, strict_idx)
    return (slo, shi)


def check_arcchain(arcs, tag, get_d):
    """arcs cover [u(0), u(120)] consecutively"""
    ok = True
    d_first = get_d(arcs[0], 'd1')
    d_last = get_d(arcs[-1], 'd2')
    ok &= check(sp.expand(d_first[0] - 1) == 0 and
                sp.expand(d_first[1]) == 0, f'{tag}: chain start != u(0)')
    u120 = L.u_deg(120)
    ok &= check(sp.expand(d_last[0] - u120[0]) == 0 and
                sp.expand(d_last[1] - u120[1]) == 0,
                f'{tag}: chain end != u(120)')
    for k in range(len(arcs) - 1):
        a, bnext = get_d(arcs[k], 'd2'), get_d(arcs[k + 1], 'd1')
        ok &= check(sp.expand(a[0] - bnext[0]) == 0 and
                    sp.expand(a[1] - bnext[1]) == 0,
                    f'{tag}: chain break at arc {k}')
    return ok


# ----------------------------------------------------------------
# corner-zone verification
# ----------------------------------------------------------------
def verify_corner():
    from hole_certificates_corner import DATA
    print('== corner zone ==')
    S0 = parse(DATA['S0'])
    check(S0 == sp.Rational(1, 32), 'S0 mismatch')

    # region generator soundness
    R02 = sp.expand(t ** 2 + t * (1 - s) + (1 - s) ** 2)
    LEAVES = ('C-low', 'C-high', 'C-ext')
    for leaf in LEAVES:
        gd = {k: parse(v) for k, v in DATA['leaves'][leaf].items()}
        check(sp.expand(gd['s'] - s) == 0, f'{leaf}: gen s')
        check(sp.expand(gd['g'] - (t - s)) == 0, f'{leaf}: gen g')
        check(sp.expand(gd['R0slack'] - (1 - R02)) == 0,
              f'{leaf}: gen R0slack')
        check(sp.expand(gd['dg'] - (2 * s - t)) == 0, f'{leaf}: gen dg')
        # dg >= 0 derivation: 2s - t = (1-R0^2) + (s - t/2)^2 + (3/4) t^2
        check(sp.expand((2 * s - t) - ((1 - R02) + (s - t / 2) ** 2
                                       + sp.Rational(3, 4) * t ** 2)) == 0,
              f'{leaf}: dg derivation identity')
        if leaf == 'C-ext':
            check(sp.expand(gd['sfloor'] - (s - S0)) == 0,
                  f'{leaf}: gen sfloor')
            check(sp.expand(gd['scap'] - (sp.Rational(1, 16) - s)) == 0,
                  f'{leaf}: gen scap')
            check(sp.expand(gd['wedge']
                            - (sp.Rational(5, 4) * s - t)) == 0,
                  f'{leaf}: gen wedge')
        else:
            check(sp.expand(gd['scap'] - (S0 - s)) == 0,
                  f'{leaf}: gen scap')
            spl = parse(DATA['leaves'][leaf]['split'])
            want = 8 * s - 5 * t if leaf == 'C-low' else 5 * t - 8 * s
            check(sp.expand(spl - want) == 0, f'{leaf}: split gen')
    # the two zone-C splits are complementary; C-ext covers the bulk wedge
    check(sp.expand((8 * s - 5 * t) + (5 * t - 8 * s)) == 0,
          'leaf split complementarity')

    shared_gd = {k: parse(v) for k, v in DATA['shared_gens'].items()}
    shared_list = list(shared_gd.values())
    shared_names = list(shared_gd.keys())
    shared_strict = {shared_names.index('s'), shared_names.index('g')}
    check(shared_names[0] == 's' and shared_names[1] == 'g',
          'shared generator ordering (s, g first)')
    for leaf in LEAVES:
        ln = list(DATA['leaves'][leaf].keys())
        check(ln[0] == 's' and ln[1] == 'g',
              f'{leaf}: generator ordering (s, g first)')

    # witnesses per leaf
    Wit = {leaf: {k: parse_vec(v) for k, v in DATA['witnesses'][leaf].items()}
           for leaf in LEAVES}
    # Wst3 = rot120(Wst1)
    for leaf in LEAVES:
        w3 = L.rot120(Wit[leaf]['Wst1'], 1)
        check(sp.expand(sp.together(Wit[leaf]['Wst3'][0] - w3[0])) == 0
              and sp.expand(sp.together(Wit[leaf]['Wst3'][1] - w3[1])) == 0,
              f'{leaf}: Wst3 != rot120(Wst1)')
    # shared witnesses coincide across leaves
    for k in ('W0', 'WV0b', 'WV5'):
        for leafb in ('C-high', 'C-ext'):
            for c in range(2):
                check(sp.expand(sp.together(Wit['C-low'][k][c]
                                            - Wit[leafb][k][c])) == 0,
                      f'shared witness {k} differs between leaves')

    # hexagon membership (shared witnesses on the shared region)
    for wname, certs in DATA['hex_shared'].items():
        w = Wit['C-low'][wname]
        for k in range(6):
            n = L.u_deg((30 + 60 * k) % 360)
            expr = H - (w[0] * n[0] + w[1] * n[1])
            check_ineq(certs[k], expr, shared_list,
                       f'hex/{wname}/{k}')
    if 'hex_ext_shared' in DATA:
        egd = {k: parse(v) for k, v in DATA['leaves']['C-ext'].items()}
        for wname, certs in DATA['hex_ext_shared'].items():
            w = Wit['C-ext'][wname]
            for k in range(6):
                n = L.u_deg((30 + 60 * k) % 360)
                expr = H - (w[0] * n[0] + w[1] * n[1])
                check_ineq(certs[k], expr, list(egd.values()),
                           f'hex-ext/{wname}/{k}')
    for leaf in LEAVES:
        gd = {k: parse(v) for k, v in DATA['leaves'][leaf].items()}
        glist, gnames = list(gd.values()), list(gd.keys())
        for wname, certs in DATA['hex_leaf'][leaf].items():
            w = Wit[leaf][wname]
            for k in range(6):
                n = L.u_deg((30 + 60 * k) % 360)
                expr = H - (w[0] * n[0] + w[1] * n[1])
                check_ineq(certs[k], expr, glist,
                           f'hex/{wname}[{leaf}]/{k}')

    # witness validity
    def check_validity(vd, W, gens_list, gnames, tag, leaf_wits,
                       max_s=sp.Rational(1, 32)):
        strict_idx = {gnames.index('s'), gnames.index('g')}
        for wname, per_set in vd.items():
            for j_str, item in per_set.items():
                j = int(j_str)
                tagj = f'{tag}/{wname}-vs-K{j}'
                kind = item['kind']
                if kind == 'congruent-petal':
                    jr = item['ref']
                    xl_j = L.to_local(j, leaf_wits[wname])
                    xl_r = L.to_local(jr, leaf_wits[wname])
                    check(sp.expand(sp.together(xl_j[0] - xl_r[0])) == 0 and
                          sp.expand(sp.together(xl_j[1] - xl_r[1])) == 0,
                          f'{tagj}: congruence local coords differ')
                    check(L.ab_of(j) == L.ab_of(jr),
                          f'{tagj}: congruence params differ')
                    continue
                if kind == 'congruent-rot':
                    ref, jr = item['ref'], item['ref_j']
                    xl_j = L.to_local(j, leaf_wits[wname])
                    xl_r = L.to_local(jr, leaf_wits[ref])
                    check(sp.expand(sp.together(xl_j[0] - xl_r[0])) == 0 and
                          sp.expand(sp.together(xl_j[1] - xl_r[1])) == 0,
                          f'{tagj}: rot-congruence local coords differ')
                    check(L.ab_of(j) == L.ab_of(jr),
                          f'{tagj}: rot-congruence params differ')
                    continue
                a, b = L.ab_of(j)
                xloc = L.to_local(j, leaf_wits[wname])
                if kind == 'disk':
                    P = sel_points(a, b, xloc)[item['center']]
                    expr = ((xloc[0] - P[0]) ** 2 + (xloc[1] - P[1]) ** 2
                            - 1)
                    check_ineq(item['cert'], expr, gens_list, tagj + '/disk',
                               need_strict=True, strict_ok_idx=strict_idx)
                elif kind in ('sel', 'sel-tree'):
                    lohi = check_sel_node(item, gens_list, tagj, a, b,
                                          xloc, strict_idx)
                    if lohi is not None:
                        slo_r, shi_r = lohi
                        check(slo_r <= 0 and shi_r >= max_s,
                              f'{tagj}: selection s-intervals do not '
                              f'cover [0, {max_s}]')
                else:
                    check(False, f'{tagj}: unknown kind {kind}')

    check_validity(DATA['validity']['shared'], None, shared_list,
                   shared_names, 'shared', Wit['C-low'],
                   max_s=sp.Rational(1, 32))
    # shared witnesses appear identically in all leaves (checked above);
    # the ext-shared certificates cover the C-ext region.
    egd = {k: parse(v) for k, v in DATA['leaves']['C-ext'].items()}
    check_validity(DATA['validity']['ext-shared'], None,
                   list(egd.values()), list(egd.keys()), 'ext-shared',
                   Wit['C-ext'], max_s=sp.Rational(1, 16))
    for leaf in LEAVES:
        gd = {k: parse(v) for k, v in DATA['leaves'][leaf].items()}
        check_validity(DATA['validity'][leaf], None, list(gd.values()),
                       list(gd.keys()), leaf, Wit[leaf],
                       max_s=sp.Rational(1, 16) if leaf == 'C-ext'
                       else sp.Rational(1, 32))

    # completeness: every witness used in a fitting triple must have a
    # validity record against all six sets (shared or leaf-specific), plus
    # a hexagon-membership certificate
    for leaf in LEAVES:
        used = set()
        for arc in DATA['fitting'][leaf]:
            used.update(arc['triple'])
        shared_v = DATA['validity']['shared']
        ext_v = DATA['validity'].get('ext-shared', {})
        leaf_v = DATA['validity'][leaf]
        hexnames = (set(DATA['hex_shared'].keys())
                    | set(DATA.get('hex_ext_shared', {}).keys())
                    | set(DATA['hex_leaf'][leaf].keys()))
        for wname in used:
            check(wname in hexnames,
                  f'{leaf}: witness {wname} lacks hexagon certificate')
            if leaf == 'C-ext':
                pools = [leaf_v.get(wname, {}), ext_v.get(wname, {})]
            else:
                pools = [leaf_v.get(wname, {}), shared_v.get(wname, {})]
            for j in range(6):
                have = any(j in p or str(j) in p for p in pools)
                check(have, f'{leaf}: witness {wname} lacks validity '
                            f'record vs K{j}')

    # fitting arcs
    for leaf in LEAVES:
        gd = {k: parse(v) for k, v in DATA['leaves'][leaf].items()}
        glist, gnames = list(gd.values()), list(gd.keys())
        strict_idx = {gnames.index('s'), gnames.index('g')}
        arcs = DATA['fitting'][leaf]
        check_arcchain(arcs, f'fitting[{leaf}]',
                       lambda A, kk: parse_vec(A[kk]))
        for arc in arcs:
            tr = arc['triple']
            w = L.selection_vector([Wit[leaf][tr[0]], Wit[leaf][tr[1]],
                                    Wit[leaf][tr[2]]])
            d1, d2 = parse_vec(arc['d1']), parse_vec(arc['d2'])
            tagA = f'fitting[{leaf}]/{arc["name"]}'
            cr = d1[0] * d2[1] - d1[1] * d2[0]
            check_ineq(arc['cross'], cr, glist, tagA + '/cross')
            for dd, ek in ((d1, 'end1'), (d2, 'end2')):
                lin = w[0] * dd[0] + w[1] * dd[1]
                quad = lin ** 2 - H ** 2 * (dd[0] ** 2 + dd[1] ** 2)
                check_ineq(arc[ek]['lin'], lin, glist, tagA + f'/{ek}/lin')
                check_ineq(arc[ek]['quad'], quad, glist,
                           tagA + f'/{ek}/quad', need_strict=True,
                           strict_ok_idx=strict_idx)
    print(f'  corner zone: {"OK" if not FAIL else "FAILURES"}')


# ----------------------------------------------------------------
# bulk verification
# ----------------------------------------------------------------
def verify_bulk():
    from hole_certificates_bulk import DATA
    print('== bulk zone ==')
    roots = [[parse(v) for v in r] for r in DATA['roots']]
    boxes = DATA['boxes']
    # tiling: disjoint interiors + total area (per root union)
    area = sp.Integer(0)
    rects = []
    for bx in boxes:
        s1, s2, t1, t2 = [parse(v) for v in bx['box']]
        check(s1 < s2 and t1 < t2, 'degenerate box')
        check(any(r[0] <= s1 and s2 <= r[1] and r[2] <= t1 and t2 <= r[3]
                  for r in roots), 'box outside all roots')
        rects.append((s1, s2, t1, t2))
        area += (s2 - s1) * (t2 - t1)
    total = sum((r[1] - r[0]) * (r[3] - r[2]) for r in roots)
    check(area == total, 'box areas do not tile the roots')
    # roots cover the bulk s-range [1/32, 1/2]:
    check(roots[0][0] == sp.Rational(1, 32) and roots[0][1] == roots[1][0]
          and roots[1][1] == sp.Rational(1, 2), 'root s-ranges')
    # root-1 t-floor 1/32 <= s on its s-range; root-2 t-floor 1/16 <= s ok
    check(roots[0][2] <= sp.Rational(1, 32)
          and roots[1][2] <= sp.Rational(1, 16), 'root t-floors')
    for i in range(len(rects)):
        for j in range(i + 1, len(rects)):
            a, b = rects[i], rects[j]
            overlap = (min(a[1], b[1]) > max(a[0], b[0])
                       and min(a[3], b[3]) > max(a[2], b[2]))
            if overlap:
                check(False, f'boxes {i},{j} overlap')
    # root covers the bulk region {1/32<=s, s<=t<=min(tmax,1-s), s+t<=1}:
    #   s ranges in [1/32, 1/2] (s<=t & s+t<=1 => s<=1/2 <= root),
    #   t <= 1-s <= 1-1/32 <= 2/3?  1-1/32 = 31/32 > 2/3 — the root's
    #   t-cap 2/3 is justified by t <= tmax(s) <= tmax(1/2) < 2/3:
    tmax_half_ok = sp.expand((sp.Rational(2, 3)) ** 2
                             + sp.Rational(2, 3) * sp.Rational(1, 2)
                             + sp.Rational(1, 4) - 1)
    check(exact_sign_q3num(tmax_half_ok) > 0,
          'root t-cap: R0^2(1/2, 2/3) > 1 must hold')
    # (R0^2 decreasing in s: for s <= 1/2, tmax(s) <= tmax(1/2) < 2/3.)

    for bi, bx in enumerate(boxes):
        s1, s2, t1, t2 = [parse(v) for v in bx['box']]
        tag = f'box{bi}'
        if bx['kind'] == 'disjoint':
            why = bx['why']
            if why == 'below-diagonal':
                check(t2 <= s1, f'{tag}: below-diagonal fails')
            elif why == 'above-half':
                check(t1 >= 1 - s1, f'{tag}: above-half fails')
            elif why == 'above-R0':
                v = sp.expand(t1 ** 2 + t1 * (1 - s2) + (1 - s2) ** 2 - 1)
                check(exact_sign_q3num(v) >= 0, f'{tag}: above-R0 fails')
            elif why == 'wedge':
                check(s2 <= sp.Rational(1, 16)
                      and t2 <= sp.Rational(5, 4) * s1,
                      f'{tag}: wedge reason fails (covered by C-ext)')
            else:
                check(False, f'{tag}: unknown disjoint reason')
            continue
        # certified box
        t2e = parse(bx['t2e'])
        cap = min(t2, 1 - s1)
        if t2e != cap:
            v = sp.expand(t2e ** 2 + t2e * (1 - s2) + (1 - s2) ** 2 - 1)
            check(exact_sign_q3num(v) >= 0,
                  f'{tag}: t2e fact fails (neither cap nor R0-bound)')
        sets = [(parse(x[0]), parse(x[1])) for x in bx['sets']]
        t1e = parse(bx['t1e'])
        if t1e != t1:
            # raised floor is only legitimate under the C-ext wedge
            check(s2 <= sp.Rational(1, 16)
                  and t1e == sp.Rational(5, 4) * s1,
                  f'{tag}: t1e fact fails')
        check(sets[0] == (t1e, 1 - s2), f'{tag}: sliver superset params')
        for j in range(1, 6):
            check(sets[j] == (s1, 1 - t2e), f'{tag}: petal superset params')
        wit = {k: (parse(v[0]), parse(v[1]))
               for k, v in bx['witnesses'].items()}
        for k, (wx, wy) in wit.items():
            for kk in range(6):
                n = L.u_deg((30 + 60 * kk) % 360)
                check(exact_sign_q3num(H - (wx * n[0] + wy * n[1])) >= 0,
                      f'{tag}/{k}: outside hexagon')
        for k, per_set in bx['validity'].items():
            wx = sp.Matrix([wit[k][0], wit[k][1]])
            for j_str, item in per_set.items():
                j = int(j_str)
                a, b = sets[j]
                xloc = L.to_local(j, wx)
                tagj = f'{tag}/{k}-vs-{j}'
                if item['kind'] == 'cone':
                    v = parse(item['value'])
                    want = (-xloc[1] if item['side'] == 'B'
                            else -(R3 * xloc[0] + xloc[1]))
                    check(sp.expand(v - want) == 0,
                          f'{tagj}: cone value mismatch')
                    check(exact_sign_q3num(v) > 0, f'{tagj}: cone fails')
                elif item['kind'] == 'disk':
                    P = sel_points(a, b, xloc)[item['center']]
                    v = sp.expand((xloc[0] - P[0]) ** 2
                                  + (xloc[1] - P[1]) ** 2 - 1)
                    check(sp.expand(v - parse(item['value'])) == 0,
                          f'{tagj}: disk value mismatch')
                    check(exact_sign_q3num(v) > 0, f'{tagj}: disk fails')
                elif item['kind'] == 'sel':
                    arcs = item['arcs']
                    check_arcchain(arcs, tagj,
                                   lambda A, kk: parse_vec(A[kk]))
                    for arc in arcs:
                        w_sel = sel_w(a, b, xloc, arc['sigma'])
                        d1 = parse_vec(arc['d1'])
                        d2 = parse_vec(arc['d2'])
                        check(exact_sign_q3num(d1[0] * d2[1]
                                               - d1[1] * d2[0]) > 0,
                              f'{tagj}: arc not <180')
                        for dd in (d1, d2):
                            lin = sp.expand(w_sel[0] * dd[0]
                                            + w_sel[1] * dd[1])
                            quad = sp.expand(lin ** 2 - H ** 2
                                             * (dd[0] ** 2 + dd[1] ** 2))
                            check(exact_sign_q3num(lin) >= 0
                                  and exact_sign_q3num(quad) > 0,
                                  f'{tagj}: endpoint fails')
                elif item['kind'] == 'sel-param':
                    # parametric non-membership vs K(t,1-s) at V_0 on the
                    # feasible part of the box (diagonal-adjacent boxes)
                    check(j == 0, f'{tagj}: sel-param only for K_0')
                    gd2 = {k2: parse(v2)
                           for k2, v2 in item['gens'].items()}
                    check(sp.expand(gd2['s'] - (s - s1)) == 0
                          and sp.expand(gd2['g'] - (t - s)) == 0
                          and sp.expand(gd2['shi'] - (s2 - s)) == 0
                          and sp.expand(gd2['tlo'] - (t - t1)) == 0
                          and sp.expand(gd2['thi'] - (t2 - t)) == 0,
                          f'{tagj}: sel-param gens mismatch')
                    R02b = sp.expand(t ** 2 + t * (1 - s) + (1 - s) ** 2)
                    check(sp.expand(gd2['R0slack'] - (1 - R02b)) == 0,
                          f'{tagj}: sel-param R0slack mismatch')
                    g2list = list(gd2.values())
                    xsym = L.to_local(0, wx)
                    check_sel_arcs(item['arcs'], g2list, tagj,
                                   t, 1 - s, xsym, set())
                else:
                    check(False, f'{tagj}: unknown kind')
        arcs = bx['fitting']
        check_arcchain(arcs, f'{tag}/fitting',
                       lambda A, kk: parse_vec(A[kk]))
        for arc in arcs:
            tr = arc['triple']
            w = L.selection_vector([sp.Matrix([wit[tr[0]][0],
                                               wit[tr[0]][1]]),
                                    sp.Matrix([wit[tr[1]][0],
                                               wit[tr[1]][1]]),
                                    sp.Matrix([wit[tr[2]][0],
                                               wit[tr[2]][1]])])
            d1, d2 = parse_vec(arc['d1']), parse_vec(arc['d2'])
            check(exact_sign_q3num(d1[0] * d2[1] - d1[1] * d2[0]) > 0,
                  f'{tag}/fit: arc not <180')
            for dd in (d1, d2):
                lin = sp.expand(w[0] * dd[0] + w[1] * dd[1])
                quad = sp.expand(lin ** 2 - H ** 2 * (dd[0] ** 2
                                                      + dd[1] ** 2))
                check(exact_sign_q3num(lin) >= 0
                      and exact_sign_q3num(quad) > 0,
                      f'{tag}/fit: endpoint fails')
        if bi % 25 == 0:
            print(f'  ... box {bi}/{len(boxes)}', flush=True)
    print(f'  bulk zone: {"OK" if not FAIL else "FAILURES"}')


def verify_numeric_spotcheck(n=6):
    print('== numeric defense-in-depth ==')
    import numpy as np
    from hole_lab import Hole, staircase, HCONST
    rng = np.random.default_rng(7)
    for _ in range(n):
        lev = rng.uniform(0.03, 0.95)
        q = 1 - lev
        cap = ((-q + np.sqrt(4 - 3 * q * q)) / 2 - lev) * 0.8
        if cap <= 0:
            continue
        gaps = rng.uniform(0.1, 1, 5)
        gaps *= rng.uniform(0.2, 0.9) * cap / gaps.sum()
        a = staircase(lev, gaps=gaps)
        try:
            hole = Hole(a)
        except ValueError:
            continue
        f, phi, _ = hole.min_F_S(ntheta=300, m=3000)
        ok = f - HCONST > 0
        print(f'  a={np.round(a, 3)}: margin {f - HCONST:+.5f} '
              f'{"OK" if ok else "FAIL"}')
        check(ok, 'numeric spot-check failed')


if __name__ == '__main__':
    verify_corner()
    verify_bulk()
    if '--numeric' in sys.argv:
        verify_numeric_spotcheck()
    print()
    if FAIL:
        print(f'*** {len(FAIL)} FAILURES ***')
        sys.exit(1)
    print('ALL CERTIFICATES VERIFIED: under the standing assumptions, '
          'F_S(phi) > h for every phi')
    print('(modulo Lemmas 2.1-2.3 and 3.1-3.3 of hole_set_noncover.md, '
          'proved there)')
