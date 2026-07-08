r"""MOSEK-backed SOS certification with exact Q(sqrt3) rationalization.

Certifies  q >= 0  on  {g_i >= 0} ∩ {h_j = 0}  (variables z, typically
(s,t) plus adjoined algebraic quantities) in Putinar form

    q = sigma_0 + sum_i sigma_i * g_i + sum_j lambda_j * h_j ,

sigma_* SOS, lambda_j free polynomials.  Pipeline:

  1. numeric solve (cvxpy + MOSEK), maximizing the smallest-eigenvalue
     margin of the Gram matrices so rounding has room;
  2. rationalize every Gram entry to p + q*sqrt3 (small denominators) and
     every lambda coefficient likewise;
  3. exact affine repair: the coefficient-matching identity is restored
     exactly by adjusting lambda (free) and the sigma_0 Gram entries along
     a fixed well-conditioned subset;
  4. exact verification: identity by expansion over Q(sqrt3), PSD of each
     Gram by exact LDL^T (all pivots > 0, or >= 0 with consistent kernel).

The emitted certificate is a dict that verify_hole_noncover.py can
re-check without MOSEK.
"""
import itertools
import numpy as np
import sympy as sp
from fractions import Fraction

R3 = sp.sqrt(3)


# ----------------------------------------------------------------
# helpers
# ----------------------------------------------------------------
def q3_parts(e):
    e = sp.expand(e)
    rat = e.subs(R3, 0)
    return rat, sp.expand((e - rat) / R3)


def exact_sign(c):
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


def round_q3(x, den=64, den_r3=64):
    """nearest p + q*sqrt3 with denominators bounded (2-dim rounding on
    the lattice basis (1, sqrt3))"""
    r3 = float(R3)
    best = None
    for qd in range(-den_r3, den_r3 + 1):
        qq = Fraction(qd, den_r3)
        pp = Fraction(x - float(qq) * r3).limit_denominator(den)
        err = abs(float(pp) + float(qq) * r3 - x)
        if best is None or err < best[0]:
            best = (err, pp, qq)
    _, pp, qq = best
    return sp.Rational(pp) + sp.Rational(qq) * R3


def monomials(vars_, deg):
    out = []
    for total in range(deg + 1):
        for combo in itertools.combinations_with_replacement(
                range(len(vars_)), total):
            m = sp.Integer(1)
            for i in combo:
                m *= vars_[i]
            out.append(sp.expand(m))
    return out


def poly_coeff_map(e, vars_):
    """{(monomial-exponents, 0/1 for sqrt3): Rational}"""
    d = {}
    rat, irr = q3_parts(e)
    for part, tag in ((rat, 0), (irr, 1)):
        if part == 0:
            continue
        pp = sp.Poly(part, *vars_)
        for mono, c in pp.terms():
            d[(mono, tag)] = d.get((mono, tag), sp.Rational(0)) \
                + sp.Rational(c)
    return d


def _pair(e):
    """exact (p, q) with e = p + q*sqrt3, p,q Rational"""
    e = sp.expand(e)
    rat, irr = q3_parts(e)
    return sp.Rational(rat), sp.Rational(irr)


