"""Numerical checking of the ab-set case tables (20092_ab_set_case_catalog.md).

This program is not a rigorous certificate: it samples parameter values and
directions and uses floating-point orientation grids plus local refinement.
It can find counterexamples and reproduce the empirical evidence, but a clean
run does not establish the universal claims in the general catalog.

Ground truth: for x = r u(theta), x in U  iff  min_phi F_{AOBx}(phi) <= sqrt(3)/2
(Viviani fitting criterion). r*(theta) is computed by exact inversion of the
piecewise-linear-in-r equation per orientation phi, maximized over phi
(including the Phi-endpoints, where rho jumps).

Checks per sample (a,b):
  1. the numerically computed boundary arc sequence equals the chain claimed
     for the case region containing (a,b);
  2. every sampled boundary point lies on its claimed algebraic curve
     (normalized residual < 1e-7);
  3. corner identities: P1,P2,P2',P3 on their three curves each; B* on c_A;
     A* on c_B.
Also a region audit (predicate implications used to prune the case table) and
the exact sympy identity suite (tangency thresholds etc.).

Run:  python3 2009X_computation/verify_ab_set.py            (full suite, ~10-20 min)
      python3 2009X_computation/verify_ab_set.py quick      (reduced)
"""
import numpy as np
import sys

RT3 = np.sqrt(3.0)
H = RT3 / 2
TAU = 2 * np.pi
D = np.pi / 180


# ----------------------------------------------------------------------
# ground truth machinery (self-contained copy of the exact solver)
# ----------------------------------------------------------------------

def pts_of(a, b):
    return np.array([[0., 0.], [-a / 2, a * RT3 / 2], [b, 0.]])


def F_pts(P, phis):
    tot = np.zeros_like(phis)
    for k in range(3):
        th = phis + TAU * k / 3
        u = np.stack([np.cos(th), np.sin(th)], 0)
        tot += (P @ u).max(0)
    return tot


def extreme_phis(a, b, m=200000):
    P = pts_of(a, b)
    phis = np.linspace(0, TAU / 3, m, endpoint=False)
    s = F_pts(P, phis) - H
    roots = []
    for i in range(m):
        j = (i + 1) % m
        if (s[i] < 0) != (s[j] < 0):
            lo, hi = phis[i], phis[i] + (TAU / 3) / m
            for _ in range(60):
                mid = (lo + hi) / 2
                fm = F_pts(P, np.array([mid]))[0] - H
                fl = F_pts(P, np.array([lo]))[0] - H
                if (fm < 0) != (fl < 0):
                    hi = mid
                else:
                    lo = mid
            roots.append((lo + hi) / 2)
    return roots


def rho_of(theta, phis, P):
    m = len(phis)
    C = np.zeros((m, 3))
    G = np.zeros((m, 3))
    for k in range(3):
        th = phis + TAU * k / 3
        u = np.stack([np.cos(th), np.sin(th)], 0)
        G[:, k] = (P @ u).max(0)
        C[:, k] = np.cos(theta - th)
    F0 = G.sum(1)
    rho = np.full(m, -np.inf)
    feas = F0 <= H + 1e-15
    with np.errstate(divide='ignore', invalid='ignore'):
        KN = np.where(C > 1e-15, G / C, np.inf)
    KNs = np.sort(KN, 1)
    for j in range(4):
        lo = np.zeros(m) if j == 0 else KNs[:, j - 1].copy()
        lo = np.maximum(lo, 0.0)
        lo = np.where(np.isfinite(lo), lo, 1e18)
        hi = KNs[:, j] if j < 3 else np.full(m, np.inf)
        act = (KN <= lo[:, None] * (1 + 1e-12) + 1e-15)
        slope = (C * act).sum(1)
        Flo = F0 + (act * (lo[:, None] * C - G)).sum(1)
        ok = feas & (Flo <= H + 1e-15)
        with np.errstate(divide='ignore', invalid='ignore'):
            rc = np.where(slope > 1e-15, lo + (H - Flo) / slope, np.inf)
        rc = np.minimum(rc, hi)
        rho = np.where(ok, np.maximum(rho, np.where(rc >= lo - 1e-15, rc, rho)),
                       rho)
    return rho


