import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("div", "Hello World", [HTMLNode("span", "Nested")], {"class": "test"})
        expected_repr = "HTMLNode(tag=div, value=Hello World, children=[HTMLNode(tag=span, value=Nested, children=[], props={})], props={'class': 'test'})"
        self.assertEqual(repr(node), expected_repr)

    def test_to_html(self):
        node = HTMLNode("div", "Hello World", [HTMLNode("span", "Nested")], {"class": "test"})
        expected_html = '<div class="test">Hello World<span>Nested</span></div>'
        # Uncomment the following line when to_html is implemented
        # self.assertEqual(node.to_html(), expected_html)   
        # For now, we will just check the raise NotImplementedError
        with self.assertRaises(NotImplementedError):
            node.to_html() 

        
    def test_props_to_html(self):
        node = HTMLNode("div", "Hello World", [], {"class": "test", "id": "main"})
        expected_props = 'class="test" id="main"'
        self.assertEqual(node.props_to_html(), expected_props)
        # Uncomment the following line when to_html is implemented
        # self.assertEqual(node.to_html(), f'<div {expected_props}>Hello World</div>')


if __name__ == "__main__":
    unittest.main()