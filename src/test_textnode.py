import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_with_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_no_default_and_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

    def test_not_eq_with_different_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_with_none_text(self):
        node = TextNode(None, TextType.BOLD) # None == None
        node2 = TextNode(None, TextType.BOLD)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()