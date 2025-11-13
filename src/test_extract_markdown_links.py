import unittest

from inline_helpers import extract_markdown_links
from textnode import *

class TestExtractMarkdownLinks(unittest.TestCase): 
    def test_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        results = extract_markdown_links(text)
        self.assertListEqual([('to boot dev', 'https://www.boot.dev')], results)

    def test_multiple_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        results = extract_markdown_links(text)
        self.assertListEqual(
            [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')],
              results
        )

    def test_no_matches(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        results = extract_markdown_links(text)
        self.assertEqual(len(results), 0)

    def test_no_matches(self):
        text = "This is image ![to boot dev](https://www.boot.dev)"
        results = extract_markdown_links(text)
        self.assertEqual(len(results), 0)

    def test_text_type_error(self):
        with self.assertRaisesRegex(TypeError, 'text should be a string'):
            extract_markdown_links(False)
