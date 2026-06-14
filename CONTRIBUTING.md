# Contributing to Open Chess Analyzer

Thank you for considering a contribution.

## Ways to contribute

- Report PGN parsing bugs
- Add sample PGN files from different sources
- Improve documentation and examples
- Add tests for edge cases
- Help design Stockfish/UCI integration
- Improve report output formats

## Development setup

```bash
git clone https://github.com/chattydragon/open-chess-analyzer.git
cd open-chess-analyzer
python -m pip install -e .
python -m unittest discover -s tests
```

## Pull request guidelines

- Keep changes focused and small
- Add or update tests when changing parser behavior
- Do not commit API keys, tokens, engine binaries, or personal game databases
- Prefer reproducible examples under `examples/`

## Issue labels to use

- `bug`: incorrect behavior
- `enhancement`: new capability
- `documentation`: docs-only improvement
- `good first issue`: suitable for new contributors
- `help wanted`: useful but not currently assigned
