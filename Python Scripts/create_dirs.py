import os
import os.path
def folders():
    root = 'CyberSecurity-Notes'
    if os.path.isdir(root):
        pass
    os.mkdir(root)
    for week in range(1, 25):
        os.makedirs('{}/Week{}'.format(root,week))
        for day in range(1, 4):
            os.makedirs('{}/Week {}/Day{}'.format(root,week,day))
folders()
