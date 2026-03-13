from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = "plain text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text:
            if self.text_type == other.text_type:
                if self.url == other.url:
                    return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise Exception("error: not valid text type")
    if text_node.text_type == TextType.TEXT:
        leaf = LeafNode(tag=None, value=text_node.text)
        return leaf
    if text_node.text_type == TextType.BOLD:
        leaf = LeafNode(tag="b", value=text_node.text)
        return leaf
    if text_node.text_type == TextType.ITALIC:
        leaf = LeafNode(tag="i", value=text_node.text)
        return leaf
    if text_node.text_type == TextType.CODE:
        leaf = LeafNode(tag="code", value=text_node.text)
        return leaf
    if text_node.text_type == TextType.LINK:
        leaf = LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        return leaf
    if text_node.text_type == TextType.IMAGE:
        leaf = LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        return leaf
    
