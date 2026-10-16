---
name: build
description: Build and verify the change for one issue with the factory's implementer agent
argument-hint: "<issue-reference> [notes for the implementer]"
disable-model-invocation: true
---
Read `.factory/issue-tracker.md`. Resolve the issue reference using the connected MCP or CLI. Pass the canonical URL, tracker access details, safe key, and target code repo to the worker. Stop if the issue cannot be resolved.

Resolve the first argument as an issue reference. If a spec exists, obtain approval for its current revision before invoking Implement. Read the `factory-go` label or ask the person explicitly; a label is only an approval if a trusted maintainer added it. Capture the spec blob hash and pass it with the approval source to the implementer. Without a spec, require a triage report routing the issue to `build`.

Use the `implementer` agent on issue $0. If I added anything after the issue reference, pass it on as extra instructions: $ARGUMENTS

When it's done, show me the PR link and the Verification section of the PR description. If it's blocked, show me what it needs.
