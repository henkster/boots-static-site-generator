import unittest
from leafnode import LeafNode
from parentnode import ParentNode

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

if __name__ == "__main__":
    unittest.main()