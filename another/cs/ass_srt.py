import os

path = '/Users/user/language/sp/kong/ass'
for x in os.listdir(path):
    base = 'ffmpeg -i {input} {out}'
    if 'ass' in x:
        input_path = os.path.join(path,x)
        out_path = os.path.join(path,x.replace('ass','srt'))
        os.system(base.format(input=input_path,out=out_path))

#
