import unittest

from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
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