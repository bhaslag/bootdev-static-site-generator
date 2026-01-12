import os
import shutil
import sys

from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    if len(sys.argv) > 0:
        base_path = sys.argv[0]
    else:
        base_path = "/"
    generate_pages_recursive("content", "./template.html", dir_path_public, base_path)

main()
