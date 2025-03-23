class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if self.props is not None:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children = None, props = None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Parent node must have children")
        content = ""
        for child in self.children:
            content = str(content + child.to_html())
        return f"<{self.tag}>{content}</{self.tag}>"
    
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