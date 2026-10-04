# Repository instructions

- Make the smallest focused change that satisfies the issue.
- Reproduce defects with a failing test before changing production code.
- Use parameterized SQL queries. Never interpolate user input into SQL.
- Do not weaken, delete, or skip assertions to make tests pass.
- Run `pytest -q`, `ruff check .`, and `bandit -r app -q` after code changes.
- Update `docs/CHANGELOG.md` when behavior or security changes.
- Do not merge pull requests.
