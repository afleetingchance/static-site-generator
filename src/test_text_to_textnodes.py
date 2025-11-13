import unittest

from inline_helpers import text_to_textnodes
from textnode import *

class TestTextToTextnodes(unittest.TestCase): 
    def test_bold(self):
        new_nodes = text_to_textnodes("This is text with a **bold** word")
        self.assertListEqual([
                TextNode('This is text with a ', TextType.PLAIN),
                TextNode('bold', TextType.BOLD),
                TextNode(' word', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_italic(self):
        new_nodes = text_to_textnodes("This is text with a _italic_ word")
        self.assertListEqual([
                TextNode('This is text with a ', TextType.PLAIN),
                TextNode('italic', TextType.ITALIC),
                TextNode(' word', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_code(self):
        new_nodes = text_to_textnodes("This is text with a `code block` word")
        self.assertListEqual([
                TextNode('This is text with a ', TextType.PLAIN),
                TextNode('code block', TextType.CODE),
                TextNode(' word', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_split_images(self):
        new_nodes = text_to_textnodes("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)")
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        new_nodes = text_to_textnodes("This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)")
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_start_block(self):
        new_nodes = text_to_textnodes("`code block` word. This is...")
        self.assertListEqual([
                TextNode('code block', TextType.CODE),
                TextNode(' word. This is...', TextType.PLAIN),
            ],
            new_nodes
        )

    def test_end_block(self):
        new_nodes = text_to_textnodes("This is a `code block`")
        self.assertListEqual([
                TextNode('This is a ', TextType.PLAIN),
                TextNode('code block', TextType.CODE),
            ],
            new_nodes
        )

    def test_all_blocks(self):
        new_nodes = text_to_textnodes("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        self.assertListEqual([
                TextNode("This is ", TextType.PLAIN),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.PLAIN),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.PLAIN),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.PLAIN),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            new_nodes
        )