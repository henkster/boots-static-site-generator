class HtmlNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""
        return "".join(f" {key}=\"{value}\"" for key, value in self.props.items())

    def __repr__(self):
        return f"HtmlNode(tag: {self.tag!r}, value: {self.value!r}, children: {self.children!r}, props: {self.props!r})" # !r calls the repr for each.

class ParentNode(HtmlNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("All parent nodes must have a tag")
        if not self.children:
            raise ValueError("All parent nodes must have children")

        html = f"<{self.tag}{super().props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
    
    def __repr__(self):
        return f"ParentNode(tag: {self.tag!r}, children: {self.children!r}, props: {self.props!r})"
        
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