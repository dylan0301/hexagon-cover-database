r"""Numerical laboratory for the hexagonal hole set.

Setup (prompts/hole-set-noncover.md): H = regular hexagon, vertices
V_k = u(60k deg), k = 0..5. On edge V_i V_{i+1} sits the split point
p_i = q_{i+1} with |V_i p_i| = a_i, |V_{i+1} p_i| = b_{i+1} = 1 - a_i.
At each vertex V_i the ab-set K_i = K(a_i, b_i) (catalog: ab_set.md) is
placed with apex O at V_i, the "B" ray toward V_{i-1} (length b_i) and the
"A" ray toward V_{i+1} (length a_i).  The local catalog frame is
*orientation-reversing*:  global = V_i + X u(beta_i) + Y u(beta_i - 90deg),
beta_i = 240deg + 60deg*i  (direction V_i -> V_{i-1}).

Hole:  S = H \ (K_0 ∪ ... ∪ K_5).

Standing assumptions: a_0 > a_1 > ... > a_5 (all in (0,1)) and
R_0^2 = a_0^2 + a_0 b_0 + b_0^2 <= 1 with b_0 = 1 - a_5.

This module provides membership tests, boundary tracing, hole support
function / fitting functional F_S, and plotting.  Numerical only — the
proof-quality artifacts live elsewhere.
"""
import numpy as np

import verify_ab_set as V  # exact per-orientation radial solver etc.

RT3 = np.sqrt(3.0)
HCONST = RT3 / 2
TAU = 2 * np.pi
D = np.pi / 180


def u(deg):
    t = np.asarray(deg, float) * D
    return np.stack([np.cos(t), np.sin(t)], axis=-1)


VERT = u(60.0 * np.arange(6))          # V_0..V_5
BETA = 240.0 + 60.0 * np.arange(6)      # local +X direction (toward V_{i-1})
EX = u(BETA)                            # local x-axis in global coords
EY = u(BETA - 90.0)                     # local y-axis in global coords


def admissible(avec, tol=0.0):
    a = np.asarray(avec, float)
    if a.shape != (6,):
        return False, 'need 6 parameters'
    if not np.all(a > tol) or not np.all(a < 1 - tol):
        return False, 'a_i out of (0,1)'
    if not np.all(np.diff(a) < -tol):
        return False, 'need strict descent a_0 > ... > a_5'
    b0 = 1 - a[5]
    R02 = a[0] ** 2 + a[0] * b0 + b0 ** 2
    if R02 > 1 + tol:
        return False, f'R_0^2 = {R02:.6f} > 1'
    return True, 'ok'


