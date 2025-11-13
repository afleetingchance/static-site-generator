import unittest

from block_helpers import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph\ntext in a p\ntag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_headings(self):
        md = """
            # This is **bolded** heading

            ## sub heading

            ### sub sub heading

            #### heading x4

            ##### heading x5

            ###### heading x6

            This is a paragraph with _italic_ text and `code` here
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is <b>bolded</b> heading</h1><h2>sub heading</h2><h3>sub sub heading</h3><h4>heading x4</h4><h5>heading x5</h5><h6>heading x6</h6><p>This is a paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff</code></pre></div>",
        )

    def test_quoteblock(self):
        md = """
            > This text some _italic words_
            > And some **bold words** too
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote><q>This text some <i>italic words</i></q><q>And some <b>bold words</b> too</q></blockquote></div>",
        )

    def test_unorderedblock(self):
        md = """
            - This text some _italic words_
            - And some **bold words** too
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This text some <i>italic words</i></li><li>And some <b>bold words</b> too</li></ul></div>",
        )

    def test_orderedblock(self):
        md = """
            1. This text some _italic words_
            2. And some **bold words** too
        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This text some <i>italic words</i></li><li>And some <b>bold words</b> too</li></ol></div>",
        )