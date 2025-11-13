import unittest

from block_helpers import block_to_block_type
from block_types import BlockTypes

class TestBlockToBlocktype(unittest.TestCase):
    def test_heading1(self):
        block_type = block_to_block_type('# This is a heading')
        self.assertEqual(BlockTypes.HEADING, block_type)

    def test_heading6(self):
        block_type = block_to_block_type('###### This is a heading')
        self.assertEqual(BlockTypes.HEADING, block_type)

    def text_fail_heading7(self):
        block_type = block_to_block_type('####### This is a heading?')
        self.assertEqual(BlockTypes.PARAGRAPH, block_type)

    def test_code(self):
        block_type = block_to_block_type('```This is a code block```')
        self.assertEqual(BlockTypes.CODE, block_type)

    def test_fail_code_prefix(self):
        block_type = block_to_block_type('more code? ```This is a code block```')
        self.assertEqual(BlockTypes.PARAGRAPH, block_type)

    def test_fail_code_suffix(self):
        block_type = block_to_block_type('```This is a code block``` more code?')
        self.assertEqual(BlockTypes.PARAGRAPH, block_type)

    def test_code(self):
        block_type = block_to_block_type('```This is a code block```')
        self.assertEqual(BlockTypes.CODE, block_type)

    def test_single_quote(self):
        block_type = block_to_block_type('> This is a quote')
        self.assertEqual(BlockTypes.QUOTE, block_type)

    def test_multiline_quote(self):
        block_type = block_to_block_type('> This is a quote   \n> This is another quote')
        self.assertEqual(BlockTypes.QUOTE, block_type)

    def test_fail_not_all_line_quotes(self):
        block_type = block_to_block_type('> This is a quote\nThis is another quote?')
        self.assertEqual(BlockTypes.PARAGRAPH, block_type)

    def test_single_unordered(self):
        block_type = block_to_block_type('- This is a u list item')
        self.assertEqual(BlockTypes.UNORDERED_LIST, block_type)

    def test_multiline_unordered(self):
        block_type = block_to_block_type('- This is a u list item\n- Another u list item')
        self.assertEqual(BlockTypes.UNORDERED_LIST, block_type)

    def test_fail_not_all_line_unordered(self):
        block_type = block_to_block_type('- This is a u list item\n-Another u list item?')
        self.assertEqual(BlockTypes.PARAGRAPH, block_type)

    def test_single_ordered(self):
        block_type = block_to_block_type('1. This is a u list item')
        self.assertEqual(BlockTypes.ORDERED_LIST, block_type)

    def test_multiline_ordered(self):
        block_type = block_to_block_type('1. This is a u list item\n2. Another u list item')
        self.assertEqual(BlockTypes.ORDERED_LIST, block_type)

    def test_fail_not_all_line_ordered(self):
        block_type = block_to_block_type('1. This is a u list item\n2.Another u list item?')
        self.assertEqual(BlockTypes.PARAGRAPH, block_type)

    def test_fail_ordered_not_start_at_one(self):
        block_type = block_to_block_type('2. This is a u list item\n3.Another u list item?')
        self.assertEqual(BlockTypes.PARAGRAPH, block_type)

    def test_fail_ordered_skips_number(self):
        block_type = block_to_block_type('1. This is a u list item\n3.Another u list item?')
        self.assertEqual(BlockTypes.PARAGRAPH, block_type)