from enum import Enum
from htmlnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type: TextType, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    
    def __repr__(self):
        return str("TextNode(" + self.text + ", " + self.text_type.value + ", " + self.url + ")")
    
    
def text_node_to_html_node(text_node: TextNode):
    # (tag, value, props = None)
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        props = {"href": text_node.url}
        return LeafNode("a", text_node.text, props)
    if text_node.text_type == TextType.IMAGE:
        props = {"src": text_node.url, "alt": text_node.text}
        return LeafNode("img", "", props)
    # invalid type
    raise Exception("Textnode contains invalid TextType")