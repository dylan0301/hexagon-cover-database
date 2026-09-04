#!/usr/bin/env python3
"""Render the deterministic publication PNGs for the trace presets.

The shaded polygons are sampled subsets of source-conditioned unions.  They
explain the finite-enclosure geometry but are not proof certificates.
"""
from __future__ import annotations

from collections.abc import Iterable, Iterator
import math
import os
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/hexagon-cover-matplotlib")

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as MplPolygon
import numpy as np
from shapely.geometry import GeometryCollection, MultiPolygon, Polygon
from shapely.ops import unary_union

from generate_trace_assets import (
    H,
    PRESETS,
    ROOT,
    Envelope,
    Preset,
    actual_gaps,
    evaluate_preset,
    role_mask,
    validate_presets,
)


FIG_DIR = ROOT / "arrange/paper_draft/figures/trace_exact_ab"
V = np.array(
    [
        [math.cos(index * math.pi / 3.0), math.sin(index * math.pi / 3.0)]
        for index in range(6)
    ],
    dtype=float,
)
HEXAGON = Polygon(V)

matplotlib.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 8.0,
        "axes.titlesize": 10.0,
        "axes.linewidth": 0.8,
        "figure.dpi": 100,
        "savefig.dpi": 190,
        "path.simplify": False,
    }
)


def edge_point(index: int, parameter: float) -> np.ndarray:
    return V[index] + parameter * (V[(index + 1) % 6] - V[index])


def rotate(point: np.ndarray, theta: float) -> np.ndarray:
    cosine, sine = math.cos(theta), math.sin(theta)
    return np.array(
        [
            cosine * point[0] - sine * point[1],
            sine * point[0] + cosine * point[1],
        ]
    )


def line_intersection(
    normal_1: np.ndarray,
    offset_1: float,
    normal_2: np.ndarray,
    offset_2: float,
) -> np.ndarray:
    return np.linalg.solve(
        np.vstack([normal_1, normal_2]), np.array([offset_1, offset_2])
    )


def triangle_vertices(normals: np.ndarray, offsets: np.ndarray) -> np.ndarray:
    points = np.array(
        [
            line_intersection(normals[0], offsets[0], normals[1], offsets[1]),
            line_intersection(normals[1], offsets[1], normals[2], offsets[2]),
            line_intersection(normals[2], offsets[2], normals[0], offsets[0]),
        ]
    )
    center = points.mean(axis=0)
    order = np.argsort(
        np.arctan2(points[:, 1] - center[1], points[:, 0] - center[0])
    )
    return points[order]


def positive_compositions(
    total: float, parts: int, steps: int
) -> Iterator[np.ndarray]:
    if parts == 1:
        yield np.array([total])
        return
    epsilon = min(1e-5, total / max(1000, parts * 100))
    if total <= parts * epsilon:
        yield np.full(parts, total / parts)
        return
    if parts == 2:
        for parameter in np.linspace(epsilon, total - epsilon, steps):
            yield np.array([parameter, total - parameter])
        return
    for first in range(steps + 1):
        for second in range(steps + 1 - first):
            third = steps - first - second
            weights = np.array([first, second, third], dtype=float)
            yield (weights + 0.35) / (weights.sum() + 1.05) * total


