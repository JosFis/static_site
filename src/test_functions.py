import unittest

from textnode import TextNode, TextType
from functions import split_nodes_delimiter, extract_markdown_images, extract_markdown_links

class TestFunctions(unittest.TestCase):
    # split_nodes_delimiter
    def test_split_nodes_delimiter_code(self):
        node = TextNode(TextType.TEXT, "This is text with a `code block` word")
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].content, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].content, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].content, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT) 

    def test_split_nodes_delimiter_bold(self):
        node = TextNode(TextType.TEXT, "This is text with a **bolded phrase** in the middle")
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
       
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].content, "This is text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].content, "bolded phrase")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].content, " in the middle")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT) 
        
    def test_split_nodes_delimiter_italic(self):
        node = TextNode(TextType.TEXT, "This is text with an _italicized word_ in the middle")
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].content, "This is text with an ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].content, "italicized word")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[2].content, " in the middle")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
    
    def test_split_nodes_delimiter_none(self):
        node = TextNode(TextType.TEXT, "This is plain text without delimiters")
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].content, "This is plain text without delimiters")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
    
    def test_split_nodes_delimiter_bold_italic(self):
        node = TextNode(TextType.TEXT, "This is **bold** and _italic_ text")
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)

        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].content, "This is ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].content, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].content, " and ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].content, "italic")
        self.assertEqual(new_nodes[3].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[4].content, " text")
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT) 

    # extract_markdown_images
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    # extract_markdown_links
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a link [link](https://www.google.com), please check it out!"
        )
        self.assertListEqual([("link", "https://www.google.com")], matches)

    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

        

if __name__ == "__main__":
    unittest.main()