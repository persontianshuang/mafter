from pydub import AudioSegment

from tool import mymongo


input_path = "/Users/user/language/sp/MagicKaito"
nx_data = list(mymongo.pymg('mynihongo1','sentences').find({'sentence_Nx':{'$nin':['not in Nx']}}))[:315]
for index,x in enumerate(nx_data):
    print(index)
    # mp3 = AudioSegment.from_mp3('/Users/user/language/sp/MagicKaito/moshu01.mp3') # 打开mp3文件
    #
    # base_pydub = "mp3[{start}*1000:{end}*1000].export('{out_mp3_path}', format='mp3')"
    # this_pydub = base_pydub.format(
    #     start = x['start_seconds'],
    #     end = x['end_seconds'],
    #     out_mp3_path = input_path+'/split/'+'moshu01_'+str(index)+'.mp3',
    # )
    # exec(this_pydub)
