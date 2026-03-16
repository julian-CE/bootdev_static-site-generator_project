from copystatic import copy_static
from generatepage import generate_page_recursive

def main():
    copy_static("static", "public")
    generate_page_recursive("./content", "template.html", "./public")

main()
