"""Small dependency-free PGN parsing helpers.

This module intentionally implements only a conservative subset of PGN parsing.
It is enough for metadata extraction and lightweight public demos while the
project evolves toward full chess-engine backed analysis.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

HEADER_RE = re.compile(r'^\[(?P<key>[A-Za-z0-9_]+)\s+"(?P<value>.*)"\]$')
MOVE_NUMBER_RE = re.compile(r'\b\d+\.(?:\.\.)?')
COMMENT_RE = re.compile(r'\{[^}]*\}')
VARIATION_RE = re.compile(r'\([^()]*\)')
RESULT_TOKENS = {"1-0", "0-1", "1/2-1/2", "*"}


@dataclass(frozen=True)
class GameSummary:
    """Basic PGN game summary."""

    headers: dict[str, str]
    moves: list[str]

    @property
    def white(self) -> str:
        return self.headers.get("White", "Unknown")

    @property
    def black(self) -> str:
        return self.headers.get("Black", "Unknown")

    @property
    def result(self) -> str:
        return self.headers.get("Result", "*")

    @property
    def move_count(self) -> int:
        """Number of half-moves (plies) in the mainline."""
        return len(self.moves)


def _strip_variations(text: str) -> str:
    previous = None
    current = text
    while previous != current:
        previous = current
        current = VARIATION_RE.sub(" ", current)
    return current


def parse_pgn(pgn_text: str) -> GameSummary:
    """Parse a single PGN game into a lightweight summary.

    The parser extracts bracket headers and tokenizes mainline movetext while
    ignoring comments, numeric annotation glyphs, and simple variations.
    """
    headers: dict[str, str] = {}
    movetext_lines: list[str] = []

    for raw_line in pgn_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        match = HEADER_RE.match(line)
        if match:
            headers[match.group("key")] = match.group("value")
        else:
            movetext_lines.append(line)

    movetext = " ".join(movetext_lines)
    movetext = COMMENT_RE.sub(" ", movetext)
    movetext = _strip_variations(movetext)
    movetext = MOVE_NUMBER_RE.sub(" ", movetext)

    tokens = []
    for token in movetext.split():
        token = token.strip()
        if not token or token in RESULT_TOKENS:
            continue
        if token.startswith("$") and token[1:].isdigit():
            continue
        tokens.append(token)

    return GameSummary(headers=headers, moves=tokens)


def summarize_pgn(pgn_text: str) -> str:
    """Return a Markdown summary for a PGN game."""
    game = parse_pgn(pgn_text)
    event = game.headers.get("Event", "Unknown event")
    site = game.headers.get("Site", "Unknown site")
    date = game.headers.get("Date", "Unknown date")
    return "\n".join([
        "# Game Summary",
        "",
        f"- Event: {event}",
        f"- Site: {site}",
        f"- Date: {date}",
        f"- White: {game.white}",
        f"- Black: {game.black}",
        f"- Result: {game.result}",
        f"- Moves (plies): {game.move_count}",
        "",
    ])
