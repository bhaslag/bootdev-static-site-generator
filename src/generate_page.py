import os

from markdown_blocks import markdown_to_html_node

def extract_markdown_h1(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("No h1 found")

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.isfile(from_path):
        raise FileNotFoundError(f"Source file not found: {from_path}")

    if not os.path.isfile(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    # Read markdown source
    with open(from_path, "r", encoding="utf-8") as f:
        markdown_file_content = f.read()

    page_content = markdown_to_html_node(markdown_file_content).to_html()
    page_title = extract_markdown_h1(markdown_file_content)

    # Read template
    with open(template_path, "r", encoding="utf-8") as f:
        template_file_content = f.read()

    # Replace placeholders
    final_html = (
        template_file_content
        .replace("{{ Title }}", page_title)
        .replace("{{ Content }}", page_content)
        .replace('href="/', f'href="{base_path}"')
        .replace('src="/', f'src="{base_path}"')
    )

    # Write output
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    os.makedirs(dest_dir_path, exist_ok=True)

    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)

        #recurse
        if os.path.isdir(src_path):
            generate_pages_recursive(src_path, template_path, dest_path, base_path)

        elif os.path.isfile(src_path) and entry.endswith(".md"):
            dest_path = os.path.splitext(dest_path)[0] + ".html"
            generate_page(src_path, template_path, dest_path, base_path)