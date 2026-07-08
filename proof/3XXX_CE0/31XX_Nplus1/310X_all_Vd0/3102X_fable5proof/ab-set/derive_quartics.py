"""Exact symbolic derivations for the ab-set: EP curve parametrizations,
implicit quartics, corner points, case thresholds."""
import sympy as sp

a, b, X, Y, t = sp.symbols('a b X Y t', real=True)
c, s = sp.symbols('c s', real=True)  # cos(phi), sin(phi)
h = sp.sqrt(3) / 2

O_ = sp.Matrix([0, 0])
A_ = sp.Matrix([-a / 2, sp.sqrt(3) * a / 2])
B_ = sp.Matrix([b, 0])
PTS = {'O': O_, 'A': A_, 'B': B_}


def u_of(k):
    """unit normal u(phi + 120k) in terms of c=cos phi, s=sin phi"""
    ck = sp.cos(2 * sp.pi * k / 3)
    sk = sp.sin(2 * sp.pi * k / 3)
    return sp.Matrix([c * ck - s * sk, s * ck + c * sk])


def ep_param(Qn, Q2n, chir):
    """symbolic parametrization of EP curve (x at vertex S0∩S1, Q on shared
    side (side1 if chir==1 else side0), Q2 on side2). Returns (x(c,s), y(c,s))."""
    Q = PTS[Qn]
    Q2 = PTS[Q2n]
    u0, u1, u2 = u_of(0), u_of(1), u_of(2)
    c2 = (Q2.T * u2)[0]
    if chir == 1:
        c1 = (Q.T * u1)[0]
        c0 = h - c1 - c2
    else:
        c0 = (Q.T * u0)[0]
        c1 = h - c0 - c2
    M = sp.Matrix([[u0[0], u0[1]], [u1[0], u1[1]]])
    xy = M.solve(sp.Matrix([c0, c1]))
    return sp.simplify(sp.expand_trig(sp.expand(xy[0]))), \
        sp.simplify(sp.expand_trig(sp.expand(xy[1])))


def implicitize(xp, yp):
    """eliminate c,s (with c^2+s^2=1) from X=xp, Y=yp."""
    p1 = sp.expand(sp.together(X - xp))
    p2 = sp.expand(sp.together(Y - yp))
    p3 = c**2 + s**2 - 1
    gb = sp.groebner([sp.numer(sp.together(p1)), sp.numer(sp.together(p2)),
                      p3], c, s, X, Y, order='lex')
    # the elimination ideal: polys free of c,s
    elim = [g for g in gb.exprs if not (g.has(c) or g.has(s))]
    return elim


if __name__ == '__main__':
    for (Qn, Q2n, ch) in [('B', 'O', 0), ('A', 'O', 1), ('B', 'A', 0),
                          ('A', 'B', 1)]:
        xp, yp = ep_param(Qn, Q2n, ch)
        print(f'--- EP {Qn}|{Q2n} c{ch}:')
        print('  x(phi) =', sp.simplify(xp))
        print('  y(phi) =', sp.simplify(yp))
        el = implicitize(xp, yp)
        for e in el:
            print('  implicit:', sp.factor(sp.expand(e)))
