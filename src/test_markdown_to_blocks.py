import unittest

from block_helpers import markdown_to_blocks
from textnode import *

class TestMarkdownToBlocks(unittest.TestCase): 
    def test_multiple_blocks(self):
        blocks = markdown_to_blocks('''# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
This is the same paragraph on a new line

- This is the first list item in a list block
- This is a list item
- This is another list item'''
        )
        self.assertListEqual([
                '# This is a heading',
                '''This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
This is the same paragraph on a new line''',
                '''- This is the first list item in a list block
- This is a list item
- This is another list item'''
            ],
            blocks
        )

    def test_single_block(self):
        blocks = markdown_to_blocks('# This is a heading')
        self.assertListEqual(['# This is a heading'],
            blocks
        )

    def test_extra_whitespace(self):
        blocks = markdown_to_blocks('''  # This is a heading
''')
        self.assertListEqual(['# This is a heading'],
            blocks
        )

    def test_extra_new_lines(self):
        blocks = markdown_to_blocks('''# This is a heading




This is a paragraph of text. It has some **bold** and _italic_ words inside of it.''')
        self.assertListEqual([
                '# This is a heading',
                'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.',
            ],
            blocks
        )