class Hole:
    def __init__(self, avec, bvec=None, check=True):
        """bvec=None: the standard hole (b_i = 1 - a_{i-1}, standing
        assumptions enforced).  Explicit bvec: any per-vertex ab-sets
        (used for the reduced/relaxed holes)."""
        self.a = np.asarray(avec, float)
        if bvec is None:
            if check:
                ok, msg = admissible(avec, tol=-1e-12)
                if not ok:
                    raise ValueError(msg)
            self.b = np.array([1 - self.a[(i - 1) % 6] for i in range(6)])
        else:
            self.b = np.asarray(bvec, float)
        self.sigma = self.a + self.b
        self.R2 = self.a ** 2 + self.a * self.b + self.b ** 2

    # ---------------- frames ----------------
    def to_local(self, i, xy):
        """global (N,2) -> catalog frame of K_i"""
        d = np.asarray(xy, float) - VERT[i]
        return np.stack([d @ EX[i], d @ EY[i]], axis=-1)

    def to_global(self, i, XY):
        XY = np.asarray(XY, float)
        return (VERT[i] + XY[..., :1] * EX[i][None, :]
                + XY[..., 1:] * EY[i][None, :]) if XY.ndim > 1 else (
            VERT[i] + XY[0] * EX[i] + XY[1] * EY[i])

    # ---------------- membership ----------------
    def Fmin_local(self, i, XY, nphi=1024, iters=48):
        """min_phi F_{A,O,B,x}(phi) for x in catalog frame of K_i.
        XY: (N,2). Returns (N,) array."""
        a, b = self.a[i], self.b[i]
        P = V.pts_of(a, b)                     # rows O, A, B
        XY = np.atleast_2d(np.asarray(XY, float))
        N = len(XY)
        phis = np.linspace(0, TAU / 3, nphi, endpoint=False)

        def Fval(phi_arr):
            # phi_arr: (N, M) -> F for each point at each phi
            tot = np.zeros_like(phi_arr)
            for k in range(3):
                th = phi_arr + TAU * k / 3
                c, s = np.cos(th), np.sin(th)
                m = np.max(P[:, 0][:, None, None] * c[None]
                           + P[:, 1][:, None, None] * s[None], axis=0)
                px = XY[:, 0][:, None] * c + XY[:, 1][:, None] * s
                tot += np.maximum(m, px)
            return tot

        Fg = Fval(np.broadcast_to(phis, (N, nphi)).copy())
        j = np.argmin(Fg, axis=1)
        dph = (TAU / 3) / nphi
        lo = phis[j] - 1.5 * dph
        hi = phis[j] + 1.5 * dph
        gr = (np.sqrt(5) - 1) / 2
        for _ in range(iters):
            c1 = hi - gr * (hi - lo)
            c2 = lo + gr * (hi - lo)
            f1 = Fval(c1[:, None])[:, 0]
            f2 = Fval(c2[:, None])[:, 0]
            m1 = f1 < f2
            hi = np.where(m1, c2, hi)
            lo = np.where(m1, lo, c1)
        best = Fval(((lo + hi) / 2)[:, None])[:, 0]
        return np.minimum(best, Fg[np.arange(N), j])

    def in_K(self, i, xy, tol=1e-9, nphi=1024):
        """membership of global points in K_i (True = inside, incl. bdry tol)"""
        XY = self.to_local(i, np.atleast_2d(xy))
        ang = np.degrees(np.arctan2(XY[:, 1], XY[:, 0]))
        r = np.hypot(XY[:, 0], XY[:, 1])
        incone = ((ang >= -1e-11) & (ang <= 120 + 1e-11)) | (r < 1e-13)
        res = np.zeros(len(XY), bool)
        if incone.any():
            f = self.Fmin_local(i, XY[incone], nphi=nphi)
            res[incone] = f <= HCONST + tol
        return res

    def in_hex(self, xy, tol=1e-12):
        xy = np.atleast_2d(xy)
        # hexagon with vertices VERT: edges midpoint normals u(30+60k), support h
        ok = np.ones(len(xy), bool)
        for k in range(6):
            n = u(30.0 + 60 * k)
            ok &= (xy @ n) <= HCONST + tol
        return ok

    def in_hole(self, xy, tol=1e-9, nphi=1024):
        """strictly-in-hole test (up to tol): in hexagon and in no K_i"""
        xy = np.atleast_2d(xy)
        res = self.in_hex(xy)
        for i in range(6):
            if res.any():
                res &= ~self.in_K(i, xy, tol=-tol, nphi=nphi)
        return res

    # ---------------- boundary tracing ----------------
    def trace_K(self, i, ntheta=600, m=6000):
        """polyline of the chain Gamma of K_i (catalog frame radial scan),
        returned in *global* coordinates, plus local (theta, r) arrays."""
        a, b = self.a[i], self.b[i]
        P = V.pts_of(a, b)
        roots = V.extreme_phis(a, b, m=40000)
        ths = np.linspace(1e-7, TAU / 3 - 1e-7, ntheta)
        rs = rstar_grid(ths, P, roots, m=m)
        XY = np.stack([rs * np.cos(ths), rs * np.sin(ths)], axis=1)
        return self.to_global(i, XY), ths, rs

    def hole_boundary_points(self, ntheta=600, m=6000, tol=1e-8):
        """points of ∂K_i chains that lie in H and in no other K_j:
        candidate support points of the hole closure."""
        pts = []
        tags = []
        traces = []
        for i in range(6):
            g, ths, rs = self.trace_K(i, ntheta=ntheta, m=m)
            traces.append((g, ths, rs))
        for i in range(6):
            g = traces[i][0]
            keep = self.in_hex(g, tol=1e-9)
            for j in range(6):
                if j == i or not keep.any():
                    continue
                keep &= ~self.in_K(j, g, tol=-tol)
            pts.append(g[keep])
            tags += [i] * int(keep.sum())
        return np.vstack(pts), np.array(tags), traces

    # ---------------- fitting functional ----------------
    @staticmethod
    def F_of_points(pts, phis):
        """F_S over the point cloud pts at orientations phis (deg allowed via
        radians input); phis in radians, shape (M,)"""
        tot = np.zeros_like(phis)
        for k in range(3):
            th = phis + TAU * k / 3
            nvec = np.stack([np.cos(th), np.sin(th)], axis=0)
            tot += (pts @ nvec).max(axis=0)
        return tot

    def F_S(self, phis_deg=None, ntheta=600, m=6000, pts=None):
        if pts is None:
            pts, _, _ = self.hole_boundary_points(ntheta=ntheta, m=m)
        if phis_deg is None:
            phis_deg = np.linspace(0, 120, 481)
        phis = np.asarray(phis_deg, float) * D
        return phis_deg, self.F_of_points(pts, phis), pts

    def min_F_S(self, ntheta=600, m=6000, pts=None, refine=True):
        phis_deg, F, pts = self.F_S(ntheta=ntheta, m=m, pts=pts)
        j = int(np.argmin(F))
        lo, hi = (phis_deg[j] - 0.5) * D, (phis_deg[j] + 0.5) * D
        gr = (np.sqrt(5) - 1) / 2
        if refine:
            for _ in range(60):
                c1, c2 = hi - gr * (hi - lo), lo + gr * (hi - lo)
                f1 = self.F_of_points(pts, np.array([c1]))[0]
                f2 = self.F_of_points(pts, np.array([c2]))[0]
                if f1 < f2:
                    hi = c2
                else:
                    lo = c1
        phim = (lo + hi) / 2
        return (self.F_of_points(pts, np.array([phim]))[0], phim / D, pts)


