import os

def dirlist(path):
    filelist =  os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath)
        else:
            if filepath[-3:]=='mp4':
                print(filepath)

dirlist('/Volumes/My Passport')