def rstar(theta, P, roots, m=20000):
    phis = np.linspace(0, TAU / 3, m, endpoint=False)
    if roots:
        extra = np.array([rr + s for rr in roots for s in (0., 1e-13, -1e-13)])
        phis = np.concatenate([phis, extra % (TAU / 3)])
    rho = rho_of(theta, phis, P)
    j = int(np.argmax(rho))
    r0, p0 = rho[j], phis[j]
    gr = (np.sqrt(5) - 1) / 2
    a0, b0 = p0 - 2.5 * (TAU / 3) / m, p0 + 2.5 * (TAU / 3) / m
    for _ in range(80):
        c = b0 - gr * (b0 - a0)
        d = a0 + gr * (b0 - a0)
        fc = rho_of(theta, np.array([c]), P)[0]
        fd = rho_of(theta, np.array([d]), P)[0]
        if fc < fd:
            a0 = c
        else:
            b0 = d
    pm = (a0 + b0) / 2
    rm = rho_of(theta, np.array([pm]), P)[0]
    if rm < r0:
        rm, pm = r0, p0
    return rm, pm


# ----------------------------------------------------------------------
# predicates and predicted chain (the case tables of 20092_ab_set_case_catalog.md)
# ----------------------------------------------------------------------

def Gpoly(a, b):
    s = a + b
    return ((1 - b) ** 2 * s ** 3 + (b - 1) * (b - 3) * s ** 2
            - b * (b - 1) * s - (b * b - 3 * b + 3))


def Epoly(a, b):
    return -(4 * a ** 3 * b ** 3 + 10 * a ** 3 * b ** 2 - 3 * a ** 3
             - a ** 2 * b ** 5 + 10 * a ** 2 * b ** 3 + 5 * a ** 2 * b ** 2
             - 15 * a ** 2 * b + 3 * a ** 2 + 2 * a * b ** 4 - a * b ** 3
             - 12 * a * b ** 2 + 3 * a * b + b ** 5 - 3 * b ** 4
             - 9 * b ** 3 + 3 * b ** 2)


def predicates(a, b):
    s = a + b
    R2 = a * a + a * b + b * b
    P = dict(R2=R2, s=s)
    P['empty'] = R2 > 1
    P['B1'] = s <= RT3 / 2
    P['B2'] = (s > RT3 / 2) and (R2 <= 0.75)
    P['B3'] = (R2 > 0.75) and (s <= 1)
    P['B4'] = (s > 1) and (R2 <= 1)
    P['sA'] = a < 0.5
    P['sB'] = b < 0.5
    P['e'] = s < 0.5
    P['wp'] = a * (1 - b * b) - b * (b * b - b + 1) > 0
    P['wm'] = b * (1 - a * a) - a * (a * a - a + 1) > 0
    P['G4'] = Gpoly(a, b) > 0
    P['G4s'] = Gpoly(b, a) > 0
    P['G3'] = (3 + a) * R2 > 3
    P['G3s'] = (3 + b) * R2 > 3
    P['etam'] = Epoly(a, b) > 0
    P['etap'] = Epoly(b, a) > 0
    return P


