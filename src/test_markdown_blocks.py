import unittest
from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_from_assignment_with_a_line_with_space(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

 

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_normal_heading(self):
        result = block_to_block_type("###### word ")
        self.assertEqual(result, BlockType.HEADING)

    def test_not_heading_with_seven_hashes(self):
        result = block_to_block_type("####### word ")
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_normal_code(self):
        text = """
```
This is a code block.
```
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.CODE)

    def test_normal_quote(self):
        text = """
> First
> Second
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.QUOTE)

    def test_not_quote_missing_gt(self):
        text = """
> First
Second
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_quote_without_space(self):
        text = """
>First
>Second
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.QUOTE)

    def test_normal_unordered_list(self):
        text = """
- First
- Second
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_not_unordered_list_with_space_first(self):
        text = """
 - First
- Second
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_normal_ordered_list(self):
        text = """
1. First
20. Second
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_ordered_list_must_start_with_1(self):
        text = """
2. First
3. Second
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_ordered_list_with_space_first(self):
        text = """
1. First
 20. Second
""".strip("\n")
        result = block_to_block_type(text)
        self.assertEqual(result, BlockType.PARAGRAPH)

    # From solution, pretty lacking
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()