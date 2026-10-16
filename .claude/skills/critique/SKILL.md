---
name: critique
description: Adversarial review of one issue's factory PR, reported here and never posted on GitHub
argument-hint: "<issue-reference>"
disable-model-invocation: true
---
Read `.factory/issue-tracker.md`. Resolve the issue reference using the connected MCP or CLI. Pass the canonical URL, tracker access details, safe key, and target code repo to the worker. Stop if the issue cannot be resolved.

Use the `reviewer` agent on the PR for issue $ARGUMENTS.

Show me its findings and verdict exactly as it wrote them. Don't fix anything and don't post anything on GitHub.
