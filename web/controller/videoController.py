import bson

from db.sentences.video import VideoSentences
from history.video import VideoSubFlow
from tool import mymongo


def video_list():
    # print(VideoSubFlow.objects.all())
    def get_data(item):
        data = {
            'name': item.name,
            'id': str(item.id)
        }
        return data
    v_list = [get_data(x) for x in VideoSubFlow.objects.all()]
    return v_list

# vl = video_list()
# print(vl)

# video_single_info

def video_url(video_id):
    if video_id != 'undefined':
        video_id= bson.objectid.ObjectId(video_id)
        vsf = VideoSubFlow.objects(id = video_id)[0]
        return vsf.flow_url



def video_detail(video_id):
    if video_id != 'undefined':
        print(video_id.split('/'))
        video_id= bson.objectid.ObjectId(video_id)
        vsf = VideoSubFlow.objects(id = video_id)[0]
        # vsf = VideoSubFlow.objects.all()[1]
        def get_data(item):
            # sentence = VideoSentences.objects(id=item.belongsto_sentence.id)[0]

            sentence = VideoSentences.objects(id=item.belongsto_sentence.id)[0]
            if  sentence.sentence_Nx=='N3':
                # print(sentence.sentence_Nx)
                data = {
                    'sentence_jp': sentence.sentence_jp,
                    'sentence_cn': sentence.sentence_cn,
                    'words_list': [{'mecab':y['word_mecab'],'id':str(y['word_id']),'word_belongsto_n':y['word_Nx']} for y in sentence.words_list],
                    'start': sentence.start_seconds,
                    'end': str(float(sentence.end_seconds)+1.1),

                }
                return data
            else:
                return ''
        v_detail = [get_data(x) for x in vsf.items if get_data(x)!='']
        print(len(v_detail))
        return v_detail

v_d = video_detail('5951323ad9f0920c4e6aa800')
print(v_d)



def word_dtails(bson_id):
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

def add_video():
    pass
