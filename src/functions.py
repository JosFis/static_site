from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.content.split(delimiter)
        for i, part in enumerate(parts):
            if i % 2 == 0:
                if part:
                    new_nodes.append(TextNode(TextType.TEXT, part))
            else:
                new_nodes.append(TextNode(text_type, part))

    return new_nodes
