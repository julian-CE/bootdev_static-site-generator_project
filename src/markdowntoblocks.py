from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UL = "unordered_list"
    OL = "ordered_list"

def markdown_to_blocks(markdown):
    split = markdown.split("\n\n")
    result = []
    for block in split:
        block = block.strip()
        if len(block) == 0:
            continue
        result.append(block)
    return result

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UL
    current = 1
    if block.startswith(f"{current}. "):
        lines = block.split("\n")
        for line in lines:
            if not line.startswith(f"{current}. "):
                return BlockType.PARAGRAPH
            current+=1
        return BlockType.OL
    return BlockType.PARAGRAPH
    
