from copystatic import copy_static
from generatepage import generate_page_recursive
import sys

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    copy_static("static", "docs")
    generate_page_recursive("./content", "template.html", "./docs", basepath)

main()
