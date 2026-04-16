import unittest
from htmlnode import HtmlNode

# Can do a lot more with tests for HtmlNode and methods like props_to_html in the future.
class TestHtmlNode_Props_ShouldBeEmptyStringWhenNone(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode()
        self.assertEqual(node.props_to_html(), "")

class TestHtmlNode_Props_ShouldBeConvertedToHtmlWhenPresent(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode(props={"test1": "a", "test2": "b"})
        self.assertEqual(node.props_to_html(), " test1=\"a\" test2=\"b\"")

# This isn't that useful but a way to test my repr for now.
class TestHtmlNode_Repr(unittest.TestCase):
    def test_eq(self):
        node = HtmlNode(tag="testTag")
        self.assertEqual(str(node), "HtmlNode(tag: 'testTag', value: None, children: None, props: None)")

if __name__ == "__main__":
    unittest.main()