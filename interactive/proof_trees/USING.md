# [USE] Opening and navigating the tree bundle

[\[MAIN\]](README.md) · [\[NOTATION\]](NOTATION.md)

**Start at `README.md` in a Markdown preview. The downloadable bundle also includes an offline `index.html`; a repository checkout can generate it with the commands below.** Keep the folder together so relative links continue to work.

## Terms used here

A **tree** is a hierarchy of statements and their reasons. A bracketed label is a page link, not a mathematical variable. Markdown preview means the rendered view of a `.md` file; raw text still shows the indentation but does not activate links. A calculation leaf is where the conceptual tree stops expanding a long verification. [GLOSSARY](GLOSSARY.md) defines the mathematical vocabulary; each argument page also repeats the definitions it needs.

## Tree

- **Markdown view.**
    - Every tree is a nested Markdown list, not a fenced code block.
    - Bracketed labels are real links to separate `.md` files.
    - Example: click [\[D\]](D.md) to open `D.md`; its own children and calculation leaf are clickable.
    - Top and bottom navigation links return to [\[MAIN\]](README.md) or related parent trees.
    - Mathematical expressions use standard dollar-delimited LaTeX; display depends on the Markdown renderer's math support.
- **Offline browser view.**
    - Open `index.html`; no server or internet connection is required for the local trees.
    - Click a node label to change pages.
    - Click a disclosure triangle to expand or collapse a branch.
    - Use the page selector, Back button, or Main button to navigate.
    - Use Expand all / Collapse all for the current tree.
    - Equations are embedded as MathML; no external font or script files are bundled.
    - External proof-source links open GitHub and require internet access.
- **Separate flow from detail.**
    - Main geometry and short midpoint arguments remain in the proof-tree pages.
    - A CALCULATION LEAF links to a page in `details/`.
    - Those pages state the required inputs and outputs and link to the exact repository derivations.
    - They do not claim to reproduce every long calculation or the complete certificate data.
- **Read in proof order.**
    - [\[SETUP\]](SETUP.md) → [\[CLASSIFICATION\]](CLASSIFICATION.md) → [\[MIDPOINTS\]](MIDPOINTS.md).
    - Shared enclosure idea [\[WITNESS\]](WITNESS.md); selected-gap theorem [\[BC\]](BC.md); then [\[N0\]](N0.md).
    - Zero-gap branches [\[F\]](F.md) and [\[AREA\]](AREA.md).
    - Nonzero-gap count [\[LENGTH\]](LENGTH.md) and routing [\[SUPPLIER\]](SUPPLIER.md).
    - Finish with [\[D\]](D.md), [\[PERIMETER\]](PERIMETER.md), or [\[REPLACEMENT\]](REPLACEMENT.md) as required.
- **Scope and provenance.**
    - All repository source links are pinned to `c9baa75d090ee888fa85b575bdfb061f244197d0`.
    - This is a presentation layer built from the discussed repository proof, not an independent full proof audit.
    - This directory is maintained in the repository under `interactive/proof_trees/`. Uploading HTML to GitHub does not itself deploy a website; GitHub displays its source.

## Complete page map

- [\[MAIN\]](README.md)
    - [\[SETUP\]](SETUP.md)
        - [\[CLASSIFICATION\]](CLASSIFICATION.md)
        - [\[MIDPOINTS\]](MIDPOINTS.md)
            - [\[C-MIDPOINT\]](C-MIDPOINT.md)
            - [\[SELF-MIDPOINT\]](SELF-MIDPOINT.md)
            - [\[T3-MIDPOINT\]](T3-MIDPOINT.md)
    - [\[N0\]](N0.md)
    - [\[SUPPLIER\]](SUPPLIER.md)
        - [\[LENGTH\]](LENGTH.md)
        - [\[BC\]](BC.md)
        - [\[D\]](D.md)
        - [\[PERIMETER\]](PERIMETER.md)
        - [\[REPLACEMENT\]](REPLACEMENT.md)
    - [\[F\]](F.md)
        - [\[CALIPERS\]](CALIPERS.md)
    - [\[AREA\]](AREA.md)
    - [\[WITNESS\]](WITNESS.md)
    - [\[NOTATION\]](NOTATION.md)
    - Calculation leaves
        - [\[BC-CALC\]](details/BC-calculations.md)
        - [\[D-CALC\]](details/D-calculations.md)
        - [\[F-CALC\]](details/F-certificate.md)
        - [\[BOUNDS\]](details/length-area-bounds.md)
        - [\[REPLACE-CALC\]](details/replacement-margins.md)
        - [\[HANDOFFS\]](details/handoffs.md)

[\[MAIN\]](README.md) Return to the main tree.


## Build and check the offline viewer

Markdown navigation on GitHub requires no installation. To create the single-file browser viewer from a repository checkout, run from `interactive/proof_trees/`:

```bash
python -m pip install -r requirements.txt
npm install --ignore-scripts --no-audit --no-fund
python check.py
python build.py
python check.py --html
python build.py --check
```

Then open the generated `index.html`. Build dependencies are pinned; only the build needs Python, Node, and the installed packages. The generated file embeds the pages and MathML and does not use external scripts or fonts. It is intentionally ignored by Git; the Markdown, renderer, and checks are the maintained source. A supplied release/download bundle can include the generated file.

Use the **Start here** and **Glossary** buttons for vocabulary. Each page's **Terms used here** panel is open initially and can be folded once familiar. The expansion state of each page is remembered during that browser session.
