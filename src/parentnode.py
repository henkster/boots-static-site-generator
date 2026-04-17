from htmlnode import HtmlNode

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