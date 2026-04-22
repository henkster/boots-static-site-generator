import re
from textnode import TextNode, TextType

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "_", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_link(text_nodes)
    text_nodes = split_nodes_image(text_nodes)
    return text_nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    result = []
    for old_node in old_nodes:
        if (old_node.text_type != TextType.TEXT):
            result.append(old_node)
            continue
        image_list = extract_markdown_images(old_node.text)
        text = old_node.text
        for image_tuple in image_list:
            texts = text.split(f"![{image_tuple[0]}]({image_tuple[1]})")
            if texts[0] != "":
                result.append(TextNode(texts[0], TextType.TEXT))
            result.append(TextNode(image_tuple[0], TextType.IMAGE, image_tuple[1]))
            text = texts[1]
        if text != "":
            result.append(TextNode(text, TextType.TEXT))
    return result

def split_nodes_link(old_nodes):
    result = []
    for old_node in old_nodes:
        if (old_node.text_type != TextType.TEXT):
            result.append(old_node)
            continue
        link_list = extract_markdown_links(old_node.text)
        text = old_node.text
        for link_tuple in link_list:
            texts = text.split(f"[{link_tuple[0]}]({link_tuple[1]})")
            if texts[0] != "":
                result.append(TextNode(texts[0], TextType.TEXT))
            result.append(TextNode(link_tuple[0], TextType.LINK, link_tuple[1]))
            text = texts[1]
        if text != "":
            result.append(TextNode(text, TextType.TEXT))
    return result

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)