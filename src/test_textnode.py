import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_equal_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD, 'www.github.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'www.github.com')
        self.assertEqual(node, node2)

    def test_equal(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_unequal_urls(self):
        node = TextNode("This is a text node", TextType.BOLD, 'www.github.com')
        node2 = TextNode("This is a text node", TextType.BOLD, 'www.github.com/someprofile')
        self.assertNotEqual(node, node2)

    def test_unequal_missing_url(self):
        node = TextNode("This is a text node", TextType.BOLD, 'www.github.com')
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_unequal_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_unequal_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()