def rho_grid(thetas, phis, P):
    """rho_phi(theta) on the full (ntheta, m) grid — vectorized port of
    verify_ab_set.rho_of."""
    m = len(phis)
    nt = len(thetas)
    C = np.zeros((nt, m, 3))
    G = np.zeros((m, 3))
    for k in range(3):
        th = phis + TAU * k / 3
        uv = np.stack([np.cos(th), np.sin(th)], 0)
        G[:, k] = (P @ uv).max(0)
        C[:, :, k] = np.cos(thetas[:, None] - th[None, :])
    F0 = G.sum(1)                                   # (m,)
    feas = F0 <= HCONST + 1e-15                     # (m,)
    rho = np.full((nt, m), -np.inf)
    with np.errstate(divide='ignore', invalid='ignore'):
        KN = np.where(C > 1e-15, G[None, :, :] / C, np.inf)   # (nt,m,3)
    KNs = np.sort(KN, axis=2)
    for j in range(4):
        lo = np.zeros((nt, m)) if j == 0 else KNs[:, :, j - 1].copy()
        lo = np.maximum(lo, 0.0)
        lo = np.where(np.isfinite(lo), lo, 1e18)
        hi = KNs[:, :, j] if j < 3 else np.full((nt, m), np.inf)
        act = KN <= lo[:, :, None] * (1 + 1e-12) + 1e-15
        slope = (C * act).sum(2)
        Flo = F0[None, :] + (act * (lo[:, :, None] * C - G[None])).sum(2)
        ok = feas[None, :] & (Flo <= HCONST + 1e-15)
        with np.errstate(divide='ignore', invalid='ignore'):
            rc = np.where(slope > 1e-15, lo + (HCONST - Flo) / slope, np.inf)
        rc = np.minimum(rc, hi)
        rho = np.where(ok & (rc >= lo - 1e-15), np.maximum(rho, rc), rho)
    return rho


def rstar_grid(thetas, P, roots, m=6000):
    """r*(theta) for an array of thetas: max over a phi grid (+ inserted
    Phi endpoints) of rho_phi(theta), with a golden refinement pass around
    the grid argmax."""
    phis = np.linspace(0, TAU / 3, m, endpoint=False)
    if roots:
        extra = np.array([rr + s for rr in roots
                          for s in (0., 1e-13, -1e-13)]) % (TAU / 3)
        phis = np.concatenate([phis, extra])
    rho = rho_grid(np.asarray(thetas, float), phis, P)
    j = np.argmax(rho, axis=1)
    r0 = rho[np.arange(len(thetas)), j]
    p0 = phis[j]
    dph = (TAU / 3) / m
    lo, hi = p0 - 2.5 * dph, p0 + 2.5 * dph
    gr = (np.sqrt(5) - 1) / 2

    def rho_at(pv):
        out = np.empty(len(thetas))
        for t in range(len(thetas)):
            out[t] = rho_grid(np.array([thetas[t]]), np.array([pv[t]]), P)[0, 0]
        return out

    # vectorized golden refinement (all thetas at once, one phi per theta)
    for _ in range(70):
        c1 = hi - gr * (hi - lo)
        c2 = lo + gr * (hi - lo)
        f1 = _rho_diag(thetas, c1, P)
        f2 = _rho_diag(thetas, c2, P)
        m1 = f1 > f2
        hi = np.where(m1, c2, hi)
        lo = np.where(m1, lo, c1)
    rref = _rho_diag(thetas, (lo + hi) / 2, P)
    return np.maximum(r0, rref)


