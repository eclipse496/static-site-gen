import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is paragraph text")
        self.assertEqual(repr(node), "HTMLNode(tag=p, value=This is paragraph text, children=None, props=None)")

if __name__ == "__main__":
    unittest.main()