"""Command line interface for Open Chess Analyzer."""

from __future__ import annotations

import argparse
from pathlib import Path

from .pgn import summarize_pgn


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate a Markdown summary for a PGN game.")
    parser.add_argument("pgn_file", help="Path to a PGN file")
    args = parser.parse_args(argv)

    pgn_path = Path(args.pgn_file)
    pgn_text = pgn_path.read_text(encoding="utf-8")
    print(summarize_pgn(pgn_text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
