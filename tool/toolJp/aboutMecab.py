

try:
    from natto import MeCab
except:
    pass

from tool.toolJp import kanaTrans
class SentenceToMecab():
    '''
    :ex
    w = SentenceToMecab("「ねえ、まるで雪みたいだね」と、明里あかりは言った。").start()
    '''
    def __init__(self,text):
        self.text = text
    def start(self):
        '''
        检验是否满足mecab 11个值
        :return:
        '''
        last_mecab = list(self.mecab_yield())
        # if len(x)==11
        filter_mecab = [x for x in last_mecab if len(x)==12]
        return  filter_mecab

    def mecab_yield(self):
        '''
        :return: ["みたい","名詞","非自立","形容動詞語幹","*","*","*","みたい", "ミタイ","ミタイ",""]
        '''
        for cc in list(self.get_kana()):
            if type(cc)==list:
                # if kanaTrans.trans(cc[-2])==cc[0]:
                    # if cc[0][0] in kanaTrans.pianjiaming and cc[0][-1] in kanaTrans.pianjiaming:
                new_mecab = cc+[kanaTrans.trans(cc[-2])]+[kanaTrans.trans(cc[-1])]
                yield new_mecab



    def get_kana(self):
        # with MeCab() as nm:  "-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd"  改默认 vi /usr/local/etc/mecabrc
        # with MeCab("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd") as nm:
        with MeCab() as nm:
            for n in nm.parse(str(self.text), as_nodes=True):
                if not n.is_eos():
                    if n.feature.split(',')[0]!='記号' and n.feature.split(',')[2:]!=['*', '*', '*', '*', '*']:
                        yield [n.surface]+n.feature.split(',')

# text
# 1.
# w = SentenceToMecab("「ねえ、まるで雪みたいだね」と、明里あかりは言った。").start()
# print(w)
# 2.
# l = SentenceToMecab("「ねえ、まるで雪みたいだね」と、明里あかりは言った。").mecab_yield()
# print(list(l))

# 3.
# s = SentenceToMecab("ＡＳＡ感度").start()
# print(s)
# ['ＡＳＡ', '名詞', '固有名詞', '組織', '*', '*', '*', 'ASA', 'エイエスエイ', 'エイエスエイ', 'えいえすえい']
# a[:-3]
