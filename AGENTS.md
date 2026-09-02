
# Repository instructions

## Mathematical authority

A mathematical claim is established by a numbered source under `proof/` whose
status supports the claim, or by an exact certificate explicitly incorporated
by the paper. Navigation files, interactive pages, prompts, experiments, and
failed approaches are not proof authorities.

## Non-negotiable conventions

- Use **C triangle** and **V triangle**.
- Let the original open triangles be \(U_C,U_0,\ldots,U_5\), with
  \(O\in U_C\) and \(V_i\in U_i\). Put \(T_C=\overline{U_C}\) and
  \(T_i=\overline{U_i}\). Use closed classifications on the \(T\)'s and retain
  the \(U\)'s whenever openness matters.
- Uppercase \((A_i,B_i,C_i)\) denotes actual maximal reaches.
- Lowercase \((a_i,b_i,c_i)\) denotes selected lower bounds and must be
  introduced by an explicit inequality such as \(a_i\le A_i\).
- Define \(N_+\) only from \(A_i+B_i>1\).
- Preserve singleton boundary gaps.
- Preserve the CE1/CE2 distinction, all endpoint strictness, actual V-type
  restrictions on neighboring support, connected-component selectors, and
  both charts in the Vd1 replacement.
- Do not replace the exact zero-gap certificate by numerical evidence.

## Repository layout

- `proof/`: proof sources and certificate code.
- `arrange/`: canonical paper and publication support.
- `interactive/`: generated and hand-authored visual explanations.
- `prompts/`: research prompt archive.

Do not recreate a top-level `tools`, `release`, `.vscode`, or formalization
directory. Put support code next to the content it validates.

## GitHub delivery from ChatGPT and Codex

GitHub capabilities depend on the active ChatGPT or Codex surface. Installing
the ChatGPT Codex Connector or loading this file does not itself grant write
access. Use the connector-native procedures below only when the current session
exposes approved write actions; otherwise report the capability limitation.

An external GitHub write is authorized only when the user explicitly asks to
push, publish, or open a pull request. A request to edit files does not authorize
external delivery. A request to commit without asking to push authorizes only a
local commit. The target repository is `dylan0301/hexagon-cover-database`, its
default branch is `main`, and its normal delivery path is a feature branch and
pull request.

`AGENTS.md` can route an agent to an available capability; it cannot grant an
unavailable tool, GitHub App scope, ChatGPT action permission, repository role,
or branch-policy bypass. Treat the local shell and the GitHub connector as
different authorization paths. In particular, a failed unauthenticated
`git push` from a sandbox does not establish that the connected GitHub App
cannot write.

Never request or commit a personal access token merely to deliver changes. Do
not put credentials in repository files, workflow inputs, logs, patches, or
artifacts.

### Connector preflight

Before an external write:

1. Finish the requested changes and run the checks required by this file.
2. Use the installed GitHub plugin or connector, not shell `git push`, as the
   first delivery path. Where the surface exposes them, resolve the authenticated
   login, GitHub App installation, selected repository, and repository metadata
   through read operations. Record unavailable fields as `not exposed`; do not
   infer that they passed or failed.
3. Inspect capabilities by the operations the current session can actually
   perform, not by assuming exact tool names. A one-file delivery needs branch
   creation plus create/update/delete-content actions that advance that branch.
   An atomic multi-file delivery needs blob, tree, commit, and non-forced ref
   update actions. Pull-request delivery also needs a create-or-find-PR action.
   Common non-normative names include `create_branch`, `create_file`,
   `update_file`, `delete_file`, `create_blob`, `create_tree`, `create_commit`,
   `update_ref`, `create_pull_request`, `fetch_file`, and `compare_commits`.
4. Check the connected identity's reported repository permission, but do not
   treat a metadata field such as `push: true` as proof that every write action
   is enabled. The action must also be exposed by the current ChatGPT or Codex
   surface, allowed by ChatGPT action controls, authorized by the GitHub App
   installation, and accepted by repository and organization rules.
5. Check the minimum permissions for the selected route: Contents write for
   file/Git-object/ref changes; Pull requests write for PR creation; Contents
   write plus Workflows write for creating or deleting
   `.github/workflows/**`; and Actions write for workflow dispatch. For an
   Actions bridge, also confirm that repository and organization policy permit
   the requested `GITHUB_TOKEN` write permissions.
6. Read the current `main` commit immediately before branch creation. When the
   user did not name a branch, create
   `chatgpt/<task-slug>-<UTC-YYYYMMDDHHMMSS>`, with a lowercase ASCII slug made
   only of letters, digits, and hyphens. When the user supplied a nonexistent
   branch, create it from fresh `main`; when it already exists, confirm it is the
   intended branch and begin at its current head instead of recreating it.
   Never treat `main` as a feature branch or write to it under this playbook.
7. Search for an open pull request with the same head and base. Reuse and update
   it instead of creating a duplicate.

