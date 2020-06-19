import os
import os.path
import shutil

def pptx_copy():
    path = "~/Downloads"
    path = os.path.expanduser(path)
    for file in os.listdir(path):
        if file.endswith(".ppt") or file.endswith(".pptx"):
            dst = os.getcwd()
            filepath = os.path.join(path, file)
            shutil.copy2(filepath,dst)
pptx_copy()
