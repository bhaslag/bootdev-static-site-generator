from enum import Enum

BlockType = Enum('BlockType', [
   ("PARAGRAPH", "paragraph"),
   ("HEADING", "heading"),
   ("CODE", "code"),
   ("QUOTE", "quote"),
   ("UL", "ul"),
   ("OL", "ol")
   ])

def markdown_to_blocks(doc):
   strings = []

   for line in doc.split("\n\n"):
      if len(line) == 0:
         continue

      strings.append(line.strip())

   return strings

def block_to_blocktype(block):