If the current session exposes only search and fetch operations, report a
capability limitation rather than a repository permission failure. Do not keep
retrying equivalent reads or claim that this file can make the connector
writable.

### Preferred connector-native delivery

The delivery target is a feature branch and pull request to `main`. A successful
content action may create a commit and advance the named branch internally; it
does not also need a separately exposed `update_ref` action. Never omit the
feature-branch argument, because content actions commonly default to `main`.

For one UTF-8 text file within the connector's documented size and encoding
limits:

1. Create the feature branch from the exact fresh `main` commit, or refetch the
   current head of an existing user-supplied feature branch.
2. For a new path, create the file on that branch. Creating a file does not
   create the branch implicitly.
3. For an existing path, fetch the file on that branch, retain its current blob
   SHA, and pass that SHA with the complete replacement content to the update
   operation.
4. For a deletion, use a connector delete action with the current blob SHA, or
   use the atomic Git-object route below.
5. Do not run concurrent updates or deletes for the same path. Refetch before a
   subsequent operation because the first write changes the content SHA.

For multiple files, deletions, executable files, or binary artifacts such as
PDFs, publish one atomic commit through Git objects:

1. Fetch the feature branch's current head commit and tree.
2. Create a blob for every new or replaced file. Use UTF-8 only for text and
   base64 for exact binary bytes.
3. Create a tree with the current tree as `base_tree_sha`. Preserve each
   existing file mode; use `100644` for a new ordinary file and `100755` only
   for a file that must be executable. Use `type: "blob"` for ordinary files and
   a tree entry with `sha: null` only for an intended deletion.
4. Never omit `base_tree_sha` when modifying this repository: a root tree made
   from only the changed entries can make unrelated paths appear deleted.
5. Create one commit whose parent is the current feature-branch head, then move
   that branch to the new commit with a non-forced reference update. Creating
   blobs, a tree, or a commit alone does not publish the change; the reference
   update is the connector equivalent of a push.

After either path, fetch the resulting commit and compare the feature branch to
`main`. Confirm every changed path, status, mode, and the SHA-256 of the exact
remote bytes against the validated local result. Reuse the matching open pull
request or create one with that feature branch as `head` and `main` as `base`.
Report the branch, remote final-head commit SHA, pull-request URL, and check
state. A connector-created remote commit need not have the same SHA as a local
commit containing equivalent files.

On a stale file SHA or non-fast-forward update, read the new branch head,
reapply the intended changes, rerun affected checks, and retry once. Never set
`force: true` to resolve a race or branch-policy rejection.

### Classifying connector failures

Preserve the exact status, message, error details, retry headers, and
`X-Accepted-GitHub-Permissions` header when the connector returns them. Classify
failures before choosing a fallback:

- No write operation in the session: product-surface or workspace capability
  limitation.
- `401`: expired or revoked connection; the GitHub app must be reconnected.
- `403` or `Resource not accessible by integration`: missing ChatGPT action
  approval, GitHub App scope, user/repository permission, or a repository rule.
- `403` with rate-limit headers or `429`: throttling; honor `Retry-After` or the
  reset time rather than changing delivery routes.
- `404` for a known repository: GitHub may be masking a missing installation,
  repository selection, or authorization.
- `409`: stale branch or file state, a concurrent update, or a ref conflict.
- `422`: invalid or stale SHA/ref data, an existing new-file path, a duplicate
  branch, invalid pull-request base/head, no commits between the branches, or a
  ruleset rejection.
- `5xx` or an explicit transient connector failure: retry with bounded backoff;
  it is not evidence that Actions should replace the connector.

When `main` is protected, remain on the feature-branch and pull-request path.
Contents permission does not bypass required reviews, signed commits, naming
rules, restricted paths, size limits, or other rulesets. If delivery did not
produce a verifiable commit, do not say that the repository was updated.

### Controlled GitHub Actions fallback

Use this fallback only when all of the following are true:

- The user explicitly authorized external delivery.
- Connector write authorization is established, but a needed payload, binary,
  size, or atomic multi-file operation is absent or limited, and that exact
  capability limitation has been recorded.
- The connected identity can still create and later remove a transient workflow
  and its payload on the feature branch, and can inspect the resulting run.
- Repository and organization policy allow a feature-branch workflow to receive
  the narrowly scoped `GITHUB_TOKEN` permissions described below.
- The fallback remains confined to the same feature branch and pull-request
  workflow; it never writes directly to `main`.

Do not select this fallback after `401`, a non-rate-limit `403`, a masked
authorization `404`, disabled ChatGPT actions, insufficient App scopes,
insufficient repository role, or a ruleset denial. Those require reconnecting
or changing the relevant administrator-controlled permission or policy. If the
connector cannot install and remove the transient workflow, stop and report the
blocker. Do not invent credentials or describe Actions as a way to manufacture
connector permission.

