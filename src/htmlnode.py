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
