r"""Certificate generator for the hole-set non-coverability proof.

Produces `hole_certificates.py` (exact data, importable) which
`verify_hole_noncover.py` re-checks from scratch.

Architecture (see hole_set_noncover.md):

  * Reduced theorem on T = {0 <= s <= t, R0^2 <= 1} (WLOG s+t <= 1 by the
    mirror lemma): F_{S~(s,t)}(phi) > h for all phi.
  * Zone C (s <= 1/32): two leaves C-low / C-high (split 5t <=> 8s), each
    with 7 exact witnesses and 4 phi-arcs.
  * Bulk (1/32 <= s <= 1/2): boxes with constant supersets and constant
    rational witnesses.
  * Every claim is compiled to:  "sinusoid <w(s,t), u> >= h on an arc
    [d1, d2]"  ->  (arc <= 180 deg) + two endpoint inequalities, each a
    polynomial inequality in (s,t) over the leaf region, certified by an
    exact positive combination of region generators (Handelman style).
  * Witness validity vs a set K(a,b):  either a disk inequality
    |x_loc - P|^2 >= 1 (P in {A,O,B}, diameter lemma) or a selection
    certificate: arcs covering [0,120] with selection vectors from
    {A,O,B,x}^3 whose sinusoid stays >= h (+ margin) on each arc.

All data exact over Q(sqrt3)(s,t).  Numerics are used ONLY to search; every
emitted object is verified exactly here and re-verified independently by
verify_hole_noncover.py.
"""
import itertools
import numpy as np
import sympy as sp
from fractions import Fraction

import hole_cert_lib as L

s, t = L.s, L.t
R3, H = L.R3, L.H

# ================================================================
# leaf regions
# ================================================================
S0 = sp.Rational(1, 32)


def leaf_gens(leaf):
    """generators g >= 0 describing each corner leaf.

    'dg' = 2s - t is nonnegative on the region: it equals
    R0slack + (s^2 - s t + t^2) and s^2-st+t^2 = (s-t/2)^2 + (3/4)t^2 >= 0;
    the verifier re-checks this derivation."""
    R02 = L.R0_sq()
    base = {'s': s, 'g': t - s, 'R0slack': sp.expand(1 - R02),
            'dg': 2 * s - t}
    if leaf == 'C-ext':
        base['sfloor'] = s - S0
        base['scap'] = sp.Rational(1, 16) - s
        base['wedge'] = sp.Rational(5, 4) * s - t
        return base
    base['scap'] = S0 - s
    if leaf == 'C-low':
        base['split'] = 8 * s - 5 * t
    else:
        base['split'] = 5 * t - 8 * s
    return base


# ================================================================
# witnesses (locked design)
# ================================================================
def witnesses(leaf):
    u60, u90, u150, u240 = (L.u_deg(60), L.u_deg(90), L.u_deg(150),
                            L.u_deg(240))
    V0 = sp.Matrix(L.VERT[0]); V5 = sp.Matrix(L.VERT[5])
    g = t - s
    W = {}
    W['W0'] = sp.Matrix([0, 0])
    W['WV0b'] = V0 + t * u240 + 2 * t * u150
    W['WV5'] = V5 + 2 * t * u90 + (t / 2) * u60
    if leaf in ('C-low', 'C-ext'):
        xi, pull = sp.Rational(21, 40) * g, g / 20
    else:
        xi, pull = s / 3, g / 60
    ck = (1 - xi ** 2) / (1 + xi ** 2)
    sk = 2 * xi / (1 + xi ** 2)
    c60, s60 = sp.Rational(1, 2), R3 / 2
    u1 = sp.Matrix([c60 * ck + s60 * sk, s60 * ck - c60 * sk])  # u(60-kap)
    c2k, s2k = ck ** 2 - sk ** 2, 2 * sk * ck
    c210, s210 = -R3 / 2, -sp.Rational(1, 2)
    u2 = sp.Matrix([c210 * c2k + s210 * s2k, s210 * c2k - c210 * s2k])
    zloc = u1 + (s / R3) * u150 + (s / R3) * u2 + pull * u1
    W['Wst1'] = L.to_global(1, zloc)
    W['Wst3'] = L.rot120(W['Wst1'], 1)
    A0, O0, B0 = L.AOB_global(0)
    mloc = sp.Matrix([R3 * t, t + 2 * (1 - s)])
    mglob = sp.Matrix([mloc[0] * L.EX[0][0] + mloc[1] * L.EY[0][0],
                       mloc[0] * L.EX[0][1] + mloc[1] * L.EY[0][1]])
    R02 = L.R0_sq()
    W['Wdip'] = (A0 + B0) / 2 + (sp.Rational(4, 15) * (1 - R02)
                                 + s ** 2 / 16) * mglob
    return {k: sp.Matrix([sp.cancel(sp.together(v[0])),
                          sp.cancel(sp.together(v[1]))]) for k, v in W.items()}


