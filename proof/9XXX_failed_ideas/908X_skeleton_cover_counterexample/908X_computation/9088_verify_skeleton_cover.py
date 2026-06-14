#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


SIDE_TOL = 1e-9
COVER_TOL = 1e-9
MERGE_TOL = 1e-9


@dataclass(frozen=True)
class Point:
    x: float
    y: float


@dataclass(frozen=True)
class Triangle:
    name: str
    declared_side: float
    vertices: tuple[Point, Point, Point]


def point_from_json(raw: dict[str, Any]) -> Point:
    return Point(float(raw["x"]), float(raw["y"]))


def sub(a: Point, b: Point) -> Point:
    return Point(a.x - b.x, a.y - b.y)


def cross(a: Point, b: Point) -> float:
    return a.x * b.y - a.y * b.x


def dist(a: Point, b: Point) -> float:
    return math.hypot(a.x - b.x, a.y - b.y)


def hexagon_vertices() -> list[Point]:
    return [Point(math.cos(i * math.pi / 3), math.sin(i * math.pi / 3)) for i in range(6)]


def triangle_orientation(vertices: tuple[Point, Point, Point]) -> float:
    return cross(sub(vertices[1], vertices[0]), sub(vertices[2], vertices[0]))


def side_lengths(triangle: Triangle) -> tuple[float, float, float]:
    v = triangle.vertices
    return dist(v[0], v[1]), dist(v[1], v[2]), dist(v[2], v[0])


def interval_on_segment(start: Point, end: Point, triangle: Triangle) -> tuple[float, float] | None:
    vertices = triangle.vertices
    orientation = triangle_orientation(vertices)
    if abs(orientation) <= SIDE_TOL:
        raise ValueError(f"{triangle.name} is degenerate")

    sign = 1.0 if orientation > 0 else -1.0
    direction = sub(end, start)
    t_min = 0.0
    t_max = 1.0

    for i in range(3):
        a = vertices[i]
        b = vertices[(i + 1) % 3]
        edge = sub(b, a)
        base = sign * cross(edge, sub(start, a))
        slope = sign * cross(edge, direction)
        threshold = -COVER_TOL

        if abs(slope) <= SIDE_TOL:
            if base >= threshold:
                continue
            return None

        root = (threshold - base) / slope
        if slope > 0:
            t_min = max(t_min, root)
        else:
            t_max = min(t_max, root)

        if t_min > t_max + COVER_TOL:
            return None

    return max(0.0, t_min), min(1.0, t_max)


def merge_intervals(intervals: list[tuple[float, float] | None]) -> list[tuple[float, float]]:
    valid = sorted(interval for interval in intervals if interval is not None and interval[1] >= interval[0])
    merged: list[list[float]] = []

    for start, end in valid:
        if not merged or start > merged[-1][1] + MERGE_TOL:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return [(start, end) for start, end in merged]


def segment_is_covered(merged: list[tuple[float, float]]) -> bool:
    return len(merged) == 1 and merged[0][0] <= COVER_TOL and merged[0][1] >= 1.0 - COVER_TOL


def format_intervals(intervals: list[tuple[float, float]]) -> str:
    if not intervals:
        return "(empty)"
    return " ".join(f"[{start:.12f}, {end:.12f}]" for start, end in intervals)


def load_triangles(path: Path, drop_triangle: str | None) -> list[Triangle]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    triangles: list[Triangle] = []

    for item in raw["triangles"]:
        if item["name"] == drop_triangle:
            continue
        vertices = tuple(point_from_json(point) for point in item["vertices"])
        if len(vertices) != 3:
            raise ValueError(f"{item['name']} does not have three vertices")
        triangles.append(Triangle(item["name"], float(item["side"]), vertices))

    return triangles


def verify_triangle_geometry(triangles: list[Triangle]) -> tuple[bool, float, list[str]]:
    ok = True
    max_side = 0.0
    lines: list[str] = []

    for triangle in triangles:
        sides = side_lengths(triangle)
        max_side = max(max_side, *sides, triangle.declared_side)
        spread = max(sides) - min(sides)
        declared_gap = max(abs(side - triangle.declared_side) for side in sides)
        if max(sides) >= 1.0 - SIDE_TOL or triangle.declared_side >= 1.0 - SIDE_TOL:
            ok = False
        if spread > 5e-12 or declared_gap > 5e-12:
            ok = False
        lines.append(
            f"{triangle.name}: declared={triangle.declared_side:.12f}, "
            f"computed=({sides[0]:.12f}, {sides[1]:.12f}, {sides[2]:.12f})"
        )

    return ok, max_side, lines


def verify_skeleton_cover(triangles: list[Triangle]) -> tuple[bool, list[str]]:
    hexagon = hexagon_vertices()
    origin = Point(0.0, 0.0)
    lines: list[str] = []
    ok = True

    for i in range(6):
        merged = merge_intervals(
            [interval_on_segment(hexagon[i], hexagon[(i + 1) % 6], triangle) for triangle in triangles]
        )
        covered = segment_is_covered(merged)
        ok = ok and covered
        lines.append(f"edge {i}: {format_intervals(merged)} {'ok' if covered else 'GAP'}")

    for i in range(6):
        merged = merge_intervals([interval_on_segment(origin, hexagon[i], triangle) for triangle in triangles])
        covered = segment_is_covered(merged)
        ok = ok and covered
        lines.append(f"radial {i}: {format_intervals(merged)} {'ok' if covered else 'GAP'}")

    return ok, lines


def parse_args() -> argparse.Namespace:
    default_json = Path(__file__).with_name("9086_counterexample_cover.json")
    parser = argparse.ArgumentParser(description="Verify the May 24 skeleton-cover counterexample.")
    parser.add_argument("json_path", nargs="?", type=Path, default=default_json)
    parser.add_argument("--drop-triangle", help="omit a named triangle before checking coverage")
    parser.add_argument(
        "--expect-failure",
        action="store_true",
        help="exit successfully only if the verifier detects failure",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    triangles = load_triangles(args.json_path, args.drop_triangle)

    geometry_ok, max_side, geometry_report = verify_triangle_geometry(triangles)
    cover_ok, cover_report = verify_skeleton_cover(triangles)
    ok = geometry_ok and cover_ok

    print(f"triangles checked: {len(triangles)}")
    print(f"max side length: {max_side:.12f}")
    print("triangle geometry:")
    for line in geometry_report:
        print(f"  {line}")
    print("skeleton coverage:")
    for line in cover_report:
        print(f"  {line}")

    if args.expect_failure:
        if ok:
            print("expected failure, but verification passed")
            return 1
        print("expected failure detected")
        return 0

    if ok:
        print("verification passed")
        return 0

    print("verification failed")
    return 1


if __name__ == "__main__":
    sys.exit(main())
