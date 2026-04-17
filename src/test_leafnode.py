import unittest
from leafnode import LeafNode

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