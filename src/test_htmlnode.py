import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    ## HTMLNode
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

    ## LeafNode
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_span(self):
        node = LeafNode("span", "Inline text")
        self.assertEqual(node.to_html(), "<span>Inline text</span>")
    
    def test_leaf_to_html_no_tag(self): 
        node = LeafNode(value="Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_no_value(self):
        node = LeafNode("div")
        with self.assertRaises(ValueError):
            node.to_html()
            
    def test_leaf_node_no_value(self):
        node = LeafNode("div")
        with self.assertRaises(ValueError):
            node.to_html()

    ## ParentNode
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_no_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "No tag")])

    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

if __name__ == "__main__":
    unittest.main()