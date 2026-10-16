---
name: spec
description: Interview me about a triaged issue, then write the spec to a draft PR
argument-hint: "<issue-reference>"
disable-model-invocation: true
---
Read `.factory/issue-tracker.md`. Resolve the issue reference using the connected MCP or CLI. Pass the canonical URL, tracker access details, safe key, and target code repo to the worker. Stop if the issue cannot be resolved.

1. Use the `spec-writer` agent in questions mode for issue $ARGUMENTS.
2. Ask me all of its questions in one go, with its suggested answer under each. If I say "go", use its suggestions.
3. Use the `spec-writer` agent in write mode for issue $ARGUMENTS and pass it my answers word for word.
4. Show me the PR link and stop. I'll read the spec and approve it before anything gets built.
