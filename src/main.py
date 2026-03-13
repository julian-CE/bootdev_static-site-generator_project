print("hello world")
from textnode import TextNode, TextType
from htmlnode import HTMLNODE, LeafNode, ParentNode

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    grandchild = LeafNode("b", "grandchild")
    child = ParentNode("span", [grandchild])
    parent = ParentNode("div", [child])

    print(parent.to_html())


main()
