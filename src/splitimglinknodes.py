from textnode import TextNode, TextType
from re_handler import extract_markdown_images, extract_markdown_links
from delimiter import split_nodes_delimiter

def split_nodes_image(old_nodes):
    result = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            result.append(node)
            continue
        original_text = node.text
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            before_img = sections[0]
            if sections[0] != "":
                result.append(TextNode(before_img, TextType.TEXT))
            result.append(TextNode(image[0], TextType.IMAGE, image[1]))
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            result.append(node)
            continue
        original_text = node.text
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            before_link = sections[0]
            if sections[0] != "":
                result.append(TextNode(before_link, TextType.TEXT))
            result.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            result.append(TextNode(original_text, TextType.TEXT))
    return result

def text_to_textnodes(text):
    delimited1 = split_nodes_delimiter([TextNode(text, text_type=TextType.TEXT)], "`", TextType.CODE)
    delimited2 = split_nodes_delimiter(delimited1, "_", TextType.ITALIC)
    delimited3 = split_nodes_delimiter(delimited2, "**", TextType.BOLD)
    split_images = split_nodes_image(delimited3)
    split_links = split_nodes_link(split_images)
    return split_links
