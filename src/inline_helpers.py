import re

from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.PLAIN:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
        case _:
            raise TypeError('Invalid text type')

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_nodes = node.text.split(delimiter)
        for i in range(len(split_nodes)):
            if i % 2 == 0:
                if split_nodes[i] != '':
                    new_nodes.append(TextNode(split_nodes[i], node.text_type))
            else:
                new_nodes.append(TextNode(split_nodes[i], text_type))

    return new_nodes
            
def extract_markdown_images(text):
    if not isinstance(text, str):
        raise TypeError('text should be a string')

    return re.findall(r"\!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    if not isinstance(text, str):
        raise TypeError('text should be a string')

    return re.findall(r"(?:[^\!]|^)\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)

        if len(images) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        for i in range(len(images)):
            split_nodes = text.split(f'![{images[i][0]}]({images[i][1]})', 1)

            if split_nodes[0] != '':
                new_nodes.append(TextNode(split_nodes[0], TextType.PLAIN))
            new_nodes.append(TextNode(images[i][0], TextType.IMAGE, images[i][1]))
            text = split_nodes[1]

        if text != '':
            new_nodes.append(TextNode(text, TextType.PLAIN))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)

        if len(links) == 0:
            new_nodes.append(node)
            continue

        text = node.text
        for i in range(len(links)):
            split_nodes = text.split(f'[{links[i][0]}]({links[i][1]})', 1)

            if split_nodes[0] != '':
                new_nodes.append(TextNode(split_nodes[0], TextType.PLAIN))
            new_nodes.append(TextNode(links[i][0], TextType.LINK, links[i][1]))
            text = split_nodes[1]

        if text != '':
            new_nodes.append(TextNode(text, TextType.PLAIN))

    return new_nodes

def text_to_textnodes(text):
    start_node = TextNode(text, TextType.PLAIN)
    new_nodes = split_nodes_delimiter([start_node], '**', TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, '_', TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, '`', TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes