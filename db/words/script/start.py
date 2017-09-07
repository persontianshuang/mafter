from tool import mymongo
from db.words.base import Words
# 1.   words_backup_01
for each in mymongo.pymg('mynihongo1','raw_sgk').find({'can_mecab': 1}):
    w = Words()
    w.raw = each['raw']

    w.hiragana = each['hiragana']

    w.mecab = each['mecab']
    w.tags = [x for x in each['mecab'][1:-4] if x!='*']

    w.meaning = each['meaning']
    try:
        w.Nx = each['Nx']
    except:
        try:
            w.Nx = 'S'+str(each['import'])
        except:
            w.Nx = 'S0'

    w.save()
