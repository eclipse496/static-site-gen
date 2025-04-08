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

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_string = node.text.split(delimiter)
        if len(split_string) == 1:
            # no delimiter found
            new_nodes.append(node)
            continue
        if len(split_string) % 2 == 0:
            # no matching closing delimiter
            raise Exception(f"No closing delimiter {delimiter} found in {node.text}")
        for i, str in enumerate(split_string):
            # even i = outside delimiter
            # odd i = inside delimiter
            if split_string[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(str, TextType.TEXT))
            else:
                split_nodes.append(TextNode(str, text_type))
        new_nodes.extend(split_nodes)
    return new_nodes