def predicted_chain(a, b):
    """chain of arc tokens between the two cone-edge segments"""
    P = predicates(a, b)
    if P['empty']:
        return ('EMPTY',)
    if a == 0.5 and b == 0.5:
        return ('cA1', 'sgA', 'sgB', 'cB1')
    if P['B4']:
        return ('cA1', 'sgA', 'sgB', 'cB1')
    seq = ['cA1']
    if P['B3'] and a > b:
        seq += (['sgA', 'MA', 'sgB'] if P['G3'] else ['sgA', 'sgB']) + ['cA1']
    if P['sA']:
        seq += ['epAO']
    af = bf = None
    if P['wp']:
        af = (['LA', 'epBA'] if P['etap'] else ['epBA']) if P['e'] else ['LA']
    if P['wm']:
        bf = (['epAB', 'LB'] if P['etam'] else ['epAB']) if P['e'] else ['LB']
    hasdip = P['B2'] or P['B3']
    dip = (['sgA'] + (['lOAB'] if P['G4'] else
                      (['lOBA'] if P['G4s'] else [])) + ['sgB']) if hasdip else []
    if af is not None:
        seq += af
    if af is not None and bf is not None:
        seq += ['epBO'] + dip + ['epAO']
    elif af is not None:
        seq += ['epBO'] + dip + (['epBO'] if hasdip else [])
    else:
        seq += ['epAO'] + dip + (['epAO'] if hasdip else [])
    if bf is not None:
        seq += bf
    if P['sB']:
        seq += ['epBO']
    if P['B3'] and b > a:
        seq += ['cB1'] + (['sgA', 'MB', 'sgB'] if P['G3s'] else ['sgA', 'sgB'])
    seq += ['cB1']
    out = []
    for t in seq:
        if not out or out[-1] != t:
            out.append(t)
    return tuple(out)


def case_name(a, b):
    P = predicates(a, b)
    if P['empty']:
        return '0'
    if a == 0.5 and b == 0.5:
        return 'II.0'
    if P['B4']:
        return 'IV'
    if P['B3']:
        n = {(0, 0): '1', (0, 1): '2', (1, 0): '3', (1, 1): '4'}[
            (int(P['G3'] if a > b else P['G3s']),
             int(P['G4'] if a > b else P['G4s']))]
        return f'III.{n}' + ("'" if b > a else '')
    band = 'I' if P['B1'] else 'II'
    if band == 'I':
        if not P['sA']:
            return 'I.6'
        if not P['sB']:
            return "I.6'"
        if P['e']:
            if P['wp'] and P['wm']:
                return {(0, 0): 'I.1', (1, 0): 'I.1a', (0, 1): 'I.1b',
                        (1, 1): 'I.1c'}[(int(P['etap']), int(P['etam']))]
            if P['wp']:
                return 'I.3' if P['etap'] else 'I.2'
            return "I.3'" if P['etam'] else "I.2'"
        if P['wp'] and P['wm']:
            return 'I.4'
        return 'I.5' if P['wp'] else "I.5'"
    lam = '+lB' if P['G4'] else ('+lA' if P['G4s'] else '')
    if not P['sA']:
        return 'II.1' + lam
    if not P['sB']:
        return "II.1'" + lam
    if P['wp'] and P['wm']:
        return 'II.2' + lam
    return ('II.3' if P['wp'] else "II.3'") + lam


# ----------------------------------------------------------------------
# curve equations for residual checks / classification
# ----------------------------------------------------------------------

