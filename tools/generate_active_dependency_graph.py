#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from collections import deque
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PROOF = ROOT / "proof"
GRAPH_PATH = PROOF / "ACTIVE_DEPENDENCY_GRAPH.json"
TEXT_PATH = PROOF / "ACTIVE_DEPENDENCIES.txt"
ROOT_SOURCE = PROOF / "0XXX_main/0000_main_theorem.md"
STATUS_SOURCE = PROOF / "0XXX_main/0002_status_and_dependencies.md"
EXTRA_SEEDS = [
    PROOF / "4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/414b_complete_placement_reaudit.md",
]
RECURSE_STATUSES = {"Proven", "Reduction"}
LEAF_STATUSES = {"Definition", "Reference"}
TRACKED_STATUSES = RECURSE_STATUSES | LEAF_STATUSES
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+?\.md)(?:#[^)]*)?\)")
ELECTRONIC_OBJECTS = [
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_00.py",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_01.py",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_02.py",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_03.py",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_04.py",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_05.py",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_polynomials.py",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_mixed_overlap_core_derivation.py",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_global_core_positivity.py",
]


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def status(path: Path, *, required: bool = True) -> str:
    head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:20])
    match = re.search(r"^Status:\s*(.+?)\s*$", head, re.M)
    if not match:
        if required:
            raise RuntimeError(f"proof source lacks Status line: {rel(path)}")
        return "Unstated"
    return match.group(1)


def links(path: Path) -> list[Path]:
    output: list[Path] = []
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        href = unquote(raw.split("#", 1)[0])
        if "://" in href:
            continue
        target = (path.parent / href).resolve()
        try:
            target.relative_to(PROOF.resolve())
        except ValueError:
            continue
        if not target.is_file():
            raise RuntimeError(f"broken in-proof Markdown link: {rel(path)} -> {href}")
        output.append(target)
    return sorted(set(output), key=lambda p: rel(p))


def render() -> tuple[str, str]:
    seeds = [ROOT_SOURCE, STATUS_SOURCE, *EXTRA_SEEDS]
    seeds.extend(links(STATUS_SOURCE))
    queue: deque[Path] = deque(path.resolve() for path in seeds if path.is_file())
    nodes: dict[str, dict[str, object]] = {}
    inactive_links: dict[str, list[dict[str, str]]] = {}

    while queue:
        path = queue.popleft()
        path_rel = rel(path)
        if path_rel in nodes:
            continue
        source_status = status(path)
        if source_status not in TRACKED_STATUSES:
            raise RuntimeError(
                f"active seed has non-proof status {source_status!r}: {path_rel}"
            )

        dependencies: list[str] = []
        inactive: list[dict[str, str]] = []
        if source_status in RECURSE_STATUSES:
            for target in links(path):
                target_rel = rel(target)
                target_status = status(target, required=False)
                if "/9XXX_failed_ideas/" in f"/{target_rel}/":
                    inactive.append({"path": target_rel, "status": target_status})
                    continue
                if target_status in TRACKED_STATUSES:
                    dependencies.append(target_rel)
                    if target_status in RECURSE_STATUSES:
                        queue.append(target)
                    elif target_rel not in nodes:
                        nodes[target_rel] = {
                            "status": target_status,
                            "dependencies": [],
                            "kind": "proof-source",
                        }
                else:
                    inactive.append({"path": target_rel, "status": target_status})

        nodes[path_rel] = {
            "status": source_status,
            "dependencies": sorted(set(dependencies)),
            "kind": "proof-source",
        }
        if inactive:
            inactive_links[path_rel] = inactive

    for object_rel in ELECTRONIC_OBJECTS:
        object_path = ROOT / object_rel
        if not object_path.is_file():
            raise RuntimeError(f"missing electronic proof object: {object_rel}")
        nodes[object_rel] = {
            "status": "Electronic",
            "dependencies": [],
            "kind": "electronic-proof-object",
        }

    graph = {
        "schema": 1,
        "root": rel(ROOT_SOURCE),
        "generated_by": "tools/generate_active_dependency_graph.py",
        "edge_semantics": (
            "untyped Markdown proof citations; cycles are permitted and the graph "
            "is not a logical dependency order"
        ),
        "nodes": {key: nodes[key] for key in sorted(nodes)},
        "inactive_links": {
            key: inactive_links[key] for key in sorted(inactive_links)
        },
    }
    graph_text = json.dumps(graph, indent=2, sort_keys=True) + "\n"
    list_text = (
        "# Generated transitive active proof-reference graph: path|expected status\n"
        "# Edges are untyped Markdown citations; cycles are permitted.\n"
    )
    list_text += "".join(
        f"{key}|{nodes[key]['status']}\n" for key in sorted(nodes)
    )
    return graph_text, list_text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    graph_text, list_text = render()
    if args.check:
        failures = []
        if not GRAPH_PATH.is_file() or GRAPH_PATH.read_text(encoding="utf-8") != graph_text:
            failures.append(str(GRAPH_PATH.relative_to(ROOT)))
        if not TEXT_PATH.is_file() or TEXT_PATH.read_text(encoding="utf-8") != list_text:
            failures.append(str(TEXT_PATH.relative_to(ROOT)))
        if failures:
            raise SystemExit("generated active dependency files are stale: " + ", ".join(failures))
        return
    GRAPH_PATH.write_text(graph_text, encoding="utf-8")
    TEXT_PATH.write_text(list_text, encoding="utf-8")


if __name__ == "__main__":
    main()
