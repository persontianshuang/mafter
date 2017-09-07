from mongoengine import *

from db.sentences import music
from history import base


class MusicItem(base.Item):
    '''
    sentence_jp
    Nx
    tags:
    '''
    belongsto_sentence = ReferenceField((music.MusicSentences), required=True,dbref=True)#,dbref=True

class MusicSubFlow(base.SubFlow):
    '''
    name，flow_url，
    tags：【'女性向'，'男性向' 'N1'】# N几的句子最多
    items
    '''
    flow_url = URLField()
    wy_song_id = StringField(),
    song_img = URLField(),
    songer = StringField(),

    tags = ListField(StringField(max_length=20))






# s = VideoSubFlow()
# s.items.append(VideoItem('342'))
# s.save()
