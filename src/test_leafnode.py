import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p_with_props(self):
        node = LeafNode("p", "Hello, world!", {'title': "Title Here", 'style': 'width: 100%;'})
        self.assertEqual(node.to_html(), '<p title="Title Here" style="width: 100%;">Hello, world!</p>')

    def test_leaf_to_html_raw_with_props(self):
        node = LeafNode(None, "Hello, world!", {'title': "Title Here", 'style': 'width: 100%;'})
        self.assertEqual(node.to_html(), 'Hello, world!')

    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_left_to_html_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_left_to_html_value_error_raw(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, None)
            node.to_html()


if __name__ == "__main__":
    unittest.main()