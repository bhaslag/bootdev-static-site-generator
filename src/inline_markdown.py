import re

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
          new_nodes.append(node)
          continue
        
        else:
          parts = node.text.split(delimiter)

          if len(parts) % 2 == 0:
            raise Exception("Invalid markdown, unmatched delimiter")

          node_type = text_type

        for i, split_text in enumerate(parts):
          if split_text == "":
            continue

          if i % 2 == 0:
            node_type = TextType.TEXT

          else:
            node_type = text_type

          new_nodes.append(TextNode(split_text, node_type))

    return new_nodes

def split_nodes_link(old_nodes):
  new_nodes = []

  for node in old_nodes:
    current_text = node.text

    for link_text, link_url in extract_markdown_links(node.text):
      sections = current_text.split(f"[{link_text}]({link_url})", 1)
      before = sections[0]
      after = sections[1]

      if (len(before) > 0):
        new_nodes.append(TextNode(before, TextType.TEXT))

      new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

      current_text = after

  return new_nodes

def split_nodes_image(old_nodes):
  new_nodes = []

  for node in old_nodes:
    current_text = node.text

    for img_alt, img_src in extract_markdown_images(node.text):
      sections = current_text.split(f"![{img_alt}]({img_src})", 1)
      before = sections[0]
      after = sections[1]

      if (len(before) > 0):
        new_nodes.append(TextNode(before, TextType.TEXT))

      new_nodes.append(TextNode(img_alt, TextType.IMAGE, img_src))

      current_text = after

  return new_nodes

def extract_markdown_images(text):
  pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(pattern, text)

  return matches

def extract_markdown_links(text):
  pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
  matches = re.findall(pattern, text)

  return matches