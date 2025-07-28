from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

import re

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

def extract_markdown_images(text):
    pattern = r'!\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    
    return matches

def extract_markdown_links(text):
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, text)
    
    return matches

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(r'\[([^\]]+)\]\(([^)]+)\)', node.content)
        for i in range(0, len(parts), 3):
            if i < len(parts) and parts[i]:
                new_nodes.append(TextNode(TextType.TEXT, parts[i]))
            if i + 1 < len(parts):
                new_nodes.append(TextNode(TextType.LINK, parts[i + 1], parts[i + 2])) 

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = re.split(r'!\[([^\]]+)\]\(([^)]+)\)', node.content)
        for i in range(0, len(parts), 3):
            if i < len(parts) and parts[i]:
                new_nodes.append(TextNode(TextType.TEXT, parts[i]))
            if i + 1 < len(parts):
                new_nodes.append(TextNode(TextType.IMAGE, parts[i + 1], parts[i + 2]))

    return new_nodes

def text_to_textnodes(text):
    new_nodes = []
    if not text:
        return new_nodes

    node = TextNode(TextType.TEXT, text)
    new_nodes = split_nodes_image([node])
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)    

    return new_nodes