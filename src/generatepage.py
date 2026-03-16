from markdowntoblocks import markdown_to_html_node
import os

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:

        if line.startswith("# "):
            line = line.strip("#")
            return line.strip()
    raise Exception("error: no h1 header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    dest_dir = os.path.dirname(dest_path)
    os.makedirs(dest_dir, exist_ok=True)
    with open(from_path, "r") as file:
        file_content = file.read()
    with open(template_path, "r") as template:
        template_content = template.read()
    html = markdown_to_html_node(file_content).to_html()
    title = extract_title(file_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html)
    template_content = template_content.replace("href=\"/", f"href=\"{basepath}")
    template_content = template_content.replace("src=\"/", f"src=\"{basepath}")
    with open(dest_path, "w") as destination:
        destination.write(template_content)

def generate_page_recursive(src, template_path, dest, basepath):
    entries = os.listdir(src)
    for entry in entries:
        if os.path.isfile(os.path.join(src, entry)):
            dest_file = os.path.join(dest, entry.replace(".md", ".html"))
            generate_page(os.path.join(src, entry), template_path, dest_file, basepath)
        else:
            generate_page_recursive(os.path.join(src, entry), template_path, os.path.join(dest, entry), basepath)