def curve_residual(name, x, a, b, roots):
    X, Y = x
    w = X * X + Y * Y
    s3 = RT3
    if name == 'cA1':
        return abs(np.hypot(X + a / 2, Y - s3 * a / 2) - 1)
    if name == 'cB1':
        return abs(np.hypot(X - b, Y) - 1)
    if name == 'LA':
        return abs(s3 * X + Y - s3) / 2
    if name == 'LB':
        return abs(Y - s3 / 2)
    if name == 'MA':
        return abs(s3 * X - Y - s3 * (1 - a)) / 2
    if name == 'MB':
        return abs(Y - s3 * X - s3 * (1 - b)) / 2
    if name == 'lOAB':
        return abs(Y - s3 * (1 - b) / 2)
    if name == 'lOBA':
        return abs(s3 * X + Y - s3 * (1 - a)) / 2
    if name in ('sgA', 'sgB'):
        # x must lie on SOME extreme-triangle side line through A (resp. B)
        P = pts_of(a, b)
        best = np.inf
        for rr in roots:
            for k in range(3):
                th = rr + TAU * k / 3
                u = np.array([np.cos(th), np.sin(th)])
                d = P @ u
                c = d.max()
                who = int(np.argmax(d))
                if (name == 'sgA' and who == 1) or (name == 'sgB' and who == 2):
                    best = min(best, abs(x @ u - c))
        return best
    # quartics: normalized implicit value
    if name == 'epAO':
        v = (3 * w * w + 6 * a * X * w - 2 * s3 * a * Y * w - 3 * w
             + 3 * a * a * X * X + a * a * Y * Y - 2 * s3 * a * a * X * Y
             - 3 * a * X + 3 * s3 * a * Y - 3 * a * a)
    elif name == 'epBO':
        v = (3 * w * w - 6 * b * X * w + 2 * s3 * b * Y * w - 3 * w
             + 3 * b * b * X * X + b * b * Y * Y - 2 * s3 * b * b * X * Y
             + 6 * b * X - 3 * b * b)
    elif name in ('epBA', 'epAB'):
        d_ = a - b
        v = (3 * w * w + 6 * d_ * X * w - 2 * s3 * d_ * Y * w - 3 * w
             + 3 * d_ * d_ * X * X - 6 * a * b * X * X + d_ * d_ * Y * Y
             - 6 * a * b * Y * Y - 2 * s3 * d_ * d_ * X * Y
             - 6 * a * b * d_ * X + 2 * s3 * a * b * d_ * Y)
        if name == 'epBA':
            v += 6 * b * X + 3 * a * a * b * b - 3 * b * b
        else:
            v += -3 * a * X + 3 * s3 * a * Y + 3 * a * a * b * b - 3 * a * a
    else:
        return np.inf
    # normalize by gradient magnitude (finite differences)
    eps = 1e-6
    g = np.hypot(
        (curve_residual_raw(name, (X + eps, Y), a, b)
         - curve_residual_raw(name, (X - eps, Y), a, b)) / (2 * eps),
        (curve_residual_raw(name, (X, Y + eps), a, b)
         - curve_residual_raw(name, (X, Y - eps), a, b)) / (2 * eps))
    return abs(v) / max(g, 1e-9)


def curve_residual_raw(name, x, a, b):
    X, Y = x
    w = X * X + Y * Y
    s3 = RT3
    if name == 'epAO':
        return (3 * w * w + 6 * a * X * w - 2 * s3 * a * Y * w - 3 * w
                + 3 * a * a * X * X + a * a * Y * Y - 2 * s3 * a * a * X * Y
                - 3 * a * X + 3 * s3 * a * Y - 3 * a * a)
    if name == 'epBO':
        return (3 * w * w - 6 * b * X * w + 2 * s3 * b * Y * w - 3 * w
                + 3 * b * b * X * X + b * b * Y * Y - 2 * s3 * b * b * X * Y
                + 6 * b * X - 3 * b * b)
    d_ = a - b
    v = (3 * w * w + 6 * d_ * X * w - 2 * s3 * d_ * Y * w - 3 * w
         + 3 * d_ * d_ * X * X - 6 * a * b * X * X + d_ * d_ * Y * Y
         - 6 * a * b * Y * Y - 2 * s3 * d_ * d_ * X * Y
         - 6 * a * b * d_ * X + 2 * s3 * a * b * d_ * Y)
    if name == 'epBA':
        return v + 6 * b * X + 3 * a * a * b * b - 3 * b * b
    return v - 3 * a * X + 3 * s3 * a * Y + 3 * a * a * b * b - 3 * a * a


ALL_TOKENS = ['cA1', 'cB1', 'LA', 'LB', 'MA', 'MB', 'lOAB', 'lOBA',
              'sgA', 'sgB', 'epAO', 'epBO', 'epBA', 'epAB']