Use `.github/workflows/chatgpt-apply-<task-slug>.yml` for the transient workflow
and `.github/_transient/<task-id>/` for its manifest and any payload. Use a
collision-resistant task ID. At the start of a retry or resumed delivery, first
remove or disable stale transient files belonging to that task. Install the
payload and manifest first and create the workflow last, or create all of them
in one atomic connector commit, so no run can observe a partial payload. Do not
use a top-level `tools` directory.

The workflow must:

- Trigger only for its exact feature branch and its exact transient workflow or
  payload paths. Give the task its own concurrency group with
  `cancel-in-progress: false`. Never use `pull_request_target` for this purpose.
- Set workflow-level permissions to none and use separate jobs on fresh runners.
  The validation job gets only `contents: read`; the publish job gets only
  `contents: write`; and an optional dispatch job gets `contents: read` plus
  `actions: write` and performs no checkout. Keep every other permission at
  `none`. Never combine repository-controlled validation and write permission in
  one job.
- Pin every `uses:` entry, including GitHub-owned actions, by a full commit SHA.
  Mirror the runner, environment, setup actions, language versions, and pinned
  build environment in `.github/workflows/ci.yml`; do not introduce floating
  versions. In the validation job, use a full-history checkout with
  `persist-credentials: false`, and begin shell programs with
  `set -euo pipefail`.
- Embed the expected manifest digest and audited base commit SHA in the reviewed
  workflow. The manifest must name the exact branch and base SHA and list every
  allowed path, operation (`add`, `replace`, or `delete`), final mode, and
  SHA-256 of the exact final bytes. Do not allow the payload to widen its own
  allowlist.
- Treat transported content as untrusted until verified. Permit only normalized
  repository-relative allowlisted paths. Reject absolute paths, `..`, NULs,
  symlinks, hardlinks, devices, FIFOs, sockets, and any unlisted file. If an
  archive is unavoidable, extract it into a temporary directory, validate every
  entry before copying, and copy only regular allowlisted files.
- In the read-only validation job, verify the audited base is an ancestor of the
  triggering commit and that the explicit range
  `<audited-base>..<trigger-SHA>` changes only the expected transient workflow,
  manifest, and payload paths. GitHub trigger path filters are not a security
  boundary. Apply only the reviewed payload and remove its transient files from
  the prospective bot tree.
- Run every applicable command under **Required checks**, including the two
  exact zero-gap certificate programs when their trigger condition below is
  met. After all checks and generation, revalidate the complete prospective bot
  tree against the manifest: compare an explicit base-to-tree changed-path and
  status list, every mode, and every final SHA-256. Upload that exact validated
  patch or tree as the handoff artifact; do not upload repository credentials.
- In the fresh publish job, download the validated artifact, verify its recorded
  digest and the embedded manifest again, and reconstruct the same prospective
  tree without executing repository code or any file from the artifact. Refetch
  the remote feature branch and refuse publication unless its head still equals
  the workflow trigger SHA. Revalidate the complete tree immediately before
  committing.
- Configure the commit identity as `github-actions[bot]`. Do not export the job
  token or persist checkout credentials; reference it only in the final guarded
  push. Because no repository-controlled code runs in the publish job, earlier
  checks cannot poison a token-bearing runner.
- Push one normal fast-forward commit to the exact feature branch. Never force
  push, rewrite `main`, or broaden the permissions of the persistent CI
  workflow.
- Do not assume a `GITHUB_TOKEN` push will trigger another workflow. Explicitly
  dispatch `.github/workflows/ci.yml` from the separate dispatch job. Preserve
  the reviewable validated artifact if the guarded push is rejected.

On every terminal path--success, check failure, rejected push, timeout, or
cancellation--the connected identity must remove or disable the transient
workflow first, then remove any remaining payload and manifest, and verify that
all are absent from the branch head. If interruption prevents immediate cleanup,
cleanup is the first operation on the resumed task. Report a cleanup failure
verbatim as a high-risk unresolved blocker, and never open a pull request while
a write-capable transient workflow remains installed.

After cleanup, reuse or open the normal pull request. Confirm the persistent CI
run against the exact final cleanup SHA; explicitly dispatch `ci.yml` again when
no PR or push event produced a run for that SHA. Do not weaken or edit the
persistent workflow to make the fallback pass.

### Delivery completion criteria

External delivery is complete only when the requested content is reachable from
the reported remote final-head SHA on the feature branch; every remote path,
status, mode, and byte digest has been refetched or compared; all transient
workflow, manifest, and payload paths are absent; and the matching pull request
exists. Checks must be associated with that exact final SHA. The handoff must
distinguish passing, failing, still-running, and `not exposed` check states and
include any unresolved permission, policy, or cleanup failure verbatim.

## Required checks

```bash
python -m pip install -r arrange/_support/requirements.txt
python proof/check.py
python interactive/generate.py --dependency-graph --check
python interactive/check.py
python arrange/build.py --all
```

Run the two exact zero-gap certificate programs whenever their source,
provenance, or dependent theorem changes.
