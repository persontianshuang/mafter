import requests
import hashlib
import urllib.request, urllib.parse, urllib.error
import random, re

def bd_tanslate(q):
    appid = '20170225000039881'
    secretKey = 'gq6lGI97dipZyAZa357_'
    myurl = '/api/trans/vip/translate'
    fromLang = 'auto'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = sign.encode('utf')
    m1 = hashlib.md5(sign)
    sign = m1.hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    url = 'http://'+'api.fanyi.baidu.com'+myurl
    # print(url)
    wb_data = requests.get(url)
    aa = wb_data.json()
    return aa['trans_result'][0]['dst']
# q = '駅まで一緒に行かない？'
# print(bd_tanslate(q))