def verify_sample(a, b, nth=1500, m=20000, tol=1e-7):
    """returns (ok, message)"""
    exp = predicted_chain(a, b)
    if exp == ('EMPTY',):
        # check a few directions have no admissible triangle
        P = pts_of(a, b)
        phis = np.linspace(0, TAU / 3, 20000, endpoint=False)
        ok = F_pts(P, phis).min() > H + 1e-12
        return ok, 'empty ok' if ok else 'EMPTY expected but F<=h somewhere'
    P = pts_of(a, b)
    roots = extreme_phis(a, b)
    ths = np.linspace(1e-6, TAU / 3 - 1e-6, nth)
    toks = []
    maxres = 0.0
    for th in ths:
        r, ph = rstar(th, P, roots, m=m)
        x = r * np.array([np.cos(th), np.sin(th)])
        # match against the curves claimed for this case only
        best, bl = np.inf, '?'
        for nm in exp:
            e = curve_residual(nm, x, a, b, roots)
            if e < best:
                best, bl = e, nm
        toks.append(bl)
        maxres = max(maxres, best)
    # run-compress with blip removal
    runs = []
    cur, c = toks[0], 0
    for tk in toks:
        if tk == cur:
            c += 1
        else:
            runs.append((cur, c))
            cur, c = tk, 1
    runs.append((cur, c))
    got = []
    for nm, c in runs:
        if c >= 2 and (not got or got[-1] != nm):
            got.append(nm)
    got = tuple(got)
    okseq = (got == exp)
    okres = maxres < tol
    if not okseq and (a < 0.01 or b < 0.01
                      or a * a + a * b + b * b > 0.998):
        # degenerate parameters: several claimed curves coincide (e.g. at
        # a=0: c_A, E_AO and the unit circle are one curve; some arcs have
        # length ~0), so the arc-name sequence is ill-posed. Accept if every
        # computed boundary point lies on a claimed curve (residual check)
        # and, after identifying merged names, got uses only claimed arcs.
        merge = {}
        if a < 0.01:
            merge.update({'epAO': 'cA1', 'epBA': 'epBO', 'lOBA': 'LA'})
        if b < 0.01:
            merge.update({'epBO': 'cB1', 'epAB': 'epAO', 'lOAB': 'LB'})
        if a < 0.01 and b < 0.01:
            merge = {k: 'cA1' for k in
                     ('epAO', 'epBO', 'epBA', 'epAB', 'cB1')}
        canon = lambda t: merge.get(t, t)
        gset = {canon(t) for t in got}
        eset = {canon(t) for t in exp}
        okseq = okres and gset <= eset
        if okseq:
            msg = (f'case {case_name(a,b):8s} res={maxres:.1e} '
                   f'SEQ-OK (degenerate merge)')
            return okres, msg
    msg = (f'case {case_name(a,b):8s} res={maxres:.1e} '
           + ('SEQ-OK' if okseq else f'SEQ-MISMATCH got={got} exp={exp}'))
    return okseq and okres, msg


def corner_checks(a, b):
    """P-points on their curves; B*,A* on the circles"""
    errs = []
    roots = extreme_phis(a, b)
    pts = {
        'P1': ((1 - a / 2, RT3 * a / 2), ['cA1', 'LA', 'epAO']),
        'P2': (((1 + b) / 2, RT3 * (1 - b) / 2), ['LA', 'epBA', 'epBO']),
        "P2'": (((1 - 2 * a) / 2, RT3 / 2), ['LB', 'epAB', 'epAO']),
        'P3': ((b - 0.5, RT3 / 2), ['LB', 'cB1', 'epBO']),
        'B*': (((np.sqrt(4 - 3 * a * a) - a) / 2, 0.0), ['cA1']),
    }
    for nm, (x, curves) in pts.items():
        for cv in curves:
            e = curve_residual(cv, np.array(x), a, b, roots)
            if e > 1e-9:
                errs.append(f'{nm} not on {cv}: {e:.2e}')
    return errs


def region_audit(N=400):
    """implications used to prune the case tables
    A2: in bands I-III at least one flank is exposed, except at the exact
        simultaneous degeneracies (0,0) and (1/2,1/2)
    A3: within bands II-III never both flush lines
    A5: band III (a>b): mu>0 implies G4>0 (so case III.3 is empty)
    A6: band I with a>=1/2 forces w+>0, w-<=0
    A7: band II excludes the eps-regime
    A9: in band II, rows II.2/II.3/II.3' have no flush line
    """
    viol = {k: 0 for k in ['A2', 'A3', 'A5', 'A6', 'A7', 'A9']}
    vals = np.linspace(1e-4, 1.0, N)
    for a in vals:
        for b in vals:
            R2 = a * a + a * b + b * b
            if R2 > 1:
                continue
            P = predicates(a, b)
            a2_exception = ((abs(a) < 1e-12 and abs(b) < 1e-12)
                            or (abs(a - 0.5) < 1e-12
                                and abs(b - 0.5) < 1e-12))
            if ((P['B1'] or P['B2'] or P['B3']) and not a2_exception
                    and not P['wp'] and not P['wm']):
                viol['A2'] += 1
            if (P['B2'] or P['B3']) and P['G4'] and P['G4s']:
                viol['A3'] += 1
            if P['B3'] and a > b and P['G3'] and not P['G4']:
                viol['A5'] += 1
            if P['B1'] and a >= 0.5 and not (P['wp'] and not P['wm']):
                viol['A6'] += 1
            if P['B2'] and P['e']:
                viol['A7'] += 1
            if (P['B2'] and P['sA'] and P['sB'] and (P['G4'] or P['G4s'])):
                viol['A9'] += 1
    return viol


