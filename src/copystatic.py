import os
import shutil

def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)
    copy_recursive(src, dst)

def copy_recursive(src, dst):
    entries = os.listdir(src)
    for entry in entries:
        source_path = os.path.join(src, entry)
        dest_path = os.path.join(dst, entry)
        print(f"source path: {source_path}")
        print(f"dest_path: {dest_path}")
        if os.path.isdir(source_path):
            os.mkdir(dest_path)
            copy_recursive(source_path, dest_path)
        else:
            shutil.copy(source_path, dest_path)