def sample_source_triangles(
    role: int,
    A: float,
    B: float,
    mode: str,
    theta_steps: int,
    slack_steps: int,
) -> list[Polygon]:
    """Sample valid unit source triangles with the declared reach condition."""

    vertex = V[role]
    inward = V[(role - 1) % 6] - vertex
    outward = V[(role + 1) % 6] - vertex
    anchor_A = vertex + A * inward
    anchor_B = vertex + B * outward
    required_points = np.vstack([vertex, anchor_A, anchor_B])
    polygons: list[Polygon] = []
    active_tolerance = 4e-8

    for theta in np.linspace(
        0.0, 2.0 * math.pi / 3.0, theta_steps, endpoint=False
    ):
        normals = np.array(
            [
                [
                    math.cos(theta + 2.0 * math.pi * index / 3.0),
                    math.sin(theta + 2.0 * math.pi * index / 3.0),
                ]
                for index in range(3)
            ]
        )
        projections = required_points @ normals.T
        lower_offsets = projections.max(axis=0)
        slack = H - float(lower_offsets.sum())
        if slack < -2e-8:
            continue
        slack = max(0.0, slack)
        inward_derivatives = normals @ inward
        outward_derivatives = normals @ outward
        active_inward = [
            index
            for index in range(3)
            if inward_derivatives[index] > 1e-8
            and abs(
                lower_offsets[index] - float(anchor_A @ normals[index])
            )
            < active_tolerance
        ]
        active_outward = [
            index
            for index in range(3)
            if outward_derivatives[index] > 1e-8
            and abs(
                lower_offsets[index] - float(anchor_B @ normals[index])
            )
            < active_tolerance
        ]

        offsets_to_test: list[np.ndarray] = []
        if mode == "ordinary":
            for extra in positive_compositions(
                slack, 3, max(3, slack_steps // 2)
            ):
                offsets_to_test.append(lower_offsets + extra)
        elif mode in {"out", "in"}:
            active = active_outward if mode == "out" else active_inward
            for fixed_index in active:
                free = [index for index in range(3) if index != fixed_index]
                for extra_free in positive_compositions(slack, 2, slack_steps):
                    extra = np.zeros(3)
                    extra[free] = extra_free
                    offsets_to_test.append(lower_offsets + extra)
        elif mode == "both":
            for inward_index in active_inward:
                for outward_index in active_outward:
                    fixed = {inward_index, outward_index}
                    free = [index for index in range(3) if index not in fixed]
                    if not free:
                        if slack <= 2e-7:
                            offsets_to_test.append(lower_offsets.copy())
                    elif len(free) == 1:
                        extra = np.zeros(3)
                        extra[free[0]] = slack
                        offsets_to_test.append(lower_offsets + extra)
                    else:
                        for extra_free in positive_compositions(
                            slack, len(free), slack_steps
                        ):
                            extra = np.zeros(3)
                            extra[free] = extra_free
                            offsets_to_test.append(lower_offsets + extra)
        else:
            raise ValueError(f"unknown envelope mode: {mode}")

        for offsets in offsets_to_test:
            if np.min(offsets - normals @ vertex) <= 2e-7:
                continue

            def reach(direction: np.ndarray) -> float:
                candidates = [
                    (offset - float(normal @ vertex)) / denominator
                    for normal, offset in zip(normals, offsets, strict=True)
                    if (denominator := float(normal @ direction)) > 1e-9
                ]
                return min(candidates) if candidates else float("inf")

            reach_A = reach(inward)
            reach_B = reach(outward)
            if mode in {"in", "both"} and abs(reach_A - A) > 2e-5:
                continue
            if mode in {"out", "both"} and abs(reach_B - B) > 2e-5:
                continue
            polygon = Polygon(triangle_vertices(normals, offsets))
            if not polygon.is_valid:
                polygon = polygon.buffer(0)
            clipped = polygon.intersection(HEXAGON)
            if isinstance(clipped, Polygon) and clipped.area > 1e-9:
                polygons.append(clipped)
            elif isinstance(clipped, (MultiPolygon, GeometryCollection)):
                polygons.extend(
                    component
                    for component in clipped.geoms
                    if isinstance(component, Polygon) and component.area > 1e-9
                )
    return polygons


def union_geometry(polygons: list[Polygon]):
    if not polygons:
        return GeometryCollection()
    return unary_union(polygons).buffer(0)


def iter_polygons(geometry) -> Iterable[Polygon]:
    if isinstance(geometry, Polygon):
        yield geometry
    elif isinstance(geometry, (MultiPolygon, GeometryCollection)):
        for component in geometry.geoms:
            if isinstance(component, Polygon):
                yield component


def draw_geometry(
    axes,
    geometry,
    *,
    color: str,
    alpha: float,
    hatch: str | None,
    zorder: float,
) -> None:
    first = True
    for polygon in iter_polygons(geometry):
        x_coordinates, y_coordinates = polygon.exterior.xy
        axes.add_patch(
            MplPolygon(
                np.column_stack([x_coordinates, y_coordinates]),
                closed=True,
                facecolor=color,
                edgecolor=color,
                alpha=alpha,
                hatch=hatch,
                linewidth=0.7,
                zorder=zorder,
                label="sampled envelope" if first else None,
            )
        )
        first = False


def draw_support_arrows(axes, roles: list[str]) -> None:
    for index, code in enumerate(roles):
        left, right = role_mask(code)
        if left:
            point = 0.52 * V[(index - 1) % 6]
            axes.plot(
                [V[index, 0], point[0]],
                [V[index, 1], point[1]],
                color="#2d737a",
                linestyle="--",
                linewidth=1.1,
            )
        if right:
            point = 0.52 * V[(index + 1) % 6]
            axes.plot(
                [V[index, 0], point[0]],
                [V[index, 1], point[1]],
                color="#2d737a",
                linestyle="--",
                linewidth=1.1,
            )


ENVELOPE_CACHE: dict[tuple[object, ...], object] = {}


def envelope_geometry(envelope: Envelope, mode: str):
    key = (
        envelope.role,
        round(envelope.a, 8),
        round(envelope.b, 8),
        mode,
    )
    if key not in ENVELOPE_CACHE:
        theta_steps, slack_steps = (150, 5) if mode == "ordinary" else (240, 7)
        ENVELOPE_CACHE[key] = union_geometry(
            sample_source_triangles(
                envelope.role,
                envelope.a,
                envelope.b,
                mode,
                theta_steps,
                slack_steps,
            )
        )
    return ENVELOPE_CACHE[key]


def render_preset(preset: Preset, output: Path) -> None:
    result = evaluate_preset(preset)
    # Render near the physical width used by the two-column paper panels so
    # point labels remain legible after LaTeX places the raster.
    figure, axes = plt.subplots(figsize=(3.5, 3.15), facecolor="white")
    boundary = np.vstack([V, V[0]])
    axes.plot(
        boundary[:, 0], boundary[:, 1], color="#263238", linewidth=1.8,
        label="hexagon",
    )
    for index in range(6):
        axes.plot(
            [0.0, V[index, 0]], [0.0, V[index, 1]],
            color="#68767a", linewidth=0.55, alpha=0.45,
        )
        axes.text(
            V[index, 0] + 0.025, V[index, 1] + 0.025,
            rf"$V_{{{index}}}$", fontsize=9,
        )

    for envelope in preset.envelopes:
        draw_geometry(
            axes,
            envelope_geometry(envelope, "ordinary"),
            color="#98a5a2",
            alpha=0.075,
            hatch="..",
            zorder=0.5,
        )
        if envelope.mode != "ordinary":
            draw_geometry(
                axes,
                envelope_geometry(envelope, envelope.mode),
                color="#4c8b95",
                alpha=0.22,
                hatch="//",
                zorder=1.0,
            )

    first_gap = True
    for gap in actual_gaps(preset):
        left = edge_point(gap.edge, gap.left)
        right = edge_point(gap.edge, gap.right)
        axes.plot(
            [V[gap.edge, 0], left[0]],
            [V[gap.edge, 1], left[1]],
            color="#263238", linewidth=3.0, alpha=0.60,
        )
        axes.plot(
            [right[0], V[(gap.edge + 1) % 6, 0]],
            [right[1], V[(gap.edge + 1) % 6, 1]],
            color="#263238", linewidth=3.0, alpha=0.60,
        )
        axes.plot(
            [left[0], right[0]], [left[1], right[1]],
            color="#b2701d", linewidth=5.0,
            label="actual V-gap" if first_gap else None,
        )
        axes.scatter(
            [left[0], right[0]], [left[1], right[1]],
            color="#b2701d", s=28, zorder=7,
        )
        first_gap = False

    draw_support_arrows(axes, preset.roles)
    radii = result["radii"]
    for index, radius in enumerate(radii):
        point = radius * V[index]
        axes.scatter([point[0]], [point[1]], color="#7254a0", s=34, zorder=8)
        axes.text(
            point[0] + 0.018, point[1] + 0.018,
            rf"$D_{{{index}}}$", fontsize=8,
        )
    for label, x_coordinate, y_coordinate in preset.extras:
        axes.scatter(
            [x_coordinate], [y_coordinate], color="#7254a0", s=32, zorder=8
        )
        axes.text(
            x_coordinate + 0.018, y_coordinate + 0.018,
            rf"${label}$", fontsize=8,
        )

    triangle = np.asarray(result["triangle"], dtype=float)
    closed_triangle = np.vstack([triangle, triangle[0]])
    axes.plot(
        closed_triangle[:, 0], closed_triangle[:, 1],
        color="#a23f35", linestyle="--", linewidth=1.8,
        label=f"min. enclosing side {result['side']:.3f}",
    )
    axes.scatter([0.0, 0.5], [0.0, 0.0], color="#7254a0", s=26, zorder=8)
    axes.text(0.015, -0.045, "$O$", fontsize=9)
    axes.text(0.51, 0.02, "$M_0$", fontsize=9)

    axes.set_aspect("equal", adjustable="box")
    axes.set_xlim(-1.15, 1.15)
    axes.set_ylim(-1.05, 1.08)
    axes.axis("off")
    figure.tight_layout(pad=0.15)
    figure.savefig(
        output,
        dpi=190,
        bbox_inches="tight",
        facecolor="white",
        metadata={"Software": "hexagon-cover-database trace renderer"},
    )
    plt.close(figure)


def main() -> None:
    validate_presets()
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    for index, preset in enumerate(PRESETS, 1):
        output = FIG_DIR / f"{preset.key}.png"
        render_preset(preset, output)
        print(f"{index:02d} {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