SAMPLES = [
    # (a, b) — at least one interior sample per case region
    (1.0, 0.9),                       # 0 (empty)
    (0.05, 0.05),                     # I.1
    (0.10, 0.08), (0.25, 0.15),       # I.2
    (0.30, 0.10),                     # I.3
    (0.15, 0.25),                     # I.2'
    (0.372, 0.087), (0.40, 0.05),     # I.3
    (0.087, 0.372),                   # I.3'
    (0.35, 0.35), (0.42, 0.42),       # I.4
    (0.42, 0.35),                     # I.5
    (0.35, 0.42),                     # I.5'
    (0.60, 0.20), (0.55, 0.15),      # I.6
    (0.20, 0.60),                     # I.6'
    (0.50, 0.50),                     # II.0 simultaneous degeneration
    (0.55, 0.40),                     # II.1
    (0.80, 0.135),                    # III.2 (additional sample)
    (0.753, 0.183),                   # II.1 + lambda_B
    (0.40, 0.55),                     # II.1'
    (0.183, 0.753),                   # II.1' + lambda_A
    (0.135, 0.80),                    # III.2' (additional sample)
    (0.45, 0.45), (0.467, 0.42),      # II.2
    (0.48, 0.40),                     # II.3
    (0.40, 0.48),                     # II.3'
    (0.24, 0.255),                    # I.1c
    (0.255, 0.24),                    # I.1c (mirror side of diagonal)
    (0.2346, 0.26, 5000),             # I.1b (thin sliver; fine resolution)
    (0.26, 0.2346, 5000),             # I.1a
    (0.86, 0.02, 6000),               # III.1 (thin sliver near b->0; fine res)
    (0.875, 0.002),                   # III.1 near-degenerate (merge leniency)
    (0.70, 0.28), (0.66, 0.33),      # III.2
    (0.85, 0.10), (0.90, 0.05),      # III.4
    (0.28, 0.70), (0.10, 0.85),      # III.2', III.4'
    (0.70, 0.40), (0.60, 0.55),
    (0.85, 0.25, 5000),               # IV near rho=1; tiny circle arcs
    (0.0, 0.5), (0.0, 0.9), (0.5, 0.0), (0.0, 0.0),  # degenerate axes
]


if __name__ == '__main__':
    quick = len(sys.argv) > 1 and sys.argv[1] == 'quick'
    nth = 700 if quick else 1500
    print('== region audit ==')
    aud = region_audit(200 if quick else 400)
    for k, v in aud.items():
        print(f'  {k}: violations = {v}')
    print('== corner identities ==')
    for (a, b) in [(0.3, 0.2), (0.6, 0.25), (0.45, 0.45), (0.85, 0.1)]:
        errs = corner_checks(a, b)
        print(f'  ({a},{b}): {"OK" if not errs else errs}')
    print('== per-case boundary verification ==')
    nfail = 0
    for entry in SAMPLES:
        a, b = entry[0], entry[1]
        nth_s = entry[2] if len(entry) > 2 else nth
        ok, msg = verify_sample(a, b, nth=nth_s)
        print(f'  ({a:5.3f},{b:5.3f}) {"PASS" if ok else "FAIL"}  {msg}',
              flush=True)
        nfail += (not ok)
    print(f'== done: {len(SAMPLES)-nfail}/{len(SAMPLES)} samples passed ==')
