import os
import os.path
import shutil

def stu_activities():
    path = os.path.expanduser(r'~/Downloads')
    file = os.listdir(path)
    for filename in file:
        if "readme" in filename:
            src = path+'/'+filename
            dst = os.getcwd()
            filepath = os.path.join(src, filename)
            shutil.copy2(src,dst)

stu_activities()
