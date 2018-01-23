# -*- coding: UTF-8 -*-
import time
import os
import sys
import svnconfig

def svn_export():
    current_path=os.getcwd()
    dist=svnconfig.setting['dist']
    svn_path=svnconfig.setting['svn']
    os.chdir(svn_path)
    sys.path.append(svn_path)
    rmtree(dist)
    # svnconfig.setting['dist']=dist+time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime())
    cmd='python svn_cmd.py export %(url)s %(dist)s '%svnconfig.setting
    print "execute: %s"%cmd
    code=os.system(cmd)
    os.chdir(current_path)
    # print ">>>>", current_path
    return code


def rmtree(file_path):
    # print file_path
    for root, dirs, files in os.walk(file_path, topdown=False):
        # print root, dirs, files
        for name in files:
            os.remove(os.path.join(root, name))
            # print ">>> os.remove: ", os.path.join(root, name)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
            # print "### os.rmdir: ",os.path.join(root, name)
    pass

if __name__ == "__main__":
    print u"kaishi"
    rmtree("e:\\myspace\space_fsrc\\UI_AUTO\\RC_selenium\\links_selenium\\file\\cases")
