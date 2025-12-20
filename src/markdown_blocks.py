
def markdown_to_blocks(doc):
   strings = []

   for line in doc.split("\n\n"):
      if len(line) == 0:
         continue

      strings.append(line.strip())

   return strings