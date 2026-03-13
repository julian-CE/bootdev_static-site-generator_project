import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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

if __name__ == "__main__":
    unittest.main()