def rot_tanhalf(base, xi, sign):
    """rotate `base` by the angle with tan(half) = xi (rational), sign +/-"""
    ck = (1 - xi ** 2) / (1 + xi ** 2)
    sk = sign * 2 * xi / (1 + xi ** 2)
    R = sp.Matrix([[ck, -sk], [sk, ck]])
    e = R * base
    return sp.Matrix([sp.cancel(sp.together(e[0])),
                      sp.cancel(sp.together(e[1]))])


def cut_dirs(leaf='C-low'):
    """unnormalized cut vectors (the arc lemma works with any
    nonzero directions): eL ~ u(90 - cL*t), eR ~ u(90 + (5/2) t)"""
    cuts = {'u0': L.u_deg(0), 'u60': L.u_deg(60), 'u120': L.u_deg(120)}
    cL = t if leaf == 'C-ext' else sp.Rational(3, 4) * t
    cuts['eL'] = sp.Matrix([cL, 1])
    cuts['eR'] = sp.Matrix([-sp.Rational(5, 2) * t, 1])
    return cuts


FITTING_ARCS = [('A', 'u0', 'eL', ('WV0b', 'W0', 'WV5')),
                ('B', 'eL', 'eR', ('Wst1', 'Wst3', 'Wdip')),
                ('D', 'eR', 'u120', ('Wst1', 'WV5', 'Wdip'))]


# ================================================================
# exact positivity certificates (Handelman-style)
# ================================================================
def q3_parts(e):
    """split an expanded Q(sqrt3)-polynomial into (rat, irr): e = rat +
    sqrt3*irr, both in Q[s,t]"""
    e = sp.expand(e)
    rat = e.subs(R3, 0)
    irr = sp.expand((e - rat) / R3)
    irr = sp.expand(irr)
    return rat, irr


def exact_sign_q3(c):
    """exact sign of c = p + q*sqrt3 with p, q rational. Returns -1/0/+1."""
    c = sp.expand(c)
    p, q = q3_parts(c)
    p, q = sp.Rational(p), sp.Rational(q)
    if p == 0 and q == 0:
        return 0
    if p >= 0 and q >= 0:
        return 1
    if p <= 0 and q <= 0:
        return -1
    # mixed signs: compare p^2 vs 3 q^2
    if p > 0:                      # q < 0: sign = sign(p^2 - 3q^2)
        return 1 if p ** 2 > 3 * q ** 2 else (-1 if p ** 2 < 3 * q ** 2 else 0)
    return -1 if p ** 2 > 3 * q ** 2 else (1 if p ** 2 < 3 * q ** 2 else 0)


def gen_products(gens, degmax, degcap=None):
    """products of generators (as polynomials + exponent tuples)"""
    gnames = list(gens.keys())
    gpolys = [sp.expand(gens[k]) for k in gnames]
    prods, alphas = [], []
    for deg in range(degmax + 1):
        for combo in itertools.combinations_with_replacement(
                range(len(gpolys)), deg):
            alpha = [0] * len(gpolys)
            for i in combo:
                alpha[i] += 1
            p = sp.Integer(1)
            for i, a in enumerate(alpha):
                if a:
                    p *= gpolys[i] ** a
            p = sp.expand(p)
            if degcap is not None and sp.total_degree(
                    p.subs(R3, sp.Integer(0)) + p, s, t) > degcap:
                continue
            prods.append(p)
            alphas.append(tuple(alpha))
    return gnames, prods, alphas


_GP_CACHE = {}


def gen_scale(g):
    """power-of-two rational making the generator O(1) on the region
    (max |coefficient| ~ 1); exact positive scalar"""
    g = sp.expand(g)
    mx = 0
    for part in q3_parts(g):
        if part == 0:
            continue
        pp = sp.Poly(part, s, t)
        mx = max(mx, max(abs(sp.Rational(c)) for c in pp.coeffs()))
    if mx == 0:
        return sp.Integer(1)
    lam = sp.Integer(1)
    while mx * lam < 1:
        lam *= 2
    while mx * lam > 2:
        lam /= 2
    return lam


