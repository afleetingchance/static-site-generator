import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode('div', 'Some text', props={'title': 'Hello World', 'type': 'submit', 'style': 'width: 100%; text-align: center;'})
        expected = ' title="Hello World" type="submit" style="width: 100%; text-align: center;"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_none_props(self):
        node = HTMLNode('div', 'Some text')
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_empty_props(self):
        node = HTMLNode('div', 'Some text', props={})
        self.assertEqual(node.props_to_html(), '')

    def test_props_to_html_type_error_props(self):
        with self.assertRaises(TypeError):
            node = HTMLNode('div', 'Some text', props=['some attribute'])
            node.props_to_html()

if __name__ == "__main__":
    unittest.main()