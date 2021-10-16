#!/usr/bin/env python

"""Tests for `lorem_text` package."""

import re
import unittest

from click.testing import CliRunner

from lorem_text import cli, lorem


class TestLorem_text(unittest.TestCase):
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

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        help_result = runner.invoke(cli.main, ["--help"])
        sentence_result = runner.invoke(cli.main, ["--s"])
        words_result = runner.invoke(cli.main, ["--words=4"])
        assert help_result.exit_code == 0
        assert sentence_result.exit_code == 0
        assert words_result.exit_code == 0
        # Test for paragraph
        para_result = (runner.invoke(cli.main)).output
        size = len(re.split(",", para_result))
        assert 3 <= size <= 15
        # Test for words
        words_result = (runner.invoke(cli.main, "--words=120")).output
        word_len = len(words_result.split())
        assert word_len == 120
        # Test for sentence
        sentence_result = (runner.invoke(cli.main, "--s")).output
        size = len(re.split(",", sentence_result))
        assert 2 <= size <= 5


if __name__ == "__main__":
    unittest.main()
