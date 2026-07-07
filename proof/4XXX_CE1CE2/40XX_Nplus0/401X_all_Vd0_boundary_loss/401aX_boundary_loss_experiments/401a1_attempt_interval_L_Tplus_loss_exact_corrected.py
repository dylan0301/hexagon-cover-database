from mpmath import iv, mp
mp.dps = 50
ETAMAX = 1 - 3 ** 0.5 / 2


def bnd(x):
    return float(x.a), float(x.b)


def ell_iv(eta):
    c = 1 - eta
    disc = 4 * c * c - 3
    lo, hi = bnd(disc)
    if hi < 0:
        return None
    return c * (1 - iv.sqrt(iv.mpf([max(0, lo), max(0, hi)]))) / 2


def eval_box(Rlo, Rhi, tlo, thi, elo, ehi, cut=0.0):
    R = iv.mpf([Rlo, Rhi])
    tau = iv.mpf([tlo, thi])
    eta = iv.mpf([elo, ehi])
    Aroot = iv.sqrt(1 - R + R * R)
    delta = R / (Aroot + 1)
    x = (1 + tau) / (1 + R)
    u = R * x
    # Corrected C-geometry formula: w=(1-R)(u-delta-eta)/R.
    w = (1 - R) * (u - delta - eta) / R
    s = 1 - u - w
    dplus = R + u
    dE = (1 - R) / R + w
    dminus = (1 - R) / R + s + w
    if cut > 0 and (bnd(dplus)[1] < cut or bnd(dE)[1] < cut or bnd(dminus)[1] < cut):
        return "cut", None
    cons = [R, 1 - R, tau, R - tau, eta, 1 - eta, x, 1 - x, u, w, s, 1 - 2 * R * s]
    cons.append(Aroot - (R * (1 - s) + (1 - u)))
    cons.append(R / 2 + (1 - u) - 0.5)
    cons.append(Aroot - (R / 2 + (1 - u) - R * s))
    cons.append(x - 0.5)
    for c0 in cons:
        if bnd(c0)[1] < 0:
            return "infeasible", None
    ell = ell_iv(eta)
    if ell is None:
        return "infeasible_ell", None
    if bnd(ell - s)[0] > 0:
        return "infeasible_order", None
    Delta = (s + ell) ** 4 - (s + ell) ** 2 + s * ell
    if bnd(Delta)[0] > 0:
        return "infeasible_delta", None
    h = ell - u
    if bnd(h)[1] < 0:
        return "ell_lt_u", None
    y = 1 - u
    Acoef = 2 * x * x - x + 2 * tau
    Bcoef = 1 - x * x
    Eh = y * tau - Acoef * h - Bcoef * h * h
    if bnd(Eh)[0] > 0:
        return "E_h_pos", (bnd(Eh)[0],)
    return "unresolved", (bnd(h), bnd(Eh), bnd(Delta), bnd(s), bnd(w), bnd(x), bnd(u), bnd(eta))


def run(max_depth=24, cut=0.0):
    stack = [(0.1, 0.999, 0.0, 0.999, 0.0, ETAMAX, 0)]
    counts = {}
    examples = []
    while stack:
        box = stack.pop()
        Rlo, Rhi, tlo, thi, elo, ehi, d = box
        status, info = eval_box(Rlo, Rhi, tlo, thi, elo, ehi, cut)
        counts[status] = counts.get(status, 0) + 1
        if status == "unresolved":
            if d >= max_depth:
                if len(examples) < 20:
                    examples.append((box, info))
            else:
                widths = [Rhi - Rlo, thi - tlo, ehi - elo]
                i = max(range(3), key=lambda k: widths[k])
                if i == 0:
                    m = (Rlo + Rhi) / 2
                    stack.append((Rlo, m, tlo, thi, elo, ehi, d + 1))
                    stack.append((m, Rhi, tlo, thi, elo, ehi, d + 1))
                elif i == 1:
                    m = (tlo + thi) / 2
                    stack.append((Rlo, Rhi, tlo, m, elo, ehi, d + 1))
                    stack.append((Rlo, Rhi, m, thi, elo, ehi, d + 1))
                else:
                    m = (elo + ehi) / 2
                    stack.append((Rlo, Rhi, tlo, thi, elo, m, d + 1))
                    stack.append((Rlo, Rhi, tlo, thi, m, ehi, d + 1))
    print(counts)
    for e in examples[:10]:
        print(e)


if __name__ == "__main__":
    run(24, 0.0)
