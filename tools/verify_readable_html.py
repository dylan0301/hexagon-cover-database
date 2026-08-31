#!/usr/bin/env python3
"""Static integrity audit for the reader-oriented interactive graph."""
from __future__ import annotations
import base64
import json
import re
import subprocess
import tempfile
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'interactive' / 'readable_proof_dependency_data.json'
HTML = ROOT / 'interactive' / 'readable_proof_dependency_graph.html'


def main() -> None:
    data = json.loads(DATA.read_text(encoding='utf-8'))
    nodes = data['nodes']
    ids = {node['id'] for node in nodes}
    if len(ids) != len(nodes):
        raise SystemExit('duplicate statement IDs in readable dependency data')
    if data['meta']['nodeCount'] != len(nodes):
        raise SystemExit('node-count metadata is stale')

    indegree = {node_id: 0 for node_id in ids}
    outgoing: dict[str, list[str]] = defaultdict(list)
    edge_count = 0
    for node in nodes:
        for dep in node['deps']:
            if dep not in ids:
                raise SystemExit(f"unknown dependency: {node['id']} -> {dep}")
            outgoing[dep].append(node['id'])
            indegree[node['id']] += 1
            edge_count += 1
    if edge_count != data['meta']['edgeCount']:
        raise SystemExit('edge-count metadata is stale')
    queue = deque(node_id for node_id, degree in indegree.items() if degree == 0)
    seen = 0
    while queue:
        node_id = queue.popleft()
        seen += 1
        for target in outgoing[node_id]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    if seen != len(nodes):
        raise SystemExit('readable logical dependency graph is cyclic')

    for key, figure in data['figures'].items():
        prefix = 'data:image/png;base64,'
        if not figure['src'].startswith(prefix):
            raise SystemExit(f'non-embedded figure payload: {key}')
        raw = base64.b64decode(figure['src'][len(prefix):], validate=True)
        if not raw.startswith(b'\x89PNG\r\n\x1a\n'):
            raise SystemExit(f'invalid PNG payload: {key}')

    zero = data['figures'].get('zero_gap_original')
    if zero is None or not zero['repositoryPath'].endswith(
        'interactive/assets/readable_dependency/zero_gap_nine_point_witness.png'
    ):
        raise SystemExit('zero-gap card is not bound to the restored nine-point asset')
    zg = next(row for row in data['finiteRows'] if row['id'] == 'ZG0')
    if zg['figures'] != ['zero_gap_original']:
        raise SystemExit('ZG0 uses an incorrect figure key')

    html = HTML.read_text(encoding='utf-8')
    for marker in [
        'id="graphSvg"', 'id="routingTable"', 'id="caseCards"',
        'id="reportBody"', 'id="indexTable"', 'Reader-oriented hexagon-cover proof graph'
    ]:
        if marker not in html:
            raise SystemExit(f'missing HTML interface marker: {marker}')
    script_match = re.search(r'<script>(.*)</script>', html, re.S)
    if not script_match:
        raise SystemExit('interactive HTML has no inline script')
    with tempfile.TemporaryDirectory() as td:
        js = Path(td) / 'graph.js'
        js.write_text(script_match.group(1), encoding='utf-8')
        subprocess.run(['node', '--check', str(js)], check=True)

    print(
        f"verified readable HTML: {len(nodes)} nodes, {edge_count} edges, "
        f"{len(data['figures'])} embedded PNG figures"
    )


if __name__ == '__main__':
    main()
