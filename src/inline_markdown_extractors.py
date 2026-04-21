import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

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