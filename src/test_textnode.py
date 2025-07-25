import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode(TextType.BOLD, "This is a text node")
        node2 = TextNode(TextType.BOLD, "This is a text node")
        self.assertEqual(node, node2)
    
    def test_not_equal_different_text(self):
        node = TextNode(TextType.BOLD, "Text A")
        node2 = TextNode(TextType.BOLD, "Text B")
        self.assertNotEqual(node, node2)

    def test_not_equal_different_type(self):
        node = TextNode(TextType.BOLD, "Same text")
        node2 = TextNode(TextType.ITALIC, "Same text")
        self.assertNotEqual(node, node2)

    def test_not_equal_different_url(self):
        node = TextNode(TextType.LINK, "anchor text](url1", url="url1")
        node2 = TextNode(TextType.LINK, "anchor text](url1", url="url2")
        self.assertNotEqual(node, node2)

    def test_equal_none_url(self):
        node = TextNode(TextType.TEXT, "plain text", url=None)
        node2 = TextNode(TextType.TEXT, "plain text", url=None)
        self.assertEqual(node, node2)

    def test_not_equal_one_none_url(self):
        node = TextNode(TextType.TEXT, "plain text", url=None)
        node2 = TextNode(TextType.TEXT, "plain text", url="http://example.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()