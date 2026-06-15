# Targets: Skeleton, Half-Skeleton, Lotus, Benzene

Status: Definition

## Skeleton

$$
S=\partial H\cup [V_0,V_3]\cup [V_1,V_4]\cup [V_2,V_5].
$$

## Half-skeleton

$$
S_{1/2}=\partial H\cup\{O,M_0,\dots,M_5\}.
$$

## Finite radial targets

For $0\le t\le 1$, define

$$
P_i(t)=(1-t)V_i.
$$

For a finite list $\mathbf t=(t_1,\dots,t_k)$, define

$$
S_{\mathbf t}=S_{1/2}\cup\{P_i(t_j):i=0,\dots,5,\ j=1,\dots,k\}.
$$

The current finite-point values are kept as decimals:

$$
0.382,\qquad 0.5,\qquad 0.634.
$$

Since

$$
P_i(0.5)=M_i,
$$

the $0.5$ layer is already included in $S_{1/2}$.

## Benzene

Let

$$
B_i=\frac{V_i+V_{i+1}}{3}.
$$

Then

$$
\mathrm{Benzene}=S\cup\{B_0,\dots,B_5\}.
$$

## Lotus

Let

$$
D_i=\{p:\|p-V_i\|\le 1\}.
$$

Let $A_i^-\subset \partial D_{i-1}$ and $A_i^+\subset \partial D_{i+1}$ be the two unit-circle arcs from $O$ to $V_i$. Define

$$
L_i=A_i^-\cup A_i^+.
$$

The lotus target is

$$
\mathrm{Lotus}=\partial H\cup\bigcup_{i=0}^5 L_i.
$$

It is a one-dimensional target, not the filled parity/XOR region.
