# Repository instructions

## Proof and layout

- Proof authority: numbered sources under `proof/` with supporting status, or exact certificates incorporated by the paper—not navigation, experiments, or numerical evidence.
- Use **C triangle** and **V triangle**. Original open triangles are `U_C,U_0,...,U_5`, with `O in U_C`, `V_i in U_i`; their closures are `T_C,T_i`. Apply closed classifications to `T`; retain `U` whenever openness matters.
- Uppercase `(A_i,B_i,C_i)` means actual maximal reaches; lowercase `(a_i,b_i,c_i)` means explicitly stated lower bounds, e.g. `a_i <= A_i`. Define `N_+` only by `A_i+B_i>1`.
- Preserve singleton gaps, CE1/CE2, endpoint strictness, V-type restrictions on adjacent support, connected-component selectors, both Vd1 replacement charts, and exact zero-gap certificates.
- Keep proof sources in `proof/`, the canonical paper in `arrange/paper_draft/`, and visualizations in `interactive/`. Keep support code beside its content; do not add top-level `tools/`, `release/`, `.vscode/`, or formalization directories.

## Checks

For proof, paper, or code changes, follow `.github/workflows/ci.yml`:

```bash
python -m pip install -r arrange/_support/requirements.txt
python proof/check.py
python interactive/generate.py --dependency-graph --check
python interactive/generate.py --trace-assets --check
python interactive/check.py
python arrange/build.py --all
git diff --check
```

Run both exact zero-gap certificate programs listed in CI when their source, provenance, or dependent theorem changes. Use CI's pinned environment for publication builds; update affected generated artifacts and verify the PDF. For instructions-only edits, inspect the complete diff and run `git diff --check`; do not regenerate unrelated artifacts.

## Publishing methods

- Use the requested branch. Otherwise create `chatgpt/<task>-<UTC-YYYYMMDDHHMMSS>` from fresh `main` and reuse or open a PR to `main`. Write directly to `main` only when explicitly requested and repository rules permit it. Never force-push or bypass protection.
- Prefer the connected GitHub tools. Discover available write actions before concluding that publishing is unavailable; shell networking and connector authorization are independent. Never request or store credentials to work around a failure.
- **One text file:** fetch it on the target branch, then call `update_file` with its current **blob SHA**, complete replacement text, and explicit branch. Use `create_file` only for a new path; create the branch first if needed. Serialize writes to the same path.
- **Multiple files, deletions, or binaries:** fetch the current branch head and tree; `create_blob` for changed files (base64 for binary bytes); `create_tree` with that remote tree as `base_tree_sha`, preserving modes and using `sha: null` only for intended deletions; `create_commit` parented at the current branch head; `update_ref` with `force: false`. This Git-object route successfully published the proof-compression changes.
- **Actions fallback:** use only for a demonstrated payload or tool limitation, never to bypass authorization or repository rules. Scope it to the delivery branch, pin actions, verify allowlisted paths and byte hashes, and separate read-only validation from minimally privileged publication. Remove temporary workflows and payloads on success or failure. Explicitly dispatch CI when a `GITHUB_TOKEN` push does not trigger it.

## Common errors and verification

- `422 Tree SHA does not exist`: a local tree hash is not a remote Git object. Create the tree on GitHub first; reuse verified uploaded blobs instead of uploading everything again.
- Stale file SHA or non-fast-forward: refetch, reapply, rerun affected checks, and retry once. Parent commits at the **current target-branch head**, not an old `main` SHA; never force an update to hide a race.
- Omitting `base_tree_sha` can delete unrelated paths. Omitting the branch in a content action can accidentally write to `main`.
- For manifests, the empty-byte SHA-256 is `hashlib.sha256(b'').hexdigest()`, not an empty string. Hash exact bytes, including binary files.
- A local commit, uploaded blobs, or a green validation/transport workflow is **not publication**. Refetch the remote branch and files; verify the final commit, changed paths, modes, and exact contents. For batch delivery, compare byte hashes with the validated manifest.
- Confirm temporary delivery files are absent and inspect CI for the **final remote SHA**, including any cleanup commit. Report that SHA, branch, PR when applicable, and actual check state; never claim that queued or running checks passed.
