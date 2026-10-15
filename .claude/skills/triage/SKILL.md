---
name: triage
description: Triage one GitHub issue with the factory's triage agent
argument-hint: "<issue-number>"
disable-model-invocation: true
---
Use the `triage` agent on issue #$ARGUMENTS. Give it the issue number. It reads everything else itself.

When it's done, show me its SIZE and ROUTE lines and a two-sentence summary of what it found. Don't start any other stage.
