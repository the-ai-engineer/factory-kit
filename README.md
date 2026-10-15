# factory-kit

A small software factory for Claude Code. Four agents turn a GitHub issue into a reviewed pull request, and a fifth grades past runs so the factory can improve its own rules.

Everything is plain markdown in your repo, so the whole team runs the same process. You can drive it by hand with slash commands, or let GitHub Actions run it when someone adds a label.

## What's in here

```
.claude/
├── settings.json          # allows a small set of read-only git and gh commands
├── agents/
│   ├── triage.md          # researches, reproduces, sizes, routes (sonnet)
│   ├── spec-writer.md     # interviews you, writes specs/<N>.md (opus)
│   ├── implementer.md     # builds and proves the change (sonnet)
│   ├── reviewer.md        # adversarial review, returns a verdict (opus)
│   └── scorer.md          # grades finished runs (haiku)
└── skills/
    ├── ship/              # /ship <N>      the whole pipeline
    ├── triage/            # /triage <N>    one stage at a time...
    ├── spec/              # /spec <N>
    ├── build/             # /build <N>
    ├── critique/          # /critique <N>
    └── improve/           # /improve [days]
.factory/
└── code-quality.md        # your repo's rules; every agent reads it
.github/workflows/
├── factory.yml            # label an issue `factory` to run /ship
└── factory-improve.yml    # runs /improve every Monday
```

## Install

You need Claude Code, the GitHub CLI (`gh auth login`), and a GitHub repo.

```bash
git clone --branch codex/import-factory-kit https://github.com/the-ai-engineer/factory-kit
cd factory-kit
# For a fresh target repository with none of these directories:
cp -R .claude .factory .github /path/to/your-repo/
```

The target path is an example. If the repository already has any of these directories, merge files individually and review differences first. Do not overwrite existing agent definitions, settings, or workflows. The defaults allow only selected read-only commands; approve writes deliberately and add only the project commands you intend to allow.

Then, in your repo:

1. Make sure `CLAUDE.md` lists your build, lint, type check and test commands. The agents run whatever it says.
2. Add those commands to `permissions.allow` in `.claude/settings.json`, for example `"Bash(npm test *)"`.
3. Rewrite the "This repo" section of `.factory/code-quality.md`.
4. Commit it all, so the whole team gets the same factory.

## Run it by hand

Open Claude Code in your repo and pick an issue number:

```
/ship 42
```

Or one stage at a time, which is the best way to learn what each agent does:

```
/triage 42
/spec 42
/build 42
/critique 42
```

Small, clear issues skip the spec. Anything that needs a decision gets a spec PR first, and nothing is built until you approve it.

## Run it from GitHub

1. Add a repo secret called `FACTORY_ANTHROPIC_API_KEY`. Give the factory its own key so its spend shows up separately in the Claude Console.
2. Install the Claude GitHub app on the repo.
3. In `factory.yml`, add the target project’s dependency setup and test commands to `--allowedTools`. Review the write permissions, credentials, and trusted code before enabling headless execution.
4. Set the repository Actions variable `FACTORY_ENABLED` to `true`. Both workflows are opt-in; without their enable variables they skip the agent jobs.
5. Set `FACTORY_IMPROVE_ENABLED=true` only when you want weekly improvement runs. The schedule is Monday at 07:17 UTC, not local time.

The workflow checks out factory definitions from the default branch, accepts same-repository numeric `factory/<N>` PRs only, and checks that the triggering person has write, maintain, or admin access. It validates the issue number before passing it to Claude. These checks limit entry to the workflow; the agent still executes repository code, and role prompts are not a security sandbox.

Trusted operators can:

- add the `factory` label to an issue to start a run
- add the `factory-go` label to a factory PR to approve its spec or confirm a decision, which carries the run on

When enabled, the `improve` workflow opens a PR for repeated problems. A person reviews and merges it; score summaries are suggestions, not proof that a rule improves performance.

One thing to know: PRs opened with the default `GITHUB_TOKEN` don't trigger your other workflows, so your normal CI won't run on factory PRs. If you need it to, use a GitHub App token for `GH_TOKEN` instead.

## How the stages hand off

All state lives on GitHub, so local and CI runs see the same thing:

- triage posts a write-up comment on the issue and a `size:` label
- the spec and the code go on one branch, `factory/<N>`, with one PR
- the `factory-go` label on that PR records maintainer approval; `/ship` checks outstanding decisions and passes approval for the current spec revision. Direct `/build` must also obtain approval
- every run ends with a `factory-ledger` comment on the issue and the `factory-run` label, which is what `/improve` reads

## Make it yours

Fix the immediate problem, then investigate whether a rule or check would prevent it, in `.factory/code-quality.md`, `CLAUDE.md`, or the agent's own file. Test rule changes on representative tasks before using them more widely. Change an agent's model with the `model:` line at the top of its file.

## Validation and limits

Run `python3 -m unittest discover -s tests -v` in this repository for trigger-validation tests. They check numeric identifiers, fork rejection, repository and branch checks, and the shared task identifier. These tests do not run an LLM or prove the full workflow.

Agents and skills are editable instructions, not a deterministic workflow engine or permission sandbox. Worktrees share the host, credentials, ports, caches, and external services. Test the local stages on a disposable repository before enabling Actions. No API-backed end-to-end factory run has been performed for this import.

GitHub is the demonstrated tracker. The kit never merges PRs. Keep paid course prose out of this repository.