def _padd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def _psub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def _pmul(a, b):
    return (a[0] * b[0] + 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def _pdiv(a, b):
    den = b[0] ** 2 - 3 * b[1] ** 2
    num = _pmul(a, (b[0], -b[1]))
    return (num[0] / den, num[1] / den)


def _psign(a):
    p, q = a
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


def ldl_psd_check(G):
    """exact LDL^T over Q(sqrt3) using pair arithmetic; True iff PSD"""
    n = G.shape[0]
    A = [[_pair(G[i, j]) for j in range(n)] for i in range(n)]
    for k in range(n):
        piv = A[k][k]
        sgn = _psign(piv)
        if sgn < 0:
            return False
        if sgn == 0:
            for j in range(k, n):
                if A[k][j] != (0, 0) and _psign(A[k][j]) != 0:
                    return False
                if A[k][j][0] != 0 or A[k][j][1] != 0:
                    return False
            continue
        for i in range(k + 1, n):
            f = _pdiv(A[i][k], piv)
            for j in range(k, n):
                A[i][j] = _psub(A[i][j], _pmul(f, A[k][j]))
    return True


# ----------------------------------------------------------------
# main certifier
# ----------------------------------------------------------------
def sos_certify(q, vars_, gens=(), eqs=(), deg=2, den=256, verbose=False,
                eq_deg=None, schmudgen=True, _trim=None, trim_tol=1e-6,
                min_eps=None, _pin=frozenset()):
    """Certify q >= 0 on {g >= 0 for g in gens} ∩ {h = 0 for h in eqs}.

    deg: half-degree of sigma_0.  schmudgen: also use pairwise products
    of the generators.  Two-stage: plain feasibility with facial
    reduction (numerically-null basis monomials dropped), then a
    margin-maximizing re-solve on the reduced bases, then exact
    rationalization.  Returns certificate dict or None."""
    import cvxpy as cp
    q = sp.expand(q)
    gens = [sp.expand(g) for g in gens]
    if schmudgen:
        base_g = list(gens)
        for i in range(len(base_g)):
            for j in range(i, len(base_g)):
                pg = sp.expand(base_g[i] * base_g[j])
                if sp.total_degree(pg.subs(R3, 2), *vars_) <= 2 * deg:
                    gens.append(pg)
    basis0 = monomials(vars_, deg)
    bases = [basis0]
    for g in gens:
        dg = sp.total_degree(sp.expand(g).subs(R3, 2), *vars_)
        bases.append(monomials(vars_, max(0, deg - (dg + 1) // 2)))
    origidx = [list(range(len(b))) for b in bases]
    fellback = [False] * len(bases)
    if _trim is not None:
        # facial reduction: drop numerically-null monomials but keep every
        # block nonempty (a 1x1 constant block is harmless; the constant
        # is always original index 0).  Blocks whose basis was trimmed
        # entirely are spurious -- remember them so the forced-margin
        # fallback does not resurrect them
        newor = []
        for mi, b in enumerate(bases):
            keep = [k for k in range(len(b)) if (mi, k) not in _trim]
            if not keep:
                keep = [0]
                fellback[mi] = True
            newor.append(keep)
        origidx = newor
        bases = [[b[k] for k in keep]
                 for b, keep in zip(bases, origidx)]

    lam_bases = []
    for h in eqs:
        dh = sp.total_degree(sp.expand(h).subs(R3, 2), *vars_)
        dl = 2 * deg - dh if eq_deg is None else eq_deg
        lam_bases.append(monomials(vars_, max(0, dl)))

    # decision variables: Gram = A + sqrt3*B per block (exact field
    # model); PSD imposed on the real combination A + sqrt(3) B
    r3f = float(R3)
    As = [cp.Variable((len(b), len(b)), symmetric=True) for b in bases]
    Bs = [cp.Variable((len(b), len(b)), symmetric=True) for b in bases]
    lam_r_v = [cp.Variable(len(lb)) for lb in lam_bases]
    lam_i_v = [cp.Variable(len(lb)) for lb in lam_bases]
    eps = [cp.Variable() for _ in bases]

    tgt = poly_coeff_map(q, vars_)
    all_polys = [sp.Integer(1)] + [sp.expand(g) for g in gens]
    entry_maps = []
    for mi, b in enumerate(bases):
        emap = {}
        for k in range(len(b)):
            for l in range(k, len(b)):
                prod = sp.expand(all_polys[mi] * b[k] * b[l])
                emap[(k, l)] = poly_coeff_map(prod, vars_)
        entry_maps.append(emap)
    lam_maps = []
    for hj, lb in zip(eqs, lam_bases):
        lam_maps.append([poly_coeff_map(sp.expand(hj * m), vars_)
                         for m in lb])

    keys = set(tgt)
    for emap in entry_maps:
        for mm in emap.values():
            keys |= set(mm)
    for lmap in lam_maps:
        for mm in lmap:
            keys |= set(mm)
    keys = sorted(keys)

    # coefficient c of a product splits as (c0, c1); an entry a + b*sqrt3
    # contributes a*c0 + 3*b*c1 to the rational row and a*c1 + b*c0 to the
    # sqrt3 row of the same monomial
    def splitc(mm, mono):
        c0 = mm.get((mono, 0), sp.Rational(0))
        c1 = mm.get((mono, 1), sp.Rational(0))
        return float(c0), float(c1)

    monos = sorted({mono for (mono, tag) in keys})
    cons = []
    for mono in monos:
        e_rat, e_irr = 0, 0
        for mi, emap in enumerate(entry_maps):
            for (k, l), mm in emap.items():
                c0, c1 = splitc(mm, mono)
                if c0 == 0 and c1 == 0:
                    continue
                mult = 1 if k == l else 2
                a_ = As[mi][k, l]
                b_ = Bs[mi][k, l]
                e_rat = e_rat + mult * (c0 * a_ + 3 * c1 * b_)
                e_irr = e_irr + mult * (c1 * a_ + c0 * b_)
        for lj, lmap in enumerate(lam_maps):
            for mk, mm in enumerate(lmap):
                c0, c1 = splitc(mm, mono)
                if c0 == 0 and c1 == 0:
                    continue
                e_rat = e_rat + c0 * lam_r_v[lj][mk] \
                    + 3 * c1 * lam_i_v[lj][mk]
                e_irr = e_irr + c1 * lam_r_v[lj][mk] \
                    + c0 * lam_i_v[lj][mk]
        t0_, t1_ = splitc(tgt, mono)
        cons.append(e_rat == t0_)
        cons.append(e_irr == t1_)
    if _trim is None:
        # stage 1: minimum-trace feasibility.  Trace penalization drives
        # every spurious Gram entry to zero, so the facial reduction that
        # follows keeps exactly the monomials the identity needs.
        cons1 = list(cons)
        tr = 0
        # entry bounds tame the near-degenerate split direction
        # (dA, dB) = (sqrt3, -1)*gamma, which float PSD barely sees and
        # which otherwise balloons the primal norm until MOSEK gives up
        bigM = max(100.0, 10.0 * max(
            (abs(float(v)) for v in tgt.values()), default=1.0))
        for mi in range(len(bases)):
            cons1.append(As[mi] + r3f * Bs[mi] >> 0)
            cons1.append(cp.abs(As[mi]) <= bigM)
            cons1.append(cp.abs(Bs[mi]) <= bigM)
            tr = tr + cp.trace(As[mi]) + r3f * cp.trace(Bs[mi])
        for lv in list(lam_r_v) + list(lam_i_v):
            cons1.append(cp.abs(lv) <= bigM)
        prob = cp.Problem(cp.Minimize(tr), cons1)
        try:
            prob.solve(solver=cp.MOSEK, verbose=False)
        except Exception as e:
            if verbose:
                print('  MOSEK failed:', e)
            return None
        if prob.status not in ('optimal', 'optimal_inaccurate'):
            if verbose:
                print(f'  infeasible ({prob.status})')
            return None
        trim = set()
        for mi in range(len(bases)):
            Gv = As[mi].value + r3f * Bs[mi].value
            for k in range(len(bases[mi])):
                if Gv[k, k] < trim_tol:
                    trim.add((mi, k))
        if verbose:
            print(f'  stage 1 (min-trace) OK; trimming {len(trim)} monomials')
        res = sos_certify(q, vars_, gens=gens, eqs=eqs, deg=deg, den=den,
                          verbose=verbose, eq_deg=eq_deg,
                          schmudgen=False, _trim=trim, trim_tol=trim_tol,
                          min_eps=min_eps)
        if res is None and trim and trim_tol > 1e-9:
            # over-trimming can leave stage 2 barely feasible; retry with a
            # more conservative facial reduction
            if verbose:
                print(f'  retrying with trim_tol={trim_tol * 1e-2:g}')
            return sos_certify(q, vars_, gens=gens, eqs=eqs, deg=deg,
                               den=den, verbose=verbose, eq_deg=eq_deg,
                               schmudgen=False, trim_tol=trim_tol * 1e-2,
                               min_eps=min_eps)
        if res is None and min_eps is None:
            # last resort for strictly positive q: force every block
            # interior so the rounding is entrywise-safe everywhere
            res = sos_certify(q, vars_, gens=gens, eqs=eqs, deg=deg,
                              den=den, verbose=verbose, eq_deg=eq_deg,
                              schmudgen=False,
                              min_eps=sp.Rational(1, 1024))
        if res is not None:
            return res
        # final fallback: the min-trace stage-1 solution itself is a
        # feasible Gram decomposition -- reconstruct exactly from it
        if verbose:
            print('  reconstructing from the stage-1 solution directly')
        s1_fallback = True
    else:
        s1_fallback = False
    if not s1_fallback:
        # stage 2: maximize per-block interior margins on the reduced bases
        bigM = max(100.0, 10.0 * max(
            (abs(float(v)) for v in tgt.values()), default=1.0))
        for mi in range(len(bases)):
            n = len(bases[mi])
            cons.append(As[mi] + r3f * Bs[mi] - eps[mi] * np.eye(n) >> 0)
            cons.append(cp.abs(As[mi]) <= bigM)
            cons.append(cp.abs(Bs[mi]) <= bigM)
            if min_eps is not None and (fellback[mi] or mi in _pin):
                cons.append(As[mi] == 0)
                cons.append(Bs[mi] == 0)
                cons.append(eps[mi] == 0)
            else:
                cons.append(eps[mi] >= (0 if min_eps is None
                                        else float(min_eps)))
            cons.append(eps[mi] <= 1)
        for lv in list(lam_r_v) + list(lam_i_v):
            cons.append(cp.abs(lv) <= bigM)
        prob = cp.Problem(cp.Maximize(cp.sum(cp.hstack(eps))), cons)
        try:
            prob.solve(solver=cp.MOSEK, verbose=False)
        except Exception as e:
            if verbose:
                print('  MOSEK failed:', e)
            return None
        if prob.status not in ('optimal', 'optimal_inaccurate'):
            if verbose:
                print(f'  infeasible ({prob.status})')
            return None
        if verbose:
            print('  per-block margins:',
                  [round(float(e.value), 6) for e in eps])

        # iterate the facial reduction: a zero-margin block whose stage-2
        # solution still has numerically-null diagonal entries is sitting on
        # a smaller face -- trim those entries and re-solve
        grow = set(_trim)
        for mi in range(len(bases)):
            evi = float(eps[mi].value) if eps[mi].value is not None else 0.0
            if evi < 1e-5 and len(bases[mi]) > 1:
                Gv = As[mi].value + r3f * Bs[mi].value
                for k in range(len(bases[mi])):
                    if Gv[k, k] < 1e-6:
                        grow.add((mi, origidx[mi][k]))
        if grow != set(_trim):
            if verbose:
                print(f'  re-trimming {len(grow) - len(_trim)} more monomials')
            return sos_certify(q, vars_, gens=gens, eqs=eqs, deg=deg, den=den,
                               verbose=verbose, eq_deg=eq_deg,
                               schmudgen=False, _trim=grow, trim_tol=trim_tol,
                               min_eps=min_eps)

    def _retry_interior():
        # exact reconstruction failed on a singular face: retry this same
        # face with the surviving blocks forced interior, which makes the
        # rounding entrywise-safe (needs q to have genuine margin).  Blocks
        # whose stage-2 value is essentially zero are pinned to zero --
        # they are spurious and often sit on monomials nothing can cancel
        if min_eps is not None:
            return None
        pins = set()
        for mi_ in range(len(bases)):
            Gv_ = As[mi_].value + r3f * Bs[mi_].value
            ev_ = float(np.linalg.eigvalsh((Gv_ + Gv_.T) / 2).min())
            if ev_ < 1e-5 and float(np.abs(Gv_).max()) < 1e-3:
                pins.add(mi_)
        if verbose:
            print(f'  retrying face with forced interior margins '
                  f'(pinning {sorted(pins)})')
        return sos_certify(q, vars_, gens=gens, eqs=eqs, deg=deg, den=den,
                           verbose=verbose, eq_deg=eq_deg, schmudgen=False,
                           _trim=_trim, trim_tol=trim_tol,
                           min_eps=sp.Rational(1, 1024),
                           _pin=frozenset(pins))

    # ---------------- rationalize ----------------
    # Interior blocks (margin >= 1e-5): entrywise rounding is PSD-safe,
    # and each entry gets an exact correction unknown.  Singular blocks:
    # entrywise rounding would leave the PSD cone, so round the
    # eigenvector DIRECTIONS (their entry ratios lie in Q(sqrt3) when the
    # face is rational) and leave the scales mu^2 as unknowns.  One exact
    # twisted linear solve over Q then determines scales, lambdas and the
    # interior corrections simultaneously, making the identity exact.
    interior = []
    Gr = [None] * len(bases)
    sing_dirs = [None] * len(bases)
    blk_margin = []
    for mi in range(len(bases)):
        Gv_ = As[mi].value + r3f * Bs[mi].value
        blk_margin.append(float(np.linalg.eigvalsh(
            (Gv_ + Gv_.T) / 2).min()))
    for mi in range(len(bases)):
        n = len(bases[mi])
        evi = blk_margin[mi]
        if evi >= 1e-5:
            interior.append(mi)
            M = sp.zeros(n, n)
            for k in range(n):
                for l in range(k, n):
                    a_ = Fraction(
                        float(As[mi].value[k, l])).limit_denominator(den)
                    b_ = Fraction(
                        float(Bs[mi].value[k, l])).limit_denominator(den)
                    v = sp.Rational(a_) + sp.Rational(b_) * R3
                    M[k, l] = v
                    M[l, k] = v
            Gr[mi] = M
        else:
            Gv = As[mi].value + r3f * Bs[mi].value
            w_, V_ = np.linalg.eigh((Gv + Gv.T) / 2)
            dirs = []
            for j in range(n):
                if w_[j] > 1e-6:
                    v = V_[:, j]
                    piv = int(np.argmax(np.abs(v)))
                    v = v / v[piv]
                    dirs.append(sp.Matrix([round_q3(float(x), den, den)
                                           for x in v]))
            sing_dirs[mi] = dirs
            Gr[mi] = sp.zeros(n, n)

    def assemble():
        tot = sp.Integer(0)
        for mi, b in enumerate(bases):
            gpoly = all_polys[mi]
            for k in range(len(b)):
                for l in range(len(b)):
                    tot += Gr[mi][k, l] * gpoly * b[k] * b[l]
        for lj, lb in enumerate(lam_bases):
            for mk, m in enumerate(lb):
                tot += lam_r[lj][mk] * eqs[lj] * m
        return sp.expand(tot)

    # unknown pair variables (p, q) standing for p + q*sqrt3, each with a
    # polynomial factor; column order mu, lambda, delta so the pivoting
    # prefers scales and multipliers and leaves corrections at zero
    lam_r = [[sp.Integer(0)] * len(lb) for lb in lam_bases]
    for _attempt in range(4):
        unk = []          # (kind, payload, coeff-map of its factor)
        for mi in range(len(bases)):
            if sing_dirs[mi] is None:
                continue
            for dj, d in enumerate(sing_dirs[mi]):
                lf = sp.expand(sum(d[k] * bases[mi][k]
                                   for k in range(len(bases[mi]))))
                F = sp.expand(all_polys[mi] * lf * lf)
                unk.append(('mu', (mi, dj), poly_coeff_map(F, vars_)))
        for lj, lb in enumerate(lam_bases):
            for mk, m in enumerate(lb):
                F = sp.expand(eqs[lj] * m)
                unk.append(('lam', (lj, mk), poly_coeff_map(F, vars_)))
        for mi in interior:
            b = bases[mi]
            for k in range(len(b)):
                for l in range(k, len(b)):
                    F = sp.expand(all_polys[mi] * b[k] * b[l]
                                  * (1 if k == l else 2))
                    unk.append(('del', (mi, k, l), poly_coeff_map(F, vars_)))

        resid0 = sp.Integer(0)
        for mi in interior:
            b = bases[mi]
            gpoly = all_polys[mi]
            for k in range(len(b)):
                for l in range(len(b)):
                    resid0 += Gr[mi][k, l] * gpoly * b[k] * b[l]
        rmap = poly_coeff_map(sp.expand(q - resid0), vars_)

        keys = set(rmap)
        for _, _, fm in unk:
            keys |= set(fm)
        monos = sorted({mono for (mono, tag) in keys})
        rows = []
        rhs = []
        for mono in monos:
            for tag in (0, 1):
                row = []
                for _, _, fm in unk:
                    c0 = fm.get((mono, 0), sp.Rational(0))
                    c1 = fm.get((mono, 1), sp.Rational(0))
                    # p-column then q-column of the pair
                    if tag == 0:
                        row.extend([c0, 3 * c1])
                    else:
                        row.extend([c1, c0])
                rows.append(row)
                rc0 = rmap.get((mono, 0), sp.Rational(0))
                rc1 = rmap.get((mono, 1), sp.Rational(0))
                rhs.append(rc0 if tag == 0 else rc1)
        Amat = sp.Matrix(rows)
        bvec = sp.Matrix(rhs)
        try:
            sol, params = Amat.gauss_jordan_solve(bvec)
        except ValueError:
            if verbose:
                print('  exact linear system inconsistent')
            return _retry_interior()
        plist = list(params) if params else []

        def eval_vals(yvals):
            sub = dict(zip(plist, yvals)) if plist else {}
            return [sp.Rational(sol[2 * i].subs(sub))
                    + sp.Rational(sol[2 * i + 1].subs(sub)) * R3
                    for i in range(len(unk))]

        vals = eval_vals([sp.Integer(0)] * len(plist))
        neg_mu = any(kind == 'mu' and exact_sign(v) < 0
                     for (kind, _, _), v in zip(unk, vals))
        if neg_mu and plist:
            # the free parameters span the exact solution space: any
            # RATIONAL choice keeps the identity exact, so search it with
            # a float LP for nonnegative scales and small corrections
            from scipy.optimize import linprog
            r3v = float(R3)
            sub0 = {p_: 0 for p_ in plist}
            npar = len(plist)
            A_ub, b_ub = [], []
            cvec = [0.0] * npar + [-1.0]
            for i, (kind, payload, _) in enumerate(unk):
                b0 = float(sol[2 * i].subs(sub0)) \
                    + r3v * float(sol[2 * i + 1].subs(sub0))
                cf = [float(sol[2 * i].coeff(p_))
                      + r3v * float(sol[2 * i + 1].coeff(p_))
                      for p_ in plist]
                if kind == 'mu':
                    # tau <= mu_i(y):  -cf.y + tau <= b0
                    A_ub.append([-c_ for c_ in cf] + [1.0])
                    b_ub.append(b0)
                elif kind == 'del':
                    mi = payload[0]
                    ev = blk_margin[mi]
                    db = max(1e-4, 0.3 * ev / max(1, len(bases[mi])))
                    A_ub.append(cf + [0.0])
                    b_ub.append(db - b0)
                    A_ub.append([-c_ for c_ in cf] + [0.0])
                    b_ub.append(db + b0)
            r = linprog(cvec, A_ub=A_ub, b_ub=b_ub,
                        bounds=[(None, None)] * (npar + 1),
                        method='highs')
            if r.status == 0:
                yq = [sp.Rational(Fraction(float(v)).limit_denominator(
                    1 << 24)) for v in r.x[:npar]]
                vals = eval_vals(yq)

        # scales must be nonnegative; drop noise directions and re-solve
        bad = [(payload, v) for (kind, payload, _), v in zip(unk, vals)
               if kind == 'mu' and exact_sign(v) < 0]
        if bad:
            noise = [pl for pl, v in bad if abs(float(v)) < 1e-3]
            if len(noise) < len(bad):
                if verbose:
                    print('  negative singular scale (non-noise)')
                return _retry_interior()
            for mi, dj in sorted(noise, reverse=True):
                del sing_dirs[mi][dj]
            continue

        for (kind, payload, _), v in zip(unk, vals):
            if kind == 'mu':
                mi, dj = payload
                d = sing_dirs[mi][dj]
                Gr[mi] = (Gr[mi] + v * d * d.T).applyfunc(sp.expand)
            elif kind == 'lam':
                lj, mk = payload
                lam_r[lj][mk] = v
            else:
                mi, k, l = payload
                Gr[mi][k, l] = sp.expand(Gr[mi][k, l] + v)
                Gr[mi][l, k] = Gr[mi][k, l]
        break
    else:
        if verbose:
            print('  scale sign loop exhausted')
        return _retry_interior()

    resid = sp.expand(q - assemble())
    if resid != 0:
        if verbose:
            print('  residual nonzero after exact solve')
        return _retry_interior()

    # ---------------- exact PSD checks ----------------
    for mi, M in enumerate(Gr):
        if not ldl_psd_check(M):
            if verbose:
                print(f'  Gram {mi} not exactly PSD after rounding')
            return _retry_interior()

    return {'vars': [sp.srepr(v) for v in vars_],
            'gens': [sp.srepr(sp.expand(g)) for g in gens],
            'eqs': [sp.srepr(sp.expand(h)) for h in eqs],
            'bases': [[sp.srepr(m) for m in b] for b in bases],
            'grams': [[[sp.srepr(M[k, l]) for l in range(M.shape[1])]
                       for k in range(M.shape[0])] for M in Gr],
            'lam_bases': [[sp.srepr(m) for m in lb] for lb in lam_bases],
            'lams': [[sp.srepr(v) for v in lr] for lr in lam_r],
            'poly': sp.srepr(q)}


def verify_sos(cert):
    """standalone exact re-check of a certificate produced above"""
    vars_ = [sp.sympify(v) for v in cert['vars']]
    gens = [sp.sympify(g) for g in cert['gens']]
    eqs = [sp.sympify(h) for h in cert['eqs']]
    q = sp.sympify(cert['poly'])
    all_polys = [sp.Integer(1)] + gens
    tot = sp.Integer(0)
    for mi, (bss, gm) in enumerate(zip(cert['bases'], cert['grams'])):
        b = [sp.sympify(m) for m in bss]
        M = sp.Matrix([[sp.sympify(gm[k][l]) for l in range(len(b))]
                       for k in range(len(b))])
        if not ldl_psd_check(M):
            return False, f'gram {mi} not PSD'
        for k in range(len(b)):
            for l in range(len(b)):
                tot += M[k, l] * all_polys[mi] * b[k] * b[l]
    for lj, (lbs, lvs) in enumerate(zip(cert['lam_bases'], cert['lams'])):
        for m, v in zip(lbs, lvs):
            tot += sp.sympify(v) * eqs[lj] * sp.sympify(m)
    if sp.expand(q - tot) != 0:
        return False, 'identity fails'
    return True, 'ok'


def suggest_squares(q, vars_, gens=(), deg=2, tol=1e-4, den=256,
                    schmudgen=True):
    """Run the min-trace stage-1 SDP only and return the dominant Gram
    eigen-directions as exact polynomials over Q(sqrt3), for use as
    auxiliary square generators in the exact Handelman LP (whose vertex
    reconstruction avoids PSD rounding entirely)."""
    import cvxpy as cp
    q = sp.expand(q)
    gens = [sp.expand(g) for g in gens]
    if schmudgen:
        base_g = list(gens)
        for i in range(len(base_g)):
            for j in range(i, len(base_g)):
                pg = sp.expand(base_g[i] * base_g[j])
                if sp.total_degree(pg.subs(R3, 2), *vars_) <= 2 * deg:
                    gens.append(pg)
    bases = [monomials(vars_, deg)]
    for g in gens:
        dg = sp.total_degree(sp.expand(g).subs(R3, 2), *vars_)
        bases.append(monomials(vars_, max(0, deg - (dg + 1) // 2)))
    r3f = float(R3)
    As = [cp.Variable((len(b), len(b)), symmetric=True) for b in bases]
    Bs = [cp.Variable((len(b), len(b)), symmetric=True) for b in bases]
    tgt = poly_coeff_map(q, vars_)
    all_polys = [sp.Integer(1)] + gens
    entry_maps = []
    for mi, b in enumerate(bases):
        emap = {}
        for k in range(len(b)):
            for l in range(k, len(b)):
                emap[(k, l)] = poly_coeff_map(
                    sp.expand(all_polys[mi] * b[k] * b[l]), vars_)
        entry_maps.append(emap)
    keys = set(tgt)
    for emap in entry_maps:
        for mm in emap.values():
            keys |= set(mm)
    monos = sorted({mono for (mono, tag) in keys})
    cons = []
    for mono in monos:
        er, ei = 0, 0
        for mi, emap in enumerate(entry_maps):
            for (k, l), mm in emap.items():
                c0 = float(mm.get((mono, 0), 0))
                c1 = float(mm.get((mono, 1), 0))
                if c0 == 0 and c1 == 0:
                    continue
                mult = 1 if k == l else 2
                er += mult * (c0 * As[mi][k, l] + 3 * c1 * Bs[mi][k, l])
                ei += mult * (c1 * As[mi][k, l] + c0 * Bs[mi][k, l])
        cons.append(er == float(tgt.get((mono, 0), 0)))
        cons.append(ei == float(tgt.get((mono, 1), 0)))
    bigM = max(100.0, 10.0 * max(
        (abs(float(v)) for v in tgt.values()), default=1.0))
    tr = 0
    for mi in range(len(bases)):
        cons.append(As[mi] + r3f * Bs[mi] >> 0)
        cons.append(cp.abs(As[mi]) <= bigM)
        cons.append(cp.abs(Bs[mi]) <= bigM)
        tr = tr + cp.trace(As[mi]) + r3f * cp.trace(Bs[mi])
    prob = cp.Problem(cp.Minimize(tr), cons)
    try:
        prob.solve(solver=cp.MOSEK, verbose=False)
    except Exception:
        return []
    if prob.status not in ('optimal', 'optimal_inaccurate'):
        return []
    out = []
    seen = set()
    for mi, b in enumerate(bases):
        Gv = As[mi].value + r3f * Bs[mi].value
        Gv = (Gv + Gv.T) / 2
        w_, V_ = np.linalg.eigh(Gv)
        top = max(w_.max(), 1.0)
        for j in range(len(b)):
            if w_[j] > tol * top:
                v = V_[:, j]
                piv = int(np.argmax(np.abs(v)))
                v = v / v[piv]
                lf = sum(round_q3(float(v[k]), den, den) * b[k]
                         for k in range(len(b)))
                lf = sp.expand(lf)
                key = sp.srepr(lf)
                if key not in seen and lf != 0:
                    seen.add(key)
                    out.append(lf)
    return out
