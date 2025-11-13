import unittest

from inline_helpers import split_nodes_delimiter
from textnode import *

class TestSplitNodesDelimiter(unittest.TestCase): 
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], '**', TextType.BOLD)
        self.assertListEqual([
                TextNode('This is text with a ', TextType.PLAIN),
                TextNode('bold', TextType.BOLD),
                TextNode(' word', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_italic(self):
        node = TextNode("This is text with a _italic_ word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertListEqual([
                TextNode('This is text with a ', TextType.PLAIN),
                TextNode('italic', TextType.ITALIC),
                TextNode(' word', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertListEqual([
                TextNode('This is text with a ', TextType.PLAIN),
                TextNode('code block', TextType.CODE),
                TextNode(' word', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_start_block(self):
        node = TextNode("`code block` word. This is...", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertListEqual([
                TextNode('code block', TextType.CODE),
                TextNode(' word. This is...', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_end_block(self):
        node = TextNode("This is a `code block`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertListEqual([
                TextNode('This is a ', TextType.PLAIN),
                TextNode('code block', TextType.CODE),
            ],
            new_nodes
        )

    def test_multiple_blocks(self):
        node = TextNode("This is a `code block` and another `code thing`.", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], '`', TextType.CODE)
        self.assertListEqual([
                TextNode('This is a ', TextType.PLAIN),
                TextNode('code block', TextType.CODE),
                TextNode(' and another ', TextType.PLAIN),
                TextNode('code thing', TextType.CODE),
                TextNode('.', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_ignore_unspecified_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], '_', TextType.ITALIC)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is text with a **bold** word")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
