# Changelog

## v0.1.1 - Maintenance and tooling

- CLI: handle missing or unreadable PGN files with a clean error and exit code 2
- Output: label move totals as "Moves (plies)" and document half-move semantics
- CI: run tests across Python 3.9–3.13 and add a ruff lint job
- Tests: cover comment/variation stripping, missing headers, empty input, NAG tokens
- Docs: add AGENTS.md, fix README quick-start example to match actual output
- Repo hygiene: remove private planning documents from the public tree

## v0.1.0 - Initial public foundation

- Added dependency-free PGN parsing helpers
- Added Markdown summary generation
- Added sample PGN file
- Added unit tests
- Added project documentation and roadmap
