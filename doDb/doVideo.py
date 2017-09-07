from db.sentences.video import VideoSentences
from doDb.doSentence import word_sentence
from history.video import VideoSubFlow,VideoItem
from tool.toolVedio import sub


# user = users.get_user('meng')
# 获取参数的变量名
def exec_dict_to_db(dict,db):
    for attr in dict.keys():
        exec('db.{}=dict[attr]'.format(str(attr)))
class SaveNewVideo():
    def __init__(self,name,flow_url,srt_path,sub_from_url):
        self.name = name
        self.flow_url = flow_url
        self.srt_path = srt_path
        self.sub_from_url = sub_from_url
    def start(self):
        vsf = VideoSubFlow()
        vsf.name = self.name
        vsf.flow_url = self.flow_url
        vsf.sub_from_url = self.sub_from_url
        vsf.save()

        srt = list(sub.DoubleSub(self.srt_path).srt())

        for each in srt[:30]:
            video_sentence = VideoSentences()
            for attr in each.keys():
                exec('video_sentence.{}=each[attr]'.format(str(attr)))
            video_sentence.save()
            word_sentence(video_sentence)

            vi = VideoItem(sentence_jp=each['sentence_jp'],belongsto_sentence=video_sentence)
            vsf.items.append(vi)
            vsf.save()
        # for it in vsf.items:
        #     ss = VideoSentences.objects(id=it.belongsto_sentence.id)[0]
        #     word_sentence(ss)


SaveNewVideo(
    name='路人女主第二季03',
    srt_path='/Users/user/language/sp/lr/3.srt',
    flow_url='http://oqyvocafw.bkt.clouddn.com/3.mp4',
    sub_from_url = 'https://sub.kamigami.org/78495.html'

).start()

# SaveNewVideo(
#     name='魔术快斗01',
#     srt_path='/Users/user/language/sp/MagicKaito/moshu01.srt',
#     flow_url='http://oqyvocafw.bkt.clouddn.com/moshu01.mp4',
#     sub_from_url = 'https://sub.kamigami.org/3308.html'
# ).start()

# 由于银魂是 .sub .idx 的字幕文件 难以转化为.srt 故放弃  name='银魂255',


# vsf = VideoSubFlow.objects.all()[1]
# print(vsf.items)
# import bson
# def video_detail(video_id):
#     if video_id != 'undefined':
#         print(video_id)
#         video_id= bson.objectid.ObjectId(video_id)
#         vsf = VideoSubFlow.objects(id = video_id)[0]
#         # vsf = VideoSubFlow.objects.all()[1]
#         def get_data(item):
#             sentence = VideoSentences.objects(id=item.belongsto_sentence.id)[0]
#             # data = {
#             #     'sentence_jp': sentence.sentence_jp,
#             #     'sentence_cn': sentence.sentence_cn,
#             #     'words_list': [{'mecab':y['word_mecab'],'id':str(y['word_id']),'word_belongsto_n':y['word_Nx']} for y in sentence.words_list],
#             #     'start': sentence.start_seconds,
#             #     'end': sentence.end_seconds
#             # }
#             data = [word['word_Nx'] for word in sentence.words_list if word['word_Nx'][0]=='N']
#             return data
#         v_detail = [get_data(x) for x in vsf.items]
#         return v_detail
# v_d = video_detail('595135ddd9f0920de73739ac')
# print(v_d)


