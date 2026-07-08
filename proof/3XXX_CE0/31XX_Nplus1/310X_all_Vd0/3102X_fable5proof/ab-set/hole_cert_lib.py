r"""Exact library for the hole-set non-coverability proof.

Everything here is exact sympy over Q(sqrt3)(s,t).

Geometry (see prompts/hole-set-noncover.md and hole_set_noncover.md):
  hexagon H with vertices V_k = u(60k deg);
  reduced hole S~(s,t):  sliver K_0 = K(t, 1-s) at V_0,
  petals K_i = K(s, 1-t) at V_i, i=1..5.
  Local catalog frame at V_i:  global = V_i + X u(beta_i) + Y u(beta_i-90),
  beta_i = 240 + 60 i (deg); the map is orientation-reversing.

Key reductions implemented/verified here:
  * mirror symmetry  (s,t) <-> (1-t, 1-s);
  * monotonicity  K(a',b') subset K(a,b) for a'>=a, b'>=b  (proof in doc);
  * arc lemma: a linear functional >= h0 > 0 on an arc <= 180deg iff both
    endpoint values >= h0  (proof in doc);
  * membership machinery:  x in K(a,b) iff min_phi F_{A,O,B,x}(phi) <= h,
    F_{P}(phi) = sum_k max_{p in P} <p, u(phi+120k)>.

The certificates emitted by hole_cert_gen.py are lists of polynomial
inequalities in (s,t) over the leaf regions; verify_hole_noncover.py
re-checks them exactly.
"""
import sympy as sp

R3 = sp.sqrt(3)
H = R3 / 2
s, t = sp.symbols('s t', real=True)
HALF = sp.Rational(1, 2)


def u_deg(d):
    """exact unit vector for angle d in degrees (d rational: exact via
    sympy cos/sin of pi*d/180)"""
    a = sp.pi * sp.Rational(d) / 180
    return sp.Matrix([sp.cos(a), sp.sin(a)])


def rot(v, d):
    a = sp.pi * sp.Rational(d) / 180
    c, si = sp.cos(a), sp.sin(a)
    return sp.Matrix([c * v[0] - si * v[1], si * v[0] + c * v[1]])


def rot120(v, k=1):
    """exact rotation by 120k degrees"""
    return rot(v, 120 * (k % 3))


VERT = [sp.simplify(u_deg(60 * k)) for k in range(6)]
BETA = [240 + 60 * k for k in range(6)]
EX = [sp.simplify(u_deg(BETA[i] % 360)) for i in range(6)]
EY = [sp.simplify(u_deg((BETA[i] - 90) % 360)) for i in range(6)]


def to_global(i, XY):
    return sp.Matrix([VERT[i][0] + XY[0] * EX[i][0] + XY[1] * EY[i][0],
                      VERT[i][1] + XY[0] * EX[i][1] + XY[1] * EY[i][1]])


def to_local(i, g):
    d = sp.Matrix([g[0] - VERT[i][0], g[1] - VERT[i][1]])
    return sp.Matrix([d.dot(EX[i]), d.dot(EY[i])])


def ab_of(i):
    """catalog parameters (a,b) of the set at vertex i in the reduced hole"""
    return (t, 1 - s) if i == 0 else (s, 1 - t)


def AOB_local(i):
    """catalog points A=(a u(120)), O, B=(b,0) of the set at vertex i,
    local frame"""
    a, b = ab_of(i)
    A = sp.Matrix([-a / 2, R3 * a / 2])
    O = sp.Matrix([0, 0])
    B = sp.Matrix([b, 0])
    return A, O, B


def AOB_global(i):
    return tuple(to_global(i, P) for P in AOB_local(i))


# --------------------------------------------------------------------
# F-functional machinery (exact, for a finite point list)
# --------------------------------------------------------------------
def F_terms(points, k, c, sg):
    """list of <p, n_k> for p in points, with n_k = R_{120k} (c,sg)."""
    out = []
    for p in points:
        n = rot120(sp.Matrix([c, sg]), k)
        out.append(sp.expand(p[0] * n[0] + p[1] * n[1]))
    return out


def selection_vector(points_by_normal):
    """Given a choice sigma_k (one point per k=0,1,2), the selection lower
    bound  sum_k <sigma_k, R_{120k} u>  equals <w, u> with
    w = sum_k R_{-120k} sigma_k.  Returns w (2-vector, exact)."""
    w = sp.Matrix([0, 0])
    for k, p in enumerate(points_by_normal):
        w = w + rot(sp.Matrix([p[0], p[1]]), -120 * k)
    return sp.Matrix([sp.expand(w[0]), sp.expand(w[1])])


def endpoint_ineqs(w, d, h0=H):
    """Inequalities certifying <w, d/|d|> >= h0 for an (unnormalized,
    nonzero) direction d:  returns [<w,d>, <w,d>^2 - h0^2 |d|^2]; both
    must be >= 0.  (If d is exactly unit, the second alone with the
    first is still what we emit.)"""
    wd = sp.expand(w[0] * d[0] + w[1] * d[1])
    d2 = sp.expand(d[0] ** 2 + d[1] ** 2)
    return [wd, sp.expand(wd ** 2 - h0 ** 2 * d2)]


# --------------------------------------------------------------------
# region generators
# --------------------------------------------------------------------
def R0_sq():
    return sp.expand(t ** 2 + t * (1 - s) + (1 - s) ** 2)


def region_T_gens():
    """generators g >= 0 of the reduced admissible region
    (WLOG half s+t<=1)"""
    return {'s': s, 'ts': t - s, 'R0': sp.expand(1 - R0_sq()),
            'half': 1 - s - t}


# --------------------------------------------------------------------
# numeric helpers (for search only; proofs never rely on them)
# --------------------------------------------------------------------
def lambdify2(e):
    return sp.lambdify((s, t), e, 'numpy')
