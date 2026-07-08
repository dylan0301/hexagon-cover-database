"""Parallel bulk generation: split the two roots into s-strips and
process each in its own process; merge with merge_bulk.py."""
import sys
import sympy as sp
import gen_bulk as GB

STRIPS = [
    (sp.Rational(1, 32), sp.Rational(3, 64), sp.Rational(1, 32), sp.Rational(2, 3), True),
    (sp.Rational(3, 64), sp.Rational(1, 16), sp.Rational(1, 32), sp.Rational(2, 3), True),
    (sp.Rational(1, 16), sp.Rational(1, 8), sp.Rational(1, 16), sp.Rational(2, 3), False),
    (sp.Rational(1, 8), sp.Rational(1, 4), sp.Rational(1, 16), sp.Rational(2, 3), False),
    (sp.Rational(1, 4), sp.Rational(1, 2), sp.Rational(1, 16), sp.Rational(2, 3), False),
]

if __name__ == "__main__":
    k = int(sys.argv[1])
    s1, s2, t1, t2, wedge = STRIPS[k]
    root = (s1, s2, t1, t2)
    boxes = GB.process_box(root)
    with open(f"bulk_part{k}.py", "w") as f:
        f.write("DATA = " + repr({"root": [sp.srepr(v) for v in root],
                                  "boxes": boxes}) + "\n")
    print(f"strip {k}: {len(boxes)} boxes")
