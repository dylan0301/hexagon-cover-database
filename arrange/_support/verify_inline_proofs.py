#!/usr/bin/env python3
"""Check immediate proofs, dependency order, and preservation of both editions.

This is an editorial regression audit, not a formal verification of mathematics.
It compares the complete proof bodies with the canonical manuscript, allowing
only the documented statement merges and small editorial replacements.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "arrange/paper_draft"
EDITION = PAPER / "inline_proofs"
STATEMENT = re.compile(r"\\begin\{(theorem|lemma|proposition|corollary)\}(?:\[[^\]]*\])?")
REFERENCE = re.compile(r"\\(?:eqref|ref|pageref|cref|Cref|autoref|zcref|zCref)(?:\[[^\]]*\])?\{([^}]+)\}")
LABEL = re.compile(r"\\label\{([^}]+)\}")
PROOF_START = re.compile(r"\\begin\{proof\}(?:\[[^\]]*\])?")


def active(text: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def expand(path: Path, stack: tuple[Path, ...] = ()) -> str:
    path = path.resolve()
    if path in stack:
        raise ValueError(f"cyclic TeX input: {path}")

    def include(match: re.Match[str]) -> str:
        target = Path(match[1]).with_suffix(".tex")
        candidate = path.parent / target
        if not candidate.is_file():
            candidate = PAPER / target
        return expand(candidate, (*stack, path))

    return re.sub(r"\\input\{([^}]+)\}", include, active(path.read_text()))


def normalized(text: str) -> str:
    # Aliased theorem counters require type-aware references after consolidation.
    text = re.sub(r"(?:Lemma|Proposition|Theorem|Corollary)(?:~|\s)+\\ref\{([^}]+)\}",
                  r"\\zcref{\1}", active(text))
    text = text.replace(r"\zcref[S]", r"\zcref")
    for alias, target in json.loads((EDITION / "source_map.json").read_text())["equation_aliases"].items():
        text = text.replace("{" + alias + "}", "{" + target + "}")
    return re.sub(r"\s+", "", text)


def statement_body(text: str) -> str:
    text = STATEMENT.sub("", text)
    text = re.sub(r"\\end\{(?:theorem|lemma|proposition|corollary)\}", "", text)
    text = LABEL.sub("", text)
    text = text.replace(r"\begin{equation}", r"\[").replace(r"\end{equation}", r"\]")
    return normalized(text)


@dataclass
class Result:
    labels: list[str]
    statement: str
    proof: str
    start: int
    statement_end: int
    proof_start: int | None
    proof_end: int


def results(text: str) -> list[Result]:
    starts = list(STATEMENT.finditer(text))
    found = []
    for index, match in enumerate(starts):
        end_token = "\\end{" + match[1] + "}"
        end = text.index(end_token, match.end()) + len(end_token)
        limit = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        proof = PROOF_START.search(text, end, limit)
        proof_end = text.index("\\end{proof}", proof.end()) if proof else end
        found.append(Result(
            LABEL.findall(text[match.start():end]), text[match.start():end],
            text[proof.end():proof_end].strip() if proof else "",
            match.start(), end, proof.start() if proof else None, proof_end,
        ))
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf", type=Path, help="also audit proof starts in the rendered edition")
    args = parser.parse_args()
    canonical = expand(PAPER / "main.tex")
    inline = expand(EDITION / "main.tex")
    source_map = json.loads((EDITION / "source_map.json").read_text())
    merges = source_map["statement_merges"]
    errors: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    old = results(canonical)
    new = results(inline)
    old_labels = {label: result for result in old for label in result.labels}
    new_labels = {label: result for result in new for label in result.labels}
    labels: dict[str, int] = {}
    for match in LABEL.finditer(inline):
        require(match[1] not in labels, f"duplicate inline label: {match[1]}")
        labels[match[1]] = match.start()

    aliases = source_map["equation_aliases"]
    missing = set(LABEL.findall(canonical)) - labels.keys() - aliases.keys()
    require(not missing, f"missing canonical labels: {sorted(missing)}")
    for alias, target in aliases.items():
        require(alias in LABEL.findall(canonical) and target in labels,
                f"unresolved equation consolidation: {alias} -> {target}")
    formal_prefixes = ("lem:", "thm:", "prop:", "cor:")
    require({label for label in old_labels if label.startswith(formal_prefixes)}
            == {label for label in new_labels if label.startswith(formal_prefixes)},
            "formal statement inventory differs beyond the declared merges")
    require(len(old) - len(new) == len(merges), "statement count does not match the declared merges")
    for body, calculation in merges.items():
        require(body in old_labels and calculation in old_labels, f"unknown merge: {body}")
        require(body in new_labels and new_labels.get(body) is new_labels.get(calculation),
                f"merged labels are not on the same statement: {body}, {calculation}")

    for result in old:
        key = result.labels[0]
        if key in merges.values():
            continue  # The duplicate calculation's full hypotheses are on its body statement.
        expected = result.statement
        for before, after in source_map["editorial_statement_replacements"].get(key, []):
            require(expected.count(before) == 1, f"statement replacement no longer matches: {key}")
            expected = expected.replace(before, after)
        target = new_labels.get(key)
        require(target is not None and statement_body(expected) in statement_body(target.statement),
                f"canonical statement changed or missing: {key}")

    for match in REFERENCE.finditer(inline):
        for label in match[1].split(","):
            require(label.strip() in labels, f"unresolved inline reference: {label.strip()}")
    # Labels may retain their original internal names; no appendix appears in print.
    without_labels = LABEL.sub("", inline)
    without_labels = REFERENCE.sub("", without_labels)
    require(not re.search(r"\\appendix\b|\bappendi(?:x|ces)\b", without_labels, re.I),
            "appendix command or printed appendix referral remains")

    proof_starts = {m.start() for m in PROOF_START.finditer(inline)}
    assigned = set()
    for result in new:
        key = result.labels[0]
        require(result.proof_start is not None and bool(result.proof), f"missing proof: {key}")
        if result.proof_start is None:
            continue
        assigned.add(result.proof_start)
        require(not inline[result.statement_end:result.proof_start].strip(),
                f"proof does not immediately follow statement: {key}")
        for match in REFERENCE.finditer(inline[result.start:result.proof_end]):
            for label in match[1].split(","):
                label = label.strip()
                require(labels.get(label, -1) <= result.proof_end,
                        f"forward reference in statement or proof: {key} -> {label}")
    require(proof_starts == assigned, "orphan or multiply assigned proof environment")

    preserved = 0
    for result in old:
        key = result.labels[0]
        if key in merges or not result.proof:
            continue
        expected = result.proof
        for before, after in source_map["editorial_proof_replacements"].get(key, []):
            require(expected.count(before) == 1, f"editorial replacement no longer matches: {key}")
            expected = expected.replace(before, after)
        target = new_labels.get(key)
        require(target is not None and normalized(expected) in normalized(target.proof),
                f"canonical proof material changed or missing: {key}")
        preserved += 1

    # The main proof was detached from its statement in the canonical edition.
    main_marker = r"\begin{proof}[Proof of Theorem~\ref{thm:main}]"
    assembly = canonical.split(main_marker, 1)[1].split(r"\end{proof}", 1)[0]
    core, _ = assembly.split("The scaling equivalence", 1)
    require(normalized(core) in normalized(new_labels["thm:main"].proof),
            "main theorem assembly was not preserved")
    require("prop:open-closed-scaled" in new_labels["cor:expanded-closed"].proof
            and "thm:main" in new_labels["cor:expanded-closed"].proof,
            "scaling corollary lacks its separate deduction")

    for label in ("eq:orientation-type-I", "eq:orientation-type-II"):
        require(labels[label] < labels["prop:vd0-exact-trace-normalization"],
                "orientation charts must precede normalization")
    require(new_labels["prop:vd0-exact-trace-normalization"].proof_end < inline.index("A_i:=\\max"),
            "actual reaches must be defined after normalization")
    require(labels["thm:fixed-nzero"] < labels["lem:two-vertex-replacement"],
            "N0 must precede replacement")
    require(labels["thm:paper-exact-mixed-certificate"] < labels["thm:reader-witness-enclosure"],
            "exact certificate must precede witness-enclosure conclusion")
    require(new[-2].labels[0] == "thm:main" and new[-1].labels[0] == "cor:expanded-closed",
            "main theorem and scaling corollary must conclude the paper")

    # Preserve the manifest and transcript identity; proof/check.py authenticates the files.
    marker = "% BEGIN GENERATED 3105X PROVENANCE"
    old_certificate = (PAPER / "A_zero_gap_exact_certificate.tex").read_text()
    new_certificate = (EDITION / "06_zero_gap.tex").read_text()
    require(old_certificate.split(marker)[1].split("% END GENERATED 3105X PROVENANCE")[0]
            == new_certificate.split(marker)[1].split("% END GENERATED 3105X PROVENANCE")[0],
            "exact-certificate provenance changed")
    digest = "dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485"
    require(digest in new_certificate, "exact certificate transcript digest missing")
    # Typography and metadata are shared verbatim, without touching the canonical source.
    require((PAPER / "main.tex").read_text().split(r"\input{01_introduction}")[0]
            == (EDITION / "main.tex").read_text().split(r"\input{inline_proofs/")[0],
            "inline preamble, metadata, or abstract differs from the canonical paper")

    if args.pdf:
        import fitz

        with fitz.open(args.pdf) as document:
            pages = [page.get_text() for page in document]
        require(len(re.findall(r"\bProof\.", "\n".join(pages))) == len(new),
                "rendered proof count differs from the source inventory")
        require(not re.search(r"\bappendi(?:x|ces)\b", "\n".join(pages), re.I),
                "rendered PDF contains an appendix referral")
        # Subsequent amsart pages have a two-line running head before the body.
        for number, page in enumerate(pages[1:], start=2):
            body = [line.strip() for line in page.splitlines()[2:] if line.strip()]
            require(not body or not body[0].startswith("Proof."),
                    f"proof starts on a new page after its statement: page {number}")
        print(f"Rendered inline edition: {len(pages)} pages checked")

    if errors:
        raise SystemExit("verify_inline_proofs: FAILED\n" + "\n".join(f"- {e}" for e in errors))
    print(f"verify_inline_proofs: PASS ({len(old)} original statements, {len(new)} immediate proofs, "
          f"{len(merges)} merges, {preserved} complete proof bodies preserved)")
    print("All statements and equation targets accounted for; no forward proof dependencies; exact provenance unchanged.")


if __name__ == "__main__":
    main()