def gen_products_cached(gens, degmax, degcap):
    key = (tuple((k, sp.srepr(sp.expand(v))) for k, v in gens.items()),
           degmax, degcap)
    if key not in _GP_CACHE:
        lams = {k: gen_scale(v) for k, v in gens.items()}
        gens_sc = {k: sp.expand(lams[k] * v) for k, v in gens.items()}
        gnames, prods, alphas = gen_products(gens_sc, degmax, degcap=degcap)
        pms = [monomap(p) for p in prods]
        lamlist = [lams[k] for k in gnames]
        _GP_CACHE[key] = (gnames, prods, alphas, pms, lamlist)
    return _GP_CACHE[key]


def monomap_r3shift(m):
    """monomap of sqrt3*p given monomap of p (rat<->irr swap, x3)"""
    out = {}
    for (mono, tag), c in m.items():
        if tag == 0:
            out[(mono, 1)] = c
        else:
            out[(mono, 0)] = 3 * c
    return out


def monomap(e):
    """exact monomial map of a Q(sqrt3)[s,t] polynomial:
    {(mono, 0/1): Rational}"""
    d = {}
    rat, irr = q3_parts(e)
    for part, tag in ((rat, 0), (irr, 1)):
        if part == 0:
            continue
        pp = sp.Poly(part, s, t)
        for mono, c in pp.terms():
            d[(mono, tag)] = d.get((mono, tag), sp.Rational(0)) + sp.Rational(c)
    return d


