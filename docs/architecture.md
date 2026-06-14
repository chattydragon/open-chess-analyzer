# Architecture

Open Chess Analyzer starts with a small local-first architecture:

1. PGN input
2. Parser and metadata extraction
3. Analysis modules
4. Report generation

The current release implements steps 1, 2, and a basic Markdown report. Planned modules include optional Stockfish/UCI engine evaluation, mistake classification, and richer learning reports.

## Design principles

- Local-first and privacy-preserving by default
- Reproducible analysis from plain PGN files
- Optional integrations rather than mandatory cloud dependencies
- Small, testable modules
