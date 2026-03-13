from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            result.append(node)
            continue
        if delimiter not in node.text:
            result.append(node)
            continue
        new_nodes = []
        split_old_node = node.text.split(delimiter)
        if len(split_old_node) % 2 == 0:
            raise Exception("error: invalid delimiter syntax")
        for i in range(len(split_old_node)):
            if split_old_node[i] == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(split_old_node[i], TextType.TEXT))
            else:
                new_nodes.append(TextNode(split_old_node[i], text_type))
        result.extend(new_nodes)
    
    return result
