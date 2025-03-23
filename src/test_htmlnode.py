import unittest

from htmlnode import HTMLNode, ParentNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is paragraph text")
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=This is paragraph text, children=None, props=None)")

class TestParentNode(unittest.TestCase):
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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_raw(self):
        node = LeafNode(None, "This is raw text")
        self.assertEqual(node.to_html(), "This is raw text")

    def test_leaf_to_html_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

    def test_leaf_to_html_custom_tag(self):
        node = LeafNode("BBQ", "I am surrounded by barbeque")
        self.assertEqual(node.to_html(), "<BBQ>I am surrounded by barbeque</BBQ>")

if __name__ == "__main__":
    unittest.main()