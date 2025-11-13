import unittest

from inline_helpers import extract_markdown_images
from textnode import *

class TestExtractMarkdownImages(unittest.TestCase): 
    def test_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        results = extract_markdown_images(text)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], 'rick roll')
        self.assertEqual(results[0][1], 'https://i.imgur.com/aKaOqIh.gif')

    def test_multiple_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        results = extract_markdown_images(text)
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0][0], 'rick roll')
        self.assertEqual(results[0][1], 'https://i.imgur.com/aKaOqIh.gif')
        self.assertEqual(results[1][0], 'obi wan')
        self.assertEqual(results[1][1], 'https://i.imgur.com/fJRm4Vk.jpeg')

    def test_no_matches(self):
        text = "This is text with a [rick roll](https://i.imgur.com/aKaOqIh.gif)"
        results = extract_markdown_images(text)
        self.assertEqual(len(results), 0)

    def test_text_type_error(self):
        with self.assertRaisesRegex(TypeError, 'text should be a string'):
            extract_markdown_images(False)
