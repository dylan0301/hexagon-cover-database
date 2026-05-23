# CE0 + Vd1/Vd2 Rhombus Geometry

Status: Proven local lemma

## Setup

Let $ABCD$ be a rhombus with side length

$$
L=1+\epsilon,
$$

and angles

$$
\angle DAB=\angle DCB=60^\circ,
\qquad
\angle ABC=\angle ADC=120^\circ.
$$

Let $X\in AD$ satisfy

$$
XD=x.
$$

Let $\triangle XYZ$ be a clockwise unit equilateral triangle containing $B$. Let the line $XZ$ meet the line $AB$ at $P$, and set

$$
\angle AXP=\theta.
$$

Let the line $YZ$ meet $AB$ at $N$ and segment $BC$ at $Q$.

## Formula for $PB$

In $\triangle AXP$,

$$
AX=L-x,
\qquad
\angle XAP=60^\circ,
\qquad
\angle AXP=\theta.
$$

Hence

$$
AP=(L-x)\frac{\sin\theta}{\sin(60^\circ+\theta)}.
$$

Since $PB=L-AP$,

$$
\boxed{PB=L-(L-x)\frac{\sin\theta}{\sin(60^\circ+\theta)}.}
$$

## Formula for $BQ$

The sine-rule computation through $\triangle PZN$ and $\triangle NBQ$ gives

$$
BQ=(PB-PN)\frac{\sin\theta}{\sin(60^\circ-\theta)},
$$

where

$$
PN=(1-XP)\frac{\sqrt3/2}{\sin\theta},
\qquad
XP=(L-x)\frac{\sqrt3/2}{\sin(60^\circ+\theta)}.
$$

After simplifying using

$$
\sin(60^\circ+\theta)\sin(60^\circ-\theta)=\frac34-\sin^2\theta,
$$

we obtain

$$
\boxed{BQ=L\frac{\sin(60^\circ+\theta)}{\sin(60^\circ-\theta)}-x-\frac{\sqrt3}{2\sin(60^\circ-\theta)}.}
$$

These are the local trigonometric formulas used to extract $(a,b)$-data in the CE0 + Vd1/Vd2 proof.
