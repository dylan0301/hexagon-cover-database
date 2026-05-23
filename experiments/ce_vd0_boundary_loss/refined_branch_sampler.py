import math
import random

TOL = 1e-10


def feasible_b(a, c, b, tol=TOL):
    if not (-tol <= a <= 1 + tol and -tol <= c <= 1 + tol and -tol <= b <= 1 - a + tol):
        return False
    u = a + b
    if a * a + a * b + b * b > 1 + tol:
        return False
    Delta = u ** 4 - u ** 2 + a * b
    p = min(a, b)
    q = max(a, b)
    cell1 = Delta <= tol and c ** 4 - c ** 2 + p * c - p * p <= tol
    cell2 = Delta >= -tol and ((u * u - 1) * c * c + q * c - q * q) <= tol
    return cell1 or cell2


def label(a, c, b):
    u = a + b
    Delta = u ** 4 - u ** 2 + a * b
    p = min(a, b)
    q = max(a, b)
    if abs(b - (1 - a)) < 1e-8 and c <= max(a, 1 - a) + 1e-8 and feasible_b(a, c, b):
        return "Full"
    if Delta <= 1e-7 and abs(c ** 4 - c ** 2 + p * c - p * p) < 1e-7 and feasible_b(a, c, b):
        return "L"
    E = ((u * u - 1) * c * c + q * c - q * q)
    if Delta >= -1e-7 and abs(E) < 1e-7 and feasible_b(a, c, b):
        if b <= a + 1e-8:
            return "T-"
        beta = b / c if c > 1e-12 else float("inf")
        disc = 4 * u * u - 3
        if disc >= -1e-9:
            bp = (1 + math.sqrt(max(0, disc))) / 2
            bm = (1 - math.sqrt(max(0, disc))) / 2
            return "T+hi" if abs(beta - bp) < abs(beta - bm) else "T+lo"
        return "T+?"
    return "other"


def candidates(a, c):
    vals = []
    b = 1 - a
    if feasible_b(a, c, b) and c <= max(a, 1 - a) + 1e-9:
        vals.append((label(a, c, b), b))

    disc = 4 * c * c - 3
    if disc >= -1e-12:
        b = c * (1 - math.sqrt(max(0, disc))) / 2
        if b <= a + 1e-8 and feasible_b(a, c, b):
            vals.append((label(a, c, b), b))

    A = c * c
    Bq = 2 * a * c * c
    Cq = (a * a - 1) * c * c + a * c - a * a
    if A > 1e-14:
        disc = Bq * Bq - 4 * A * Cq
        if disc >= -1e-12:
            for b in [(-Bq + math.sqrt(max(0, disc))) / (2 * A), (-Bq - math.sqrt(max(0, disc))) / (2 * A)]:
                if b <= a + 1e-8 and feasible_b(a, c, b):
                    vals.append((label(a, c, b), b))

    A = 1 - c * c
    Bq = -(2 * a * c * c + c)
    Cq = (1 - a * a) * c * c
    if abs(A) > 1e-14:
        disc = Bq * Bq - 4 * A * Cq
        if disc >= -1e-12:
            for b in [(-Bq + math.sqrt(max(0, disc))) / (2 * A), (-Bq - math.sqrt(max(0, disc))) / (2 * A)]:
                if b >= a - 1e-8 and feasible_b(a, c, b):
                    vals.append((label(a, c, b), b))

    out = []
    for lab, b in vals:
        if -1e-8 <= b <= 1 - a + 1e-8 and lab != "other":
            if not any(abs(b - b0) < 1e-7 for _, b0 in out):
                out.append((lab, b))
    return out


def B(a, c):
    vals = candidates(a, c)
    if not vals:
        return None, None
    lab, b = max(vals, key=lambda z: z[1])
    return b, lab


def c_feas(r, u, w):
    if r <= 1 or u <= 0 or w <= 0:
        return False
    s = 1 - u - w
    t = 1 - u
    if not (0 < s < t < 1):
        return False
    D = math.sqrt(r * r - r + 1)
    delta = 1 / (D + r)
    g1 = 1 - r * u
    g5 = u - delta - w / (r - 1)
    if not (0 <= g1 <= 1 and 0 <= g5 <= 1):
        return False
    if 2 * s > r + 1e-11:
        return False
    if r * u > 1 + 1e-11:
        return False
    if 1 - s + r * t > D + 1e-11:
        return False
    if 0.5 + r * (t - 0.5) < -1e-11:
        return False
    if 0.5 + r * t - s > D + 1e-11:
        return False
    return True


def sample(n=200000, cut=None):
    best = {}
    for _ in range(n):
        p = random.random()
        if p < 0.45:
            r = 1 + 10 ** random.uniform(-8, 5)
        elif p < 0.75:
            r = 1 + random.random() * 50
        else:
            R = random.uniform(1e-4, 0.999)
            r = 1 / R
        D = math.sqrt(r * r - r + 1)
        delta = 1 / (D + r)
        u = random.random() / r
        wmax = min(1 - u, (r - 1) * max(0, u - delta))
        if wmax <= 0:
            continue
        w = wmax * (random.random() ** 2 if random.random() < 0.6 else random.random())
        if not c_feas(r, u, w):
            continue
        s = 1 - u - w
        if cut:
            dE = abs(r - 1) + w
            dp = 1 / r + u
            dm = (r - 1) + s + w
            if min(dE, dp, dm) < cut:
                continue
        g1 = 1 - r * u
        g5 = u - 1 / (D + r) - w / (r - 1)
        B5, l5 = B(s, 1 - g5)
        B1, l1 = B(u, 1 - g1)
        if B5 is None or B1 is None:
            continue
        F = B5 + B1
        key = (l5, l1)
        if key not in best or F > best[key][0]:
            best[key] = (F, (r, u, w, s, 1 - u, g1, g5, B5, B1))
    return best


if __name__ == "__main__":
    for cut in [None, 0.05, 0.1]:
        print("CUT", cut)
        best = sample(200000, cut)
        for key, (F, data) in sorted(best.items(), key=lambda kv: -kv[1][0])[:20]:
            print(key, F, data)
