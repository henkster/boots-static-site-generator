import unittest
from textnode import TextNode, TextType

class TestTextNode_ShouldBeEqualWithNoUrl(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

class TestTextNode_ShouldBeEqualWithNoDefaultAndNoneUrl(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertEqual(node, node2)

class TestTextNode_ShouldNotBeEqualWithDifferentTypes(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

class TestTextNode_ShouldBeEqualWithNoneText(unittest.TestCase):
    def test_eq(self):
        node = TextNode(None, TextType.BOLD) # None == None
        node2 = TextNode(None, TextType.BOLD)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()