from copystatic import copy_static
from generatepage import generate_page_recursive
import sys

def main():
    basepath = sys.argv[1]
    if not basepath:
        basepath = "/"
    copy_static("static", "public")
    generate_page_recursive("./content", "template.html", "./docs", basepath)

main()
