# [START] Read the proof without knowing its terminology

[\[MAIN\]](README.md) · [\[GLOSSARY\]](GLOSSARY.md) · [\[USE\]](USING.md)

## Terms used here

The **unit hexagon** is the closed regular hexagon whose six sides have length $1$. An **open unit equilateral triangle** has three sides of length $1$ but does not include its boundary. Triangles may be translated or rotated. To **cover** the hexagon means every point of the hexagon, including its boundary, belongs to at least one open triangle.

## Tree

- **The claim:** seven such triangles cannot cover the unit hexagon.
    - Assume a cover exists and derive a contradiction.
- **Assign the triangles to seven special points.**
    - One triangle contains the center, and six others contain the six vertices.
    - Call them the **C triangle** and **V triangles**. The letter V means vertex.
    - Why must they be different? Two points in one open unit triangle have distance less than $1$, while these seven special points have pairwise distances at least $1$.
    - Full setup: [SETUP](SETUP.md).
- **Measure the boundary/inward tradeoff.**
    - A V triangle covers initial intervals of the two boundary edges at its vertex.
    - If their actual lengths sum to more than $1$, call that V triangle **supercritical**.
    - Such a triangle misses the midpoint of its own center-to-vertex segment, called its **spoke**.
    - Short geometric explanation: [MIDPOINTS](MIDPOINTS.md).
- **Ask whether the six V triangles cover the perimeter by themselves.**
    - A **gap** is a point or interval they miss; the C triangle must cover it. A single missing point is still a gap.
    - With no gaps, the proof uses either exterior-area loss or nine points that cannot all fit in the C triangle.
    - With a gap, the C triangle contains exactly one spoke midpoint; length bounds sharply limit the other triangles.
- **Who contains a missed midpoint?**
    - A V triangle at a neighboring vertex may contain it; call that triangle a **neighboring supplier** of the midpoint.
    - For example, a triangle based at vertex $V_0$ containing midpoint $M_1$ supplies $M_1$ on the next spoke.
    - This is a concrete point-containment statement, not a new kind of triangle.
    - The proof shows only one such supplying triangle can remain in the relevant case, then checks its few possible types and positions: [SUPPLIER](SUPPLIER.md).
- **Read the linked main tree.**
    - [MAIN](README.md) assembles the cases.
    - [D](D.md), for example, is the four-point contradiction when the supplier is based at the center's distinguished vertex index. The D page repeats its input and definitions, so it can be opened directly.
    - A **calculation leaf** marks a long local verification left below the speaking cutoff. The midpoint proofs remain expanded.

This is a navigation and explanation layer. The numbered proof sources linked from each argument remain the mathematical authority. A return link is navigation, not a claim that a proof depends on its parent page.
