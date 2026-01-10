def extract_markdown_h1(markdown):
    blocks = markdown.split("\n\n")
    title = ""

    for block in blocks:
        if block.startwith("#"):
           lines = block.split("\n")
           title = lines[0]
           title = title.replace("# ", "")
           title = title.strip()

    if len(title) == 0:
       raise Exception("No h1 found")

    return title