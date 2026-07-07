"""Small outward-rounded Decimal interval arithmetic helper.

This module is intentionally tiny. It is used by the 3100aX verifier scripts
as a building block for independently checkable interval calculations.
It only implements the operations needed by the current certificates.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext, ROUND_FLOOR, ROUND_CEILING
from typing import Iterable, Union

Number = Union[int, float, str, Decimal]

PREC = 80


def _dec(x: Number) -> Decimal:
    if isinstance(x, Decimal):
        return x
    if isinstance(x, float):
        return Decimal(str(x))
    return Decimal(x)


def _op_down(fn) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_FLOOR
        return +fn()


def _op_up(fn) -> Decimal:
    with localcontext() as ctx:
        ctx.prec = PREC
        ctx.rounding = ROUND_CEILING
        return +fn()


@dataclass(frozen=True)
class Interval:
    lo: Decimal
    hi: Decimal

    def __init__(self, lo: Number, hi: Number | None = None):
        object.__setattr__(self, "lo", _dec(lo))
        object.__setattr__(self, "hi", _dec(lo if hi is None else hi))
        if self.lo > self.hi:
            raise ValueError(f"empty interval [{self.lo}, {self.hi}]")

    @staticmethod
    def hull(values: Iterable["Interval"]) -> "Interval":
        vals = list(values)
        if not vals:
            raise ValueError("cannot take hull of an empty list")
        return Interval(min(v.lo for v in vals), max(v.hi for v in vals))

    def __repr__(self) -> str:
        return f"Interval({self.lo}, {self.hi})"

    def __add__(self, other: Number | "Interval") -> "Interval":
        other = ensure_interval(other)
        return Interval(
            _op_down(lambda: self.lo + other.lo),
            _op_up(lambda: self.hi + other.hi),
        )

    __radd__ = __add__

    def __sub__(self, other: Number | "Interval") -> "Interval":
        other = ensure_interval(other)
        return Interval(
            _op_down(lambda: self.lo - other.hi),
            _op_up(lambda: self.hi - other.lo),
        )

    def __rsub__(self, other: Number | "Interval") -> "Interval":
        other = ensure_interval(other)
        return other.__sub__(self)

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __mul__(self, other: Number | "Interval") -> "Interval":
        other = ensure_interval(other)
        products_lo = [
            _op_down(lambda a=a, b=b: a * b)
            for a in (self.lo, self.hi)
            for b in (other.lo, other.hi)
        ]
        products_hi = [
            _op_up(lambda a=a, b=b: a * b)
            for a in (self.lo, self.hi)
            for b in (other.lo, other.hi)
        ]
        return Interval(min(products_lo), max(products_hi))

    __rmul__ = __mul__

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            raise ZeroDivisionError(f"interval contains zero: {self}")
        return Interval(
            _op_down(lambda: Decimal(1) / self.hi),
            _op_up(lambda: Decimal(1) / self.lo),
        )

    def __truediv__(self, other: Number | "Interval") -> "Interval":
        other = ensure_interval(other)
        return self * other.reciprocal()

    def __rtruediv__(self, other: Number | "Interval") -> "Interval":
        other = ensure_interval(other)
        return other.__truediv__(self)

    def __pow__(self, n: int) -> "Interval":
        if not isinstance(n, int) or n < 0:
            raise ValueError("only nonnegative integer powers are supported")
        if n == 0:
            return Interval(1)
        out = Interval(self.lo, self.hi)
        for _ in range(n - 1):
            out = out * self
        return out

    def sqrt(self) -> "Interval":
        if self.lo < 0:
            raise ValueError(f"sqrt of interval with negative lower endpoint: {self}")
        return Interval(
            _op_down(lambda: self.lo.sqrt()),
            _op_up(lambda: self.hi.sqrt()),
        )

    def width(self) -> Decimal:
        return self.hi - self.lo

    def contains_zero(self) -> bool:
        return self.lo <= 0 <= self.hi


def ensure_interval(x: Number | Interval) -> Interval:
    if isinstance(x, Interval):
        return x
    return Interval(x)


def sqr(x: Number | Interval) -> Interval:
    x = ensure_interval(x)
    if x.lo >= 0:
        return Interval(_op_down(lambda: x.lo * x.lo), _op_up(lambda: x.hi * x.hi))
    if x.hi <= 0:
        return Interval(_op_down(lambda: x.hi * x.hi), _op_up(lambda: x.lo * x.lo))
    hi = max(_op_up(lambda: x.lo * x.lo), _op_up(lambda: x.hi * x.hi))
    return Interval(0, hi)
