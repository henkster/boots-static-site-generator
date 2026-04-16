import unittest
from leafnode import LeafNode

# Can do a lot more with tests for HtmlNode and methods like props_to_html in the future.
class TestLeaf_BasicCreation(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(None, "value")
        self.assertEqual(node.to_html(), "value")

class TestLeafNode_ShouldCreateParagraphHtml(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

class TestLeafNode_ShouldCreateAnchorHtml(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

class TestLeafNode_ShouldCreateValueWhenNoTag(unittest.TestCase):
    def test_eq(self):
        node = LeafNode(None, "This is just raw text.")
        self.assertEqual(node.to_html(), "This is just raw text.")

class TestLeafNode_ShouldRaiseValueErrorWhenNoneValue(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("test", None)
        with self.assertRaises(ValueError):
            node.to_html()

class TestLeafNode_ShouldRaiseValueErrorWhenEmptyStringValue(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("test", "")
        with self.assertRaises(ValueError):
            node.to_html()

class TestLeafNode_Repr(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("tag", "value")
        self.assertEqual(str(node), "LeafNode(tag: 'tag', value: 'value', props: None)")

if __name__ == "__main__":
    unittest.main()