import bson

from db.sentences.music import MusicSentences
from history.music import MusicSubFlow
from tool import mymongo


def music_list():
    # print(musicSubFlow.objects.all())
    def get_data(item):
        data = {
            'name': item.name,
            'id': str(item.id)
        }
        return data
    v_list = [get_data(x) for x in MusicSubFlow.objects.all()]
    return v_list

# vl = music_list()
# print(vl)

# music_single_info

def music_url(music_id):
    if music_id != 'undefined':
        music_id= bson.objectid.ObjectId(music_id)
        vsf = MusicSubFlow.objects(id = music_id)[0]
        return vsf.flow_url



def music_detail(music_id):
    if music_id != 'undefined':
        music_id= bson.objectid.ObjectId(music_id)
        vsf = MusicSubFlow.objects(id = music_id)[0]
        # vsf = musicSubFlow.objects.all()[1]
        def get_data(item):
            sentence = MusicSentences.objects(id=item.belongsto_sentence.id)[0]
            data = {
                'sentence_jp': sentence.sentence_jp,
                'sentence_cn': sentence.sentence_cn,
                'words_list': [{'mecab':y['word_mecab'],'id':str(y['word_id']),'word_belongsto_n':y['word_Nx']} for y in sentence.words_list],
                'start': sentence.start_seconds,
                'end': sentence.end_seconds
            }
            return data
        v_detail = [get_data(x) for x in vsf.items]
        return v_detail

# v_d = music_detail('594e47b1d9f0920d10dfdf7e')
# print(v_d)



def word_dtails(bson_id):
    if bson_id != 'undefined':
        bson_id= bson.objectid.ObjectId(bson_id)
        db_words = mymongo.pymg('mynihongo1','words')
        searched_word = db_words.find_one({'_id':bson_id})
        data = {
            'tags': '/'.join(searched_word['tags']),
            'meaning': searched_word['meaning'],
            'Nx': searched_word['Nx'],
            'raw_word': searched_word['mecab'][7],
            'this_word': searched_word['mecab'][0],
            'speak': searched_word['mecab'][-2],
        }
        return data

def search_word(bson_id):
    bson_id= bson.objectid.ObjectId(bson_id)
    db_words = mymongo.pymg('mynihongo1','words')
    searched_word = db_words.find_one({'_id':bson_id})
    data = {
        'tags': '/'.join(searched_word['tags']),
        'meaning': searched_word['meaning'],
        'Nx': searched_word['Nx'],
        'raw_word': searched_word['mecab'][7],
        'this_word': searched_word['mecab'][0],
        'speak': searched_word['mecab'][-2],
    }
    return data

# sw = search_word('594b9b3bd9f0920586858f27')
# print(sw)

def add_music():
    pass
