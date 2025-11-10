import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child")
        child_node2 = LeafNode("p", "another child", {'title': 'A Title Here'})
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), '<div><span>child</span><p title="A Title Here">another child</p></div>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        with self.assertRaisesRegex(ValueError, 'ParentNode needs a tag'):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode(None, [child_node])
            parent_node.to_html()

    def test_to_html_tag_type_error(self):
        with self.assertRaisesRegex(TypeError, 'ParentNode tag needs to be a string'):
            child_node = LeafNode('span', "child")
            parent_node = ParentNode(True, [child_node])
            parent_node.to_html()

    def test_to_html_no_children(self):
        with self.assertRaisesRegex(ValueError, 'ParentNode needs children'):
            parent_node = ParentNode('div', None)
            parent_node.to_html()

    def test_to_html_empty_children(self):
        with self.assertRaisesRegex(ValueError, 'ParentNode needs children'):
            parent_node = ParentNode('div', [])
            parent_node.to_html()

    def test_to_html_children_type_error(self):
        with self.assertRaisesRegex(TypeError, 'ParentNode children needs to be a list'):
            parent_node = ParentNode('div', {'some prop': True})
            parent_node.to_html()

if __name__ == "__main__":
    unittest.main()