import unittest

from open_chess_analyzer import parse_pgn, summarize_pgn

SAMPLE = (
    '[Event "Club Training Game"]\n'
    '[Site "Local Club"]\n'
    '[Date "2026.06.14"]\n'
    '[White "Alice"]\n'
    '[Black "Bob"]\n'
    '[Result "1-0"]\n'
    "\n"
    "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 1-0\n"
)


class PgnParserTests(unittest.TestCase):
    def test_parses_headers(self):
        game = parse_pgn(SAMPLE)
        self.assertEqual(game.white, "Alice")
        self.assertEqual(game.black, "Bob")
        self.assertEqual(game.result, "1-0")

    def test_counts_move_tokens(self):
        game = parse_pgn(SAMPLE)
        self.assertEqual(game.move_count, 6)
        self.assertEqual(game.moves[:2], ["e4", "e5"])

    def test_summary_contains_markdown_fields(self):
        summary = summarize_pgn(SAMPLE)
        self.assertIn("# Game Summary", summary)
        self.assertIn("- White: Alice", summary)
        self.assertIn("- Moves (plies): 6", summary)

    def test_strips_comments_and_variations(self):
        pgn = (
            '[White "A"]\n[Black "B"]\n[Result "1-0"]\n\n'
            "1. e4 {best by test} e5 (1... c5 2. Nf3) 2. Nf3 Nc6 1-0\n"
        )
        game = parse_pgn(pgn)
        self.assertEqual(game.moves, ["e4", "e5", "Nf3", "Nc6"])

    def test_handles_missing_headers(self):
        game = parse_pgn("1. e4 e5 *\n")
        self.assertEqual(game.white, "Unknown")
        self.assertEqual(game.black, "Unknown")
        self.assertEqual(game.result, "*")
        self.assertEqual(game.move_count, 2)

    def test_empty_input(self):
        game = parse_pgn("")
        self.assertEqual(game.move_count, 0)
        self.assertEqual(game.result, "*")

    def test_ignores_nag_tokens(self):
        game = parse_pgn('[Result "*"]\n\n1. e4 $1 e5 $2 *\n')
        self.assertEqual(game.moves, ["e4", "e5"])


if __name__ == "__main__":
    unittest.main()
