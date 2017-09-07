from pydub import AudioSegment

import os, re

# 打开mp3文件
mp3 = AudioSegment.from_mp3('/Users/user/language/sp/turan/3.mp3')

# 切割前17.5秒并覆盖保存


from tool import mymongo
input_path = '/Users/user/language/sp/turan/3.mp3'
for x in mymongo.pymg('mynihongo2','subs').find({'name':'徒然喜欢你03'}):
    mp3_path = '/Users/user/language/sp/turan/mp3_split3/{}.mp3'.format(str(x['index']))

    mp3[float(x['start_seconds'])*1000:float(x['end_seconds'])*1000].export(mp3_path, format="mp3")


