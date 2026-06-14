# Open Chess Analyzer

Open Chess Analyzer is an open-source PGN chess game analyzer designed for learners, coaches, and club players who want reproducible local game review reports.

The current `v0.1.0` scope focuses on a lightweight, dependency-free PGN parser and summary generator. The roadmap includes Stockfish/UCI engine evaluation, blunder detection, Lichess PGN import support, and beginner-friendly natural-language review reports.

## Why this project exists

Many chess players export PGN files from Lichess, Chess.com, or tournament software, but turning those games into structured learning notes still takes manual work. This project aims to make that workflow open, scriptable, and easy to extend.

## Features

- Parse PGN headers such as players, result, event, site, and date
- Count moves from PGN movetext
- Detect result and basic game metadata
- Generate Markdown analysis summaries
- Provide sample PGN data and tests
- Roadmap for Stockfish/UCI evaluation and mistake classification

## Installation

```bash
git clone https://github.com/chattydragon/open-chess-analyzer.git
cd open-chess-analyzer
python -m pip install -e .
```

No runtime dependency is required for the current basic parser.

## Quick start

```bash
python -m open_chess_analyzer examples/sample.pgn
```

Example output:

```markdown
# Game Summary

- White: Alice
- Black: Bob
- Result: 1-0
- Moves: 10
```

## Development

Run tests:

```bash
python -m unittest discover -s tests
```

## Project status

This repository is in early public development. The first goal is to provide a stable, tested base for PGN parsing and local analysis reports. Engine-backed evaluation and richer coaching feedback are planned next.

## Roadmap highlights

- Stockfish/UCI engine integration
- Blunder, mistake, and inaccuracy classification
- Lichess and Chess.com PGN import examples
- HTML and Markdown report generation
- GitHub Actions continuous integration
- Docker support
- Beginner-friendly explanations powered by optional API integrations

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [ROADMAP.md](ROADMAP.md).

## License

MIT License. See [LICENSE](LICENSE).
