import unittest
from htmlnode import HtmlNode, ParentNode, LeafNode

# Can do a lot more with tests for HtmlNode and methods like props_to_html in the future.
class TestHtmlNode(unittest.TestCase):
    def test_props_should_be_empty_string_when_set_to_none(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_should_be_converted_to_html_when_present(self):
        node = HtmlNode(props={"test1": "a", "test2": "b"})
        self.assertEqual(node.props_to_html(), " test1=\"a\" test2=\"b\"")

    # This isn't that useful but a way to test my repr for now.
    def test_repr(self):
        node = HtmlNode(tag="testTag")
        self.assertEqual(str(node), "HtmlNode(tag: 'testTag', value: None, children: None, props: None)")

class TestParentNode(unittest.TestCase):
    # My original naming, not great yet.
    def test_to_html_should_create_paragraph_with_children_html(self):
        childnode1 = LeafNode("b", "Bold text")
        childnode2 = LeafNode(None, "Normal text")
        childnode3 = LeafNode("i", "Italic text")
        childnode4 = LeafNode(None, "Normal text")
        node = ParentNode("p", [childnode1, childnode2, childnode3, childnode4])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")

    # From lesson as helper, not consistent with my naming.
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

class TestLeaf(unittest.TestCase):
    def test_to_html_should_return_value_only_when_no_tag(self):
        node = LeafNode(None, "value")
        self.assertEqual(node.to_html(), "value")

    def test_to_html_should_createParagraphHtml(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_should_create_anchor_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_should_create_value_when_no_tag(self):
        node = LeafNode(None, "This is just raw text.")
        self.assertEqual(node.to_html(), "This is just raw text.")

    def test_to_html_should_raise_value_error_when_none_value(self):
        node = LeafNode("test", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_should_raise_value_error_when_value_is_empty_string(self):
        node = LeafNode("test", "")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_repr(self):
        node = LeafNode("tag", "value")
        self.assertEqual(str(node), "LeafNode(tag: 'tag', value: 'value', props: None)")

if __name__ == "__main__":
    unittest.main()