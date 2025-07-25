import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType
from converter import text_node_to_html_node 

class TestConverter(unittest.TestCase):
    def test_text(self):
        node = TextNode(TextType.TEXT, "This is a text node")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode(TextType.BOLD, "This is bold text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "strong")
        self.assertEqual(html_node.value, "This is bold text")
    
    def test_italic(self):
        node = TextNode(TextType.ITALIC, "This is italic text")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "em")
        self.assertEqual(html_node.value, "This is italic text")
    
    def test_code(self):
        node = TextNode(TextType.CODE, "This is code")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")
    
    def test_link(self):
        node = TextNode(TextType.LINK, "This is a link", "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "https://example.com")
    
    def test_image(self):
        node = TextNode(TextType.IMAGES, "This is an image", "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://example.com/image.png")
        self.assertEqual(html_node.props["alt"], "This is an image")
    
    def test_invalid_text_type(self):
        with self.assertRaises(ValueError):
            text_node_to_html_node(TextNode(None, "This is a md node"))
    

if __name__ == "__main__":
    unittest.main()