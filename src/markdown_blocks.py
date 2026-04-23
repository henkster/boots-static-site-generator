from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph",
    HEADING = "heading",
    CODE = "code",
    QUOTE = "quote",
    UNORDERED_LIST = "unordered_list",
    ORDERED_LIST = "ordered_list"
    
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    if re.search(r"^#{1,6}\s\w", block):
        return BlockType.HEADING
    if re.search(r"^\`{3}\n[\w\s\.]*\n\`{3}$", block):
        return BlockType.CODE
    if len(re.findall(r"^\>", block, re.MULTILINE)) == len(block.split("\n")):
        return BlockType.QUOTE
    if len(re.findall(r"^\-\s\w*", block, re.MULTILINE)) == len(block.split("\n")):
        return BlockType.UNORDERED_LIST
    if len(re.findall(r"^\d*\.\s\w*", block, re.MULTILINE)) == len(block.split("\n")) and re.search("^1", block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH