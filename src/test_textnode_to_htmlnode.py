import unittest

from main import text_node_to_html_node
from textnode import *

class TestTextNodeToHtmlNode(unittest.TestCase): 
    def test_plain(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), '<b>This is a bold node</b>')

    def test_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.value, "This is a italic node")
        self.assertEqual(html_node.to_html(), '<i>This is a italic node</i>')

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.value, "This is a code node")
        self.assertEqual(html_node.to_html(), '<code>This is a code node</code>')

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, 'www.github.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.to_html(), '<a href="www.github.com">This is a link node</a>')

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, 'github.png')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.to_html(), '<img src="github.png" alt="This is an image node"></img>')

    def test_image_no_alt(self):
        node = TextNode(None, TextType.IMAGE, 'github.png')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.to_html(), '<img src="github.png"></img>')

    def test_invalid_text_type(self):
        with self.assertRaisesRegex(TypeError, 'Invalid text type'):
            node = TextNode('What type am I?', 'Some nonsense')
            text_node_to_html_node(node)