def _rho_diag(thetas, phis, P):
    """rho_{phis[t]}(thetas[t]) for paired arrays (diagonal evaluation)."""
    nt = len(thetas)
    C = np.zeros((nt, 3))
    G = np.zeros((nt, 3))
    for k in range(3):
        th = phis + TAU * k / 3
        uv = np.stack([np.cos(th), np.sin(th)], 0)
        G[:, k] = (P @ uv).max(0)
        C[:, k] = np.cos(thetas - th)
    F0 = G.sum(1)
    feas = F0 <= HCONST + 1e-15
    rho = np.full(nt, -np.inf)
    with np.errstate(divide='ignore', invalid='ignore'):
        KN = np.where(C > 1e-15, G / C, np.inf)
    KNs = np.sort(KN, 1)
    for j in range(4):
        lo = np.zeros(nt) if j == 0 else KNs[:, j - 1].copy()
        lo = np.maximum(lo, 0.0)
        lo = np.where(np.isfinite(lo), lo, 1e18)
        hi = KNs[:, j] if j < 3 else np.full(nt, np.inf)
        act = KN <= lo[:, None] * (1 + 1e-12) + 1e-15
        slope = (C * act).sum(1)
        Flo = F0 + (act * (lo[:, None] * C - G)).sum(1)
        ok = feas & (Flo <= HCONST + 1e-15)
        with np.errstate(divide='ignore', invalid='ignore'):
            rc = np.where(slope > 1e-15, lo + (HCONST - Flo) / slope, np.inf)
        rc = np.minimum(rc, hi)
        rho = np.where(ok & (rc >= lo - 1e-15), np.maximum(rho, rc), rho)
    return rho


def staircase(level, gaps=None, spread=0.01):
    """convenient admissible parameter vector: a_i ≈ level, descending.
    gaps: 5 positive gaps (a_i - a_{i+1}); default equal, total = spread."""
    if gaps is None:
        gaps = np.full(5, spread / 5)
    gaps = np.asarray(gaps, float)
    a0 = level + gaps.sum() / 2
    a = a0 - np.concatenate([[0], np.cumsum(gaps)])
    return a


def reduced_hole(s, t):
    """the 2-parameter reduced hole S~(s,t):  K_0 = K(t, 1-s) at V_0 and
    the five petals K(s, 1-t) at V_1..V_5.  By monotonicity
    (K decreasing in both arguments) S~ is contained in the true hole of
    every admissible staircase with a_5 = s, a_0 = t."""
    if not (0 <= s <= t <= 1):
        raise ValueError('need 0 <= s <= t <= 1')
    R02 = t * t + t * (1 - s) + (1 - s) ** 2
    if R02 > 1 + 1e-12:
        raise ValueError(f'R_0^2 = {R02:.6f} > 1: not in reduced region')
    a = np.array([t, s, s, s, s, s])
    b = np.array([1 - s] + [1 - t] * 5)
    return Hole(a, bvec=b)


if __name__ == '__main__':
    for lev, sp in [(0.05, 0.01), (0.2, 0.02), (0.5, 0.05), (0.8, 0.02)]:
        a = staircase(lev, spread=sp)
        ok, msg = admissible(a)
        print(f'level {lev}: {msg}; a = {np.round(a, 4)}')
        if not ok:
            continue
        hole = Hole(a)
        f, phi, pts = hole.min_F_S(ntheta=400, m=4000)
        print(f'  min F_S = {f:.6f}  (h = {HCONST:.6f}, margin '
              f'{f - HCONST:+.6f}) at phi = {phi:.3f} deg; '
              f'{len(pts)} boundary pts')
