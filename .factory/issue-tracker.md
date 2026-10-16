# Issue tracker

Read this before any factory stage. Use the user's connected MCP or CLI for Linear or GitHub issues. GitHub still hosts the code and pull requests. Do not install another tracker client or copy a Linear issue into GitHub.

## Resolve the reference once

Accept a Linear key such as `LIN-123`, a Linear issue URL, a full GitHub issue URL such as `https://github.com/acme/app/issues/123`, or a GitHub issue number in the current repo. Read the issue with the connected tool. Use the tool's documented commands; do not invent a Linear CLI command.

A URL such as `https://github.com/issues/123` is missing the owner and repo. Ask for the full reference. If a key matches several connected workspaces, ask which one. If the tracker is unavailable, stop and explain what connection is missing.

Pass these details to every worker:

- Tracker, workspace or GitHub repo, and the tracker's issue ID.
- Canonical issue URL and displayed key or number.
- Target code repo, branch, spec path, and PR URL when known.
- Relevant findings, approved decisions, and how to access the tracker.

Use `factory/<key>` and `specs/<key>.md`. For Linear, the key is its identifier, for example `LIN-123`. For a GitHub issue in the target code repo, keep its number, for example `123`. For a GitHub issue in another repo, use `gh-<owner>-<repo>-<number>`. Check the branch name with `git check-ref-format --branch`. Never put a raw URL into a branch, path, or shell command. Verify that an existing branch or PR links the same canonical issue before reusing it; stop on a naming conflict.

## Use the original tracker

Read the issue, comments, and triage there. Search duplicates in the same workspace or repo. Save triage and run records as comments on that issue. Update an existing size field or label when supported; missing optional metadata must not block work. Do not create new tracker fields, labels, or workflow states automatically.

For GitHub, use the resolved issue URL or explicit repo when calling `gh issue`, so another repo's issue number is never applied to the target repo. For Linear, use its connected MCP or CLI. Preserve the original reference in reports and PR descriptions.

Find the code PR in the target GitHub repo by its resolved branch. Specs and code share that PR. Link the PR back on the original issue. Use `Closes #123` only for an issue in the same GitHub repo. Otherwise include the canonical issue URL without claiming to close it. A ready PR is not a completed issue; a person decides when to merge and close it.

## Approval and records

Spec approval is approval of the current spec revision, whether given in chat or on the PR. Pass the approval source and spec blob hash to the implementer. Human answers may be on the issue or PR; read both. Resume local runs with `/ship <issue-reference>` after approval or a decision. The supplied GitHub label workflow accepts only same-repo numeric `factory/<N>` branches. It does not dispatch Linear or cross-repo issues; do not tell those users that adding `factory-go` will start a run. The label is never a Linear issue label.

Post the `factory-ledger` comment on the original issue, including its canonical URL, key, target repo, branch, spec path, PR URL, times, outcome, and any pending decisions. Resume from this record and current PR state, not just chat memory. If writing the record fails, report the failure and current PR so the person can recover it.

For `/improve`, search recent ledger comments in the configured tracker workspace or repo. Use `factory-run` only if that label exists and is used there. Filter by the ledger's finished time, not just issue update time. If the connector cannot search comments, ask for issue references to score. Missing tracker access or search coverage must not be presented as zero runs. Count distinct canonical issue URLs, not bare numbers.

Agents inherit the session's tools so connected MCP tools remain available. Existing tool permissions still apply. Reviewer and scorer must not write to the tracker or PR. Prompts describe role boundaries; they do not enforce MCP access controls.
