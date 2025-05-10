import re
import sys
import unittest
from unittest.mock import patch

from lorem_text import lorem
from lorem_text.cli import lorem_cli


class TestLoremText(unittest.TestCase):
    """Tests for `lorem_text` package."""

    def test_short_words(self):
        self.assertEqual(len(lorem.words(4).split()), 4, "Should be 4")

    def test_long_words(self):
        self.assertEqual(len(lorem.words(600).split()), 600, "Should be 600")

    def test_sentence(self):
        sen = lorem.sentence()
        size = len(re.split(",", sen))
        self.assertTrue(2 <= size <= 5)

    def test_paragraph(self):
        para = lorem.paragraph()
        size = len(re.split(",", para))
        self.assertTrue(2 <= size <= 15)

    def test_paragraphs(self):
        paras = lorem.paragraphs(2)
        size = len(paras)
        self.assertTrue(size >= 10)


class TestCLI(unittest.TestCase):
    def run_main(self, args):
        with patch.object(sys, "argv", ["prog"] + args):
            from io import StringIO
            from contextlib import redirect_stdout

            out = StringIO()
            with redirect_stdout(out):
                lorem_cli()
            return out.getvalue()

    def test_cli_main_exit_code(self):
        self.run_main([])  # should not raise

    def test_cli_help_exit_code(self):
        with self.assertRaises(SystemExit) as cm:
            self.run_main(["--help"])
        self.assertEqual(cm.exception.code, 0)

    def test_cli_sentence_flag_output(self):
        output = self.run_main(["--s"])
        size = len(re.split(r"[.!?]", output.strip()))
        self.assertTrue(2 <= size <= 5)

    def test_cli_words_flag_output(self):
        output = self.run_main(["--words=4"])
        self.assertEqual(len(output.split()), 4)

    def test_paragraph_output_size(self):
        output = self.run_main([])
        size = len(re.split(r"[.!?]", output.strip()))
        self.assertTrue(3 <= size <= 15)

    def test_words_output_120(self):
        output = self.run_main(["--words=120"])
        self.assertEqual(len(output.split()), 120)


if __name__ == "__main__":
    unittest.main()
