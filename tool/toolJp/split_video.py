import os
import time

from tool import mymongo



def split_video(time,input_mp4_path,out_path):
    if float(time[0])<2:
        a = -0.2
        b = 5.3
    else:
        a = -2.2
        b = 4.2
    base_ffmpeg_split = "ffmpeg  -i {input_path} -vcodec copy -acodec copy -ss {start} -to {end} {out_path} -y"
    this_ffmpeg = base_ffmpeg_split.format(
        input_path = input_mp4_path,
        start = float(time[0])+a,
        end = float(time[1])+b,
        out_path = out_path,
    )
    os.system(this_ffmpeg)
input_path = '/Users/user/language/sp/动漫/言叶之庭/kodoba.mp4'
for x in mymongo.pymg('mynihongo2','subs').find({'name':'言叶之庭'}):
    times = [x['start_seconds'],x['end_seconds']]
    split_video(times,input_path,'/Users/user/language/sp/动漫/言叶之庭/mp4_split/{}.mp4'.format(str(x['index'])))





# input_path = "/Users/user/language/sp/MagicKaito"
# nx_data = list(mymongo.pymg('mynihongo1','sentences').find({'sentence_Nx':{'$nin':['not in Nx']}}))[:31]
# for index,x in enumerate(nx_data):
#     print(index)
#     print(x['_id'])
#     base_ffmpeg_split = "ffmpeg  -i {input_path} -vcodec copy -acodec copy -ss {start} -to {end} {out_path} -y"
#     this_ffmpeg = base_ffmpeg_split.format(
#         input_path = input_path+'/moshu01.mp4',
#         start = float(x['start_seconds'])-2,
#         end = float(x['end_seconds'])+3,
#         out_path = input_path+'/split_mp4/'+'moshu01_'+str(index)+'.mp4',
#     )
#
#     os.system(this_ffmpeg)




# os.system()
