import tool.toolMusic.songInfo as songInfo
from db.sentences.music import MusicSentences
from doDb.doSentence import word_sentence
from history.music import MusicSubFlow,MusicItem


# user = users.get_user('meng')

class SaveNewMusic():
    def __init__(self,name,flow_url,wy_song_id,song_img,songer,input):
        self.name = name
        self.flow_url = flow_url
        self.wy_song_id = wy_song_id,
        self.song_img = song_img,
        self.songer = songer
        self.input = input


    def start(self):
        msf =  MusicSubFlow()
        msf.name = self.name
        msf.flow_url = self.flow_url
        msf.wy_song_id  = self.wy_song_id
        msf.song_img  = self.song_img
        msf.songer  = self.songer
        msf.save()


        song_lyric = songInfo.SongFuncs(self.input).song_sentences()
        # 没问题
        for each in song_lyric:
            music_sentence = MusicSentences()
            for attr in each.keys():
                exec('music_sentence.{}=each[attr]'.format(str(attr)))

            music_sentence.save()
            word_sentence(music_sentence)

            mi = MusicItem(sentence_jp=each['sentence_jp'],belongsto_sentence=music_sentence)  #出问题了
            # mi = MusicItem(sentence_jp=each['sentence_jp'])
            msf.items.append(mi)
            msf.save()
            # for it in vsf.items:
            #     ss = VideoSentences.objects(id=it.belongsto_sentence.id)[0]
            #     word_sentence(ss)
input_song = 'http://music.163.com/#/song?id=28517520'
si = songInfo.SongFuncs(input_song).song_info()
# si = {'songer': '玉置浩二', 'song_name': '初恋', 'song_img': 'http://p1.music.126.net/2E4jT3lC-9jhbCDkWqdp7A==/3232564186618495.jpg', 'song_id': '29750519', 'mp3': 'http://m10.music.126.net/20170626214235/a18bf9b48dcebdfa5f3dd61ee36a534a/ymusic/f7b0/3bed/ceb6/b32118281358d5202a0fc76d0c2277c5.mp3'}
SaveNewMusic(
    name = si['song_name'],
    flow_url = si['mp3'],
    wy_song_id = si['song_id'],
    song_img = si['song_img'],
    songer = si['songer'],
    input = input_song
).start()
#
# # self,name,flow_url,wy_song_id,song_img
#
#
#
#
print(si['mp3'])
