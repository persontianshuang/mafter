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
    base = '/Users/user/cs_program/chuja/mafter'
    remove_file_in_dir(base + '/static/static/css')
    remove_file_in_dir(base + '/static/static/js')
    remove_file_in_dir(base + '/templates')

def copy_vue():
    band = '/Users/user/cs_program/chuja/mafter'
    front = '/Users/user/cs_program/chuja/mfront'
    copy_file_in_dir(band+'/static/static/css',front+'/dist/static/css')
    copy_file_in_dir(band+'/static/static/js',front+'/dist/static/js')
    shutil.copy(front+'/dist/index.html',band+'/templates/index.html')
remove_py()
copy_vue()
