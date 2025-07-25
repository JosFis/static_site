from htmlnode import LeafNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
    """
    Converts a TextNode to a LeafNode with HTML representation.
    """
    if text_node.text_type == TextType.TEXT:
        return LeafNode(value=text_node.content)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("strong", text_node.content)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("em", text_node.content)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.content)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.content, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGES:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.content})
    else:
        raise ValueError("Unsupported text type")