def certify_nonneg(q, gens, degmax=4, verbose=False, extra_sq=None):
    """Exact identity  q = sum_alpha (p_alpha + q_alpha*sqrt3)
    * prod g_i^alpha_i  with rational p_alpha, q_alpha >= 0.
    Returns list of (coeff, alpha) with coeff in Q(sqrt3) or None."""
    q = sp.expand(q)
    qdeg = sp.total_degree(sp.expand(q.subs(R3, sp.Integer(2))), s, t)
    pad = 2 if degmax >= 4 else 0
    gnames, prods0, alphas0, pm0, lamlist = gen_products_cached(
        gens, degmax, max(qdeg, 2) + pad)
    if extra_sq:
        # auxiliary square generators l^2 (globally nonnegative), used
        # alone or multiplied by one region generator
        nbase = len(gens)
        prods0 = list(prods0)
        alphas0 = list(alphas0)
        pm0 = list(pm0)
        base_polys = [sp.expand(v) for v in gens.values()]
        for isq, lroot in enumerate(extra_sq):
            sq = sp.expand(lroot ** 2)
            adds = [(sq, tuple([0] * nbase + [1 if k == isq else 0
                                              for k in range(len(extra_sq))]))]
            for ib, bp in enumerate(base_polys):
                al = [0] * nbase
                al[ib] = 1
                adds.append((sp.expand(sq * bp),
                             tuple(al + [1 if k == isq else 0
                                         for k in range(len(extra_sq))])))
            for p_, a_ in adds:
                prods0.append(p_)
                alphas0.append(a_)
                pm0.append(monomap(p_))
    else:
        alphas0 = [tuple(list(a) + []) for a in alphas0]
    # coefficient model: c_alpha = p_alpha + q_alpha*sqrt3, constraint
    # p + sqrt3 q >= 0 (real nonnegativity); columns: g^a and sqrt3*g^a
    nP = len(prods0)
    qm = monomap(q)
    pm = list(pm0) + [monomap_r3shift(m) for m in pm0]
    keys = sorted(set(qm) | set().union(*[set(m) for m in pm]),
                  key=lambda k: (k[1], k[0]))
    A = np.zeros((len(keys), 2 * nP))
    b = np.zeros(len(keys))
    for r, k in enumerate(keys):
        b[r] = float(qm.get(k, 0))
        for c, m in enumerate(pm):
            A[r, c] = float(m.get(k, 0))
    from scipy.optimize import linprog
    r3f = float(R3)
    # unknowns: [p (nP, free), qp (nP, >=0), qm (nP, >=0)], q = qp - qm
    A3 = np.zeros((len(keys), 3 * nP))
    A3[:, :nP] = A[:, :nP]
    A3[:, nP:2 * nP] = A[:, nP:]
    A3[:, 2 * nP:] = -A[:, nP:]
    A_ub = np.zeros((nP, 3 * nP))
    for i in range(nP):
        A_ub[i, i] = -1.0
        A_ub[i, nP + i] = -r3f
        A_ub[i, 2 * nP + i] = r3f
    eta = 1e-3
    cobj = np.concatenate([np.ones(nP), (r3f + eta) * np.ones(nP),
                           (-r3f + eta) * np.ones(nP)])
    res = linprog(cobj, A_ub=A_ub, b_ub=np.zeros(nP), A_eq=A3, b_eq=b,
                  bounds=[(None, None)] * nP + [(0, None)] * (2 * nP),
                  method='highs-ds')
    if not res.success:
        if verbose:
            print(f'   LP infeasible at degmax={degmax}')
        return None
    x3 = res.x
    x = np.concatenate([x3[:nP], x3[nP:2 * nP] - x3[2 * nP:]])
    # support in alpha-space
    supp = [i for i in range(nP)
            if abs(x[i]) > 1e-10 or abs(x[nP + i]) > 1e-10]
    for i in range(nP):                 # headroom: low-degree products
        if sum(alphas0[i]) <= 1 and i not in supp:
            supp.append(i)
    supp = sorted(supp)
    cols = supp + [nP + i for i in supp]
    Pex = sp.Matrix([[pm[c].get(k, sp.Rational(0)) for c in cols]
                     for k in keys])
    qex = sp.Matrix([qm.get(k, sp.Rational(0)) for k in keys])
    try:
        sol, params = Pex.gauss_jordan_solve(qex)
    except ValueError:
        if verbose:
            print('   exact system inconsistent on support')
        return None
    xf = np.array([x[c] for c in cols])
    m = len(supp)

    # exact vertex reconstruction: solve on the LP-active columns only,
    # iteratively dropping columns whose exact value comes out negative.
    active = [i for i in range(len(cols)) if abs(xf[i]) > 1e-9]
    if not active:
        active = [0]
    xr = None
    for _ in range(8):
        Pact = Pex[:, active]
        try:
            sola, parama = Pact.gauss_jordan_solve(qex)
        except ValueError:
            # inconsistent: enlarge with all columns once, then fail
            if len(active) == len(cols):
                break
            active = list(range(len(cols)))
            continue
        if parama:
            sola = sola.subs({p: 0 for p in parama})
        vals_full = [sp.Rational(0)] * len(cols)
        okrat = True
        for idx, i in enumerate(active):
            v = sola[idx]
            if not getattr(v, 'is_Rational', False):
                okrat = False
                break
            vals_full[i] = sp.Rational(v)
        if not okrat:
            break
        coeffs = [vals_full[j] + vals_full[m + j] * R3 for j in range(m)]
        neg = [j for j in range(m) if exact_sign_q3(coeffs[j]) < 0]
        if not neg:
            xr = vals_full
            break
        # drop the negative coefficient's columns and retry
        newactive = [i for i in active
                     if not any(i == j or i == m + j for j in neg)]
        if newactive == active:
            break
        active = newactive
    if xr is None:
        if verbose:
            print('   no nonnegative exact vertex found')
        return None
    coeffs = [xr[j] + xr[m + j] * R3 for j in range(m)]
    resid = sp.expand(q - sum(coeffs[j] * prods0[supp[j]]
                              for j in range(m)))
    if resid != 0:
        if verbose:
            print('   exact residual nonzero (bug)')
        return None
    out = []
    for j, c in enumerate(coeffs):
        if c == 0:
            continue
        al = alphas0[supp[j]]
        scale = sp.Integer(1)
        for i, a in enumerate(al):
            if a and i < len(lamlist):
                scale *= lamlist[i] ** a
        out.append((sp.expand(c * scale), al))
    return out


def certify_nonneg_auto(q, gens, verbose=False, samples=None):
    for degmax in (2, 3, 4, 5, 6):
        cert = certify_nonneg(q, gens, degmax=degmax, verbose=verbose)
        if cert is not None:
            return cert, degmax, None
    # Schmuedgen-style rescue: add squares centered at the numeric argmin
    if samples:
        fn = sp.lambdify((s, t), q, 'numpy')
        vals = [(float(fn(sv, tv)), sv, tv) for sv, tv in samples]
        _, s0, t0 = min(vals)
        from fractions import Fraction
        sr = sp.Rational(Fraction(s0).limit_denominator(256))
        tr = sp.Rational(Fraction(t0).limit_denominator(256))
        aux = [t - tr, s - sr, (s - sr) + (t - tr), (s - sr) - (t - tr),
               t - R3 / 2, t - R3 * s]
        for degmax in (3, 4, 5):
            cert = certify_nonneg(q, gens, degmax=degmax, verbose=verbose,
                                  extra_sq=aux)
            if cert is not None:
                return cert, degmax, aux
    return None, None, None


if __name__ == '__main__':
    print('This module is driven by gen_corner.py / gen_bulk.py')
