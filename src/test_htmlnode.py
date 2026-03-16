import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from markdowntoblocks import markdown_to_html_node


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "hello cruel world", props={"href": "https://www.google.com", "target": "_blank"})
        response =  " href=\"https://www.google.com\" target=\"_blank\" "
        self.assertEqual(node.props_to_html(), response)
    def test_eq2(self):
        node = HTMLNode("p", "hello cruel world", props={"href": "https://www.boot.dev/dashboard", "target": "_blank"})
        response =  " href=\"https://www.boot.dev/dashboard\" target=\"_blank\" "
        self.assertEqual(node.props_to_html(), response)
    def test_not_eq(self):
        node = HTMLNode("p", "hello cruel world", props={"href": "https://www.google.com", "target": "_blank"})
        response =  " href=\"https://www.boot.dev/dashboard\" target=\"_blank\" "
        self.assertNotEqual(node.props_to_html(), response)
    
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_b(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
    def test_leaf_to_html_link1(self):
        node = LeafNode("p", "Hello, world!", props={"href": "https://www.boot.dev/dashboard", "target": "_blank"})
        self.assertEqual(node.to_html(), "<p href=\"https://www.boot.dev/dashboard\" target=\"_blank\">Hello, world!</p>")

class TestParentNode(unittest.TestCase):
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

class TestMDtoHTMLnode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

if __name__ == "__main__":
    unittest.main()
