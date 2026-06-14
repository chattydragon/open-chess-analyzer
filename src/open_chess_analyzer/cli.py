"""Command line interface for Open Chess Analyzer."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .pgn import summarize_pgn


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="open-chess-analyzer",
        description="Generate a Markdown summary for a PGN game.",
    )
    parser.add_argument("pgn_file", type=Path, help="Path to a PGN file")
    args = parser.parse_args(argv)

    pgn_path: Path = args.pgn_file
    try:
        pgn_text = pgn_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"error: file not found: {pgn_path}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"error: could not read {pgn_path}: {exc}", file=sys.stderr)
        return 2

    print(summarize_pgn(pgn_text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
