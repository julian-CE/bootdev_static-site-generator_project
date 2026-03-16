from enum import Enum
from htmlnode import ParentNode, LeafNode, HTMLNode
from splitimglinknodes import text_node_to_html_node, text_to_textnodes


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
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            text = block.replace("\n", " ")
            node = ParentNode("p", text_to_children(text))
            children.append(node)
        elif block_type == BlockType.HEADING:
            tag_count = get_tag_count(block)
            text = block[tag_count + 1:]
            node = ParentNode(f"h{tag_count}", text_to_children(text))
            children.append(node)
        elif block_type == BlockType.CODE:
            text = block[4:-3]
            text_leaf = LeafNode(None, text)
            code_node = ParentNode("code", [text_leaf])
            pre_node = ParentNode("pre", [code_node])
            children.append(pre_node)
        elif block_type == BlockType.QUOTE:
            text = process_quote(block)
            node = ParentNode("blockquote", text_to_children(text))
            children.append(node)
        elif block_type == BlockType.UL:
            lines = block.split("\n")
            items = []
            for line in lines:
                text = line[2:]
                node = ParentNode("li", text_to_children(text))
                items.append(node)
            node = ParentNode("ul", items)
            children.append(node)
        elif block_type == BlockType.OL:
            lines = block.split("\n")
            items = []
            for line in lines:
                parts = line.split(". ", 1)
                text = parts[1]
                node = ParentNode("li", text_to_children(text))
                items.append(node)
            node = ParentNode("ol", items)
            children.append(node)
    return ParentNode("div", children)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []

    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))

    return children

def get_tag_count(text):
    count = 0
    for char in text:
        if char == "#":
            count+=1
        else:
            break
    return count

def process_quote(text):
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(line[1:].strip())
    text = " ".join(cleaned_lines)
    return text

def process_list(text):
    lines = text.split("\n")
    cleaned_lines = []
    for line in lines:
        cleaned_lines.append(lines[1:].strip())
    text = " ".join(cleaned_lines)
    return text
