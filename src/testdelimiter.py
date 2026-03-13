import unittest

from textnode import TextNode, TextType
from delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        result2 = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT),]
        self.assertEqual(result, result2)
    def test_eq2(self):
        old_nodes = [TextNode("This is text with a _italic_ word", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)
        result2 = [TextNode("This is text with a ", TextType.TEXT), TextNode("italic", TextType.ITALIC), TextNode(" word", TextType.TEXT),]
        self.assertEqual(result, result2)
    def test_eq3(self):
        old_nodes = [TextNode("This is text with a **bold** word", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        result2 = [TextNode("This is text with a ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" word", TextType.TEXT),]
        self.assertEqual(result, result2)
    def test_eq3(self):
        old_nodes = [TextNode("This is **text** with two **bold** words", TextType.TEXT)]
        result = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        result2 = [TextNode("This is ", TextType.TEXT), TextNode("text", TextType.BOLD), TextNode(" with two ", TextType.TEXT), TextNode("bold", TextType.BOLD), TextNode(" words", TextType.TEXT),]
        self.assertEqual(result, result2)


if __name__ == "__main__":
    unittest.main()
