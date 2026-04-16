from htmlnode import HtmlNode

class LeafNode(HtmlNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if self.tag:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        return self.value
    
    def __repr__(self):
        return f"LeafNode(tag: {self.tag!r}, value: {self.value!r}, props: {self.props!r})"