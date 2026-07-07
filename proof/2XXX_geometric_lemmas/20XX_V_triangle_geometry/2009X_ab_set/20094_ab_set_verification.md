# ab-set: verification summary

Status: Empirical

This file summarizes the machine verification of the case tables in
[`20092_ab_set_case_catalog.md`](20092_ab_set_case_catalog.md)
(script: [`2009X_computation/verify_ab_set.py`](2009X_computation/verify_ab_set.py);
supporting exact-algebra scripts developed during the derivation:
tangency/threshold identities re-derived in sympy).

## Method

Ground truth is computed from first principles only:
a point $x$ lies in the union $U$ of unit equilateral triangles containing $\{A,O,B\}$ iff
$\min_\varphi F_{\{A,O,B,x\}}(\varphi)\le\frac{\sqrt3}{2}$ (Viviani fitting criterion, proved in
[`20093_ab_set_proofs.md`](20093_ab_set_proofs.md) §1). For each direction $\theta$ the boundary radius
$r^*(\theta)=\max_{\varphi\in\Phi}\rho_\varphi(\theta)$ is evaluated by *exact* inversion of the
piecewise-linear-in-$r$ equation $\sum_k\max(m_k,rc_k)=\frac{\sqrt3}2$ per orientation, maximized
over a fine orientation grid with golden-section refinement **and** the exact $\Phi$-endpoints
added (where $\rho_\varphi$ jumps). Accuracy of $r^*$: ~$10^{-12}$ (validated against closed-form
points, e.g. circle points, to $10^{-14}$).

Checked per sample $(a,b)$:

1. **Chain identity** — the maximal-arc decomposition of $\{(\theta,r^*(\theta))\}$ (1500–5000
   directions) matches the claimed counterclockwise arc list of the case containing $(a,b)$;
2. **Curve residuals** — every boundary sample point lies on its claimed algebraic curve
   (gradient-normalized residual $<10^{-7}$; observed residuals are at machine precision,
   $\sim10^{-15}$, except on quartic arcs where the normalization dominates, still $<10^{-9}$);
3. **Corner identities** — $P_1\in c_A\cap L_A\cap E_{AO}$, $P_2\in L_A\cap E_{BA}\cap E_{BO}$,
   $P_2'\in L_B\cap E_{AB}\cap E_{AO}$, $P_3\in L_B\cap c_B\cap E_{BO}$, $B^*\in c_A$
   (residuals $<10^{-9}$); the tangency/threshold identities ($a=\frac12$, $b=\frac12$,
   $\sigma=\frac12$, $w_\pm$, $\mathcal E$, $\mathcal G$, $(3+a)R^2-3$) were derived and verified
   *exactly* in sympy during the derivation (see
   [`20093_ab_set_proofs.md`](20093_ab_set_proofs.md), Appendix).

## Region audit (predicate implications used to prune the case tables)

Verified on a $400\times400$ grid over $\{a,b\in(0,1],\ R\le1\}$ — all with **zero violations**:

| audit | statement |
|---|---|
| A2 | in bands I–III at least one of $w_\pm>0$ |
| A3 | within bands II–III never $\mathcal G(a,b)>0\wedge\mathcal G(b,a)>0$ |
| A5 | band III, $a>b$: $(3+a)R^2>3\Rightarrow\mathcal G(a,b)>0$ (case "$M_A$ without $\lambda_B$" empty) |
| A6 | band I, $a\ge\frac12\Rightarrow w_+>0\wedge w_-\le0$ |
| A7 | band II excludes $\sigma<\frac12$ |
| A9 | band II: flush lines only in rows II.1/II.1′ |
| (extra) | band III, $a>b$: $\mathcal G(b,a)>0$ never; and $a>\frac12>b$ always ($700^2$ grid) |

## Independent structural cross-check

During the derivation, a $21\times21$ parameter sweep (254 admissible points) was classified by a
*pattern-based* method (contact patterns of the critical triangle at the maximizing orientation,
independent of the curve equations); the predicted chains agreed at 242/254 points exactly, and at
the remaining 12 points the discrepancy was demonstrated to be sub-resolution arcs
(e.g. at $(0.848,0.040)$ the flank segment $s_B^{\mathrm{out}}$ has angular extent
$0.36^\circ$ and is present at higher resolution exactly as claimed) or points within $2\cdot10^{-3}$
of a threshold curve.

Additional targeted confirmations:

* $\eta$-threshold: bisection along $a=0.135$ located the appearance of the $L_B$ arc at
  $b=0.272251\ldots$, where the real roots of $\mathcal D_B$, $\mathcal C_B$ coincide to
  $2\cdot10^{-16}$ and $\mathcal E(a,b)=-5.6\cdot10^{-17}$;
* case I.1c verified at $(0.24,0.255)$: ten-arc chain
  $c_A,E_{AO},L_A,E_{BA},E_{BO},E_{AO},E_{AB},L_B,E_{BO},c_B$;
* mid-gap corner formulas $V=A+u(r_2-90^\circ)$, $\widetilde V=A+u(r_3-90^\circ)$ confirmed at
  $(0.85,0.10)$ to $10^{-6}$ (numeric corner localization) and exactly (on-circle/on-line
  identities);
