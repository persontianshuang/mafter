import requests
import json
import re
from bs4 import BeautifulSoup


class SongFuncs():
    def __init__(self,wy_song_url):
        self.song_id = wy_song_url.split('=')[1].strip()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.138 Safari/537.36',
            'Cookie': 'appver=1.5.0.75771',
            'Referer': 'http://music.163.com/'
        }
        self.mp3_url = ''
        self.song_dtails = {}
        self.all_lyric = {}
        self.jp = ''
        self.cn = ''

    def song_info(self):
        '''
        为了 class ComeFromSong(ComeFrom)
        :return:
        '''
        self.get_mp3_url()
        me = self.get_song_dtails()
        song_info_data ={
            #mp3 只有很短的有效时间，还需要下载到本地，上传到七牛云
            'mp3': self.mp3_url,
            'song_name': me['songs'][0]['name'],
            'song_id': self.song_id,
            'song_img': me['songs'][0]['album']['blurPicUrl'],
            'songer': me['songs'][0]['artists'][0]['name'],
        }
        return song_info_data

    def song_sentences(self):
        '''
        为了 class SongSentences(Sentences)
        :return:
        '''
        self.lyric_cn_jp()
        song_sentences_data = []
        for jp in self.jp:
            for cn in self.cn:
                if jp[0]==cn[0]:
                    song_sentence = ''
                    try:
                        r = re.split(r'[:.]',jp[0][1:])
                        print(r)
                        mini_seconds = float('0.'+r[2])
                        song_time = int(r[0])*60+int(r[1])+mini_seconds
                        single_data = {
                            'split_mp3': self.mp3_url,
                            'sentence_jp': jp[1],
                            'sentence_cn': cn[1],
                            'raw_song_time': jp[0][1:],
                            'start_song_time': str(round(song_time, 2)),
                        }
                        song_sentences_data.append(single_data)
                    except:
                        print('no')

        def trans_song_info(song):
            for index ,x in enumerate(song):
                if index+1 < len(song):
                    data = {
                        'sentence_cn': x['sentence_cn'],
                        'sentence_jp': x['sentence_jp'],
                        'start_raw': x['raw_song_time'],
                        'end_raw': song[index+1]['raw_song_time'],
                        'start_seconds': x['start_song_time'],
                        'end_seconds': song[index+1]['start_song_time'],
                    }
                    yield data

        return list(trans_song_info(song_sentences_data))



        # mp3 url
    def get_mp3_url(self):
        mp3_url = 'http://music.163.com/api/song/enhance/download/url?br=320000&id={}'
        mp3_url = mp3_url.format(self.song_id)
        self.mp3_url = requests.get(mp3_url,headers=self.headers).json()['data']['url']
        return self.mp3_url

        # song dtails
    def get_song_dtails(self):
        dtails_url = 'http://music.163.com/api/song/detail/?id=28377211&ids=[{}]'
        url = dtails_url.format(self.song_id)
        self.song_dtails = requests.get(url,headers=self.headers).json()
        return self.song_dtails

    # song 歌词
    def get_song_lyric(self):
        song_lyric = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'
        lyric_url = song_lyric.format(self.song_id)
        self.all_lyric = requests.get(lyric_url,headers=self.headers).json()
        return  self.all_lyric

    #     每一句的 中文 和 日语歌词
    def lyric_cn_jp(self):
        self.get_song_lyric()
        self.cn = [x.split(']') for x in self.all_lyric['tlyric']['lyric'].split('\n') if x !='']
        self.jp = [x.split(']') for x in self.all_lyric['lrc']['lyric'].split('\n') if x !='']
        return self.cn,self.jp


# s = SongFuncs('http://music.163.com/=29750519').song_sentences()
# s = SongFuncs('http://music.163.com/#/song?id=31649312').song_info()
# print(s)

