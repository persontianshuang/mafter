import re

import pysrt


#'/Users/user/Desktop/ds/subtitle.srt'
class Sub:
    def __init__(self,srt_path):
        self.srt_path = srt_path

    def single_srt(self):
        sub_list = self.first()
        single_srts = []
        for x in sub_list:
            data = {
                'sentence': x['sentence'],
                'start_seconds': self.trans_to_seconds(x['start_time'],x['end_time'])[0],
                'end_seconds': self.trans_to_seconds(x['start_time'],x['end_time'])[1],
            }
            single_srts.append(data)
        return single_srts


    def double_srt(self):
        sub_list = self.first()
        double_srts = []
        for s in range(len(sub_list)-1):
            if sub_list[s]['start_time'] ==sub_list[s + 1]['start_time'] and sub_list[s]['end_time'] ==sub_list[s + 1]['end_time']:
                data = {
                    'jp': sub_list[s]['sentence'],
                    'cn': sub_list[s+1]['sentence'],
                    'start_seconds': self.trans_to_seconds(sub_list[s]['start_time'],sub_list[s]['end_time'])[0],
                    'end_seconds': self.trans_to_seconds(sub_list[s]['start_time'],sub_list[s]['end_time'])[1],
                }
                double_srts.append(data)
        return double_srts

    def first(self):
        # subs = pysrt.open(self.srt_path,encoding='utf_8')
        subs = pysrt.open(self.srt_path)
        def pretreatment(raw_text):
            sub1 = re.sub(r'[\ufeff\u3000]',' ',raw_text)
            sub2 = re.sub(r'({.+\d})','',sub1)
            def html_tag(sub_tag):
                after_text = re.compile(r'>(.+)</').findall(sub_tag)[0]
                return after_text
            # while
            after_text=sub2
            try:
                # if 还有标签 继续去掉
                while after_text!=html_tag(after_text):
                    after_text = html_tag(after_text)
            except:
                pass

            return after_text

        def sub_yield(pysrt_subs):
            for x in pysrt_subs:
                e_sub = {
                    'sentence': pretreatment(x.text),
                    'start_time': x.start,
                    'end_time': x.end
                    # 'start_time': time_to_seconds(x.start)-1,
                    # 'end_time': time_to_seconds(x.end)+1
                }
                yield e_sub
        return list(sub_yield(subs))

    def time_to_seconds(self,time):
        # 00:22:42,960
        rp = re.split(r'[:,]',str(time))
        # hours = int(time.hours)
        # minutes = int(time.minutes)
        # seconds = int(time.seconds)

        hours = int(rp[0])
        minutes = int(rp[1])
        seconds = int(rp[2])
        mini_seconds = float('0.'+rp[3])
        seconds_time = hours*60*60 + minutes*60 + seconds + mini_seconds

        seconds_time = str(round(seconds_time, 2))
        return seconds_time

    def trans_to_seconds(self,start,end):
        # def var_to_dict(*args):

        start_seconds = self.time_to_seconds(start)
        end_seconds = self.time_to_seconds(end)
        # var_to_dict(start_seconds,end_seconds)
        return (start_seconds,end_seconds)

# d = Sub('/Users/user/language/sp/半泽直树/1/1c.srt').single_srt()
# print(d)
# from db.subs import Subs
#
# for x in Subs.objects(name="半泽直树1"):
#     for y in d:
#         if x.start_seconds==y['start_seconds'] and x.end_seconds==y['end_seconds']:
#             x.jp = y['sentence']
#             x.save()



