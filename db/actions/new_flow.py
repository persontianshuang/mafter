from tool.toolVedio import sub
from db.words.word import Words
from db.sentences.sentence import Sentences
from db.subFlow.flow import Flow
from db.subs import Subs

from db.actions import ws



class Video:
    def create(self,name,mp4_url=''):
        sub_list= Subs.objects(name = name)

        flow_video = Flow.objects(name = name)
        if flow_video:
            new_flow = flow_video[0]
        else:
            new_flow = Flow()
            new_flow.name = name
            new_flow.type = 'video'
            new_flow.mp4_url = mp4_url


            new_flow.num = len(sub_list)
            new_flow.save()
        # if Sentences.objects(flow_name = new_flow.name)
        for x in sub_list:
            sub_sentence = Sentences.objects(belongsto_flow=new_flow,flow_id=x['index'])
            if sub_sentence:
                pass
            else:
                s = Sentences()
                s.belongsto_flow = new_flow
                s.flow_id = x['index']
                s.flow_name = new_flow.name
                s.jp = x['jp']
                s.cn = x['cn']
                # s.cn = '当前没有字幕哦，锻炼自己的翻译能力吧'
                s.start_seconds = x['start_seconds']
                s.end_seconds = x['end_seconds']
                s.save()
                ws.word_sentence(s)
    def delete(self,name):
        delete_flow = Flow.objects(name=name)
#         删除flow,sentence,word sentence -1  事务保持一致性   drop
# Video().create('半泽直树1','http://oqyvocafw.bkt.clouddn.com/longvacation/1.mp4')
# 鲁邦三世VS柯南  路人女主第二季03 徒然喜欢你03  longvacation1 言叶之庭
# for x in Sentences.objects(flow_name = '半泽直树1'):
#
#     bs = 'http://oum9zyri9.bkt.clouddn.com/hanza/1/{}.mp4'
#
#     x.split_mp4_url = bs.format(str(x.flow_id))
#     x.save()
# 图片
# for x in Flow.objects(name = '半泽直树1'):
#     x.img = 'http://op5p4i8dh.bkt.clouddn.com/hanza/hanza.jpg'
#     x.save()

# new_flow.name = '路人女主第二季03'
# new_flow.type = 'video'
# new_flow.mp4_url = 'http://oqyvocafw.bkt.clouddn.com/3.mp4'
#
#
# new_flow.save()
# d = sub.DoubleSub('/Users/user/language/sp/lr/3.srt').srt()
# create
# delete
# update


# def create(self,dict):
#     new_flow = Flow()
#     new_flow.name = '路人女主第二季03'
#     new_flow.type = 'video'
#     new_flow.mp4_url = 'http://oqyvocafw.bkt.clouddn.com/3.mp4'
#
#
#     new_flow.save()
#     d = sub.Sub('/Users/user/language/sp/lr/3.srt').double_srt()
#
#     sub_list = list(d)
#     print(sub_list)
#     for x in sub_list:
#         s = Sentences()
#         s.belongsto_flow = new_flow
#         s.jp = x['jp']
#         s.cn = x['cn']
#         s.start_seconds = x['start_seconds']
#         s.end_seconds = x['end_seconds']
#         s.save()
#         ws.word_sentence(s)
