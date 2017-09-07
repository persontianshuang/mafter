from datetime import datetime

from mongoengine import *

from db.config import _MongoengineConnect

connect(_MongoengineConnect)

class Subs(Document):
    # 中日cn_jp  日本jp  中国cn
    type = StringField()

    name = StringField()
    jp = StringField(default='')
    cn = StringField(default='')

    start_seconds = StringField()
    end_seconds = StringField()

    split_mp3_url = StringField(default='')
    split_mp4_url = StringField(default='')
    index = IntField()

from tool.toolVedio.sub import Sub

def cn(name,path):
    s_srt = Sub(path).single_srt()
    for index,x in enumerate(s_srt):
        new_video = Subs()

        new_video.cn = x['sentence']
        new_video.name = name
        new_video.index = index
        new_video.start_seconds = x['start_seconds']
        new_video.end_seconds = x['end_seconds']
        new_video.save()

def jp(name,path):
    s_srt = Sub(path).single_srt()
    for index,x in enumerate(s_srt):
        new_video = Subs()

        new_video.jp = x['sentence']
        new_video.name = name
        new_video.index = index
        new_video.start_seconds = x['start_seconds']
        new_video.end_seconds = x['end_seconds']
        new_video.save()

# jp('longvacation1','/Users/user/language/sp/longvacation/sub/01.srt')
# cn('半泽直树01','/Users/user/language/sp/半泽直树/hanza/1c.srt')

# for x in range(1,11):
#     cn('半泽直树'+str(x),'/Users/user/language/sp/半泽直树/hanza/{}c.srt'.format(str(x)))

def jp_cn(name,path):
    s_srt = Sub(path).double_srt()
    for index,x in enumerate(s_srt):
        new_video = Subs()

        new_video.jp = x['jp']
        new_video.cn = x['cn']
        new_video.name = name
        new_video.index = index
        new_video.start_seconds = x['start_seconds']
        new_video.end_seconds = x['end_seconds']
        new_video.save()

# jp_cn('言叶之庭','/Users/user/language/sp/动漫/言叶之庭/kodoba.srt')

# for x in range(1,9):
#     jp_cn('空之境界'+str(x),'/Users/user/language/sp/kong/ass/{}.srt'.format(str(x)))
