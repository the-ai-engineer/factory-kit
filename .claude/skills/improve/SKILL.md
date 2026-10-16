---
name: improve
description: Score recent factory runs and open a PR that fixes the factory's most common failures
argument-hint: "[days, default 14]"
disable-model-invocation: true
---
1. Validate the optional days argument as a positive integer; default to 14. Find recent runs: `gh issue list --label factory-run --state all --limit 100 --json number,updatedAt`. Keep the issues updated in the last $ARGUMENTS days, or 14 days if no number was given.
2. Use the `scorer` agent on each issue. Run several at once. Report missing data as unverified; do not average missing values as zero. Group repeated causes by distinct issue number so repeated attempts on one issue do not look like three separate issues.
3. Group the results by `cause`. Ignore `none`, and ignore any cause that appears fewer than three times.
4. For each cause that repeats, read the evidence and decide on one small fix to the factory itself. That means `CLAUDE.md`, `.factory/code-quality.md`, or a file in `.claude/agents/` or `.claude/skills/`. Never change application code here.
5. Make the edits in a fresh worktree. Resolve and fetch the default branch. Generate a unique run suffix using a UTC timestamp plus a random identifier; use it in both the worktree path and `factory-improve/<suffix>` branch. Do not reuse a fixed path or date-only branch. Commit, push the branch, and open a PR. In the description, list each cause, how many runs it hit, their issue numbers, and the edit that addresses it. Add a table of the average scores. Confirm the commit and PR are preserved before removing the worktree. Never merge your own improvements.
6. If no cause repeats, don't open a PR. Just report the average scores.
