from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        # value is required for leafnode
        # no children allowed
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf nodes must have a value")
        if self.tag == None:
            # return raw text if no tag
            return self.value
        else:
            return (f"<{self.tag}>{self.value}</{self.tag}>")
        