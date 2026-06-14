# AGENTS.md

Guidance for AI coding agents (Codex, Claude, etc.) working in this repository.

## Project

Open Chess Analyzer is a dependency-free PGN parser and Markdown summary
generator written in Python with a `src/` layout. Engine-backed analysis
(Stockfish/UCI) is planned on the roadmap, not yet implemented.

## Layout

- `src/open_chess_analyzer/` — package: `pgn.py` (parser), `cli.py` (entry point)
- `tests/` — `unittest` suite
- `examples/` — sample PGN inputs
- `docs/` — architecture and design notes

## Setup

```bash
python -m pip install -e .
```

## Required checks before committing

Run both and make sure they pass:

```bash
python -m unittest discover -s tests   # tests
ruff check .                           # lint
```

CI runs the test suite on Python 3.9–3.13 and `ruff check` on 3.11. Every
change must keep all jobs green.

## Conventions

- Keep the core parser dependency-free. New runtime dependencies need discussion.
- Match the existing style. Ruff config (target `py39`) lives in `pyproject.toml`.
- Public API is re-exported from `open_chess_analyzer/__init__.py`; update
  `__all__` when adding public symbols.
- Add or update tests in `tests/` for any parser behavior change.
- Never commit API keys, tokens, engine binaries, or personal game databases
  (see `CONTRIBUTING.md`).

## Scope notes

- `GameSummary.move_count` counts half-moves (plies), not full moves.
- The parser handles a single PGN game; multi-game files are not split yet.

## Roadmap

See `ROADMAP.md`. Near-term: Stockfish/UCI evaluation, blunder/mistake
classification, Lichess/Chess.com PGN import, HTML reports.
