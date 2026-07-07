# Strict Supercritical $AB$-Union Corollary

Status: Proven

Let $A,O,B$ be three points with angle $120^\circ$ at $O$. Put

$$
A=ae_A,\qquad B=be_B,
$$

where $e_A$ and $e_B$ are unit directions with angle $120^\circ$, and let

$$
C=\{ue_A+ve_B:u\ge0,\ v\ge0\}.
$$

The local $AB$-union set is

$$
\mathcal U_{AB}(a,b)=C\cap\bigcup\{T:T\text{ is a closed unit equilateral triangle and }O,A,B\in T\}.
$$

If no such triangle exists, this union is empty.

This corollary records the exact non-axis frontier of $\mathcal U_{AB}(a,b)$ in
cone coordinates. It is the strict $\sigma=a+b>1$, $R^2<1$ specialization of
Band IV in
[`20092_ab_set_case_catalog.md`](20092_ab_set_case_catalog.md), with proof
inherited from
[`20093_ab_set_proofs.md`](20093_ab_set_proofs.md). In the notation below,
$\rho=R^2$.

## Corollary

Assume the strict branch

$$
a+b>1, \qquad \rho=a^2+ab+b^2<1.
$$

Work in cone coordinates

$$
x=ue_A+ve_B, \qquad u\ge0, \qquad v\ge0,
$$

where $e_A$ and $e_B$ are unit directions with angle $120^\circ$.  The metric is

$$
\lVert ue_A+ve_B\rVert^2=u^2+v^2-uv.
$$

Let

$$
A=(a,0), \qquad B=(0,b), \qquad h=\frac{\sqrt3}{2}, \qquad D=\sqrt{4\rho-3}.
$$

Define

$$
\alpha=\frac{h(a+2b-aD)}{2\rho}, \qquad \beta=\frac{h(a-b+(a+b)D)}{2\rho},
$$

$$
\gamma=\frac{h(-a+b+(a+b)D)}{2\rho}, \qquad \delta=\frac{h(2a+b-bD)}{2\rho},
$$

and

$$
\Omega=\alpha\delta-\gamma\beta= \frac{3(1-D)(D+3)}{16\rho}>0.
$$

The five junction points are

$$
P_0=\left(0,\frac{-a+\sqrt{4-3a^2}}{2}\right),
$$

$$
P_1=\left(a-\frac{\beta}{h},\frac{\alpha}{h}\right),
$$

$$
P_2=\left( \frac{\delta(a\alpha-b\beta)}{\Omega}, \frac{\alpha(b\delta-a\gamma)}{\Omega} \right),
$$

$$
P_3=\left(\frac{\delta}{h},b-\frac{\gamma}{h}\right),
$$

$$
P_4=\left(\frac{-b+\sqrt{4-3b^2}}{2},0\right).
$$

The curve is ordered as

$$
P_0\to P_1\to P_2\to P_3\to P_4.
$$

It is the union of four pieces:

$$
\Gamma_{AB}=\Gamma_A^{\mathrm{circ}}\cup\Gamma_A^{\mathrm{lin}} \cup\Gamma_B^{\mathrm{lin}}\cup\Gamma_B^{\mathrm{circ}}.
$$

The first piece is the circle arc centered at $A$:

$$
\Gamma_A^{\mathrm{circ}}: \quad (u-a)^2+v^2-(u-a)v=1,
$$

with branch

$$
v=\frac{u-a+\sqrt{4-3(u-a)^2}}{2}, \qquad 0\le u\le a-\frac{\beta}{h}.
$$

The second piece is the line segment from $P_1$ to $P_2$:

$$
\Gamma_A^{\mathrm{lin}}: \quad \alpha(u-a)+\beta v=0.
$$

Equivalently,

$$
v=\frac{\alpha}{\beta}(a-u).
$$

The third piece is the line segment from $P_2$ to $P_3$:

$$
\Gamma_B^{\mathrm{lin}}: \quad \gamma u+\delta(v-b)=0.
$$

Equivalently,

$$
v=b-\frac{\gamma}{\delta}u.
$$

The fourth piece is the circle arc centered at $B$:

$$
\Gamma_B^{\mathrm{circ}}: \quad u^2+(v-b)^2-u(v-b)=1,
$$

with branch

$$
v=b+\frac{u-\sqrt{4-3u^2}}{2}, \qquad \frac{-b+\sqrt{4-3b^2}}{2}\le u\le\frac{\delta}{h}.
$$

This last arc is traversed from $P_3$ to $P_4$, so $u$ decreases along the boundary orientation.

Thus the strict $a+b>1$ $AB$-union curve consists of exactly two unit-circle arcs and two line segments.

The endpoint chord of each line piece coincides with the line piece itself.  It is neither above nor below the corresponding boundary piece.

## Proof

Identify the cone-coordinate point $x=ue_A+ve_B$ with the Band IV coordinates
used in [`20092_ab_set_case_catalog.md`](20092_ab_set_case_catalog.md). The
Band IV chain there is

$$
c_A[B^*\to V]\to s_A^{\mathrm{IV}}\to s_B^{\mathrm{IV}}\to c_B[V'\to A^*].
$$

The two circle pieces become the circle equations centered at $A=(a,0)$ and
$B=(0,b)$ in the cone metric
$\lVert ue_A+ve_B\rVert^2=u^2+v^2-uv$. Solving the two Band IV extreme side
lines $s_A^{\mathrm{IV}}$ and $s_B^{\mathrm{IV}}$ in these cone coordinates
gives the displayed coefficients $\alpha,\beta,\gamma,\delta$ and their
intersection $P_2$; their intersections with the two circle arcs are $P_1$ and
$P_3$, while $P_0$ and $P_4$ are the cone-edge endpoints $A^*$ and $B^*$ in
these coordinates. The Band IV catalog proves that no other non-axis arcs
occur, and the proof file derives the extreme side lines from the endpoint
orientations. Hence the four-piece frontier above is exactly the strict
supercritical $AB$-union frontier.

The corollary assumes $\rho<1$. At $\rho=1$, one has $D=1$ and $\Omega=0$;
the nondegenerate four-piece formula must be replaced by its limiting
degeneration.
