import os
import shutil

def remove_file_in_dir(targetDir):
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,file)
        if os.path.isfile(targetFile):
            os.remove(targetFile)

def copy_file_in_dir(sourse_dir,target_dir):
    for file in os.listdir(target_dir):
        target_file = os.path.join(target_dir,file)
        sourse_file = os.path.join(sourse_dir,file)
        if os.path.isfile(target_file):
            shutil.copy(target_file,sourse_file)

def remove_py():
    remove_file_in_dir('/Users/user/pynew/project/chjia/r1/static/static/css')
    remove_file_in_dir('/Users/user/pynew/project/chjia/r1/static/static/js')
    remove_file_in_dir('/Users/user/pynew/project/chjia/r1/templates')

def copy_vue():
    copy_file_in_dir('/Users/user/pynew/project/chjia/r1/static/static/css','/Users/user/pynew/web/nihongo/dist/static/css')
    copy_file_in_dir('/Users/user/pynew/project/chjia/r1/static/static/js','/Users/user/pynew/web/nihongo/dist/static/js')
    shutil.copy('/Users/user/pynew/web/nihongo/dist/index.html','/Users/user/pynew/project/chjia/r1/templates/index.html')
remove_py()
copy_vue()
