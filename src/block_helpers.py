import re

from functools import reduce
from block_types import BlockTypes
from parentnode import ParentNode
from inline_helpers import *

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    blocks = list(map(lambda block: block.strip(), blocks))
    blocks = list(filter(lambda block: block != '', blocks))
    return blocks

def block_to_block_type(text_block):
    if re.match(r'^\#{1,6} ', text_block):
        return BlockTypes.HEADING
    elif re.match(r'^\`\`\`.*?\`\`\`$', text_block, re.DOTALL):
        return BlockTypes.CODE
    elif reduce(lambda acc, line: acc and re.match(r'^\> ', line.strip()), text_block.split('\n'), True):
        return BlockTypes.QUOTE
    elif reduce(lambda acc, line: acc and re.match(r'^\- ', line.strip()), text_block.split('\n'), True):
        return BlockTypes.UNORDERED_LIST
    elif reduce(lambda acc, line: (acc[0] and re.match(rf'^{acc[1]}\. ', line.strip()), acc[1] + 1), text_block.split('\n'), (True, 1))[0]:
        return BlockTypes.ORDERED_LIST
    else:
        return BlockTypes.PARAGRAPH
    
def block_to_html_node(block, block_type):
    match block_type:
        case BlockTypes.HEADING:
            return block_to_h_parent_node(block)
        case BlockTypes.CODE:
            return block_to_code_parent_node(block)
        case BlockTypes.QUOTE:
            return block_to_quote_parent_node(block)
        case BlockTypes.UNORDERED_LIST:
            return block_to_unordered_list_parent_node(block)
        case BlockTypes.ORDERED_LIST:
            return block_to_ordered_list_parent_node(block)
        case _:
            return block_to_paragraph_parent_node(block)
        
def block_to_h_parent_node(block):
    match = re.match(r'^(\#+) (.*?)$', block, re.DOTALL)
    heading_count = len(match.group(1))
    children = markdown_to_children(match.group(2))
    return ParentNode(f'h{heading_count}', children)

def block_to_code_parent_node(block):
    match = re.match(r'^\`{3}\s*(.*?)\s*\`{3}$', block, re.DOTALL)
    children = markdown_to_children(match.group(1), False)
    return ParentNode('pre', [ParentNode('code', children)])

def block_to_quote_parent_node(block):
    block_items = list(map(lambda item: re.match(r'^\> (.*?)$', item.strip()).group(1), block.split('\n')))
    children = []
    for item in block_items:
        children.append(ParentNode('q', markdown_to_children(item)))

    return ParentNode('blockquote', children)

def block_to_unordered_list_parent_node(block):
    block_items = list(map(lambda item: re.match(r'^\- (.*?)$', item.strip()).group(1), block.split('\n')))
    children = []
    for item in block_items:
        children.append(ParentNode('li', markdown_to_children(item)))
    return ParentNode('ul', children)

def block_to_ordered_list_parent_node(block):
    block_items = list(map(lambda item: re.match(r'^\d+\. (.*?)$', item.strip()).group(1), block.split('\n')))
    children = []
    for item in block_items:
        children.append(ParentNode('li', markdown_to_children(item)))
    return ParentNode('ol', children)

def block_to_paragraph_parent_node(block):
    children = markdown_to_children(block)
    return ParentNode('p', children)

def markdown_to_children(markdown_text, should_format_inline=True):
    if markdown_text:
        children = []
        if should_format_inline:
            for text_node in text_to_textnodes(markdown_text):
                children.append(text_node_to_html_node(text_node))
        else:
            children.append(LeafNode(None, markdown_text))
        return children
    
    return []
    
def markdown_to_html_node(markdown_text):
    blocks = markdown_to_blocks(markdown_text)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        children.append(block_to_html_node(block, block_type))

    return ParentNode('div', children)
