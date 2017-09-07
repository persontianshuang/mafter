from mongoengine import *

from db.sentences import video
from history import base


class VideoItem(base.Item):
    '''
    sentence_jp
    Nx
    tags:
    '''
    belongsto_sentence = ReferenceField((video.VideoSentences), required=True,dbref=True)#,dbref=True

class VideoSubFlow(base.SubFlow):
    '''
    name，flow_url，
    tags：【'女性向'，'男性向' 'N1'】# N几的句子最多
    items
    '''
    flow_url = URLField()
    sub_from_url = URLField()
    tags = ListField(StringField(max_length=20))


# s = VideoSubFlow()
# s.items.append(VideoItem('342'))
# s.save()