* band-IV vertex formulas $V=A+u(\varphi_+-90^\circ)$, $V'=B+u(\varphi_-+90^\circ)$ confirmed at
  $(0.7,0.4)$;
* $R\to1$ degeneration ($(0.85,0.25)$, $R=0.99875$): boundary = two extreme-triangle segments
  through $A$ and $B$ (+ tiny circle arcs), converging to the base $[A,B]$.

## Per-case boundary verification

At least one interior sample of **every** case region of
[`20092_ab_set_case_catalog.md`](20092_ab_set_case_catalog.md) was verified — the numerically
computed boundary (from the support-function ground truth) consists of exactly the claimed arcs in
the claimed counterclockwise order, and every sampled boundary point lies on its claimed curve. The
column "res" is the maximum over the sample's directions of the gradient-normalized residual to the
claimed curve (tolerance $10^{-7}$; observed values are essentially machine precision).

| $(a,b)$ | case | arcs | max res |
|---|---|---|---|
| $(1.00,0.90)$ | 0 (empty) | — ($\min_\varphi F>h$) | — |
| $(0.05,0.05)$, $(0.10,0.08)$ | I.1 | 8 | $1.8\times10^{-15}$ |
| $(0.26,0.2346)$ | I.1a | 10 | $2.1\times10^{-15}$ |
| $(0.2346,0.26)$ | I.1b | 10 | $1.9\times10^{-15}$ |
| $(0.24,0.255)$, $(0.255,0.24)$ | I.1c | 10 | $2.1\times10^{-15}$ |
| $(0.25,0.15)$, $(0.10,0.08)$ | I.2 | 5 | $2.2\times10^{-15}$ |
| $(0.15,0.25)$ | I.2′ | 5 | $1.4\times10^{-15}$ |
| $(0.372,0.087)$, $(0.40,0.05)$ | I.3 | 6 | $4.7\times10^{-15}$ |
| $(0.087,0.372)$ | I.3′ | 6 | $1.5\times10^{-15}$ |
| $(0.35,0.35)$, $(0.42,0.42)$ | I.4 | 8 | $3.4\times10^{-15}$ |
| $(0.42,0.35)$ | I.5 | 5 | $2.3\times10^{-15}$ |
| $(0.35,0.42)$ | I.5′ | 5 | $1.8\times10^{-15}$ |
| $(0.60,0.20)$, $(0.55,0.15)$, $(0.5,0.0)$ | I.6 | 4 | $2.4\times10^{-15}$ |
| $(0.20,0.60)$, $(0.0,0.5)$ | I.6′ | 4 | $1.9\times10^{-15}$ |
| $(0.55,0.40)$ | II.1 | 7 | $2.2\times10^{-15}$ |
| $(0.753,0.183)$ | II.1 + $\lambda_B$ | 8 | $5.2\times10^{-15}$ |
| $(0.40,0.55)$ | II.1′ | 7 | $2.2\times10^{-15}$ |
| $(0.183,0.753)$ | II.1′ + $\lambda_A$ | 8 | $4.6\times10^{-15}$ |
| $(0.45,0.45)$ | II.2 | 9 | $3.5\times10^{-15}$ |
| $(0.467,0.42)$, $(0.48,0.40)$ | II.3 | 7 | $5.7\times10^{-15}$ |
| $(0.40,0.48)$ | II.3′ | 7 | $6.1\times10^{-15}$ |
| $(0.86,0.02)$ | III.1 | 10 | $\sim10^{-14}$ |
| $(0.875,0.002)$ | III.1 (near-degenerate $b\to0$) | (merge) | $2.1\times10^{-13}$ |
| $(0.80,0.135)$, $(0.70,0.28)$ | III.2 | 11 | $7.5\times10^{-15}$ |
| $(0.135,0.80)$ | III.2′ | 11 | $6.7\times10^{-15}$ |
| $(0.85,0.10)$, $(0.90,0.05)$ | III.4 | 11 | $4.9\times10^{-15}$ |
| $(0.0,0.90)$ | III.4′ | (degenerate merge) | $7.6\times10^{-13}$ |
| $(0.70,0.40)$, $(0.60,0.55)$, $(0.85,0.25)$ | IV | 4 | $3.2\times10^{-15}$ |
| $(0.0,0.0)$ | I.2′ (all curves $\to$ unit circle) | (degenerate merge) | $1.6\times10^{-15}$ |

("degenerate merge": at $a=0$ or $b=0$ several claimed curves coincide — e.g. at $a=0$, $c_A$,
$E_{AO}$ and the unit circle are one curve and some arcs have length $0$ — so the arc-name
_sequence_ is ill-posed; the check then confirms every boundary point lies on a claimed curve and
the realized arcs form an admissible sub-list. The near-degenerate point $(0.875,0.002)$ is the
$b\to0$ tip of the III.1 sliver: its two $s_B$ pieces are present but too short to resolve at fixed
angular sampling, so it too is accepted under the sub-list rule; the interior III.1 point
$(0.86,0.02)$ resolves all ten arcs exactly. Separately, as $R\to1$ (band IV, e.g. $(0.85,0.25)$)
the two circular arcs shrink to the points $B,A$ and the two extreme segments approach the base
$[A,B]$.)

The exact run log is produced by `python3 2009X_computation/verify_ab_set.py` (region audit + corner identities +
the per-case table above). Every sample passes.
