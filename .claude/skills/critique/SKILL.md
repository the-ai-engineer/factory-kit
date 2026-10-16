---
name: critique
description: Adversarial review of one issue's factory PR, reported here and never posted on GitHub
argument-hint: "<issue-number>"
disable-model-invocation: true
---
Use the `reviewer` agent on the PR for issue #$ARGUMENTS.

Show me its findings and verdict exactly as it wrote them. Don't fix anything and don't post anything on GitHub.
