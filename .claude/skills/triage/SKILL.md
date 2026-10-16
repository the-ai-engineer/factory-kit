---
name: triage
description: Triage one Linear or GitHub issue with the factory's triage agent
argument-hint: "<issue-reference>"
disable-model-invocation: true
---
Read `.factory/issue-tracker.md`. Resolve the issue reference using the connected MCP or CLI. Pass the canonical URL, tracker access details, safe key, and target code repo to the worker. Stop if the issue cannot be resolved.

Use the `triage` agent on issue $ARGUMENTS. Pass it the resolved tracker details.

When it's done, show me its SIZE and ROUTE lines and a two-sentence summary of what it found. Don't start any other stage.
