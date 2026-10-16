# Code quality rules

Every factory agent should read this file; confirm that it did when checking a run. When an agent makes the same mistake twice, fix the current result and consider whether a rule or check would prevent a repeat. Test the change before adopting it. Keep each rule short and specific to this repo.

## General

- Make the smallest change that solves the issue. No drive-by refactors.
- Follow the patterns already used in the file you're changing.
- Every bug fix comes with a regression test that fails without the fix.
- No commented-out code, no debug logging, no TODOs without an issue number.
- Comments explain why, never what. Delete comments that repeat the code.

## This repo

Replace these examples with your own:

- Database changes go through a migration in `db/migrations/`. Never edit an existing migration.
- New API endpoints need a request test in `tests/api/`.
- UI components use the shared components in `src/ui/`. Don't add new CSS colours.
